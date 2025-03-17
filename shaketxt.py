#!/usr/bin/env python3
"""
generate_text.py

This script loads a trained character-level RNN model (from checkpoints and saved mappings)
and uses it to generate text based on user-provided prompts. A simple GUI is implemented using
pygame which allows you to input:
    - A prompt text.
    - A temperature value (controls randomness in generation).
    - A desired generation length.
Upon clicking the "Generate" button, the script generates text from the prompt and displays it.
Ensure that you have already trained a model (using train_rnn.py) and that the checkpoint files and
mapping files (char2idx.npy and idx2char.npy) are available in the checkpoint directory.

Requirements:
- Python 3.10
- TensorFlow 2.19.0
- Pygame
- Numpy
"""

import tensorflow as tf
import numpy as np
import os
import pygame
import argparse

# Initialize pygame font module
pygame.init()
pygame.font.init()
FONT = pygame.font.Font(None, 32)


# --- InputBox class for text input in pygame ---
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        # Define the rectangle area for the input box.
        self.rect = pygame.Rect(x, y, w, h)
        # Colors for active and inactive states.
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.text = text
        # Render the initial text.
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        """
        Handles mouse and keyboard events.
        Activates the box on click and updates the text when keys are pressed.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle active state if the input box is clicked.
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            # Update the color based on active state.
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    # Optionally, you can handle 'Enter' events here.
                    pass
                elif event.key == pygame.K_BACKSPACE:
                    # Remove the last character.
                    self.text = self.text[:-1]
                else:
                    # Add the pressed key character.
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        """
        Optionally update the width of the input box if the text is too long.
        """
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        """
        Draw the text and the rectangle on the given screen.
        """
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)


# --- Button class for clickable buttons in pygame ---
class Button:
    def __init__(self, x, y, w, h, text):
        # Define the rectangle area for the button.
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color('grey')
        self.text = text
        # Render the button text.
        self.txt_surface = FONT.render(text, True, pygame.Color('white'))

    def draw(self, screen):
        """
        Draw the button (rectangle and centered text) on the screen.
        """
        pygame.draw.rect(screen, self.color, self.rect)
        text_x = self.rect.x + (self.rect.w - self.txt_surface.get_width()) // 2
        text_y = self.rect.y + (self.rect.h - self.txt_surface.get_height()) // 2
        screen.blit(self.txt_surface, (text_x, text_y))

    def is_clicked(self, event):
        """
        Check if the button is clicked based on a mouse event.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False


def wrap_text(text, font, max_width):
    """
    Helper function to wrap text into multiple lines so that each line does not exceed max_width.
    Splits text by spaces.
    """
    words = text.split(' ')
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "
    lines.append(current_line)
    return lines


def generate_text(model, start_string, generation_length, temperature, char2idx, idx2char):
    """
    Generates text using the trained model.

    Parameters:
        model: The trained tf.keras model for text generation.
        start_string: The initial text prompt as a string.
        generation_length: Number of characters to generate.
        temperature: Sampling temperature (higher = more random).
        char2idx: Dictionary mapping characters to indices.
        idx2char: Numpy array mapping indices to characters.

    Returns:
        A string containing the generated text.
    """
    # Convert the start string to numbers (vectorizing).
    input_eval = [char2idx.get(s, 0) for s in start_string]
    input_eval = tf.expand_dims(input_eval, 0)

    text_generated = []
    # Reset the model states for each stateful layer
    for layer in model.layers:
        if hasattr(layer, 'reset_states'):
            layer.reset_states()
    for i in range(generation_length):
        # Get predictions from the model.
        predictions = model(input_eval)
        predictions = tf.squeeze(predictions, 0)  # Remove the batch dimension. Shape: (T, vocab_size)

        # Adjust the predictions by the temperature.
        predictions = predictions / temperature
        # Use the predictions from the last time step.
        last_prediction = predictions[-1]  # Shape: (vocab_size,)
        # Sample from the distribution using categorical sampling.
        predicted_id = tf.random.categorical(tf.expand_dims(last_prediction, 0), num_samples=1)[0, 0].numpy()

        # Use the predicted id as the next input to the model.
        input_eval = tf.expand_dims([predicted_id], 0)
        text_generated.append(idx2char[predicted_id])

    return start_string + ''.join(text_generated)


def main():
    # Parse command-line arguments for model parameters and file paths.
    parser = argparse.ArgumentParser(description="Generate text using a trained character-level RNN model.")
    parser.add_argument('--checkpoint_dir', type=str, default='./checkpoints',
                        help="Directory containing model checkpoints and mapping files.")
    parser.add_argument('--embedding_dim', type=int, default=128,
                        help="Dimension of the embedding layer (must match training).")
    parser.add_argument('--rnn_units', type=int, default=256,
                        help="Number of units in the RNN cell (must match training).")
    parser.add_argument('--num_layers', type=int, default=1,
                        help="Number of RNN layers (must match training).")
    parser.add_argument('--generation_length', type=int, default=200,
                        help="Default number of characters to generate.")
    parser.add_argument('--temperature', type=float, default=1.0,
                        help="Default sampling temperature.")
    parser.add_argument('--batch_size', type=int, default=1,
                        help="Batch size for the model.")
    args = parser.parse_args()

    # Load the saved mapping dictionaries (char2idx and idx2char).
    char2idx_path = os.path.join(args.checkpoint_dir, "char2idx.npy")
    idx2char_path = os.path.join(args.checkpoint_dir, "idx2char.npy")
    if not os.path.exists(char2idx_path) or not os.path.exists(idx2char_path):
        print("Mapping files not found in checkpoint directory. Please run train_rnn.py first.")
        return
    char2idx = np.load(char2idx_path, allow_pickle=True).item()
    idx2char = np.load(idx2char_path, allow_pickle=True)

    # Determine the vocabulary size from the loaded mapping.
    vocab_size = len(char2idx)

    # Build the model architecture for inference (batch size 1).
    def build_model(batch_size):
        model = tf.keras.Sequential()
        # Define an explicit Input layer with a fixed batch size and variable sequence length
        model.add(tf.keras.Input(shape=(None,), batch_size=batch_size, dtype=tf.int32))
        # Embedding layer now simply converts integer indices to dense vectors
        model.add(tf.keras.layers.Embedding(vocab_size, args.embedding_dim))
        for i in range(args.num_layers):
            model.add(tf.keras.layers.LSTM(
                args.rnn_units,
                return_sequences=True,
                stateful=True,
                dropout=0.2,
                recurrent_dropout=0.2,
                recurrent_initializer='glorot_uniform'
            ))
        model.add(tf.keras.layers.Dense(vocab_size))
        return model

    # Build the model with batch_size=1 for inference.
    model = build_model(batch_size=1)

    # Load the trained model weights from the final checkpoint.
    final_checkpoint_path = os.path.join(args.checkpoint_dir, "final_checkpoint.weights.h5")
    if os.path.exists(final_checkpoint_path):
        model.load_weights(final_checkpoint_path)
        print("Model weights loaded from final_checkpoint.weights.h5.")
    else:
        print("Final checkpoint not found. Please train the model first using train_rnn.py.")
        return

    # Set up the pygame GUI.
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Text Generation with RNN")
    clock = pygame.time.Clock()

    # Create InputBox instances for prompt, temperature, and generation length.
    prompt_box = InputBox(50, 50, 700, 32, text="Enter prompt here...")
    temp_box = InputBox(50, 100, 100, 32, text=str(args.temperature))
    length_box = InputBox(200, 100, 100, 32, text=str(args.generation_length))

    # Create a button to trigger text generation.
    generate_button = Button(350, 100, 100, 32, "Generate")

    # Variable to store generated text.
    generated_text = ""
    # Define a rectangle area for displaying the generated text.
    output_rect = pygame.Rect(50, 150, 700, 400)

    running = True
    while running:
        for event in pygame.event.get():
            # Handle quit events.
            if event.type == pygame.QUIT:
                running = False
            # Handle events for input boxes.
            prompt_box.handle_event(event)
            temp_box.handle_event(event)
            length_box.handle_event(event)
            # Check if the generate button was clicked.
            if generate_button.is_clicked(event):
                # Get the prompt text from the input box.
                prompt = prompt_box.text
                try:
                    # Convert temperature and length inputs to proper types.
                    temperature = float(temp_box.text)
                    gen_length = int(length_box.text)
                except ValueError:
                    # If conversion fails, use default values.
                    temperature = args.temperature
                    gen_length = args.generation_length
                # Generate text using the model.
                generated_text = generate_text(model, prompt, gen_length, temperature, char2idx, idx2char)

        # Update the input boxes.
        prompt_box.update()
        temp_box.update()
        length_box.update()

        # Fill the screen with a background color.
        screen.fill((30, 30, 30))

        # Draw labels for the input boxes.
        prompt_label = FONT.render("Prompt:", True, pygame.Color('white'))
        screen.blit(prompt_label, (50, 20))
        temp_label = FONT.render("Temperature:", True, pygame.Color('white'))
        screen.blit(temp_label, (50, 80))
        length_label = FONT.render("Gen Length:", True, pygame.Color('white'))
        screen.blit(length_label, (200, 80))

        # Draw the input boxes and the generate button.
        prompt_box.draw(screen)
        temp_box.draw(screen)
        length_box.draw(screen)
        generate_button.draw(screen)

        # Display the generated text (wrapped to fit in the output rectangle).
        if generated_text:
            wrapped_lines = wrap_text(generated_text, FONT, output_rect.width)
            y_offset = output_rect.y
            for line in wrapped_lines:
                line_surface = FONT.render(line, True, pygame.Color('white'))
                screen.blit(line_surface, (output_rect.x, y_offset))
                y_offset += line_surface.get_height() + 2

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
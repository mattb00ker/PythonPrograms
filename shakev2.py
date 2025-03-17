#!/usr/bin/env python3
"""
shakev2.py

This script trains a character-level text generation model on the complete works of Shakespeare.
It reads text from a file, preprocesses it, builds a stateful LSTM model with an explicit Input layer
to support variable sequence lengths, and trains the model while saving checkpoints.

The model architecture is:
    - Input layer: Accepts variable-length sequences with a fixed batch size.
    - Embedding layer: Converts input integers to dense vectors.
    - LSTM layers: Stacked stateful LSTM layers with dropout for better generalization.
    - Dense layer: Outputs logits for each character in the vocabulary.

Hyperparameters are hardcoded in this script.
Requirements:
    - Python 3.10
    - TensorFlow 2.19.0
    - Numpy
"""

import tensorflow as tf
import numpy as np
import os

# ------------------ Hyperparameters (Hardcoded) ------------------
TEXT_FILE = "shake.txt"  # Path to the text file containing Shakespeare's works
EPOCHS = 1  # Number of training epochs
BATCH_SIZE = 64  # Batch size for training (fixed for stateful RNN)
SEQ_LENGTH = 50  # Length of each training sequence
EMBEDDING_DIM = 128  # Dimension of the embedding layer
RNN_UNITS = 256  # Number of units in each LSTM layer (using a higher value for better output)
NUM_LAYERS = 1  # Number of stacked LSTM layers
LEARNING_RATE = 0.001  # Learning rate for the optimizer
CHECKPOINT_DIR = './checkpoints'  # Directory to save model checkpoints


# ------------------------------------------------------------------

def main():
    # ------------------ Read and Preprocess Text Data ------------------
    # Read the entire text file into a single string
    with open(TEXT_FILE, 'r', encoding='utf-8') as f:
        text = f.read()
    text = text[:5000]  # For quick testing: use only the first 5000 characters; remove for full training

    # Convert text to lowercase for consistency
    text = text.lower()

    # Create a sorted list of unique characters (vocabulary) in the text
    vocab = sorted(set(text))
    vocab_size = len(vocab)

    # Create mapping dictionaries: character -> index and index -> character
    char2idx = {u: i for i, u in enumerate(vocab)}
    idx2char = np.array(vocab)

    # Convert the text to its integer representation
    text_as_int = np.array([char2idx[c] for c in text])

    # ------------------ Create Training Sequences ------------------
    # Create a TensorFlow dataset from the integer array
    char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)
    # Batch the data into sequences of (SEQ_LENGTH + 1) so we have input and target
    sequences = char_dataset.batch(SEQ_LENGTH + 1, drop_remainder=True)

    def split_input_target(chunk):
        """
        Splits a sequence into an input sequence and a target sequence.
        The target sequence is the input sequence shifted one character to the right.
        """
        input_text = chunk[:-1]
        target_text = chunk[1:]
        return input_text, target_text

    # Map each sequence to (input, target) pairs
    dataset = sequences.map(split_input_target)
    # Shuffle and batch the dataset for training
    dataset = dataset.shuffle(10000).batch(BATCH_SIZE, drop_remainder=True)

    # ------------------ Build the Stateful LSTM Model ------------------
    # Create a Sequential model with an explicit Input layer.
    # The Input layer specifies a fixed batch size and variable sequence length (None).
    model = tf.keras.Sequential()
    model.add(tf.keras.Input(shape=(None,), batch_size=BATCH_SIZE, dtype=tf.int32))
    # Embedding layer converts integer inputs to dense vectors.
    model.add(tf.keras.layers.Embedding(vocab_size, EMBEDDING_DIM))

    # Add NUM_LAYERS LSTM layers with dropout. All layers output a sequence.
    for i in range(NUM_LAYERS):
        model.add(tf.keras.layers.LSTM(
            RNN_UNITS,
            return_sequences=True,
            stateful=True,  # Maintains state between batches for continuity in training
            dropout=0.2,  # Dropout to reduce overfitting
            recurrent_dropout=0.2,
            recurrent_initializer='glorot_uniform'
        ))

    # Dense layer outputs logits for each character in the vocabulary.
    model.add(tf.keras.layers.Dense(vocab_size))

    # ------------------ Compile the Model ------------------
    def loss(labels, logits):
        """
        Loss function: Sparse Categorical Crossentropy.
        `from_logits=True` indicates that the output values are raw logits.
        """
        return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)

    # Compile the model using the Adam optimizer
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=LEARNING_RATE), loss=loss)

    # ------------------ Prepare Checkpoint Saving ------------------
    # Ensure the checkpoint directory exists.
    if not os.path.exists(CHECKPOINT_DIR):
        os.makedirs(CHECKPOINT_DIR)

    # Create a callback to save model weights after each epoch.
    checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
        filepath=os.path.join(CHECKPOINT_DIR, "ckpt_{epoch}.weights.h5"),
        save_weights_only=True
    )

    # ------------------ Train the Model ------------------
    model.fit(dataset, epochs=EPOCHS, callbacks=[checkpoint_callback])

    # Save the final model weights for later use.
    model.save_weights(os.path.join(CHECKPOINT_DIR, "final_checkpoint.weights.h5"))
    # Save the mapping dictionaries so they can be used during text generation.
    np.save(os.path.join(CHECKPOINT_DIR, "char2idx.npy"), char2idx)
    np.save(os.path.join(CHECKPOINT_DIR, "idx2char.npy"), idx2char)


if __name__ == "__main__":
    main()
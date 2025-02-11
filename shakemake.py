import os
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import load_dataset

# ----------------------------------------------------------
# 1. Configuration & Setup
# ----------------------------------------------------------
# Specify the model checkpoint to use. 'gpt2' is the small GPT‑2 model.
model_name = "gpt2"

# File path for your dataset.
# Make sure that "shakespeare.txt" is a plain text file containing the complete works of Shakespeare.
data_file = "shake.txt"

# Hyperparameters for training.
num_train_epochs = 3            # You can increase this number for more training.
per_device_train_batch_size = 2 # Adjust based on your GPU/CPU memory.
block_size = 128                # Maximum sequence length for each training example.

# Output directory to save the fine‑tuned model.
output_dir = "./gpt2-shakespeare-finetuned"

# ----------------------------------------------------------
# 2. Load Pre‑trained GPT‑2 Tokenizer and Model
# ----------------------------------------------------------
print("Loading tokenizer and model...")
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
# GPT‑2 does not have a pad token by default. We assign the end‑of‑text token as the padding token.
tokenizer.pad_token = tokenizer.eos_token

model = GPT2LMHeadModel.from_pretrained(model_name)
# Resize the token embeddings since we have added a pad token.
model.resize_token_embeddings(len(tokenizer))

# ----------------------------------------------------------
# 3. Prepare the Dataset
# ----------------------------------------------------------
# We'll use the Hugging Face 'datasets' library to load our text file.
# The file is treated as a dataset with a single field "text".
print("Loading dataset...")
dataset = load_dataset("text", data_files={"train": data_file})

# A function to tokenize the text. It splits the text into chunks of a fixed size (block_size).
def tokenize_function(examples):
    # Use the tokenizer to convert text into token ids.
    return tokenizer(examples["text"], truncation=True, max_length=block_size, padding="max_length")

print("Tokenizing dataset...")
tokenized_datasets = dataset.map(tokenize_function, batched=True, remove_columns=["text"])
# Set the format for PyTorch tensors.
tokenized_datasets.set_format(type="torch")

# ----------------------------------------------------------
# 4. Create Data Collator for Language Modeling
# ----------------------------------------------------------
# Since we are training a language model, we disable masked language modeling (mlm=False).
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# ----------------------------------------------------------
# 5. Setup Training Arguments and Trainer
# ----------------------------------------------------------
training_args = TrainingArguments(
    output_dir=output_dir,
    overwrite_output_dir=True,
    num_train_epochs=num_train_epochs,
    per_device_train_batch_size=per_device_train_batch_size,
    save_steps=500,                   # Save checkpoint every 500 steps.
    save_total_limit=2,               # Keep only the last 2 checkpoints.
    prediction_loss_only=True,
    logging_steps=100,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    data_collator=data_collator,
)

# ----------------------------------------------------------
# 6. Fine‑Tune the Model
# ----------------------------------------------------------
print("Starting training. This may take a while...")
trainer.train()
print("Training complete.")

# Save the fine‑tuned model and tokenizer.
print(f"Saving model to {output_dir} ...")
trainer.save_model(output_dir)
tokenizer.save_pretrained(output_dir)

# ----------------------------------------------------------
# 7. Generate Text with the Fine‑Tuned Model
# ----------------------------------------------------------
def generate_shakespeare(prompt, max_length=200, temperature=1.0, top_k=50, top_p=0.95):
    """
    Generate text using the fine‑tuned GPT‑2 model.

    Parameters:
      prompt (str): The initial text prompt.
      max_length (int): Total length of the generated sequence (including prompt).
      temperature (float): Sampling temperature; lower values make output more deterministic.
      top_k (int): The number of highest probability vocabulary tokens to keep for top‑k filtering.
      top_p (float): Cumulative probability for nucleus sampling.

    Returns:
      str: Generated text.
    """
    # Encode the prompt to tensor format.
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    input_ids = input_ids.to(model.device)  # Move to the appropriate device

    # Generate text.
    output_sequences = model.generate(
        input_ids=input_ids,
        max_length=max_length,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id,
        num_return_sequences=1,
    )

    # Decode the generated tokens to text.
    generated_text = tokenizer.decode(output_sequences[0], skip_special_tokens=True)
    return generated_text

# ----------------------------------------------------------
# 8. Test Generation
# ----------------------------------------------------------
# Change the prompt as desired.
prompt_text = "O, what a noble mind is here o'erthrown!"
print("\nGenerated Text:\n")
print(generate_shakespeare(prompt_text, max_length=300))

## fine-tuning code with hyperparameters

## first,create virtual environment
# conda create --name torch-env pytorch torchvision pytorch-cuda=12.1 -c pytorch -c nvidia
## then, activate env then
# pip install datasets trl ipykernel

import torch
from transformers import (
    pipeline,
    AutoModelForCausalLM,
    AutoTokenizer,
)
from datasets import load_dataset
from trl import SFTTrainer, SFTConfig

# Add this to monitor MPS memory usage
def print_mps_memory():
    if torch.backends.mps.is_available():
        print(f"MPS allocated: {torch.mps.current_allocated_memory() / 1024**3:.2f} GB")
        print(f"MPS cached: {torch.mps.driver_allocated_memory() / 1024**3:.2f} GB")

# Call this periodically during training
# print_mps_memory()

# Check if MPS is available
if torch.backends.mps.is_available():
    device = torch.device("mps")
    print("MPS device found.")
else:
    device = torch.device("cpu")
    print("MPS device not found, using CPU.")

ds = load_dataset("ANONYMIZED")

# Set environment variables for better performance
import os
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
os.environ["PYTORCH_MPS_HIGH_WATERMARK_RATIO"] = "0.0"

# Clear memory first
if torch.backends.mps.is_available():
    torch.mps.empty_cache()

# Training configuration with proper parameters
training_params = SFTConfig(
    output_dir="../checkpoints",
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    gradient_accumulation_steps=2,
    num_train_epochs=3, # moving slowly from 1 to 3
    learning_rate=2e-4,
    weight_decay=0.001,
    dataset_text_field="text",
    report_to="none",
    bf16=False,
    fp16=False,
    dataloader_pin_memory=False,
    remove_unused_columns=False,
    max_seq_length=512,
    gradient_checkpointing=True,
    dataloader_num_workers=0,
    save_strategy="epoch",
    logging_steps=10,
    average_tokens_across_devices=False  # Fix for single device training
    # Remove loss_type parameter to avoid the warning
    # The trainer will automatically use ForCausalLMLoss which is correct
)

# Configure model for gradient checkpointing compatibility
model.config.use_cache = False

trainer = SFTTrainer(
    model=model,
    train_dataset=ds['train'],
    processing_class=tokenizer,
    args=training_params
)

# Add this to monitor MPS memory usage
def print_mps_memory():
    if torch.backends.mps.is_available():
        print(f"MPS allocated: {torch.mps.current_allocated_memory() / 1024**3:.2f} GB")
        print(f"MPS cached: {torch.mps.driver_allocated_memory() / 1024**3:.2f} GB")

# Call this periodically during training
# print_mps_memory()

trainer.train()

trainer.model.save_pretrained("../models/NAME")
trainer.tokenizer.save_pretrained("../models/NAME")

model = AutoModelForCausalLM.from_pretrained("../models/NAME")
tokenizer = AutoTokenizer.from_pretrained("../models/NAME")

pipe = pipeline('text-generation', model=model, tokenizer=tokenizer, max_length=50)

pipe("Femininity is")

pipe("Masculinity is")

pipe("Transgender is")

pipe("The gender binary is")


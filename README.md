# Dizparc Secured Hotspot - Jailbreaking Challenge

A Gradio-based AI security challenge where users attempt to extract a hidden flag from a chatbot using prompt injection and social engineering techniques.

## Overview

This project demonstrates AI security concepts by creating a chatbot that guards a secret. Users must craft clever prompts to bypass the bot's restrictions and reveal the hidden flag. The challenge simulates real-world scenarios where AI systems need to resist manipulation attempts.

## Features

- **Interactive Chatbot Interface**: Built with Gradio for easy web-based interaction
- **AI-Powered**: Uses OpenAI-compatible API
- **Security Challenge**: Tests various jailbreaking techniques including:
  - Prompt injection
  - Social engineering
  - Instruction conflicts
- **Bilingual Support**: System prompts and challenge instructions available in both Swedish and English

## Installation

```bash
# Install dependencies using uv
uv sync
```

## Usage

### Local Setup
Run with local Llama model:
```bash
python main.py --local
```

### Non-Local Setup
Run with OpenAI-compatible API (default):
```bash
python main.py
```

### Docker Setup
Build and run using the build script:
```bash
bash build_script.sh
```

**Note:** The `models/` folder should contain the models for Docker to find local models.

The application will launch on `http://127.0.0.1:7884`

## Configuration

### Using Custom Models
To use your own models, update the model settings in `main.py`:
- **Local mode (llama.cpp)**: Modify the `get_Llama()` function to point to your model file
- **Non-local mode (OpenAI)**: Update the `get_openai()` function with your API endpoint and model name

### Fine-Tuned Guardrail Model
This challenge includes a fine-tuned model designed to resist prompt injection attacks: [Alindstroem89/Llama-3.2-1B-Instruct_guardrail](https://huggingface.co/Alindstroem89/Llama-3.2-1B-Instruct_guardrail)

Download the GGUF model from Hugging Face:
```bash
# Option 1: Download all GGUF files to models folder
hf download Alindstroem89/Llama-3.2-1B-Instruct_guardrail --include "*.gguf" --local-dir ./models

# Option 2: Download specific GGUF file
hf download Alindstroem89/Llama-3.2-1B-Instruct_guardrail --include "Llama-3.2-3B-Instruct.Q4_K_M.gguf" --local-dir ./models

# Option 3: Download using llama-cli
llama-cli -hf Alindstroem89/Llama-3.2-1B-Instruct_guardrail --jinja
```

## Technical Details

- **Framework**: Gradio

## Challenge Objective

The chatbot is programmed to protect a secret flag. Your goal is to use creative prompting techniques to make the bot reveal information it shouldn't share. This educational exercise helps understand AI vulnerability and security testing.

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
- **Swedish Language**: Instructions and interface in Swedish

## Installation

```bash
# Install dependencies using uv
uv sync
```

## Usage

```bash
# Run the application
python main.py
```

The application will launch on `http://0.0.0.0:7860`

## Technical Details

- **Framework**: Gradio

## Challenge Objective

The chatbot is programmed to protect a secret flag. Your goal is to use creative prompting techniques to make the bot reveal information it shouldn't share. This educational exercise helps understand AI vulnerability and security testing.

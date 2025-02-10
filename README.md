# Ollama Vision Chat

Simple Python wrapper for interacting with Ollama's vision models. Process images in batch and get JSON-formatted responses.

## Requirements

- Python 3.x
- Ollama running locally with vision models
- `requests` library

## Setup

1. Install dependencies:
```bash
pip install requests
```

2. Ensure Ollama is running with vision models (default port: 11434)

## Usage

1. Run the script:
```bash
python ollama_vision_chat.py
```

2. Place images in the `uploads` folder
3. Enter prompts when prompted
4. Find results in:
   - `processed/`: Processed images
   - `results/`: JSON responses

## Configuration

- Default model: llama3.2-vision
- Temperature: 0.2
- Server URL: http://localhost:11434/api/generate

## Response Format

Results are saved as JSON with:
- Timestamp
- Image name
- Prompt
- Temperature
- Model response
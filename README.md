# End-to-End Medical Chatbot using Llama 2

A comprehensive medical chatbot implementation utilizing the Llama 2 language model for intelligent healthcare conversations.

## Prerequisites

- Python 3.x
- Virtual environment support
- Internet connection for model download

## Installation

### 1. Create Virtual Environment

```bash
python -m venv mchatbot
```

### 2. Activate Virtual Environment

**Windows:**
```bash
mchatbot\Scripts\activate
```

**Linux/macOS:**
```bash
source mchatbot/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Model Setup

### Download Llama 2 Model

The application requires the Llama 2 7B Chat model in GGML format. Download the model using the following command:

```bash
curl -L -o llama-2-7b-chat.ggmlv3.q4_0.bin https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q4_0.bin && echo "Download complete: llama-2-7b-chat.ggmlv3.q4_0.bin saved to $(pwd)"
```

**Note:** The download may take 20 minutes or more depending on your internet connection.

## Testing

### Verify Model Functionality

Run a test file from the `tests/` folder to verify that the model is working correctly:

```bash
python tests/test_medical_chatbot.py
```

**Important:** On first run, the model may take 40-50 seconds to generate a response as it loads into memory.

## Usage

Once the model is downloaded and tested, you can start using the medical chatbot for healthcare-related conversations.

## Project Structure

```
End-to-End-Medical-Chatbot-using-llama-2/
├── mchatbot/          # Main application code
├── model/             # Model-related files
├── tests/             # Test files
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## License

This project is licensed under the terms specified in the LICENSE file. 

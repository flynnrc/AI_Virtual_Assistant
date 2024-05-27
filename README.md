# AI Virtual Assistant

## Overview
This Python script allows you to have an interactive conversation with an AI assistant. 

## Installation
Before running the script, ensure you have installed the following dependencies:
- OpenAI library: `pip install openai`

### API Key Setup
To use the OpenAI language model in the script, you need to obtain an API key from OpenAI. Follow these steps:
1. Sign up for an account on the [OpenAI website](https://openai.com/).
2. Generate an API key from your account dashboard.
3. Replace `'your key here'` in the script with your API key:
    ```python
    openai.api_key = 'your key here'
    ```

## Usage
1. Run the script
2. Input your message when prompted. Type `-exit` to quit the chat or by alternative means.
3. The script will generate a response from the AI based on the provided input.

## License
This project is licensed under the [MIT License](LICENSE).
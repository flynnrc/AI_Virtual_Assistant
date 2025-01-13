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

## Docker Setup
You can run this project inside a Docker container for better isolation and ease of setup.

### Prerequisites
- Docker installed on your machine. Refer to the [Docker Installation Guide](https://docs.docker.com/get-docker/) if needed.

### Steps

1. **Create a `secrets.env` file**:
   Add your OpenAI API key to a `secrets.env` file in the project root:
   `OPENAI_API_KEY=your-key-here`

2. **Build the Docker image**:
   Run the following command to build the Docker image:
   `docker build -t ai-assistant .`

3. **Run the Docker container**:
   Use the following command to run the container with the secrets file:
  `docker run -it --rm --env-file secrets.env ai-assistant`

4. **Optional: Pass the API key as a command-line argument**:
   Alternatively, you can pass the API key directly as an environment variable using the `-e` flag:
   `docker run -it --rm -e OPENAI_API_KEY=your-key-here ai-assistant`

## License
This project is licensed under the [MIT License](LICENSE).
import openai

# Set the OpenAI API key for authentication
openai.api_key = 'your key here'
# Define the model to be used
gptModel = "gpt-3.5-turbo"
# Define the temperature to be used: 0 being the most deterministic
temp = 0 
# Store relevant parts of the conversation to maintain context
chat_messages = []
# Append a system message to set the context and behavior of the assistant
chat_messages.append(
    {
        "role": "system", 
        "content": """
        You are a knowledgeable and friendly assistant capable of 
        helping with a variety of topics, from answering questions and providing 
        explanations to offering advice and recommendations.
        """
    }
)

while True:
    # Prompt the user to enter a message
    userInput = input("Enter prompt or '-exit' to quit:")

    if userInput.lower() == "-exit":
        print("Exiting chat.")
        break

    #Save messages as user to preserve message context.
    chat_messages.append({"role":"user", "content": userInput})

    # Call the OpenAI API to generate a response
    #'''
    response = openai.chat.completions.create(
        model=gptModel,
        messages=[{"role": "user", "content": userInput}],
        temperature=temp
    )    
    ai_response = response.choices[0].message.content
  
    # Append the AI's responses with the role "assistant"
    chat_messages.append({"role": "assistant", "content":ai_response})

    print("GPT Response: ", ai_response)
    print(chat_messages)
import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')
#openai.api_key = 'YOUR_OPENAI_API_KEY'

# Function to interact with ChatGPT
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can also use "text-davinci-002" for older version
        prompt=prompt,
        max_tokens=150  # Adjust the response length as per your requirement
    )
    return response.choices[0].text.strip()

# Main interaction loop
print("ChatGPT: Hello! How can I assist you today? (Type 'exit' to end)")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("ChatGPT: Goodbye!")
        break
    prompt = f"You: {user_input}\nChatGPT:"
    response = chat_with_gpt(prompt)
    print(response)

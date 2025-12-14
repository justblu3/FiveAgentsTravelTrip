from openai import OpenAI

# We point the client to your local Ollama server
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama', # specific key not required, but the field cannot be empty
)

def ask_llama(prompt):
    response = client.chat.completions.create(
        model="llama3", # Make sure this matches what you pulled (llama3 or llama3.2)
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Test it
print("Sending request to Llama...")
answer = ask_llama("Explain in one sentence what a Travel Agent does.")
print("\nLlama Answer:", answer)
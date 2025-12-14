from openai import OpenAI

# Setup the connection to Ollama once
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama',
)

class Agent:
    def __init__(self, name, system_instruction):
        self.name = name
        self.system_instruction = system_instruction

    def work(self, task_input):
        print(f"\n🔹 {self.name} is working...")
        response = client.chat.completions.create(
            model="llama3", 
            messages=[
                {"role": "system", "content": self.system_instruction},
                {"role": "user", "content": task_input}
            ]
        )
        return response.choices[0].message.content
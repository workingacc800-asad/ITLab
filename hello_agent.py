import os 
from dotenv import load_dotenv
from openai import OpenAI
from google import genai

load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

# 3. Call the model on Groq
response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "system", "content": "You are a fast and helpful AI assistant."},
        {"role": "user", "content": "Hello! What can you do?"}
    ]
)
while True:
    #ask the user for input
    user_input = input("\n Enter your query: ")

    #if user want to exit
    if user_input.lower().strip() in ["quit","exit"]:
        print("Good Byee")
        break
    if not user_input.strip():
        continue
    # 3. Call the model on Groq
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": "You are a fast and helpful AI assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    print(f"\nAI: {response.choices[0].message.content} ")

#Here we will practice about dotenv
import os
from dotenv import load_dotenv
from dotenv import dotenv_values
from dotenv import find_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
print(groq_api_key)

env_file_path = find_dotenv()
print(env_file_path)
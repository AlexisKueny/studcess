from openrouter import OpenRouter
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenRouter(api_key=os.getenv("OPENROUTER_SDK_KEY")) 
print(client)
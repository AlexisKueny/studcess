from openrouter import OpenRouter
from dotenv import load_dotenv
import os

load_dotenv()

with OpenRouter(api_key=os.getenv("OPENROUTER_SDK_KEY")) as client:
    response = client.responses.send(
        model="~openai/gpt-sol-latest",
        input="What is the meaning of life?",
    )

    if response.status != "completed":
        message = response.error.message if response.error else f"Response ended as {response.status}"
        raise RuntimeError(message)

    message = next(item for item in response.output if item.type == "message")
    print(next(part.text for part in message.content if part.type == "output_text"))
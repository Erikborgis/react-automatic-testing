import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def call_openai_api(prompt):

    # Set your API key
    openai.api_key = os.getenv("CHAT_GPT_API_KEY")

    model_engine = "text-davinci-003"

    # Send the request
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=150,
        temperature=0.1
    )

    # Print the completion
    return response.choices[0].text
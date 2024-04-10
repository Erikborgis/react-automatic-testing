from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set API key and initialize client.
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Call openai api and ask it to generate unit test for react native component with specified temperature.
def call_openai_api(message, temperature):

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message,
        temperature=temperature,
        top_p=0.1
    )

    content = response.choices[0].message.content
    return content

# Takes the react component, the failing unit test, the error message for the failing unit test and the path to the react component.
def regenerate_test(message, temperature):

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages= message,
        temperature=temperature,
        top_p=0.1
    )

    content = response.choices[0].message.content
    return content

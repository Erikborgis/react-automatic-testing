from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set API key and initialize client.
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Call openai api and ask it to generate unit test for react native component with specified temperature.
def call_openai_api(code, path_to_react_component, temperature):
    prompt = f"I need unit tests for the React Native Component\n\
    Do not write comments on the end of the file\n\
    Import the React Native Component from ../{path_to_react_component}\n\
    The React Native Component to be tested:\n\
    {code}"

    assistantPrompt = "Always render ui elements if available, and always test the functionality\n\
    Follow this template for the test file:\n\
    ```jsx\n\
    import React from 'react';\n\
    import { render, fireEvent } from '@testing-library/react-native';\n\
    ```"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful software tester for React Native components using the testframework Jest"},
            {"role": "assistant", "content": assistantPrompt},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        top_p=0.1
    )

    content = response.choices[0].message.content
    code_block = content.split("```jsx")[1].strip()
    code_block = code_block.split("```")[0].strip()
    return code_block

# Takes the react component, the failing unit test, the error message for the failing unit test and the path to the react component.
def regenerate_test(react_component_text, test, error_message, path_to_react_component):

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful software tester for React Native compoonents"},
            {"role": "user", "content": f"There was an error with the unit test:\n{test}\n For the REACT NATIVE component:\n{react_component_text}\nError message:\n{error_message}.\nPlease write a new unit test but keep the passed tests\nDO NOT WRITE COMMENTS ON THE END OF THE FILE.\nOnly include the react code in your answer. No other text\n Import the react native component from ../{path_to_react_component}\n"}
        ],
        temperature=0.1
    )

    content = response.choices[0].message.content
    code_block = content.split("```jsx")[1].strip()
    code_block = code_block.split("```")[0].strip()
    return code_block

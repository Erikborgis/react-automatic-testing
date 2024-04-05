from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def call_openai_api(prompt, path_to_react_component):

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful software tester"},
            {"role": "user", "content": f"Write unit tests for the react component with the framework Jest.\nDO NOT WRITE COMMENTS ON THE END OF THE FILE.\nSurround the test with ```jsx.\n Import the react component from ../{path_to_react_component}\n React component:\n {prompt}"}
        ],
        max_tokens=600,
        temperature=0.1
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
            {"role": "system", "content": "You are a helpful software tester"},
            {"role": "user", "content": f"There was an error with the unit test:\n{test}\n For the react component:\n{react_component_text}\nError message:\n{error_message}.\nPlease write a new unit test\nDO NOT WRITE COMMENTS ON THE END OF THE FILE.\nOnly include the react code in your answer. No other text\n Import the react component from ../{path_to_react_component}\n"}
        ],
        max_tokens=600,
        temperature=0.1
    )

    content = response.choices[0].message.content
    code_block = content.split("```jsx")[1].strip()
    code_block = code_block.split("```")[0].strip()
    return code_block

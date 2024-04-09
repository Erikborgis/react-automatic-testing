def create_default_prompts(path_to_react_component, code):
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

  return prompt, assistantPrompt

def create_assistant_prompts(created_test_content, test_logs):
  assistant_prompt_list = []
  for i in range(len(created_test_content)):
    prompt = f"This was the result of your {i} try:\n\
      {created_test_content[i]}\n\
      This was the failing log in it:\n\
      {test_logs[i]}\n"
    assistant_prompt_list.append(prompt)
  
  return assistant_prompt_list

def retry_prompt(path_to_react_component, code, failed_test_prompt_list):
  messages = []
  _, assistant_prompt = create_default_prompts(path_to_react_component, code)
  
  messages.append({"role": "system", "content": "You are a helpful software tester for React Native components using the testframework Jest"})
  messages.append({"role": "assistant", "content": assistant_prompt})

  for prompt_text in failed_test_prompt_list:
    messages.append({"role": "assistant", "content": prompt_text})

  messages.append({"role": "user", "content": f"Fix the test file, make sure you rewrite the whole file but only fix the error."})
  print(messages)
  return messages


def first_prompt(path_to_react_component, code):
  prompt, assistant_prompt = create_default_prompts(path_to_react_component, code)
  messages = []

  messages.append({"role": "system", "content": "You are a helpful software tester for React Native components using the testframework Jest"})
  messages.append({"role": "assistant", "content": assistant_prompt})
  messages.append({"role": "user", "content": prompt})
  
  print(messages)
  return messages
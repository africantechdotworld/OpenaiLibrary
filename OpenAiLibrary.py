import os
import openai

userInput = input("Please enter your input")
openai.api_key = "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"
response_data = openai.Completion.create(
engine = "text-davinci-003",
prompt = userInput,
max_tokens = 256
)
print(response_data["choices"] [0] ["text"])
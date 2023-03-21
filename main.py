import os
import openai



openai.api_key = os.getenv("OPENAI_API_KEY")

flagy="Y"
while(flagy=="Y"):

    gpt_prompt = str(input("Enter your Query: "))


    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=gpt_prompt,
      temperature=0.5,
      max_tokens=256,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )


    print(response['choices'][0]['text'])

    print("Do you still want to continue (Y/N)")
    flagy=str(input())
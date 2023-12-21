import os

import openai as open_ai_origin
from dotenv import load_dotenv

load_dotenv()


# 皮api


def init_openai():
    open_ai_origin.api_key = os.getenv("open_key_f_1")
    open_ai_origin.proxy = "http://127.0.0.1:7890"
    open_ai_origin.api_base = os.getenv("api_base")
    return open_ai_origin


def get_completion(prompt, model="gpt-3.5-turbo"):
    openai = init_openai()
    completion = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message['content']


# test
print(get_completion("1+1是什么"))

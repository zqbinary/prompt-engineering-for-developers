import json
import os

import requests
from dotenv import load_dotenv


# 套皮openai curl 方案

def get_completion_(prompt):
    load_dotenv()
    apiUrl = 'https://api2.hdxia.com/v1/chat/completions'
    apiKey = os.getenv("open_key_f_1")
    temperature = 1.0
    max_tokens = 600
    # model = 'gpt-4'
    model = "gpt-3.5-turbo"

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + apiKey
    }
    proxy = {
        "http": "http://127.0.0.1:7890",
        "https": "http://127.0.0.1:7890"
    }

    post = {
        'model': model,
        'max_tokens': max_tokens,
        'temperature': temperature,
        'messages': [
            # {
            #     'role': 'system',
            #     'content': '请输入你的提示信息'
            # },
            {
                'role': 'user',
                'content': prompt
            }
        ]
    }

    try:
        response = requests.post(
            apiUrl,
            headers=headers,
            data=json.dumps(post),
            timeout=None,
            proxies=proxy
        )
        print(f"Response status code: {response.status_code}")

        if response.status_code == 200:
            if response.text:
                data = response.json()
                print('response:', data)
                return data['choices'][0]['message']['content']

            else:
                print("The response is empty.")
        else:
            print(f"Request failed, response content: {response.text}")
    except Exception as e:
        print('Error:', e)


if __name__ == '__main__':
    print(get_completion_("1+1等于几"))

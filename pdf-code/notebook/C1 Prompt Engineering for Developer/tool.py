import zhipuai
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()
zhipuai.api_key = os.getenv("api_key")

IS_STREAM = False


def get_completion(prompt):
    messages = [{"role": "user", "content": prompt}]
    response = zhipuai.model_api.sse_invoke(
        model="chatglm_turbo",
        prompt=messages,
        temperature=0,
    )

    answer = ""
    for event in response.events():
        if event.event == "add":
            if IS_STREAM:
                print(event.data, end="")
            else:
                answer += event.data
        elif event.event == "error" or event.event == "interrupted":
            print(event.data, end="")
        elif event.event == "finish":
            if IS_STREAM:
                print(event.data, end="")
            else:
                answer += event.data
        else:
            if IS_STREAM:
                print(event.data, end="")

    return answer

# test
# print(get_completion("hello 你好"))

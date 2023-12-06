import zhipuai
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()
zhipuai.api_key = os.getenv("api_key")


def get_completion(prompt):
    messages = [{"role": "user", "content": prompt}]
    response = zhipuai.model_api.sse_invoke(
        model="chatglm_turbo",
        prompt=messages,
        temperature=0,
        top_p=0.7,
        incremental=True
    )

    answer = ""
    for event in response.events():
        if event.event == "add":
            answer += event.data
            # print(event.data, end="")
        elif event.event == "error" or event.event == "interrupted":
            print(event.data, end="")
        elif event.event == "finish":
            # print(event.data)
            # print(event.meta, end="")
            answer += event.data
        else:
            print(event.data, end="")

    return answer

# for test
# print(get_completion("hello 你好"))

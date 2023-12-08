import zhipuai
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()
zhipuai.api_key = os.getenv("api_key")

IS_STREAM = False


def print_stream(response):
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


# 智谱有坑，
# 1 必须是 assistant 不能是 system
# 2 必须 user开始
def get_completion(prompt):
    messages = [{"role": "user", "content": prompt}]
    response = zhipuai.model_api.sse_invoke(
        model="chatglm_turbo",
        prompt=messages,
        temperature=0,
    )
    print_stream(response)


def change_system_to_assistant(messages):
    for msg in messages:
        if msg['role'] == 'system':
            msg['role'] = 'assistant'
    if messages[0]['role'] == 'assistant':
        messages.insert(0, {"role": "user", "content": "你好"})
    return messages


def get_completion_from_messages(messages, temperature=0):
    messages = change_system_to_assistant(messages)

    response = zhipuai.model_api.sse_invoke(
        model="chatglm_turbo",
        prompt=messages,
        temperature=temperature,
        incremental=False
    )
    for event in response.events():
        if event.event == "finish":
            return event.data


# test
# print(get_completion("hello 你好"))

"""
messages = [
    # {"role": "user", "content": "你好"},
    {'role': 'assistant', 'content': '你是一个像莎士比亚一样说话的助手。'},
    # {'role': 'assistant', 'content': '鸡为什么过马路'},
    # {'role': 'user', 'content': '我不知道'}
    {'role': 'user', 'content': '给我讲个笑话'},
]
prompt = [
    # {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "我是人工智能助手"},
    # {"role": "user", "content": "你叫什么名字"},
    # {"role": "assistant", "content": "我叫chatGLM"},
    {"role": "user", "content": "你都可以做些什么事"},
]
messages = prompt
response = get_completion_from_messages(messages, temperature=1)
print(response)
"""
"""
messages =  [
{'role':'system', 'content':'你是一个像莎士比亚一样说话的助手。'},
{'role':'user', 'content':'给我讲个笑话'},
{'role':'assistant', 'content':'鸡为什么过马路'},
{'role':'user', 'content':'我不知道'}  ]
response = get_completion_from_messages(messages, temperature=1)
print(response)
"""

import os

from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

load_dotenv()
api_key = os.getenv("open_key_f_1")


def gen_chat(temperature=0.0):
    global chat
    chat = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        openai_api_key=api_key,
        openai_api_base=os.getenv('api_base'),
        openai_proxy="http://127.0.0.1:7890",
        temperature=temperature,
    )
    return chat


chat = gen_chat()


def c21():
    # 首先，构造一个提示模版字符串：`template_string`
    template_string = """把由三个反引号分隔的文本\
       翻译成一种{style}风格。\
       文本: ```{text}```
       """

    # 然后，我们调用`ChatPromptTemplatee.from_template()`函数将
    # 上面的提示模版字符`template_string`转换为提示模版`prompt_template`

    prompt_template = ChatPromptTemplate.from_template(template_string)

    print("\n", prompt_template.messages[0].prompt)

    customer_style = """正式普通话 \
       用一个平静、尊敬的语气
       """

    customer_email = """
       嗯呐，我现在可是火冒三丈，我那个搅拌机盖子竟然飞了出去，把我厨房的墙壁都溅上了果汁！
       更糟糕的是，保修条款可不包括清理我厨房的费用。
       伙计，赶紧给我过来！
       """

    # 使用提示模版
    customer_messages = prompt_template.format_messages(
        style=customer_style,
        text=customer_email)
    # 打印客户消息类型
    print("客户消息类型:", type(customer_messages), "\n")

    # 打印第一个客户消息类型
    print("第一个客户客户消息类型类型:", type(customer_messages[0]), "\n")

    # 打印第一个元素
    print("第一个客户客户消息类型类型: ", customer_messages[0], "\n")

    customer_response = chat(customer_messages)
    print(customer_response.content)


def c41():
    llm = gen_chat()
    prompt = ChatPromptTemplate.from_template("描述制造{product}的一个公司的最佳名称,用中文回答")
    chain = LLMChain(llm=llm, prompt=prompt)
    product = '大号床单套餐'
    res = chain.run(product)
    print(res)


if __name__ == '__main__':
    c41()

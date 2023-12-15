# 导入tool函数装饰器
import sys
from datetime import date

from langchain.agents import initialize_agent
from langchain.agents import tool

sys.path.append('../')
from llm import gen_chat


@tool
def time(text: str) -> str:
    """
    返回今天的日期，用于任何需要知道今天日期的问题。\
    输入应该总是一个空字符串，\
    这个函数将总是返回今天的日期，任何日期计算应该在这个函数之外进行。
    """
    return str(date.today())


from langchain.agents import AgentType


def c71():
    global llm
    llm = gen_chat()
    # 初始化代理
    agent = initialize_agent(
        tools=[time],  # 将刚刚创建的时间工具加入代理
        llm=llm,  # 初始化的模型
        agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,  # 代理类型
        handle_parsing_errors=True,  # 处理解析错误
        verbose=True  # 输出中间步骤
    )
    # 使用代理询问今天的日期.
    # 注: 代理有时候可能会出错（该功能正在开发中）。如果出现错误，请尝试再次运行它。
    agent("今天的日期是？")


if __name__ == "__main__":
    c71()

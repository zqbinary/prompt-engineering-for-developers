import sys

sys.path.append('../')
from llm import gen_emm_chat,gen_chat


# import langchain
import pandas as pd
from IPython.display import display, Markdown  # 在jupyter显示信息的工具

# langchain.debug = True
from langchain.chains import LLMChain, RetrievalQA
from langchain.vectorstores import DocArrayInMemorySearch  # 向量存储
from langchain_community.document_loaders import CSVLoader


# 盗版的gpt
# output
# 猫：[-0.007912245514100764, -0.00993155027967353, -0.010532062414242241]
# Incorrect API key provided: sess-pNG*********************************tUAI. You can find your API key at https://platform.openai.com/account/api-keys. (request id: 202312141540497621737250A3ZW1rA)
def t1():
    embeddings = gen_emm_chat()
    embed = embeddings.embed_query("猫")
    # print(embed)
    print("猫：" + str(embed[:3]))
    # """
    embed = embeddings.embed_query("狗")
    print("狗：" + str(embed[:3]))
    embed = embeddings.embed_query("香蕉")
    print("香蕉：" + str(embed[:3]))
    # """
# require: `pip install "langchain[docarray]"`.
# failed
from langchain.indexes import VectorstoreIndexCreator

def c51():
    file = './data/聊城1.csv'
    # loader = CSVLoader(file, encoding='utf-8')
    loader = CSVLoader(file, encoding='utf-8')
    data = pd.read_csv(file, usecols=[0, 1, 2, 3, 4], encoding='utf-8')
    # 显示一下数据,也可以不用
    header = data.head()
    print(header)
    llm = gen_chat()
    index = VectorstoreIndexCreator(vectorstore_cls=DocArrayInMemorySearch
                                    ).from_loaders([loader])
    query = '用md表格，列出所有井盖产品,对每个产品进行描述总结'
    response = index.query(query, llm=llm)
    print(response)


def c52():
    from langchain.chains import RetrievalQA  # 虽然名字里没有Chain,却的确是一个Chain，用于帮助检索文档
    file = './data/聊城1.csv'
    # loader = CSVLoader(file, encoding='utf-8')
    loader = CSVLoader(file, encoding='utf-8')
    doc = loader.load()
    # 0 title
    # 4 content
    data = pd.read_csv(file, usecols=[0, 1, 2, 3, 4], encoding='utf-8')
    header = data.head()
    embed = gen_emm_chat()
    print(header)
    db = DocArrayInMemorySearch.from_documents(doc, embed)
    llm = gen_chat()
    retriever = db.as_retriever()  # retriever是一个通用接口，定义了接收查询内容并返回相似文档的方法
    # 实例化一个RetrievalQA链
    qa_stuff = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        verbose=True
    )

    query = '用md表格，列出所有井盖产品,对每个产品进行描述总结'
    response = qa_stuff.run(query)
    print('1', response)
    md_data = Markdown(response)
    print('2', md_data)
    display(md_data)


def c53():
    file = './data/聊城1.csv'
    # loader = CSVLoader(file, encoding='utf-8')
    loader = CSVLoader(file, encoding='utf-8')
    docs = loader.load()

    embeddings = gen_emm_chat()
    db = DocArrayInMemorySearch.from_documents(docs, embeddings)
    query = '列出所有井盖产品,对每个产品进行描述总结'
    docs2 = db.similarity_search(query)
    print('doc2', docs2)
    llm = gen_chat()
    qdocs = "".join(docs[i].page_content for i in range(len(docs2)))
    response = llm.call_as_llm(f"{qdocs} 问题：请用md列出所有井盖产品，并对每个产品进行总结")
    print(response)


def c54():
    file = './data/聊城1.csv'
    # loader = CSVLoader(file, encoding='utf-8')
    loader = CSVLoader(file, encoding='utf-8')
    docs = loader.load()

    embeddings = gen_emm_chat()
    db = DocArrayInMemorySearch.from_documents(docs, embeddings)
    retriever = db.as_retriever()
    print('1', flush=True)
    llm = gen_chat()
    print('2', flush=True)
    qa_stuff = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        verbose=True
    )
    query = '列出一个井盖产品,对产品进行描述总结'
    response = qa_stuff.run(query)
    print(response)


if __name__ == "__main__":
    try:
        t1()
        # c51()
        # c52()
        # c53()
        c54()
    except Exception as e:
        print(str(e))

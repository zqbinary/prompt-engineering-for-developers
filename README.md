![figures/readme.png](https://github.com/datawhalechina/prompt-engineering-for-developers/blob/main/figures/readme2.png)

# 面向开发者的 LLM 入门课程

## 项目简介
在原项目的基础上，不用原来的openid ,用智谱ai做。

启动
jupyter notebook


**在线阅读地址：[面向开发者的 LLM 入门课程-在线阅读](https://datawhalechina.github.io/prompt-engineering-for-developers/)**

**PDF下载地址：[面向开发者的 LLM 入门教程-PDF](https://github.com/datawhalechina/prompt-engineering-for-developers/releases)**

**英文原版地址：[吴恩达关于大模型的系列课程](https://learn.deeplearning.ai)**

**双语字幕视频地址：[吴恩达 x OpenAI的Prompt Engineering课程专业翻译版](https://www.bilibili.com/video/BV1Bo4y1A7FU/?share_source=copy_web)**

**中英双语字幕下载：[《ChatGPT提示工程》非官方版中英双语字幕](https://github.com/GitHubDaily/ChatGPT-Prompt-Engineering-for-Developers-in-Chinese)**

**视频讲解：[面向开发者的 Prompt Engineering 讲解（数字游民大会）](https://www.bilibili.com/video/BV1PN4y1k7y2/?spm_id_from=333.999.0.0)**

**目录结构说明：**

    content：基于原课程复现的双语版代码，可运行的 Notebook，更新频率最高，更新速度最快。
    
    docs：文字教程版在线阅读源码，适合阅读的 md。
    
    figures：图片文件。
    
    pdf-code：文字教程版源码，适合阅读的 Notebook。

## 内容大纲

### 一、面向开发者的 Prompt Engineering

注：吴恩达《ChatGPT Prompt Engineering for Developers》课程中文版

**目录：**

1. 简介 Introduction @邹雨衡
2. Prompt 的构建原则 Guidelines @邹雨衡
3. 如何迭代优化 Prompt Itrative @邹雨衡
4. 文本总结 Summarizing @玉琳
5. 文本推断 Inferring @长琴
6. 文本转换 Transforming @玉琳
7. 文本扩展 Expanding @邹雨衡
8. 聊天机器人 Chatbot @长琴
9. 总结 @长琴

  附1 使用 ChatGLM 进行学习 @宋志学
  
 ### 二、搭建基于 ChatGPT 的问答系统
 
 注：吴恩达《Building Systems with the ChatGPT API》课程中文版
 
 **目录：**

1. 简介 Introduction @Sarai
2. 模型，范式和 token Language Models, the Chat Format and Tokens @仲泰
3. 检查输入-分类 Classification @诸世纪
4. 检查输入-监督 Moderation @诸世纪
5. 思维链推理 Chain of Thought Reasoning @万礼行
6. 提示链 Chaining Prompts @万礼行
7. 检查输入 Check Outputs @仲泰
8. 评估（端到端系统）Evaluation @邹雨衡
9. 评估（简单问答）Evaluation-part1 @陈志宏、邹雨衡
10. 评估（复杂问答）Evaluation-part2 @邹雨衡
11. 总结 Conclusion @Sarai
  
 ### 三、使用 LangChain 开发应用程序
 
 注：吴恩达《LangChain for LLM Application Development》课程中文版
 
 **目录：**

1. 简介 Introduction @Sarai
2. 模型，提示和解析器 Models, Prompts and Output Parsers @Joye
3. 存储 Memory @徐虎
4. 模型链 Chains @徐虎
5. 基于文档的问答 Question and Answer @苟晓攀
6. 评估 Evaluation @苟晓攀
7. 代理 Agent @Joye
8. 总结 Conclusion @Sarai

 ### 四、使用 LangChain 访问个人数据

 注：吴恩达《LangChain Chat with Your Data》课程中文版

 **目录：**

1. 简介 Introduction @Joye
2. 加载文档 Document Loading @Joye
3. 文档切割 Document Splitting @苟晓攀
4. 向量数据库与词向量 Vectorstores and Embeddings @刘伟鸿、仲泰
5. 检索 Retrieval @刘伟鸿
6. 问答 Question Answering @邹雨衡
7. 聊天 Chat @高立业
8. 总结 Summary @高立业

### 五、使用 Gradio 搭建生成式 AI 应用

注：吴恩达《Building Generative AI Applications with Gradio》课程中文版

 **目录：**

1. 简介 Introduction @韩颐堃
2. 图像总结应用 Image Captioning App @宋志学
3. NLP 任务接口 NLP Tasks Interface @宋志学
4. 图像生成应用 Image Generation App @小饭同学
5. 描述与生成游戏 Describe and Generate Game @小饭同学
6. 与任意 LLM 交流 Chat with Any LLM @韩颐堃
7. 总结 Conclusion @韩颐堃

### 六、评估改进生成式 AI

注：吴恩达《Evaluating and Debugging Generative AI》课程中文版

 **目录：**

1. 简介 Introduction @高立业
2. 测量权重和偏差 W&B @陈逸涵
3. 训练一个扩散模型 Traing a Diffusion Model with W&B @苟晓攀
4. 评估扩散模型 Evaluating Diffusion Models @苟晓攀
5. 评估与追踪 LLM LLM Evaluation and Tracing with W&B @陈逸涵
6. 微调语言模型 Finetuing a Language Model  @高立业
7. 总结 Conclusion @高立业
  
### 七、微调大语言模型

注：吴恩达《Finetuning Large Language Model》课程中文版

**目录：**

1. 简介 Introduction @韩颐堃
2. 为什么要微调 Why Finetune @宋志学
3. 微调的应用场景 Where Finetuning Fits in @陈逸涵
4. 指令微调 Instruction Tuning @韩颐堃
5. 数据处理 Data Proparation @高立业
6. 训练过程 Training Process @王熠明
7. 评估迭代 Evalution and Itration @邓宇文
8. 入门注意事项 Considration on Getting Started Now @韩颐堃
9. 总结 Conclusion @韩颐堃

### 配套视频

双语字幕视频：[吴恩达 x OpenAI的Prompt Engineering课程专业翻译版](https://www.bilibili.com/video/BV1Bo4y1A7FU/?share_source=copy_web) @万礼行

## 致谢

**核心贡献者**

- [邹雨衡-项目负责人](https://github.com/logan-zou)（Datawhale成员-对外经济贸易大学研究生）
- [长琴-项目发起人](https://yam.gift/)（内容创作者-Datawhale成员-AI算法工程师）
- [玉琳-项目发起人](https://github.com/Sophia-Huang)（内容创作者-Datawhale成员）
- [徐虎-教程编撰者](https://github.com/xuhu0115)（内容创作者-Datawhale成员）
- [刘伟鸿-教程编撰者](https://github.com/Weihong-Liu)（内容创作者-江南大学非全研究生）
- [Joye-教程编撰者](https://Joyenjoye.com)（内容创作者-数据科学家）
- [高立业](https://github.com/0-yy-0)（内容创作者-DataWhale成员-算法工程师）
- [魂兮](https://github.com/wisdom-pan)（内容创作者-前端工程师）
- [宋志学](https://github.com/KMnO4-zx)（内容创作者-Datawhale成员）
- [韩颐堃](https://github.com/YikunHan42)（内容创作者-Datawhale成员）
- [陈逸涵](https://github.com/6forwater29) (内容创作者-Datawhale意向成员-AI爱好者)
- [仲泰](https://github.com/ztgg0228)（内容创作者-Datawhale成员）
- [万礼行](https://github.com/leason-wan)（内容创作者-视频翻译者）
- [王熠明](https://github.com/Bald0Wang)（内容创作者-Datawhale成员）
- [邓宇文](https://github.com/GKDGKD)（内容创作者-Datawhale成员）
- [小饭同学](https://github.com/xinqi-fan)（内容创作者）
- [诸世纪](https://github.com/very-very-very)（内容创作者-算法工程师）
- [Zhang Yixin](https://github.com/YixinZ-NUS)（内容创作者-IT爱好者）
- Sarai（内容创作者-AI应用爱好者）


**其他**

1. 特别感谢 [@Sm1les](https://github.com/Sm1les)、[@LSGOMYP](https://github.com/LSGOMYP) 对本项目的帮助与支持；
2. 感谢 [GithubDaily](https://github.com/GitHubDaily) 提供的双语字幕；
3. 如果有任何想法可以联系我们 DataWhale 也欢迎大家多多提出 issue；
4. 特别感谢以下为教程做出贡献的同学！

<a href="https://github.com/datawhalechina/prompt-engineering-for-developers/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=datawhalechina/prompt-engineering-for-developers" />
</a>

Made with [contrib.rocks](https://contrib.rocks).

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=datawhalechina/prompt-engineering-for-developers&type=Date)](https://star-history.com/#datawhalechina/prompt-engineering-for-developers&Date)


## 关注我们

<div align=center>
<p>扫描下方二维码关注公众号：Datawhale</p>
<img src="figures/qrcode.jpeg" width = "180" height = "180">
</div>
Datawhale 是一个专注于数据科学与 AI 领域的开源组织，汇集了众多领域院校和知名企业的优秀学习者，聚合了一群有开源精神和探索精神的团队成员。微信搜索公众号Datawhale可以加入我们。

## LICENSE
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey" /></a><br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议</a>进行许可。

from metagpt.actions import Action
from writeDirecotory import WriteDirecotory
from typing import Dict
import asyncio


class WriteContent(Action):

    def __init__(self, name: str = "", directory: str = "", language: str = "Chinese", *args, **kwargs):
        super().__init__(**kwargs)
        self.language = language
        self.directory = directory

    async def run(self, topic: str, *args, **kwargs) -> str:
        COMMON_PROMPT = """
        You are now a seasoned technical professional in the field of the internet. 
        We need you to write a technical tutorial with the topic "{topic}".
        """
        CONTENT_PROMPT = COMMON_PROMPT + """
        Now I will give you the module directory titles for the topic. 
        Please output the detailed principle content of this title in detail. 
        If there are code examples, please provide them according to standard code specifications. 
        Without a code example, it is not necessary.

        The module directory titles for the topic is as follows:
        {directory}

        Strictly limit output according to the following requirements:
        1. Follow the Markdown syntax format for layout.
        2. If there are code examples, they must follow standard syntax specifications, have document annotations, and be displayed in code blocks.
        3. The output must be strictly in the specified language, {language}.
        4. Do not have redundant output, including concluding remarks.
        5. Strict requirement not to output the topic "{topic}".
        现在我将为您提供该主题的模块目录标题。
        请详细输出此标题的详细原理内容。
        如果有代码示例，请按照标准代码规范提供。
        没有代码示例则不需要提供。

        该主题的模块目录标题如下：
        {directory}

        严格按照以下要求限制输出：
        1. 遵循Markdown语法格式进行布局。
        2. 如果有代码示例，必须遵循标准语法规范，具备文档注释，并以代码块形式显示。
        3. 输出必须严格使用指定语言{language}。
        4. 不得有冗余输出，包括总结性陈述。
        5. 严禁输出主题"{topic}"。
        """
        prompt = CONTENT_PROMPT.format(
            topic=topic, language=self.language, directory=self.directory)
        return await self._aask(prompt=prompt)


# dic = """{"title": "MySql教程", "directory": [{"介绍": ["什么是MySql", "MySql的优势"]}, {"安装与配置": ["下载MySql", "安装步骤", "配置MySql"]} , {"基本操作": ["连接数据库", "创建数据库", "创建表", "插入数据", "查询数据", "更新数据", "删除数据"]} , {"高级操作": ["使用索引", "事务处理", "备份与恢复", "性能优化"]}]}"""
# wd = WriteDirecotory()
# dic = asyncio.run(wd.run("MySql"))

# w = WriteContent("WriteDirecotory", dic, "Chinese")
# t = asyncio.run(w.run("MySql"))

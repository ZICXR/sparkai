from metagpt.actions import Action
from typing import Dict
import asyncio
from metagpt.utils.common import OutputParser

class WriteDirecotory(Action):
    def __init__(self, name: str = "", language: str = "Chinese", *args, **kwargs):
        super().__init__(**kwargs)
        self.language = language

    async def run(self, topic: str, *args, **kwargs) -> Dict: # 返回字典格式
        COMMON_PROMPT = """
        You are now a seasoned technical professional in the field of the internet. 
        We need you to write a technical tutorial with the topic "{topic}".
        """  # 命令模板
        DIRECTORY_PROMPT = COMMON_PROMPT + """
        Please provide the specific table of contents for this tutorial, strictly following the following requirements:
        1. The output must be strictly in the specified language, {language}.
        2. Answer strictly in the dictionary format like {{"title": "xxx", "directory": [{{"dir 1": ["sub dir 1", "sub dir 2"]}}, {{"dir 2": ["sub dir 3", "sub dir 4"]}}]}}.
        3. The directory should be as specific and sufficient as possible, with a primary and secondary directory.The secondary directory is in the array.
        4. Do not have extra spaces or line breaks.
        5. Each directory title has practical significance.
        """
        prompt = DIRECTORY_PROMPT.format(topic=topic, language=self.language)
        resp = await self._aask(prompt=prompt)
        # print(resp)
        return OutputParser.extract_struct(resp, dict)


# w = WriteDirecotory("WriteDirecotory", "Chinese")
# asyncio.run(w.run("MySql"))
import re
import asyncio
from metagpt.actions import Action
from metagpt.logs import logger
import subprocess


class SimpleRunCode(Action):  # 本行为不使用LLM
    name: str = "SimpleRunCode"

    async def run(self, code_text: str):
        result = subprocess.run(["python3", "-c", code_text], capture_output=True, text=True)  # 运行 code_text代码
        code_result = result.stdout  # 获取执行结果
        logger.info(f"{code_result=}")  # 输出
        return code_result





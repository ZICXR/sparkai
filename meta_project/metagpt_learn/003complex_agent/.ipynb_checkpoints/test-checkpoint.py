import asyncio
from metagpt.logs import logger
from tutorialAssistant import TutorialAssistant

async def main():
    msg = "Mysql 教程"
    role = TutorialAssistant()
    logger.info(msg)
    result = await role.run(msg)
    logger.info(result)

asyncio.run(main())

# /mnt/workspace/MetaGPT/data/tutorial_docx/


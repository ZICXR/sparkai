from simpleCoder import SimpleCoder
from  simpleWriteCode import SimpleWriteCode
import asyncio
from metagpt.logs import logger


async def main():
    msg = "write a function that calculates the sum of a list"
    role = SimpleCoder()
    logger.info(msg)
    result = await role.run(msg)
    logger.info(result)

asyncio.run(main())




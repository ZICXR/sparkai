import asyncio
from metagpt.subscription import SubscriptionRunner
from metagpt.roles import Searcher
from metagpt.schema import Message

async def trigger():
    while True:
        yield Message("the latest news about OpenAI")
        await asyncio.sleep(3600 * 24)

async def callback(msg: Message):
    print(msg.content)
async def main():
    pb = SubscriptionRunner()
    await pb.subscribe(Searcher(), trigger(), callback)
    await pb.run()

asyncio.run(main())
from metagpt.logs import logger
from metagpt.roles.role import Role, RoleReactMode
from metagpt.schema import Message
from simpleWriteCode import SimpleWriteCode


class SimpleCoder(Role):
    name: str = "Alice"   # 名字
    profile: str = "SimpleCoder"  # 角色

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([SimpleWriteCode])  # 配置写代码的行为
    # 配备好之后，我们定义的行动SimpleWriteCode就会被加入到代办self.rc.todo中

    async def _act(self) -> Message:  # 返回结果
        # 格式化字符串（f-string）
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        todo = self.rc.todo            # todo will be SimpleWriteCode()
        # 要求我们的智能体来执行这个动作，也就是我们需要调用todo.run()方法

        msg = self.get_memories(k=1)[0]   # find the most recent messages

        code_text = await todo.run(msg.content)
        msg = Message(content=code_text, role=self.profile, cause_by=type(todo))

        return msg


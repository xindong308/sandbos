import os
from asyncio import timeout

from dotenv import load_dotenv
from e2b import Sandbox

load_dotenv()
E2B_API_KEY = os.getenv('E2B_API_KEY')
E2B_API_URL = os.getenv('E2B_API_URL')
E2B_DOMAIN = os.getenv('E2B_DOMAIN')
E2B_TEMPLATE = os.getenv('E2B_TEMPLATE')

#   sandbox.connect() #连接已有沙箱
#   sandbox.create_sandbox() #创建沙箱
#   sandbox.get_sandbox() #获取沙箱
#   sandbox.delete_sandbox() #删除沙箱
def demo01():
    sandbox = Sandbox.create(
        template=os.environ["E2B_TEMPLATE"],
        api_key=os.environ["E2B_API_KEY"],
        api_url=os.environ["E2B_API_URL"],
        domain=os.environ["E2B_DOMAIN"],
        timeout=300,
    )
    try:
        # 在沙箱中执行 Shell 命令
        result = sandbox.commands.run('echo "Hello from Base"')
        print(result.stdout.strip())

        # 写入文件
        path = "/home/user/workspace/hello.txt"
        sandbox.files.write(path, "Hello from file\n")

        # 通过命令读取文件
        result = sandbox.commands.run(f"cat {path}")
        print(result.stdout.strip())

        # 通过文件接口读取文件
        content = sandbox.files.read(path)
        print(content.strip())
    finally:
        # 操作完成或发生异常时，释放沙箱
        sandbox.kill()

if __name__ == '__main__':
    demo01()

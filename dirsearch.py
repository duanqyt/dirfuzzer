import sys

from lib.core.settings import OPTIONS_FILE
from lib.parse.config import ConfigParser

# 提示Python环境要求
if sys.version_info < (3, 12):
    sys.exit('Sorry, Python < 3.12 is not supported.')


def main():
    # 加载配置
    config = ConfigParser()
    config.read(OPTIONS_FILE)

    # 判断本地环境是否满足依赖，不满足就安装
    if config.getboolean("[options]", "check-dependencies"):    # 默认给的是True
        try:
            # 进入检测本地依赖
            pass
        except:
            # 处理异常
            pass
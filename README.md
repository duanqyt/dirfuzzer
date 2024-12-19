# dirfuzzer

> 仅仅就是把dirsearch抄一遍，其他的加点儿自己想法重写一遍。单纯为了学习。

1. dirsearch.py
   1. 程序入口
   2. argparse解析命令行参数
2. lib/core/arguments.py
   1. 定义并解析命令行参数，以便主程序了解用户输入的配置和选项
   2. 处理异常情况和无效参数
3. lib/core/logger.py
   1. 记录日志
   2. 输出到终端、报告
4. lib/core/dictionary.oy
   1. 加载用户指定的字典文件
   2. 提供字典迭代处理逻辑，用于生成URL
5. lib/core/queue.oy
   1. 实现扫描任务队列
   2. 将字典的路径组织位任务队列，以便worker现成使用
6. lib/controller/controller.py
   1. 主控制器，接受主程序参数和配置
   2. 初始化线程池并启动扫描任务
   3. 收集、处理、输出扫描结果
7. lib/connection/requester.py
   1. 发送http请求
   2. 实现重试逻辑、超时、错误处理、用户代理伪装等
8. lib/core/fuzzer.py
   1. 核心逻辑模块儿，注意从任务队列取出路镜
   2. 使用requester模块发送请求分析响应
   3. 负责结果的收集和过滤（404等）
9. lib/core/report.py
   1. 出报告
   2. 格式化输出
10. lib/utils/    # 存放工具函数，如日志处理、URL格式化等
11. lib/core/progress.py   # 实现扫描进度显示

> 那么，捋清楚功能之后第一件事儿就是从哪个文件开始抄，在gpt的引导下，第一个文件还是抄dirsearch.py吧，先弄清楚程序怎么调的。

`dirsearch.py` → `lib/core/arguments.py` → `lib/controller/controller.py` → `lib/core/dictionary.py` → `lib/core/queue.py` → `lib/connection/requester.py` → `lib/core/fuzzer.py`

# dirsearch.py

**dirsearch.py主要干了这几件事儿：**

* 先验证下python版本符合要求，3.12下直接报错退出
* 有个忽略警告，不知道啥东西，先忽略
* main函数
  * 加载配置文件,所以创建了lib/core/settings.py，给OPTIONS_FILE="options.ini",进而创建options.py。
  * 接着自然就是读取配置文件，为了定义读取功能ConfigParser()得创建个lib.parse.config 并编写 ConfigParser，然后建立test.lib.parse并编写test_config。
  *

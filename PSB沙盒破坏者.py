#这是一个初中生Turbowarp转python上手就写代码的结果,有很多问题和搞笑的地方请不要和我说,自己偷笑即可,有些代码确实有点招笑了:P
'''
项目名: Project Sandbox Breaker(PSB)项目沙盒破坏者
项目核心功能: 突破 TurboWarp/在线编辑器的沙盒限制
适用人群:
  前提:拥有扩展功能的项目编辑器(比如TW)
  需要底层功能的图形化玩家
  想突破限制的 Scratch 高级玩家
  
用法:
以turbowarp为例使用官方扩展库内的WebSocket扩展最方便
在改程序启动的前提下用前面提到的扩展连接ws://127.0.0.1:55555/
如果连接成功应该会收到消息"连接成功!"

指令发送格式:{"指令名":["数据1","数据2","..."]}
目前已经有的指令:
  {"信息_性能":[]}
  {"信息_系统":[]}
  {"刷新":[]}
  {"调用_cmd":["(要写的命令)"]}
(需要注意的是如果发送的指令不正确则会让客户端断开联机,这防止有其他程序占用端口,即使这几乎不可能)
'''
'''
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\\  =  /0
                    ___/‘---’\\___
                  .‘ \\|       |/ ‘.
                 / \\\\|||  :  |||// \\\\
                / _||||| -:- |||||- \\\\
               |   | \\\\\\  -  /// |   |
               | \\_|  ‘‘\\---/‘‘  |_/ |
               \\  .-\\__  ‘-‘  ___/-. /
             ___‘..‘  /--.--\\  ‘..‘___
          ."" ‘<  ‘.___\\_<|>_/___.’ >’ "".
         | | :  ‘- \\‘.;‘\\ _ /‘;.’/ - ’ : | |
         \\  \\ ‘_.   \\_ __\\ /__ _/   .-’ /  /
     =====‘-.____‘.___ \\_____/___.-’___.-’=====
                       ‘=---=‘
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
           佛祖保佑   永无BUG
          代码无错   运行顺利
          Ctrl+C/V   永不宕机
         无人抄袭      遇事自清
        我写的不是Bug，是未记载的特性
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
夫代码之形，若鬼神之作，观之诡谲，然能奔逸绝尘。但见荧屏无赤错，何须雕琢问玄机？——能跑便是天道，报错再修未迟。----VovaLU.QWQ沃瓦
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<<<MTI>>>
Copyright (c) 2025~2026 VovaLU.QWQ沃瓦

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

作者: VovaLU.QWQ沃瓦
邮箱: vova1525@foxmail.com
'''

# ------------------------------导入和初始化------------------------------
import GPUtil
import platform
import random
import string
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import psutil
import threading
import time
import subprocess
import sys
import requests
import json
import os
import threading

# ------------------------------一些打包的类------------------------------
def 获取性能占用():
  开始耗时 = time.time()
  CPU性能占用 = psutil.cpu_percent(interval=0.1)
  内存占用 = psutil.virtual_memory().percent
  gpus = GPUtil.getGPUs()  # 这里获取的就是所有GPU
  
  GPU数量 = len(GPUtil.getGPUs())
  GPU组 = []
  GPU显存组 = []
  for gpu in gpus:
    # 核心占用
    GPU组.append(f"{gpu.load*100:.1f}%")
    
    # 显存信息
    显存信息 = {
    "已用MB": gpu.memoryUsed,
    "总共MB": gpu.memoryTotal,
    "占用率": f"{gpu.memoryUtil*100:.1f}%"
    }
    GPU显存组.append(显存信息)
  结束耗时 = time.time()
  总耗时 = 结束耗时 - 开始耗时
  if GPU数量 != 0:
    数据 = {
      "计算耗时":f"{总耗时}",
      "CPU":f"{CPU性能占用}",
      "内存":f"{内存占用}",
      "独立显卡?": True,
      "GPUlen":f"{GPU数量}",
      "GPU_占用": GPU组,
      "GPU_显存占用": GPU显存组
    }
  else:
    数据 = {
      "计算耗时":f"{总耗时}",
      "CPU":f"{CPU性能占用}",
      "内存":f"{内存占用}",
      "独立显卡?": False, 
    }
  换行json_str = json.dumps(数据, ensure_ascii=False, indent=2)
  数据json_str = json.dumps(数据, ensure_ascii=False)
  print(f"获取系统占用信息:\n{换行json_str}")
  return 数据json_str

def 启动同目录下的程序():
 if os.path.exists("qianduan.exe"):
    info = subprocess.STARTUPINFO()
    info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = 0
    subprocess.run(["./qianduan.exe"])
    sys.exit(0)
 else:
   print("ERROR没有程序")

def 随机串(长度=3):
  """生成指定长度的随机字符串（包含字母和数字）"""
  # 随机选择字符
  字符集 = string.ascii_letters + string.digits  # 大小写字母+数字
  随机串 = ''.join(random.choice(字符集) for _ in range(长度))
  return 随机串

def 运行命令(命令):
  命令参数 = str(命令)
  try:
    subprocess.Popen(命令参数, shell=True)
    print(f"运行命令({命令参数})成功✅")
    return f"运行命令({命令参数})成功✅"
  except Exception as e:
    print(f"运行命令({命令参数})失败!❌")
    print(f"错误:{e}")
    return [f"运行命令({命令参数})失败!❌","错误:{e}"]
    

class 线程函数:     #线程函数(让别的函数跑在子线程)
  def 运行(self, 函数, 线程名字=None):
    if 线程名字 == None:
      线程名字 = f"未命名线程_{随机串(4)}"
    else:
      线程名字 = f"{线程名字}_{随机串(4)}"
    线程变量 = threading.Thread(target=函数, daemon=True, name=线程名字)
    线程变量 .start()
    print(f"由{函数}启动的的线程'{线程名字}'开始运行")
线程 = 线程函数()

class 广播函数:    #广播函数
  def __init__(self):
    self.广播字典 = {}
  
  def 当收到广播(self, 广播名称, 要执行的函数):
    self.广播字典[广播名称] = 要执行的函数
  
  def 广播(self, 广播名称):
      if 广播名称 in self.广播字典:
        self.广播字典[广播名称]()
广播 = 广播函数()

所有实例 = []
class ws_dt:     # ws服务器函数
  def __init__(self, 端口=9000, 处理类=None):
    self.端口 = 端口
    self.处理类 = 处理类
    self.server = None
    self.所有实例 = []  # 存所有客户端实例

  def 客户端连接(self):
    """检测当前是否有客户端连接"""
    return len(self.所有实例) > 0
  
  def 客户端数量(self):
    """获取当前连接的客户端数量"""
    return len(self.所有实例)
  
  def 设置(self, 处理类, 端口=9000):
    """设置服务器参数"""
    self.端口 = 端口
    self.处理类 = 处理类
      
  def 开启(self):  # 改名open→开启
    """启动服务器"""
    
    
    # 动态创建处理类，能访问到ws_dt实例
    外层self = self  # 保存引用，供内部类使用
    
    class 自定义处理类(WebSocket):
      def handleConnected(客户端self):
        外层self.所有实例.append(客户端self)
        客户端self.sendMessage("连接成功！")
        print("有新客户端链接")

      def handleMessage(客户端self):
        # 分解客户端信息
        global 客户端指令, 客户端指令数据
        客户端消息 = 客户端self.data
        存1 = json.loads(客户端消息)
        客户端指令 = list(存1.keys())[0]
        客户端指令数据 = 存1[客户端指令]

        print(f"收到指令{客户端指令}!携带数据:{客户端指令数据}")  # 打印收到的消息
        广播.广播(客户端指令)  # 广播收到的消息
      
      def handleClose(客户端self):
        if 客户端self in 外层self.所有实例:
          外层self.所有实例.remove(客户端self)
        print("有客户端断开连接")
    
    self.server = SimpleWebSocketServer('localhost', self.端口, 自定义处理类)
    print(f"✅ 服务器启动在端口 {self.端口}")
    self.server.serveforever()
  
  def 说话(self, 内容):  # 改名say→说话
    """给所有客户端发消息"""
    for 实例 in self.所有实例:  # 用self.所有实例
      try:
        实例.sendMessage(str(内容))
      except:
        pass  # 发送失败就跳过
    print(f"广播给 {len(self.所有实例)} 个客户端: {内容}")

class 文件:     #管理和下载文件函数
  
  
  def 检查(路径):
    if os.path.exists(str(路径)):
      return True
    else:
      return False
  
  # 检查并创建文件夹
  def 创建文件夹(名称):
    os.makedirs(名称, exist_ok=True)
  
  # 写文件
  def 写(文件路径, 内容):
    """创建并写入文件（直接写入内容）"""
    父目录 = os.path.dirname(文件路径)
    if 父目录:
      os.makedirs(父目录, exist_ok=True)
    
    with open(文件路径, 'w', encoding='utf-8') as f:
      f.write(str(内容))
      
  # 读文件
  def 读(被读取的文件或路径):
    with open(file=被读取的文件或路径, mode="r", encoding="utf-8") as f:
      return f.read()
  # 下载文件
  def 下载_URL(url,path):
    r = requests.get(url, stream=True)
    with open(path, "wb") as f:
      for chunk in r.iter_content(8192):
        f.write(chunk)

# -----------------------------------------------IIII---主程序---IIII----------------------------------------------- 
# ------------------------------程序广播处理响应函数------------------------------
def 示列():
  global 客户端指令, 客户端指令数据
  存1 = 客户端指令
  存2 = 客户端指令数据
  try:
    # 这里写代码
    ws.说话(f'["ok","{存1}"]')
    print(f'["ok","{存1}"]')
  except Exception as e:
    ws.说话(f'["error","{存1}","{e}"]')
    print(f'["error","{存1}","{e}"]')

def cmd():
  global 客户端指令, 客户端指令数据
  存1 = 客户端指令
  存2 = 客户端指令数据
  参数 = str(存2[0])
  结果 = os.system(参数)
  if 结果 == 0:
    ws.说话(f'["ok","{存1}","{参数}"]')
    print(f'["ok","{存1}","{参数}"]')
  else:
    ws.说话(f'["error","{存1}","参数不正确"]')
    print(f'["error","{存1}","参数不正确"]')

def 系统信息():
  global 客户端指令, 客户端指令数据
  存1 = 客户端指令
  存2 = 客户端指令数据
  try:
    系统信息数据 = {
      "os":f"{platform.system()}",
      "version":f"{platform.version()}"
    }
    str = json.dumps(系统信息数据, ensure_ascii=False)
    ws.说话(f'["ok","{存1}",{str}]')
    print(f'["ok","{存1}",{str}]')
  except Exception as e:
    ws.说话(f'["error","{存1}","{e}"]')
    print(f'["error","{存1}","{e}"]')
  
def 刷新():
  global 客户端指令, 客户端指令数据
  存1 = 客户端指令
  存2 = 客户端指令数据
  ws.说话(f'["ok","{存1}"]')
  print(f'["ok","{存1}"]')

def 性能信息():
  global 客户端指令, 客户端指令数据
  存1 = 客户端指令
  存2 = 客户端指令数据
  获取性能占用信息 = 获取性能占用()
  ws.说话(f'["ok","{存1}",{获取性能占用信息}]')
  print(f'["ok","{存1}",{获取性能占用信息}]')

# 最终启动
def 启动所有响应式广播():
  广播.当收到广播("刷新", 刷新)
  广播.当收到广播("信息_性能", 性能信息)
  广播.当收到广播("信息_系统", 系统信息)
  广播.当收到广播("调用_cmd", cmd)
启动所有响应式广播()
# ------------------------------主程序------------------------------
启动同目录下的程序()
# 设置服务器启动端口并启动
ws = ws_dt(端口=55555, 处理类=None)
线程.运行(ws.开启, "ws服务器线程")
time.sleep(0.1)  # 等待服务器启动

while True:
  pass
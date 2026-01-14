#这是一个初中生Turbowarp转python上手就写代码的结果,有很多问题和搞笑的地方请不要和我说,自己偷笑即可,有些代码确实有点招笑了:P
# 采用2空格缩进
版本 = "0.0.7测试开发版"
mc项目名 = "Fuse_Launcher"
留言 = [
  "作为MFX-studio工作室的一员我并不称职,我常忙于我的其他项目却忘记了我所谓后端工程师的职务,在这里说一声抱歉,即使我们成员可能看不到",
  "到底是谁他妈的说启动器好做的?",
  "我们不该为了目标而编程而是为了编程的快乐而编程,这本该是一种享受",
  "作为初学者才发现我已经写了快1000行python代码了,回看走过的路我感到无比自豪(2025/12/22)"
]
# 别以为这个logo有转义问题,r格式化是个好东西
logo = r'''
 __   __                      __  __                       ____    ____    ____      
/\ \ /\ \  __                /\ \/\ \          __         /\  _`\ /\  _`\ /\  _`\    
\ `\`\/'/'/\_\    ___      __\ \ \_\ \  __  __/\_\        \ \ \L\ \ \,\L\_\ \ \L\ \  
 `\/ > <  \/\ \ /' _ `\  /'_ `\ \  _  \/\ \/\ \/\ \        \ \ ,__/\/_\__ \\ \  _ <' 
    \/'/\`\\ \ \/\ \/\ \/\ \L\ \ \ \ \ \ \ \_\ \ \ \        \ \ \/   /\ \L\ \ \ \L\ \
    /\_\\ \_\ \_\ \_\ \_\ \____ \ \_\ \_\ \____/\ \_\        \ \_\   \ `\____\ \____/
    \/_/ \/_/\/_/\/_/\/_/\/___L\ \/_/\/_/\/___/  \/_/  _______\/_/    \/_____/\/___/ 
                           /\____/                    /\______\                      
                           \_/__/                     \/______/                     
                        -----XingHui-studio项目PSB为您服务-----
'''
免责声明 = '''
Project-Sandbox-Breaker (PSB) - 免责声明
本工具由一名初中生开发者编写，旨在技术探索和学习。它允许任意Scratch/TurboWarp项目访问您的操作系统，包括但不限于：
执行任意终端命令（通过调用_cmd指令）
获取系统信息（性能数据、硬件信息等）
独特的MC套件(由其他项目打包而来)
未来可能扩展的文件系统操作,和其他功能

本工具绝不允许用于以下非法目的：
侵入、非法控制他人计算机信息系统
实施信息网络犯罪活动
破坏计算机信息系统功能或数据
窃取、篡改、删除他人计算机信息系统中存储、处理或传输的数据
任何违反上述禁止性规定的行为均构成计算机犯罪，使用者将承担全部法律责任。

作者明确声明不承担因使用或滥用本工具导致的任何直接或间接损害责任，包括但不限于：
系统损坏、数据丢失或隐私泄露
因非法使用而产生的法律纠纷和经济损失
其他任何形式的连带责任

<如继续使用本工具，即表示您已充分阅读、理解并完全接受本免责声明的所有条款。如不同意，请立即停止使用并删除本工具。>
'''

详细信息 = '''
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
  {"信息_性能":[]} 获取系统性能的各各占用(单位:%)
  {"信息_系统":[]} 获取系统信息
  {"刷新":[]} 刷新,一般情况下用于测试后端程序是否卡死或者检测连接
  {"调用_cmd":["(要写的命令)"]} 顾名思义是调用终端的(在0.0.3版本更新了数据返回,支持了多行输入(有BUG))
    # MC特别功能
    {"MC_查服务器":["主机ip","端口(如果有,没有可以不写)"]} 查MC服务器
    {"MC_支持列表":[""]} 查询<MC_获取_参数>的支持列表
    {"MC_获取_参数":["1.21.8(写java我的世界版本)"]}
    {"MC_合成_参数":["0"]} 这个数组数据写0代表测试,暂且我没有考虑如何传入参数
  {"i":[""]} 获取当前的后端版本和作者信息
返回数据的解析:
  ["(状态,一般是ok或者error,或者有较为特殊的r(未知))","使用的指令名","如果有输入数据的话这里会有输入数据","如果有返回数据的话这里会有返回数据.否则不会有这个组"]
(需要注意的是如果发送的指令不正确则会让客户端断开联机,这防止有其他程序占用端口,即使这几乎不可能)

这是一个由VovaLU.QWQ沃瓦制作的用于图形化编程的一个搭配程序"
该程序可以让图形化玩家访问系统的终端命令并且随着用户的提议增加新功能和指令"
联系方式:邮箱vova1525@foxmail.com"
官方qq群:971463342
但请注意：
- 这是一个个人开源项目,本产品非商业产品,但支持被别人项目采用并商用分发只要符合免责声明(反正我是MIT协议,代码你爱咋咋用出事别找我,和我无关)
- 技术支持限于力所能及的范围
- 不保证及时响应或问题解决
'''
详细信息 = 详细信息 + "\n" +f"版本:{版本}"

cmd命令黑名单 = [
  "del",
  "rm",
  "format",
  "chkdsk /f",
  "shutdown /s /t 0",
  "poweroff",
  "reboot",
  "taskkill /f /im",
  "systemreset",
  "cipher /w:",
  "sdelete",
  # 尽可能禁用可能的start安全漏洞
  "start cmd /c",
  "start cmd.exe /c",
  "start cmd /k",
  "start cmd.exe /k"
  ]

支持的MC版本 = [
  "1.13",
  "1.13.1", 
  "1.13.2",
  "1.14",
  "1.14.1",
  "1.14.2",
  "1.14.3",
  "1.14.4",
  "1.15",
  "1.15.1",
  "1.15.2",
  "1.16",
  "1.16.1",
  "1.16.2",
  "1.16.3", 
  "1.16.4",
  "1.16.5",
  "1.17",
  "1.17.1",
  "1.18",
  "1.18.1",
  "1.18.2",
  "1.19",
  "1.19.1",
  "1.19.2",
  "1.19.3",
  "1.19.4",
  "1.20",
  "1.20.1",
  "1.20.2",
  "1.20.3",
  "1.20.4",
  "1.20.5",
  "1.20.6",
  "1.21",
  "1.21.1",
  "1.21.2",
  "1.21.3",
  "1.21.4",
  "1.21.5",
  "1.21.6",
  "1.21.7",
  "1.21.8",
  "1.21.9",
  "1.21.10",
  "1.21.11"
]
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
默认路径 = "~"

默认配置文件字典 = {
  "测试":"测试文本"
}
# ------------------------------导入和初始化------------------------------
from art import text2art
import time
#实现查询服务器和详细数据的库
from mcstatus import JavaServer as java服务器, BedrockServer as 基岩服务器
import GPUtil
import platform
import random
import string
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import psutil
import subprocess
import sys
import requests
import json
import os
import threading

加载初始时间 = time.time()
默认参数 = {
  "游戏名":"测试",
  "游戏目录":"0",
  "资源目录":"0",
  "资源索引版本":"0",
  "用户UUID":"000000000-0000-0000-0000-000000000000",
  # 试玩版访问令牌,离线写0
  "访问令牌":"0",
  # 客户端令牌,离线写0
  "客户端ID":"0",
  # Xbox账户ID,离线写0或者空字符""
  "XboxID":"0",
  # 用户类型,试玩版要写demo,离线是legacy或者mojang,真实账号写msa
  "用户类型":"legacy",
  "游戏目录":"0",
  "jvm虚拟机参数_java.exe路径":"0",
  "jvm虚拟机参数_最大内存":"0",
  "jvm虚拟机参数_标准内存":"0",
  "jvm虚拟机参数_所有jar文件":"0",
  }
# ------------------------------一些打包的类------------------------------
def rizhi(字符串):
  print(f"--日志-- '{字符串}'")
  
def 艺术字(字符串,字体=0):  # 该功能由'ASCII-BOOM项目分支而来'
  # 注意,这个函数可以设置"全局字体"变量让您无需一个个的对这个进行调整如果您没有特殊需求的话
  rizhi(f"收到数据|text:'{字符串}',字体:'{字体}'")
  默认字体库 = [
    # 基础经典
    "standard",    # 标准等宽 0
    "block",       # 方块厚重 1  
    "slant",       # 右斜体 2
    "script",      # 手写体 3
    
    # 恐怖风格
    "bloody",      # 血腥 4
    "ghost",       # 鬼影 5
    "poison",      # 毒液 6
    "ogre",        # 食人魔 7
    
    # 科技特效
    "digital",     # 数码故障 8
    "cyberlarge",  # 赛博大字 9
    "fire",        # 火焰 10
    "water",       # 水流 11
    
    # 3D立体
    "larry3d",     # 3D立体 12
    "isometric1",  # 等角投影 13
    "isometric2",  # 等角投影2 14
    "isometric3",  # 等角投影3 15
    
    # 花式精选
    "fancy1",      # 花式1 16
    "fancy10",     # 花式10 17
    "fancy20",     # 花式20 18
    "fancy30",     # 花式30 19
    
    # 特殊风格
    "varsity",     # 学院风 20
    "twinaps",     # 扭曲恐怖 21
    "earth",       # 大地 22
    "nancyj"       # 诡异花体 23
  ]
  if "自定字体库" in globals():
    字体库 = globals()["自定字体库"]
    rizhi("使用自定字体支持库列表生成")
  else:
    字体库 = 默认字体库
    rizhi("使用默认字体支持库列表生成")
  if "全局字体" in globals():
    字体 = globals()["全局字体"]
    选择字体 = 字体库[字体]
  else:
    选择字体 = 字体库[字体]
  try:
    result = text2art(字符串,font=选择字体)
    rizhi("成功生成艺术字")
    return result
  except Exception as e:
    rizhi(f"出现错误!!!错误:{e}")
    return None

class 服务器查询(): # 由我的世界批量服务器查询分支而来
  # 需要: from mcstatus import JavaServer as java服务器, BedrockServer as 基岩服务器
  # 需要: import json
  # 需要: import threading
  # 需要: import time
  #列表数据格式: ["ip或者主机名","如果有端口在这里写端口"]

  def BE(列表数据):
    超时时长 = 5
    端口_默认_基岩 = "19132"
    if len(列表数据) == 1:
      主机 = 列表数据[0]
      服务器 = f"{主机}:{端口_默认_基岩}"
    elif len(列表数据) == 2:
      主机 = 列表数据[0]
      端口 = 列表数据[1]
      服务器 = f"{主机}:{端口}"
    print(f"合成服务器地址:{服务器}")
    print("基岩方式查询")
    try:
      服务器实例 = 基岩服务器.lookup(f"{服务器}", timeout=超时时长)
      print(f"查询到服务器实例数据")
      # 基岩版只有status方法
      状态 = 服务器实例.status()
      print(f"查询到数据!{状态}")
      print(f"基岩服在线: {状态.players.online}, 延迟: {状态.latency}ms")
      try:
        # 解析_解析对象
        motd_解析 = 状态.motd.parsed
        print(f"对象解析_motd_解析")
        motd_原始 = 状态.motd.raw
        print(f"对象解析_motd_原始")
        玩家_在线 = 状态.players.online
        print(f"对象解析_玩家_在线")
        玩家_最大 = 状态.players.max
        print(f"对象解析_玩家_最大")
        延迟 = 状态.latency
        print(f"对象解析_延迟")
        服务器版本 = 状态.version.name
        print(f"对象解析_服务器版本")
        协议版本 = 状态.version.protocol
        print(f"对象解析_协议版本")
        地图map = 状态.map_name
        print(f"对象解析_地图map")
        游戏模式 = 状态.gamemode
        print(f"对象解析_游戏模式")
        # -----------------------------
        print("对象解析完成,开始解析为json")
        # 解析_解析所有对象数据为json更加方便
        解析json = {
          "m":"BE",
          "player(=)":f"{玩家_在线}",# 玩家在线值
          "player(+)":f"{玩家_最大}",# 玩家最大值
          "motd":f"{motd_原始}",# 原始motd数据
          "ping":f"{延迟}",# 延迟
          "s_v":f"{服务器版本}",# 服务器版本
          "p_v":f"{协议版本}",# 协议版本
          "icon":"",# 基岩没有icon
          "map":f"{地图map}",# 地图map
          "gm":f"{游戏模式}",# 协议版本
        }
        数据 = json.dumps(解析json, ensure_ascii=False)
        打印json = json.dumps(解析json, indent=2, ensure_ascii=False)
        print(f"解析为json成功:/n{打印json}")
        print("[OK]基岩方式查询成功")
        return 数据
      except Exception as e:
        print(f"BE解析失败!{e}")
    except Exception as e:
      print(f"BE获取失败!{e}")
  # _________________分割_________________
  def JE(列表数据):
    超时时长 = 5
    if len(列表数据) == 1:
      主机 = 列表数据[0]
      服务器 = 主机
    elif len(列表数据) == 2:
      主机 = 列表数据[0]
      端口 = 列表数据[1]
      服务器 = f"{主机}:{端口}"
    print(f"合成服务器地址:{服务器}")
    print("java方式查询")
    try:
      # 获取状态信息
      服务器实例 = java服务器.lookup(f"{服务器}", timeout=超时时长)
      print(f"查询到服务器实例数据")
      状态 = 服务器实例.status()
      print(f"查询到状态数据{状态}")
      print(f"服务器在线人数: {状态.players.online}, 延迟: {状态.latency}ms")
      # 此处把q查询给去掉了,大部分服务器不开而且查询很耗时
      try:
        # 解析_解析对象
        motd_解析 = 状态.motd.parsed
        print(f"对象解析_motd_解析")
        motd_原始 = 状态.motd.raw
        print(f"对象解析_motd_原始")
        玩家_在线 = 状态.players.online
        print(f"对象解析_玩家_在线")
        玩家_最大 = 状态.players.max
        print(f"对象解析_玩家_最大")
        延迟 = 状态.latency
        print(f"对象解析_延迟")
        服务器版本 = 状态.version.name
        print(f"对象解析_服务器版本")
        协议版本 = 状态.version.protocol
        print(f"对象解析_协议版本")
        favicon = 状态.raw.get('favicon')
        print(f"对象解析_favicon")
        # -----------------------------
        print("对象解析完成,开始解析为json")
        # 解析_解析所有对象数据为json更加方便
        解析json = {
          "m":"JE",
          "player(=)":f"{玩家_在线}",# 玩家在线值
          "player(+)":f"{玩家_最大}",# 玩家最大值
          "motd":f"{motd_原始}",# 原始motd数据
          "ping":f"{延迟}",# 延迟
          "s_v":f"{服务器版本}",# 服务器版本
          "p_v":f"{协议版本}",# 协议版本
          "icon":f"{favicon}"# URL格式的icon(logo)
        }
        数据 = json.dumps(解析json, ensure_ascii=False)
        打印json = json.dumps(解析json, indent=2, ensure_ascii=False)
        print(f"解析为json成功:/n{打印json}")
        print("[OK]java方式查询成功")
        return 数据
      except Exception as e:
        print(f"JE解析失败!{e}")
    except Exception as e:
      print(f"JE获取失败!{e}")
  # _________________分割_________________
  def 通查(列表数据):
    class 结果容器:  # 临时类当容器
      pass
    
    def JE任务():
      结果容器.JE结果 = 服务器查询.JE(列表数据)  # 存结果
    
    def BE任务():
      结果容器.BE结果 = 服务器查询.BE(列表数据)  # 存结果
    
    JE线程 = threading.Thread(target=JE任务, daemon=True)
    BE线程 = threading.Thread(target=BE任务, daemon=True)
    
    JE线程.start()
    BE线程.start()
    
    for i in range(50):  # 检查50次,5秒
      time.sleep(0.1)
      if hasattr(结果容器, 'JE结果'):  # 检查JE
        return 结果容器.JE结果
      if hasattr(结果容器, 'BE结果'):  # 检查BE
        return 结果容器.BE结果
    
    print("timeout")
    return None

def 获取json(版本):
  print(f"接收到任务:获取json版本信息{版本}")
  URL链 = f"https://bmclapi2.bangbang93.com/version/{版本}/json"
  try:
    response = requests.get(URL链)
    if response.status_code == 200:
      总数据 = json.loads(response.text)
      发送 = 总数据["id"]
      print(f"获取我的世界JSON版本,请求成功\n{发送}")
      return 总数据
    else:
      print(f"获取我的世界JSON版本,请求失败")
  except Exception as e:
    print(f"获取我的世界JSON版本数据出错:{e}")

def 初始化文件夹(路径):        
  global 分类文件夹_主文件夹,分类文件夹_游戏,分类文件夹_JDK,分类文件夹_游戏_实例,分类文件夹_游戏_材质,分类文件夹_游戏_Java库,mc项目名
  try:
    if 路径 == "~":
      分类文件夹_主文件夹 = os.path.join(os.path.expanduser(路径), f"{mc项目名}")
    else:
      if 检测读写权限(路径) == True:
        分类文件夹_主文件夹 = os.path.join(路径, f"{mc项目名}")
      else:
        print("ERROR!路径不合法!")
        return False
    print(f"成功合成主文件夹{分类文件夹_主文件夹}")
    
    分类文件夹_游戏 = os.path.join(分类文件夹_主文件夹, ".minecraft")
    print(f"成功合成游戏文件夹{分类文件夹_游戏}")
    
    分类文件夹_游戏_实例 = os.path.join(分类文件夹_游戏, "versions")
    print(f"成功合成游戏实例文件夹{分类文件夹_游戏_实例}")
    
    分类文件夹_游戏_材质 = os.path.join(分类文件夹_游戏, "assets")
    print(f"成功合成游戏材质文件夹{分类文件夹_游戏_材质}")
    
    分类文件夹_游戏_Java库 = os.path.join(分类文件夹_游戏, "libraries")
    print(f"成功合成游戏Java库文件夹{分类文件夹_游戏_Java库}")
    
    分类文件夹_JDK = os.path.join(分类文件夹_主文件夹, "JDK")
    print(f"成功合成JDK文件夹{分类文件夹_JDK}")
    
    os.makedirs(分类文件夹_主文件夹, exist_ok=True)
    os.makedirs(分类文件夹_游戏, exist_ok=True)
    os.makedirs(分类文件夹_游戏_实例, exist_ok=True)
    os.makedirs(分类文件夹_游戏_材质, exist_ok=True)
    os.makedirs(分类文件夹_游戏_Java库, exist_ok=True)
    os.makedirs(分类文件夹_JDK, exist_ok=True)
    print("所有文件夹创建或检测成功(yes)")
    return True
  except Exception as e:
    print("所有文件夹创建或检测失败(no)")
    return False

def 检测读写权限(路径):
  try:
    # 创建测试文件
    测试文件 = os.path.join(路径, "权限测试.tmp")
    with open(测试文件, "w") as f:
      f.write("test")
    
    # 读取测试文件
    with open(测试文件, "r") as f:
      f.read()
      
    # 删除测试文件
    os.remove(测试文件)
    return True
  except Exception as e:
    print(f"error!路径 {路径} 无读写权限: {e}")
    return False

class 解析():
  def 生成启动参数(字典数据,设置参数=None):
    if 设置参数 != None:
      # 游戏参数
      游戏名 = 设置参数["游戏名"]
      游戏目录 = 设置参数["游戏目录"]
      资源目录 = 设置参数["资源目录"]
      资源索引版本 = 设置参数["资源索引版本"]
      用户UUID = 设置参数["用户UUID"]
      访问令牌 = 设置参数["访问令牌"]
      客户端ID = 设置参数["客户端ID"]
      微软XboxID = 设置参数["XboxID"]
      用户类型 = 设置参数["用户类型"] 
    
      # JVM虚拟机参数
      JavaEXE路径 = 设置参数["jvm虚拟机参数_java.exe路径"]
      Java虚拟机最大内存 = "-Xmx" + 设置参数["jvm虚拟机参数_最大内存"]
      Java虚拟机最小内存 = "-Xms" + 设置参数["jvm虚拟机参数_标准内存"]
    else:
      # 游戏参数
      游戏名 = "0"
      游戏目录 = "0"
      资源目录 = "0"
      资源索引版本 = "0"
      用户UUID = "0"
      访问令牌 = "0"
      客户端ID = "0"
      微软XboxID = "0"
      用户类型 = "0"
      
      # JVM虚拟机参数
      JavaEXE路径 = "0"
      Java虚拟机最大内存 = "-Xmx" + "0"
      Java虚拟机最小内存 = "-Xms" + "0"
    try:
      if 字典数据["minimumLauncherVersion"] >= 21:
        # 解析json
        json解析_ID = 字典数据["id"]
        json解析_启动参数配置 = 字典数据["arguments"]
        json解析_资源索引配置 = 字典数据["assetIndex"]
        json解析_核心文件下载配置 = 字典数据["downloads"]
        json解析_java版本要求配置 = 字典数据["javaVersion"]
        json解析_游戏依赖库配置 = 字典数据["libraries"]
        json解析_游戏主类配置 = 字典数据["mainClass"]
        json解析_最低启动器版本要求 = 字典数据["minimumLauncherVersion"]
        json解析_版本发布时间 = 字典数据["releaseTime"]
        json解析_版本发行版本 = 字典数据["type"]
        # 启动参数
        # 过滤掉字典
        游戏启动参数列表 = []
        for 参数 in json解析_启动参数配置["game"]:
          if isinstance(参数, str):
            游戏启动参数列表.append(参数)  
        
        JVM参数列表 = [
          "java",    # 
          "-Xmx$最大内存$",    # 
          "-Xms$最小内存$",    #
          "-Xss1M",    # 线程栈大小1MB
          "-Xmn256m",    # 新生代内存256MB
          # 对于MC的优化
          "-Dlog4j.formatMsgNoLookups=true",    # 修复代码漏洞
          "-XX:+UseG1GC",    #使用G1垃圾回收器
          "-XX:-UseAdaptiveSizePolicy",    # 禁用自适应大小策略（稳定GC行为）
          "-XX:-OmitStackTraceInFastThrow",  # 保留完整堆栈跟踪（便于调试）
          "-Dfml.ignoreInvalidMinecraftCertificates=True",    # 忽略证书验证问题
          "-Dfml.ignorePatchDiscrepancies=True",    # 忽略版本补丁差异
          "-Dminecraft.launcher.brand=minecraft-launcher",    # 伪装成正版启动器
          "-Dminecraft.launcher.version=2.1.3674",    # 伪装启动器版本
          "-Dnarrator=false",     # 禁用旁白功能
          # 系统伪装
          '-Dos.name="Windows 10"',    #伪装系统
          "-Dos.version=10.0",    # 伪装系统版本
          "原生库路径",    #java原生库路径
          "-cp",    #
          "所有jar",    #所有jar文件
          "主类"    #游戏主类
          ]
        原生库路径 = "-Djava.library.path=" + "./natives"
        # 合并预设的JVM参数
        启动参数列表 = JVM参数列表 + 游戏启动参数列表
        输出2 = 启动参数列表
        print(f"抓取到游戏启动参数并合并jvm配置\n{启动参数列表}\n")
        if 设置参数 != None:
          字符串 = " ".join(启动参数列表)
          # 整理游戏参数配置
          字符串 = 字符串.replace("${auth_player_name}", f"{游戏名}")   #游戏名参数
          字符串 = 字符串.replace("${version_name}", f"{json解析_ID}")   #游戏版本参数
          字符串 = 字符串.replace("${game_directory}", f"{游戏目录}")   #游戏目录参数
          字符串 = 字符串.replace("${assets_root}", f"{资源目录}")   #游戏目录里面的资源目录参数
          字符串 = 字符串.replace("${assets_index_name}", f"{资源索引版本}")   #资源目录的索引版本
          字符串 = 字符串.replace("${auth_uuid}", f"{用户UUID}")   #顾名思义,写个UUID在里面
          字符串 = 字符串.replace("${auth_access_token}", f"{访问令牌}")    #访问令牌,离线写0
          字符串 = 字符串.replace("${clientid}", f"{客户端ID}")   #客户端ID,离线写0,有时也叫做客户端令牌但那是错的
          字符串 = 字符串.replace("${auth_xuid}", f"{微软XboxID}")    #XboxID,离线写0
          字符串 = 字符串.replace("${user_type}", f"{用户类型}")    #用户类型,试玩版要写demo,离线是legacy或者mojang,真实账号写msa
          字符串 = 字符串.replace("${version_type}", f"{json解析_版本发行版本}")   
          # 整理JVM虚拟机配置
          字符串 = 字符串.replace("java", f"{JavaEXE路径}")
          字符串 = 字符串.replace("-Xmx", f"{Java虚拟机最大内存}")
          字符串 = 字符串.replace("-Xms", f"{Java虚拟机最小内存}")
          字符串 = 字符串.replace("原生库路径", f"{原生库路径}")
          字符串 = 字符串.replace("主类", f"{json解析_游戏主类配置}")
          # 字符串 = 字符串.replace("", f"{}")
          # 最终播报
          输出1 = 字符串
          print(f"解析成功:{字符串}")
          return 输出1
        else:
          return 输出2
    except Exception as e:
      print(f"解析失败:{e}")
      return "0"
  
  def 获取并下载所有文件(元组数据):
    try:
      if 元组数据["minimumLauncherVersion"] >= 21:
        # 解析json
        json解析_ID = 元组数据["id"]
        下载_核心文件 = 元组数据["downloads"]["client"]["url"]
        json解析_java版本要求配置 = 元组数据["javaVersion"]
        json解析_游戏依赖库配置 = 元组数据["libraries"]
        文件.下载_URL()
    except Exception as e:
      print(f"解析失败:{e}")

def 初始化文件夹并读取配置():
  global 默认配置文件字典
  配置配置文件字符串 = json.dumps(默认配置文件字典, ensure_ascii=False)
  if 初始化文件夹(默认路径) == True:
    配置目录 = os.path.join(分类文件夹_主文件夹, "配置.json")
    if not 文件.检查(配置目录) == True:
      print("配置文件不存在,初始化中")
      文件.写(配置目录, 配置配置文件字符串)
      print("初始化完毕")
    配置 = 文件.读(配置目录)
    配置 = json.loads(配置)
    return 配置

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
   print("ERROR没有程序(如果该程序不在打包后的项目文件中,那这恰恰表明他正在正常的运行)")

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
    线程变量.start()
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
class 服务器:     # ws服务器函数
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
        客户端self.sendMessage("[OK]连接成功!")
        print("有新客户端连接")

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
    
    self.server = SimpleWebSocketServer('', self.端口, 自定义处理类)
    print(f"[OK]服务器启动在端口 {self.端口}")
    self.server.serveforever()
  
  def 说话(self, 内容):
    """给所有客户端发消息"""
    for 实例 in self.所有实例:  # 用self.所有实例
      try:
        实例.sendMessage(str(内容))
      except:
        pass  # 发送失败就跳过
    print(f"给 {len(self.所有实例)} 个客户端发送内容: {内容}")

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

# -----------------------------------------------IIII---逻辑和响应处理---IIII----------------------------------------------- 
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

def 我的世界服务器查询():
  global 客户端指令, 客户端指令数据
  存1 = 客户端指令
  存2 = 客户端指令数据
  try:
    结果 = 服务器查询.通查(存2)
    if 结果 != None:
      ws.说话(f'["ok","{存1}",{结果}]')
      print(f'["ok","{存1}",{结果}]')
    else:
      ws.说话(f'["error","{存1}","参数不正确"]')
      print(f'["error","{存1}","参数不正确"]')
  except Exception as e:
    ws.说话(f'["error","{存1}","{e}"]')
    print(f'["error","{存1}","{e}"]')
    
def 详情():
  global 客户端指令, 客户端指令数据,版本
  存1 = 客户端指令
  存2 = 客户端指令数据
  详情列表 = [
    "这是一个由VovaLU.QWQ沃瓦制作的用于图形化编程的一个搭配程序",
    " 该程序可以让图形化玩家访问系统的终端命令并且随着用户的提议增加新功能和指令",
    f" 现在的版本:{版本}",
    " 联系方式:邮箱vova1525@foxmail.com",
    " 官方qq群:971463342"
  ]
  信息 = '\n'.join(详情列表)
  try:
    ws.说话(f'["ok","{存1}","{信息}"]')
    print(f'["ok","{存1}","{信息}"]')
  except Exception as e:
    ws.说话(f'["error","{存1}","{e}"]')
    print(f'["error","{存1}","{e}"]')


def cmd():
  try:
    global 客户端指令, 客户端指令数据
    存1 = 客户端指令
    存2 = 客户端指令数据
    命令数组 = 存2
    全部 = ' '.join(存2)   # 全部拼接仅仅用于检测命令是否安全
    是否不安全 = any(s in 全部 for s in cmd命令黑名单) # 检测输入参数是否安全
    计数 = 0
    所有结果 = []
    if 是否不安全 == False:
      for 单行参数 in 命令数组:
        计数 += 1   # 计数
        参数列表 = 单行参数.split()   # 拆分成参数列表
        结果 = subprocess.run(参数列表, shell=False, capture_output=True, text=True, timeout=10)   #运行并存储结果
        返回内容 = 结果.stdout
        返回码 = 结果.returncode
        if 返回码 == 0:
          所有结果.append(f"{返回内容}")
        else:
          所有结果.append(f"错误:{结果.stderr}")
          print(f'["error","{存1}","第{计数}个参数不正确!错误返回:{结果.stderr}"]')
      ws.说话(f'["ok","{存1}","{命令数组}","{所有结果}"]')
      print(f'["ok","{存1}","{命令数组}","{所有结果}"]')
    else:
      ws.说话(f'["error","{存1}","参数不合法!({命令数组})"]')
      print(f'["error","{存1}","参数不合法({命令数组})"]')
  except Exception as e:
    ws.说话(f'["error","出现严重错误!错误内容:{e}"]')
    print(f'["error","出现严重错误!错误内容:{e}"]')

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

def 获取MC支持列表():
  global 客户端指令, 客户端指令数据, 支持的MC版本
  存1 = 客户端指令
  存2 = 客户端指令数据
  try:
    返回 = json.dumps(支持的MC版本, ensure_ascii=False)
    ws.说话(f'["ok","{存1}",{返回}]')
    print(f'["ok","{存1}"","{返回}"]')
  except Exception as e:
    ws.说话(f'["error","{存1}","{e}"]')
    print(f'["error","{存1}","{e}"]')

def 获取MC_json参数():
  global 客户端指令, 客户端指令数据
  存1 = 客户端指令
  存2 = 客户端指令数据
  try:
    数据 = 存2[0]
    返回 = 获取json(数据)
    返回 = json.dumps(返回, ensure_ascii=False)
    ws.说话(f'["ok","{存1}",{返回}]')
    print(f'["ok","{存1}"",{返回}]')
  except Exception as e:
    ws.说话(f'["error","{存1}","{e}"]')
    print(f'["error","{存1}","{e}"]')

def 合成MC_json参数():
  global 客户端指令, 客户端指令数据
  存1 = 客户端指令
  存2 = 客户端指令数据
  try:
    if 存2[0] != "0":
      数据 = 存2[0]
      设置参数 = 存2[1]
      设置参数 = json.loads(设置参数)
      返回 = 解析.生成启动参数(数据, 设置参数)
      ws.说话(f'["ok","{存1}","{返回}"]')
      print(f'["ok","{存1}","{返回}"]')
    else:
      start = time.time()
      ws.说话(f'["i","{存1}","检测到测试用语,正在测试"]')
      数据 = 获取json("1.21.8")
      设置参数 = None
      返回 = 解析.生成启动参数(数据, 设置参数)
      end = time.time()
      end = end - start
      end = f"{end:.6f}"
      结果 = [f"{end}",f"{返回}"]
      ws.说话(f'["ok","{存1}",{结果}]')
      print(f'["ok","{存1}",{结果}]')
  except Exception as e:
    ws.说话(f'["error","{存1}","{e}"]')
    print(f'["error","{存1}","{e}"]')

# 最终启动
def 启动所有响应式广播():
  # 详情,也作为示例使用
  广播.当收到广播("i", 详情)
  # 基础系统套件
  广播.当收到广播("刷新", 刷新)
  广播.当收到广播("信息_性能", 性能信息)
  广播.当收到广播("信息_系统", 系统信息)
  # 高级系统套件
  广播.当收到广播("调用_cmd", cmd) # 让图形化调用CMD,但这是不安全的
  # MC套件
  广播.当收到广播("MC_查服务器", 我的世界服务器查询)
  广播.当收到广播("MC_支持列表", 获取MC支持列表)
  广播.当收到广播("MC_获取_参数", 获取MC_json参数)
  广播.当收到广播("MC_合成_参数", 合成MC_json参数)
启动所有响应式广播()
# ------------------------------主程序------------------------------
print(logo)
print(免责声明) #免责
print(详细信息) #详细信息

初始化文件夹(默认路径)
print(初始化文件夹并读取配置())

启动同目录下的程序()
# 设置服务器启动端口并启动
ws = 服务器(端口=55555, 处理类=None)
线程.运行(ws.开启, "ws服务器线程")
time.sleep(0.1)  # 等待服务器启动

加载完成时间 = time.time()
加载耗时 = 加载完成时间 - 加载初始时间
加载耗时 = round(加载耗时, 5)
print(f"启动耗时:{加载耗时}秒")

开发者模式 = True
while True:
  if 开发者模式 == True:
    客户端消息 = input("开发者模式:TRUE|您可以在没有客户端的情况下直接测试命令\n")
    存1 = json.loads(客户端消息)
    客户端指令 = list(存1.keys())[0]
    客户端指令数据 = 存1[客户端指令]
    广播.广播(客户端指令)
  else:
    pass
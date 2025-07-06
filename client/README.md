# 客户端文档

此目录存储客户端 (用于更新状态/设备状态)

**Windows**:
  - [WinDevice](#WinDevice) *(已安装 Python 推荐)*
  - [Win_Simple](#Win_Simple) *(未安装 Python 推荐)*

**Android**:
  - [AutoxjsScript](#AutoxjsScript) *(无需 Root, 需安装额外软件)*
  - [MagiskService](#MagiskService) *(需 Root)*

**Linux**:
  - [LinuxScriptKDE](#LinuxScriptKDE) *(KDE Python 脚本)*
  - [LinuxScriptHyprland](#LinuxScriptHyprland) *(Hyprland 原生脚本)*

**MacOS**:
  - [AppleShortcuts](#AppleShortcuts)

**CLI** (命令行):
  - [HomeworkDevice](#HomeworkDevice)
  - [CMDConsole](#CMDConsole) *(不建议使用)*
  - [CmdConsoleMulti](#CmdConsoleMulti) *(不建议使用)*

**Others** (其他):
  - [MinecraftScript](#MinecraftScript)
  - [BrowserScript](#BrowserScript)
  - [Zhixuewang](#Zhixuewang)

> [!TIP]
> 欢迎提交 Issue / PR 贡献自己的脚本！

## 快速跳转

- [客户端文档](#客户端文档)
  - [快速跳转](#快速跳转)
- [Windows](#windows)
  - [WinDevice](#windevice)
    - [配置](#配置)
    - [依赖安装](#依赖安装)
    - [自启动](#自启动)
      - [1. PM2](#1-pm2)
      - [2. 自启脚本](#2-自启脚本)
    - [无法获取网易云媒体信息](#无法获取网易云媒体信息)
  - [Win\_Simple](#win_simple)
    - [配置](#配置-1)
    - [使用](#使用)
- [Android](#android)
  - [AutoxjsScript](#autoxjsscript)
    - [软件下载](#软件下载)
    - [配置](#配置-2)
    - [使用](#使用-1)
    - [安卓低版本运行](#安卓低版本运行)
    - [启动时报错](#启动时报错)
  - [MagiskService](#magiskservice)
    - [配置](#配置-3)
    - [使用](#使用-2)
- [Linux](#linux)
  - [LinuxScriptKDE](#linuxscriptkde)
    - [配置](#配置-4)
    - [使用](#使用-3)
  - [LinuxScriptHyprland](#linuxscripthyprland)
    - [配置](#配置-5)
    - [使用](#使用-4)
- [MacOS](#macos)
  - [AppleShortcuts](#appleshortcuts)
    - [FullVer](#fullver)
    - [FastVer](#fastver)
- [CLI](#cli)
  - [HomeworkDevice](#homeworkdevice)
    - [配置](#配置-6)
    - [使用](#使用-5)
  - [CMDConsole](#cmdconsole)
    - [配置](#配置-7)
    - [使用](#使用-6)
  - [CmdConsoleMulti](#cmdconsolemulti)
    - [配置](#配置-8)
    - [使用](#使用-7)
- [Others](#others)
  - [MinecraftScript](#minecraftscript)
    - [Minescript](#minescript)
    - [配置](#配置-9)
    - [使用](#使用-8)
    - [自启](#自启)
  - [BrowserScript](#browserscript)
    - [配置](#配置-10)
  - [Zhixuewang](#zhixuewang)
    - [配置](#配置-11)
    - [使用](#使用-9)
  - [Other repos](#other-repos)

# Windows

## [WinDevice](./win_device.py)

> by: [@wyf9](https://github.com/wyf9)
> Co-authored-by: [@kmizmal](https://github.com/kmizmal)
> Co-authored-by: [@pwnInt](https://github.com/pwnInt) - **^C / 鼠标空闲检测**
> Co-authored-by: [@gongfuture](https://github.com/gongfuture) - **媒体信息获取**
> Co-authored-by: [@LeiSureLyYrsc](https://github.com/LeiSureLyYrsc) - **异步支持**

在 Windows 上自动更新设备状态

依赖: `httpx`, `pywin32`

### 配置

https://github.com/sleepy-project/sleepy/blob/23c14c9a8a32a29a6f60b3d4347e07a5e32e64fc/client/win_device.py#L29-L75

### 依赖安装

```bat
:: 必装依赖，其他为可选 (对应功能需要)
pip install pywin32 requests
```

```bat
:: 媒体状态依赖 (Python <= 3.9)
:: winrt-runtime 仅适用于 python 3.10+ (下面两个 winrt.windows.xxx 的依赖中有, 无需手动安装)
pip install winrt
```

```bat
:: 媒体状态依赖 (Python >= 3.10)
pip install winrt.windows.media.control winrt.windows.foundation
```

```bat
:: 电池状态依赖
pip install psutil
```

### 自启动

有两种方式:

#### 1. PM2

可以使用 PM2 来自启动 / 管理进程 *(搜索: **[Windows PM2 自启](https://www.bing.com/search?q=Windows%20PM2%20%E8%87%AA%E5%90%AF)**)*

> PM2 启动命令参考: `pm2 start python --name sleepywin -- -u win_device.py` <br/>
> *如日志出现乱码请手动设置编码环境变量*

<!-- **(不加 `-u` 参数会导致 `pm2 log` 命令没有输出)** -->

#### 2. 自启脚本

`win_device_autostart.vbs`

自启脚本，使启动后不显示窗口 *(适用于不想用第三方软件托管进程的情况下)*

1. 将 `win_device_autostart.vbs` 放入 `shell:startup` *(开始菜单 -> 启动)* 文件夹
2. 将 `win_device.py` 放入 `%UserProfile%` *(用户主目录)* 文件夹

> [!TIP]
> `shell:startup` 和 `%UserProfile%` 两个文件夹可用运行窗口 (`Win+R`) 打开

### 无法获取网易云媒体信息

> **原因**: 网易云音乐不会设置 SMTC 状态，导致无法获取媒体信息

**解决方法**: 安装 [BetterNCM](https://github.com/std-microblock/BetterNCM)，并安装 `InfLink` 插件，启用其中的 `SMTC` 功能即可正常获取

## [Win_Simple](./Win_Simple/dist/Win_Simple.exe)

> by: [@kmizmal](https://github.com/kmizmal) <br/>
> 源代码: [`./Win_Simple/script.py`](./Win_Simple/script.py)

### 配置

配置文件 (首次打开自动在同级目录下创建): `config.ini`
> `config.ini` 里面的注释写的很详细了，不再提供示例

### 使用

下载后双击 `Win_Simple.exe` 初始化配置文件，然后在同级目录下的 `config.ini` 中填写配置，重新打开即可

> [!TIP]
> 如何开机自启? <br/>
> 创建一个 `Win_Simple.exe` 的快捷方式，然后扔到 `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup` 下即可

# Android

## [AutoxjsScript](./autoxjs_device.js)

> by: [@wyf9](https://github.com/wyf9) <br/>
> Co-authored-by: [@NyaOH-Nahida](https://github.com/NyaOH-Nahida)

使用 [Autox.js](https://web.archive.org/web/20241224233444/https://github.com/kkevsekk1/AutoX) 编写的安卓自动更新状态脚本

### 软件下载

在使用前，请确保**已安装** Autox.js *且*授予**无障碍权限**

**下载**: [aiselp/AutoX (Release)](https://github.com/aiselp/AutoX/releases)

### 配置

https://github.com/sleepy-project/sleepy/blob/e6b77af1e4333ad570983b5bf9ac397cb1d40d7b/client/autoxjs_device.js#L8-L15

### 使用

启动后可点击 Autox.js 右上角的日志图标查看日志

![image](https://files.catbox.moe/x93248.png)

- 当手机息屏 (应用名返回为空) 时视为未在使用
- 当脚本退出时也会更新状态为未在使用 *(不包括 Autox.js 直接停止运行)*

### 安卓低版本运行

如果需要在较低的安卓版本运行，无法安装上面 repo 中的安装包，可以从下载站下载旧版本:

http://www.autoxjs.com/topic/116/autox-js

另外，此链接中的版本运行脚本会报错，可以参考 [这里](https://kimi.moonshot.cn/share/cvnt3n0nnlrcp7r98mmg) 的解决方案

<details>
<summary>点击展开</summary>

*之所以报错是因为 **AutoX.js 旧版本不支持 Javascript 中的模板字符串***

解决方案: **手动将脚本中的模板字符串替换为 `+` 连接的形式**，如:

```js
// Before
console.log(`[sleepyc] ${msg}`);
// After
console.log('[sleepyc] ' + msg);
```

</details>

### 启动时报错

如果可以安装软件, 但首次启动时报错:

<details>
<summary>展开报错示例</summary>

```java
错误信息:
Unable to start activity ComponentInfo{org.autojs.autoxjs.v7/org.autojs.autojs.ui.splash.SplashActivity}: java.lang.SecurityException: Unable to start service Intent { cmp=org.autojs.autoxjs.v7/com.stardust.autojs.IndependentScriptService }: Unable to launch app org.autojs.autoxjs.v7/10361 for service Intent { cmp=org.autojs.autoxjs.v7/com.stardust.autojs.IndependentScriptService }: process is bad
java.lang.RuntimeException: Unable to start activity ComponentInfo{org.autojs.autoxjs.v7/org.autojs.autojs.ui.splash.SplashActivity}: java.lang.SecurityException: Unable to start service Intent { cmp=org.autojs.autoxjs.v7/com.stardust.autojs.IndependentScriptService }: Unable to launch app org.autojs.autoxjs.v7/10361 for service Intent { cmp=org.autojs.autoxjs.v7/com.stardust.autojs.IndependentScriptService }: process is bad
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:3903)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:4049)
	at android.app.servertransaction.LaunchActivityItem.execute(LaunchActivityItem.java:101)
	at android.app.servertransaction.TransactionExecutor.executeCallbacks(TransactionExecutor.java:135)
	at android.app.servertransaction.TransactionExecutor.execute(TransactionExecutor.java:95)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:2443)
	at android.os.Handler.dispatchMessage(Handler.java:106)
	at android.os.Looper.loopOnce(Looper.java:211)
	at android.os.Looper.loop(Looper.java:300)
	at android.app.ActivityThread.main(ActivityThread.java:8348)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:582)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1028)
Caused by: java.lang.SecurityException: Unable to start service Intent { cmp=org.autojs.autoxjs.v7/com.stardust.autojs.IndependentScriptService }: Unable to launch app org.autojs.autoxjs.v7/10361 for service Intent { cmp=org.autojs.autoxjs.v7/com.stardust.autojs.IndependentScriptService }: process is bad
	at android.app.ContextImpl.startServiceCommon(ContextImpl.java:1916)
	at android.app.ContextImpl.startService(ContextImpl.java:1874)
	at android.content.ContextWrapper.startService(ContextWrapper.java:827)
	at com.stardust.autojs.servicecomponents.ScriptServiceConnection$Companion.start(ScriptServiceConnection.kt:129)
	at org.autojs.autojs.ui.splash.SplashActivity.onCreate(SplashActivity.kt:51)
	at android.app.Activity.performCreate(Activity.java:8577)
	at android.app.Activity.performCreate(Activity.java:8541)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1437)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:3884)
	... 12 more

```

</details>

有两种解决方案:

1. 检查系统设置 (如 Google `Play 保护机制` 可能会将其阻止)
2. 找 wyf9 获取旧版安装包

## [MagiskService](./magisk/service.sh)

> by: [@kmizmal](https://github.com/kmizmal)

适用于 Magisk Root 环境的服务脚本

### 配置

[./magisk/config.cfg](./magisk/config.cfg)

https://github.com/sleepy-project/sleepy/blob/7bb1866e8448d921f6161f1200164a19914d9910/client/magisk/config.cfg#L1-L6

> [!TIP]
> 详见 [说明](./magisk/README.md)

### 使用

刷入 [magisk.zip](./magisk/magisk.zip) 并重启即可

# Linux

## [LinuxScriptKDE](./linux_device_kde.py)

> by: [@RikkaNaa](https://github.com/RikkaNaa)

适用于 Linux KDE 桌面环境，且需要系统安装 [kdotool](https://github.com/jinliu/kdotool)

如获取失败则视为未在使用，[变量计时参考](https://github.com/RikkaNaa/sleepy/commit/9d5b4fc2014b725df24304beaa9439a5eb07099b)

### 配置

https://github.com/sleepy-project/sleepy/blob/7fc21380a259247533db76f3a0443fa550fcffec/client/linux_device_kde.py#L18-L28

### 使用

可自行配置本脚本的自启动

> 当进程接收到 `SIGTERM` 信号时将会发送未在使用请求

## [LinuxScriptHyprland](./linux_device_hyprland.sh)

> by: [@inoryxin](https://github.com/inoryxin)

适用于 Linux Hyprland 桌面环境，无需任何依赖，开箱即用

### 配置

https://github.com/sleepy-project/sleepy/blob/7fc21380a259247533db76f3a0443fa550fcffec/client/linux_device_hyprland.sh#L7-L12

### 使用

直接启动即可

> [!TIP]
> 开机自启可自行在 `hyprland.conf` 中配置 <br/>
> **注意: 需要给脚本加上可执行权限 *(`chmod +x`)*, 否则无法运行!**

# MacOS

## [AppleShortcuts](https://github.com/Detritalw/Sleepy-Client-Shortcuts)

> by: [@Detritalw](https://github.com/Detritalw) <br/>
> ***指向外部资源***

### FullVer

[点击链接安装完整版, 支持 Apple Watch, iPhone, iPad, mac...](https://www.icloud.com/shortcuts/aa31f2a5295842939be354285d4e9d14)

### FastVer

[点击链接安装极速版](https://www.icloud.com/shortcuts/eec863215bfb4d7ea7228b6032d1fc6c)

**建议设置自动化 → 打开App → 选择全部App → 设置为不确认，立即执行 → 选择快捷指令为Sleepy Client Shortcuts Fast，即可获得超级好的体验。**

> [!WARNING]
> **IOS 版本 >= 18 才可使用** *(获取前台 App 命令)*
> 这里的链接可能不是最新，[建议到项目内查看](https://www.icloud.com/shortcuts/92fbddbf922343f5b076c828f788371f)

> [!TIP]
> 你可以将该快捷指令设置为操作按钮、控制中心按钮、锁定屏幕按钮、敲击 2 / 3 下背板指令来快捷使用

# CLI

## [HomeworkDevice](./homework_device.py)

> by: [@wyf9](https://github.com/wyf9)

一个手动设置设备状态的示例 ***(不止!)*** *用来展示你的作业进度*

依赖: `requests`

### 配置

https://github.com/sleepy-project/sleepy/blob/2df5d622844816867506adc6d211dc5138fdefc0/client/homework_device.py#L5-L9

### 使用

脚本提供了一些函数:

- `left(num: int)`: 设置剩余作业的数量 (为 `0` 则移除) *[device id: `homework-left`]*
- `writing(name: str)`: 设置正在写的作业 (名称为空字符串则移除) *[device id: `homework-writing`]*

还有一些扩展函数, 可以调用 ~~全部 *(存疑)*~~ 大部分 API:

<details>
<summary>点击展开列表</summary>

> 点击链接跳转 api 文档

- [`query()`](../doc/api.md#query): 查看当前状态 *(未格式化输出)*
- [`status_list()`](../doc/api.md#status-list): 查看可用状态列表 *(未格式化输出)*
- [`metrics()`](../doc/api.md#metrics): 查看统计数据 *(未格式化输出)*
- [`status(stat: int)`](../doc/api.md#status-set): 设置状态
- [`device_set(id: str, show_name: str, msg: str, using: bool = True)`](../doc/api.md#device-set): 设备状态设置
- [`device_remove(id: str)`](../doc/api.md#device-remove): 移除设备状态
- [`device_clear()`](../doc/api.md#device-clear): 清除设备状态
- [`private_mode(private: bool)`](../doc/api.md#device-private-mode): 开关隐私模式
- [`save_data()`](../doc/api.md#storage-save-data): 保存数据到 `data.json`

</details>

那么，如何使用这两个函数呢？

1. 直接使用

使用 `python homework_device.py` 直接打开, 并用执行函数 *(`eval()`)* 的方式发送请求，

如：`left(114514)`

> 如何将多个调用写在一行？可用逗号分隔：`left(114513), writing('五 年 中 考 三 年 模 拟')`

2. 其他程序调用

```py
from time import sleep
from homework_device import left, writing # import

for i in range(114514, 1, -1):
    left(i)
    writing(f'My Homework #{i}')
    sleep(11.45)
```

## [CMDConsole](./cmd_console.py)

> by: [@wyf9](https://github.com/wyf9) <br/>
> *留档，不建议使用*

一个简单的命令行客户端，用于手动更新状态

依赖: `requests`

### 配置

https://github.com/sleepy-project/sleepy/blob/e6b77af1e4333ad570983b5bf9ac397cb1d40d7b/client/cmd_console.py#L14-L21

### 使用

启动脚本, 按照提示操作即可

## [CmdConsoleMulti](./cmd_console_multi.py)

> by: [@wyf9](https://github.com/wyf9) <br/>
> *留档，不建议使用*

[CMDConsole](#cmdconsole) 的旧版本 (可选择多个服务)

### 配置

https://github.com/sleepy-project/sleepy/blob/e6b77af1e4333ad570983b5bf9ac397cb1d40d7b/client/cmd_console_multi.py#L14-L23

### 使用

同上, 多了一步选择服务

# Others

## [MinecraftScript](./mc_script.py)

> by: [@wyf9](https://github.com/wyf9)

依赖: `requests`

一个使用 Minescript mod 在 Minecraft Java 版中上报游戏内信息的脚本

### Minescript

在使用前, 你需要下载 Minescript mod:

Links: [MCMod.cn](https://www.mcmod.cn/class/7594.html) / [Modrinth](https://modrinth.com/mod/minescript) / [Repo](https://github.com/maxuser0/minescript)

> 也可在各大启动器的 Modrinth 源中直接下载

在下载并启动一次后, 打开 `.minecraft/versions/你的版本/minescript/` 目录, 并进行两个操作:

1. 新建 `config.txt`, 内容:

```txt
# Lines starting with "#" are ignored.
# 替换为你的 Python 可执行程序路径
python="C:\Program Files\Python312\python.exe"
```

2. 将 [`mc_script.py`](./mc_script.py) 复制到此目录, 并改名为 `sleepy.py` (也可为其他名字)

### 配置

需要配置两处:

1. 基本服务

https://github.com/sleepy-project/sleepy/blob/e6b77af1e4333ad570983b5bf9ac397cb1d40d7b/client/mc_script.py#L16-L24

2. `app_name` 格式

https://github.com/sleepy-project/sleepy/blob/e6b77af1e4333ad570983b5bf9ac397cb1d40d7b/client/mc_script.py#L116

### 使用

配置完成后重启 Minecraft 进入游戏, 按 `T` *(默认键位, 可能不同)* 打开聊天栏, 并输入: `\sleepy` **(即上面重命名后的文件名去掉 `.py` 后缀)* 回车启动

停止: `\sleepy stop`

### 自启

也可以配置自启, 只需在 `config.txt` 中新增一行:

```txt
autorun[*]=eval 'execute("\\sleepy")'
```

## [BrowserScript](./browser-script-2025.2.10.user.js)

> by: [@nuym](https://github.com/nuym)

在任何支持油猴脚本的浏览器均可使用，*据作者↑说是为了解决 Mac 无法获取窗口标题，遂退而求其次获取浏览器页面（有系统就有浏览器，即有用户脚本）*

- [点击安装 (GitHub raw)](https://github.com/sleepy-project/sleepy/raw/refs/heads/main/client/browser-script.user.js)

- [点击安装 (ghp.ci)](https://ghp.ci/https://raw.githubusercontent.com/sleepy-project/sleepy/main/client/browser-script.user.js)

### 配置

https://github.com/sleepy-project/sleepy/blob/2df5d622844816867506adc6d211dc5138fdefc0/client/browser-script.user.js#L18-L25

## [Zhixuewang](./zhixue.py)

> by: [@NiuFuyu855](https://github.com/NiuFuyu855)

获取你的智学网成绩并展示在页面上

依赖: `requests`, `zhixuewang`

### 配置

https://github.com/sleepy-project/sleepy/blob/73a5e3507c1ca0454bc39c685541d53d228df41f/client/zhixue.py#L38-L47

同时需要添加环境变量:

```env
sleepy_page_zhixue = true
```

### 使用

需要将本脚本放在服务器的 `server.py` 同级目录运行，或编辑 L195-L197:

https://github.com/sleepy-project/sleepy/blob/73a5e3507c1ca0454bc39c685541d53d228df41f/client/zhixue.py#L195-L197

## Other repos

> [!IMPORTANT]
> 在功能 / API 实现上有不同，需要进行修改以与本分支适配 (见 [API #device-set](../doc/api.md#device-set))

- [1812z/sleepy] Android [Macrodroid](https://www.bing.com/search?q=Macrodroid%20download): [(main) `前台应用状态.macro`](https://github.com/1812z/sleepy/blob/main/%E5%89%8D%E5%8F%B0%E5%BA%94%E7%94%A8%E7%8A%B6%E6%80%81.macro)
- [HBWuChang/sleepy] Android Magisk: [(main) `_example/magisk/service.sh`](https://github.com/HBWuChang/sleepy/blob/main/_example/magisk/service.sh) *(详见脚本目录)*
- [HBWuChang/sleepy] Windows Python: [(main) `_example/win.py`](https://github.com/HBWuChang/sleepy/blob/main/_example/win.py)

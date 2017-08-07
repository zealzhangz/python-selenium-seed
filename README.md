# Python+selenium自动化测试种子工程 (https://github.com/zealzhangz/python-selenium-seed)

![测试结果](https://github.com/zealzhangz/python-selenium-seed/blob/master/result.png)

# 简介
最近看到测试的童鞋每次发布后的回归测试忙的前仰后翻,加之想简单研究一下前端的自动化测试。因此从建好的自动化测试工程抽出以下种子工程供大家参考。本工程以GitHub为例子,完整运行该工程需要GitHub账号信息。本人也是newcomer,不正之处还请指教。

## 配置环境
#### 环境配置参考 [Python环境下selenium自动化测试实战](https://zealzhangz.gitbooks.io/python-selenium)

## 开始使用
#### 在/python-selenium-seed/CommonUtil/setttings.py用自己的GitHub账号替换以下字段
```python
# Your username
USER_NAME = "yourusername"

# Default password
PASSWD = "yourpassword"
```
#### 在/python-selenium-seed/CommonUtil/setttings.py替换webdriver本地路径
```python
# Browser web driver path
WEB_DRIVER_PATH = "/yourwebdriverpath/chromedriver"
```
#### 启动
运行以下命令或者直接在IDE中配置运行以下命令,在Intelli IDEA中的配置运行参考上面的配置环境
```sh
python run.py
```

## Contributing

Check [CONTRIBUTING.md](https://github.com/zealzhangz/python-selenium-seed/blob/master/CONTRIBUTING.md)

## History

Check [Release](https://github.com/zealzhangz/python-selenium-seed/releases) list.

## License

[MIT License](http://zealzhangz.mit-license.org/)
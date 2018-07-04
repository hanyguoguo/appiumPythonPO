appium+python+PO 自动化测试框架
====
1.项目概述
-------
python2.7编写，使用目前较为流行的UI自动化测试工具Appium，采用PO设计模型，按照page层、handle层、business层和case层组织框架，使用unittest组织测试用例，HTMLTestRunner生成测试报告，测试过程中错误截图，并生成日志文件。init文件管理元素定位，yaml组织管理appium启动命令，运用了多进程，可实现多台设备同时运行。
###
2.目录简介
-------
* 2.1 base：存放基础封装，如driver。
* 2.2 business：业务层，封装业务相关的方法。
* 2.3 case：存放测试用例，程序入口在test_case.py中。
* 2.4 config：配置相关，包括定位信息和启动命令信息。
* 2.5 handle：操作层，封装对页面元素的操作API。
* 2.6 jpg：错误截图，用例执行过程中，如果失败会截图保存。
* 2.7 log：存放日志文件，多线程运行多个设备，会生成多个日志文件。
* 2.8 page：page层，封装页面元素。
* 2.9 report：测试报告，收集每次运行结果。
* 2.10 untils： 公共的工具模块。


3.效果展示图
-------
整体结构
###
![](https://github.com/hanyguoguo/appiumPythonPO/blob/master/img/tree.png)

控制台展示
###
![](https://github.com/hanyguoguo/appiumPythonPO/blob/master/img/workbench.png)

测试日志
###
![](https://github.com/hanyguoguo/appiumPythonPO/blob/master/img/testlog.png)

测试报告
###
![](https://github.com/hanyguoguo/appiumPythonPO/blob/master/img/testreport.png)

4、不足和优化
-------
日志和报告部分需要进一步优化；脚本入口目前在case文件中，可封装成启动引擎，从case中分离出来；设备的管理需要进一步优化，如通过无线连接设备。等

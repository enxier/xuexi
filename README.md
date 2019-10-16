### 关于自动学习

修改自[Alivon](https://github.com/Alivon)/[Panda-Learning](https://github.com/Alivon/Panda-Learning)自动学习，为本人python编程习作，不承担任何法律后果。

#### 特点：

1. 通过帐户密码和扫描二维码两种方式登陆。
2. 记录学习内容，不重复学习。
3. 模拟人的操作方式，单线程、显示网页、多种积分和点点通查询方式、每个网页学习时长随机、网页随机滑动等，防止被封号。
4. 自动打开网页学习，集满25个积分和24个点点通后，自动结束学习。


### 如何自动学习

首先下载安装Chrome浏览器，https://www.google.cn/chrome/index.html

然后下载相对版本的chromedriver，http://chromedriver.storage.googleapis.com/index.html

最后下载pandalearning.exe，把它和chromedriver放在相同的目录中。

点击pandalearning.exe开始学习。

### 关于手动输入验证码

第一次运行，根据提示填写用户标记名，选择保存用户信息，然后根据提示输入钉钉帐户名和密码。

下次运行程序，填写你的用户标记名，会自动读取并填写钉钉帐户名和密码。

由于没有实现自动识别验证码，需要手动输入验证码，并点击提交。

### 关于扫码登录

也支持扫码登录。不管提示，连续两次回车，打开二维码，用手机学习强国扫码授权，进行学习。

### 关于多线程学习

最新版本增加多线程学习模式（默认为单线程学习，防止封号，不怕封号的，可以多线程学习），增加两个参数，是否显示窗口（ hidden 或 show ）和多线程学习（ single 或 multithread ）。

#### 开启方法：

在命令行中执行pandalearning.exe时，增加两个参数。

##### 多线程，不显示窗口

> pandalearning.exe multithread hidden

##### 多线程，显示窗口（默认）

> pandalearning.exe multithread

##### 单线程（默认），显示窗口（默认）

> pandalearning.exe 
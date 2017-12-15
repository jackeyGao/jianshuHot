# jianshuHot

Scrapy抓取简书热门生成电子书发送到Kindle


[简书](http://www.jianshu.com)是个学习的[~~好网站~~](https://www.zhihu.com/question/263977474)， 我大多只关注首页上的人们文章， 但是最近因为忙错过了很多首页上的文章，所以有了想法把每天的热门top生成mobi推送到kindle。这样在地铁上也能快速翻完.

环境准备:

- 一台主机(需要联网)
- Gitbook
- calibre(Gitbook 依赖calibre的`ebook-convert`)
- Python2.7.9(calibre 需要`python2.7.9`)
- 项目地址:  **[jianshuHot](https://github.com/jackeyGao/jianshuHot)**

## 关于calibre安装
```bash
sudo -v && wget -nv -O- https://raw.githubusercontent.com/kovidgoyal/calibre/master/setup/linux-installer.py | sudo python -c "import sys; main=lambda:sys.stderr.write('Download failed\n'); exec(sys.stdin.read()); main()"
```

官网文档提供的安装脚本看似简单， 执行之后也可以安装使用了， 但是gitbook调用`ebook-convert`时候会报错， 这个地方报错应该是QT的错误(至少我遇到的是, 具体错误信息忘记截图了)如果遇到此错误直接安装QT pyQT即可. [calibre 安装页面](http://calibre-ebook.com/download_linux)有依赖表

## Gitbook 安装

需要安装`nodejs`和`npm`然后执行`npm install -g gitbook-cli`

## 安装jianshuHot

需要强调的是此部分需要解决大量的依赖,

**`scrapy`**所依赖的python包很多， 而且这些依赖的python大多需要一些系统库， 必要的时候需要`apt-get`、`yum`安装一下, 如`python-devel` `libffi-devel` `libxml-devel`等....

**`peewee`** (数据库ORM)要`mysql-devel`， 以上举例都是已知的， 这是在我部署之后写的， 部署的过程没有详细记录， 现在只能靠回忆来写本章节.

```bash
$ git clone https://github.com/jackeyGao/jianshuHot
$ cd jianshuHot
$ pip install -r requirements.txt
```

## 初始化程序

```bash
$ sh init.sh
```

## 邮件配置

这里发送邮件使用的[sendEmail](http://caspian.dotconf.net/menu/Software/SendEmail/), [下载地址](http://caspian.dotconf.net/menu/Software/SendEmail/) . 解压后把解压的`sendEmail`重命名到`/usr/local/bin/sendEmail`理论上都能安装成功， 这个是免编译的， 只需要机器上安装了`perl`

然后修改start.sh 邮箱配置， 写成你自己163邮箱， 也可以用其他品牌邮箱， 如果你用其他品牌别忘了改下`smtp.163.com`, 改成相应的smtp服务器即可.

**注意:** 无论你用哪个邮箱都必须把此邮箱账号加入亚马逊**`已认可的发件人电子邮箱列表`**， 确保发送的文档能到达亚马逊Cloud

```bash
$ vim start.sh
....
YOURKINDLE_MAIL_ADDRESS="xxxxx@kindle.cn"
YOUR_SEND_MAIL_USERNAME="xxxx@163.com"
YOUR_SEND_MAIL_SECRET = 'xxxxxxxxxxxx'
MOBI_BOOK_PATH='./output/book.mobi'
...
```

## 开始抓取生成

```bash
$ sh start.sh
```

执行后会自动抓取页面生成markdown， 下载每个文章的图片， 然后gitbook通过markdown生成此次文档列表的`book.mobi` (output/book.mobi), 在start.sh 最后面有个备份的操作， 会把此次的mobi备份到`output/books`. 然后发送到指定的kindle地址邮箱.

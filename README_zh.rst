========
pycronic
========

这个项目受到了 `cronic`_ 的启发，并在原始脚本的基础上增加了一些额外的功能。比如通过自定义的SMTP发送报警邮件、保存所有的cron jobs的运行日志。

为什么要使用pycronic?
=====================

我们都知道，crontab拥有自己的邮件通知系统，当你的cron job产生一些输出时，他会发送一封邮件通知到你设置的邮箱地址。但是，当你要运行的cron job特别多时，这些邮件简直会多的看不过来。所以我们需要让它的邮件通知变的更聪明点，只在任务出错的时候通知我们。

所以，你可能会把你的crontab配置成这样： ::

    # 重定向所有的标准输出，这样只有在脚本有错误输出的时候我们才会接到邮件
    * * * * * some_work > /dev/null

    # 或者你更懒一些关掉了所有的输出，这样你的脚本要是出错了，可能过了几个星期你都不会发现
    * * * * * some_work > /dev/null 2>&1

如果使用pycronic，事情将会变得更简单 ::

    cronic="/usr/local/bin/cronic"                                                                       
    * * * * * &cronic some_work

所有你要做的就是用cronic命令放在你脚本前面，它会帮你检查你的脚本的返回值、检查是不是有错误输出，如果有问题的话，它会发邮件通知你。 ::

    MAIL TITLE: [Cronic@server1] Error occoured when running "backup"

    MAIL CONTENT: 

    Cronic Error Report
    ===================

    [2013-11-12 16:07:24.228788] Cronic detected failure or error output for the command:

    backup

    RESULT CODE: 2

    ERROR OUTPUT:
    ~~~~~~~~~~~~~

    Can not connect to database!

    STANDARD OUTPUT:
    ~~~~~~~~~~~~~~~~

    Starting backup...

默认设置下，cronic还会把你的脚本运行结果存储在目录(/tmp/pycronic)中。

如何安装
========

使用pip来安装: ::

    # pypi
    sudo pip install pycronic
    # 或者github
    sudo pip install -e git+https://github.com/piglei/pycronic/#egg=pycronic

配置
====

安装好了以后，运行cronic试试看： ::

    $ cronic 
    Usage: cronic YOUR_COMMAND

    $ cronic ls
    Config file "/etc/pycronic.conf" does not exist!
    Run "cronic init" to create a default one."

然后运行 "sudo cronic init" 来创建一个默认的配置文件: ::

    # Log path for pycronic, pycronic will store all logs to this directory
    log_path = /tmp/pycronic

    # Send an error email or not, default to not send
    send_alert_email = True

    # Email Title
    mail_title = [Cronic@%(host)s] Error occoured when running "%(command)s"

    # Email receivers
    # receivers = sample@sample.com

    # Email smtp server config
    [email_config_smtp]
    # username = username
    # host = smtp.sample.com
    # password = password
    # FROM = Cronic <pycronic@sample.com>
    # port = 587

如何使用
========

当你运行的命令没有产生错误的时候，cronic不会输出任何东西: ::

    piglei@macbook-pro:etc$ cronic ls
    piglei@macbook-pro:etc$ cat /tmp/pycronic/ls.log 
    [The script result will be stored in the log file]

但是当有错误发生时，它会产生这样的输出: ::

    $ cronic ls asdf
    Cronic Error Report
    ===================

    [2013-11-12 15:49:03.349575] Cronic detected failure or error output for the command:

    ls asdf

    RESULT CODE: 1

    ERROR OUTPUT: 
    ~~~~~~~~~~~~~

    ls: asdf: No such file or directory

    STANDARD OUTPUT:
    ~~~~~~~~~~~~~~~~

    None

如果你已经配置好了你的crontab的话，这个时候就会发送一封这样的邮件到你的邮箱了。

或者你也可以修改"/etc/pycronic.conf"来配置smtp服务来通过它来发送错误邮件，我们也更推荐这么干。

配置上crontab
=============

现在在crontab里使用它吧: ::

    $ crontab -e
    # If you have not config your pycronic.conf's smtp config, you can still
    # use crontab to send error emails.
    MAILTO="piglei2007@gmail.com"
    cronic="/usr/local/bin/cronic"                                                                       

    */5 * * * *  $cronic YOUR SCRIPT

Enjoy!

.. _cronic: http://habilis.net/cronic/


========
pycronic
========

`Chinese Version`_

This project is inspired by `cronic`_ and privided some extra useful functions
such as sending email error report by SMTP and store logs of crontab scripts.

Why pycronic?
=============

Crontab has the ability to send mail notification when any output was generated
executing your script as we know. And it will send bunch of emails to you 
every day if your has a lof of scripts, what if we only want to get the mail 
when something goes wrong?

As a result, You may config your crontab like this: ::

    # Redirect all standard output to /dev/null so we will get an email
    # only if this script has some standard error output.
    * * * * * some_work > /dev/null

    # Or this to ignore all output for lazy people, but you will never 
    # be notified if your script fails.
    * * * * * some_work > /dev/null 2>&1

Using pycronic to make things simpler: ::

    cronic="/usr/local/bin/cronic"                                                                       
    * * * * * &cronic some_work

All you need is prepend cronic to your script.
**cronic** command will check the return code and the error output for you, if something
wents wrong, you will get an email notification through crontab's default mailing system
or your customized STMP server. ::

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

And cronic will stores all your scripts output to a directory(/tmp/pycronic by default).

Installation
============

Using pip: ::

    # Install from pypi
    sudo pip install pycronic
    # Or install from github
    sudo pip install -e git+https://github.com/piglei/pycronic/#egg=pycronic

Configuration
=============

After the installation, run "cronic" in your command line to verify: ::

    $ cronic 
    Usage: cronic YOUR_COMMAND

    $ cronic ls
    Config file "/etc/pycronic.conf" does not exist!
    Run "cronic init" to create a default one."

Then run "sudo cronic init" to creat a default config file under /etc, the default config
file should looked like this: ::

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

How to use
==========

cronic will be silent if no error has occured when running a script: ::

    piglei@macbook-pro:etc$ cronic ls
    piglei@macbook-pro:etc$ cat /tmp/pycronic/ls.log 
    [The script result will be stored in the log file]

But if an error has occured(cronic will check the standard error output), it will print
an error message like this: ::

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

If you have configured your crontab, now an email will send to your email address.

You can also modify config to send mail through smtp instead of using crontab 
and this is the more recommended.

Rock crontab
============

Now config your crontab, using pycronic to wrap your scripts: ::


    $ crontab -e
    # If you have not config your pycronic.conf's smtp config, you can still
    # use crontab to send error emails.
    MAILTO="piglei2007@gmail.com"
    cronic="/usr/local/bin/cronic"                                                                       

    */5 * * * *  $cronic YOUR SCRIPT

Enjoy!

.. _cronic: http://habilis.net/cronic/
.. _Chinese Version: https://github.com/piglei/pycronic/blob/master/README_zh.rst


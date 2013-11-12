========
pycronic
========

This project is inspired by `cronic`_ and privided some useful functions
like sending email error report by SMTP and store logs of crontab scripts.

Installation
============

Use pip install from github: ::

    sudo pip install https://github.com/piglei/pycronic.git

Configuration
=============

After the installation, run "cronic" in your command line to verify: ::

    $ cronic 
    Usage: cronic YOUR_COMMAND

    $ cronic ls
    Config file "/etc/pycronic.conf" does not exist!
    Run "cronic init" to create a default one."

Now run "sudo cronic init" to creat a default config file under /etc, the default config
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

cronic will output nothing if no error has occured when running a script: ::

    piglei@macbook-pro:etc$ cronic ls
    piglei@macbook-pro:etc$ cat /tmp/pycronic/ls.log 
    [The script result will be stored in the log file]

But if an error has occured(cronic will check the standard error output), it will output
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

You can also config "/etc/pycronic.conf" to send mail through smtp instead of using crontab 
and this is the more recommended way.

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


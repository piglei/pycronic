# -*- coding: utf-8 -*-

default_mail_title = "[Cronic@%(host)s] Error occoured when running \"%(command)s\""

default_config_file = '''\
# Log path for pycronic, pycronic will store all logs to this directory
log_path = /tmp/pycronic

# Send an error email or not, default to not send
send_alert_email = False

# Email Title
mail_title = %s

# Email receivers
# receivers = sample@sample.com

# Email smtp server config
# [email_config_smtp]
# username = username
# host = smtp.sample.com
# password = password
# from = Cronic <pycronic@sample.com>
# port = 587
''' % (default_mail_title)


error_report_tmpl = '''\
Cronic Error Report
===================

[%(now)s] Cronic detected failure or error output for the command:

%(command)s

RESULT CODE: %(ret_code)s

ERROR OUTPUT: 
~~~~~~~~~~~~~

%(stderr_content)s

STANDARD OUTPUT:
~~~~~~~~~~~~~~~~

%(stdout_content)s
'''


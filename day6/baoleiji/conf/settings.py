#_*_coding:utf-8_*_
__author__ = 'jieli'
import sys


DATABASE = {
    'host': '192.168.2.211',
    'port': 3306,
    'db_name': 'audit_test',
    #'db_name': 'audit',
    'username': 'root',
    'password':'alex3714'
}

MaxTaskProcesses = 4

Welcome_msg = '''
|-------\033[32;1m[Welcome login OldBoy Auditing server]\033[0m-------|
|            Version :   0.1                         |
|            Author  :   Alex Li                     |
|            QQ Group:   29215534                    |
|----------------------------------------------------|\n\n'''

DatabaseInitSqlFile = 'src/audit.sql'
DatabaseInitSqlFileWithSample = 'src/audit_sample.sql'
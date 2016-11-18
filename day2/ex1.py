# -*- coding:utf-8 -*-
from os import system, popen
import  commands

system('ipconfig')
cmd_res = system('dir')
print '---',cmd_res
cmd_res2 = popen('dir').read()
print '---',cmd_res2

cmd_res3 = commands.getoutput('dir')
print '---',cmd_res3
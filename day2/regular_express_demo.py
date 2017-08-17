# -*- coding:utf-8 -*-
__auth__ = 'christian'

import re

"""
. 匹配除换行符以外的任意字符
\d 数字0-9中的任意一个
\s 可以匹配一个空格（也包括Tab等空白符）
\w 可以匹配一个字母或数字
+ 匹配前一个字符1次或无限次
* 匹配前一个字符0次或无限次
？匹配前一个字符0次或一次
[] 字符集，对应的位置可以是字符集中的任意字符,可以逐一给出，也可以给出范围，[^abc]取反，不是abc的任意字符
() 正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）
"""

print '-----str1--------'
str1 = 'a23b\na34b'
print '--->', re.findall(r"a(\d+)b", str1)
print '--->', re.findall(r"a(\d+)b.+a(\d+)b", str1)
print '--->', re.findall(r"a(\d+)b.+a(\d+)b", str1, re.S)  # 加上re.S后。将会匹配换行符，默认.不会匹配换行符。
print '--->', re.findall(r"^a(\d+)b", str1, re.M)   # 加上re.M后,^$标志将会匹配每一行，默认^和$只会匹配第一行。

print '\n-----str2--------'
str2 = 'abcfjacefmadfkaefnamf'
print '--->', re.findall(r"a[bced]+f", str2)  # 逐一给出
print '--->', re.findall(r"a[b-e]+f", str2)  # 给出范围
print '--->', re.findall(r"a[^bcde]+f", str2)  # [^ ] 取反


m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')

print "m.string:", m.string
print "m.re:", m.re
print "m.pos:", m.pos
print "m.endpos:", m.endpos
print "m.lastindex:", m.lastindex
print "m.lastgroup:", m.lastgroup

print "m.group(1,2):", m.group(1, 2)  # 如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。
print "m.groups():", m.groups()
print "m.groupdict():", m.groupdict()
print "m.start(2):", m.start(2)
print "m.end(2):", m.end(2)
print "m.span(2):", m.span(2)
print r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3')

print '\n-----line--------'
line ='192.168.0.1 25/Oct/2012:14:46:34 "GET /api HTTP/1.1" 200 44 "http://abc.com/search" "Mozilla/5.0"'
reg = re.compile('^(?P<remote_ip>[^\s]*) (?P<date>[^ ]*) "(?P<request>[^"]*)" (?P<status>[^ ]*) (?P<size>[^ ]*) \
"(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)"')
regMatch = reg.match(line)
line_bits = regMatch.groupdict()
print line_bits
for k, v in line_bits.items() :
  print k+": "+v



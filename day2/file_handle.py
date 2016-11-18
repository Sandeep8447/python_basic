# -*-coding:utf-8-*-
#append "a"

# read and write at the same time.
# r+ w+
import string
fileHandle = file("lockfile.txt", "w+")
print 'first line:', fileHandle.readline()
print fileHandle.tell()
print 'second line:', fileHandle.readline()
#fileHandle.write("change third line")
fileHandle.flush()#将内存中的数据写入到硬盘
print fileHandle.tell() #游标的位置
#fileHandle.seek(6)
#print fileHandle.tell()
fileHandle.close()

fileHandle = file("lockfile.txt", "r")
for line in fileHandle.xreadlines():
    print line
fileHandle.close()

fileHandle = file("lockfile.txt", "w")
cases = list(string.uppercase)
print cases
list_cases = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J\n', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U\n', 'V', 'W', 'X', 'Y', 'Z']
fileHandle.writelines(list_cases)
print fileHandle.truncate(8)
fileHandle.close()


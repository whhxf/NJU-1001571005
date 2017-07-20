#coding=utf-8
"""
@Conan
3.4作业
2. 输入一个字符串“I like Python very much 2333 because Python is very cute 666.”，
判别该字符串中数字字符和单词的个数，并将第一次出现的Python替换成你偶像的名字并输出新字符串
"""

str = 'I like Python very much 2333 because Python is very cute 666.'
digit = [i for i in str if i.isdigit()]
alpha = [i for i in str if i.isalpha()]
print 'digit has %s and alpha has %s'%(len(digit),len(alpha))
print str.replace('Python', 'Conan', 1)
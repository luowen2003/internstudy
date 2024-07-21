import string

text = """
Got this panda plush toy for my daughter's birthday,
who loves it and takes it everywhere. It's soft and
super cute, and its face has a friendly look. It's
a bit small for what I paid though. I think there
might be other options that are bigger for the
same price. It arrived a day earlier than expected,
so I got to play with it myself before I gave it
to her.
"""

def wordcount(text):
    text = text.lower()
    text = text.replace(',',"").replace(':',"").replace('.',"")
    word_list = text.split()
    dict={}  #定义一个空的字典，在后面的运算中逐步添加数据
    a=0
    for key in word_list: #遍历整个列表
        if key==' ':
            a+=1
        else:
            if key in dict.keys():  #判断当前key是否已经存在
                dict[key]=dict[key]+1  #在当前key的个数上加 1
            else:
                dict[key]=1  #当前key第一次出现
    print(dict)
    return

wordcount(text)
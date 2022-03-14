'''
先看这里：本代码利用规则删除非情感词
keys：列表格式，利用规则进行筛选后的词语
add：列表格式，手动添加
delete：列表格式，手动删除
'''


import json
with open("/Users/nxcy/Desktop/自然语言处理数据/分词结果txt和json/测试.json", encoding="utf-8") as f:
    dict = json.load(f)
# 查看所有词的词性
cixing=[]
for i in dict.keys():
    # print(dict[i]['词性'].keys())
    # cixing.append(dict[i]['词性'].keys())
    for j in dict[i]['词性'].keys():
        cixing.append(j)
cixingset=set(cixing)#初始词性种类集合
#定义一个函数 看下包含某个词性的有哪些词语
def print_cx(dict,cx):
    for i in dict:
        if cx in dict[i]['词性'].keys():
            # print(i)
            print(i,dict[i])
# -----------------------------------------------
#定义一个函数 看下包含某个词性的有哪些词语
def print_cx(dict,cx):
    """输出含有某个词性的词语，还有以他为key的字典
       并输出为txt文本格式
       file1 = open(cx+".txt","w")
    Args:
        dict ([type]): 导入的json字典文件
        cx (‘n’): 手动输入的词性 
    """ 
    file1 = open(cx+".txt","w")  # 新建一个txt文件用来保存      
    for i in dict:
        if cx in dict[i]['词性'].keys():
            # print(i)
            print(i,dict[i])
            file1.writelines(str(i)+'----'+str(dict[i])+'\n')
    file1.close()
# -----------------------------------------------
# 定义一个函数，输出只包含某个词性的词语
# 想看一看只含有动词词性的词语需要怎么删除
def one(dict,cx):
    """只输出包含一个词性的词语
       这里最后再给他输出为txt
    Args:
        dict (字典): dict
        cx (字符串): 'v'

    Returns:
        返回print输出: [description]
    """    
    file1= open('只包含词性'+cx+'的词语.txt','w')
    for i in dict:
        if cx in dict[i]['词性'].keys() and len(dict[i]['词性'].keys()) == 1:
            # print(i)
            file1.writelines(str(i)+'----'+str(dict[i])+'\n')
            print(i,dict[i])
    file1.close()
# -----------------------------------------------
def print_cx_morethanone(dict,cx):
    """输出含有某个词性的词语，还有以他为key的字典
       但是还有一个条件就是不能只包含一个词性
       又添加了含有n这个词性，可以自己改
    Args:
        dict ([type]): 导入的json字典文件
        cx (‘n’): 手动输入的词性 
    """         
    for i in dict:
        if cx in dict[i]['词性'].keys() and len(dict[i]['词性'].keys()) > 1 and 'n' in dict[i]['词性'].keys():
            # print(i)
            print(i,dict[i])
# -----------------------------------------------
# 以下开始筛选词语
def inter(a,b):
    """这个函数是用来看一个集合和另一个集合是否有交集的
    用法如下：
    lst1=['a','b','c']
    lst2=['x']
    lst3=inter(lst1,lst2)
    if lst3:  如果这里有重合的，那么就是True 没有重合的就是False
        print(lst3)
    else:
        print("Empty")

    Args:
        a ([type]): 列表
        b ([type]): 列表

    Returns:
        [type]: 就直接用if来做选择判断
    """    
    return list(set(a)&set(b))
#---------------------------------------------------
# 删除词频小于5的词语
for i in list(dict.keys()):
    sum=0
    for j in dict[i]['词性'].keys():
        # print(dict[i]['词性'][j])
        sum=sum+dict[i]['词性'][j]
    if sum<5:
        # print(i)
        dict.pop(i)

#----------------------
# 删除含有以下词性的词语
d=['b','c','e','f','m','nrf','o','p','q','r','s','t','u','w','y','z','']
keys=list(dict.keys())
for i in keys:
    x=dict[i]['词性'].keys()
    if inter(x,d):
        # print(i,dict[i])
        dict.pop(i)

#---------------------
# 删除只含有以下词性的词语，条件是词性只有一个
d=['Ag','Dg','Ng','Tg','Vg','d','j','h','k','v','vd','vn']
keys=list(dict.keys())
for i in keys:
    x=dict[i]['词性'].keys()
    if len(x)==1 and inter(x,d):
        dict.pop(i)
        # print(i,dict[i])
print('完成')
# print(i,dict[i])      
#---------------------
# 手动要添加的词语（被误删了）
keys=list(dict.keys())
add=['值得','浪费','带娃','可玩性','遛娃','不推荐','买不起','解压','有点累','超喜欢','买不起','很多','好多','棒','太久','好久','美','热门','加勒比海盗']
keys=keys+add
delete=['##','～～','～～～','啊～','呃呃',]
for i in delete:
    try:
        keys.remove(i)
    except:
        print("'"+i+"'"+'不在要删除的列表里面')
# keys.pop('ShanghaiDisneyResort')
# with open("/Users/nxcy/Desktop/筛选后的情感词.txt", "w", encoding='utf-8') as f:
#     json.dump(keys, f)  # 写为一行
# file = open('/Users/nxcy/Desktop/筛选后的情感词.txt','w')
# file.write(str(keys))
# file.close()
# -----------------------------------
# 写入到txt
with open("/Users/nxcy/Desktop/自然语言处理数据/分词结果txt和json/筛选后的情感词列表.txt", 'w') as f:
    for i in keys:
        f.write(i+'\n')
# -----------------------------------
# 读取txt，存为列表
f = open("/Users/nxcy/Desktop/筛选后的情感词.txt","r")
lines = f.readlines()
x=[]
for line in lines:
    line=line.strip('\n')# 删除\n
    print(line)
    x.append(line)
# -----------------------------------
# 输出x，x即为关键词
print(x)
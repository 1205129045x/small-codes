# 导入去除长度大于50的评论的文件（/Users/nxcy/Desktop/自然语言处理数据/被处理的excel/去除长度大于50的评论.xlsx）
from email import header
import sys
sys.path.append('/Users/nxcy/Documents/HanLP/my-nlp- processing')
from function import *
import pandas as pd
from pyhanlp import *
CRFLexicalAnalyzer = JClass("com.hankcs.hanlp.model.crf.CRFLexicalAnalyzer")
analyzer = CRFLexicalAnalyzer()
data1 = pd.read_excel('/Users/nxcy/Desktop/自然语言处理数据/被处理的excel/去除长度大于50的评论.xlsx')

'''
with open("/Users/nxcy/Desktop/自然语言处理数据/分词结果txt和json/筛选过后的情感分词.json", encoding="utf-8") as f:
    dict = json.load(f)
sentimentwords=list(dict.keys())
# 上面这部分是读取我之前存的筛选过后的情感词，现在要更新了
'''
f = open("/Users/nxcy/Desktop/自然语言处理数据/分词结果txt和json/筛选后的情感词列表.txt","r")
lines = f.readlines()
sentimentwords=[]
for line in lines:
    line=line.strip('\n')# 删除\n
    # print(line)
    sentimentwords.append(line)
# 读取我之前筛选好的情感词，并将情感词存为列表
big=[]#大列表，用来存所有话的词
for sentence in data1['内容'].values.tolist():
    s=analyzer.analyze(sentence.replace(" ", ""))
    s=str(s).split()
    # s为这种形式 ['价格/n', '是/v', '贵/a']
    # 然后接下来就是遍历这个s，用spilt('/')进行分割，提取出[价格,是,贵]
    #存[价格,是,贵]这些词，这一步可以直接加个if语句，如果有词语在我们筛选好的情感词汇里面的话，我们再给他添加进去
    small=[]#小列表，用来存一句话的词
    for i in range(len(s)):
        string=str(s[i])
        f=string.split('/')
        if f[0] in sentimentwords:
            small.append(f[0])
    big.append(small)
# print(big)    
newtest=[x for x in big if x] #删除空列表[]
# print(newtest)
test=pd.DataFrame(data=newtest)
test.to_csv('/Users/nxcy/Desktop/自然语言处理数据/被处理的excel/评论保留情感词汇的分词结果.csv',index=None, header=None,encoding='utf_8_sig')
import sys
sys.path.append('/Users/nxcy/Documents/HanLP/my-nlp- processing')
from function import *
with open("/Users/nxcy/Desktop/自然语言处理数据/分词结果txt和json/统计词频和词性还有分数.json", encoding="utf-8") as f:
    dict = json.load(f)
orderdictandwirite(dict,'测试')

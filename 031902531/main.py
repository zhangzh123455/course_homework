import sys
from pypinyin import  lazy_pinyin,pinyin
import os
class Mgc_treenode(object):
    #建立树的结点
    def __init__(self,value=None):
        self.value=value
        self.son=dict()
        self.num=0
class Mgc_tree(object):
    #建树
    def __init__(self,s):
        self.root=Mgc_treenode()
        self.count=0
        self.s=s
        for i in s:
            self.insert(i)
    def insert(self,mgc):
        #插入函数
        self.count+=1
        current_node=self.root
        parent=[]
        parent.append(self.root)
        child=[]
        len1=len(mgc)
        for w in range(len1):
            word=mgc[w]
            if((word>='A' and word <='Z') or (word>='a' and word<='z')):#英文无需判断拼音,但为查找方便将英文全部转化为小写插入树中
                temp_word=word.lower()
                if temp_word not in current_node.son:
                    next = Mgc_treenode(value=temp_word)
                    current_node.son[temp_word] = next
                    current_node = next
                else:
                    current_node = current_node.son[temp_word]
                if w==len1-1:
                    current_node.num=self.count
                    # 尾结点标志
            else:#中文需插入中文拼音，中文拼音拆分以及中文拼音的第一个字母
                temp_list = lazy_pinyin(word)
                temp_word1 = temp_list[0]
                child=[]
                child.append(Mgc_treenode(temp_word1))
                if(len(temp_word1)>1):
                    child.append(Mgc_treenode(temp_word1[0]))
                for i in range(len(parent)):
                    for j in child:
                        parent[i].son[j.value]=j
                if len(temp_word1)>1:
                    child.append(child[1])
                    for m in range(1,len(temp_word1)):
                        child[1].son[temp_word1[m]]=Mgc_treenode(temp_word1[m])
                        child[1]=child[1].son[temp_word1[m]]
                if w==len1-1:
                    for k in child:
                        k.num=self.count#尾结点标志
            parent=child.copy()

    def search(self,text,l):
        #查找函数
        b_list=[]#用来存放接下来要插入到父亲结点的结点列表
        number=0#用来计算total的值
        for j in range(l):
            start=0
            end =0
            p=self.root
            for i in range(len(text[j])):
                ca=text[j][i]
                temp_list=lazy_pinyin(ca)
                m=temp_list[0]
                m=m.lower()
                if m in p.son and p is self.root:
                    start=i
                if m in p.son:
                    p=p.son[m]
                if m in self.root.son:
                    start=i
                    p=self.root.son[m]
                if p.num != 0:
                    end=i
                    flag=p.num
                if end!=0 and (i==len(text[j])-1 or text[j][i+1] not in p.son):
                    #这边要注意输出最长的匹配字符串，例如falungong错误输出成falung的情况
                    s1=text[j][start:end+1]
                    s2=str(j+1)
                    s1='Line'+s2+': <'+self.s[flag-1]+'> '+s1
                    b_list.append(s1)
                    end=0
                    p=self.root
                    number+=1
        s2='Total: '+str(number)
        b_list.insert(0,s2)
        with open(ans_path,mode="w",encoding="utf-8") as fp:
            #输出函数
            for i in b_list:
                fp.write(i)
                fp.write('\n')
if __name__ == '__main__':
    word_path=sys.argv[1]
    org_path=sys.argv[2]
    ans_path=sys.argv[3]
    with open(word_path, encoding='utf-8') as f1:
        #读取敏感词词库
        ws = f1.read().split('\n')
    model=Mgc_tree(ws)
    #通过敏感词建树
    with open(org_path,encoding='utf-8') as f2:
        #读取待检测文本
        test_wenben=f2.read().split('\n')
    long=len(test_wenben)
    model.search(test_wenben,long)#调用查找函数，输出匹配的敏感词

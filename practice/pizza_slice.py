from collections import defaultdict as d
import sys

#sys.setrecursionlimit(10000)

m,n=map(int,raw_input().split())
nums=map(int,raw_input().split())

def rec(arr,split=20,help=False,param=0):
    mn,mx,dic=arr[0],arr[-1],d(list)
    width=(mx-mn)/(1.*split)
    width=(mx-mn)/(1.*width)
    half=width/2.0;ref=mn-half
    if help:
        step=round((param-ref)/width)
        idx=ref+(step*width)
        return idx
    for i in xrange(len(arr)):
        num=arr[i]
        step=round((num-ref)/width)
        idx=ref+(step*width)
        dic[idx].append(i)
    return dic

def reArray(dic,dSort):
    array=[]
    for key in dSort:
        thickness=dic[key][-1]-dic[key][0]+1
        array.append(key*thickness)
    return array

ct = 0 #kDic={}
def knapsack(W,wt,n):
    pass #if (W,tuple(wt),n) in kDic:
    pass #    return kDic[(W,tuple(wt),n)]
    if n==0 or W==0:
        #kDic[(W,tuple(wt),n)]=0,[]
        return 0,[]
        global ct
        ct+=1
        print ct
    if (wt[n-1] > W):
        val=knapsack(W,wt,n-1)
        #kDic[(W,tuple(wt),n)]=val
        return val
    else:
        exc=knapsack(W,wt,n-1)
        inc=knapsack(W-wt[n-1],wt,n-1)
        inc=wt[n-1]+inc[0],inc[1]+[n-1]
        val=[exc,inc][inc[0]>=exc[0]]
        #kDic[(W,tuple(wt),n)]=val
        return val

dic=rec(nums,split=20000)
dSort=sorted(dic)
reArr=reArray(dic,dSort)

#dic2=rec(reArr,split=400)
#dSort2=sorted(dic2)
#reArr2=reArray(dic2,dSort2)

#est, idx = knapsack(m,reArr2,len(reArr2))
est, idx = knapsack(m,reArr,len(reArr))

realIdx = reduce(lambda x,y:x+y,[dic[dSort[x]] for x in idx])
realSum = sum([nums[x] for x in realIdx])
excess = realSum-m
if excess>0:
    for i in xrange(len(idx)):
        if sum([nums[x] for x in realIdx[:i]])>=excess:
            realIdx=realIdx[i:]
            break
newSum = sum([nums[x] for x in realIdx])

print len(realIdx)
print " ".join(map(str,realIdx))


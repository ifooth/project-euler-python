'''
Created on Jun 7, 2012

@author: Joe Lei
'''

import decimal
import logging
from collections import OrderedDict

from euler.lib import *

log = logging.getLogger(__name__)


def problem_79():
    mydata=[i.strip() for i in data.openfile('keylog.txt')]
    key=mydata[0]          
    
def problem_80():
    decimal.getcontext().prec=102    
    i_sum=0
    l_temp=set(i*i for i in range(1,10))
    for i in filter(lambda x:x not in l_temp,range(2,100)):
        if i in l_temp:continue
        i_sum+=sum(int(i) for i in str((decimal.Decimal(i).sqrt()*10**99))[0:100:1])
        #print(str((decimal.Decimal(i).sqrt()*10**99)))
    return i_sum

def problem_89():
    roman_num = data.openfile('roman.txt').split('\n')
    roman_len = sum(len(i) for i in roman_num)
    roman_new = [num2roman(roman2num(i)) for i in roman_num]
    roman_len_new = sum(len(i) for i in roman_new)
    n = 'XIIIIII'
    log.info(n)
    log.info(roman2num(n))
    log.info(num2roman(roman2num(n)))
    return roman_len_new - roman_len    

def roman2num(roman):
    roman_chars = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    return sum(roman_chars[i] for i in str(roman))

def num2roman(num):
    roman_chars = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    roman_chars = OrderedDict(sorted(roman_chars.items(),key=lambda x:x[1],reverse=True))
    result = ''
    for r in roman_chars:
        a,b = divmod(num,roman_chars[r])
        num = b
        result += r*a
    return result

        
        
def problem_92():    
    s_set=set()
    for i in range(2,10000000):
        temp=i
        s_temp=set()
        while temp!=89:
            temp=sum(int(j)**2 for j in str(temp))
            if temp==1:break
            elif temp not in s_temp:s_temp.add(temp)
            else:break            
        else:
            s_set.update(s_temp)
    return len(s_set)
def problem_95():
    i_result=[0,0]    
    for i in range(220,1000):
        temp=ext.XInt(i).sumOfDivisors()
        n=1
        if temp==1:continue
        while i!=temp:            
            temp=ext.XInt(temp).sumOfDivisors
            n+=1
            if temp==1 or temp>1000:break
        else:
            if i_result[0]<n:i_result=[n,i]
    return i_result

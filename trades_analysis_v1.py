# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:44:19 2019

topic:   To count every profit and loss trades, calcuate profit/loss ratio,, no, of profit trades,etc.

@author: Meet Kakadiya
"""
# taking input of unspecified lines 

a=int(input())
trades=[] 
while a > -1000:
    trades.append(a)
    a=int(input())
    


#total sum of trades
print("total number of trades:", len(trades), "total sum of all trades:", sum(trades), sep="\n")

#counting profit and loss trades and adding them in one list

profit_trades=[]
loss_trades=[]
for i in trades:
    if (i>0):
        profit_trades.append(i)
    else:
        loss_trades.append(i)
        
print("total no. of profit trades:", len(profit_trades), "gross profit:", sum(profit_trades), sep="\n")

print("total no. of loss trades:", len(loss_trades), "gross loss:", sum(loss_trades), sep="\n")

'''
"%.2f" % 1.2632563
   prints=>  1.26
 prints the specified number of digits after decimal point
'''
print("how much times loss is profit:", "%.3f" % (sum(profit_trades)/sum(loss_trades)), sep="\n")
        
print("max profit:", max(profit_trades), "max loss:", max(loss_trades), sep="\n")  

'''
current output example:
    
    runfile('F:/git projects/All my repositories/Trading/trades_analysis_v1.py', wdir='F:/git projects/All my repositories/Trading')

+105

-32

+36

+48

-12

+159

+258

-36

-15

+414

+26

+98

+88

-10000
total number of trades:
13
total sum of all trades:
1137
total no. of profit trades:
9
gross profit:
1232
total no. of loss trades:
4
gross loss:
-95
how much times loss is profit:
-12.968
max profit:
414
max loss:
-12

'''



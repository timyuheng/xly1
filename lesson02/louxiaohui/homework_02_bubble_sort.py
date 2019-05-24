#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
#l = [11, 5, 9, 7, 4, 2, 3, 1]
l = [3, 7, 2, 5, 20, 11]

'''
1, 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2, 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3, 针对所有的元素重复以上的步骤，除了最后一个。
4, 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
'''
# 排序进行的次数，len个数排len-1次
for i in range(0, len(l)-1):
    '''
    每次比较 len(l)-1-i 次
    第一次找到最大值，将其放到列表最后一个元素下
    第二次找到第二最大值，将其放到列表倒数第二个元素下
    ... ...
    最后一次比较，找到第二最小值，将其放到列表第二个元素下，最小值为第一个元素
    '''
    for j in range(0, len(l)-1-i):
        # 相邻元素比较，若逆序则交换，左小右大
        if l[j] >= l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
    print ("第{}次比较后的数组：" .format(i+1))
    print (l)

#!/usr/bin/python3
#-*- coding: UTF-8 -*-

def insertsort(arr):
    '''list is a number list'''
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

if __name__ =='__main__':
    li = list(map(int,input().split()))
    arr=insertsort(li)
    print ("排序后的数组:") 
    for i in range(len(arr)): 
        print ("%d" %arr[i])

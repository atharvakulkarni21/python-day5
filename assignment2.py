# Assignment 2
list1 = [10,20,40,60,70,80]
list2 = [5,15,25,35,45,60]
MergedList =list1+list2
print("merged list is ", MergedList)
SortedList=[]
for i in range(min(MergedList),max(MergedList)+1):
    if i in MergedList:
        SortedList.append(i)
print("sorted list is ", SortedList)
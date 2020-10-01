#this code is for predifed array it will give you an basic idea how
# Bubble sort Works
# psedo Algo Below

toBeSorted=[99,77,44,31,64,28,67,45,34,63]

def bubbleSort(toBeSorted):
n = len(toBeSorted)
for i in range(n-1):
for j in range(0, n-i-1):
if toBeSorted[j] > toBeSorted[j+1] :
toBeSorted[j], toBeSorted[j+1] = toBeSorted[j+1], toBeSorted[j]

result=bubbleSort(toBeSorted)
if result != -1:
print('sorted array is',toBeSorted,'\nsorted by BUBBLE SORT')

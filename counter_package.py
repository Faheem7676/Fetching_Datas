#code to find top 3 element in their counts
#using most common
from collections import Counter

arr=[1,5,4,3,5,2,1,1,5,6,8,1,2,4,2,4,7,8,7,3]
counter=Counter(arr)
top_three=counter.most_common(3)
print(top_three)

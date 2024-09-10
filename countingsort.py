def countingsort(list):
    max_value=max(list)
    count=[0]*[max_value+1]
    for i in range(list):
        count[i]=count[i]+1
    for i in range(len(count)):
        count[i]=count[i]+count[i-1]
    output=[0]*len(list)
    for i in reversed(list):
        output[count[i]-1]=i
        count[i]=count[i]-1
    for i in range(len(list)):
        list[i]=output[i]
    return list
n=int(input("Enter the element:"))
list=[]
for i in range(n):
    list.append(int(input()))
result=countingsort(list)
print(result)

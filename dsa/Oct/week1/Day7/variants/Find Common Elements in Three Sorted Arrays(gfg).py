ar1 = [1, 5, 5, 5 ]
ar2 = [3, 4, 5, 5, 10]
ar3 = [5, 5, 10, 20]
intersection=[]
freq1={}
freq2={}
freq3={}


for i in ar1:
    if i not in freq1:
        freq1[i]=1
    else:
        freq1[i]+=1
for i in ar2:
    if i not in freq2:
        freq2[i]=1
    else:
        freq2[i]+=1
for i in ar3:
    if i not in freq3:
        freq3[i]=1
    else:
        freq3[i]+=1
print(freq1)
print(freq2)
print(freq3)
for i in freq1:
    if i in freq2 and i in freq3:
        minimum=min(freq1[i],freq2[i],freq3[i])
        for j in range(minimum):
            intersection.append(i)

print(intersection)




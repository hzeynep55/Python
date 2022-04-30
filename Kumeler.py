
#Kümeler
a=[23,2,6,5,48,52,12,3,45,25,63]
b=[12,36,52,45,89,2,1,4,78,63,98,85]

ortak=[]
afarkli=[]
bfarkli=[]
for i in range(len(a)):
  for j in range(len(b)):
    if a[i]==b[j]:
      ortak.append(a[i])
      
for k in range(len(a)):
  if a[k] not in ortak:
    afarkli.append(a[k])

for m in range(len(b)):
  if b[m] not in ortak:
    bfarkli.append(b[m])

       
    

print(f"a ve b kümesinin ortak elemanları {ortak}")
print(f"a kümesinin ortak olmayan elemanları {afarkli}")
print(f"b kümesinin ortak olmayan elemanları {bfarkli}")

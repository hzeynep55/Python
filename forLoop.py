
isim=["Ahmet","Oya","Yasemin"]
for i in range(len(isim)):
    name=isim[i]
    for j in range(len(isim[i])):
        if j==0:
            harf=name[j]

        if j==len(name)-1:
            sonharf=name[j]

    print(name,harf,"harfi ile başlar. ",sonharf," harfi ile biter")
    
    
    

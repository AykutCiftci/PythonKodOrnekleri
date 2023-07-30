num = 10
if num <= 10 and num >= 1:
    j=1
    while num > 0:
        while num > 0:
            print("{sayı1} X {jj} = {sonuç}".format(sayı1=num,jj=j,sonuç=num*j))
            j+=1
            if j == 11:
                break
        num-=1
        j=1
        print("\n")
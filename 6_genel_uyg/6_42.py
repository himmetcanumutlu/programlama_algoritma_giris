#Kodu yazan-->Ramazan Polat
#Yazılma tarihi-->18.12.2023
#Soru-->Klavyeden girilen iki pozitif tam sayıyı -çarpma operatörü kullanmadan- çarpan program
a = int(input("İlk pozitif tamsayıyı giriniz:"))
b = int(input("İkinci pozitif tamsayıyı giriniz:"))
c=0
for i in range (1, a+1, 1):
    for x in range(1, b+1 ,1):
        c=c+1
print(c)

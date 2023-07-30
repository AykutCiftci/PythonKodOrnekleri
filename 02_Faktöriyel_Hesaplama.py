num = int(input("Sayı giriniz :"))
factorial = 1
if num < 0:
	print("Negatif sayıların faktöriyeli olmaz ..")
elif num == 0:
	print("Sonuç : 1")
else:
	for i in range(1,num+1):
		factorial = factorial * i
	print("Sonuç : ",factorial)
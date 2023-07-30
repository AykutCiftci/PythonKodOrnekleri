num = int(input("Sayı giriniz :"))
if num < 0:
	print("Negatif sayıların faktöriyeli olmaz ..")
else:
	def fanc(num):
		if num > 1:
			return fanc(num - 1) * num
		else:
			return 1
	print(fanc(num))
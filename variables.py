a = float(input("введите первое число: "))
b = float(input("введите второе число: "))
sum = a + b

print (a, "+", b, " = ", sum)

text = a, "+", b, " = ", sum
somefile = open('Расчёты.txt','a')
print(text, file=somefile)

somefile.close()
a = (input("ведите имя: "))
b = (input("ведите фамилию: "))
sum = a + b

print (a, "+", b, " = ", sum)

text = a, "+", b, " = ", sum
somefile = open('имя фамилия.txt','a')
print(text, file=somefile)

somefile.close()
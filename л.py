a = (input(" введите имя : "))
b = (input(" введите фамилию : "))
d = (input(" введите пароль : "))

print (a, b)


somefile = open('имя фамилия.txt','a')
print(a, file=somefile)

somefile.close()
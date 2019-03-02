
s = input("введите знак +,-,*,/: ")

if s in ('+','-','*','/'):
    x = float(input('Введите первое число: '))
    y = float(input('Введите второе число: '))
    if s == '+':
        res = ("%.2f" % (x + y))
    elif s == '-':
        res = ("%.2f" % (x - y))
    elif s == '*':
        res = ("%.2f" % (x * y))
    elif s == '/':
        if y != 0:
            res = ("%.2f" % (x / y))
        else:
            print("Деление на ноль!")
    else:
        print("Неверный знак операции!")
print (x, s, y, " = ", res)

infile = x, s, y, '=', res
somefile = open('Расчёты.txt','a')
print(infile, file=somefile)

somefile.close()
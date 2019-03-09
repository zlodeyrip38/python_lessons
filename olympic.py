import turtle # Импортируем библиотеку turtle

turtle.color("blue") # Устанавливаем цвет черепашки
turtle.penup() # Поднимаем курсор
turtle.goto(-110, -25) # Переходим по нужным координатам
turtle.pendown() # Опускаем курсор
turtle.circle(45) # Рисуем круг с радиусом 45

turtle.color("black")
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(45)

turtle.color("red")
turtle.penup()
turtle.goto(110, -25)
turtle.pendown()
turtle.circle(45)

turtle.color("yellow")
turtle.penup()
turtle.goto(-55, -75)
turtle.pendown()
turtle.circle(45)

turtle.color("green")
turtle.penup()
turtle.goto(55, -75)
turtle.pendown()
turtle.circle(45)

turtle.color("black")
turtle.penup()
turtle.goto(0, 80)
turtle.pendown()
turtle.write("Olympic Symbol") # Вместо еще одного круга выводим надпись "Olympic Symbol"

turtle.done()

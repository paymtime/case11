import turtle

def ice(order, size):
    koch(order, size)
    turtle.right(120)
    koch(order, size)
    turtle.right(120)
    koch(order, size)

def koch(order, size):
    if order == 0:          
        turtle.forward(size)
    else:
        koch(order-1, size/3)   
        turtle.left(60)
        koch(order-1, size/3)
        turtle.right(120)
        koch(order-1, size/3)
        turtle.left(60)
        koch(order-1, size/3)

def main():
    turtle.up()
    turtle.goto(-100,0)
    turtle.down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    ice(n, a)

main()
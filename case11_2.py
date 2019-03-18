import turtle


def tree(l, n):
    if n == 0:
        return
    turtle.forward(l)
    turtle.right(30)
    tree(0.75*l, n-1)
    turtle.left(60)
    tree(0.75*l, n-1)
    turtle.right(30)
    turtle.backward(l)


def main():
    turtle.speed(1)
    turtle.left(90)
    tree(int(input()), int(input()))


if __name__ == '__main__':
    main()

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

def main1():
    turtle.up()
    turtle.goto(-100,0)
    turtle.down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    ice(n, a)

main1()

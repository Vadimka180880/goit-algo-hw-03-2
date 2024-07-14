import turtle
import argparse

def koch_curve(t, order, size):
    """
    Малює криву Коха за допомогою черепахової графіки.
    
    t: черепаха (turtle)
    order: рівень рекурсії
    size: довжина лінії
    """
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch_curve(t, order-1, size)
        t.left(60)
        koch_curve(t, order-1, size)
        t.right(120)
        koch_curve(t, order-1, size)
        t.left(60)
        koch_curve(t, order-1, size)

def snowflake(t, order, size):
    """
    Малює сніжинку Коха за допомогою черепахової графіки.
    
    t: черепаха (turtle)
    order: рівень рекурсії
    size: довжина сторони
    """
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def main():
    parser = argparse.ArgumentParser(description='Draw a Koch snowflake with a specified recursion level.')
    parser.add_argument('order', type=int, help='Recursion level of the Koch snowflake')
    parser.add_argument('size', type=int, nargs='?', default=300, help='Size of the snowflake (default: 300)')

    args = parser.parse_args()
    order = args.order
    size = args.size

    # Налаштування черепахової графіки
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor('white')

    t = turtle.Turtle()
    t.speed(0)  # Найвища швидкість малювання
    t.penup()
    t.goto(-size/2, size/3)
    t.pendown()

    # Малювання сніжинки Коха
    snowflake(t, order, size)

    # Завершення роботи
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()

# Виклик програми ввести у командному рядку :  python Home_work_3_2.py 3 300

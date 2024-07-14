import turtle
import time

# Налаштування екрану
screen = turtle.Screen()
screen.title("Towers of Hanoi")
screen.bgcolor("white")
screen.setup(width=800, height=600)

# Налаштування черепахи
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Позиції стрижнів
positions = {
    'A': -250,
    'B': 0,
    'C': 250
}

# Списки для кожного стрижня
towers = {
    'A': [],
    'B': [],
    'C': []
}

# Функція для малювання дисків
def draw_disk(x, y, disk):
    pen.penup()
    pen.goto(x - 20 * disk, y)
    pen.pendown()
    pen.begin_fill()
    pen.color("blue")
    pen.forward(40 * disk)
    pen.left(90)
    pen.forward(20)
    pen.left(90)
    pen.forward(40 * disk)
    pen.left(90)
    pen.forward(20)
    pen.left(90)
    pen.end_fill()

# Функція для оновлення екрану
def update_screen():
    pen.clear()
    for tower in towers:
        x = positions[tower]
        y = -200
        for disk in towers[tower]:
            draw_disk(x, y, disk)
            y += 30

# Функція для переміщення дисків
def move_disk(source, target):
    disk = towers[source].pop()
    towers[target].append(disk)
    update_screen()
    time.sleep(1)  # Додаємо затримку в 1 секунду між переміщеннями

def hanoi(n, source, auxiliary, target):
    if n > 0:
        hanoi(n-1, source, target, auxiliary)
        print(f"Move disk {n} from {source} to {target}")
        move_disk(source, target)
        screen.update()
        hanoi(n-1, auxiliary, source, target)

def main():
    n = int(input("Enter the number of disks: "))
    
    # Ініціалізація стрижнів
    for i in range(n, 0, -1):
        towers['A'].append(i)
    
    update_screen()
    screen.tracer(0)
    
    hanoi(n, 'A', 'B', 'C')
    
    screen.mainloop()

if __name__ == "__main__":
    main()

import math
print("Завдання 1") #Введення двох сторін трьох прямокутників.Виведення їх площ.
def rectangle_area(a, b):
    return a * b

rectangles = []
for i in range(1, 4):
    a = float(input(f"Введіть довжину сторони a прямокутника {i}: "))
    b = float(input(f"Введіть довжину сторони b прямокутника {i}: "))
    rectangles.append((a, b))

for i, (a, b) in enumerate(rectangles, start=1):
    area = rectangle_area(a, b) 
    print(f"Площа прямокутника {i}: {area}")


print("Завдання 2") #Обчислення гіпотенузи прямокутних трикутників

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

triangles = []
for i in range(1, 3):
    a = float(input(f"Введіть довжину катета a трикутника {i}: "))
    b = float(input(f"Введіть довжину катета b трикутника {i}: "))
    triangles.append((a, b))

hypotenuses = [hypotenuse(a, b) for a, b in triangles]

print(f"Гіпотенуза першого трикутника: {hypotenuses[0]}")
print(f"Гіпотенуза другого трикутника: {hypotenuses[1]}")

if hypotenuses[0] > hypotenuses[1]:
    print("Гіпотенуза першого трикутника більше.")
elif hypotenuses[0] < hypotenuses[1]:
    print("Гіпотенуза другого трикутника більше.")
else:
    print("Гіпотенузи трикутників рівні.")


print("Завдання 3") #Перевірка чи лежать точки всередині кола

def is_inside_circle(x, y, a, b, R):
    return (x - a)**2 + (y - b)**2 < R**2

a = float(input("Введіть координату a центру кола: "))
b = float(input("Введіть координату b центру кола: "))
R = float(input("Введіть радіус кола R: "))

points = {
    'P': (float(input("Введіть координату x точки P: ")), float(input("Введіть координату y точки P: "))),
    'F': (float(input("Введіть координату x точки F: ")), float(input("Введіть координату y точки F: "))),
    'L': (float(input("Введіть координату x точки L: ")), float(input("Введіть координату y точки L: ")))
}

inside_count = sum(is_inside_circle(x, y, a, b, R) for x, y in points.values())

print(f"Кількість точок, що лежать всередині кола: {inside_count}")


print("Завдання 4") #Обчислення площі чотирикутника

X = float(input("Введіть довжину сторони X: "))
Y = float(input("Введіть довжину сторони Y: "))
Z = float(input("Введіть довжину сторони Z: "))
T = float(input("Введіть довжину сторони T: "))

rectangle_area = X * Y
triangle_area = 0.5 * Z * T
total_area = rectangle_area + triangle_area

print(f"Площа чотирикутника: {total_area}")


print("Завдання 5") #Пошук натуральних чисел, що діляться на задані числ
n = int(input("Введіть максимальне натуральне число n: "))
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))

result = [i for i in range(1, n + 1) if i % a == 0 and i % b == 0 and i % c == 0]

print(f"Числа, що діляться на {a}, {b} і {c}: {result}")

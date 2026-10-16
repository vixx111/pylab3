import random

def solve_task2(filename_f='f2.txt', filename_g='g2.txt', count=20):
    numbers = [random.randint(-50, 50) for _ in range(count)]
    with open(filename_f, 'w') as f:
        for num in numbers:
            f.write(f"{num} ")
    print(f"[Задача 2] Файл '{filename_f}' заполнен: {numbers}")
    even_numbers = []
    with open(filename_f, 'r') as f:
        content = f.read().split()
        for item in content:
            num = int(item)
            if num % 2 == 0:
                even_numbers.append(num)
    with open(filename_g, 'w') as g:
        for num in even_numbers:
            g.write(f"{num} ")
    print(f"[Задача 2] Файл '{filename_g}' создан. Четные числа: {even_numbers}")
    return even_numbers
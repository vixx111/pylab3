import random
def solve_task1(filename_f='f1.txt', filename_g='g1.txt', m=3, n=2, count=20):
    numbers = [random.randint(-50, 50) for _ in range(count)]
    with open(filename_f, 'w') as f:
        for num in numbers:
            f.write(f"{num} ")

    print(f"[Задача 1] Файл '{filename_f}' заполнен: {numbers}")
    filtered_numbers = []
    with open(filename_f, 'r') as f:
        content = f.read().split()
        for item in content:
            num = int(item)
            if num % m == 0 and num % n != 0:
                filtered_numbers.append(num)
    with open(filename_g, 'w') as g:
        for num in filtered_numbers:
            g.write(f"{num} ")
    print(f"[Задача 1] Файл '{filename_g}' создан. Числа (дел. на {m}, не дел. на {n}): {filtered_numbers}")
    return filtered_numbers
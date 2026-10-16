from mypackage.module1 import solve_task1
from mypackage.module2 import solve_task2

def main():
    print("Запуск Задачи 1")
    solve_task1(m=3, n=2)
    print("\nЗапуск Задачи 2")
    solve_task2()
if __name__ == "main":
    main()
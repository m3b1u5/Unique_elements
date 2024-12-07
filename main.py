# ДЗ: Количество уникальных элементов
import random

def main():
    random_list = [random.randrange(1,10) for _ in range(random.randint(20,30))]
    print(f"Список: {random_list}")
    print(f"Уникальные элементы: {set(random_list)}")
    print(f"Количество уникальных элементов в списке: {len(set(random_list))}")

main()
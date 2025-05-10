def test_grades():
    """
    Завдання 1: Фільтрація високих оцінок
    """
    grades = [85, 60, 90, 70, 55, 100, 40, 78]
    high_grades = [grade for grade in grades if grade > 70]
    print("Високі оцінки:", high_grades)
    print("Кількість високих оцінок:", len(high_grades))


def shopping_list_filter():
    """
    Завдання 2: Фільтрація довгих назв товарів
    """
    shopping_list = ["молоко", "хліб", "масло", "яйця", "сир", "яблука"]
    long_items = [item for item in shopping_list if len(item) > 4]
    print("Товари з назвами довшими за 4 символи:", long_items)
    print("Кількість таких товарів:", len(long_items))


def find_duplicates():
    """
    Завдання 3: Пошук чисел, що повторюються
    """
    numbers = [1, 2, 3, 4, 3, 2, 5, 6, 5, 7]
    duplicates = []
    for num in numbers:
        if numbers.count(num) > 1 and num not in duplicates:
            duplicates.append(num)
    print("Числа, що повторюються:", duplicates)


def main():
    """
    Головне меню для запуску завдань
    """
    while True:
        print("\nОберіть завдання:")
        print("1. Високі оцінки за тест")
        print("2. Фільтрація списку покупок")
        print("3. Пошук дубльованих чисел")
        print("4. Вийти")

        choice = input("Ваш вибір (1-4): ")

        if choice == '1':
            test_grades()
        elif choice == '2':
            shopping_list_filter()
        elif choice == '3':
            find_duplicates()
        elif choice == '4':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


# Запуск програми
if __name__ == "__main__":
    main()

def apply_all_func(int_list, *functions):
    """
    Применяет несколько функций к списку чисел и возвращает результаты.

    Аргументы:
    int_list (list): Список чисел (целых или с плавающей точкой).
    *functions: Множество функций, которые должны быть применены к списку.

    Возвращает:
    dict: Словарь, где ключом является имя функции, а значением — результат её работы
          с переданным списком.

    Исключения:
    TypeError: Если входной параметр не является списком или элементы списка не являются числами.
    ValueError: Если передан пустой список.
    """
    # Создаем пустой словарь для хранения результатов
    results = {}

    # Проверка, что входной параметр является списком
    if not isinstance(int_list, list):
        raise TypeError("Функция принимает только список чисел.")

    # Проверка, что все элементы списка — числа (int или float)
    if not all(isinstance(num, (int, float)) for num in int_list):
        raise TypeError("Все элементы списка должны быть числами (int, float).")

    # Проверка на пустоту списка
    if len(int_list) == 0:
        raise ValueError("Список не должен быть пустым.")

    # Перебираем все переданные функции и применяем их к списку
    for function in functions:
        try:
            # Применяем функцию и сохраняем результат в словарь по ключу её имени
            results[function.__name__] = function(int_list)
        except Exception as e:
            # В случае ошибки сохраняем сообщение об ошибке в словарь
            results[function.__name__] = f"Error: {e}"

    # Возвращаем словарь с результатами
    return results


try:
    # Пример вызова функции с функциями max и min
    print(apply_all_func([6, 20, 15, 9], max, min))

    # Пример вызова функции с другими функциями (len, sum, sorted)
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
except TypeError as e:
    # Обработка ошибок типа TypeError (например, если передан неверный тип данных)
    print(f"Ошибка TypeError. {e}")
except ValueError as e:
    # Обработка ошибок типа ValueError (например, если передан пустой список)
    print(f"Ошибка ValueError. {e}")

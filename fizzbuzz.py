"""FizzBuzz: классическая задача.

Функция fizzbuzz(n) возвращает список строк для чисел 1..n:
- кратные 3 заменяются на "Fizz",
- кратные 5 — на "Buzz",
- кратные 15 — на "FizzBuzz".
"""


def fizzbuzz(n):
    """Возвращает список строк FizzBuzz для чисел от 1 до n."""
    result = []
    for i in range(1, n + 1):
        # Сначала проверяем кратность 15 (и 3, и 5)
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            # Обычное число — просто строковое представление
            result.append(str(i))
    return result


if __name__ == "__main__":
    # Печатаем результат для n = 15 построчно
    for line in fizzbuzz(15):
        print(line)

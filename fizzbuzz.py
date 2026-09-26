"""FizzBuzz: классическая задача.

Функция fizzbuzz(n) возвращает список строк для чисел 1..n:
- кратные 3 заменяются на "Fizz",
- кратные 5 — на "Buzz",
- кратные 15 — на "FizzBuzz".
"""

import argparse


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


def positive_int(value):
    try:
        number = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("N must be a positive integer") from exc
    if number < 1:
        raise argparse.ArgumentTypeError("N must be a positive integer")
    return number


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Print FizzBuzz for numbers from 1 to N.")
    parser.add_argument("N", nargs="?", type=positive_int, default=15,
                        help="positive upper bound (default: 15)")
    args = parser.parse_args()
    for line in fizzbuzz(args.N):
        print(line)

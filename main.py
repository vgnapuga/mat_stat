import os
import math
from itertools import permutations

from typing import Generator


# def permutations(elements:list, n:int) -> Generator[list[int], None, None]:
#     """Алгоритм Хипа"""
#     yield elements.copy()

#     c:list[int] = [0] * n
#     i = 0

#     while (i < n):
#         if (c[i] < i):
#             if (i % 2 == 0):
#                 elements[0], elements[i] = elements[i], elements[0]
#             else:
#                 elements[c[i]], elements[i] = elements[i], elements[c[i]]

#             yield elements.copy()

#             c[i] += 1
#             i = 0
#         else:
#             c[i] = 0
#             i += 1


def solution(n:int, m:int) -> float:
    days:list[int] = [day for day in range(1, n + 1)]
    length:int = 0
    result:int = 0

    for permutation in permutations(days, n):
        length += 1
        days_to_wait:list[int] = permutation[:m]
        max_from_days_to_wait:int = max(days_to_wait)

        if (n in days_to_wait):
            continue

        last_waiting_day:int = permutation[m - 1]
        for i in range(m, n):
            current_day:int = permutation[i]

            if (current_day == n):
                result += 1
                break
            elif (current_day > last_waiting_day):
                if (current_day < max_from_days_to_wait):
                    continue

                break

    return round(result / length, 3)


def main() -> None:
    os.system("clear")

    n:int = int(input("Введите общее кол-во дней: "))

    for i in range(1, n):
        result:float = solution(n, i)
        print(f"Вероятность при {i} днях ожидания:", result)


if (__name__ == "__main__"):
    main()
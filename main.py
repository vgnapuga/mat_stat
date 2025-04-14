from typing import Generator


def permutations(elements:list, n:int) -> Generator[list, list, list]:
    """Алгоритм Хипа"""
    yield elements.copy()

    c:list = [0] * n
    i = 0

    while i < n:
        if (c[i] < i):
            if (i % 2 == 0):
                elements[0], elements[i] = elements[i], elements[0]
            else:
                elements[c[i]], elements[i] = elements[i], elements[c[i]]

            yield elements.copy()

            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1

def calculate_permutations(n:int) -> list:
    days:list = [day for day in range(1, n + 1)]

    all_permutations:list = list(permutations(days, n))
    return all_permutations

def solution(n:int, m:int) -> float:
    permutations:list = calculate_permutations(n)
    result:int = 0

    for permutation in permutations:
        if (n in permutation[:m]):
            continue

        last_waiting_day:int = permutation[m - 1]
        for i in range(m, n):
            current_day:int = permutation[i]

            if (current_day == n):
                result += 1
                break
            elif (current_day > last_waiting_day):
                break
            else:
                continue

    return result / len(permutations)

def main() -> None:
    n:int = int(input("Введите общее кол-во дней: "))
    m:int = int(input("Введите кол-во дней для обязательного ожидания: "))

    result:float = solution(n, m)
    print("Вероятность продажи по максимальной цене:", result)

if (__name__ == "__main__"):
    main()
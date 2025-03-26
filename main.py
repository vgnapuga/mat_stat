def permutations(elements:list, n:int):
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
    return print(all_permutations)

def solution(n:int, m:int) -> int:
    permutations:list = calculate_permutations(n)

def main() -> None:
    n:int = int(input("Введите общее кол-во дней: "))
    m:int = int(input("Введите кол-во дней для обязательного ожидания: "))

    solution(n, m)

if (__name__ == "__main__"):
    main()
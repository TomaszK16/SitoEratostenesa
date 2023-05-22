import math

n = 0
while n <= 0:
    try:
        n = int(input("> Wprowadź liczbę maksymalną tablicy: "))
        if n <= 0: print("> Liczba musi należeć do zbioru liczb naturalnych i nie równać się 0! Spróbuj ponownie.")
    except:
        print("> Liczba musi być liczbą -_-")

numbers = [*[None, None], *[True for x in range(n-1)]]

for i in range(2, int(math.sqrt(n))):
    if numbers[i] == True:
        multiplier = 2
        while i * multiplier <= n:
            numbers[i * multiplier] = False
            multiplier += 1

for i in range(0, len(numbers)):
    print(f"{i}: {numbers[i]}")
input()
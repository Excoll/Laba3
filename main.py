from memo_decorator import limited_cache

@limited_cache(max_size=3)
def slow_square(n):
    print(f"Обчислюю квадрат числа {n}...")
    return n * n

print(slow_square(2))  # Обчислюється
print(slow_square(3))  # Обчислюється
print(slow_square(4))  # Обчислюється

print(slow_square(2))  # Береться з кешу
print(slow_square(3))  # Береться з кешу

print(slow_square(5))  # Обчислюється (кеш переповниться)

# Перевірка — чи 4 видалилось з кешу
print(slow_square(4))  # Буде обчислюватись наново
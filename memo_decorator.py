from collections import OrderedDict

def limited_cache(max_size=5):
    """
    Декоратор мемоізації з обмеженим розміром кешу.
    max_size — максимальна кількість збережених результатів.
    """

    def decorator(func):
        cache = OrderedDict()

        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))

            # Якщо ключ уже є — повертаємо з кешу
            if key in cache:
                cache.move_to_end(key)  # позначаємо як використаний
                return cache[key]

            # Викликаємо функцію та кладемо результат
            result = func(*args, **kwargs)
            cache[key] = result

            # Якщо кеш переповнений — видаляємо найстаріший елемент
            if len(cache) > max_size:
                cache.popitem(last=False)

            return result

        return wrapper

    return decorator
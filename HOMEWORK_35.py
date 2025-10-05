"""
=======================================
 ЗАДАНИЕ 1. МАТЕМАТИЧЕСКИЕ ВЫЧИСЛЕНИЯ
=======================================
Нужно:
1) Реализовать heavy_math(x) — "тяжёлая" функция (CPU-bound).
   Например: число Фибоначчи, факториал, интеграл и т.п.
2) Написать три варианта:
   - Последовательно
   - В потоках
   - В процессах
3) Замерить время и сравнить.
"""

import threading
import time
from functools import wraps
from multiprocessing import Process, Queue
from typing import Any, Callable, List

import requests


# ---------------------------
# Декоратор замера времени
# ---------------------------
def measure_time(label: str = "") -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{label} {end - start:.2f} сек")
            return result

        return wrapper

    return decorator


# ---------------------------
# Общая функция для математики
# ---------------------------
def heavy_math(x: int) -> int:
    """
    TODO: Реализовать "тяжёлую" математическую задачу.
    Например: рекурсивный fib(n), факториал через цикл и т.п.
    """
    if x <= 1:
        return x
    return heavy_math(x - 1) + heavy_math(x - 2)


# ---------------------------
# 1. Последовательный вариант
# ---------------------------
@measure_time("[Математика] Последовательно:")
def math_sequential(N: int = 35) -> None:
    a = []
    for i in range(30, N):
        result = heavy_math(i)
        a.append(result)
    print(f"Процесс:\n{a}")


# ---------------------------
# 2. Потоки
# ---------------------------
@measure_time("[Математика] Потоки:")
def math_threads(N: int = 35) -> None:
    a = []
    lock = threading.Lock()

    def worker(x: int) -> None:
        result = heavy_math(x)
        with lock:
            a.append(result)

    threads = []

    for i in range(30, N):
        t = threading.Thread(target=worker, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"Потоки:\n{a}")


# ---------------------------
# 3. Процессы
# ---------------------------
def worker_math(x: int, queue: Queue) -> None:
    result = heavy_math(x)
    queue.put(result)


@measure_time("[Математика] Процессы:")
def math_processes(N: int = 35) -> None:
    results_queue = Queue()

    processes = []

    for i in range(30, N):
        p = Process(target=worker_math, args=(i, results_queue))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    results = []

    while not results_queue.empty():
        results.append(results_queue.get())

    print(f"Процессы:\n{results}")


"""
=======================================
 ЗАДАНИЕ 2. GET-ЗАПРОСЫ
=======================================
Нужно:
1) Реализовать fetch_url(url), который делает GET-запрос.
2) Написать три варианта:
   - Последовательно
   - В потоках
   - В процессах
3) Замерить время и сравнить.
"""


# ---------------------------
# Общая функция для запросов
# ---------------------------
def fetch_url(url: str) -> str:
    """
    TODO: Реализовать GET-запрос через requests.get(url).
    Вернуть, например, status_code.
    """
    print(f"Start {url}")
    try:
        response = requests.get(url)
        print(f"Запрос: {url}, имеет статус {response.status_code}")
    except Exception as e:
        print(f"Ошибка запроса {url}: {e}")
    return url


# ---------------------------
# 1. Последовательный вариант
# ---------------------------
@measure_time("[GET] Последовательно:")
def net_sequential(urls: List[str]) -> None:
    print("START SEQUENTIAL")
    for url in urls:
        result = fetch_url(url)
        print(f"url={url} -> " f"result={result}")
        print("FINISH")


# ---------------------------
# 2. Потоки
# ---------------------------
@measure_time("[GET] Потоки:")
def net_threads(urls: List[str]) -> None:
    print("START TREADS")

    def worker(url: str) -> None:
        result = fetch_url(url)
        print(f"url={url} ->" f"result={result}")
        print("FINISH")

    threads = []

    for url in urls:
        t = threading.Thread(target=worker, args=(url,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


# ---------------------------
# 3. Процессы
# ---------------------------
def worker_net(url: str) -> None:
    result = fetch_url(url)
    print(f"url={url} ->" f"result={result}")
    print("FINISH")


@measure_time("[GET] Процессы:")
def net_processes(urls: List[str]) -> None:
    processes = []
    print("START PROCESSES")
    for url in urls:
        p = Process(target=worker_net, args=(url,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()


"""
=======================================
 ЗАПУСК ТЕСТОВ
=======================================
"""

if __name__ == "__main__":
    # Задание 1: математика
    print("\n=== ЗАДАНИЕ 1: МАТЕМАТИКА ===")
    math_sequential(N=35)
    math_threads(N=35)
    math_processes(N=35)

    # Задание 2: GET-запросы
    print("\n=== ЗАДАНИЕ 2: GET-ЗАПРОСЫ ===")
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/3",
        "https://httpbin.org/delay/4",
    ]
    net_sequential(urls)
    net_threads(urls)
    net_processes(urls)

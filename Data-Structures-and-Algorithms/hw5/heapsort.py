
def heapify(a, n, i):
    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and a[left] > a[largest]:
        largest = left

    if right < n and a[right] > a[largest]:
        largest = right

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)


def heap_sort(a):
    n = len(a)

    # 1. Строим max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)

    # 2. Переносим максимумы в конец
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)

    return a


a = [2, 6, 5, 3, 8, 7, 1, 0]

heap_sort(a)
print(a)

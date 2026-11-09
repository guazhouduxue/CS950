def print_items(items):
    for item in items:
        print(item)


def quick_sort(items):
    """返回升序排列的新列表，不修改原列表。"""
    if len(items) <= 1:
        return items[:]

    pivot = items[len(items) // 2]
    smaller = [item for item in items if item < pivot]
    equal = [item for item in items if item == pivot]
    larger = [item for item in items if item > pivot]

    return quick_sort(smaller) + equal + quick_sort(larger)


def main():
    numbers = [8, 3, 1, 7, 0, 10, 2, 3]
    print("排序前：", numbers)
    print("排序后：", quick_sort(numbers))
        


if __name__ == "__main__":
    main()

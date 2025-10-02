def find_insert_position(sorted_list: list, value) -> int:
    low = 0
    high = len(sorted_list)
    while low < high:
        mid = (low + high) // 2
        if sorted_list[mid] <= value:
            low = mid + 1
        else:
            high = mid
    return low

def test_insert_position():
    lst = [1, 3, 5, 7, 9]
    print(lst)
    for v in [0, 1, 2, 5, 6, 10]:
        pos = find_insert_position(lst, v)
        print(f"Insert {v} at position {pos}")

    for v in [0, 4, 8, 10]:
        pos = find_insert_position(lst, v)
        new = lst.copy()
        new.insert(pos, v)
        print(f"After inserting {v}: {new}")

if __name__ == "__main__":
    test_insert_position()
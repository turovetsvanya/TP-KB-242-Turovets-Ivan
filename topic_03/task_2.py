def test_list_methods():
    a = [1, 2, 3]
    print("Initial list:", a)
    a.append(4)
    print("After append(4):", a)
    a.extend([5, 6])
    print("After extend([5,6]):", a)
    a.insert(0, 100)
    print("After insert(0, 100):", a)
    a.remove(2)
    print("After remove(2):", a)
    b = a.copy()
    print("After list (b):", b)
    b.reverse()
    print("b after reverse():", b)
    b.sort()
    print("b after sort():", b)
    b.clear()
    print("b after clear():", b)

if __name__ == "__main__":
    test_list_methods()
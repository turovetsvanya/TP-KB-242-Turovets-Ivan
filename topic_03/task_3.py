def test_dict_methods():
    d = {"a": 1, "b": 2}
    print("Initial dictionary:", d)
    d.update({"b": 20, "c": 30})
    print("After update({'b':20, 'c':30}):", d)
    del d["a"]
    print("After del d['a']:", d)

    print("keys():", list(d.keys()))
    print("values():", list(d.values()))
    print("items():", list(d.items()))
    
    d2 = d.copy()
    print("copy d2:", d2)
    d2.clear()
    print("d2 after clear():", d2)

if __name__ == "__main__":
    test_dict_methods
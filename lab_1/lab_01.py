from typing import List, Dict, Optional
import re

students_list: List[Dict[str, str]] = [
    {"name": "Bob",  "phone": "0631234567", "email": "bob@example.com",  "group": "KB-242"},
    {"name": "Emma", "phone": "0632345678", "email": "emma@example.com", "group": "KB-242"},
    {"name": "Jon",  "phone": "0633456789", "email": "jon@example.com",  "group": "KB-242"},
    {"name": "Zak",  "phone": "0634567890", "email": "zak@example.com",  "group": "KB-242"},
]

def normalize_name(name: str) -> str:
    """Return normalized form of name for sorting/searching (lowercase, stripped)."""
    return name.strip().lower()

def find_all_by_name(name: str) -> List[int]:
    """Return list of indices of students whose name equals the given name (case-insensitive)."""
    target = normalize_name(name)
    return [i for i, s in enumerate(students_list) if normalize_name(s["name"]) == target]

def find_first_by_name(name: str) -> Optional[int]:
    """Return first index of a student by name or None if not found."""
    ids = find_all_by_name(name)
    return ids[0] if ids else None

def input_nonempty(prompt: str) -> str:
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("Field cannot be empty. Please try again.")

def validate_phone(phone: str) -> bool:

    phone_clean = phone.strip()
    return bool(re.fullmatch(r"\+?\d{7,15}", phone_clean))

def validate_email(email: str) -> bool:

    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email.strip()))

def insert_sorted(new_item: Dict[str, str]) -> None:
    """Insert new_item into students_list while keeping the list sorted by name."""
    name = normalize_name(new_item["name"])
    insert_pos = 0
    for i, item in enumerate(students_list):
        if name > normalize_name(item["name"]):
            insert_pos = i + 1
        else:
            break
    students_list.insert(insert_pos, new_item)

def print_all_list() -> None:
    if not students_list:
        print("Student list is empty.")
        return

    widths = {
        "idx": max(3, len(str(len(students_list)))),
        "name": max(4, max(len(s["name"]) for s in students_list)),
        "phone": max(5, max(len(s["phone"]) for s in students_list)),
        "email": max(5, max(len(s["email"]) for s in students_list)),
        "group": max(5, max(len(s["group"]) for s in students_list)),
    }
    header = f'{"#":>{widths["idx"]}}  {"Name":<{widths["name"]}}  {"Phone":<{widths["phone"]}}  {"Email":<{widths["email"]}}  {"Group":<{widths["group"]}}'
    print(header)
    print("-" * len(header))
    for i, s in enumerate(students_list):
        print(f'{i:>{widths["idx"]}}  {s["name"]:<{widths["name"]}}  {s["phone"]:<{widths["phone"]}}  {s["email"]:<{widths["email"]}}  {s["group"]:<{widths["group"]}}')

def add_new_element() -> None:
    print("Add a new student. Enter the data:")
    name = input_nonempty("  Name: ")
    phone = input_nonempty("  Phone (digits, optional +): ")
    while not validate_phone(phone):
        print("  Invalid phone format. Use only digits (7-15) or start with +.")
        phone = input_nonempty("  Phone: ")
    email = input_nonempty("  Email: ")
    while not validate_email(email):
        print("  Invalid email. Please try again.")
        email = input_nonempty("  Email: ")
    group = input_nonempty("  Group: ")

    new_item = {"name": name.strip(), "phone": phone.strip(), "email": email.strip(), "group": group.strip()}
    insert_sorted(new_item)
    print("New record added.")

def delete_element() -> None:
    name = input_nonempty("Enter exact name to delete: ")
    ids = find_all_by_name(name)
    if not ids:
        print("Element not found.")
        return
    if len(ids) == 1:
        idx = ids[0]
    else:
        print("Multiple records with that name were found. Choose index to delete:")
        print_all_list()
        while True:
            try:
                idx = int(input("Enter index: "))
                if idx in ids:
                    break
                print("Index is not in the list of found items.")
            except ValueError:
                print("Error: enter a number.")
    removed = students_list.pop(idx)
    print(f"Removed: {removed['name']} ({removed['phone']})")

def update_element() -> None:
    name = input_nonempty("Enter exact name of the student to update: ")
    ids = find_all_by_name(name)
    if not ids:
        print("Element not found.")
        return

    if len(ids) > 1:
        print("Multiple records with that name were found. Here they are:")
        print_all_list()
        while True:
            try:
                idx = int(input("Enter the index of the record you want to update: "))
                if idx in ids:
                    break
                print("Index does not belong to found records.")
            except ValueError:
                print("Enter a number.")
    else:
        idx = ids[0]

    current = students_list[idx]
    print("Current data (leave empty to keep unchanged):")
    print(f"  Name: {current['name']}")
    print(f"  Phone: {current['phone']}")
    print(f"  Email: {current['email']}")
    print(f"  Group: {current['group']}")

    new_name = input("  New name: ").strip()
    new_phone = input("  New phone: ").strip()
    if new_phone and not validate_phone(new_phone):
        while True:
            print("  Invalid phone format.")
            new_phone = input("  New phone: ").strip()
            if not new_phone or validate_phone(new_phone):
                break
    new_email = input("  New email: ").strip()
    if new_email and not validate_email(new_email):
        while True:
            print("  Invalid email.")
            new_email = input("  New email: ").strip()
            if not new_email or validate_email(new_email):
                break
    new_group = input("  New group: ").strip()

    updated = {
        "name": new_name if new_name else current["name"],
        "phone": new_phone if new_phone else current["phone"],
        "email": new_email if new_email else current["email"],
        "group": new_group if new_group else current["group"],
    }

    if normalize_name(updated["name"]) != normalize_name(current["name"]):
        del students_list[idx]
        insert_sorted(updated)
    else:
        students_list[idx] = updated

    print("Record updated.")

def print_help() -> None:
    print("""
Available commands:
  C - Create (add new record)
  U - Update (modify existing record)
  D - Delete (remove a record)
  P - Print (show all records)
  S - Search (search by name)
  X - Exit
  H - Help
    """)

def search_by_name() -> None:
    name = input_nonempty("Enter name to search (partial or full): ")
    target = name.strip().lower()
    found = []
    for i, s in enumerate(students_list):
        if target in s["name"].lower():
            found.append((i, s))
    if not found:
        print("Nothing found.")
        return
    print("Found records:")
    for i, s in found:
        print(f"  [{i}] {s['name']} | {s['phone']} | {s['email']} | {s['group']}")

def main() -> None:
    print("=== Sorted student phonebook — lab_01 ===")
    print_help()
    while True:
        choice = input("Enter command [C/U/D/P/S/X/H]: ").strip().upper()
        match choice:
            case "C":
                add_new_element()
            case "U":
                update_element()
            case "D":
                delete_element()
            case "P":
                print_all_list()
            case "S":
                search_by_name()
            case "H":
                print_help()
            case "X":
                print("Exit. Goodbye.")
                break
            case _:
                print("Invalid command. Press H for help.")

if __name__ == "__main__":
    main()
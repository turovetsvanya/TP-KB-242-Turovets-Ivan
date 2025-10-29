from operations import perform_operation

def main():
    while True:
        perform_operation()
        cont = input("Do you want to perform another operation? (yes/no): ").lower()
        if cont != 'yes':
            print("Thank you for using the calculator!")
            break

if __name__ == "__main__":
    main()
import logging
from operations import perform_operation

logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def main():
    while True:
        perform_operation()
        cont = input("Do you want to perform another operation? (yes/no): ").lower()

        logging.info(f"User chose to continue: {cont}")

        if cont != 'yes':
            print("Thank you for using the calculator!")
            logging.info("Program exited by user.")
            break

if __name__ == "__main__":
    main()
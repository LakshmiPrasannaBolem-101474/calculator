import logging
logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def add(a, b):
    result = a + b
    logging.info(f"Addition | Inputs: {a}, {b} | Result: {result}")
    return result
def subtract(a, b):
    result = a - b
    logging.info(f"Subtraction | Inputs: {a}, {b} | Result: {result}")
    return result
def multiply(a, b):
    result = a * b
    logging.info(f"Multiplication | Inputs: {a}, {b} | Result: {result}")
    return result
def divide(a, b):
    if b == 0:
        logging.error("Division by zero attempted")
        raise ZeroDivisionError("Cannot divide by zero")

    result = a / b
    logging.info(f"Division | Inputs: {a}, {b} | Result: {result}")
    return result
def calculator():
    while True:
        try:
            print("\n===== Calculator Menu =====")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")

            choice = input("Choose operation (1-5): ")

            if choice == "5":
                print("Exiting Calculator...")
                break

            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", add(a, b))

            elif choice == "2":
                print("Result:", subtract(a, b))

            elif choice == "3":
                print("Result:", multiply(a, b))

            elif choice == "4":
                print("Result:", divide(a, b))

            else:
                print("Invalid choice!")
                logging.error("Invalid menu choice entered")

        except ValueError:
            print("Invalid input! Please enter numbers only.")
            logging.error("ValueError: Non-numeric input provided")

        except ZeroDivisionError as e:
            print(e)

        except Exception as e:
            print("Unexpected error occurred.")
            logging.error(f"Unexpected Error: {e}")
if __name__ == "__main__":
    calculator()
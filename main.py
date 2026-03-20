import argparse
from typing import Callable, Dict


OPERATIONS: Dict[str, Callable[[float, float], float]] = {
    "add": lambda left, right: left + right,
    "subtract": lambda left, right: left - right,
    "multiply": lambda left, right: left * right,
    "divide": lambda left, right: left / right,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Simple calculator for terminal-based math operations."
    )
    parser.add_argument("--left", type=float, help="First number.")
    parser.add_argument("--right", type=float, help="Second number.")
    parser.add_argument(
        "--operation",
        choices=sorted(OPERATIONS.keys()),
        help="Operation to apply.",
    )
    return parser.parse_args()


def ask_number(label: str) -> float:
    while True:
        raw_value = input(f"{label}: ").strip()
        try:
            return float(raw_value)
        except ValueError:
            print("Enter a valid number.")


def ask_operation() -> str:
    options = {
        "1": "add",
        "2": "subtract",
        "3": "multiply",
        "4": "divide",
    }

    print("\nChoose an operation")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")

    while True:
        choice = input("Option: ").strip()
        if choice in options:
            return options[choice]
        print("Choose one of the listed options.")


def calculate(left: float, right: float, operation: str) -> float:
    if operation == "divide" and right == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return OPERATIONS[operation](left, right)


def main() -> None:
    args = parse_args()

    left = args.left if args.left is not None else ask_number("First number")
    right = args.right if args.right is not None else ask_number("Second number")
    operation = args.operation or ask_operation()

    try:
        result = calculate(left, right, operation)
    except ZeroDivisionError as error:
        print(f"Error: {error}")
        raise SystemExit(1) from error

    print("\nCalculation result")
    print("------------------")
    print(f"Operation: {operation}")
    print(f"Result: {result}")


if __name__ == "__main__":
    main()

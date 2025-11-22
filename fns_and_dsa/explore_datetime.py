from datetime import datetime, timedelta

def display_current_datetime():
    # Save current date and time
    current_date = datetime.now()

    # Format and display
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")

def calculate_future_date(days_to_add):
    # Save future date
    future_date = datetime.now() + timedelta(days=days_to_add)

    # Format and return
    return future_date.strftime("%Y-%m-%d")


def main():
    # Part 1: Display current datetime
    display_current_datetime()

    # Part 2: Ask user for number of days
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        future = calculate_future_date(days)
        print(f"Future date: {future}")
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")


if __name__ == "__main__":
    main()

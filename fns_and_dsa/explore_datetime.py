from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return "Current date and time: " + current_date.strftime("%Y-%m-%d %H:%M:%S")

def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    return "Future date: " + future_date.strftime("%Y-%m-%d")

def main():
    print(display_current_datetime())
    days = int(input("Enter the number of days to add to the current date: "))
    print(calculate_future_date(days))

if __name__ == "__main__":
    main()
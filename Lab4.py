# Function 1: Check if the given number is a proper day number and return "It is a Weekday!" if it is, or "It is a Weekend!" if it is not.
def check_weekday_or_weekend(day_number):
    if day_number < 1 or day_number > 7: 
        return ("NOt a proper day number!")
    elif 1 <= day_number <= 5:
        return ("It is a Weekday!")
    else: 
        return ("It is a Weeknend!")

day_number = int(input("What value is the day:"))
print (check_weekday_or_weekend(day_number))

# Function 2: Check if the given number is a proper day number and return the corresponding day name.
def get_day_name(day_number):
    day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if 1 <= day_number <=  7:
        return (f"It is a {day_list [day_number-1]}!")
    else: 
        return ("Not a proper day number!")
day_number = int(input("What value is the day number:"))
print (get_day_name(day_number))
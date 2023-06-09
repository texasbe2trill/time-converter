"""Ask the user to input a time in the 24 hour format and then converts
the 24 hour time into 12 hour time format using the modulo operator."""
print("=== 24-Hour to 12-Hour Time Converter ===")
print(
    "Please enter the 24 hour time (00:00 - 23:59) in HH:MM format you wish to convert:"
)

# Ask the user for what time they would like to input.

TIME_INPUT = str(input())

# Split the input from the user

time_result = TIME_INPUT.split(":")
hour_input, minute_input = time_result

# Casts hour_input and minute_input to an integer.

hour_input = int(hour_input)
minute_input = int(minute_input)
print("\n")
# Defines a function for hour_convert


def hour_convert():
    """Takes hour input then uses the modulo operator to mod by 12"""
    return int(hour_input) % 12


# Defines a function for hour_convert_mod


def hour_convert_mod(number):
    """Takes a number (12) then uses the modulo opertor to mod by 24"""
    return number % 24


# Creates a while loop to check for valid input for time entered by the user.

while (
    int(hour_input) > 23
    or int(hour_input) < 00
    or int(minute_input not in range(00, 60))
):
    print("Please enter a valid time in HH:MM format (00:00 - 23:59):")

    # Takes input as a string, then splits the input using ':' as a delimeter.

    TIME_INPUT = str(input())
    time_result = TIME_INPUT.split(":")
    hour_input, minute_input = time_result

    # Updates hour_input and minute_input variables to an integer

    hour_input = int(hour_input)
    minute_input = int(minute_input)

# Nested If statements for time/minute conditions within minute range of 00, 10 entered by user.

if minute_input in range(00, 10):
    minute_input_result = str(minute_input).zfill(2)
    if int(hour_input) == 0:
        print(
            f"The 12 hour equivalent is: {hour_convert_mod(12)}:{minute_input_result} AM"
        )

    elif int(hour_input) == 12:
        print(
            f"The 12 hour equivalent is: {hour_convert_mod(12)}:{minute_input_result} PM"
        )

    # Else if statements for hour input equal to 0 and 12, with minute input not in range of 00, 10.

    elif int(hour_input) == 0 and minute_input not in range(00, 10):
        print(f"The 12 hour equivalent is: {hour_convert_mod(12)}:{minute_input} AM")

    elif int(hour_input) == 12 and minute_input not in range(00, 10):
        print(f"The 12 hour equivalent is: {hour_convert_mod(12)}:{minute_input} PM")

    # Nested statements for all hours that do not equal 0 or 12 and minute input in range of 00, 10.

    elif int(hour_input) not in (0, 12) and minute_input in range(00, 10):
        if hour_input < 12:
            print(
                f"The 12 hour equivalent is: {hour_convert()}:{minute_input_result} AM"
            )
        else:
            print(
                f"The 12 hour equivalent is: {hour_convert()}:{minute_input_result} PM"
            )

# Else if statements for all other conditions entered by the user.

elif int(hour_input) == 0:
    print(f"The 12 hour equivalent is: {hour_convert_mod(12)}:{minute_input} AM")

elif int(hour_input) == 12:
    print(f"The 12 hour equivalent is: {hour_convert_mod(12)}:{minute_input} PM")

elif int(hour_input) < 12:
    print(f"The 12 hour equivalent is: {hour_convert()}:{minute_input} AM")

else:
    print(f"The 12 hour equivalent is: {hour_convert()}:{minute_input} PM")

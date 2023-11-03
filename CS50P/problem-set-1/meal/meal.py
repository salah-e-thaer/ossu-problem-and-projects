def main():
    time = input("What time is it? ")
    time_in_numbers = convert(time)

    if time_in_numbers >= 7.0 and time_in_numbers <= 8.0:
        print("breakfast time")
    elif time_in_numbers >= 12.0 and time_in_numbers <= 13.0:
        print("lunch time")
    elif time_in_numbers >= 18.0 and time_in_numbers <= 19.0:
        print("dinner time")
    else:
        print("it's not time for any meal.")

def convert(time):
    hours, minutes = time.split(":")
    return float(int(hours) + (int(minutes) / 60))


if __name__ == "__main__":
    main()
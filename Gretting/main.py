while True:
    hour = int(input("Enter the current hour (0-23): "))

    if 5 <= hour < 12:
        greeting = "Good Morning"
    elif 12 <= hour < 17:
        greeting = "Good Afternoon"
    elif 17 <= hour < 21:
        greeting = "Good Evening"
    elif (21 <= hour < 24) or (0 <= hour < 5):
        greeting = "Good Night"
    else:
        greeting = "Invalid hour entered"

    print(greeting)
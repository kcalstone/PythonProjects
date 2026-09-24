while True:
    #tempC = int(input("Enter your temperature in Celsius: "))
    try:
        tempC = int(input("Please enter your temperature in Celsius as a whole number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

tempF = (tempC * (9/5)) + 32

print(tempF)

if tempF > 86:
    print("It's too hot out--stay hydrated and seek air conditioning.")
elif tempF < 86 and tempF> 68:
    print("It's really nice out--enjoy the nice weather.")
elif tempF <68 and tempF > 40:
    print("It's a little chilly out--bring a jacket.")
elif tempF < 40 and tempF > 25:
    print("Bring a heavy jacket.")
else:
    print("Just stay inside--it's too cold.")
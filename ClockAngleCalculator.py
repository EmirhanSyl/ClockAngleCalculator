import math

hour = input("Please enter hour. [0 - 24): ")
minute = input("Please enter minute. [0, 60): ")

def AngleCalculator(hour, min):
    if hour >= 12 & hour < 24:
        hour -= 12

    angle = math.fabs(11 * min - 60 * hour) / 2
    return angle


if __name__ == "__main__":
    print("Angle between scorpion and minute hand is: " + str(AngleCalculator(int(hour), int(minute))))



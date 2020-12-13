import re
start = "Python program for Temperature conversion"
print(re.match(r'[A-Z a-z]+', start))
print(" ")
print(re.match(r'[A-Z a-z]+', 'select operation'))
print("1. Celcius to Fahrenheit,Kelvin,Rankine")
print("2. Fahrenheit to Celcius,Kelvin,Rankine")
print("3. Kelvin to Celcius,Fahrenheit,Rankine")
print("4. Rankineto Celcius,Fahrenheit,Kelvin")
print("")
choice = int(input("Enter Choice (1/2/3/4): "))
print("")


# celcius conversion
class cel:
    def __init__(self, temp):
        self.temp = temp_1
        ans_1 = float((temp * 9/5) + 32)
        ans_2 = float((temp + 273.15))
        ans_3 = float((temp * 9/5) + 491.67)
        print("fah = ", ans_1)
        print("kel = ", ans_2)
        print("ran = ", ans_3)


# parent class for fahrenheit conversion
class fah:
    def __init__(self, temp):
        self.temp = temp_2
        pass


# child class for fahrenheit conversion
class conv(fah):
    def __init__(self, temp):
        fah.__init__(self, temp)
        ans_4 = ((temp - 32) * 5/9)
        ans_5 = ((temp - 32) * 5/9 + 273.15)
        ans_6 = (temp + 459.67)
        print("cel = ", ans_4)
        print("kel = ", ans_5)
        print("ran = ", ans_6)


# parent class for kelvin conversion
class kel:
    def __init__(self, temp):
        self.temp = temp_3
        pass


# child class for kelvin conversion
class conv_1(kel):
    def __init__(self, temp):
        kel.__init__(self, temp)
        ans_7 = float(temp - 273.15)
        ans_8 = float(((temp - 273.15) * 9 / 5) + 32)
        ans_9 = float(temp * 1.8)
        print("cel = ", ans_7)
        print("fah = ", ans_8)
        print("ran = ", ans_9)


# class for rankine conversion
class ran:
    def __init__(self, temp):
        self.temp = temp_4
        ans_10 = float((temp - 491.67) * 5/9)
        ans_11 = float(temp - 459.67)
        ans_12 = float(temp * 5/9)
        print("cel = ", ans_10)
        print("fah = ", ans_11)
        print("kel = ", ans_12)

# selecting inputs for type of conversion
if choice == 1:
    temp_1 = float(input("Enter Celcius: "))
    a = cel(temp_1)

elif choice == 2:
    temp_2 = float(input("Enter Fahrenheit: "))
    b = fah(temp_2)
    e = conv(temp_2)

elif choice == 3:
    temp_3 = float(input("Enter Kelvin: "))
    c = kel(temp_3)
    f = conv_1(temp_3)

elif choice == 4:
    temp_4 = float(input("Enter Rankine: "))
    d = ran(temp_4)

else:
    print("Enter valid input")

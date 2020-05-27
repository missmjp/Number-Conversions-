#write program that takes 4 digit Arabic numbers and outputs
#the year in Roman Numberals
# 1 = I  2 = II  3 = III 4 = IV 5 = V  6 = VI 7 = VII  8 = VIII  9 = IX  10 = X

#first function to find the roman numeral for the thousands place
#It returns both the roman numeral string and an integer to use to subract from the original number to get to the next place
def RomanThousandsPlace(uT):
    if uT // 1000 == 3:
        rmThousand = "MMM"
        minThou = 3000
    elif uT // 1000 == 2:
        rmThousand = "MM"
        minThou = 2000
    else:
        rmThousand = "M"
        minThou = 1000
    return rmThousand, minThou

 #same code as above, this time made up of 9 if elif statments to get value      
def RomanHundredsPlace(uH):
    if uH // 100 == 9:
        rmHundred = "CM" 
        minHun = 900
    elif uH // 100 == 8:
        rmHundred = "DCCC"
        minHun = 800
    elif uH // 100 == 7:
        rmHundred = "DCC"
        minHun = 700
    elif uH // 100 == 6:
        rmHundred = "DC"
        minHun = 600
    elif uH // 100 == 5:
        rmHundred = "D"
        minHun = 500
    elif uH // 100 == 4:
        rmHundred = "CD"
        minHun = 400
    elif uH // 100 == 3:
        rmHundred = "CCC"
        minHun = 300
    elif uH // 100 == 2:
        rmHundred = "CC"
        minHun = 200
    elif uH // 100 == 1:
        rmHundred = "C"
        minHun = 100
    else:
        rmHundred = " "
        minHun = 0
    return rmHundred, minHun


def RomanTensPlace(uT):
    if uT // 10 == 9:
        rmTens = "XC" 
        minTen = 90
    elif uT // 10 == 8:
        rmTens = "LXXX" 
        minTen = 80
    elif uT // 10 == 7:
        rmTens = "LXX" 
        minTen = 70
    elif uT // 10 == 6:
        rmTens = "LX" 
        minTen = 60
    elif uT // 10 == 5:
        rmTens = "L" 
        minTen = 50
    elif uT // 10 == 4:
        rmTens = "XL" 
        minTen = 40
    elif uT // 10 == 3:
        rmTens = "XXX" 
        minTen = 30
    elif uT // 10 == 2:
        rmTens = "XX" 
        minTen = 20
    elif uT // 10 == 1:
        rmTens = "X" 
        minTen = 10
    else:
        rmTens = " "
        minTens = 0
    return rmTens , minTen 
    

def RomanOnesPlace(uO):
    if uO // 1 == 9:
        rmOne = "IX" 
        minOne = 9
    elif uO // 10 == 8:
        rmOne = "VIII" 
        minOne = 8
    elif uO // 10 == 7:
        rmOne = "VII" 
        minOne = 7
    elif uO // 10 == 6:
        rmOne = "VI" 
        minOne = 6
    elif uO // 10 == 5:
        rmOne = "V" 
        minOne = 5
    elif uO // 10 == 4:
        rmOne = "IV" 
        minOne = 4
    elif uO // 10 == 3:
        rmOne = "III" 
        minTen = 3
    elif uO // 10 == 2:
        rmOne = "II" 
        minOne = 2
    elif uO // 10 == 1:
        rmOne = "I" 
        minOne = 1
    else:
        rmOne = " "
        minOne = 0
    return rmOne, minOne
    

#first get input from user and store it in a variable
ArabicYear = int(input("Enter a year from 1000-3000: "))

#Call first function to find the thousands value, and place both return values into separate variables to be used later
RomThou, AYthou = RomanThousandsPlace(ArabicYear)
#use the return value of the integer variable to subtract the thousands from the original number to get the hundreds leftover
newYear = ArabicYear - AYthou

#Call second function to find the hundreds value, and place both return values into separate variables to be used later
RomHun, AYhun = RomanHundredsPlace(newYear)
newYear2 = newYear - AYhun 

RomTen, AYten = RomanTensPlace(newYear2)
newYear3 = newYear2 - AYten

RomOne, AYone = RomanOnesPlace(newYear3)

#print result combining all roman numerals 
print(RomThou + RomHun + RomTen + RomOne)
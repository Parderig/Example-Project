string = "Walter"
bill = int(input("How much was the meal?"))
integer = 7
double = 1.22
double = double + integer
boolean = True
slice = 'h'
string_that_is_a_slice = "W"
list = ["Zazie","Brennan", "Kassidy", "Ezra","Patrick"]
list.append("Walter")

def this(price):
  price = (price/100) * 15
  print("This is your tip {}" .format(price))
  if price%2 == 0:
    print("But honestly you should be tipping over card.")

#this(bill)

for i in list:
  print(i)
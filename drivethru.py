# Write code below 💖
# Drive-Thru 🚙
# Codédex
def welcome():
  print("Welcome to Harshitha's Resturant!")
  print('Here are the availible items to order:')
  menu = ['1. 🍔Cheeseburger', 
          '2. 🍟Fries', 
          '3. 🥤Soda' , 
          '4. 🍦IceCream' , 
          '5. 🍪Cookie']
  print(menu)

def get_item():
  
  value_of_ordered_item = int(input('Enter the value of the ordered item:'))

  if value_of_ordered_item == 1:
    print('🍔CheeseBurger')
  elif value_of_ordered_item == 2:
    print('🍟Fries')
  elif value_of_ordered_item == 3:
    print('🥤Soda')
  elif value_of_ordered_item == 4:
    print('🍦Ice Cream')
  elif value_of_ordered_item == 5:
    print('🍪Cookie')
  else :
    print('Error value entered does not exist')

welcome()
get_item()

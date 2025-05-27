gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print('SORTING HAT\n')

#Question--1
print('Question 1: \n')
print('Q1) Do you like Dawn or Dusk? \n  1) Dawn \n  2) Dusk \n')

answer = int(input('Enter the answer(1-2):'))

if answer == 1:
  guyffindor = gryffindor + 1
  ravenclaw = ravenclaw + 1
elif answer == 2:
  hufflepuff = hufflepuff + 1
  slytherin = slytherin + 1
else:
  print('Wrong Input.') 

#Question--2
print('\nQuestion 2:\n')
print('Q2)When I am Dead, I want people to remeber me as:\n  1) The Good \n  2) The Great \n  3) The Wise \n  4) The Bold \n')

answer = int(input('Enter the answer(1-4):'))

if answer == 1:
  hufflepuff = hufflepuff + 2
elif answer == 2:
  slytherin = slytherin + 2
elif answer == 3:
  ravenclaw = ravenclaw + 2
elif answer == 4:
  gryffindor = gryffindor +2
else:
  print('Wrong Input.')

#Question--3
print('Question 3:')
print('Q3) Which kind of instrument nost pleases your ear? \n  1) The Violin \n  2) The Trumpet \n  3) The Piano \n  4) The Drum \n')

answer = int(input('Enter the answer (1-4):'))

if answer == 1:
  slytherin = slytherin + 4
elif answer == 2:
  hufflepuff = hufflepuff + 4
elif answer == 3:
  ravenclaw = ravenclaw + 4
elif answer == 4:
  gryffindor = gryffindor + 4
else :
  print('Wrong Input.')

#Printing scores of each House
print('Gryffindor = ' , gryffindor)
print('Ravenclaw = ' , ravenclaw)
print('Hufflepuff = ' , hufflepuff)
print('Slytherin = ' , slytherin)




things_to_do = ['Go to Puri Jaganath Temple',
                'Visit Vrindavan',
                'Go to Switzerland',
                'Live in a random personhouse for a day.',
                'Grow Older by learning new things and lessons in life',
                'Open a cozy Resturant',
                'Road trip with Family.']

print(things_to_do)

things_to_do.append('Stay Happy and Lively all the time')
things_to_do.insert(4,'Forgive your past mistakes')
things_to_do.remove('Go to Switzerland')
things_to_do.pop(6)

print(things_to_do)

for i in range(len(things_to_do)):
  print(things_to_do[i])


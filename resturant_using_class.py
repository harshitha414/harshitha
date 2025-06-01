# Write code below 💖
class Resturant:
  name = ''
  category = ''
  rating = 0.0
  delivery = False

bobs_burgers = Resturant()
bobs_burgers.name = 'Bobs Burger'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False 

Rameshwaram = Resturant()
Rameshwaram.name = 'Rameshwaram Cafe'
Rameshwaram.category = 'Breakfast/Lunch/Dinner Cuisine'
Rameshwaram.rating = 3.8
Rameshwaram.delivery = False

Udupi = Resturant()
Udupi.name = 'Udupi Park'
Udupi.category = 'Lunch cuisine'
Udupi.rating = 2.9
Udupi.delivery = True

print(vars(bobs_burgers))
print(vars(Rameshwaram))
print(vars(Udupi))





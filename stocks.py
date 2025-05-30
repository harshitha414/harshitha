#Given List of stock prices for a day.
stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

#Finds price on the given day.

def price_at(x):
  answer = stock_prices[x-1]
  return answer
  
#Finds the maximum price of stock between two given days.

def max_price(a,b): 
  answer_max =0
  for x in range(a,b+1):
    answer_max = max(answer_max , price_at(x))
  return answer_max

#Finds the minimum price of stock btween two given days.

def min_price(a,b):
  answer_min = price_at(a)
  for x in range(a, b+1):
    answer_min = min(answer_min , price_at(x))
  return answer_min

#Calling the functions:

print(price_at(5))
print(max_price(5,10))
print(min_price(1,10))

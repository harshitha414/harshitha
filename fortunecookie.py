import random

text = [
  "Don't pursue happiness - create it.",
  "All things are difficult before they are easy.",
  "The early bird gets the worm, but the second mouse gets the cheese.",
  "Someone in your life needs a letter.",
  "Don't just think. Act!",
  "Your heart will skip a beat.",
  "The fortune you search for is in another one.",
  "Help! i'm being held by prisinor at a Chinese bakery."
]

def fortune():
  ranfortune = random.randint(0, len(text)-1)
  message = ""
  
  if ranfortune == 0:
    message = text[0]
  elif ranfortune == 1:
    message = text[1]
  elif ranfortune == 2:
    message = text [2]
  elif ranfortune == 3:
    message = text[3]
  elif ranfortune == 4:
    message = text[4]
  elif ranfortune == 5:
    message = text[5]
  elif ranfortune == 6:
    message = text[6]
  elif ranfortune == 7:
    message = text[7]
  elif ranfortune == 8:
    message = text[8]
  else:
    message = 'Error'
    
  print(message)

fortune()
fortune()
fortune()

     

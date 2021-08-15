# Define your functions
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  
  if res == 'a':
    return 'You selected a Small 🤏'
  elif res == 'b':
    return 'You selected a Medium 🖖'
  elif res == 'c':
    return 'You selected a Large 🙌'
  else:
    print_message()
    return get_size()

def print_message():
  print("I'm sorry, I did not understand your selection. 🥺 \nPlease enter the corresponding letter for your response. 👽")

def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte ")
  if res == 'a':
    return 'You selected a Brewed Coffee'
  elif res == 'b':
    return 'You selected a Mocha'
  elif res == 'c':
    return 'You selected a Latte'
  else:
    print_message()
    return get_drink_type()

def coffee_bot():
  print("Welcome to the cafe!")

  print(get_size())

  print(get_drink_type())

# Call coffee_bot()!
coffee_bot()
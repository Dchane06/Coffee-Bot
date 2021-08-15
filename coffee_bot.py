# Functions
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  
  if res == 'a':
    return 'Small'
  elif res == 'b':
    return 'Medium'
  elif res == 'c':
    return 'Large'
  elif res == 'secret':
    return 'That\'s an awfully hot coffee pot.'
  else:
    print_message()
    return get_size()

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ")
  if res == 'a':
    return 'Brewed Coffee :)'
  elif res == 'b':
    return 'Mocha :O'
  elif res == 'c':
    return order_latte()
  elif res == 'secret2':
    return 'YOUR USING WAY TOO MANY NAPKINS, BAPKINS, FLAM WHILE I FLAMIN FLAMAKINS BA BANNA BA BANNA BANNAKINS!'
  else:
    print_message()
    return get_drink_type()

def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% Milk \n[b] Non-fat Milk \n[c] Soy Milk \n> ")
  if res == 'a':
    return 'Regular Latte!'
  elif res == 'b':
    return 'Non-fat Latte!'
  elif res == 'c':
    return 'Soy Latte!'
  else:
    print_message()
    return order_latte()


def coffee_bot():
  print("Welcome to the cafe!")

  size = get_size()
  drink_type = get_drink_type()

  print('Alright, that\'s a {} {}!'.format(size, drink_type))

  name = input('Can I get your name please? \n> ')

  print('Thanks {}! Your drink will be ready shortly.'.format(name))


coffee_bot()
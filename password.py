import random
def generate():
  low = "abcdefghijklmnopqrstuvwxyz"
  numbers = "1234567890"
  up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  chars = "!@#$%^&*;:,.?><"
  password = ""
  for i in range(5):
    rand_low = random.choice(low)
    rand_numbers = random.choice(numbers)
    rand_up = random.choice(up)
    rand_chars = random.choice(chars)
    password += rand_low + rand_numbers + rand_up + rand_chars
  return password

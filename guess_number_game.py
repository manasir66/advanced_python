class GuessTheNumber:

  def __init__(self, number, mn=0, mx=100):
    self.number = number
    self.mn = mn
    self.mx = mx
    self.guesses = 0

  def get_guess(self):

    guess = input(f"Please guess a number between {self.mn} - {self.mx} : ")
    
    if self.valid_number(guess):
      return int(guess)
    else:
      print("Enter a valid number : ")
      return self.get_guess()
    
  def valid_number(self, str_num):
    try:
      number = int(str_num)
    except:
      return False
    
    return self.mn <= number <= self.mx

  def guess_now_play(self):
    while True:
      self.guesses += 1

      guess = self.get_guess()

      if guess < self.number:
        print("Guess was under ")
      elif guess > self.number:
        print("Guess was over ")
      else:
        print("You guessed it correctly")
        break


game = GuessTheNumber(48, 0, 100)
game.guess_now_play()
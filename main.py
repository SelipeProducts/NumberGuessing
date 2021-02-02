import random

class rand_num_game:
  the_score = 100
  game_running = False
  def rand_num_gen(self):
    return random.randint(1, 20)

  def ask_input(self):
    the_input = input("Guess a number: ")
    the_input = int(the_input)
    return the_input
  
  def give_hint_easy(self, random, my_input):
    if(my_input == random):
      self.game_running = False
    elif(my_input > random):
      if(my_input > random*2):
        print("That input is WAY too big.")  
      else:
        print("That input is too big.")
    elif(my_input < random):   
      if(my_input < random/2):
        print("That input is WAY too small.")
      else:
        print("That input is too small.")

  def compare(self, random, my_input):
    if(random != my_input):
      self.the_score -= 10
    else:
      self.game_running = False
      print("Number Found!")
  
  def start_game(self): 
    print("Random Number Guessing Game: (1-20)\n")
    self.game_running = True
    rand_num = self.rand_num_gen()
    #print("Rand Num: " + str(rand_num))
    while(self.game_running == True):
      #rand_num_game1 = rand_num_game()
      user_input = self.ask_input()
      self.give_hint_easy(rand_num, user_input)
      self.compare(rand_num, user_input)
      print("Score: " + str(self.the_score)+"\n")
      if (self.the_score <= 0):
        print("Game Over!")
        break;
    

#-------------------------------------

rand_num_game1 = rand_num_game()
rand_num_game1.start_game()

# rand_num = rand_num_game1.rand_num_gen()

# user_input = rand_num_game1.ask_input()


# rand_num_game1.give_hint_easy(rand_num, user_input)


#self.the_score should not be accessed directly in futute projects. Next time add a getter method and use that to access the data
# HL component 1- Get (and Check) user input

# To Do
# Check a lowest is an interger (any interger)
# Check that the highest is more than lowest (lowest bound only)
# Check that rounds is more than 1 (upper bound only)
# Check that the guess is between lowest and highest lower and upper open

# heading
def instructions():
    print()
    print("-*-*-* Welcome to the Higher Lower Game -*-*-*- ")
    print()
    print("For each game you will be asked to ... \n"
          "- Enter a 'low' and 'high' number. The computer will  use this numbers for all the rounds in a given game")
    print()
  

        






# Number checking function goes here
def int_check(question, low=None, high=None) :

  situation = ""

  if low is not None and high is not None:
      situation = "both"
  elif low is not None and high is None:
      situation = "low only"

  while True:


      try:
          response = int(input(question))

          # checks input is not too highest
          # too low if a both upper and lower bounds
          # are specified
          if situation == "both":
              if response <low or response > high:
                  print ("Please enter a number between {} and {}".format(low, high))
                  continue

          # checks input is not too lower
          elif situation == "low only":
              if response < low:
                  print("Please enter a number that is more than (or equal to) {}".format(low))
                  continue

          return response

      # checks input is a interger
      except ValueError:
          print("Please enter an interger")
          continue

 
# Main routine
print()
lowest = int_check("Low Number: ")
highest = int_check ("High Number: ")
highest = int_check("Rounds: ", 1)
guess = int_check("Guess ", lowest, highest)



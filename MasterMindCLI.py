#The classic mastermind game for the console
'''
Author: Gitter-ram
Version: 1.0
'''
def doIntro():
  print("*****************************")
  print("*Welcome To Mastermind v.1.0*")
  print("**************-By Gitter-ram*")
def showMainMenu():
  print("Main Menu:")
  print("1.Play")
  print("2.How to play")
  print("3.High-score")
  print("4.About")
  print("5.Quit")
  a = input("------------------------\n Your choice:")
  if a not in (1,2,3,4,5):
    print("Invalid input. Try again.")
    showMainMenu()
  elif a == 1:
    PlayGame()
  elif a == 2:
    showHelp()
  elif a == 3:
    showHighScore()
  elif a == 4:
    showAbout()
  elif a == 5
    print("Thanks for Visiting! Bye.")
    a = input("Hit Enter to continue.")
    exit()
  else:
    print("Please Enter the correct option number.")
    a =input("Restart The game and enter the correct OPTION NUMBER.")
    exit()

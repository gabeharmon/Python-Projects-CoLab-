# -*- coding: utf-8 -*-
"""CPS THINKPAD - Group Project (GH, EB, JS)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zSsMYIMFGFeekK8OfSPH7wJtrtjdB0HC
"""

import random
import datetime
print("                              CPS THINKPAD")
print("")
name = input("What is your name? ")
print("Hello,", name)
print("")
print("The date and time is", datetime.datetime.now())
print("")

gameChoice = input("What would you like to do? (Type 'wordguess', 'addition', 'madlibs', 'hangman', 'trivia', or 'calculator'). ")
print("")

# wordguess

if gameChoice == "wordguess":
  print("                              WORD GUESS")
  print("")
  print("It's time for some ocean trivia. Guess the next letter.")
  num = int(random.random() * 10)
  word = " "
  if num == 13:
    word = "Whales"
  if num == 12:
    word = "Sand"
  if num == 11:
    word = "Seaweed"
  if num == 10:
    word = "Goldfish"
  if num == 9:
    word = "Angelfish"
  elif num == 8:
    word = "Guppy"
  elif num == 7:
    word = "Clownfish"
  elif num == 6:
    word = "Oyster"
  elif num == 5:
    word = "Pirhana"
  elif num == 4:
    word = "Jellyfish"
  elif num == 3:
    word = "Clam"
  elif num == 2:
    word = "Catfish"
  elif num == 1:
    word = "Squid"
  elif num == 0:
    word = "Bass"

  print(word[0])
  wordCount = ""
  for i in word:
    wordCount = wordCount + "- "
  print(wordCount)

  count = 0

  for i in word:
    count += 1

  countMatcher = 1

  for i in word[1:]:
    guess = input("")
    if guess == i:
      print("Correct")
      countMatcher += 1
      if countMatcher == count:
        print("You got it. The correct word was", word + ".")
    else:
      print("Incorrect, try again.")
      break

#addition game

elif gameChoice == "addition":
  print("                              ADDITION")
  print("")
  print("Let's play an addition game.")
  numberOfGames = int(input("How many questions would you like to answer? "))
  correctAnswers = 0
  incorrectAnswers = 0
  for i in range(numberOfGames):
    x = int(random.random()*10)
    y = int(random.random()*10)
    answer = x + y
    print(x, "+", y)
    playerAnswer = int(input(""))
    if playerAnswer == answer:
      print("Correct ㋡")
      correctAnswers += 1
    else:
      print("Incorrect ☹, the correct answer was", answer)
      incorrectAnswers += 1
  correctPercentage = correctAnswers / numberOfGames * 100
  correctPercentage = int(correctPercentage)
  if correctPercentage == 1.0:
    correctPercentage = 100
  print("You answered", correctPercentage, "%", "of questions correctly.")
  if correctPercentage > 80:
    print("Good job!")
  else:
    print("Try again.")

# madlibs

elif gameChoice == "madlibs":
  print("                              MAD-LIBS")
  print("")
  print("Let's play mad-libs!")
  print("First, choose your story.")
  story = input("1 - Jungle Explorer, 2 - Princes and Princesses")
  if story == "1":
    print("Jungle Explorer!")
    name = input("Choose a name: ")
    noun = input("Choose a noun: ")
    adjective = input("Choose an adjective: ")
    verb = input("Choose a verb: ")
    noun2 = input("Choose a noun: ")
    adjective2 = input("Choose an adjective: ")
    noun3 = input("Choose a plural noun: ")
    print("In the wilderness of Brazil, an explorer that goes by the name of", name, "started their course. He brought with him his trusty", noun, "and went on his way.")
    print(name, "was a very", adjective, "explorer, and always knew how to", verb, ". On his journey, he came across a wild", noun2, "and fought it off with his", adjective2, "sword.")
    print("He finally finished his journey when he came across the giant pot of", noun3, ".")
  elif story == "2":
    print("Princes and Princesses!")
    name = input("Choose a name: ")
    noun = input("Choose a plural noun: ")
    verb = input("Choose an verb ending in -ing: ")
    noun2 = input("Choose a noun: ")
    noun3 = input("Choose a noun: ")
    adjective2 = input("Choose an adjective: ")
    noun3 = input("Choose a plural noun: ")
    print("Once upon a time there was a prince named", name, "who was the prince of", noun, "and was very good at", verb + ". One day, he was tasked with slaying the giant", noun2 + ".")
    print(name, "was a very", adjective2, "prince who feared nothing. He approached the", noun2, "and hit it with a", adjective2, "sword.")
    print("He was rewarded with", noun3, "for his bravery.")


# calculator

elif gameChoice == "calculator":
  print("                              CALCULATOR")
  print("")
  ca = "active"
  while ca == "active":
    calcChoice = input("What would you like to calculate? (Type '+', '-', '*', '/', '^', or 'done' to exit)")
    if calcChoice == "+":
      x = float(input("Value 1: "))
      y = float(input("Value 2: "))
      print(x + y)
    elif calcChoice == "-":
      x = float(input("Value 1: "))
      y = float(input("Value 2: "))
      print(x - y)
    elif calcChoice == "*":
      x = float(input("Value 1: "))
      y = float(input("Value 2: "))
      print(x * y)
    elif calcChoice == "/":
      x = float(input("Value 1: "))
      y = float(input("Value 2: "))
      print(x / y)
    elif calcChoice == "^":
      x = float(input("Value 1: "))
      y = float(input("To the power of: "))
      print(x ** y)
    elif calcChoice == "done":
      break
    else:
      print("Invalid command!")

#hangman

elif gameChoice == "hangman":
  print("                              HANGMAN")
  lst = []
  strikes = 0
  print("Player 1 will input lowercased letters until a word is made, and player 2 has seven attempts to guess player 1's letter.")
  print("When player 2 has guessed the entire word, player 1 should enter 'done' and player 2 should enter 'done' to end the game.")
  while True:
    Player2 = input("Player 1, please enter a lowercased letter ") # to finish both players must type "done"
    Player1 = input("Player 2, try to guess the lowercased letter ")
    if Player1 == Player2:
      print("letter found")
      lst.append(Player1)
      if Player2 =="done":
        print("Congrats, your word was",lst)
        break
    elif Player1 != Player2:
      while Player1 != Player2:
        print("guess again")
        Player1 = input("please guess again ")
        strikes += 1
        if strikes == 7 :
          print("Game Over")
          break
    elif Player2 == "done":
      print("Congrats, your word was", lst)
      break

elif gameChoice == "trivia":
  print("                               TRIVIA")
  def triviaGame():
    import random

    artQuest= {"q1": "Who painted Starry Night?" ,"a1": "Van Gogh" ,"q2": "Who painted the Mona Lisa?" ,"a2": "Leonardo da Vinci"}
    sciQuest= {"q1": "Which type of rock is made from magma?" ,"a1": "Igneous" ,"q2": "What is FE the chemical symbol for?" ,"a2": "Iron"}
    histQuest= {"q1": "Who was the 1st U.S. president?" ,"a1": "George Washington" ,"q2": "What year did the war of 1812 start" ,"a2": "1812"}
    sporQuest= {"q1": "What Lions quarterback went to the Rams and won a super bowl?" ,"a1": "Matthew Stafford" ,"q2": "What is Tom Brady's number?" ,"a2": "12"}

    gameType=input("Select a Category: Art, Science, History, or Sports")
    #Decide game type
    if gameType== "Art" or gameType== "art":
      #Question 1
      num=random.randint(1,4)
      if num == 1 or num== 2:
        print(artQuest["q1"])
        answer= input("what is the answer?")
        if answer== artQuest["a1"]:
          print("Correct")
        else:
          print("Wrong. The answer is",artQuest["a1"])
      #question 2
      elif num == 3 or num== 4:

        print(artQuest["q2"])
        answer= input(str("what is the answer?"))
        if answer== artQuest["a2"]:
          print("Correct")
        else:
          print("Wrong. The answer is",artQuest["a2"])

    elif gameType== "Science" or gameType== "science":
      #Question 1
      num=random.randint(1,4)
      if num == 1 or num== 2:
        print(sciQuest["q1"])
        answer= input("what is the answer?")
        if answer== sciQuest["a1"]:
          print("Correct")
        else:
          print("Wrong. The answer is",sciQuest["a1"])
      #question 2
      elif num == 3 or num== 4:

        print(sciQuest["q2"])
        answer= input("what is the answer?")
        if answer== sciQuest["a2"]:
          print("Correct")
        else:
          print("Wrong. The answer is",sciQuest["a2"])

    elif gameType== "History" or gameType== "history":
      #Question 1
      num=random.randint(1,4)
      if num == 1 or num== 2:
        print(histQuest["q1"])
        answer= input("what is the answer?")
        if answer== histQuest["a1"]:
          print("Correct")
        else:
          print("Wrong. The answer is",histQuest["a1"])
      #question 2
      elif num == 3 or num== 4:

        print(histQuest["q2"])
        answer= input("what is the answer?")
        if answer== histQuest["a2"]:
          print("Correct")
        else:
          print("Wrong. The answer is",histQuest["a2"])

    elif gameType== "Sports" or gameType== "sports":
      #Question 1
      num=random.randint(1,4)
      if num == 1 or num== 2:
        print(sporQuest["q1"])
        answer= input("what is the answer?")
        if answer== sporQuest["a1"]:
          print("Correct")
        else:
          print("Wrong. The answer is",sporQuest["a1"])
      #question 2
      elif num == 3 or num== 4:

        print(sporQuest["q2"])
        answer= input("what is the answer?")
        if answer== sporQuest["a2"]:
          print("Correct")
        else:
          print("Wrong. The answer is",sporQuest["a2"])
  triviaGame()
else:
  print("Invalid command!")
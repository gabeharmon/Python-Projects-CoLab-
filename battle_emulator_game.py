# -*- coding: utf-8 -*-
"""Battle Emulator Game

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Z4hqiuFGaediX8YwHJC9Ofn68XCHWCYW

**Battle Emulator Game**
"""

# Initialize and welcome

import random
print("Welcome to the battle system emulator!")
print("Your health: 15")
print("Yikes! A Pencil Pusher!")
print("")

# Gags have fixed health; established before while loop

cogHealth = 40
playerHealth = 15
pie = 8
flower = 4
anvil = 12

# Gags have fixed

pieStorage = 4
flowerStorage = 5
anvilStorage = 3

while cogHealth > 0 and playerHealth > 0:
  print("Pies in inventory: ", pieStorage)
  print("Flowers in inventory: ", flowerStorage)
  print("Anvils in inventory: ", anvilStorage)
  print("")
  cogAttack = random.random() # Randomize type of cog attack
  playerMove = input("Type 'pie' (medium accuracy, medium power), 'flower' (high accuracy, low power), or 'anvil' (low accuracy, high power). ")
  print("")

# Player chooses a move that corresponds to one of the following items

  if playerMove == "pie":
    hit = random.random() # Chance of player hit
    if pieStorage > 0: # Confirm player has pies
      pieStorage = pieStorage - 1 # Remove a pie when used
      if hit > 0.4: # Player has a 60% chance of a hit
        cogHealth = cogHealth - pie # Pie is worth 8 damage subtracted from cog health
        print("The pie hit! -8")
      else:
        print("You missed!")
    else:
      print("")
      print("You are out of pies!") # If the player has no pies, they're out of luck
      print("")

# Same logic applies to other gags, only modifications

  if playerMove == "flower":
    hit = random.random()
    if flowerStorage > 0:
      flowerStorage = flowerStorage - 1
      if hit > 0.1:
        cogHealth = cogHealth - flower
        print("The flower hit! -4")
      else:
        print("You missed!")
    else:
      print("")
      print("You are out of flowers!")
      print("")

  if playerMove == "anvil":
    hit = random.random()
    if anvilStorage > 0:
      anvilStorage = anvilStorage - 1
      if hit > 0.7:
        cogHealth = cogHealth - anvil
        print("The anvil hit! -12")
      else:
        print("You missed!")
    else:
      print("")
      print("You are out of anvils!")
      print("")

# Now the cog fights back...

  if cogAttack >= 0.75: # cogAttack is randomized at each iteration, 'if' statements correspond to random result
    hit = random.random() # Chance of cog attack hitting
    if hit >= 0.75:
      playerHealth = playerHealth - 2
      print("The cog played Rolodex! -2")
    else:
      print("The cog missed!")

  if cogAttack >= 0.50 and cogAttack < 0.75:
    hit = random.random()
    if hit >= 0.75:
      playerHealth = playerHealth - 4
      print("The cog played Paper Cut! -4")
    else:
      print("The cog missed!")

  if cogAttack >= 0 and cogAttack < 0.50:
    hit = random.random()
    if hit >= 0.25:
      playerHealth = playerHealth - 3
      print("The cog played Paperwork! -3")
    else:
      print("The cog missed!")

  if playerHealth <= 0:
    print("You went sad!")
    break

  if cogHealth <= 0:
    print("You beat the cog!")
    break

# End each iteration with health updates before player makes new move

  print("")
  print("Cog: ", cogHealth)
  print("Player: ", playerHealth)
  print("")

print("Thanks for playing! Let's try a harder cog!")
print("")
print("Yikes! A Corporate Raider!")
print("Your health: 65")
print("")

cogHealth = 100
playerHealth = 65
pie = 24
flower = 12
anvil = 36

pieStorage = 6
flowerStorage = 7
anvilStorage = 5

while cogHealth > 0 and playerHealth > 0:
  print("Pies in inventory: ", pieStorage)
  print("Flowers in inventory: ", flowerStorage)
  print("Anvils in inventory: ", anvilStorage)
  print("")
  cogAttack = random.random()
  playerMove = input("Type 'pie' (medium accuracy, medium power), 'flower' (high accuracy, low power), or 'anvil' (low accuracy, high power). ")
  print("")

  if playerMove == "pie":
    hit = random.random()
    if pieStorage > 0:
      pieStorage = pieStorage - 1
      if hit > 0.4:
        cogHealth = cogHealth - pie
        print("The pie hit! -24")
      else:
        print("You missed!")
    else:
      print("")
      print("You are out of pies!")
      print("")

  if playerMove == "flower":
    hit = random.random()
    if flowerStorage > 0:
      flowerStorage = flowerStorage - 1
      if hit > 0.1:
        cogHealth = cogHealth - flower
        print("The flower hit! -12")
      else:
        print("You missed!")
    else:
      print("")
      print("You are out of flowers!")
      print("")

  if playerMove == "anvil":
    hit = random.random()
    if anvilStorage > 0:
      anvilStorage = anvilStorage - 1
      if hit > 0.7:
        cogHealth = cogHealth - anvil
        print("The anvil hit! -36")
      else:
        print("You missed!")
    else:
      print("")
      print("You are out of anvils!")
      print("")

  if cogAttack >= 0.75:
    hit = random.random()
    if hit >= 0.75:
      playerHealth = playerHealth - 4
      print("The cog played Rolodex! -4")
    else:
      print("The cog missed!")

  if cogAttack >= 0.50 and cogAttack < 0.75:
    hit = random.random()
    if hit >= 0.75:
      playerHealth = playerHealth - 8
      print("The cog played Paper Cut! -8")
    else:
      print("The cog missed!")

  if cogAttack >= 0 and cogAttack < 0.50:
    hit = random.random()
    if hit >= 0.25:
      playerHealth = playerHealth - 6
      print("The cog played Paperwork! -6")
    else:
      print("The cog missed!")

  if playerHealth <= 0:
    print("You went sad!")
    break

  if cogHealth <= 0:
    print("You beat the cog!")
    break

  print("")
  print("Cog: ", cogHealth)
  print("Player: ", playerHealth)
  print("")

# Game concludes

print("")
print("Thanks for playing the ToonTown Python battle emulator!")
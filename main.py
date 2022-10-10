print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

cross_road = input("You come at a crossroad. Which direction would you go? Right or Left? ").lower()

if cross_road == "left":
  print("Good choice. On to the next step!")
  river = input("You get to a lake with an island in the middle. Would you wait for a boat to come or swim across the lake? Type 'wait' or 'swim'. ").lower()
  if river == "wait":
    print("Patience is key. You made it to the island. ")
    door_choice = input("You arrive at a house with 3 doors. One red, one yellow, and one blue. Which door would you choose? ").lower()
    if door_choice == "yellow":
      print("Let's gooooo! You found the treasure! ")
    elif door_choice == "blue":
      print("Ouch! The beast got your ass. Game Over Buddy!")
    elif door_choice == "red":
      print("Shiiit!! You got toasted by an outragoues fire. Game Over! ")
    else:
      print("Time ran out! Someone beat you to the treasure. Game Over! ")
  else:
    print("Damn! You were attacked by a Piranha that left you dead at the bottom of the lake. Game Over, I guess. ")
else:
  print("Oops, you fell into a hole. Game Over!")
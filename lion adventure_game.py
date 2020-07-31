import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
spear = 0
flower = 0

required = ("\nUse only A, B, or C\n") 

#The story is broken into sections, starting with "intro"
def intro():
  print ("After a heavy night work in office, you awaken the "
  "next morning in a thick, dank forest.  " 
  " you stand and observe at your new, "
  "unfamiliar place. The silence quickly fades when you hear a "
  "loud roaring sound coming behind you. A hungry lion is "
  "running towards you. You will:")
  time.sleep(1)
  print ("""  A. Grab a nearby rock and throw it at the lion
  B. Lie down and wait for lion
  C. Run""")
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_rock()
  elif choice in answer_B:
    print ("\nWelp, you are a fool. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_run()
  else:
    print (required)
    intro()

def option_rock(): 
  print ("\nThe lion is stunned, but regains control. He begins "
  "running towards you again. Will you:")
  time.sleep(1)
  print ("""  A. Run
  B. Throw another rock
  C. Run towards a nearby cave""")
  choice = input(">>> ")
  if choice in answer_A:
    option_run()
  elif choice in answer_B:
    print ("\nYou decided to throw another rock, as if the first " 
    "rock thrown did much damage. The rock flew well over the "
    "lion head. You missed. \n\nYou died!")
  elif choice in answer_C:
    option_cave()
  else:
    print (required)
    option_rock()

def option_cave():
  print ("\nYou were hesitant, since the cave was dark and "
  "dread. Before you fully enter, you notice a shiny spear on "
  "the ground. Do you pick up a spear. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    sword = 1 #adds a spear
  else:
    spear= 0
  print ("\nWhat do you do next?")
  time.sleep(1)
  print ("""  A. Hide in silence
  B. Fight
  C. Run""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nReally? You're going to hide in the dark? I think "
    "lion can see very well in the dark, right? Not sure, but "
    "for me it is YES, so...\n\nYou died!")
  elif choice in answer_B:
   if spear > 0:
    print ("\nYou laid in wait. The shining spear attracted "
    "the lion, which thought you were no match. As he walked "
    "closer and closer, your heart beat increases rapidly. As the lion "
    "reached out to grab the spear, you pierced the blade into "
    "its chest. \n\nYou survived!")
   else: #If the user didn't grab the spear
     print ("\nYou should have picked up that spear. You're "
     "defenseless. \n\nYou died!")
  elif choice in answer_C:
    print ("As the lion enters the dark cave, you sliently "
    "sneak out. You're several feet away, but the lion turns "
    "around and sees you running.")
    option_run()
  else:
    print (required)
    option_cave()

def option_run():
  print ("\nYou run as quickly as possible, but the lion's "
  "speed is too great. You will:")
  time.sleep(1)
  print ("""  A. Hide behind boulder
  B. Trapped, so you fight
  C. Run towards an abandoned village""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("You're easily spotted. "
    "\n\nYou died!")
  elif choice in answer_B:
    print ("\nYou're no match for an lion. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_village()
  else:
    print (required)
    option_run()
    
def option_village():
  print ("\nWhile frantically running, you notice a rusted "
  "spear lying in the mud. You quickly reach down and grab it, "
  "but miss. You try to calm your heavy breathing as you hide "
  "behind a delapitated building, waiting for the lion to come "
  "charging around the corner. You notice a purple flower "
  "near your foot. Do you pick it up? Y/N")
  choice = input(">>> ")
  if choice in yes:
    flower = 1 #adds a flower
  else:
    flower = 0
  print ("You hear its heavy footsteps and ready yourself for "
  "the impending lion.")
  time.sleep(1)
  if flower > 0:
    print ("\nYou quickly hold out the purple flower, somehow "
    "hoping it will stop the lion. It does! The lion was looking "
    "for love. "
    "\n\nThis got weird, but you survived!")
  else: #If the user didn't grab the spear
     print ("\nMaybe you should have picked up the flower. "
     "\n\nYou died!")

intro()
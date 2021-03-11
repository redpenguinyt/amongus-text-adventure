import random,sys,time

def type1(text, delay=0.01):
  for i in text:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(delay)
  time.sleep(0.5)
  print()

def type1input(text):
  type1(text)
  return input("")

def getName():
  name = type1input("What is your name?")
  if name.lower() == "bubblegum":
    type1("What are you doing, you impostor?")
    name = getName()
  elif name.lower() == "player":
    type1("The True Name")
  elif name.lower() == "bobdafish":
    type1("I'm your best friend, bruh. Why dont you choose your own name, huh?")
    name = getName()
  elif name.lower() == "impostor":
    type1("You're a crewmate")
    name = getName()
  elif name.lower() == "mr cheese":
    type1("I'm the one that always dies. Please don't choose my name :(")
    name = getName()
  elif name.lower() == "timothy":
    type1("That is my name and my name only. Get your OWN name (I'm the creator by the way).")
    name = getName()
  return name
name = getName()

def impostorVotedOut():
  print(". 　　　。　　　　•　 　ﾟ　　。 　　.")
  print("　　　.　　　 　　.　　　　　。　　 。　. 　")
  print(".　　 。　　　　　 ඞ 。 . 　　 • 　　　　•")
  type1("　　ﾟ　　 bubblegum was The Impostor.　 。　.")
  print("　　'　　　             　 　　。")
  print("　　ﾟ　　　.　　　. ,　　　　.　 .")

def youVotedOut():
  print(". 　　　。　　　　•　 　ﾟ　　。 　　.")
  print("　　　.　　　 　　.　　　　　。　　 。　. 　")
  print(".　　 。　　　　　 ඞ 。 . 　　 • 　　　　•")
  text = "　　ﾟ　　 " + name + " was not The Impostor.　 。　."
  type1(text)
  type1("　　'　　　 1 Impostor remains 　 　　。")
  print("　　ﾟ　　　.　　　. ,　　　　.　 .")

def endings(ending):
  if ending == "betrayed":
    type1("You got the Betrayal ending!")
    youVotedOut()
  elif ending == "true":
    impostorVotedOut()
    type1("You got the true ending! Here's a medal!")
    print(" _______________")
    print("|@@@@|     |####|")
    print("|@@@@|     |####|")
    print("|@@@@|     |####|")
    print("\@@@@|     |####/")
    print(" \@@@|     |###/")
    print("  `@@|_____|##'")
    print("       (O)")
    print("    .-'''''-.")
    print("  .'  * * *  `.")
    print(" :  *       *  :")
    print(": ~  T R U E  ~ :")
    print(": ~E N D I N G~ :")
    print(" :  *       *  :")
    print("  `.  * * *  .'")
    print("    `-.....-'")
  elif ending == "somehow":
    impostorVotedOut()
    type1("...",0.5)
    type1("Uhh, ok? You got the Somehow Ending!")
    type1("¯\_(ツ)_/¯")
  elif ending == "evil":
    print(". 　　　。　　　　•　 　ﾟ　　。 　　.")
    print("　　　.　　　 　　.　　　　　。　　 。　. 　")
    print(".　　 。　　　　　 ඞ 。 . 　　 • 　　　　•")
    type1("　　ﾟ　　 bubblegum was not The Impostor.　 。　.")
    print("　　'　　　             　 　　。")
    print("　　ﾟ　　　.　　　. ,　　　　.　 .")
    print("")
    type1("As it turns out, it was you all along! You successfully kill/yeet everyone from MIR HQ, and achieve your goal of eradicating MIR Corp. The end.")
    print("   ,    ,    /\   /\ ")
    print("  /( /\ )\  _\ \_/ /_")
    print("  |\_||_/| < \_   _/ >")
    print("  \______/  \|0   0|/")
    print("    _\/_   _(_  ^  _)_")
    print("   ( () ) /`\|V\"\"\"V|/`\ ")
    print("     {}   \  \_____/  /")
    print("     ()   /\   )=(   /\ ")
    print("     {}  /  \_/\=/\_/  \ ")
    type1("You got The Evil Ending!")
  elif ending == "secret":
    impostorVotedOut()
    type1("Well done! You got The Secret Ending!")
    type1("...",1.5)
    if random.randint(1,5) != 1:
      type1("Not much to say about it")
  elif ending == "infinity":
    print(" _        __ _       _ _         ")
    print("(_)      / _(_)     (_) |        ")
    print(" _ _ __ | |_ _ _ __  _| |_ _   _ ")
    print("| | '_ \|  _| | '_ \| | __| | | |")
    print("| | | | | | | | | | | | |_| |_| |")
    print("|_|_| |_|_| |_|_| |_|_|\__|\__, |")
    print("                            __/ |")
    print("                           |___/")
    type1("You got the infinity ending! Since you wanted this ending so much, have it again!")
    endings("infinity")
  exit()

def meetingCalled(whereFrom,score):
  print("")
  print("*************************")
  type1("A Meeting has been called")
  print("*************************")
  print("")

  type1("Everyone arrives at the meeting table to discuss what happened")
  if whereFrom == "d":
    type1("You say: \"I believe that bubblegum is the impostor! They have been venting all over the place!\"")
    type1("mr cheese says: \"Do we have actual proof?\"")
    choice = type1input("what proof will you provide, they vented(v), you saw them acting sus on doorlogs(d), or tell them to just trust you(t)?").lower()
    if choice == "v":
      type1("You say \"I saw them vent!\"")
      type1("bobdafish is confused. He was with you the whole time, and he never saw anyone vent. You're acting kinda sus! Everyone votes for you, even though you did a medbay scan")
      endings("betrayal")
    elif choice == "d":
      type1("You say \"I saw them acting sus on doorlogs!\"")
      type1("bobdafish backs you up, and everyone votes for bubblegum")
      endings("evil")
    elif choice == "t":
      type1("You say \"Just trust me!\"")
      type1("The other crewmates look at each other...")
      if random.randint(1,3) == 1:
        type1("and vote for you. You got voted out, even though you scanned earlier.")
        endings("betrayed")
      else:
        type1("and vote for bubblegum! He gets voted out, even though all you said was trust me")
        endings("somehow")
    else:
      type1("You said nothing. Since you were accusing bubblegum without backing up your claim, everyone voted for you, despite you scanning previously")
      endings("betrayed")

  elif whereFrom == "o":
    if score == 3:
      type1("You say: \"I found a body in office! I then searched for culprits and saw bubblegum venting\"")
      text = "bobdafish says: \"I can back up " + name + ", they scanned, lots of us saw\""
      type1(text)
      type1("everyone obviously voted bubblegum, except bubblegum, who skipped.")
      endings("true")
    else:
      type1("You say: \"I found a body in office. Didn't see anyone\"")
      type1("bubblegum asks \"Any sus?\", which is weird, because why would you be sussing anyone?")
      choice = type1input("Who are you voting? bubblegum(b), yourself(m), or skip(s)?").lower()
      if choice == "b":
        type1("You voted for bubblegum.")
        
        endings("somehow")
      elif choice == "m":
        type1("You voted for yourself. A bunch of other people also voted for you.")
        youVotedOut()
        exit()
      elif choice == "s":
        type1("You skipped")
        whereToGo(score)

def goDoorlogs(score,isAgain):
  if isAgain:
    randomText = random.randint(1,11)
    if randomText == 1:
      type1("Stop coming back!")
    elif randomText == 2:
      type1("Stop it!")
    elif randomText == 3:
      type1("I'm warning you!")
    elif randomText == 4:
      type1("What do you want from me? D:")
    elif randomText == 5:
      type1("What are you doing?")
    elif randomText == 6:
      type1("Subscribe to Red Penguin!")
      type1("and PikaRules!",0.1)
    elif randomText == 7:
      type1("JUST STOP!")
    elif randomText == 8:
      type1("GO BACK")
    elif randomText == 9:
      type1("STOOP IIT")
    elif randomText == 10:
      type1("ALRIGHT! Fine, I'll give you an ending.")
      endings("infinity")
    whereToGo(score,True)
  
  elif score == 1:
    type1("There is nothing new. You go back")
    whereToGo(score,True)
  elif score != 2:
    type1("While watching doorlogs, you spot something weird. Your friend bubblegum has gone to the North area, then suddenly appeared at the South-West area.")
    if type1input("What do you do? Ignore it(i), or call a meeting(m)?") == "i":
      score = 1
      type1("You head back to the launchpad to check the diagnostics of the spaceship.")
      whereToGo(score)
    else:
      type1("As you run to call a meeting, you see bubblegum ahead of you.")
      choice = type1input("What do you do? Confront him(c), keep walking(w), or run(r)?")
      if choice == "c":
        type1("As you walk up to bubblegum, his stomach opens up, revealing the greusome truth! Bubblegum is the evil alien traitor! This is your last thought as you are eaten alive, never to be seen again.")
        exit()
      elif choice == "w":
        type1("As you walk past, you feel something in your chest. A knife! You turn to look at bubblegum. His face appears to show no emotion, before you fall unconcious and die")
        exit()
      elif choice == "r":
        score = -1
        type1("Like a scaredy cat, you ran for your life")
        whereToGo(score)
      else:
        type1("you stood there, unable to decide what to do. Bubblegum stabbed you.")
        exit()
  else:
    type1("On doorlogs, along with your new friends, you see some confusing data. It says that bubblegum passed north sensor to go to office, then appeared at north west sensor coming from cafeteria.")
    if type1input("What do you do? Do nothing whastoever(n), or call a meeting(m)?") == "m":
      type1("You run to call a meeting with your friends. You press the button.")
      score = 3
      meetingCalled("d",score)
    else:
      type1("bubblegum calls a meeting and votes you out with no reasoning whatsoever.")
      youVotedOut()

def goLab(score):
  if random.randint(1,2) == 1 or score == 2:
    if score == 2:
      type1("Despite having already been at lab, you go there again")
    type1("To get to the lab, you must pass through decontamination. As you do, you see ahead of you your friend bubblegum gobbling up your friend Mr cheese! He sees you watching, then jumps in a vent")
    if type1input("What do you do? Ignore it(i) or report it(r)?") == "i":
      if score != 2:
        type1("You ignore the chunk of meat on the ground and keep heading to lab. Suddenly, your friend bobdafish turns a corner and sees you walking away from a fresh dead body. He reports the body, you are instantly voted out and thrown off the base, which is on a tall mountain by the way")
        youVotedOut()
        exit()
      else:
        type1("you ignore the meat, and keep running to lab (for no reason.)")
        type1("bobdafish comes along later, and sees bubblegum vent, who gets voted out.")
        endings("secret")
    else:
      type1("You report the body, and everyone instantly heads to the cafeteria table, confused and frightened.")
      if random.randint(1,5) == 1:
        text = "Bubblegum says \" I dunno " + name + " kinda sus\". Everyone votes you, agreeing it's a self report. Welcome to Among us. Tbh you picked a bad map to start on"
        type1(text)
        youVotedOut()
        exit()
      else:
        type1("You explain to them what you just saw, the death of mr cheese, the venting. Everyone believes you and instantly votes out bubblegum. YOU HAVE WON YOUR FIRST GAME OF AMOGN US! Plus you had some good randoms! Tbh you picked a bad map to start on tho.")
        impostorVotedOut()
        exit()

  else:
    type1("You reach lab safely (good job!). You complete your tasks and head to medbay.")
    if score != 1:
      type1("While in medbay, bubblegum vents and kills you. Lol")
      exit()
    else:
      type1("A bunch of people come in to medbay to watch you scan! You are clear!")
      score = 2
      whereToGo(score)

def goOffice(score):
  type1("You head upwards to the office, so you can upload some data. As you are uploading, the lights go out, and you realise that the fusebox is right next to you. How convienient! As you fix the lights, you find a body next to you!")
  if type1input("What do you do? Report it(r), or do not(n)?") == "n":
    if score == 2:
      type1("You don't report the body, but instead look around for the culprit, and you see bubblegum jumping into a vent! However, At that moment, bobdafish enters the room and sees you next to the body! Luckily, he saw you scan, so when he reports the body, he doesn't accuse you.")
      score = 3
      meetingCalled("o",score)
    else:
      type1("You idiot. Someone else came in and saw you next to the body. You got voted out")
      youVotedOut()
  else:
    type1("You reported the body.")
    meetingCalled("o",score)

def whereToGo(score,isEndless=False):
  if score != 2:
    location = type1input("Where do you go? Lab(l),Doorlogs(d) or Office(o)?")
  else:
    location = type1input("Where do you go? Doorlogs(d) or Office(o)?")
  if location == "d":
    goDoorlogs(score,isEndless)
  elif location == "l":
    goLab(score)
  elif location == "o":
    goOffice(score)
  elif location == "score2":
    score = 2
    type1("Your score is now 2")
    whereToGo(score)
  else:
    if random.randint(1,3) == 1:
      type1("Please select a location")
    else:
      type1("type something valid")
    whereToGo(score)


print("*************************************************")
print("              AMOGN US: MIR HQ MYSTERY")
print("*************************************************")

hello = "Hey there " + name + "!"
type1(hello)
print("Welcome to MIR HQ, the central hub for all intergalactic travels and expeditions. But something doesn't seem right. There may be a traitor in your midst! You have just arrived on The Skald, and you have refueled it at the launch pad.")
score = 0
whereToGo(score)

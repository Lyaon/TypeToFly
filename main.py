# Imports
import os
import time
import random
import colorama # Ex: print(Fore.RED + 'This text is RED in color')
from colorama import Fore, Style
#intro
print('Welcome to Type to Fly')
time.sleep(1)
print('Here you can learn how to fly or go on the flight mission!')
time.sleep(1.5)
print('Hopefully nothing bad happens...')
time.sleep(2)
os.system('clear')
while True:
  # variables
  damage = 0  # default 5
  headwinds = random.randint(0, 50)  # Used for landing/takeoff
  engine = 0
  startspeed = 0;
  headwindspercentage = headwinds / 100
  choice1save = 0
  choice1save2 = 0
  lateness = 0
  chance1 = random.randint(1, 3)
  survivalchance1 = random.randint(1,4)
  survivalchance2 = random.randint(1,3)
  runway01 = 1000
  runway02 = 1500
  runway03 = 2000
  correct = 0
  # functions
  def latenesschecker():
    if lateness >= 60:
      print(Fore.RED + "You are more than an hour behind schedule. You failed!" + Style.RESET_ALL)
      time.sleep(1.5)
    else: 
      print(Fore.GREEN + "You come in for a smooth landing and get to your family in time!" + Style.RESET_ALL)
  # Code start
  print("Flight selection engaged")
  print('1. Training')
  print('2. Flying')
  flightselection = int(input('Make a selection: '))
  # Training
  if flightselection == 1:
    print('Takeoff Training Engaged')
    print(' ')
    print('To begin you must turn on the following:')
    print('1. Battery')
    print('2. Avionics')
    print('3. APU')
    print('4. Fuel Pump')
    print('5. Starter')
    print('6. Ignition')
    print('In the future there may be choices trying to decieve you!')
    starting = input('Start the plane (e.g. 1,2,3): ')
    if starting == ('1,2,3,4,5,6'):
      print('The plane engine begins to start')
      for i in range(100):
        engine = engine + 1
        print('{}%'.format(engine))
        time.sleep(startspeed)
        if startspeed < 0.3:
          startspeed = 0.5
        else:
          startspeed = startspeed - 0.33
      print('The plane is ready to taxi!')
    else:
      print(Fore.RED + "Incorrect starting sequence, please try again" + Style.RESET_ALL)
      continue
    print("The parking break is released, and you taxi and get ready to go onto the runway.")
    print("You need to request clearance to takeoff. Use the following format to request clearance!")
    print("Tower, (your call sign which is Training 1281) requesting takeoff at runway 01.")
    takeoff = input('Request clearance: ')
    if takeoff == ('Tower, Training 1281 requesting takeoff at runway 01.'):
      print("ATC: Permission granted, have a safe flight Training 1281.")
    else:
      print(Fore.RED + 'ATC: You failed to request proper clearance and are denied clearance.' + Style.RESET_ALL)
      print('Please return to the airport')
      continue
    print("The engines throttle up and you are up up and away!")
    print("You successfully completed the takeoff training!")
    time.sleep(1)
    os.system('clear')
    # Takeoff Training
    print('Takeoff Training engaged')
    print('You begin 1000ft. in the air and slowly descending.')
    print('You need to do a number of things to land')
    print('First, request clearance to land using the previous format,')
    print('but replacing ready at Runway 01 with inbound for landing at runway 01.')
    landingreq = input('Request clearance: ')
    if landingreq == ('Tower, Training 1281 inbound for landing at runway 01.'):
      print('ATC: CleaRED for landing Training 1281.')
      print('Prepare for the following by changing the following:')
      print('1. Flaps to 10 degrees')
      print('2. Landing gear')
      print('3. Throttle to 40 percent throttle')
      landingprocedure = input('Prepare for landing: ')
      if landingprocedure == ('1,2,3'):
        print('Successfully prepaRED for landing. ')
        print('Before landing you need to learn about headwinds')
        print('This means it takes longer to stop on the runway.')
        print('For example if it normally takes 1500m to land then you need to increase it by x%')
        print('This is based on headwind. For example if there is a headwind of 10%')
        print('Then you will need 1100m to land because 1000 + 10%.')
        print(' ')
        print('Time to come in for a landing')
        print('Today there is a headwind of {}kts and it will take you 1000m to land normally'.format(headwinds))
      landinglength = int(input('It will take __ metres to stop with the headwind: '))
    # Checks if the correct length needed to land is inputted
      if landinglength == runway01 * (1 + headwindspercentage):
        print('Successfully calculate the extra length needed to stop.')
        print(' ')
        print('Fortunatly for this flight the runway is long enough')
        print('In other cases you may need to switch to a longer one!')
        print('To change runways say:')
        print('Tower, Training 1281 requesting a runway change to runway xx')
        time.sleep(1.5)
        os.system('clear')
        print('You are now ready for landing')
        print('You steadily approach and touch down with a little bounce')
        print('You now throttle down and brake and come to a nice stop!')
        print('Flight Training complete!')
        time.sleep(1.5)
        os.system('clear')
      else:
        print(Fore.RED + 'Failed to prepare for landing!' + Style.RESET_ALL)
        continue
    else:
      print(Fore.RED + 'ATC: Request failed. You are not authorized to land Training 1281.' + Style.RESET_ALL)
      continue
# Full Adventure Flight
  headwinds = random.randint(1, 20)  # Used for landing/takeoff
  engine = 0
  startspeed = 0
  visibility = random.randint(1, 100)  # See how far they can see
  headwindspercentage = headwinds / 100
  choice1save = 0
  choice1save2 = 0
  lateness = 0
  chance1 = random.randint(1, 3)
  if flightselection == 2:
    print("Flight Challenge Loading")
    time.sleep(1)
    os.system('clear')
    print("The flight begins at 0900h.")
    print("Its a nice day with a headwind of {} ".format(headwinds))
    print("You are headed to your families house for summer break.")
    print("The goal is to get there and be less than an hour late but you must survive and land safely.")
    print("Do you skip the safety checks to hurry?")
    print("1. Yes")
    print("2. No")
    choice1 = int(input("Make a choice: "))
    if choice1 == 1:
      choice1save = choice1save + 1
      print("You decide to skip the checks...")
      print("Hopefully you don't regret it!")
    if choice1 == 2: 
      time.sleep(2)
      choice1save2 = choice1save2 + 1
      lateness = lateness + 10
      print("You take the time to check but now you are late...")
      print("Hopefully it pays off!")
    print("You hop into your seat and prepare to take off!")
    print('1. Battery')
    print('2. Avionics')
    print('3. APU')
    print('4. Fuel Pump')
    print('5. Landing Gear')
    print('6. Starter')
    print('7. Ignition')
    startingsequence = input("Turn on the plane (e.g. 1,2,3): ")
    if startingsequence == ('1,2,3,4,6,7'):
      time.sleep(0.5)
      os.system('clear')
      print("Starting sequence correct")
      print("You taxi to the runway and prepare to enter onto it.")
      print("You are assigned the call sign Challenge 3223 and are at runway 01.")
      while True: 
        takeoffreq = input("Request takeoff clearance (Use hint for help): ")
        if takeoffreq == ('Tower, Challenge 3223 requesting takeoff at runway 01.'):
          print("ATC: Permission granted Challenge 3223, have a good flight.")
          print("You pull onto the runway and throttle up.")
          if choice1save == 1:
            print("The plane lifts off and you think you pull up the landing gear.")
          break
        if takeoffreq == ('hint'):
          time.sleep(1)
          os.system('clear')
          print("Try saying: Tower, Challenge 3223 requesting takeoff at runway 01.")
          continue
        else:
          print("Invalid takeoff request")
      print("You continue to rise into the clouds...")
      time.sleep(1)
      print("1000ft")
      time.sleep(1.5)
      print("2000ft")
      time.sleep(1.5)
      print("3000ft")
      time.sleep(1.5)
      print("4000ft")
      time.sleep(1.5)
      print("5000ft")
      time.sleep(1)
      print("6000ft")
      time.sleep(1.5)
      print("7000ft")
      time.sleep(1.5)
      print("8000ft")
      time.sleep(1.5)
      print("9000ft")
      time.sleep(1.5)
      print("10000ft")
      if chance1 < 2:
        print("You successfully reach cruising altitude,")
        print("But the winds were not in your favour and it took longer than expected")
        print("You are now further delayed")
        lateness = lateness + 12
      else: 
        print("You successfully reach cruising altitude without many issues...")
      print("As you pop out of the clouds you see a massive dark cloud ahead that you hadnt seen before.")
      print("You are currently {} minutes behind schedule.".format(lateness))
      print("You will cut your time in half if you go through it but run the risk of damage ")
      print("Do you go through?")
      print("1. Yes")
      print("2. No")
      choice2 = int(input("Make a choice: "))
      if choice2 == 1:
        lateness = lateness / 2
        damage = damage + 30
        print("It is a horrible fight to get through the storm clouds!")
        time.sleep(1.5)
        print("The wind is blowing hard")
        print("You are struggling to keep the plane up and you plummit 2500ft.")
        print("You get to the eye of the storm and manage to level off")
        print(" ")
        if choice1save == 1: 
          print("All of a sudden you hear a loud crack...")
          time.sleep(1)
          print("And warning lights start to flash")
          time.sleep(1)
          print("Your landing gear failed because you skipped the checks.")
          print("It will now be a struggle to land...")
          time.sleep(1)
          print(" ")
          print("Should you try to land nearby or continue to your family?")
          print("Do you continue travelling?")
          print("1. Yes")
          print("2. No")
          choice3 = int(input("Make a choice: "))
          if choice3 == 1: 
            print("You decide to risk it and continue flying towards Vancouver")
          if choice3 == 2: 
            print("You decide to play it safe and take the safe route")
            print("You come in for a landing at the nearest airport")
            print(Fore.RED + "You have failed the goal to get to your family in time." + Style.RESET_ALL)
            time.sleep(1.5)
            continue
        if choice1save == 0:
          print("You gave yourself quite a scare going through the storm")
      if choice2 == 2:
        lateness + 20
        print("You go the safe route but it delays you by another 20 minutes.")
      os.system('clear')
      print("You finally are back on course with a few bumps and bruises")
      print("As you break free of storm the sun is shining. You are finally going to make it!")
      time.sleep(1)
      print(" ")
      print("The sun...")
      print("Its shining in your eyes...")
      print("You are struggling to see and can't fly the plane!")
      print("To try and see again you have to blindly go up or down to block out the sun")
      print("1. Go up")
      print("2. Go down")
      choice4 = int(input("Make a choice: "))
      if choice4 == 1: 
        print("You choose to pull up")
        print("By doing this you lose alot of your airspeed and start to stall...")
        print("You fall into a spin and just manage to pull out of it at 500ft")
      if choice4 == 2: 
        print("You decend down and regain your sight but you gain alot of speed and pull up to hard...")
        print("This causes strain on the aircraft and slightly damages the airplane...")
        damage = damage + 10
      time.sleep(1.5)
      os.system('clear')
      print("You get back up to your cruising alititude with the sun no longer in your eyes")
      print("and continue on your flight")
      time.sleep(1.5)
      print(" ")
      # Plays the emergency landing scenario
      if damage >= 30: 
        print("All of a sudden your engine starts to sputter")
        print("You look at the fuel guage and see it is almost empty")
        if choice2 == 1: 
          print("Apparently when you flew into the storm it punctuRED your fuel tank")
        else: 
          print("You are not totally sure what happened but it is still a problem")
        print("You have to make an emergency landing")
        print("You might be able to glide to vancouver but it would be risky and the chance of fail is high")
        print("Or you could find a place below you and most likely survive")
        print("Do you try and land nearby? Or try and make it to Vancouver")
        print("1. Yes")
        print("2. No")
        choice5 = int(input("Make a choice: "))
        if choice5 == 1:
          print("You decide to land close by")
          print("You look below and see the following: ")
          print("1. Field")
          print("2. Forest")
          print("3. Flat mountainous terrain")
          print("4. Calm lake")
          choice6 = int(input("Make a choice: "))
          if choice6 == 1:
            print("You choose the field and it has a very high chance of success")
            if survivalchance1 <= 3:
              print(Fore.GREEN + "You touch down softly in the field and are unharmed. It takes a while but someone finds you and you are home safe!" + Style.RESET_ALL)
              continue
            else: 
              print("While the field had a good chance you got unlucky and crashed")
              print(Fore.RED + "There was no hope for survival" + Style.RESET_ALL)
              continue
          if choice6 == 2:
            print("You choose the forest and has a low chance of success")
            if survivalchance2 < 2: 
              print("Somehow you survived the odds and survive the landing")
              print(Fore.GREEN + "Your crash is very obvious so someone finds you quickly and you survive!" + Style.RESET_ALL)
              continue
            else: 
              print(Fore.RED + "The odds weren't good anyway and you sadly didnt make it" + Style.RESET_ALL)
              continue
          if choice6 == 3:
            print("You choose to land on a mountain which is risky but atleast its flat")
            if survivalchance2 <= 2:
              print("An interesting choice but it pays off. You crash on a tall mountain")
              print(Fore.GREEN + "Its easy to see and you are quickly found and saved!" + Style.RESET_ALL)
              continue
            else: 
              print(Fore.RED + "Landing on a mountain is difficult and you didn't make it" + Style.RESET_ALL)
              continue
          if choice6 == 4:
            print("You choose to land on a lake which has a 50/50 chance of survival")
            if survivalchance1 <= 2: 
              print("You head for the lake and somehow survive")
              print(Fore.GREEN + "It takes a few hours but someone finds you and you survive" + Style.RESET_ALL)
            else: 
              print(Fore.RED + "It was a gamble and you lost")
              print("You crash into the lake and your plane crumbles and sinks to the bottom")
              print("With you still in it!")
        # instead of emergency landing you try and get to Vancouver, there is a 1/3
        if choice5 == 2:
          print("You decide to try and make it to Vancouver")
          if chance1 < 2:
            print("You  made it!")
            print("You now must select a runway before declaring your landing")
            print("Today the headwind is {}kts. Remember your training!".format(headwinds))
            print("Currently you are looking at Runway 01 which is {}m long".format(runway01))
            runwaylength = int(input("Enter the length needed to land: "))
            if runwaylength == runway01 * (1 + headwindspercentage):
              # if runway 1 is to short
              if runwaylength > runway01:
                correct = correct + 1
                print("You successfully calculated the distance")
                print("But the runway is to short")
                print("Select another runway")
                print("1. Runway 02")
                print("2. Runway 03")
                # runway 2 or 3 selector
                runwayselect = int(input("Make a selection: "))
                # runway 2 selector. Checks to see if it is long enough if they got the previous question right. 
                if runwayselect == 1:
                  print("You select Runway 02 which is {}m long.".format(runway02))
                  if correct == 1: 
                    # asks the user if they think the runway will be long enough
                    tf1 = input("Will this runway work (Enter y or n): ")
                    if tf1 == ('y') and runwaylength <= runway02:
                      print("The runway will work!")
                    if tf1 == ('n'):
                      print("You decide to select Runway 03")
                      print("Because the other 2 arent long enough.")
                # Runway 03 select. ** is readying for landing request **
                if runwayselect == 2: 
                  print("You select Runway 03 which is {}m long.".format(runway03))
                  print("It is long enough so you are ready to land")
              # basic response if the calculations and runways are long enough. ** Needs the landing request to continue
              if runwaylength <= runway01: 
                print("The runway length is long enough!")
                print("you are clear to come in for a landing!")
            else: 
              print("Incorrect landing length")
              continue
            # landing request for all runways 
              print("You now must declare your landing: ")
            while True: 
              landingdeclare1 = input("Declare your landing (Type hint for help): ")
              if landingdeclare1 == ("Tower, Challenge 3223 inbound for landing at runway 01."):
                break
                print("You successfully requested landing at runway 01!")
              if landingdeclare1 == ("Tower, Challenge 3223 inbound for landing at runway 02."):
                break
                print("You successfully reuqested landing at runway 02!")
              if landingdeclare1 == ("Tower, Challenge 3223 inbound for landing at runway 03."):
                break
                print("you successfully requested landing at runway 03!")
              if landingdeclare1 == ("hint"):
                print("Try saying Tower, Challenge 3223 inbound for landing at runway(put your runway number)")
                continue
              else: 
                print(Fore.RED + "You failed to properly request landing and were denied landing." + Style.RESET_ALL)
                continue
            else: 
              print(Fore.RED + "You incorrectly prepaRED for landing, got distracted and crashed!" + Style.RESET_ALL)
              continue
          else: 
            print(Fore.RED + "You couldn't quite make it to Vancouver and crashed" + Style.RESET_ALL)
            continue
      # The final else if everything else is good and there isnt to much damage this will trigger
      else: 
        print("You  made it!")
        print("You have lined up with the runway and are starting to descend")
        print("First you need to prepare your controls.")
        print("1. Landing Gear")
        print("2. Flaps")
        print("3. Reading Light")
        print("4. Throttle Down")
        print("5. Windshield Wipers")
        choice6 = input("Prepare for landing (e.g. 1,2,3): ")
        if choice6 == ('1,2,4'):
          print("You successfully prepaRED for landing!")
          print(" ")
          print("You now must select a runway before declaring your landing")
          print("Today the headwind is {}kts. Remember your training!".format(headwinds))
          print("Currently you are looking at Runway 01 which is {}m long".format(runway01))
          runwaylength = int(input("Enter the length needed to land: "))
          if runwaylength == runway01 * (1 + headwindspercentage):
            # if runway 1 is to short
            if runway01 < runwaylength:
              correct = correct + 1
              print("You successfully calculated the distance")
              print("But the runway is to short")
              print("Select another runway")
              print("1. Runway 02")
              print("2. Runway 03")
              # runway 2 or 3 selector
              runwayselect = int(input("Make a selection: "))
              # runway 2 selector. Checks to see if it is long enough if they got the previous question right. 
              if runwayselect == 1:
                print("You select Runway 02 which is {}m long.".format(runway02))
                if correct == 1: 
                  # asks the user if they think the runway will be long enough
                  tf1 = input("Will this runway work (Enter y or n): ")
                  if tf1 == ('y') and runwaylength <= runway02:
                    print("The runway will work!")
                  elif tf1 == ('n'):
                    print("You decide to select Runway 03")
                    print("Because the other 2 arent long enough.")
              # Runway 03 select. ** is readying for landing request **
              if runwayselect == 2: 
                print("You select Runway 03 which is {}m long.".format(runway03))
                print("It is long enough so you are ready to land")
            # basic response if the calculations and runways are long enough. ** Needs the landing request to continue
            if runwaylength <= runway01: 
              print("The runway length is long enough!")
              print("you are clear to come in for a landing!")
          # landing request for all runways 
          print("You now must declare your landing")
          while True: 
            landingdeclare1 = input("Declare your landing (Type hint for help): ")
            if landingdeclare1 == ("Tower, Challenge 3223 inbound for landing at runway 01."):
              print("You successfully requested landing at runway 01!")
              latenesschecker()
              # breaks this out of loop and continue is for completling mission. Same for all
              break
              continue
            if landingdeclare1 == ("Tower, Challenge 3223 inbound for landing at runway 02."):
              print("You successfully requested landing at runway 02!")
              latenesschecker()
              break
              continue
            if landingdeclare1 == ("Tower, Challenge 3223 inbound for landing at runway 03."):
              print("you successfully requested landing at runway 03!")
              latenesschecker()
              break
              continue
            # final landing hint
            if landingdeclare1 == ("hint"):
              print("Try saying Tower, Challenge 3223 inbound for landing at runway(put your runway number)")
              continue
            # landing request fail
            else: 
              print(Fore.RED + "You failed to properly request landing and were denied landing." + Style.RESET_ALL)
              continue
        # mission failed to prepare error
        else:
          print(Fore.RED + "You incorrectly prepaRED for landing, got distracted and crashed!" + Style.RESET_ALL)
          continue
    # mission starting sequence fail
    else:
      print(Fore.RED + "Incorrect starting sequence" + Style.RESET_ALL)
      continue

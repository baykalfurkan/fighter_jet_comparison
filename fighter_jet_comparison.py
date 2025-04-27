# -*- coding: utf-8 -*-

from lists import *

print("Welcome to dogfight comparison software.")


while True:
    choice = input('\nWhich one will you compare ?(modern/ww2): ')

    if choice == 'modern':
      
       for kod, ad in modernPlanes.items():
          print(f"-{ad} ({kod})")
       c2f1 = input("\nFirst fighter jet: ")
       c2f2 = input("Second fighter jet: ")
       choice2 = input("\n-BVR Rating (bvr)\n-Armament rating (arm)\n-Technology rating (tech)\n-Avionics rating (avio)\n-Maneuverability rating (manev)\n-Thrust/Weight (tw)\n-speed _mach_\n-Fuel Economy _km/l_ (fuele)\n-cost _$_\n-Dogfight Rating (rate)\n-Radar Cross Section max _m^2_ (rcs)\n-power _k lbf_ \n-Flight Cost Per Hour _$_ (fcph)\n\nWhich feature do you want to compare: ")
       

       if c2f1 not in planes or c2f2 not in planes:
          print("One or more of the planes are not registered.")
          continue

       if choice2 not in planes[c2f1].__dict__:
          print("The property you entered is not registered.")
          continue


       plane1_value = planes[c2f1].__dict__[choice2]
       plane2_value = planes[c2f2].__dict__[choice2]

       if choice2 == "cost" or choice2 == "rcs" or choice2 == "fcph" or choice2 == "fuele":
           if plane1_value > plane2_value:
             print(f"--> {c2f2} is better than {c2f1} in terms of {choice2}. ({plane2_value}/{plane1_value}) <--")
           else:
              print(f"--> {c2f1} is better than {c2f2} in terms of {choice2}. ({plane1_value}/{plane2_value}) <--")

       else:
           if plane1_value > plane2_value:
                print(f"--> {c2f1} is better than {c2f2} in terms of {choice2}. ({plane1_value}/{plane2_value}) <--")
           elif plane1_value < plane2_value:
                print(f"--> {c2f2} is better than {c2f1} in terms of {choice2}. ({plane2_value}/{plane1_value}) <--")
           else:
                print(f"--> {c2f1} and {c2f1} are equal in terms of {choice2}. <--")
       


    elif choice == 'ww2':
   
       for kod, ad in ww2Planes.items():
          print(f"-{ad} ({kod})")
       c3f1 = input("\nFirst fighter: ")
       c3f2 = input("Second fighter: ")
       choice3 = str(input("\n-Number built (number)\n-Turn Radius _Full flaps_ (tradius)\n-Speed/Accele./Agility pts (saa)\n-Min Power/mass _hp/kg_ (minpm)\n-Max Power/mass _hp/kg_ (maxpm)\n-Climb Rate _ft/min_ (crate)\n-Max. Take Off _kg_ (maxtoff)\n-Engine Power _hp_ (epower)\n-Max Speed _kmh_ (mspeedkm)\n-Max Speed _mach_ (msppedm)\n-Max Range _km_ (mrange)\n-Service Ceiling _ft_ (sceiling)\n\nWhich feature do you want to compare: "))
       
       if c3f1 not in planes or c3f2 not in planes:
          print("One or more of the planes are not registered.")
          continue

       if choice3 not in planes[c3f1].__dict__:
          print("The property you entered is not registered.")
          continue


       plane1_value = planes[c3f1].__dict__[choice3]
       plane2_value = planes[c3f2].__dict__[choice3]

       if choice3 == "tradius" :
           if plane1_value > plane2_value:
             print(f"--> {c3f2} is better than {c3f1} in terms of {choice3}. ({plane2_value}/{plane1_value}) <--")
           else:
              print(f"--> {c3f1} is better than {c3f2} in terms of {choice3}. ({plane1_value}/{plane2_value}) <--")

       elif choice3 == "minpm" or choice3 == "maxpm":
           print(f"--> {c3f1} {choice3} is {plane1_value},\n    {c3f2} {choice3} is {plane2_value} <-- ")

       else:
           if plane1_value > plane2_value:
                print(f"--> {c3f1} is better than {c3f2} in terms of {choice3}. ({plane1_value}/{plane2_value}) <--")
           elif plane1_value < plane2_value:
                print(f"--> {c3f2} is better than {c3f1} in terms of {choice3}. ({plane2_value}/{plane1_value}) <--")
           else:
                print(f"--> {c3f1} and {c3f1} are equal in terms of {choice3}. <--")
   
    else:
       print("\nYou entered a wrong value!")
       continue
   
   
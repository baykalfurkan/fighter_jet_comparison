
# -*- coding: utf-8 -*-

class MFighter():
   
   Fighter = "Modern"

   def  __init__(self, bvr, arm, tech, avio, manev, tw, speed, fuele, cost, orign, rate, rcs, power, fcph):
      self.bvr = bvr            #BVR Rating                 % 
      self.arm = arm            #Armament rating           x/10
      self.tech = tech          #Technology rating          "
      self.avio = avio          #Avionics rating            "
      self.manev = manev        #Maneuverability rating     "
      self.tw = tw              #Thrust/Weight
      self.speed = speed        #                          mach
      self.fuele = fuele        #Fuel Economy              km/l 
      self.cost = cost          #                           $
      self.orign = orign        #AAM origin
      self.rate = rate          #Dogfight Rating            %
      self.rcs = rcs            #Radar Cross Section max    m^2
      self.power = power        #                          k lbf
      self.fcph = fcph          #Flight Cost Per Hour       $
 


class WFighter():
   
   Fighter = "WW2"
   
   def  __init__(self, country, type, number, tradius, saa, minpm, maxpm, crate, maxtoff, epower, mspeedkm, mspeedm, mrange ,sceiling):
      self.country = country      #
      self.type = type            #Type of aircraft
      self.number = number        #Number built
      self.tradius = tradius      #Turn Radius (Full flaps)
      self.saa = saa              #Speed/Accele./Agility pts
      self.minpm = minpm          #Min Power/mass                (hp/kg)
      self.maxpm = maxpm          #Max Power/mass                (hp/kg)
      self.crate = crate          #Climb Rate                   (ft/min)
      self.maxtoff = maxtoff      #Max. Take Off                  (kg)
      self.epower = epower        #Engine Power                   (hp)
      self.msppedkm = mspeedkm    #Max Speed                     (km/h)
      self.mspeedm = mspeedm      #Max Speed                     (Mach)
      self.mrange = mrange        #Max Range                      (km)
      self.sceiling = sceiling    #Service Ceiling                (ft)
      
 


planes = {
"f35" : MFighter(94, 8.6, 9.5, 9, 8.5, 1.07, 1.60, 0.80, 1800000000, 'NATO', 70, 0.3, 43, 43200),           #F-35 LIGHTNING 2
"f16ef" : MFighter(78, 7.9, 9, 9, 7.9, 1.11, 2, 0.91, 35000000, 'NATO', 58, 1.5, 32, 12000),                #F-16E/F BLOCK 60
"f22" : MFighter(98, 8.2, 10, 9.8, 9.4, 1.26, 2.25, 0.47, 250000000, 'NATO', 86, 0.4, 35, 61200),           #F-22 RAPTOR
"fa18ef" : MFighter(83, 7.9, 8.9, 9, 7.8, 1.03, 1.80, 0.60, 80000000, 'NATO', 57, 2.5, 22, 13200),          #F/A-18E/F SUPER HORNET
"rafale" : MFighter(90,  8.6, 8.5, 8.4, 9.3, 1.13, 2, 0.70, 130000000, 'NATO', 76, 2, 17, 28000),           #Dassault Rafale
"su30" : MFighter(85, 8.4, 8, 8, 9.7, 1.05, 2, 0.25, 60000000, 'Russia', 89, 4, 27.3, 24000),               #SUKHOI SU-30
"gripen" : MFighter(81, 8, 8, 7.9, 9, 1.03, 2, 1.06, 45000000, 'NATO', 74, 1.5, 18, 7800),                  #Saab JAS-39 Gripen
"j10" : MFighter(75, 7.5, 7.5, 8, 8.6, 1.08, 2, 0.76, 35000000, 'China', 58, 1.5, 29, 4800),                #CHENGDU J-10
"su35" : MFighter(87, 8.4, 8.2, 8.3, 9.9, 1.21, 2.25, 0.20, 75000000, 'Russia', 95, 3.5, 31.4, 36000),      #SUKHOI SU-35
"f15e" : MFighter(88, 8, 9, 9, 8.2, 1.07, 2.50, 0.45, 135000000, 'NATO', 64, 3.5, 32, 32500),               #F-15E STRIKE EAGLE
"su57" : MFighter(97, 8.1, 9.3, 9.3, 10, 1.36, 2.3, 0.45, 150000000, 'Russia', 97, 0.5, 37, 45000),         #SUKHOI PAK FA
"mig35" : MFighter(83, 7.6, 8.3, 8.3, 9.6, 1.14, 2.25, 0.44, 55000000 ,'Russia', 92, 2, 19.8, 15600),       #MIG-35 FULCRUM F
"su30mki" : MFighter(86, 8.4, 8.2, 8.2, 9.7, 1.05, 2, 0.23, 65000000, 'Russia', 94, 3.5, 27.3, 23000),      #SUKHOI SU-30MKI
"su27" : MFighter(80, 8.4, 7.8, 8, 9.4, 1.05, 2, 0.26, 50000000, 'Russia', 87, 5, 27.3, 21600),             #SUKHOI SU-27
"mirage" : MFighter(68, 6.5, 6.9, 7.4, 7.1, 0.92, 2.20, 1.05, 28000000, 'NATO', 47, 2.5, 21, 8280),         #MIRAGE 2000E

"p38" : WFighter('USA', 'Heavy Fighter', 10050, 596, 54, 0.174, 0.298, 4750, 9888, 1725, 713, 0.58, 2092, 44000),      #P-38 Lightning
"fw190" : WFighter('Germany', 'Fighter', 20000, 671, 45, 0.347, 0.532, 2950, 4899, 1700, 657, 0.54, 805, 37500),       #Fw 190 Wurger
"yak3" : WFighter('USSR', 'Fighter', 4900, 516, 100, 0.412, 0.616, 3645, 3157, 1300, 665, 0.54, 661, 35040),           #Yakovlev Yak-3
"spitfire" : WFighter('UK', 'Fighter', 20350, 450, 72, 0.532, 0.687, 3650, 3856, 2050, 721, 0.59, 1770, 43450)        #Supermarine Spitfire

}

print("Welcome to dogfight comparison software.")


while True:
    choice = input('\nWhich one will you compare (modern/ww2): ')

    if choice == 'modern':
      
       print("\n-F-35 LIGHTNING 2 (f35)\n-F-16E/F BLOCK 60 (f16ef)\n-F-22 RAPTOR (f22)\n-F/A-18E/F SUPER HORNET (fa18ef)\n-Dassault Rafale (rafale)\n-SUKHOI SU-30 (su30)\n-Saab JAS-39 Gripen (gripen)\n-CHENGDU J-10 (j10)\n-SUKHOI SU-35 (su35)\n-F-15E STRIKE EAGLE (f15e)\n-SUKHOI PAK FA (su57)\n-MIG-35 FULCRUM F (mig35)\n-SUKHOI SU-30MKI (su30mki)\n-SUKHOI SU-27 (su27)\n-MIRAGE 2000E (mirage)")
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

       if property == "cost" or property == "rcs" or property == "fcph" or property == "fuele":
           if plane1_value > plane2_value:
             print(f"--> {c2f1} is better than {c2f2} in terms of {choice2}. <--")
           else:
              print(f"--> {c2f2} is better than {c2f1} in terms of {choice2}. <--")

       else:
           if plane1_value > plane2_value:
                print(f"--> {c2f1} is better than {c2f2} in terms of {choice2}. <--")
           elif plane1_value < plane2_value:
                print(f"--> {c2f2} is better than {c2f1} in terms of {choice2}. <--")
           else:
                print(f"--> {c2f1} and {c2f1} are equal in terms of {choice2}. <--")
       


    elif choice == 'ww2':
   
       print("\n-P-38 Lightning (p38)\n-Fw 190 Wurger (fw190)\n-Yakovlev Yak-3 (yak3)\n-Supermarine Spitfire (spitfire)")
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

       if property == "cost" or property == "rcs" or property == "fcph" or property == "fuele":
           if plane1_value > plane2_value:
             print(f"--> {c3f1} is better than {c3f2} in terms of {choice3}. <--")
           else:
              print(f"--> {c3f2} is better than {c3f1} in terms of {choice3}. <--")

       else:
           if plane1_value > plane2_value:
                print(f"--> {c3f1} is better than {c3f2} in terms of {choice3}. <--")
           elif plane1_value < plane2_value:
                print(f"--> {c3f2} is better than {c3f1} in terms of {choice3}. <--")
           else:
                print(f"--> {c3f1} and {c3f1} are equal in terms of {choice3}. <--")
   
    else:
       print("\nYou entered a wrong value!")
       continue
   
   
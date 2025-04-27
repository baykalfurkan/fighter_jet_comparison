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
"spitfire" : WFighter('UK', 'Fighter', 20350, 450, 72, 0.532, 0.687, 3650, 3856, 2050, 721, 0.59, 1770, 43450),        #Supermarine Spitfire
"p40" : WFighter('USA', 'Fighter', 13800, 497 ,97 ,0.283, 0.401, 2500, 4057, 1150, 579, 0.47, 1046, 29000),            #P-40 Warhawk
"p51" : WFighter('USA', 'Fighter-Bomber', 16000, 633 ,59 ,0.316, 0.497, 3200, 5443, 1720, 703, 0.57, 2655, 42000),     #P-51 Mustang
"bf109" : WFighter('USA', 'MR Fighter', 34000, 533, 58, 0.426, 0.591, 3400, 2767, 1180, 639, 0.52, 1094, 11127),       #Messerschmitt Bf 109
"p39" : WFighter('USA', 'Fighter', 9600, 420, 75, 0.313, 0.490, 3750, 3833, 1200, 605, 0.49, 845, 31000)               #P-39 Airacobra

}


modernPlanes = {
    "f35": "F-35 LIGHTNING 2",
    "f16ef": "F-16E/F BLOCK 60",
    "f22": "F-22 RAPTOR",
    "fa18ef": "F/A-18E/F SUPER HORNET",
    "rafale": "Dassault Rafale",
    "su30": "SUKHOI SU-30",
    "gripen": "Saab JAS-39 Gripen",
    "j10": "CHENGDU J-10",
    "su35": "SUKHOI SU-35",
    "f15e": "F-15E STRIKE EAGLE",
    "su57": "SUKHOI PAK FA",
    "mig35": "MIG-35 FULCRUM F",
    "su30mki": "SUKHOI SU-30MKI",
    "su27": "SUKHOI SU-27",
    "mirage": "MIRAGE 2000E"
}


ww2Planes = {
    "p38": "P-38 Lightning",
    "fw190": "Fw 190 Wurger",
    "yak3": "Yakovlev Yak-3",
    "spitfire": "Supermarine Spitfire",
    "p40": "P-40 Warhawk",
    "p51": "P-51 Mustang",
    "bf109": "Messerschmitt Bf 109",
    "p39": "P-39 Airacobra"
    
}

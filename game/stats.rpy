# DAY %(p)s                      KONOHA VILLAGE


# HANABI
label ik111:
    
    screen statk1():
        if inoangry == 0:
            image "kha1.png" 
        else:
            image "kha2.png" 
        
        text "Name: Hanabi":
            xpos 130 ypos 120
            size 30 color "#000000" italic False bold False
            
        text "Status: Excited":
            xpos 130 ypos 220
            size 30 color "#000000" italic False bold False
    
    show screen statk1
    $ select = renpy.imagemap("ks1a.png", "ks1b.png", [
                                           (835, 110, 1170, 210, "mission"),
                                           (725, 450, 1170, 560, "return"),
                                           (1725, 285, 1825, 415, "right"),
                                           (1120, 280, 1220, 405, "left"),
                                           (100, 720, 300, 1020, "hana"),
                                           (320, 720, 515, 1020, "hima"),
                                           (530, 720, 735, 1020, "hina"),
                                           (755, 720, 955, 1020, "cho"),
                                           (970, 720, 1175, 1020, "ino"),
                                           (1190, 720, 1395, 1020, "saku"),
                                           (1410, 720, 1610, 1020, "tsuna"),
                                           (1630, 720, 1830, 1020, "sara"),
                                           ]) 
    
    
    if select == "mission":
        "It is really easy to complete Hanabi missions."
        "Just try to find her in the Hyuga house during night..."
        "Go out on a date with her and be nice she will easily fall in love with you."
        $ renpy.transition(dissolve)
        jump ik111
        
        
    if select == "return":
        
        hide screen statk1
        jump statsscreen
        
    if select == "right":
        if inoangry == 0:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump ik111
        else:
            $ renpy.transition(dissolve)
            jump ik111
            
        
    if select == "left":
        if inoangry == 0:
            $ renpy.transition(dissolve)
            jump ik111
        else:
            $ inoangry = 0
            $ renpy.transition(dissolve)
            jump ik111
        
        jump ik111
        
    if select == "hana":
        
        hide screen statk1
        $ renpy.transition(dissolve)
        jump ik111
        
    if select == "hima":
        
        hide screen statk1
        $ renpy.transition(dissolve)
        jump ik112
        
    if select == "hina":
        
        hide screen statk1
        $ renpy.transition(dissolve)
        jump ik113
    
    if select == "cho":
        
        hide screen statk1
        $ renpy.transition(dissolve)
        jump ik114
        
    if select == "ino":
        
        hide screen statk1
        $ renpy.transition(dissolve)
        jump ik115
        
    if select == "saku":
        
        hide screen statk1
        $ renpy.transition(dissolve)
        jump ik116
        
    if select == "tsuna":
        
        hide screen statk1
        $ renpy.transition(dissolve)
        jump ik117
        
    if select == "sara":
        
        hide screen statk1
        $ renpy.transition(dissolve)
        jump ik118
        
        
# HIMAWARI 
label ik112:
    
    screen statk2():
        if inoangry == 0:
            image "khim1.png" 
        elif inoangry == 1:
            image "khim2.png"
        elif inoangry == 2:
            image "khim3.png"  
        elif inoangry == 3:
            image "khim4.png"
        elif inoangry == 4:
            image "khim5.png"
        else:
            image "khim6.png" 
        
        text "Name: Himawari":
            xpos 130 ypos 120
            size 30 color "#000000" italic False bold False
            
        text "Status: Lost in time":
            xpos 130 ypos 220
            size 30 color "#000000" italic False bold False
    
    show screen statk2
    $ select = renpy.imagemap("ks1a.png", "ks1b.png", [
                                           (835, 110, 1170, 210, "mission"),
                                           (725, 450, 1170, 560, "return"),
                                           (1725, 285, 1825, 415, "right"),
                                           (1120, 280, 1220, 405, "left"),
                                           (100, 720, 300, 1020, "hana"),
                                           (320, 720, 515, 1020, "hima"),
                                           (530, 720, 735, 1020, "hina"),
                                           (755, 720, 955, 1020, "cho"),
                                           (970, 720, 1175, 1020, "ino"),
                                           (1190, 720, 1395, 1020, "saku"),
                                           (1410, 720, 1610, 1020, "tsuna"),
                                           (1630, 720, 1830, 1020, "sara"),
                                           ]) 
    
    
    if select == "mission":
        "Himawari is a little tricky."
        "You need to complete the S rank mission to unlock her."
        "Then you can find her younger version in the forest during the night or older version in the stadium during the day."
        "Just be careful what option you pick when you play with her.. You didn't want to mess the timeline, don't you?"
        $ renpy.transition(dissolve)
        jump ik112
        
        
    if select == "return":
        
        hide screen statk2
        jump statsscreen
        
    if select == "right":
        if inoangry == 0:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump ik112
        elif inoangry == 1:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump ik112
        elif inoangry == 2:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump ik112
        elif inoangry == 3:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump ik112
        elif inoangry == 4:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump ik112
        elif inoangry == 5:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump ik112
        else:
            $ renpy.transition(dissolve)
            jump ik112
            
        
    if select == "left":
        if inoangry == 0:
            $ renpy.transition(dissolve)
            jump ik112
        elif inoangry == 1:
            $ inoangry = inoangry -1
            $ renpy.transition(dissolve)
            jump ik112
        elif inoangry == 2:
            $ inoangry = inoangry -1
            $ renpy.transition(dissolve)
            jump ik112
        elif inoangry == 3:
            $ inoangry = inoangry -1
            $ renpy.transition(dissolve)
            jump ik112
        elif inoangry == 4:
            $ inoangry = inoangry -1
            $ renpy.transition(dissolve)
            jump ik112
        elif inoangry == 5:
            $ inoangry = inoangry -1
            $ renpy.transition(dissolve)
            jump ik112
        else:
            $ inoangry = 5
            $ renpy.transition(dissolve)
            jump ik112
        
        jump ik111
        
    if select == "hana":
        
        hide screen statk2
        $ renpy.transition(dissolve)
        jump ik111
        
    if select == "hima":
        
        hide screen statk2
        $ renpy.transition(dissolve)
        jump ik112
        
    if select == "hina":
    
        hide screen statk2
        $ renpy.transition(dissolve)
        jump ik113
    
    if select == "cho":
        
        hide screen statk2
        $ renpy.transition(dissolve)
        jump ik114
        
    if select == "ino":
        
        hide screen statk2
        $ renpy.transition(dissolve)
        jump ik115
        
    if select == "saku":
        
        hide screen statk2
        $ renpy.transition(dissolve)
        jump ik116
        
    if select == "tsuna":
        
        hide screen statk2
        $ renpy.transition(dissolve)
        jump ik117
        
    if select == "sara":
        
        hide screen statk2
        $ renpy.transition(dissolve)
        jump ik118 
 
 
 
# HINATA
label ik113:
    
    screen statk3():
        if inoangry == 0:
            image "khin1.png" 
        elif inoangry == 1:
            image "khin2.png" 
        elif inoangry == 2:
            image "khin3.png"
        elif inoangry == 3:
            image "khin4.png"
        elif inoangry == 4:
            image "khin5.png"
        elif inoangry == 5:
            image "khin6.png"
        elif inoangry == 6:
            image "khin7.png"
        else:
            image "khin8.png" 
        
        text "Name: Hinata":
            xpos 130 ypos 120
            size 30 color "#000000" italic False bold False
            
        text "Status: Horny":
            xpos 130 ypos 220
            size 30 color "#000000" italic False bold False
    
    show screen statk3
    $ select = renpy.imagemap("ks1a.png", "ks1b.png", [
                                           (835, 110, 1170, 210, "mission"),
                                           (725, 450, 1170, 560, "return"),
                                           (1725, 285, 1825, 415, "right"),
                                           (1120, 280, 1220, 405, "left"),
                                           (100, 720, 300, 1020, "hana"),
                                           (320, 720, 515, 1020, "hima"),
                                           (530, 720, 735, 1020, "hina"),
                                           (755, 720, 955, 1020, "cho"),
                                           (970, 720, 1175, 1020, "ino"),
                                           (1190, 720, 1395, 1020, "saku"),
                                           (1410, 720, 1610, 1020, "tsuna"),
                                           (1630, 720, 1830, 1020, "sara"),
                                           ]) 
    
    
    if select == "mission":
        "If you want to unlock Hinata you need to complete S rank mission 2 times."
        "Then you can find her in an empty room in your house."
        "Get closer to her and try to interact with Sarada and Himawari to progress in her story."
        "Use Namigan on her to unlock her second personality."
        $ renpy.transition(dissolve)
        jump ik113
        
        
    if select == "return":
        
        hide screen statk3
        jump statsscreen
        
    if select == "right":
        if inoangry == 0:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump ik113
        elif inoangry <= 6:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump ik113
        else:
            $ renpy.transition(dissolve)
            jump ik113
            
        
    if select == "left":
        if inoangry == 0:
            $ renpy.transition(dissolve)
            jump ik113
        if inoangry >= 1:
            $ inoangry = inoangry -1
            $ renpy.transition(dissolve)
            jump ik113
        else:
            $ inoangry = inoangry -1
            $ renpy.transition(dissolve)
            jump ik113
        
        jump ik111
        
    if select == "hana":
        
        hide screen statk3
        $ renpy.transition(dissolve)
        jump ik111
        
    if select == "hima":
        
        hide screen statk3
        $ renpy.transition(dissolve)
        jump ik112
        
    if select == "hina":
        
        hide screen statk3
        $ renpy.transition(dissolve)
        jump ik113
    
    if select == "cho":
        
        hide screen statk3
        $ renpy.transition(dissolve)
        jump ik114
        
    if select == "ino":
        
        hide screen statk3
        $ renpy.transition(dissolve)
        jump ik115
        
    if select == "saku":
        
        hide screen statk3
        $ renpy.transition(dissolve)
        jump ik116
        
    if select == "tsuna":
        
        hide screen statk3
        $ renpy.transition(dissolve)
        jump ik117
        
    if select == "sara":
        
        hide screen statk3
        $ renpy.transition(dissolve)
        jump ik118 
 
 
 
 # CHOCHO
label ik114:
    
    screen statk4():
        if inoangry == 0:
            image "kcho1.png" 
        elif inoangry == 1:
            image "kcho2.png" 
        elif inoangry == 2:
            image "kcho3.png"
        elif inoangry == 3:
            image "kcho4.png"
        elif inoangry == 4:
            image "kcho5.png"
        elif inoangry == 5:
            image "kcho6.png"
        else:
            image "kcho7.png" 
        
        text "Name: Chocho":
            xpos 130 ypos 120
            size 30 color "#000000" italic False bold False
            
        text "Status: Bodyguard / drunk":
            xpos 130 ypos 220
            size 30 color "#000000" italic False bold False
    
    show screen statk4
    $ select = renpy.imagemap("ks1a.png", "ks1b.png", [
                                           (835, 110, 1170, 210, "mission"),
                                           (725, 450, 1170, 560, "return"),
                                           (1725, 285, 1825, 415, "right"),
                                           (1120, 280, 1220, 405, "left"),
                                           (100, 720, 300, 1020, "hana"),
                                           (320, 720, 515, 1020, "hima"),
                                           (530, 720, 735, 1020, "hina"),
                                           (755, 720, 955, 1020, "cho"),
                                           (970, 720, 1175, 1020, "ino"),
                                           (1190, 720, 1395, 1020, "saku"),
                                           (1410, 720, 1610, 1020, "tsuna"),
                                           (1630, 720, 1830, 1020, "sara"),
                                           ]) 
    
    
    if select == "mission":
        "Try to find Chocho in the Konoha bar during the night."
        "Then you can find her during a day in the restaurant and offer her some Ryo for her services."
        "Do not forget to visit Tsunade and learn the expansion jutus. It is more fun when you know how to use it."
        $ renpy.transition(dissolve)
        jump ik114
        
        
    if select == "return":
        
        hide screen statk4
        jump statsscreen
        
    if select == "right":
        if inoangry == 0:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump ik114
        elif inoangry <= 5:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump ik114
        else:
            $ renpy.transition(dissolve)
            jump ik114
            
        
    if select == "left":
        if inoangry == 0:
            $ renpy.transition(dissolve)
            jump ik114
        if inoangry >= 1:
            $ inoangry = inoangry -1
            $ renpy.transition(dissolve)
            jump ik114
        else:
            $ inoangry = inoangry -1
            $ renpy.transition(dissolve)
            jump ik114
        
        
        
    if select == "hana":
        
        hide screen statk4
        $ renpy.transition(dissolve)
        jump ik111
        
    if select == "hima":
        
        hide screen statk4
        $ renpy.transition(dissolve)
        jump ik112
        
    if select == "hina":
        
        hide screen statk4
        $ renpy.transition(dissolve)
        jump ik113
    
    if select == "cho":
        
        hide screen statk4
        $ renpy.transition(dissolve)
        jump ik114
        
    if select == "ino":
        
        hide screen statk4
        $ renpy.transition(dissolve)
        jump ik115
        
    if select == "saku":
        
        hide screen statk4
        $ renpy.transition(dissolve)
        jump ik116
        
    if select == "tsuna":
        
        hide screen statk4
        $ renpy.transition(dissolve)
        jump ik117
        
    if select == "sara":
        
        hide screen statk4
        $ renpy.transition(dissolve)
        jump ik118 
 
 
 
 

 # INO
label ik115:
    
    screen statk5():
        if inoangry == 0:
            image "ki1.png" 
        elif inoangry == 1:
            image "ki2.png" 
        elif inoangry == 2:
            image "ki3.png"
        elif inoangry == 3:
            image "ki4.png"
        else:
            image "ki5.png" 
        
        text "Name: Ino":
            xpos 130 ypos 120
            size 30 color "#000000" italic False bold False
            
        text "Status: Flower girl":
            xpos 130 ypos 220
            size 30 color "#000000" italic False bold False
    
    show screen statk5
    $ select = renpy.imagemap("ks1a.png", "ks1b.png", [
                                           (835, 110, 1170, 210, "mission"),
                                           (725, 450, 1170, 560, "return"),
                                           (1725, 285, 1825, 415, "right"),
                                           (1120, 280, 1220, 405, "left"),
                                           (100, 720, 300, 1020, "hana"),
                                           (320, 720, 515, 1020, "hima"),
                                           (530, 720, 735, 1020, "hina"),
                                           (755, 720, 955, 1020, "cho"),
                                           (970, 720, 1175, 1020, "ino"),
                                           (1190, 720, 1395, 1020, "saku"),
                                           (1410, 720, 1610, 1020, "tsuna"),
                                           (1630, 720, 1830, 1020, "sara"),
                                           ]) 
    
    
    if select == "mission":
        "Ino can sell you some flowers in the local shop."
        "You can have lunch with her and grow your relationship if you buy delicious food for her."
        "It is a good idea to drink with her sometimes and pick long drinks."
        "Never say that you love her, she can be scared and stop all your future actions with her."
        $ renpy.transition(dissolve)
        jump ik115
        
        
    if select == "return":
        
        hide screen statk5
        jump statsscreen
        
    if select == "right":
        if inoangry == 0:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump ik115
        elif inoangry <= 3:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump ik115
        else:
            $ renpy.transition(dissolve)
            jump ik115
            
        
    if select == "left":
        if inoangry == 0:
            $ renpy.transition(dissolve)
            jump ik115
        if inoangry >= 1:
            $ inoangry = inoangry -1
            $ renpy.transition(dissolve)
            jump ik115
        else:
            $ inoangry = 4
            $ renpy.transition(dissolve)
            jump ik115
        
        
        
    if select == "hana":
        
        hide screen statk5
        $ renpy.transition(dissolve)
        jump ik111
        
    if select == "hima":
        
        hide screen statk5
        $ renpy.transition(dissolve)
        jump ik112
        
    if select == "hina":
        
        hide screen statk5
        $ renpy.transition(dissolve)
        jump ik113
    
    if select == "cho":
        
        hide screen statk5
        $ renpy.transition(dissolve)
        jump ik114
        
    if select == "ino":
        
        hide screen statk5
        $ renpy.transition(dissolve)
        jump ik115
        
    if select == "saku":
        
        hide screen statk5
        $ renpy.transition(dissolve)
        jump ik116
        
    if select == "tsuna":
        
        hide screen statk5
        $ renpy.transition(dissolve)
        jump ik117
        
    if select == "sara":
        
        hide screen statk5
        $ renpy.transition(dissolve)
        jump ik118 
 


# SAKURA
label ik116:
    
    screen statk6():
        if inoangry == 0:
            image "ksa1.png" 
        elif inoangry == 1:
            image "ksa2.png" 
        else:
            image "ksa3.png" 
        
        text "Name: Sakura":
            xpos 130 ypos 120
            size 30 color "#000000" italic False bold False
            
        text "Status: Wicked":
            xpos 130 ypos 220
            size 30 color "#000000" italic False bold False
    
    show screen statk6
    $ select = renpy.imagemap("ks1a.png", "ks1b.png", [
                                           (835, 110, 1170, 210, "mission"),
                                           (725, 450, 1170, 560, "return"),
                                           (1725, 285, 1825, 415, "right"),
                                           (1120, 280, 1220, 405, "left"),
                                           (100, 720, 300, 1020, "hana"),
                                           (320, 720, 515, 1020, "hima"),
                                           (530, 720, 735, 1020, "hina"),
                                           (755, 720, 955, 1020, "cho"),
                                           (970, 720, 1175, 1020, "ino"),
                                           (1190, 720, 1395, 1020, "saku"),
                                           (1410, 720, 1610, 1020, "tsuna"),
                                           (1630, 720, 1830, 1020, "sara"),
                                           ]) 
    
    
    if select == "mission":
        "If you want to unlock Sakura you need to get the medallion from Sarada."
        "Tsunade can help you solve the mystery about it and if you complete S rank mission you will find out the way how to use it."
        "Then you can play with her or unleash her and buy some flowers to complete her story."
        "Do not forget to talk with Sarada and see the family reunion."
        $ renpy.transition(dissolve)
        jump ik116
        
        
    if select == "return":
        
        hide screen statk6
        jump statsscreen
        
    if select == "right":
        if inoangry == 0:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump ik116
        elif inoangry <= 1:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump ik116
        else:
            $ renpy.transition(dissolve)
            jump ik116
            
        
    if select == "left":
        if inoangry == 0:
            $ renpy.transition(dissolve)
            jump ik116
        elif inoangry == 1:
            $ inoangry = inoangry -1
            $ renpy.transition(dissolve)
            jump ik116
        else:
            $ inoangry = 1
            $ renpy.transition(dissolve)
            jump ik116
        
        
        
    if select == "hana":
        
        hide screen statk6
        $ renpy.transition(dissolve)
        jump ik111
        
    if select == "hima":
        
        hide screen statk6
        $ renpy.transition(dissolve)
        jump ik112
        
    if select == "hina":
        
        hide screen statk6
        $ renpy.transition(dissolve)
        jump ik113
    
    if select == "cho":
        
        hide screen statk6
        $ renpy.transition(dissolve)
        jump ik114
        
    if select == "ino":
        
        hide screen statk6
        $ renpy.transition(dissolve)
        jump ik115
        
    if select == "saku":
        
        hide screen statk6
        $ renpy.transition(dissolve)
        jump ik116
        
    if select == "tsuna":
        
        hide screen statk6
        $ renpy.transition(dissolve)
        jump ik117
        
    if select == "sara":
        
        hide screen statk6
        $ renpy.transition(dissolve)
        jump ik118 



# TSUNADE
label ik117:
    
    screen statk7():
        if inoangry == 0:
            image "kt1.png" 
        elif inoangry == 1:
            image "kt2.png" 
        elif inoangry == 2:
            image "kt3.png"
        elif inoangry == 3:
            image "kt4.png"
        elif inoangry == 4:
            image "kt5.png"
        elif inoangry == 5:
            image "kt6.png"
        else:
            image "kt7.png" 
        
        text "Name: Tsunade":
            xpos 130 ypos 120
            size 30 color "#000000" italic False bold False
            
        text "Status: Your busty teacher":
            xpos 130 ypos 220
            size 30 color "#000000" italic False bold False
    
    show screen statk7
    $ select = renpy.imagemap("ks1a.png", "ks1b.png", [
                                           (835, 110, 1170, 210, "mission"),
                                           (725, 450, 1170, 560, "return"),
                                           (1725, 285, 1825, 415, "right"),
                                           (1120, 280, 1220, 405, "left"),
                                           (100, 720, 300, 1020, "hana"),
                                           (320, 720, 515, 1020, "hima"),
                                           (530, 720, 735, 1020, "hina"),
                                           (755, 720, 955, 1020, "cho"),
                                           (970, 720, 1175, 1020, "ino"),
                                           (1190, 720, 1395, 1020, "saku"),
                                           (1410, 720, 1610, 1020, "tsuna"),
                                           (1630, 720, 1830, 1020, "sara"),
                                           ]) 
    
    
    if select == "mission":
        "You can find Tsunade in the school and talk with her. But if you want to play with her you need to increase your Namigan with level seven or more."
        "Then you can learn expansion technique. It is a necessary step in some parts of this game."
        "You need to drink with her a lot and buy an expansion scroll to find out her real limits."
        "To finish her story you need to unlock Himawari and have chakra level 40 or more."
        $ renpy.transition(dissolve)
        hide screen statk7
        jump ik117
        
        
    if select == "return":
        
        hide screen statk7
        jump statsscreen
        
    if select == "right":
        if inoangry == 0:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump ik117
        elif inoangry <= 5:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump ik117
        else:
            $ renpy.transition(dissolve)
            jump ik117
            
        
    if select == "left":
        if inoangry == 0:
            $ renpy.transition(dissolve)
            jump ik117
        elif inoangry >= 1:
            $ inoangry = inoangry -1
            $ renpy.transition(dissolve)
            jump ik117
        else:
            $ inoangry = 5
            $ renpy.transition(dissolve)
            jump ik117
        
        
        
    if select == "hana":
        
        hide screen statk7
        $ renpy.transition(dissolve)
        jump ik111
        
    if select == "hima":
        
        hide screen statk7
        $ renpy.transition(dissolve)
        jump ik112
        
    if select == "hina":
        
        hide screen statk7
        $ renpy.transition(dissolve)
        jump ik113
    
    if select == "cho":
        
        hide screen statk7
        $ renpy.transition(dissolve)
        jump ik114
        
    if select == "ino":
        
        hide screen statk7
        $ renpy.transition(dissolve)
        jump ik115
        
    if select == "saku":
        
        hide screen statk7
        $ renpy.transition(dissolve)
        jump ik116
        
    if select == "tsuna":
        
        hide screen statk7
        $ renpy.transition(dissolve)
        jump ik117
        
    if select == "sara":
        
        hide screen statk7
        $ renpy.transition(dissolve)
        jump ik118 
 
 
 
# SARADA
label ik118:
    
    screen statk8():
        if inoangry == 0:
            image "ksr1.png" 
        elif inoangry == 1:
            image "ksr2.png" 
        else:
            image "ksr3.png" 
        
        text "Name: Sarada":
            xpos 130 ypos 120
            size 30 color "#000000" italic False bold False
            
        text "Status: Konoha Leader":
            xpos 130 ypos 220
            size 30 color "#000000" italic False bold False
    
    show screen statk8
    $ select = renpy.imagemap("ks1a.png", "ks1b.png", [
                                           (835, 110, 1170, 210, "mission"),
                                           (725, 450, 1170, 560, "return"),
                                           (1725, 285, 1825, 415, "right"),
                                           (1120, 280, 1220, 405, "left"),
                                           (100, 720, 300, 1020, "hana"),
                                           (320, 720, 515, 1020, "hima"),
                                           (530, 720, 735, 1020, "hina"),
                                           (755, 720, 955, 1020, "cho"),
                                           (970, 720, 1175, 1020, "ino"),
                                           (1190, 720, 1395, 1020, "saku"),
                                           (1410, 720, 1610, 1020, "tsuna"),
                                           (1630, 720, 1830, 1020, "sara"),
                                           ]) 
    
    
    if select == "mission":
        "Sarada can help you increase your Namigan power. Go to the forest during night and talk with her in the school during the day to make it happened."
        "When she finally meet you in your room talk with her a lot and be patient and sweet to her... You do not want to make her angry."
        "Finishing her story means complete the game... So do not be hurried with it..."
        "You need to train all your powers to make her obey or love you..."
        $ renpy.transition(dissolve)
        jump ik118
        
        
    if select == "return":
        
        hide screen statk8
        jump statsscreen
        
    if select == "right":
        if inoangry == 0:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump ik118
        elif inoangry == 1:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump ik118
        else:
            $ renpy.transition(dissolve)
            jump ik118
            
        
    if select == "left":
        if inoangry == 0:
            $ renpy.transition(dissolve)
            jump ik118
        elif inoangry == 1:
            $ inoangry = inoangry -1
            $ renpy.transition(dissolve)
            jump ik118
        else:
            $ inoangry = 1
            $ renpy.transition(dissolve)
            jump ik118
        
        
        
    if select == "hana":
        
        hide screen statk8
        $ renpy.transition(dissolve)
        jump ik111
        
    if select == "hima":
        
        hide screen statk8
        $ renpy.transition(dissolve)
        jump ik112
        
    if select == "hina":
        
        hide screen statk8
        $ renpy.transition(dissolve)
        jump ik113
    
    if select == "cho":
        
        hide screen statk8
        $ renpy.transition(dissolve)
        jump ik114
        
    if select == "ino":
        
        hide screen statk8
        $ renpy.transition(dissolve)
        jump ik115
        
    if select == "saku":
        
        hide screen statk8
        $ renpy.transition(dissolve)
        jump ik116
        
    if select == "tsuna":
        
        hide screen statk8
        $ renpy.transition(dissolve)
        jump ik117
        
    if select == "sara":
        
        hide screen statk8
        $ renpy.transition(dissolve)
        jump ik118  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
# DAY %(p)s                      ROCK VILLAGE   
# DAY %(p)s                      ROCK VILLAGE   
# DAY %(p)s                      ROCK VILLAGE   
# DAY %(p)s                      ROCK VILLAGE          
# DAY %(p)s                      ROCK VILLAGE        
        
label is111:
    screen stati1():
        if inoangry == 0:
            image "ite1.png" 
        elif inoangry == 1:
            image "ite2.png" 
        else:
            image "ite3.png" 
        
        text "Name: Tenten":
            xpos 130 ypos 120
            size 30 color "#000000" italic False bold False
        text "Status: Tool master":
            xpos 130 ypos 220
            size 30 color "#000000" italic False bold False
    
    show screen stati1
    $ select = renpy.imagemap("is1a.png", "is1b.png", [
                                           (835, 110, 1170, 210, "mission"),
                                           (725, 450, 1170, 560, "return"),
                                           (1725, 285, 1825, 415, "right"),
                                           (1120, 280, 1220, 405, "left"),
                                           (100, 720, 300, 1020, "tenten"),
                                           (320, 720, 515, 1020, "temari"),
                                           (530, 720, 735, 1020, "samui"),
                                           (755, 720, 955, 1020, "mitsuki"),
                                           (970, 720, 1175, 1020, "mei"),
                                           (1190, 720, 1395, 1020, "kushina"),
                                           (1410, 720, 1610, 1020, "kuro"),
                                           (1630, 720, 1830, 1020, "kaguya"),
                                           ]) 
    
    
    if select == "mission":
        "Just try to talk with Tenten and go out with her to have some progress in her story."
        "Talk with Kurotsuchi and unlock the Namigan path to see what Tenten can offer to you."
        "Play with her body and do not forget to buy a dildo and chakra clips!"
        "She is maybe a little different, but you can enjoy a lot of fun with her."
        jump is111
        
        
    if select == "return":
        hide screen stati1
        jump drock
        
    if select == "right":
        
        if inoangry == 0:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump is111
        elif inoangry == 1:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump is111
        else:
            $ renpy.transition(dissolve)
            jump is111
        
    if select == "left":
        
        if inoangry == 0:
            $ renpy.transition(dissolve)
            jump is111
        elif inoangry == 1:
            $ inoangry = inoangry -1
            $ renpy.transition(dissolve)
            jump is111
        else:
            $ inoangry = 1
            $ renpy.transition(dissolve)
            jump is111
        
    if select == "tenten":
        
        hide screen stati1
        jump is111
        
    if select == "temari":
        
        hide screen stati1
        jump is112
        
    if select == "samui":
        
        hide screen stati1
        jump is113
        
    if select == "mitsuki":
        
        hide screen stati1
        jump is114
        
    if select == "mei":
        
        hide screen stati1
        jump is115
        
    if select == "kuro":
        
        hide screen stati1
        jump is117
        
    if select == "kushina":
        
        hide screen stati1
        jump is116
        
    if select == "kaguya":
        
        hide screen stati1
        jump is118
        


# TEMARI

label is112:
    screen stati2():
        if inoangry == 0:
            image "it1.png" 
        elif inoangry == 1:
            image "it2.png" 
        elif inoangry == 2:
            image "it3.png" 
        elif inoangry == 3:
            image "it4.png" 
        elif inoangry == 4:
            image "it5.png" 
        else:
            image "it6.png" 
        
        text "Name: Temari":
            xpos 130 ypos 120
            size 30 color "#000000" italic False bold False
        text "Status: Unchainted wind user":
            xpos 130 ypos 220
            size 30 color "#000000" italic False bold False
    
    show screen stati2
    $ select = renpy.imagemap("is1a.png", "is1b.png", [
                                           (835, 110, 1170, 210, "mission"),
                                           (725, 450, 1170, 560, "return"),
                                           (1725, 285, 1825, 415, "right"),
                                           (1120, 280, 1220, 405, "left"),
                                           (100, 720, 300, 1020, "tenten"),
                                           (320, 720, 515, 1020, "temari"),
                                           (530, 720, 735, 1020, "samui"),
                                           (755, 720, 955, 1020, "mitsuki"),
                                           (970, 720, 1175, 1020, "mei"),
                                           (1190, 720, 1395, 1020, "kushina"),
                                           (1410, 720, 1610, 1020, "kuro"),
                                           (1630, 720, 1830, 1020, "kaguya"),
                                           ]) 
    
    
    if select == "mission":
        "All Temari actions are triggered during the night."
        "Find her in the park and defeat her to unlock more options."
        "Then you can visit her in the house and have even more fun."
        jump is112
        
        
    if select == "return":
        hide screen stati2
        jump drock
        
    if select == "right":
        
        if inoangry == 0:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump is112
        elif inoangry <= 4:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump is112
        else:
            $ renpy.transition(dissolve)
            jump is112
        
    if select == "left":
        
        if inoangry == 0:
            $ renpy.transition(dissolve)
            jump is112
        elif inoangry >= 1:
            $ inoangry = inoangry -1
            $ renpy.transition(dissolve)
            jump is112
        else:
            $ inoangry = 4
            $ renpy.transition(dissolve)
            jump is112
        
    if select == "tenten":
        
        hide screen stati2
        jump is111
        
    if select == "temari":
        
        hide screen stati2
        jump is112
        
    if select == "samui":
        
        hide screen stati2
        jump is113
        
    if select == "mitsuki":
        
        hide screen stati2
        jump is114
        
    if select == "mei":
        
        hide screen stati2
        jump is115
        
    if select == "kuro":
        
        hide screen stati2
        jump is117
        
    if select == "kushina":
        
        hide screen stati2
        jump is116
        
    if select == "kaguya":
        
        hide screen stati2
        jump is118
        
        

# SAMUI

label is113:
    screen stati3():
        if inoangry == 0:
            image "isa1.png" 
        elif inoangry == 1:
            image "isa2.png" 
        else:
            image "isa3.png" 
        
        text "Name: Samui":
            xpos 130 ypos 120
            size 30 color "#000000" italic False bold False
        text "Status: Sex addict / drunk":
            xpos 130 ypos 220
            size 30 color "#000000" italic False bold False
    
    show screen stati3
    $ select = renpy.imagemap("is1a.png", "is1b.png", [
                                           (835, 110, 1170, 210, "mission"),
                                           (725, 450, 1170, 560, "return"),
                                           (1725, 285, 1825, 415, "right"),
                                           (1120, 280, 1220, 405, "left"),
                                           (100, 720, 300, 1020, "tenten"),
                                           (320, 720, 515, 1020, "temari"),
                                           (530, 720, 735, 1020, "samui"),
                                           (755, 720, 955, 1020, "mitsuki"),
                                           (970, 720, 1175, 1020, "mei"),
                                           (1190, 720, 1395, 1020, "kushina"),
                                           (1410, 720, 1610, 1020, "kuro"),
                                           (1630, 720, 1830, 1020, "kaguya"),
                                           ]) 
    
    
    if select == "mission":
        "Samui is a drunk. You can find her in the Konoha, just look around the bar."
        "Just try to wake her up gently and then meet her near the Konoha gate."
        "If she accepts your invitation for a dinner you can visit her at the guest house."
        "You need to take her chakra more than 10 times to unlock all her scenes."
        "Then you can finally have sex with her without increasing her addiction."
        jump is113
        
        
    if select == "return":
        hide screen stati3
        jump drock
        
    if select == "right":
        
        if inoangry == 0:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump is113
        elif inoangry <= 1:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump is113
        else:
            $ renpy.transition(dissolve)
            jump is113
        
    if select == "left":
        
        if inoangry == 0:
            $ renpy.transition(dissolve)
            jump is113
        elif inoangry >= 1:
            $ inoangry = inoangry -1
            $ renpy.transition(dissolve)
            jump is113
        else:
            $ inoangry = 1
            $ renpy.transition(dissolve)
            jump is113
        
    if select == "tenten":
        
        hide screen stati3
        jump is111
        
    if select == "temari":
        
        hide screen stati3
        jump is112
        
    if select == "samui":
        
        hide screen stati3
        jump is113
        
    if select == "mitsuki":
        
        hide screen stati3
        jump is114
        
    if select == "mei":
        
        hide screen stati3
        jump is115
        
    if select == "kuro":
        
        hide screen stati3
        jump is117
        
    if select == "kushina":
        
        hide screen stati3
        jump is116
        
    if select == "kaguya":
        
        hide screen stati3
        jump is118
        
        
        
        
# MITSUKI

label is114:
    screen stati4():
        if inoangry == 0:
            image "imi1.png" 
        elif inoangry == 1:
            image "imi2.png" 
        else:
            image "imi2.png" 
        
        text "Name: Mitsuki":
            xpos 130 ypos 120
            size 30 color "#000000" italic False bold False
        text "Status: Clon servant":
            xpos 130 ypos 220
            size 30 color "#000000" italic False bold False
    
    show screen stati4
    $ select = renpy.imagemap("is1a.png", "is1b.png", [
                                           (835, 110, 1170, 210, "mission"),
                                           (725, 450, 1170, 560, "return"),
                                           (1725, 285, 1825, 415, "right"),
                                           (1120, 280, 1220, 405, "left"),
                                           (100, 720, 300, 1020, "tenten"),
                                           (320, 720, 515, 1020, "temari"),
                                           (530, 720, 735, 1020, "samui"),
                                           (755, 720, 955, 1020, "mitsuki"),
                                           (970, 720, 1175, 1020, "mei"),
                                           (1190, 720, 1395, 1020, "kushina"),
                                           (1410, 720, 1610, 1020, "kuro"),
                                           (1630, 720, 1830, 1020, "kaguya"),
                                           ]) 
    
    
    if select == "mission":
        "Mitsuki is only a lab subject right now."
        "You can order her to strip and have some fun, but that is all right now..."
        jump is114
        
        
    if select == "return":
        hide screen stati4
        jump drock
        
    if select == "right":
        
        if inoangry == 0:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump is114
        elif inoangry == 1:
            $ renpy.transition(dissolve)
            jump is114
        else:
            $ renpy.transition(dissolve)
            jump is114
        
    if select == "left":
        
        if inoangry == 0:
            $ renpy.transition(dissolve)
            jump is114
        elif inoangry == 1:
            $ inoangry = inoangry -1
            $ renpy.transition(dissolve)
            jump is114
        else:
            $ inoangry = 0
            $ renpy.transition(dissolve)
            jump is114
        
    if select == "tenten":
        
        hide screen stati4
        jump is111
        
    if select == "temari":
        
        hide screen stati4
        jump is112
        
    if select == "samui":
        
        hide screen stati4
        jump is113
        
    if select == "mitsuki":
        
        hide screen stati4
        jump is114
        
    if select == "mei":
        
        hide screen stati4
        jump is115
        
    if select == "kuro":
        
        hide screen stati4
        jump is117
        
    if select == "kushina":
        
        hide screen stati4
        jump is116
        
    if select == "kaguya":
        
        hide screen stati4
        jump is118
        
        
        
        
        
# MEI

label is115:
    screen stati5():
        if inoangry == 0:
            image "im1.png" 
        elif inoangry == 1:
            image "im2.png" 
        else:
            image "im3.png" 
        
        text "Name: Mei":
            xpos 130 ypos 120
            size 30 color "#000000" italic False bold False
        text "Status: Wandering Mizukage":
            xpos 130 ypos 220
            size 30 color "#000000" italic False bold False
    
    show screen stati5
    $ select = renpy.imagemap("is1a.png", "is1b.png", [
                                           (835, 110, 1170, 210, "mission"),
                                           (725, 450, 1170, 560, "return"),
                                           (1725, 285, 1825, 415, "right"),
                                           (1120, 280, 1220, 405, "left"),
                                           (100, 720, 300, 1020, "tenten"),
                                           (320, 720, 515, 1020, "temari"),
                                           (530, 720, 735, 1020, "samui"),
                                           (755, 720, 955, 1020, "mitsuki"),
                                           (970, 720, 1175, 1020, "mei"),
                                           (1190, 720, 1395, 1020, "kushina"),
                                           (1410, 720, 1610, 1020, "kuro"),
                                           (1630, 720, 1830, 1020, "kaguya"),
                                           ]) 
    
    
    if select == "mission":
        "You can find Me in the Konoha, just look around the gate."
        "Try to get some information about her situation - look around the school."
        "After completing first S rank mission you will finally be able to interact with her and use your charm on her."
        "To finish her story you need to talk with Sarada and Tsunade."
        jump is115
        
        
    if select == "return":
        hide screen stati5
        jump drock
        
    if select == "right":
        
        if inoangry == 0:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump is115
        elif inoangry <= 1:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump is115
        else:
            $ renpy.transition(dissolve)
            jump is115
        
    if select == "left":
        
        if inoangry == 0:
            $ renpy.transition(dissolve)
            jump is115
        elif inoangry >= 1:
            $ inoangry = inoangry -1
            $ renpy.transition(dissolve)
            jump is115
        else:
            $ inoangry = inoangry -1
            $ renpy.transition(dissolve)
            jump is115
        
    if select == "tenten":
        
        hide screen stati5
        jump is111
        
    if select == "temari":
        
        hide screen stati5
        jump is112
        
    if select == "samui":
        
        hide screen stati5
        jump is113
        
    if select == "mitsuki":
        
        hide screen stati5
        jump is114
        
    if select == "mei":
        
        hide screen stati5
        jump is115
        
    if select == "kuro":
        
        hide screen stati5
        jump is117
        
    if select == "kushina":
        
        hide screen stati5
        jump is116
        
    if select == "kaguya":
        
        hide screen stati5
        jump is118
        
        

# KUSHINA

label is116:
    screen stati6():
        if inoangry == 0:
            image "ikus1.png" 
        elif inoangry == 1:
            image "ikus2.png" 
        elif inoangry == 2:
            image "ikus3.png"
        else:
            image "ikus4.png" 
        
        text "Name: Kushina":
            xpos 130 ypos 120
            size 30 color "#000000" italic False bold False
        text "Status: Uzumaki ancestor":
            xpos 130 ypos 220
            size 30 color "#000000" italic False bold False
    
    show screen stati6
    $ select = renpy.imagemap("is1a.png", "is1b.png", [
                                           (835, 110, 1170, 210, "mission"),
                                           (725, 450, 1170, 560, "return"),
                                           (1725, 285, 1825, 415, "right"),
                                           (1120, 280, 1220, 405, "left"),
                                           (100, 720, 300, 1020, "tenten"),
                                           (320, 720, 515, 1020, "temari"),
                                           (530, 720, 735, 1020, "samui"),
                                           (755, 720, 955, 1020, "mitsuki"),
                                           (970, 720, 1175, 1020, "mei"),
                                           (1190, 720, 1395, 1020, "kushina"),
                                           (1410, 720, 1610, 1020, "kuro"),
                                           (1630, 720, 1830, 1020, "kaguya"),
                                           ]) 
    
    
    if select == "mission":
        "Kushina is really tricky, you need to talk a lot with Mitsuka and Kurotsuchi to unlock her."
        "Then you can interact with her or even take her to the Konoha."
        "Just try to take her out for a few times and you will see what will happen..."
        jump is116
        
        
    if select == "return":
        hide screen stati6
        jump drock
        
    if select == "right":
        
        if inoangry == 0:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump is116
        elif inoangry <= 2:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump is116
        else:
            $ renpy.transition(dissolve)
            jump is116
        
    if select == "left":
        
        if inoangry == 0:
            $ renpy.transition(dissolve)
            jump is116
        elif inoangry >= 1:
            $ inoangry = inoangry -1
            $ renpy.transition(dissolve)
            jump is116
        else:
            $ inoangry = 2
            $ renpy.transition(dissolve)
            jump is116
        
    if select == "tenten":
        
        hide screen stati6
        jump is111
        
    if select == "temari":
        
        hide screen stati6
        jump is112
        
    if select == "samui":
        
        hide screen stati6
        jump is113
        
    if select == "mitsuki":
        
        hide screen stati6
        jump is114
        
    if select == "mei":
        
        hide screen stati6
        jump is115
        
    if select == "kuro":
        
        hide screen stati6
        jump is117
        
    if select == "kushina":
        
        hide screen stati6
        jump is116
        
    if select == "kaguya":
        
        hide screen stati6
        jump is118
    
    
    
    
    
# KUROTSUCHI

label is117:
    screen stati7():
        if inoangry == 0:
            image "iku1.png" 
        elif inoangry == 1:
            image "iku2.png" 
        else:
            image "iku2.png" 
        
        text "Name: Kurotsuchi":
            xpos 130 ypos 120
            size 30 color "#000000" italic False bold False
        text "Status: Third Tsuchikage":
            xpos 130 ypos 220
            size 30 color "#000000" italic False bold False
    
    show screen stati7
    $ select = renpy.imagemap("is1a.png", "is1b.png", [
                                           (835, 110, 1170, 210, "mission"),
                                           (725, 450, 1170, 560, "return"),
                                           (1725, 285, 1825, 415, "right"),
                                           (1120, 280, 1220, 405, "left"),
                                           (100, 720, 300, 1020, "tenten"),
                                           (320, 720, 515, 1020, "temari"),
                                           (530, 720, 735, 1020, "samui"),
                                           (755, 720, 955, 1020, "mitsuki"),
                                           (970, 720, 1175, 1020, "mei"),
                                           (1190, 720, 1395, 1020, "kushina"),
                                           (1410, 720, 1610, 1020, "kuro"),
                                           (1630, 720, 1830, 1020, "kaguya"),
                                           ]) 
    
    
    if select == "mission":
        "Kurotsuchi have only a few Namigan scenes right now. Just try to talk with her and use your Namigan."
        "Increase Namigan to level 30 or more and look around the park in the Iwagakure then you can enjoy some fun with her."
        jump is117
        
        
    if select == "return":
        hide screen stati7
        jump drock
        
    if select == "right":
        
        if inoangry == 0:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump is117
        elif inoangry == 1:
            $ renpy.transition(dissolve)
            jump is117
        else:
            $ renpy.transition(dissolve)
            jump is117
        
    if select == "left":
        
        if inoangry == 0:
            $ renpy.transition(dissolve)
            jump is117
        elif inoangry == 1:
            $ inoangry = inoangry -1
            $ renpy.transition(dissolve)
            jump is117
        else:
            $ inoangry = 0
            $ renpy.transition(dissolve)
            jump is117
        
    if select == "tenten":
        
        hide screen stati7
        jump is111
        
    if select == "temari":
        
        hide screen stati7
        jump is112
        
    if select == "samui":
        
        hide screen stati7
        jump is113
        
    if select == "mitsuki":
        
        hide screen stati7
        jump is114
        
    if select == "mei":
        
        hide screen stati7
        jump is115
        
    if select == "kuro":
        
        hide screen stati7
        jump is117
        
    if select == "kushina":
        
        hide screen stati7
        jump is116
        
    if select == "kaguya":
        
        hide screen stati7
        jump is118
        
        
        
# KAGUYA

label is118:
    screen stati8():
        if inoangry == 0:
            image "ik1.png" 
        elif inoangry == 1:
            image "ik2.png" 
        elif inoangry == 2:
            image "ik3.png"
        else:
            image "ik4.png" 
        
        text "Name: Kaguya":
            xpos 130 ypos 120
            size 30 color "#000000" italic False bold False
        text "Status: Evil queen":
            xpos 130 ypos 220
            size 30 color "#000000" italic False bold False
    
    show screen stati8
    $ select = renpy.imagemap("is1a.png", "is1b.png", [
                                           (835, 110, 1170, 210, "mission"),
                                           (725, 450, 1170, 560, "return"),
                                           (1725, 285, 1825, 415, "right"),
                                           (1120, 280, 1220, 405, "left"),
                                           (100, 720, 300, 1020, "tenten"),
                                           (320, 720, 515, 1020, "temari"),
                                           (530, 720, 735, 1020, "samui"),
                                           (755, 720, 955, 1020, "mitsuki"),
                                           (970, 720, 1175, 1020, "mei"),
                                           (1190, 720, 1395, 1020, "kushina"),
                                           (1410, 720, 1610, 1020, "kuro"),
                                           (1630, 720, 1830, 1020, "kaguya"),
                                           ]) 
    
    
    if select == "mission":
        "Try to talk with Mitsuka and Kurotstutchi during day they will give you some clues about cloning."
        "After you unlock Kaguya, look around the hall."
        "Just try to not upset her and she can reward you with her love."
        jump is118
        
        
    if select == "return":
        hide screen stati8
        jump drock
        
    if select == "right":
        
        if inoangry == 0:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump is118
        elif inoangry <= 2:
            $ inoangry = inoangry +1
            $ renpy.transition(dissolve)
            jump is118
        else:
            $ renpy.transition(dissolve)
            jump is118
        
    if select == "left":
        
        if inoangry == 0:
            $ renpy.transition(dissolve)
            jump is118
        elif inoangry >= 1:
            $ inoangry = inoangry -1
            $ renpy.transition(dissolve)
            jump is118
        else:
            $ inoangry = 2
            $ renpy.transition(dissolve)
            jump is118
        
    if select == "tenten":
        
        hide screen stati8
        jump is111
        
    if select == "temari":
        
        hide screen stati8
        jump is112
        
    if select == "samui":
        
        hide screen stati8
        jump is113
        
    if select == "mitsuki":
        
        hide screen stati8
        jump is114
        
    if select == "mei":
        
        hide screen stati8
        jump is115
        
    if select == "kuro":
        
        hide screen stati8
        jump is117
        
    if select == "kushina":
        
        hide screen stati8
        jump is116
        
    if select == "kaguya":
        
        hide screen stati8
        jump is118
    
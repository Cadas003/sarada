# DAY %(p)s                      ROCK VILLAGE

label dharem:

    scene dharem0

    $ select = renpy.imagemap("dharem0.jpg", "dharem1.jpg", [
                                               (815, 860, 1080, 955, "gate"),
                                               (670, 430, 950, 535, "spa"),
                                               (220, 415, 540, 520, "village"),
                                               (990, 330, 1255, 435, "house"),
                                               (910, 115, 1190, 220, "cave"),
                                               (1320, 200, 1650, 320, "forest"),
                                               ]) 
    if select == "gate":
        scene black with circleirisin       
        show dharemgate with circleirisout
        menu:
            "Talk with Mikoto":
                $ renpy.transition(dissolve)
                show mikoa 
                show mikoop
                mik "Good to see you again. How can I help?"
                menu mikototalk:
                    "Talk":
                        if extra1 ==0:
                            p "Can you tell me something about yourself?"
                            mik "Ehm... And what do you want to know?"
                            $ extra1 = 1
                            p "Maybe something about that weird eye you have before."
                            $ renpy.transition(dissolve)
                            hide mikoop
                            show mikoshar2
                            mik "You mean this?"
                            p "Yews... You are from the Uchiha clan right?"
                            mik "Probably... I am not sure... I didn't remember anything from my past."
                            mik "Or maybe I should say I do not have any past."
                            p "And what that mean?"
                            mik "I am a clone."
                            p "Ehm... Sorry..."
                            mik "For what? Being a clone is nothing bad. Actually, my life is pretty amazing."
                            mik "I can do whatever I want and have sex with whatéver I want."
                            p "Ehm... Why you talk about sex?"
                            mik "Becuase I like it..."
                            p "Good to know... Maybe we can have some fun together..."
                            mik "Mmm.... that sounds good to me..."
                            $ renpy.transition(dissolve)
                            hide mikoshar2
                            show mikook
                            mik "But not now... I have some work to do..."
                            p "Sure... Ehmmm... Maybe tomorrow?"
                            mik "Maybe...."
                            scene black with circleirisin               
                            show nharem0 with circleirisout
                            jump nharem
                            
                        else:
                            p "Can you tell me something about yourself?"
                            mik "Ehm... And what do you want to know?"
                            p "Are you happy in this village?"
                            mik "Sure... Anything else?"
                            p "..."
                            jump mikototalk
                            
                        
                        
                    "About village":
                        if extra1 ==1:
                            p "I just wonder if is anything I should know about the village."
                            $ extra1 = 2
                            mik "This village is a unique place where we do not tolerate any kind of aggression."
                            p "And what that mean?"
                            mik "It means that any intruders will be expelled."
                            p "And what if someone has a bad intetnitos and want to attack someone in the village."
                            mik "It is just simply not possible..."
                            p "Why?"
                            $ renpy.transition(dissolve)
                            hide mikoop
                            show mikoshar2
                            mik "The special jutsu is released in this village."
                            mik "It can preventively banish everyone who wants to attack."
                            p "And who cast it?"
                            mik "It is a work of some special shinobies that live here in the village..."
                            mik "I believe you will meet them sooner or later..."
                            p "That would be nice..."
                            $ renpy.transition(dissolve)
                            hide mikoshar2
                            show mikook
                            mik "Any other questions?"
                            p "Not right now..."
                            scene black with circleirisin               
                            show nharem0 with circleirisout
                            jump nharem 
                            
                        else:
                            p "Is there anything I should know about the village?"
                            mik "Just do not try to harm anyone and you will be fine."
                            p "Why would I harm anyone?"
                            mik "..."
                            mik "Do you have other questions?"
                            p "Maybe..."
                            jump mikototalk
                        
                    "Exclusive private service":
                        p "So can you show me the village?"
                        if extra1 <=1:
                            mik "Sorry, But I do not have a time right now maybe later."
                            p "Ok...."
                            scene black with circleirisin               
                            show dharem0 with circleirisout
                            jump dharem
                        else:
                            mik "Sure where you want to go?"
                            menu:
                                
                                "Village":
                                    p "Can you show me something interesting in the village?"
                                    mik "Sure, just follow me."
                                    scene black with circleirisin 
                                    show dhremvillage with circleirisout
                                    $ renpy.transition(dissolve)
                                    hide mikoa 
                                    hide mikoop
                                    show mikoa 
                                    show mikook
                                    p "Hmmm... Nice... And what is interesting here?"
                                    mik "Just wait for a moment..."
                                    $ renpy.transition(dissolve)
                                    hide mikoa 
                                    hide mikook
                                    show mik2a
                                    show mik2ok
                                    mik "So do you think this is interesting enough for you?"
                                    p "Huh? Sure... You look amazing..."
                                    mik "Thanks... Do you like my boobs?"
                                    p "Yeah..."
                                    mik "You can play with them if you want."
                                    menu:
                                        "Play with them":
                                            p "Time for some tools..."
                                            $ renpy.transition(dissolve)
                                            show mik2l1
                                            hide mik2ok
                                            show mik2shock
                                            mik "huh???"
                                            p "Lightning style!!! *zap*"
                                            $ renpy.transition(dissolve)
                                            show mik2l2
                                            mik "What is???"
                                            $ renpy.transition(dissolve)
                                            show mik2l3
                                            hide mik2shock
                                            show mik2shar
                                            mik "Yessss...*moan*"
                                            mik "More...."
                                            p "Sure.... *zap*"
                                            $ renpy.transition(dissolve)
                                            show mik2m2
                                            hide mik2shar
                                            show mik2clop
                                            mik "Yesss...*squirt*"
                                            p "Hehe... this is sweet...."
                                            $ renpy.transition(dissolve)
                                            show mik2m1
                                            hide mik2l3
                                            mik "Mmmmm.... That was funny..."
                                            $ renpy.transition(dissolve)
                                            hide mik2l2
                                            hide mik2m2
                                            hide mik2clop
                                            show mik2op
                                            p "Yeah... It was...."
                                            mik "Next time I will play with you."
                                            p "Ok... I am looking forward for it."                                            
                                            scene black with circleirisin       
                                            show nharem0 with circleirisout
                                            jump nharem
                                            
                                        "Fuck hre boobs":
                                            p "Expansion!!!"
                                            $ renpy.transition(dissolve)
                                            hide mik2a
                                            hide mik2ok
                                            show mik2b
                                            show mik2op
                                            mik "Ahhh... *moan*"
                                            $ renpy.transition(dissolve)
                                            show mik2p1
                                            p "Sure..."
                                            $ renpy.transition(dissolve)
                                            hide mik2p1
                                            show mik2p2
                                            hide mik2op
                                            show mik2op
                                            mik " You have nice hard dick..."
                                            $ renpy.transition(dissolve)
                                            hide mik2p2
                                            show mik2p3
                                            p "Thanks your boobs is awesome too..."
                                            $ renpy.transition(dissolve)
                                            hide mik2p3
                                            show mik2p4
                                            mik "So warm..."
                                            $ renpy.transition(dissolve)
                                            hide mik2p4
                                            show mik2p3
                                            hide mik2op
                                            show mik2clop
                                            p "Hmmm..."
                                            $ renpy.transition(dissolve)
                                            hide mik2p3
                                            show mik2p2
                                            p "I love big boobs!!!"
                                            $ renpy.transition(dissolve)
                                            hide mik2p2
                                            show mik2p3
                                            p "Fuck!!!"
                                            $ renpy.transition(dissolve)
                                            hide mik2p3
                                            show mik2p4
                                            p "This is too much *splurt*"
                                            $ renpy.transition(dissolve)
                                            show mik2p5
                                            hide mik2clop
                                            show mik2hap
                                            mik "Nice...*drip*"
                                            $ renpy.transition(dissolve)
                                            show mik2p6
                                            mik "You cum so much... *drip lick*"
                                            p "Yeah, because you are so sexi."
                                            mik "Thanks."
                                            mik "Come to see me again if you want some fun..."
                                            p "Sure..."
                                            scene black with circleirisin       
                                            show nharem0 with circleirisout
                                            jump nharem
                                    
                                
                                "SPA":
                                    p "I want to check the spa."
                                    mik "Allright..."
                                    scene black with circleirisin 
                                    show dharemspa with circleirisout
                                    $ renpy.transition(dissolve)
                                    hide mikoa 
                                    hide mikoop
                                    show mikoa 
                                    show mikook
                                    p "This place look nice..."
                                    mik "Yes..."
                                    $ renpy.transition(dissolve)
                                    hide mikoa 
                                    hide mikook
                                    show mikob
                                    show mikook
                                    mik "Do you want to take a bath with me?"
                                    p "Absolutely!"
                                    mik "But you need to strip too for that... "
                                    p "Yeah... I know..."
                                    mik "Mmm.... Looks you are ready for me..."
                                    $ renpy.transition(dissolve)
                                    hide mikob
                                    hide mikook
                                    p "Ehm... *mumble*"
                                    mik "Do not be shy, just do it!"
                                    $ renpy.transition(dissolve)
                                    show mik3a
                                    show mik3ok
                                    show mik3p1
                                    mik "Yes... This feels really good."
                                    $ renpy.transition(dissolve)
                                    hide mik3p1
                                    show mik3p2
                                    mik "Ahhh...*moan*"
                                    mik "Do you like my boobs?"
                                    $ renpy.transition(dissolve)
                                    hide mik3p2
                                    show mik3p3
                                    p "Yeah... But they should be bigger..."
                                    mik "I can make that happen for you... EXPANSION!"
                                    $ renpy.transition(dissolve)
                                    hide mik3a
                                    hide mik3ok
                                    hide mik3p3
                                    show mik3b
                                    show mik3hap
                                    show mik3p2
                                    p "Wow... This is better!"
                                    p "That boobs I want to slap them!"
                                    $ renpy.transition(dissolve)
                                    hide mik3p2
                                    show mik3p1
                                    mik "Then do it!"
                                    $ renpy.transition(dissolve)
                                    hide mik3p1
                                    show mik3p2
                                    p "*slap*"
                                    $ renpy.transition(dissolve)
                                    hide mik3p2
                                    show mik3p3
                                    show mik3h1
                                    hide mik3hap
                                    show mik3cl
                                    mik "Yeah!!!*moan * MORE!!!"
                                    p "*slap*" with hpunch
                                    $ renpy.transition(dissolve)
                                    hide mik3p3
                                    show mik3p2
                                    show mik3h2
                                    p "I can try this too!!! Kage bunshin no jutsu!!!"
                                    $ renpy.transition(dissolve)
                                    hide mik3p2
                                    show mik3p1
                                    show mik3p6
                                    show mik3p8
                                    hide mik3cl
                                    show mik3sup
                                    mik "Huh? Kage bunshin??? *moan*"
                                    $ renpy.transition(dissolve)
                                    hide mik3p1
                                    show mik3p2
                                    hide mik3sup
                                    show mik3ok
                                    mik "Perfect!!! *moan*"
                                    $ renpy.transition(dissolve)
                                    hide mik3p2
                                    show mik3p3
                                    p "Yeah... I think so!!!"
                                    $ renpy.transition(dissolve)
                                    hide mik3p3
                                    show mik3p2
                                    p "Fuck!!!! *slap*"
                                    $ renpy.transition(dissolve)
                                    hide mik3p2
                                    show mik3p3
                                    show mik3h3
                                    mik "Ahhhh*heavy moaning*"
                                    p "Take it all!!! *splurt*"
                                    $ renpy.transition(dissolve)
                                    show mik3p4
                                    mik "*heavy moaning*"
                                    $ renpy.transition(dissolve)
                                    hide mik3ok
                                    show mik3hap
                                    show mik3p5
                                    show mik3p7
                                    p "Yeah!!! *splurt*"
                                    $ renpy.transition(dissolve)
                                    show mik3p9
                                    mik "MMMm....*heavy moaning* So much sperm..."
                                    p "Yeah... I think now you really need a bath...."
                                    mik "Yes...*gigle*"
                                    scene black with circleirisin       
                                    "It looks like Mikoto is a really horny woman... That relationship can work."
                                    show nharem0 with circleirisout
                                    jump nharem
                                
                                "Cave":
                                    p "Is there anything what I can check near the village?."
                                    mik "Huh? Only forest. Or one old cave."
                                    p "Old cave? That sounds good to me, lets go."
                                    scene black with circleirisin 
                                    show dharemcave with circleirisout
                                    $ renpy.transition(dissolve)
                                    hide mikoa 
                                    hide mikoop
                                    show mikoa 
                                    show mikook
                                    p ".... Normal cave..."
                                    mik "I told you.... But no one is around."
                                    p "So we can do something together right?"
                                    $ renpy.transition(dissolve)
                                    hide mikoa 
                                    hide mikook
                                    mik "And what do you want to do?"
                                    p "I will show you.... Just lay down and...."
                                    $ renpy.transition(dissolve)
                                    show miko4a
                                    show miko4ok
                                    p "You know what to do right?"
                                    mik "Sure.... But put your dick in my ass now!"
                                    p "In your ass??? Ok...."
                                    $ renpy.transition(dissolve)
                                    show miko4p1
                                    hide miko4ok
                                    show miko4op
                                    mik "Hehe... Expansion!!!"
                                    $ renpy.transition(dissolve)
                                    hide miko4a
                                    show miko4b
                                    hide miko4p1
                                    show miko4p1
                                    hide miko4op
                                    show miko4op
                                    p "Sweet..."
                                    $ renpy.transition(dissolve)
                                    hide miko4p1
                                    show miko4p2
                                    mik "Yess...."
                                    $ renpy.transition(dissolve)
                                    hide miko4op
                                    show miko4clop
                                    hide miko4p2
                                    show miko4p3
                                    p "Lick it!!!"
                                    $ renpy.transition(dissolve)
                                    hide miko4p3
                                    show miko4p4
                                    mik "Expansion!!!"
                                    $ renpy.transition(dissolve)
                                    hide miko4b
                                    show miko4c
                                    hide miko4clop
                                    show miko4ok
                                    hide miko4p4
                                    show miko4p3
                                    p "Wow!!!"
                                    $ renpy.transition(dissolve)
                                    hide miko4p3
                                    show miko4p2
                                    p "This is so hot!!"
                                    $ renpy.transition(dissolve)
                                    hide miko4p2
                                    show miko4p3
                                    hide miko4ok
                                    show miko4sgok
                                    mik "Ahhhh... *moaning*"
                                    $ renpy.transition(dissolve)
                                    hide miko4p3
                                    show miko4p4
                                    mik "Yes!!! ahredr!!!"
                                    $ renpy.transition(dissolve)
                                    hide miko4p4
                                    show miko4p3
                                    hide miko4sgok
                                    show miko4sgop
                                    p "Ahhh!!!*splurt*"
                                    $ renpy.transition(dissolve)
                                    hide miko4p3
                                    show miko4p2
                                    show miko4sp1
                                    mik "Give me your sperm..."
                                    $ renpy.transition(dissolve)
                                    hide miko4p2
                                    show miko4p3
                                    show miko4sp2
                                    p "Yeah!!!!"
                                    menu:
                                        "Cum in":
                                            $ renpy.transition(dissolve)
                                            hide miko4p3
                                            show miko4p4
                                            p "Take it all!!! *splurt*"
                                            $ renpy.transition(dissolve)
                                            show miko4p7
                                            mik "Ahhh!!! *Moan*"
                                            $ renpy.transition(dissolve)
                                            show miko4p8
                                            p "Awesome!!!!"
                                            mik "MMm.... My ass is so full right now..."
                                            p "Yeah.... It is..."
                                            mik "I wonder if you can fill me right now every day."
                                            p "We should definitely try it..."
                                            scene black with circleirisin       
                                            show nharem0 with circleirisout
                                            jump nharem
                                            
                                            
                                        "Cum out":
                                            
                                            $ renpy.transition(dissolve)
                                            hide miko4p3
                                            show miko4p2
                                            mik "Cum on my body!!!"
                                            $ renpy.transition(dissolve)
                                            hide miko4p2
                                            show miko4p1
                                            p "Sure.... *splurt*"
                                            $ renpy.transition(dissolve)
                                            show miko4p5
                                            mik "Sweet! *Moan*"
                                            $ renpy.transition(dissolve)
                                            show miko4p6
                                            p "...."
                                            p "Look at you...."
                                            mik "I am hot right?"
                                            p "Yes you are...."
                                            scene black with circleirisin       
                                            show nharem0 with circleirisout
                                            jump nharem
                                    
                                    
                                "Forset":
                                    p "I need to breathe some fresh air."
                                    mik "Alright, we can go to the forest..."
                                    p "Sounds good to me."
                                    scene black with circleirisin 
                                    show dharemforest with circleirisout
                                    $ renpy.transition(dissolve)
                                    hide mikoa 
                                    hide mikoop
                                    show mikoa 
                                    show mikook
                                    p "Ahhh... This is what I needed!"
                                    mik "Is there anything what I can do for you to make you feel better?"
                                    p "Actually, I know about something... Just take these clothes off..."
                                    $ renpy.transition(dissolve)
                                    hide mikoa 
                                    hide mikook
                                    show mikob
                                    show mikook
                                    mik "You mean like this?"
                                    p "Exactly!"
                                    $ renpy.transition(dissolve)
                                    hide mikob
                                    hide mikook
                                    p "And now...."
                                    $ renpy.transition(dissolve)
                                    show mik6a
                                    show mik6op
                                    show mik6p1
                                    mik "Ahhhh!!!*moan*"
                                    p "Yeah... This is just what I needed."
                                    $ renpy.transition(dissolve)
                                    hide mik6p1
                                    show mik6p2
                                    mik "*moan*"
                                    $ renpy.transition(dissolve)
                                    hide mik6p2
                                    show mik6p3
                                    hide mik6op
                                    show mik6clop
                                    p "And now..."
                                    $ renpy.transition(dissolve)
                                    hide mik6p3
                                    show mik6p2
                                    p "Kage bunshin no jutsu!"
                                    $ renpy.transition(dissolve)
                                    hide mik6p2
                                    show mik6p1
                                    show mik6tf1
                                    hide mik6clop
                                    show mik6ok
                                    mik "Fuck my boobs!!!"
                                    $ renpy.transition(dissolve)
                                    hide mik6p1
                                    show mik6p2
                                    hide mik6tf1
                                    show mik6tf2
                                    mik "deeper!!!"
                                    $ renpy.transition(dissolve)
                                    hide mik6p2
                                    show mik6p3
                                    hide mik6tf2
                                    show mik6tf3
                                    mik "*moan*"
                                    $ renpy.transition(dissolve)
                                    hide mik6p3
                                    show mik6p2
                                    hide mik6tf3
                                    show mik6tf4
                                    p "What if I try this??? *clamp*"
                                    $ renpy.transition(dissolve)
                                    hide mik6p2
                                    show mik6p1
                                    hide mik6tf4
                                    show mik6tf3
                                    show mik6l1
                                    hide mik6ok
                                    show mik6cl
                                    mik "*moan pain*"
                                    p "Fuck this is good...  Lightning style!!! *zap*"
                                    $ renpy.transition(dissolve)
                                    hide mik6p1
                                    show mik6p2
                                    hide mik6tf3
                                    show mik6tf2
                                    show mik6l2
                                    p "Yeah!!! *splurt zap*"
                                    $ renpy.transition(dissolve)
                                    hide mik6p2
                                    show mik6p3
                                    show mik6p4
                                    hide mik6tf2
                                    show mik6tf3
                                    show mik6l3
                                    mik "Ahhh!!!*heavy moaning*"
                                    $ renpy.transition(dissolve)
                                    show mik6p5
                                    hide mik6tf3
                                    show mik6tf4
                                    p "You are so hot! *splurt*"
                                    $ renpy.transition(dissolve)
                                    hide mik6cl
                                    show mik6op
                                    show mik6tf5
                                    mik "Ahhh!!!*squirt drip*"
                                    $ renpy.transition(dissolve)
                                    show mik6tf5
                                    show mik6l4
                                    mik "Awesome!!!! *moan*"
                                    p "Yeah... I think so... Fresh air is the best..."
                                    p "Thanks for.... Am.... Everything..."
                                    mik "Hehe... You are welcome."
                                    scene black with circleirisin       
                                    show nharem0 with circleirisout
                                    jump nharem
                                
                                
                                
                    "Nothing":
                        scene black with circleirisin               
                        show dharem0 with circleirisout
                        jump dharem 
                        
                        
                scene black with circleirisin               
                show drock0 with circleirisout
                jump drock 
                
                show dharemspa with circleirisout
                
            
            "Return to Konoha":
                "You leave the village."
                scene black with circleirisin   
                "After a day of traveling you come to the Konoha."
                $ day = day + 1
                show droom with circleirisout
                jump nday
                
            "Go to hidden stone village":
                scene black with circleirisin               
                show drock0 with circleirisout
                jump drock  
                
            "Assign":
                "There is nothing to do right now."
                jump dharem
                
            "Rest":
                "You need to get some rest."
                scene black with circleirisin               
                show nharem0 with circleirisout
                jump nharem
            
            "Go back to the map":
                scene black with circleirisin               
                show dharem0 with circleirisout
                jump dharem  
        
    if select == "spa":
        scene black with circleirisin  
        show dharemspa with circleirisout     
        jump dharemspa1
        
        
        
    if select == "village":
        scene black with circleirisin  
        show dhremvillage with circleirisout        
        jump dhremvillage1           
            
        
    if select == "house":      
                    
        scene black with circleirisin  
        show dharemhouse with circleirisout
        jump dharemhouse1
        
        
        
    if select == "cave":
        scene black with circleirisin  
        show dharemcave with circleirisout
        jump dharemcave1
        
        
        
    if select == "forest": 
        scene black with circleirisin  
        show dharemforest with circleirisout
        jump dharemforest1













################################ dhraemspa1 
################################ dhraemspa1
################################ dhraemspa1
################################ dhraemspa1 
################################ dhraemspa1
label dharemspa1:
    scene dharemspa
    menu:
        "Enjoy SPA procedure":
            "You decided to take some time and rest."
            "After a few hours you feel much better and your chakra is now refilled."
            $ chakra = chakra + 1
            scene black with circleirisin               
            show nharem0 with circleirisout
            jump nharem      
        
        "Call Kushina": ### 9 max Kushina
            if kushinamission >= 10:
                    $ renpy.transition(dissolve)
                    if kushinadress == 0:
                        show kusa
                    if kushinadress == 1:
                        show kusb
                    if kushinadress == 2:
                        show kusc
                    show kusnn
                    p "It is good to see you here.."
                    p "So what should I do now?"
                    menu nkushinamigan1:
                        "Titfuck":
                            p "Maybe I just fuck your boobs."
                            p "Lay down Kushina, I want to enjoy it."
                            $ renpy.transition(dissolve)
                            hide kusa
                            hide kusb
                            hide kusc
                            hide kusd
                            hide kusnn
                            show kus3a
                            show kus3nok
                            p "Yes, this is what I want..."
                            $ renpy.transition(dissolve)
                            show kus3tf1
                            p "That boobs is so soft."
                            $ renpy.transition(dissolve)
                            hide kus3tf1
                            show kus3tf2
                            p "Fuck! Feel good between them."
                            $ renpy.transition(dissolve)
                            hide kus3tf2
                            show kus3tf3
                            hide kus3nok
                            show kus3nop
                            ku "Mmmm...."
                            $ renpy.transition(dissolve)
                            hide kus3tf3
                            show kus3tf4
                            p "What?"
                            $ renpy.transition(dissolve)
                            hide kus3tf2
                            show kus3tf3
                            ku "*moan*"
                            $ renpy.transition(dissolve)
                            hide kus3tf3
                            show kus3tf2
                            p "Ok..."
                            $ renpy.transition(dissolve)
                            hide kus3tf2
                            show kus3tf3
                            p "What now?"
                            menu nkuntf1:
                                "Clips":
                                    p "This will be fun!"
                                    $ renpy.transition(dissolve)
                                    hide kus3tf3
                                    show kus3tf4
                                    show kus3l1
                                    hide kus3nop
                                    show kus3cl
                                    ku "Arhghhh!!!"
                                    $ renpy.transition(dissolve)
                                    hide kus3tf4
                                    show kus3tf3
                                    p "And now!!! Lightning style!"
                                    $ renpy.transition(dissolve)
                                    hide kus3tf3
                                    show kus3tf2
                                    show kus3l2
                                    ku "*moan*"
                                    $ renpy.transition(dissolve)
                                    hide kus3tf2
                                    show kus3tf3
                                    p "More!!!"
                                    $ renpy.transition(dissolve)
                                    hide kus3tf3
                                    show kus3tf4
                                    show kus3l3
                                    hide kus3cl
                                    show kus3clop
                                    ku "*Heavy moan*"
                                    $ renpy.transition(dissolve)
                                    hide kus3tf4
                                    show kus3tf3
                                    p "Yes..."
                                    $ renpy.transition(dissolve)
                                    hide kus3tf3
                                    show kus3tf2
                                    hide kus3l3
                                    p "Fuck..."
                                    $ renpy.transition(dissolve)
                                    hide kus3tf2
                                    show kus3tf3
                                    hide kus3l2
                                    p "Hehe... This is funny..."
                                    $ renpy.transition(dissolve)
                                    hide kus3l1
                                    hide kus3clop
                                    show kus3nop
                                    p "Time to..."
                                    jump nkuntf1
                                    
                                "Slap":
                                    p "Do you like this??? *slap*"
                                    $ renpy.transition(dissolve)
                                    hide kus3tf3
                                    show kus3tf4
                                    show kus3h1
                                    hide kus3nop
                                    show kus3cl
                                    ku "OOOOO!!!"
                                    $ renpy.transition(dissolve)
                                    hide kus3tf4
                                    show kus3tf3
                                    p "Yeah! More! *slap*"
                                    $ renpy.transition(dissolve)
                                    hide kus3tf3
                                    show kus3tf2
                                    show kus3h2
                                    ku "*moan pain*"
                                    $ renpy.transition(dissolve)
                                    hide kus3tf2
                                    show kus3tf3
                                    p "Slap that tits! *slap*"
                                    $ renpy.transition(dissolve)
                                    hide kus3tf3
                                    show kus3tf4
                                    show kus3h3
                                    hide kus3cl
                                    show kus3clop
                                    ku "*Heavy moan*"
                                    $ renpy.transition(dissolve)
                                    hide kus3tf4
                                    show kus3tf3
                                    p "Hehe... That huge boobs is awesome!"
                                    $ renpy.transition(dissolve)
                                    hide kus3tf3
                                    show kus3tf2
                                    p "And that red color...."
                                    $ renpy.transition(dissolve)
                                    hide kus3tf2
                                    show kus3tf3
                                    p "I shuld heal it a little... Palm Jutsu!"
                                    $ renpy.transition(dissolve)
                                    $ renpy.transition(dissolve)
                                    hide kus3tf3
                                    show kus3tf4
                                    hide kus3h1
                                    hide kus3h2
                                    hide kus3h3
                                    hide kus3clop
                                    show kus3nop
                                    p "YEah good..."
                                    $ renpy.transition(dissolve)
                                    hide kus3tf4
                                    show kus3tf3
                                    p "And now..."
                                    jump nkuntf1
                                    
                                "Cum":
                                    p "Time to finish it!"
                                    $ renpy.transition(dissolve)
                                    hide kus3tf3
                                    show kus3tf4
                                    hide kus3nop
                                    show kus3nok
                                    ku "....."
                                    $ renpy.transition(dissolve)
                                    hide kus3tf4
                                    show kus3tf3
                                    p "Yeah! Almost!!!"
                                    $ renpy.transition(dissolve)
                                    hide kus3tf3
                                    show kus3tf4
                                    p "Open that mouth!"
                                    $ renpy.transition(dissolve)
                                    hide kus3tf4
                                    show kus3tf3
                                    hide kus3nok
                                    show kus3nop
                                    p "Yeah!!! *splurt*"
                                    $ renpy.transition(dissolve)
                                    hide kus3tf3
                                    show kus3tf4
                                    show kus3tf5
                                    ku "Aaaaa...  *moan drip*"
                                    $ renpy.transition(dissolve)
                                    show kus3tf6
                                    p "Fuck!!!"
                                    $ renpy.transition(dissolve)
                                    show kus3tf7
                                    p "...."
                                    p "That was good...."
                                    ku "Mmmmm...."
                                    p "Time to clean all this mess..."
                                    scene black with circleirisin   
                                    "Kushina clean her body and drink all sperm."
                                    "It is good to have her in your harem."
                                    scene black with circleirisin               
                                    show nharem0 with circleirisout
                                    jump nharem
                            
                        "Kage bunshin":
                            p "I just want to fuck you hard..."
                            p "Strip and get on all four."
                            $ renpy.transition(dissolve)
                            hide kusa
                            hide kusb
                            hide kusc
                            hide kusd
                            hide kusnn
                            show kus2a
                            show kus2ok
                            p "Yes this is good..."
                            $ renpy.transition(dissolve)
                            show kus2p1
                            p "Or maybe... Kage bunshin no jutsu!"
                            $ renpy.transition(dissolve)
                            show kus2p5
                            show kus2p6
                            p "And time to fuck you hard!"
                            $ renpy.transition(dissolve)
                            hide kus2p1
                            show kus2p2
                            hide kus2ok
                            show kus2op
                            ku "Ahhh...*moan*"
                            $ renpy.transition(dissolve)
                            hide kus2p2
                            show kus2p3
                            p "Hehe...."
                            $ renpy.transition(dissolve)
                            hide kus2p3
                            show kus2p4
                            p "Fell so good..."
                            $ renpy.transition(dissolve)
                            hide kus2p4
                            show kus2p3
                            ku "Yeah *moan*"
                            $ renpy.transition(dissolve)
                            hide kus2p3
                            show kus2p2
                            p "Come on!!!"
                            $ renpy.transition(dissolve)
                            hide kus2p2
                            show kus2p3
                            hide kus2op
                            show kus2org
                            ku "Yessss....*heavy moaning*"
                            p "Fuck this is!!!*splurt*"
                            $ renpy.transition(dissolve)
                            hide kus2p3
                            show kus2p4
                            show kus2spo3
                            ku "Ahhhh..."
                            $ renpy.transition(dissolve)
                            hide kus2p4
                            show kus2p3
                            show kus2spo4
                            p "Awesome!!!!"
                            $ renpy.transition(dissolve)
                            hide kus2p3
                            show kus2p2
                            p "Take it all!!!*splurt*"
                            $ renpy.transition(dissolve)
                            hide kus2p2
                            show kus2p1
                            show kus2spo1
                            ku "More!!!"
                            $ renpy.transition(dissolve)
                            show kus2spo2
                            hide kus2org
                            show kus2cl
                            p "Hehe.....Look at you..."
                            ku "Mmmm....*moan*"
                            p "You look so dirty now.... Come on, no time to rest... Clean yourself."
                            ku "....."
                            scene black with circleirisin        
                            "That was good... But your Kage bunshin take too much of your chakra."
                            "But looks like Kushina enjoyed it too..."
                            scene black with circleirisin               
                            show nharem0 with circleirisout
                            jump nharem
                        
                        "Mixed training":
                            if expscroll ==0:
                                p "I need an expansion scroll for this."
                                p "I should visit the shop in the Konoha."
                                jump nkushinamigan1
                                
                                
                            else:
                                p "I just want to fuck you hard..."
                                p "Strip and get on all four."
                                $ renpy.transition(dissolve)
                                hide kusa
                                hide kusb
                                hide kusc
                                hide kusd
                                hide kusnn
                                show kus2a
                                show kus2ok
                                p "Yes this looks good... But I want more!"
                                p "Boob expansion!"
                                $ renpy.transition(dissolve)
                                hide kus2a
                                hide kus2ok
                                show kus2b
                                show kus2op
                                ku "Ahhhh.... *moan*"
                                p "It looks better right?"
                                $ renpy.transition(dissolve)
                                show kus2p1
                                p "And this open mouth! Kage bunshin no jutsu!"
                                $ renpy.transition(dissolve)
                                show kus2bl1
                                hide kus2p1
                                show kus2p2
                                p "And time to fuck you hard!"
                                $ renpy.transition(dissolve)
                                hide kus2bl1
                                show kus2bl2
                                ku "mgmmmm....*moan*"
                                $ renpy.transition(dissolve)
                                hide kus2p2
                                show kus2p3
                                hide kus2bl2
                                show kus2bl3
                                p "Hehe...."
                                $ renpy.transition(dissolve)
                                hide kus2p3
                                show kus2p4
                                hide kus2bl3
                                show kus2bl4
                                p "Fell so good..."
                                $ renpy.transition(dissolve)
                                hide kus2p4
                                show kus2p3
                                hide kus2bl4
                                show kus2bl3
                                ku "gmhmmm*choke*"
                                $ renpy.transition(dissolve)
                                hide kus2p3
                                show kus2p2
                                hide kus2bl3
                                show kus2bl4
                                p "Yes Suck it harder!!!"
                                $ renpy.transition(dissolve)
                                hide kus2p2
                                show kus2p3
                                hide kus2op
                                show kus2cl
                                hide kus2bl4
                                show kus2bl3
                                ku "ghghgmmmm...*gag cough*"
                                $ renpy.transition(dissolve)
                                hide kus2p3
                                show kus2p4
                                hide kus2bl3
                                show kus2bl4
                                ku "ggtggrg...*choke*"
                                $ renpy.transition(dissolve)
                                hide kus2p4
                                show kus2p3
                                hide kus2bl4
                                show kus2bl3
                                p "Yes more!!!"
                                $ renpy.transition(dissolve)
                                hide kus2p3
                                show kus2p2
                                hide kus2bl3
                                show kus2bl4
                                p "Take it all!!!*splurt*"
                                $ renpy.transition(dissolve)
                                hide kus2p2
                                show kus2p3
                                hide kus2bl4
                                show kus2bl3
                                ku "ggggg...*gag*"
                                $ renpy.transition(dissolve)
                                hide kus2p2
                                show kus2p3
                                hide kus2bl4
                                show kus2bl3
                                show kus2spi1
                                p "Yessss!!!*splurt*"
                                $ renpy.transition(dissolve)
                                hide kus2bl3
                                show kus2bl4
                                show kus2spi2
                                show kus2bl5
                                ku "gggggg....*gag cough choke*"
                                $ renpy.transition(dissolve)
                                show kus2bl6
                                p "Fuck*drip* this feeels..."
                                ku ".....*choke*"
                                p "Hey? Are you still here?"
                                ku "...."
                                p "Looks like everything is fine.."
                                scene black with circleirisin               
                                show nharem0 with circleirisout
                                jump nharem
                        
                        "Boob expansion":
                            if expscroll ==0:
                                p "I need an expansion scroll for this."
                                p "I should visit the shop in the Konoha."
                                jump nkushinamigan1
                                
                                
                            else:
                                p "Time to see how big they can be."
                                p "First, get into the position."
                                $ renpy.transition(dissolve)
                                hide kusa
                                hide kusb
                                hide kusc
                                hide kusd
                                hide kusnn
                                show kus2a
                                show kus2ok
                                p "And now."
                                p "Boob expansion!"
                                $ renpy.transition(dissolve)
                                hide kus2a
                                hide kus2ok
                                show kus2b
                                show kus2op
                                ku "Ahhhh.... *moan*"
                                p "This looks good... But I want more!"
                                p "Maximum expansion!"
                                $ renpy.transition(dissolve)
                                hide kus2b
                                hide kus2op
                                show kus2c
                                show kus2org
                                ku "Ahggrrggg...*heavy moaning*"
                                p "Wow! They are huge! and now..."
                                $ renpy.transition(dissolve)
                                show kus2p1
                                p "Yeah time to fuck you!"
                                $ renpy.transition(dissolve)
                                hide kus2p1
                                show kus2p2
                                hide kus2org
                                show kus2op
                                p "Nice..."
                                $ renpy.transition(dissolve)
                                hide kus2p2
                                show kus2p3
                                ku "mmmmmm....*moan*"
                                $ renpy.transition(dissolve)
                                hide kus2p3
                                show kus2p4
                                p "This will make you sexier. *scratch*"
                                $ renpy.transition(dissolve)
                                hide kus2p4
                                show kus2p3
                                show kus2text
                                p "Nice...."
                                $ renpy.transition(dissolve)
                                hide kus2p3
                                show kus2p4
                                ku "*moan*"
                                $ renpy.transition(dissolve)
                                hide kus2p4
                                show kus2p3
                                p "yeah*slap*"
                                $ renpy.transition(dissolve)
                                hide kus2p3
                                show kus2p2
                                show kus3h1
                                p "Hehe...*slap*"
                                $ renpy.transition(dissolve)
                                hide kus2p2
                                show kus2p3
                                hide kus2op
                                show kus2cl
                                show kus3h2
                                ku "Arggg...*moan*"
                                $ renpy.transition(dissolve)
                                hide kus2p3
                                show kus2p4
                                p "Do you want more? *slap*"
                                $ renpy.transition(dissolve)
                                hide kus2p4
                                show kus2p3
                                show kus3h3
                                p "Hehe... Look at you..."
                                $ renpy.transition(dissolve)
                                hide kus2p3
                                show kus2p2
                                p "You look so ...."
                                $ renpy.transition(dissolve)
                                hide kus2p2
                                show kus2p3
                                hide kus2cl
                                show kus2op
                                menu:
                                    "Cum in":
                                        ku "argggg...*moan*"
                                        $ renpy.transition(dissolve)
                                        hide kus2p2
                                        show kus2p3
                                        p "Yessss!!!*splurt*"
                                        $ renpy.transition(dissolve)
                                        hide kus2p3
                                        show kus2p4
                                        show kus2spi1
                                        ku "mmmm...*drip*"
                                        $ renpy.transition(dissolve)
                                        show kus2spi2
                                        p "....**drip....."
                                        ku "Oooo...*moan*"
                                        p "It feels good to cum inside."
                                        ku "*moan*"
                                        p "OK... Time to clean you a little..."
                                    "Cum out":
                                        ku "Yesss...*moan*"
                                        $ renpy.transition(dissolve)
                                        hide kus2p3
                                        show kus2p1
                                        p "Take it all!!! *splurt*"
                                        $ renpy.transition(dissolve)
                                        show kus2spo1
                                        ku "more...*drip*"
                                        $ renpy.transition(dissolve)
                                        show kus2spo2
                                        p "Fuck look at you!"
                                        ku "mmm...*moan*"
                                        p "You look really dirty..."
                                        ku "...."
                                        p "Who cares right?"
                                        
                                scene black with circleirisin               
                                show nharem0 with circleirisout
                                jump nharem
            else:
                "How you want to talk with her if she is not here?"
                scene black with circleirisin               
                show dharem0 with circleirisout
                jump dharem
                

####################################### 14 je max pre Chocho
####################################### 14 je max pre Chocho
####################################### 14 je max pre Chocho
        
        
        "Call Chocho":
            
            if chochostats >=15:
                $ renpy.transition(dissolve)
                show chocho1
                show chochonna
                ch "...."
                p "Now we can enjoy some fun together."
                menu chochocroom11:
                    "Basic training": 
                            p "Now undress!"
                            ch "With pleasure."
                            $ renpy.transition(dissolve)
                            hide chocho1
                            hide chochonna
                            hide chochoshy
                            show chocho5
                            show chochonna
                            show chochoc
                            show chochoshy                        
                            p "Good."
                            p "Now I want to..."
                            menu:
                                "Slash her":
                                    p "Time to give you some pleasure."
                                    ch "....."
                                    p "Give that headband away."
                                    $ renpy.transition(dissolve)
                                    hide chochoc
                                    p "So do you want kiss or slash?"
                                    ch "..."
                                    $ renpy.transition(dissolve)
                                    hide chochosadna
                                    hide chochonna
                                    show chochocl
                                    p "I am not hearing anything."
                                    ch "...."
                                    p "Chocho!" with hpunch
                                    ch "Slash me..."
                                    "Slash!" with vpunch
                                    ch "ARGH!!!!"
                                    "Slash!" with hpunch
                                    show chochoscars1
                                    ch "Oooooooo....."
                                    p "Do you want more???"
                                    "Slash!" with hpunch
                                    hide chochocl
                                    show chochoclop
                                    show chochocry
                                    ch "Yes...."
                                    ch "MORE!!!"
                                    p "????"
                                    p "Anything you want..."
                                    "Slash!" with hpunch
                                    show chochoscars2
                                    ch "Yesssss....."
                                    "Slash!" with hpunch
                                    show chochoh
                                    ch "More!!!"
                                    "Slash!" with hpunch
                                    ch "Aaaaaaaa...."
                                    p "...."
                                    p "Now I know what is the best way how to treat you."
                                    $ renpy.transition(dissolve)
                                    hide chochoh
                                    p "But this wounds look pretty bad."
                                    $ renpy.transition(dissolve)
                                    hide chochoclop
                                    show chochonna
                                    hide chochocry
                                    p "Chocho, you heal yourself now."
                                    ch "Ok...."
                                    ch "Mystical Palm Technique!"
                                    $ renpy.transition(dissolve)
                                    hide chochoscars1
                                    hide chochoscars2
                                    p "I wish anything can heal that fast."
                                    ch "..."
                                    p "I think I can control you and Namigan better now."
                                    $ eyes = eyes + 1
                                    p "You can dress now."
                                    $ renpy.transition(dissolve)
                                    hide chocho5
                                    hide chochosadna
                                    hide chochonna
                                    hide chochoshy
                                    show chocho1
                                    show chochonna
                                    show chochoc
                                    show chochoshy 
                                    p "Ok..."
                                    p "See you next time..."                                    
                                    scene black with circleirisin               
                                    show nharem0 with circleirisout
                                    jump nharem
                                    
                                "Use toys":
                                    p "Ok, first I need to pick that chakra clip."
                                    ch "I am ready for it."
                                    $ renpy.transition(dissolve)
                                    show chochoclips
                                    ch "...."
                                    p "Do you like it?"
                                    $ renpy.transition(dissolve)
                                    hide chochosadna
                                    hide chochonna
                                    show chochocl
                                    ch "Yes...."
                                    p "Now I use that thing you have in the bag."
                                    ch "You mean my dildo?"
                                    p "Yes. Just give it to me."
                                    ch "Sure..."
                                    with fade
                                    p "...."
                                    p "Nice... But you should put it here..."
                                    $ renpy.transition(dissolve)
                                    show chochodil
                                    ch "Mmmmmm...."
                                    $ renpy.transition(dissolve)
                                    hide chochocl
                                    show chochoorg    
                                    ch "YES!!!!"
                                    p "Hmm... What if I charge you a little?"
                                    p "Lightning style!!!"
                                    $ renpy.transition(dissolve)
                                    show chocholig
                                    "Zap...."
                                    ch "Grggggggg..."
                                    p "More power!!!"
                                    $ renpy.transition(dissolve)
                                    show chocholight
                                    hide chochoorg 
                                    show chochocl
                                    ch "AAAAAAAAaaaaa..."
                                    p "This is pretty hard to do manually."
                                    p "I mean Namigan and lightning style together..."
                                    $ renpy.transition(dissolve)
                                    hide chocholight
                                    ch "Mmmmmm..."
                                    p "More Lightning!"
                                    $ renpy.transition(dissolve)
                                    show chocholig
                                    ch "Yesssss..."
                                    p "...."
                                    p "What a weird chick."
                                    $ renpy.transition(dissolve)
                                    hide chocholight
                                    p "huh...This is harder than it looks"
                                    $ renpy.transition(dissolve)
                                    hide chocholig
                                    p "That is my limit..."
                                    $ eyes = eyes + 1
                                    p "Maybe I should remove these things..."
                                    $ renpy.transition(dissolve)
                                    hide chochodil
                                    hide chochoclips
                                    ch "But..."
                                    $ renpy.transition(dissolve)
                                    hide chochocl
                                    show chochosadna
                                    p "Look like you really like it... But It is very hard to hold that kind of jutsu without killing you."
                                    p "Now dress..."
                                    $ renpy.transition(dissolve)
                                    hide chocho5
                                    hide chochosadna
                                    hide chochoshy
                                    show chocho1
                                    show chochosadna
                                    show chochoc
                                    ch "....."
                                    p "See you next time..."                                    
                                    scene black with circleirisin               
                                    show nharem0 with circleirisout
                                    jump nharem
                                
                                "Expansion":
                                        p "Time to try change your body size."                                       
                                        ch "My body can change size easily."
                                        p "Yes, I know. But now I need to change it."
                                        $ renpy.transition(dissolve)
                                        hide chochosadna
                                        hide chochonna
                                        show chochocl
                                        p "Concentrate..."
                                        p "Expansion!!!"
                                        $ renpy.transition(dissolve)
                                        hide chocho5
                                        hide chochocl
                                        hide chochoshy
                                        hide chochoc
                                        show chocho6
                                        show chochocl
                                        show chochoc
                                        ch "...."
                                        $ renpy.transition(dissolve)
                                        hide chochocl
                                        show chochonna
                                        ch "nice..."
                                        p "Yes... I mean... Your body looks more chubby now."
                                        ch "Thanks."
                                        p "I wonder If I can make it even bigge."
                                        p "Expansion!!!"
                                        with fade
                                        p "..."
                                        p "Nothing happened..."
                                        p "Maybe if I concentrate more..."
                                        p "Expansion!!!"
                                        $ renpy.transition(dissolve)
                                        hide chochonna
                                        show chochoopna
                                        ch "Wow... I feeel...."
                                        ch "....."
                                        $ renpy.transition(dissolve)
                                        hide chochoopna
                                        show chochoorg
                                        show chochomilk2
                                        ch "Aaaaaa..."
                                        p "Wow. Nice... I mean..."
                                        p "Look like this is the maximum size I can change."
                                        $ chakra  = chakra  + 1
                                        p "But you react pretty well to more chakra."
                                        $ renpy.transition(dissolve)
                                        hide chochomilk2
                                        show chochomilk1
                                        ch "...."
                                        p "But I know You can be bigger."
                                        menu:
                                            "Increase size":
                                                p "I want to see your bigger body."
                                                p "Use your expansion technique."
                                                ch "Sure."
                                                ch "Baika no jutsu!"
                                                $ renpy.transition(dissolve)
                                                hide chochoorg
                                                hide chocho6
                                                hide chochoshy
                                                show chocho6 with dissolve:
                                                    xalign 0.5 yalign 0.5
                                                    xzoom 2.5 yzoom 2.5
                                                show chochoorg with dissolve:
                                                    xalign 0.5 yalign 0.5
                                                    xzoom 2.5 yzoom 2.5
                                                p "Wow..."
                                                p "That works well but... I think you will only increase your boobs size."
                                                ch "..."
                                                p "Newermind... just...."
                                                p "Release that jutsu...."
                                                ch "Sure...."
                                                $ renpy.transition(dissolve)
                                                hide chochoorg
                                                hide chocho6
                                                show chocho6
                                                show chochoorg
                                                p "Good..."
                                            "That is enough":
                                                p "I think this is enough."                                    
                                        p "Time to make you normal."
                                        p "Expansion Kai!"
                                        $ renpy.transition(dissolve)
                                        hide chocho6
                                        hide chochoorg
                                        hide chochoshy
                                        hide chochoc
                                        show chocho5
                                        show chochocl
                                        show chochoc
                                        p "And everything is smaller now."
                                        p "You can dress now."
                                        ch "Ok..."
                                        $ renpy.transition(dissolve)
                                        hide chocho5
                                        hide chochocl
                                        hide chochoshy
                                        show chocho1
                                        show chochosadna
                                        show chochoc
                                        ch "..."
                                        p "This is not funny...."                                    
                                        scene black with circleirisin               
                                        show nharem0 with circleirisout
                                        jump nharem
                                        
                                   
                                    
                            
                    "Let her blow":                        
                            p "I want to use your mouth today."
                            p "You can undress yourself."
                            ch "If you want it."
                            $ renpy.transition(dissolve)
                            hide chocho1
                            hide chochonna
                            hide chochoshy
                            show chocho5
                            show chochonna
                            show chochoc                                       
                            p "Good."
                            p "The last blowjob was very good."
                            p "I really want to see if you can make it better."
                            ch "Blowjob?"
                            $ renpy.transition(dissolve)
                            show chochoshy 
                            p "Yes..."
                            ch "Mmmm...Blowjob...."
                            $ renpy.transition(dissolve)
                            hide chocho5
                            hide chochonna
                            hide chochoc
                            hide chochoshy
                            p "Calm down."
                            ch "Blowjob!!!"
                            p "Come on Chocho, I know you want my sperm, but calm down."
                            ch "Mmmmmm..."
                            $ renpy.transition(dissolve)
                            show ch2b
                            show ch2bn
                            p "Or not..."
                            p "Just do it!."
                            ch "Mgmmmffmm.."
                            $ renpy.transition(dissolve)
                            hide ch2b
                            hide ch2bn
                            show ch2a
                            show ch2an                
                            p "You really need something in your mouth."
                            ch "Mgmhgdddfssa...."
                            $ renpy.transition(dissolve)
                            hide ch2a
                            hide ch2an
                            show ch2b
                            show ch2bn                
                            ch "GGgrggggfghhh..."
                            p "Like reverse facefuck."
                            $ renpy.transition(dissolve)
                            hide ch2bn
                            show ch2bcl
                            ch "Grgmmmfm... mgmfghfg..."
                            p "You facefuck yourself."
                            $ renpy.transition(dissolve)
                            hide ch2b
                            hide ch2bcl
                            show ch2a
                            show ch2acl
                            ch "Mgmmmfhddd???"
                            p "Newermind."                
                            $ renpy.transition(dissolve)
                            hide ch2a
                            hide ch2acl
                            show ch2b
                            show ch2bcl
                            ch "Mgmhfhmfgdsss..."
                            p "Yes continue..."
                            $ renpy.transition(dissolve)
                            hide ch2b
                            hide ch2bcl
                            show ch2a
                            show ch2adow
                            ch "Mgmmmg!!!"
                            p "I will come soon if you suck so much."
                            $ renpy.transition(dissolve)
                            hide ch2a
                            hide ch2adow
                            show ch2b
                            show ch2bdow
                            ch "Sssgghmmghgmmm...."
                            p "Yes just like that!"
                            $ renpy.transition(dissolve)
                            hide ch2b
                            hide ch2bdow
                            show ch2a
                            show ch2adow
                            p "More...."
                            $ renpy.transition(dissolve)
                            hide ch2a
                            hide ch2adow
                            show ch2b
                            show ch2bdow
                            ch "Gmmhfmmdfmmd..."
                            $ renpy.transition(dissolve)
                            hide ch2b
                            hide ch2bdow
                            show ch2a
                            show ch2adow
                            ch "Grgggggg..."
                            p "I need to train harder."
                            $ renpy.transition(dissolve)
                            hide ch2a
                            hide ch2adow
                            show ch2b
                            show ch2bdow
                            p "kage bunshin no jutsu!"
                            $ renpy.transition(dissolve)
                            show ch2p1
                            ch "????"
                            $ renpy.transition(dissolve)
                            hide ch2b
                            hide ch2bdow
                            show ch2a
                            show ch2adow
                            hide ch2p1
                            show ch2p2
                            p "This is a good use of Shinobi powers."
                            $ renpy.transition(dissolve)
                            hide ch2a
                            hide ch2adow
                            show ch2b
                            show ch2bdow
                            hide ch2p2
                            show ch2p3
                            ch "MMmmmmmmmgmmmmm..."
                            $ renpy.transition(dissolve)
                            hide ch2b
                            hide ch2bdow
                            show ch2a
                            show ch2adow
                            hide ch2p3
                            show ch2p2
                            p "This is the reason why is womans here always happy."
                            $ renpy.transition(dissolve)
                            hide ch2a
                            hide ch2adow
                            show ch2b
                            show ch2bdow
                            hide ch2p2
                            show ch2p1
                            ch "Gmgmmfdmmmd..."
                            $ renpy.transition(dissolve)
                            hide ch2b
                            hide ch2bdow
                            show ch2a
                            show ch2adow
                            hide ch2p3
                            show ch2p2
                            p "Fuck YEAH!!!!" with hpunch
                            hide ch2a
                            hide ch2adow
                            show ch2b
                            show ch2bdow
                            $ eyes = eyes + 1
                            p "Eat this!"
                            $ renpy.transition(dissolve)
                            show ch2sp1
                            hide ch2p2
                            show ch2p1
                            ch "Grgggfghhh...."
                            $ renpy.transition(dissolve)
                            hide ch2p1
                            show ch2p2
                            p "And more...."
                            $ renpy.transition(dissolve)
                            show ch2sp2
                            hide ch2p2
                            show ch2p3
                            ch "!!!!!"
                            $ renpy.transition(dissolve)
                            hide ch2p3
                            show ch2p2
                            p "YEAH One more time...."
                            $ renpy.transition(dissolve)
                            hide ch2p2
                            show ch2p3
                            p "Incoming!"
                            $ renpy.transition(dissolve)
                            show ch2sp3
                            ch "MMGMGMMGMFMMGMFMG...."                
                            $ renpy.transition(dissolve)
                            hide ch2bdow
                            show ch2bcl
                            show ch2sp4
                            ch "Mgmmm...."
                            p "Wow..."
                            ch "Gmmgmfmgmgm..."
                            p "Fucking amazing Chocho."
                            p "...."
                            p "You can drink it all."
                            ch "grmmmm..."
                            $ renpy.transition(dissolve)
                            hide ch2sp2
                            hide ch2sp1
                            hide ch2sp4
                            hide ch2sp3
                            hide ch2p3
                            hide ch2bcl
                            hide ch2b
                            p "You can also dress now."
                            ch "...."
                            $ renpy.transition(dissolve)
                            show chocho1
                            show chochonna
                            show chochoc
                            p "That was a relly good blowjob... I will come back later..."
                            ch "Good..."
                            scene black with circleirisin               
                            show nharem0 with circleirisout
                            jump nharem
                            
                    "From behind":
                            p "I want to fuck you from behind."
                            p "Just undress Chocho."
                            $ renpy.transition(dissolve)
                            hide chocho1
                            hide chochonna
                            hide chochoshy
                            show chocho5
                            show chochonna
                            show chochoc   
                            ch "..."
                            p "Come on, Show me your ass!"
                            ch "If you really want it..."
                            $ renpy.transition(dissolve)
                            hide chocho5
                            hide chochonna
                            hide chochoc
                            hide chochoshy
                            show ch3a
                            show ch3n
                            p "Nice ass."
                            p "I want to play with your ass."
                            ch "Sure...."
                            $ renpy.transition(dissolve)
                            show ch3p1
                            p "It is good to have your approval."                
                            $ renpy.transition(dissolve)
                            hide ch3p1
                            show ch3wet
                            show ch3p2
                            p "Hehe..."
                            $ renpy.transition(dissolve)
                            hide ch3n
                            show ch3cl
                            ch "Mmmmm!!!"
                            $ renpy.transition(dissolve)
                            hide ch3p2
                            show ch3p3
                            p "Good Chocho."
                            $ renpy.transition(dissolve)
                            hide ch3p3
                            show ch3p2
                            ch "Deeper!!!"
                            $ renpy.transition(dissolve)
                            hide ch3p2
                            show ch3p3
                            ch "Deeper!!!"
                            p "Do not shout so loud!"
                            ch "Sorry..."
                            $ renpy.transition(dissolve)
                            hide ch3p3
                            show ch3p4
                            hide ch3cl
                            show ch3shock
                            ch "Argggg..."
                            $ renpy.transition(dissolve)
                            hide ch3p4
                            show ch3p3
                            p "So tight for such a big woman!"
                            $ renpy.transition(dissolve)
                            hide ch3p3
                            show ch3p2
                            ch "..."
                            $ renpy.transition(dissolve)
                            hide ch3p2
                            show ch3p3
                            ch "I control size of my pussy."
                            $ renpy.transition(dissolve)
                            hide ch3p3
                            show ch3p4
                            hide ch3shock
                            show ch3up
                            ch "AAaaa...."
                            p "I know... You tell it before."
                            $ renpy.transition(dissolve)
                            hide ch3p4
                            show ch3p3
                            ch "...."
                            $ renpy.transition(dissolve)
                            hide ch3p3
                            show ch3p2
                            hide ch3up
                            show ch3cl
                            p "Nice....."
                            $ renpy.transition(dissolve)
                            hide ch3p2
                            show ch3p3
                            p "But I should...."
                            menu:
                                "Use toys":
                                    p "Play with you a little..."
                                    $ renpy.transition(dissolve)
                                    show ch3clips
                                    hide ch3p3
                                    show ch3p2
                                    ch "......"
                                    $ renpy.transition(dissolve)
                                    hide ch3p2
                                    p "Do not worry, I brought a whip too."
                                    "Slash!" with hpunch
                                    show ch3sl1
                                    ch "YESSSSS!!!!"
                                    p "Hehe, You are such a dirty little whore."
                                    ch "Little?"
                                    p "What about this?"
                                    $ renpy.transition(dissolve)
                                    show ch3d1
                                    hide ch3cl
                                    show ch3n
                                    ch "!!!!"
                                    ch "What do you want to..."
                                    $ renpy.transition(dissolve)
                                    hide ch3d1
                                    show ch3d2
                                    p "Nothing just put it inside your ass..."
                                    ch "But..."
                                    ch "Argggggg...."
                                    $ renpy.transition(dissolve)
                                    hide ch3d2
                                    show ch3d3
                                    hide ch3n
                                    show ch3shock
                                    ch "GRGGGGGGG!!!!!!"
                                    p "It seems to fit in perfectly."
                                    "Slash!" with hpunch
                                    ch "!!!!"
                                    "Slash!" with hpunch
                                    show ch3sl2
                                    ch "MORE!!!!"
                                    "Slash!" with hpunch
                                    show ch3sl2
                                    hide ch3d3
                                    show ch3d2
                                    p "Huh too hard it almost falls out."
                                    $ renpy.transition(dissolve)
                                    hide ch3d2
                                    show ch3d3
                                    ch "Mmmmm..."
                                    "Slash!" with hpunch
                                    p "More power!!!"
                                    "Slash!" with hpunch
                                    show ch3sl3
                                    hide ch3shock
                                    show ch3up
                                    ch "AAaaaaaa..."
                                    "Slash!" with hpunch
                                    show ch3p1
                                    p "And time for something funny..."
                                    $ renpy.transition(dissolve)
                                    hide ch3p1
                                    show ch3p2
                                    p "But I think this will be fast!!!"
                                    $ renpy.transition(dissolve)
                                    hide ch3p2
                                    show ch3p3
                                    ch "Yessssss..."
                                    $ renpy.transition(dissolve)
                                    hide ch3p3
                                    show ch3p4
                                    ch "Aaaaaaa...."
                                    $ renpy.transition(dissolve)
                                    hide ch3p3
                                    show ch3p2
                                    p "Stop making that sounds of sounds!"
                                    $ renpy.transition(dissolve)
                                    hide ch3p2
                                    show ch3p3
                                    hide ch3up
                                    show ch3cl
                                    ch "MMMMmmmm..."
                                    $ renpy.transition(dissolve)
                                    hide ch3p3
                                    show ch3p4
                                    p "That is sexy too..."
                                    $ renpy.transition(dissolve)
                                    hide ch3p4
                                    show ch3p3
                                    p "I just...."
                                    jump chochocumfbh
                                "Increase boobs size":
                                    p "Time for some expansion technique."
                                    $ renpy.transition(dissolve)
                                    hide ch3p3
                                    show ch3p2
                                    p "Focus..."
                                    $ renpy.transition(dissolve)
                                    hide ch3p2
                                    show ch3p1
                                    p "..."
                                    p "Expansion technique, boobs of the angels!"
                                    $ renpy.transition(dissolve)
                                    hide ch3a
                                    hide ch3p1
                                    hide ch3cl
                                    hide ch3wet
                                    show ch3b
                                    show ch3wet
                                    show ch3p1
                                    show ch3cl
                                    ch "...."
                                    $ renpy.transition(dissolve)
                                    hide ch3cl
                                    show ch3shock
                                    ch "What the fuck?"
                                    $ renpy.transition(dissolve)
                                    hide ch3p1
                                    show ch3p2
                                    p "Nice!!!!"
                                    $ renpy.transition(dissolve)
                                    hide ch3p2
                                    show ch3p3
                                    ch "But..."
                                    "Slap!" with hpunch
                                    hide ch3p3
                                    show ch3p2
                                    show ch3h1
                                    p "Just shut up!"
                                    $ renpy.transition(dissolve)
                                    hide ch3shock
                                    show ch3n
                                    ch "...."
                                    $ renpy.transition(dissolve)
                                    hide ch3p2
                                    show ch3p3
                                    p "Good Chocho..."
                                    $ renpy.transition(dissolve)
                                    hide ch3p3
                                    show ch3p2
                                    ch "....."
                                    $ renpy.transition(dissolve)
                                    hide ch3p2
                                    show ch3p3
                                    ch "Deeper!!!"
                                    $ renpy.transition(dissolve)
                                    hide ch3p3
                                    show ch3p2
                                    ch "Please!!!"
                                    $ renpy.transition(dissolve)
                                    hide ch3p2
                                    show ch3p3
                                    p "No problem..."
                                    $ renpy.transition(dissolve)
                                    hide ch3p3
                                    show ch3p4
                                    ch "Argggg...."
                                    $ renpy.transition(dissolve)
                                    hide ch3n
                                    hide ch3p4
                                    show ch3p3
                                    show ch3cl
                                    p "That ass just shake."
                                    "Slap!" with hpunch
                                    hide ch3p3
                                    show ch3h2
                                    show ch3p2
                                    p "Nice..."
                                    "Slap!" with hpunch
                                    hide ch3p2
                                    show ch3p3
                                    p "Hehe..."
                                    $ renpy.transition(dissolve)
                                    hide ch3p3
                                    show ch3p4
                                    p "But you still look like ..."
                                    $ renpy.transition(dissolve)
                                    hide ch3p4
                                    show ch3p3
                                    ch "What???"
                                    "Slap!" with hpunch
                                    hide ch3p3
                                    show ch3p2
                                    p "I will show you..."
                                    $ renpy.transition(dissolve)
                                    hide ch3p2
                                    show ch3p3
                                    p "Just a moment...."                        
                                    $ renpy.transition(dissolve)
                                    hide ch3p3
                                    show ch3text
                                    show ch3p3                        
                                    p "There it is...."
                                    ch "...."
                                    $ renpy.transition(dissolve)
                                    hide ch3p3
                                    hide ch3cl
                                    show ch3n
                                    show ch3p4
                                    ch "Chubby????"
                                    $ renpy.transition(dissolve)
                                    hide ch3p4
                                    show ch3p3
                                    p "Yeah!"
                                    $ renpy.transition(dissolve)
                                    hide ch3p3
                                    show ch3p2
                                    p "That is what bother you most?"
                                    $ renpy.transition(dissolve)
                                    hide ch3p2
                                    show ch3p3
                                    p "You are such a..."
                                    $ renpy.transition(dissolve)
                                    hide ch3p3
                                    show ch3p4
                                    hide ch3n
                                    show ch3cl
                                    p "....."
                                    $ renpy.transition(dissolve)
                                    hide ch3p4
                                    show ch3p3
                                    p "Fuckkkkkk....."
                                    jump chochocumfbh
                            menu chochocumfbh: 
                                "Cum in":
                                    $ renpy.transition(dissolve)
                                    hide ch3p3
                                    show ch3p4
                                    p "Awesome!!!"
                                    $ renpy.transition(dissolve)
                                    show ch3spin1
                                    ch "YESSSSSSS!!!!"
                                    $ renpy.transition(dissolve)
                                    hide ch3cl
                                    show ch3up
                                    p "YEAH!"                        
                                    $ renpy.transition(dissolve)
                                    show ch3spin2
                                    ch "Aaaaaa....."
                                    p "....."
                                    with fade
                                    p "Coco, your pussy is amazing."
                                    ch "Thanks."
                                
                                "Cum out":
                                    $ renpy.transition(dissolve)
                                    hide ch3p3
                                    show ch3p2
                                    p "Just a moment!"
                                    $ renpy.transition(dissolve)
                                    hide ch3p2
                                    show ch3p1
                                    p "Whoah!"
                                    $ renpy.transition(dissolve)
                                    show ch3spout1
                                    ch "MORE!!!!"
                                    $ renpy.transition(dissolve)
                                    hide ch3cl
                                    show ch3up
                                    p "Fuck!"                        
                                    $ renpy.transition(dissolve)
                                    show ch3spout2
                                    ch "Aaaaaa....."
                                    p "....."
                                    with fade
                                    p "That was funny."
                            $ eyes = eyes + 1
                            p "But you should clean yourself now."
                            p "You look like a little piggy."
                            ch "....."
                            p "Or stay like this if you want..."
                            scene black with circleirisin               
                            show nharem0 with circleirisout
                            jump nharem
                        
                    "She's a Lady":                           
                            p "Chocho, you are so beautiful to me."
                            p "Show me your body in that pink suit!"
                            $ renpy.transition(dissolve)
                            hide chocho1
                            hide chochonna
                            hide chochoshy
                            show chocho2
                            show chochonna
                            show chochoc   
                            ch "You really like it?"
                            p "Of course, I'm loving it."
                            p "I want to fuck you like a lady!"
                            ch "You mean...."
                            $ renpy.transition(dissolve)
                            hide chocho2
                            hide chochonna
                            hide chochoc
                            hide chochoshy
                            show ch1c
                            show ch1na
                            ch "Something like this?"
                            p "Exactly!"
                            p "Ou CHOCHO!!!"
                            p "There are so many things what I want to do with you right now."
                            ch "Where do you want me to start?"
                            p "........."
                            p "First I undress you..."
                            $ renpy.transition(dissolve)
                            hide ch1c
                            hide ch1na
                            show ch1d
                            show ch1na
                            p "And now..."
                            menu:
                                "Use toys and expansion":
                                    p "I just need to concentrate."
                                    p "And play a little with that body."
                                    p "Expansion!"
                                    $ renpy.transition(dissolve)
                                    hide ch1d
                                    hide ch1na
                                    show ch1a
                                    show ch1na
                                    ch "Mmmm.... What you want to do?"
                                    p "You will see."
                                    p "I start with this...."
                                    $ renpy.transition(dissolve)
                                    show ch1r1
                                    ch "Ouch... That hurt..."
                                    p "So maybe if I touch it first..."
                                    $ renpy.transition(dissolve)
                                    show ch1touch
                                    p "It would hurt less right???"
                                    ch "Maybe..."
                                    $ renpy.transition(dissolve)
                                    hide ch1touch
                                    hide ch1na
                                    show ch1r2
                                    show ch1op
                                    ch "!!!!!!!!!!"
                                    ch "OUCHHHHHH!!!"
                                    p "heh... I think it would hurt less..."
                                    ch "No it hurt more!"
                                    p "Lightning style!" with hpunch
                                    show ch1l1
                                    ch "Grgggggg...."
                                    $ renpy.transition(dissolve)
                                    hide ch1op
                                    show ch1cl
                                    ch "AAAAaaaaaaaaa..."
                                    p "Lightnint style, electric boobs!"
                                    $ renpy.transition(dissolve)
                                    show ch1l2
                                    ch "ARGGGG!"
                                    $ renpy.transition(dissolve)
                                    hide ch1cl
                                    show ch1clop
                                    p "Huh... It is harder than it looks like."
                                    p "Maybe I just..."
                                    "Slash!" with hpunch
                                    show ch1sl1
                                    ch "Yes.... Slash me hard..."
                                    "Slash!" with hpunch
                                    p "No problem with that."
                                    $ renpy.transition(dissolve)
                                    hide ch1l2
                                    p "But it is harder to concentrate on other things like."
                                    p "Maybe...."
                                    $ renpy.transition(dissolve)
                                    show ch1an1
                                    hide ch1clop
                                    show ch1cl
                                    ch "What do you want to do with that thing?"
                                    p "Silence!"
                                    "Slash!" with hpunch
                                    show ch1sl2
                                    p "This...."                        
                                    $ renpy.transition(dissolve)
                                    hide ch1an1
                                    show ch1an2
                                    ch "!!!!"
                                    $ renpy.transition(dissolve)
                                    hide ch1cl
                                    show ch1na
                                    ch "I have no problem with that..."
                                    ch "MMMMmmmmm....Just put it deeper..."
                                    $ renpy.transition(dissolve)
                                    hide ch1an2
                                    show ch1an3
                                    p "More Lightnings!"
                                    $ renpy.transition(dissolve)
                                    show ch1l2
                                    ch "Yes, More!"
                                    "Slash!" with hpunch
                                    p "And deeper...."
                                    $ renpy.transition(dissolve)
                                    hide ch1an3
                                    show ch1an4
                                    hide ch1na
                                    show ch1op
                                    ch "Put it all in there!"
                                    "Slash!" with hpunch
                                    p "Hehe.... Ok...."
                                    $ renpy.transition(dissolve)
                                    hide ch1an4
                                    ch "Aaaaaaaaaaaaa....."
                                    p "And it magically disappears."
                                    "Slash!" with hpunch
                                    show ch1sl3
                                    hide ch1op
                                    show ch1org
                                    show ch1milk
                                    ch "YESESESESESESESES!!!!!"
                                    with fade
                                    ch "This is perfect!!!!"
                                    $ renpy.transition(dissolve)
                                    hide ch1l2
                                    p "Sure, it is... But it is hard to hold it longer."                        
                                    p "I feel stronger now... But tired at the same time."
                                    $ chakra = chakra + 1
                                    p "I should end this..."
                                    $ renpy.transition(dissolve)
                                    hide ch1r1
                                    hide ch1l1
                                    p "...."
                                    $ renpy.transition(dissolve)
                                    hide ch1r2
                                    p "I need to get back this thing from your ass too..."
                                    p "Push CHOCHO!"
                                    ch "Ok..."
                                    $ renpy.transition(dissolve)
                                    show ch1an4
                                    hide ch1org
                                    show ch1op
                                    hide ch1milk
                                    ch "ARGGGGG!!!!"
                                    p "Nice...."
                                    p "Maybe I help you a little..."
                                    $ renpy.transition(dissolve)
                                    hide ch1an4
                                    show ch1an3
                                    hide ch1op
                                    show ch1sad
                                    ch "Ouuu..."
                                    ch "It was over already?"
                                    p "Yes Chocho...."
                                    $ renpy.transition(dissolve)
                                    hide ch1an3
                                    show ch1an2
                                    p "Just a last piece..."
                                    $ renpy.transition(dissolve)
                                    hide ch1an2
                                    show ch1an1
                                    p "And it is almost out..."
                                    $ renpy.transition(dissolve)
                                    hide ch1an1
                                    p "Chocho???"
                                    $ renpy.transition(dissolve)
                                    hide ch1sad
                                    show ch1na
                                    p "Ehm... It was funny... But you can dress now.... And heal yourself."
                                    ch "Sure...."
                                    $ renpy.transition(dissolve)
                                    hide ch1na
                                    hide ch1a
                                    hide ch1sl1
                                    hide ch1sl2
                                    hide ch1sl3
                                    ch "....."
                                    $ renpy.transition(dissolve)
                                    show chocho2
                                    show chochonna
                                    p "And now..."
                                    ch "...."
                                    p "Just see you later..."
                                    scene black with circleirisin               
                                    show nharem0 with circleirisout
                                    jump nharem
                                    
                                "Just normal fuck":
                                    p "I am tired today..."
                                    p "Maybe I just fuck you regular today..."
                                    ch "What???"
                                    $ renpy.transition(dissolve)
                                    show ch1a1
                                    p "Just wait...."
                                    $ renpy.transition(dissolve)
                                    hide ch1a1
                                    show ch1a2
                                    ch "Mmmmmmmmm...."
                                    $ renpy.transition(dissolve)
                                    hide ch1a2
                                    show ch1a3
                                    ch "That is nice..."
                                    p "....."
                                    $ renpy.transition(dissolve)
                                    hide ch1a3
                                    show ch1a4
                                    hide ch1na
                                    show ch1shock
                                    ch "Ouch!"
                                    p "To deep?"
                                    $ renpy.transition(dissolve)
                                    hide ch1a4
                                    show ch1a3
                                    ch "It just suprise me a litle."
                                    p "Chocho???"
                                    $ renpy.transition(dissolve)
                                    hide ch1a3
                                    show ch1a2
                                    ch "Yes???"
                                    p "Tell my story about secret Akimichi male expansion Jutsu."
                                    $ renpy.transition(dissolve)
                                    hide ch1a2
                                    show ch1a3
                                    hide ch1shock
                                    show ch1op
                                    ch "You mean punishing Jutsu?"
                                    p "Yes...."
                                    $ renpy.transition(dissolve)
                                    hide ch1a3
                                    show ch1a4
                                    ch "....."
                                    ch "There was a time.....mmmmmmmmm ...... When our clan lead hearing torturing squad."
                                    $ renpy.transition(dissolve)
                                    hide ch1a4
                                    show ch1a3
                                    ch "Enemy Shinobi... more....... wasn't always too talkative."
                                    ch "There was a time.... yessss.... When our clan lead hearing torturing squad."
                                    $ renpy.transition(dissolve)
                                    hide ch1a3
                                    show ch1a2
                                    hide ch1op
                                    show ch1na
                                    ch "When female Shinobi.... aaa.... didn't want to talk our guy start to fuck her."
                                    $ renpy.transition(dissolve)
                                    hide ch1a2
                                    show ch1a3
                                    ch "And start using partial expansion jutsu."
                                    $ renpy.transition(dissolve)
                                    hide ch1a3
                                    show ch1a4
                                    hide ch1na
                                    show ch1cl
                                    ch "Aaaaaaa...."
                                    ch "And...."
                                    $ renpy.transition(dissolve)
                                    hide ch1a4
                                    show ch1a3
                                    ch "He still fucknig her... And slowly..... slowly.... increase the size of his penis."
                                    p "Nice work..."
                                    $ renpy.transition(dissolve)
                                    hide ch1a3
                                    show ch1a2
                                    ch "Captured Shinobi have only two options.... fuckkkk...... tell what she know or die."
                                    $ renpy.transition(dissolve)
                                    hide ch1a2
                                    show ch1a3
                                    p "Look like cruel dead."
                                    $ renpy.transition(dissolve)
                                    hide ch1a3
                                    show ch1a4
                                    hide ch1cl
                                    show ch1clop
                                    ch "Yesssssss..."
                                    ch "Or dead by pleasure...."
                                    $ renpy.transition(dissolve)
                                    hide ch1a4
                                    show ch1a3
                                    hide ch1clop
                                    show ch1na
                                    ch "We need to be carefull.... Mmmm...... how far we decide to expand...."
                                    $ renpy.transition(dissolve)
                                    hide ch1a3
                                    show ch1a2
                                    ch "Yessss.... It could be dangerous..."
                                    $ renpy.transition(dissolve)
                                    hide ch1a2
                                    show ch1a3
                                    hide ch1na
                                    show ch1org
                                    ch "Aaaaaaaa....."
                                    $ renpy.transition(dissolve)
                                    hide ch1a3
                                    show ch1a4
                                    p "Yessss....."
                                    $ renpy.transition(dissolve)
                                    show ch1aspin
                                    ch "OOooo...."
                                    p "Fuck, Fuck, Fuck...."
                                    $ renpy.transition(dissolve)
                                    show ch1aspin2
                                    ch "Mmmmmmmm..."
                                    with fade
                                    $ renpy.transition(dissolve)
                                    hide ch1org
                                    show ch1na
                                    ch "Nice......"
                                    $ eyes = eyes + 1
                                    p "Yes... Just... Normal sex..."
                                    p "With mind control...."
                                    p "...."
                                    p "Just clean yourself now..."
                                    $ renpy.transition(dissolve)
                                    hide ch1na
                                    hide ch1d
                                    hide ch1a4
                                    hide ch1aspin
                                    hide ch1aspin2
                                    p "....."
                                    $ renpy.transition(dissolve)
                                    show chocho5
                                    show chochonna
                                    ch "Do you like looking at my body?"
                                    p "????"
                                    p "Ehm yes, why?"
                                    ch "Nothing... just...."
                                    p "But dress yourself, please... It would not be good if you go out like this."
                                    $ renpy.transition(dissolve)
                                    hide chocho5
                                    hide chochonna
                                    show chocho1
                                    show chochonna
                                    p "That dress??? Meh... ok..."
                                    scene black with circleirisin               
                                    show nharem0 with circleirisout
                                    jump nharem

                                    
                                "Kage bunshin no jutsu":
                                    p "It is just...."
                                    p "One man is simply not enough."
                                    p "But I need to be smart!"
                                    p "Expansion!"
                                    $ renpy.transition(dissolve)
                                    hide ch1d
                                    hide ch1na
                                    show ch1a
                                    show ch1na
                                    p "And now I start with that boobs..."
                                    $ renpy.transition(dissolve)
                                    show ch1touch
                                    p "Nice"
                                    $ renpy.transition(dissolve)
                                    hide ch1touch
                                    show ch1r1
                                    hide ch1na
                                    show ch1op
                                    ch "Ouch!"
                                    p "That fit you best."                
                                    ch "MMMMmmm"
                                    $ renpy.transition(dissolve)
                                    show ch1tf1
                                    ch "Nice...."
                                    $ renpy.transition(dissolve)
                                    hide ch1tf1
                                    show ch1tf2
                                    ch "I love penis between my boobs."
                                    $ renpy.transition(dissolve)
                                    hide ch1tf2
                                    show ch1tf3
                                    hide ch1op
                                    show ch1cl
                                    p "I love it too!"
                                    $ renpy.transition(dissolve)
                                    hide ch1tf3
                                    show ch1tf2
                                    p "Big brown tities."
                                    $ renpy.transition(dissolve)
                                    hide ch1tf2
                                    show ch1tf1
                                    ch "Mmmmmm....."
                                    $ renpy.transition(dissolve)
                                    hide ch1tf1
                                    show ch1tf2
                                    p "Kage bunshin no jutsu!"
                                    p "I need one kage bunshin!"
                                    $ renpy.transition(dissolve)
                                    hide ch1tf2
                                    show ch1tf3    
                                    hide ch1r1
                                    p "To put this in your ass..."
                                    $ renpy.transition(dissolve)
                                    show ch1an1
                                    p "And other one here..."
                                    $ renpy.transition(dissolve)
                                    show ch1nf1
                                    hide ch1an1
                                    show ch1an2
                                    ch "What do you want to do?"
                                    p "Just fuck your nipple a little..."
                                    $ renpy.transition(dissolve)
                                    hide ch1an2
                                    show ch1an3
                                    hide ch1tf3
                                    show ch1tf2 
                                    hide ch1cl
                                    show ch1clop
                                    ch "What???"
                                    p "Just calm down..."
                                    $ renpy.transition(dissolve)
                                    hide ch1an3
                                    show ch1an4
                                    hide ch1tf2
                                    show ch1tf1
                                    hide ch1nf1
                                    show ch1nf2                        
                                    ch "ARGGGGGGGGGGGGGG!!!!!"
                                    p "It fits in perfectly!!!"
                                    $ renpy.transition(dissolve)
                                    hide ch1tf1
                                    show ch1tf2
                                    p "I should put it deeper!!!"
                                    $ renpy.transition(dissolve)
                                    show ch1nfblood
                                    hide ch1nf2
                                    show ch1nf3
                                    hide ch1clop
                                    show ch1shock
                                    ch "AAaaaaaaa!!!!"
                                    p "Huh???"
                                    $ renpy.transition(dissolve)
                                    hide ch1tf2
                                    show ch1tf3
                                    hide ch1nf3
                                    show ch1nf2
                                    p "That was a little harder than I want."
                                    ch "!!!!"
                                    $ renpy.transition(dissolve)
                                    hide ch1tf3
                                    show ch1tf2
                                    p "Just calm down and heal yourself..."
                                    ch "....."
                                    $ renpy.transition(dissolve)
                                    hide ch1shock
                                    show ch1clop
                                    ch "Healing technique Nipple doctor!"
                                    $ renpy.transition(dissolve)
                                    hide ch1tf2
                                    show ch1tf1
                                    hide ch1nfblood
                                    p "???"
                                    p "And some Shinobi thinks that the technique was rubbish."
                                    p "I want more fun!"
                                    $ renpy.transition(dissolve)
                                    hide ch1tf1
                                    show ch1tf2
                                    hide ch1nf2
                                    show ch1nf3
                                    show ch1a1
                                    p "And now I can continue...."
                                    $ renpy.transition(dissolve)
                                    hide ch1tf2
                                    show ch1tf3
                                    hide ch1nf3
                                    show ch1nf2
                                    ch "Aaaaaaaaaaaaa..."
                                    $ renpy.transition(dissolve)
                                    hide ch1tf3
                                    show ch1tf2
                                    hide ch1nf2
                                    show ch1milk
                                    hide ch1clop
                                    show ch1org
                                    show ch1nf3                        
                                    ch "Yesss!!!!"
                                    p "Fuck!!!!"
                                    $ renpy.transition(dissolve)
                                    hide ch1tf2
                                    show ch1tf3
                                    hide ch1nf3
                                    show ch1nf2
                                    show ch1tfsp1
                                    p "First clone is ready!!!"
                                    $ renpy.transition(dissolve)
                                    hide ch1nf2
                                    show ch1nf3
                                    show ch1tfsp2
                                    ch "Moreee!!!!"
                                    $ renpy.transition(dissolve)
                                    hide ch1nf3
                                    show ch1nf2
                                    show ch1tfsp3
                                    ch "AAAaa.a..."
                                    $ renpy.transition(dissolve)
                                    hide ch1nf2
                                    show ch1nf3
                                    show ch1nfsp1
                                    p "Yeah!!!!"
                                    $ renpy.transition(dissolve)
                                    show ch1nfsp2
                                    hide ch1org
                                    show ch1clop
                                    ch "So much sperm!"
                                    $ renpy.transition(dissolve)
                                    show ch1aspout
                                    p "Fuck!!!!!"
                                    $ eyes = eyes + 1
                                    ch "....."
                                    with fade
                                    $ renpy.transition(dissolve)
                                    hide ch1clop
                                    show ch1na
                                    p "Huh... I think that was everything I have right now..."
                                    ch "So much....."
                                    p "....."
                                    p "That is so......"
                                    p "We need to pull my penises out of you..."
                                    $ renpy.transition(dissolve)
                                    hide ch1na
                                    hide ch1a
                                    hide ch1nf3
                                    hide ch1tf3
                                    hide ch1nfsp1
                                    hide ch1nfsp2
                                    hide ch1tfsp1
                                    hide ch1tfsp2
                                    hide ch1tfsp3
                                    hide ch1aspout
                                    hide ch1milk
                                    hide ch1an4
                                    hide ch1a1
                                    p "...."
                                    ch "Please, pull it out Carefully."
                                    p "Sure...."
                                    with fade
                                    ch "......"
                                    ch "Aaaaaa....."
                                    with fade
                                    p "We did it!"
                                    with fade
                                    p "Now, put that pink suit on you..."
                                    $ renpy.transition(dissolve)
                                    show ch1b
                                    show ch1na
                                    p "How do you feel?"
                                    ch "I feel perfect."
                                    p "I am exhausted!"
                                    p "I need some rest now... Bye.."
                                    scene black with circleirisin               
                                    show nharem0 with circleirisout
                                    jump nharem
            else:
                "How you want to talk with her if she is not here?"
                scene black with circleirisin               
                show dharem0 with circleirisout
                jump dharem
                
                
            
                
####################################### 19 je max pre Ino
        "Pick Ino":
            
            if inoslave >=20:
                        $ renpy.transition(dissolve)
                        show inon1
                        show inonna
                        p "It worked....What now?"
                        menu inon2222:
                            "Strip":                                
                                    p "Time to take off her clothes..." 
                                    i "....."
                                    p "Strip!" with hpunch
                                    i "Sure..."
                                    $ renpy.transition(dissolve)
                                    hide inon1
                                    hide inonna
                                    show inon3
                                    show inonna
                                    p "Nice, looks like there is no more resistance to that order."
                                    p "Her boobs are so adorable..."
                                    p "Maybe I can play with them a little..."
                                    "You grab her boobs and start to touching her whole body..."
                                    "But you didn't see any reaction..."
                                    "At least it is fun!"
                                    p "Hehe.... My chakra is running low I should cancel this jutsu."
                                    p "Ok Ino you can dress now..."
                                    $ renpy.transition(dissolve)
                                    hide inon2
                                    hide inon3
                                    hide inonna
                                    show inon1
                                    show inonna
                                    p "Good girl..."
                                    p "Time to do something else..."
                                    scene black with circleirisin               
                                    show nharem0 with circleirisout
                                    jump nharem
                                
                            "Massage":                                
                                    p "Time for a massage!" 
                                    i "Massage...."
                                    $ renpy.transition(dissolve)
                                    hide inon1
                                    hide inonna
                                    show inon3
                                    show inonna
                                    $ renpy.transition(dissolve)
                                    hide inon3
                                    hide inonna
                                    show ino3n1
                                    show ino3nor
                                    p "Huh, that was fast!"
                                    p "It looks like really want it Ino."
                                    i "...."
                                    p "Say it girl..."
                                    i "Please touch my body..."
                                    $ renpy.transition(dissolve)
                                    hide ino3nor
                                    show ino3cl
                                    show ino3h3
                                    i "Mmmmm...*moan*"
                                    p "You really like my touch right?"
                                    p "And if I use both hands..."
                                    $ renpy.transition(dissolve)
                                    hide ino3clsad
                                    hide ino3hap
                                    hide ino3cl
                                    show ino3hap
                                    show ino3h4
                                    p "Yes you really like it..."
                                    i "Yesssss..."
                                    "You start to massaging her body."
                                    i "Touch me more please...."
                                    p "Sure...."
                                    p "Good we can continue...."
                                    menu:
                                        "Touch her pussy":
                                            "You slowly release her boobs..."    
                                            $ renpy.transition(dissolve)
                                            hide ino3h3
                                            hide ino3h4
                                            hide ino3hap
                                            show ino3nor
                                            p "What now?"
                                            i "Please touch my pussy..."
                                            $ renpy.transition(dissolve)
                                            show ino3h1
                                            p "What a nice body...."
                                            $ renpy.transition(dissolve)
                                            hide ino3h1
                                            show ino3h2
                                            hide ino3nor
                                            hide ino3sad
                                            show ino3cl
                                            i "Mmmmm...*moan*"
                                            $ renpy.transition(dissolve)
                                            hide ino3h2
                                            show ino3h1
                                            p "You like it right?"
                                            $ renpy.transition(dissolve)
                                            hide ino3h1
                                            show ino3h2
                                            hide ino3cl
                                            show ino3clop
                                            i "Yessss...."
                                            $ renpy.transition(dissolve)
                                            hide ino3h2
                                            show ino3h1
                                            i "More.....*moan*"
                                            $ renpy.transition(dissolve)
                                            hide ino3h1
                                            show ino3h2
                                            i "Aaaarg...*Heavy breathing*"
                                            $ renpy.transition(dissolve)
                                            show ino3drops
                                            p "Nice Ino..."
                                            p "Looks like you really enjoyed it..."
                                            i "*Exhausted*"
                                            p "But everything once end.... you can dress now."
                                            i "Yesssss......"
                                            $ renpy.transition(dissolve)
                                            hide ino3n1
                                            hide ino3nor
                                            hide ino3h3
                                            hide ino3h2
                                            hide ino3clop
                                            hide ino3drops
                                            hide ino3h4
                                            show inon1
                                            show inonna
                                            p "Good girl..."
                                            i "Thanks..."
                                            scene black with circleirisin               
                                            show nharem0 with circleirisout
                                            jump nharem
                                        "Just boobs":
                                            p "I just play a little more with that boobs..."
                                            with fade
                                            "You give a nice massage to Ino."
                                            "It is nice to touch her boobs..."                                      
                                            with fade
                                            p "Ok you can dress now."
                                            $ renpy.transition(dissolve)
                                            hide ino3n1
                                            hide ino3hap
                                            hide ino3cl
                                            hide ino3nor
                                            hide ino3h3
                                            hide ino3h4
                                            show inon1
                                            show inonna
                                            p "Hmm... You still look good..."
                                            i "*moan*"
                                            p "Nevermind..."
                                            scene black with circleirisin               
                                            show nharem0 with circleirisout
                                            jump nharem
                                
                            "Play with her":  
                                        p "Ok Ino. Strip." 
                                        i "..."
                                        $ renpy.transition(dissolve)
                                        hide inon1
                                        hide inonna
                                        show inon3
                                        show inonna
                                        p "What a nice body...."
                                        p "What should I do now?"
                                        menu:
                                            "Cum on her":
                                                p "This is probably best option."
                                                p "Hmmmm.... *fap fap fap*"
                                                i "..."
                                                p "Show me your tounge! *fap fap fap*"
                                                $ renpy.transition(dissolve)
                                                hide inonna
                                                show inonnaop
                                                p "Yes! *fap fap fap*"
                                                i "...."
                                                p "Fuck!!! *Spurt*"
                                                $ renpy.transition(dissolve)
                                                show inosperm
                                                i "......"
                                                p "Hehe... Looks like you need to clean yourself..."
                                                i "...."
                                                p "You can dress up too!"
                                                $ renpy.transition(dissolve)
                                                hide inon3
                                                hide inonnaop
                                                show inon1
                                                show inonna
                                                hide inosperm
                                                p "Don't worry, we will do something more funny next time."
                                                p "And you will do all the job, not me!"
                                                scene black with circleirisin               
                                                show nharem0 with circleirisout
                                                jump nharem
                                                
                                            "Expansion":
                                                p "Time forexpansion technique."
                                                p "I love her busty version."
                                                p "Concentrate..."
                                                p "Expansion!"
                                                $ renpy.transition(dissolve)
                                                hide inon3
                                                hide inonna
                                                show inon4
                                                show inonna
                                                i "Mmmmmm.... *moan*"
                                                p "Nice!"
                                                p "But I want more!"
                                                p "Expansion!"
                                                with fade
                                                $ renpy.transition(dissolve)
                                                hide inonna
                                                show inoclsad
                                                i "AAA..... *hurt*"
                                                p "Fuck you Ino.  I know they can be bigger!"
                                                p "Expansion!" with hpunch
                                                hide inon4
                                                hide inoclsad
                                                show inon5
                                                show inoclop
                                                p "hehe... Nice..."
                                                p "This is the size that fit you more..."
                                                i "Ouch...."
                                                $ renpy.transition(dissolve)
                                                show inotouch1
                                                p "Mmmm.... That size...."
                                                $ renpy.transition(dissolve)
                                                show inotouch2
                                                show inomilk3
                                                hide inoclop
                                                show inonnaorg
                                                i "aaaaaaaa.... *squirt*"
                                                p "So much milk....."
                                                p "hehe.... You are really interesting...."
                                                i "Yessss...."
                                                $ renpy.transition(dissolve)
                                                hide inomilk3
                                                p "But it is time to cancel it..."
                                                $ renpy.transition(dissolve)
                                                hide inotouch1
                                                p "Expansion Kai!"
                                                $ renpy.transition(dissolve)
                                                hide inotouch2
                                                hide inon5
                                                hide inonnaorg
                                                show inon3
                                                show inocl
                                                p "Now you can dress..."
                                                $ renpy.transition(dissolve)
                                                hide inon3
                                                hide inocl
                                                show inon1
                                                show inocl
                                                p "And do whatever you want... Bye...."
                                                scene black with circleirisin               
                                                show nharem0 with circleirisout
                                                jump nharem
                                                
                                            "Use clips":
                                                    p "Maybe i can use that clips...."
                                                    p "But not on that small boobs..."
                                                    p "Expanison!"
                                                    $ renpy.transition(dissolve)
                                                    hide inon3
                                                    hide inonna
                                                    show inon4
                                                    show inonna
                                                    i "Mmmmmm.... *moan*"
                                                    p "Now there is more place to clips. *pinch*"
                                                    $ renpy.transition(dissolve)
                                                    show inoclip1
                                                    hide inonna
                                                    show inonnaop
                                                    i "Arghhhh!!!"
                                                    $ ninjutsu = ninjutsu + 1
                                                    p "Hehe Nice...."
                                                    i "!!!!!"
                                                    p "And one more here... *pinch*"
                                                    $ renpy.transition(dissolve)
                                                    show inoclip2
                                                    hide inonnaop
                                                    show inoclop
                                                    i "!!!!!!!"
                                                    p "It really fit you..."
                                                    p "But it looks like you are not satisfied."
                                                    i "...."
                                                    p "Lightning style!"
                                                    $ renpy.transition(dissolve)
                                                    show inolight1
                                                    i "Yesssss.... *groaning*"
                                                    p "You really enjoy it right?"
                                                    $ renpy.transition(dissolve)
                                                    show inoclip2
                                                    hide inoclop
                                                    show inonnaop
                                                    i "...."
                                                    p "Full power!!!"
                                                    $ renpy.transition(dissolve)
                                                    show inolight2
                                                    i "AAA.... *groaning*"
                                                    p "Heh...."
                                                    $ renpy.transition(dissolve)
                                                    show inomilk2
                                                    hide inonnaop
                                                    show inonnaorg
                                                    i "More..... *squirt*"
                                                    p "Hehe...."
                                                    $ renpy.transition(dissolve)
                                                    hide inolight2
                                                    p "It is fun but hard to keep..."
                                                    $ renpy.transition(dissolve)
                                                    hide inolight1
                                                    p "You are really nasty...."
                                                    p "But my chakra is really low now..."
                                                    p "I should cancel it."
                                                    i "*moan*"
                                                    p "Expansion kai!"
                                                    $ renpy.transition(dissolve)
                                                    hide inon4
                                                    hide inoclip2
                                                    hide inoclip1
                                                    hide inomilk2
                                                    hide inonnaorg
                                                    show inon3
                                                    show inonnaop
                                                    p "You can dress now..."
                                                    $ renpy.transition(dissolve)
                                                    hide inon3
                                                    hide inonnaop
                                                    show inon1
                                                    show inonnaop
                                                    p "Good..."
                                                    p "Or maybe you should stay naked?"
                                                    i "...."
                                                    p "Who cares..."
                                                    scene black with circleirisin               
                                                    show nharem0 with circleirisout
                                                    jump nharem        
                                                
                                
                            "Blowjob":
                                        p "I want to fuck your mouth today."                                        
                                        p "You know what to do now."
                                        i "...."
                                        $ renpy.transition(dissolve)
                                        hide inon1
                                        hide inonna
                                        show inon3
                                        show inonna
                                        p "Come on, get into the position."
                                        $ renpy.transition(dissolve)
                                        hide inon3
                                        hide inonna
                                        show ino4d
                                        show ino4dok
                                        p "It looks like you really want to suck my cock right?"
                                        $ renpy.transition(dissolve)
                                        show ino4bl1
                                        i "..."
                                        p "That was yes right?"
                                        $ renpy.transition(dissolve)
                                        hide ino4d
                                        hide ino4dok
                                        hide ino4bl1                                        
                                        show ino4a
                                        show ino4aok  
                                        show ino4bl1
                                        i "....."
                                        p "You can take it in your mouth now."
                                        i "....."
                                        p "Do not worry I will help you..."
                                        $ renpy.transition(dissolve)
                                        hide ino4bl1
                                        hide ino4aok 
                                        show ino4acl
                                        show ino4bl2
                                        i "Huh??? *Slurp smack drip*"
                                        p "Yes that is nice..."
                                        $ renpy.transition(dissolve)
                                        hide ino4bl2
                                        hide ino4acl
                                        show ino4aclop
                                        show ino4bl1
                                        p "But you should try harder...."
                                        p "You should be able to put it all in!"
                                        i ".... *cough*"
                                        p "Take a deep breath!"
                                        $ renpy.transition(dissolve)
                                        hide ino4bl1
                                        hide ino4aclop
                                        show ino4acl
                                        show ino4bl2
                                        p "Deeper!!!"
                                        i "*Slurp*"
                                        $ renpy.transition(dissolve)
                                        hide ino4bl2
                                        hide ino4acl
                                        show ino4acl
                                        show ino4bl3
                                        i "Grggggrhhh.... *Slurp gag cough*"
                                        p "Fuck... "
                                        p "deeper!!!!"
                                        $ renpy.transition(dissolve)
                                        hide ino4bl3
                                        hide ino4acl
                                        show ino4aokop
                                        show ino4bl4       
                                        i "mgmmhmmm... * choke*"
                                        p "YEAH!!!"
                                        $ renpy.transition(dissolve)
                                        hide ino4bl4
                                        hide ino4aokop
                                        show ino4aokop
                                        show ino4bl3
                                        i "Glurp...."
                                        p "And again!"
                                        $ renpy.transition(dissolve)
                                        hide ino4bl3
                                        hide ino4aokop
                                        show ino4aokop
                                        show ino4bl4 
                                        i "Grgggggggg... * choke*"    
                                        p "Yeah... You love it...."
                                        menu:
                                            "Increase boob size":
                                                p "It will be nice to increase it them for a little..."                                                
                                                p "Expansion!!!"
                                                $ renpy.transition(dissolve)
                                                hide ino4a
                                                show ino4b
                                                hide ino4bl4
                                                hide ino4aokop
                                                show ino4acl
                                                show ino4bl3
                                                i "MGMMMGGG!!! *Slurp*"
                                                p "Hehe nice!!!"
                                                $ renpy.transition(dissolve)
                                                hide ino4bl3
                                                hide ino4acl
                                                show ino4aokop
                                                show ino4bl4
                                                p "Shit I think I will cum soon...."
                                                
                                            "Just Cum":
                                                p "Fuck this is just so good...."
                                                $ renpy.transition(dissolve)
                                                hide ino4bl4
                                                hide ino4aokop
                                                show ino4acl
                                                show ino4bl3
                                                i "ghmmmm....*Slurp*"
                                                $ renpy.transition(dissolve)
                                                hide ino4bl3
                                                hide ino4acl
                                                show ino4aokop
                                                show ino4bl4
                                                p "Shit I think I will cum soon...."
                                                
                                        menu:
                                            "Cum in":
                                                p "Fuck! Take it ! *spurt*"
                                                $ renpy.transition(dissolve)                                        
                                                hide ino4aokop
                                                show ino4acl
                                                hide ino4bl4
                                                show ino4bl4
                                                show ino4blin
                                                p "YEAH!!! *spurt*"
                                                i "!!!! * choke*"
                                                p "Hehe... Good girl... Just drink it now and celan my penis...."
                                                i "grggfggg... *gulp*"
                                                with fade
                                                i "chrrrr....*swallow*"
                                                $ renpy.transition(dissolve)                                        
                                                hide ino4blin                                     
                                                p "Good job Ino."
                                                $ renpy.transition(dissolve) 
                                                hide ino4acl
                                                show ino4aclop
                                                hide ino4bl4
                                                show ino4bl1
                                                p "My penis is clean now!"
                                                i "....*swallow*"
                                                p "You can dress now...."
                                                $ renpy.transition(dissolve)
                                                hide ino4aokop
                                                hide ino4aclop
                                                hide ino4a
                                                hide ino4b
                                                hide ino4bl1
                                                hide ino4blout
                                                p "It is nice to know that I can cum in mouth too..."
                                                $ renpy.transition(dissolve)
                                                show inon1
                                                show inonnaop
                                                p "Anyway.... See you later..."
                                                scene black with circleirisin               
                                                show nharem0 with circleirisout
                                                jump nharem 
                                                
                                            "Cum out":
                                                $ renpy.transition(dissolve)
                                                hide ino4bl4
                                                hide ino4aokop
                                                show ino4acl
                                                show ino4bl3
                                                i "Grggggrhhh.... *Slurp gag cough*"
                                                p "Fuck... That is nice!"
                                                p "I think I will cum on your face...."
                                                $ renpy.transition(dissolve)
                                                hide ino4bl3
                                                hide ino4acl
                                                show ino4acl
                                                show ino4bl2
                                                i "mgmmhmmm... * slurp*"
                                                p "Fuck! Take it !"
                                                $ renpy.transition(dissolve)
                                                hide ino4bl2
                                                hide ino4acl
                                                show ino4aokop
                                                show ino4bl1
                                                p "YEAH!!! *spurt*"
                                                $ renpy.transition(dissolve)
                                                show ino4blout
                                                i "!!!!"
                                                with fade
                                                p "That was good..."
                                                p "But it can be better you need to try harder next time!"
                                                i ".... *drip*"
                                                p "You can dress now... And clean yourself...."
                                                $ renpy.transition(dissolve)
                                                hide ino4aokop
                                                hide ino4a
                                                hide ino4b
                                                hide ino4bl1
                                                hide ino4blout
                                                p ".... Maybe I shuld cum in your mouth next time...."
                                                $ renpy.transition(dissolve)
                                                show inon1
                                                show inonnaop
                                                p "Huh? You are clean already?"
                                                i "..."
                                                p "Ok..."
                                                scene black with circleirisin               
                                                show nharem0 with circleirisout
                                                jump nharem 
                                            
                                        
                                        
                                
                            "Titfuck":
                                
                                        p "Ok Ino. Time to fuck your tits..."                                         
                                        i "..."
                                        p "Lay down and take your clothes off."
                                        $ renpy.transition(dissolve)
                                        hide inon1
                                        hide inonna    
                                        show ino3n1
                                        show ino3nor
                                        p "Yes... This is nice..."
                                        p "But this tits is now just too small for me..."
                                        p "Expansion!"
                                        $ renpy.transition(dissolve)
                                        hide ino3n1
                                        hide ino3nor
                                        show ino3n2
                                        show ino3shy
                                        show ino3shock
                                        i "Argggg.... *moan*"
                                        p "Wow!!! That is better..."    
                                        p "I really want to stick it in now!"
                                        $ renpy.transition(dissolve)
                                        show ino3tf1
                                        p "Just like that!"
                                        $ renpy.transition(dissolve)
                                        hide ino3tf1
                                        show ino3tf2
                                        i "MMmmm....*moan*"
                                        $ renpy.transition(dissolve)
                                        hide ino3tf2
                                        hide ino3shock
                                        show ino3cl
                                        show ino3tf3
                                        p "Shit this is so good!"
                                        $ renpy.transition(dissolve)
                                        hide ino3tf3
                                        show ino3tf4
                                        p ".... *slip*"
                                        $ renpy.transition(dissolve)
                                        hide ino3tf4
                                        show ino3tf3
                                        p "*slip slip*"
                                        i "Mmmmm..."
                                        $ renpy.transition(dissolve)
                                        hide ino3tf3
                                        show ino3tf2
                                        p "Your tits is so soft!"                                        
                                        $ renpy.transition(dissolve)
                                        hide ino3tf2
                                        show ino3tf3
                                        hide ino3cl
                                        show ino3clop
                                        p "Just fucking amazing!"
                                        $ renpy.transition(dissolve)
                                        hide ino3tf3
                                        show ino3tf4
                                        p ".... *slip*"
                                        $ renpy.transition(dissolve)
                                        hide ino3tf4
                                        show ino3tf3
                                        p "Yeah!!! I am almost *slurp*"
                                        $ renpy.transition(dissolve)
                                        hide ino3tf3
                                        show ino3tf4
                                        show ino3tfsp1
                                        p "YES!!!! *slurp*"
                                        $ renpy.transition(dissolve)
                                        hide ino3tf4
                                        show ino3tf3
                                        hide ino3tfsp1
                                        show ino3tfsp1
                                        i "Aaaaa..."
                                        $ renpy.transition(dissolve)
                                        hide ino3tf3
                                        show ino3tf2
                                        hide ino3tfsp1
                                        show ino3tfsp1
                                        show ino3tfsp2
                                        p "You are really pretty Ino..."
                                        p "hehe.... *drop*"
                                        i "Mmmm...*lick*"
                                        $ renpy.transition(dissolve)
                                        hide ino3clop
                                        show ino3hap
                                        hide ino3tfsp1
                                        p "Huh?"
                                        p "You already start to lick it?"
                                        p "Good girl. *You tapped Ino on the head*"
                                        $ renpy.transition(dissolve)
                                        hide ino3tfsp2
                                        hide ino3tf2
                                        hide ino3shy
                                        p "You can dress now..."
                                        $ renpy.transition(dissolve)
                                        hide ino3n2
                                        hide ino3hap
                                        p "You are really amazing!"
                                        $ renpy.transition(dissolve)
                                        show inon1
                                        show inonna
                                        p "You still look happy... I know why...."
                                        scene black with circleirisin               
                                        show nharem0 with circleirisout
                                        jump nharem 
                            
                            "Fuck pussy":                                
                                        p "Time to fuck your pussy..."                                         
                                        i "Yes!"
                                        p "Are you looking forward to it? Me too..."
                                        p "Just ....."
                                        $ renpy.transition(dissolve)
                                        hide inon1
                                        hide inonna
                                        show ino3n1
                                        show ino3hap
                                        p "Huh??, That was fast. Like you really want it.."
                                        show ino3shy
                                        i "Please fuck me..."
                                        p "Lol... If you really want it..."
                                        $ renpy.transition(dissolve)
                                        show ino3p1
                                        i ".... *mumble*"
                                        p "Tell it one more time..."
                                        $ renpy.transition(dissolve)
                                        hide ino3hap
                                        show ino3clop
                                        i "Please, please, please, fuck me..."
                                        $ renpy.transition(dissolve)
                                        hide ino3p1
                                        show ino3p2
                                        hide ino3clop
                                        show ino3cl                                        
                                        i "Yesss!!!!"
                                        p "You are so cute Ino. Just..."
                                        $ renpy.transition(dissolve)
                                        hide ino3p2
                                        show ino3p3
                                        p "A little deeper...."
                                        $ renpy.transition(dissolve)
                                        hide ino3p3
                                        show ino3p4
                                        hide ino3cl
                                        show ino3clop 
                                        i "More....*moan*"
                                        $ renpy.transition(dissolve)
                                        hide ino3p4
                                        show ino3p3
                                        p "Amazing pussy..."
                                        $ renpy.transition(dissolve)
                                        hide ino3p3
                                        show ino3p4
                                        i "Aaaaaa..."
                                        $ renpy.transition(dissolve)
                                        hide ino3p4
                                        show ino3p3
                                        p "That is so good..."
                                        menu inofupu111:
                                            "Lightning fuck":
                                                p "Time for some fun... *pinch*"
                                                $ renpy.transition(dissolve)
                                                show ino3clips
                                                hide ino3clop
                                                show ino3shock
                                                i "Arggg...."  
                                                $ renpy.transition(dissolve)
                                                hide ino3p3
                                                show ino3p4
                                                p "Nice....And now release a little lightning..."
                                                $ renpy.transition(dissolve)                                                
                                                hide ino3p4
                                                show ino3p3
                                                show ino3l1
                                                i "Mmmmmm *moan*"
                                                $ renpy.transition(dissolve)                                                
                                                hide ino3p3
                                                show ino3p4
                                                show ino3l2
                                                show ino3l3
                                                p "hehe... Time to fun!"
                                                $ renpy.transition(dissolve)                                                
                                                hide ino3p4
                                                show ino3p3
                                                show ino3milk
                                                hide ino3shock
                                                show ino3clsad
                                                show ino3l4
                                                hide ino3l3
                                                p "heh..."
                                                $ renpy.transition(dissolve)
                                                hide ino3p3
                                                show ino3p4
                                                show ino3l5
                                                hide ino3l4
                                                p "Slowly..."
                                                $ renpy.transition(dissolve)
                                                hide ino3p4
                                                show ino3p3
                                                show ino3l3
                                                hide ino3l5
                                                p "And more power!"
                                                $ renpy.transition(dissolve)
                                                hide ino3p3
                                                show ino3p4
                                                show ino3l4
                                                i "GRGGGG!!!*zap*"
                                                $ renpy.transition(dissolve)
                                                hide ino3p4
                                                show ino3p3
                                                show ino3l5
                                                i "ZZzzzzz.... *Pain*"
                                                $ renpy.transition(dissolve)
                                                hide ino3l5
                                                hide ino3p3
                                                show ino3p4
                                                hide ino3milk
                                                p "Huh... I am loosing power...."
                                                $ renpy.transition(dissolve)
                                                hide ino3l4
                                                hide ino3p4
                                                show ino3p3
                                                i "....."
                                                $ renpy.transition(dissolve)
                                                hide ino3l3
                                                hide ino3l2
                                                hide ino3l1
                                                hide ino3p3
                                                show ino3p4
                                                hide ino3clsad
                                                show ino3clop
                                                i "Ahhhhh...."
                                                $ renpy.transition(dissolve)
                                                hide ino3p4
                                                show ino3p3
                                                hide ino3clips
                                                jump inofupu111
                                                
                                                
                                            "Cum in":
                                                p "That is my limit!"
                                                $ renpy.transition(dissolve)
                                                hide ino3p3
                                                show ino3p4
                                                show ino3milk                                        
                                                i "YES!!! *sqiurt*"
                                                $ renpy.transition(dissolve)
                                                hide ino3p4
                                                show ino3p3
                                                hide ino3clop 
                                                show ino3org
                                                p "Yeah! *slurp*"
                                                $ renpy.transition(dissolve)
                                                hide ino3p3
                                                show ino3p4
                                                show ino3pspin1
                                                p "!!!!*slurp*"
                                                $ renpy.transition(dissolve)
                                                show ino3pspin2
                                                p "....."
                                                with fade
                                                p "That was.... good... *drop*"
                                                $ renpy.transition(dissolve)
                                                hide ino3org
                                                show ino3cl
                                                i "......*drop*"
                                                i "Just..."
                                                
                                            "Cum out":
                                                p "Shit, you are amazing!"
                                                $ renpy.transition(dissolve)
                                                hide ino3p3
                                                show ino3p4
                                                show ino3milk                                        
                                                i "OOoooooooo!!! *sqiurt*"
                                                $ renpy.transition(dissolve)
                                                hide ino3p4
                                                show ino3p3
                                                p "Nice!"
                                                $ renpy.transition(dissolve)
                                                hide ino3p3
                                                show ino3p2
                                                hide ino3clop 
                                                show ino3org
                                                p "Fuck almost!!!"
                                                $ renpy.transition(dissolve)
                                                hide ino3p2
                                                show ino3p1                                                
                                                p "Yeah! *slurp*"
                                                $ renpy.transition(dissolve)
                                                show ino3pspout1
                                                p "!!!!*slurp*"
                                                $ renpy.transition(dissolve)
                                                show ino3pspout2
                                                p "YEAH!!!!"
                                                with fade
                                                p "What an incredible fuck she is!!! *drop*"
                                                $ renpy.transition(dissolve)
                                                hide ino3org
                                                show ino3cl
                                                i "......*drop*"
                                                i "Mmmm....."
                                                
                                        
                                        p "Incredible... And you really enjoy it!!!."
                                        p "But first clean yourself..."
                                        $ renpy.transition(dissolve)
                                        hide ino3pspin1
                                        hide ino3pspin2
                                        hide ino3pspout1
                                        hide ino3pspout2
                                        hide ino3shy
                                        hide ino3milk
                                        hide ino3p4
                                        hide ino3p1
                                        p "Now you can dress..."                                    
                                        $ renpy.transition(dissolve)
                                        hide ino3n1
                                        hide ino3cl
                                        hide ino3nor
                                        p "...."
                                        $ renpy.transition(dissolve)
                                        show inon1
                                        show inonna
                                        p "Ok... Now back to the work..."
                                        scene black with circleirisin               
                                        show nharem0 with circleirisout
                                        jump nharem 
                                        
                                
                            "Fuck ass":
                              
                                        p "Ok... So it is time to fuck your ass."
                                        i "Sure..."
                                        $ renpy.transition(dissolve)
                                        hide inon1
                                        hide inonna
                                        show ino4d
                                        show ino4dok
                                        p "You really want it right girl? *mlask*"
                                        p "But there is much more possibilities, so what should I do?"
                                        menu inoassfuck5555:
                                            "Toys":
                                                if healscroll == 1:
                                                    p "Time to play a little..."
                                                    p "First I need to prepare...."
                                                    $ renpy.transition(dissolve)
                                                    hide ino4sl1
                                                    hide ino4sl2
                                                    hide ino4sl3
                                                    hide ino4sl4
                                                    hide ino4slbl
                                                    hide ino4text1
                                                    hide ino4text2
                                                    hide ino4ap4
                                                    hide ino4dok
                                                    hide ino4d
                                                    hide ino4e
                                                    hide ino4f
                                                    show ino4d
                                                    show ino4dok  
                                                    with fade
                                                    p "Ok... Maybe if I start with something like..."
                                                    $ renpy.transition(dissolve)
                                                    show ino4ap1
                                                    i "...."
                                                    $ renpy.transition(dissolve)
                                                    hide ino4ap1
                                                    show ino4ap2
                                                    p "Still no reaction..."
                                                    $ renpy.transition(dissolve)
                                                    hide ino4ap2
                                                    show ino4ap3
                                                    p "I just pull it in and try something else..."
                                                    $ renpy.transition(dissolve)
                                                    hide ino4ap3
                                                    show ino4ap4
                                                    i "Uhmpf...."
                                                    p "Ok time for..."
                                                    p "Expansion!!!!"
                                                    $ renpy.transition(dissolve)
                                                    hide ino4ap4
                                                    hide ino4dok
                                                    hide ino4d
                                                    show ino4e
                                                    show ino4dcl                                                
                                                    show ino4ap4
                                                    p "Good but I should try harder...."
                                                    p "Expansion!!!"
                                                    $ renpy.transition(dissolve)
                                                    hide ino4ap4
                                                    hide ino4dcl
                                                    hide ino4e
                                                    show ino4f
                                                    show ino4dcl                                               
                                                    show ino4ap4
                                                    i "ARghhhhh *pain*"
                                                    p "Yes that looks better... Hmm but she miss something...."                                                
                                                    $ renpy.transition(dissolve)
                                                    show ino4text1
                                                    p "And some more here to not forget..."
                                                    $ renpy.transition(dissolve)
                                                    show ino4text2
                                                    hide ino4dcl
                                                    show ino4dok
                                                    i "......."
                                                    p "Do you want to be fucked now?"
                                                    i "...."
                                                    show ino4sl1 with hpunch
                                                    p "What???? *slash*"
                                                    show ino4sl2 with vpunch
                                                    hide ino4dok
                                                    show ino4dshock
                                                    i "Yes....."
                                                    show ino4sl3 with vpunch
                                                    p "Yes what???"
                                                    show ino4sl4 with vpunch
                                                    i "Yes, Fuck me!"
                                                    p "Ask for it bitch! *slash*" with hpunch
                                                    i "Please fuck me...."
                                                    p "Louder!"
                                                    show ino4slbl with hpunch
                                                    i "Please fuck me *roar scream*...."
                                                    p "....."
                                                    p "It looks like I overdo it a little."
                                                    p "Should I heal her?"
                                                    menu:
                                                        "Later":
                                                            p "Maybe later now she looks good."
                                                        "Now":
                                                            p "Time to use scroll..."
                                                            p "Healing jutsu!"
                                                            $ renpy.transition(dissolve)
                                                            hide ino4sl1
                                                            hide ino4sl2
                                                            hide ino4sl3
                                                            hide ino4sl4
                                                            hide ino4slbl
                                                            p "Nice...."
                                                            p "And remove this..."
                                                            $ renpy.transition(dissolve)
                                                            hide ino4text1
                                                            hide ino4text2
                                                            p "And pull that out..."
                                                            hide ino4ap4
                                                            p "And now...."
                                                else:
                                                    "I need healing scroll for that."
                                                    p "Just have to be careful."
                                                $ renpy.transition(dissolve)    
                                                hide ino4dshock
                                                show ino4dok
                                                jump inoassfuck5555
                                                
                                            "Fuck her ass":
                                                p "Ok...."
                                                $ renpy.transition(dissolve)
                                                hide ino4ap4
                                                show ino4as4
                                                hide ino4dok
                                                show ino4dcl
                                                i "...."
                                                $ renpy.transition(dissolve)
                                                hide ino4as1
                                                show ino4as2
                                                p "Nice warm ass..."
                                                $ renpy.transition(dissolve)
                                                hide ino4as2
                                                show ino4as3
                                                p "Yeah that is good..."
                                                $ renpy.transition(dissolve)
                                                hide ino4as3
                                                show ino4as4
                                                hide ino4dcl
                                                show ino4dclop
                                                i "Ouch..."
                                                $ renpy.transition(dissolve)
                                                hide ino4as4
                                                show ino4as3
                                                p "She like it!"
                                                $ renpy.transition(dissolve)
                                                hide ino4as3
                                                show ino4as2
                                                i "...."
                                                $ renpy.transition(dissolve)
                                                hide ino4as2
                                                show ino4as3
                                                i "Yessss... *moan*"
                                                $ renpy.transition(dissolve)
                                                hide ino4as3
                                                show ino4as4
                                                hide ino4dclop
                                                show ino4dokop
                                                i "Mmmmmm..."
                                                $ renpy.transition(dissolve)
                                                hide ino4as4
                                                show ino4as3
                                                p "Yeah...."
                                                $ renpy.transition(dissolve)
                                                hide ino4as3
                                                show ino4as2
                                                p "Amazing... But...."
                                                menu:
                                                    "Cum in":
                                                        p "Fuck!"
                                                        $ renpy.transition(dissolve)
                                                        hide ino4as2
                                                        show ino4as3
                                                        p "I can't hold it anymore..."
                                                        $ renpy.transition(dissolve)
                                                        hide ino4as3
                                                        show ino4as4
                                                        show ino4asin1
                                                        p "Yeah!!! *slurp*"
                                                        $ renpy.transition(dissolve)
                                                        show ino4asin2
                                                        hide ino4dokop
                                                        show ino4dok
                                                        p "hehe.... *drip*"
                                                        i "......"
                                                        p "That was funny..."
                                        
                                                        
                                                    "Cum out":
                                                        p "Yeah!!!"
                                                        $ renpy.transition(dissolve)
                                                        hide ino4as2
                                                        show ino4as1
                                                        p "Take it Ino! *slurp*"
                                                        $ renpy.transition(dissolve)
                                                        show ino4asout1
                                                        p "More!!! *slurp*"
                                                        $ renpy.transition(dissolve)
                                                        show ino4asout2
                                                        hide ino4dokop
                                                        show ino4dok
                                                        p "Nice look... *drip*"
                                                        i "......"
                                                        p "You enjoy it right?"
                                                        
                                                    "Hold it":
                                                        p "I should hold it...."
                                                        $ renpy.transition(dissolve)
                                                        hide ino4as2
                                                        show ino4as1
                                                        p "And try something else..."
                                                        $ renpy.transition(dissolve)
                                                        hide ino4as1        
                                                        hide ino4dokop
                                                        show ino4dok
                                                        jump inoassfuck5555
                                                
                                            "Kage Bunshin":
                                                p "Time to play!"
                                                p "Just need to prepare everything..."
                                                $ renpy.transition(dissolve)
                                                hide ino4dok
                                                hide ino4d
                                                hide ino4f
                                                hide ino4sl1
                                                hide ino4sl2
                                                hide ino4sl3
                                                hide ino4sl4
                                                hide ino4slbl
                                                hide ino4text1
                                                hide ino4text2
                                                hide ino4ap4
                                                hide ino4as1
                                                hide ino4dok
                                                hide ino4d
                                                hide ino4e
                                                hide ino4f
                                                hide ino4asout1
                                                hide ino4asout2
                                                hide ino4asin1
                                                hide ino4asin2
                                                hide ino4as4
                                                show ino4a
                                                show ino4aok
                                                p "And now.... Expasion!!!"
                                                $ renpy.transition(dissolve)
                                                hide ino4a
                                                hide ino4aok
                                                show ino4b
                                                show ino4aokop
                                                p "Nice... should I make them bigger?"
                                                menu:
                                                    "NO":
                                                        p "Nah... That is good..."
                                                    "YES":
                                                        p "Sure... bigger is better."
                                                        p "Expansion!"
                                                        $ renpy.transition(dissolve)
                                                        hide ino4b
                                                        hide ino4aokop
                                                        show ino4c
                                                        show ino4aokop
                                                        p "Nice... And now...."
                                                $ renpy.transition(dissolve)
                                                show ino4bl1
                                                p "Kage Bunshin no jutsu!"
                                                $ renpy.transition(dissolve)
                                                show ino4as1
                                                show ino4pp1
                                                p "Hehe... Nice...."
                                                p "Should I write something on her body???"
                                                menu:
                                                    "YES":
                                                        p "Hehe..."
                                                        $ renpy.transition(dissolve)                                                        
                                                        hide ino4as1
                                                        hide ino4pp1
                                                        show ino4as1
                                                        show ino4pp1
                                                        show ino4text1
                                                        p "And one as reminder..."
                                                        $ renpy.transition(dissolve)
                                                        hide ino4as1
                                                        hide ino4pp1
                                                        show ino4as1
                                                        show ino4pp1
                                                        show ino4text2
                                                        
                                                        
                                                    "NO":
                                                        p "Ok...."
                                                i "...."
                                                p "Time to fuck!"
                                                $ renpy.transition(dissolve)
                                                hide ino4as1
                                                show ino4as2
                                                hide ino4pp1                                                
                                                show ino4pp2
                                                hide ino4aokop
                                                show ino4aclop
                                                p "Do not forget to open mouth!"
                                                $ renpy.transition(dissolve)
                                                hide ino4bl1
                                                show ino4bl2
                                                hide ino4as2
                                                show ino4as3
                                                i "Mhgmmm..."
                                                $ renpy.transition(dissolve)
                                                hide ino4bl2
                                                show ino4bl3
                                                hide ino4pp2
                                                show ino4pp3
                                                p "Yeah... Stick it in!!!"
                                                $ renpy.transition(dissolve)
                                                hide ino4bl3
                                                show ino4bl4
                                                p "Deeper!!!"
                                                $ renpy.transition(dissolve)
                                                hide ino4aclop
                                                show ino4aokop
                                                hide ino4as3
                                                show ino4as4
                                                hide ino4pp3                                                
                                                show ino4pp4
                                                hide ino4bl4
                                                show ino4bl3
                                                i "mgmmmgmmgmmm... *moan gag*"
                                                $ renpy.transition(dissolve)
                                                hide ino4as4
                                                show ino4as3
                                                hide ino4pp4                                            
                                                show ino4pp3
                                                hide ino4bl3
                                                show ino4bl4
                                                p "Yeah, you can't talk right now!"
                                                $ renpy.transition(dissolve)
                                                hide ino4as3
                                                show ino4as4
                                                hide ino4pp3                                                
                                                show ino4pp2
                                                hide ino4bl4
                                                show ino4bl3
                                                i "gggrgggg *cough*"
                                                $ renpy.transition(dissolve)
                                                hide ino4as4
                                                show ino4as3
                                                hide ino4pp2                                                
                                                show ino4pp1
                                                hide ino4bl3
                                                show ino4bl4
                                                p "YEah! *slurp*"
                                                $ renpy.transition(dissolve)
                                                hide ino4as3
                                                show ino4as2
                                                show ino4pspout1
                                                hide ino4bl4
                                                show ino4bl3
                                                p "More!!!!"
                                                $ renpy.transition(dissolve)
                                                hide ino4aokop
                                                show ino4aclop
                                                hide ino4as2
                                                show ino4as1
                                                show ino4pspout2
                                                hide ino4bl3
                                                show ino4bl4
                                                i "Gmmmmgmgmm!!!"
                                                $ renpy.transition(dissolve)
                                                hide ino4pp1
                                                show ino4pp2
                                                show ino4asout1
                                                hide ino4bl4
                                                show ino4bl3                                                
                                                p "Again!!! *slurp*"
                                                $ renpy.transition(dissolve)
                                                hide ino4pp2
                                                show ino4pp3
                                                show ino4asout2
                                                hide ino4bl3
                                                show ino4bl2
                                                i "Gmmmgmmm... *drip*"
                                                $ renpy.transition(dissolve)
                                                hide ino4pp3
                                                show ino4pp4
                                                hide ino4as1
                                                show ino4as2
                                                hide ino4bl2
                                                show ino4bl3
                                                p "Incoming!!!"
                                                $ renpy.transition(dissolve)
                                                hide ino4pp4
                                                show ino4pp3
                                                hide ino4as2
                                                show ino4as3
                                                hide ino4bl3
                                                show ino4bl4
                                                i "grggg....*Gag*"
                                                $ renpy.transition(dissolve)
                                                hide ino4pp3
                                                show ino4pp4
                                                show ino4pspin1
                                                hide ino4as3
                                                show ino4as4
                                                hide ino4bl3
                                                show ino4bl4
                                                p "Multi sperm jutsu!!!"
                                                $ renpy.transition(dissolve)
                                                show ino4pspin2
                                                hide ino4as4
                                                show ino4as3
                                                hide ino4bl3
                                                show ino4bl4
                                                i "Grgggg... *gag cough*"
                                                $ renpy.transition(dissolve)
                                                hide ino4aclop
                                                show ino4aok
                                                hide ino4as3
                                                show ino4as4
                                                show ino4asin1
                                                hide ino4bl4
                                                show ino4bl3
                                                i "Ggrggggg.....*Slurp gag cough*"
                                                $ renpy.transition(dissolve)
                                                show ino4asin2
                                                hide ino4bl3
                                                show ino4bl4
                                                show ino4blin
                                                p "Wow.... *drip*"
                                                p "Look at you Ino...."
                                                p "You look like cum dump...."
                                                i "Grgggggg....."
                                                p "I'm just really exhausted now."                                                
                                                p "Namigan is already at the limit..."
                                        
                                        i "....*drip*"
                                        with fade
                                        p "ehm....You can clean yourself and dress..."
                                        $ renpy.transition(dissolve)
                                        hide ino4dok
                                        hide ino4aok
                                        hide ino4a
                                        hide ino4b
                                        hide ino4c
                                        hide ino4d
                                        hide ino4f
                                        hide ino4bl4
                                        hide ino4sl1
                                        hide ino4sl2
                                        hide ino4sl3
                                        hide ino4sl4
                                        hide ino4slbl
                                        hide ino4text1
                                        hide ino4text2
                                        hide ino4ap4
                                        hide ino4pp4
                                        hide ino4as1
                                        hide ino4dok
                                        hide ino4d
                                        hide ino4e
                                        hide ino4f
                                        hide ino4blin
                                        hide ino4asin1
                                        hide ino4asin2
                                        hide ino4pspout1
                                        hide ino4pspout2
                                        hide ino4asout1
                                        hide ino4asout2
                                        hide ino4pspin1
                                        hide ino4pspin2
                                        hide ino4as4
                                        p "I really enjoed it!"
                                        $ renpy.transition(dissolve)
                                        show inon1
                                        show inonna
                                        p "But it is time to release it. Did you clean yourself?"
                                        i "... yes......"
                                        p "No sperm in ass???"
                                        i "..... no ......"
                                        p "That is sad..... Bye..."
                                        scene black with circleirisin               
                                        show nharem0 with circleirisout
                                        jump nharem 
                
            else:
                "How you want to talk with her if she is not here?"
                scene black with circleirisin               
                show dharem0 with circleirisout
                jump dharem
    
        "Go back to the map":
            scene black with circleirisin               
            show dharem0 with circleirisout
            jump dharem 
    "This is local spa."
    scene black with circleirisin               
    show dharem0 with circleirisout
    jump dharem 




























################################ dharemhouse1
################################ dharemhouse1
################################ dharemhouse1
################################ dharemhouse1
################################ dharemhouse1
label dharemhouse1:
    if kushinaslave ==0:
            "This house is for sale. It cost 10000 Ryo."
            menu:
                "Buy":
                    if ryo >=10000:
                        $ ryo = ryo - 10000
                        $ kushinaslave = 1
                        "You bought a house. What now?"
                        jump dharemhouse1
                    else:
                        "You need more Ryo for that."
                        scene black with circleirisin               
                        show dharem0 with circleirisout
                        jump dharem 
                    
                "Later":
                    "Maybe later..."
                    scene black with circleirisin               
                    show dharem0 with circleirisout
                    jump dharem 
    else:
        menu:
            
            "Rest":
                "You gained some energy."
                scene black with circleirisin               
                show nharem0 with circleirisout
                jump nharem
                
            "Call Hinata":
                
                if hinatamission >=15:
                    $ renpy.transition(dissolve)
                    show hinab1
                    show hinabok
                    hi "Hi, What do you want to do today?"
                    menu badhinafuck1:
                        "Play with her body":
                            p "Just get naked...  I want to make you feel good..."
                            hi "You little pervert...."
                            $ renpy.transition(dissolve)
                            hide hinab1
                            hide hinabok
                            show hinab2
                            show hinabop
                            hi "So do you want to use som tools or jutsu?"
                            menu:
                                "Use tools":
                                    p "I want to use some tools."
                                    hi "Sure.... here is a whip and some toys!"
                                    hi "Show me what you got!"
                                    "*Whip*" with hpunch
                                    $ renpy.transition(dissolve)
                                    show hinabs1
                                    hide hinabsa
                                    hi "Yesss!!!"
                                    hi "Give me more!"
                                    "*Slash*" with vpunch
                                    $ renpy.transition(dissolve)
                                    show hinabs2
                                    hide hinabok
                                    show hinabop
                                    hi "More power!"
                                    "*Whip*" with hpunch
                                    $ renpy.transition(dissolve)
                                    show hinabs3
                                    hi "Finally!!!"
                                    p "Hmm what if I use this? *stick*"
                                    $ renpy.transition(dissolve)
                                    show hinabc2
                                    hi "Arggg!!! Yesssss...."
                                    $ renpy.transition(dissolve)
                                    show hinabc1
                                    hi "Ouch!!!! *moan*"
                                    hi "Slash me now!!!"
                                    "*Slash*" with vpunch
                                    $ renpy.transition(dissolve)
                                    show hinabs4
                                    hide hinabok
                                    show hinaborg
                                    show hinabm1
                                    hi "Arggg!!!! *squirt*"
                                    p "Fuck you cum again!"
                                    hi "Heh.... again.... *pant*"
                                    $ renpy.transition(dissolve)
                                    hide hinabm1
                                    show hinabm2
                                    hi "It is funny to play a little right? *pant*"
                                    p "I think so."
                                    hi "When you put that vibrator in my pussy I just..."
                                    p "I saw that..."
                                    $ renpy.transition(dissolve)
                                    hide hinaborg
                                    show hinabok
                                    show hinabsh
                                    hi "Time to clean that mess..."
                                    hi "Healing palm!"
                                    $ renpy.transition(dissolve)
                                    hide hinabs1
                                    hide hinabs2
                                    hide hinabs3
                                    hide hinabs4                                
                                    hide hinabm2
                                    hi "And this..."
                                    $ renpy.transition(dissolve)
                                    hide hinabc1
                                    hide hinabc2
                                    hi "Actually, it looks like nothing happened."
                                    p "...."
                                    hi "Next time I can play with your dick a little next time."
                                    p "Next time?"
                                    hi "I am satisfied now... And tired..."   
                                    p "Ok... So next time...."
                                    scene black with circleirisin               
                                    show nharem0 with circleirisout
                                    jump nharem
                                    
                                "Use jutsu":
                                    p "I want to test some jutsu on you..."
                                    hi "Ok... what do you want to test first?"
                                    p "Hmm... Maybe..."
                                    hi "Just start already I am bored."
                                    p "Heat jutsu..."
                                    hi "???"
                                    $ renpy.transition(dissolve)
                                    hide hinabok
                                    show hinabop
                                    show hinabdr1
                                    hi "What is that?"
                                    hi "Did you increase the temperature or what???"
                                    p "heh... Yes something like that..."
                                    $ renpy.transition(dissolve)
                                    hide hinabop
                                    show hinabcla
                                    show hinabdr2                              
                                    hi "Fuck... try something else this is not sexi..."
                                    p "Sure! Water style!"
                                    $ renpy.transition(dissolve)
                                    show hinabw1
                                    hi "Ahhh...What is that?"
                                    p "Water dragoon! *splash*"
                                    $ renpy.transition(dissolve)
                                    show hinabw2
                                    hide hinabcla
                                    show hinabclo
                                    hi "MMM...*moan* much better..."
                                    p "Full power!"
                                    $ renpy.transition(dissolve)
                                    show hinabw3
                                    hi "Yesss.... *moaning*"
                                    hi "Is that everything that you have?"
                                    hi "Use that dildo to make it more funny!"
                                    p "Sure...*stick*"
                                    $ renpy.transition(dissolve)
                                    show hinabc2
                                    hi "Arggg!!! Yesssss...."
                                    $ renpy.transition(dissolve)
                                    show hinabc1
                                    hide hinabclo
                                    show hinabop
                                    hi "Yesss... *scream*"
                                    hi "What now? *moan*"
                                    p "Lightning style!*zap*"
                                    $ renpy.transition(dissolve)
                                    show hinabl1
                                    hi "That tickle me!"
                                    p "Lightning release! *zap*"
                                    $ renpy.transition(dissolve)
                                    show hinabl2
                                    show hinabl3
                                    hide hinabop
                                    show hinaborg
                                    show hinabm1
                                    hi "Aaaaaaa... *squirt*"
                                    p "Fuck...."
                                    hi "Grrrrr.... *pant*"     
                                    p "I can't hold it anymore..."
                                    $ renpy.transition(dissolve)
                                    hide hinabl2
                                    hide hinabl3
                                    hi "What a nice using of elemental chakra."
                                    $ renpy.transition(dissolve)
                                    hide hinabm1
                                    show hinabm2
                                    p "I need to focus on it hard. To not hurt you."
                                    hi "heh...."
                                    $ renpy.transition(dissolve)
                                    hide hinabl1
                                    p "....."
                                    $ renpy.transition(dissolve)
                                    hide hinaborg
                                    show hinabok
                                    show hinabsh
                                    hi "Time to clean that mess..."
                                    hi "Just need a towel for that."
                                    $ renpy.transition(dissolve)
                                    hide hinabw1
                                    hide hinabw2
                                    hide hinabw3
                                    hide hinabdr1                               
                                    hide hinabdr2
                                    hide hinabm2
                                    hi "And take out this...*plumb*"
                                    $ renpy.transition(dissolve)
                                    hide hinabc1
                                    hide hinabc2
                                    hi "Ahhh.*moan stretch* I'm feeling so relaxed right now"
                                    p "Actually, I used too much chakra...."
                                    p "I need to rest now... See you later..."
                                    hi "Sure bye."   
                                    scene black with circleirisin               
                                    show nharem0 with circleirisout
                                    jump nharem
                                
                            
                        "Play with her boobs":
                                p "I want to play with your boobs."
                                hi "This one again? Ok....."
                                $ renpy.transition(dissolve)
                                hide hinabok
                                hide hinab2
                                hide hinab1
                                show hina7a
                                show hina7ok
                                hi "Hurry up..."
                                menu:
                                    "Milk her":
                                            hi "So what do you want to do?"
                                            p "I bring something special today."
                                            hi "You know that it is not special when you do it too often right?"
                                            p "Come on...."
                                            hi "Just dont try to be original..."
                                            p "I will put it right here..."
                                            hi "Finally..."
                                            "*Suck*"
                                            $ renpy.transition(dissolve)
                                            hide hina7ok
                                            show hina7clop
                                            show hina7m1
                                            hi "Yeah... Feel good.."
                                            p "Good to hear that..."
                                            hi "You can turn it on..."
                                            p "Sure..."
                                            "*swap*"
                                            hi "Yess.*pain moan*"
                                            $ renpy.transition(dissolve)
                                            hide hina7clop
                                            show hina7cl
                                            hi "It's sucking my boobs!"
                                            p "..."
                                            hi "Increase power!!!... *moan*"
                                            p "Sure..."
                                            $ renpy.transition(dissolve)
                                            hide hina7cl
                                            show hina7clop
                                            show hina7m2
                                            hi "Arggg... * moan*"
                                            hi "Amazing! *heavy moaning*"
                                            $ renpy.transition(dissolve)
                                            hide hina7clop
                                            show hina7org
                                            hi "Yesss.... *moan*"
                                            $ renpy.transition(dissolve)
                                            show hina7m3
                                            p "Fuck... It is leaking out again."
                                            p "....."
                                            $ renpy.transition(dissolve)
                                            hide hina7m2
                                            p "Looks like this was everything..."
                                            hi "Fuck it!!!*sigh*"
                                            p "So no more milk today?"
                                            hi "I think I reach my limit."
                                            p "..."
                                            hi "We can continue tomorrow now I am sucked out..."
                                            $ renpy.transition(dissolve)
                                            hide hina7org
                                            show hina7hap
                                            hi "It was not bad..."
                                            p "Yes, I know you already said it."
                                            p "So see you soon..."
                                            $ renpy.transition(dissolve)
                                            hide hina7hap
                                            show hina7ok
                                            hi "Wait, you will leave me like this?"
                                            p "Sure... Why not...."
                                            scene black with circleirisin               
                                            show nharem0 with circleirisout
                                            jump nharem
                                            
                                    
                                    "Touch her boobs":
                                        hi "So what do you want to do?"
                                        $ renpy.transition(dissolve)
                                        hide hina7a
                                        hide hina7ok
                                        show hina7b
                                        show hina7cl
                                        p "Your boobs are really soft..."
                                        p "This will be more and more fun."
                                        $ renpy.transition(dissolve)
                                        hide hina7cl
                                        show hina7ang
                                        hi "Do not press them that hard!"
                                        p "Why not? *squeez*"
                                        hi "Ahhhh... *moan*"
                                        p "Hehe... *squeeze*"
                                        $ renpy.transition(dissolve)
                                        hide hina7ang
                                        show hina7cl
                                        hi "Arghhh... *moan* fuck...."
                                        $ renpy.transition(dissolve)
                                        hide hina7b
                                        hide hina7cl
                                        show hina7a
                                        show hina7ok
                                        hi "Why you stop asshole?"
                                        p "Because you said you didn't like it."
                                        hi "Just grab them asshole!"
                                        "*squeez*"
                                        $ renpy.transition(dissolve)
                                        hide hina7a
                                        hide hina7ok
                                        show hina7b
                                        show hina7cl
                                        hi "Yesss..*heavy moaning*"
                                        p "Take it! *hard squeeze.*"
                                        $ renpy.transition(dissolve)
                                        hide hina7cl
                                        show hina7org
                                        hi "Aaaaaa...*moan squirt*"
                                        $ renpy.transition(dissolve)
                                        show hina7m4
                                        hi "Yessss...*heavy moaning*"
                                        p "heh..."
                                        hi "That was good..."
                                        p "What???"
                                        hi "Nothing..*angry*"
                                        hi "Just release my boob!"
                                        "You released her boobs."
                                        $ renpy.transition(dissolve)
                                        hide hina7m4
                                        hide hina7org
                                        hide hina7a
                                        hide hina7b
                                        p "...."
                                        $ renpy.transition(dissolve)
                                        show hinab2
                                        show hinabbya
                                        hi "This was..."
                                        p "Just say it!"
                                        hi "It was not bad."
                                        p "I know it from your gesture."                        
                                        hi "We can continue later."
                                        p "Maybe..."
                                        hi "..."
                                        hi "Asshole..."
                                        p "What???"
                                        hi "*sigh*"
                                        scene black with circleirisin               
                                        show nharem0 with circleirisout
                                        jump nharem
                                    "Make them bigger":
                                        hi "So what do you want to do?"
                                        p "Release your power, make your boobs bigger."
                                        hi "Sure..."
                                        $ renpy.transition(dissolve)
                                        hide hina7a
                                        hide hina7ok
                                        show hina7c
                                        show hina7cl
                                        p "Yes, this is good now shown me your tongue."
                                        $ renpy.transition(dissolve)
                                        hide hina7cl
                                        show hina7ang
                                        hi "What?"
                                        p "Just do it!"
                                        $ renpy.transition(dissolve)
                                        hide hina7ang
                                        show hina7org
                                        hi "Like this?"
                                        p "Yes now I can... *clamp*"
                                        $ renpy.transition(dissolve)
                                        show hina7cl2
                                        hi "Ghhggg??? *mumble*"
                                        p "Don't worry, I have more of them."
                                        $ renpy.transition(dissolve)
                                        show hina7cl1
                                        hi "Argifhtk??? *mumble*"
                                        p "Yes I know what you want..."
                                        p "Lightning stye! Tingling! *zap*"
                                        $ renpy.transition(dissolve)
                                        show hina7l1
                                        hi "gzzgg....*mumble*"
                                        p "You want more? Ok."
                                        p "Lightning stye! nipple release! *zap*"
                                        $ renpy.transition(dissolve)
                                        show hina7l2
                                        hi "gzzggg.g......*snore*"
                                        p "More power!"
                                        $ renpy.transition(dissolve)
                                        show hina7l3
                                        hi "sssss..*heavy moaning*"
                                        p "hehe......"
                                        hi "ssssAassssaazzhgaa...*moan*"
                                        p "That was enough...."
                                        $ renpy.transition(dissolve)
                                        hide hina7l3
                                        hide hina7l2
                                        p "Looks like it worked...."
                                        hi "gzggg....*mumble*"
                                        p "Sorry I forget..."
                                        $ renpy.transition(dissolve)
                                        hide hina7l1
                                        hide hina7cl2
                                        hide hina7org
                                        show hina7hap
                                        hi "That was FUNNY!!!"
                                        p "Yes I know."
                                        hi "Maybe if you release more lightning chakra!"
                                        p "...."
                                        hi "I really like when you play with my nipples.... And that combination has been just amazing!"
                                        p "Thanks..."
                                        hi "But I need to take them out for now.."
                                        p "Sure..."
                                        $ renpy.transition(dissolve)
                                        hide hina7l3
                                        hide hina7cl2  
                                        hide hina7c
                                        hide hina7hap
                                        hide hina7cl1
                                        hide hina7b
                                        p "...."
                                        $ renpy.transition(dissolve)
                                        show hinab2
                                        show hinabok
                                        hi "It was so much fun for me..."
                                        p "..."
                                        hi "Thanks for a wonderful evening."
                                        p "It was nothing... But I need to rest now.."
                                        hi "Yes, I understant...*sigh*"
                                        p "See you later..."
                                        scene black with circleirisin               
                                        show nharem0 with circleirisout
                                        jump nharem
                                
                        "Fuck her pussy":
                                p "It is a time to play with your pussy for a while."
                                hi "You mean?"
                                p "Yes.... Get into the position..."
                                $ renpy.transition(dissolve)
                                hide hinabok
                                hide hinab2
                                hide hinab1
                                show hina4a
                                show hina4op
                                hi "I am ready. What now?"
                                p "I will..."
                                menu:
                                    "Just fuck her":
                                        p "Fuck your pussy till you pass out..."
                                        $ renpy.transition(dissolve)
                                        show hina4p1
                                        hi "That is a challenge."
                                        hi "Show me what you got!"
                                        $ renpy.transition(dissolve)
                                        hide hina4p1
                                        show hina4p2
                                        hide hina4op
                                        show hina4ok
                                        hi "Nice... *moan*"
                                        $ renpy.transition(dissolve)
                                        hide hina4p2
                                        show hina4p3
                                        p "I am really glad you like it."
                                        $ renpy.transition(dissolve)
                                        hide hina4a
                                        show hina4b
                                        hide hina4ok
                                        show hina4ok
                                        hide hina4p3
                                        show hina4p4
                                        hi "Give me more! *moan*"
                                        $ renpy.transition(dissolve)
                                        hide hina4p4
                                        show hina4p3
                                        p "Sure..."
                                        $ renpy.transition(dissolve)
                                        hide hina4b
                                        show hina4a
                                        hide hina4ok
                                        show hina4cl
                                        hide hina4p4
                                        show hina4p3
                                        hi "Yeah! *scream*"
                                        $ renpy.transition(dissolve)
                                        hide hina4p4
                                        show hina4p3
                                        p "...."
                                        $ renpy.transition(dissolve)
                                        hide hina4p3
                                        show hina4p2
                                        p "Just...."
                                        $ renpy.transition(dissolve)
                                        hide hina4p2
                                        show hina4p3
                                        p "Wow..."
                                        $ renpy.transition(dissolve)
                                        hide hina4a
                                        show hina4b
                                        hide hina4cl
                                        show hina4cl
                                        hide hina4p3
                                        show hina4p4
                                        hi "Fuck yeah!*moan*"
                                        $ renpy.transition(dissolve)
                                        hide hina4p4
                                        show hina4p3
                                        hi "Argg..*moan*"
                                        $ renpy.transition(dissolve)
                                        hide hina4p3
                                        show hina4p2
                                        hide hina4cl
                                        show hina4ok
                                        hi "This is so good."
                                        $ renpy.transition(dissolve)
                                        hide hina4p2
                                        show hina4p3
                                        hi "I want more! *scream*"
                                        $ renpy.transition(dissolve)
                                        hide hina4b
                                        show hina4a
                                        show hina4clips
                                        hide hina4ok
                                        show hina4org
                                        hide hina4p3
                                        show hina4p4
                                        hi "Yesss!!!*scream moan*"
                                        $ renpy.transition(dissolve)
                                        show hina4milk
                                        hide hina4p4
                                        show hina4p3
                                        p "FucK!!! *splurt*"
                                        $ renpy.transition(dissolve)
                                        hide hina4p3
                                        show hina4p4
                                        show hina4spi1
                                        p "That is... *splurt*"
                                        $ renpy.transition(dissolve)
                                        show hina4spi2
                                        hi "Yesss...*moan drip*"
                                        hi "You cum in my pussy again.... *sigh*"
                                        p "Yeah... Sorry I really try but...."
                                        $ renpy.transition(dissolve)
                                        hide hina4org
                                        show hina4ok
                                        hi "Ok... I start to like it..."
                                        p "...."
                                        hi "But give me some time now I need a rest."
                                        p "Sure. Anything you want."
                                        p "Bye..."
                                        scene black with circleirisin               
                                        show nharem0 with circleirisout
                                        jump nharem
                                        
                                    "Use clone":
                                        p "Fuck you as hard as I can."
                                        $ renpy.transition(dissolve)
                                        show hina4p1
                                        hi "What do you mean by that?"
                                        $ renpy.transition(dissolve)
                                        hide hina4p1
                                        show hina4p2
                                        hide hina4op
                                        show hina4ok
                                        hi "Arg.... *moan*"
                                        $ renpy.transition(dissolve)
                                        hide hina4p2
                                        show hina4p3
                                        p "I will show you!"
                                        $ renpy.transition(dissolve)
                                        hide hina4p3
                                        show hina4p4
                                        p "Kage bunshin no jutsu!"
                                        $ renpy.transition(dissolve)
                                        hide hina4p4
                                        show hina4p3
                                        show hina4bl1
                                        hi "Hey!  What is that?"
                                        p "Just shut up!"
                                        $ renpy.transition(dissolve)
                                        hide hina4p3
                                        show hina4p2
                                        hide hina4bl1
                                        show hina4bl2
                                        hide hina4ok
                                        show hina4ga
                                        p "That feels good..."
                                        $ renpy.transition(dissolve)
                                        hide hina4p2
                                        show hina4p3
                                        hide hina4bl2
                                        show hina4bl3
                                        hi "Mgmmmm... *gag*"
                                        $ renpy.transition(dissolve)
                                        hide hina4p3
                                        show hina4p4
                                        hide hina4bl3
                                        show hina4bl4
                                        hi "*gag cough*"
                                        $ renpy.transition(dissolve)
                                        hide hina4p4
                                        show hina4p3
                                        p "It is good right?"
                                        $ renpy.transition(dissolve)
                                        hide hina4p3
                                        show hina4p2
                                        hide hina4ga
                                        show hina4gag
                                        hi "Mgmgmgmmm... *gag cough*"
                                        $ renpy.transition(dissolve)
                                        hide hina4bl4
                                        show hina4bl3
                                        p "Fuck it is so good!"
                                        $ renpy.transition(dissolve)
                                        hide hina4bl3
                                        show hina4bl2
                                        hide hina4p2
                                        show hina4p1
                                        p "Take it! *splurt*"
                                        $ renpy.transition(dissolve)
                                        hide hina4bl2
                                        show hina4bl3
                                        show hina4spo1
                                        hi "Mgmmm...*moan gag*"
                                        $ renpy.transition(dissolve)
                                        show hina4spo2
                                        hide hina4bl3
                                        show hina4bl4
                                        show hina4bl5
                                        p "More!*splurt*"
                                        $ renpy.transition(dissolve)
                                        show hina4bl6
                                        hi "gmmmgmm...*cough*"
                                        p "That was funny..."
                                        hi "..."
                                        p "Hinata???"
                                        hi "..."
                                        p "Fuck!"
                                        $ renpy.transition(dissolve)
                                        hide hina4bl6
                                        hide hina4bl5
                                        hide hina4bl4
                                        hide hina4spo2
                                        hide hina4spo1
                                        hide hina4gag
                                        hide hina4p1
                                        hide hina4a
                                        p "Hey Hinata wake up!"
                                        hi ".... *mumble*"
                                        p "Yes, she is fine... just passed out..."
                                        hi "*mumble*"
                                        p "Just need some rest... I will check her tomorrow if she is fine..."
                                        p "I just bring her to the bed and go out..."
                                        scene black with circleirisin               
                                        show nharem0 with circleirisout
                                        jump nharem
                            
                            
                        "Fuck her ass":
                                p "I want to fuck your ass tonight."
                                hi "I understant...."
                                $ renpy.transition(dissolve)
                                hide hinabok
                                hide hinab2
                                hide hinab1
                                show hina3a
                                show hina3ok
                                hi "I am ready. Come on..."
                                p "Sure."
                                $ renpy.transition(dissolve)
                                show hina3p1
                                hi "Just stick it in!"
                                $ renpy.transition(dissolve)
                                hide hina3p1
                                show hina3p2
                                hide hina3ok
                                show hina3op
                                hi "....."
                                $ renpy.transition(dissolve)
                                hide hina3p2
                                show hina3p3
                                p "Feels good right?"
                                $ renpy.transition(dissolve)
                                hide hina3p3
                                show hina3p2
                                hi "Yes. Put it deeper."
                                $ renpy.transition(dissolve)
                                hide hina3p2
                                show hina3p3
                                hi "*silent moan*"
                                $ renpy.transition(dissolve)
                                hide hina3p3
                                show hina3p4
                                hi "Just...*moan* right that..."
                                $ renpy.transition(dissolve)
                                hide hina3p4
                                show hina3p3
                                p "Your ass is so tight..."
                                $ renpy.transition(dissolve)
                                hide hina3p3
                                show hina3p4
                                hi "Just... *moan* "
                                $ renpy.transition(dissolve)
                                hide hina3a
                                show hina3b
                                hide hina3op
                                show hina3ok
                                hide hina3p4
                                show hina3p3
                                p "Nice..."
                                $ renpy.transition(dissolve)
                                hide hina3p3
                                show hina3p2
                                p "..."
                                $ renpy.transition(dissolve)
                                hide hina3p2
                                show hina3p3
                                hi "Yesss....*moan*"
                                $ renpy.transition(dissolve)
                                hide hina3b
                                show hina3a
                                hide hina3ok
                                show hina3ok
                                hide hina3p3
                                show hina3p4
                                p "That ass... I want to make it wet."
                                $ renpy.transition(dissolve)
                                hide hina3p4
                                show hina3p3
                                hi "You like it *moan* right?"
                                p "Yes... Water style!"
                                $ renpy.transition(dissolve)
                                hide hina3p3
                                show hina3p2
                                show hina3w1
                                hi "Mmmmm... *moan*"
                                $ renpy.transition(dissolve)
                                hide hina3p2
                                show hina3p3
                                show hina3w2
                                p "More!"
                                $ renpy.transition(dissolve)
                                hide hina3p3
                                show hina3p2
                                show hina3w3
                                p "Now... Do that thing again..."
                                $ renpy.transition(dissolve)
                                hide hina3p2
                                show hina3p3
                                hi "You mean? *moan*"
                                $ renpy.transition(dissolve)
                                hide hina3p3
                                show hina3p4
                                p "Yes, Show me byakugan!"
                                $ renpy.transition(dissolve)
                                hide hina3p4
                                show hina3p3
                                hide hina3ok
                                show hina3bya
                                hi "Byakugan!"
                                $ renpy.transition(dissolve)
                                hide hina3p3
                                show hina3p4
                                p "Fuck That eyes!!!"
                                $ renpy.transition(dissolve)
                                hide hina3p4
                                show hina3p3
                                p "I will..."
                                menu:
                                    "Cum in":
                                        p "Yeah!!!*splurt*"
                                        $ renpy.transition(dissolve)
                                        hide hina3p3
                                        show hina3p4
                                        show hina3spi1
                                        hi "Mmmmm..."
                                        $ renpy.transition(dissolve)
                                        show hina3spi2
                                        hide hina3bya
                                        show hina3hap
                                        hi "You are so weird. *drip*"
                                        p "Come on that eyes..."
                                        hi "... *smile*"
                                        p "It is just too hot."
                                        hi "I know."
                                        p "hehe..."
                                        hi "I think I need to go shower now."
                                        p "It looks like you need one."
                                        hi "Asshole..."
                                        p "What is with you asshole?"
                                        hi "You may go to your room now..."
                                        p "Sure..."
                                        scene black with circleirisin               
                                        show nharem0 with circleirisout
                                        jump nharem
                                        
                                    "Cum out":
                                        p "I will..."
                                        $ renpy.transition(dissolve)
                                        hide hina3p3
                                        show hina3p2
                                        p "Yeah!!!*splurt*"
                                        $ renpy.transition(dissolve)
                                        hide hina3p2
                                        show hina3p1
                                        show hina3spo1
                                        hi "Mmmmm..."
                                        $ renpy.transition(dissolve)
                                        show hina3spo2
                                        hide hina3bya
                                        show hina3hap
                                        hi "Look at my body! *drip*"
                                        p "I am actually doing it right now."
                                        hi "I am so sticky! *smile*"
                                        p "Sorry for that."
                                        hi "I am not sure what is worse, to have it in the ass or on my skin."
                                        p "..."
                                        hi "I think I need to go shower now."
                                        p "That is true... You look ehm... dirty..."
                                        hi "Because I am dirty...."
                                        p "I see that..."
                                        hi "Just leave me please."
                                        p "Sure... Bye..."
                                        scene black with circleirisin               
                                        show nharem0 with circleirisout
                                        jump nharem
                                        
                                
                                
                        "Something else":
                                        p "I want to have fun with you tonight."
                                        hi "Sure. What do you want to do?"
                                        p "I was thinking you can choose what we do tonight."
                                        hi "Hmm... So I will pick the possition..."
                                        $ renpy.transition(dissolve)
                                        hide hinabok
                                        hide hinab2
                                        hide hinab1
                                        show hina1
                                        show hina1ok
                                        hi "Do you want me or not?"
                                        p "Of course I want you!"
                                        hi "So what do you wait for?"
                                        p "Let's play for a while... *stick*"
                                        $ renpy.transition(dissolve)
                                        show hina1d1
                                        hi "nice....Turn it on!"
                                        $ renpy.transition(dissolve)
                                        hide hina1d1
                                        show hina1d2
                                        hi "Fuck * moan* this is good."
                                        hi "But I want to feel real dick! Stick it in!"
                                        $ renpy.transition(dissolve)
                                        show hina1p1
                                        p "Allright...."
                                        $ renpy.transition(dissolve)
                                        hide hina1p1
                                        show hina1p2
                                        hide hina1ok
                                        show hina1cl
                                        hi "Yes...*moan* that feels good."
                                        $ renpy.transition(dissolve)
                                        hide hina1p2
                                        show hina1p3
                                        hi "Deeper!"
                                        $ renpy.transition(dissolve)
                                        hide hina1p3
                                        show hina1p4
                                        p "Fuck..."
                                        $ renpy.transition(dissolve)
                                        hide hina1p4
                                        show hina1p3
                                        hi "Mmmmm...*moan*"
                                        $ renpy.transition(dissolve)
                                        hide hina1p3
                                        show hina1p2
                                        hide hina1cl
                                        show hina1sad
                                        hi "Stick it deeper agian!"
                                        $ renpy.transition(dissolve)
                                        hide hina1p2
                                        show hina1p3
                                        p "Sure..."
                                        $ renpy.transition(dissolve)
                                        hide hina1p3
                                        show hina1p4
                                        hi "And fuck my boobs!"
                                        $ renpy.transition(dissolve)
                                        hide hina1p4
                                        show hina1p3
                                        p "???"
                                        $ renpy.transition(dissolve)
                                        hide hina1p3
                                        show hina1p2
                                        hi "Use Kage Bunshin it will be more fun!"
                                        $ renpy.transition(dissolve)
                                        hide hina1p2
                                        show hina1p3
                                        p "Ok...."
                                        $ renpy.transition(dissolve)
                                        hide hina1p3
                                        show hina1p4
                                        p "Kage Bunshin no jutsu!"
                                        $ renpy.transition(dissolve)
                                        hide hina1p4
                                        show hina1p3
                                        hide hina1sad
                                        show hina1clop
                                        show hina1tf1
                                        hi "Mmmmm....*moan*"
                                        $ renpy.transition(dissolve)
                                        hide hina1p3
                                        show hina1p2
                                        hide hina1tf1
                                        show hina1tf2
                                        hi "YYEah!!!*moan*"
                                        $ renpy.transition(dissolve)
                                        hide hina1p2
                                        show hina1p3
                                        hide hina1tf2
                                        show hina1tf3
                                        p "That ASS!!! *slap*" 
                                        $ renpy.transition(dissolve)
                                        hide hina1p3
                                        show hina1p4
                                        hide hina1tf3
                                        show hina1tf4
                                        show hina1h1
                                        hi "Aaaaa...*heavy moaning*"
                                        p "Fuck yeah! *slap*"
                                        $ renpy.transition(dissolve)
                                        hide hina1p4
                                        show hina1p3
                                        hide hina1tf4
                                        show hina1tf3
                                        show hina1h2
                                        hi "More!!!!*scream*"
                                        $ renpy.transition(dissolve)
                                        hide hina1p3
                                        show hina1p4
                                        hide hina1tf3
                                        show hina1tf4
                                        p "Sure! *slap*"
                                        show hina1h3 with hpunch
                                        hide hina1clop
                                        show hina1org
                                        hi "Argggg!!!!*moaning *"
                                        $ renpy.transition(dissolve)
                                        hide hina1p4
                                        show hina1p3
                                        hide hina1tf4
                                        show hina1tf3
                                        hi "Cum on my boobs!!*moan scream*"
                                        p "..."
                                        menu:
                                            "Cum in":
                                                p "Fuck!!!!*splurt*"
                                                $ renpy.transition(dissolve)
                                                hide hina1p3
                                                show hina1p4
                                                hide hina1tf3
                                                show hina1tf4
                                                show hina1spi1
                                                p "Yeah!!!*splurt*"
                                                $ renpy.transition(dissolve)
                                                show hina1spi2
                                                show hina1ts1
                                                hi "Aaaaa...*moan drip*"
                                                $ renpy.transition(dissolve)
                                                show hina1ts2
                                                hi "This is so good....*drip*"
                                                p "Yeah... Your boobs is...."
                                                hi "Just shut up I want to enjoy your sperm in me."
                                                p "Ehm... Sure..."
                                                scene black with circleirisin               
                                                show nharem0 with circleirisout
                                                jump nharem
                                                
                                            "Cum out":
                                                p "I will...."
                                                $ renpy.transition(dissolve)
                                                hide hina1p3
                                                show hina1p2
                                                hide hina1tf3
                                                show hina1tf4
                                                p "Fuck!!!!*splurt*"
                                                $ renpy.transition(dissolve)
                                                hide hina1p2
                                                show hina1p1
                                                show hina1spo1
                                                p "Yeah!!!*splurt*"
                                                $ renpy.transition(dissolve)
                                                show hina1spo2
                                                show hina1ts1
                                                hi "Aaaaa...*moan drip*"
                                                $ renpy.transition(dissolve)
                                                show hina1ts2
                                                hi "This is so good....*drip*"
                                                p "Yeah... Your boobs is...."
                                                hi "You cum so much on my body."
                                                hi "mmmmmm...."
                                                scene black with circleirisin     
                                                "Hinata fall asleep, you decide to not wake her up."
                                                show nharem0 with circleirisout
                                                jump nharem
                                                
                    
                    
                
                else:
                    "She is not here."
                    jump dharemhouse1
                    
                
            "Call Himawari":
                "..."
                if hinami <=10:
                    "Himawari is not a part of your harem for now."
                    jump dharemhouse1
                else:
                    $ renpy.transition(dissolve)
                    show himad
                    show hibln
                    show hishy
                    "Time to have som fun."
                    menu himold1:
                        "Undress":
                            p "You can take off your clothes now."
                            h "..."
                            $ renpy.transition(dissolve)
                            hide hishy
                            hide hibln
                            hide himad
                            hide himaak
                            show himan
                            show hibln
                            show hishy
                            p "That is nice."
                            p "We train really hard last time."
                            p "Now is time to have some fun."
                            menu:
                                "Naked training":
                                    p "I need your help today."
                                    p "This is a good time for training do you agree?"
                                    hide hishy
                                    h "Yes you need to get stronger."
                                    p "Sure can we start?"
                                    h "Yes I am ready."
                                    p "Do you want to put your clothes on?"
                                    h "No this is fine."
                                    p "Yes I see that."
                                    hide hibln
                                    show hiblop
                                    h "We can start if you want."
                                    p "Ok be ready."
                                    with fade
                                    "It was one of the most interesting training."
                                    hide hiblop
                                    show hibln
                                    "She really give everything to that training."
                                    show hidrops
                                    "In fact yours abilities are stronger now."
                                    $ taijutsu = taijutsu + 1
                                    $ genjutsu = genjutsu + 1
                                    $ ninjutsu = ninjutsu + 1
                                    "But your influence on her is same as before training."
                                    "Himawari look tired too..."
                                    scene black with circleirisin               
                                    show nharem0 with circleirisout
                                    jump nharem
                                    
                                "Use chakra clips":
                                    p "Ok it is a good time to train your endurance."
                                    hide hishy
                                    p "Do you know what it mean?"
                                    $ renpy.transition(dissolve)
                                    hide hibln
                                    hide himan
                                    show himanup
                                    show hiclhappy
                                    p "Good girl."
                                    p "Look like you really start to like it."
                                    p "So... Should I use that clips?"
                                    hide hiclhappy
                                    show hiclopen
                                    h "Yes please...."
                                    p "When you ask so nicely."
                                    hide hiclopen
                                    show hiclips
                                    show hiclorg
                                    h "Yesss..." with hpunch
                                    p "That is the reaction I like."
                                    p "Maybe I should press a little."
                                    hide hiclorg
                                    show hiblorg
                                    h "Aaaaaa..." with hpunch
                                    p "Heh maybe I repeat that some times..."
                                    with fade
                                    h "!!!" with hpunch
                                    with fade
                                    h "aaaaa..."
                                    $ renpy.transition(dissolve)
                                    show himilk
                                    hide hiblorg
                                    show hiclorg
                                    h "Awesomeee..."
                                    p "Huh?"
                                    p "Look like you enjoy it more than I think."
                                    "That is a demonstartion of how you can milk a woman with a medium size boobs."
                                    p "Sure I enjoy it too."
                                    p "First take off that clips."
                                    $ renpy.transition(dissolve)
                                    hide himilk
                                    hide hiclips
                                    p "Good now I need some rest... See you later."
                                    scene black with circleirisin               
                                    show nharem0 with circleirisout
                                    jump nharem

                                "Whip training":
                                        p "Ok so maybe this will be booring."
                                        hide hishy
                                        p "It is time to test your body endurance and recovery."
                                        hide hibln
                                        show hiblop
                                        h "I have a large ammout of chakra my recovery is extremly fast."
                                        p "I need to see it to belive it."
                                        hide hiblop
                                        show hibln
                                        h "How you want to test it?"
                                        p "I have that special whip."
                                        p "Just stay still."
                                        h "Sure but tell me.."
                                        show hiang
                                        "Whip, whip, whip...." with hpunch
                                        show hiscars
                                        h "Auuuu..." with hpunch
                                        hide hibln
                                        show hiclopen
                                        p "Huh maybe I slash her more than I had."
                                        hide hiang
                                        with fade
                                        h "...."
                                        $ renpy.transition(dissolve)
                                        hide hiclopen
                                        show hiblsad
                                        hide hiscars
                                        p "Huh?"
                                        h "I told you my body can heal really fast."
                                        p "Maybe you inherited that ability."
                                        p "Hmmm..."
                                        p "Nevermind let's try it again."
                                        "Whip, whip, whip...." with hpunch
                                        show hiscars
                                        hide hiblsad
                                        show hiclorg
                                        h "Noooooo...." with hpunch
                                        p "Wait for it."
                                        with fade                                        
                                        hide hiscars
                                        p "that is really impressive healing ability."
                                        p "Let's try it a few more times."
                                        with fade
                                        "..."
                                        with fade
                                        $ renpy.transition(dissolve)
                                        show hiscars
                                        "That was fun. But there is also a possibility to fuck her. Try it next time ok?"
                                        scene black with circleirisin               
                                        show nharem0 with circleirisout
                                        jump nharem
                                
                        "Play with her":
                            p "Time to play with you a little."          
                            p "Take that cloak off and lay down."                            
                            $ renpy.transition(dissolve)
                            hide hishy
                            hide hibln
                            hide himad
                            hide himaak
                            show h1bodyn1
                            show h1clhappy
                            p "Look like you will never understant that."
                            p "Put your underwear off."
                            $ renpy.transition(dissolve)
                            hide h1bodyn1
                            hide h1clhappy
                            show h1bodyn2
                            show h1normal
                            p "Good girl. Hmm..."
                            p "Actually I like when you hold your boob."
                            p "Anyway...What now?"
                            menu:
                                "Touch her everywhere":
                                    p "Look like you need some tenderness."
                                    $ renpy.transition(dissolve)
                                    show h1bg
                                    hide h1normal
                                    show h1clhappy
                                    p "Do you like it?"
                                    h "Yes it is very nice."
                                    p "And what if I touch you there?"
                                    $ renpy.transition(dissolve)
                                    show h1tp
                                    h "...."
                                    p "Maybe if I rub you a little."
                                    h "Mmmmm" with hpunch
                                    p "And stick it in."
                                    $ renpy.transition(dissolve)
                                    hide h1tp
                                    hide h1bg
                                    show h1tp1
                                    hide h1clhappy
                                    show h1clop
                                    h "Yessss..."
                                    p "...."
                                    $ renpy.transition(dissolve)
                                    hide h1tp1
                                    show h1tp
                                    p "And one more time."
                                    $ renpy.transition(dissolve)
                                    hide h1tp
                                    show h1bg
                                    show h1tp1
                                    hide h1clop
                                    show h1org
                                    h "......"
                                    p "Look like you like it."
                                    p "But I know another place you will like."
                                    $ renpy.transition(dissolve)
                                    hide h1tp1
                                    show h1ta1
                                    hide h1org
                                    show h1scared
                                    h "!!!!" 
                                    p "Hehe."
                                    $ renpy.transition(dissolve)
                                    hide h1ta1
                                    show h1tp1
                                    hide h1scared
                                    show h1open
                                    p "You need to get use to change."
                                    $ renpy.transition(dissolve)
                                    hide h1tp1
                                    show h1ta1
                                    hide h1open
                                    show h1ouch
                                    h "Aaaaaa...."
                                    p "Huh?"
                                    h "Yessss..." with hpunch
                                    p "Ok...."
                                    $ renpy.transition(dissolve)
                                    hide h1ta1
                                    show h1ta
                                    hide h1bg
                                    p "..."
                                    h "That was amazing"
                                    p "You really enjoy it."
                                    h "..."
                                    p "Ok, I will rest now... You should lick my cock during whole night."
                                    h "Sure..."
                                    scene black with circleirisin               
                                    show nharem0 with circleirisout
                                    jump nharem
                                "Pain Train":
                                    p "This is a goot time to try pain train."
                                    p "We already do it so you can do it."
                                    h "Yes I am ready"
                                    p "First I need to attach that clips."
                                    $ renpy.transition(dissolve)
                                    show h1clips
                                    h "...."
                                    p "Nice... You are brave."
                                    p "I will test a whip on you now."
                                    "Slash!" with hpunch
                                    hide h1normal
                                    show h1open
                                    h "Mmmmm..."
                                    show h1slash1
                                    "Slash!" with hpunch
                                    hide h1open
                                    show h1clop
                                    h "!!!!"
                                    p "Yes more!"
                                    show h1slash2
                                    "Whip!" with hpunch
                                    hide h1clop
                                    show h1org
                                    h "Au...."
                                    p "Heh look like you can endure it."
                                    $ renpy.transition(dissolve)
                                    hide h1slash1
                                    p "And your body will heal really fast."
                                    $ renpy.transition(dissolve)
                                    hide h1slash2
                                    p "I need to test your nipple sensitivity now."
                                    p "Lightning style!" with hpunch
                                    $ renpy.transition(dissolve)
                                    hide h1clips
                                    show h1clipsl
                                    hide h1org
                                    show h1ouch
                                    h "Argggg...."
                                    "wzzzmmmm"
                                    h "!!!!"
                                    show h1slash2
                                    "Slash!" with hpunch                                    
                                    p "More!"
                                    show h1slash1
                                    hide h1ouch
                                    show h1clop
                                    "Slash!" with hpunch
                                    p "That is actually nice."
                                    h "Grrrr...."
                                    p "My lightning style is impresive right?"
                                    h "....."
                                    p "Ok that is enough."
                                    hide h1clipsl
                                    hide h1clop
                                    show h1sad
                                    p "Your body is so pretty."
                                    $ renpy.transition(dissolve)
                                    hide h1slash1
                                    hide h1slash2
                                    p "And you self heal once again."
                                    p "Ok, I will rest now... You should lick my cock during whole night."
                                    h "Sure..."
                                    scene black with circleirisin               
                                    show nharem0 with circleirisout
                                    jump nharem                                 
                                "Special Jutsu":
                                    p "I want to test something on you."
                                    $ renpy.transition(dissolve)
                                    show h1bg
                                    p "The preparation is important."
                                    with fade
                                    p "Look like your boobs is ok..."
                                    p "Time for attach the clips."
                                    $ renpy.transition(dissolve)
                                    hide h1bg
                                    show h1clips
                                    hide h1normal
                                    show h1open
                                    h "What are you going to do?"
                                    p "It is one experiment. I need to create stable chakra bridge."
                                    $ renpy.transition(dissolve)
                                    show h1ta
                                    h "What you mean by th...."
                                    $ renpy.transition(dissolve)
                                    hide h1ta
                                    show h1ta1
                                    hide h1clips
                                    show h1clipsl
                                    hide h1open
                                    show h1suprise
                                    h "What????"
                                    p "Shut up I must focus."
                                    $ renpy.transition(dissolve)
                                    hide h1ta1
                                    show h1ta
                                    h "But what you want to do?"
                                    $ renpy.transition(dissolve)
                                    hide h1ta
                                    show h1ta1
                                    hide h1clipsl
                                    show h1clips
                                    p "Look like it ready..."
                                    h "What is ready?"
                                    p "Lightning style - Circle of pleasure!" with vpunch
                                    $ renpy.transition(dissolve)
                                    hide h1clips
                                    show h1clipslu
                                    hide h1suprise
                                    show h1scared
                                    h "Aaaaaaa...."
                                    p "More!" with hpunch
                                    "Wzmmmmm..."
                                    $ renpy.transition(dissolve)
                                    hide h1scared
                                    show h1clop
                                    h "Argggggg....."
                                    with fade
                                    h "!!!!"
                                    with fade
                                    h "...."
                                    $ renpy.transition(dissolve)
                                    hide h1clipslu
                                    hide h1ta1
                                    show h1clips
                                    hide h1clop
                                    show h1clnormal
                                    p "Huh? It seems that it was all."
                                    p "..."
                                    $ renpy.transition(dissolve)
                                    hide h1clnormal
                                    show h1normal
                                    p "You did well."
                                    p "Ok, I will rest now... You should lick my cock during whole night."
                                    h "Sure..."
                                    scene black with circleirisin               
                                    show nharem0 with circleirisout
                                    jump nharem
                            
                        "Play with me":
                            p "This is the good time to show me your skills."
                            h "And what you mean by that?"
                            p "You know give me a nice handjob or something."
                            hide hibln
                            show hiblop
                            h "Ok I can do that just lay down."
                            p "I am very curious if you improve."                            
                            $ renpy.transition(dissolve)
                            hide hishy
                            hide hiclopen
                            hide himaak
                            hide himad
                            show h2body
                            show h2h1
                            show h2clhappy
                            p "Huh.. That was fast. What now?"
                            menu hiblowj1:
                                "Slap her":
                                    p "That as need one slap!"
                                    $ renpy.transition(dissolve)
                                    show h2red
                                    "Slap!" with vpunch
                                    p "And maybe more than one."
                                    "Slap!" with vpunch
                                    $ renpy.transition(dissolve)
                                    hide h2h1
                                    show h2h2
                                    hide h2clhappy
                                    hide h2cllick
                                    hide h2lick
                                    show h2scared
                                    h "Ouchhhh..."
                                    p "Move your hand faster!"
                                    $ renpy.transition(dissolve)
                                    hide h2h2
                                    show h2h3
                                    hide h2red
                                    h "Yes I try to...."
                                    $ renpy.transition(dissolve)
                                    show h2red
                                    "Slap!" with vpunch
                                    $ renpy.transition(dissolve)
                                    hide h2h3
                                    show h2h2
                                    h "Aacchhh..."
                                    $ renpy.transition(dissolve)
                                    hide h2h2
                                    show h2h1
                                    hide h2scared
                                    show h2cllick
                                    p "Come on you can do it better."
                                    $ renpy.transition(dissolve)
                                    hide h2h1
                                    show h2h2
                                    h "...."
                                    "Slap!" with vpunch
                                    $ renpy.transition(dissolve)
                                    hide h2h2
                                    show h2h3
                                    h "Auuu...."
                                    "Slap!" with vpunch
                                    $ renpy.transition(dissolve)
                                    hide h2h3
                                    show h2h2
                                    p "Yes!!!"
                                    "Slap!" with vpunch
                                    $ renpy.transition(dissolve)
                                    hide h2h2
                                    show h2h1
                                    p "MORE!"
                                    "Slap!" with vpunch
                                    p "Maybe I should do something else too."
                                    $ renpy.transition(dissolve)
                                    hide h2red
                                    jump hiblowj1
                                    
                                "Use whip":
                                    p "I want to try somthing."
                                    $ renpy.transition(dissolve)
                                    show h2scar1
                                    "Slash!" with vpunch
                                    p "Nice!"
                                    "Slash!" with vpunch
                                    $ renpy.transition(dissolve)
                                    show h2scar2
                                    hide h2cllick
                                    hide h2clhappy
                                    show h2scared
                                    h "Ouchhhh..."
                                    p "Move your hand faster!"
                                    $ renpy.transition(dissolve)
                                    hide h2h1
                                    show h2h3
                                    hide h2scar1
                                    h "Yes I try to...."
                                    $ renpy.transition(dissolve)
                                    show h2scar1
                                    "Whip!" with vpunch
                                    $ renpy.transition(dissolve)                                    
                                    hide h2h3
                                    show h2h2
                                    h "Ommmm...."
                                    $ renpy.transition(dissolve)
                                    hide h2h2
                                    show h2h1
                                    hide h2scared
                                    show h2cllick
                                    p "I say faster! That scars heal again and I still not cum!"
                                    $ renpy.transition(dissolve)
                                    hide h2scar2
                                    hide h2h1
                                    show h2h2
                                    h "Ok...."
                                    "Slash!" with vpunch
                                    $ renpy.transition(dissolve)
                                    show h2scar2
                                    hide h2h2
                                    show h2h3
                                    h "Auuu...."
                                    "Whip!" with vpunch
                                    $ renpy.transition(dissolve)
                                    hide h2scar1
                                    hide h2h3
                                    show h2h2
                                    p "Again!"
                                    "Whip!" with vpunch
                                    $ renpy.transition(dissolve)
                                    show h2scar1
                                    hide h2h2
                                    show h2h1
                                    p "MORE!"
                                    "Slash!" with vpunch
                                    p "That is fun what now?"
                                    $ renpy.transition(dissolve)
                                    hide h2scar1
                                    hide h2scar2
                                    jump hiblowj1
                                "Use clips":
                                    p "I think you need a motivation."
                                    $ renpy.transition(dissolve)
                                    hide h2h1
                                    show h2h2
                                    p "Do not move for a moment."
                                    $ renpy.transition(dissolve)
                                    show h2clips
                                    hide h2clhappy
                                    hide h2cllick
                                    hide h2lick
                                    show h2down
                                    h "!!!!"
                                    p "Nice right???"
                                    $ renpy.transition(dissolve)
                                    hide h2h2
                                    show h2h3
                                    h "Yes...."
                                    $ renpy.transition(dissolve)
                                    hide h2h3
                                    show h2h2
                                    p "And there is more!"
                                    $ renpy.transition(dissolve)
                                    hide h2h2
                                    show h2h1
                                    p "Lightning style!" with hpunch
                                    hide h2down
                                    show h2open2
                                    show h2clipsl
                                    h "Arggg..."
                                    $ renpy.transition(dissolve)
                                    hide h2h1
                                    show h2h2
                                    p "Good right?"
                                    $ renpy.transition(dissolve)
                                    hide h2h2
                                    show h2h3
                                    h "Ouuuu..."
                                    $ renpy.transition(dissolve)
                                    hide h2h3
                                    show h2h2
                                    hide h2clipsl
                                    hide h2open2
                                    show h2open
                                    h "....."
                                    $ renpy.transition(dissolve)
                                    hide h2h2
                                    show h2h1
                                    p "One more time!"
                                    $ renpy.transition(dissolve)
                                    hide h2h1
                                    show h2h2
                                    "Wzmmmm..."
                                    $ renpy.transition(dissolve)
                                    show h2clipsl
                                    hide h2open
                                    show h2org
                                    h "Yesssss...."
                                    $ renpy.transition(dissolve)
                                    hide h2h2
                                    show h2h3
                                    p "That technique is impressive right?"
                                    $ renpy.transition(dissolve)
                                    hide h2h3
                                    show h2h1
                                    h "......Very......"
                                    $ renpy.transition(dissolve)
                                    hide h2org
                                    show h2clhappy
                                    p "Should I try something else?"
                                    $ renpy.transition(dissolve)
                                    hide h2clipsl
                                    hide h2clips
                                    jump hiblowj1
                                    
                                "Cum":
                                    p "I am almost...."
                                    p "Yesssss!!! *splurt*"
                                    $ renpy.transition(dissolve)
                                    show h2spermin
                                    with fade
                                    p "Take it all!"
                                    $ renpy.transition(dissolve)
                                    hide h2h1
                                    show h2h3
                                    show h2spermout
                                    with fade
                                    p "Good hand work..."
                                    h "Thanks...."
                                    p "You can clean yourself now and dress up."
                                    h "Sure..."
                                    $ renpy.transition(dissolve)
                                    hide h2body
                                    hide h2h3
                                    hide h2h2
                                    hide h2h1
                                    hide h2spermout
                                    hide h2spermin
                                    hide h2clhappy
                                    hide h2cllick
                                    show himaak
                                    show hibln
                                    p "You have really good skill."
                                    p "But I still hope you will be better next time."
                                    h "I will try..."
                                    scene black with circleirisin               
                                    show nharem0 with circleirisout
                                    jump nharem
                            
                        "Fuck her":
                            p "No foreplay today."
                            p "Just strip and lay down"
                            h "Sure."                                                     
                            $ renpy.transition(dissolve)
                            hide hishy
                            hide hibln
                            hide himad
                            hide himaak
                            show hi3body
                            show hi3normal
                            p "There is a few thing I can do with her."
                            p "Where should I start?"
                            menu hima5551:
                                "Slap her":
                                    p "You need a male touch."
                                    show hi3hl1
                                    "SLAP!" with vpunch
                                    h "Arggg...."
                                    $ renpy.transition(dissolve)
                                    hide hi3normal
                                    show hi3onest
                                    p "That was good."
                                    show hi3hr1
                                    "SLAP!" with vpunch
                                    h "Yesss..."
                                    hide hi3hl1
                                    show hi3hl2
                                    "SLAP!" with vpunch
                                    $ renpy.transition(dissolve)
                                    show hi3drops
                                    hide hi3onest
                                    show hi3open
                                    h "Stronger!"
                                    hide hi3hr1
                                    show hi3hr2
                                    "SLAP!" with vpunch
                                    p "No problem."
                                    $ renpy.transition(dissolve)
                                    hide hi3open
                                    show hi3org
                                    h "Stronger!!!"
                                    hide hi3hl2
                                    show hi3hl3
                                    "SLAP!" with vpunch
                                    p "Seriously???"
                                    p "My hand is in fire. How does your ass have to feel?"
                                    hide hi3hr2
                                    show hi3hr3
                                    "SLAP!" with vpunch
                                    h "THIS !!!"
                                    $ renpy.transition(dissolve)
                                    hide hi3org
                                    show hi3org2
                                    p "heh..."
                                    p "Your ass is nice red now..."
                                    p "Should I countinue?"
                                    menu:
                                        "Just continue":
                                            p "No time for rest..."
                                            p "What now?"
                                            $ renpy.transition(dissolve)
                                            hide hi3org2
                                            show hi3normal
                                            hide hi3hr3
                                            show hi3hr1
                                            hide hi3hl3
                                            show hi3hl1
                                            
                                        "Give her time to heal":
                                            p "Relax now..."
                                            p "That red color is almost glowing..."
                                            $ renpy.transition(dissolve)
                                            hide hi3hr3
                                            show hi3hr2
                                            hide hi3hl3
                                            show hi3hl2
                                            p "That is better...."
                                            p "I wait just a little longer..."
                                            with fade
                                            $ renpy.transition(dissolve)
                                            hide hi3hr2
                                            show hi3hr1
                                            hide hi3org2
                                            show hi3normal
                                            hide hi3hl2
                                            show hi3hl1
                                            hide hi3drops
                                            p "Maybe a one moment..."
                                            with fade
                                            $ renpy.transition(dissolve)
                                            hide hi3hr1
                                            hide hi3hl1
                                            p "It look good... What now?"
                                    
                                    jump hima5551
                                "Use clips":
                                    p "Maybe I use something you like now."
                                    $ renpy.transition(dissolve)
                                    hide hi3clips
                                    p "Like that clips."
                                    $ renpy.transition(dissolve)
                                    hide hi3normal
                                    show hi3clhappy
                                    h "Mmmmmm..."
                                    p "And you know what's going to happen."
                                    h "Lightning style..."
                                    p "Exactly..."
                                    p "But you must beg for it..."
                                    $ renpy.transition(dissolve)
                                    hide hi3clhappy
                                    show hi3clok
                                    h "...."
                                    h "Please use your lightning style..."
                                    p "???"
                                    h "Release your energy in to my nipples..."
                                    h "Please...."
                                    p "That was pathetic..."
                                    p "Lightning style jutsu!" with hpunch
                                    hide hi3clips
                                    show hi3clipsl
                                    show hi3drops
                                    h "Yessss...."
                                    $ renpy.transition(dissolve)
                                    hide hi3clok
                                    show hi3org
                                    p "More chakra!" with hpunch 
                                    p "Lightning style second gate!"
                                    hide hi3clipsl
                                    show hi3clipslex
                                    h "Yessss!!!"  with hpunch
                                    $ renpy.transition(dissolve)
                                    hide hi3org
                                    show hi3org2
                                    h "Arrrr....."
                                    with fade
                                    p "Hehe... that is funny..."
                                    $ renpy.transition(dissolve)
                                    hide hi3clipslex
                                    show hi3clipsl
                                    p "But I must spare a little chakra."
                                    $ renpy.transition(dissolve)
                                    hide hi3clipsl
                                    show hi3clips
                                    menu:
                                        "Keep clips":
                                            p "You look good with that clips."
                                            $ renpy.transition(dissolve)
                                            hide hi3org2
                                            show hi3normal
                                            p "You can keep her for next step."
                                                                                        
                                        "Remove clips":
                                            p "That clips is nice."
                                            $ renpy.transition(dissolve)
                                            hide hi3org2
                                            show hi3normal
                                            $ renpy.transition(dissolve)
                                            p "But it is time to remove them and try something else."
                                            hide hi3clips
                                            hide hi3drops
                                    
                                    jump hima5551
                                "Use whip":
                                    p "You need to respect me."
                                    p "I have one tool that can help you with that..."
                                    show hi3scar1
                                    "Whip!" with hpunch
                                    h "Argg.g...."
                                    $ renpy.transition(dissolve)
                                    hide hi3normal
                                    show hi3clteeth                                    
                                    h "Why????"
                                    "Whip!" with hpunch
                                    p "Is it not clear?"
                                    show hi3scar2
                                    show hi3drops
                                    "Whip!" with hpunch
                                    p "Your body is not that strong as you think."
                                    "Slash!" with hpunch
                                    h "!!!!"
                                    $ renpy.transition(dissolve)
                                    hide hi3clteeth
                                    show hi3clop
                                    h "Ouuuuu...."
                                    p "You need to endure this!!!!"
                                    "Slash!" with hpunch 
                                    h "Arggg..."
                                    show hi3scar3
                                    "Whip!" with hpunch
                                    h "!!!!"
                                    p "That is the right response."
                                    show hi3scar3
                                    $ renpy.transition(dissolve)
                                    hide hi3clop
                                    show hi3clteeth
                                    "Whip!" with hpunch
                                    h "...."
                                    p "You need to be quiet..."
                                    "Whip!" with hpunch
                                    h "...."
                                    p "Look like you understant."
                                    p "What now?"
                                    menu:
                                        "Supress her healing ability.":
                                            p "This time you will keep these scars."
                                            p "It will remind you that lesson for a moment."
                                            p "My next step is..."
                                            $ renpy.transition(dissolve)
                                            hide hi3clteeth
                                            show hi3normal
                                        "Give her time to heal.":
                                            p "That was nice whiping training."
                                            p "I give you a time to heal these scars."
                                            with fade
                                            $ renpy.transition(dissolve)
                                            hide hi3scar1 
                                            hide hi3clteeth
                                            show hi3normal
                                            p "..."                                            
                                            $ renpy.transition(dissolve)
                                            hide hi3scar2
                                            p "Yes they are disappearing."
                                            $ renpy.transition(dissolve)
                                            hide hi3scar3
                                            hide hi3drops
                                            p "You look good."
                                            p "Now is time for..."                                    
                                    jump hima5551
                                "Use dildo":
                                    p "Time for your favorite toy!"
                                    p "Or my...."
                                    p "Take a breath."
                                    $ renpy.transition(dissolve)
                                    hide hi3normal
                                    show hi3scared
                                    h "Wait what?" 
                                    show hi3dil1
                                    h "Arg...." with hpunch
                                    p "Come on I know you love that."
                                    p "And you love more when I turn this on."
                                    $ renpy.transition(dissolve)
                                    hide hi3dil1
                                    show hi3drops
                                    show hanal
                                    hide hi3scared
                                    show hi3clop
                                    h "Yaiksssss..."
                                    p "hehh..."
                                    $ renpy.transition(dissolve)
                                    hide hi3clop
                                    show hi3clteeth
                                    h "Mmmmmmm...."
                                    p "Still that sad look..."
                                    p "maybe I turn it off..."
                                    $ renpy.transition(dissolve)
                                    hide hanal
                                    show hi3dil1
                                    hide hi3clteeth
                                    show hi3sad                                    
                                    h "No...."
                                    p "???"
                                    h "Turn it on...."
                                    p "Sure."
                                    $ renpy.transition(dissolve)
                                    hide hi3dil1
                                    show hanal
                                    hide hi3sad
                                    show hi3clhappy
                                    h "Mmmmm..."
                                    $ renpy.transition(dissolve)
                                    hide hi3clhappy
                                    show hi3org
                                    p "That was enough..."
                                    menu:
                                        "Remove dildo":
                                            p "I just turn it off."
                                            $ renpy.transition(dissolve)
                                            hide hanal
                                            show hi3dil1
                                            h "Wait..."
                                            p "And pull it out."
                                            $ renpy.transition(dissolve)
                                            hide hi3dil1
                                            hide hi3org
                                            show hi3normal
                                            hide hi3drops
                                            p "And now is time for."
                                            
                                        "Let dildo inside":
                                            p "I just turn it off."
                                            $ renpy.transition(dissolve)
                                            hide hanal
                                            show hi3dil1
                                            h "Wait..."
                                            p "But I will leve it in your ass."
                                            $ renpy.transition(dissolve)
                                            hide hi3org
                                            show hi3normal
                                            p "Because the fun is just beginning."                                            
                                    
                                    jump hima5551
                                "Fuck her":
                                    p "This is a good time for real action!"
                                    p "Give you a pleasure you want so much."
                                    $ renpy.transition(dissolve)
                                    hide hi3normal
                                    show hi3clhappy
                                    show hi3p1
                                    h "Are you going to fuck me finally?"
                                    p "Yes something like that."
                                    p "I mean..."
                                    $ renpy.transition(dissolve)
                                    hide hi3p1
                                    show hi3p2
                                    h "Aaaaaaa..."
                                    p "Yesss..."
                                    $ renpy.transition(dissolve)
                                    hide hi3p2
                                    show hi3p3
                                    hide hi3clhappy
                                    show hi3clteeth
                                    show hi3drops
                                    h "More..."
                                    $ renpy.transition(dissolve)
                                    hide hi3p3
                                    show hi3p2
                                    p "That pussy..."
                                    $ renpy.transition(dissolve)
                                    hide hi3p2
                                    show hi3p3
                                    hide hi3clteeth
                                    show hi3clop
                                    p "Is amazing."
                                    $ renpy.transition(dissolve)
                                    hide hi3p3
                                    show hi3p2
                                    h "Fuck ME!"
                                    $ renpy.transition(dissolve)
                                    hide hi3p2
                                    show hi3p3
                                    h "Harder!"
                                    $ renpy.transition(dissolve)
                                    hide hi3p3
                                    show hi3p2
                                    h "Harder!!!" with hpunch
                                    $ renpy.transition(dissolve)
                                    hide hi3p2
                                    show hi3p3
                                    hide hi3clop
                                    show hi3org
                                    h "Yesss!!!"
                                    $ renpy.transition(dissolve)
                                    hide hi3p3
                                    show hi3p2
                                    hide hi3org
                                    show hi3org2
                                    h "Aaaaaaa...."
                                    p "Shit Iam almost..."
                                    $ renpy.transition(dissolve)
                                    hide hi3p2
                                    show hi3p3
                                    p "..."
                                    menu:
                                        "Cum inside":
                                            h "That is..."   
                                            hide hi3p3
                                            show hi3spermin
                                            p "Take that!" with hpunch
                                            with fade
                                            p "!!!"
                                            with fade
                                            h "Yesssssss...."
                                            with fade
                                            p "..."
                                            with fade
                                            p "I am always happy after our training."
                                            with fade
                                            h "...."
                                            p "But all good ends once."
                                            h "..."
                                            p "You will be with me tonight. And take care of my body."
                                            h "Sure..."
                                            scene black with circleirisin               
                                            show nharem0 with circleirisout
                                            jump nharem
                                            
                                        "Cum out":
                                            $ renpy.transition(dissolve)
                                            hide hi3p3
                                            show hi3p2
                                            p "Just a moment..."
                                            $ renpy.transition(dissolve)
                                            hide hi3p2
                                            show hi3p1
                                            show hi3spermout
                                            p "On your body!"
                                            $ renpy.transition(dissolve)
                                            hide hi3spermout
                                            show hi3spermout2
                                            h "Aaaaaa..."
                                            $ renpy.transition(dissolve)
                                            hide hi3spermout2
                                            show hi3spermout3
                                            p "Huh..."
                                            p "Look like that was everything..."
                                            with fade
                                            h "Everything..."
                                            with fade
                                            p "Are you alright?"
                                            h "Yes just. That was amazing."
                                            p "Meh..."
                                            p "You can do it better next time."
                                            p "You will be with me tonight. And take care of my body."
                                            h "Sure..."
                                            scene black with circleirisin               
                                            show nharem0 with circleirisout
                                            jump nharem
                                            
                        "Kage bunshin":
                            p "I always want to try this."
                            p "I think it will be a real fun! Strip!"
                            h "Sure."                                                     
                            $ renpy.transition(dissolve)
                            hide hishy
                            hide hibln
                            hide himaak
                            hide himad
                            p "Kage bunshin no jutsu!!!" with hpunch
                            h "Argg.... *moan*"
                            $ renpy.transition(dissolve)
                            show him3xa
                            show him3xdo
                            show him3xbl1
                            show him3xf1
                            p "Yes. This is what I am talking about!!!"
                            $ renpy.transition(dissolve)
                            hide him3xbl1
                            show him3xbl2
                            p "Right. Open that mouth."
                            $ renpy.transition(dissolve)
                            hide him3xbl2
                            show him3xbl3
                            h "mgm*gag*"
                            $ renpy.transition(dissolve)
                            hide him3xdo
                            show him3xok
                            hide him3xbl3
                            show him3xbl4
                            hide him3xf1
                            show him3xf2
                            p "Yeah... That ass is hot too!!!"
                            $ renpy.transition(dissolve)
                            hide him3xbl4
                            show him3xbl3
                            hide him3xf2
                            show him3xf3
                            p "Maybe I should...."
                            menu:
                                "Continue":
                                    p "Fuck her hard!"
                                "Big boobs expansion":
                                    p "Use boobs expansion."
                                    $ renpy.transition(dissolve)
                                    hide him3xbl3
                                    show him3xbl2
                                    hide him3xf3
                                    show him3xf4
                                    p "Boobs expansion!"
                                    $ renpy.transition(dissolve)
                                    hide him3xok
                                    hide him3xa
                                    hide him3xf4
                                    hide him3xbl2
                                    show him3xb
                                    show him3xcl
                                    show him3xf4
                                    show him3xbl2
                                    h "MGHGMM??? *gag shock*"
                                    $ renpy.transition(dissolve)
                                    hide him3xbl2
                                    show him3xbl3
                                    hide him3xf4
                                    show him3xf3
                                    p "Yes this is better!"
                                    
                                "Huge boobs expansion":
                                    p "Make them really big."
                                    $ renpy.transition(dissolve)
                                    hide him3xbl3
                                    show him3xbl2
                                    hide him3xf3
                                    show him3xf4
                                    p "Boobs expansion, full release!"
                                    $ renpy.transition(dissolve)
                                    hide him3xok
                                    hide him3xa
                                    hide him3xf4
                                    hide him3xbl2
                                    show him3xc
                                    show him3xcl
                                    show him3xf4
                                    show him3xbl2
                                    h "MGHGMM??? *gag shock*"
                                    $ renpy.transition(dissolve)
                                    hide him3xbl2
                                    show him3xbl3
                                    hide him3xf4
                                    show him3xf3
                                    p "I just love huge boobs!"
                                    
                            $ renpy.transition(dissolve)
                            hide him3xbl3
                            show him3xbl2
                            hide him3xf3
                            show him3xf4 
                            h "Gmmgmm.*gag cough*"
                            $ renpy.transition(dissolve)
                            hide him3xcl
                            hide him3xok
                            show him3xdo
                            hide him3xbl2
                            show him3xbl3
                            hide him3xf4
                            show him3xf3 
                            p "I want to fuck you more..."
                            $ renpy.transition(dissolve)
                            hide him3xbl3
                            show him3xbl4
                            hide him3xf3
                            show him3xf2
                            h "gggg... *gag*"
                            $ renpy.transition(dissolve)
                            hide him3xbl4
                            show him3xbl3
                            hide him3xf2
                            show him3xf3
                            p "Yeah!!! *splurt*"
                            $ renpy.transition(dissolve)
                            hide him3xdo
                            show him3xok
                            hide him3xbl3
                            show him3xbl2
                            hide him3xf3
                            show him3xf4
                            show him3xf5
                            p "Fucking awesome!!!"
                            $ renpy.transition(dissolve)
                            hide him3xbl2
                            show him3xbl3
                            show him3xf6
                            h "Mgmmm !!! *cough*"
                            $ renpy.transition(dissolve)
                            hide him3xok
                            show him3xdo
                            hide him3xbl3
                            show him3xbl4
                            show him3xbl5
                            p "Shit!!!*splurt*"
                            $ renpy.transition(dissolve)
                            show him3xbl6
                            h "hggghgh....*drip*"
                            p "That was really epic!"
                            h "Ghhgh.... *cough*"
                            p "Hehe, nice right?"
                            h "Gggggh.... *cough gag*"
                            p "Good night, kid."
                            scene black with circleirisin               
                            show nharem0 with circleirisout
                            jump nharem
                            
                
            "Call Hanabi":
                if hanabislave >=8:
                            $ renpy.transition(dissolve)
                            show hanaa
                            show hannok
                            ha "..."
                            p "Nice... What now?"
                            menu:
                                "Strip her":
                                        ha "...."
                                        $ renpy.transition(dissolve)
                                        hide hanaa
                                        hide hannok
                                        show hanab
                                        show hannsad
                                        p "Yeah... Good girl..."
                                        p "Kiss me!"
                                        ha "mmmm... *smooch*"
                                        p "Yeah... That is good...."
                                        ha "*moan smooch*"
                                        $ renpy.transition(dissolve)
                                        hide hannsad
                                        show hancl
                                        p "Your tongue is amazing. I hope it can do more than just kissing."
                                        ha "..."
                                        p "I am tired today, next time we can have more fun..."
                                        scene black with circleirisin  
                                        "You ordered Hanabi to dress and release Namigan. She didn't remember anything and was happy that she can help you."
                                        show nharem0 with circleirisout
                                        jump nharem
                                    
                                "Play with her":
                                        p "Now show me your body."
                                        $ renpy.transition(dissolve)
                                        hide hanaa
                                        hide hannok
                                        show hanab
                                        show hannok
                                        p "Come closer... *smooch*"
                                        ha "*smooch*"
                                        p "I want to try something today.*clamp*"
                                        $ renpy.transition(dissolve)
                                        show hanl1
                                        ha "*moan pain*"
                                        p "Yeah this looks good on you...*clamp*"
                                        $ renpy.transition(dissolve)
                                        show hanl2
                                        ha "*groan*"
                                        p "Nice... I wonder how much you can endure..."
                                        p "Lightning style!!! *zap*"
                                        $ renpy.transition(dissolve)
                                        show hanl3
                                        hide hannok
                                        show hanclop
                                        ha "Mmmmm...**"
                                        p "More power!!!"
                                        $ renpy.transition(dissolve)
                                        show hanl4
                                        ha "*moan pain*"
                                        $ renpy.transition(dissolve)
                                        show hanl5
                                        hide hanclop
                                        show hannorg
                                        ha "Yeah! *moan groan*"
                                        p "Fuck you are so good..."
                                        $ renpy.transition(dissolve)
                                        hide hanl5
                                        ha "*moaning*"
                                        $ renpy.transition(dissolve)
                                        hide hanl4
                                        p "I am running out of the chakra..."
                                        $ renpy.transition(dissolve)
                                        hide hanl3
                                        p "Nice.... "
                                        ha "Ahhh...."
                                        p "But I can still try something else..."
                                        $ renpy.transition(dissolve)
                                        show hantext
                                        p "Nice.... Now rub my cock!"
                                        ha "*fap fap*"
                                        p "Ohhh... Good..."
                                        ha "*fap fap*"
                                        p "Yeah...."
                                        ha "*fap fap fap*"
                                        p "Ahhh...*splurt*"
                                        $ renpy.transition(dissolve)
                                        hide hannorg
                                        show hannhap
                                        show hansp1
                                        p "FUCK!!!**splurt"
                                        $ renpy.transition(dissolve)
                                        show hansp2
                                        ha "...*drip*"
                                        p "Awesome...."
                                        p "You have some skills..."
                                        ha "..."
                                        p "Nevermind..."
                                        p "Time to put you back together..."
                                        scene black with circleirisin  
                                        "Hanabi is really funny playdoll.. I hope she will not figure out what is really happening."
                                        show nharem0 with circleirisout
                                        jump nharem
                                        
                                
                                "Boob Expansion":
                                        p "I want to try something new today..."
                                        p "Just open your kimono a little and sit down..."
                                        $ renpy.transition(dissolve)
                                        hide hanaa
                                        hide hannok
                                        show han4a
                                        show han4nsad
                                        p "Nice...."
                                        p "You can take it off now..."
                                        $ renpy.transition(dissolve)
                                        hide han4a
                                        hide han4nsad
                                        show han4b
                                        show han4nsad
                                        p "That was easy..."
                                        ha "...."
                                        p "And now..."
                                        menu:
                                            "Slash her":
                                                p "I will just have some fun..."
                                                ha "...."
                                                p "Take this... *slash*"
                                                $ renpy.transition(dissolve)
                                                hide han4clsad
                                                hide han4nsad
                                                show han4nok
                                                show han4sl1
                                                ha "Ahhhh...*moan*"
                                                p "Yeah!!!*slash*"
                                                $ renpy.transition(dissolve)
                                                show han4sl2
                                                p "You love it right???"
                                                ha "Mmmm..."
                                                p "And now!!!*slash*" with hpunch
                                                $ renpy.transition(dissolve)
                                                show han4sl3
                                                hide han4nok
                                                show han4clop
                                                ha "YeSSSS!!!!! * heavy moaning*"
                                                p "Nice... But this is probably too much right now..."
                                                ha "mmmmmm...."
                                                p "Time to put yourself together Hanabi..."
                                                scene black with circleirisin  
                                                "Expansion is always funny, mainly with the Hyuga girls."
                                                "You heal the scars and she didn't notice anything."
                                                show nharem0 with circleirisout
                                                jump nharem
                                                
                                            "Medium expasnion":
                                                p "Boobs expansion!!!"
                                                $ renpy.transition(dissolve)
                                                hide han4b
                                                hide han4nsad
                                                show han4c
                                                show han4clsad
                                                ha "*Moan*"
                                                p "Awesome!!! "
                                                p "Now is time to put some clips on that boobs..."
                                                ha "*clamp*"
                                                $ renpy.transition(dissolve)
                                                show han4l1
                                                ha "mmmm...."
                                                p "Lightning style!!!"
                                                $ renpy.transition(dissolve)
                                                hide han4clsad
                                                show han4nok
                                                show han4l2
                                                ha "*heavy moaning*"
                                                p "Yeah!!! More power! *zap*"
                                                $ renpy.transition(dissolve)
                                                hide han4nok
                                                show han4nhap
                                                show han4l3
                                                p "Do you like it???"
                                                ha "Ahhhh...*heavy groaning*"
                                                $ renpy.transition(dissolve)
                                                hide han4nhap
                                                show han4norg
                                                p "That was probably yes..."
                                                ha "*moan*"
                                                p "You love it right???"
                                                ha "Mmmm..."
                                                p "Ok... I will now release the Namigan... Put yourself together..."
                                                scene black with circleirisin  
                                                "Expansion is always funny, mainly with the Hyuga girls."
                                                show nharem0 with circleirisout
                                                jump nharem
                                                
                                            "Fuck her boobs":
                                                p "Boobs expansion!!!"
                                                $ renpy.transition(dissolve)
                                                hide han4b
                                                hide han4nsad
                                                show han4c
                                                show han4clsad
                                                ha "*Moan*"
                                                p "Awesome!!! "
                                                p "But I want them a little bigger..."
                                                p "Boobs expansion!!!"
                                                $ renpy.transition(dissolve)
                                                hide han4c
                                                hide han4clsad
                                                show han4d
                                                show han4clop
                                                ha "mmmm...."
                                                $ renpy.transition(dissolve)
                                                show han4tf1
                                                p "Good..."
                                                $ renpy.transition(dissolve)
                                                hide han4tf1
                                                show han4tf2
                                                ha "*moaning*"
                                                p "Yeah!!!"
                                                $ renpy.transition(dissolve)
                                                hide han4tf2
                                                show han4tf3
                                                p "Do you like it???"
                                                $ renpy.transition(dissolve)
                                                hide han4tf3
                                                show han4tf4
                                                ha "..."
                                                $ renpy.transition(dissolve)
                                                hide han4tf4
                                                show han4tf3
                                                p "I like it and that is important..."
                                                $ renpy.transition(dissolve)
                                                hide han4tf4
                                                show han4tf3
                                                hide han4clop
                                                show han4nok
                                                p "Nice..."
                                                $ renpy.transition(dissolve)
                                                hide han4tf3
                                                show han4tf2
                                                ha "*moan*"
                                                $ renpy.transition(dissolve)
                                                hide han4tf2
                                                show han4tf3
                                                p "I will..."
                                                $ renpy.transition(dissolve)
                                                hide han4tf3
                                                show han4tf4
                                                p "Yeah!!!"
                                                $ renpy.transition(dissolve)
                                                hide han4nok
                                                show han4nhap
                                                show han4tf5
                                                ha "Mmmm...*drip squirt*"
                                                $ renpy.transition(dissolve)
                                                show han4milk
                                                show han4tf6
                                                ha "Ahhh....*drip*"
                                                p "Hmmm.. You look good now...."
                                                ha "Aaa....."
                                                p "But it is time to clean this..."
                                                p "Drink all the sperm first, then clean the rest..."
                                                scene black with circleirisin  
                                                "It is amazing to fuck her boobs when they have that size."
                                                "I wonder if she noticed anything."
                                                show nharem0 with circleirisout
                                                jump nharem
                                                
                                            
                                        
                                        
                                
                                "Fuck her":
                                        p "I want to fuck your pussy now...."
                                        ha "..."
                                        p "You know what to do..."
                                        $ renpy.transition(dissolve)
                                        hide hanaa
                                        hide hannok
                                        show han3a
                                        show han3nok
                                        p "Yeah, just like that... *smooch*"
                                        ha "...."
                                        $ renpy.transition(dissolve)
                                        show han3p1
                                        p "Yeah... Now is time to..."
                                        $ renpy.transition(dissolve)
                                        hide han3p1
                                        show han3p2
                                        ha "Mmmm... *moan*"
                                        $ renpy.transition(dissolve)
                                        hide han3p2
                                        show han3p3
                                        p "Nice...."
                                        $ renpy.transition(dissolve)
                                        hide han3p3
                                        show han3p4
                                        hide han3nok
                                        show han3cl
                                        ha "*groan*"
                                        $ renpy.transition(dissolve)
                                        hide han3p4
                                        show han3p3
                                        p "You are gorgeous..."
                                        $ renpy.transition(dissolve)
                                        hide han3p3
                                        show han3p2
                                        ha "*moan*"
                                        $ renpy.transition(dissolve)
                                        hide han3p2
                                        show han3p3
                                        hide han3cl
                                        show han3nhap
                                        p "It is good right?"
                                        $ renpy.transition(dissolve)
                                        hide han3p3
                                        show han3p4
                                        ha "Ahhh....*heavy moaning*"
                                        $ renpy.transition(dissolve)
                                        hide han3p4
                                        show han3p3
                                        hide han3nhap
                                        show han3norg
                                        p "Fuck this is hot!!!"
                                        menu:
                                            "Slash her":
                                                p "Take this!!! *slash*"
                                                $ renpy.transition(dissolve)
                                                hide han3p3
                                                show han3p2
                                                show han3sl1
                                                ha "*moan pain*"
                                                p "And more!!! *slash*"
                                                $ renpy.transition(dissolve)
                                                hide han3p2
                                                show han3p3
                                                hide han3norg
                                                show han3clop
                                                show han3sl2
                                                ha "*heavy moaning*"
                                                p "And one more time! *slash*" with vpunch
                                                $ renpy.transition(dissolve)
                                                hide han3p3
                                                show han3p4
                                                show han3sl3
                                                ha "Ahhh...*moan pain*"
                                                p "Maybe I will try this too..."
                                                $ renpy.transition(dissolve)
                                                hide han3p4
                                                show han3p3
                                                hide han3clop
                                                show han3norg
                                                show han3pierce
                                                show han3milk
                                                ha "Yessss!!!! *heavy moaning*"
                                                p "Fuck!!! * splurt*"
                                                $ renpy.transition(dissolve)
                                                hide han3p3
                                                show han3p4
                                                show han3p5
                                                ha "*moan drip*"
                                                $ renpy.transition(dissolve)
                                                show han3p6
                                                p "Wow... Your pussy is awesome..."
                                                ha "..."
                                                p "Yeah... I forgot... You can't answer me in this state.."
                                                p "Time to cancel Namigan and get you back to normal..."
                                                scene black with circleirisin  
                                                "When you fuck the Hanabi, you forget about all current problems."
                                                "You should do it more often."
                                                show nharem0 with circleirisout
                                                jump nharem
                                                
                                            "Cum out":
                                                p "Fuck... I should cum on your body..."
                                                $ renpy.transition(dissolve)
                                                hide han3p3
                                                show han3p2
                                                ha "*moan*"
                                                $ renpy.transition(dissolve)
                                                hide han3p2
                                                show han3p1
                                                p "Fuck!!! * splurt*"
                                                $ renpy.transition(dissolve)
                                                show han3p7
                                                ha "*moan drip*"
                                                $ renpy.transition(dissolve)
                                                show han3p8
                                                p "Wow... Your pussy is awesome..."
                                                ha "..."
                                                p "Yeah... I forgot... You can't answer me in this state.."
                                                p "Time to cancel Namigan and get you back to normal..."
                                                scene black with circleirisin  
                                                "When you fuck the Hanabi, you forget about all current problems."
                                                "You should do it more often."
                                                show nharem0 with circleirisout
                                                jump nharem
                                                
                                            "Kage bunshin":
                                                p "I want more!!!"
                                                $ renpy.transition(dissolve)
                                                hide han3p3
                                                show han3p2
                                                ha "*moan*"
                                                $ renpy.transition(dissolve)
                                                hide han3p2
                                                show han3p3
                                                p "Kage bunshin no jutsu!!!"
                                                $ renpy.transition(dissolve)
                                                hide han3p3
                                                show han3p4
                                                hide han3norg
                                                show han3cl
                                                show han3p9
                                                show han3p11
                                                p "Nice...."
                                                $ renpy.transition(dissolve)
                                                hide han3p4
                                                show han3p3
                                                ha "Ahhh...*moan*"
                                                $ renpy.transition(dissolve)
                                                hide han3p3
                                                show han3p2
                                                p "Fuck this is good..."
                                                $ renpy.transition(dissolve)
                                                hide han3p2
                                                show han3p3
                                                hide han3cl
                                                show han3clop
                                                ha "*moan*"
                                                $ renpy.transition(dissolve)
                                                hide han3p3
                                                show han3p4
                                                p "Yaah! *splurt*"
                                                $ renpy.transition(dissolve)
                                                hide han3p4
                                                show han3p3
                                                show han3p10
                                                p "More! *spurt*"
                                                $ renpy.transition(dissolve)
                                                hide han3p3
                                                show han3p2
                                                show han3p12
                                                p "This is so good..."
                                                $ renpy.transition(dissolve)
                                                hide han3p2
                                                show han3p3
                                                p "And finally!!!"
                                                $ renpy.transition(dissolve)
                                                hide han3p3
                                                show han3p4
                                                show han3p5
                                                hide han3clop
                                                show han3norg
                                                ha "*moan drip*"
                                                $ renpy.transition(dissolve)
                                                show han3p6
                                                p "Yeah!!!"
                                                p "You are so dirty right now!!!"
                                                ha "Aaaa....*moan*"
                                                p "And relaxed...."
                                                p "I hope you enjoyed it."
                                                ha "...."
                                                scene black with circleirisin 
                                                "It is good to use Kage Bunshin and cum more times at once..."
                                                "Hanabi liked it too... I think..."
                                                show nharem0 with circleirisout
                                                jump nharem
                                        
                                    
                        
                        
                                "Go somewhere else":
                                    scene black with circleirisin               
                                    show dharem0 with circleirisout
                                    jump dharem 
                    
                else:
                    "Hanabi is not here right now. Find her in the Konoha."
                    scene black with circleirisin               
                    show dharem0 with circleirisout
                    jump dharem 
            
            "More fun":
                if hinami <=10:
                    "You need Himawari for this option..."
                    scene black with circleirisin               
                    show dharem0 with circleirisout
                    jump dharem 
                elif hinatamission <=14:
                    "You need Hinata for this option..."
                    scene black with circleirisin               
                    show dharem0 with circleirisout
                    jump dharem 
                elif hanabislave <=7: 
                    "You need Hanabi for this option..."
                    scene black with circleirisin               
                    show dharem0 with circleirisout
                    jump dharem 
                else:
                    p "So finally I have all three of the Hyuga girls..."
                    p "Kage bunshin no jutsu!!!"
                    $ renpy.transition(dissolve)
                    show hhh1
                    ha "Mmmmm... *moaning*"
                    $ renpy.transition(dissolve)
                    hide hhh1
                    show hhh2
                    hi "Fuck this is good!!!"
                    $ renpy.transition(dissolve)
                    hide hhh2
                    show hhh3
                    h "More!!! *moaning*"
                    $ renpy.transition(dissolve)
                    hide hhh3
                    show hhh2
                    p "Wow..."
                    $ renpy.transition(dissolve)
                    hide hhh2
                    show hhh1
                    hi "Yesss....*moan*"
                    $ renpy.transition(dissolve)
                    hide hhh1
                    show hhh2
                    p "Yeah this is good...."
                    $ renpy.transition(dissolve)
                    hide hhh2
                    show hhh3
                    p "You are so hot girls!!!"
                    $ renpy.transition(dissolve)
                    hide hhh3
                    show hhh2
                    ha "*moan*"
                    $ renpy.transition(dissolve)
                    hide hhh2
                    show hhh1
                    h "Ahhh....*moan*"
                    $ renpy.transition(dissolve)
                    hide hhh1
                    show hhh2
                    p "Nice.... Maybe this will help..."
                    $ renpy.transition(dissolve)
                    hide hhh2
                    show hhh3
                    show hhhtext
                    hi "Ahhhhh... Yesss...*moan squirt*"
                    $ renpy.transition(dissolve)
                    show hhhmilk
                    p "Yeah!!!*splurt*"
                    $ renpy.transition(dissolve)
                    show hhhsp1
                    hi "More!!! *drip*"
                    $ renpy.transition(dissolve)
                    show hhhsp2
                    p "This is everything I had."
                    ha "....*moan drip*"
                    h "Mmm...*moan*"
                    with fade
                    p "Ok... Now is time to clean the mess... Lick it all... I'll be watching you..."
                    $ renpy.transition(dissolve)
                    hide hhhmilk
                    hide hhhtext
                    hide hhhsp1
                    hide hhhsp2
                    p "I love this girls..."
                    scene black with circleirisin 
                    show nharem0 with circleirisout
                    jump nharem
            
            "Go back to the map":
                scene black with circleirisin               
                show dharem0 with circleirisout
                jump dharem 
            
    scene black with circleirisin               
    show dharem0 with circleirisout
    jump dharem 




















################################ dharemcave1
################################ dharemcave1
################################ dharemcave1
################################ dharemcave1
################################ dharemcave1
label dharemcave1:
    menu:
        "Explore the cave":
            "You go into the cave and try to find some items."
            $ randomnum = renpy.random.randint(1,3) # (randomize between 1 and 3)
            if randomnum==1:
                "You didn't find anything useful."
                scene black with circleirisin               
                show nharem0 with circleirisout
                jump nharem
            if randomnum==2:
                "You find some old kunais and sold it."
                $ ryo = ryo + 100
                "You got 100 ryo."
                scene black with circleirisin               
                show nharem0 with circleirisout
                jump nharem
            if randomnum==3:
                "You find a rare armor. And got 300 Ryo."
                $ ryo = ryo + 300
                scene black with circleirisin               
                show nharem0 with circleirisout
                jump nharem
                
        "Have fun with Tsunade":
            if tsumission >=17:
                scene black with circleirisin               
                show doffice with circleirisout
                show doffice
                $ renpy.transition(dissolve)
                if tsunapick ==1:
                    show tsunade1
                if tsunapick ==2:
                    show tsunade2
                if tsunapick ==3:
                    show tsunade3
                show tsunanna
                t "%(p)s...."
                p "So what I can do now?"
                menu:
                    
                                "Basic boob grow":
                                        $ tsunapick = 1 
                                        p "Now prepare yourself for training!"
                                        t "..."
                                        $ renpy.transition(dissolve)
                                        hide tsunade1
                                        hide tsunade2
                                        hide tsunade3 
                                        hide tsunanna
                                        show tsunade1n
                                        show tsunanna                                        
                                        p "Good now is time to have some fun."
                                        p "What should I do first?"
                                        menu tsuboobs1:
                                            "Increase boob size":
                                                if tsunapick == 3:
                                                    p "I really want to make them really huge!"
                                                    p "Expansion!!!" with hpunch
                                                    hide tsunanna 
                                                    show tsunaclop
                                                    t "ARgggg!!!"
                                                    p "More!!!"
                                                    $ renpy.transition(dissolve)
                                                    show tsunamil3
                                                    t "Yeah!"
                                                    p "Just another milk."
                                                    p "Hmm... Maybe I can sell it or something...."
                                                    $ renpy.transition(dissolve)
                                                    hide tsunamil3                                                    
                                                    hide tsunaclop
                                                    show tsunanna 
                                                    p "Huh?"
                                                    p "I need to focus more on training."                                                    
                                                    
                                                elif tsunapick == 2:
                                                    $ tsunapick = 3
                                                    p "That boobs look great but I need to make them bigger!"
                                                    p "Expansion!!!" with hpunch
                                                    hide tsunanna 
                                                    show tsunahapna
                                                    t "Yes!!!"
                                                    p "Chakra control!"
                                                    $ renpy.transition(dissolve)
                                                    hide tsunade2n
                                                    show tsunade3n
                                                    hide tsunahapna
                                                    show tsunanna
                                                    t "Nice!"
                                                    p "I completely agree."
                                                    p "What now?"
                                                else:
                                                    p "Your boobs are now so small. I must change it!"
                                                    $ tsunapick = 2
                                                    p "Expansion!!!" with hpunch
                                                    hide tsunade1n
                                                    show tsunade2n
                                                    hide tsunanna 
                                                    show tsunahapna
                                                    p "Huh? That was easy!"
                                                    t "You can now concentrate your chakra."
                                                    p "I will try."
                                                    p "Concentrate!"
                                                    $ renpy.transition(dissolve)
                                                    show tsunamil2
                                                    t "Yeah!!!"
                                                    p "So much milk...."
                                                    p "hmmmm...."
                                                    $ renpy.transition(dissolve)
                                                    hide tsunamil2                                                    
                                                    hide tsunahapna
                                                    show tsunanna 
                                                jump tsuboobs1
                                                
                                            "Decrease boob size":
                                                if tsunapick == 1:
                                                    p "Not sure if it is possible but I will try!"
                                                    p "Reduction!!!" with hpunch
                                                    p "..."
                                                    t "Arg...."
                                                    $ renpy.transition(dissolve)
                                                    show tsunamil1
                                                    p "That was unexpected."
                                                    t "...."
                                                    $ renpy.transition(dissolve)
                                                    hide tsunamil1
                                                    p "This is the smallest boobs she can have."
                                                    jump tsuboobs1
                                                elif tsunapick == 2:
                                                    $ tsunapick = 1
                                                    p "Time to make them small again."
                                                    p "Reduction!!!" with hpunch
                                                    t "!!!"
                                                    $ renpy.transition(dissolve)
                                                    hide tsunade2n
                                                    show tsunade1n
                                                    hide tsunanna 
                                                    show tsunanna 
                                                    t "Ouch..."
                                                    p "Look like it work."
                                                    p "But I still think bigger is better."
                                                    jump tsuboobs1
                                                else:
                                                    $ tsunapick = 2
                                                    p "Goodbye huge boobs."
                                                    p "Reduction!!!" with hpunch
                                                    t "Arghhhhhh..."
                                                    $ renpy.transition(dissolve)
                                                    hide tsunade3n
                                                    show tsunade2n
                                                    hide tsunanna 
                                                    show tsunanna 
                                                    p "Size is still nice."
                                                    p "Justt...."
                                                    jump tsuboobs1
                                                jump tsuboobs1
                                                
                                            "Write some motivation notes":
                                                if tsunapick == 1:
                                                    p "What will look good on this small boobs..."
                                                    p "Mabye something like...."
                                                    $ renpy.transition(dissolve)
                                                    show tsunate1
                                                    t "What is this?"
                                                    p "Nothing, just some message."
                                                elif tsunapick == 2:
                                                    p "These boobs are nice, but need some love."
                                                    p "Letter here and letter there."
                                                    $ renpy.transition(dissolve)
                                                    show tsunate2
                                                    t "Milk machine?"
                                                    p "Why not? You still squirting milk.."
                                                    p "Ok, I write something else too..."
                                                elif tsunapick == 3:
                                                    p "Huge boobs need huge message."
                                                    p "Something like save all shinobi!"
                                                    p "or...."
                                                    $ renpy.transition(dissolve)
                                                    show tsunate3
                                                    t "????"
                                                    p "That is good too..."
                                                p "And one more here."
                                                $ renpy.transition(dissolve)    
                                                show tsunate0
                                                t "...."
                                                p "Yes it look good."
                                                t "...."
                                                p "But maybe I should focus on something else."
                                                p "And remove that notes."
                                                $ renpy.transition(dissolve)
                                                hide tsunate0
                                                hide tsunate1
                                                hide tsunate2
                                                hide tsunate3
                                                p "....."
                                                p "Still good."
                                                jump tsuboobs1
                                                
                                            "Slash her":
                                                p "Maybe if I..."
                                                #$ randomnum = renpy.random.randint(1,3) # (randomize between 1 and 3)
                                                if tsunapick == 1:
                                                    with hpunch
                                                    hide tsunanna 
                                                    show tsunasl1
                                                    show tsunasadna
                                                    t "Ouch! What are you doing?"
                                                    p "Calm down now. Just want to test something."
                                                    t "But what?"
                                                elif tsunapick == 2:
                                                    hide tsunanna 
                                                    with hpunch
                                                    show tsunasl2
                                                    show tsunasadna
                                                    t "That really hurt!"
                                                    p "Calm down now. Just want to test something."
                                                    t "Carefully please."
                                                elif tsunapick == 3:
                                                    hide tsunanna 
                                                    with hpunch
                                                    show tsunasl3
                                                    show tsunasadna
                                                    t "What the?"
                                                    p "Calm down now. Just want to test something."
                                                    t "Sure."
                                                p "And one more time."
                                                with hpunch
                                                show tsunasla
                                                t "!!!"
                                                p "Nice right?"
                                                $ renpy.transition(dissolve)
                                                hide tsunasadna
                                                show tsunanna
                                                t "This is no pain for me!"
                                                p "Show me your healing powers now!"
                                                t "No problem."
                                                t "Mitotic Regeneration Jutsu."
                                                $ renpy.transition(dissolve)
                                                hide tsunasla
                                                hide tsunasl1
                                                hide tsunasl2
                                                hide tsunasl3
                                                p "That work nice."
                                                jump tsuboobs1
                                            "Just focus on training":
                                                p "Ok that is enough."
                                                p "We can continue with normal training."
                                                t "Sure..."
                                                scene black with circleirisin               
                                                show nharem0 with circleirisout
                                                "You spend the rest of the day with training."
                                                $ chakra = chakra + 1 
                                                "The sun is already set, what now?"
                                                jump nharem                                                                                           
                                        
                                        
                                        
                                        
                                        
                                "Chakra resistance":
                                        p "Time to train chakra resistance."
                                        p "Show me your boobs now!"
                                        t "Anything you want."
                                        $ renpy.transition(dissolve)
                                        hide tsunade1
                                        hide tsunanna
                                        hide tsunade2
                                        hide tsunanna
                                        hide tsunade3
                                        show ts1
                                        show ts1p1
                                        show ts1a
                                        show ts1clcl
                                        p "Nice. But what now?"
                                        menu tsunatits12:
                                            "Use Chakra whip":
                                                p "Time to try it in the good old way."
                                                p "Tsunade?"
                                                t "Yes?"
                                                p "Take this!" with hpunch
                                                show ts1sl1
                                                t "!!!!"
                                                $ renpy.transition(dissolve)
                                                hide ts1clcl
                                                show ts1clna
                                                t "Why would you?"
                                                p "Silence!"
                                                "Slash!" with hpunch    
                                                show ts1sl2
                                                t "Ouuuuuuuuu...."
                                                p "Nice look like you still feel pain."
                                                $ renpy.transition(dissolve)
                                                hide ts1clna
                                                show ts1sadna
                                                t "Of course I feel pain, why would I......"
                                                "Slash!" with hpunch    
                                                show ts1sl3
                                                t "Argggg...."
                                                p "Yeah.... That look nice on you...."
                                                p "But it is time to try something else."
                                                p "Heal yourself..."
                                                t "Sure..."
                                                $ renpy.transition(dissolve)
                                                hide ts1sadna
                                                show ts1clcl
                                                hide ts1sl1
                                                hide ts1sl2
                                                hide ts1sl3
                                                jump tsunatits12
                                                
                                            "Lightning style":
                                                p "Maybe if I try to attach these things to..."
                                                with fade
                                                p "hmmm"
                                                $ renpy.transition(dissolve)
                                                show ts1ring
                                                t "!!!!"
                                                $ renpy.transition(dissolve)
                                                hide ts1clcl
                                                show ts1clna
                                                show ts1blood
                                                t "That hurts!"
                                                p "Shut up!"
                                                p "You need to obey my order!"
                                                t "OK. But..."
                                                p "Lightning style!"
                                                $ renpy.transition(dissolve)
                                                hide ts1blood
                                                show ts1light
                                                t "Arggggggg!!!"
                                                $ renpy.transition(dissolve)
                                                hide ts1clna
                                                show ts1sadna
                                                p "Do not screw like that."
                                                $ renpy.transition(dissolve)
                                                hide ts1light
                                                p "You can always heal you instantly after this play."
                                                t "Yes but..."
                                                p "Lightning style!"
                                                $ renpy.transition(dissolve)
                                                show ts1light
                                                hide ts1sadna
                                                show ts1clcl
                                                t "Arggg!!!"
                                                p "Yes. That is funny."
                                                p "But maybe I should try something else."
                                                $ renpy.transition(dissolve)
                                                hide ts1light
                                                hide ts1ring
                                                jump tsunatits12
                                                
                                                
                                            "Just fuck her a little":
                                                p "Maybe you should try harder..."
                                                p "Just move your boobs a little..."
                                                $ renpy.transition(dissolve)
                                                hide ts1a
                                                hide ts1p1
                                                show ts1p2
                                                show ts1b
                                                t "Sure..."
                                                $ renpy.transition(dissolve)
                                                hide ts1b
                                                hide ts1p2
                                                show ts1p1
                                                show ts1a
                                                hide ts1clcl
                                                show ts1clna
                                                p "Nice you can continue."
                                                $ renpy.transition(dissolve)
                                                hide ts1a
                                                hide ts1p1
                                                show ts1p2
                                                show ts1b
                                                t "I know you like it."
                                                $ renpy.transition(dissolve)
                                                hide ts1b
                                                hide ts1p2
                                                show ts1touch
                                                show ts1p1
                                                show ts1a
                                                p "Do not be so sassy only because you have large boobs..."
                                                $ renpy.transition(dissolve)
                                                hide ts1a
                                                hide ts1p1
                                                show ts1p2
                                                show ts1b
                                                p "Yes I like it..."
                                                $ renpy.transition(dissolve)
                                                hide ts1b
                                                hide ts1p2
                                                show ts1p1
                                                show ts1a
                                                hide ts1clna
                                                show ts1sadna
                                                t "I know it!"
                                                $ renpy.transition(dissolve)
                                                hide ts1a
                                                hide ts1p1
                                                show ts1p2
                                                show ts1b
                                                t "It is hard to resist my boobs right?"
                                                $ renpy.transition(dissolve)
                                                hide ts1b
                                                hide ts1p2
                                                show ts1p1
                                                show ts1a
                                                hide ts1touch
                                                hide ts1sadna
                                                show ts1clcl
                                                p "Yes, it is. But maybe we can try something else too."
                                                jump tsunatits12
                                            "Cum":
                                                p "I am almost...."
                                                $ renpy.transition(dissolve)
                                                show ts1sp1
                                                p "Take it bich!"
                                                $ renpy.transition(dissolve)
                                                show ts1sp2
                                                hide ts1clcl
                                                show ts1sadna
                                                t "........."
                                                $ renpy.transition(dissolve)
                                                hide ts1sp1
                                                hide ts1sp2
                                                show ts1sp3
                                                p "That one was really good."
                                                p "It feels like......"
                                                $ chakra = chakra + 1 
                                                p "Yes.... I fell stronger now!"
                                                p "Listen Tsunade. I enjoy it today."
                                                t "Come back again to train with me."
                                                p "You can count with that."
                                                scene black with circleirisin  
                                                show nharem0 with circleirisout
                                                jump nharem
                                                
                                    
                                        
                                        
                                        
                                "Chakra endurance":
                                        p "We need to work on my endurance."
                                        t "...."
                                        p "Now it is time to set you in the right position."
                                        t "..."
                                        p "I think, You know what I am talking about..."
                                        $ renpy.transition(dissolve)
                                        hide tsunade1
                                        hide tsunan
                                        hide tsunade2
                                        hide tsunanna
                                        hide tsunade3 
                                        show ts3a
                                        show ts3nna
                                        p "Good... Now we can start."
                                        t "Please be carefull..."
                                        p "Of course I will be careful. But tell me do you like it?"
                                        $ renpy.transition(dissolve)
                                        hide ts3a
                                        hide ts3nna
                                        show ts3p1   
                                        show ts3a
                                        show ts3opna
                                        t "Yesssss..."
                                        p "That is the right answer."
                                        $ renpy.transition(dissolve)
                                        hide ts3a
                                        hide ts3opna
                                        hide ts3p1
                                        show ts3p2
                                        show ts3a                                        
                                        show ts3nna
                                        t "Aaaaa..."
                                        p "And this is only beginning."                                        
                                        t "....."
                                        p "What should I do now?"
                                        menu tsunafuck21:
                                            "Increase her boobs size":
                                                p "I should focus my chakra now."
                                                p "Expansion!!!"
                                                $ renpy.transition(dissolve)
                                                hide ts3a
                                                hide ts3nna
                                                hide ts3p2
                                                show ts3p2
                                                show ts3b
                                                show ts3cl
                                                t "Yeahhh...."
                                                p "That boobs are adorable...."
                                                t "....."
                                                t "Thank you..."
                                                $ renpy.transition(dissolve)
                                                hide ts3b
                                                hide ts3cl
                                                hide ts3p2
                                                show ts3p4
                                                show ts3b
                                                show ts3nna
                                                p "I need to focus more and make them bigger."
                                                t "...."
                                                p "Expansion!"
                                                $ renpy.transition(dissolve)
                                                hide ts3b
                                                hide ts3nna
                                                hide ts3p4
                                                show ts3p2
                                                show ts3c
                                                show ts3nna
                                                t "Argggg..."
                                                p "Yeah. I can do that and fuck you in the same time."
                                                $ renpy.transition(dissolve)
                                                hide ts3c
                                                hide ts3nna
                                                hide ts3p2
                                                show ts3p4
                                                show ts3c
                                                show ts3nna
                                                p "Fuck. It still work..."
                                                $ renpy.transition(dissolve)
                                                hide ts3c
                                                hide ts3nna
                                                hide ts3p4
                                                show ts3p2
                                                show ts3b
                                                show ts3opna
                                                t "Aaaa...."
                                                p "But it is harder to hold them big. Expansion!"
                                                $ renpy.transition(dissolve)
                                                hide ts3b
                                                hide ts3opna
                                                hide ts3p2
                                                show ts3p1
                                                show ts3c
                                                show ts3opna
                                                p "Maybe I should make them small again and try something else."
                                                $ renpy.transition(dissolve)
                                                hide ts3c
                                                hide ts3opna
                                                hide ts3p1
                                                show ts3p2
                                                show ts3b
                                                show ts3cl
                                                p "Release!"
                                                $ renpy.transition(dissolve)
                                                hide ts3b
                                                hide ts3cl
                                                hide ts3p2
                                                show ts3p2
                                                show ts3a
                                                show ts3cl
                                                t "I just like them big."
                                                p "Me to."
                                                $ renpy.transition(dissolve)
                                                hide ts3cl
                                                show ts3nna
                                                p "What now???"                                                
                                                jump tsunafuck21                                                                                         
                                            
                                            "Increase your penis size":
                                                p "Time for some extra size."                                                
                                                $ renpy.transition(dissolve)
                                                hide ts3a
                                                hide ts3nna
                                                hide ts3p2
                                                show ts3p4
                                                show ts3a
                                                show ts3cl
                                                p "Deeper!!!"
                                                p "And...."
                                                with fade
                                                p "Expansion!!!"
                                                $ renpy.transition(dissolve)
                                                hide ts3a
                                                hide ts3cl
                                                hide ts3p4                                                
                                                show ts3a
                                                show ts3opna
                                                show ts3p5
                                                t "Yeah!!!"
                                                p "Exactly..."
                                                $ renpy.transition(dissolve)
                                                hide ts3a
                                                hide ts3opna
                                                hide ts3p5
                                                show ts3p4
                                                show ts3a
                                                show ts3opna
                                                p "And in again!"
                                                $ renpy.transition(dissolve)
                                                hide ts3a
                                                hide ts3opna
                                                hide ts3p4
                                                show ts3a
                                                show ts3opna
                                                show ts3p5
                                                t "More!!!"
                                                p "Maybe I can increase the size it a little."
                                                $ renpy.transition(dissolve)
                                                hide ts3a
                                                hide ts3opna
                                                hide ts3p5                                                
                                                show ts3a
                                                show ts3cl
                                                show ts3p6
                                                t "YEAH!!!!!!!"
                                                p "Great!"
                                                $ renpy.transition(dissolve)
                                                hide ts3a
                                                hide ts3cl
                                                hide ts3p6                                                
                                                show ts3a
                                                show ts3sadna                                                
                                                show ts3p5
                                                p "And I finally feel her belly."
                                                $ renpy.transition(dissolve)
                                                hide ts3a
                                                hide ts3sadna
                                                hide ts3p5
                                                show ts3p4
                                                show ts3a
                                                show ts3sadna
                                                t "Aaaa...."
                                                p "You might really like it..."
                                                $ renpy.transition(dissolve)
                                                hide ts3a
                                                hide ts3sadna
                                                hide ts3p4                                                
                                                show ts3a
                                                show ts3cl
                                                show ts3p5
                                                p "But I like it too...."
                                                $ renpy.transition(dissolve)
                                                hide ts3a
                                                hide ts3cl
                                                hide ts3p5                                                
                                                show ts3a
                                                show ts3cl
                                                show ts3p6
                                                t "My belly will break!"
                                                $ renpy.transition(dissolve)
                                                hide ts3a
                                                hide ts3cl
                                                hide ts3p6                                                
                                                show ts3a
                                                show ts3cl
                                                show ts3p5
                                                p "Maybe we should try to make it more natural."
                                                $ renpy.transition(dissolve)
                                                hide ts3a
                                                hide ts3cl
                                                hide ts3p5   
                                                show ts3p4
                                                show ts3a
                                                show ts3cl
                                                t "...."
                                                $ renpy.transition(dissolve)
                                                hide ts3a
                                                hide ts3cl
                                                hide ts3p4 
                                                show ts3p2
                                                show ts3a
                                                show ts3nna
                                                p "And what now?"   
                                                jump tsunafuck21
                                                
                                                
                                            "Use some toys":
                                                p "Maybe if I use this on you..."
                                                $ renpy.transition(dissolve)
                                                show ts3ring
                                                hide ts3nna
                                                show ts3cl
                                                t "!!!"
                                                p "Yeah that is nice..."
                                                t "It really hurts!"
                                                p "Silence!" with hpunch
                                                show ts3slash1
                                                t "OUCH!!!"
                                                p "That was fun one more!"
                                                "Slash!" with vpunch
                                                show ts3slash2
                                                hide ts3cl
                                                show ts3sadna
                                                t "ArggGG!!!"
                                                p "Do not worry I will give you some power."
                                                $ renpy.transition(dissolve)
                                                show ts3lig
                                                t "!!!"
                                                p "And more!!!"
                                                "Slash!" with vpunch
                                                show ts3slash3
                                                t "Yeah!!!"
                                                p "I know you like it."
                                                p "Lightning style!"
                                                $ renpy.transition(dissolve)
                                                show ts3light
                                                t "Yes!!!!"
                                                p "More!" with hpunch
                                                t "AAAAAA!!!!"
                                                $ renpy.transition(dissolve)
                                                hide ts3sadna
                                                show ts3opna
                                                show ts3milk
                                                p "And more milk."
                                                p "You are just like busty sadistic cow!"
                                                p "..."
                                                p "But I need to train."
                                                p "Heal yourself and put that things out..."
                                                t "...."
                                                $ renpy.transition(dissolve)
                                                hide ts3opna
                                                show ts3nna
                                                t "Sure..."
                                                $ renpy.transition(dissolve)
                                                hide ts3milk
                                                hide ts3light
                                                hide ts3lig
                                                hide ts3slash1
                                                hide ts3slash2
                                                hide ts3slash3
                                                hide ts3ring
                                                jump tsunafuck21
                                                
                                            "Just cum":
                                                p "Yeah, that is amazing!"                                                
                                                $ renpy.transition(dissolve)
                                                hide ts3a
                                                hide ts3nna
                                                hide ts3p2
                                                show ts3p1
                                                show ts3a
                                                show ts3cl
                                                p "I always dream about fucking Tsunade."
                                                $ renpy.transition(dissolve)
                                                hide ts3a
                                                hide ts3cl
                                                hide ts3p1
                                                show ts3p2
                                                show ts3a
                                                show ts3nna
                                                p "More!"
                                                $ renpy.transition(dissolve)
                                                hide ts3a
                                                hide ts3nna
                                                hide ts3p2
                                                show ts3p4
                                                show ts3a
                                                show ts3nna
                                                t "Yes!!!"
                                                $ renpy.transition(dissolve)
                                                hide ts3a
                                                hide ts3nna
                                                hide ts3p4
                                                show ts3p2
                                                show ts3a
                                                show ts3nna
                                                p "Shit, I am already...."
                                                $ renpy.transition(dissolve)
                                                hide ts3a
                                                hide ts3nna
                                                hide ts3p2
                                                show ts3p4
                                                show ts3a
                                                show ts3nna
                                                menu:
                                                    "Cum in":
                                                        $ renpy.transition(dissolve)
                                                        hide ts3a
                                                        hide ts3nna
                                                        hide ts3p4
                                                        show ts3a
                                                        show ts3opna
                                                        show ts3p5
                                                        t "YES!!!!"
                                                        p "!!!" with hpunch
                                                        show ts3spin
                                                        p "WOW!!!"
                                                        $ renpy.transition(dissolve)
                                                        show ts3milk
                                                        t "AAAAAAA...."
                                                        p "...."
                                                        p "Looks like you enjoy it."
                                                        $ renpy.transition(dissolve)
                                                        hide ts3opna
                                                        show ts3nna
                                                        t "That was... I mean that training..."
                                                        p "Yes... Pretty intensive..."
                                                        p "But I need to train a lot to master it."
                                                        t "...."
                                                        t "We can do it tomorrow if you want."
                                                        t "I mean, train together."
                                                        p "Yes I understant. But I need rest now."
                                                        p "See you later."
                                                        $ chakra = chakra + 1 
                                                        scene black with circleirisin  
                                                        show nharem0 with circleirisout
                                                        jump nharem

                                                        
                                                    "Cum out":
                                                        $ renpy.transition(dissolve)
                                                        hide ts3a
                                                        hide ts3nna
                                                        hide ts3p4
                                                        show ts3p2
                                                        show ts3a
                                                        show ts3opna
                                                        p "Take it!!!"
                                                        $ renpy.transition(dissolve)
                                                        hide ts3a
                                                        hide ts3opna
                                                        hide ts3p2
                                                        show ts3p3
                                                        show ts3a
                                                        show ts3opna
                                                        show ts3spout
                                                        p "That one was really good."
                                                        $ renpy.transition(dissolve)
                                                        hide ts3opna
                                                        show ts3nna
                                                        t "Yes, your skills are better now."
                                                        p "Yes... My skills."
                                                        p "But I need to train a lot to master it."
                                                        t "...."
                                                        t "We can do it tomorrow if you want."
                                                        t "I mean, train together."
                                                        p "I really am looking forward to it."
                                                        p "So I will see you tomorrow."
                                                        $ chakra = chakra + 1 
                                                        scene black with circleirisin  
                                                        show nharem0 with circleirisout
                                                        jump nharem
                                                
                                "Chakra release":
                                        p "I want to increase my chakra supply."
                                        p "Understant."
                                        $ renpy.transition(dissolve)
                                        hide tsunan
                                        hide tsunanna
                                        show tsunanna        
                                        hide tsunade1
                                        hide tsunan
                                        hide tsunade2
                                        hide tsunanna
                                        hide tsunade3 
                                        p "Great..."
                                        $ renpy.transition(dissolve)
                                        show ts4a
                                        show ts4op
                                        ti "I am ready. Now you can use my mouth to release all your chakra supply."
                                        $ renpy.transition(dissolve)
                                        show ts4p1
                                        p "Are you sure?"
                                        t "Yeah... Just stick it in!"
                                        $ renpy.transition(dissolve)
                                        hide ts4p1
                                        show ts4p2
                                        p "Oh yeah, it feels so good."
                                        p "I really want to stick it deeper!!!"
                                        $ renpy.transition(dissolve)
                                        hide ts4p2
                                        show ts4p3
                                        t "Mggfhfh...*cough*"
                                        p "Fuck... Just a little...."
                                        $ renpy.transition(dissolve)
                                        hide ts4op
                                        show ts4cl
                                        hide ts4p3
                                        show ts4p4
                                        t "grgghhh...*gag cough*"
                                        p "This is so fucking awesome!!!"
                                        $ renpy.transition(dissolve)
                                        hide ts4p4
                                        show ts4p3
                                        t "chrrrrr... *cough wheeze*"
                                        $ renpy.transition(dissolve)
                                        hide ts4p3
                                        show ts4p2
                                        p "And in!"
                                        $ renpy.transition(dissolve)
                                        hide ts4p2
                                        show ts4p3
                                        p "Yeah!!!"
                                        $ renpy.transition(dissolve)
                                        hide ts4p3
                                        show ts4p4
                                        t "*cough gag*"
                                        $ renpy.transition(dissolve)
                                        hide ts4p4
                                        show ts4p3
                                        p "Hehe... This will be fun..."
                                        $ renpy.transition(dissolve)
                                        hide ts4cl
                                        show ts4op
                                        hide ts4p3
                                        show ts4p2
                                        show ts4text
                                        t "Mhhmmmhh??? *cough*"
                                        $ renpy.transition(dissolve)
                                        hide ts4p2
                                        show ts4p3
                                        p "Looks good right?"
                                        $ renpy.transition(dissolve)
                                        hide ts4p3
                                        show ts4p4
                                        t "Ghhgnm...*gag*"
                                        $ renpy.transition(dissolve)
                                        hide ts4p4
                                        show ts4p3
                                        p "Just a little..."
                                        $ renpy.transition(dissolve)
                                        hide ts4p3
                                        show ts4p2
                                        t "Hmmhh,??? *cough wheeze*"
                                        $ renpy.transition(dissolve)
                                        hide ts4p2
                                        show ts4p3
                                        p "And...."
                                        $ renpy.transition(dissolve)
                                        hide ts4p3
                                        show ts4p4
                                        p "Yeah!!!*splurt*"
                                        $ renpy.transition(dissolve)
                                        hide ts4op
                                        show ts4cl
                                        hide ts4p4
                                        show ts4p4
                                        show ts4p5
                                        t "gghfhgrggg...*gag cough moan drip*"
                                        $ renpy.transition(dissolve)
                                        show ts4p6
                                        p "Awesome!!! *drip*"
                                        t "*cough wheeze*"
                                        p "Are you allright???"
                                        t "ghhgh.... *gag cough*"
                                        p "Yeah, I forgot..."
                                        $ renpy.transition(dissolve)
                                        hide ts4op
                                        hide ts4a
                                        hide ts4p4
                                        hide ts4p5
                                        hide ts4p6
                                        hide ts4text
                                        p "..."
                                        t "*cough swallow*"
                                        $ renpy.transition(dissolve)
                                        show tsunade1n
                                        show tsunahap
                                        t "Mmmm... Tasty..."
                                        p "Yeah... See you later..."
                                        $ chakra = chakra + 1 
                                        scene black with circleirisin  
                                        show nharem0 with circleirisout
                                        jump nharem
                                        
                                "Chakra mixed training":
                                        p "Time to show you some extra fun."
                                        t "I will do anything that you want."
                                        p "I am waiting..."
                                        $ renpy.transition(dissolve)
                                        hide tsunade1
                                        hide tsunan
                                        hide tsunade2
                                        hide tsunanna
                                        hide tsunade3 
                                        show ts2b2
                                        show ts2
                                        show ts2nna
                                        p "Yes that is what I was talking about."
                                        p "Time for fun."
                                        menu tsunalay1:
                                            "Have some fun":
                                                p "Maybe I should play with her a little..."
                                                if tier ==2:
                                                    p "First body."
                                                    $ tier = 1
                                                    $ renpy.transition(dissolve)
                                                    hide ts2a1
                                                    hide ts2a2
                                                    hide ts2b2
                                                    hide ts2nna
                                                    hide ts2
                                                    show ts2b1
                                                    show ts2
                                                    show ts2nna
                                                else:
                                                    p "Body looks fine."
                                                    p "Maybe..."    
                                                    $ renpy.transition(dissolve)
                                                    hide ts2b2
                                                    hide ts2nna
                                                    hide ts2
                                                    show ts2b1
                                                    show ts2
                                                    show ts2nna
                                                    
                                                p "Nice."
                                                p "If I attach this on the nipples.."
                                                $ renpy.transition(dissolve)
                                                show ts2ring
                                                t "...."
                                                t "Looking good..."
                                                p "And put this in..."
                                                $ renpy.transition(dissolve)
                                                show ts2an
                                                hide ts2nna
                                                show ts2downa
                                                t "But..."
                                                p "Com on."
                                                p "I know you like it!"
                                                $ renpy.transition(dissolve)
                                                show ts2shy
                                                show ts2clip
                                                t "Arggg... Yes but..."
                                                p "So do not be so embarrassed..."
                                                p "Your body is beautiful and should be played with it."
                                                t "Sure..."
                                                p "Lightning style..."
                                                $ renpy.transition(dissolve)
                                                show ts2lig
                                                hide ts2downa
                                                show ts2hapna
                                                t "AAAaaaaaaa!!!"
                                                p "Do you want more?"
                                                t "...."
                                                t "YES!"
                                                p "If you really want it..."
                                                t "Yes PLEASE!"
                                                p "Lightning style 5000 volts!"
                                                $ renpy.transition(dissolve)
                                                show ts2light
                                                hide ts2hapna
                                                show ts2cl
                                                t "AAAAAAWwwwwwww...."
                                                $ renpy.transition(dissolve)
                                                hide ts2light
                                                p "Heh..."
                                                $ renpy.transition(dissolve)
                                                show ts2light
                                                t "aaaaaa...."
                                                p "If other women react like you..."
                                                p "But time for some change..."
                                                $ renpy.transition(dissolve)
                                                hide ts2light
                                                hide ts2lig
                                                hide ts2cl
                                                hide ts2clip
                                                hide ts2ring
                                                hide ts2an
                                                show ts2nna
                                                jump tsunalay1
                                            "Change boob size":
                                                if tier == 1:
                                                    $ tier = 2
                                                    p "Time to make them bigger."
                                                    p "Expansion!"
                                                    if everystats == 1:
                                                        $ renpy.transition(dissolve)
                                                        hide ts2b2
                                                        hide ts2
                                                        hide ts2nna
                                                        show ts2a2
                                                        show ts2
                                                        show ts2nna
                                                        t "Yes!!!!"
                                                        
                                                    else:
                                                        $ renpy.transition(dissolve)
                                                        hide ts2b1
                                                        hide ts2
                                                        hide ts2nna
                                                        show ts2a1
                                                        show ts2
                                                        show ts2nna
                                                        t "Yes!!!!"
                                                    p "How she looks better?"
                                                    menu:
                                                        "Dressed":
                                                            p "..."
                                                            $ renpy.transition(dissolve)
                                                            hide ts2a1
                                                            hide ts2
                                                            hide ts2nna
                                                            show ts2a2
                                                            show ts2
                                                            show ts2nna
                                                            p "Ok."
                                                        "Undressed":
                                                            p "Show me boobs"
                                                            $ renpy.transition(dissolve)
                                                            hide ts2a2
                                                            hide ts2
                                                            hide ts2nna
                                                            show ts2a1
                                                            show ts2
                                                            show ts2nna
                                                            p "Nice."
                                                        
                                                    jump tsunalay1
                                                    
                                                else:
                                                    $ tier = 1
                                                    p "Maybe they should be smaller."
                                                    p "Chakra release!"
                                                    if everystats == 1:
                                                        $ renpy.transition(dissolve)
                                                        hide ts2a2
                                                        hide ts2
                                                        hide ts2nna
                                                        show ts2b2
                                                        show ts2
                                                        show ts2nna
                                                        p "It works!"
                                                        
                                                    else:
                                                        $ renpy.transition(dissolve)
                                                        hide ts2a1
                                                        hide ts2
                                                        hide ts2nna
                                                        show ts2b1
                                                        show ts2
                                                        show ts2nna
                                                        p "It works!"
                                                    p "How she looks better?"
                                                    menu:
                                                        "Dressed":
                                                            p "..."
                                                            $ renpy.transition(dissolve)
                                                            hide ts2b1
                                                            hide ts2
                                                            hide ts2nna
                                                            show ts2b2
                                                            show ts2
                                                            show ts2nna
                                                            p "Ok."
                                                        "Undressed":
                                                            p "Show me boobs"
                                                            $ renpy.transition(dissolve)
                                                            hide ts2b2
                                                            hide ts2
                                                            hide ts2nna
                                                            show ts2b1
                                                            show ts2
                                                            show ts2nna
                                                            p "Nice."
                                                        
                                                    jump tsunalay1
                                                     
                                            "Fuck her":
                                                p "Maybe I should stop playing around."
                                                p "I think you know what I want to do now."
                                                $ renpy.transition(dissolve)
                                                show ts2p1
                                                t "Finally..."                                                
                                                $ renpy.transition(dissolve)
                                                hide ts2p1
                                                show ts2shy
                                                hide ts2nna
                                                show ts2cl
                                                show ts2p2
                                                t "Mmmmmm..."
                                                $ renpy.transition(dissolve)
                                                hide ts2p2
                                                show ts2p3
                                                p "Yep just like I like it."
                                                $ renpy.transition(dissolve)
                                                hide ts2p3
                                                show ts2p2
                                                t "More..."
                                                $ renpy.transition(dissolve)
                                                hide ts2p2
                                                show ts2p3
                                                p "This is so..."
                                                $ renpy.transition(dissolve)
                                                hide ts2p3
                                                show ts2p2
                                                p "Good to be inside..."
                                                $ renpy.transition(dissolve)
                                                hide ts2p2
                                                show ts2p3
                                                t "This is....."
                                                $ renpy.transition(dissolve)
                                                hide ts2p3
                                                show ts2p2
                                                t "Yaiks...."
                                                $ renpy.transition(dissolve)
                                                hide ts2p2
                                                show ts2p3
                                                hide ts2cl
                                                show ts2hapna
                                                t "Just..."
                                                $ renpy.transition(dissolve)
                                                hide ts2p3
                                                show ts2p2
                                                p "So warm inside..."
                                                $ renpy.transition(dissolve)
                                                hide ts2p2
                                                show ts2p3
                                                p "But I am not sure if this is..."
                                                $ renpy.transition(dissolve)
                                                hide ts2p3
                                                show ts2p2
                                                p "I need a rest or..."
                                                menu:
                                                    "Just cum":
                                                        p "I will cum...."
                                                        $ renpy.transition(dissolve)
                                                        hide ts2p2
                                                        show ts2p3
                                                        p "Take it bitch!"
                                                        $ renpy.transition(dissolve)
                                                        show ts2spin
                                                        p "YEAH!"
                                                        t "So much sperm..."
                                                        $ renpy.transition(dissolve)
                                                        show ts2spin2
                                                        t "Nice...."
                                                        p "Wow...."
                                                        with fade
                                                        p "I think every sex is just better..."
                                                        t "Sex?"
                                                        p "I mean training, of course..."
                                                        p "And I feel stronger again."
                                                        $ chakra = chakra + 1 
                                                        p "Not sure how it is possible, but my chakra control is just better now."
                                                        t "Of course it is..."
                                                        $ renpy.transition(dissolve)
                                                        hide ts2hapna
                                                        show ts2nna 
                                                        t "Actually, it is the basics of the training."
                                                        t "If you do something with passion the result is always better."
                                                        scene black with circleirisin  
                                                        show nharem0 with circleirisout
                                                        jump nharem
                                                    "Try something else":
                                                        p "Just want to do something else."
                                                        $ renpy.transition(dissolve)
                                                        hide ts2p2
                                                        show ts2p1
                                                        p "Before I cum on you."
                                                        $ renpy.transition(dissolve)
                                                        hide ts2p1
                                                        hide ts2hapna
                                                        show ts2nna                                                
                                                        jump tsunalay1
                                                        
                                            
                                            "Dick Expansion":
                                                p "Maybe I should stop playing around."
                                                p "I think you know what I want to do now."
                                                $ renpy.transition(dissolve)
                                                show ts2p1
                                                t "Finally..."                                                
                                                $ renpy.transition(dissolve)
                                                hide ts2p1
                                                show ts2shy
                                                hide ts2nna
                                                show ts2cl
                                                show ts2p2
                                                t "Mmmmmm..."
                                                $ renpy.transition(dissolve)
                                                hide ts2p2
                                                show ts2p3
                                                p "Yep just like I like it."
                                                $ renpy.transition(dissolve)
                                                hide ts2p3
                                                show ts2p2
                                                t "More..."
                                                $ renpy.transition(dissolve)
                                                hide ts2p2
                                                show ts2p1
                                                p "I want to give you more..."
                                                p "Maybe... some changes or...."
                                                if tier == 2:
                                                    $ renpy.transition(dissolve)
                                                    hide ts2a1
                                                    hide ts2a2
                                                    hide ts2
                                                    hide ts2cl
                                                    show ts2b1
                                                    show ts2
                                                    show ts2cl
                                                    p "And now..."
                                                p "Expansion!"
                                                $ renpy.transition(dissolve)
                                                hide ts2p1
                                                show ts2pb1
                                                hide ts2cl
                                                show ts2downa
                                                t "It looks huge now!"
                                                p "Yeah. Are you ready?"
                                                $ renpy.transition(dissolve)
                                                hide ts2pb1
                                                show ts2pb2
                                                t "Just do it slowly..."
                                                p "Sure... but..."
                                                $ renpy.transition(dissolve)
                                                hide ts2pb2
                                                show ts2pb3
                                                show ts2cl
                                                hide ts2downa
                                                t "AARGHHHHH!!!!!"
                                                t "This is so good!!!!"
                                                $ renpy.transition(dissolve)
                                                hide ts2pb3
                                                show ts2pb2
                                                p "I just wonder how it fit in?"
                                                $ renpy.transition(dissolve)
                                                hide ts2pb2
                                                show ts2pb3
                                                t "Aaaaaaa...."
                                                $ renpy.transition(dissolve)
                                                hide ts2pb3
                                                show ts2pb2
                                                p "But you do not care right?"
                                                $ renpy.transition(dissolve)
                                                hide ts2pb2
                                                show ts2pb3
                                                hide ts2cl
                                                show ts2nna
                                                t "Grrggg....Just fuck me hard!"
                                                $ renpy.transition(dissolve)
                                                hide ts2pb3
                                                show ts2pb2
                                                p "Sure..."
                                                $ renpy.transition(dissolve)
                                                hide ts2pb2
                                                show ts2pb3
                                                t "Oooooo....."
                                                $ renpy.transition(dissolve)
                                                hide ts2pb3
                                                show ts2pb2
                                                hide ts2nna
                                                show ts2hapna
                                                t "Awesome..."
                                                $ renpy.transition(dissolve)
                                                hide ts2pb2
                                                show ts2pb3
                                                p "Look like you enjoy it more than me..."
                                                $ renpy.transition(dissolve)
                                                hide ts2pb3
                                                show ts2pb2
                                                t "Aaaaaaaaaaa."
                                                $ renpy.transition(dissolve)
                                                hide ts2pb2
                                                show ts2pb3
                                                p "Fuck this is just too good..."
                                                $ renpy.transition(dissolve)
                                                hide ts2pb3
                                                show ts2pb2
                                                p "If I do not stop soon I will..."
                                                $ renpy.transition(dissolve)
                                                hide ts2pb2
                                                show ts2spout
                                                show ts2pb1
                                                p "YEAH!!!!"
                                                with fade
                                                t "Aaaaaaaaa...."
                                                $ renpy.transition(dissolve)
                                                show ts2spout2
                                                hide ts2hapna
                                                show ts2cl
                                                t "More....."
                                                with fade
                                                p "huh...."
                                                p "Just.... I think this training is really something."
                                                $ renpy.transition(dissolve)
                                                hide ts2pb1
                                                t "It looks like your chakra control is better now."
                                                $ chakra = chakra + 1 
                                                p "Yes, it is weird how fast it can work."
                                                p "I mean normal training took twice more time."
                                                p "But this is so fast and good...."
                                                p "Because I just love it..."
                                                t "......"
                                                p "I am really excited about our next training."
                                                scene black with circleirisin  
                                                show nharem0 with circleirisout
                                                jump nharem
                                    
               
                        
                                            
                            


                    
                    
   
                    
                    
                    
                    
                    
                    
                
            else:
                "Tsunade is still in the Konoha."
                scene black with circleirisin               
                show dharem0 with circleirisout
                jump dharem 
            
        "Go back to the map":
            scene black with circleirisin               
            show dharem0 with circleirisout
            jump dharem  



































################################ dharemforest1
################################ dharemforest1
################################ dharemforest1
################################ dharemforest1
################################ dharemforest1


label dharemforest1:
    scene dharemforest 
    menu:
        "Look around":
            "You look around the forest... And didn't find anything useful..."
            scene black with circleirisin               
            show nrock0 with circleirisout
            jump dharem   
            
        "Call Tenten":
            if tenslave <=4:
                "You can find Tenten in the hidden rock village."
                scene black with circleirisin               
                show nrock0 with circleirisout
                jump dharem 
                
                
            else:
                            $ renpy.transition(dissolve)
                            show ten0a
                            show ten0nok
                            p "So what now?"
                            menu:
                                "Play with her body":
                                    p "Is time to play with your body a little."
                                    p "Now, Strip!"
                                    $ renpy.transition(dissolve)
                                    hide ten0nok
                                    hide ten0a
                                    show ten0c
                                    show ten0nok
                                    p "Good... But what about this?"
                                    $ renpy.transition(dissolve)
                                    show ten0text
                                    te "..."
                                    p "Hehe..."
                                    p "Water style!"
                                    $ renpy.transition(dissolve)
                                    show ten0w1
                                    te "..."
                                    p "Water explosion! *splash*"
                                    $ renpy.transition(dissolve)
                                    show ten0w2
                                    te "mhmmmm....*moan*" 
                                    p "Better right?"
                                    p "Water dragoon! *splash*"
                                    $ renpy.transition(dissolve)
                                    show ten0w3
                                    hide ten0nok
                                    show ten0nop
                                    p "Look at you now... Time to show you my cock..."
                                    p "Your mission is now to make me cum before you ok?"
                                    te "Sure... *fap fap*"
                                    p "Let's start now... *clamp*"
                                    $ renpy.transition(dissolve)
                                    show ten0l1
                                    te "Ouch...."
                                    p "Hehe. You are loosing already... *clamp*"
                                    $ renpy.transition(dissolve)
                                    show ten0l2
                                    hide ten0nok
                                    show ten0nop
                                    te "Ahhhh...*pain fap*"
                                    p "SNice... But try you must be faster to make me cum first."
                                    te "*fap fap*"
                                    p " Yeah... This is beter... Lightning tingling!"
                                    $ renpy.transition(dissolve)
                                    show ten0l3
                                    te "Ahh... *moan fap fap*"
                                    p "Fuck, More power!"
                                    $ renpy.transition(dissolve)
                                    show ten0l4
                                    hide ten0nop
                                    show ten0nshock
                                    te "Arggg!!! *moan fap fap*"
                                    p "Yeah.... Full release!"
                                    $ renpy.transition(dissolve)
                                    show ten0l5
                                    te "Ahhhh!!!! *heavy moaning fap*"
                                    p "Yeah!"
                                    $ renpy.transition(dissolve)
                                    hide ten0nshock
                                    show ten0norg
                                    show ten0m1
                                    te "Yess!!! *heavy moaning fap fap fap*"
                                    $ renpy.transition(dissolve)
                                    show ten0m2
                                    p "Yeah... This is good..."
                                    te "Ahhh....*moan fap fap fap fap*"
                                    $ renpy.transition(dissolve)
                                    hide ten0l4
                                    hide ten0l5
                                    show ten0sp1
                                    p "Fuck!!! *splurt*"
                                    $ renpy.transition(dissolve)
                                    show ten0sp2
                                    hide ten0l3
                                    te "Mmm...*moan fap fap*"
                                    p "Good girl... You can stop that now."
                                    te "....*mumble*"
                                    p "It was really good but now is time to clean youreslf..."
                                    te "Ok..."                                    
                                    $ renpy.transition(dissolve)
                                    hide ten0l1
                                    hide ten0l2
                                    hide ten0norg
                                    hide ten0c
                                    hide ten0m2
                                    hide ten0m1
                                    hide ten0w1
                                    hide ten0w2
                                    hide ten0w3
                                    hide ten0text
                                    hide ten0sp1
                                    hide ten0sp2
                                    p "Wow that was good..."
                                    with fade
                                    "After some time."
                                    $ renpy.transition(dissolve)
                                    show ten0a
                                    show ten0nok
                                    p "You are looking good now."
                                    p "Just that boobs are... Hmm who cares bye..."
                                    scene black with circleirisin  
                                    show nharem0 with circleirisout
                                    jump nharem
                                
                                "Blowjob":
                                        p "Is time to give me a nice blowjob."
                                        p "Now, Strip and start to suck my cock!"
                                        te "Sure..."
                                        $ renpy.transition(dissolve)
                                        hide ten0nok
                                        hide ten0a
                                        show ten2a
                                        show ten2sad
                                        show ten2bl0
                                        p "Yeah... This is nice... Suck it!"
                                        $ renpy.transition(dissolve)
                                        hide ten2bl0
                                        show ten2bl1
                                        p "Good girl."
                                        $ renpy.transition(dissolve)
                                        hide ten2bl1
                                        show ten2bl2
                                        p "Yeah!"
                                        $ renpy.transition(dissolve)
                                        hide ten2bl2
                                        show ten2bl3
                                        te "Mgmmh..*mumble*"
                                        $ renpy.transition(dissolve)
                                        hide ten2bl3
                                        show ten2bl2
                                        p "What? You want more?"
                                        $ renpy.transition(dissolve)
                                        hide ten2bl2
                                        show ten2bl1
                                        te "Mgmgmgm... *gag cough*"
                                        $ renpy.transition(dissolve)
                                        hide ten2bl1
                                        show ten2bl2
                                        p "Ok. Kage bunshin no jutsu!"
                                        $ renpy.transition(dissolve)
                                        hide ten2sad
                                        show ten2back
                                        hide ten2bl2
                                        show ten2bl3                                        
                                        show ten2p1
                                        te "Mmmmm...*moan cough*"
                                        $ renpy.transition(dissolve)
                                        hide ten2bl3
                                        show ten2bl2
                                        p "Nice right?"
                                        $ renpy.transition(dissolve)
                                        hide ten2bl2
                                        show ten2bl1
                                        p "And now..."
                                        menu:
                                            "Just fuck":
                                                p "I will fuck your pussy..."
                                                $ renpy.transition(dissolve)
                                                hide ten2bl1
                                                show ten2bl2
                                                hide ten2p1
                                                show ten2p2
                                                te "Ahhfhgh...*moan mumble*"
                                                $ renpy.transition(dissolve)
                                                hide ten2bl2
                                                show ten2bl3
                                                hide ten2p2
                                                show ten2p3
                                                p "Yeah..."
                                                $ renpy.transition(dissolve)
                                                hide ten2back
                                                show ten2f
                                                hide ten2bl3
                                                show ten2bl2
                                                hide ten2p3
                                                show ten2p4
                                                p "I want to try this too..."
                                                $ renpy.transition(dissolve)
                                                hide ten2bl2
                                                show ten2bl1
                                                hide ten2p4
                                                show ten2p3
                                                p "Hehe..."
                                                $ renpy.transition(dissolve)
                                                hide ten2bl1
                                                show ten2bl2
                                                hide ten2p3
                                                show ten2p2
                                                te "*mumble moan gag*"
                                                $ renpy.transition(dissolve)
                                                hide ten2bl2
                                                show ten2bl3
                                                hide ten2p2
                                                show ten2p3
                                                p "What? Is it too much for you?"
                                                $ renpy.transition(dissolve)
                                                hide ten2f
                                                show ten2sad
                                                hide ten2bl3
                                                show ten2bl2
                                                hide ten2p2
                                                show ten2p3
                                                te "Mmhgmmhm... *gag cough moan*"
                                                $ renpy.transition(dissolve)
                                                hide ten2bl2
                                                show ten2bl1
                                                hide ten2p3
                                                show ten2p4
                                                p "Yeah.. I feel it same!"
                                                $ renpy.transition(dissolve)
                                                hide ten2bl1
                                                show ten2bl2
                                                hide ten2p4
                                                show ten2p3
                                                p "Shit!!!"
                                                $ renpy.transition(dissolve)
                                                hide ten2bl2
                                                show ten2bl3
                                                hide ten2p3
                                                show ten2p2
                                                p "Drink it all! *splurt*"
                                                $ renpy.transition(dissolve)
                                                $ renpy.transition(dissolve)
                                                hide ten2sad
                                                show ten2org
                                                hide ten2bl3
                                                show ten2bl3
                                                show ten2bl4
                                                hide ten2p2
                                                show ten2p3
                                                te "Agghghgfh *gag cough slurp moan*"
                                                $ renpy.transition(dissolve)
                                                show ten2bl5
                                                hide ten2p3
                                                show ten2p4
                                                p "Yeah!"
                                                $ renpy.transition(dissolve)
                                                hide ten2p4
                                                show ten2p3
                                                te "*cough slurp moan*"
                                                $ renpy.transition(dissolve)
                                                hide ten2p3
                                                show ten2p2
                                                p "Shit this is amazing! *splurt*"
                                                $ renpy.transition(dissolve)
                                                hide ten2p2
                                                show ten2p1
                                                show ten2p5
                                                te "*drip cough*"
                                                $ renpy.transition(dissolve)
                                                show ten2p6
                                                p "Yeah...."
                                                te "*slurp cough drip*"
                                                p "Hehe... It was fun right?"
                                                te "*gag cough slurp*"
                                                p "Sure... I will take it out now..."
                                                $ renpy.transition(dissolve)
                                                hide ten2bl3
                                                te "Ahhhhh.. *deep inhale*"
                                                p "But you need to drink it all now..."
                                                te "Sure.... *slurp*"
                                                $ renpy.transition(dissolve)
                                                hide ten2p1
                                                hide ten2p5
                                                hide ten2p6
                                                hide ten2bl4
                                                hide ten2bl5
                                                hide ten2org
                                                hide ten2text
                                                hide ten2a
                                                p "It looks like you are really enjoying it."
                                                te "*slurp drink*"
                                                p "Now you can dress..."
                                                $ renpy.transition(dissolve)
                                                show ten0a
                                                show ten0nok
                                                p "Good girl..."
                                                p "I wonder if you like it...."
                                                scene black with circleirisin                   
                                                show nharem0 with circleirisout
                                                jump nharem
                                                
                                            "Boob expansion":
                                                    p "I want to make your boobs bigger!"
                                                    te "??? *mumble*"
                                                    p "Expansion scroll activation!"
                                                    $ renpy.transition(dissolve)
                                                    hide ten2bl1
                                                    hide ten2p1
                                                    hide ten2back
                                                    hide ten2a
                                                    show ten2b
                                                    show ten2back
                                                    show ten2bl2                                                    
                                                    show ten2p2
                                                    p "Nice!"
                                                    $ renpy.transition(dissolve)
                                                    hide ten2bl1
                                                    show ten2bl2
                                                    hide ten2p1
                                                    show ten2p2
                                                    te "Ahhfhgh...*moan mumble*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten2bl2
                                                    show ten2bl3
                                                    hide ten2p2
                                                    show ten2p3
                                                    p "Time to fuck you..."
                                                    $ renpy.transition(dissolve)
                                                    hide ten2back
                                                    show ten2f
                                                    hide ten2bl3
                                                    show ten2bl2
                                                    hide ten2p3
                                                    show ten2p4
                                                    p "And maybe try this too..."
                                                    $ renpy.transition(dissolve)
                                                    hide ten2bl2
                                                    show ten2bl1
                                                    hide ten2p4
                                                    show ten2p3
                                                    show ten2text
                                                    p "Hehe..."
                                                    $ renpy.transition(dissolve)
                                                    hide ten2bl1
                                                    show ten2bl2
                                                    hide ten2p3
                                                    show ten2p2
                                                    te "*mumble moan gag*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten2bl2
                                                    show ten2bl3
                                                    hide ten2p2
                                                    show ten2p3
                                                    p "What? Is it too much for you?"
                                                    $ renpy.transition(dissolve)
                                                    hide ten2f
                                                    show ten2sad
                                                    hide ten2bl3
                                                    show ten2bl2
                                                    hide ten2p2
                                                    show ten2p3
                                                    te "Mmhgmmhm... *gag cough moan*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten2bl2
                                                    show ten2bl1
                                                    hide ten2p3
                                                    show ten2p4
                                                    p "Yeah.. I feel it same!"
                                                    $ renpy.transition(dissolve)
                                                    hide ten2bl1
                                                    show ten2bl2
                                                    hide ten2p4
                                                    show ten2p3
                                                    p "Shit!!!"
                                                    $ renpy.transition(dissolve)
                                                    hide ten2bl2
                                                    show ten2bl3
                                                    hide ten2p3
                                                    show ten2p2
                                                    p "Drink it all! *splurt*"
                                                    $ renpy.transition(dissolve)
                                                    $ renpy.transition(dissolve)
                                                    hide ten2sad
                                                    show ten2org
                                                    hide ten2bl3
                                                    show ten2bl3
                                                    show ten2bl4
                                                    hide ten2p2
                                                    show ten2p3
                                                    te "Agghghgfh *gag cough slurp moan*"
                                                    $ renpy.transition(dissolve)
                                                    show ten2bl5
                                                    hide ten2p3
                                                    show ten2p4
                                                    p "Yeah!"
                                                    $ renpy.transition(dissolve)
                                                    hide ten2p4
                                                    show ten2p3
                                                    te "*cough slurp moan*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten2p3
                                                    show ten2p2
                                                    p "Shit this is amazing! *splurt*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten2p2
                                                    show ten2p1
                                                    show ten2p5
                                                    te "*drip cough*"
                                                    $ renpy.transition(dissolve)
                                                    show ten2p6
                                                    p "Yeah...."
                                                    te "*slurp cough drip*"
                                                    p "Hehe... It was fun right?"
                                                    te "*gag cough slurp*"
                                                    p "Sure... I will take it out now..."
                                                    $ renpy.transition(dissolve)
                                                    hide ten2bl3
                                                    te "Ahhhhh.. *deep inhale*"
                                                    p "But you need to drink it all now..."
                                                    te "Sure.... *slurp*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten2p1
                                                    hide ten2p5
                                                    hide ten2p6
                                                    hide ten2bl4
                                                    hide ten2bl5
                                                    hide ten2org
                                                    hide ten2text
                                                    hide ten2a
                                                    hide ten2b
                                                    p "It looks like you are really enjoying it."
                                                    te "*slurp drink*"
                                                    p "Now you can dress..."
                                                    $ renpy.transition(dissolve)
                                                    show ten0a
                                                    show ten0nok
                                                    p "Good girl."
                                                    p "Time to go home..."
                                                    scene black with circleirisin                   
                                                    show nharem0 with circleirisout
                                                    jump nharem
                                                
                                                
                                            "Titfuck":
                                                    p "I want to fuck your tits!"
                                                    te "ghmgmmm *mumble*"
                                                    p "Expansion scroll activation!"
                                                    $ renpy.transition(dissolve)
                                                    hide ten2bl1
                                                    hide ten2p1
                                                    hide ten2back
                                                    hide ten2a
                                                    show ten2b
                                                    show ten2back
                                                    show ten2bl0                                                    
                                                    show ten2p2
                                                    p "Nice ... But I need them bigger for titfuck!"
                                                    p "Expansion scroll next level!"
                                                    $ renpy.transition(dissolve)
                                                    hide ten2back
                                                    hide ten2b
                                                    show ten2c
                                                    show ten2f
                                                    hide ten2p1
                                                    show ten2p2
                                                    te "Ahhfhgh...*moan mumble pain*"
                                                    p "Time to fuck that big boobs!"
                                                    $ renpy.transition(dissolve)
                                                    hide ten2bl0
                                                    show ten2tf1
                                                    hide ten2p2
                                                    show ten2p3
                                                    p "Yeah..."
                                                    $ renpy.transition(dissolve)
                                                    hide ten2f
                                                    show ten2sad
                                                    hide ten2tf1
                                                    show ten2tf2
                                                    hide ten2p3
                                                    show ten2p4
                                                    p "Good. *slap*" with hpunch
                                                    $ renpy.transition(dissolve)
                                                    hide ten2tf2
                                                    show ten2tf3
                                                    hide ten2p4
                                                    show ten2p3
                                                    show ten2h1
                                                    te "Ahhh!! *moan*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten2tf3
                                                    show ten2tf4
                                                    hide ten2p3
                                                    show ten2p2
                                                    p "Nice !!! *slap*" with hpunch
                                                    $ renpy.transition(dissolve)
                                                    hide ten2tf4
                                                    show ten2tf3
                                                    hide ten2p2
                                                    show ten2p3
                                                    show ten2h2
                                                    p "You like it right?"
                                                    $ renpy.transition(dissolve)
                                                    hide ten2sad
                                                    show ten2back
                                                    hide ten2tf3
                                                    show ten2tf2
                                                    hide ten2p2
                                                    show ten2p3
                                                    te "YESSSSS!!! *heavy moaning*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten2tf2
                                                    show ten2tf3
                                                    hide ten2p3
                                                    show ten2p4
                                                    p "Yeah.. I feel it same! *slap*" with hpunch
                                                    $ renpy.transition(dissolve)
                                                    hide ten2tf3
                                                    show ten2tf4
                                                    hide ten2p4
                                                    show ten2p3
                                                    show ten2h2
                                                    p "Shit!!!"
                                                    $ renpy.transition(dissolve)
                                                    hide ten2tf4
                                                    show ten2tf3
                                                    hide ten2p3
                                                    show ten2p2
                                                    p "FUCK! So good!"
                                                    $ renpy.transition(dissolve)
                                                    hide ten2back
                                                    show ten2org
                                                    hide ten2tf4
                                                    show ten2tf3
                                                    hide ten2p2
                                                    show ten2p1
                                                    te "Agghghgfh *Heavy moaning*"
                                                    $ renpy.transition(dissolve)
                                                    show ten2p5
                                                    hide ten2tf3
                                                    show ten2tf2
                                                    p "Yeah! *splurt*"
                                                    $ renpy.transition(dissolve)
                                                    show ten2p5
                                                    hide ten2tf2
                                                    show ten2tf3
                                                    te "Ahhhh...*Heavy moaning*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten2tf3
                                                    show ten2tf4
                                                    p "Shit this is amazing! *splurt*"
                                                    $ renpy.transition(dissolve)
                                                    show ten2tf5                                                    
                                                    te "ahhhh... *drip moan*"
                                                    $ renpy.transition(dissolve)
                                                    show ten2tf6
                                                    p "Yeah...."
                                                    $ renpy.transition(dissolve)
                                                    show ten2tf7
                                                    te "ahhhh... *drip moan*"
                                                    p "Hehe... Big boobs are really something."
                                                    te "Mmmmm.... *moan*"
                                                    p "But now is time to clean you and cancel that expansion..."
                                                    te "Sure.... *slurp*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten2p1
                                                    hide ten2p5
                                                    hide ten2p6
                                                    hide ten2bl4
                                                    hide ten2bl5
                                                    hide ten2org
                                                    hide ten2text
                                                    hide ten2a
                                                    hide ten2c
                                                    hide ten2h1
                                                    hide ten2h2
                                                    hide ten2h3
                                                    hide ten2tf4 
                                                    hide ten2tf5
                                                    hide ten2tf6
                                                    hide ten2tf7
                                                    p "It looks like you are really enjoying it."
                                                    te "*slurp drink*"
                                                    p "Now you can dress..."
                                                    $ renpy.transition(dissolve)
                                                    show ten0a
                                                    show ten0nok
                                                    p "Good girl..."
                                                    p "See you later...."
                                                    scene black with circleirisin                   
                                                    show nharem0 with circleirisout
                                                    jump nharem
                                
                                
                                
                                
                                "Kage bunshin":
                                        p "Now is time for some Kage Bunshin tricks."
                                        te "Mmmm...*mumble*"
                                        p "I just need to pick a right position. Now you can strip!"
                                        te "Sure..."
                                        $ renpy.transition(dissolve)
                                        hide ten0nok
                                        hide ten0a
                                        p "Kage Bunshin no jutsu!"
                                        p "Yeah! That is good!"
                                        $ renpy.transition(dissolve)
                                        show ten1a
                                        show ten1front
                                        show ten1bl1
                                        show ten1f1
                                        show ten1h1
                                        te "Mgmmhgmhm... *mumble*"
                                        p "Yeah... This is nice... I will fuck you hard!"
                                        $ renpy.transition(dissolve)
                                        hide ten1bl1
                                        show ten1bl2
                                        hide ten1f1
                                        show ten1f2
                                        p "Amazing pussy..."
                                        $ renpy.transition(dissolve)
                                        hide ten1f1
                                        show ten1cl
                                        hide ten1bl2
                                        show ten1bl3
                                        hide ten1f2
                                        show ten1f3
                                        p "And mouth pussy too..."
                                        $ renpy.transition(dissolve)
                                        hide ten1bl3
                                        show ten1bl2
                                        hide ten1f3
                                        show ten1f4
                                        te "*cough mumble*"
                                        $ renpy.transition(dissolve)
                                        hide ten1bl2
                                        show ten1bl1
                                        hide ten1f4
                                        show ten1f3
                                        p "But these boobs look smaller..."
                                        $ renpy.transition(dissolve)
                                        hide ten1cl
                                        show ten1back
                                        hide ten1bl1
                                        show ten1bl2
                                        hide ten1f3
                                        show ten1f2
                                        te "Mhmmh??? *cough mumble*"
                                        menu tenn221:
                                            "Just cum":
                                                p "It is fine right now."
                                                $ renpy.transition(dissolve)
                                                hide ten1bl2
                                                show ten1bl3
                                                hide ten1f2
                                                show ten1f3
                                                te "Mgmmgm..*moan cough*"
                                                $ renpy.transition(dissolve)
                                                hide ten1bl3
                                                show ten1bl2
                                                hide ten1f2
                                                show ten1f3
                                                p "And too hot right now!"
                                                $ renpy.transition(dissolve)
                                                hide ten1bl2
                                                show ten1bl1
                                                hide ten1f3
                                                show ten1f4
                                                p "More!!!"
                                                $ renpy.transition(dissolve)
                                                hide ten1back
                                                show ten1cl
                                                hide ten1bl1
                                                show ten1bl2
                                                hide ten1f4
                                                show ten1f3
                                                p "Shit!!!"
                                                $ renpy.transition(dissolve)
                                                hide ten1bl2
                                                show ten1bl3
                                                hide ten1f3
                                                show ten1f2
                                                p "Yeah! *splurt*"
                                                $ renpy.transition(dissolve)
                                                show ten1bl4
                                                hide ten1f2
                                                show ten1f1
                                                te "*gag cough slurp*"
                                                $ renpy.transition(dissolve)
                                                show ten1bl5
                                                show ten1f7
                                                p "Shit!!! *splurt*"
                                                $ renpy.transition(dissolve)
                                                show ten1f8
                                                p "And more!!!"
                                                $ renpy.transition(dissolve)
                                                hide ten1f1
                                                show ten1f2
                                                te "Aghhghg...*heavy moaning gag*"
                                                $ renpy.transition(dissolve)
                                                hide ten1f2
                                                show ten1f3
                                                p "Hehe... *splurt*"
                                                $ renpy.transition(dissolve)
                                                hide ten1f2
                                                show ten1f3
                                                show ten1h2
                                                p "Take it all bitch!"
                                                $ renpy.transition(dissolve)
                                                hide ten1f3
                                                show ten1f4
                                                te "Grggdfgsgdsdf.... *cough gag moan*"
                                                $ renpy.transition(dissolve)
                                                show ten1f5
                                                p "YEah!!! *splurt*"
                                                $ renpy.transition(dissolve)
                                                show ten1f6
                                                p "You are real cum dumpster!"
                                                te "Hmgmhgmhm... *cough*"
                                                p "Wow...."
                                                te "grgggg..*gag cough*"
                                                p "Are you allright?"
                                                te "grgfgf... *gag moan cough*"
                                                scene black with circleirisin   
                                                "Tenten passed out. It looks like it was too much for her."
                                                "You washed her in the water and dress her... It was a lot of work but you did it."
                                                show nharem0 with circleirisout
                                                jump nharem
                                                
                                            "Medium whip expansion":
                                                    p "Time to change your boobs size."
                                                    p "Expansion scroll activation!"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1bl2
                                                    hide ten1f2
                                                    hide ten1back
                                                    hide ten1a
                                                    hide ten1h1
                                                    show ten1b
                                                    show ten1back
                                                    show ten1f2
                                                    show ten1bl2
                                                    show ten1h1
                                                    p "Nice..."
                                                    $ renpy.transition(dissolve)
                                                    hide ten1bl2
                                                    show ten1bl3
                                                    hide ten1f2
                                                    show ten1f3
                                                    te "Mgmmgm..*moan cough*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1bl3
                                                    show ten1bl2
                                                    hide ten1f2
                                                    show ten1f3
                                                    p "Silence! *slash*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1bl2
                                                    show ten1bl1
                                                    show ten1s1
                                                    hide ten1f3
                                                    show ten1f4
                                                    te "Argggg... *moan pain gag*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1back
                                                    show ten1cl
                                                    hide ten1bl1
                                                    show ten1bl2
                                                    hide ten1f4
                                                    show ten1f3
                                                    p "Fuck!!! *slash*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1bl2
                                                    show ten1bl3
                                                    hide ten1f3
                                                    show ten1f2
                                                    show ten1s2
                                                    te "ggrggfhgfhf...*moan gag pain*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1cl
                                                    show ten1bl
                                                    hide ten1bl3
                                                    show ten1bl2
                                                    hide ten1f2
                                                    show ten1f3
                                                    show ten1s3
                                                    p "More!!! *slash*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1bl2
                                                    show ten1bl3
                                                    hide ten1f3
                                                    show ten1f2
                                                    show ten1s4
                                                    p "Yeah! *splurt*"
                                                    $ renpy.transition(dissolve)
                                                    show ten1bl4
                                                    hide ten1f2
                                                    show ten1f1
                                                    te "*gag cough slurp*"
                                                    $ renpy.transition(dissolve)
                                                    show ten1bl5
                                                    show ten1f7
                                                    p "Shit!!! *splurt*"
                                                    $ renpy.transition(dissolve)
                                                    show ten1f8
                                                    p "And more!!!"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1f1
                                                    show ten1f2
                                                    te "Aghhghg...*heavy moaning gag*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1f2
                                                    show ten1f3
                                                    p "Hehe... *splurt*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1f2
                                                    show ten1f3
                                                    show ten1h2
                                                    p "Take it all bitch!"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1f3
                                                    show ten1f4
                                                    te "Grggdfgsgdsdf.... *cough gag moan*"
                                                    $ renpy.transition(dissolve)
                                                    show ten1f5
                                                    p "YEah!!! *splurt*"
                                                    $ renpy.transition(dissolve)
                                                    show ten1f6
                                                    p "You are real cum dumpster!"
                                                    te "Hmgmhgmhm... *cough*"
                                                    p "Wow...."
                                                    te "grgggg..*gag cough*"
                                                    p "Are you allright?"
                                                    te "grgfgf... *gag moan cough*"
                                                    scene black with circleirisin   
                                                    "Tenten passed out. It looks like it was too much for her."
                                                    "You washed her in the water and dress her... It was a lot of work but you did it."
                                                    show nharem0 with circleirisout
                                                    jump nharem
                                            
                                            "Full expansion":
                                                    p "I hope you are ready!"
                                                    p "Expansion scroll activation!"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1bl2
                                                    hide ten1f2
                                                    hide ten1back
                                                    hide ten1a
                                                    hide ten1h1
                                                    show ten1b
                                                    show ten1back
                                                    show ten1f3
                                                    show ten1bl3
                                                    show ten1h1
                                                    p "Nice..."
                                                    te "Mgmgmmgm... *gag pain*"
                                                    p "You can take it Tenten."
                                                    p "Expanison second level!"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1bl3
                                                    hide ten1f3
                                                    hide ten1back
                                                    hide ten1b
                                                    hide ten1h1
                                                    show ten1c
                                                    show ten1back
                                                    show ten1f2
                                                    show ten1bl2
                                                    show ten1h1
                                                    te "Ghhahahhhaaaa... *moan gag pain*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1bl2
                                                    show ten1bl3
                                                    hide ten1f2
                                                    show ten1f3
                                                    te "Mgmmgm..*moan cough*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1bl3
                                                    show ten1bl2
                                                    hide ten1f2
                                                    show ten1f3
                                                    p "Hehe... great..."
                                                    $ renpy.transition(dissolve)
                                                    hide ten1bl2
                                                    show ten1bl1
                                                    hide ten1f3
                                                    show ten1f4
                                                    te "Argggg... *moan pain gag*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1back
                                                    show ten1cl
                                                    hide ten1bl1
                                                    show ten1bl2
                                                    hide ten1f4
                                                    show ten1f3
                                                    p "What about this? *clamp*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1bl2
                                                    show ten1bl3
                                                    hide ten1f3
                                                    show ten1f2
                                                    show ten1m1
                                                    te "ggrggfhgfhf...*heavy moaning*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1cl
                                                    show ten1bl
                                                    hide ten1bl3
                                                    show ten1bl2
                                                    hide ten1f2
                                                    show ten1f3
                                                    show ten1m2
                                                    p "Nice!!!"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1bl2
                                                    show ten1bl3
                                                    hide ten1f3
                                                    show ten1f2
                                                    p "Yeah! *splurt*"
                                                    $ renpy.transition(dissolve)
                                                    show ten1bl4
                                                    hide ten1f2
                                                    show ten1f1
                                                    te "*gag cough slurp*"
                                                    $ renpy.transition(dissolve)
                                                    show ten1bl5
                                                    show ten1f7
                                                    p "Shit!!! *splurt*"
                                                    $ renpy.transition(dissolve)
                                                    show ten1f8
                                                    p "And more!!!"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1f1
                                                    show ten1f2
                                                    te "Aghhghg...*heavy moaning gag*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1f2
                                                    show ten1f3
                                                    p "Hehe... *splurt*"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1f2
                                                    show ten1f3
                                                    show ten1h2
                                                    p "Take it all bitch!"
                                                    $ renpy.transition(dissolve)
                                                    hide ten1f3
                                                    show ten1f4
                                                    te "Grggdfgsgdsdf.... *cough gag moan*"
                                                    $ renpy.transition(dissolve)
                                                    show ten1f5
                                                    p "YEah!!! *splurt*"
                                                    $ renpy.transition(dissolve)
                                                    show ten1f6
                                                    p "You are real cum dumpster!"
                                                    te "Hmgmhgmhm... *cough*"
                                                    p "Wow...."
                                                    te "grgggg..*gag cough*"
                                                    p "Are you allright?"
                                                    te "grgfgf... *gag moan cough*"
                                                    scene black with circleirisin   
                                                    "Tenten passed out. It looks like it was too much for her."
                                                    "You washed her in the water and dress her... It was a lot of work but you did it."
                                                    show nharem0 with circleirisout
                                                    jump nharem
                
                
                
                
               
        
        "Go back to the map":
            scene black with circleirisin               
            show dharem0 with circleirisout
            jump dharem   
            
################################ dhremvillage1
################################ dhremvillage1
################################ dhremvillage1
################################ dhremvillage1
################################ dhremvillage1

label dhremvillage1:
    scene dhremvillage
    menu:
        "Call Sarada":
            if saradaeyes >= 23: # 22 je max pre Saradu
                        $ renpy.transition(dissolve)
                        show sn
                        hide snn
                        show sblind
                        p "Hello Sarada...."
                        s "..."
                        $ eyes = eyes +1
                        p "Why you wear so much clothes?"
                        p "Take them off kid!"
                        $ renpy.transition(dissolve)
                        hide sblind
                        hide sblindop
                        hide snn
                        hide sn
                        show snnaked1
                        show sblindop
                        p "Now it is time to have some fun."
                        menu:
                            "Fuck her ass":
                                p "I think I want to ass fuck you tonight kid!"
                                $ renpy.transition(dissolve)
                                hide snnaked1
                                hide sblindop
                                show s5n
                                show s5normal
                                p "But I'll start off gental."
                                p "Going to tease you a little before sticking up your butt!"
                                with fade
                                p "hmm..."
                                $ renpy.transition(dissolve)
                                hide s5n
                                hide s5normal
                                show s5h
                                show s5normal
                                p "Yes kid they are as soft as usual. *Squeeze*"
                                s "... *Soft moan*"
                                p "Hmm you got nothing clever to say? Maybe I'll be a little rougher then?"
                                $ renpy.transition(dissolve)
                                with fade
                                hide s5normal
                                show s5open
                                s "aaahhh! *Moan*"
                                p "Yeah! That is more of the reaction I wanted! Now it's time for your reward!"
                                $ renpy.transition(dissolve)
                                hide s5open
                                hide s5h
                                show s5penis
                                show s5h
                                show s5closed
                                show s5cry
                                p "*Slip* So tight... Come on kid! I know you can take it so stop crying!"
                                $ renpy.transition(dissolve)
                                hide s5cry
                                p "Open your eyes."
                                $ renpy.transition(dissolve)
                                hide s5closed
                                show s5rrr
                                p "Doesn't look like you're having fun!"
                                p "Maybe that means I need to fuck you harder! *Slam*" with hpunch
                                $ renpy.transition(dissolve)
                                hide s5rrr
                                show s5tounge
                                s "aaaaarr...*Pant*" with vpunch
                                p "Yeah that is more like it!"
                                s "Yeah... Fuck me harder!"
                                p "As your wish! *Slam*" with hpunch
                                $ renpy.transition(dissolve)
                                hide s5tounge
                                show s5wow
                                s "Yessssss! *Grunting*"
                                p "!!!" with hpunch
                                menu:
                                    "Cum in":
                                        $ renpy.transition(dissolve)
                                        show s5spermin
                                        p "Fucking awesome!*Splurt*"
                                        s "So much sperm.*Drip*"
                                        $ renpy.transition(dissolve)
                                        hide s5penis
                                        p "It is a gift for you kid!"
                                        with fade
                                        p "Clean yourself off kid and get dressed!"
                                        $ renpy.transition(dissolve)
                                        with fade
                                        hide s5spermin
                                        hide s5h
                                        hide s5wow
                                        show sn
                                        show sblindop
                                        p "Good job kid... But you should try harder next time..."
                                        s "....."
                                        scene black with circleirisin               
                                        show nharem0 with circleirisout
                                        jump nharem
                                        
                                    "Cum out":
                                        $ renpy.transition(dissolve)
                                        show s5spermout
                                        p "Take it all bitch! *Splurt*"
                                        s "aaaaaahhh! *Splat*"
                                        hide s5penis
                                        $ renpy.transition(dissolve)
                                        p "Hehe you look like the cum loving slut you are!"
                                        with fade
                                        p "What a nasty little slut!"
                                        $ renpy.transition(dissolve)
                                        show s5shy
                                        s "...*dripping*"
                                        p "Clean yourself off kid and get dress!"
                                        $ renpy.transition(dissolve)
                                        with fade
                                        hide s5spermout
                                        hide s5spermin
                                        hide s5shy
                                        hide s5h
                                        hide s5wow
                                        show sn
                                        show sblindop
                                        p "I wonder if you really feel it..."
                                        s "..."
                                        p "It doesn't matter now..."
                                        scene black with circleirisin               
                                        show nharem0 with circleirisout
                                        jump nharem
                                
                            "Punish her":
                                p "Ok I have a lot of toys I want to use on you tonight kid, hehe..."
                                p "First I'm going to play with your titties!"
                                $ renpy.transition(dissolve)
                                hide snnaked1
                                hide sblindop
                                show s5h
                                show s5normal
                                p "I really missed your boobies! I love playing with them so much!"
                                p "I could hold your boobs all day! I never want to let them go!"
                                p "But... I think they could be even more beautiful... With Chakra clips!"
                                $ renpy.transition(dissolve)
                                show s5clips
                                hide s5normal
                                hide s5sad
                                show s5closed
                                show s5shy
                                s "*Pinch!* ....."
                                p "I know you like it, so don't act all shy now!"
                                p "Hmm... Maybe I'll use this on you then!"
                                "*whip!*" with hpunch
                                show s5scar1
                                hide s5shy
                                hide s5closed
                                show s5open
                                s "*Moan* Amazing."
                                p "You really like it when I whip you right?"
                                s "Yes... more!!! *Heavy panting*"
                                p "I want you to beg me for it! Like the good little slave you are!"
                                s "Please whip me. Punish me!!! I've been a bad girl and need to be whipped!"
                                "*Smack!*" with hpunch
                                show s5scar2
                                hide s5open
                                show s5tounge
                                show s5cry
                                s "aaaarrr! *Sob*"
                                p "Damn kid... You really like to be whipped a lot huh?"
                                p "It looks like you cum every time I smack you!"
                                "*slash!*" with hpunch
                                show s5scar3
                                hide s5tounge
                                show s5wow
                                hide s5cry
                                show s5milk
                                s "AaaaHHH! *Squirt*"
                                p "Fuck yes! That's a good girl! Spraying her jucies and begging me for more!"
                                "*whip*" with hpunch
                                s "!!!! *Drool*"
                                p "Ah, yea Now it's my turn..."
                                $ renpy.transition(dissolve)
                                show s5dick
                                p "Just a little more."
                                with fade
                                p "Hmm I wonder if this..."
                                $ renpy.transition(dissolve)
                                show s5dildotf
                                p "*Slip* Yes it fits so nicely between your tits!"
                                p "Here it comes bitch! *Splurt*" with hpunch
                                show s5spermmouth
                                show s5shy
                                show s5cry2
                                s "Ooouuuu! *Drip*"
                                p "Shit.... Look at yourself. You look like a fucking whore!"
                                p "Maybe I should take a picture of you." 
                                p "Nah too risky."
                                p "Ok time to fix you up."
                                p "First I need to heal you."
                                $ renpy.transition(dissolve)
                                hide s5scar1
                                hide s5scar2
                                hide s5scar3
                                p "And take these toys off."
                                $ renpy.transition(dissolve)
                                hide s5dick
                                hide s5dildotf
                                hide s5clips
                                hide s5shy
                                hide s5cry2
                                hide s5wow
                                show s5normal
                                p "You look almost normal..."
                                p "You can clean the rest off. Using your tongue that is!"
                                $ renpy.transition(dissolve)
                                hide s5normal
                                show s5tounge
                                hide s5spermmouth
                                hide s5milk
                                show s5sperm
                                p "Nicely done kid."
                                p "It is fine to see you naked but you can catch cold. Now get dressed!"
                                $ renpy.transition(dissolve)
                                hide s5sperm
                                hide s5tounge
                                hide s5h
                                show sn
                                show sblindop                                
                                p "No go back to the work... I will come back later..."
                                p "Maybe..."
                                s "..."                                
                                scene black with circleirisin               
                                show nharem0 with circleirisout
                                jump nharem
                                
                            "Fuck her nipples":
                                p "I really want to fuck your nipples!"
                                $ renpy.transition(dissolve)
                                hide snnaked1
                                hide sblindop                                
                                show s5h
                                show s5sad
                                p "Your Tits are so amazing! I love squeezing them!"
                                p "Ok just squeeze them together a little more..."
                                $ renpy.transition(dissolve)
                                hide s5sad
                                hide s5h
                                show s5nf
                                show s5sad
                                show s5nfnl
                                show s5nfnr
                                p "This should work again..."
                                p "What nipple should I fuck today?"
                                menu:
                                    "Right nipple":
                                        p "Time to try it! Going to give your right nip some love!"
                                        with fade
                                        p "Expansion scrool activated! Nipple Expansion!"
                                        $ renpy.transition(dissolve)
                                        hide s5nfnr
                                        show s5nfnrp
                                        s "*Push* AAAAAAAWWWWWWW!!!" with hpunch
                                        $ renpy.transition(dissolve)
                                        hide s5sad
                                        show s5tounge
                                        p "Yeah let it out bitch! Scream as much as you want!"
                                        p "I know you love it!"
                                        p "Push More!!" with hpunch
                                        with fade
                                        p "Yeah...."
                                        $ renpy.transition(dissolve)
                                        hide s5tounge
                                        show s5wow
                                        s "!!!*Drool*"
                                        p "Almost...."
                                        $ renpy.transition(dissolve)
                                        show s5nfnrsp
                                        p "Fuck!!! *Splurt*"
                                        s "aaaaaahhh! *drip*"
                                        $ renpy.transition(dissolve)
                                        show s5shy
                                        p "This is a dream come ture!"
                                        with fade
                                        p "Amazing how it is able to fit inside."
                                        with fade
                                        p "Fuck that was fun... I came so hard! But it is time for you to clean yourself off and get dressed!"
                                        $ renpy.transition(dissolve)
                                        hide s5wow
                                        hide s5shy
                                        hide s5nfnrp
                                        hide s5nfnrsp
                                        hide s5nf
                                        hide s5nfnl
                                        hide s5nfnr
                                        show snnaked1
                                        show sblindop
                                        p "Huh? Not getting dressed?"
                                        p "Whatever.. I don't care until I am satisfied."                                        
                                        s "...."
                                        scene black with circleirisin               
                                        show nharem0 with circleirisout
                                        jump nharem
                                    "Left nipple":
                                        p "Time to try it! I'm going to try to put it in your left nipple now."
                                        with fade
                                        p "Expansion scrool activated! Nipple Expansion!"
                                        hide s5nfnl
                                        show s5nfnlp
                                        s "AAAAAAAWWWWWWW! *Slip*" with hpunch
                                        hide s5sad
                                        show s5tounge
                                        p "Good girl! Let me hear you scream!"
                                        p "I know you love it!"
                                        p "More!" with hpunch
                                        with fade
                                        p "Yeah...."
                                        hide s5tounge
                                        show s5wow
                                        s "!!!"
                                        p "Almost...."
                                        show s5nfnlsp
                                        p "Fuck!!! *Splurt*"
                                        s "aaaaaahhh! *Drip*"
                                        with fade
                                        show s5shy
                                        p "So good... Like a dream..."
                                        with fade
                                        p "It is amazing that my dick can fit in there!"
                                        with fade
                                        p "Fuck that was fun... I came so hard! But it is time for you to clean yourself off and get dressed!"
                                        $ renpy.transition(dissolve)
                                        hide s5wow
                                        hide s5shy
                                        hide s5nfnrp
                                        hide s5nfnrsp
                                        hide s5nf
                                        hide s5nfnl
                                        hide s5nfnr
                                        hide s5nfnlsp
                                        show snnaked1
                                        hide s5nfnlp
                                        show sblindop
                                        p "Huh? Not getting dressed?"
                                        p "Whatever.. I don't care until I am satisfied."                                        
                                        s "...."
                                        scene black with circleirisin               
                                        show nharem0 with circleirisout
                                        jump nharem
                                
                            "Kage bunshin no jutsu":
                                p "Ok kid time for something special."
                                p "kage bunshin no jutsu!"with hpunch
                                p "Remember the story you told me, about your mommy and daddy? Let's recreate that moment... Sounds fun right?"
                                p "Let's lick down here... Get your pussy nice and moist..."
                                with fade
                                p "Can't forget about your titties!"
                                $ renpy.transition(dissolve)
                                hide snnaked1
                                hide sblindop
                                show s5h
                                show s5open
                                p "That's it... I can tell you're starting to loosen up."
                                with fade
                                p "Do you want my dick?"
                                s "Yesssssss!!!"
                                s "Please fuck me hard!"
                                p "Well... Since you asked so nicely... Hehe..."
                                $ renpy.transition(dissolve)
                                hide s5h
                                hide s5open
                                show s5penis
                                show s5h
                                show s5tounge
                                s "Ooouuuuu! *Moan*"
                                p "We just started! Don't give out just yet!!!"
                                p "Squeezing your boobs is the best!"
                                $ renpy.transition(dissolve)
                                hide s5h
                                hide s5open
                                hide s5penis
                                show s5nf
                                show s5sad
                                show s5nfnl
                                show s5nfnr
                                show s5penis
                                p "Time to fuck your nipples now!"
                                p "Expansion scrool activated! Nipple Expansion!"
                                with fade
                                s "Please put it in!*beg*"
                                with fade
                                p "Don't worry we will! *Jam*"
                                $ renpy.transition(dissolve)
                                hide s5sad
                                hide s5nfnl
                                hide s5nfnr
                                show s5nfnrp
                                show s5nfnlp
                                hide s5tounge
                                show s5wow
                                s "Yesssssss!!! *Panting*"
                                p "Take it bitch." with hpunch
                                s "Moreeeee.... *Drool*"
                                $ renpy.transition(dissolve)
                                hide s5wow
                                show s5closed
                                show s5dick
                                p "kage bunshin no jutsu really have some benefits!"
                                s "aaaaHhhh! *Heavy moaning*"
                                $ renpy.transition(dissolve)
                                hide s5closed
                                show s5tounge
                                s "Arrrrrggggg *moan*"
                                p "Shit!"
                                $ renpy.transition(dissolve)
                                show s5spermin
                                p "Fucking awesome! *Splurt*" with hpunch
                                $ renpy.transition(dissolve)
                                show s5nfnrsp
                                s "Ouuuu *Drip*"
                                p "Looks like the left clone is ready too!"
                                $ renpy.transition(dissolve)
                                show s5nfnlsp
                                s ".....*Squirt*"
                                $ renpy.transition(dissolve)
                                hide s5tounge
                                show s5wow
                                p "Catch this kid!"
                                $ renpy.transition(dissolve)
                                show s5spermmouth
                                s "More!!! *Splat"
                                p "Time for a finale" with hpunch
                                $ renpy.transition(dissolve)
                                show s5spermout
                                p "YESSS!!! *Squirt squirt squirt*" with hpunch
                                s "Ugh yessss... *Moaning* ... Yummy... *Dripping*"
                                $ renpy.transition(dissolve)
                                hide s5wow
                                show s5closed
                                p "She's covered with cum!"
                                p "But I enjoyed it!"
                                "..."
                                s "... *Dripping*"
                                p "Quite the mess... Well your up kid time to clean yourself off..."
                                $ renpy.transition(dissolve)
                                hide s5dick
                                hide s5spermin
                                hide s5spermmouth
                                hide s5spermout
                                hide s5nfnrsp
                                hide s5nfnlsp
                                hide s5penis
                                hide s5shy
                                hide s5nfnlp
                                hide s5nfnrp
                                show s5nfnl
                                show s5nfnr
                                hide s5closed
                                show s5open
                                p "I guess I'll have to let go of your tits now..."
                                $ renpy.transition(dissolve)
                                hide s5nf
                                hide s5nfnl
                                hide s5nfnr
                                hide s5h
                                hide s5open
                                show sn
                                show sblind
                                p "Sigh... All good things must come to an end."
                                p "But I can do this tomorrow too!"
                                p "Just be a good girl and wait for me."
                                s ".... *moan*"
                                scene black with circleirisin               
                                show nharem0 with circleirisout
                                jump nharem
            else:
                "How you want to talk with her if she is not here?"
                scene black with circleirisin               
                show dharem0 with circleirisout
                jump dharem
                
####################################### 12 je max pre Sakuru             
        "Call Sakura":
            if sakuraslave >= 13: # 12 je max pre Sakuru
                p "Where are you Sakura?"
                $ renpy.transition(dissolve)
                show saku1
                show sakunna
                p "Here you are...."
                menu sakuratrain95111:
                    "Play with her body": 
                            p "Concentrate..."
                            p "Time for something easy."
                            p "Take your clothes off!"
                            $ renpy.transition(dissolve)
                            hide saku1
                            hide sakunna
                            show saku3
                            show sakunna
                            p "That was so easy..."
                            p "Maybe I can play a little with you."
                            "You grab Sakura boobs."
                            sa "MMMmmmmmm... *moan*"
                            p "hehe... It looks like you like it..."
                            $ renpy.transition(dissolve)
                            hide sakunna
                            show sakunorg
                            sa "Arggggg....*breath*"
                            p "I have something for you. *clamp*"
                            $ renpy.transition(dissolve)
                            show sakuclips
                            hide sakunorg
                            show sakunshock
                            sa "!!!!"
                            p "That suprise you right? What about that?"
                            $ renpy.transition(dissolve)
                            show sakuclip
                            sa "OUCH *pain*"
                            p "Lightning style!"
                            $ renpy.transition(dissolve)
                            show sakul1
                            sa "Zzzzzz...."
                            p "Hehe... Funny... More power!"
                            $ renpy.transition(dissolve)
                            show sakul2
                            sa "Argggggg ...*huming*"
                            p "It is really shocking, right???"
                            p "Lightning circle! *zap*"
                            $ renpy.transition(dissolve)
                            show sakul3
                            hide sakunshock
                            show sakunorg
                            sa "Aaaaaa..."
                            $ renpy.transition(dissolve)
                            show sakul4
                            p "Heh.. It is complete..."
                            $ renpy.transition(dissolve)
                            show sakumilk
                            sa "Aaaaaaa.. *moan*"
                            p "And hard to keep..."
                            p "But she enjoy it..."
                            $ renpy.transition(dissolve)
                            hide sakul2
                            p "...."
                            $ renpy.transition(dissolve)
                            hide sakul3
                            hide sakul4
                            p "That was fun, but I will do more next time..."                               
                            p "So prepare for the next time Sakura."
                            sa "*moan*"
                            scene black with circleirisin               
                            show nharem0 with circleirisout
                            jump nharem
                            
                                
                        
                    "Pain train":   
                            p "Time to pain train!"
                            p "Now..."
                            p "Take your clothes off!"
                            $ renpy.transition(dissolve)
                            hide saku1
                            hide sakunna
                            show saku3
                            show sakunna
                            p "Nice... Hmmm... Maybe..."
                            p "If I use that whip on your body..."
                            "*Slash*" with hpunch
                            sa "Arggggg...*whip*"
                            $ renpy.transition(dissolve)
                            hide sakunna
                            show sakunnouch
                            p "Yes... Like that..."
                            p "But harder!"
                            "*Slash*" with hpunch
                            show sakusc1
                            sa "Aaaaaa... *pain*"
                            p "Heh... maybe..."
                            "*Whip*" with hpunch
                            show sakusc2
                            sa "Oooooo... *moan*"
                            p "Your tone has changed."
                            "*Whip*" with vpunch
                            $ renpy.transition(dissolve)
                            hide sakunnouch
                            show sakunorg
                            sa "More!!!!!"
                            p "Hehe...."
                            sa "...."
                            p "You just say more again!"
                            sa "..."
                            p "I hope you can take that."
                            "*Slash*" with hpunch
                            show sakusc3
                            p "Hehe..."
                            "*Slash*" with hpunch
                            p "You are really funny..."
                            "*Whip*" with vpunch
                            sa "YESSSS!!!! *moan*"
                            "*Slash*" with hpunch
                            show sakusc4
                            sa "Aaaaaaaa.... *Heavy Moaning*"
                            p "How can you enjoy it? You are an empty doll or not???"
                            sa "Yessss.... *moaning*"
                            p "This is a little weird but ok..."
                            p "It looks like you have enough... or maybe want continue... who know?"
                            p "Anyway, time to end it."
                            sa "*sad moaning*"
                            p "Hehe..."
                            scene black with circleirisin               
                            show nharem0 with circleirisout
                            jump nharem
                            
                    "Blowjob":
                            p "I want a blowjob now..."
                            p "Take your clothes off!"
                            $ renpy.transition(dissolve)
                            hide saku1
                            hide sakunna
                            show saku3
                            show sakunna
                            p "Yes that is good..."
                            p "Now... Get on your knees."
                            sa "..."
                            p "NOW!"
                            $ renpy.transition(dissolve)
                            hide saku3
                            hide sakunna
                            show saku3a
                            show saku3ok
                            p "That is nice..."
                            p "Open your mouth."
                            sa "....."
                            p "Ou... I see... You want my help again right?"
                            p "No problem..."
                            $ renpy.transition(dissolve)
                            hide saku3a
                            hide saku3ok
                            show saku3b
                            show saku3h1
                            sa "Mgmmmmmhhh..."
                            p "Yes, that is nice... Just don't bite!"
                            $ renpy.transition(dissolve)
                            hide saku3h1
                            show saku3h2
                            sa "mgmmmmm!!! *gag*"
                            p "There is a lot of space here..."
                            $ renpy.transition(dissolve)
                            hide saku3h2
                            show saku3h1
                            p "Just hold it open."
                            menu:
                                "Regular blow":
                                    $ renpy.transition(dissolve)
                                    hide saku3h1
                                    hide saku3ok
                                    show saku3ok
                                    show saku3p1
                                    p "Be a nice girl and suck my dick!"
                                    $ renpy.transition(dissolve)
                                    hide saku3p1
                                    show saku3p2
                                    hide saku3ok
                                    show saku3okbl
                                    sa "grggggfg!!! *gag*"
                                    $ renpy.transition(dissolve)
                                    hide saku3p2
                                    show saku3p3
                                    hide saku3okbl
                                    show saku3clop
                                    p "Yes. That is nice!"
                                    p "Deeper!!!"
                                    $ renpy.transition(dissolve)
                                    hide saku3p3
                                    show saku3p4
                                    hide saku3clop
                                    show saku3cl
                                    sa "grggggfgfg!!! *gag cough*"
                                    $ renpy.transition(dissolve)
                                    hide saku3p4
                                    show saku3p3
                                    hide saku3cl
                                    show saku3clop
                                    p "Fuck!!!"
                                    $ renpy.transition(dissolve)
                                    hide saku3p3
                                    show saku3p4
                                    hide saku3clop
                                    show saku3cl
                                    p "That is good to be inside."
                                    p "Maybe if I use this...*clamp*"
                                    $ renpy.transition(dissolve)
                                    show saku3clips
                                    hide saku3p4
                                    show saku3p3
                                    hide saku3cl
                                    show saku3clop
                                    sa "Aggggg... *gag pain*"
                                    p "Yeah just like that! Lightning style!"
                                    $ renpy.transition(dissolve)
                                    show saku3l1
                                    hide saku3p3
                                    show saku3p4
                                    hide saku3clop
                                    show saku3cl
                                    p "And more power!"
                                    $ renpy.transition(dissolve)
                                    show saku3l2
                                    hide saku3p4
                                    show saku3p3
                                    hide saku3cl
                                    show saku3clop
                                    sa "grrrrr!!! *gag cough*"
                                    $ renpy.transition(dissolve)
                                    hide saku3p3
                                    show saku3p4
                                    hide saku3clop
                                    show saku3cl
                                    p "I just... *spurt*"
                                    $ renpy.transition(dissolve)
                                    show saku3sp1
                                    show saku3milk
                                    sa "Arggfggmmgm... *drip*"
                                    $ renpy.transition(dissolve)
                                    show saku3sp2
                                    p "heh..... You are so hot!"
                                    p "Just cumming in your throat is..."
                                    p "So fucking amazing!"
                                    sa "grrrrr!!! *Slurp gag cough*"
                                    p "ehhm.... Why did I even say that?"
                                    p "You can't understand me or?"
                                    sa "*moan*"
                                    p "Who cares... Bye..."
                                    scene black with circleirisin               
                                    show nharem0 with circleirisout
                                    jump nharem
                                "Nipple fuck":
                                    p "Time to play with your nipple."
                                    $ renpy.transition(dissolve)
                                    hide saku3h1
                                    show saku3nf1
                                    hide saku3ok
                                    show saku3ok
                                    p "Expansion scroll!!!"
                                    p "Just push it a little..."
                                    $ renpy.transition(dissolve)
                                    hide saku3nf1
                                    show saku3nf2
                                    sa "Grrrr...."
                                    p "That is nice, but your mouth want it too. Kage bunshin!"
                                    $ renpy.transition(dissolve)
                                    show saku3p1
                                    p "Nice!"
                                    $ renpy.transition(dissolve)
                                    hide saku3nf2
                                    show saku3nf3
                                    hide saku3p1
                                    show saku3p2
                                    hide saku3ok
                                    show saku3sad
                                    sa "Aaagggraaaa.... *pain*"
                                    p "Shit that is so good!"
                                    $ renpy.transition(dissolve)
                                    hide saku3nf3
                                    show saku3nf2
                                    hide saku3p2
                                    show saku3p3
                                    hide saku3sad
                                    show saku3cl
                                    sa "Ggggggggrgggg.... *gag*"
                                    $ renpy.transition(dissolve)
                                    hide saku3p4
                                    show saku3p3
                                    hide saku3nf2
                                    show saku3nf3
                                    hide saku3cl
                                    show saku3clop
                                    p "Fuck!!!"
                                    $ renpy.transition(dissolve)
                                    hide saku3p3
                                    show saku3p4
                                    hide saku3nf3
                                    show saku3nf2
                                    hide saku3clop
                                    show saku3cl
                                    sa "*gag cough*"
                                    $ renpy.transition(dissolve)
                                    hide saku3p4
                                    show saku3p3
                                    hide saku3nf2
                                    show saku3nf3
                                    hide saku3cl
                                    show saku3clop
                                    p "Time to play. "
                                    "*Slash!*" with hpunch
                                    show saku3sl1
                                    $ renpy.transition(dissolve)
                                    hide saku3p3
                                    show saku3p4
                                    hide saku3nf3
                                    show saku3nf2
                                    hide saku3clop
                                    show saku3cl
                                    hide saku3cry
                                    show saku3cry
                                    sa "Grgggfgg... *gag pain*"
                                    "*Slash!*" with hpunch
                                    show saku3sl2
                                    sa "ARGGGGGGGG!!!!!"
                                    p "And one more time!"
                                    "*Slash!*" with hpunch
                                    show saku3sl3
                                    $ renpy.transition(dissolve)
                                    hide saku3p4
                                    show saku3p3
                                    hide saku3nf2
                                    show saku3nf3
                                    hide saku3cry
                                    hide saku3cl
                                    show saku3clop
                                    show saku3cry
                                    p "Take it! *spurt*"
                                    $ renpy.transition(dissolve)
                                    show saku3nfsp1
                                    hide saku3p3
                                    show saku3p4
                                    hide saku3cry
                                    hide saku3clop
                                    show saku3clop
                                    show saku3cry
                                    p "Yes!!!"
                                    show saku3nfsp2
                                    hide saku3p4
                                    show saku3p3
                                    hide saku3cry
                                    hide saku3clop
                                    show saku3clop
                                    show saku3cry
                                    sa "Glurp.... *cough*"
                                    $ renpy.transition(dissolve)
                                    show saku3sp1
                                    p "Take it all! *spurt*"
                                    $ renpy.transition(dissolve)
                                    show saku3sp2
                                    p "Wow...."
                                    sa "grggggg..."
                                    p "You are really amazing..."
                                    p "I will definitely try it again after I got more chakra!"
                                    sa "*gag*"
                                    sa "*moan*"
                                    p "Who cares... Bye..."
                                    scene black with circleirisin               
                                    show nharem0 with circleirisout
                                    jump nharem
                        
                    "Fuck her":   
                            p "Ok. Just..."
                            p "Take your clothes off!"
                            $ renpy.transition(dissolve)
                            hide saku1
                            hide sakunna
                            show saku3
                            show sakunna
                            p "Yes that is good..."
                            p "Maybe you can turn around now."
                            $ renpy.transition(dissolve)
                            hide saku3
                            hide sakunna
                            show saku2a
                            show saku2ok
                            p "Huh? So you seriously want it right?"
                            sa "*mumble*"
                            p "It is just normal you want it... Even in that form."
                            $ renpy.transition(dissolve)
                            hide saku2ok
                            show saku2cl
                            sa "...."
                            p "Time to have fun."
                            menu:
                                "Clone":
                                    p "It is really a two man job."
                                    $ renpy.transition(dissolve)
                                    show saku2p1
                                    p "Kage bunshin no jutsu."
                                    $ renpy.transition(dissolve)
                                    show saku2bl1
                                    p "It will be very funny."
                                    $ renpy.transition(dissolve)
                                    hide saku2p1
                                    show saku2p2
                                    hide saku2bl1
                                    show saku2bl2
                                    hide saku2cl
                                    show saku2cln
                                    sa "..."
                                    $ renpy.transition(dissolve)
                                    hide saku2p2
                                    show saku2p3
                                    hide saku2bl2
                                    show saku2bl3
                                    p "Come on!"
                                    $ renpy.transition(dissolve)
                                    hide saku2p3
                                    show saku2p4
                                    hide saku2bl3
                                    show saku2bl4
                                    sa "Arrrr.... *moan*"
                                    $ renpy.transition(dissolve)
                                    hide saku2p4
                                    show saku2p3
                                    hide saku2bl4
                                    show saku2bl3
                                    hide saku2cln
                                    show saku2opn
                                    p "Amazing..."
                                    $ renpy.transition(dissolve)
                                    hide saku2p2
                                    show saku2p3
                                    hide saku2bl2
                                    show saku2bl3
                                    hide saku2opn
                                    show saku2cln
                                    sa "Yes!!!"
                                    $ renpy.transition(dissolve)
                                    hide saku2p3
                                    show saku2p4
                                    hide saku2bl3
                                    show saku2bl4
                                    sa "mmmmmm *moan*"
                                    $ renpy.transition(dissolve)
                                    hide saku2p4
                                    show saku2p3
                                    hide saku2bl4
                                    show saku2bl3
                                    hide saku2cln
                                    show saku2orgn
                                    sa "Aaaaaa *Heavy moaning* "
                                    $ renpy.transition(dissolve)
                                    hide saku2p3
                                    show saku2p4
                                    hide saku2bl3
                                    show saku2bl4
                                    p "Yeah! *slurp*"
                                    $ renpy.transition(dissolve)
                                    hide saku2bl4
                                    show saku2bl3
                                    show saku2spin1
                                    sa "YES!!!!"
                                    $ renpy.transition(dissolve)
                                    hide saku2bl3
                                    show saku2bl2
                                    show saku2spin2
                                    p "You look pretty good now! More!"
                                    $ renpy.transition(dissolve)
                                    hide saku2bl2
                                    show saku2bl1
                                    hide saku2orgn
                                    show saku2org
                                    show saku2blo1
                                    "*puff*"
                                    $ renpy.transition(dissolve)
                                    show saku2blo2
                                    p "Amazing!"
                                    $ renpy.transition(dissolve)
                                    hide saku2bl1
                                    show saku2bl2
                                    hide saku2org
                                    show saku2orgn
                                    sa "Mmmm... *drip*"
                                    $ renpy.transition(dissolve)
                                    show saku2spin2
                                    sa "Mmmm....*drip*"
                                    $ renpy.transition(dissolve)
                                    hide saku2bl2
                                    show saku2bl3
                                    sa "Grggggg... *gag*"
                                    $ renpy.transition(dissolve)
                                    hide saku2bl3
                                    show saku2bl4
                                    show saku2bli1
                                    p "Yeah!!! *spurt*"
                                    $ renpy.transition(dissolve)
                                    show saku2bli2
                                    sa "GRGGGG.... *gag cough*"
                                    p "You are.... so good..."
                                    p "... Emh...Who cares, right?"
                                    sa "*gag moan*"
                                    p "..."
                                    scene black with circleirisin               
                                    show nharem0 with circleirisout
                                    jump nharem
                                    
                                "Toys":    
                                    p "Maybe you can show me something that Tsunade teach you..."
                                    sa "..."
                                    p "Can you show me expansion technique?"
                                    sa "....."
                                    $ renpy.transition(dissolve)
                                    hide saku2a
                                    show saku2b
                                    hide saku2cl
                                    show saku2cl
                                    p "Nice... "
                                    sa "... "
                                    if sakuraslave == 9:
                                        $ sakuraslave = 10
                                    p "Can you make them bigger?"
                                    sa "*mumble*"
                                    $ renpy.transition(dissolve)
                                    hide saku2b
                                    show saku2c
                                    hide saku2cl
                                    show saku2cl
                                    p "Wow, you are a really good student."
                                    p "There is not many things I can do for you but..."
                                    $ renpy.transition(dissolve)
                                    show saku2p1
                                    p "You didn't expect anything right now. Right?"
                                    $ renpy.transition(dissolve)
                                    hide saku2p1
                                    show saku2p2
                                    hide saku2cl
                                    show saku2n
                                    sa "mmmmm...."
                                    $ renpy.transition(dissolve)
                                    hide saku2p2
                                    show saku2p3
                                    p "I know I can do more than that."
                                    "*salsh*" with hpunch
                                    show saku2sl1
                                    hide saku2p3
                                    show saku2p4
                                    sa "Aegggg.... *pain*"
                                    "*salsh*" with hpunch
                                    show saku2sl2
                                    hide saku2p4
                                    show saku2p3
                                    hide saku2n
                                    show saku2clop
                                    sa "YESSSSSSS!!!!"
                                    $ renpy.transition(dissolve)
                                    hide saku2p3
                                    show saku2p2
                                    p "Is it working for you?"
                                    "*salsh*" with hpunch
                                    show saku2sl3
                                    hide saku2p2
                                    show saku2p3
                                    sa "AaaAAAA.... *heavy moaning*"
                                    $ renpy.transition(dissolve)
                                    hide saku2p3
                                    show saku2p4
                                    p "I think that counts as a yes. *slash*"
                                    $ renpy.transition(dissolve)
                                    hide saku2p4
                                    show saku2p3
                                    p "And one last time!"
                                    "*salsh*" with hpunch
                                    show saku2sl4
                                    hide saku2p3
                                    show saku2p4
                                    hide saku2clop
                                    show saku2org
                                    sa "Arrrrrrrrrrrrr... *moan pain*"
                                    $ renpy.transition(dissolve)
                                    hide saku2p4
                                    show saku2p3
                                    p "Fuck I will..."
                                    menu:
                                        "Cum in":
                                            p "YEAH!!!"
                                            $ renpy.transition(dissolve)
                                            hide saku2p3
                                            show saku2p2
                                            p "Just..."
                                            $ renpy.transition(dissolve)
                                            hide saku2p2
                                            show saku2p3
                                            p "!!! *spurt*"
                                            $ renpy.transition(dissolve)
                                            hide saku2p3
                                            show saku2p4
                                            show saku2spin1
                                            sa "MMMmmmmm.... *moan drip*"
                                            $ renpy.transition(dissolve)
                                            show saku2spin2
                                            p "That was good...."
                                            p "I will fill you again soon..."
                                            scene black with circleirisin               
                                            show nharem0 with circleirisout
                                            jump nharem
                                            
                                            
                                        "Cum out":
                                            p "Yeah just..."
                                            $ renpy.transition(dissolve)
                                            hide saku2p3
                                            show saku2p2
                                            p "Fuck! *spurt*"
                                            $ renpy.transition(dissolve)
                                            hide saku2p2
                                            show saku2p1
                                            sa "Mmmmmmm.... *moan*"
                                            $ renpy.transition(dissolve)
                                            show saku2spo1
                                            sa "Yesssss.... *drip*"
                                            $ renpy.transition(dissolve)
                                            show saku2spo2
                                            p "Fuck..."
                                            p "That was good...."
                                            p "Just look at you..."
                                            sa "*moan*"
                                            p "Nevermind..."
                                            scene black with circleirisin               
                                            show nharem0 with circleirisout
                                            jump nharem
                            
                    "Call Mikoto":
                        p "I think this is the right time to call Mikoto."
                        $ renpy.transition(dissolve)
                        hide saku1
                        hide sakunna
                        $ renpy.transition(dissolve)
                        show saku1:
                            xalign 0.0 yalign 1.0
                        show sakunna:
                            xalign 0.0 yalign 1.0
                        "...."
                        show mikoa:
                            xalign 1.0 yalign 1.0
                        show mikop:                                
                            xalign 1.0 yalign 1.0
                        mik "huh??? It looks like you want to have some fun with Sakura."
                        p "Yeah... Do you want to join us???"
                        mik "Sure...."
                        $ renpy.transition(dissolve)
                        hide saku1
                        hide sakunna
                        hide mikoa
                        hide mikop
                        p "kage bunshin no jutsu!!!"
                        $ renpy.transition(dissolve)
                        show misa1a
                        show misa1mok
                        show misa1op
                        show misa1p1
                        show misa1s1
                        mik "This is nice..."
                        $ renpy.transition(dissolve)
                        hide misa1p1
                        hide misa1s1
                        show misa1p2
                        show misa1s2
                        mik "Yesss... Fuck me harder..."
                        $ renpy.transition(dissolve)
                        hide misa1p2
                        hide misa1s2
                        show misa1p3
                        show misa1s3
                        s "...."
                        p "Do you want something???"
                        $ renpy.transition(dissolve)
                        hide misa1p3
                        hide misa1s3
                        show misa1p4
                        show misa1s4
                        p "Maybe this?"
                        $ renpy.transition(dissolve)
                        hide misa1p4
                        hide misa1s4
                        show misa1p3
                        show misa1s3
                        hide misa1op
                        show misa1cl
                        show misa1l1
                        mik "Yesss... This is good..."
                        $ renpy.transition(dissolve)
                        hide misa1p3
                        hide misa1s3
                        show misa1p2
                        show misa1s2
                        hide misa1mok
                        show misa1mcl
                        p "Hehe... I feel it same way... Lightning style!!! *zap*"
                        $ renpy.transition(dissolve)
                        hide misa1p2
                        hide misa1s2
                        show misa1p3
                        show misa1s3
                        show misa1l2
                        mik "MMm....*moan*"
                        $ renpy.transition(dissolve)
                        hide misa1cl
                        show misa1op
                        s "...."
                        $ renpy.transition(dissolve)
                        hide misa1p3
                        hide misa1s3
                        show misa1p4
                        show misa1s4
                        p "You want more right?"
                        $ renpy.transition(dissolve)
                        hide misa1p4
                        hide misa1s4
                        show misa1p3
                        show misa1s3
                        show misa1l3
                        mik "Yess!!!! *moan*"
                        $ renpy.transition(dissolve)
                        hide misa1p3
                        hide misa1s3
                        show misa1p2
                        show misa1s2
                        p "I think this is it!!!"
                        $ renpy.transition(dissolve)
                        hide misa1p2
                        hide misa1s2
                        show misa1p3
                        show misa1s3
                        s "...."
                        $ renpy.transition(dissolve)
                        hide misa1p3
                        hide misa1s3
                        show misa1p4
                        show misa1s4
                        show misa1s5
                        p "Fuck!!!*splurt*"
                        $ renpy.transition(dissolve)
                        show misa1s6
                        show misa1p5
                        mik "Yess... Cum more!!!"
                        $ renpy.transition(dissolve)
                        show misa1p6
                        s "...."
                        p "Hehe..."
                        p "funny...."
                        mik "Yes it was..."
                        mik "It is good to have Sakura here in the village."
                        p "For sure it is..."
                        scene black with circleirisin               
                        show nharem0 with circleirisout
                        jump nharem
                        
                    
                    "Call Sarada":
                        if saradaeyes <= 22:
                            "Sarada is not here, try something else."
                            jump sakuratrain95111
                        else:
                            p "Time for double fun."
                            p "Come here Sarada!!!"
                            $ renpy.transition(dissolve)
                            hide saku1
                            hide sakunna
                            show sn:
                                xalign 1.0 yalign 1.0
                            show sblind:                                
                                xalign 1.0 yalign 1.0
                            s "...."
                            $ renpy.transition(dissolve)
                            show saku1:
                                xalign 0.0 yalign 1.0
                            show sakunna:
                                xalign 0.0 yalign 1.0
                            p "Ok girls..."
                            p "Take your clothes off!"
                            $ renpy.transition(dissolve)
                            hide saku1
                            hide sakunna
                            show saku3:
                                xalign 0.0 yalign 1.0
                            show sakunna:
                                xalign 0.0 yalign 1.0
                            hide sblind
                            hide sn
                            show snnaked1:
                                xalign 1.0 yalign 1.0
                            show sblind:
                                xalign 1.0 yalign 1.0
                            p "Hmm... look at you girls."
                            p "Sarada has bigger boobs and longer hair."
                            p "And Sakura looks like she is on same age."
                            p "Anyway, girls you know what to do."
                            p "Try to make me feel happy..."
                            sa "..."
                            $ renpy.transition(dissolve)
                            hide snnaked1
                            hide sakunna
                            hide sblind
                            hide saku3
                            show sasa1
                            show sasa1ln
                            show sasa1rn
                            p "Nice. Maybe I can try something like..."
                            menu:
                                "Lightning":
                                    $ renpy.transition(dissolve)
                                    show sasa1p1
                                    p "Yes, that feels so good..."
                                    p "Just shake a little with your boobs."
                                    $ renpy.transition(dissolve)
                                    hide sasa1p1
                                    show sasa1p2
                                    hide sasa1rn
                                    show sasa1rdow
                                    s "Like that?"
                                    p "Yes, continue..."
                                    $ renpy.transition(dissolve)
                                    hide sasa1p2
                                    show sasa1p3
                                    hide sasa1ln
                                    show sasa1lang
                                    p "Huh? is something wrong Sakura?"
                                    sa ".... *mumble*"
                                    $ renpy.transition(dissolve)
                                    hide sasa1p3
                                    show sasa1p2
                                    p "You miss something right? *clamp*"
                                    $ renpy.transition(dissolve)
                                    show sasa1c1
                                    hide sasa1p2
                                    show sasa1p1
                                    sa "Mmmmmm... *moan*"
                                    p "And this is for you...*clamp*"
                                    $ renpy.transition(dissolve)
                                    show sasa1c2
                                    hide sasa1p1
                                    show sasa1p2
                                    hide sasa1rdow
                                    show sasa1rsad
                                    show sasa1rcry
                                    hide sasa1c1
                                    show sasa1c1
                                    s "OUCH!!! *pain*"
                                    $ renpy.transition(dissolve)
                                    hide sasa1p2
                                    show sasa1p3
                                    hide sasa1c1
                                    show sasa1c1
                                    p "Hehe that feels good right?"
                                    $ renpy.transition(dissolve)
                                    hide sasa1p3
                                    show sasa1p2
                                    hide sasa1c1
                                    show sasa1c1
                                    p "And now. Lightning style!"
                                    $ renpy.transition(dissolve)
                                    hide sasa1p2
                                    show sasa1p3
                                    hide sasa1c1
                                    show sasa1c1
                                    show sasa1l1
                                    s "Yessssss! *Heavy moaning*"
                                    $ renpy.transition(dissolve)
                                    hide sasa1p2
                                    show sasa1p1
                                    hide sasa1rsad
                                    show sasa1rdow
                                    hide sasa1c1
                                    show sasa1c1
                                    hide sasa1l1
                                    show sasa1l1
                                    s "Do you like it? So more power!"
                                    $ renpy.transition(dissolve)
                                    hide sasa1p1
                                    show sasa1p2
                                    show sasa1l2
                                    hide sasa1rdow
                                    show sasa1rn
                                    hide sasa1lang
                                    show sasa1lshock
                                    hide sasa1c1
                                    show sasa1c1
                                    hide sasa1l1
                                    show sasa1l1
                                    p "Hehe... You both look so hot now!"
                                    $ renpy.transition(dissolve)
                                    hide sasa1p2
                                    show sasa1p3
                                    hide sasa1c1
                                    show sasa1c1
                                    hide sasa1l1
                                    show sasa1l1
                                    p "Just continue..."
                                    $ renpy.transition(dissolve)
                                    hide sasa1p3
                                    show sasa1p2
                                    hide sasa1lshock
                                    show sasa1lop
                                    hide sasa1c1
                                    show sasa1c1
                                    hide sasa1l1
                                    show sasa1l1
                                    sa "Mmmmmm... *moan*"
                                    $ renpy.transition(dissolve)
                                    hide sasa1p2
                                    show sasa1p1
                                    hide sasa1c1
                                    show sasa1c1
                                    hide sasa1l1
                                    show sasa1l1
                                    p "Huh what?"
                                    $ renpy.transition(dissolve)
                                    hide sasa1p1
                                    show sasa1p2
                                    hide sasa1c1
                                    show sasa1c1
                                    hide sasa1l1
                                    show sasa1l1
                                    sa "Yeesssss...."
                                    $ renpy.transition(dissolve)
                                    hide sasa1p2
                                    show sasa1p3
                                    hide sasa1c1
                                    show sasa1c1
                                    hide sasa1l1
                                    show sasa1l1
                                    p "Fuck... So hot!"
                                    $ renpy.transition(dissolve)
                                    hide sasa1p3
                                    show sasa1p2
                                    hide sasa1c1
                                    show sasa1c1
                                    hide sasa1l1
                                    show sasa1l1
                                    p "I just...."
                                    s "More!!!!"
                                    $ renpy.transition(dissolve)
                                    hide sasa1p2
                                    show sasa1p3
                                    hide sasa1rn
                                    show sasa1rorg
                                    show sasa1sp1
                                    hide sasa1l2
                                    hide sasa1c1
                                    show sasa1c1
                                    hide sasa1l1
                                    show sasa1l1
                                    p "Yeah! *spurt*"
                                    sa "....."
                                    s "More...."
                                    $ renpy.transition(dissolve)
                                    hide sasa1lop
                                    show sasa1lclop
                                    show sasa1sp2
                                    hide sasa1c1
                                    show sasa1c1
                                    hide sasa1l1
                                    show sasa1l1
                                    s "That was nice...."
                                    p "Ehm... Yes it was... But you should clean yourself now."
                                    s "*Lick*"
                                    $ renpy.transition(dissolve)
                                    hide sasa1sp1
                                    hide sasa1sp2
                                    hide sasa1rorg
                                    show sasa1rop
                                    hide sasa1rcry
                                    hide sasa1l1
                                    p "That was fast...."
                                    sa "...."
                                    p "Well, back to business now..."
                                    scene black with circleirisin               
                                    show nharem0 with circleirisout
                                    jump nharem
                                    
                                    
                                "Just squeez":
                                    $ renpy.transition(dissolve)
                                    show sasa1p1
                                    p "Yes, that feels so good..."
                                    p "I want to enjoy it..."
                                    $ renpy.transition(dissolve)
                                    hide sasa1p1
                                    show sasa1p2
                                    hide sasa1rn
                                    show sasa1rdow
                                    s "Do you like it?"
                                    p "Yes, you are so hot."
                                    $ renpy.transition(dissolve)
                                    hide sasa1p2
                                    show sasa1p3
                                    hide sasa1ln
                                    show sasa1lang
                                    p "Ehm. You are hot too Sakura."
                                    sa ".... *mumble*"
                                    $ renpy.transition(dissolve)
                                    hide sasa1p3
                                    show sasa1p2
                                    p "Yeah, I think so..."
                                    p "Enjoy time with Sarada..."
                                    $ renpy.transition(dissolve)
                                    hide sasa1p2
                                    show sasa1p1
                                    s "I just want to touch you..."
                                    $ renpy.transition(dissolve)
                                    hide sasa1p1
                                    show sasa1p2
                                    show sasa1t1
                                    hide sasa1rdow
                                    show sasa1rn
                                    p "Your nipple is so hard..."
                                    $ renpy.transition(dissolve)
                                    hide sasa1p2
                                    show sasa1p3
                                    show sasa1t3
                                    p "And Sarada boobs is so soft."
                                    $ renpy.transition(dissolve)
                                    hide sasa1p3
                                    show sasa1p2
                                    hide sasa1lang
                                    show sasa1lop
                                    sa "Mmmmm....*moan*"
                                    $ renpy.transition(dissolve)
                                    hide sasa1p2
                                    show sasa1p1
                                    show sasa1t2
                                    hide sasa1t1
                                    p "But nipple is hard!"
                                    $ renpy.transition(dissolve)
                                    hide sasa1p1
                                    show sasa1p2
                                    hide sasa1t2
                                    show sasa1t2
                                    s "Ouch!"
                                    $ renpy.transition(dissolve)
                                    hide sasa1p2
                                    show sasa1p3
                                    hide sasa1t2
                                    show sasa1t2
                                    p "Yes... It is just..."
                                    $ renpy.transition(dissolve)
                                    hide sasa1p3
                                    show sasa1p2
                                    hide sasa1t2
                                    show sasa1t2
                                    s "Aaaaaa.... *moan*"
                                    $ renpy.transition(dissolve)
                                    hide sasa1p2
                                    show sasa1p3
                                    hide sasa1rn
                                    show sasa1rorg
                                    show sasa1sp1
                                    hide sasa1t2
                                    show sasa1t2
                                    p "Yeah! *spurt*"
                                    sa "....."
                                    s "More...."
                                    $ renpy.transition(dissolve)
                                    hide sasa1lop
                                    show sasa1lclop
                                    show sasa1sp2
                                    hide sasa1t2
                                    show sasa1t2
                                    s "That was nice...."
                                    p "Ehm... Yes it was... But you should clean yourself now."
                                    s "*Lick*"
                                    $ renpy.transition(dissolve)
                                    hide sasa1sp1
                                    hide sasa1sp2
                                    hide sasa1t2
                                    hide sasa1t3
                                    hide sasa1rorg
                                    show sasa1rop
                                    p "That was fast...."
                                    p "Well, back to business now..."
                                    scene black with circleirisin               
                                    show nharem0 with circleirisout
                                    jump nharem
                        
                        
                        scene black with circleirisin               
                        show nharem0 with circleirisout
                        jump nharem
            else:
                "How you want to talk with her if she is not here?"
                scene black with circleirisin               
                show dharem0 with circleirisout
                jump dharem
                
        "Go back to the map":
            scene black with circleirisin               
            show dharem0 with circleirisout
            jump dharem 
                

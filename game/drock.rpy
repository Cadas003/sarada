# DAY %(p)s                      ROCK VILLAGE

label drock:

    scene drock0

    $ select = renpy.imagemap("drock0.jpg", "drock1.jpg", [
                                               (816, 72, 1094, 171, "gate"),
                                               (196, 229, 480, 345, "park"),
                                               (1432, 432, 1887, 561, "lab"),
                                               (710, 376, 1087, 471, "town"),
                                               (904, 670, 1238, 798, "village"),
                                               (1390, 950, 1460, 1015, "cheatc"),
                                               ])
    if select == "gate":
        menu:
            "Return to Konoha":
                "You leave the Iwagakure."
                scene black with circleirisin
                "After a day of traveling you come to the Konoha."
                $ day = day + 1
                show droom with circleirisout
                jump nday

            "Kunoichi":
                scene black with circleirisin
                show is1a with circleirisout
                jump is111

            "Работа":
                menu:
                    "Легко":
                        "Вы решаете помочь местным жителям с уборкой города."
                        "Вы заработали 100 рё."
                        $ ryo  = ryo + 100
                        jump nrock
                    "средний":
                        "Вы решили осмотреть деревню, чтобы поймать животных."
                        $ ryo  = ryo + 100 + taijutsu
                        "Вы успешно захватили дикого кабана."
                        jump nrock


                    "Сложный":
                        "Вы решаете защитить деревню и захватить вражеского шиноби."
                        $ ryo  = ryo + 100 + taijutsu + genjutsu
                        "Вы успешно победили все угрозы."
                        jump nrock

            "Hidden tree village":
                if kagumission >=10:
                    scene black with circleirisin
                    show dharem0 with circleirisout
                    jump dharem

                elif samuilove == 1:
                    scene black with circleirisin
                    show dharem0 with circleirisout
                    jump dharem
                else:
                    scene black with circleirisin
                    show dharemout with circleirisout
                    show mikb
                    show mikok
                    mik "Don't come any closer."
                    p "Why?"
                    mik "This village lives in peace. We didn't want a problem."
                    p "I will not bring any problems to you or village."
                    $ renpy.transition(dissolve)
                    hide mikok
                    show mikshar
                    mik "Sorry I have orders. No intruders. Please accept it and leave."
                    p "Ok... I don't want to put you in troubles."
                    mik "Thanks..."
                    p "But is there any options how I can enter this village? Is there anything you need?"
                    $ renpy.transition(dissolve)
                    hide mikshar
                    show mikok
                    mik "Hmmm..."
                    mik "Actually, yes... Our village is poor and we need a merchant that will invest in our town."
                    p "And???"
                    mik "If you can spend some Ryo you will be able to enter the city."
                    p "Hmmm... And how many Ryo I need to offer for entering the town?"
                    mik "Only 10 000..."
                    menu:
                        "Accept":
                            p "Hmmm..."
                            if ryo >=10000:
                                $ ryo  = ryo -10000
                                $ samuilove = 1
                                p "I think it is quite acceptable..."
                                p "Here is Ryo for the entering the town."
                                mik "Thanks... Now you can enter, but please don't do anything aggressive."
                                p "Sure..."
                                scene black with circleirisin
                                show dharem0 with circleirisout
                                jump dharem
                            else:
                                p "I think it is quite acceptable..."
                                p "But I don't have 10 000 Ryo."
                                mik "So come back when you have them..."
                                p "Ok...."
                                scene black with circleirisin
                                show drock0 with circleirisout
                                jump drock

                        "Too much":
                            p "Sorry but it is too much."
                            mik "Ok...Come back again if you change your mind..."
                            scene black with circleirisin
                            show drock0 with circleirisout
                            jump drock

            "Go to map":
                scene black with circleirisin
                show drock0 with circleirisout
                jump drock

    if select == "park":
        scene black with circleirisin
        show rpark with circleirisout
        jump rpark

    if select == "lab":
        if kushinamission == 0:
            scene black with circleirisin
            show rlab with circleirisout
            jump rocklab
        else:
            menu:
                "Go to the hospital":
                    scene black with circleirisin
                    show rlab with circleirisout
                    jump rocklab

                "Visit Kushina":
                    scene black with circleirisin
                    show rbad with circleirisout
                    jump rockclone



    if select == "town":
        if kagumission >=2:
            menu:
                "Visit Kaguay":
                    scene black with circleirisin
                    show rtown with circleirisout
                    jump rockkagud

                "Visit Kurotsuchi":
                    scene black with circleirisin
                    show rtown with circleirisout
                    jump rocktown


        else:

            scene black with circleirisin
            show rtown with circleirisout
            jump rocktown

    if select == "village":
        if tenmission == 0:
            "You go to the village center."
            $ tenmission =1
            "Hey!!!" with hpunch
            $ renpy.transition(dissolve)
            show ten0a
            show ten0ok
            te "%(p)s , Is it really you?"
            p "Tenten?"
            te "I know it! The jutsu is loosing power!"
            p "What are you talking about?"
            te "You were able to free from Kawaki jutsu."
            te "So there is an option that more people will break from it right?"
            p "Ehm... Sorry for disappointing you, but no."
            p "It looks like I posses some special kekkei genkai."
            $ renpy.transition(dissolve)
            hide ten0ok
            show ten0sad
            te "Shit... So there is not hope again?"
            p "There is still hope. If I learn to control this power, I believe that there is a chance to save everyone."
            te "Really?"
            $ renpy.transition(dissolve)
            hide ten0sad
            show ten0op
            te "Amazing! You must tell me everything you know about it!"
            p "Ok... but it is not too much right now."
            te "It doesn't matter... You must be hungry. Come with me, I will buy you something delicious."
            menu:
                "OK":
                    p "I can't say no to that."
                    te "Great. Jsut follow me..."
                    scene black with circleirisin
                    "You spend some time with Tenten and eat a good food."

                "No":
                    p "Sorry, but I do not have a time for that right now."
                    te "Really?"
                    p "Yes... But I will come back to visit you later."
                    te "Great. You can find me in the shop."
                    scene black with circleirisin
            show nrock0 with circleirisout
            jump nrock
        else:
            scene black with circleirisin
            show rday with circleirisout
            jump rshop

    if select == "cheatc":
        if cheatx >=10:
            menu cheat3:
                "Taijutsu +10":
                    $ taijutsu = taijutsu + 10
                    jump cheat3
                "Genjutsu +10":
                    $ genjutsu = genjutsu + 10
                    jump cheat3
                "Ninjutsu +10":
                    $ ninjutsu = ninjutsu + 10
                    jump cheat3
                "Namigan +10":
                    $ eyes = eyes + 10
                    jump cheat3
                "Chakra + 10":
                    $ chakra = chakra + 10
                    jump cheat3
                "Ryo + 10 000":
                    $ ryo = ryo + 10000
                    jump cheat3
                "Unlock hidden tree village":
                    $ kagumission = 10
                    jump cheat3
                "Complete character story":
                    "This is dangerous option and can break some important part of story."
                    menu:
                        "Mitsuka":
                            $ mitsukimission = 7
                            jump cheat3
                        "Kushina":
                            $ kushinamission = 9
                            jump cheat3
                        "Kurotsuchi":
                            $ kuroslave = 6
                            jump cheat3
                        "Tenten":
                            $ tenmission = 16
                            jump cheat3
                        "Kaguya":
                            $ kagumission = 9
                            jump cheat3

                        "Temari":
                            $ temamission = 11
                            jump cheat3

                        "Main story":
                            $ missionsa = 6
                            "You complete some main mission. Now is time to face Himawari."
                            jump cheat3
                        "Nothing":
                            jump cheat3

                "Nothing":
                    jump drock
        else:
            $ cheatx = cheatx +1
            jump drock





label rpark:
    scene rpark
    menu:
        "Look around":
            if kuroslave == 0:
                "You walk around the park..."
                "It is a beautiful place, but you didn't find anything interesting."
                scene black with circleirisin
                show drock0 with circleirisout
                jump drock
            else:
                "You decide to locate Kurotsuchi chakra."
                "You find her after a moment."
                $ renpy.transition(dissolve)
                show kuroa
                show kurook
                kr "Hello. So how can I help you?"
                if kuroslave == 1:
                    p "I want to test my Namigan on you."
                    kr "Ok... What should I do?"
                    p "Nothing. Just stay calm."
                    kr "OK...."
                    p "Namigan!!!"
                    if eyes <=30:
                        kr "...."
                        kr "That was it?"
                        $ kuroslave = 2
                        p "Ehm... NO... I am not sure...."
                        kr "Try it again..."
                        p "NAMIGAN!!!" with hpunch
                        kr "..."
                        p "Ehm... What ther fuck?"
                        "Your Namigan is not so strong! You need to improve it..."
                        p "It looks like I need to train it more."
                        kr "Probably. I am not sure how it should work but this was... weak..."
                        p "Yeah... Anyway, thanks for the help."
                        kr "No problem."
                        scene black with circleirisin
                        show nrock0 with circleirisout
                        jump nrock
                    else:
                        $ renpy.transition(dissolve)
                        hide kurook
                        show kurocl
                        kr "Arggg...."
                        $ kuroslave = 3
                        p "Is it working?"
                        $ renpy.transition(dissolve)
                        hide kurocl
                        show kuronok
                        kr ".."
                        p "Nice... It worked..."
                        kr "..."
                        p "So what should I do know?"
                        kr "..."
                        p "Can you say something?"
                        kr "..."
                        p "Looks like she is now only an empty doll."
                        p "Let's test if she will obey me... STRIP!"
                        kr "...."
                        $ renpy.transition(dissolve)
                        hide kuroa
                        show kurob
                        hide kuronok
                        show kuronsad
                        p "Nice... It was easy..."
                        p "Your boobs are small but at least not tiny."
                        kr "...."
                        p "You can dress now."
                        $ renpy.transition(dissolve)
                        hide kurob
                        show kuroa
                        hide kuronsad
                        show kuronok
                        kr "...."
                        p "Namigan - KAI!"
                        kr "That was it?"
                        $ renpy.transition(dissolve)
                        hide kuronok
                        show kurook
                        p "What?"
                        kr "As I think It will not work on me..."
                        p "You didn't remember what happened?"
                        kr "Something happened?"
                        p "You were under my namigan power."
                        $ renpy.transition(dissolve)
                        hide kurook
                        show kuroshock
                        kr "Really? I didn't feel anything."
                        p "Can I practice it on you later?"
                        kr "Sure... Just... It is weird, I can't remember anything."
                        $ renpy.transition(dissolve)
                        hide kuroshock
                        show kurook
                        kr "...."
                        p "It is normal... Now recover a little I will come back later... Thanks..."
                        scene black with circleirisin
                        show nrock0 with circleirisout
                        jump nrock

                if kuroslave == 2:
                    p "I want to test my Namigan on you."
                    kr "Again?Ok... What should I do this time?"
                    p "Nothing. Just stay calm."
                    kr "Do what you want..."
                    p "Namigan!!!"
                    if eyes <=30:
                        kr "...."
                        kr "That was it?"
                        $ kuroslave = 2
                        p "Ehm... NO... I am not sure...."
                        kr "Try it again..."
                        p "NAMIGAN!!!" with hpunch
                        kr "..."
                        p "Ehm... What ther fuck?"
                        "Your Namigan is not so strong! You need to improve it..."
                        p "It looks like I need to train it more."
                        kr "Probably. I am not sure how it should work but this was... weak..."
                        p "Yeah... Anyway, thanks for the help."
                        kr "No problem."
                        scene black with circleirisin
                        show nrock0 with circleirisout
                        jump nrock
                    else:
                        $ renpy.transition(dissolve)
                        hide kurook
                        show kurocl
                        kr "Arggg...."
                        $ kuroslave = 3
                        p "Is it working?"
                        $ renpy.transition(dissolve)
                        hide kurocl
                        show kuronok
                        kr ".."
                        p "Nice... It worked..."
                        kr "..."
                        p "So what should I do know?"
                        kr "..."
                        p "Can you say something?"
                        kr "..."
                        p "Looks like she is now only an empty doll."
                        p "Let's test if she will obey me... STRIP!"
                        kr "...."
                        $ renpy.transition(dissolve)
                        hide kuroa
                        show kurob
                        hide kuronok
                        show kuronsad
                        p "Nice... It was easy..."
                        p "Your boobs are small but at least not tiny."
                        kr "...."
                        p "You can dress now."
                        $ renpy.transition(dissolve)
                        hide kurob
                        show kuroa
                        hide kuronsad
                        show kuronok
                        kr "...."
                        p "Namigan - KAI!"
                        kr "That was it?"
                        $ renpy.transition(dissolve)
                        hide kuronok
                        show kurook
                        p "What?"
                        kr "As I think It will not work on me..."
                        p "You didn't remember what happened?"
                        kr "Something happened?"
                        p "You were under my namigan power."
                        $ renpy.transition(dissolve)
                        hide kurook
                        show kuroshock
                        kr "Really? I didn't feel anything."
                        p "Can I practice it on you later?"
                        kr "Sure... Just... It is weird, I can't remember anything."
                        $ renpy.transition(dissolve)
                        hide kuroshock
                        show kurook
                        kr "...."
                        p "It is normal... Now recover a little I will come back later... Thanks..."
                        scene black with circleirisin
                        show nrock0 with circleirisout
                        jump nrock

                if kuroslave >= 3:
                    p "I want to test my Namigan on you."
                    kr "Again? Ok... What should I do this time?"
                    p "Nothing. Just stay calm."
                    kr "Do what you want..."
                    p "Namigan!!!"
                    $ renpy.transition(dissolve)
                    hide kurook
                    show kuronok
                    kr "Arggg...."
                    p "Nice..."
                    p "I want to try something."
                    menu kurofuck12:
                        "Strip":
                            kr "..."
                            p "Ok... Show me your naked body."
                            kr "..."
                            if kuroslave == 3:
                                $ kuroslave = 4
                            p "NOW!"
                            $ renpy.transition(dissolve)
                            hide kuroa
                            show kurob
                            hide kuronok
                            show kuronsad
                            kr "..."
                            p "Looks good..."
                            kr "...."
                            p "But it is time to release it. First dress..."
                            $ renpy.transition(dissolve)
                            hide kurob
                            show kuroa
                            p "Namigan - KAI!"
                            kr "That was it?"
                            $ renpy.transition(dissolve)
                            hide kuronok
                            show kurook
                            p "Nothing again?"
                            kr "Ehmmm... What happened?"
                            p "I just test my Namigan on you. And it worked again."
                            kr "Something happened?"
                            p "Ehm... I try to talk to you, but you didn't respond."
                            $ renpy.transition(dissolve)
                            hide kurook
                            show kuroshock
                            kr "HUH? That sounds weird."
                            p "Yeah... I know... But it is ok. Trust me."
                            kr "Sure... Just... It is weird, I can't remember anything."
                            $ renpy.transition(dissolve)
                            hide kuroshock
                            show kurook
                            kr "...."
                            p "It is normal... Now recover a little I will come back later... Thanks..."
                            scene black with circleirisin
                            show nrock0 with circleirisout
                            jump nrock


                        "Kneel":
                            if eyes  <= 10:
                                "Your Namigan is too weak for this."
                                jump kurofuck12
                            else:
                                kr "..."
                                p "Ok... Now strip and get on your knees."
                                $ renpy.transition(dissolve)
                                hide kuroa
                                hide kuronok
                                show kuro1
                                show kuro1sad
                                p "Nice... I wonder what will happen when I touch you..."
                                $ renpy.transition(dissolve)
                                show kuro1h1
                                p "Nothing? How about this?"
                                $ renpy.transition(dissolve)
                                show kuro1h2
                                hide kuro1sad
                                show kuro1and
                                kr "Ahhh....*moan*"
                                p "Finally some reaction..."
                                if kuroslave == 4:
                                    $ kuroslave = 5
                                p "Now focus on the nipples...*twist*" with hpunch
                                $ renpy.transition(dissolve)
                                hide kuro1and
                                show kuro1op
                                kr "*moan*"
                                p "Hehe... *zip* I want to cum on your small boobs..."
                                $ renpy.transition(dissolve)
                                show kuro1p1
                                hide kuro1h2
                                p "Yes... Do you want it?"
                                $ renpy.transition(dissolve)
                                hide kuro1h1
                                hide kuro1op
                                show kuro1ok
                                kr "..."
                                p "Don't act like that, baby. You need something... Hmm.. Maybe..."
                                $ renpy.transition(dissolve)
                                show kuro1text
                                p "Yes, This is better..."
                                kr "...."
                                $ renpy.transition(dissolve)
                                show kuro1h1
                                p "Fuck, It is so good... Open your mouth now!"
                                $ renpy.transition(dissolve)
                                hide kuro1ok
                                show kuro1op
                                p "Yeah...*splurt*"
                                $ renpy.transition(dissolve)
                                show kuro1p2
                                hide kuro1h1
                                p "Heh..."
                                kr "....."
                                p "I was wondering if you react to this somehow...."
                                kr "...."
                                p "Still nothing... Time to clean you..."
                                $ renpy.transition(dissolve)
                                hide kuro1p2
                                hide kuro1p1
                                hide kuro1
                                hide kuro1op
                                hide kuro1text
                                p "And you can dress..."
                                $ renpy.transition(dissolve)
                                show kuroa
                                show kuronok
                                p "Namigan KAI!"
                                $ renpy.transition(dissolve)
                                show kuronok
                                show kurosad
                                kr "Huh... What was that?"
                                p "Do you feel something?"
                                kr "I am not sure.. But This time..."
                                kr "I smell something..."
                                p "Ehm... I am not sure what you mean..."
                                kr "..."
                                p "Anyway... It was funny... I will come back later.."
                                kr "What?"
                                p "Nothing... Thanks for your help."
                                kr "Sure... Bye..."
                                scene black with circleirisin
                                show nrock0 with circleirisout
                                jump nrock

                        "Fuck":
                            if eyes  <= 20:
                                "Your Namigan is too weak for this."
                                jump kurofuck12

                            else:
                                kr "uhm..."
                                if kuroslave == 5:
                                    $ kuroslave = 6
                                p "Ok... Now strip and get on all four."
                                $ renpy.transition(dissolve)
                                hide kuroa
                                hide kuronok
                                show kuro2a
                                show kuro2sad
                                p "Time to have some fun with you."
                                kr "..."
                                $ renpy.transition(dissolve)
                                show kuro2p1
                                p "You know what it mean right?"
                                $ renpy.transition(dissolve)
                                hide kuro2p1
                                show kuro2p2
                                hide kuro2sad
                                show kuro2cl
                                kr "Ouch... *pain*"
                                $ renpy.transition(dissolve)
                                hide kuro2p2
                                show kuro2p3
                                p "Finally some reaction!"
                                $ renpy.transition(dissolve)
                                hide kuro2p3
                                show kuro2p4
                                kr "Ahhh! *moan pain*"
                                $ renpy.transition(dissolve)
                                hide kuro2p4
                                show kuro2p3
                                p "It feels a little weird fucking you like this."
                                $ renpy.transition(dissolve)
                                hide kuro2p3
                                show kuro2p2
                                kr "Mmmm....*moan*"
                                $ renpy.transition(dissolve)
                                hide kuro2p2
                                show kuro2p3
                                p "I think I can do something else now."
                                $ renpy.transition(dissolve)
                                hide kuro2p3
                                show kuro2p4
                                kr "Oommmmm... *mumble moan*"
                                $ renpy.transition(dissolve)
                                hide kuro2p4
                                show kuro2p3
                                p "Maybe...."
                                menu kuroboobex:
                                    "Artist style":
                                        $ renpy.transition(dissolve)
                                        hide kuro2p3
                                        show kuro2p2
                                        p "I just want to fuck you."
                                        $ renpy.transition(dissolve)
                                        hide kuro2p2
                                        show kuro2p3
                                        p "Kage bunshin no jutsu!"
                                        $ renpy.transition(dissolve)
                                        hide kuro2p3
                                        show kuro2p4
                                        show kuro2p7
                                        hide kuro2cl
                                        show kuro2ok
                                        kr "Mmmm... *moan*"
                                        $ renpy.transition(dissolve)
                                        hide kuro2p4
                                        show kuro2p3
                                        p "But you still miss something."
                                        $ renpy.transition(dissolve)
                                        hide kuro2p3
                                        show kuro2p2
                                        p "Wait for a moment."
                                        $ renpy.transition(dissolve)
                                        hide kuro2p2
                                        show kuro2p3
                                        show kuro2text
                                        kr "Hmm??? *mumble*"
                                        $ renpy.transition(dissolve)
                                        hide kuro2p3
                                        show kuro2p4
                                        p "Yes... This looks better."


                                    "Water style":
                                        if expscroll ==0:
                                            p "I need expansion scroll for that."
                                            jump kuroboobex

                                        else:
                                            p "It's time to test my skills."
                                            $ renpy.transition(dissolve)
                                            hide kuro2p3
                                            show kuro2p2
                                            p "Expansion scroll activation!"
                                            $ renpy.transition(dissolve)
                                            hide kuro2p2
                                            hide kuro2a
                                            hide kuro2cl
                                            show kuro2b
                                            show kuro2sad
                                            show kuro2p2
                                            kr "Ahhh... *moan pain*"
                                            $ renpy.transition(dissolve)
                                            hide kuro2p2
                                            show kuro2p3
                                            p "Nice... But still want more!"
                                            $ renpy.transition(dissolve)
                                            hide kuro2p3
                                            show kuro2p4
                                            p "Kage bunshin no jutsu!"
                                            $ renpy.transition(dissolve)
                                            hide kuro2p4
                                            show kuro2p3
                                            show kuro2p7
                                            hide kuro2sad
                                            show kuro2ok
                                            kr "Mmmm... *moan*"
                                            $ renpy.transition(dissolve)
                                            hide kuro2p3
                                            show kuro2p2
                                            p "Water style jutsu!"
                                            $ renpy.transition(dissolve)
                                            hide kuro2p2
                                            show kuro2p3
                                            show kuro2w1
                                            kr "Ahhh...*moan*"
                                            p "Water explosion jutus!"
                                            $ renpy.transition(dissolve)
                                            hide kuro2p3
                                            show kuro2p4
                                            show kuro2w2
                                            kr "Yesss! *heavy moaning*"
                                            $ renpy.transition(dissolve)
                                            hide kuro2p4
                                            show kuro2p3
                                            p "Water dragoon jutsu!"
                                            $ renpy.transition(dissolve)
                                            hide kuro2p3
                                            show kuro2p4
                                            show kuro2w3


                                    "Expansion":
                                        if expscroll ==0:
                                            p "I need expansion scroll for that."
                                            jump kuroboobex
                                        else:
                                            p "It's time to test my skills."
                                            $ renpy.transition(dissolve)
                                            hide kuro2p3
                                            show kuro2p2
                                            p "Expansion scroll activation!"
                                            $ renpy.transition(dissolve)
                                            hide kuro2p2
                                            hide kuro2a
                                            hide kuro2cl
                                            show kuro2b
                                            show kuro2sad
                                            show kuro2p2
                                            kr "Ahhh... *moan pain*"
                                            $ renpy.transition(dissolve)
                                            hide kuro2p2
                                            show kuro2p3
                                            p "Nice... But still want more!"
                                            $ renpy.transition(dissolve)
                                            hide kuro2p3
                                            show kuro2p4
                                            p "Boob expansion level 2 !"
                                            $ renpy.transition(dissolve)
                                            hide kuro2p4
                                            hide kuro2b
                                            hide kuro2sad
                                            show kuro2c
                                            show kuro2sad
                                            show kuro2p4
                                            kr "Yessss... *heavy moaning*"
                                            $ renpy.transition(dissolve)
                                            hide kuro2p4
                                            show kuro2p3
                                            p "And now!"
                                            $ renpy.transition(dissolve)
                                            hide kuro2p3
                                            show kuro2p4
                                            p "Kage bunshin no jutsu!"
                                            $ renpy.transition(dissolve)
                                            hide kuro2p4
                                            show kuro2p3
                                            show kuro2p7
                                            hide kuro2sad
                                            show kuro2ok
                                            kr "Mmmm... *moan*"
                                            $ renpy.transition(dissolve)
                                            hide kuro2p3
                                            show kuro2p2
                                            p "I will use this! *clamp*"
                                            $ renpy.transition(dissolve)
                                            hide kuro2p2
                                            show kuro2p3
                                            show kuro2l1
                                            kr "Ahhh...*moan*"
                                            p "Lightning tingling jutus!"
                                            $ renpy.transition(dissolve)
                                            hide kuro2p3
                                            show kuro2p4
                                            show kuro2l2
                                            hide kuro2ok
                                            show kuro2ok
                                            kr "Yesss! *heavy moaning*"
                                            $ renpy.transition(dissolve)
                                            hide kuro2p4
                                            show kuro2p3
                                            p "Full power!!!"
                                            $ renpy.transition(dissolve)
                                            hide kuro2p3
                                            show kuro2p4
                                            show kuro2l3
                                kr "Ahhhhh... *heavy moaning*"
                                $ renpy.transition(dissolve)
                                hide kuro2p4
                                show kuro2p3
                                hide kuro2sad
                                hide kuro2ok
                                show kuro2cl
                                p "Fuck, you are really one of my favorite Kage!"
                                $ renpy.transition(dissolve)
                                hide kuro2p3
                                show kuro2p2
                                kr "Yesss.. *heavy moaning*"
                                $ renpy.transition(dissolve)
                                hide kuro2p2
                                show kuro2p3
                                p "You are definitely on the top five."
                                $ renpy.transition(dissolve)
                                hide kuro2p3
                                show kuro2p4
                                kr "Aaaa...*heavy moaning*"
                                $ renpy.transition(dissolve)
                                hide kuro2p4
                                show kuro2p3
                                p "Yeah!"
                                $ renpy.transition(dissolve)
                                hide kuro2p3
                                show kuro2p2
                                p "This is it!!! *splurt*"
                                $ renpy.transition(dissolve)
                                hide kuro2p2
                                show kuro2p1
                                show kuro2p5
                                hide kuro2cl
                                show kuro2ok
                                kr "Yesss...*heavy moaning*"
                                $ renpy.transition(dissolve)
                                show kuro2p6
                                p "Ahhh!!! *splurt*"
                                $ renpy.transition(dissolve)
                                show kuro2p8
                                kr "Mmm... *moan drip*"
                                p "Fuck! That was really good."
                                kr "..... *mumble*"
                                p "But I lost use too much chakra..."
                                p "Quick clean yourself and dress..."
                                $ renpy.transition(dissolve)
                                hide kuro2p1
                                hide kuro2p5
                                hide kuro2p6
                                hide kuro2p7
                                hide kuro2p8
                                hide kuro2a
                                hide kuro2b
                                hide kuro2c
                                hide kuro2cl
                                hide kuro2ok
                                hide kuro2l1
                                hide kuro2l2
                                hide kuro2l3
                                hide kuro2w1
                                hide kuro2w2
                                hide kuro2w3
                                hide kuro2text
                                p "Fuck, I really made a mess today."
                                with fade
                                "After a few minutes."
                                $ renpy.transition(dissolve)
                                show kuroa
                                show kuronok
                                p "Finally!"
                                kr "..."
                                p "Namigan KAI!"
                                $ renpy.transition(dissolve)
                                show kuronok
                                show kurosad
                                kr "Ahhghh..."
                                p "It was fun, right?"
                                kr "What is going on?"
                                p "Everything is fine now. I just use too much chakra today."
                                kr "Ahhh... *pain* My body, my boobs."
                                p "Your boobs?"
                                $ renpy.transition(dissolve)
                                show kurosad
                                show kuroouch
                                kr "I think I need some rest now."
                                p "Ok. Do whatever you want."
                                kr "...."
                                p "Anyway, thanks again for your help."
                                kr "Do not forget."
                                kr "I do it only because you promise to break Kawaki jutsu."
                                p "Yeah. Bye..."
                                scene black with circleirisin
                                show nrock0 with circleirisout
                                jump nrock




        "Relax":
            "You decide to relax a little in the park."
            "After some time you feel a weird feeling."
            "Your chakra is now a little stronger."
            $ chakra = chakra + 1
            "It was so refreshing."
            scene black with circleirisin
            show nrock0 with circleirisout
            jump nrock
        "Go to map":
            scene black with circleirisin
            show drock0 with circleirisout
            jump drock

#  ROCK KUSHINA LABEL
#  ROCK KUSHINA LABEL
#  ROCK KUSHINA LABEL
#  ROCK KUSHINA LABEL
#  ROCK KUSHINA LABEL

label rockclone:
    scene rbad
    if kushinamission == 1:
        $ renpy.transition(dissolve)
        show kusa
        show kusok
        ku "Hello %(p)s . Do you want to play?"
        p "Ehm... Sure, what do kind of game you want to play today?"
        ku "Dressing game!"
        p "That sounds good to me."
        ku "So did you bring me some clothes?"
        p "No. Why?"
        $ kushinamission = 2
        $ renpy.transition(dissolve)
        hide kusok
        show kussad
        ku "We can't play, dressing game if I don't have any clothes... You are dumb."
        p "Yeah. Sure. Can we talk about..."
        ku "I don't want to talk! Bring me some clothes!"
        p "...."
        scene black with circleirisin
        show nrock0 with circleirisout
        jump nrock

    if kushinamission >= 10:
        "Kushina is in your harem now."
        scene black with circleirisin
        show drock0 with circleirisout
        jump drock

    elif kushinamission == 2:
        $ renpy.transition(dissolve)
        show kusa
        show kusok
        ku "Hello %(p)s . Did you bring me some clothes?"
        p "No. I don't have any clothes for you."
        $ renpy.transition(dissolve)
        hide kusok
        show kussad
        ku "Come back when you have some!"
        p "*sigh* sure..."
        scene black with circleirisin
        show drock0 with circleirisout
        jump drock

    elif kushinamission == 3:
        $ renpy.transition(dissolve)
        show kusa
        show kusok
        ku "Hello %(p)s . Did you bring me some clothes?"
        p "Yes, I have some clothes for you."
        $ renpy.transition(dissolve)
        hide kusok
        show kussmile
        ku "Really!!! Give it to me!!!"
        p "Wait!!!"
        $ renpy.transition(dissolve)
        hide kusa
        hide kussmile
        p "Sure you can take it..."
        $ renpy.transition(dissolve)
        show kusb
        show kussmile
        ku "This one looks so good what do you think about them?"
        menu:
            "Looks good":
                p "I think this dress looks good on you..."
                p "Maybe if you..."
            "Didn't like it":
                p "I really didn't like them."
                p "You should try somet...."
        $ renpy.transition(dissolve)
        hide kusb
        hide kussmile
        p "...."
        $ renpy.transition(dissolve)
        show kusc
        show kussmile
        ku "And what about this one?"
        p "*sigh*"
        ku "You like them, don't you?"
        p "Sure... Why not..."
        $ kushinamission = 4
        $ renpy.transition(dissolve)
        hide kussmile
        show kussad
        ku "But what dress should I wear?"
        p "*sigh*"
        ku "Please pick one I can't decide."
        p "Really?"
        ku "Yes Pick One I will show them all to you."
        p "How?"
        $ renpy.transition(dissolve)
        hide kusc
        hide kussad
        ku "Just give me a moment."
        ku "Kage bunshin no jutsu!"
        p "huh???"
        $ renpy.transition(dissolve)
        show kusa:
            xalign 0.0 yalign 1.0
        show kusok:
            xalign 0.0 yalign 1.0
        $ renpy.transition(dissolve)
        show kusb
        show kussmile
        $ renpy.transition(dissolve)
        show kusc:
            xalign 1.0 yalign 1.0
        show kuscl:
            xalign 1.0 yalign 1.0
        p "Nice..."
        ku "So what dress you like the most?"
        menu:
            "Left":
                p "I think your original clothes was the best."
                $ kushinadress = 0
                ku "Really?"
                p "Yeah... It looks better on you."
                ku "Ok. I think you are right."

            "Middle":
                p "I really like that skirt. And the green color fit for your eyes."
                $ kushinadress = 1
                ku "You are so sweet. I will keep these clothes if you want."
                p "Yes... I like them most..."

            "Right":
                p "i like that new white top. You should keep it."
                $ kushinadress = 2
                ku "Are you sure about that?"
                p "Yeah... We can change it later if you didn't feel comfortable right?"
                ku "Yes...You are right."
        $ renpy.transition(dissolve)
        hide kusa
        hide kusb
        hide kusc
        hide kusok
        hide kussmile
        hide kuscl
        ku "Kai!!!"
        if kushinadress == 0:
            show kusa
        if kushinadress == 1:
            show kusb
        if kushinadress == 2:
            show kusc
        show kussmile
        ku "That was fun right?"
        p "Fun?"
        ku "You know, dressing new clothes and picking the best one."
        ku "We really should do it more often."
        p "*sigh*"
        p "I was hoping that this was the last..."
        ku "Come to be a little funnier!"
        p "..."
        ku "We can have a lot of fun together."
        p "I think we have a different ideas about the definition of the word fun."
        ku "*Humpf*"
        p "I need to go now..."
        $ renpy.transition(dissolve)
        hide kussmile
        show kussad
        ku "Wait!!!"
        ku "You can pick what we will do next time if you want."
        ku "Just visit me sometimes..."
        p "Yeah... Sure."
        scene black with circleirisin
        show nrock0 with circleirisout
        jump nrock

    else:
        $ renpy.transition(dissolve)
        if kushinadress == 0:
            show kusa
        if kushinadress == 1:
            show kusb
        if kushinadress == 2:
            show kusc
        show kusok
        ku "Hello %(p)s . Do you want to play?"
        menu kushinatalker:
            "Talk":
                if kushinamission == 4:
                    p "I want to ask you something."
                    $ renpy.transition(dissolve)
                    hide kusok
                    show kussad
                    ku "Ugh... Talking is boring, Lets do something funny instead."
                    $ kushinamission = 5
                    p "Come on... We will play later..."
                    ku "Ok, so what do you want to know?"
                    p "You are clnoe right?"
                    ku "I am not sure. What is clone?"
                    p "That mean you are cloned from the dna of the Kushina Uzumaki."
                    $ renpy.transition(dissolve)
                    hide kussad
                    show kuscl
                    ku "And what that mean?"
                    p "Ehm... That's mean your DNA was created in the lab... Or something like that."
                    p "...."
                    ku "What?"
                    p "I am not sure. Are you a clone or not?"
                    $ renpy.transition(dissolve)
                    hide kuscl
                    show kussad
                    ku "My head is hurting now."
                    p "*Sigh*"
                    p "Can you tell me something about yourself?"
                    ku "Sure... I like flowers and dress and unicorns and deserts and...."
                    p "Good to know... And how old are you?"
                    $ renpy.transition(dissolve)
                    hide kussad
                    show kusok
                    ku "They told me I am 25 years old."
                    p "Huh... Ok and where do you live?"
                    ku "What do you mean by that? I live here in this room!"
                    p "So you live in the hospital? 25 years."
                    ku "Yes..."
                    p "That must be pretty booring..."
                    ku "It is terribly boring... That is the reason I want to play with you."
                    p "Can you go outside?"
                    $ renpy.transition(dissolve)
                    hide kusok
                    show kussad
                    ku "..."
                    ku "No..."
                    p "Why?"
                    ku "They tell me it is too dangerous and I must stay here."
                    p "What if I came with you?"
                    $ renpy.transition(dissolve)
                    hide kussad
                    show kussmile
                    ku "That will be amazing!!!"
                    p "I will talk about it with Tsuchikage. Maybe she will allow it."
                    ku "Great! Let's go outside today!"
                    p "Wait! I need to talk with her first."
                    ku "Sure.... Go Go go... *chuckle*"
                    p "*sigh* Ok... Bye..."
                    scene black with circleirisin
                    show nrock0 with circleirisout
                    jump nrock

                elif kushinamission == 5:
                    p "I want to ask you something."
                    $ renpy.transition(dissolve)
                    hide kusok
                    show kussad
                    ku "Can we already go outside together?"
                    p "Ehm... no but..."
                    $ renpy.transition(dissolve)
                    hide kusok
                    show kussad
                    ku "Noooo!!! i want to go outside!!!"
                    p "Yeah but..."
                    ku "Get out!!!"
                    scene black with circleirisin
                    p "Shit I need to talk with Kurotsuchi."
                    show drock0 with circleirisout
                    jump drock

                elif kushinamission == 6:
                    p "I have some good news."
                    $ renpy.transition(dissolve)
                    hide kusok
                    show kusop
                    ku "Can we go outside together?"
                    $ kushinamission = 7
                    p "Yes...Tsuchikage approved it."
                    ku "That is amazing lets go!"
                    p "Ok... But you must stay close to me."
                    ku "Sure!!!"
                    scene black with circleirisin
                    "After some time...."
                    show rhall with circleirisout
                    $ renpy.transition(dissolve)
                    hide kusop
                    if kushinadress == 0:
                        show kusa
                    if kushinadress == 1:
                        show kusb
                    if kushinadress == 2:
                        show kusc
                    show kussmile
                    ku "Wow, this city is amazing. I never see so many new things!"
                    p "I am glad you are happy."
                    ku "Yes. I hope we will spend more days like this together."
                    p "Only if you are a good girl."
                    ku "Yes, I will be!"
                    p "Ok... it is time to go home... i will go with you..."
                    $ renpy.transition(dissolve)
                    hide kussmile
                    show kussad
                    ku "hmpf.... really?"
                    p "Yeah... but do not be sad. We will have more fun next time."
                    ku "Great!!!"
                    scene black with circleirisin
                    show nrock0 with circleirisout
                    jump nrock

                elif kushinamission == 8:
                    p "You look different today. Is everything alright?"
                    $ kushinamission = 9
                    $ renpy.transition(dissolve)
                    hide kusok
                    show kussad
                    ku "Yeah... I just..."
                    p "What?"
                    ku "I was wondering what is the life outside the village..."
                    p "I am not sure what you mean by that."
                    ku "It is amazing that you take me out of this room and show me new places."
                    ku "But somethimes I dream about leaving this town... You know... for day or two...."
                    p "I am not surprised. It is understapable that you want to see more of the world."
                    p "I can take you to the Konoha if you want."
                    $ renpy.transition(dissolve)
                    hide kussad
                    show kusop
                    ku "Really?"
                    p "Yeah, Tsuchikage already approved it so there is no problem. But..."
                    ku "But???"
                    p "You need to stay close to me and obey my orders."
                    ku "I understant."
                    p "Good..."
                    ku "So when can we go?"
                    p "Just give me some time I need to finish something here first."
                    ku "I'll be waiting here for you."
                    p "Ok... See you later."
                    scene black with circleirisin
                    show nrock0 with circleirisout
                    jump nrock
                else:
                    p "I want to ask you something."
                    $ renpy.transition(dissolve)
                    hide kusok
                    show kussad
                    if kushinamission >= 9:
                        ku "We are going to the Konoha?"
                        menu:
                            "Yes":
                                p "Yes. We can go..."
                                ku "Awesome!!!"
                                scene black with circleirisin
                                "You leave the hidden rock village with Kushina."
                                $ day = day + 1
                                show nmap0 with circleirisout
                                "And after some time finally reach the Konoha village. You spend whole day here showing Kushina every peace of the village."
                                $ renpy.transition(dissolve)
                                hide kusa
                                hide kusb
                                hide kusc
                                hide kusok
                                hide kussmile
                                hide kuscl
                                if kushinadress == 0:
                                    show kusa
                                if kushinadress == 1:
                                    show kusb
                                if kushinadress == 2:
                                    show kusc
                                show kusok
                                ku "Thank you %(p)s for taking me here..."
                                p "No problem. But it is time to go back to the Iwagakure."
                                ku "Yes, I know... Before we go sleep... Can you buy me a drink?"
                                p "Sure... I know one bar here.."
                                ku "Sweet..."
                                scene black with circleirisin
                                show nbar with circleirisout
                                $ renpy.transition(dissolve)
                                hide kusa
                                hide kusb
                                hide kusc
                                hide kusok
                                show samuia:
                                    xalign 1.0 yalign 1.0
                                show samuiorg:
                                    xalign 1.0 yalign 1.0
                                sam "Hehe... Who is this hot woman??? Isn't it my friend Kushina?"
                                p "Ehm... Your friend?"
                                sam "Sure... I know her from... where it was??? hehe..."
                                p "It looks like you are drunk..."
                                $ renpy.transition(dissolve)
                                if kushinadress == 0:
                                    show kusa:
                                        xalign 0.0 yalign 1.0
                                if kushinadress == 1:
                                    show kusb:
                                        xalign 0.0 yalign 1.0
                                if kushinadress == 2:
                                    show kusc:
                                        xalign 0.0 yalign 1.0
                                show kusok:
                                    xalign 0.0 yalign 1.0
                                ku "You are funny..."
                                sam "Come on sweetie... Lets drink with me..."
                                ku "Yes!!!"
                                p "This looks interesting...."
                                with fade
                                "Girls start to drink really hard..."
                                with fade
                                "It is hard to tell because Samui was already pretty drunk..."
                                $ renpy.transition(dissolve)
                                hide kusa
                                hide kusb
                                hide kusc
                                hide kusok
                                hide samuia
                                hide samuiorg
                                "After some drinks Samui starts to have some notes about having a threesome."
                                if kushinalove >=6:
                                    ku "That sounds good... But I need more drink for it."
                                    p "No problem..."
                                    with fade
                                    "After some time..."
                                    $ renpy.transition(dissolve)
                                    show kussa
                                    show kussakok
                                    show kussashap
                                    sam "Hehe... Look at her... What a nice boobs."
                                    ku "Hmmmmm.... *sleepy*"
                                    sam "Looks like she is tired... What you want to do now?"
                                    p "I have one idea..."
                                    p "Kage bunshin no jutsu!"
                                    $ renpy.transition(dissolve)
                                    show kussapk1
                                    show kussaps1
                                    show kussap1
                                    sam "Hehe... Nice..."
                                    $ renpy.transition(dissolve)
                                    hide kussapk1
                                    show kussapk2
                                    hide kussaps1
                                    show kussaps2
                                    ku "mhmmmm...*mumble*"
                                    $ renpy.transition(dissolve)
                                    hide kussapk2
                                    show kussapk3
                                    hide kussaps2
                                    show kussaps3
                                    sam "Yes... Put it deeper!"
                                    $ renpy.transition(dissolve)
                                    hide kussapk3
                                    show kussapk4
                                    hide kussaps3
                                    show kussaps4
                                    hide kussakok
                                    show kussakop
                                    ku "MMMM...*sleepy moaning*"
                                    $ renpy.transition(dissolve)
                                    hide kussapk4
                                    show kussapk3
                                    hide kussaps4
                                    show kussaps3
                                    hide kussashap
                                    show kussasop
                                    sam "Yes!!! Just like that!!"
                                    $ renpy.transition(dissolve)
                                    hide kussapk3
                                    show kussapk2
                                    hide kussaps3
                                    show kussaps2
                                    p "This is perfect!"
                                    $ renpy.transition(dissolve)
                                    hide kussapk2
                                    show kussapk3
                                    hide kussaps2
                                    show kussaps3
                                    hide kussakop
                                    show kussakhap
                                    ku "*mumble* this again *moan*"
                                    $ renpy.transition(dissolve)
                                    hide kussapk3
                                    show kussapk4
                                    hide kussaps3
                                    show kussaps4
                                    hide kussasop
                                    show kussassad
                                    sam "Fuck this is so good!"
                                    $ renpy.transition(dissolve)
                                    hide kussapk4
                                    show kussapk3
                                    hide kussaps4
                                    show kussaps3
                                    p "I want to try something... *scratch*"
                                    $ renpy.transition(dissolve)
                                    hide kussapk3
                                    show kussapk2
                                    hide kussaps3
                                    show kussaps2
                                    show kussatext
                                    p "Yes this is better..."
                                    $ renpy.transition(dissolve)
                                    hide kussapk2
                                    show kussapk3
                                    hide kussaps2
                                    show kussaps3
                                    hide kussassad
                                    show kussasouch
                                    sam "What is this? Hehe you are so dirty..."
                                    $ renpy.transition(dissolve)
                                    hide kussapk3
                                    show kussapk4
                                    hide kussaps3
                                    show kussaps4
                                    hide kussakhap
                                    show kussakorg
                                    ku "MMMM....*moan* Harder..."
                                    $ renpy.transition(dissolve)
                                    hide kussapk4
                                    show kussapk3
                                    hide kussaps4
                                    show kussaps3
                                    hide kussasouch
                                    show kussasorg
                                    sam "Yeah*moan* she is right... I will..."
                                    $ renpy.transition(dissolve)
                                    hide kussapk3
                                    show kussapk2
                                    hide kussaps3
                                    show kussaps2
                                    show kussap2
                                    p "SHit it is too hot!!!*splurt*"
                                    $ renpy.transition(dissolve)
                                    hide kussapk2
                                    show kussapk3
                                    hide kussaps2
                                    show kussaps3
                                    show kussap3
                                    ku "Ahhhh..."
                                    $ renpy.transition(dissolve)
                                    hide kussapk3
                                    show kussapk4
                                    hide kussaps3
                                    show kussaps4
                                    show kussaps5
                                    p "And more!!!!*splurt*"
                                    $ renpy.transition(dissolve)
                                    show kussaps6
                                    show kussapk5
                                    sam "Yeah...*drip*"
                                    $ renpy.transition(dissolve)
                                    show kussapk6
                                    p "Fuck... This is everything I have..."
                                    ku "Mmmm..."
                                    sam "So much sperm... Feels so good..."
                                    ku "zzzzzz...."
                                    p "Fuck... Looks like she fall asleep... What is wrong with her?"
                                    $ renpy.transition(dissolve)
                                    hide kussasorg
                                    show kussashap
                                    sam "Maybe she is just too drunk... I will help you with her... Just pull it out first."
                                    sam "Or do you want second round?"
                                    scene black with circleirisin
                                    "You decide to fuck Samui one more time... Then she fall asleep too It was too exhausting for her."
                                    "You take Kushina to your home and clean her... Then  take her back to Iwagakure next day."
                                    show nrock0 with circleirisout
                                    jump nrock
                                else:
                                    "But Kushina didn't fall for it."
                                    "Maybe if you improve her relationship with her..."
                                    "You take Kushina to your home and go with her back to Iwagakure next day."
                                    scene black with circleirisin
                                    show nrock0 with circleirisout
                                    jump nrock

                            "No":
                                p "Ehm... No I am still not ready..."
                                ku "So come back when you are ready... Or do you want something else?"
                                jump kushinatalker
                    else:
                        ku "Hmpf... Ok.. What do you want to know?"
                        "Fuck there is nothing what I want to know about her right now...."
                        p "Ehm.... How do you feel?"
                        ku "Pretty good actually when you are with me."
                        $ renpy.transition(dissolve)
                        hide kussad
                        show kusok
                        ku "Anything else?"
                        jump kushinatalker

            "Change dress":
                p "I think you should change your dress..."
                ku "Yeah you are right..."
                $ renpy.transition(dissolve)
                hide kusa
                hide kusb
                hide kusc
                hide kusok
                hide kussmile
                hide kuscl
                ku "Just give me a moment."
                ku "Kage bunshin no jutsu!"
                p "..."
                $ renpy.transition(dissolve)
                show kusa:
                    xalign 0.0 yalign 1.0
                show kusok:
                    xalign 0.0 yalign 1.0
                $ renpy.transition(dissolve)
                show kusb
                show kussmile
                $ renpy.transition(dissolve)
                show kusc:
                    xalign 1.0 yalign 1.0
                show kuscl:
                    xalign 1.0 yalign 1.0
                p "Nice..."
                ku "So what dress you like the most?"
                menu:
                    "Left":
                        p "I think your original clothes was the best."
                        $ kushinadress = 0
                        ku "Really?"
                        p "Yeah... It looks better on you."
                        ku "Ok. I think you are right."

                    "Middle":
                        p "I really like that skirt. And the green color fit for your eyes."
                        $ kushinadress = 1
                        ku "You are so sweet. I will keep these clothes if you want."
                        p "Yes... I like them most..."

                    "Right":
                        p "i like that new white top. You should keep it."
                        $ kushinadress = 2
                        ku "Are you sure about that?"
                        p "Yeah... We can change it later if you didn't feel comfortable right?"
                        ku "Yes...You are right."
                $ renpy.transition(dissolve)
                hide kusa
                hide kusb
                hide kusc
                hide kusok
                hide kussmile
                hide kuscl
                ku "Kai!!!"
                if kushinadress == 0:
                    show kusa
                if kushinadress == 1:
                    show kusb
                if kushinadress == 2:
                    show kusc
                show kusok
                ku "That was fun right?"
                p "Yeah..."
                ku "So what do you want to do now?"
                jump kushinatalker

            "Have fun":
                if kushinamission <=6:
                    p "Yeah. There a lot of things  I want to do with her."
                    p "But I need to gain her trust first before I try something."
                    jump kushinatalker

                elif kushinamission == 7:
                    p "I have some ideas what we can do together."
                    $ kushinamission = 8
                    $ kushinalove = 1
                    ku "Do you want to go out with me?"
                    p "Yes... But first I want to try something else."
                    $ renpy.transition(dissolve)
                    hide kusok
                    show kusop
                    ku "What?"
                    p "Do you remember our dressing game?"
                    ku "Yes..."
                    p "I want to show you similiar game."
                    $ renpy.transition(dissolve)
                    hide kusop
                    show kusok
                    ku "What kind of game is it?"
                    p "I will show you first you need to take off your clothes."
                    $ renpy.transition(dissolve)
                    hide kusok
                    show kussad
                    ku "Why?"
                    p "Do you want to go outside?"
                    ku "Yes but..."
                    p "Then do what I say!"
                    ku "Sure..."
                    $ renpy.transition(dissolve)
                    hide kusa
                    hide kusb
                    hide kusc
                    hide kussad
                    show kusd
                    show kussad
                    show kusshy
                    ku "And what now?"
                    $ renpy.transition(dissolve)
                    show kush1
                    hide kussad
                    show kuscl
                    ku "Argggg *moan*"
                    p "Shit, Your boobs are so soft..."
                    ku "Don't grab them like this!"
                    p "Sorry maybe i should...*pinch*"
                    $ renpy.transition(dissolve)
                    show kush2
                    ku "Ahhh....*moan* that feels weird..."
                    p "Good right? *squeeze*"
                    ku "Yess... *moan* I feel a weird pressure..."
                    p "Where?"
                    ku "In my boobs and.... ahhhh...."
                    ku "*heavy moaning*"
                    ku "*squirt*"
                    $ renpy.transition(dissolve)
                    hide kuscl
                    show kusorg
                    show kusm1
                    ku "Yesss!!!*heavy moaning*"
                    p "Wow! I do not know you are so sensitive..."
                    ku "Ahhhh!!!!*moan*"
                    p "...."
                    $ renpy.transition(dissolve)
                    hide kush1
                    hide kush2
                    hide kusm1
                    show kusm2
                    ku "That was so good...."
                    p "I told you! Right?"
                    ku "Yesss...*moan dizzy*"
                    $ renpy.transition(dissolve)
                    hide kusorg
                    show kuscl
                    p "Do you want to go outside now?"
                    ku "Mmmm... Yes... Go out..."
                    p "Good so dress up and we can go..."
                    ku "Sure....."
                    scene black with circleirisin
                    "You spend the whole day with Kushina... She looks a little different now."
                    "She still want to hold your hand."
                    show nrock0 with circleirisout
                    jump nrock

                else:
                    p "Do you want to go out with me?"
                    $ renpy.transition(dissolve)
                    hide kusok
                    show kusop
                    ku "Yes, Yes Lets go!"
                    p "But first I want to play with your body a little..."
                    ku "That will be fun!!!"
                    $ renpy.transition(dissolve)
                    hide kusa
                    hide kusb
                    hide kusc
                    hide kusop
                    show kusd
                    show kussmile
                    show kusshy
                    ku "What do you want to do?"
                    menu kushinafucker:
                        "Play with boobs":
                            p "Can I touch your boobs?"
                            ku ".... Yes... It was fun last time..."
                            p "Ok....*squeeze*"
                            $ renpy.transition(dissolve)
                            show kush1
                            hide kussmile
                            show kuscl
                            ku "Argggg *moan*"
                            p "Your boobs are so soft..."
                            ku "MMM...*moan* Pich my nipples!!!"
                            p "If you want it..*pinch*"
                            $ renpy.transition(dissolve)
                            show kush2
                            ku "Ahhh....*moan* that feels good..."
                            p "Hehe... *squeeze*"
                            ku "Yess... *moan* that.... pressure..."
                            p "*squeeze*"
                            ku "My boobs.... ahhhh...."
                            ku "They are going to explode... *heavy moaning*"
                            ku "*squirt*"
                            $ renpy.transition(dissolve)
                            hide kuscl
                            show kusorg
                            show kusm1
                            ku "Yesss!!!*heavy moaning*"
                            p "Wow! You are so sensitive..."
                            ku "Ahhhh!!!!*moan*"
                            p "...."
                            $ renpy.transition(dissolve)
                            hide kush1
                            hide kush2
                            hide kusm1
                            show kusm2
                            ku "That was so good...."
                            p "I told you! Right?"
                            ku "Yesss...*moan dizzy*"
                            $ renpy.transition(dissolve)
                            hide kusorg
                            show kuscl
                            p "Do you want to go outside now?"
                            ku "Mmmm... Yes... Go out..."
                            p "Just dress up and we can go..."
                            ku "Dress up..."
                            scene black with circleirisin
                            "You spend the whole day with Kushina..."
                            "She still want to hold your hand."
                            show nrock0 with circleirisout
                            jump nrock

                        "Slash her":
                            if whip ==0:
                                "You need to buy whip first!"
                                "You can do it in the shop."
                            elif kushinaslash ==0:
                                p "I bring something new today."
                                ku "What is it?"
                                p "This beautifuill whip."
                                ku "It looks shiny... what do you want to do with it?"
                                $ kushinaslash = 1
                                p "This..."
                                "*Slash*"with hpunch
                                hide kussmile
                                show kuscl
                                show kussc1
                                ku "OUCH!!!!"
                                "You want to slash her again...."
                                ku "Auu.... No!!!"
                                p "Huh???"
                                $ renpy.transition(dissolve)
                                hide kuscl
                                show kuscry
                                ku "That hurt!!!! Please do not hit me again."
                                p "Do not worry you will like it..."
                                ku "No! It is hurting me... Please..."
                                p "One more time..."
                                ku "*sob*"
                                p "...."
                                p "Come on stop crying..."
                                ku "Buhuuu...*sob sob*"
                                p "I will not hit you again... I use this potion on you, and it will not hurt anymore..."
                                ku "*sob*"
                                $ renpy.transition(dissolve)
                                hide kussc1
                                p "How do you feel now?"
                                ku "*sob* It still hurt... But it is better now..."
                                p "Ok... We can go out now if you want..."
                                $ renpy.transition(dissolve)
                                hide kuscry
                                show kuscl
                                ku "*snivel* Ok.... I want to go out... But do not hurt me again..."
                                p "Ok..."
                                scene black with circleirisin
                                "That was a weird day."
                                "Kushina has been always behind you with an uncertain look."
                                show nrock0 with circleirisout
                                jump nrock
                            else:
                                p "I have one toy here."
                                ku "What is it?"
                                p "This beautifuill whip."
                                $ renpy.transition(dissolve)
                                hide kussmile
                                show kussad
                                ku "Oh no!!! Please not this again..."
                                p "Come on you will like it..."
                                ku "No please... It hurts so much last time!"
                                p "Just one time and then...."
                                "*Slash*"with hpunch
                                hide kussad
                                show kuscl
                                show kussc1
                                ku "OUCH!!!!*pain*"
                                p "Is it better now?"
                                $ renpy.transition(dissolve)
                                hide kuscl
                                show kuscry
                                ku "No it still hurt... Pleas not again...*sob*"
                                p "Come on do not act like a child..."
                                ku "*cry weep*"
                                p "Kushina..."
                                ku "*sob*"
                                p "Come on stop crying..."
                                ku "Buhuuu...*sob sob*"
                                p "I will not hit you again... I use this potion on you, and it will not hurt anymore..."
                                ku "*sob*"
                                $ renpy.transition(dissolve)
                                hide kussc1
                                p "Is it better now?"
                                ku "*sob* It still hurt so much... I want to go out now."
                                p "Ok... But do not cry anymore ok?"
                                $ renpy.transition(dissolve)
                                hide kuscry
                                show kuscl
                                ku "*snivel* Ok.... But do not hurt me again..."
                                p "Sure."
                                scene black with circleirisin
                                "That was a weird day."
                                "Kushina has been always behind you with an uncertain look."
                                show nrock0 with circleirisout
                                jump nrock

                        "Use pen":
                            if kushinalove ==1:
                                p "I want to try something new today."
                                $ kushinalove = 2
                                ku "And what is it?"
                                p "Just close your eyes I will show you..."
                                $ renpy.transition(dissolve)
                                hide kussmile
                                show kussad
                                ku "It will not hurt right?"
                                p "Sure. Do not worry..."
                                ku "Ok..."
                                $ renpy.transition(dissolve)
                                hide kussad
                                show kuscl
                                ku "And what now???"
                                p "*drawing*"
                                ku "What are you doing? *giggling* It is tickling me.."
                                p "Just one moment..."
                                $ renpy.transition(dissolve)
                                show kust1
                                p "You can open your eyes now..."
                                $ renpy.transition(dissolve)
                                hide kuscl
                                show kussad
                                ku "huh???"
                                $ renpy.transition(dissolve)
                                hide kussad
                                show kussmile
                                ku "This look amazing!"
                                p "You like it?"
                                ku "Yes... What you draw there? Is something like temporary tattoo?"
                                p "Ehm... No it is just normal marker... you can wash it if you want.."
                                ku "No... Draw some more symbols on my body!"
                                p "Symbols? huh... Ok..."
                                p "*drawing*"
                                ku "Hehe... *giggling* it is funny..."
                                p "Just one moment..."
                                $ renpy.transition(dissolve)
                                show kust2
                                ku "This is looking even better!!!"
                                p "You like it?"
                                ku "Yeah! I am like some kind of..."
                                $ renpy.transition(dissolve)
                                hide kussmile
                                show kuscl
                                ku "ehm...."
                                p "Maybe I can finish that sentence."
                                ku "What???"
                                p "Nothing, We can go out if you want. Just wash yourself first..."
                                $ renpy.transition(dissolve)
                                hide kuscl
                                show kusok
                                ku "No... I like this! I will wash myself later!"
                                p "Ok... But it will not be good if anyone will see it, ok?"
                                ku "Sure I will be carefull..."
                                scene black with circleirisin
                                "You spend another good day with Kushina... She checks often her new marks."
                                show nrock0 with circleirisout
                                jump nrock
                            else:
                                p "I bring you something today.."
                                ku "And what is it?"
                                p "This marker"
                                $ renpy.transition(dissolve)
                                hide kussmile
                                show kusok
                                ku "You will draw something on my body again?"
                                p "Yes... how do you know?"
                                ku "hehe"
                                $ renpy.transition(dissolve)
                                hide kusok
                                show kusop
                                ku "You can start... I like that feeling!"
                                p "*drawing*"
                                ku "*giggling* hehe..."
                                $ renpy.transition(dissolve)
                                show kust1
                                p "How do you like it?"
                                $ renpy.transition(dissolve)
                                hide kusop
                                show kussmile
                                ku "Hehe... It is nice."
                                ku "I want more!"
                                p "I have no problem with that..."
                                p "*drawing*"
                                ku "Hehe... *giggling* it feels good..."
                                p "Just one moment..."
                                $ renpy.transition(dissolve)
                                show kust2
                                ku "Wow! It's so much prettier than before!"
                                p "Yes. It looks really good on you."
                                $ renpy.transition(dissolve)
                                hide kussmile
                                show kuscl
                                ku "Thank you. Can we go out now?"
                                p "Sure... Just dress first..."
                                $ renpy.transition(dissolve)
                                hide kuscl
                                show kusok
                                ku "Sure give me moment..."
                                scene black with circleirisin
                                "You spend another good day with Kushina... She checks often her new marks."
                                show nrock0 with circleirisout
                                jump nrock
                        "Use dildo":
                            if kushinalove ==1:
                                "Try to draw something on her body first..."
                                jump kushinafucker
                            elif kushinalove ==2:
                                p "I prepared something extra for you today!"
                                $ kushinalove = 3
                                ku "What?"
                                p "Do you want to enjoy a whole new experience today?"
                                ku "Sure!!!"
                                p "Do you know what is this?"
                                $ renpy.transition(dissolve)
                                hide kussmile
                                show kusok
                                ku "Hmmm... Give it to me...."
                                p "Sure...."
                                ku "...."
                                "Kushina turn dildo on."
                                $ renpy.transition(dissolve)
                                hide kusok
                                show kusshock
                                ku "hu???"
                                "*bzmmm*"
                                p "Let me show you how it work..."
                                "You grab the dildo and slowly start to move it on Kushina body."
                                $ renpy.transition(dissolve)
                                hide kusshock
                                show kussmile
                                ku "mmmmm... *moan* That feels good..."
                                ku "Is it some kind of massage device?"
                                p "Sure you can call it that way...."
                                "You slowly move it to her pussy."
                                $ renpy.transition(dissolve)
                                hide kussmile
                                show kuscl
                                show kusd1
                                ku "Ahhh... *moan* That is so good...*moan*"
                                "*splash*"
                                $ renpy.transition(dissolve)
                                hide kuscl
                                show kusdildo
                                show kusorg
                                ku "Yeass...*moan*"
                                p "Looks like you're enjoying it."
                                ku "Mmmm....*heavy moaning*"
                                $ renpy.transition(dissolve)
                                show kusd2
                                ku "Yesss!!!*squirt*"
                                $ renpy.transition(dissolve)
                                show kusdildoorg
                                ku "Ahhhh....*moan squirt*" with hpunch
                                p "Nice...."
                                "Kushina lean to you and kiss you..."
                                "*smooch*"
                                ku "That was amazing..."
                                ku "I never feel like this when I do it alone.... *heavy breathing*"
                                p "You did this alone?"
                                ku "Yes...*exhale* I need to do something when I am all day alone in the room."
                                p "Heh... I undertsant that!!!"
                                ku "*moan*"
                                p "So what now? Do you still want to go out?"
                                ku "Yes... *heavy breathing* just give me a moment."
                                scene black with circleirisin
                                "You spend another good day with Kushina..."
                                "It was fun... "
                                "Hmm... I wonder, how she loose her virginity?"
                                show nrock0 with circleirisout
                                jump nrock
                            else:
                                p "I bring you your favorite toy today!"
                                ku "What it is? That massage device? Or marker?"
                                p "I think you know how to use it..."
                                ku "Hehe... Yes... but it is better when you hold it..."
                                ku "I mean, if you want...."
                                $ renpy.transition(dissolve)
                                hide kussmile
                                show kusok
                                p "I can do that for you but first.."
                                "*smooch*"
                                $ renpy.transition(dissolve)
                                hide kusok
                                show kusop
                                ku "Mmmm... That was nice... Now turn it on please..."
                                "*bzmmm*"
                                "You turn on dildo and continue with the kissing Kushinas body."
                                $ renpy.transition(dissolve)
                                hide kusop
                                show kussmile
                                ku "mmmmm... *moan* That feels good..."
                                ku "Just..."
                                "Kushina grab your hand with a dildo and move it to her pussy."
                                $ renpy.transition(dissolve)
                                hide kussmile
                                show kuscl
                                show kusd1
                                ku "Stick it in please....*moan*"
                                "*splash*"
                                $ renpy.transition(dissolve)
                                hide kuscl
                                show kusdildo
                                show kusorg
                                ku "Yeass...*moan*"
                                p "...."
                                ku "Mmmm*smooch*...."
                                $ renpy.transition(dissolve)
                                show kusd2
                                ku "Yesss!!!*squirt*"
                                $ renpy.transition(dissolve)
                                show kusdildoorg
                                ku "Ahhhh....*moan squirt*" with hpunch
                                p "Nice...."
                                "Kushina lean to you and kiss you..."
                                "*smooch*"
                                ku "That was amazing..."
                                p "..."
                                ku "Just.... mmmmm *moaning*"
                                "Kushina kiss you again."
                                "*Smooch*"
                                ku "Can you take me somewhere else now?"
                                p "Ehm... Sure... But get dressed..."
                                ku "Yeah... Dress..."
                                scene black with circleirisin
                                "You spend another good day with Kushina..."
                                "Every time when you two was alone, she kiss you... "
                                show nrock0 with circleirisout
                                jump nrock

                        "Fuck her":
                            if kushinalove <=2:
                                p "Good idea, but try to get her trust first."
                                jump kushinafucker

                            elif kushinalove ==3:
                                p "I prepared something extra for you today!"
                                $ kushinalove = 4
                                ku "Yes? What?"
                                p "Just calm down. Do you see that before?*zap*"
                                "You drop your pants."
                                $ renpy.transition(dissolve)
                                hide kussmile
                                show kusok
                                ku "Hm.... Looks like you have something down there..."
                                p "Ehm... Yes... it is..."
                                ku "Just kidding! I know that man has a penis."
                                p "Sure... But do you know what to do with it???"
                                $ renpy.transition(dissolve)
                                hide kusok
                                show kusop
                                ku "Yes... ehm...."
                                p "Just calm down and lay on the bed."
                                ku "Sure...."
                                $ renpy.transition(dissolve)
                                hide kusop
                                hide kusa
                                hide kusb
                                hide kusc
                                hide kusd
                                hide kusshy
                                ku "..."
                                $ renpy.transition(dissolve)
                                show kus1a
                                show kus1sad
                                show kus1shy
                                ku "What now?"
                                p "We should start with something you know like..."
                                $ renpy.transition(dissolve)
                                hide kus1a
                                hide kus1sad
                                hide kus1shy
                                show kus1b
                                show kus1sad
                                show kus1shy
                                p "You like when I grab your boobs right?"
                                $ renpy.transition(dissolve)
                                hide kus1sad
                                show kus1cl
                                ku "Yes... It feels good..."
                                p "And what if I do this?"
                                $ renpy.transition(dissolve)
                                show kus1tf1
                                ku "Do what?"
                                $ renpy.transition(dissolve)
                                hide kus1tf1
                                show kus1tf2
                                ku "You just put it between my boobs?"
                                p "..."
                                $ renpy.transition(dissolve)
                                hide kus1tf2
                                show kus1tf3
                                ku "How it feels?"
                                $ renpy.transition(dissolve)
                                hide kus1tf3
                                show kus1tf4
                                p "Good..."
                                $ renpy.transition(dissolve)
                                hide kus1tf4
                                show kus1tf3
                                hide kus1cl
                                show kus1ok
                                ku "It is warm, right?"
                                $ renpy.transition(dissolve)
                                hide kus1tf3
                                show kus1tf2
                                "You squeezed her boobs a little."
                                $ renpy.transition(dissolve)
                                hide kus1tf2
                                show kus1tf3
                                hide kus1ok
                                show kus1clorg
                                ku "Arghhh.. *moan*"
                                $ renpy.transition(dissolve)
                                hide kus1tf3
                                show kus1tf4
                                ku "Yeah... Squeeze them hard!!! *moan*"
                                $ renpy.transition(dissolve)
                                hide kus1tf4
                                show kus1tf3
                                "*squeeze*"
                                $ renpy.transition(dissolve)
                                hide kus1tf3
                                show kus1tf4
                                ku "Yeasss...*heavy moaning*"
                                $ renpy.transition(dissolve)
                                hide kus1tf4
                                show kus1tf3
                                show kus1milk2
                                p "Fuck this is hot!!! *splurt*"
                                $ renpy.transition(dissolve)
                                hide kus1tf3
                                show kus1tf4
                                show kus1tf5
                                ku "Ahhhhh....*maon*"
                                $ renpy.transition(dissolve)
                                hide kus1tf4
                                show kus1tf3
                                p "Yeah!!!*splurt*"
                                $ renpy.transition(dissolve)
                                hide kus1tf3
                                show kus1tf2
                                show kus1tf6
                                hide kus1clorg
                                show kus1org
                                ku "More!!*moan*"
                                $ renpy.transition(dissolve)
                                hide kus1tf2
                                show kus1tf1
                                hide kus1tf6
                                show kus1tf6
                                show kus1tf7
                                hide kus1milk2
                                p "*splurt*"
                                ku "Ahhhh...*moan*"
                                ku "You cum alot on my boobs...*moan*"
                                p "Ehm... Yeah... I see that..."
                                p "Fuck! Your boobs is hot!"
                                $ renpy.transition(dissolve)
                                hide kus1org
                                show kus1hap
                                ku "Hehe... I like them too... And how you hold them..."
                                p "Do you like it??"
                                ku "Yes... it is hot... I feel nice trembling in my pussy..."
                                ku "Maybe we can focus more on that part next time."
                                p "Sure..."
                                ku "Can we go out now?"
                                p "Sure... Just clean yourself..."
                                $ renpy.transition(dissolve)
                                hide kus1tf5
                                ku "Sure *glog*"
                                p "Do you want to drink it all?"
                                ku "Sure, it is tasty..."
                                p "Ok...."
                                scene black with circleirisin
                                "You spend another good day with Kushina..."
                                "You must fuck her pussy next time!!!"
                                show nrock0 with circleirisout
                                jump nrock

                            else:
                                p "I want to be closer to you today."
                                ku "I want to be close to you, too..."
                                p "Maybe we can....*zap*"
                                "You drop your pants."
                                $ renpy.transition(dissolve)
                                hide kussmile
                                show kusok
                                ku "Yes... I want to feel your dick!"
                                $ renpy.transition(dissolve)
                                hide kusop
                                hide kusok
                                hide kusa
                                hide kusb
                                hide kusc
                                hide kusd
                                hide kusshy
                                p "huh..."
                                $ renpy.transition(dissolve)
                                show kus1a
                                show kus1ok
                                show kus1shy
                                ku "What do you want with me now?"
                                menu:
                                    "Fuck her boobs":
                                        p "I want to fuck your big boobs!"
                                        $ renpy.transition(dissolve)
                                        hide kus1a
                                        hide kus1ok
                                        hide kus1shy
                                        show kus1b
                                        show kus1sad
                                        show kus1shy
                                        p "You like when I grab them, right?"
                                        $ renpy.transition(dissolve)
                                        hide kus1sad
                                        show kus1cl
                                        ku "Yes... It feels good..."
                                        p "And now..."
                                        $ renpy.transition(dissolve)
                                        show kus1tf1
                                        ku "Yes, stick it in!"
                                        $ renpy.transition(dissolve)
                                        hide kus1tf1
                                        show kus1tf2
                                        ku "MMm... Nice"
                                        p "..."
                                        $ renpy.transition(dissolve)
                                        hide kus1tf2
                                        show kus1tf3
                                        ku "So warm..."
                                        $ renpy.transition(dissolve)
                                        hide kus1tf3
                                        show kus1tf4
                                        p "..."
                                        $ renpy.transition(dissolve)
                                        hide kus1tf4
                                        show kus1tf3
                                        hide kus1cl
                                        show kus1ok
                                        ku "Harder!*moan*"
                                        $ renpy.transition(dissolve)
                                        hide kus1tf3
                                        show kus1tf2
                                        "You squeezed her boobs a little harder."
                                        $ renpy.transition(dissolve)
                                        hide kus1tf2
                                        show kus1tf3
                                        hide kus1ok
                                        show kus1clorg
                                        ku "Arghhh.. *moan*"
                                        $ renpy.transition(dissolve)
                                        hide kus1tf3
                                        show kus1tf4
                                        ku "Yeah... Squeeze them hard!!! *moan*"
                                        $ renpy.transition(dissolve)
                                        hide kus1tf4
                                        show kus1tf3
                                        "*squeeze*"
                                        $ renpy.transition(dissolve)
                                        hide kus1tf3
                                        show kus1tf4
                                        ku "Yeasss...*heavy moaning*"
                                        $ renpy.transition(dissolve)
                                        hide kus1tf4
                                        show kus1tf3
                                        show kus1milk2
                                        p "Fuck this is hot!!! *splurt*"
                                        $ renpy.transition(dissolve)
                                        hide kus1tf3
                                        show kus1tf4
                                        show kus1tf5
                                        ku "Ahhhhh....*maon*"
                                        $ renpy.transition(dissolve)
                                        hide kus1tf4
                                        show kus1tf3
                                        p "Yeah!!!*splurt*"
                                        $ renpy.transition(dissolve)
                                        hide kus1tf3
                                        show kus1tf2
                                        show kus1tf6
                                        hide kus1clorg
                                        show kus1org
                                        ku "More!!*moan*"
                                        $ renpy.transition(dissolve)
                                        hide kus1tf2
                                        show kus1tf1
                                        hide kus1tf6
                                        show kus1tf6
                                        show kus1tf7
                                        hide kus1milk2
                                        p "*splurt*"
                                        ku "Ahhhh...*moan*"
                                        ku "You cum alot on my boobs...*moan*"
                                        p "Ehm... Yeah... I see that..."
                                        p "Fuck! Your boobs is hot!"
                                        $ renpy.transition(dissolve)
                                        hide kus1org
                                        show kus1hap
                                        ku "Hehe... I like them too... And how you hold them..."
                                        p "Do you like it??"
                                        ku "Yes... it is hot... I feel nice trembling in my pussy..."
                                        p "Do not worry, I will fuck your pussy next time."
                                        ku "Good..."
                                        ku "Can we go out now?"
                                        p "Sure... Just clean yourself..."
                                        $ renpy.transition(dissolve)
                                        hide kus1tf5
                                        ku "Sure *glog*"
                                        p "Good girl...."
                                        ku "*glog* tasty..."
                                        scene black with circleirisin
                                        "You spend another wonderfull day with Kushina..."
                                        "Fucking her tits improved your happiness."
                                        show nrock0 with circleirisout
                                        jump nrock

                                    "Fuck her pussy":
                                        p "I want to play with your pussy..."
                                        ku "That sounds good..."
                                        $ renpy.transition(dissolve)
                                        hide kus1sad
                                        hide kus1ok
                                        show kus1cl
                                        ku "How do you want to start this?"
                                        p "Easily..."
                                        $ renpy.transition(dissolve)
                                        show kus1p1
                                        ku "MMm... Nice!"
                                        $ renpy.transition(dissolve)
                                        hide kus1p1
                                        show kus1p2
                                        ku "Yesss... I feel it..."
                                        $ renpy.transition(dissolve)
                                        hide kus1p2
                                        show kus1p3
                                        ku "Arggg...*moan*"
                                        $ renpy.transition(dissolve)
                                        hide kus1p3
                                        show kus1p4
                                        p "Yeah..."
                                        $ renpy.transition(dissolve)
                                        hide kus1p4
                                        show kus1p3
                                        hide kus1cl
                                        show kus1ok
                                        ku "This feel...*moan*"
                                        $ renpy.transition(dissolve)
                                        hide kus1p3
                                        show kus1p2
                                        p"I want to squeeze that boobs!"
                                        $ renpy.transition(dissolve)
                                        hide kus1a
                                        hide kus1ok
                                        hide kus1shy
                                        show kus1b
                                        hide kus1p2
                                        show kus1p3
                                        show kus1clorg
                                        show kus1shy
                                        ku "Arghhh.. *moan*"
                                        $ renpy.transition(dissolve)
                                        hide kus1p3
                                        show kus1p4
                                        ku "Fuck me !!! *moan*"
                                        $ renpy.transition(dissolve)
                                        hide kus1b
                                        hide kus1clorg
                                        hide kus1shy
                                        show kus1a
                                        hide kus1p4
                                        show kus1p3
                                        show kus1org
                                        show kus1shy
                                        p "More!!!"
                                        $ renpy.transition(dissolve)
                                        hide kus1p3
                                        show kus1p2
                                        ku "Yeasss...*heavy moaning*"
                                        $ renpy.transition(dissolve)
                                        hide kus1p2
                                        show kus1p3
                                        show kus1milk
                                        p "Fuck this is hot!!!"
                                        $ renpy.transition(dissolve)
                                        hide kus1p3
                                        show kus1p4
                                        p "I will..."
                                        $ renpy.transition(dissolve)
                                        hide kus1p4
                                        show kus1p3
                                        menu:
                                            "Cum in":
                                                ku "Ahhhh*heavy moaning*"
                                                $ renpy.transition(dissolve)
                                                hide kus1p3
                                                show kus1p4
                                                p "Yeah *splurt*"
                                                hide kus1clorg
                                                show kus1org
                                                show kus1spi1
                                                ku "Ahhhhh....*moan* Fill my pussy!!!"
                                                $ renpy.transition(dissolve)
                                                show kus1spi2
                                                p "Fuck!!!splurt*"
                                                ku "You cum alot again..."
                                                $ renpy.transition(dissolve)
                                                hide kus1milk
                                                ku "It is dripping out of my pussy..*moan drip*"
                                                p "..."
                                                ku "MMm... *moan*"
                                                with fade
                                                p "..."
                                                ku "I want to go to the shop now!"
                                                p "Sure, we can go, you earned it."
                                                $ renpy.transition(dissolve)
                                                hide kus1org
                                                show kus1hap
                                                ku "Really!!! AWESOME!!!"
                                                ku "Just wait here I will be ready soon!"
                                                scene black with circleirisin
                                                "Kushina go to the shower and then you take her to some shop."
                                                show nrock0 with circleirisout
                                                jump nrock

                                            "Cum out":
                                                ku "Ahhhh*heavy moaning*"
                                                $ renpy.transition(dissolve)
                                                hide kus1p3
                                                show kus1p2
                                                p "Yeah *splurt*"
                                                $ renpy.transition(dissolve)
                                                hide kus1p2
                                                show kus1p1
                                                hide kus1clorg
                                                show kus1org
                                                show kus1spo1
                                                ku "Ahhhhh....*moan*"
                                                $ renpy.transition(dissolve)
                                                show kus1spo2
                                                p "More!!!*splurt*"
                                                $ renpy.transition(dissolve)
                                                show kus1spo3
                                                ku "So warm...."
                                                $ renpy.transition(dissolve)
                                                hide kus1milk
                                                ku "Mmmmm...*moan drip*"
                                                p "That was...."
                                                ku "Yessss...*moan*"
                                                ku "You cum alot over my body...*moan*"
                                                p "Yeah... "
                                                p "You are so hot."
                                                $ renpy.transition(dissolve)
                                                hide kus1org
                                                show kus1hap
                                                ku "Hehe... That was fun!!! Can we go out now?"
                                                p "That was fast..."
                                                p "You don't need any time for recovery or..."
                                                ku "No, I am fine. And after that I am more than fine."
                                                ku "Just give me a moment to clean myself."
                                                p "Yeah.. Sure..."
                                                scene black with circleirisin
                                                "Kushina drink all your sperm and then you go out with her."
                                                show nrock0 with circleirisout
                                                jump nrock

                                        scene black with circleirisin
                                        "You spend another wonderfull day with Kushina..."
                                        "Her pussy tasted so sweet!"
                                        show nrock0 with circleirisout
                                        jump nrock


                                    "Fuck boobs and pussy":
                                        p "I want to fuck your whole body!"
                                        ku "Ok... And how you want to do it?"
                                        p "Kage bunshin no jutsu!"
                                        ku "huh? You create your own clone??? It is hot...."
                                        $ renpy.transition(dissolve)
                                        hide kus1a
                                        hide kus1ok
                                        hide kus1shy
                                        show kus1b
                                        show kus1sad
                                        show kus1shy
                                        p "*squeeze*"
                                        $ renpy.transition(dissolve)
                                        hide kus1sad
                                        show kus1cl
                                        ku "Mmmm...*moan*"
                                        $ renpy.transition(dissolve)
                                        show kus1tf1
                                        ku "Yes... *moan* fuck my boobs!!! and my pussy..."
                                        $ renpy.transition(dissolve)
                                        hide kus1tf1
                                        show kus1tf2
                                        ku "MMm... Nice"
                                        p "..."
                                        $ renpy.transition(dissolve)
                                        hide kus1tf2
                                        show kus1tf3
                                        ku "So warm..."
                                        $ renpy.transition(dissolve)
                                        hide kus1tf3
                                        show kus1tf4
                                        p "And now..."
                                        $ renpy.transition(dissolve)
                                        hide kus1tf4
                                        show kus1tf3
                                        show kus1p1
                                        hide kus1cl
                                        show kus1ok
                                        ku "Yess... Stick itin!!! *moan*"
                                        $ renpy.transition(dissolve)
                                        hide kus1tf3
                                        show kus1tf2
                                        hide kus1p1
                                        show kus1p2
                                        ku "This is fun! *moan*"
                                        $ renpy.transition(dissolve)
                                        hide kus1tf2
                                        show kus1tf3
                                        hide kus1p2
                                        show kus1p3
                                        hide kus1ok
                                        show kus1clorg
                                        ku "Arghhh.. *moan*"
                                        $ renpy.transition(dissolve)
                                        hide kus1tf3
                                        show kus1tf4
                                        hide kus1p3
                                        show kus1p4
                                        ku "Yeah... Squeeze them hard!!! *moan*"
                                        $ renpy.transition(dissolve)
                                        hide kus1tf4
                                        show kus1tf3
                                        hide kus1p4
                                        show kus1p3
                                        "*squeeze*"
                                        $ renpy.transition(dissolve)
                                        hide kus1tf3
                                        show kus1tf4
                                        hide kus1p3
                                        show kus1p2
                                        ku "Yeasss...*heavy moaning*"
                                        $ renpy.transition(dissolve)
                                        hide kus1tf4
                                        show kus1tf3
                                        hide kus1p2
                                        show kus1p3
                                        show kus1milk2
                                        p "Fuck that body is!!! *splurt*"
                                        $ renpy.transition(dissolve)
                                        hide kus1tf3
                                        show kus1tf4
                                        show kus1tf5
                                        hide kus1p3
                                        show kus1p4
                                        ku "Ahhhhh....*maon*"
                                        $ renpy.transition(dissolve)
                                        hide kus1tf4
                                        show kus1tf3
                                        hide kus1p4
                                        show kus1p3
                                        hide kus1p4
                                        show kus1p3
                                        p "Yeah!!!*splurt*"
                                        $ renpy.transition(dissolve)
                                        hide kus1tf3
                                        show kus1tf2
                                        show kus1tf6
                                        hide kus1p3
                                        show kus1p2
                                        hide kus1clorg
                                        show kus1org
                                        ku "More!!*moan*"
                                        $ renpy.transition(dissolve)
                                        hide kus1tf2
                                        show kus1tf1
                                        hide kus1tf6
                                        show kus1tf6
                                        show kus1tf7
                                        hide kus1p2
                                        show kus1p3
                                        p "YEAH!!!!"
                                        $ renpy.transition(dissolve)
                                        hide kus1p3
                                        show kus1p4
                                        p "*splurt*"
                                        $ renpy.transition(dissolve)
                                        show kus1spi1
                                        ku "Ahhhh...*moan* fill my pussy!!!"
                                        $ renpy.transition(dissolve)
                                        show kus1spi2
                                        p "Shit!!!"
                                        ku "*drip*You cum in my pussy... and on my boobs...*moan*"
                                        p "You like it right!"
                                        ku "It is amazing...*moan*"
                                        $ renpy.transition(dissolve)
                                        hide kus1org
                                        show kus1hap
                                        hide kus1milk2
                                        ku "I want to stay like this...."
                                        p "You do not want to come out?"
                                        ku "I want but...*moan* give me a moment..."
                                        p "Whatever you want."
                                        scene black with circleirisin
                                        if kushinalove ==4:
                                            "Kushina really enjoed it!"
                                            "Now you can try to fuck her in some other place."
                                            $ kushinalove = 5
                                            show nrock0 with circleirisout
                                            jump nrock
                                        else:
                                            "Fucking her tits and pussy was truly amazing. She need some time to recover."
                                            "You spend another great day with her."
                                            show nrock0 with circleirisout
                                            jump nrock



                                scene black with circleirisin
                                "You spend another good day with Kushina..."
                                "Every time when you two was alone, she kiss you... "
                                show nrock0 with circleirisout
                                jump nrock

                        "Go outside first":
                            if kushinalove <=4:
                                "She is not ready to have sex outside."
                                jump kushinafucker

                            else:
                                p "I think we can go out first.."
                                ku "You do not want to have some fun?"
                                p "Maybe later..."
                                ku "OK...."
                                scene black with circleirisin
                                show rcave with circleirisout
                                $ renpy.transition(dissolve)
                                hide kusa
                                hide kusb
                                hide kusc
                                hide kusd
                                hide kussmile
                                hide kusshy
                                hide kusop
                                if kushinadress == 0:
                                    show kusa
                                if kushinadress == 1:
                                    show kusb
                                if kushinadress == 2:
                                    show kusc
                                show kusok
                                if kushinalove ==5:
                                    ku "This place is familiar to me somehow."
                                    p "It is normal... Hidden stone places looks all same."
                                    ku "Yeah... probably..."
                                    $ kushinalove =6
                                    ku "What you want to do now?"
                                    p "Just strip and lay down I will show you."
                                    ku "Huh? how???"
                                    p "Just put your hands in the air and make yourself comfortable."
                                    ku "Ehm... I will try..."
                                    $ renpy.transition(dissolve)
                                    hide kusa
                                    hide kusb
                                    hide kusc
                                    hide kusd
                                    hide kussmile
                                    hide kusshy
                                    hide kusop
                                    show kus4a
                                    show kus4ok
                                    ku "Maybe like this?"
                                    p "Yes it is perfect..."
                                    ku "And what now?"
                                else:
                                    ku "We are here again.... I know what you want to do..."
                                    p "Really???"
                                    ku "Yeah...."
                                    $ renpy.transition(dissolve)
                                    hide kusa
                                    hide kusb
                                    hide kusc
                                    hide kusd
                                    hide kussmile
                                    hide kusshy
                                    hide kusop
                                    show kus4a
                                    show kus4ok
                                    ku "I am ready... Do whatever you want with me."
                                p "Good... I think I will use some jutsu first..."
                                ku ".... Yeah... Some sexi jutsu..."
                                p "First I will do something you like..."
                                ku "What is it?"
                                "You pull out a marker."
                                ku "hehe... Yes, body painting."
                                $ renpy.transition(dissolve)
                                show kus4t1
                                hide kus4ok
                                show kus4cl
                                ku "MMM... Nice...*moan*"
                                ku "Draw more things on my body!"
                                $ renpy.transition(dissolve)
                                show kus4t2
                                ku "Yess....*moan*"
                                p "And now Water style - water splash submission!"
                                $ renpy.transition(dissolve)
                                show kus4w1
                                ku "Hehe... It is cold.. What if that drawing dissapear?"
                                if kushinalove ==5:
                                    $ kushinalove =6
                                p "Do not worry, It will hold long enough on you..."
                                p "Water tingling dragoon!"
                                $ renpy.transition(dissolve)
                                show kus4w2
                                ku "Hehe... this is funny *Chuckle* more"
                                p "Water steam orgasm!"
                                $ renpy.transition(dissolve)
                                show kus4w3
                                hide kus4cl
                                show kus4hap
                                ku "MMM... *moan* so good..."
                                p "This is good time for...."
                                $ renpy.transition(dissolve)
                                show kus4p1
                                ku "Pussy time right?"
                                $ renpy.transition(dissolve)
                                hide kus4p1
                                show kus4p2
                                p "Yeah...."
                                $ renpy.transition(dissolve)
                                hide kus4p2
                                show kus4p3
                                ku "Deeper!!! *moan chuckle*"
                                $ renpy.transition(dissolve)
                                hide kus4p3
                                show kus4p4
                                hide kus4hap
                                show kus4shy
                                show kus4shock
                                ku "Arggg...*pain* too deep!"
                                $ renpy.transition(dissolve)
                                hide kus4p4
                                show kus4p3
                                p "But good right?"
                                $ renpy.transition(dissolve)
                                hide kus4p3
                                show kus4p2
                                ku "Ehm...*moan*"
                                $ renpy.transition(dissolve)
                                hide kus4p2
                                show kus4p3
                                hide kus4shock
                                show kus4cl
                                ku "I am not sure...."
                                $ renpy.transition(dissolve)
                                hide kus4p3
                                show kus4p2
                                ku "Stick it in again...*moan*"
                                $ renpy.transition(dissolve)
                                hide kus4p2
                                show kus4p3
                                p "Sure..."
                                $ renpy.transition(dissolve)
                                hide kus4p3
                                show kus4p4
                                ku "Arggg...*moan* it is better now!"
                                $ renpy.transition(dissolve)
                                hide kus4p4
                                show kus4p3
                                hide kus4cl
                                show kus4clop
                                p "I told you..."
                                $ renpy.transition(dissolve)
                                hide kus4p3
                                show kus4p2
                                ku "Mmmm...*moan*"
                                $ renpy.transition(dissolve)
                                hide kus4p2
                                show kus4p3
                                ku "Yesss....*heavy moan*"
                                $ renpy.transition(dissolve)
                                hide kus4p3
                                show kus4p4
                                p "...."
                                $ renpy.transition(dissolve)
                                hide kus4p4
                                show kus4p3
                                p "ahhhh*heavy moaning*"
                                $ renpy.transition(dissolve)
                                hide kus4p3
                                show kus4p2
                                hide kus4clop
                                show kus4org
                                p "Shit... this is too good..."
                                $ renpy.transition(dissolve)
                                hide kus4p2
                                show kus4p3
                                menu:
                                    "Cum in":
                                        ku "Yesss...*heavy moan*"
                                        $ renpy.transition(dissolve)
                                        hide kus4p3
                                        show kus4p4
                                        p "Tak it all!!!*splurt*"
                                        $ renpy.transition(dissolve)
                                        show kus4spi1
                                        p "And more...*splurt*"
                                        $ renpy.transition(dissolve)
                                        show kus4spi2
                                        ku "Ahhh...*drip*"
                                        $ renpy.transition(dissolve)
                                        hide kus4org
                                        show kus4clop
                                        ku "Mmmm... So much sperm inside me."
                                        with fade
                                        p ".... So what do you want do do now??"
                                        ku "Maybe we can go to the bar or something?"
                                        p "Sounds good... lets go... just clean up first..."
                                        ku "Allright..."
                                        scene black with circleirisin
                                        "You go to the bar with Kushina. She really don't know how to drink."
                                        "You must carry her to her room."
                                        show nrock0 with circleirisout
                                        jump nrock


                                    "Cum out":
                                        ku "Cum on my boobs please... *heavy moan*"
                                        $ renpy.transition(dissolve)
                                        hide kus4p3
                                        show kus4p2
                                        p "Yeah!!*splurt*"
                                        $ renpy.transition(dissolve)
                                        hide kus4p2
                                        show kus4p1
                                        show kus4spo1
                                        p "And more...*splurt*"
                                        $ renpy.transition(dissolve)
                                        show kus4spo2
                                        ku "Ahhh, More please....*drip*"
                                        $ renpy.transition(dissolve)
                                        show kus4spo3
                                        p "!!!" with hpunch
                                        $ renpy.transition(dissolve)
                                        hide kus4org
                                        show kus4clop
                                        ku "AAhhhhh....*moan* so hot..."
                                        with fade
                                        p "Hehe... look at yourself..."
                                        $ renpy.transition(dissolve)
                                        hide kus4clop
                                        show kus4shock
                                        ku "??? Is something wrong???"
                                        p "No just... Shit I hear something!!!"
                                        ku "What???"
                                        p "Quick! Let's run away."
                                        scene black with circleirisin
                                        "That was close... Someone must hear the noise and want to check what is going on."
                                        "But it was fun!"
                                        show nrock0 with circleirisout
                                        jump nrock

                    jump kushinatalker


            "Use Namigan":
                if kushinamission <=  7:
                    p "I want to show you something funny."
                    ku "Something funny? What is it?"
                    p "You will see, just give me your hands."
                    ku "OK..."
                    p "Namigan!" with hpunch
                    $ renpy.transition(dissolve)
                    hide kusok
                    show kusnn
                    p "Nice... It works..."
                    "*beeep*"
                    p "Huh? What was that?"
                    ku "..."
                    mi "Hey, What is going on?"
                    p "Fuck, Mitsuka is coming... Namigan KAI!"
                    $ renpy.transition(dissolve)
                    hide kusnn
                    show kusok
                    ku "Ouch...*dizzy*"
                    $ renpy.transition(dissolve)
                    hide kusok
                    hide kusa
                    hide kusb
                    hide kusc
                    show mit1
                    show mitok
                    mi "Hey!What are you doing here?"
                    p "Ehm... Nothing, I just..."
                    mi "It is forbidden to use any kind of jutsu in this hospital!"
                    p "Yeah... But..."
                    mi "Please, this is place for recovery. Do not do anything stupid here."
                    p "Sure..."
                    mi "Ok... Now please leave... Looks like Kushina didn't feel alright."
                    p "..."
                    scene black with circleirisin
                    show nrock0 with circleirisout
                    jump nrock

                else:
                    p "I want to show you something funny."
                    ku "Something funny? What is it?"
                    p "You will see, but first we need to go outside."
                    $ renpy.transition(dissolve)
                    hide kusok
                    show kussmile
                    ku "We are going out? Amazing!"
                    p "Just follow me..."
                    ku "Yaiks!"
                    scene black with circleirisin
                    $ renpy.transition(dissolve)
                    hide kussmile
                    hide kusa
                    hide kusb
                    hide kusc
                    show rcave with circleirisout
                    $ renpy.transition(dissolve)
                    if kushinadress == 0:
                        show kusa
                    if kushinadress == 1:
                        show kusb
                    if kushinadress == 2:
                        show kusc
                    show kusop
                    p "Fine looking like no one is around."
                    ku "This place is amazing. It is good to feel fresh air."
                    p "Now, give me your hands."
                    ku "OK..."
                    p "Namigan!" with hpunch
                    $ renpy.transition(dissolve)
                    hide kusok
                    hide kusop
                    show kusnn
                    p "Nice... It works..."
                    p "So what should I do now?"
                    menu kushinamigan:
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
                            menu kuntf:
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
                                    jump kuntf

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
                                    jump kuntf

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
                                    "After releasing Namigan she didn't have a single clue what really happened."
                                    show nrock0 with circleirisout
                                    jump nrock

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
                            show nrock0 with circleirisout
                            jump nrock

                        "Mixed training":
                            if expscroll ==0:
                                p "I need an expansion scroll for this."
                                p "I should visit the shop in the Konoha."
                                jump kushinamigan


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
                                p "Fuck I should take it out quickly...."
                                scene black with circleirisin
                                "Huh? That was a close Kushina start to check-in with your sperm."
                                "But you react quickly and she is now ok... Maybe a little confused but who care.."
                                show nrock0 with circleirisout
                                jump nrock

                        "Boob expansion":
                            if expscroll ==0:
                                p "I need an expansion scroll for this."
                                p "I should visit the shop in the Konoha."
                                jump kushinamigan


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
                                        p "OK... Time to clean you a little and release that expansion jutsu."
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
                                        p "Who cares right? Time to release all this jutsu."

                                scene black with circleirisin
                                "It was really something see Kushina like this."
                                "She complained about weird pressure in her breast. I wonder why."
                                show nrock0 with circleirisout
                                jump nrock

                    scene black with circleirisin
                    show nrock0 with circleirisout
                    jump nrock

            "Final brainwash":
                "..."
                if kagumission <= 9:
                    p "I want to do something extra today."
                    ku "That sounds funny."
                    p "Ehmmm... Maybe...."
                    ku "So, What is it?"
                    p "Not sure right now..."
                    ku "Owwww... Booring..."
                    scene black with circleirisin
                    show drock0 with circleirisout
                    jump drock

                elif kushinamission == 9:
                    p "I want to do something extra today."
                    ku "That sounds funny."
                    $ kushinamission = 10
                    p "It will be funny... Just relax..."
                    ku "Sure..."
                    p "Namigan! Final brainwash!!!" with hpunch
                    ku "Ahhhhh!!! *moan pain*"
                    $ renpy.transition(dissolve)
                    hide kusok
                    show kusnn
                    p "Good... Now go to the hidden tree village I will come to see you soon..."
                    ku "...."
                    ku "Sure..."
                    scene black with circleirisin
                    show nrock0 with circleirisout
                    jump nrock
                else:
                    "She is not ready for this."
                    "Improve your relationship with her first..."
                    scene black with circleirisin
                    show drock0 with circleirisout
                    jump drock

            "Back to the city":
                scene black with circleirisin
                show drock0 with circleirisout
                jump drock


        scene black with circleirisin
        show drock0 with circleirisout
        jump drock




#  ROCK TOWN LABEL
#  ROCK TOWN LABEL
#  ROCK TOWN LABEL
#  ROCK TOWN LABEL
#  ROCK TOWN LABEL

label rocktown:
    scene rtown
    if mitsukimission ==1:
        $ renpy.transition(dissolve)
        show kuroa:
            xalign 1.0 yalign 1.0
        show kurook:
            xalign 1.0 yalign 1.0
        show mit1:
            xalign 0.0 yalign 1.0
        show mitok:
            xalign 0.0 yalign 1.0
        kr "Hello %(p)s . It is good that you are here."
        kr "Is there any problem in our hospital?"
        mi "No lady Tsuchikage. He wanted to explore our hospital and spy on our techniques."
        p "Spy is a little hard word. I just want to know what all you do in the hospital."
        mi "I am not sure if it is a good idea."
        kr "We need to cooperate with the Hidden leaf village."
        $ mitsukimission = 2
        kr "%(p)s is the only known person who can break Kawaki jutsu for now."
        mi "Yes, I understand that, but I think."
        $ renpy.transition(dissolve)
        hide kurook
        show kuroouch:
            xalign 1.0 yalign 1.0
        kr "You are here to protect the people and help us not to think!"
        mi "...."
        mi "I understant lady Tsuchikage."
        $ renpy.transition(dissolve)
        hide mitok
        show mitsad:
            xalign 0.0 yalign 1.0
        kr "You will help him and do anything he say!"
        mi "..."
        kr "Do you understant?"
        mi "Yes lady Tsuchikage."
        kr "Now leave..."
        $ renpy.transition(dissolve)
        hide mitsad
        hide mit1
        kr "So we already solved this."
        $ renpy.transition(dissolve)
        hide kuroouch
        show kurook:
            xalign 1.0 yalign 1.0
        kr "Is there anything else I can do for you?"
        p "No... Thank you..."
        p "I am a little surprised by your order. In the past time everything was sealed or hidden from the other villages."
        kr "Yes... Guess how it ends?"
        kr "Many hatred, wars and conflicts..."
        kr "From the Kawaki incident, we decide to share our initial togeher and cooperation bring us peace."
        p "Yes I see. Thank you for your permission."
        kr "If there is anything else I can do for you, let me know."
        p "Good to know. See you later."
        scene black with circleirisin
        show nrock0 with circleirisout
        jump nrock
    elif kagumission == 1:
        $ renpy.transition(dissolve)
        show kuroa
        show kurook
        kr "Hello %(p)s , I have some work please come back later."
        $ kagumission = 2
        p "I have one quick question."
        kr "Ok... But be fast."
        p "I heard you already successfully cloned some Shinobi."
        kr "Yes... It is true... And?"
        p "I already spoke with Kushina Uzumaki clone..."
        $ renpy.transition(dissolve)
        hide kurook
        show kuroouch
        kr "Yes... She still can be a little unstable so she must be under control..."
        p "How many Shinobi you actually cloned?"
        kr "It is hard to tell because some clones died during the process..."
        p "But how many of them survived?"
        kr "Hundreds..."
        p "Seriously? Why are they not in the hospital?"
        $ renpy.transition(dissolve)
        hide kuroouch
        show kurosad
        kr "Most of them are stable and not dangerous. They lived in the village and help with the work."
        kr "Some shinobis escaped and lived in the forest.And some species were too dangerous and was destroyed."
        p "I understand. But Kushina tell me about some white woman."
        kr "Hmm... She must talk about Kaguay Otsotsuki clone."
        p "What???" with hpunch
        kr "She is one of our ambitious project..."
        p "You mean that Kaguay? The woman that almost destroys the world?"
        kr "Yes... But do not worry... We developed chakra nullifier to prevent any dangerous situations."
        p "Why you even want to clone her?"
        kr "There was hope that she can use some kind of the strong jutsu and break the Kawaki jutsu."
        p "And?"
        $ renpy.transition(dissolve)
        hide kurosad
        show kuroouch
        kr "It was not successful... She have really strong chakra but that is all... without original memories she is unable to do anything."
        p "Where can I hind her?"
        kr "She works here during the day... What she does during the night is her thing."
        p "So she is here?"
        kr "Yes, I already said that."
        p "Can you call her?"
        $ renpy.transition(dissolve)
        hide kuroouch
        show kurook
        kr "Um... I do not have time for that. But go through this door and she is in the last office."
        p "Thanks..."
        kr "No problem...But be careful, she is physically ok, but her personality is weird."
        p "Thanks for warning."
        $ renpy.transition(dissolve)
        hide kuroa
        hide kurook
        p "Hmm.. I wonder if it is really Kaguay."
        p ".... last office...."
        $ renpy.transition(dissolve)
        show kaga1
        show kagaok
        ka "What are you doing here?"
        p "Uhh???"
        ka "Uhh??? It is your final answer?"
        p "No... Sorry... I was looking for you."
        $ renpy.transition(dissolve)
        hide kagaok
        show kagacl
        ka "Really??? That is so sweet? Do I know you?"
        p "I think no.... I am %(p)s ..."
        $ renpy.transition(dissolve)
        hide kagacl
        show kagaok
        ka "Then why you are looking for me if you do not know me?"
        p "That is really a good question."
        ka "I have a lot of work so..."
        p "Wait!"
        $ renpy.transition(dissolve)
        hide kagaok
        show kagasad
        ka "Don't yell at me, please."
        p "Sorry, I just want to know you better and be your friend."
        ka "Friend? I do not have friends."
        p "Why?"
        ka "I am not sure... It looks like everybody is a little afraid of me."
        p "Hmm.. I understand that."
        ka "What???"
        p "Nothing... Do you want to be my friend?"
        $ renpy.transition(dissolve)
        hide kagasad
        show kagahap
        ka "Yes... It will be awesome we can..."
        ka "Ehm... What actually friends do?"
        p "Do not worry... I will show you... We can go to the dinner or..."
        ka "I am hungry, lets go to the dinner!!!"
        p "Ok... Sure..."
        scene black with circleirisin
        "It was a good day. Kaguya is not so scary as you think at the first time."
        "She just needs some love and she will be ok."
        show nrock0 with circleirisout
        jump nrock


    elif tenmission == 4:
        $ renpy.transition(dissolve)
        show kuroa
        show kurook
        kr "Hello %(p)s , I have some work please come back later."
        p "Just a quick question, is there any nice place around the village?"
        $ tenmission = 5
        kr "Our park is really beautifull."
        p "Yes, it is... But I was thinking about something more.... There are so many rocks. Is there any lake here?"
        kr "No... But you can find a waterfall near the village. Not many people know about him because it is hidden with jutsu."
        p "Why you use jutsu to hide waterfall?"
        $ renpy.transition(dissolve)
        hide kurook
        show kuroouch
        kr "I am not sure it was a measure of previous Hokage."
        kr "Maybe he wants to protect our water supplies or something."
        p "But why you do not cancel it?"
        $ renpy.transition(dissolve)
        hide kuroouch
        show kurosad
        kr "It will take too much chakra and there is no need to cancel that jutsu."
        p "Ok... How can I find it?"
        "Tsuchikage showed you a map."
        kr "Just go between these two rocks and you will find it."
        p "Thanks..."
        scene black with circleirisin
        show nrock0 with circleirisout
        jump nrock

    elif kushinamission == 2:
        $ renpy.transition(dissolve)
        show kuroa
        show kurook
        kr "Hello %(p)s . What can I do for you?"
        p "It is good that you are asking."
        p "Kushina want some clothes and I don't know where can I find some."
        $ renpy.transition(dissolve)
        hide kurook
        show kuroouch
        $ kushinamission = 3
        kr "Shit... "
        p "???"
        kr "She already talks with me about the new clothes."
        kr "I totally forget abou it."
        kr "Can you bring them to her?"
        p "Sure I have no problem with that."
        kr "Thanks... There are in the box."
        p "Ok..."
        scene black with circleirisin
        show nrock0 with circleirisout
        jump nrock

    elif kushinamission <= 1:
        $ renpy.transition(dissolve)
        show kuroa
        show kurook
        kr "Hello %(p)s , I have some work please come back later."
        p "Sure..."
        scene black with circleirisin
        show drock0 with circleirisout
        jump drock

    else:
        $ renpy.transition(dissolve)
        show kuroa
        show kurook
        kr "Hello %(p)s . What can I do for you?"
        menu kurotalk:
            "Talk":
                if kushinamission == 5:
                    p "Can you tell me something about Kushina Uzumaki?"
                    $ renpy.transition(dissolve)
                    hide kurook
                    show kurosad
                    kr "Kushina Uzumaki... She was amazing kunoichi killed by the nine tails."
                    $ kushinamission = 6
                    kr "But you want to know something about her clone right?"
                    p "Yes... Who gives you the DNA sample."
                    kr "I cannot tell you who give me the DNA sample."
                    p "Why?"
                    kr "Because Her sample was delivered by the unknown Anbu member."
                    p "I see...."
                    p "But, Why you decide to clone her?"
                    $ renpy.transition(dissolve)
                    hide kurosad
                    show kuroouch
                    kr "In fact, we want to clone Naruto Uzumaki, but they deliver us the wrong DNA sample."
                    p "You want to clone Naruto Uzumaki?"
                    kr "Yes... But we still didn't have his DNA sample. Maybe If you talk with Sarada Uchiha she can send us his sample."
                    p "Ok...."
                    p "Back to Kushina, Why you decide to keep her clone after all."
                    kr "At first we want to find some answers about the hidden kinjutsu of the Uzumaki clan."
                    $ renpy.transition(dissolve)
                    hide kuroouch
                    show kurosad
                    kr "But she is absolutely useless... She can use some jutsu, but if no one teaches her the original jutsu she just didn't know them."
                    p "So why is she still in the hospital?"
                    kr "She is a living being after all. We need to protect her."
                    p "Yeah, but she told me she must stay in her room."
                    $ renpy.transition(dissolve)
                    hide kurosad
                    show kurocl
                    kr "That is true... Hmmm..."
                    kr "If you have some time you can take her somewhere out."
                    $ renpy.transition(dissolve)
                    hide kurocl
                    show kurosad
                    kr "It would be good for her and I think you can protect her if someone want to hurt her."
                    p "I just want to say the same thing."
                    p "So it is ok if I take her out sometimes?"
                    kr "You can do anything you want with her."
                    p "Hehe...That is what I wanted to hear."
                    kr "What?"
                    p "Nothing... See you later."
                    scene black with circleirisin
                    show nrock0 with circleirisout
                    jump nrock
                else:
                    p "Is everything ok right now in the village."
                    $ renpy.transition(dissolve)
                    hide kurook
                    show kurocl
                    kr "Yes everything is fine."
                    p "Good to know that."
                    $ renpy.transition(dissolve)
                    hide kurocl
                    show kurook
                    jump kurotalk

            "Work":
                p "Is there some way how I can earn some ryo?"
                kr "Yes... You can take a guard shift at the main gate."
                p "What should I do when I'm there?"
                kr "Just control the people who want to enter the village and stop enemy threat."
                kr "I can pay you 200 ryo."
                menu:
                    "Take it":
                        p "OK it sounds good."
                        kr "Ok, go to the main gate."
                        $ ryo  = ryo + 200
                        scene black with circleirisin
                        show nrock0 with circleirisout
                        jump nrock

                    "Maybe later":
                        p "Thanks for the offer, but I have no time for that."
                        kr "Come back again if you change your mind."
                        jump kurotalk

            "Namigan":
                if kuroslave == 0:
                    kr "Is there anything I can do for you?"
                    p "Actually, yes, I want to test my Namigan for you."
                    $ renpy.transition(dissolve)
                    hide kurook
                    show kurocl
                    kr "Ok. I have no problem with that. But you should find my original body."
                    p "Your original body?"
                    kr "Sure. Do you think I will spend a whole day here?"
                    p "Ehm..."
                    kr "You are silly, Just look around the park. You will find my original there."
                    p "OK... Thanks..."
                    $ kuroslave = 1
                    scene black with circleirisin
                    show drock0 with circleirisout
                    jump drock
                else:
                    kr "Is there anything I can do for you?"
                    p "Actually, yes, I want to test my Namigan for you."
                    kr "Ok. My original is somewhere around the local park."
                    jump kurotalk


            "Something else":
                p "How are you today?"
                kr "I feel fine, thanks."
                p "Can I invite you for a dinner or something?"
                $ renpy.transition(dissolve)
                hide kurook
                show kurosad
                kr "That is so nice. But I have a lot of work right now."
                p "Maybe later?"
                kr "Yeah, maybe..."
                $ renpy.transition(dissolve)
                hide kurosad
                show kurook
                jump kurotalk

            "Back to the city":
                scene black with circleirisin
                show nrock0 with circleirisout
                jump nrock

# HOSPITAL LABEL
# HOSPITAL LABEL
# HOSPITAL LABEL
# HOSPITAL LABEL
# HOSPITAL LABEL

label rocklab:
    scene rlab
    if mitsukimission ==0:
        $ renpy.transition(dissolve)
        show mit1
        show mitok
        mi"Hello. What can I do for you, are you hurt?"
        p "Ehm... I am not sure..."
        mi "I see so maybe you have some kind of amnesia. Did you take a hit in your head in the past time?"
        p "...."
        p "Probably. I am a Shinobi so I fight a lot."
        mi "We can do some test if you want to find a proper cure for you."
        menu:
            "OK":
                p "Ok.. Let's do some tests."
                mi "Sure..."
                mi "Follow me..."
                with fade
                "...."
                with fade
                "After some time."
                mi "So... It looks like you are perfectly healthy man."
                mi "There were some weird measures from the start that show you suffer the side effects from some weird technique but it will probably be ok."
                p "???"
                mi "There is nothing serious to worry about.Is there something else I can do for you?"
                p "Yes... Can I check healing methods you use in this hospital?"
                mi "...."
                mi "Did Tsuchikage approve it?"
                p "Ehm... Sure why not."
                mi "I need to talk with her first... Please come back later."
                p "Sure..."
                $ mitsukimission = 1
                scene black with circleirisin
                show drock0 with circleirisout
                jump drock

            "No I am fine":
                p "No. Thank you. I feel good."
                mi "So why you come into this hospital?"
                p "I am a visitor from the Konoha, I want to check your healing methods."
                mi "...."
                mi "Did Tsuchikage approve it?"
                p "Ehm... Sure why not."
                mi "I need to talk with her first... Please come back later."
                p "Sure..."
                $ mitsukimission = 1
                scene black with circleirisin
                show drock0 with circleirisout
                jump drock

    elif mitsukimission ==1:
        p "..."
        p "Looks like no one is here."
        p "Only some wounded peoples and this locked room... I wonder what is inside."
        p "Maybe if I..."
        "Zap!!!" with hpunch
        p "Shit... There is some kind of protecting jutsu on the lock."
        scene black with circleirisin
        show drock0 with circleirisout
        jump drock
    elif mitsukimission ==2:
        $ renpy.transition(dissolve)
        show mit1
        show mitok
        mi "Lady Tsuchikage give you a permission to every room in this building."
        p "Yes I know."
        $ mitsukimission = 3
        mi "But first we need to do some test to you and add your DNA sample to our database."
        p "Why?"
        $ renpy.transition(dissolve)
        hide mitok
        show mitop
        mi "We have some security measures here, and if I do not add you to the exception list it can kill you."
        p "Ehm... Ok How long it will take?"
        mi "I need 24 hours for that... First sit here and..."
        p "Ouch!!!" with hpunch
        p "What the fuck was that?"
        mi "I needed your blood sample."
        p "..."
        mi "Ok now rest... we will continue later..."
        scene black with circleirisin
        "You spend a whole day in the hospital. But you got the access to the building."
        show nrock0 with circleirisout
        jump nrock


    else:
        $ renpy.transition(dissolve)
        show mit1
        show mitok
        mi"Oh... It is you!"
        menu mitsukitalk:
            "Talk about her":
                if mitsukimission ==3:
                    p "Can you tell me something about yourself?"
                    mi "And what do you want to know?"
                    $ mitsukimission = 4
                    p "You look like Mitsuki of the hidden leaf."
                    mi "Yes... And?"
                    p "And??? Who the hell are you?"
                    mi "I think it is simple... I am a clone."
                    p "Clone?"
                    $ renpy.transition(dissolve)
                    hide mitok
                    show mitop
                    mi "Yes... There was a project to make this village safer."
                    mi "To prevent killing locals."
                    p "Yes... I remember the akuta project right?"
                    mi "Exactly... Problem was they were too aggressive."
                    mi "Whole project ended with big collateral damage."
                    p "Ok, what happened then?"
                    $ renpy.transition(dissolve)
                    hide mitop
                    show mitok
                    mi "Orochimaru decides to cooperate with Iwagakure to help create the perfect tools for defense."
                    p "Orochimaru? Why ?"
                    mi "Who knows... Maybe he wants to experiment in the bigger place and this village was desperate."
                    p "I am still not sure if that works well... I already faced some kunoichi that looks like you and want to fight me!"
                    mi "Yes... It is possible some clones was stolen in the past and maybe reprogramed."
                    p "Reprogramed????"
                    $ renpy.transition(dissolve)
                    hide mitok
                    show mitang
                    p "Again what the fuck are you?"
                    mi "I am a clone..."
                    p "But you are programed to do what?"
                    mi "Protect this village and fulfil the orders."
                    p "And you must fullfil all the orders?"
                    mi "No only the orders from my master, lady tsuchikage."
                    p "But she ordered you to obey my orders so you must do everything I tell you right?"
                    mi "...."
                    $ renpy.transition(dissolve)
                    hide mitang
                    show mitsad
                    mi "Yes...."
                    p "Good to know that..."
                    menu:
                        "Order her to strip":
                            p "Ok so strip for me!"
                            $ renpy.transition(dissolve)
                            hide mitsad
                            show mitang
                            mi "What?"
                            p "You heard me correct. STRIP!"
                            $ renpy.transition(dissolve)
                            show mitshy
                            mi "But..."
                            p "Right now!"
                            mi "Sure...."
                            $ renpy.transition(dissolve)
                            hide mit1
                            show mit2
                            hide mitang
                            show mitsad
                            hide mitshy
                            show mitshy
                            mi "What now?"
                            p "I don't know yet... Maybe you can tell me more..."
                            mi "Ok... but this is...."
                            p "Just ignore the fact that you are naked."
                            mi "...."
                            p "Just kidding... YOu can dress now..."
                            mi "Thanks..."
                            $ renpy.transition(dissolve)
                            hide mit2
                            show mit1
                            hide mitsad
                            show mitsad
                            hide mitshy
                            jump mitsukitalk

                        "That is all":
                            p "But I want to ask you about something else..."
                            jump mitsukitalk

                elif mitsukimission ==4:
                    p "Can you tell me something about yourself?"
                    mi "What exactly you want to know?"
                    $ mitsukimission = 5
                    p "You are woman right?"
                    mi "Yes and???"
                    p "How is it possible... I remember Mitsuki was a man?"
                    $ renpy.transition(dissolve)
                    hide mitsad
                    hide mitok
                    show mitop
                    mi "In the past, we had some difficulties with cloning man."
                    p "Why?"
                    mi "I am not sure... There was nothing wrong with it until Orochimaru was here as the main cloning scientist."
                    mi "Then when we procedure was complete Orochimaru left the village and new main scientist declare that it will be better to create only woman clones."
                    p "Hmmm... Let me guess, he was old and lonely right?"
                    mi "Yes, how do you know that? Did you know them?"
                    p "Ehm... I think I didn't know him."
                    p "But tell me was there any other changes after Orochimaru left?"
                    mi "Yes... New clones need to train new justice and healing methods."
                    p "Can you tell me some examples?"
                    $ renpy.transition(dissolve)
                    hide mitop
                    show mitok
                    mi "Ehmmm... I remember some kind of messaging and implementing the portions with different ways."
                    p "????"
                    mi "It is really important to take a good care of an injured man."
                    jump mitsukitalk

                elif mitsukimission ==5:
                    p "Can you tell me something about yourself?"
                    mi "What exactly you want to know?"
                    $ mitsukimission = 6
                    p "You said you need to obey the orders."
                    mi "Yes. It is true."
                    p "So do you have your own free will?"
                    mi "...."
                    $ renpy.transition(dissolve)
                    hide mitsad
                    hide mitok
                    hide mitop
                    show mitsad
                    mi "I am not sure..."
                    p "Do you have a dreams?"
                    mi "Yes."
                    p "What do you usually dream about?"
                    $ renpy.transition(dissolve)
                    hide mitsad
                    show mitok
                    mi "Sometimes I dream about travelling around the world."
                    mi "I want to explore it... see the rivers and seas."
                    p "So you have desires?"
                    mi "Yes...Maybe..."
                    p "And why are you still here?"
                    mi "I can't leave this village... It was an order...."
                    p "I see..."
                    p "Ehm.... But maybe there is something more in you."
                    p "Do you like candy?"
                    mi "Yes I like chocolate. And candy hearts..."
                    p "That sounds like you have taste.... Adn maybe your own free will..."
                    mi "Maybe... But it is not free will... I need to obbey the orders."
                    p "I understant that..."
                    mi "I can be programed to love chocolate and maybe someone just give me the desire to travel."
                    mi "I cannot be sure...."
                    p "..."
                    jump mitsukitalk
                else:
                    p "Can you tell me something about yourself?"
                    mi "What exactly you want to know?"
                    p "ehm.... Maybe..."
                    p "Nothing strikes me right now."
                    mi "So what now?"
                    jump mitsukitalk

            "Talk about hospital":
                if mitsukimission <=5:
                    p "Tell me something about this place."
                    mi "This is the hidden stone hospital."
                    mi "We heal here light and serious wounds."
                    mi "It was destroyed many times, but we will repair it every time."
                    p "Is there something more interesting?"
                    mi "We have many blood samples from the famous Shinobi!"
                    p "Good to know that..."
                    jump mitsukitalk

                elif mitsukimission ==6:
                    p "Tell me something about this place."
                    mi "This is the hidden stone hospital."
                    mi "We heal here light and serious..."
                    $ mitsukimission = 7
                    $ kushinamission = 1
                    p "Shut up already.... You tell me, that you are a clone right?"
                    mi "Yes..."
                    p "And where they create you?"
                    $ renpy.transition(dissolve)
                    hide mitsad
                    hide mitok
                    hide mitop
                    show mitsad
                    mi "Here..."
                    p "You mean at this hospital?"
                    mi "Yes...There are a special rooms and laboratories."
                    p "Ok... I want to visit the lab."
                    mi "You just can't."
                    p "Why?"
                    $ renpy.transition(dissolve)
                    hide mitsad
                    show mitok
                    mi "Only lady Tsuchikage can enter the laboratory."
                    mi "After some rouge Shinobi steals our samples we need to be more careful."
                    p "Yeah... I understant that..."
                    p "Can you show me some rooms, then?"
                    mi "Sure... For now most of them are occupied by the clones similar to me."
                    p ".... That sounds funny..."
                    $ renpy.transition(dissolve)
                    hide mitok
                    show mitop
                    mi "But they need to be programmed first...."
                    p "So, here is someone else I can talk to?"
                    mi "You can talk with wounded people that are around, but most of them need to rest."
                    mi "We have successfully cloned a Kushina Uzumaki from her DNA sample, you can try to talk with her."
                    p "Kushina????"
                    p "Why you didn't say this to me sooner."
                    mi "NO, Because you didn't ask."
                    p "Where can I find her?"
                    mi "She is in here room."
                    p "And ehere it is?"
                    mi "I will show you. But you need to know something about her."
                    p "What?"
                    mi "She maybe looks like Kushina Uzumaki, but she is only the clone of her. She will not have any memories about her past."
                    p "Are you sure about that?"
                    mi "Not 100 percent sure, she is a little different. But try to act nice to her."
                    p "Sure... So I can visit her?"
                    mi "Yes... Follow me..."
                    scene black with circleirisin
                    show rbad with circleirisout
                    $ renpy.transition(dissolve)
                    show mit1:
                        xalign 0.0 yalign 1.0
                    show mitok:
                        xalign 0.0 yalign 1.0
                    mi "Hello miss Uzumaki. I bring you a visit."
                    show kusa:
                        xalign 1.0 yalign 1.0
                    show kusok:
                        xalign 1.0 yalign 1.0
                    p "Kushina is it really you?"
                    ku "Yes. I am Kushina. And who are you?"
                    p "It is me %(p)s ."
                    ku "Sorry did I know you?"
                    mi "I told you already she didn't know anything from her past."
                    mi "She can have some memories from the original, but it is very rare."
                    p "Sure.... It is just... I see her again and..."
                    p "Wow! I don't remember her boobs are such a big!"
                    ku "You are funny..."
                    $ renpy.transition(dissolve)
                    hide mitok
                    show mitop:
                        xalign 0.0 yalign 1.0
                    mi "Yes... I am not sure why, but it looks like secondary cloning was aimed at creating subjects with bigger boobs."
                    p "That old lonely scientis again?"
                    mi "...."
                    p "Ok... please leave us Mitsuka I want to be with her alone."
                    mi "Sure...."
                    $ renpy.transition(dissolve)
                    hide mitop
                    hide mit1
                    ku "Bye...."
                    ku "Hehe... So who are you?"
                    p "You can call me %(p)s ."
                    ku "And I am Kushina... Nice to meet you %(p)s san."
                    p "Just %(p)s ."
                    ku "Ok %(p)s ."
                    p "....."
                    ku "It is good to see someone else. In the last days only lady tsuchikage an Mitsuka come to visit me."
                    ku "Can we play together?"
                    p "Ehm... Sure what kind of the game you want to play?"
                    ku "Something funny... Maybe hide and seek. Find me!"
                    $ renpy.transition(dissolve)
                    hide kusa
                    hide kusok
                    p "Really???"
                    p "You just hide under the bed."
                    $ renpy.transition(dissolve)
                    show kusa
                    show kussad
                    ku "That is not fair you find me very fast!"
                    p "Yes, I am a Shinobi... even If I close my eyes I still can feel your chakra..."
                    ku "That is so cool!!! Ehmmm... No it is booring... "
                    p "What?"
                    p "*sigh*"
                    ku "Are you allright?"
                    p "Yeah I just remember I need to do something."
                    ku "Really??? Can you visit me again sometime?"
                    p "Sure..."
                    $ renpy.transition(dissolve)
                    hide kussad
                    show kussmile
                    ku "And we will do something funny then ok?"
                    p "ok..."
                    ku "Great..."
                    p "Hmmm..."
                    ku "What?"
                    p "I also have one more question. Is there anyone else except you?"
                    ku "Yes... I saw one woman long time ago... She was all in white dress.. And her skin was white too..."
                    p "White skin? It is common..."
                    ku "No...I mean... Really white!"
                    p "Sure... And where is she now?"
                    ku "I am not sure. But I think, she lives in the village."
                    p "Thanks for the information. Bye..."
                    $ kagumission = 1
                    ku "Bye..."
                    scene black with circleirisin
                    p "What the fuck was that?"
                    show nrock0 with circleirisout
                    jump nrock

                else:
                    p "Tell me something about this place."
                    mi "This is the hidden stone hospital."
                    mi "We heal here light and serious..."
                    p "Yes I already heared that..."
                    p "Is there any more secret rooms or projects?"
                    mi "No... Cloning was the only side project here."
                    p "Ok..."
                    jump mitsukitalk

            "Use Namigan":
                p "Can I test my namigan on you?"
                mi "Your namigan? Why?"
                p "I just want to know how it affects you."
                mi "It is not a good idea I am here to help people not to be some kind of text subject."
                p "I think you can be both..."
                mi "Ask lady Tsuchikage first please..."
                p "Hmm... maybe..."
                jump mitsukitalk

            "Something else":
                if mitsukimission <=3:
                    p "There is nothing right now what I want from her."
                    p "Except some dirty things."
                    jump mitsukitalk
                else:
                    p "I want to see your naked body."
                    mi "Again?"
                    p "Sure... So do not argue with me and strip."
                    mi "Sure..."
                    $ renpy.transition(dissolve)
                    hide mit1
                    show mit2
                    hide mitok
                    hide mitsad
                    hide mitang
                    show mitsad
                    hide mitshy
                    show mitshy
                    mi "What now?"
                    p "Nothing... I just want to watch a little..."
                    mi "This is really embarrassing."
                    with fade
                    p "Hmmm.."
                    mi "Can I dress now?"
                    p "...."
                    mi "Please?"
                    p "Yeah, you can dress."
                    mi "Thanks..."
                    $ renpy.transition(dissolve)
                    hide mit2
                    show mit1
                    hide mitok
                    hide mitsad
                    hide mitang
                    show mitok
                    hide mitshy
                    show mitshy
                    p "And what now?"
                    jump mitsukitalk

            "Back to the city":
                scene black with circleirisin
                show drock0 with circleirisout
                jump drock




label rshop:
    scene rday
    if tenslave >=5:
        "Looks like the shop is now closed..."
        scene black with circleirisin
        show drock0 with circleirisout
        jump drock

    $ renpy.transition(dissolve)
    show ten0a
    show ten0ok
    te "Can I help you?"
    menu ten0bla:
        "Talk":
            if tenmission == 1:
                p "Maybe...I want to know why you are here."
                $ tenmission =2
                te "Huh? Weird question. Where should I be?"
                p "Do not take it wrong, but I think you lived in the hidden leaf village."
                te "Yes it is true."
                $ renpy.transition(dissolve)
                hide ten0ok
                show ten0op
                te "But Lee has some ancestors here."
                p "I do not know that."
                te "Why do you think his name is ROCK Lee???"
                p "Not sure... Maybe it just sounds cool."
                te "It is because his ancestors was a member of the hidden rock village - Iwagakure."
                te "There was now mainly because their bodies were hard as rock."
                p "Ehm...."
                p "So Lee is here too?"
                $ renpy.transition(dissolve)
                hide ten0op
                show ten0ok
                te "No... He is trapped in the jutus with Metal."
                p "That is bad..."
                te "There was right here when they disappear."
                $ renpy.transition(dissolve)
                hide ten0ok
                show ten0sad
                te "I hope they will come back once, so I am waiting for them."
                p "It must be really hard for you."
                te "Yes it was. But I opened a shop with ninja tools and other stuff."
                p "Other stuff?"
                $ renpy.transition(dissolve)
                hide ten0sad
                show ten0ok
                te "I have food, tools and weapons. If you need something, you will be able to find it here."
                p "Ehm... Thanks... Good to know."
                te "..."
                te "Can I help you with something else?"
                p "Maybe later..."
                te "OK... Bye..."
                scene black with circleirisin
                show nrock0 with circleirisout
                jump nrock
            elif tenmission == 3:
                p "Maybe..."
                $ tenmission =4
                te "So what do you need?"
                p "How it is possible that you are not in Kawaki jutsu."
                te "Good question."
                $ renpy.transition(dissolve)
                hide ten0ok
                show ten0op
                te "You know... I am a tool specialist."
                p "???"
                te "I collect many rare tools and weapons. One of them was Benihisago."
                p "Yeah.. I remember that one... It was used in the last war against ginkaku and kinkaku."
                te "Exactly. It has a unique ability to suck in anyone."
                p "But there were some circumstances right? "
                te "Yes... It can trap many shinobis but they need to say their most frequent word."
                p "It was pretty weird right?"
                $ renpy.transition(dissolve)
                hide ten0op
                show ten0ok
                te "Exactly. And that is the reason why we decide to create a specific tool similar to Benihisago, but with the ability to capture only one person at a time."
                p "I think it is too dangerous."
                te "No it is not. You can use it against a single enemy without hurting anyone."
                p "Ok. But how you get in?"
                te "I think Lee sensed something. And use it to save me."
                p "So he actually uses a ninja tool against own wife?"
                $ renpy.transition(dissolve)
                hide ten0ok
                show ten0cl
                te "He use it to save me..."
                p "Was it a first time?"
                $ renpy.transition(dissolve)
                hide ten0cl
                show ten0clop
                te "Of course it was a first time!"
                p "Hehe... I'm just kidding."
                p "But how do you get out of the tool?"
                te "He must put a time lock on it. So I stay inside only a few years."
                $ renpy.transition(dissolve)
                hide ten0clop
                show ten0ok
                te "Then it sets me free automatically."
                p "A few years?"
                te "Yes... Maybe 10 or more."
                p "And you think it is normal?"
                te "...."
                te "I need to get back to work now."
                p "Ok..."
                te "Bye..."
                scene black with circleirisin
                show nrock0 with circleirisout
                jump nrock

            elif tenmission == 11:
                p "Can we talk for a moment?"
                te "Sure. What do you want to know?"
                p "Is everything right between us?"
                te "???"
                $ tenmission = 12
                p "Do not take it wrong but... I just felt like you are not happy right now."
                te "Am I? I mean... Why you think that? I always have a smile on my face."
                p "Yeah, I see.. But it feels cold today."
                $ renpy.transition(dissolve)
                hide ten0ok
                show ten0op
                te "It is not cold smile it is completely normal."
                p "Sorry but I do not belive you."
                te "Why?"
                p "It has just felt. I think you have some kind of block inside you."
                te "It is because..."
                $ renpy.transition(dissolve)
                hide ten0op
                show ten0sad
                p "What?"
                te "You are so nice on me."
                p "And it is wrong because?"
                te "I started to feel something."
                p "Huh? Something like love?"
                te "I am not sure. It is more like desire..."
                p "That is not bad. We decided to be friends with benefits or?"
                te "Yes, I know, But I am scared what if I start to like it more and more?"
                p "And that bothers you?"
                $ renpy.transition(dissolve)
                hide ten0sad
                show ten0clop
                te "Yes...."
                p "Hmm..."
                te "What?"
                p "I think it is ok... You feel remorse, but it is normal."
                te "..."
                p "But it is the exact e opposite of what I want to achieve with you."
                p "I just want to make you feel better."
                $ renpy.transition(dissolve)
                hide ten0clop
                show ten0ok
                te "You are so sweet."
                te "Do you really care about me?"
                p "Of course, you are my friend."
                te "Thanks %(p)s ."
                te "You say exactly what I wanted to hear."
                p "So are you ok now?"
                te "Yes, thank you."
                p "..."
                te "I have some work right now. Plese come back later."
                p "Sure..."
                scene black with circleirisin
                show nrock0 with circleirisout
                jump nrock

            elif tenslave == 4:
                p "Are you still in contact with other girls?"
                te "Not really, I sometimes talk with Ino."
                p "Yeah... I heard that before..."
                p "Do you like it here?"
                te "Huh? Sure... This place has a different architecture, but it is fine..."
                p "Some girls already leave the village and come to the hidden tree village... Do you want to follow them?"
                $ renpy.transition(dissolve)
                hide ten0ok
                show ten0op
                te "Hmm... Not really... I will stay here and keep my shop open..."
                menu:
                    "Force her -Final brainwash":
                        p "..."
                        if kagumission <= 9:
                            p "I am not ready for that..."
                            te "What?"
                            p "Nothing...."
                            jump ten0bla
                        else:
                            p "But you do not have an option right now."
                            te "???"
                            p "Namigan! Final brainwash..."
                            $ tenslave = 5
                            te "Arggghhh!!!"
                            $ renpy.transition(dissolve)
                            hide ten0op
                            show ten0nsad
                            p "Nice..."
                            p "Now close the shop and go to the hidden tree village..."
                            te "Sure..."
                            p "I will find you there later..."
                            scene black with circleirisin
                            "Tenten leave the village and is now part of your harem."
                            show nrock0 with circleirisout
                            jump nrock

                    "Meh":
                        p "Ok... I just wanted to hear your opinion..."
                        te "Sure... anything else?"
                        jump ten0bla

            else:
                p "Are you still in contact with other girls?"
                te "Not really, I sometimes talk with Ino."
                p "Why only Ino?"
                $ renpy.transition(dissolve)
                hide ten0ok
                show ten0op
                te "Most of my friends is still in Kawaki jutsu."
                p "Yeah... I forgot..."
                p "But there are definitely more girls in the Konoha."
                te "Maybe... But Ino was always my closest friend."
                p "Really? Why?"
                $ renpy.transition(dissolve)
                hide ten0op
                show ten0ok
                te "..."
                te "Why not?"
                p "Good comment"
                jump ten0bla

        "Go out":
            if tenmission <= 1:
                p "Do you want to go out with me?"
                t "Ehm... Maybe later. I need to do something first."
                p "Ok..."
                scene black with circleirisin
                show drock0 with circleirisout
                jump drock
            elif tenmission == 2:
                p "Do you want to go out with me?"
                $ tenmission = 3
                t "Hmmm.. I think I have a minute or two..."
                p "Great!"
                t "Where you want to go now?"
                p "Hmm... I saw a park in this village it could be a nice place to relax."
                t "That sounds good to me..."
                p "Ok then, let's go."
                $ renpy.transition(dissolve)
                hide ten0ok
                hide ten0a
                scene black with circleirisin
                show rpark with circleirisout
                $ renpy.transition(dissolve)
                show ten0a
                show ten0ok
                te "It is really nice weather here."
                p "..."
                p "Yes it is..."
                te "I remember how Metal trains here."
                te "He must do 1 000 push up, because he fails to do 5 000 squads."
                p "I was always wondering why he does such a hard training."
                te "He just want to be stronger."
                $ renpy.transition(dissolve)
                hide ten0ok
                show ten0sad
                te "...."
                p "Do not be sad... He will come back, every jutsu can be broken."
                te "I hope so..."
                te "This place is nice... But I think I didn't want to be here."
                te "Sorry %(p)s  , see you later..."
                $ renpy.transition(dissolve)
                hide ten0sad
                hide ten0a
                p "Tenten?"
                p "Hmm... This will not work... I need to find another place...."
                scene black with circleirisin
                show nrock0 with circleirisout
                jump nrock


            elif tenmission == 3:
                p "Do you want to go out with me?"
                te "Ehm... Maybe later. I need to do something first."
                p "Ok..."
                scene black with circleirisin
                "This will not work, try to talk with her first."
                show drock0 with circleirisout
                jump drock
            elif tenmission == 4:
                p "Do you want to go out with me?"
                te "Sorry... I don't have a time for that right now."
                p "Ok..."
                scene black with circleirisin
                "This will not work, maybe if you find another place where you can take her.."
                show drock0 with circleirisout
                jump drock
            elif tenmission == 5:
                p "Do you want to go out with me?"
                $ tenmission = 6
                te "Ehm... Maybe later. I need to do something first."
                p "Come on! I found a special place near the village you must see it!"
                te "A special place?"
                p "Believe me it is wonderful... Just come with me!"
                te "Ok... You look very excited so it must be really wonderful."
                p "Ok then, let's go."
                $ renpy.transition(dissolve)
                hide ten0ok
                hide ten0a
                scene black with circleirisin
                te "Are we already there?"
                p "I am not sure. Actually, this will be the first time I go to that place."
                te "What???"
                p "Do not worry, I saw a map once we are close."
                show rwater with circleirisout
                $ renpy.transition(dissolve)
                show ten0a
                show ten0shock
                te "Wow... What the hell?"
                te "This place is amazing! It is protected by some kind of weird jutsu right?"
                p "Yeah..."
                $ renpy.transition(dissolve)
                hide ten0shock
                show ten0ok
                te "It looks like I can swim here."
                p "Sure... Why not..."
                $ renpy.transition(dissolve)
                hide ten0ok
                hide ten0a
                show ten0b
                show ten0cl
                te "Time for fun!"
                p "Huh? You had a swimsuit under clothes?"
                te "Sure, it is more practical."
                p "???"
                $ renpy.transition(dissolve)
                hide ten0cl
                hide ten0b
                "Tenten jump into the water."
                p "Be carefull..."
                with fade
                te "Hihi..."
                with fade
                te "That was refreshing."
                $ renpy.transition(dissolve)
                show ten0b
                show ten0ok
                show ten0w4
                p "Looks like you like swimming."
                te "Yes... It is a good way to release all stress."
                te "But I need to take a dry dress now."
                p "Sure..."
                $ renpy.transition(dissolve)
                hide ten0b
                hide ten0ok
                show ten0a
                show ten0ok
                hide ten0w4
                te "Hmmm..."
                p "What?"
                te "This feels a little weird..."
                p "You didn't like it here?"
                te "This place is amazing. I forgot all my troubles for a moment."
                p "And it is bad because you should feel bad for something?"
                $ renpy.transition(dissolve)
                hide ten0ok
                show ten0op
                te "I almost forget how good it is to have some free time and enjoy it."
                p "You are still young and pretty you should smile more often."
                te "You are right..."
                te "There are so many things I didn't do for a very long time."
                p "For example?"
                $ renpy.transition(dissolve)
                hide ten0op
                show ten0cl
                show ten0shy
                te "It is very private."
                p "Ok... Then tell me something."
                te "What?"
                p "How long you do not have a sex?"
                $ renpy.transition(dissolve)
                hide ten0cl
                show ten0shock
                te "%(p)s !!!!"
                p "So it is really long right?"
                te "...."
                $ renpy.transition(dissolve)
                hide ten0shock
                show ten0cl
                te "Maybe too long..."
                menu:
                    "Give her proposal":
                        p "I was thinking about something."
                        te "???"
                        p "Maybe we can be friends with benefits."
                        $ renpy.transition(dissolve)
                        hide ten0cl
                        show ten0shock
                        te "%(p)s ! What do you think about me! I am a married woman."
                        p "Yes, I know, but your husband is not here."
                        te "...."
                        p "And you still have some needs, right?"
                        $ renpy.transition(dissolve)
                        hide ten0shock
                        show ten0sad
                        te "Maybe..."
                        p "I know it is not an ideal situation. But I have needs too... And maybe we can help each other."
                        te "How exactly will it work?"
                        p "We can go sometimes here and be free for a moment."
                        p "Swim, kiss and enjoy our bodies."
                        $ renpy.transition(dissolve)
                        hide ten0sad
                        show ten0ok
                        te "That sounds good."


                    "Kiss her":
                        p "*smooch*"
                        $ renpy.transition(dissolve)
                        hide ten0cl
                        show ten0clop
                        te "Mmmm..."
                        $ renpy.transition(dissolve)
                        hide ten0clop
                        show ten0shock
                        te "I mean, %(p)s ! What the hell?"
                        p "Calm down, do you like it or not?"
                        te "I...."
                        $ renpy.transition(dissolve)
                        hide ten0shock
                        show ten0sad
                        te "It was nice... But I am still married."
                        p "Yeah I know, Sorry..."
                        p "But you are too hard for yourself."
                        te "..."
                        p "I was just thinking you can enjoy a good kiss."
                        $ renpy.transition(dissolve)
                        hide ten0sad
                        show ten0ok
                        te "I enjoyed it... But is it right?"
                        p "I think it is... We can be friends with benefit."
                        te "That sounds good."
                te "But you must promise me that no one will know about this deal."
                p "Of course...."
                $ renpy.transition(dissolve)
                hide ten0ok
                show ten0clop
                te "Ok... *smooch*"
                p "...."
                te "We need some kind of password to protect our secret."
                p "Password?"
                te "Yes... Something like dance or training to prevent the others to spread a gossip."
                p "Ok... What about swimming?"
                te "Hmmm.. It sounds good... So next time just tell me you want to swim and I will go with you If I have a mood."
                p "Mood? Ok...."
                te "So we have a deal?"
                p "Yes...."
                scene black with circleirisin
                "Tenten sits close to you and kiss you. It can be a good start."
                "You spend a day with Tenten near the waterfall."
                show nrock0 with circleirisout
                jump nrock

            else:
                p "Do you want to swim with me?"
                te "Sure..."
                p "Ok then, let's go."
                $ renpy.transition(dissolve)
                hide ten0ok
                hide ten0a
                scene black with circleirisin
                show rwater with circleirisout
                $ renpy.transition(dissolve)
                show ten0a
                show ten0ok
                te "This place is amazing. What do you want to do now?"
                menu tentenfuckw:
                    "Play with her body":
                        if tenmission == 6:
                            p "Hmm... I thought we can actually swim a little first."
                            $ tenmission = 7
                            te "Sure. It sounds good."
                            $ renpy.transition(dissolve)
                            hide ten0ok
                            hide ten0a
                            show ten0b
                            show ten0ok
                            "Tenten jump into the water."
                            te "This is really refreshing."
                            "You carefully go into the water and swim close to Tenten."
                            p "Your body looks really hot."
                            te "Thanks."
                            p "*smooch*"
                            $ renpy.transition(dissolve)
                            hide ten0ok
                            show ten0cl
                            show ten0w4
                            "You start kissing Tenten and take her slowly out from the water."
                            "Then you start massaging her boobs."
                            te "Ahhh... *moan*"
                            "She'd grab your penis..."
                            "You slowly take off her swimsuit, and rub her pussy."
                            $ renpy.transition(dissolve)
                            hide ten0cl
                            hide ten0b
                            show ten0c
                            show ten0ok
                            hide ten0w4
                            show ten0w4
                            show ten0shy
                            te "MMMmmmm....*fap fap*"
                            p "Yesss..."
                            te "Ahhh...*moan fap fap*"
                            p "Shit...*splurt*"
                            $ renpy.transition(dissolve)
                            hide ten0ok
                            show ten0op
                            show ten0sp1
                            te "Mmmm...*heavy moaning*"
                            te "Ahhh... *moan* It looks like you cumm a lot....."
                            p "Yes... Your hand is really skilled in this."
                            te "Hehe..."
                            p "Did you like it too?"
                            $ renpy.transition(dissolve)
                            hide ten0op
                            show ten0ok
                            te "Yes.... I almost forgot how good it is when someone touch me."
                            p "*smooch*"
                            te "But I need to swim now again to take your sperm off my body."
                            p "Ok... I was thinking this is some kind of water supply but who care..."
                            "Tenten jump into the water again."
                            "*splash*"
                            scene black with circleirisin
                            show nrock0 with circleirisout
                            jump nrock
                        else:
                            p "Hmm... I thought we can actually swim a little first."
                            te "Sure. It sounds good."
                            $ renpy.transition(dissolve)
                            hide ten0ok
                            hide ten0a
                            show ten0b
                            show ten0ok
                            "Tenten jump into the water."
                            te "Come closer to me, I won't bite you."
                            "You carefully go into the water and swim close to Tenten."
                            te "*smooch*"
                            $ renpy.transition(dissolve)
                            hide ten0ok
                            show ten0cl
                            show ten0w4
                            "You start kissing Tenten and take her slowly out from the water."
                            "Then you start massaging her boobs."
                            if tenmission == 7:
                                $ tenmission = 8
                            te "Ahhh... *moan*"
                            "She'd grab your penis..."
                            "You slowly take off her swimsuit, and rub her pussy."
                            $ renpy.transition(dissolve)
                            hide ten0cl
                            hide ten0b
                            show ten0c
                            show ten0ok
                            hide ten0w4
                            show ten0w4
                            show ten0shy
                            te "MMMmmmm....*fap fap*"
                            p "Fuck... You are really wet...."
                            te "Ahhh...*moan fap fap*"
                            p "Water style!"
                            $ renpy.transition(dissolve)
                            show ten0w1
                            hide ten0ok
                            show ten0clop
                            te "Yes!!! *moan* MORE!!!"
                            p "Water style - blue dragon!"
                            $ renpy.transition(dissolve)
                            show ten0w2
                            te "Ahhh...*heavy moaining.*"
                            p "Water style! full release!"
                            $ renpy.transition(dissolve)
                            show ten0w3
                            te "Yessss.... *moan squirt*"
                            p "Shit...*splurt*"
                            $ renpy.transition(dissolve)
                            hide ten0ok
                            show ten0op
                            show ten0sp1
                            te "Mmmm...*heavy moaning*"
                            te "Ahhh... *moan* That was awesome!"
                            p "Hehe..."
                            te "I really liked your water style..."
                            p "...."
                            $ renpy.transition(dissolve)
                            hide ten0op
                            show ten0ok
                            te "We should do this more often."
                            te "*smooch*"
                            p "I have no problem with that."
                            te "Time for some swimming. Ehm... I mean it for real this time."
                            "Tenten jump into the water again."
                            "*splash*"
                            scene black with circleirisin
                            show nrock0 with circleirisout
                            jump nrock

                    "Use tools":
                        if dildo == 0:
                            "Ok, this will be really nice, but you need to buy dildo first."
                            jump tentenfuckw
                        elif tenmission <= 7:
                            p "I bring a toy today."
                            te "I am not in a mood for toys right now. Do you want to do something else?"
                            "She is not ready for the dildo, try to tease her a little first."
                            jump tentenfuckw
                        elif tenmission == 8:
                            p "I bring a toy today."
                            te "What kind of toy?"
                            $ tenmission = 9
                            "You showed a dildo to Tenten."
                            te "Mmm... This looks interesting... What about some foreplay first?"
                            p "*smooch*"
                            "You kiss Tenten and start to undress her slowly."
                            $ renpy.transition(dissolve)
                            hide ten0ok
                            hide ten0a
                            show ten0c
                            show ten0clop
                            te "Mmmm...*moan*"
                            "You start to rub her pussy."
                            te "Yes.... *moan* and now..."
                            $ renpy.transition(dissolve)
                            hide ten0c
                            hide ten0clop
                            show ten4a
                            show ten4ok
                            te "Do you want to play with me more?"
                            $ renpy.transition(dissolve)
                            show ten4v1
                            hide ten4ok
                            show ten4cl
                            te "Ahhhhhh !!! *moan*"
                            p "Is it good?"
                            te "Ahhh... *moan* Yesss...."
                            p "And if I turn it on..."
                            $ renpy.transition(dissolve)
                            show ten4v2
                            hide ten4cl
                            show ten4clop
                            te "*heavy moaning*"
                            p "Hehe..."
                            te "Fuck this is!!! *moan squirt*"
                            $ renpy.transition(dissolve)
                            show ten4v3
                            hide ten4clop
                            show ten4org
                            te "Ahhhhhh....*squirt*"
                            $ renpy.transition(dissolve)
                            show ten4milk
                            p "Wow...Is it really that good?"
                            $ renpy.transition(dissolve)
                            hide ten4v2
                            hide ten4org
                            show ten4op
                            te "Ahhh...*moan* That was awesome."
                            te "MMMm..... *moan*"
                            "You slowly take the dildo out of Tenten pussy."
                            $ renpy.transition(dissolve)
                            hide ten4v1
                            hide ten4milk
                            te "I wonder if it will be this good next time."
                            p "It is only one way to find the answer."
                            te "Yesss... We need to do it again."
                            p "Exactly...."
                            te "But now I want to take a nap...."
                            p "Sure..."
                            scene black with circleirisin
                            show nrock0 with circleirisout
                            jump nrock
                        else:
                            p "I bring a toy today."
                            te "You mean?"
                            "You showed a dildo to Tenten."
                            te "Mmm... This looks interesting... What about some foreplay first?"
                            p "*smooch*"
                            "You kiss Tenten and start to undress her slowly."
                            $ renpy.transition(dissolve)
                            hide ten0ok
                            hide ten0a
                            show ten0c
                            show ten0clop
                            te "Mmmm...*moan*"
                            "You start to rub her pussy."
                            te "Yes.... *moan* and now..."
                            $ renpy.transition(dissolve)
                            hide ten0c
                            hide ten0clop
                            show ten4a
                            show ten4ok
                            te "Mmmmm...*moan* I want more..."
                            $ renpy.transition(dissolve)
                            show ten4v1
                            hide ten4ok
                            show ten4cl
                            te "Ahhhhhh !!! *moan*"
                            p "Nice..."
                            te "Ahhh... *moan* Yesss...."
                            p "And if I turn it on..."
                            $ renpy.transition(dissolve)
                            show ten4v2
                            hide ten4cl
                            show ten4clop
                            te "*heavy moaning*"
                            p "Hehe..."
                            te "Fuck this is!!! *moan squirt*"
                            $ renpy.transition(dissolve)
                            show ten4v3
                            hide ten4clop
                            show ten4org
                            te "Ahhhhhh....*squirt*"
                            $ renpy.transition(dissolve)
                            show ten4milk
                            p "Great..."
                            $ renpy.transition(dissolve)
                            hide ten4v2
                            hide ten4org
                            show ten4op
                            te "Ahhh...*moan* That was awesome."
                            te "MMMm..... *moan*"
                            "You slowly take the dildo out of Tenten pussy."
                            $ renpy.transition(dissolve)
                            hide ten4v1
                            hide ten4milk
                            te "It is nice to play like this."
                            p "..."
                            te "I feel really tired and relaxed right now."
                            p "It is ok... We can rest for a moment together."
                            te "That sounds good..."
                            scene black with circleirisin
                            show nrock0 with circleirisout
                            jump nrock

                    "Fuck her boobs":
                        if tenmission <= 8:
                            p "I want to play with you a little."
                            te "Play with me? How?"
                            p "Maybe, play with your boobs and cum between them."
                            te "Hmmm... Now I do not have a mood for it."
                            te "You need to play with me first to earn a proper tit fuck"
                            jump tentenfuckw

                        elif tenmission == 9:
                            p "I want to play with you a little."
                            te "Play with me? How?"
                            p "Maybe, play with your boobs and cum between them."
                            te "Hmm... Just show me how you want to do it..."
                            $ tenmission = 10
                            p "First I will *smooch*"
                            "You kiss Tenten and start to undress her."
                            $ renpy.transition(dissolve)
                            hide ten0ok
                            hide ten0a
                            show ten0c
                            show ten0clop
                            te "MMm... That is a good start..."
                            "You slowly put Tenten on the ground."
                            $ renpy.transition(dissolve)
                            hide ten0c
                            hide ten0clop
                            show ten3a
                            show ten3ok
                            p "And now..."
                            $ renpy.transition(dissolve)
                            show ten3tf1
                            te "You are already pretty hard."
                            p "Yeah...."
                            $ renpy.transition(dissolve)
                            hide ten3tf1
                            show ten3tf2
                            te "Nice..."
                            $ renpy.transition(dissolve)
                            hide ten3tf2
                            show ten3tf3
                            hide ten3ok
                            show ten3cl
                            p "Fuck...."
                            $ renpy.transition(dissolve)
                            hide ten3tf3
                            show ten3tf4
                            p "Your boobs is awesome..."
                            $ renpy.transition(dissolve)
                            hide ten3tf4
                            show ten3tf3
                            te "Mmm... I feel it between my boobs."
                            $ renpy.transition(dissolve)
                            hide ten3tf3
                            show ten3tf2
                            p "More!!!"
                            $ renpy.transition(dissolve)
                            hide ten3tf2
                            show ten3tf3
                            p "Yeah!!!"
                            $ renpy.transition(dissolve)
                            hide ten3tf3
                            show ten3tf4
                            hide ten3cl
                            show ten3ok
                            te "Is it a good feeling?"
                            $ renpy.transition(dissolve)
                            hide ten3tf4
                            show ten3tf3
                            p "It is awesome!"
                            $ renpy.transition(dissolve)
                            hide ten3tf3
                            show ten3tf2
                            p "I think I will cum soon..."
                            $ renpy.transition(dissolve)
                            hide ten3tf2
                            show ten3tf3
                            te "Yes... Cum on my face!"
                            $ renpy.transition(dissolve)
                            hide ten3tf3
                            show ten3tf4
                            p "Sure... *splurt*"
                            $ renpy.transition(dissolve)
                            hide ten3ok
                            show ten3cl
                            show ten3tf5
                            te "Ah! *drip*"
                            $ renpy.transition(dissolve)
                            show ten3tf6
                            p "Nice... It look good on you..."
                            te "You really cum on my face."
                            p "Yes and?"
                            te "I need to wash it down."
                            $ renpy.transition(dissolve)
                            hide ten3tf4
                            hide ten3tf5
                            hide ten3tf6
                            hide ten3cl
                            hide ten3a
                            p "huh?"
                            "She jumped in the water and start swimming."
                            scene black with circleirisin
                            "You decided to relax on the shore. When you woke up Tenten was gone."
                            show nrock0 with circleirisout
                            jump nrock

                        else:
                            p "I want to play with you a little."
                            te "Ok... Just come closer to me..."
                            p "*smooch*"
                            "You kiss Tenten and start to undress her."
                            $ renpy.transition(dissolve)
                            hide ten0ok
                            hide ten0a
                            show ten0c
                            show ten0clop
                            te "Mmm... That is a good start. Now stick in between my boobs."
                            "You slowly put Tenten on the ground."
                            $ renpy.transition(dissolve)
                            hide ten0c
                            hide ten0clop
                            show ten3a
                            show ten3ok
                            p "Like this?"
                            $ renpy.transition(dissolve)
                            show ten3tf1
                            te "Yes.... Massage them with your dick."
                            p "...."
                            $ renpy.transition(dissolve)
                            hide ten3tf1
                            show ten3tf2
                            te "Mmmmm..."
                            $ renpy.transition(dissolve)
                            hide ten3tf2
                            show ten3tf3
                            hide ten3ok
                            show ten3cl
                            p "Fuck...."
                            $ renpy.transition(dissolve)
                            hide ten3tf3
                            show ten3tf4
                            p "Your boobs is great..."
                            $ renpy.transition(dissolve)
                            hide ten3tf4
                            show ten3tf3
                            te "Mmm... I feel it between my boobs."
                            $ renpy.transition(dissolve)
                            hide ten3tf3
                            show ten3tf2
                            p "More!!!"
                            $ renpy.transition(dissolve)
                            hide ten3tf2
                            show ten3tf3
                            p "Yeah!!!"
                            $ renpy.transition(dissolve)
                            hide ten3tf3
                            show ten3tf4
                            hide ten3cl
                            show ten3ok
                            te "Is it a good feeling?"
                            $ renpy.transition(dissolve)
                            hide ten3tf4
                            show ten3tf3
                            p "It is amazing!"
                            $ renpy.transition(dissolve)
                            hide ten3tf3
                            show ten3tf2
                            p "I think I will cum soon..."
                            $ renpy.transition(dissolve)
                            hide ten3tf2
                            show ten3tf3
                            te "Cum on my face!"
                            $ renpy.transition(dissolve)
                            hide ten3tf3
                            show ten3tf4
                            p "Sure... *splurt*"
                            $ renpy.transition(dissolve)
                            hide ten3ok
                            show ten3cl
                            show ten3tf5
                            te "Ah! *drip*"
                            $ renpy.transition(dissolve)
                            show ten3tf6
                            p "Nice... It look good on you..."
                            te "MMM... It taste good."
                            p "???"
                            te "But I still need to wash it down."
                            $ renpy.transition(dissolve)
                            hide ten3tf4
                            hide ten3tf5
                            hide ten3tf6
                            hide ten3cl
                            hide ten3a
                            p "huh?"
                            "She jumped in the water and start swimming."
                            scene black with circleirisin
                            "You decided to relax on the shore. When you woke up Tenten was gone."
                            show nrock0 with circleirisout
                            jump nrock

                    "Fuck her pussy":
                        if tenmission <= 9:
                            p "I think we can try something more today."
                            te "What exactly you mean?"
                            p "I really want to fuck you."
                            te "What? NO! It is too soon for it."
                            p "..."
                            te "But we can do something else."
                            jump tentenfuckw
                        elif tenmission == 10:
                            p "I think we can try something more today."
                            te "What exactly you mean?"
                            p "I really want to fuck you."
                            te "Hmm... I don't know... I think are we ready for it?"
                            $ tenmission = 11
                            p "I think we need to try it and then we will know..."
                            te "...."
                            p "What?"
                            te "I am just not ready for it... Sorry..."
                            scene black with circleirisin
                            te "Tenten left the place."
                            show nrock0 with circleirisout
                            jump nrock

                        elif tenmission == 11:
                            p "I think we can try something more today."
                            te "What exactly you mean?"
                            p "I really want to fuck you."
                            te "Sorry but I am still not ready."
                            p "Ok..."
                            te "But we can do something else."
                            jump tentenfuckw

                        elif tenmission == 12:
                            p "I think we can try something more today."
                            te "What exactly you mean?"
                            p "I really want to fuck you."
                            te "Hmm... I don't know... I think are we ready for it?"
                            $ tenmission = 13
                            p "I think we are."
                            p "*smooch*"
                            te "Mmmm..*smooch*"
                            $ renpy.transition(dissolve)
                            hide ten0a
                            hide ten0ok
                            show ten3a
                            show ten3ok
                            te "%(p)s ...."
                            p "Yes Tenten?"
                            te "I really want to feel you inside of me."
                            p "Ok..."
                            $ renpy.transition(dissolve)
                            hide ten3ok
                            show ten3sho
                            show ten3f1
                            te "Huh?"
                            p "Are you allright?"
                            te "Yes just stick it in..."
                            $ renpy.transition(dissolve)
                            hide ten3f1
                            show ten3f2
                            te "Ahhh...*moan*"
                            $ renpy.transition(dissolve)
                            hide ten3f2
                            show ten3f3
                            hide ten3sho
                            show ten3cl
                            te "Yesss...*moan*"
                            $ renpy.transition(dissolve)
                            hide ten3f3
                            show ten3f4
                            p "Yeah... This is good..."
                            $ renpy.transition(dissolve)
                            hide ten3f4
                            show ten3f3
                            te "More!"
                            $ renpy.transition(dissolve)
                            hide ten3f3
                            show ten3f2
                            te "Ahhh...*moan*"
                            $ renpy.transition(dissolve)
                            hide ten3f2
                            show ten3f3
                            p "That pussy!!!"
                            $ renpy.transition(dissolve)
                            hide ten3f3
                            show ten3f4
                            te "So good...*moan*"
                            $ renpy.transition(dissolve)
                            hide ten3f4
                            show ten3f3
                            hide ten3cl
                            show ten3clo
                            p "Yeah..."
                            $ renpy.transition(dissolve)
                            hide ten3f3
                            show ten3f2
                            te "Fuck me!!! *heavy moaning*"
                            $ renpy.transition(dissolve)
                            hide ten3f2
                            show ten3f3
                            p "Shit!!!"
                            $ renpy.transition(dissolve)
                            hide ten3f3
                            show ten3f4
                            hide ten3clo
                            show ten3org
                            te "Ahhhh...*heavy moaning*"
                            $ renpy.transition(dissolve)
                            hide ten3f4
                            show ten3f3
                            p "Yes!!!"
                            menu:
                                "Cum in":
                                    $ renpy.transition(dissolve)
                                    hide ten3f3
                                    show ten3f4
                                    p "I am almost!!!*splurt*"
                                    $ renpy.transition(dissolve)
                                    show ten3f7
                                    te "Mmm...*hevay moaning*"
                                    $ renpy.transition(dissolve)
                                    show ten3f8
                                    p "Yeah...."
                                    te "Ahhhh... *moan*"
                                    te "Sperm is flowing out of my pussy now..."
                                    p "Yeah sorry."
                                    te "Ok... I just wash myself in waterfall."
                                    p "Good..."

                                "Cum out":
                                    $ renpy.transition(dissolve)
                                    hide ten3f3
                                    show ten3f2
                                    p "Shit...."
                                    $ renpy.transition(dissolve)
                                    hide ten3f2
                                    show ten3f1
                                    show ten3f5
                                    p "Yeah... *splurt*"
                                    $ renpy.transition(dissolve)
                                    show ten3f6
                                    te "Mmmmm... *moan*"
                                    p "That was just... huh...."
                                    te "Yes... *moan* So good..."
                                    te " You are really amazing *moan*"
                                    te "So much sperm...."
                                    p "Hehe... You need to clean yourself now."
                                    te "Mmm...*moan* Yes..."
                            scene black with circleirisin
                            "Tenten jump into the water and start cleaning herself."
                            "You were finally able to fuck her pussy... You feel really hyped now."
                            show nrock0 with circleirisout
                            jump nrock

                        else:
                            p "I really want to fuck your pussy."
                            te "Mmmm..*smooch*"
                            p "*smooch*"
                            te "So what do you waiting for?"
                            $ renpy.transition(dissolve)
                            hide ten0a
                            hide ten0ok
                            show ten3a
                            show ten3ok
                            p "Nothing..."
                            te "Just stick it in %(p)s ...."
                            p "Ok..."
                            $ renpy.transition(dissolve)
                            hide ten3ok
                            show ten3sho
                            show ten3f1
                            te "Come on...."
                            p "Again that funny face."
                            te "Yes, just stick it in..."
                            $ renpy.transition(dissolve)
                            hide ten3f1
                            show ten3f2
                            te "Ahhh...*moan*"
                            $ renpy.transition(dissolve)
                            hide ten3f2
                            show ten3f3
                            hide ten3sho
                            show ten3cl
                            te "Yesss...*moan*"
                            $ renpy.transition(dissolve)
                            hide ten3f3
                            show ten3f4
                            p "Yeah... This is good..."
                            $ renpy.transition(dissolve)
                            hide ten3f4
                            show ten3f3
                            te "More!"
                            $ renpy.transition(dissolve)
                            hide ten3f3
                            show ten3f2
                            te "Ahhh...*moan*"
                            $ renpy.transition(dissolve)
                            hide ten3f2
                            show ten3f3
                            p "That pussy!!!"
                            $ renpy.transition(dissolve)
                            hide ten3f3
                            show ten3f4
                            te "So good...*moan*"
                            $ renpy.transition(dissolve)
                            hide ten3f4
                            show ten3f3
                            hide ten3cl
                            show ten3clo
                            p "Yeah..."
                            $ renpy.transition(dissolve)
                            hide ten3f3
                            show ten3f2
                            te "Fuck me!!! *heavy moaning*"
                            $ renpy.transition(dissolve)
                            hide ten3f2
                            show ten3f3
                            p "Shit!!!"
                            $ renpy.transition(dissolve)
                            hide ten3f3
                            show ten3f4
                            hide ten3clo
                            show ten3org
                            te "Ahhhh...*heavy moaning*"
                            $ renpy.transition(dissolve)
                            hide ten3f4
                            show ten3f3
                            p "Fuck I should..."
                            menu tentenpussyfuck:
                                "Lightning style":
                                    if clips ==0:
                                        "You need to buy chakra clips first."
                                        jump tentenpussyfuck
                                    else:
                                        p "Time to try something..."
                                        $ renpy.transition(dissolve)
                                        hide ten3f3
                                        show ten3f4
                                        te "Ahhh... *moan* What?"
                                        if tenmission == 13:
                                            $ tenmission = 14
                                        $ renpy.transition(dissolve)
                                        hide ten3f4
                                        show ten3f3
                                        p "This...*clamp*"
                                        $ renpy.transition(dissolve)
                                        hide ten3f3
                                        show ten3f2
                                        show ten3l1
                                        te "Ahh...*moan*"
                                        $ renpy.transition(dissolve)
                                        hide ten3f2
                                        show ten3f3
                                        hide ten3org
                                        show ten3sho
                                        te "What do you want to do with it?"
                                        $ renpy.transition(dissolve)
                                        hide ten3f3
                                        show ten3f4
                                        p "Lightning style! *zap*"
                                        $ renpy.transition(dissolve)
                                        hide ten3f4
                                        show ten3f3
                                        show ten3l2
                                        te "Mmmm... It is a gentle tingle feeling."
                                        $ renpy.transition(dissolve)
                                        hide ten3f3
                                        show ten3f2
                                        p "Yeah... And now..."
                                        $ renpy.transition(dissolve)
                                        hide ten3f2
                                        show ten3f3
                                        p "More power!!!"
                                        $ renpy.transition(dissolve)
                                        hide ten3f3
                                        show ten3f4
                                        show ten3l3
                                        te "ARgggg *moan pain*"
                                        $ renpy.transition(dissolve)
                                        hide ten3f3
                                        show ten3f2
                                        hide ten3sho
                                        show ten3org
                                        te "This is *pain* ahhh *moan*"
                                        $ renpy.transition(dissolve)
                                        hide ten3f2
                                        show ten3f3
                                        te "*squirt*"
                                        $ renpy.transition(dissolve)
                                        hide ten3f3
                                        show ten3f4
                                        show ten3milk
                                        te "Yeah!!!! *heavy moaning*"
                                        $ renpy.transition(dissolve)
                                        hide ten3f4
                                        show ten3f3
                                        hide ten3l3
                                        p "Fuck your milk is flowing out!"
                                        $ renpy.transition(dissolve)
                                        hide ten3f3
                                        show ten3f2
                                        hide ten3l2
                                        te "Ahhh...*moan*"
                                        $ renpy.transition(dissolve)
                                        hide ten3f2
                                        show ten3f3
                                        te "More....*moan*"
                                        $ renpy.transition(dissolve)
                                        hide ten3f3
                                        show ten3f4
                                        p "Hehe... Maybe later... Now is time for..."
                                        $ renpy.transition(dissolve)
                                        hide ten3f4
                                        show ten3f3
                                        hide ten3l1
                                        hide ten3milk
                                        jump tentenpussyfuck

                                "Water style":
                                    $ renpy.transition(dissolve)
                                    hide ten3w1
                                    hide ten3w2
                                    hide ten3w3
                                    hide ten3f3
                                    show ten3f4
                                    p "Use this!"
                                    p "Water style!"
                                    $ renpy.transition(dissolve)
                                    show ten3w1
                                    hide ten3f4
                                    show ten3f3
                                    te "%(p)s ..."
                                    p "Water dragoon jutsu!!!"
                                    $ renpy.transition(dissolve)
                                    show ten3w2
                                    hide ten3f3
                                    show ten3f2
                                    te "Ahhhh... *heavy moaning*"
                                    $ renpy.transition(dissolve)
                                    hide ten3f2
                                    show ten3f3
                                    p "Water style jutsu!"
                                    $ renpy.transition(dissolve)
                                    show ten3w3
                                    hide ten3f3
                                    show ten3f4
                                    te "Yesss....*heavy moaning*"
                                    $ renpy.transition(dissolve)
                                    hide ten3f4
                                    show ten3f3
                                    p "And now..."
                                    jump tentenpussyfuck


                                "Cum in":
                                    $ renpy.transition(dissolve)
                                    hide ten3f3
                                    show ten3f4
                                    p "I am almost!!!*splurt*"
                                    $ renpy.transition(dissolve)
                                    show ten3f7
                                    te "Mmm...*hevay moaning*"
                                    $ renpy.transition(dissolve)
                                    show ten3f8
                                    hide ten3org
                                    show ten3ok
                                    p "Yeah...."
                                    te "Ahhhh... *moan*"
                                    te "Sperm is flowing out of my pussy now..."
                                    p "Yeah sorry."
                                    te "Ok... I just wash myself in waterfall."
                                    p "Good..."
                                    scene black with circleirisin
                                    "Tenten jump into the water and start cleaning herself."
                                    show nrock0 with circleirisout
                                    jump nrock


                                "Cum out":
                                    $ renpy.transition(dissolve)
                                    hide ten3f3
                                    show ten3f2
                                    p "Shit...."
                                    $ renpy.transition(dissolve)
                                    hide ten3f2
                                    show ten3f1
                                    show ten3f5
                                    hide ten3org
                                    show ten3ok
                                    p "Yeah... *splurt*"
                                    $ renpy.transition(dissolve)
                                    show ten3f6
                                    te "Mmmmm... *moan*"
                                    p "That was just... huh...."
                                    te "Yes... *moan* So good..."
                                    te " You are really amazing *moan*"
                                    te "So much sperm...."
                                    p "Hehe... You need to clean yourself now."
                                    te "Mmm...*moan* Yes..."
                                    scene black with circleirisin
                                    "Tenten jump into the water and start cleaning herself."
                                    show nrock0 with circleirisout
                                    jump nrock



                    "Fuck her ass":
                        if tenmission <= 13:
                            p "I want to fuck your ass right now!"
                            te "%(p)s ! I am not ready fir this!"
                            p "But..."
                            te "Just... No!"
                            jump tentenfuckw

                        elif tenmission == 14:
                            p "I want to fuck your ass right now!"
                            $ tenmission = 15
                            te "%(p)s !"
                            p "What?"
                            te "Fine.... Just do it gently."
                            p "Sure... Hehe..."
                            $ renpy.transition(dissolve)
                            hide ten0a
                            hide ten0ok
                            "Tenten slowly take her dress off and spread legs."
                            $ renpy.transition(dissolve)
                            show ten4a
                            show ten4ok
                            te "Do you have some kind of lubricant?"
                            p "No. But do not worry, It will not hurt you."
                            $ renpy.transition(dissolve)
                            show ten4f1
                            te "Are you sure?"
                            $ renpy.transition(dissolve)
                            hide ten4f1
                            show ten4f2
                            hide ten4ok
                            show ten4sad
                            te "Ahhh!!!*pain*"
                            p "Are you ok?"
                            te "Yes... Just put it in slowly."
                            p "Sure..."
                            $ renpy.transition(dissolve)
                            hide ten4f2
                            show ten4f3
                            te "Ahhh... *moan pain*"
                            $ renpy.transition(dissolve)
                            hide ten4f3
                            show ten4f2
                            show ten4h1
                            te "My nipple!!!"
                            $ renpy.transition(dissolve)
                            hide ten4f2
                            show ten4f3
                            p "So now you are not focussing on the ass?"
                            $ renpy.transition(dissolve)
                            hide ten4f3
                            show ten4f2
                            hide ten4sad
                            show ten4clop
                            te "Ahhh *pain* Yess.. this is good... More...*moan*"
                            $ renpy.transition(dissolve)
                            hide ten4f2
                            show ten4f3
                            show ten4h2
                            te "Deeper!!! *moan*"
                            $ renpy.transition(dissolve)
                            hide ten4f3
                            show ten4f4
                            te "FUCK!!!! *moan scream*"
                            $ renpy.transition(dissolve)
                            hide ten4f4
                            show ten4f3
                            p "Oh... Your but is squeezing my dick!"
                            $ renpy.transition(dissolve)
                            hide ten4f3
                            show ten4f2
                            te "Deeper please *heavy moaning*"
                            $ renpy.transition(dissolve)
                            hide ten4f2
                            show ten4f3
                            hide ten4clop
                            show ten4org
                            te "Ahhh!!!*heavy moaning*"
                            $ renpy.transition(dissolve)
                            hide ten4f3
                            show ten4f4
                            p "Fuck this is so good!"
                            $ renpy.transition(dissolve)
                            hide ten4f4
                            show ten4f3
                            hide ten4h1
                            p "Ahhh..."
                            menu:
                                "Cum in":
                                    p "This is just..."
                                    $ renpy.transition(dissolve)
                                    hide ten4f3
                                    show ten4f4
                                    p "Fuck! *splurt*"
                                    $ renpy.transition(dissolve)
                                    show ten4f7
                                    te "Mmm...*drip*"
                                    $ renpy.transition(dissolve)
                                    show ten4f8
                                    te "Ahh... *moan* You fill my buthole with sperm...*drip*"
                                    p "Yeah... It is dripping out now."
                                    te "hehe..."
                                    te "I should clean it now..."
                                    p "I can help you."
                                    te "Yes... I know you can..."
                                    scene black with circleirisin
                                    show nrock0 with circleirisout
                                    jump nrock

                                "Cum out":
                                    p "Yeah!!!"
                                    $ renpy.transition(dissolve)
                                    hide ten4f3
                                    show ten4f2
                                    p "Take it all !!!*splurt*"
                                    $ renpy.transition(dissolve)
                                    hide ten4f2
                                    show ten4f1
                                    show ten4f5
                                    te "Ahh...*moan drip*"
                                    $ renpy.transition(dissolve)
                                    show ten4f6
                                    te "Yess... So much sperm on my belly."
                                    p "Huh..."
                                    te "That was really good..."
                                    p "Yes I think so..."
                                    te "You are still holding my boob."
                                    p "It is really soft..."
                                    te "Do you want to wash my body now?"
                                    p "Sure..."
                                    scene black with circleirisin
                                    show nrock0 with circleirisout
                                    jump nrock

                        else:
                            p "I want to fuck your ass right now!"
                            te "Hehe... I know you want..."
                            p "..."
                            $ renpy.transition(dissolve)
                            hide ten0a
                            hide ten0ok
                            "Tenten slowly take her dress off and spread legs."
                            $ renpy.transition(dissolve)
                            show ten4a
                            show ten4ok
                            te "Do you have some kind of lubricant?"
                            p "I think you already know the answer *spit*"
                            $ renpy.transition(dissolve)
                            show ten4f1
                            te "...."
                            $ renpy.transition(dissolve)
                            hide ten4f1
                            show ten4f2
                            hide ten4ok
                            show ten4sad
                            te "Ahhh!!!*pain*"
                            p "Are you ok?"
                            te "Yes... It is good..."
                            p "Sure..."
                            $ renpy.transition(dissolve)
                            hide ten4f2
                            show ten4f3
                            te "Ahhh... *moan pain*"
                            $ renpy.transition(dissolve)
                            hide ten4f3
                            show ten4f2
                            show ten4h1
                            te "Yes... Squeeze that nipple."
                            $ renpy.transition(dissolve)
                            hide ten4f2
                            show ten4f3
                            p "Sure..."
                            $ renpy.transition(dissolve)
                            hide ten4f3
                            show ten4f2
                            te "Ahhh *pain* Yess.. this is good... More...*moan*"
                            $ renpy.transition(dissolve)
                            hide ten4f2
                            show ten4f3
                            show ten4h2
                            hide ten4sad
                            show ten4clop
                            te "Deeper!!! *moan*"
                            $ renpy.transition(dissolve)
                            hide ten4f3
                            show ten4f4
                            te "FUCK!!!! *moan scream*"
                            $ renpy.transition(dissolve)
                            hide ten4f4
                            show ten4f3
                            p "Oh... Your but is squeezing my dick!"
                            $ renpy.transition(dissolve)
                            hide ten4f3
                            show ten4f2
                            te "Deeper please *heavy moaning*"
                            $ renpy.transition(dissolve)
                            hide ten4f2
                            show ten4f3
                            hide ten4clop
                            show ten4org
                            te "Ahhh!!!*heavy moaning*"
                            $ renpy.transition(dissolve)
                            hide ten4f3
                            show ten4f4
                            p "Fuck this is so good!"
                            $ renpy.transition(dissolve)
                            hide ten4f4
                            show ten4f3
                            hide ten4h1
                            p "Ahhh..."
                            menu:
                                "Cum in":
                                    p "This is just..."
                                    $ renpy.transition(dissolve)
                                    hide ten4f3
                                    show ten4f4
                                    p "Fuck! *splurt*"
                                    $ renpy.transition(dissolve)
                                    show ten4f7
                                    te "Mmm...*drip*"
                                    $ renpy.transition(dissolve)
                                    show ten4f8
                                    te "Ahh... *moan* You fill my buthole with sperm...*drip*"
                                    p "Yeah... It is dripping out now."
                                    te "hehe..."
                                    te "I should clean it now..."
                                    p "I can help you."
                                    te "Yes... I know you can..."
                                    scene black with circleirisin
                                    show nrock0 with circleirisout
                                    jump nrock

                                "Cum out":
                                    p "Yeah!!!"
                                    $ renpy.transition(dissolve)
                                    hide ten4f3
                                    show ten4f2
                                    p "Take it all !!!*splurt*"
                                    $ renpy.transition(dissolve)
                                    hide ten4f2
                                    show ten4f1
                                    show ten4f5
                                    te "Ahh...*moan drip*"
                                    $ renpy.transition(dissolve)
                                    show ten4f6
                                    te "Yess... So much sperm on my belly."
                                    p "Huh..."
                                    te "That was really good..."
                                    p "Yes I think so..."
                                    te "You are still holding my boob."
                                    p "It is really soft..."
                                    te "Do you want to wash my body now?"
                                    p "Sure..."
                                    scene black with circleirisin
                                    show nrock0 with circleirisout
                                    jump nrock

                    "Kage bunshin":
                        if tenmission <= 14:
                            p "Do you ever try something crazy?"
                            te "Like what?"
                            p "I am not sure... Kage bunshin?"
                            te "Huh???? It can be funny but... Ehm..."
                            te "Lets just do something else first."
                            jump tentenfuckw

                        else:
                            p "Do you ever try something crazy?"
                            te "Of course..."
                            if tenmission == 15:
                                $ tenmission = 16
                            p "*smooch*"
                            $ renpy.transition(dissolve)
                            hide ten0a
                            hide ten0ok
                            "Tenten slowly take her dress off and lay on her back."
                            $ renpy.transition(dissolve)
                            show ten3a
                            show ten3ok
                            te "So what do you want to do?"
                            p "This... kage bunshin no jutsu! *puff*"
                            $ renpy.transition(dissolve)
                            hide ten3ok
                            show ten3sho
                            show ten3f1
                            show ten3tf1
                            te "Huh???"
                            p "I hope you are ready for it."
                            $ renpy.transition(dissolve)
                            hide ten3tf1
                            show ten3tf2
                            hide ten3f1
                            show ten3f2
                            te "Ahh..*moan*"
                            $ renpy.transition(dissolve)
                            hide ten3tf1
                            show ten3tf2
                            hide ten3f1
                            show ten3f2
                            hide ten3sho
                            show ten3cl
                            te "Of course I am... *moan*"
                            $ renpy.transition(dissolve)
                            hide ten3tf2
                            show ten3tf3
                            hide ten3f2
                            show ten3f3
                            p "Fuck You are so hot!"
                            $ renpy.transition(dissolve)
                            hide ten3tf3
                            show ten3tf4
                            hide ten3f3
                            show ten3f4
                            te "Hehe.. Will you cum on my face?"
                            $ renpy.transition(dissolve)
                            hide ten3tf4
                            show ten3tf3
                            hide ten3f4
                            show ten3f3
                            p "Definitely!"
                            $ renpy.transition(dissolve)
                            hide ten3tf3
                            show ten3tf2
                            hide ten3f3
                            show ten3f2
                            hide ten3cl
                            show ten3clo
                            te "Hehe... *moan*"
                            $ renpy.transition(dissolve)
                            hide ten3tf2
                            show ten3tf3
                            hide ten3f2
                            show ten3f3
                            p "Fuck!!! It is just too good!"
                            $ renpy.transition(dissolve)
                            hide ten3tf3
                            show ten3tf4
                            show ten3tf5
                            hide ten3f4
                            show ten3f3
                            hide ten3clo
                            show ten3org
                            p "Yeah!!! *splurt*"
                            $ renpy.transition(dissolve)
                            show ten3tf6
                            hide ten3f3
                            show ten3f2
                            te "Ahhh... *heavy moaning*"
                            $ renpy.transition(dissolve)
                            hide ten3f2
                            show ten3f3
                            te "Yes, cum on my body! *moan scream*"
                            $ renpy.transition(dissolve)
                            hide ten3f3
                            show ten3f4
                            te "Ahhh...*heavy moaning*"
                            $ renpy.transition(dissolve)
                            hide ten3f4
                            show ten3f3
                            show ten3milk
                            te "Ahhh...*heavy moaning*"
                            $ renpy.transition(dissolve)
                            hide ten3f3
                            show ten3f2
                            p "Fuck!!!*splurt*"
                            $ renpy.transition(dissolve)
                            hide ten3f2
                            show ten3f1
                            show ten3f5
                            te "Yesss!!!*moan drip*"
                            $ renpy.transition(dissolve)
                            show ten3f6
                            p "Fuck! You are really amazing!"
                            te "Mmmm...*moan*"
                            te "Thanks..."
                            p "Are you ok?"
                            te "Yes... It was really awesome..."
                            te "Ahhhh...*sweet moaning*"
                            te "I just need a minute or two to recover... My pussy and boobs are trembling..."
                            p "Sure."
                            scene black with circleirisin
                            show nrock0 with circleirisout
                            jump nrock




                    "Use Namigan":
                        if tenslave == 0:
                            p "I want to show you something."
                            $ tenslave = 1
                            te "Ok... What is it?"
                            p "My Namigan..."
                            $ renpy.transition(dissolve)
                            hide ten0ok
                            show ten0op
                            te "I was wondering when you decide to tell me about it."
                            p "I am not sure how it works right now. I need a lot of training to completely understand it."
                            te "I understand every power need training to master it."
                            p "Do you want to help me with it?"
                            te "Help you? How?"
                            p "I will test it on you."
                            $ renpy.transition(dissolve)
                            hide ten0op
                            show ten0shock
                            te "What?"
                            p "I just use it and see what will happen."
                            te "That sounds dangerous."
                            p "But it is for good things."
                            $ renpy.transition(dissolve)
                            hide ten0shock
                            show ten0cl
                            te "I am not sure %(p)s. Give me a day to think about it."
                            p "Ok...."
                            te "Hmm... "
                            scene black with circleirisin
                            show nrock0 with circleirisout
                            jump nrock
                        elif tenslave == 1:
                            p "Can I use my Namigan on you?"
                            te "I was thinking about it today..."
                            p "And?"
                            $ renpy.transition(dissolve)
                            hide ten0ok
                            show ten0op
                            te "You can use it. But be carefull."
                            p "Sure..."
                            p "Namigan!!!"
                            if eyes  <= 5:
                                te "..."
                                $ renpy.transition(dissolve)
                                hide ten0op
                                show ten0cl
                                p "Tenten?"
                                te "Yes?"
                                $ renpy.transition(dissolve)
                                hide ten0cl
                                show ten0ok
                                te "What just happened?"
                                p "It looks like nothing at all."
                                te "And what it mean?"
                                p "My namigan is not working. It is probably too weak."
                                $ renpy.transition(dissolve)
                                hide ten0ok
                                show ten0sad
                                te "That is bad right?"
                                p "Yes... But do you feel anything?"
                                te "Just a little tingle."
                                p "Hmm..."
                                te "Do not worry we can test it later and do other things now."
                                te "Do you want to do something else?"
                                jump tentenfuckw
                            else:
                                $ renpy.transition(dissolve)
                                hide ten0op
                                show ten0cl
                                p "Tenten?"
                                te "..."
                                p "Open your eyes."
                                $ renpy.transition(dissolve)
                                hide ten0cl
                                show ten0nok
                                p "Nice..."
                                $ tenslave = 2
                                p "I wonder if you obey me."
                                p "Strip!"
                                $ renpy.transition(dissolve)
                                hide ten0nok
                                hide ten0a
                                show ten0c
                                show ten0nok
                                p "Hmm.. You complete it without any hesitation."
                                p "It is a really good start."
                                p "I wonder if you react to this."
                                p "Water style!"
                                $ renpy.transition(dissolve)
                                show ten0w1
                                te "..."
                                p "Nothing?"
                                te "mhmmmm...." with hpunch
                                p "Ou! What was that?"
                                p "Quick dress!"
                                $ renpy.transition(dissolve)
                                hide ten0nok
                                hide ten0c
                                show ten0a
                                show ten0nok
                                p "Namigan KAI!"
                                $ renpy.transition(dissolve)
                                hide ten0nok
                                show ten0ok
                                te "What was that?"
                                p "Do you remember anything?"
                                te "No. What happened? I feel wet."
                                p "????"
                                te "Just a little, but it is weird."
                                p "Is it the only thing you feel?"
                                $ renpy.transition(dissolve)
                                hide ten0ok
                                show ten0op
                                te "Yes. How long I was under Namigan?"
                                p "Maybe a minute or two. What do you feel?"
                                te "I am not sure... It was like sleeping."
                                p "Did it hurt?"
                                $ renpy.transition(dissolve)
                                hide ten0op
                                show ten0ok
                                te "No... It was fine."
                                p "So, can we continue again next time?"
                                $ renpy.transition(dissolve)
                                hide ten0ok
                                show ten0cl
                                te "Sure... We can continue right now if you want."
                                p "Thanks, but I need to refill my chakra. It cost me more power than I thought."
                                te "Ok... I want to swim now. You can join me if you want."
                                p "I will just lay here for a moment."
                                te "Ok...."
                                scene black with circleirisin
                                show nrock0 with circleirisout
                                jump nrock

                        elif tenslave == 2:
                            if eyes  <= 5:
                                te "..."
                                $ renpy.transition(dissolve)
                                hide ten0op
                                show ten0cl
                                p "Tenten?"
                                te "Yes?"
                                $ renpy.transition(dissolve)
                                hide ten0cl
                                show ten0ok
                                te "What just happened?"
                                p "It looks like nothing at all."
                                te "And what it mean?"
                                p "My namigan is not working. It is probably too weak."
                                $ renpy.transition(dissolve)
                                hide ten0ok
                                show ten0sad
                                te "That is bad right?"
                                p "Yes... But do you feel anything?"
                                te "Just a little tingle."
                                p "Hmm..."
                                te "Do not worry we can test it later and do other things now."
                                te "Do you want to do something else?"
                                jump tentenfuckw
                            else:
                                p "Can I use my Namigan on you?"
                                te "Of course..."
                                $ renpy.transition(dissolve)
                                hide ten0ok
                                show ten0op
                                te "But be carefull."
                                p "Sure..."
                                p "Namigan!!!"
                                $ renpy.transition(dissolve)
                                hide ten0op
                                show ten0cl
                                p "Tenten?"
                                te "..."
                                p "Open your eyes."
                                $ renpy.transition(dissolve)
                                hide ten0cl
                                show ten0nok
                                p "Nice..."
                                p "Yes! It worked again!"
                                p "Now, Strip!"
                                $ renpy.transition(dissolve)
                                hide ten0nok
                                hide ten0a
                                show ten0c
                                show ten0nok
                                p "Hehe... Nice... But you miss something..."
                                p "Maybe some nice text on your body..."
                                menu:
                                    "Use pen":
                                        $ renpy.transition(dissolve)
                                        show ten0text
                                        p "Yes... This is better..."
                                    "Meh":
                                        p "Or maybe not."
                                p "Now is time to test my powers."
                                p "What else should I do now?"
                                menu:
                                    "Lightning style":
                                        p "Time to try this... *clamp*"
                                        $ renpy.transition(dissolve)
                                        show ten0l1
                                        te "Ouch...."
                                        p "And this... *clamp*"
                                        $ renpy.transition(dissolve)
                                        show ten0l2
                                        hide ten0nok
                                        show ten0nop
                                        te "Ahhhh...*pain*"
                                        p "So you finally feel something right?"
                                        te "...."
                                        p "Lightning tingling!"
                                        $ renpy.transition(dissolve)
                                        show ten0l3
                                        p "More power!"
                                        $ renpy.transition(dissolve)
                                        show ten0l4
                                        hide ten0nop
                                        show ten0nshock
                                        te "Arggg!!! *moan pain*"
                                        p "Full release!"
                                        $ renpy.transition(dissolve)
                                        show ten0l5
                                        te "Ahhhh!!!!"
                                        p "YEah!"
                                        $ renpy.transition(dissolve)
                                        hide ten0nshock
                                        show ten0norg
                                        show ten0m1
                                        te "Yess!!! *heavy moaning*"
                                        $ renpy.transition(dissolve)
                                        show ten0m2
                                        p "nice... Finally something!"
                                        te "Ahhh....*moan*"
                                        $ renpy.transition(dissolve)
                                        hide ten0l4
                                        hide ten0l5
                                        p "You are really a perverse girl."
                                        $ tenslave = 3
                                        te "Hhhh.... *mumble*"
                                        $ renpy.transition(dissolve)
                                        hide ten0l3
                                        hide ten0m1
                                        p "Time to put it down..."
                                        $ renpy.transition(dissolve)
                                        hide ten0l1
                                        hide ten0l2
                                        hide ten0norg
                                        show ten0nop
                                        p "Good... Now clean yourself and dress!"
                                        $ renpy.transition(dissolve)
                                        hide ten0nop
                                        hide ten0c
                                        hide ten0m2
                                        hide ten0text
                                        p "Hurry!"
                                        $ renpy.transition(dissolve)
                                        show ten0c
                                        show ten0nok
                                        p "Namigan KAI!"
                                        $ renpy.transition(dissolve)
                                        hide ten0nok
                                        show ten0op
                                        te "Ahhh... *moan*"
                                        p "???"
                                        p "What was that?"
                                        te "I am not sure... I have a weird dream. Where I am?"
                                        p "You are here with me we was testing my Namigan. Do you feel good?"
                                        te "Yes... Actually I feel really good. It is like..."
                                        p "???"
                                        $ renpy.transition(dissolve)
                                        hide ten0op
                                        show ten0cl
                                        te "My body is..."
                                        p "What? Is something hurting you?"
                                        te "No. Everything is fine..."
                                        p "Good... I need some rest now... To refill my chakra."
                                        $ renpy.transition(dissolve)
                                        hide ten0cl
                                        show ten0ok
                                        te "Can I lay next to you?"
                                        p "Sure..."
                                        scene black with circleirisin
                                        show nrock0 with circleirisout
                                        jump nrock

                                    "Water style":
                                        p "It is a really good start."
                                        p "Water style!"
                                        $ renpy.transition(dissolve)
                                        show ten0w1
                                        te "..."
                                        p "Still nothing?"
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
                                        te "Oooo...."
                                        p "That was all? What a poor reaction."
                                        p "Now dress! It is not funny!"
                                        $ renpy.transition(dissolve)
                                        hide ten0nop
                                        hide ten0c
                                        show ten0a
                                        show ten0nok
                                        p "Namigan KAI!"
                                        $ renpy.transition(dissolve)
                                        hide ten0nok
                                        show ten0ok
                                        te "What was that?"
                                        p "Do you remember anything?"
                                        te "No. What happened? I feel wet."
                                        p "????"
                                        te "Just a little, but it is weird."
                                        p "Is it the only thing you feel?"
                                        $ renpy.transition(dissolve)
                                        hide ten0ok
                                        show ten0op
                                        te "Yes. How long I was under Namigan?"
                                        p "Maybe a minute or two. What do you feel?"
                                        te "It was almost exactly like the last time.."
                                        p "Yes... I think so."
                                        $ renpy.transition(dissolve)
                                        hide ten0op
                                        show ten0ok
                                        te "..."
                                        p "I need to refill my chakra."
                                        $ renpy.transition(dissolve)
                                        hide ten0ok
                                        show ten0cl
                                        te "Ok... I want to swim now. You can join me if you want."
                                        te "Good."
                                        scene black with circleirisin
                                        show nrock0 with circleirisout
                                        jump nrock


                        else:
                            p "I want to test my Namigan."
                            te "Sure... I am ready..."
                            p "Good..."
                            $ renpy.transition(dissolve)
                            hide ten0ok
                            show ten0op
                            te "Just be careful."
                            p "I am always very careful..."
                            p "Namigan!!!"
                            $ renpy.transition(dissolve)
                            hide ten0op
                            show ten0nok
                            p "It works nice. And now."
                            menu tennami1:
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
                                    p "Namigan KAI!"
                                    $ renpy.transition(dissolve)
                                    hide ten0nok
                                    show ten0op
                                    te "Ahhh... *moan*"
                                    p "Are you allright?"
                                    te "Yeah... wow... That was amazing."
                                    p "???"
                                    te "I am not sure why, but sometimes that you use Namigan on me, I just feel really good."
                                    p "It can be a side effect of my powers."
                                    $ renpy.transition(dissolve)
                                    hide ten0op
                                    show ten0ok
                                    te "MMM... It is a really nice side effect..."
                                    p "I am happy you like it, but I need to recover some chakra now."
                                    te "Ok...I will be here with you for a while."
                                    p "Can you give me a massage?"
                                    te "Hmpf... ok... If it is what you need."
                                    p "Yeah... I really need to feel your hands on my body..."
                                    te "Silly..."
                                    scene black with circleirisin
                                    "Tenten give you a nice massage... It was a nice relaxing after using so much chakra."
                                    show nrock0 with circleirisout
                                    jump nrock

                                "Blowjob":
                                    if eyes  <= 15:
                                        p "Is time to give me a nice blowjob."
                                        p "Now, Strip and start to suck my cock!"
                                        te "...."
                                        p "Now!!!" with hpunch
                                        te "...."
                                        p "What the fuck?"
                                        te "...."
                                        p "Obviously, she didn't listen to me. My Namigan is weak."
                                        p "I should try something else."
                                        jump tennami1

                                    if tenslave == 3:
                                        p "Is time to give me a nice blowjob."
                                        p "Now, Strip and start to suck my cock!"
                                        te "...."
                                        p "Now!!!" with hpunch
                                        $ tenslave = 4
                                        $ renpy.transition(dissolve)
                                        hide ten0nok
                                        hide ten0a
                                        p "Yeah... This is nice... Suck it!"
                                        $ renpy.transition(dissolve)
                                        show ten2a
                                        show ten2sad
                                        show ten2bl1
                                        te "Mmmghhgh... *mumble*"
                                        p "Yes... Just like that..."
                                        $ renpy.transition(dissolve)
                                        hide ten2bl1
                                        show ten2bl2
                                        te "Grggg... *cough*"
                                        $ renpy.transition(dissolve)
                                        hide ten2bl2
                                        show ten2bl3
                                        p "You are not really good at this. Use your tongue!"
                                        te "mmhmhm* mumble gough*"
                                        $ renpy.transition(dissolve)
                                        hide ten2sad
                                        show ten2f
                                        hide ten2bl3
                                        show ten2bl2
                                        p "Who cares..."
                                        $ renpy.transition(dissolve)
                                        hide ten2bl2
                                        show ten2bl1
                                        te "gerrg...*gag*"
                                        $ renpy.transition(dissolve)
                                        hide ten2bl1
                                        show ten2bl2
                                        p "You want to breath?"
                                        $ renpy.transition(dissolve)
                                        hide ten2bl2
                                        show ten2bl3
                                        p "Use your nose bitch!"
                                        $ renpy.transition(dissolve)
                                        hide ten2bl3
                                        show ten2bl2
                                        te "mmhm.... *mumble cough*"
                                        $ renpy.transition(dissolve)
                                        hide ten2bl2
                                        show ten2bl1
                                        p "Yeah..."
                                        $ renpy.transition(dissolve)
                                        hide ten2bl1
                                        show ten2bl2
                                        hide ten2f
                                        show ten2org
                                        p "This will be fast..."
                                        $ renpy.transition(dissolve)
                                        hide ten2bl2
                                        show ten2bl3
                                        p "Just... *splurt*"
                                        $ renpy.transition(dissolve)
                                        show ten2bl4
                                        p "Take it! *splurt*"
                                        $ renpy.transition(dissolve)
                                        show ten2bl5
                                        p "Ahhhhh... That was good..."
                                        te "*slurp Gag cough*"
                                        p "But you need to train a lot... Drink it now!"
                                        te "gghhgm...*slurp choke*"
                                        p "Quick!"
                                        $ renpy.transition(dissolve)
                                        hide ten2bl4
                                        hide ten2bl5
                                        hide ten2bl3
                                        p "Goood girl... Time to put your clothes on."
                                        $ renpy.transition(dissolve)
                                        hide ten2org
                                        hide ten2a
                                        p "...."
                                        $ renpy.transition(dissolve)
                                        show ten0a
                                        show ten0nok
                                        p "Namigan KAI!"
                                        $ renpy.transition(dissolve)
                                        hide ten0nok
                                        show ten0op
                                        te "..."
                                        te "What just happened?"
                                        p "Why you asking?"
                                        te "I do not feel anything now... Just some weird taste."
                                        p "I am not sure... I just try to use Namigan for a ehm.... Shorter time."
                                        $ renpy.transition(dissolve)
                                        hide ten0op
                                        show ten0cl
                                        te "This is not good enough. You need to do it properly next time!"
                                        p "Ehm... I will try harder next time."
                                        te "Good... Now we can do something else if you want..."
                                        p "I just need rest now..."
                                        te "Sure..."
                                        scene black with circleirisin
                                        show nrock0 with circleirisout
                                        jump nrock



                                    else:
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
                                        menu tentenjf1:
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
                                                p "Good girl... Namigan KAI!"
                                                $ renpy.transition(dissolve)
                                                hide ten0nok
                                                show ten0ok
                                                te "Ahhh... *moan* That was good..."
                                                $ renpy.transition(dissolve)
                                                hide ten0ok
                                                show ten0shock
                                                show ten0shy
                                                te "Huh? Sorry..."
                                                p "Nice reaction..."
                                                te "It was just so good and... Huh..."
                                                p "I am glad you enjoy it... I enjoyed it too."
                                                te "What?"
                                                p "Hehe... I just need some relax now... You can swim or whatever you want to do."
                                                $ renpy.transition(dissolve)
                                                hide ten0shock
                                                show ten0op
                                                te "Yeah.. Good idea..."
                                                scene black with circleirisin
                                                show nrock0 with circleirisout
                                                jump nrock

                                            "Boob expansion":
                                                if expscroll ==0:
                                                    "You need to buy expansion scroll first!"
                                                    jump tentenjf1
                                                else:
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
                                                    p "Good girl... Namigan KAI!"
                                                    $ renpy.transition(dissolve)
                                                    hide ten0nok
                                                    show ten0ok
                                                    te "Ahhh... *moan* That was good..."
                                                    $ renpy.transition(dissolve)
                                                    hide ten0ok
                                                    show ten0shock
                                                    show ten0shy
                                                    te "Huh? Sorry..."
                                                    p "Nice reaction..."
                                                    te "It was just so good and my boobs are... Huh..."
                                                    p "Your boobs?"
                                                    te "I am not sure."
                                                    p "It is ok, but I need some relax now..."
                                                    $ renpy.transition(dissolve)
                                                    hide ten0shock
                                                    show ten0op
                                                    te "Yeah.. Good idea..."
                                                    scene black with circleirisin
                                                    show nrock0 with circleirisout
                                                    jump nrock


                                            "Titfuck":
                                                if expscroll ==0:
                                                    "You need to buy expansion scroll first!"
                                                    jump tentenjf1

                                                else:
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
                                                    p "Good girl... Namigan KAI!"
                                                    $ renpy.transition(dissolve)
                                                    hide ten0nok
                                                    show ten0ok
                                                    te "Ahhh... *moan* My boobies!"
                                                    $ renpy.transition(dissolve)
                                                    hide ten0ok
                                                    show ten0shock
                                                    show ten0shy
                                                    te "They are so..."
                                                    p "Hehe..."
                                                    te "Uh... Sorry it is just..."
                                                    p "I understand... It is ok."
                                                    te "Is it?"
                                                    p "Yeah... Now go swim and I will stay here and rest for a while..."
                                                    $ renpy.transition(dissolve)
                                                    hide ten0shock
                                                    show ten0op
                                                    te "Yeah.. Good idea..."
                                                    scene black with circleirisin
                                                    show nrock0 with circleirisout
                                                    jump nrock

                                                scene black with circleirisin
                                                show nrock0 with circleirisout
                                                jump nrock




                                "Kage bunshin":
                                    if eyes  <= 30:
                                        p "Now is time for some Kage Bunshin tricks."
                                        te "...."
                                        p "Kage Bunshin no jutsu..." with vpunch
                                        p "What the fuck?"
                                        scene black with circleirisin
                                        "Your Namigan control is at a low level. Creating more clones canceled your power and you fall out."
                                        "Tenten take care of you. It is good that she was clothed when you're passed out."
                                        show nrock0 with circleirisout
                                        jump nrock

                                    else:
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
                                        menu tenn22:
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
                                                show nrock0 with circleirisout
                                                jump nrock

                                            "Medium whip expansion":
                                                if expscroll == 0:
                                                    "You need expansion scroll for that."
                                                    jump tenn22
                                                else:
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
                                                    show nrock0 with circleirisout
                                                    jump nrock

                                            "Full expansion":
                                                if expscroll == 0:
                                                    "You need expansion scroll for that."
                                                    jump tenn22

                                                else:
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
                                                    show nrock0 with circleirisout
                                                    jump nrock


                                        scene black with circleirisin
                                        show nrock0 with circleirisout
                                        jump nrock


                            scene black with circleirisin
                            show nrock0 with circleirisout
                            jump nrock

        "Buy stuff":
            menu:
                "Instant Ramen - 50 ryo":
                    if ryo >=50:
                        $ ramen = ramen +1
                        $ ryo = ryo - 50
                        "You buy 1 ramen."
                        "Do you want something else?"
                        jump rshop
                    else:
                        "You need more money."
                        jump rshop

                "Delicious food - 250 ryo":
                    if ryo >=250:
                        $ supply = supply +1
                        $ ryo = ryo - 250
                        "You buy some delicious food."
                        "Do you want something else?"
                        jump rshop
                    else:
                        "You need more money."
                        jump rshop

                "Chocolate dessert - 400 ryo":
                    if ryo >=400:
                        $ chocolate = chocolate +1
                        $ ryo = ryo - 400
                        "You buy 1 chocolate dessert."
                        "Do you want something else?"
                        jump rshop
                    else:
                        "You need more money."
                        jump rshop

                "Buy jewel - 600 ryo":
                    if ryo >=600:
                        $ jewel = jewel +1
                        $ ryo = ryo - 600
                        "You buy 1 beautiful jewel."
                        "Do you want something else?"
                        jump rshop
                    else:
                        "You need more money."
                        jump rshop

                "Return":
                    jump rshop

        "Buy ninja equipment":
            menu:
                "Chakra shuriken - 1000 ryo":
                    if ryo >=1000:
                        $ ninjutsu = ninjutsu +1
                        $ ryo = ryo - 1000
                        "Your Ninjutsu has increased."
                        "Do you want something else?"
                        jump rshop
                    else:
                        "You need more money."
                        jump rshop
                "Legendary sword - 1000 ryo":
                    if ryo >=1000:
                        $ taijutsu = taijutsu +1
                        $ ryo = ryo - 1000
                        "Your Taijutsu has increased."
                        "Do you want something else?"
                        jump rshop
                    else:
                        "You need more money."
                        jump rshop
                "Chakra vial - 1000 ryo":
                    if ryo >=1000:
                        $ genjutsu = genjutsu +1
                        $ ryo = ryo - 1000
                        "Your Genjutsu has increased."
                        "Do you want something else?"
                        jump rshop
                    else:
                        "You need more money."
                        jump rshop
                "Return":
                    jump rshop
        "Buy special equipment":
            menu:
                "Dildo - 500 ryo":
                    if dildo ==1:
                        "You already buy it."
                        jump rshop
                    elif ryo >=500:
                        $ dildo = 1
                        $ ryo = ryo - 500
                        "You bought dildo. The store clerk gave you a weird look.."
                        "Do you want something else?"
                        jump rshop
                    else:
                        "You need more money."
                        jump rshop
                "Chakra clips - 500 ryo":
                    if clips ==1:
                        "You already buy it."
                        jump rshop
                    elif ryo >=500:
                        $ clips = 1
                        $ ryo = ryo - 500
                        "You bought chakra clips. They can help you increase.... Ehm... That doesn't matter right?"
                        "Do you want something else?"
                        jump rshop
                    else:
                        "You need more money."
                        jump rshop
                "Chakra whip - 500 ryo":
                    "This is a chakra whip. You can use this whip to steal chakra from whoever use it on."
                    "It can leave marks on the body."
                    if whip ==1:
                        "You already have one."
                        jump rshop
                    else:
                        if ryo >=500:
                            "You bought a chakra whip. Use it wisely."
                            "Do you want something else?"
                            $ whip = 1
                            $ ryo = ryo - 500
                            jump rshop
                        else:
                            "You need more money."
                            jump rshop

                "Slippery scroll - 1000 ryo":
                    "This scroll can make human skin more slippery."
                    "......"
                    "Weird."
                    if slipscroll ==1:
                        "You already have this scroll."
                        jump rshop
                    else:
                        if ryo >=1000:
                            "Ok you bought this scroll. But what now?"
                            "Do you want something else?"
                            $ slipscroll = 1
                            $ ryo = ryo - 1000
                            jump rshop
                        else:
                            "You need more money."
                            jump rshop


                "Healing scroll - 1000 ryo":
                    "This is a special healing scroll."
                    "You can use it to heal injuries and marks left on the body."
                    if healscroll ==1:
                        "You already have this scroll."
                        jump rshop
                    else:
                        if ryo >=1000:
                            "You bought the healing scroll. You can heal wounds now."
                            "Do you want something else?"
                            $ healscroll = 1
                            $ ryo = ryo - 1000
                            jump rshop
                        else:
                            "You need more money."
                            jump rshop

                "Expansion - soothing scroll - 1000 ryo":
                    "This is a special expansion scroll."
                    "Medical ninja use it for operations to create more space a in specific body part."
                    "You must use it carefully."
                    if expscroll ==1:
                        "You already have this scroll."
                        jump rshop
                    else:
                        if ryo >=1000:
                            "You bought that scroll. Good luck."
                            "Do you want something else?"
                            $ expscroll = 1
                            $ ryo = ryo - 1000
                            jump rshop
                        else:
                            "You need more money."
                            jump rshop
                "Return":
                    jump rshop




        "Go to map":
            scene black with circleirisin
            show drock0 with circleirisout
            jump drock

########### KAGUYA OFFICE ############
########### KAGUYA OFFICE ############
########### KAGUYA OFFICE ############
########### KAGUYA OFFICE ############
########### KAGUYA OFFICE ############

label rockkagud:
    scene rtown
    $ renpy.transition(dissolve)
    show kaga1
    show kagaok
    ka "Hello %(p)s..."
    if kagumission <= 2:
        ka "Can you come back later please? I need to finish some papers."
        p "Sure..."
        scene black with circleirisin
        show drock0 with circleirisout
        jump drock
    else:
        ka "I already finished all of my work for today. What do you want to do?"
        menu kagudaytalk:
            "Talk":
                if kagumission <= 5:
                    p "What is actually your job?"
                    ka "I am working as a personal manager for miss Tsuchikage."
                    p "So you are her secretary?"
                    ka "No... I am personal manager!"
                    p "You are working with papers?"
                    ka "Yes..."
                    p "So you are secretary."
                    $ renpy.transition(dissolve)
                    hide kagaok
                    show kagaang
                    ka "No!"
                    p "Then what is different?"
                    ka "I am here solving difficult probelms and preparing important papers."
                    p "And What about making coffee?"
                    ka "I am not talking about this topic anymore."
                    p "..."
                    $ renpy.transition(dissolve)
                    hide kagaang
                    show kagaok
                    jump kagudaytalk
                else:
                    p "Do you remember anything from your past?"
                    ka "Sure, I lived here for a few years. Do you want to know about something specific?"
                    p "I was talking about something else."
                    ka "About what?"
                    p "Do you have something like genetic memory?"
                    ka "Uh? If you talk about the original Kaguya, I have no memories from her."
                    p "Let me know if you remember something important."
                    jump kagudaytalk



            "Go out":
                if kagumission == 3:
                    p "I am very hungry. Maybe we can go to the lunch together."
                    ka "Great... Ehm... Not that you are hungry, but I want to eat something too..."
                    p "Then we can go to the park and spend some time together if you have a time."
                    ka "That sounds even better."
                    scene black with circleirisin
                    $ renpy.transition(dissolve)
                    hide kaga1
                    hide kagaok
                    "You go to the restaurant with Kaguya, then you take her to the park."
                    show rpark with circleirisout
                    $ renpy.transition(dissolve)
                    show kaga1
                    show kagaok
                    ka "That food was delicious."
                    p "Yes, I enjoyed it too. Do you go often to the restaurants?"
                    ka "No... It was actually my first time."
                    p "Really? Why? You said that you live here a few years already."
                    $ renpy.transition(dissolve)
                    hide kagaok
                    show kagacl
                    ka "Yes... But every time I am out of my house I feel weird."
                    p "Why?"
                    $ renpy.transition(dissolve)
                    hide kagacl
                    show kagasad
                    ka "Just look around. Everyone is staring at me even right now."
                    p "Because you are beautiful..."
                    ka "Thank you... But... It is not that... They stare at me with hate."
                    p "..."
                    p "It is their problem not yours..."
                    ka "Do you know why they hate me?"
                    p "Ehm... Actually yes... But it is not your fault."
                    $ renpy.transition(dissolve)
                    hide kagasad
                    show kagaok
                    ka "Can you tell me why they hate me?"
                    p "Do you really want to know?"
                    ka "Yes!"
                    menu:
                        "Tell her":
                            p "It is not really your fault."
                            $ kagumission = 4
                            p "They are just scared because you are because you are the clone of someone who was really powerful."
                            $ renpy.transition(dissolve)
                            hide kagaok
                            show kagashock
                            ka "I am a clone???"
                            p "You didn't know it?"
                            $ renpy.transition(dissolve)
                            hide kagashock
                            show kagacl
                            ka "Just kidding, please continue."
                            p "She was known as the goddess. The person who eats a chakra fruit and gain an enormous power."
                            ka "That is not bad, or?"
                            p "Yeah... But the problem was that she tries to destroy the world and enslave the mankind."
                            $ renpy.transition(dissolve)
                            hide kagacl
                            show kagasad
                            ka "..."
                            p "She was defeated by the strong shinobis and sealed."
                            ka "Then why the made me from her DNA."
                            p "There was a hope that you can help to release the Kawaki jutsu."
                            ka "..."
                            $ renpy.transition(dissolve)
                            hide kagasad
                            show kagaok
                            ka "I thank you for being so honest."
                            ka "Most of the people play dumb and didn't tell me the truth."
                            p "So, are you alright now???"
                            ka "Yes..."
                            $ renpy.transition(dissolve)
                            hide kagaok
                            show kagacl
                            ka "Can I tell you a little secret?"
                            p "Sure..."
                            ka "I know that I was created by some kind of monster. I believe, but am not a monster."
                            p "Of course you are not a monster."
                            ka "You are the first man who didn't afraid of me."
                            $ renpy.transition(dissolve)
                            hide kagacl
                            show kagaok
                            ka "Maybe we can be more than friends..."
                            p "Huh? Sure that would be nice..."
                            ka "Great... ehm.... See you later...*smooch*"
                            scene black with circleirisin
                            p "What??? Ok... Maybe next time..."
                            show nrock0 with circleirisout
                            jump nrock

                        "Just go home":
                            p "Maybe later... Now I need to do something..."
                            $ renpy.transition(dissolve)
                            hide kagaok
                            show kagasad
                            ka "..."
                            ka "Sure... Bye..."
                            scene black with circleirisin
                            show nrock0 with circleirisout
                            jump nrock




                else:
                    p "Do you want to hang out with me? Maybe lunch or a walk in the park."
                    ka "That sounds great, let's do both."
                    scene black with circleirisin
                    "You go to the restaurant with Kaguya and then you take her to the park."
                    "It was a nice day and you are now closer to her."
                    scene black with circleirisin
                    show nrock0 with circleirisout
                    jump nrock

            "Have fun":
                if kagumission <= 4:
                    p "Do you want to have some fun?"
                    ka "What you mean by that?"
                    p "I think you know..."
                    "You slowly touch Kaguya hand..."
                    $ renpy.transition(dissolve)
                    show kagashy
                    ka "This feels good... But..."
                    ka "I am not ready for this... I need to know you better or..."
                    p "Or???"
                    ka "Ehm... I have a work come back tomorrow..."
                    scene black with circleirisin
                    show nrock0 with circleirisout
                    jump nrock

                elif kagumission == 5:
                    p "Do you want to have some fun?"
                    ka "What you mean by that?"
                    $ kagumission = 6
                    p "*Smooch*"
                    ka "Mmm.... *smooch* You want to continue where we end right?"
                    p "Yeah..."
                    $ renpy.transition(dissolve)
                    hide kagaok
                    show kagahap
                    show kagashy
                    ka "I just close the door and..."
                    $ renpy.transition(dissolve)
                    hide kaga1
                    hide kagahap
                    hide kagashy
                    show kaga2
                    show kagahap
                    show kagashy
                    ka "Do you like my body?"
                    p "Yes... You are hot... Come here..."
                    $ renpy.transition(dissolve)
                    hide kagahap
                    show kagacl
                    ka "I always want to see... ehmmm..."
                    p "What?"
                    ka "Can you strip too???"
                    p "Sure..."
                    with fade
                    $ renpy.transition(dissolve)
                    hide kagacl
                    show kagashock
                    ka "!!!"
                    p "What?"
                    ka "It is really big!"
                    p "Do you want to touch me there?"
                    $ renpy.transition(dissolve)
                    hide kagashock
                    show kagacl
                    ka "..."
                    p "Good girl... And now move with your hand..."
                    ka "Like this??? *fap fap*"
                    p "Yeah... Good..."
                    ka "*fap fap fap*"
                    p "Faster..."
                    ka "*fap fap fap*"
                    p "Shit *splurt*"
                    $ renpy.transition(dissolve)
                    hide kagacl
                    show kagashock
                    show kagasp
                    ka "What???"
                    p "Fuck that was good!"
                    $ renpy.transition(dissolve)
                    hide kagashock
                    show kagahap
                    ka "Really?"
                    p "Yes, you have a talent for this..."
                    ka "Thanks, I can do it more I am not tired!"
                    p "Huh??? Really? Ok...."
                    scene black with circleirisin
                    "You cum a few more times on Kaguya, Her hands feel really amazing."
                    show nrock0 with circleirisout
                    jump nrock
                else:
                    p "Do you want to have some fun?"
                    ka "Yes I want!"
                    p "*Smooch*"
                    ka "Mmm.... *smooch* You want to continue where we end right?"
                    p "Yeah..."
                    $ renpy.transition(dissolve)
                    hide kagaok
                    show kagahap
                    show kagashy
                    ka "I just close the door and..."
                    $ renpy.transition(dissolve)
                    hide kaga1
                    hide kagahap
                    hide kagashy
                    show kaga2
                    show kagahap
                    show kagashy
                    ka "Are you ready?"
                    p "Yes... You are hot... Come here..."
                    $ renpy.transition(dissolve)
                    hide kagahap
                    show kagaok
                    p "And now..."
                    menu daykagufucktool:
                        "Cum on her":
                            p "Can you help me a little?"
                            ka "Sure what you need?"
                            p "I feel a big pressure right here..."
                            "You put down your clothes."
                            $ renpy.transition(dissolve)
                            hide kagaok
                            show kagahap
                            ka "MMM... Sure... I can help you with that..."
                            p "Hehe..."
                            ka "Do you like it? *fap fap*"
                            p "Yeah... "
                            ka "*fap fap fap*"
                            p "It is better every time you touch my penis."
                            ka "Hehe...*fap fap*"
                            p "Faster..."
                            ka "*fap fap fap*"
                            p "Shit *splurt*"
                            $ renpy.transition(dissolve)
                            hide kagahap
                            show kagaorg
                            show kagasp
                            ka "So much sperm... *slurp*"
                            p "Huh you drink it?"
                            ka "Delicious, give me more!!!*fap fap*"
                            p "Fuck, give me a moment!"
                            ka "Hehe... Only a moment...*fap fap fap*"
                            p "Fuck, you are amazing!"
                            scene black with circleirisin
                            "You cum a few more times on Kaguya, and she drink it all..."
                            show nrock0 with circleirisout
                            jump nrock
                        "Lightning jutsu":
                            if clips == 0:
                                "You need to buy clips first."
                                jump daykagufucktool
                            else:
                                p "I birng some toys today..."
                                ka "What kind of toys?"
                                p "This one... *clamp*"
                                $ renpy.transition(dissolve)
                                hide kagaok
                                show kagacl
                                show kagal1
                                ka "Ouch...*pain* "
                                p "Do not worry you will like it... Just one more here... *clamp*"
                                $ renpy.transition(dissolve)
                                show kagal2
                                ka "Ahhh... *moan*"
                                p "Better right? "
                                ka "What now???"
                                p "Lightning style first level activated! *zap*"
                                $ renpy.transition(dissolve)
                                show kagal3
                                ka "Ahhh..*moan* This feels good..."
                                p "It will be better!!! Lightning dragoon! *zap*"
                                $ renpy.transition(dissolve)
                                hide kagacl
                                show kagaorg
                                show kagal4
                                ka "Yesss....*moan zap*"
                                p "Full release! Lightning circle! *zap*"
                                $ renpy.transition(dissolve)
                                show kagal5
                                show kagam1
                                ka "Ahhh *heavy moaning*"
                                p "Hehe... Nice right???"
                                ka "Ahhhhh!!!!*heavy moaning*"
                                $ renpy.transition(dissolve)
                                hide kagaorg
                                show kagacl
                                hide kagal4
                                hide kagal5
                                ka "That was so good... We should do often..."
                                $ renpy.transition(dissolve)
                                hide kagal3
                                p "Hehe... Sure... Just need to refill some chakra and we can do it again."
                                ka "mmm... Good...*moaning*"
                                p "I will be back to see you again soon."
                                ka "*moaning*"
                                scene black with circleirisin
                                "It cost you some of your chakra, but it was fun..."
                                show nrock0 with circleirisout
                                jump nrock
                        "Slash her":
                            if whip == 0:
                                "You need to buy whip first."
                                jump daykagufucktool
                            else:
                                p "I want to test whip on you today?"
                                ka "A whip? You mean?"
                                $ renpy.transition(dissolve)
                                hide kagaok
                                show kagacl
                                ka "It will be funny... Hehe... I am ready just slash me!"
                                p "No objections? This is good..."
                                "*Slash*" with hpunch
                                $ renpy.transition(dissolve)
                                show kagasc1
                                ka "Ahhh...*moan pain*"
                                p "Are you allright?"
                                ka "Yesss... Give me more!!!"
                                "*Slash*" with hpunch
                                $ renpy.transition(dissolve)
                                show kagasc2
                                ka "Ahhh... *moan*"
                                p "...."
                                "*Slash*" with hpunch
                                ka "Harder!!! *moan scream*"
                                "*Slash*" with hpunch
                                $ renpy.transition(dissolve)
                                show kagasc3
                                ka "Yesss!!! *heavy moaning*"
                                "*Slash*" with hpunch
                                $ renpy.transition(dissolve)
                                show kagam1
                                p "Nice..."
                                $ renpy.transition(dissolve)
                                hide kagacl
                                show kagaorg
                                ka "Ahhh... That is.... Painful... But I like it!"
                                p "Yeah... I try to make you feel good."
                                ka "Ahhhhh... moaning* and it is working...."
                                $ renpy.transition(dissolve)
                                hide kagaorg
                                show kagahap
                                ka "I wonder what you will try next time..."
                                p "I think we can try to make us cum together."
                                ka "mmm...*moaning* That sounds like fun."
                                p "Yeah... It will be..."
                                scene black with circleirisin
                                "So Kaguya can endure a pain without any problem."
                                "But it is maybe time to fuck her next time."
                                show nrock0 with circleirisout
                                jump nrock

                        "Fuck her":
                            if kagumission <= 6:
                                "This is not a good idea..."
                                "Try to build some relationship with her first."
                                jump kagufucknight12

                            elif kagumission == 7:
                                p "Hmmm..."
                                ka "What?"
                                p "Nothing... I was just thinking about that amazing titfuck you gave me last time."
                                ka "Do you want it again? Hmmm..."
                                $ kagumission = 8
                                p "Maybe..."
                                ka "I was hoping for something more today."
                                p "What you mean by that?"
                                $ renpy.transition(dissolve)
                                hide kaga2
                                hide kagaok
                                hide kagashy
                                "Kaguya seductively lay down and put her hands behind the head..."
                                $ renpy.transition(dissolve)
                                show kag3a
                                show kag3ok
                                ka "I think you know what I want."
                                $ renpy.transition(dissolve)
                                show kag3p1
                                p "..."
                                ka "Yes..."
                                $ renpy.transition(dissolve)
                                hide kag3p1
                                show kag3p2
                                hide kag3ok
                                show kag3cl
                                ka "Ahh... This is weird..."
                                p "Should I stop?"
                                ka "No put it deeper..."
                                $ renpy.transition(dissolve)
                                hide kag3a
                                show kag3b
                                hide kag3p2
                                show kag3p3
                                hide kag3cl
                                show kag3shock
                                show kag3blood
                                ka "Ahhh!!!*moan pain*"
                                p "Fuck you are really virgin..."
                                $ renpy.transition(dissolve)
                                hide kag3b
                                show kag3a
                                hide kag3p3
                                show kag3p4
                                hide kag3shock
                                show kag3shock
                                hide kag3blood
                                show kag3blood
                                ka " *moan pain*"
                                ka "Not anymore *moan*"
                                $ renpy.transition(dissolve)
                                hide kag3p4
                                show kag3p3
                                hide kag3blood
                                show kag3blood
                                p "Huh... This is..."
                                $ renpy.transition(dissolve)
                                hide kag3p3
                                show kag3p2
                                hide kag3shock
                                show kag3ok
                                hide kag3blood
                                show kag3blood
                                ka "Put it back it starts to feel good..."
                                $ renpy.transition(dissolve)
                                hide kag3p2
                                show kag3p3
                                hide kag3blood
                                show kag3blood
                                p "On your first time? That is rare..."
                                p "I will do my best!"
                                $ renpy.transition(dissolve)
                                hide kag3a
                                show kag3b
                                hide kag3p3
                                show kag3p4
                                hide kag3ok
                                show kag3ok
                                hide kag3blood
                                show kag3blood
                                ka "Yesss...*moan*"
                                $ renpy.transition(dissolve)
                                hide kag3p4
                                show kag3p3
                                hide kag3blood
                                show kag3blood
                                p "...."
                                $ renpy.transition(dissolve)
                                hide kag3p3
                                show kag3p4
                                hide kag3blood
                                show kag3blood
                                ka "More... *heavy moaning*"
                                $ renpy.transition(dissolve)
                                hide kag3p4
                                show kag3p3
                                hide kag3blood
                                show kag3blood
                                p "Sure...."
                                $ renpy.transition(dissolve)
                                hide kag3p3
                                show kag3p2
                                hide kag3ok
                                show kag3clop
                                hide kag3blood
                                show kag3blood
                                ka "Ahhh!!!! *moan squirt*"
                                $ renpy.transition(dissolve)
                                hide kag3b
                                show kag3a
                                hide kag3p2
                                show kag3p3
                                hide kag3blood
                                show kag3blood
                                hide kag3clop
                                show kag3clop
                                show kag3m1
                                p "Yeah!!!! *splurt*"
                                $ renpy.transition(dissolve)
                                hide kag3p3
                                show kag3p4
                                hide kag3clop
                                show kag3org
                                hide kag3blood
                                show kag3blood
                                show kag3p5
                                p "!!!*splurt*"
                                $ renpy.transition(dissolve)
                                show kag3p6
                                ka "Ahhh...*heavy moan*"
                                ka "That was so good..."
                                p "And the fact we did it in your office..."
                                ka "yeah..."
                                p "We need to clean you..."
                                $ renpy.transition(dissolve)
                                hide kag3a
                                hide kag3m1
                                hide kag3p4
                                hide kag3p5
                                hide kag3org
                                hide kag3blood
                                hide kag3p6
                                p "I just don't understand that you were a virgin."
                                ka "But I am not anymore..."
                                $ renpy.transition(dissolve)
                                show kaga2
                                show kagasp
                                show kagahap
                                p "..."
                                ka "Sex is so amazing..."
                                p "Yes, it is... So many women just underestimated it."
                                $ renpy.transition(dissolve)
                                hide kagahap
                                show kagacl
                                ka "We should do this every day! Maybe 5 time a day or more!!!"
                                p "Huh??? Sure that would be nice..."
                                p "But remember there is a jutsu to broke and other stuff to do..."
                                ka "Is there other women?"
                                p "Ehm... Yes...."
                                $ renpy.transition(dissolve)
                                hide kagacl
                                show kagaok
                                ka "MMM... so maybe we can have sex with them together right?"
                                p "Huh??? Sure... If you want it. But not many girls want to fuck other girls..."
                                ka "I think that should not be a problem... If we combine our powers together we can make them more helpful."
                                p "Continue..."
                                ka "Maybe next time... You need to deserve the rest of my plan."
                                p "So you actually have an evil plan?"
                                ka "I have a plan but it is not evil... Do not be scared..."
                                p "Sure... I belive you..."
                                scene black with circleirisin
                                p "So she actually has some kind of the plan. I need to do something special to make her talk."
                                show nrock0 with circleirisout
                                jump nrock


                            else:
                                p "Hmmm..."
                                ka "Do you want to fuck me today?"
                                p "Yes...."
                                ka "Hehe. So hurry up. I do not have a whole day for it!"
                                $ renpy.transition(dissolve)
                                hide kaga2
                                hide kagaok
                                hide kagashy
                                "Kaguya seductively lay down and put her hands behind the head..."
                                $ renpy.transition(dissolve)
                                show kag3a
                                show kag3ok
                                ka "I am ready for you cock."
                                $ renpy.transition(dissolve)
                                show kag3p1
                                p "..."
                                $ renpy.transition(dissolve)
                                hide kag3p1
                                show kag3p2
                                hide kag3ok
                                show kag3cl
                                ka "Mmmm... I really missed it."
                                p "Me too..."
                                $ renpy.transition(dissolve)
                                hide kag3a
                                show kag3b
                                hide kag3p2
                                show kag3p3
                                hide kag3cl
                                show kag3clop
                                ka "So good *moan*"
                                p "Fuck, you are so hot..."
                                $ renpy.transition(dissolve)
                                hide kag3b
                                show kag3a
                                hide kag3p3
                                show kag3p4
                                hide kag3clop
                                show kag3clop
                                ka "hmmm... *moan*"
                                $ renpy.transition(dissolve)
                                hide kag3p4
                                show kag3p3
                                p "This is..."
                                $ renpy.transition(dissolve)
                                hide kag3p3
                                show kag3p2
                                hide kag3clop
                                show kag3ok
                                ka "Put it deeper again!"
                                $ renpy.transition(dissolve)
                                hide kag3p2
                                show kag3p3
                                p "Sure..."
                                $ renpy.transition(dissolve)
                                hide kag3a
                                show kag3b
                                hide kag3p3
                                show kag3p4
                                hide kag3ok
                                show kag3ok
                                ka "Yesss...*moan*"
                                $ renpy.transition(dissolve)
                                hide kag3p4
                                show kag3p3
                                p "...."
                                $ renpy.transition(dissolve)
                                hide kag3p3
                                show kag3p4
                                ka "More... *heavy moaning*"
                                $ renpy.transition(dissolve)
                                hide kag3p4
                                show kag3p3
                                p "Sure...."
                                $ renpy.transition(dissolve)
                                hide kag3p3
                                show kag3p2
                                hide kag3ok
                                show kag3clop
                                ka "Ahhh!!!! *moan squirt*"
                                $ renpy.transition(dissolve)
                                hide kag3b
                                show kag3a
                                hide kag3p2
                                show kag3p3
                                hide kag3clop
                                show kag3ok
                                show kag3m1
                                menu:
                                    "Cum in":
                                        p "Yeah!!!! *splurt*"
                                        $ renpy.transition(dissolve)
                                        hide kag3p3
                                        show kag3p4
                                        hide kag3ok
                                        show kag3org
                                        show kag3p5
                                        p "!!!*splurt*"
                                        $ renpy.transition(dissolve)
                                        show kag3p6
                                        ka "Ahhh...*heavy moan*"
                                        ka "Fucking with you is amazing..."
                                        p "hehe..."
                                        p "We need to clean your pussy now..."
                                        $ renpy.transition(dissolve)
                                        hide kag3a
                                        hide kag3m1
                                        hide kag3p4
                                        hide kag3p5
                                        hide kag3org
                                        hide kag3p6
                                        p "..."
                                        $ renpy.transition(dissolve)
                                        show kaga2
                                        show kagahap
                                        ka "It was funny..."
                                        p "Funny?"
                                        $ renpy.transition(dissolve)
                                        hide kagahap
                                        show kagacl
                                        ka "Yes... My pussy is filled with your sperm. It is funny..."
                                        p "You have a strange sense of humor."
                                        p "hehe..."
                                        ka "Huh? I heard someone..."
                                        p "What?"
                                        $ renpy.transition(dissolve)
                                        hide kagacl
                                        show kagashock
                                        ka "Hide somewhere or get out, this is dangerous..."
                                        p "What?"
                                        $ renpy.transition(dissolve)
                                        hide kagashock
                                        show kagahap
                                        ka "Just kidding..."
                                        p "Not funny..."
                                        ka "It will be funny next time."
                                        p "..."
                                        scene black with circleirisin
                                        show nrock0 with circleirisout
                                        jump nrock

                                    "Cum out":
                                        p "Just..."
                                        $ renpy.transition(dissolve)
                                        hide kag3p4
                                        show kag3p3
                                        p "A moment!!!"
                                        $ renpy.transition(dissolve)
                                        hide kag3p3
                                        show kag3p2
                                        p "Yeah!!!! *splurt*"
                                        $ renpy.transition(dissolve)
                                        hide kag3p2
                                        show kag3p1
                                        hide kag3ok
                                        show kag3org
                                        show kag3p7
                                        p "!!!*splurt*"
                                        ka "More! *moan*"
                                        $ renpy.transition(dissolve)
                                        show kag3p8
                                        ka "So much sperm on my body... *heavy moan*"
                                        p "hehe..."
                                        p "I have somethingg for you..."
                                        ka "Ahh... *moan* What it is???"
                                        p "This!!! *flick*"
                                        $ renpy.transition(dissolve)
                                        hide kag3p1
                                        show kag3t1
                                        hide kag3org
                                        show kag3shock
                                        ka "Ahhh..."
                                        p "And deeper!"
                                        $ renpy.transition(dissolve)
                                        hide kag3t1
                                        show kag3t2
                                        hide kag3shock
                                        show kag3org
                                        ka "Yesss!!! *heavy moaning*"
                                        p "And final push...."
                                        $ renpy.transition(dissolve)
                                        hide kag3t2
                                        show kag3t3
                                        ka "Ahhh... So good.... *moan*"
                                        p "hehe...."
                                        ka "I wonder if I can stand right now."
                                        $ renpy.transition(dissolve)
                                        hide kag3t3
                                        hide kag3a
                                        hide kag3m1
                                        hide kag3p1
                                        hide kag3p7
                                        hide kag3org
                                        hide kag3p8
                                        p "Slowly..."
                                        $ renpy.transition(dissolve)
                                        show kaga2
                                        show kagasp
                                        show kagahap
                                        ka "And it is still in me..."
                                        p "Yeah it is... Do you like new toys?"
                                        $ renpy.transition(dissolve)
                                        hide kagahap
                                        show kagacl
                                        ka "It is.... interesting..."
                                        p "Fuck, you are hot..."
                                        ka "Thanks..."
                                        $ renpy.transition(dissolve)
                                        hide kagacl
                                        show kagaok
                                        ka "But I need to clean myself now... *glog*"
                                        p "You want to drink it all?"
                                        $ renpy.transition(dissolve)
                                        hide kagaok
                                        show kagahap
                                        ka "Sure why not?"
                                        p "Nevermind."
                                        ka "*glog glog*"
                                        p "See you later... You can return the tools to me later."
                                        scene black with circleirisin
                                        show nrock0 with circleirisout
                                        jump nrock

            "New village":
                if kagumission <=8:
                    p "I found one village in the south."
                    ka "And..."
                    p "There is a strange aura. Like yours."
                    ka "I am not in the mood to talk about it."
                    p "But...."
                    ka "Maybe if you do something nice for me..."
                    p "What do you mean by that?"
                    ka "*sigh*"
                    scene black with circleirisin
                    show drock0 with circleirisout
                    jump drock
                elif kagumission == 9:
                    p "I found one village in the south."
                    $ kagumission = 10
                    ka "Yes... I know..."
                    ka "I have a plan with her... And you can help me with it..."
                    p "Ok... But how?"
                    $ renpy.transition(dissolve)
                    hide kagaok
                    show kagahap
                    ka "I know that you namigan can control the humand mind."
                    ka "With my power you can change it permanently."
                    p "With you power?"
                    ka "With some training you can do it alone too but this can be faster..."
                    p "Where is the problem?"
                    $ renpy.transition(dissolve)
                    hide kagahap
                    show kagacl
                    ka "Problem?"
                    p "I mean why you want to do it?"
                    ka "Because I love sex and the way how you touch me is just.... amazing..."
                    p "..."
                    ka "Imagine it... If you can do it with everyone you want..."
                    p "Hmmm... But what if someone find it out?"
                    $ renpy.transition(dissolve)
                    hide kagacl
                    show kagaok
                    ka "Then you can use the cloning device from this village to create a perfect sex doll."
                    p "Sounds good..."
                    ka "But do not worry, most of the shinobis are not able to ressist you Namigan."
                    p "Ok, I am in..."
                    ka "Great follow me..."
                    scene black with circleirisin
                    hide kagaok
                    hide kaga1
                    show dharemout with circleirisout
                    $ renpy.transition(dissolve)
                    show kaga1
                    show kagaok
                    p "So, here we are."
                    ka "Yes, I belive you will like it here."
                    ka "I will tell the gurads that you can pass now... If you need anything contact me in the hidden roock village."
                    p "OK... Thanks..."
                    scene black with circleirisin
                    show dharem0 with circleirisout
                    jump dharem



            "Nothing":
                p "I just want to check if you are all right. Bye."
                ka "Bye..."
                scene black with circleirisin
                show drock0 with circleirisout
                jump drock

        scene black with circleirisin
        show drock0 with circleirisout
        jump drock

    scene black with circleirisin
    show drock0 with circleirisout
    jump drock

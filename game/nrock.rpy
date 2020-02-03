# DAY %(p)s                      ROCK VILLAGE

label nrock:

    scene nrock0

    $ select = renpy.imagemap("nrock0.jpg", "nrock1.jpg", [
                                               (816, 72, 1094, 171, "gate"),
                                               (196, 229, 480, 345, "park"),
                                               (1432, 432, 1887, 561, "lab"),
                                               (710, 376, 1087, 471, "ntown"),
                                               (904, 670, 1238, 798, "village"),
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

            "Assign":
                "There is nothing to do right now."
                jump nrock

            "Sleep":
                "Тебе нужно немного отдохнуть."
                $ day = day + 1
                scene black with circleirisin
                show drock0 with circleirisout
                jump drock

            "Kunoichi":
                scene black with circleirisin
                show is1a with circleirisout
                jump is111

            "Go to map":
                scene black with circleirisin
                show nrock0 with circleirisout
                jump nrock

    if select == "park":
        scene black with circleirisin
        show rpark with circleirisout
        jump nrpark

    if select == "lab":
        if kushinamission == 0:
            scene black with circleirisin
            show rlab with circleirisout
            jump nrocklab
        else:
            menu:
                "Пойти в больницу":
                    scene black with circleirisin
                    show rlab with circleirisout
                    jump nrocklab

                "Пойти к Кушине":
                    scene black with circleirisin
                    show rbad with circleirisout
                    jump nrockclone



    if select == "ntown":
        scene black with circleirisin
        show rnight with circleirisout
        jump nrocktown

    if select == "village":
        if tenmission == 0:
            "..."
        if kagumission >= 2:
            scene black with circleirisin
            show nstone with circleirisout
            jump nrvillage

        if temamission == 0:
            "This is a village - there are many houses, but you didn't know anyone."
            scene black with circleirisin
            show nrock0 with circleirisout
            jump nrock
        else:
            scene black with circleirisin
            show nstone with circleirisout
            jump nrvillage





label nrpark:
    scene rpark
    menu:
        "Look around":
            if temamission == 0:
                "You walk around the park..."
                $ temamission = 1
                "It is really weird that there is still some light."
                $ renpy.transition(dissolve)
                show temd
                show temcl
                ti "...."
                p "Hello..."
                $ renpy.transition(dissolve)
                hide temcl
                show temsad
                ti "Huh? What do you want?"
                p "Ehm... Nothing, I just saw you and..."
                ti "Don't disturb me!!!"
                p "Sure..."
                $ renpy.transition(dissolve)
                hide temd
                hide temsad
                p "That was weird..."
                p "Maybe if I try to...."
                $ renpy.transition(dissolve)
                show temd
                show temang
                ti "Wait!!!" with hpunch
                p "???"
                ti "I think I know you from somewhere. Who are you ???"
                p "Yes you know me. My name is %(p)s  , You beat my ass in Chunin exams."
                $ renpy.transition(dissolve)
                hide temang
                show temsad
                ti "%(p)s .... hmmm..."
                ti "Yes, I remember you... You was so weak..."
                p "Thanks..."
                ti "But how is this possible... Most of man was trapped in the Kawaki jutsu."
                p "Yes... But..."
                ti "Or maybe you are just too weak and jutsu didn't recognize you as a threat."
                p "..."
                p "I will pretend you didn't say that."
                ti "What?"
                p "Actually, I successfully escape from that jutsu with my birth given powers."
                $ renpy.transition(dissolve)
                hide temsad
                show temshock
                ti "What???"
                p "I escape!"
                ti "How is it even possible? In the past years we tried everything!"
                p "I belive it is my keekei genkai."
                $ renpy.transition(dissolve)
                hide temshock
                show temok
                ti "Hmmm... That is interesting... Can you show it to me?"
                p "I can try... Give me your hand..."
                ti "Why?"
                p "I need physical contact to work with your chakra."
                ti "Ok..."
                p "Namigan!!!" with hpunch
                $ renpy.transition(dissolve)
                hide temok
                show temnok
                ti "...."
                p "Argghhh..."
                $ renpy.transition(dissolve)
                hide temnok
                show temok
                p "Shit...."
                ti "So that was your kekkei genkai?"
                p "Yeah... I can't control it for now."
                p "And you are fighting it... That is no way it will work like this."
                ti "What you mean by that?"
                p "For now, my namigan is weak. And if you fight against it, it will just fail."
                $ renpy.transition(dissolve)
                hide temok
                show temcl
                ti "..."
                p "If you really want to help me, you need to relax and allow me to control you."
                ti "To control me?"
                p "I mean to control my powers..."
                ti "Ok..."
                p "So do you want to help me?"
                ti "Hmmm... I will see..."
                p "What?"
                ti "I need to think about it... Come here another day."
                p "OK.... see you later..."
                $ day = day + 1
                scene black with circleirisin
                show drock0 with circleirisout
                jump drock
            elif temamission >= 12:
                "Temari is now in the hidden tree village."
                scene black with circleirisin
                show nrock0 with circleirisout
                jump nrock
            elif temamission == 1:
                "You walk around the park..."
                $ temamission = 2
                "You find Temari..."
                $ renpy.transition(dissolve)
                show temd
                show temcl
                ti "...."
                p "Hi, Temari..."
                $ renpy.transition(dissolve)
                hide temcl
                show temsad
                ti "Hi, %(p)s  , I was waiting for you."
                p "Good... And why?"
                ti "Last time you tried to use your kekkei genkai on me."
                p "Yes... It was not very successful."
                ti "Exactly... It is mainly because I will not tolerate the weak one."
                p "The weak one?"
                ti "I can feel how weak you are."
                p "Ehm... That is not fair... That jutsu steal most of my powers."
                ti "That can be true, but still. I can't allow someone like you to experiment on me. Unless..."
                p "What?"
                ti "You beat my ass!"
                p "That sounds good, but what you mean by that?"
                $ renpy.transition(dissolve)
                hide temsad
                show temok
                ti "%(p)s ... You need to defeat me in the fight!"
                p "Why?"
                ti "To prove that you are not weak..."
                p "And than what?"
                ti "You can use your Namigan on me."
                p "I am not sure if it is a good idea..."
                p "I need your chakra to cooperate with mine. It can be dangerous for you if you spend your chakra in the previous fight."
                ti "Hmm... I understand... So it should be fine if I use only half of my chakra to fight against you."
                p "Wait! You can do that?"
                $ renpy.transition(dissolve)
                hide temok
                show temop
                ti "Yes. And it will be more fair to you. So are you ready?"
                p "Ehm..."
                menu:
                    "Yes":
                        p "Yes... I think I can beat your ass right now."
                        ti "Okay, if you really think so."
                        jump temabattle1

                    "No":
                        p "This day was really hard for me... We should do it tomorrow."
                        ti "OK... I will be here."

                $ day = day + 1
                scene black with circleirisin
                show drock0 with circleirisout
                jump drock

            elif temamission == 2:
                "You walk around the park..."
                "And find Temari..."
                $ renpy.transition(dissolve)
                show temd
                show temcl
                ti "...."
                p "Hi, Temari..."
                $ renpy.transition(dissolve)
                hide temcl
                show temsad
                ti "Hi, %(p)s  , do you want to fight?"
                menu:
                    "Yes":
                        p "I am ready."
                        ti "Me too..."
                        jump temabattle1

                    "No":
                        p "Maybe later..."
                        ti "Sure..."
                        scene black with circleirisin
                        show nrock0 with circleirisout
                        jump nrock

            else:
                "You walk around the park..."
                "And find Temari..."
                $ renpy.transition(dissolve)
                show temd
                show temcl
                ti "...."
                p "Hi, Temari..."
                $ renpy.transition(dissolve)
                hide temcl
                show temsad
                ti "Hi, %(p)s  , do you want to fight?"
                p "Is it all really necessary? I mean I already beat you."
                ti "It is fun. Fight with me or get out!"
                menu:
                    "Kick her ass":
                        p "Ok I am ready."
                        ti "Me too..."
                        jump temabattle1

                    "Get out":
                        p "I am not in a mood right now. Maybe later..."
                        ti "..."
                        scene black with circleirisin
                        show nrock0 with circleirisout
                        jump nrock

                scene black with circleirisin
                show nrock0 with circleirisout
                jump nrock




        "Relax":
            "You decide to relax a little in the park."
            "After some time you feel a weird feeling."
            "Your chakra is now a little stronger."
            $ chakra = chakra + 1
            "It was so refreshing."
            $ day = day + 1
            scene black with circleirisin
            show drock0 with circleirisout
            jump drock
        "Go to map":
            scene black with circleirisin
            show nrock0 with circleirisout
            jump nrock


# TEMARI BATTLE
# TEMARI BATTLE
# TEMARI BATTLE
# TEMARI BATTLE

label temabattle1:
    $ renpy.transition(dissolve)
    hide temop
    hide temd
    show temf1
    "Temari is ready for the battle."
    $ playerchakra = chakra
    $ player_max_hp = ninjutsu + taijutsu + genjutsu + chakra + eyes
    $ player_hp = player_max_hp
    $ shinobichakra = 0
    $ shinobi_max_hp = 200
    $ shinobi_hp = shinobi_max_hp
    show screen shinobi_stats_screen

    while (shinobi_hp > 0) and (player_hp > 0):
        hide temf1
        if shinobi_hp >=160:
            hide temf1
            hide temf2
            hide temf3
            hide temf4
            hide temf5
            show temf1
        elif shinobi_hp >=120:
            hide temf1
            hide temf2
            hide temf3
            hide temf4
            hide temf5
            show temf2
        elif shinobi_hp >=80:
            hide temf1
            hide temf2
            hide temf3
            hide temf4
            hide temf5
            show temf3
        elif shinobi_hp >=40:
            hide temf1
            hide temf2
            hide temf3
            hide temf4
            hide temf5
            show temf4
        else:
            hide temf1
            hide temf2
            hide temf3
            hide temf4
            hide temf5
            show temf5


        menu temff1:
            "Physical attack":
                p "Take this!"
                $ shinobi_hp = shinobi_hp - taijutsu
                show enemyslash1 with hpunch
                $ renpy.transition(dissolve)
                hide enemyslash1
                show enemyslash2 with vpunch
                $ renpy.transition(dissolve)
                hide enemyslash2
                show enemyslash3 with hpunch
                $ renpy.transition(dissolve)
                hide enemyslash3


            "Namigan":
                if playerchakra >=0:
                    p "Namigan!" with hpunch
                    show nc:
                        yalign .5 subpixel True
                        parallel:
                            xalign .5
                            alpha 1.0 zoom 1.0
                            linear .75 alpha .5 zoom .9
                            linear .75 alpha 1.0 zoom 1.0
                            repeat

                        parallel:
                            rotate 0
                            linear 5 rotate 360
                            repeat
                    $ shinobi_hp = shinobi_hp - (eyes * 2)
                    $ playerchakra = playerchakra - 10
                    "Time was stopped for a short time."
                    "You were able to hit enemy in that time window."
                    hide nc
                    ti "ARGHHHHH..."
                else:
                    p "Namigan!" with hpunch
                    "Nothing happened."
                    "You do not have enough chakra for this."

            "Lightning style":
                if playerchakra >=0:
                    p "Lightning style!" with hpunch
                    $ playerchakra = playerchakra - 10
                    $ shinobi_hp = shinobi_hp - (ninjutsu * 2)
                    $ renpy.transition(dissolve)
                    show en1light
                    ti "ARGHHHHH..."
                    $ renpy.transition(dissolve)
                    hide en1light
                    "You hit enemy Shinobi really hard."

                else:
                    p "Lightning style!" with hpunch
                    ti "Dodge..."
                    "That attack was really weak."
                    "You need more chakra to be successful."


            "Rest":
                if chakra <=25:
                    $ player_hp = min(player_hp+10, player_max_hp)
                    $ playerchakra = playerchakra + 5
                    p "You recover your hp and chakra."
                elif chakra <=50:
                    $ player_hp = min(player_hp+20, player_max_hp)
                    $ playerchakra = playerchakra + 10
                    p "You recover your hp and chakra."
                else:
                    $ player_hp = min(player_hp+30, player_max_hp)
                    $ playerchakra = playerchakra + 15
                    p "You recover your hp and chakra."





        $ randomnum = renpy.random.randint(1,5) # (randomize between 1 and 5)
        if randomnum==1:
                $ shinobi_damage = renpy.random.randint(5, 20)
                $ player_hp -= shinobi_damage
                ti "Dust Wind!!!"
                "Temari strike you with dust wind.." with hpunch
                ti "You are weak!"

        if randomnum==2:
            ti "Great Sickle Weasel!!!"
            "That look dangerous."
            $ shinobi_damage = renpy.random.randint(10, 25)
            "You feel the power of her chakra."
            ti "Take this!" with hpunch
            $ player_hp -= shinobi_damage
            "She hit you hard."



        if randomnum==3:
            ti "Wind Release: Cast Net."
            "Temari slowly heal herself."
            $ shinobi_hp = min(shinobi_hp+10, shinobi_max_hp)
        if randomnum==4:
            "Temari try to attack you."
            "But you successfully dodge that attack."
        if randomnum==5:
            ti "Wind Release: Cast Net."
            "Temari use some kind of wind style attack."
            $ shinobi_damage = renpy.random.randint(20, 30)
            ti "Take this!" with hpunch
            $ player_hp -= shinobi_damage
            "She hit you with ranged attack."




    if shinobi_hp <= 0:
        if player_hp <= 0:
            hide screen shinobi_stats_screen
            "You almost win."
            "But Temari was a really worthy opponent."
            scene black with circleirisin
            "You can win next time."
            $ day = day + 1
            show drock0 with circleirisout
            jump drock
        else:
            hide screen shinobi_stats_screen
            p "I win!!!!!"
            if temamission == 2:
                $ temamission = 3
            ti "Yes... It was a good battle."
            p "So what should I do now?"
            ti "This is your turn now, I will obey."
            menu:
                "Use Namigan":
                    hide screen shinobi_stats_screen
                    p "I think we should test my Namigan now."
                    ti "Ok... Give me a moment to heal."
                    p "..."
                    p "Sure..."
                    $ renpy.transition(dissolve)
                    hide temf1
                    hide temf2
                    hide temf3
                    hide temf4
                    hide temf5
                    show temd
                    show temok
                    jump temanami1

                "Have fun":
                    hide screen shinobi_stats_screen
                    p "Maybe there is another thing that we can do together."
                    ti "Anything, just give me a moment to heal and dress.."
                    p "You can only heal..."
                    ti "...."
                    ti "Ok...."
                    $ renpy.transition(dissolve)
                    hide temf1
                    hide temf2
                    hide temf3
                    hide temf4
                    hide temf5
                    show tema
                    show temok
                    jump temarifuck1

                "Talk":
                    p "Actually I want to ask you something."
                    p "Can you please dress and heal first?"
                    ti "What? Yeah right... "
                    $ renpy.transition(dissolve)
                    hide temf1
                    hide temf2
                    hide temf3
                    hide temf4
                    hide temf5
                    show temd
                    show temok
                    jump temaritalk1




    else:
        hide screen shinobi_stats_screen
        ti "It was a good fight."
        ti "But you are still weak. Try it again when you got stronger."
        $ day = day + 1
        scene black with circleirisin
        show drock0 with circleirisout
        jump drock

# TEMARI NAMIGAN LABEL
# TEMARI NAMIGAN LABEL
# TEMARI NAMIGAN LABEL
# TEMARI NAMIGAN LABEL
# TEMARI NAMIGAN LABEL

label temanami1:
    p "Ok... Give me your hand and try to be calm..."
    ti "Sure..."
    p "Namigan!!!"
    $ renpy.transition(dissolve)
    hide temok
    hide temsad
    show temnok
    ti "..."
    p "Nice..."
    p "And now is time for..."
    menu temanam4:
        "Playtime":
            $ temaslave = temaslave + 1
            p "First, take off your clothes..."
            $ renpy.transition(dissolve)
            hide temd
            show tema
            hide temnok
            show temnok
            p "Hmmm.. Nice... But sometihing need to change..."
            p "Kai!!!"
            $ renpy.transition(dissolve)
            hide tema
            show temb
            hide temnok
            show temnop
            ti "*moan*"
            p "I think this is not maximal size..."
            p "KAI!!!"
            $ renpy.transition(dissolve)
            hide temb
            show temc
            hide temnop
            show temnang
            ti "grrrr...."
            p "Yeah... This is better... And this ... *snick*"
            $ renpy.transition(dissolve)
            show temr1
            ti "Argg...*moan pain*"
            p "Yeah..."
            p "Water release *splash*"
            $ renpy.transition(dissolve)
            show temw2
            hide temnang
            show temnop
            ti "Ahhh...*moan*"
            p "Water dragoon *splash*"
            $ renpy.transition(dissolve)
            show temw3
            ti "Ahhh"
            $ renpy.transition(dissolve)
            show temm1
            p "Hehe... Nice... Water tornado!!!*splash*"
            $ renpy.transition(dissolve)
            show temw4
            show temm2
            ti "Mmm....*moan*"
            p "Hehe... You are really wet now... *fap fap*"
            ti "...."
            p "Just one more shot... *fap fap fap*"
            p "Yeah *fap fap splurt*"
            $ renpy.transition(dissolve)
            show temsp1
            ti "....."
            p "Hehe... This looks good..."
            ti "..."
            p "Ok clean yourself and get that things off..."
            ti "...."
            $ renpy.transition(dissolve)
            hide temsp1
            hide temw4
            hide temw3
            hide temw2
            hide temnop
            hide temm1
            hide temm2
            hide temc
            hide temr1
            p "...."
            show temf
            show temnok
            p "Namigan KAI!!!"
            $ renpy.transition(dissolve)
            hide temnok
            show temok
            ti "Huh???"
            ti "That was weird... My boobs are now..."
            p "Yes... They are big..."
            ti "How???"
            p "It looks like my Namigan cancel your suppression."
            $ renpy.transition(dissolve)
            hide temok
            show temop
            ti "Yeah... It looks like that... It feels good actually."
            p "Why you still spuressing your boob size?"
            ti "I feel better with smaller boobs..."
            p "OK... But it is only an ilusion you know?"
            $ renpy.transition(dissolve)
            hide temop
            show temcl
            ti "Everything is only illusion."
            $ day = day + 1
            scene black with circleirisin
            show drock0 with circleirisout
            jump drock

        "Pain train":
            if eyes <=10:
                "Your Namigan is too weak for that..."
                jump temanam4
            else:
                $ temaslave = temaslave + 1
                p "I want to teach you something, take off your clothes."
                $ renpy.transition(dissolve)
                hide temsad
                hide temd
                show tema
                hide temnok
                show temnok
                p "Nice... I hope you can endure this."
                "*slash*"
                $ renpy.transition(dissolve)
                hide temnok
                show temnop
                show tems1
                ti "*pain moan*"
                p "Still no discipline or resistance..."
                "*whip*"
                $ renpy.transition(dissolve)
                show tems2
                ti "arggg.... *pain*"
                p "Yeah... It is good right..."
                ti "*mumble*"
                p "Do you want more?"
                ti "mumble*"
                $ renpy.transition(dissolve)
                show tems3
                hide temnop
                show temnang
                ti "Ahhh...*moan*"
                p "I think this was enough."
                ti "*moan pain*"
                p "I don't want to hurt you anymore..."
                ti "...."
                p "Heal yourself now and dress..."
                ti "...."
                $ renpy.transition(dissolve)
                hide temsp1
                hide tems1
                hide tems2
                hide tems3
                hide temnang
                hide temm1
                hide temm2
                hide tema
                p "...."
                show temd
                show temnok
                p "Namigan KAI!!!"
                $ renpy.transition(dissolve)
                hide temnok
                show temok
                ti "Huh???"
                ti "Ahhh... My body is in fire..."
                p "What???"
                ti "I am not sure... It is like after loose a battle..."
                p "Maybe you have a rough day."
                $ renpy.transition(dissolve)
                hide temok
                show temop
                ti "Yeah... Maybe... Is your powers now stronger?"
                p "I am not sure, but I can control them better for sure."
                ti "That is good right?"
                p "Of course..."
                $ renpy.transition(dissolve)
                hide temop
                show temcl
                ti "Great... Now I need some time to rest."
                ti "See you later."
                $ day = day + 1
                scene black with circleirisin
                show drock0 with circleirisout
                jump drock

        "Blowjob":
            if eyes <=25:
                "Your Namigan is too weak for that..."
                jump temanam4
            else:
                p "Yes... This is good... Take off your clothes."
                $ temaslave = temaslave + 2
                $ renpy.transition(dissolve)
                hide temok
                hide temsad
                hide temd
                hide temnok
                hide tema
                p "Now get on your knees..."
                p "Yeah... Nice..."
                $ renpy.transition(dissolve)
                show tem3a
                show tem3pn1
                ti "Mhmmmh..."
                p "Hehe... Nice..."
                $ renpy.transition(dissolve)
                hide tem3pn1
                show tem3pn2
                if temamission == 5:
                    $ temamission = 6
                ti "* cough*"
                p "I will put it deeper..."
                $ renpy.transition(dissolve)
                hide tem3pn2
                show tem3pn3
                ti "*gag cough*"
                $ renpy.transition(dissolve)
                hide tem3pn3
                show tem3pn4
                p "Great..."
                $ renpy.transition(dissolve)
                hide tem3pn4
                show tem3pn3
                ti "*gag*"
                $ renpy.transition(dissolve)
                hide tem3pn3
                show tem3pn2
                p "So good..."
                $ renpy.transition(dissolve)
                hide tem3pn2
                show tem3pn3
                ti "*gag cough*"
                $ renpy.transition(dissolve)
                hide tem3pn3
                show tem3pn4
                p "Wow..."
                $ renpy.transition(dissolve)
                hide tem3pn4
                show tem3pn3
                p "And now...."
                $ renpy.transition(dissolve)
                hide tem3pn3
                show tem3pn4
                menu:
                    "Cum":
                        p "Take it !!! *splurt*"
                        $ renpy.transition(dissolve)
                        show tem3sp0
                        ti "Ghhhh... *gag cough*"
                        p "Fuckkk *splurt*"
                        $ renpy.transition(dissolve)
                        show tem3sp1
                        p "Yes... That was what I need..."
                        ti "Grggg... *cough* "
                        p "Great right?"
                        $ renpy.transition(dissolve)
                        hide tem3pn4
                        hide tem3sp1
                        hide tem3sp0
                        hide tem3a
                        ti "*cough*"
                        p "Heh.. It is nice to fuck your mouth."
                        p "Now you can dress..."
                        $ renpy.transition(dissolve)
                        show temd
                        show temnok
                        ti "*cough*"
                        p "Namigan KAI!!!"
                        $ renpy.transition(dissolve)
                        hide temnok
                        show temok
                        p "And it is done."
                        ti "Huh? That was weird and the taste in my mouth."
                        p "What kind of taste?"
                        ti "I am not sure..."
                        p "OK... You should ignore it..."
                        ti "Hmpf... Sure.."
                        p "See you later..."
                        $ day = day + 1
                        scene black with circleirisin
                        show drock0 with circleirisout
                        jump drock

                    "Lightning style":
                        p "I want to play a little..."
                        p "Boobs suppression KAI!"
                        $ renpy.transition(dissolve)
                        hide tem3pn4
                        hide tem3a
                        show tem3b
                        show tem3pn3
                        ti "Mgmmm...*moan*"
                        p "It is better now... And..."
                        $ renpy.transition(dissolve)
                        hide tem3pn3
                        show tem3pn2
                        show tem3l1
                        ti "*moan pain*"
                        p "Lightning style!!! *zap*"
                        $ renpy.transition(dissolve)
                        hide tem3pn2
                        show tem3pn3
                        show tem3l2
                        ti "Ahhh... *mumble gag*"
                        $ renpy.transition(dissolve)
                        hide tem3pn3
                        show tem3pn4
                        show tem3l3
                        ti "*gag cough moan*"
                        $ renpy.transition(dissolve)
                        show tem3m1
                        p "Yeah!!! !!! *splurt*"
                        $ renpy.transition(dissolve)
                        show tem3sp0
                        ti "Ghhhh... *gag cough*"
                        p "Fuckkk *splurt*"
                        $ renpy.transition(dissolve)
                        show tem3sp1
                        p "Yes... That was what I need..."
                        ti "Grggg... *cough* "
                        p "huh???"
                        $ renpy.transition(dissolve)
                        hide tem3pn4
                        hide tem3sp1
                        hide tem3sp0
                        hide tem3l3
                        hide tem3l2
                        hide tem3l1
                        hide tem3m1
                        hide tem3b
                        ti "*cough*"
                        p "Heh.. That was good... Now you can dress..."
                        $ renpy.transition(dissolve)
                        show temd
                        show temnok
                        p "NAmigan KAI!!!"
                        $ renpy.transition(dissolve)
                        hide temnok
                        show temok
                        ti "Ahhh. What was that I feel so much energy."
                        p "Yeah mee too. My namigan is really strong now."
                        ti "Great you should be able to use full power soon right?."
                        p "Yeah... I need a month or two for training, but then It will be complete."
                        $ renpy.transition(dissolve)
                        hide temok
                        show temcl
                        ti "..."
                        p "We didn't want to risk, right?"
                        ti "Sure..."
                        p "Great, see you later."
                        $ day = day + 1
                        scene black with circleirisin
                        show drock0 with circleirisout
                        jump drock
                    "Fuck her nipple":
                        p "Time for something special."
                        p "Boobs suppression KAI!"
                        $ renpy.transition(dissolve)
                        hide tem3pn4
                        hide tem3a
                        show tem3b
                        show tem3pn3
                        ti "Mgmmm...*moan*"
                        $ renpy.transition(dissolve)
                        hide tem3pn3
                        show tem3pn2
                        p "And now! More!"
                        $ renpy.transition(dissolve)
                        hide tem3pn2
                        show tem3pn3
                        p "Boobs suppression KAI!" with hpunch
                        $ renpy.transition(dissolve)
                        hide tem3pn3
                        hide tem3b
                        show tem3c
                        show tem3pn3
                        p "Finally!"
                        $ renpy.transition(dissolve)
                        hide tem3pn3
                        show tem3pn2
                        ti "*moan gag*"
                        p "Kage bunshin no jutsu!"
                        $ renpy.transition(dissolve)
                        hide tem3pn2
                        show tem3pn3
                        show tem3nf1
                        p "And push!!!"
                        ti "Ahhh... *mumble gag*"
                        $ renpy.transition(dissolve)
                        hide tem3pn3
                        show tem3pn4
                        hide tem3nf1
                        show tem3nf2
                        ti "*gag cough moan*"
                        p "Hehe..."
                        $ renpy.transition(dissolve)
                        hide tem3pn4
                        show tem3pn3
                        hide tem3nf2
                        show tem3nf3
                        p "Yeah!!! !!! *splurt*"
                        $ renpy.transition(dissolve)
                        hide tem3pn3
                        show tem3pn4
                        show tem3sp0
                        hide tem3nf3
                        show tem3nf2
                        ti "Ghhhh... *gag cough*"
                        $ renpy.transition(dissolve)
                        hide tem3nf2
                        show tem3nf3
                        p "Fuckkk *splurt*"
                        $ renpy.transition(dissolve)
                        show tem3sp1
                        hide tem3nf3
                        show tem3nf2
                        p "Yes... And more!!!"
                        hide tem3nf2
                        show tem3nf3
                        ti "gggg...*moan gag*"
                        p "Fuck... *splurt*"
                        $ renpy.transition(dissolve)
                        show tem3p5
                        ti "Grggg... *cough* "
                        $ renpy.transition(dissolve)
                        show tem3p6
                        p "That was so good..."
                        ti "*cough gsg*"
                        p "Right, sorry..."
                        $ renpy.transition(dissolve)
                        hide tem3pn4
                        hide tem3sp1
                        hide tem3sp0
                        hide tem3nf3
                        hide tem3l3
                        hide tem3l2
                        hide tem3l1
                        hide tem3p4
                        hide tem3p5
                        hide tem3p6
                        hide tem3c
                        ti "*cough*"
                        p "Heh.. That was good... Now you can dress... And drink it all alright?"
                        $ renpy.transition(dissolve)
                        show temd
                        show temnok
                        p "Namigan KAI!!!"
                        $ renpy.transition(dissolve)
                        hide temnok
                        show temok
                        ti "Ahhh. What is wrong with my nipples?."
                        p "Why you talk about nipples?"
                        $ renpy.transition(dissolve)
                        hide temok
                        show temcl
                        ti "It is just.... Arg..."
                        p "Ok... Go home and take some rest."
                        ti "..."
                        ti "Sure... It is just..."
                        p "You help me a lot today... That is good thing right?"
                        ti "Yeah..."
                        p "Great, bye."
                        $ day = day + 1
                        scene black with circleirisin
                        show drock0 with circleirisout
                        jump drock





        "Fuck her":
            if eyes <=50:
                "Your Namigan is too weak for that..."
                jump temanam4
            else:
                $ temaslave = temaslave + 3
                p "This is the right time to fuck you. Take off your clothes."
                $ renpy.transition(dissolve)
                hide temok
                hide temsad
                hide temd
                hide temnok
                hide tema
                p "Good... Now lay down."
                $ renpy.transition(dissolve)
                show tem4a
                show tem4ok
                ti "..."
                p "OK..."
                $ renpy.transition(dissolve)
                show tem4p1
                p "This will be good..."
                $ renpy.transition(dissolve)
                hide tem4p1
                show tem4p2
                ti "...."
                $ renpy.transition(dissolve)
                hide tem4p2
                show tem4p3
                hide tem4ok
                show tem4dow
                p "You like it right?"
                $ renpy.transition(dissolve)
                hide tem4p3
                show tem4p4
                ti "*Mumble*"
                $ renpy.transition(dissolve)
                hide tem4p4
                show tem4p3
                p "Yeah... Now it is for sure..."
                $ renpy.transition(dissolve)
                hide tem4p3
                show tem4p2
                p "But..."
                $ renpy.transition(dissolve)
                hide tem4p2
                show tem4p3
                p "I feel I can do much more..."
                $ renpy.transition(dissolve)
                hide tem4p3
                show tem4p4
                p "Like..."
                menu:
                    "Anal balls":
                        $ renpy.transition(dissolve)
                        hide tem4p4
                        show tem4p3
                        p "I want to try something."
                        $ renpy.transition(dissolve)
                        hide tem4p3
                        show tem4p2
                        ti "...."
                        $ renpy.transition(dissolve)
                        hide tem4p2
                        p "Here it is..."
                        $ renpy.transition(dissolve)
                        show tem4a1
                        ti "ggg...*moan*"
                        $ renpy.transition(dissolve)
                        hide tem4a1
                        show tem4a2
                        hide tem4dow
                        show tem4shock
                        p "Nice right???"
                        $ renpy.transition(dissolve)
                        hide tem4a2
                        show tem4a3
                        ti "*moan*"
                        $ renpy.transition(dissolve)
                        hide tem4a3
                        show tem4a4
                        p "Yeah... Now it is good..."
                        $ renpy.transition(dissolve)
                        show tem4p1
                        p "Hehe..."
                        $ renpy.transition(dissolve)
                        hide tem4p1
                        show tem4p2
                        hide tem4shock
                        show tem4sad
                        ti "Mmmm...*moan*"
                        $ renpy.transition(dissolve)
                        hide tem4p2
                        show tem4p3
                        p "Yeah..."
                        $ renpy.transition(dissolve)
                        hide tem4p3
                        show tem4p4
                        ti "...."
                        $ renpy.transition(dissolve)
                        hide tem4p4
                        show tem4p3
                        p "Just...."
                        $ renpy.transition(dissolve)
                        hide tem4p3
                        show tem4p4
                        p "*splurt*"
                        $ renpy.transition(dissolve)
                        show tem4p5
                        p "Yeah!!! *drip*"
                        $ renpy.transition(dissolve)
                        show tem4p6
                        ti "....."
                        p "You are really hot... Do you know it?"
                        ti "...."
                        p "Yeah... I forgot... You can clean now and dress..."
                        $ renpy.transition(dissolve)
                        hide tem4p4
                        hide tem4p5
                        hide tem4p6
                        hide tem4sad
                        hide tem4a
                        hide tem4a4
                        ti "Sure..."
                        $ renpy.transition(dissolve)
                        show temd
                        show temnok
                        p "Namigan KAI!!!"
                        $ renpy.transition(dissolve)
                        hide temnok
                        show temok
                        ti "Huh? What was that?"
                        p "Sorry I don't have a time right now... I am so exhausted."
                        $ renpy.transition(dissolve)
                        hide temok
                        show temop
                        ti "But...."
                        p "Not now..."
                        $ day = day + 1
                        scene black with circleirisin
                        show drock0 with circleirisout
                        jump drock

                    "Slash fuck":
                        $ renpy.transition(dissolve)
                        hide tem4p4
                        show tem4p3
                        p "Do you like my whip?"
                        $ renpy.transition(dissolve)
                        hide tem4p3
                        show tem4p2
                        ti "...."
                        $ renpy.transition(dissolve)
                        hide tem4p2
                        show tem4p3
                        p "Yes I think it was... *slash*"
                        $ renpy.transition(dissolve)
                        hide tem4p3
                        show tem4p4
                        show tem4s1
                        hide tem4dow
                        show tem4ang
                        ti "Mhghmmm... *pain moan*"
                        $ renpy.transition(dissolve)
                        hide tem4p4
                        show tem4p3
                        p "And more...*slash*"
                        $ renpy.transition(dissolve)
                        hide tem4p3
                        show tem4p2
                        show tem4s2
                        ti "Ahhh....*moan*"
                        $ renpy.transition(dissolve)
                        hide tem4p2
                        show tem4p3
                        p "Good right? *slash*"
                        $ renpy.transition(dissolve)
                        hide tem4p3
                        show tem4p4
                        show tem4s3
                        hide tem4ang
                        show tem4sad
                        ti "Fuck!!!*moan*"
                        $ renpy.transition(dissolve)
                        hide tem4p4
                        show tem4p3
                        p "Huh? That was weird..."
                        $ renpy.transition(dissolve)
                        hide tem4p3
                        show tem4p2
                        ti "...."
                        $ renpy.transition(dissolve)
                        hide tem4p2
                        show tem4p3
                        p "I will..."
                        $ renpy.transition(dissolve)
                        hide tem4p3
                        show tem4p4
                        hide tem4sad
                        show tem4ok
                        p "*Splurt*"
                        $ renpy.transition(dissolve)
                        show tem4p5
                        ti ".... *drip*"
                        $ renpy.transition(dissolve)
                        show tem4p6
                        p "That was good... Right???"
                        ti "...."
                        p "Ehm... Sure... Now you can clean and dress yourself..."
                        $ renpy.transition(dissolve)
                        hide tem4p4
                        hide tem4p5
                        hide tem4p6
                        hide tem4ok
                        hide tem4sad
                        hide tem4a
                        hide tem4a4
                        hide tem4s1
                        hide tem4s2
                        hide tem4s3
                        p "And heal yourself!"
                        $ renpy.transition(dissolve)
                        show temd
                        show temnok
                        p "Namigan KAI!!!"
                        $ renpy.transition(dissolve)
                        hide temnok
                        show temok
                        ti "...."
                        p "Are you all right?"
                        $ renpy.transition(dissolve)
                        hide temok
                        show temop
                        ti "Yeah... I feel really good now..."
                        p "Yeah me too... Just need some rest..."
                        ti "Ok... We can train again tomorrow."
                        p "Yeah... Maybe..."
                        $ day = day + 1
                        scene black with circleirisin
                        show drock0 with circleirisout
                        jump drock

                    "Kage bunshin":
                        $ renpy.transition(dissolve)
                        hide tem4p4
                        show tem4p3
                        p "Time to cum on your body... But first..."
                        $ renpy.transition(dissolve)
                        hide tem4p3
                        show tem4p2
                        p "Boobs suppression KAI!"
                        $ renpy.transition(dissolve)
                        hide tem4p2
                        hide tem4a
                        hide tem4dow
                        show tem4b
                        show tem4dow
                        show tem4p3
                        p "Great..."
                        $ renpy.transition(dissolve)
                        hide tem4p3
                        show tem4p4
                        p "Kage bunshin no jutsu!!!"
                        show tem4p9
                        show tem4p10
                        show tem4tf1
                        hide tem4dow
                        show tem4shock
                        ti "!!!! *moan*"
                        $ renpy.transition(dissolve)
                        hide tem4p4
                        show tem4p3
                        hide tem4tf1
                        show tem4tf2
                        p "This is good... *fap fap*"
                        $ renpy.transition(dissolve)
                        hide tem4p3
                        show tem4p2
                        hide tem4tf2
                        show tem4tf3
                        ti "Ahhh... *moan*"
                        $ renpy.transition(dissolve)
                        hide tem4p2
                        show tem4p3
                        hide tem4tf3
                        show tem4tf4
                        hide tem4shock
                        show tem4sad
                        p "Just...*fap fap*"
                        $ renpy.transition(dissolve)
                        hide tem4p3
                        show tem4p4
                        hide tem4tf4
                        show tem4tf3
                        p"Yeah!!! *fap fap*"
                        $ renpy.transition(dissolve)
                        hide tem4p4
                        show tem4p3
                        hide tem4tf3
                        show tem4tf2
                        p "Fuck!!! *fap fap*"
                        $ renpy.transition(dissolve)
                        hide tem4p3
                        show tem4p2
                        hide tem4tf2
                        show tem4tf3
                        ti "...."
                        $ renpy.transition(dissolve)
                        hide tem4p2
                        show tem4p3
                        hide tem4tf3
                        show tem4tf4
                        p "Shit this is so good!!! *splurt*"
                        $ renpy.transition(dissolve)
                        hide tem4p3
                        show tem4p4
                        show tem4tf5
                        ti "mmmm... *moan*"
                        $ renpy.transition(dissolve)
                        hide tem4p4
                        show tem4p3
                        show tem4tf6
                        p "Just a moment ... *splurt*"
                        $ renpy.transition(dissolve)
                        hide tem4p3
                        show tem4p2
                        show tem4p11
                        p "Wow!!!"
                        $ renpy.transition(dissolve)
                        hide tem4p2
                        show tem4p1
                        show tem4p12
                        ti "Ah....*heavy moaning*"
                        $ renpy.transition(dissolve)
                        show tem4p7
                        p "Yeah!!! *splurt*"
                        $ renpy.transition(dissolve)
                        show tem4p8
                        p "Wow... This is..."
                        p "Ahm...." with hpunch
                        p "Weird..."
                        $ day = day + 1
                        scene black with circleirisin
                        "It looks like you used too much of your chakra..."
                        "You woke up the next morning in the hotel, not remember what happened."
                        "I hope Temari didn't remember what happened too..."
                        show drock0 with circleirisout
                        jump drock




# TEMARI FUCK LABEL
# TEMARI FUCK LABEL
# TEMARI FUCK LABEL
# TEMARI FUCK LABEL
# TEMARI FUCK LABEL


label temarifuck1:
    ti "What do you want to do now?"
    p "Hmmm... Maybe...."
    menu:
        "Touch her":
            p "If you come a little closer..."
            ti "And?"
            p "Something is not right with you."
            ti "What?"
            p "KAI!!!"
            $ renpy.transition(dissolve)
            hide tema
            show temc
            hide temok
            show temcl

            if temamission == 3:
                ti "Huh??? You know it?"
                p "I noticed it during the fight..."
                p "And now..."
                $ renpy.transition(dissolve)
                hide temcl
                show temop
                show temh1
                $ temamission = 4
                ti "Hey!!!"
                p "Come on! You told me I can do what I want."
                ti "But this is..."
                $ renpy.transition(dissolve)
                hide temop
                show temcl
                show temh2
                p "Is this better?"
                ti "Ahhh...*moan*"
            else:
                ti "You just love big boobs right?"
                p "Yes... And touching them is even better."
                $ renpy.transition(dissolve)
                hide temcl
                show temop
                show temh1
                ti "MMM....*moan*"
                p "Feels good right?"
                p "And this..."
                $ renpy.transition(dissolve)
                hide temop
                show temcl
                show temh2
                ti "Ahhh...*moan*"
            p "Your body is really hot you know?"
            ti "Ahhh... yeah..*moan*"
            ti "It just...."
            $ renpy.transition(dissolve)
            show temd1
            p "It is really hot here right?"
            ti "Yesss... So hot...*smooch*"
            p "Nice... *smooch*"
            scene black with circleirisin
            $ day = day + 1
            "You spend some time with Temari with kissing her and massaging her breast."
            show drock0 with circleirisout
            jump drock

        "Blowjob":
            if temamission <= 4:
                p "If you come a little closer..."
                ti "And?"
                p "Kneel before me..."
                $ renpy.transition(dissolve)
                hide temok
                show temshock
                ti "Huh???"
                ti "It can be really fun... But ehmmm"
                ti "I am not in a mood for it now... Bye..."
                $ renpy.transition(dissolve)
                hide temshock
                hide tema
                p "That was fast... Maybe I need to do something first not just want a blowjob."
                $ day = day + 1
                scene black with circleirisin
                show drock0 with circleirisout
                jump drock

            else:
                p "If you come a little closer..."
                ti "And?"
                p "Kneel before me..."
                $ renpy.transition(dissolve)
                hide temok
                hide temsad
                hide tema
                p "Yes... This is good..."
                p "And now..."
                $ renpy.transition(dissolve)
                show tem3a
                show tem3p1
                ti "Mhmmmh..."
                p "How is it???"
                $ renpy.transition(dissolve)
                hide tem3p1
                show tem3p2
                ti "ghgtmmm..*moan cough*"
                p "Yes... I will put it deeper..."
                $ renpy.transition(dissolve)
                hide tem3p2
                show tem3p3
                ti "grgfg...*gag cough*"
                $ renpy.transition(dissolve)
                hide tem3p3
                show tem3p4
                p "So good..."
                $ renpy.transition(dissolve)
                hide tem3p4
                show tem3p3
                ti "Gtggfg...*gag*"
                $ renpy.transition(dissolve)
                hide tem3p3
                show tem3p2
                p "Move with your tounge a little..."
                $ renpy.transition(dissolve)
                hide tem3p2
                show tem3p3
                ti "Ghmm. gogmh??? *mumble*"
                $ renpy.transition(dissolve)
                hide tem3p3
                show tem3p4
                p "Yeah... Just like this..."
                $ renpy.transition(dissolve)
                hide tem3p4
                show tem3p3
                p "And now...."
                $ renpy.transition(dissolve)
                hide tem3p3
                show tem3p4
                p "Take it !!! *splurt*"
                $ renpy.transition(dissolve)
                show tem3sp0
                ti "Ghhhh... *gag cough*"
                p "Fuckkk *splurt*"
                $ renpy.transition(dissolve)
                show tem3sp1
                p "Yes... That was what I need..."
                ti "Grggg... *cough* "
                p "huh???"
                $ renpy.transition(dissolve)
                hide tem3p4
                hide tem3sp1
                hide tem3sp0
                hide tem3a
                "Temari pulled your cock out of her mouth."
                ti "*cough*"
                p "Heh.. That was good right?"
                $ renpy.transition(dissolve)
                show tema
                show temok
                show temsp1
                ti "*cough* Yes... It remember me the old times...."
                p "I really enjoyed it.. Your mouth is...."
                ti "I hope you will repay it to me someday... But now I need to go home..."
                p "Sure see you later..."
                $ day = day + 1
                scene black with circleirisin
                show drock0 with circleirisout
                jump drock


        "Fuck her":
            if temamission <= 9:
                p "I want to play with you more..."
                ti "Ok, but how?"
                p "Just try to use more imagination, maybe..."
                $ renpy.transition(dissolve)
                hide temok
                show temshock
                ti "Huh???"
                ti "It can be really fun... But ehmmm"
                ti "I am not in a mood for it now... Bye..."
                $ renpy.transition(dissolve)
                hide temshock
                hide tema
                p "That was fast...."
                $ day = day + 1
                scene black with circleirisin
                show drock0 with circleirisout
                jump drock
            else:
                p "Is time to fuck your pussy..."
                $ renpy.transition(dissolve)
                hide tema
                hide temsad
                hide temok
                hide temop
                ti "Sure..."
                $ renpy.transition(dissolve)
                show tem1a
                show tem1ok
                ti "I want you right now!"
                $ renpy.transition(dissolve)
                show tem1p1
                ti "Yes... Stick it in!"
                $ renpy.transition(dissolve)
                hide tem1p1
                show tem1p2
                ti "Ahhh.. So good... deeper!"
                $ renpy.transition(dissolve)
                hide tem1ok
                show tem1ou
                hide tem1p2
                show tem1p3
                ti "Yeah... Deeper!*moan*"
                $ renpy.transition(dissolve)
                hide tem1p3
                show tem1p4
                p "Nice..."
                $ renpy.transition(dissolve)
                hide tem1ou
                show tem1cl
                ti "*moan*..."
                $ renpy.transition(dissolve)
                hide tem1p4
                show tem1p3
                p "Ok..."
                $ renpy.transition(dissolve)
                hide tem1p3
                show tem1p2
                ti "Ahhh... *moan*"
                $ renpy.transition(dissolve)
                hide tem1p2
                show tem1p3
                show tem1r2
                p "You are so hot! Just..."
                $ renpy.transition(dissolve)
                hide tem1p3
                show tem1p4
                hide tem1cl
                show tem1clo
                p "Yeah... *splurt*"
                $ renpy.transition(dissolve)
                show tem1sp1
                ti "Ahhhh... *heavy moaning*"
                ti "That feels so good..."
                p "Yeah..."
                $ renpy.transition(dissolve)
                hide tem1sp1
                hide tem1p4
                hide tem1clo
                hide tem1a
                hide tem1r2
                "After a while..."
                $ renpy.transition(dissolve)
                show tema
                show temok
                show temsp1
                ti "So this is the fate of looser?"
                p "Come on."
                ti "Just kidding... It was fun..."
                p "Ehm... Sure.."
                ti "I hope you enjoy your reward..."
                $ renpy.transition(dissolve)
                hide temok
                show temop
                ti "I will go home now..."
                p "OK..."
                $ day = day + 1
                scene black with circleirisin
                show drock0 with circleirisout
                jump drock


    scene black with circleirisin
    show drock0 with circleirisout
    jump drock

# TEMARI TALK LABEL
# TEMARI TALK LABEL
# TEMARI TALK LABEL
# TEMARI TALK LABEL
# TEMARI TALK LABEL

label temaritalk1:
    ti "So what do you want to know?"
    menu:
        "Past":
            ti "The past is past... I try to not think about it too much."
            p "Why?"
            ti "Give me a normal question, please..."
            jump temaritalk1

        "Troubles":
            if temamission == 6:
                $ temamission = 7
                p "Is there anything that bothers you?"
                ti "Actually, I think I need your help."
                p "Sure... What can I do for you?"
                ti "It is... "
                $ renpy.transition(dissolve)
                hide temok
                show temcl
                ti "I am really not sure if this is the right place to talk about it..."
                p "Why not?"
                p "There is nobody here."
                ti "Yes but...."
                ti "It will be better if we talk about it in my house..."
                p "Ok... Just tell me when and..."
                $ renpy.transition(dissolve)
                hide temcl
                show temok
                ti "Right now!"
                p "Ok..."
                ti "Or..."
                ti "Tomorow!"
                p "Are you sure you feel good?"
                ti "Just... I will wait for you..."
                $ renpy.transition(dissolve)
                hide temok
                hide temcl
                hide temsad
                hide temd
                p "???"
                $ day = day + 1
                scene black with circleirisin
                "She is really weird."
                "I should visit her someday."
                show drock0 with circleirisout
                jump drock

            elif temamission == 11:
               p "..."
               if kagumission >=9:
                   p "I think you need to leave this village..."
                   ti "Really? why?"
                   p "There is probably nothing you can do right now... And it is only holding you back."
                   ti "You just don't understand it..."
                   p "..."
                   menu:
                        "Final brainwash":
                            p "Maybe, but that was not a question."
                            ti "What???"
                            p "Namigna! Final brainwash!!!" with hpunch
                            ti "Arggg!!!!"
                            $ renpy.transition(dissolve)
                            hide temok
                            show temnok
                            p "Good..."
                            $ temamission = 12
                            p "Now leave, And go to the hidden tree village..."
                            ti "...."
                            scene black with circleirisin
                            "Temari is now part of your harem."
                            show drock0 with circleirisout
                            jump drock
                        "Leave her":
                            p "Maybe... But I think it can be a good step to change the place you live..."
                            p "But I didn't want to force you."
                            ti "Good...."
                            jump temaritalk1
            else:
                p "Is there anything that bothers you?"
                ti "Nothing for now... I feel fine."
                p "Good..."
                ti "Anything else?"
                jump temaritalk1

        "Life in Konoha":
            if temamission == 4:
                $ temamission = 5
                p "I want to know how it was to live in Konoha."
                ti "It was pretty good, I was accepted as a strong kunoichi and a sister of the Kazekage."
                p "Did you miss that time?"
                ti "Sometimes... It was the time of peace, everyone was happy we can drink whole day and fuck whole night."
                p "What?"
                $ renpy.transition(dissolve)
                hide temok
                show temop
                ti "Come on, you know what I mean."
                ti "Just imagine it. A world with secret jutsu and a lot of ways how you can use them."
                p "Yeah, I know. Good old times."
                p "But let's be fair. It is not so different right now."
                ti "It is a completely different world now."
                p "Why?"
                $ renpy.transition(dissolve)
                hide temop
                show temcl
                ti "Many strong shapes disappeared and the one who left isn't capable of anything funny."
                p "Funny?"
                $ renpy.transition(dissolve)
                hide temcl
                show temclop
                ti "You know... There are a lot of secret jutsu that is forever lost."
                p "Why forever? There is still hope."
                ti "???"
                p "Come on. I am here now and my skills are stronger with every new day."
                $ renpy.transition(dissolve)
                hide temop
                show temcl
                ti "So... What kind of specail jutsu you can use?"
                p "I can use lightning style, wind style my secret heat style and many others like expansions or healing."
                ti "That sounds more promising."
                $ renpy.transition(dissolve)
                hide temcl
                show temclop
                ti "Maybe we can try it sometimes."
                p "You mean??? On you?"
                ti "Yes, Why not?...."
                p "I will look forward to it."
                $ day = day + 1
                scene black with circleirisin
                show drock0 with circleirisout
                jump drock
            else:
                p "I want to know how it was to live in Konoha."
                ti "It was pretty good, I was accepted as a strong kunoichi and a sister of the Kazekage."
                p "Did you miss that time?"
                ti "Every day..."
                p "Yeah me too...."
                $ renpy.transition(dissolve)
                hide temok
                show temop
                ti "Do not be so pessimistic, try to think about something funny."
                ti "Konoha still stands."
                p "Yeah, I know. We just need to save the fallen shinobies."
                ti "Exactly..."
                $ day = day + 1
                scene black with circleirisin
                show drock0 with circleirisout
                jump drock


        "Husband":
            if temamission == 9:
                $ temamission = 10
                p "Is there anything you can tell me about Shikamaru?"
                $ renpy.transition(dissolve)
                hide temok
                hide temsad
                show temsad
                ti "..."
                ti "What do you want to know about him?"
                p "Did you miss him?"
                ti "..."
                ti "Yes... he was a great husband and wise Shinobi."
                p "I know... But his skills was pretty weird right?"
                $ renpy.transition(dissolve)
                hide temsad
                show temop
                ti "Weird? I think it was amazing."
                ti "His shadow possession can prevent you from moving, or force you to do what he wants."
                p "HMm.. That sound pretty funny. Did he use it on you sometimes?"
                ti "..."
                p "I mean in battle of course..."
                ti "He used it on Chunin exams when we were young... And then when he was dating with me."
                p "Why? Did you try to hit him?"
                $ renpy.transition(dissolve)
                hide temop
                show temcl
                ti "Ehm... No. I was pretty bitchy and try to command him."
                ti "He just wants to shut my mouth so...."
                p "And???"
                ti "Ehm... It was funny..."
                $ renpy.transition(dissolve)
                hide temcl
                show temclop
                ti "Just try to imagine it, he literally can create a spike or hand with that jutsu."
                p "Really? I didn't know that!"
                ti "Damn, I really miss that jutsu..."
                p "And Shikamaru, right?"
                ti "When he use it and start to... MMM..."
                ti "Can we talk later? I need to go home now."
                p "Yeah sure..."
                $ day = day + 1
                scene black with circleirisin
                show drock0 with circleirisout
                jump drock
            else:
                p "Is there anything you can tell me about Shikamaru?"
                ti "He was a great husband and wise Shinobi."
                p "Yes I know that already."
                $ renpy.transition(dissolve)
                hide temok
                hide temsad
                show temsad
                ti "And he was great with shadow pining jutsu."
                p "Sotmehing else?"
                ti "No..."
                scene black with circleirisin
                "That was a waste of your time."
                $ day = day + 1
                show drock0 with circleirisout
                jump drock





#  ROCK KUSHINA LABEL NIGHT
#  ROCK KUSHINA LABEL NIGHT
#  ROCK KUSHINA LABEL NIGHT
#  ROCK KUSHINA LABEL NIGHT
#  ROCK KUSHINA LABEL NIGHT

label nrockclone:
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
    elif kushinamission >= 10:
        "Kushina is in your harem now."
        scene black with circleirisin
        show nrock0 with circleirisout
        jump nrock

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
        show nrock0 with circleirisout
        jump nrock

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
        $ day = day + 1
        scene black with circleirisin
        show drock0 with circleirisout
        jump drock

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
        menu nkushinatalker:
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
                    $ day = day + 1
                    scene black with circleirisin
                    show drock0 with circleirisout
                    jump drock

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
                    ku "Noooo!!! I want to go outside!!!"
                    p "Yeah but..."
                    ku "Get out!!!"
                    scene black with circleirisin
                    p "Shit I need to talk with Kurotsuchi."
                    show nrock0 with circleirisout
                    jump nrock
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
                    $ day = day +1
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
                    $ day = day + 1
                    scene black with circleirisin
                    show drock0 with circleirisout
                    jump drock

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
                    show drock0 with circleirisout
                    jump drock
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
                                    $ day = day + 1
                                    show drock0 with circleirisout
                                    jump drock
                                else:
                                    "But Kushina didn't fall for it."
                                    "Maybe if you improve her relationship with her..."
                                    "You take Kushina to your home and go with her back to Iwagakure next day."
                                    scene black with circleirisin
                                    $ day = day + 1
                                    show drock0 with circleirisout
                                    jump drock

                            "No":
                                p "Ehm... No I am still not ready..."
                                ku "So come back when you are ready... Or do you want something else?"
                                jump nkushinatalker
                    else:
                        ku "Hmpf... Ok.. What do you want to know?"
                        "Fuck there is nothing what I want to know about her right now...."
                        p "Ehm.... How do you feel?"
                        ku "Pretty good actually when you are with me."
                        $ renpy.transition(dissolve)
                        hide kussad
                        show kusok
                        ku "Anything else?"
                        jump nkushinatalker

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
                jump nkushinatalker

            "Have fun":
                if kushinamission <=6:
                    p "Yeah. There a lot of things  I want to do with her."
                    p "But I need to gain her trust first before I try something."
                    jump nkushinatalker

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
                    $ day = day + 1
                    "She still want to hold your hand."
                    show drock0 with circleirisout
                    jump drock

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
                    menu nkushinafucker:
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
                            $ day = day + 1
                            "She still want to hold your hand."
                            show drock0 with circleirisout
                            jump drock

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
                                $ day = day + 1
                                "Kushina has been always behind you with an uncertain look."
                                show drock0 with circleirisout
                                jump drock
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
                                p "Sure"
                                scene black with circleirisin
                                "That was a weird day."
                                $ day = day + 1
                                "Kushina has been always behind you with an uncertain look."
                                show drock0 with circleirisout
                                jump drock

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
                                $ day = day + 1
                                show drock0 with circleirisout
                                jump drock
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
                                $ day = day + 1
                                show drock0 with circleirisout
                                jump drock
                        "Use dildo":
                            if kushinalove ==1:
                                "Try to draw something on her body first..."
                                jump nkushinafucker
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
                                $ day = day + 1
                                show drock0 with circleirisout
                                jump drock
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
                                $ day = day + 1
                                show drock0 with circleirisout
                                jump drock

                        "Fuck her":
                            if kushinalove <=2:
                                p "Good idea, but try to get her trust first."
                                jump nkushinafucker

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
                                $ day = day + 1
                                show drock0 with circleirisout
                                jump drock

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
                                        $ day = day + 1
                                        show drock0 with circleirisout
                                        jump drock

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
                                                $ day = day + 1
                                                show drock0 with circleirisout
                                                jump drock

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
                                                $ day = day + 1
                                                show drock0 with circleirisout
                                                jump drock

                                        scene black with circleirisin
                                        "You spend another wonderfull day with Kushina..."
                                        "Her pussy tasted so sweet!"
                                        $ day = day + 1
                                        show drock0 with circleirisout
                                        jump drock


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
                                            $ day = day + 1
                                            show drock0 with circleirisout
                                            jump drock
                                        else:
                                            "Fucking her tits and pussy was truly amazing. She need some time to recover."
                                            "You spend another great day with her."
                                            $ day = day + 1
                                            show drock0 with circleirisout
                                            jump drock



                                scene black with circleirisin
                                "You spend another good day with Kushina..."
                                "Every time when you two was alone, she kiss you... "
                                $ day = day + 1
                                show drock0 with circleirisout
                                jump drock

                        "Go outside first":
                            if kushinalove <=4:
                                "She is not ready to have sex outside."
                                jump nkushinafucker

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
                                        $ day = day + 1
                                        show drock0 with circleirisout
                                        jump drock


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
                                        $ day = day + 1
                                        show drock0 with circleirisout
                                        jump drock





                                        scene black with circleirisin
                                        $ day = day + 1
                                        show drock0 with circleirisout
                                        jump drock

                    jump nkushinatalker


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
                    $ day = day + 1
                    scene black with circleirisin
                    show drock0 with circleirisout
                    jump drock

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
                    menu nkushinamigan:
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
                            menu nkuntf:
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
                                    jump nkuntf

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
                                    jump nkuntf

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
                                    $ day = day + 1
                                    show drock0 with circleirisout
                                    jump drock

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
                            $ day = day + 1
                            show drock0 with circleirisout
                            jump drock

                        "Mixed training":
                            if expscroll ==0:
                                p "I need an expansion scroll for this."
                                p "I should visit the shop in the Konoha."
                                jump nkushinamigan


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
                                $ day = day + 1
                                show drock0 with circleirisout
                                jump drock

                        "Boob expansion":
                            if expscroll ==0:
                                p "I need an expansion scroll for this."
                                p "I should visit the shop in the Konoha."
                                jump nkushinamigan


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
                                $ day = day + 1
                                show drock0 with circleirisout
                                jump drock

                    scene black with circleirisin
                    show drock0 with circleirisout
                    jump drock

            "Back to the city":
                scene black with circleirisin
                show nrock0 with circleirisout
                jump nrock


        scene black with circleirisin
        show drock0 with circleirisout
        jump drock




#  ROCK TOWN LABEL NIGHT
#  ROCK TOWN LABEL NIGHT
#  ROCK TOWN LABEL NIGHT
#  ROCK TOWN LABEL NIGHT
#  ROCK TOWN LABEL NIGHT

label nrocktown:
    scene rnight
    if mitsukimission ==1:
        "No one is here right now."
        scene black with circleirisin
        show nrock0 with circleirisout
        jump nrock
    else:
        "No one is here right now."
        scene black with circleirisin
        show nrock0 with circleirisout
        jump nrock

# HOSPITAL LABEL   NIGHT
# HOSPITAL LABEL   NIGHT
# HOSPITAL LABEL   NIGHT
# HOSPITAL LABEL   NIGHT
# HOSPITAL LABEL   NIGHT

label nrocklab:
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
                $ day = day + 1
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
                $ day = day + 1
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
        $ day = day + 1
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
        $ day = day +1
        scene black with circleirisin
        "You spend a whole day in the hospital. But you got the access to the building."
        show drock0 with circleirisout
        jump drock


    else:
        $ renpy.transition(dissolve)
        show mit1
        show mitok
        mi"Oh... It is you!"
        menu nmitsukitalk:
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
                            jump nmitsukitalk

                        "That is all":
                            p "But I want to ask you about something else..."
                            jump nmitsukitalk

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
                    jump nmitsukitalk

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
                    jump nmitsukitalk
                else:
                    p "Can you tell me something about yourself?"
                    mi "What exactly you want to know?"
                    p "ehm.... Maybe..."
                    p "Nothing strikes me right now."
                    mi "So what now?"
                    jump nmitsukitalk

            "Talk about hospital":
                if mitsukimission <=5:
                    p "Tell me something about this place."
                    mi "This is the hidden stone hospital."
                    mi "We heal here light and serious wounds."
                    mi "It was destroyed many times, but we will repair it every time."
                    p "Is there something more interesting?"
                    mi "We have many blood samples from the famous Shinobi!"
                    p "Good to know that..."
                    jump nmitsukitalk

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
                    $ day = day + 1
                    show drock0 with circleirisout
                    jump drock

                else:
                    p "Tell me something about this place."
                    mi "This is the hidden stone hospital."
                    mi "We heal here light and serious..."
                    p "Yes I already heared that..."
                    p "Is there any more secret rooms or projects?"
                    mi "No... Cloning was the only side project here."
                    p "Ok..."
                    jump nmitsukitalk

            "Use Namigan":
                p "Can I test my namigan on you?"
                mi "Your namigan? Why?"
                p "I just want to know how it affects you."
                mi "It is not a good idea I am here to help people not to be some kind of text subject."
                p "I think you can be both..."
                mi "Ask lady Tsuchikage first please..."
                p "Hmm... maybe..."
                jump nmitsukitalk

            "Something else":
                if mitsukimission <=3:
                    p "There is nothing right now what I want from her."
                    p "Except some dirty things."
                    jump nmitsukitalk
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
                    jump nmitsukitalk

            "Back to the city":
                scene black with circleirisin
                show nrock0 with circleirisout
                jump nrock

#################### NIGHT VILLAGE #####################
#################### NIGHT VILLAGE #####################
#################### NIGHT VILLAGE #####################
#################### NIGHT VILLAGE #####################
#################### NIGHT VILLAGE #####################


label nrvillage:
    scene nstone
    "Where you want to go?"
    menu:
        "Visit Tenten":
            $ renpy.transition(dissolve)
            hide ten0ok
            hide ten0a
            te "Hello %(p)s. Do you want to have some fun?"
            if tenmission >= 15:
                menu tentenfuckwnight:
                    "Play with her body":
                        if tenmission <= 5:
                            "Nothing."
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
                            $ day = day + 1
                            scene black with circleirisin
                            show drock0 with circleirisout
                            jump drock

                    "Use tools":
                        if tenmission <= 5:
                            "Nothing."

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
                            $ day = day + 1
                            scene black with circleirisin
                            show drock0 with circleirisout
                            jump drock

                    "Fuck her boobs":
                        if tenmission <= 5:
                            "Nothing."

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
                            $ day = day + 1
                            show drock0 with circleirisout
                            jump drock

                    "Fuck her pussy":
                        if tenmission <= 5:
                            "Nothing."

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
                            menu tentenpussyfucknight:
                                "Lightning style":
                                    if clips ==0:
                                        "You need to buy chakra clips first."
                                        jump tentenpussyfucknight
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
                                        jump tentenpussyfucknight

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
                                    jump tentenpussyfucknight


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
                                    $ day = day + 1
                                    show drock0 with circleirisout
                                    jump drock


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
                                    $ day = day + 1
                                    show drock0 with circleirisout
                                    jump drock



                    "Fuck her ass":
                        if tenmission <= 5:
                            "Nothing."


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
                                    $ day = day + 1
                                    scene black with circleirisin
                                    show drock0 with circleirisout
                                    jump drock

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
                                    $ day = day + 1
                                    scene black with circleirisin
                                    show drock0 with circleirisout
                                    jump drock

                    "Kage bunshin":
                        if tenmission <= 5:
                            "Nothing."

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
                            $ day = day + 1
                            scene black with circleirisin
                            show drock0 with circleirisout
                            jump drock

            else:
                "You knock on the door, but no one answer."
                scene black with circleirisin
                show nrock0 with circleirisout
                jump nrock


        "Visit Temari":
            "You knock on the door..."
            if temamission <= 6:
                "But no one answers..."
                scene black with circleirisin
                show nrock0 with circleirisout
                jump nrock

            elif temamission == 7:
                $ temamission = 8
                $ renpy.transition(dissolve)
                show temd
                show temok
                ti "I was waiting for you..."
                p "OK... What can I do for you?"
                ti "This is a good time for it."
                p "For what?"
                $ renpy.transition(dissolve)
                hide temd
                hide temok
                show tema
                show temop
                ti "Just come closer...."
                p "Huh???"
                ti "*smooch*"
                p "???"
                $ renpy.transition(dissolve)
                hide tema
                hide temop
                p "What is going on?"
                $ renpy.transition(dissolve)
                show tem1a
                show tem1ok
                ti "I want you right now!"
                p "OK... But why?"
                ti "Just shut up and fuck me!"
                $ renpy.transition(dissolve)
                show tem1p1
                ti "Yes... Stick it in!"
                $ renpy.transition(dissolve)
                hide tem1p1
                show tem1p2
                ti "Ahhh.. So good... deeper!"
                $ renpy.transition(dissolve)
                hide tem1ok
                show tem1ou
                hide tem1p2
                show tem1p3
                ti "Yeah... Deeper!*moan*"
                $ renpy.transition(dissolve)
                hide tem1p3
                show tem1p4
                p "Just what???"
                $ renpy.transition(dissolve)
                hide tem1ou
                show tem1cl
                ti "*moan*..."
                $ renpy.transition(dissolve)
                hide tem1p4
                show tem1p3
                p "Ok..."
                $ renpy.transition(dissolve)
                hide tem1p3
                show tem1p2
                ti "Ahhh... *moan*"
                $ renpy.transition(dissolve)
                hide tem1p2
                show tem1p3
                show tem1r2
                p "You are pretty hot!"
                $ renpy.transition(dissolve)
                hide tem1p3
                show tem1p4
                hide tem1cl
                show tem1clo
                p "I think... *splurt*"
                $ renpy.transition(dissolve)
                show tem1sp1
                ti "Ahhhh... *heavy moaning*"
                ti "That feels so good..."
                p "Yeah..."
                $ renpy.transition(dissolve)
                hide tem1sp1
                hide tem1p4
                hide tem1clo
                hide tem1a
                hide tem1r2
                "After a while..."
                $ renpy.transition(dissolve)
                show tema
                show temok
                show temsp1
                ti "Thanks, it was good..."
                p "Wait, what the hell?"
                ti "I think you just cum in my pussy..."
                p "Ehm... Yes... But you want it."
                ti "Yes... That is true..."
                $ renpy.transition(dissolve)
                hide temok
                show temop
                ti "Sex with Shinobi is better than with some normal man."
                p "But what now?"
                ti "We can be lovers if you want."
                p "Uh? I think it will be cool."
                ti "Cool? Ok... Just visit me if you want to fuck."
                p "Ehm... Sure... What now?"
                ti "You can leave or stay... It is on you..."
                p "Sure..."
                menu:
                    "Leave":
                        "You decide to go to sleep in the hotel."
                    "Stay":
                        "You decide to sleep in the Temari house."
                $ day = day + 1
                scene black with circleirisin
                show drock0 with circleirisout
                jump drock

            else:
                $ renpy.transition(dissolve)
                show tema
                show temok
                ti "I was waiting for you... "
                p "You are naked again."
                ti "Yes... Because I want to have some fun."
                if temamission == 8:
                    $ temamission = 9
                p "Me too... And now..."
                menu temafff1:
                    "Fuck her pussy":
                        p "Is time to fuck your pussy..."
                        $ renpy.transition(dissolve)
                        hide tema
                        hide temok
                        hide temop
                        ti "Sure..."
                        $ renpy.transition(dissolve)
                        show tem1a
                        show tem1ok
                        ti "I want you right now!"
                        $ renpy.transition(dissolve)
                        show tem1p1
                        ti "Yes... Stick it in!"
                        $ renpy.transition(dissolve)
                        hide tem1p1
                        show tem1p2
                        ti "Ahhh.. So good... deeper!"
                        $ renpy.transition(dissolve)
                        hide tem1ok
                        show tem1ou
                        hide tem1p2
                        show tem1p3
                        ti "Yeah... Deeper!*moan*"
                        $ renpy.transition(dissolve)
                        hide tem1p3
                        show tem1p4
                        p "Nice..."
                        $ renpy.transition(dissolve)
                        hide tem1ou
                        show tem1cl
                        ti "*moan*..."
                        $ renpy.transition(dissolve)
                        hide tem1p4
                        show tem1p3
                        p "Ok..."
                        $ renpy.transition(dissolve)
                        hide tem1p3
                        show tem1p2
                        ti "Ahhh... *moan*"
                        $ renpy.transition(dissolve)
                        hide tem1p2
                        show tem1p3
                        show tem1r2
                        p "You are so hot! Just..."
                        menu:
                            "Just cum":
                                $ renpy.transition(dissolve)
                                hide tem1p3
                                show tem1p4
                                hide tem1cl
                                show tem1clo
                                p "Yeah... *splurt*"
                                $ renpy.transition(dissolve)
                                show tem1sp1
                                ti "Ahhhh... *heavy moaning*"
                                ti "That feels so good..."
                                p "Yeah..."
                                $ renpy.transition(dissolve)
                                hide tem1sp1
                                hide tem1p4
                                hide tem1clo
                                hide tem1a
                                hide tem1r2
                                "After a while..."
                                $ renpy.transition(dissolve)
                                show tema
                                show temok
                                show temsp1
                                ti "Thanks, it was good..."
                                p "yes... You are hot...."
                                ti "Thanks... You too. But next time try to be more creative."
                                p "Ehm... Sure.."
                                ti "I am going to the bad now..."
                                $ renpy.transition(dissolve)
                                hide temok
                                show temop
                                ti "You can sleep here if you want..."
                                p "Sure..."
                                $ day = day + 1
                                scene black with circleirisin
                                show drock0 with circleirisout
                                jump drock
                            "Bigger boobs":
                                p "Your boobs is too small... Make them bigger..."
                                ti "Ahhh..*moan* But..."
                                p "Kai!!!"
                                $ renpy.transition(dissolve)
                                hide tem1a
                                show tem1b
                                hide tem1p3
                                show tem1p4
                                hide tem1r2
                                show tem1r2
                                hide tem1cl
                                show tem1clo
                                ti "Yes...*moan* Is it better?"
                                $ renpy.transition(dissolve)
                                hide tem1p4
                                show tem1p3
                                p "Yes... And I can use these too..."
                                $ renpy.transition(dissolve)
                                hide tem1p3
                                show tem1p2
                                show tem1r1
                                ti "Ahhh...*heavy moaning*"
                                $ renpy.transition(dissolve)
                                hide tem1p2
                                show tem1p3
                                p "And now reward..."
                                $ renpy.transition(dissolve)
                                hide tem1p3
                                show tem1p4
                                hide tem1clo
                                show tem1cl
                                p "Yeah *splurt*"
                                $ renpy.transition(dissolve)
                                show tem1sp1
                                ti "Ahhhh... *heavy moaning*"
                                $ renpy.transition(dissolve)
                                show tem1sp2
                                ti "so much sperm..."
                                p "Yeah..."
                                $ renpy.transition(dissolve)
                                hide tem1sp1
                                hide tem1sp2
                                hide tem1p4
                                hide tem1cl
                                hide tem1b
                                hide tem1r1
                                hide tem1r2
                                "After a while..."
                                $ renpy.transition(dissolve)
                                show temb
                                show temop
                                show temsp1
                                ti "Thanks, it was good..."
                                p "yes... You are hot...."
                                ti "Thanks... You too. But next time try to be more creative."
                                p "Ehm... Sure.."
                                ti "I am going to the bad now..."
                                $ renpy.transition(dissolve)
                                hide temok
                                show temop
                                ti "You can sleep here if you want..."
                                p "Sure..."
                                $ day = day + 1
                                scene black with circleirisin
                                show drock0 with circleirisout
                                jump drock

                            "Huge boobs":
                                p "I want to see huge boobs..."
                                ti "MMM...*moan* It will be..."
                                p "Just make them huge!"
                                ti "OK....Kai!!!"
                                $ renpy.transition(dissolve)
                                hide tem1a
                                show tem1c
                                hide tem1p3
                                show tem1p4
                                hide tem1r2
                                show tem1r2
                                hide tem1cl
                                show tem1clo
                                ti "Yes...*moan* Do you like them now?"
                                $ renpy.transition(dissolve)
                                hide tem1p4
                                show tem1p3
                                p "Yes... And now... Kage bunshin no juts!"
                                $ renpy.transition(dissolve)
                                hide tem1p3
                                show tem1p2
                                show tem1tf1
                                ti "Ahhh...*heavy moaning* More dicks."
                                $ renpy.transition(dissolve)
                                hide tem1p2
                                show tem1p3
                                hide tem1tf1
                                show tem1tf2
                                p "Yeah.."
                                $ renpy.transition(dissolve)
                                hide tem1p3
                                show tem1p4
                                hide tem1tf2
                                show tem1tf3
                                hide tem1clo
                                show tem1cl
                                ti "Fuck my boobs!!!*moan*"
                                $ renpy.transition(dissolve)
                                hide tem1p4
                                show tem1p3
                                hide tem1tf3
                                show tem1tf4
                                ti "Ahhh...*heavy moaning*"
                                $ renpy.transition(dissolve)
                                hide tem1p3
                                show tem1p4
                                hide tem1tf4
                                show tem1tf3
                                show tem1m1
                                p "Yeah *splurt*"
                                $ renpy.transition(dissolve)
                                show tem1sp1
                                ti "Ahhhh... *heavy moaning*"
                                $ renpy.transition(dissolve)
                                hide tem1tf3
                                show tem1tf2
                                show tem1sp2
                                hide tem1cl
                                show tem1ok
                                ti "so much sperm... *drip*"
                                $ renpy.transition(dissolve)
                                hide tem1tf2
                                show tem1tf3
                                show tem1sp3
                                p "Yeah..."
                                $ renpy.transition(dissolve)
                                hide tem1tf3
                                show tem1tf4
                                p "FUCK!!!*splurt*"
                                $ renpy.transition(dissolve)
                                show tem1tf5
                                ti "...."
                                ti "I need to clean myslef now."
                                p "yeah..."
                                $ renpy.transition(dissolve)
                                hide tem1tf4
                                hide tem1tf5
                                hide tem1sp1
                                hide tem1sp2
                                hide tem1sp3
                                hide tem1p4
                                hide tem1ok
                                hide tem1cl
                                hide tem1c
                                hide tem1m1
                                hide tem1r1
                                hide tem1r2
                                "After a while..."
                                $ renpy.transition(dissolve)
                                show temc
                                show temop
                                show temsp1
                                ti "Finally I was fucked by a shinobi!"
                                p "We fucked already before."
                                ti "Yes. But this was what I really need... Good jutsu..."
                                p "Ok... I will try to do something new next time..."
                                ti "Good... Now I am going to the bad..."
                                $ renpy.transition(dissolve)
                                hide temok
                                show temop
                                ti "You can sleep here if you want..."
                                p "Sure..."
                                $ day = day + 1
                                scene black with circleirisin
                                show drock0 with circleirisout
                                jump drock

                    "Fuck her ass":
                        if temamission <= 9:
                            "Sorry but this is not a good idea..."
                            "Fuck her pussy or try to talk with her first..."
                            jump temafff1
                        elif temamission == 10:
                            $ temamission = 11
                            p "I want to try something else today."
                            ti "And what should it be?"
                            p "Your ass..."
                            $ renpy.transition(dissolve)
                            hide tema
                            hide temok
                            hide temop
                            ti "Hmmm..."
                            $ renpy.transition(dissolve)
                            show tem2a
                            show tem2ok
                            ti "I thought you would never ask."
                            p "Are you sure???"
                            ti "Of course..."
                            $ renpy.transition(dissolve)
                            show tem2p1
                            p "Great!!!"
                            $ renpy.transition(dissolve)
                            hide tem2p1
                            show tem2p2
                            hide tem2ok
                            show tem2op
                            ti "Ahhh... *moan*"
                            p "Is it good?"
                            $ renpy.transition(dissolve)
                            hide tem2p2
                            show tem2p3
                            ti "Yeah... It is just too long since someone fuck my ass."
                            $ renpy.transition(dissolve)
                            hide tem2p3
                            show tem2p4
                            hide tem2op
                            show tem2clop
                            ti "Ahhh!!!*moan*"
                            $ renpy.transition(dissolve)
                            hide tem2p4
                            show tem2p3
                            p "Fuck... So good..."
                            $ renpy.transition(dissolve)
                            hide tem2p3
                            show tem2p2
                            ti "Yess!!!"
                            $ renpy.transition(dissolve)
                            hide tem2p2
                            show tem2p3
                            p "Just..."
                            $ renpy.transition(dissolve)
                            hide tem2p3
                            show tem2p4
                            hide tem2clop
                            show tem2cl
                            ti "Ahhhh *heavy moaning*"
                            p "Awesome!!! *splirt*"
                            $ renpy.transition(dissolve)
                            show tem2p5
                            ti "*heavy moaning*"
                            $ renpy.transition(dissolve)
                            show tem2p6
                            "*drip*"
                            p "huh... That was great..."
                            ti "NMmmm...."
                            ti "I missed that so much...."
                            p "..."
                            ti "Time for cleaning..."
                            $ renpy.transition(dissolve)
                            hide tem2p4
                            hide tem2p5
                            hide tem2p6
                            hide tem2cl
                            hide tem2a
                            p "..."
                            $ renpy.transition(dissolve)
                            show tema
                            show temop
                            ti "It was really good... But next time, try to be more creative..."
                            p "I will try to find something for you..."
                            p "You can use your boob jutsu too..."
                            ti "My boob jutsu? Oh... You mean stop suppressing their size..."
                            p "Exactly..."
                            ti "We will see how good you will be next time..."
                            $ day = day + 1
                            scene black with circleirisin
                            show drock0 with circleirisout
                            jump drock

                        else:
                            p "I want to fuck your ass today."
                            ti "Sure, my ass is ready for it..."
                            $ renpy.transition(dissolve)
                            hide tema
                            hide temok
                            hide temop
                            ti "Hmmm..."
                            $ renpy.transition(dissolve)
                            show tem2a
                            show tem2ok
                            ti "What do you waiting for?"
                            $ renpy.transition(dissolve)
                            show tem2p1
                            p "Nothing."
                            $ renpy.transition(dissolve)
                            hide tem2p1
                            show tem2p2
                            hide tem2ok
                            show tem2op
                            ti "Ahhh... *moan*"
                            p "Yeah...."
                            $ renpy.transition(dissolve)
                            hide tem2p2
                            show tem2p3
                            ti "Just fuck it harder!"
                            $ renpy.transition(dissolve)
                            hide tem2p3
                            show tem2p4
                            hide tem2op
                            show tem2clop
                            ti "Ahhh!!!*moan*"
                            $ renpy.transition(dissolve)
                            hide tem2p4
                            show tem2p3
                            p "So good..."
                            $ renpy.transition(dissolve)
                            hide tem2p3
                            show tem2p2
                            ti "Yess!!! Just like that!!!"
                            $ renpy.transition(dissolve)
                            hide tem2p2
                            show tem2p3
                            p "Just..."
                            $ renpy.transition(dissolve)
                            hide tem2p3
                            show tem2p4
                            hide tem2clop
                            show tem2cl
                            ti "Ahhhh *heavy moaning*"
                            menu:
                                "Just cum":
                                    p "Awesome!!! *splirt*"
                                    $ renpy.transition(dissolve)
                                    show tem2p5
                                    ti "*heavy moaning*"
                                    $ renpy.transition(dissolve)
                                    show tem2p6
                                    "*drip*"
                                    p "huh... That was great..."
                                    ti "Mmmm...."
                                    ti "that dick.."
                                    p "..."
                                    ti "Time for cleaning..."
                                    $ renpy.transition(dissolve)
                                    hide tem2p4
                                    hide tem2p5
                                    hide tem2p6
                                    hide tem2cl
                                    hide tem2a
                                    p "..."
                                    $ renpy.transition(dissolve)
                                    show tema
                                    show temop
                                    ti "It was really good... But next time, try to be more creative..."
                                    p "I will try to find something for you..."
                                    p "You can use your boob jutsu too..."
                                    ti "My boob jutsu? Oh... You mean stop suppressing their size..."
                                    p "Exactly..."
                                    ti "We will see how good you will be next time..."
                                    $ day = day + 1
                                    scene black with circleirisin
                                    show drock0 with circleirisout
                                    jump drock
                                "Cancel supresion":
                                    p "KAI!!!"
                                    $ renpy.transition(dissolve)
                                    hide tem2p4
                                    hide tem2cl
                                    hide tem2a
                                    show tem2b
                                    show tem2clop
                                    show tem2p4
                                    ti "Ahhh...*moan* you...."
                                    p "Yes! This is hot!!!"
                                    $ renpy.transition(dissolve)
                                    show tem2h1
                                    hide tem2p4
                                    show tem2p3
                                    p "And that boobies..."
                                    $ renpy.transition(dissolve)
                                    hide tem2p3
                                    show tem2p2
                                    p "Is so good!!!"
                                    $ renpy.transition(dissolve)
                                    hide tem2p2
                                    show tem2p3
                                    ti "MMM...*heavy moaning*"
                                    $ renpy.transition(dissolve)
                                    hide tem2p3
                                    show tem2p2
                                    p "Take it!!! *splirt*"
                                    $ renpy.transition(dissolve)
                                    hide tem2p2
                                    show tem2p1
                                    show tem2p7
                                    p "and more *splurt*"
                                    $ renpy.transition(dissolve)
                                    show tem2p8
                                    ti "Ahhh... *drip*"
                                    p "Hehe... Look at you..."
                                    ti "Mmmm...."
                                    ti "that was a nice trick.."
                                    p "I think so..."
                                    ti "MMm... Just give me some time..."
                                    $ renpy.transition(dissolve)
                                    hide tem2p1
                                    hide tem2p7
                                    hide tem2p8
                                    hide tem2h1
                                    hide tem2cl
                                    hide tem2clop
                                    hide tem2b
                                    p "..."
                                    $ renpy.transition(dissolve)
                                    show tema
                                    show temop
                                    ti "I didn't expect that."
                                    p "What?"
                                    ti "Canceling my boob suppression has really good timing..."
                                    p "Hehe... I just like big boobs."
                                    ti "..."
                                    $ day = day + 1
                                    scene black with circleirisin
                                    show drock0 with circleirisout
                                    jump drock
                                "Use tools":
                                    p "Awesome!!! *splirt*"
                                    $ renpy.transition(dissolve)
                                    show tem2p5
                                    ti "*heavy moaning*"
                                    $ renpy.transition(dissolve)
                                    show tem2p6
                                    "*drip*"
                                    p "huh... That was great..."
                                    ti "Mmmm...."
                                    p "Now clean yourself..."
                                    ti "Sure......."
                                    $ renpy.transition(dissolve)
                                    hide tem2p4
                                    hide tem2p5
                                    hide tem2p6
                                    p "Good... I bring something special today..."
                                    $ renpy.transition(dissolve)
                                    show tem2a1
                                    ti "Huh???"
                                    $ renpy.transition(dissolve)
                                    hide tem2a1
                                    show tem2a2
                                    hide tem2cl
                                    show tem2clop
                                    ti "Arggh... *moan*"
                                    p "A moment...."
                                    $ renpy.transition(dissolve)
                                    hide tem2a2
                                    show tem2a3
                                    p "And it is in..."
                                    ti "Yeah..."
                                    $ renpy.transition(dissolve)
                                    hide tem2clop
                                    show tem2ok
                                    ti "What now???"
                                    $ renpy.transition(dissolve)
                                    show tem2d1
                                    p "This!!! *splash*"
                                    ti "Ahhhh...."
                                    p "And on!"
                                    $ renpy.transition(dissolve)
                                    show tem2anal
                                    hide tem2ok
                                    show tem2op
                                    ti "Ahhhrgghh..."
                                    p "Good... Now you can enjoy it..."
                                    p "I will go home... And do not pull it out until the morning right?"
                                    ti "What???"
                                    p "You can thank me later."
                                    $ day = day + 1
                                    scene black with circleirisin
                                    show drock0 with circleirisout
                                    jump drock


                scene black with circleirisin
                show drock0 with circleirisout
                jump drock


        "Visit Kaguya":
            "You knock on the door..."
            if kagumission <= 1:
                "You heard someone behind the door, but no one answers."
                scene black with circleirisin
                show nrock0 with circleirisout
                jump nrock

            elif kagumission == 2:
                $ renpy.transition(dissolve)
                show kagg1
                show kaggok
                ka "Hello %(p)s..."
                p "Hi..."
                $ kagumission = 3
                p "You look so different now."
                ka "Yes, this is my favorite outfit. I wear it after I return from work."
                ka "It is much more comfortable than my work outfit."
                ka "Do you like it?"
                menu:
                    "Yes":
                        p "Yes, you look really pretty now."
                        $ renpy.transition(dissolve)
                        hide kaggok
                        show kagghap
                        ka "Thank you..."
                    "No":
                        p "I like your work outfit. This one is not so nice."
                        $ renpy.transition(dissolve)
                        hide kaggok
                        show kaggsad
                        ka "Hmpf..."

                p "Anyway, I just want to check if you are alright, and maybe go out with you and have some fun."
                $ renpy.transition(dissolve)
                hide kagghap
                hide kaggsad
                show kaggshock
                ka "You want to go out with me?"
                p "Yes... Is it so shocking for you?"
                ka "Ehm... Yes... I lived here a couple of years and no one ever wants to go out with me."
                p "That is sad... But I want to have some drinks and enjoy them with you. Are you in?"
                $ renpy.transition(dissolve)
                hide kaggshock
                show kagghap
                ka "Sure! Let's go!"
                scene black with circleirisin
                "You spend a wonderful night with Kaguya. It looks like she likes you."
                $ day = day + 1
                "But you felt really strong aura about her... Be careful, and don't try to piss her out!"
                show drock0 with circleirisout
                jump drock


            else:
                $ renpy.transition(dissolve)
                show kagg1
                show kaggok
                ka "Hello %(p)s... What do you want to do today?"
                menu kagunighttalk:
                    "Talk":
                        if kagumission <= 3:
                            p "I just want to know how are you tonight."
                            ka "I am fine... Maybe a little lonely."
                            p "I can stay with you if you want..."
                            ka "That would be nice..."
                            scene black with circleirisin
                            "You spend some time with Kaguay. She is not scary as people say."
                            $ day = day + 1
                            show drock0 with circleirisout
                            jump drock
                        else:
                            p "I just want to know how are you tonight."
                            $ renpy.transition(dissolve)
                            hide kaggok
                            show kagghap
                            ka "I feel good when you are with me."
                            p "Do you want to talk about something?"
                            ka "Not really, but maybe we can do something funny tonight."
                            p "Huh? Sure..."
                            $ renpy.transition(dissolve)
                            hide kagghap
                            show kaggok
                            jump kagunighttalk

                    "Go out":
                        if kagumission <= 3:
                            p "Do you want to go out with me tonight?"
                            ka "Sure? Where you want to go?"
                            p "To the pub or just hang out in the village."
                            $ renpy.transition(dissolve)
                            hide kaggok
                            show kagghap
                            ka "That sounds great lets go!"
                            scene black with circleirisin
                            "Kaguya was really nice tonight... You both enjoyed the night together."
                            $ day = day + 1
                            show drock0 with circleirisout
                            jump drock
                        elif kagumission == 4:
                            p "Do you want to go out with me tonight?"
                            ka "Sure? Where you want to go?"
                            $ kagumission = 5
                            p "To the pub or just hang out in the village."
                            $ renpy.transition(dissolve)
                            hide kaggok
                            show kagghap
                            ka "That sounds great lets go!"
                            scene black with circleirisin
                            show rnight with circleirisout
                            $ renpy.transition(dissolve)
                            hide kagg1
                            hide kagghap
                            show kagg1
                            show kaggok
                            ka "%(p)s ...."
                            p "What?"
                            ka "Nothing...."
                            with fade
                            ka "...."
                            ka "Can I ask you something personal?"
                            p "Ehm sure... Why not?"
                            ka "How many women have you slept with?"
                            p "Huh??? Not sure maybe ten or twenty..."
                            $ renpy.transition(dissolve)
                            hide kaggok
                            show kaggshock
                            ka "Twenty?"
                            p "Maybe more.... Why you asking?"
                            ka "Ehm... Nevermind..."
                            $ renpy.transition(dissolve)
                            hide kaggshock
                            show kaggcl
                            p "Come on. "
                            ka "..."
                            p "Ok... How many mans you slept with?"
                            ka "Zero...."
                            p "Are you crazy???" with hpunch
                            p "You are a hot woman and didn't sleep with anyone? That is not legal!"
                            ka "It is because everyone is so scared, no one wants to kiss me..."
                            p "Hmmm... *smooch*"
                            $ renpy.transition(dissolve)
                            hide kaggcl
                            show kaggok
                            ka "Mmmm..."
                            p "How it feels?"
                            ka "It was good... Do it again!"
                            p "*smooch*"
                            ka "*smooch*"
                            "You start to kissing Kaguya and slowly undressing her."
                            $ renpy.transition(dissolve)
                            hide kaggok
                            show kaggcl
                            ka "Ahhh... Wait...."
                            p "Is something wrong?"
                            ka "No just... It is just too fast..."
                            p "Should I slow down?"
                            ka "No... Maybe a little..."
                            p "*smooch*"
                            $ renpy.transition(dissolve)
                            hide kagg1
                            hide kaggcl
                            show kagg2
                            show kaggok
                            show kaggshy
                            ka "...."
                            p "Do not be shy, you are beautiful."
                            ka "Thank you..."
                            p "*smooch*"
                            scene black with circleirisin
                            "You spend the night with Kaguya and finally undress her..."
                            "Now is the time to do some funny stuff..."
                            $ day = day + 1
                            show drock0 with circleirisout
                            jump drock

                        else:
                            p "Do you want to go out with me tonight?"
                            ka "Sure? Where you want to go?"
                            p "To the pub or just hang out in the village."
                            $ renpy.transition(dissolve)
                            hide kaggok
                            show kagghap
                            ka "That sounds great lets go!"
                            scene black with circleirisin
                            show rnight with circleirisout
                            $ renpy.transition(dissolve)
                            hide kagg1
                            hide kagghap
                            show kagg1
                            show kaggok
                            ka "%(p)s ... What do you want to do now?"
                            menu kagufucknight12:
                                "Undress her":
                                    if kagumission <= 5:
                                        p "I think you know what I want..."
                                        $ renpy.transition(dissolve)
                                        hide kaggok
                                        show kaggcl
                                        ka "*smooch*"
                                        p "Yeah... This is good... *smooch*"
                                        "You start to kissing Kaguya and slowly undressing her."
                                        $ renpy.transition(dissolve)
                                        hide kaggcl
                                        show kaggok
                                        ka "Ahhh... %(p)s ..."
                                        $ renpy.transition(dissolve)
                                        hide kaggok
                                        show kaggcl
                                        p "*smooch*"
                                        $ renpy.transition(dissolve)
                                        hide kagg1
                                        hide kaggcl
                                        show kagg2
                                        show kaggok
                                        show kaggshy
                                        ka "Yesss...."
                                        p "*smooch*"
                                        "You slowly start to kissing Kaguya body."
                                        scene black with circleirisin
                                        "You spend the night with Kaguya..."
                                        "But you should really try to do something different."
                                        $ day = day + 1
                                        show drock0 with circleirisout
                                        jump drock

                                    else:
                                        p "I think you know what I want..."
                                        $ renpy.transition(dissolve)
                                        hide kaggok
                                        show kaggcl
                                        ka "*smooch*"
                                        p "Yeah... This is good... *smooch*"
                                        "You start to kissing Kaguya and slowly undressing her."
                                        $ renpy.transition(dissolve)
                                        hide kaggcl
                                        show kaggok
                                        ka "Ahhh... %(p)s ..."
                                        $ renpy.transition(dissolve)
                                        hide kaggok
                                        show kaggcl
                                        p "*smooch*"
                                        $ renpy.transition(dissolve)
                                        hide kagg1
                                        hide kaggcl
                                        show kagg2
                                        show kaggok
                                        show kaggshy
                                        ka "Yesss...."
                                        p "Do you want more?"
                                        ka "Yesss...*moan*"
                                        p "Sexy water jutsu *splash*"
                                        $ renpy.transition(dissolve)
                                        hide kaggok
                                        hide kaggshy
                                        show kaggcl
                                        show kaggshy
                                        show kaggw1
                                        ka "Ahhh... *moan feels good*"
                                        p "Second level activated *splash*"
                                        $ renpy.transition(dissolve)
                                        show kaggw2
                                        ka "Yesss.. Give me more!!! *moan smooch*"
                                        p "Final release!!! *splash*"
                                        $ renpy.transition(dissolve)
                                        show kaggw3
                                        ka "Ahhhh*heavy moaning*"
                                        $ renpy.transition(dissolve)
                                        hide kaggcl
                                        hide kaggshy
                                        show kaggorg
                                        show kaggshy
                                        show kaggm1
                                        ka "This is so good... *heavy moaning* Come her *smooch*"
                                        p "*smooch*"
                                        scene black with circleirisin
                                        "Yeah, that was fun. Kaguya is really beautiful chick."
                                        $ day = day + 1
                                        show drock0 with circleirisout
                                        jump drock

                                "Titfuck":
                                    if kagumission <= 5:
                                        "This is not a good idea..."
                                        "Try to build some relationship with her first."
                                        jump kagufucknight12

                                    elif kagumission == 6:
                                        p "Do you want to have some fun?"
                                        ka "What you mean by that?"
                                        p "I will show you just take off your top..."
                                        ka "Huh???"
                                        $ kagumission = 7
                                        $ renpy.transition(dissolve)
                                        hide kagg1
                                        hide kaggok
                                        ka "Wait... What are you???"
                                        ka "Mghmmm????"
                                        $ renpy.transition(dissolve)
                                        show kag2a
                                        show kag2ok
                                        show kag2p1
                                        ka "ghhhmmm???"
                                        p "Yes... This is good..."
                                        ka "Hmmm?? Ghhhmm???"
                                        p "Sure I will put it deeper..."
                                        $ renpy.transition(dissolve)
                                        hide kag2ok
                                        show kag2shock
                                        hide kag2p1
                                        show kag2p2
                                        ka "Hmpppgf??? *gag*"
                                        p "Yeah... it feels good right?"
                                        ka "Ghhtgmmh???? *cough gag*"
                                        p "Or it is too much for you?"
                                        $ renpy.transition(dissolve)
                                        hide kag2shock
                                        show kag2sad
                                        hide kag2p2
                                        show kag2p1
                                        ka "ghgmhmm... *mumble*"
                                        p "Yeah... I feel same... Just..."
                                        $ renpy.transition(dissolve)
                                        hide kag2sad
                                        show kag2ok
                                        show kag2h1
                                        hide kag2p1
                                        show kag2p2
                                        p "Yeah.... That nipples..."
                                        $ renpy.transition(dissolve)
                                        show kag2h2
                                        hide kag2p2
                                        show kag2p1
                                        p "Great..."
                                        $ renpy.transition(dissolve)
                                        hide kag2ok
                                        show kag2sad
                                        show kag2h1
                                        hide kag2p1
                                        show kag2p2
                                        p "Just a moment.... yeah *splurt*"
                                        $ renpy.transition(dissolve)
                                        show kag2sp1
                                        hide kag2sad
                                        show kag2shock
                                        ka "Mhmmmhmmm..*gag moan*"
                                        $ renpy.transition(dissolve)
                                        show kag2sp2
                                        p "And more.... *splurt*"
                                        $ renpy.transition(dissolve)
                                        show kag2sp3
                                        ka "Ahhhgmhmmhmm....*gag splurt moan*"
                                        p "Shit... This is so good..."
                                        ka "*mumble gag*"
                                        p "Yeah... I forgot...."
                                        $ renpy.transition(dissolve)
                                        hide kag2sp1
                                        hide kag2sp2
                                        hide kag2sp3
                                        hide kag2shock
                                        hide kag2a
                                        hide kag2h1
                                        hide kag2h2
                                        hide kag2p2
                                        p "Are you allright?"
                                        $ renpy.transition(dissolve)
                                        show kagg1
                                        show kaggok
                                        show kaggsp1
                                        ka "MMm.... Yes... I feel great... *glog*"
                                        p "Good... Your boobs are amazing!"
                                        ka "Thanks... mmmm...*slurp*"
                                        p "What?"
                                        ka "That was my first titfuck."
                                        p "Really? And do you enjoy it?"
                                        $ renpy.transition(dissolve)
                                        hide kaggok
                                        show kaggorg
                                        hide kaggsp1
                                        show kaggsp1
                                        ka "Yes... We should do it more often. Your sperm is delicious!"
                                        p "That is a great idea!"
                                        ka "Hehe... I am happy that you want to do things like this with me."
                                        p "I enjoyed it too... Maybe we can do more next time."
                                        ka "Hehe... That would be great..."
                                        p "..."
                                        p "I am really tired..."
                                        ka "Do you want to sleep here?"
                                        p "Yeah... Sure, why not...."
                                        scene black with circleirisin
                                        $ day = day + 1
                                        show drock0 with circleirisout
                                        jump drock
                                    else:
                                        p "Do you want to have some fun?"
                                        ka "What you mean by that?"
                                        p "I will show you just take off your top..."
                                        ka "Yaiks, you want to play with my tits right?"
                                        $ renpy.transition(dissolve)
                                        hide kagg1
                                        hide kaggok
                                        p "Hehe..."
                                        ka "Mghmmm...*moan*"
                                        $ renpy.transition(dissolve)
                                        show kag2a
                                        show kag2ok
                                        show kag2p1
                                        ka "*moan*"
                                        p "Yes... This is good..."
                                        ka "Hmmm....*moan cough*"
                                        p "Sure I will put it deeper..."
                                        $ renpy.transition(dissolve)
                                        hide kag2ok
                                        show kag2shock
                                        hide kag2p1
                                        show kag2p2
                                        ka "Hmpppgf... *gag cough*"
                                        p "Yeah... it feels good right?"
                                        ka "Ghhtgmmh... *moan cough gag*"
                                        p "Or it is too much for you?"
                                        $ renpy.transition(dissolve)
                                        hide kag2shock
                                        show kag2sad
                                        hide kag2p2
                                        show kag2p1
                                        ka "ghgmhmm... *mumble moan*"
                                        p "*squeeze*"
                                        $ renpy.transition(dissolve)
                                        hide kag2sad
                                        show kag2ok
                                        show kag2h1
                                        hide kag2p1
                                        show kag2p2
                                        p "That nipples...*squeeze*"
                                        $ renpy.transition(dissolve)
                                        show kag2h2
                                        hide kag2p2
                                        show kag2p1
                                        p "Great..."
                                        $ renpy.transition(dissolve)
                                        hide kag2ok
                                        show kag2sad
                                        show kag2h1
                                        hide kag2p1
                                        show kag2p2
                                        p "Just a moment.... *splurt*"
                                        $ renpy.transition(dissolve)
                                        show kag2sp1
                                        hide kag2sad
                                        show kag2shock
                                        ka "Mhmmmhmmm..*gag moan*"
                                        $ renpy.transition(dissolve)
                                        show kag2sp2
                                        p "And more.... *splurt*"
                                        $ renpy.transition(dissolve)
                                        show kag2sp3
                                        ka "Ahhhgmhmmhmm....*gag splurt moan*"
                                        p "Shit... This is so good..."
                                        ka "*mumble gag*"
                                        p "Yeah... I forgot...."
                                        $ renpy.transition(dissolve)
                                        hide kag2sp1
                                        hide kag2sp2
                                        hide kag2sp3
                                        hide kag2shock
                                        hide kag2a
                                        hide kag2h1
                                        hide kag2h2
                                        hide kag2p2
                                        p "Are you allright?"
                                        $ renpy.transition(dissolve)
                                        show kagg1
                                        show kaggok
                                        show kaggsp1
                                        ka "MMm.... Yes... I feel great... *glog*"
                                        p "Good... Your boobs are amazing!"
                                        ka "Thanks... mmmm...*slurp*"
                                        p "What?"
                                        ka "Every titfuck is better than the one before."
                                        p "Yeah, I feel same."
                                        $ renpy.transition(dissolve)
                                        hide kaggok
                                        show kaggorg
                                        hide kaggsp1
                                        show kaggsp1
                                        ka "Your delicious sperm in my mouth. *moan*"
                                        p ".... ehm.... *cough*"
                                        ka "Sorry I was just thinking about something..."
                                        p "What?"
                                        ka "Nothing... Just a fantasy..."
                                        p "..."
                                        ka "It is time to go to the bed."
                                        ka "You can stay here if you want."
                                        p "Sure...."
                                        scene black with circleirisin
                                        $ day = day + 1
                                        show drock0 with circleirisout
                                        jump drock

                                "Fuck her":
                                    if kagumission <= 7:
                                        "This is not a good idea..."
                                        "Try to build some relationship with her first."
                                        jump kagufucknight12

                                    elif kagumission == 8:
                                        p "I was thinking about what you said last time."
                                        ka "???"
                                        $ kagumission = 9
                                        p "Do you really have a plan to enslave the mankind?"
                                        $ renpy.transition(dissolve)
                                        hide kaggok
                                        show kaggsad
                                        ka "You didn't understand me. I do not want to enslave anyone. It was just..."
                                        ka "Ahhh..."
                                        p "What?"
                                        ka "I will tell it to you, but you need to deserve it. Show me what you have!"
                                        $ renpy.transition(dissolve)
                                        hide kagg1
                                        hide kaggsad
                                        p "If that is what you really want..."
                                        $ renpy.transition(dissolve)
                                        show kag1a
                                        show kag1ok
                                        show kag1p1
                                        ka "So you want to fuck my pussy? Hmm... That will be good..."
                                        $ renpy.transition(dissolve)
                                        hide kag1p1
                                        show kag1p2
                                        p "Actually I can do more that that..."
                                        $ renpy.transition(dissolve)
                                        hide kag1p2
                                        show kag1p3
                                        p "Kage bunshin no jutsu!"
                                        $ renpy.transition(dissolve)
                                        hide kag1p2
                                        show kag1p3
                                        show kag1a1
                                        hide kag1ok
                                        show kag1op
                                        ka "Ahhh... *moan* another dick?"
                                        p "Yes...."
                                        $ renpy.transition(dissolve)
                                        hide kag1p2
                                        show kag1p3
                                        hide kag1a1
                                        show kag1a2
                                        ka "My ass!!!"
                                        $ renpy.transition(dissolve)
                                        hide kag1p3
                                        show kag1p4
                                        hide kag1a2
                                        show kag1a3
                                        hide kag1op
                                        show kag1clop
                                        ka "Ahhh!!!! *moan*"
                                        p "Kage bunshin no jutsu!"
                                        $ renpy.transition(dissolve)
                                        hide kag1p4
                                        show kag1p3
                                        hide kag1a3
                                        show kag1a4
                                        show kag1bl1
                                        p "Take this!"
                                        $ renpy.transition(dissolve)
                                        hide kag1p3
                                        show kag1p2
                                        hide kag1a4
                                        show kag1a3
                                        hide kag1bl1
                                        show kag1bl2
                                        ka "Mghhmmm...*moan lick*"
                                        $ renpy.transition(dissolve)
                                        hide kag1p2
                                        show kag1p3
                                        hide kag1a3
                                        show kag1a2
                                        hide kag1clop
                                        show kag1op
                                        hide kag1bl2
                                        show kag1bl3
                                        p "Nice... suck it!!!"
                                        $ renpy.transition(dissolve)
                                        hide kag1p3
                                        show kag1p4
                                        hide kag1a2
                                        show kag1a3
                                        hide kag1bl3
                                        show kag1bl4
                                        ka "Mgmhmhgmhm...*gag cough choke*"
                                        p "Yeah...."
                                        $ renpy.transition(dissolve)
                                        hide kag1p4
                                        show kag1p3
                                        hide kag1a3
                                        show kag1a4
                                        hide kag1bl4
                                        show kag1bl3
                                        p "Awesome!!!"
                                        $ renpy.transition(dissolve)
                                        hide kag1p3
                                        show kag1p2
                                        hide kag1a4
                                        show kag1a3
                                        hide kag1bl3
                                        show kag1bl2
                                        ka "gegrg....*cough choke*"
                                        $ renpy.transition(dissolve)
                                        hide kag1p2
                                        show kag1p1
                                        hide kag1a3
                                        show kag1a2
                                        hide kag1bl2
                                        show kag1bl3
                                        p "Just... *splurt*"
                                        $ renpy.transition(dissolve)
                                        show kag1p7
                                        hide kag1a2
                                        show kag1a3
                                        hide kag1op
                                        show kag1clop
                                        hide kag1bl3
                                        show kag1bl4
                                        ka "hhrgggrgg... *moan choke*"
                                        $ renpy.transition(dissolve)
                                        show kag1p8
                                        hide kag1a3
                                        show kag1a4
                                        hide kag1bl4
                                        show kag1bl3
                                        p "You are awesome! *splurt*"
                                        $ renpy.transition(dissolve)
                                        show kag1a5
                                        hide kag1bl3
                                        show kag1bl2
                                        ka "Ahmmm...*moan gag cough*"
                                        $ renpy.transition(dissolve)
                                        show kag1a6
                                        hide kag1bl2
                                        show kag1bl3
                                        p "Drink it all!!!*splurt*"
                                        $ renpy.transition(dissolve)
                                        hide kag1bl3
                                        show kag1bl4
                                        show kag1bl5
                                        ka "Ghhh...*choke gag cough*"
                                        $ renpy.transition(dissolve)
                                        show kag1bl6
                                        p "....."
                                        p "That was pretty much everything I had."
                                        p "So do you want to tell me your plan now?"
                                        ka "chrrr....*gag cough*"
                                        p "Yeah I almost forgot..."
                                        $ renpy.transition(dissolve)
                                        hide kag1bl6
                                        hide kag1bl5
                                        hide kag1bl4
                                        hide kag1a6
                                        hide kag1a5
                                        hide kag1a4
                                        hide kag1p4
                                        hide kag1p1
                                        hide kag1p7
                                        hide kag1p8
                                        hide kag1clop
                                        hide kag1a
                                        p "..."
                                        $ renpy.transition(dissolve)
                                        show kagg2
                                        show kaggsad
                                        show kaggsp1
                                        show kaggsp2
                                        ka "Ahhh....*moan*"
                                        p "Are you allright???"
                                        ka "uh? Yes... I just...*moan* wow..."
                                        ka "It was so good..."
                                        p "So will you tell me your plan?"
                                        ka "Sure... Ehm... Where I ended last time?"
                                        p "You told me something about using our powers to make girls more helpful."
                                        $ renpy.transition(dissolve)
                                        hide kaggsad
                                        show kaggok
                                        ka "Yes. I remember..."
                                        ka "Your power can affect mind space and time."
                                        p "Huh? Really? How do you know it?"
                                        ka "I am not sure I just feel it from you."
                                        p "*sigh* Continue..."
                                        ka "You really enjoy fucking with women right?"
                                        p "Ehm... Yes that is true."
                                        ka "I enjoyed it too... Anyway.... It is hard to persuade them right?"
                                        p "Sometimes..."
                                        $ renpy.transition(dissolve)
                                        hide kaggok
                                        show kaggcl
                                        ka "But what if you use your Namigan to make it easier?"
                                        p "Huh? Really? I never think about my powers in that way!"
                                        ka "But you can use them to change or erase memories... Maybe completely delete the personality."
                                        p "Continue..."
                                        $ renpy.transition(dissolve)
                                        hide kaggcl
                                        show kaggok
                                        ka "Maybe if I help you we can capture some girls and make them have sex with us!"
                                        p "Huh... That sounds good... But where you want to do that? It is dangerous to do it in the big village there are many guards and sensory chakra type guys."
                                        ka "Yes I know... But we are both really strong..."
                                        p "So you want to fight the good guys?"
                                        ka "No.... I was thinking about creating a new home for us..."
                                        ka "I know one place in the forest between the villages. I have already built something there with my chakra."
                                        p "So you are telling me that we should live together in the other village with other women?"
                                        $ renpy.transition(dissolve)
                                        hide kaggok
                                        show kagghap
                                        ka "If you want it...."
                                        p "It actually sounds pretty cool... My own harem village..."
                                        ka "It is only an option for now... But I think it will be fun to fuck with more women..."
                                        p "Yeah... You are right... Where you want to start it?"
                                        ka "It is all about you... Right now I need some rest you destroyed all my holes... *chuckles*"
                                        p "Sure... See you later..."
                                        scene black with circleirisin
                                        $ day = day + 1
                                        show drock0 with circleirisout
                                        jump drock

                                    else:
                                        p "I want to use my kage bunshin tonight."
                                        hide kaggok
                                        show kagghap
                                        ka "That is amazing idea..."
                                        p "Are you ready for it?"
                                        $ renpy.transition(dissolve)
                                        hide kagg1
                                        hide kagghap
                                        ka "Give me a moment."
                                        $ renpy.transition(dissolve)
                                        show kag1a
                                        show kag1ok
                                        show kag1p1
                                        ka "And stick it in!"
                                        $ renpy.transition(dissolve)
                                        hide kag1p1
                                        show kag1p2
                                        ka "Make some clones please."
                                        $ renpy.transition(dissolve)
                                        hide kag1p2
                                        show kag1p3
                                        p "Sure... Kage bunshin no jutsu! *puff*"
                                        $ renpy.transition(dissolve)
                                        hide kag1p2
                                        show kag1p3
                                        show kag1a1
                                        hide kag1ok
                                        show kag1op
                                        ka "Ahhh... *moan*"
                                        p "Hehe...."
                                        $ renpy.transition(dissolve)
                                        hide kag1p2
                                        show kag1p3
                                        hide kag1a1
                                        show kag1a2
                                        ka "Right in my ass..."
                                        $ renpy.transition(dissolve)
                                        hide kag1p3
                                        show kag1p4
                                        hide kag1a2
                                        show kag1a3
                                        hide kag1op
                                        show kag1clop
                                        ka "Ahhh!!!! *moan*"
                                        p "Kage bunshin no jutsu! *puff*"
                                        $ renpy.transition(dissolve)
                                        hide kag1p4
                                        show kag1p3
                                        hide kag1a3
                                        show kag1a4
                                        show kag1bl1
                                        p "Take this!"
                                        $ renpy.transition(dissolve)
                                        hide kag1p3
                                        show kag1p2
                                        hide kag1a4
                                        show kag1a3
                                        hide kag1bl1
                                        show kag1bl2
                                        ka "Mghhmmm...*moan lick*"
                                        $ renpy.transition(dissolve)
                                        hide kag1p2
                                        show kag1p3
                                        hide kag1a3
                                        show kag1a2
                                        hide kag1clop
                                        show kag1op
                                        hide kag1bl2
                                        show kag1bl3
                                        p "Nice... suck it!!!"
                                        $ renpy.transition(dissolve)
                                        hide kag1p3
                                        show kag1p4
                                        hide kag1a2
                                        show kag1a3
                                        hide kag1bl3
                                        show kag1bl4
                                        ka "Mgmhmhgmhm...*gag cough choke*"
                                        p "Yeah...."
                                        $ renpy.transition(dissolve)
                                        hide kag1p4
                                        show kag1p3
                                        hide kag1a3
                                        show kag1a4
                                        hide kag1bl4
                                        show kag1bl3
                                        p "Awesome!!!"
                                        $ renpy.transition(dissolve)
                                        hide kag1p3
                                        show kag1p2
                                        hide kag1a4
                                        show kag1a3
                                        hide kag1bl3
                                        show kag1bl2
                                        ka "gegrg....*cough choke*"
                                        $ renpy.transition(dissolve)
                                        hide kag1p2
                                        show kag1p1
                                        hide kag1a3
                                        show kag1a2
                                        hide kag1bl2
                                        show kag1bl3
                                        p "Just... *splurt*"
                                        $ renpy.transition(dissolve)
                                        show kag1p7
                                        hide kag1a2
                                        show kag1a3
                                        hide kag1op
                                        show kag1clop
                                        hide kag1bl3
                                        show kag1bl4
                                        ka "hhrgggrgg... *moan choke*"
                                        $ renpy.transition(dissolve)
                                        show kag1p8
                                        hide kag1a3
                                        show kag1a4
                                        hide kag1bl4
                                        show kag1bl3
                                        p "You are awesome! *splurt*"
                                        $ renpy.transition(dissolve)
                                        show kag1a5
                                        hide kag1bl3
                                        show kag1bl2
                                        ka "Ahmmm...*moan gag cough*"
                                        $ renpy.transition(dissolve)
                                        show kag1a6
                                        hide kag1bl2
                                        show kag1bl3
                                        p "Drink it all!!!*splurt*"
                                        $ renpy.transition(dissolve)
                                        hide kag1bl3
                                        show kag1bl4
                                        show kag1bl5
                                        ka "Ghhh...*choke gag cough*"
                                        $ renpy.transition(dissolve)
                                        show kag1bl6
                                        p "....."
                                        p "That was pretty much everything I had."
                                        p "Did you enjoy it, too?"
                                        ka "chrrr....*gag cough*"
                                        p "Yeah I almost forgot..."
                                        $ renpy.transition(dissolve)
                                        hide kag1bl6
                                        hide kag1bl5
                                        hide kag1bl4
                                        hide kag1a6
                                        hide kag1a5
                                        hide kag1a4
                                        hide kag1p4
                                        hide kag1p1
                                        hide kag1p7
                                        hide kag1p8
                                        hide kag1clop
                                        hide kag1a
                                        p "..."
                                        $ renpy.transition(dissolve)
                                        show kagg2
                                        show kaggsad
                                        show kaggsp1
                                        show kaggsp2
                                        ka "Ahhh....*moan*"
                                        ka "That was fantastic!*moan*"
                                        p "Good to hear it..."
                                        ka "My legs are trembling now."
                                        $ renpy.transition(dissolve)
                                        hide kaggsad
                                        show kaggok
                                        ka "I think I need some rest now..."
                                        ka "You can sleep with me tonight if you want...."
                                        p "Sure... Just wash yourself first..."
                                        ka "Maybe we can wash together."
                                        p "That sound good too..."
                                        ka "Ok, come with me..."
                                        scene black with circleirisin
                                        $ day = day + 1
                                        show drock0 with circleirisout
                                        jump drock


                    "Namigan":
                        if missionsa == 0:
                            "You don't know how to use Namigan."
                            jump kagunighttalk
                        elif missionsa == 1:
                            p "I want to test something..."
                            ka "What?"
                            p "Just give me your hand please..."
                            ka "..."
                            ka "Ok..."
                            p "NAMIGAN!!!" with hpunch
                            ka "..."
                            p "Do you feel something?"
                            ka "What should I be feeling?"
                            p "Ehm...."
                            p "Nevermind."
                            $ renpy.transition(dissolve)
                            show nc:
                                yalign .5 subpixel True
                                parallel:
                                    xalign .5
                                    alpha 1.0 zoom 1.0
                                    linear .75 alpha .5 zoom .9
                                    linear .75 alpha 1.0 zoom 1.0
                                    repeat

                                parallel:
                                    rotate 0
                                    linear 5 rotate 360
                                    repeat
                            n "The Little advice mind break will not work on Kaguya."
                            p "What? Why?"
                            n "Her kekkei genkai will not allow you to use it."
                            p "Fuck..."
                            n "But time stop will allow you to have some fun... Try to unlock it first."
                            p "Great thanks..."
                            $ renpy.transition(dissolve)
                            hide nc
                            jump kagunighttalk

                        elif missionsa >=2:
                            p "I want to test something..."
                            ka "What?"
                            p "Just give me your hand please..."
                            ka "..."
                            ka "Ok..."
                            p "NAMIGAN!!! Time stop!" with hpunch
                            ka "..."
                            p "Do you feel something?"
                            ka "...."
                            p "It really works..."
                            p "So now is time to..."
                            menu kagunamifuck:
                                "Fuck her mouth and pussy":
                                    $ renpy.transition(dissolve)
                                    p "Time to fuck you... But you need to get into the right position first..."
                                    $ renpy.transition(dissolve)
                                    hide kagg1
                                    hide kaggok
                                    p "..."
                                    $ renpy.transition(dissolve)
                                    show kag4a
                                    show kag4ok
                                    p "Hehe nice... First...."
                                    $ renpy.transition(dissolve)
                                    show kag4bl1
                                    ka "..."
                                    $ renpy.transition(dissolve)
                                    hide kag4bl1
                                    show kag4bl2
                                    p "Yeah... This is good...."
                                    $ renpy.transition(dissolve)
                                    hide kag4bl2
                                    show kag4bl3
                                    ka "*moan*"
                                    $ renpy.transition(dissolve)
                                    hide kag4bl3
                                    show kag4bl2
                                    p "Did you???"
                                    $ renpy.transition(dissolve)
                                    hide kag4bl2
                                    show kag4bl1
                                    p "Nevermind... Time to fuck your pussy..."
                                    $ renpy.transition(dissolve)
                                    hide kag4bl1
                                    show kag4p1
                                    ka "..."
                                    $ renpy.transition(dissolve)
                                    hide kag4p1
                                    show kag4p2
                                    hide kag4ok
                                    show kag4cl
                                    ka "ah...*moan*"
                                    $ renpy.transition(dissolve)
                                    hide kag4p2
                                    show kag4p3
                                    p "So you re reacting even if time is stopped."
                                    $ renpy.transition(dissolve)
                                    hide kag4p3
                                    show kag4p4
                                    ka "*moaning*"
                                    $ renpy.transition(dissolve)
                                    hide kag4p4
                                    show kag4p3
                                    p "Hmmm... I want more... Kage bunshin no jutsu!"
                                    $ renpy.transition(dissolve)
                                    hide kag4p3
                                    show kag4p2
                                    show kag4bl1
                                    ka "mhfff....*moan*"
                                    $ renpy.transition(dissolve)
                                    hide kag4p2
                                    show kag4p3
                                    hide kag4cl
                                    show kag4sad
                                    hide kag4bl1
                                    show kag4bl2
                                    p "Yeah..."
                                    $ renpy.transition(dissolve)
                                    hide kag4p3
                                    show kag4p4
                                    hide kag4bl2
                                    show kag4bl3
                                    ka "Ahhmmm...*gag moan*"
                                    $ renpy.transition(dissolve)
                                    hide kag4p4
                                    show kag4p3
                                    hide kag4bl3
                                    show kag4bl2
                                    p "It is good right???"
                                    $ renpy.transition(dissolve)
                                    hide kag4p3
                                    show kag4p2
                                    hide kag4bl2
                                    show kag4bl1
                                    ka "mhfff....*moan*"
                                    $ renpy.transition(dissolve)
                                    hide kag4p2
                                    show kag4p3
                                    hide kag4bl1
                                    show kag4bl2
                                    p "Exactly... Maybe this will make you react more. Third clone with whip for extra fun..."
                                    "*slash*" with hpunch
                                    $ renpy.transition(dissolve)
                                    hide kag4p3
                                    show kag4p4
                                    hide kag4sad
                                    show kag4shock
                                    hide kag4bl2
                                    show kag4bl3
                                    show kag4sl1
                                    ka "Ghhhh!!! *moan gag pain*"
                                    "*slash*" with hpunch
                                    $ renpy.transition(dissolve)
                                    hide kag4p4
                                    show kag4p3
                                    hide kag4bl3
                                    show kag4bl2
                                    show kag4sl2
                                    p "Yeah!!!"
                                    p "You are really squeezing your pussy!!!"
                                    "*slash*" with hpunch
                                    $ renpy.transition(dissolve)
                                    hide kag4p3
                                    show kag4p2
                                    hide kag4shock
                                    show kag4org
                                    hide kag4bl2
                                    show kag4bl1
                                    show kag4sl3
                                    p "I will..."
                                    $ renpy.transition(dissolve)
                                    hide kag4p2
                                    show kag4p3
                                    hide kag4bl1
                                    show kag4bl2
                                    p "Yeah!!!! *splurt*"
                                    $ renpy.transition(dissolve)
                                    hide kag4p3
                                    show kag4p4
                                    show kag4p5
                                    hide kag4bl2
                                    show kag4bl3
                                    ka "*heavy moaning*"
                                    $ renpy.transition(dissolve)
                                    show kag4p6
                                    hide kag4bl3
                                    show kag4bl2
                                    p "Shit.... *splurt*"
                                    $ renpy.transition(dissolve)
                                    hide kag4bl2
                                    show kag4bl3
                                    show kag4bl4
                                    p "My sperm is coming from your nose!"
                                    $ renpy.transition(dissolve)
                                    show kag4bl5
                                    ka "*moan gag*"
                                    $ renpy.transition(dissolve)
                                    show kag4bl6
                                    p "Nice....*drip*"
                                    ka "*moan gag cough*"
                                    p "I maybe didn't stop them completely, but it was really funny."
                                    ka "chrgghg.... *lick gag cough*"
                                    p "Yeah... Lick it!!!"
                                    ka "*lick gag cough*"
                                    $ renpy.transition(dissolve)
                                    show kag4p1
                                    p "Looks like a third clone want to cum too..."
                                    $ renpy.transition(dissolve)
                                    show kag4p7
                                    p "Nice...*drip*"
                                    $ renpy.transition(dissolve)
                                    show kag4p8
                                    p "You are finally covered with sperm."
                                    ka "*moan cough*"
                                    p "Yeah,  I know... Time to clean you...."
                                    scene black with circleirisin
                                    "You clean Kaguya and cancel the Namigan... She was probably not know what happened to her."
                                    $ day = day + 1
                                    show drock0 with circleirisout
                                    jump drock

                                "Boob expansion":
                                    if expscroll ==0:
                                        p "I need expansion scroll for that."
                                        jump kagunamifuck
                                    else:
                                        $ renpy.transition(dissolve)
                                        p "I want to see really big boobs..."
                                        $ renpy.transition(dissolve)
                                        hide kagg1
                                        hide kaggok
                                        p "First I need to take off your clothes and then..."
                                        $ renpy.transition(dissolve)
                                        show kag1a
                                        show kag1ok
                                        p "OK... Expansion scroll activated!"
                                        $ renpy.transition(dissolve)
                                        hide kag1a
                                        hide kag1ok
                                        show kag1b
                                        show kag1ok
                                        ka "...."
                                        p "Nice.... It is definetly better right now."
                                        p "Or should I try to make them bigger?"
                                        menu:
                                            "Yes":
                                                p "Expansion scroll second level!"
                                                $ renpy.transition(dissolve)
                                                hide kag1b
                                                hide kag1ok
                                                show kag1c
                                                show kag1op
                                                ka "Ahhh...*moan*"
                                                p "This is even better! Time to fuck you!"

                                            "No":
                                                p "Mehh... I just fuck her..."
                                        $ renpy.transition(dissolve)
                                        show kag1p1
                                        ka "..."
                                        $ renpy.transition(dissolve)
                                        hide kag1p1
                                        show kag1p2
                                        p "Hehe...It is good, but something is missing."
                                        $ renpy.transition(dissolve)
                                        hide kag1p2
                                        show kag1p3
                                        p " Kage bunshin no jutsu! *puff*"
                                        $ renpy.transition(dissolve)
                                        hide kag1p2
                                        show kag1p3
                                        show kag1a1
                                        hide kag1ok
                                        hide kag1op
                                        show kag1clop
                                        show kag1bl1
                                        ka "mhhhmmmmm... *moan*"
                                        p "Hehe...."
                                        $ renpy.transition(dissolve)
                                        hide kag1p2
                                        show kag1p3
                                        hide kag1a1
                                        show kag1a2
                                        hide kag1bl1
                                        show kag1bl2
                                        ka "Right in my ass..."
                                        $ renpy.transition(dissolve)
                                        hide kag1p3
                                        show kag1p4
                                        hide kag1a2
                                        show kag1a3
                                        hide kag1clop
                                        show kag1op
                                        hide kag1bl2
                                        show kag1bl3
                                        ka "hmmmm.... *moan gag*"
                                        $ renpy.transition(dissolve)
                                        hide kag1p4
                                        show kag1p3
                                        hide kag1a3
                                        show kag1a4
                                        hide kag1bl3
                                        show kag1bl4
                                        p "Take this!"
                                        $ renpy.transition(dissolve)
                                        hide kag1p3
                                        show kag1p2
                                        hide kag1a4
                                        show kag1a3
                                        hide kag1bl4
                                        show kag1bl3
                                        ka "*moan gag*"
                                        $ renpy.transition(dissolve)
                                        hide kag1p2
                                        show kag1p3
                                        hide kag1a3
                                        show kag1a2
                                        hide kag1clop
                                        show kag1op
                                        hide kag1bl3
                                        show kag1bl2
                                        p "Yeah... Just like that..."
                                        p "Hmmm pen...."
                                        menu:
                                            "Use it":
                                                p "Wait a moment..."
                                                $ renpy.transition(dissolve)
                                                show kag1text
                                                p "Nice..."
                                            "Nah":
                                                p "I just fuck her..."
                                        $ renpy.transition(dissolve)
                                        hide kag1p3
                                        show kag1p4
                                        hide kag1a2
                                        show kag1a3
                                        hide kag1bl2
                                        show kag1bl3
                                        ka "Mgmhmhgmhm...*gag cough choke*"
                                        p "Yeah...."
                                        $ renpy.transition(dissolve)
                                        hide kag1p4
                                        show kag1p3
                                        hide kag1a3
                                        show kag1a4
                                        hide kag1bl3
                                        show kag1bl4
                                        p "Awesome!!!"
                                        $ renpy.transition(dissolve)
                                        hide kag1p3
                                        show kag1p2
                                        hide kag1a4
                                        show kag1a3
                                        hide kag1bl4
                                        show kag1bl3
                                        ka "gegrg....*cough choke*"
                                        $ renpy.transition(dissolve)
                                        hide kag1p2
                                        show kag1p3
                                        hide kag1a3
                                        show kag1a2
                                        hide kag1bl3
                                        show kag1bl2
                                        p "Just... *splurt*"
                                        $ renpy.transition(dissolve)
                                        hide kag1p3
                                        show kag1p4
                                        show kag1p5
                                        hide kag1a2
                                        show kag1a3
                                        hide kag1op
                                        show kag1clop
                                        hide kag1bl2
                                        show kag1bl3
                                        ka "*moan choke*"
                                        $ renpy.transition(dissolve)
                                        show kag1p6
                                        hide kag1a3
                                        show kag1a2
                                        hide kag1bl3
                                        show kag1bl4
                                        p "You are awesome! *splurt*"
                                        $ renpy.transition(dissolve)
                                        hide kag1a2
                                        show kag1a1
                                        show kag1a7
                                        hide kag1bl4
                                        show kag1bl3
                                        ka "Ahmmm...*moan gag cough*"
                                        $ renpy.transition(dissolve)
                                        show kag1a8
                                        hide kag1bl3
                                        show kag1bl4
                                        p "Fuck!!!*splurt*"
                                        $ renpy.transition(dissolve)
                                        show kag1bl5
                                        ka "*choke gag cough*"
                                        $ renpy.transition(dissolve)
                                        show kag1bl6
                                        p "YEAH!!!"
                                        p "That was awesome!"
                                        ka "*gag cough*"
                                        p "Hehe..."
                                        $ renpy.transition(dissolve)
                                        hide kag1bl6
                                        hide kag1bl5
                                        hide kag1bl4
                                        hide kag1a1
                                        hide kag1a7
                                        hide kag1a8
                                        hide kag1p4
                                        hide kag1p4
                                        hide kag1p5
                                        hide kag1p6
                                        hide kag1clop
                                        hide kag1a
                                        hide kag1text
                                        hide kag1b
                                        hide kag1c
                                        p "Expansion KAI!"
                                        $ renpy.transition(dissolve)
                                        show kagg2
                                        show kaggsad
                                        show kaggsp1
                                        show kaggsp2
                                        ka "*moan*"
                                        p "Still nothing?"
                                        ka "*moan*"
                                        p "Clean yourself now!"
                                        $ renpy.transition(dissolve)
                                        hide kaggsp1
                                        hide kaggsp2
                                        p "And dress yourself..."
                                        $ renpy.transition(dissolve)
                                        hide kagg2
                                        show kagg1
                                        hide kaggsad
                                        show kaggsad
                                        p "NAMIGAN KAI!!!"
                                        $ renpy.transition(dissolve)
                                        hide kaggsad
                                        show kaggok
                                        ka "..."
                                        p "Are you with me?"
                                        ka "Huh??? What is going on?"
                                        p "I use Namigan on you..."
                                        ka "Hmmm so that feelings... That pressure and taste..."
                                        p "Ehm.... Side effects???"
                                        $ renpy.transition(dissolve)
                                        hide kaggok
                                        show kagghap
                                        ka "Sure Side effects... I hope you enjoyed them."
                                        p "Yeah...."
                                        ka "Next time we can try that side effects without using Namigan."
                                        p "Ehm.... I need to go home.... Bye..."
                                        ka "Bye..."
                                        scene black with circleirisin
                                        p "That was close, I think she knows something."
                                        $ day = day + 1
                                        show drock0 with circleirisout
                                        jump drock

                                "Something special":
                                    if kagumission <= 8:
                                        "I seriously have no clue what you want to do with this option."
                                        "Try to complete Kaguya story."
                                        jump kagunamifuck
                                    else:
                                        "This option will help you create your own harem."
                                        "It will be in the next version."
                                        jump kagunamifuck


                    "Nothing":
                        scene black with circleirisin
                        show nrock0 with circleirisout
                        jump nrock

            scene black with circleirisin
            show drock0 with circleirisout
            jump drock

        "Go to map":
            scene black with circleirisin
            show nrock0 with circleirisout
            jump nrock

# DAY %(p)s                      ROCK VILLAGE

label nharem:

    scene nharem0

    $ select = renpy.imagemap("nharem0.jpg", "nharem1.jpg", [
                                               (815, 860, 1080, 955, "gaten"),
                                               (480, 100, 810, 210, "shrinen"),
                                               (780, 415, 1165, 525, "centrumn"),
                                               (230, 420, 540, 520, "villagen"),
                                               (1330, 215, 1650, 320, "forestn"),
                                               (430, 630, 480, 670, "hcheat"),
                                               ])
    if select == "gaten":
        menu:
            "Возвращение в Коноху":
                "Вы покидаете деревню."
                scene black with circleirisin
                scene black with circleirisin
                "После дня путешествий вы приезжаете в Коноху."
                $ day = day + 1
                show droom with circleirisout
                jump nday

            "Перейти в скрытую  деревню камня":
                scene black with circleirisin
                show drock0 with circleirisout
                jump drock

            "Работа":
                "Сейчас делать нечего."
                jump nharem

            "Спать":
                "Тебе нужно немного отдохнуть."
                $ day = day + 1
                scene black with circleirisin
                show dharem0 with circleirisout
                jump dharem

            "Перейти к карте":
                scene black with circleirisin
                show nharem0 with circleirisout
                jump nharem

    if select == "shrinen":
        jump nharemshrine1


    if select == "centrumn":
        scene black with circleirisin
        show nharemtown with circleirisout
        jump nharemtown1


    if select == "villagen":
        scene black with circleirisin
        show nharemvillage with circleirisout
        jump nharemvillage1


    if select == "forestn":
        scene black with circleirisin
        show nharemforest with circleirisout
        jump nharemforest1


################################ hcheat
################################ hcheat
################################ hcheat
################################ hcheat
################################ hcheat

    if select == "hcheat":
        if cheatx >=10:
            menu cheat33:
                "Taijutsu +10":
                    $ taijutsu = taijutsu + 10
                    jump cheat33
                "Genjutsu +10":
                    $ genjutsu = genjutsu + 10
                    jump cheat33
                "Ninjutsu +10":
                    $ ninjutsu = ninjutsu + 10
                    jump cheat33
                "Namigan +10":
                    $ eyes = eyes + 10
                    jump cheat33
                "Chakra + 10":
                    $ chakra = chakra + 10
                    jump cheat33
                "Ryo + 10000":
                    $ ryo = ryo + 10000
                    jump cheat33
                "Add girl to your harem":
                    "This is dangerous option and can break some important part of story."
                    menu:
                        "Sarada": # in harem
                            $ saradastats = 29
                            $ saradaeyes = 23
                            jump cheat33

                        "Himawari": # in harem
                            $ hinami = 11
                            jump cheat33

                        "Hanabi": # in harem
                            $ hanabislave = 8
                            jump cheat33

                        "Tsunade": # in harem
                            $ tsumission = 17
                            jump cheat33

                        "Chocho": # in harem
                            $ chochostats = 20
                            jump cheat33

                        "Sakura": # in harem
                            $ sakuraslave = 20
                            jump cheat33

                        "Ino": # in harem
                            $ inoslave = 20
                            jump cheat33

                        "Samui": # in harem
                            $ samuimission = 16
                            jump cheat33

                        "Mei": # in harem
                            $ meimission = 11
                            $ meipick = 13
                            $ meilove = 10
                            jump cheat33
                        "Hinata": # in harem
                            $ hinatamission = 15
                            $ hinatalove = 14
                            $ hinataslave = 13
                            jump cheat33

                        "Temari":# in harem
                            $ temamission = 12
                            jump cheat33

                        "Tenten":# in harem
                            $ tenslave = 5
                            jump cheat33

                        "Main story":
                            $ missionsa = 6
                            "You complete some main mission. Now is time to face Himawari."
                            jump cheat33


                "Nothing":
                    jump nharem
        else:
            $ cheatx = cheatx +1
            jump nharem

################################ nharemshrine1
################################ nharemshrine1
################################ nharemshrine1
################################ nharemshrine1
################################ nharemshrine1


label nharemshrine1:
    menu:
        "Look around":
            "You feel a weird chakra from this shrine..."
            "You have no clues what kind of chakra it is..."
            scene black with circleirisin
            show nharem0 with circleirisout
            jump nharem


        "Go back to the map":
            scene black with circleirisin
            show nharem0 with circleirisout
            jump nharem

################################ nharemtown1
################################ nharemtown1
################################ nharemtown1
################################ nharemtown1
################################ nharemtown1

label nharemtown1 :
    menu:
        "Explore the town":
            "This town looks too calm..."
            "I am not sure if there are any conflicts that you can solve."
            scene black with circleirisin
            show nharem0 with circleirisout
            jump nharem
###SAMUISAMUISAMUI
        "Find Samui":
            if samuimission >= 16:
                $ renpy.transition(dissolve)
                show samuib
                show samuinok
                p "Now is time to have some fun!"
                menu:
                            "Body play":
                                p "I want to play a little game with you."
                                sam "What kind of game?"
                                menu:

                                    "Use whip":
                                        if whip ==1:
                                            p "I have something for you."
                                            sam "..."
                                            "*slash*" with hpunch
                                            hide samuinok
                                            show samuiclop
                                            show samuis1
                                            sam "Argg!!!"
                                            "*slash*" with hpunch
                                            sam "Yesss... More!!!"
                                            p "I know you are pervert!"
                                            p "I want to play!!!"
                                            "*SLASH*" with hpunch
                                            sam "...."
                                            p "No reaction? What If I hit you faster?"
                                            "*Whip*" with hpunch
                                            show samuis2
                                            sam "....."
                                            p "Nothing???"
                                            hide samuiclop
                                            show samuinok
                                            sam "*moan*"
                                            "*SLASH*" with hpunch
                                            sam "Yessss!!!!*scream*"
                                            p "This is fun! Water explosion!"
                                            $ renpy.transition(dissolve)
                                            show samuiw1
                                            sam "*moan*"
                                            "*SLASH*" with hpunch
                                            show samuis2
                                            sam "Argg!!!*scream*"
                                            p "Silence!"
                                            p "Water dragon!"
                                            $ renpy.transition(dissolve)
                                            show samuiw2
                                            sam "So cold...."
                                            "*SLASH*" with hpunch
                                            sam "Arggg!!!!"
                                            "Water pipe!"
                                            $ renpy.transition(dissolve)
                                            show samuiw3
                                            sam "Yeah! * moan * .... more...."
                                            p "Take it all! *slash*" with hpunch
                                            sam "YEssssssss*heavy moaning*"
                                            $ renpy.transition(dissolve)
                                            hide samuinok
                                            show samuiclop
                                            sam "*moan*"
                                            p "hehe..."
                                            sam "...."
                                            $ renpy.transition(dissolve)
                                            hide samuiclop
                                            show samuinop
                                            sam "ach...."
                                            p "I am tired...."
                                            $ renpy.transition(dissolve)
                                            hide samuinop
                                            show samuinok
                                            sam "......"
                                            p "I will fuck you tomorrow... Now I want some rest."
                                            $ day = day + 1
                                            scene black with circleirisin
                                            show dharem0 with circleirisout
                                            jump dharem


                                        else:
                                            "Buy some clips first."
                                            scene black with circleirisin
                                            show dharem0 with circleirisout
                                            jump dharem


                                    "Send her out":
                                        p "You should go out and meet some new guys."
                                        sam "Sure master..."
                                        p "Good..."
                                        sam "...."
                                        $ renpy.transition(dissolve)
                                        hide samuib
                                        hide samuihap
                                        hide samuinok
                                        p "Bye..."
                                        with fade
                                        p "I will wait for her."
                                        with fade
                                        p "I wonder what she is doing now."
                                        with fade
                                        p "Booring...."
                                        with fade
                                        p "Huh?"
                                        $ randomnum = renpy.random.randint(1,3) # (randomize between 1 and 3)
                                        if randomnum==1:
                                            $ renpy.transition(dissolve)
                                            show samuic
                                            show samuinok
                                            show samuitext1
                                            show samuitext2
                                            show samuisp2
                                        if randomnum==2:
                                            $ renpy.transition(dissolve)
                                            show samuic
                                            show samuinop
                                            show samuitext1
                                            show samuisp2
                                        if randomnum==3:
                                            $ renpy.transition(dissolve)
                                            show samuic
                                            show samuinsmile
                                            show samuitext2
                                            show samuisp2
                                        sam "...."
                                        p "What the fuck has happened to you?"
                                        sam "..."
                                        p "Busy night, huh?"
                                        sam "..."
                                        p "Who cares... Next time I will fuck you!!!"
                                        $ day = day + 1
                                        scene black with circleirisin
                                        show dharem0 with circleirisout
                                        jump dharem


                            "Masturbate":
                                        p "Maturbate for me!"
                                        $ renpy.transition(dissolve)
                                        hide samuib
                                        hide samuinok
                                        show samui2b
                                        show samui2nsmile
                                        sam "...."
                                        p "Ok now tease your pussy more!"
                                        sam "...*moan*"
                                        p "And grab your boob!"
                                        $ renpy.transition(dissolve)
                                        hide samui2a
                                        show samui2b
                                        hide samui2nsmile
                                        show samui2nok
                                        sam "Mmmm...."
                                        p "Yes this is nice!"
                                        p "Just continue...."
                                        $ renpy.transition(dissolve)
                                        hide samui2b
                                        show samui2a
                                        hide samui2nok
                                        show samui2nok
                                        sam "...."
                                        p "Hehe..."
                                        $ renpy.transition(dissolve)
                                        hide samui2a
                                        show samui2b
                                        hide samui2nok
                                        show samui2nok
                                        sam "Mmmmmmggg...*moan*"
                                        $ renpy.transition(dissolve)
                                        hide samui2b
                                        show samui2a
                                        hide samui2nok
                                        show samui2nok
                                        p "Continue..."
                                        $ renpy.transition(dissolve)
                                        hide samui2a
                                        show samui2b
                                        hide samui2nok
                                        show samui2nsmile
                                        p "Maybe you need some help."
                                        $ renpy.transition(dissolve)
                                        hide samui2b
                                        show samui2a
                                        hide samui2nsmile
                                        show samui2nsmile
                                        show samui2p1
                                        sam "...."
                                        $ renpy.transition(dissolve)
                                        hide samui2a
                                        show samui2b
                                        hide samui2nsmile
                                        show samui2nsmile
                                        p "Kege bunshin no jutsu!"
                                        $ renpy.transition(dissolve)
                                        hide samui2b
                                        show samui2a
                                        hide samui2nsmile
                                        show samui2nok
                                        show samui2p2
                                        sam "Mmmmm...*moan*"
                                        $ renpy.transition(dissolve)
                                        hide samui2a
                                        show samui2b
                                        hide samui2nok
                                        show samui2nok
                                        p "Yeah...*fap fap*"
                                        $ renpy.transition(dissolve)
                                        hide samui2b
                                        show samui2a
                                        hide samui2nok
                                        show samui2nok
                                        p "Just grab that big boos harder...*fap fap*"
                                        $ renpy.transition(dissolve)
                                        hide samui2a
                                        show samui2b
                                        hide samui2nok
                                        show samui2nok
                                        p "Do you want my cum? *fap fap*"
                                        $ renpy.transition(dissolve)
                                        hide samui2b
                                        show samui2a
                                        hide samui2nok
                                        show samui2nop
                                        p "I think that mean yes. *fap fap*"
                                        $ renpy.transition(dissolve)
                                        hide samui2a
                                        show samui2b
                                        hide samui2nop
                                        show samui2nop
                                        p "Inocming! *splurt*"
                                        $ renpy.transition(dissolve)
                                        show samui2sp1
                                        sam "Mmmmm...*moan*"
                                        p "And more!"
                                        $ renpy.transition(dissolve)
                                        show samui2sp2
                                        hide samui2nop
                                        show samui2clop
                                        p "Fuck!!!!"
                                        sam "Please!"
                                        p "YEAH! *splurt*"with hpunch
                                        $ renpy.transition(dissolve)
                                        show samui2sp3
                                        sam "...."
                                        $ renpy.transition(dissolve)
                                        hide samui2clop
                                        show samui2nop
                                        p "hehe... Looks like she still want more...*puff*"
                                        $ renpy.transition(dissolve)
                                        hide samui2p2
                                        hide samui2p1
                                        p "But this is my limit...."
                                        p "Maybe I can break this record next time..."
                                        $ day = day + 1
                                        scene black with circleirisin
                                        show dharem0 with circleirisout
                                        jump dharem

                            "From behind":

                                    p "Take off your dress and lay down on four."
                                    $ renpy.transition(dissolve)
                                    hide samuib
                                    hide samuinok
                                    show samui3a
                                    show samui3nok
                                    p "Time for next step."
                                    menu:
                                        "Titfuck":
                                            p "Maybe I should just..."
                                            $ renpy.transition(dissolve)
                                            show samui3tf1
                                            p "Fuck you big boobs..."
                                            $ renpy.transition(dissolve)
                                            hide samui3tf1
                                            show samui3tf2
                                            p "Nice..."
                                            $ renpy.transition(dissolve)
                                            hide samui3tf2
                                            show samui3tf3
                                            sam "...."
                                            $ renpy.transition(dissolve)
                                            hide samui3tf3
                                            show samui3tf4
                                            hide samui3nok
                                            show samui3ndow
                                            p "Maybe if I use this..."
                                            $ renpy.transition(dissolve)
                                            hide samui3tf4
                                            show samui3tf3
                                            p "Water explosion!"
                                            $ renpy.transition(dissolve)
                                            hide samui3tf3
                                            show samui3tf2
                                            show samui3w1
                                            sam "mmmm..."
                                            $ renpy.transition(dissolve)
                                            hide samui3tf2
                                            show samui3tf3
                                            hide samui3ndow
                                            show samui3nback
                                            p "More!!! Waterfall!"
                                            $ renpy.transition(dissolve)
                                            hide samui3tf3
                                            show samui3tf4
                                            show samui3w2
                                            sam "....*mumble*"
                                            $ renpy.transition(dissolve)
                                            hide samui3tf4
                                            show samui3tf3
                                            p "Yeah!"
                                            $ renpy.transition(dissolve)
                                            hide samui3tf3
                                            show samui3tf2
                                            p "Water dragoon!"
                                            $ renpy.transition(dissolve)
                                            hide samui3tf2
                                            show samui3tf3
                                            hide samui3nback
                                            show samui3clop
                                            show samui3w3
                                            sam "!!!*moan*"
                                            $ renpy.transition(dissolve)
                                            hide samui3tf3
                                            show samui3tf4
                                            p "Yeah!!!"
                                            $ renpy.transition(dissolve)
                                            hide samui3tf4
                                            show samui3tf3
                                            sam "....*mumble*"
                                            p "!!!!*splurt*"
                                            $ renpy.transition(dissolve)
                                            hide samui3tf3
                                            show samui3tf4
                                            show samui3tsp1
                                            sam "mmmmm....*drip*"
                                            $ renpy.transition(dissolve)
                                            show samui3tsp2
                                            p "Hehe... Amazing..."
                                            sam "....*moan*"
                                            p "Another day, another amazing sex."
                                            $ day = day + 1
                                            scene black with circleirisin
                                            show dharem0 with circleirisout
                                            jump dharem


                                        "From behind":
                                            p "I want to fuck you."
                                            $ renpy.transition(dissolve)
                                            show samui3p1
                                            p "No objections? Ok?"
                                            $ renpy.transition(dissolve)
                                            hide samui3p1
                                            show samui3p2
                                            hide samui3nok
                                            show samui3nback
                                            p "And deeper!"
                                            $ renpy.transition(dissolve)
                                            hide samui3a
                                            show samui3b
                                            hide samui3p2
                                            show samui3p3
                                            hide samui3nback
                                            show samui3nback
                                            sam "Mmmmm....*moan*"
                                            $ renpy.transition(dissolve)
                                            hide samui3b
                                            show samui3a
                                            hide samui3p3
                                            show samui3p4
                                            hide samui3nback
                                            show samui3nback
                                            p "Bounceing boobies."
                                            $ renpy.transition(dissolve)
                                            hide samui3a
                                            show samui3b
                                            hide samui3p4
                                            show samui3p3
                                            hide samui3nback
                                            show samui3nop
                                            sam "*moan*"
                                            $ renpy.transition(dissolve)
                                            hide samui3b
                                            show samui3a
                                            hide samui3p3
                                            show samui3p2
                                            hide samui3nop
                                            show samui3nop
                                            p "...."
                                            $ renpy.transition(dissolve)
                                            hide samui3a
                                            show samui3b
                                            hide samui3p2
                                            show samui3p3
                                            hide samui3nop
                                            show samui3nop
                                            sam "Mmmmmm... *moan*"
                                            $ renpy.transition(dissolve)
                                            hide samui3b
                                            show samui3a
                                            hide samui3p3
                                            show samui3p4
                                            hide samui3nop
                                            show samui3nop
                                            p "Feels so good..."
                                            $ renpy.transition(dissolve)
                                            hide samui3a
                                            show samui3b
                                            hide samui3p4
                                            show samui3p3
                                            hide samui3nop
                                            show samui3nop
                                            p "I want to cum..."
                                            menu:
                                                "Cum in":
                                                    p "Yes..."
                                                    $ renpy.transition(dissolve)
                                                    hide samui3b
                                                    show samui3a
                                                    hide samui3p3
                                                    show samui3p4
                                                    hide samui3nop
                                                    show samui3norg
                                                    p "FUCK!!! *splurt*"
                                                    $ renpy.transition(dissolve)
                                                    show samui3sp3
                                                    sam "Mmmmm...*drip*"
                                                    $ renpy.transition(dissolve)
                                                    show samui3sp4
                                                    p "Good... Time for releaseing her from namigan..."



                                                "Cum out":
                                                    p "Yes..."
                                                    $ renpy.transition(dissolve)
                                                    hide samui3b
                                                    show samui3a
                                                    hide samui3p3
                                                    show samui3p2
                                                    hide samui3nop
                                                    show samui3norg
                                                    p "FUCK!!! *splurt*"
                                                    $ renpy.transition(dissolve)
                                                    hide samui3p2
                                                    show samui3p1
                                                    show samui3sp1
                                                    sam "Mmmmm...*drip*"
                                                    $ renpy.transition(dissolve)
                                                    show samui3sp2
                                                    p "..."


                                            p "I love busty chicks... Next time I will play more with your boobs."
                                            $ day = day + 1
                                            scene black with circleirisin
                                            show dharem0 with circleirisout
                                            jump dharem

                                        "Kage bunshin no jutsu":
                                            p "Time for something special."
                                            sam "..."
                                            p "Kage bunshin no jutsu."
                                            $ renpy.transition(dissolve)
                                            show samui3p1
                                            show samui3tf1
                                            p "Nice. I am gonna enjoy this..."
                                            $ renpy.transition(dissolve)
                                            hide samui3p1
                                            show samui3p2
                                            hide samui3tf1
                                            show samui3tf2
                                            hide samui3nok
                                            show samui3nback
                                            sam "Mmmmm...*moan*"
                                            $ renpy.transition(dissolve)
                                            hide samui3p2
                                            show samui3p3
                                            hide samui3tf2
                                            show samui3tf3
                                            p "You like it right?"
                                            $ renpy.transition(dissolve)
                                            hide samui3p3
                                            show samui3p4
                                            hide samui3tf3
                                            show samui3tf4
                                            sam "Aaaaahhh...*moan*"
                                            $ renpy.transition(dissolve)
                                            hide samui3p4
                                            show samui3p3
                                            hide samui3tf4
                                            show samui3tf3
                                            p "Yeah!"
                                            $ renpy.transition(dissolve)
                                            hide samui3p3
                                            show samui3p4
                                            hide samui3tf3
                                            show samui3tf2
                                            hide samui3nback
                                            show samui3nop
                                            sam "Mmmmm...*moan*"
                                            $ renpy.transition(dissolve)
                                            hide samui3p4
                                            show samui3p3
                                            hide samui3tf2
                                            show samui3tf3
                                            p "This feels so good..."
                                            $ renpy.transition(dissolve)
                                            hide samui3p3
                                            show samui3p2
                                            hide samui3tf3
                                            show samui3tf4
                                            sam "..."
                                            $ renpy.transition(dissolve)
                                            hide samui3p2
                                            show samui3p3
                                            hide samui3tf4
                                            show samui3tf3
                                            p "!!!"
                                            $ renpy.transition(dissolve)
                                            hide samui3p3
                                            show samui3p2
                                            hide samui3tf3
                                            show samui3tf4
                                            hide samui3nop
                                            show samui3norg
                                            sam "Ahhhh...*heavy moaning*"
                                            $ renpy.transition(dissolve)
                                            hide samui3p2
                                            show samui3p1
                                            hide samui3tf4
                                            show samui3tf3
                                            p "I will...*splurt*"
                                            $ renpy.transition(dissolve)
                                            show samui3sp1
                                            hide samui3tf3
                                            show samui3tf2
                                            sam "Mmmm...*drip*"
                                            $ renpy.transition(dissolve)
                                            show samui3sp2
                                            hide samui3tf2
                                            show samui3tf3
                                            p "Yeah... So good...*puff*"
                                            $ renpy.transition(dissolve)
                                            hide samui3p1
                                            hide samui3tf3
                                            show samui3tf4
                                            p "Hehe funny..."
                                            p "I will come back tomorrow..."
                                            $ day = day + 1
                                            scene black with circleirisin
                                            show dharem0 with circleirisout
                                            jump dharem











                            "Play with boobs":
                                p "I want to fuck your big boobs!"
                                sam "..."
                                $ renpy.transition(dissolve)
                                hide samuib
                                hide samuinok
                                show samui4a
                                show samui4nok
                                sam "What do you want to do now?"
                                menu samuitf31:
                                    "Use jutsu":
                                        p "I just wanted to have some fun with you."
                                        sam "..."
                                        $ renpy.transition(dissolve)
                                        show samui4clips
                                        sam "....."
                                        p "What about this?"
                                        p "Water explosion!*splash*"
                                        $ renpy.transition(dissolve)
                                        show samui4w1
                                        sam "...."
                                        p "I think it's time for some new toys. *clamp*"
                                        $ renpy.transition(dissolve)
                                        show samui4clips
                                        hide samui4nside
                                        show samui4nok
                                        sam "*moan*"
                                        p "Hehe... That is funny..."
                                        p "Water dragon!*splash*"
                                        $ renpy.transition(dissolve)
                                        show samui4w2
                                        sam "....*mumble*"
                                        p "I wonder if she feels anything now."
                                        p "Water orgasm!*splash*"
                                        $ renpy.transition(dissolve)
                                        show samui4w3
                                        hide samui4nok
                                        show samui4cl
                                        sam "....*sigh*"
                                        p "Maybe if I try this..."
                                        p "Lightning style tingling sensation!"
                                        $ renpy.transition(dissolve)
                                        show samui4l1
                                        sam "Mmmmmm... *moan*"
                                        $ renpy.transition(dissolve)
                                        show samui4m1
                                        p "Finally something..."
                                        p "Lightning style full release!"
                                        $ renpy.transition(dissolve)
                                        show samui4l2
                                        show samui4m2
                                        hide samui4cl
                                        show samui4norg
                                        sam "MMmmm... *heavy moaning*"
                                        p "Looks like she finally came!"
                                        sam "Aaaaaa...*moan*"
                                        $ renpy.transition(dissolve)
                                        hide samui4l2
                                        hide samui4m1
                                        p "This combination seems to work well...."
                                        p "But it consumes too much chakra."
                                        sam "...."
                                        $ renpy.transition(dissolve)
                                        hide samui4l1
                                        p "I need to recover my powers... Just take this out."
                                        $ renpy.transition(dissolve)
                                        hide samui4clips
                                        p "And go home..."
                                        $ day = day + 1
                                        scene black with circleirisin
                                        show dharem0 with circleirisout
                                        jump dharem


                                    "Titfuck":
                                        p "Time to fuck your boobs."
                                        if expscroll ==0:
                                            p "Need to buy an expansion scroll for that."
                                            jump samuitf31
                                        else:
                                            sam "..."
                                            p "But they are too small..."
                                            p "Expansion scroll! First release!"
                                            $ renpy.transition(dissolve)
                                            hide samui4a
                                            show samui4b
                                            hide samui4nok
                                            show samui4ndown
                                            sam "!!!"
                                            p "Better right?"
                                            $ renpy.transition(dissolve)
                                            show samui4tf1
                                            sam "..."
                                            $ renpy.transition(dissolve)
                                            hide samui4tf1
                                            show samui4tf2
                                            hide samui4ndown
                                            show samui4nok
                                            p "Feels so warm..."
                                            $ renpy.transition(dissolve)
                                            hide samui4tf2
                                            show samui4tf3
                                            sam "Yeah...."
                                            $ renpy.transition(dissolve)
                                            hide samui4tf3
                                            show samui4tf4
                                            p "See? This is what I am talking about."
                                            $ renpy.transition(dissolve)
                                            hide samui4nok
                                            show samui4ndown
                                            hide samui4tf4
                                            show samui4tf3
                                            sam "??? *moan*"
                                            $ renpy.transition(dissolve)
                                            hide samui4tf3
                                            show samui4tf2
                                            p "If your boobs was smaller, my penis will just pull out on the top."
                                            $ renpy.transition(dissolve)
                                            hide samui4tf2
                                            show samui4tf3
                                            hide samui4ndown
                                            show samui4nside
                                            sam "......"
                                            $ renpy.transition(dissolve)
                                            hide samui4tf3
                                            show samui4tf4
                                            p "So good..."
                                            $ renpy.transition(dissolve)
                                            hide samui4tf3
                                            show samui4tf4
                                            sam "Mmmmm..."
                                            $ renpy.transition(dissolve)
                                            hide samui4tf3
                                            show samui4tf4
                                            p "Fuck this is!!! *splurt*"
                                            $ renpy.transition(dissolve)
                                            show samui4tfsp1
                                            hide samui4nside
                                            show samui4cl
                                            sam "*drip*"
                                            $ renpy.transition(dissolve)
                                            show samui4tfsp2
                                            sam "*drip*"
                                            p "Huh???"
                                            p "We should cancel this jutsu now...KAI!"
                                            $ renpy.transition(dissolve)
                                            hide samui4tfsp2
                                            hide samui4tfsp1
                                            hide samui4tf4
                                            hide samui4b
                                            hide samui4nside
                                            hide samui4cl
                                            sam "..."
                                            $ renpy.transition(dissolve)
                                            show samuic
                                            show samuinok
                                            p "That was fun... See you later."
                                            sam "....."
                                            $ day = day + 1
                                            scene black with circleirisin
                                            show dharem0 with circleirisout
                                            jump dharem



                                    "Nipple fuck":
                                        p "I want to fuck your nipples."
                                        if expscroll ==0:
                                            p "Need to buy an expansion scroll for that."
                                            jump samuitf31

                                        else:
                                            sam "What?"
                                            if slipscroll == 0:
                                                p "Do not worry. I need a slippery scroll for that... Maybe later..."
                                                jump samuitf31
                                            else:
                                                p "It will be great fun."
                                                sam "..."
                                                p "OK. I will start with this first..."
                                                p "Expansion scroll! First release!"
                                                $ renpy.transition(dissolve)
                                                hide samui4a
                                                show samui4b
                                                hide samui4nside
                                                show samui4cl
                                                sam "*moan*"
                                                p "They need to be a little bigger."
                                                sam "..."
                                                p "Expansion scroll! Second release!"
                                                $ renpy.transition(dissolve)
                                                hide samui4b
                                                show samui4c
                                                hide samui4cl
                                                show samui4nok
                                                sam "*moan*"
                                                p "Yes... I like it more and more..."
                                                p "Time to test it..."
                                                $ renpy.transition(dissolve)
                                                show samui4nr0
                                                p "Just push!!!"
                                                $ renpy.transition(dissolve)
                                                hide samui4nok
                                                show samui4clop
                                                sam "Arggg!!!"
                                                p "Hehe...I know. Sliperly scroll activation!"
                                                $ renpy.transition(dissolve)
                                                hide samui4nr0
                                                show samui4nr1
                                                hide samui4clop
                                                show samui4nside
                                                sam "*moan*"
                                                p "Yeah!"
                                                $ renpy.transition(dissolve)
                                                hide samui4nr1
                                                show samui4nr2
                                                sam "..."
                                                $ renpy.transition(dissolve)
                                                hide samui4nr2
                                                show samui4nr1
                                                p "Yeah...."
                                                $ renpy.transition(dissolve)
                                                hide samui4nr1
                                                show samui4nr2
                                                p "Kage bunshin no jutsu!"
                                                $ renpy.transition(dissolve)
                                                hide samui4nr2
                                                show samui4nr1
                                                show samui4nl0
                                                hide samui4nside
                                                show samui4clop
                                                sam "*moan*"
                                                p "..."
                                                $ renpy.transition(dissolve)
                                                hide samui4nr1
                                                show samui4nr2
                                                hide samui4nl0
                                                show samui4nl1
                                                sam "Arggg!!!! *heavy moaning!!!*"
                                                $ renpy.transition(dissolve)
                                                hide samui4nr2
                                                show samui4nr1
                                                hide samui4nl1
                                                show samui4nl2
                                                sam "!!! *heavy moaning*"
                                                $ renpy.transition(dissolve)
                                                hide samui4nr1
                                                show samui4nr2
                                                hide samui4nl2
                                                show samui4nl1
                                                hide samui4clop
                                                show samui4norg
                                                p "Fuck! I will!!!"
                                                $ renpy.transition(dissolve)
                                                hide samui4nr2
                                                show samui4nr1
                                                hide samui4nl1
                                                show samui4nl2
                                                p "Great!!!*splurt*"
                                                $ renpy.transition(dissolve)
                                                hide samui4nr1
                                                show samui4nr3
                                                hide samui4nl2
                                                show samui4nl1
                                                sam "*moan*"
                                                $ renpy.transition(dissolve)
                                                hide samui4nl1
                                                show samui4nl2
                                                sam "More!!! *drip*"
                                                $ renpy.transition(dissolve)
                                                hide samui4nl2
                                                show samui4nl1
                                                p "YEAH!!! *splurt*"
                                                $ renpy.transition(dissolve)
                                                hide samui4nl1
                                                show samui4nl3
                                                hide samui4norg
                                                show samui4clop
                                                sam "!!!!*drip*"
                                                p "...."
                                                p "Ok... Time to go to the bed..."
                                                $ day = day + 1
                                                scene black with circleirisin
                                                show dharem0 with circleirisout
                                                jump dharem


            else:
                "Samui is not in your harem right now."
                scene black with circleirisin
                show nharem0 with circleirisout
                jump nharem



        "Go back to the map":
            scene black with circleirisin
            show nharem0 with circleirisout
            jump nharem


################################ nharemvillage1
################################ nharemvillage1
################################ nharemvillage1
################################ nharemvillage1
################################ nharemvillage1

label nharemvillage1 :
    menu:
        "Look arround":
            "You find some villagers that talking about you."
            "Many of them think you can save their friends."
            scene black with circleirisin
            show nharem0 with circleirisout
            jump nharem

###### MEIMEIMEI
        "Find Mei":
            if meipick <=12:
                $ renpy.transition(dissolve)
                show meib
                show meinok
                p "Now, give me your chakra."
                $ renpy.transition(dissolve)
                hide meinok
                show meinop
                mei "Mmmmm....*pant*"
                $ chakra = chakra + 1
                p "Wonderful... What now?"
                menu :
                    "Strip her":
                            p "Now, take your clothes off!"
                            mei "Sure..."
                            $ renpy.transition(dissolve)
                            hide meib
                            hide meinop
                            show meic
                            show meinok
                            p "I just love that body..."
                            p "What I should do now??"
                            menu meistrip9:
                                "Lightning style":
                                    if dildo ==0:
                                        "You need to buy dildo first."
                                        "Sorry but you really need one."
                                        jump meistrip9
                                    else:
                                        p "Ok time to try this one."
                                        p "Hold still..*clamp*"
                                        $ renpy.transition(dissolve)
                                        show meid2
                                        hide meinok
                                        show meinang
                                        mei "Arggg!!!"
                                        p "Yes... And one more gift for you..."
                                        $ renpy.transition(dissolve)
                                        show meid1
                                        mei "!!!"
                                        p "Calm down... It will be funny... Just turn it on a little..."
                                        $ renpy.transition(dissolve)
                                        hide meinang
                                        show meinop
                                        p "And... Lightning style!"
                                        $ renpy.transition(dissolve)
                                        show meil0
                                        mei "MMMM....*moan*"
                                        p "Tingling lightning *zap*"
                                        $ renpy.transition(dissolve)
                                        show meil1
                                        mei "!!!"
                                        p "Lightning dragoon! *zap*"
                                        $ renpy.transition(dissolve)
                                        show meil2
                                        hide meinop
                                        show meinorg
                                        mei "Yessss!!! *squirt*"
                                        $ renpy.transition(dissolve)
                                        show meimilk
                                        mei "MMMM*squirt*"
                                        p "Looks like you enjoyed it too much."
                                        mei "Arggggg....*heavy moaning*"
                                        p "That was funny right?"
                                        $ renpy.transition(dissolve)
                                        hide meimilk
                                        hide meil2
                                        hide meil1
                                        show meimilk1
                                        p "Just need to remove all things and clean her."
                                        $ renpy.transition(dissolve)
                                        hide meimilk1
                                        hide meid1
                                        hide meid2
                                        hide meinorg
                                        hide meic
                                        hide meil0
                                        p "Ok good...."
                                        $ renpy.transition(dissolve)
                                        show meia
                                        show meinok
                                        mei "..."
                                        p "Time for some rest..."
                                        $ day = day + 1
                                        scene black with circleirisin
                                        show dharem0 with circleirisout
                                        jump dharem

                                "Use whip":
                                    if whip ==0:
                                        "You need to buy whip first."
                                        "Sorry but you really need one."
                                        jump meistrip9
                                    else:
                                        p "What if I do this?"
                                        "*Slash!*" with hpunch
                                        show meisc1
                                        hide meinok
                                        show meiclop
                                        mei "Argg!*pain*"
                                        p "Yeah..."
                                        "*Slash!*" with hpunch
                                        show meisc2
                                        mei "!!!"
                                        p "And one more time!"
                                        "*Slash!*" with hpunch
                                        show meisc3
                                        mei "More!!!"
                                        p "Sure one last time!"
                                        "*Slash!*" with hpunch
                                        show meisc4
                                        hide meiclop
                                        show meinorg
                                        mei "*Heav moaning*"
                                        p "Nice one."
                                        p "But I should end it right here..."
                                        p "Heal yourself first."
                                        $ renpy.transition(dissolve)
                                        hide meimilk1
                                        hide meisc1
                                        hide meisc2
                                        hide meisc3
                                        hide meisc4
                                        hide meinorg
                                        hide meic
                                        p "Good now take on your clothes."
                                        $ renpy.transition(dissolve)
                                        show meia
                                        show meinok
                                        mei "..."
                                        p "That was enough... I will play tomorrow."
                                        $ day = day + 1
                                        scene black with circleirisin
                                        show dharem0 with circleirisout
                                        jump dharem


                                "Kage bunshin":
                                    p "Hmmm... I want to have some fun too..."
                                    p "Ok, you have 2 hands so one clone will be fine."
                                    p "Kage bunshin no jutsu!"
                                    mei "..."
                                    p "You can start now..."
                                    mei "*fap fap*"
                                    p "And open your mouth."
                                    $ renpy.transition(dissolve)
                                    hide meinok
                                    show meinop
                                    p "Yeah... Nice..."
                                    mei "*fap fap fap*"
                                    p "Shit! You are really good at this!"
                                    $ renpy.transition(dissolve)
                                    hide meinop
                                    show meinhappy
                                    mei "*fap fap fap*"
                                    p "And that boobs!"
                                    $ renpy.transition(dissolve)
                                    show meitouch
                                    mei "*fap fap fap fap*"
                                    p "I just... *splurt*"
                                    $ renpy.transition(dissolve)
                                    hide meinhappy
                                    show meinshock
                                    hide meitouch
                                    show meisp1
                                    mei "*fap fap*"
                                    p "And one more time! *splurt*"
                                    $ renpy.transition(dissolve)
                                    show meisp2
                                    p "Amazing!!!! *puff*"
                                    mei "...."
                                    p ".... You should clean yourself...."
                                    $ renpy.transition(dissolve)
                                    hide meisp1
                                    hide meisp2
                                    hide meitouch
                                    hide meinshock
                                    hide meic
                                    p "Now open your mouth and swallow."
                                    mei "*Glog*"
                                    p "Good girl..."
                                    $ renpy.transition(dissolve)
                                    show meia
                                    show meinop
                                    p "I will fuck you hard next time!"
                                    $ day = day + 1
                                    scene black with circleirisin
                                    show dharem0 with circleirisout
                                    jump dharem




                    "Fuck her face to face":
                            p "Take your clothes off and lay down, I want to fuck your pussy."
                            $ renpy.transition(dissolve)
                            hide meib
                            hide meinop
                            show mei2
                            show mei2nok
                            p "Such a good girl. Should I play with a dildo a little?"
                            menu:
                                "Yes":
                                    p "It is a great idea. Maybe something like foreplay to her!"
                                    $ renpy.transition(dissolve)
                                    show mei2d1
                                    hide mei2nok
                                    show mei2nop
                                    mei "*moan*"
                                    p "And turn it on!"
                                    $ renpy.transition(dissolve)
                                    hide mei2d1
                                    show mei2d3
                                    mei "Yesss!!!*pant*"
                                    p "..... "
                                    mei "*moaning*"
                                    p "Hehe... Looks like you are now turned on!"
                                    $ renpy.transition(dissolve)
                                    hide mei2d3
                                    show mei2d1
                                    hide mei2nop
                                    show mei2nok
                                    p "But now is time to fuck you!"
                                    $ renpy.transition(dissolve)
                                    hide mei2d1

                                "No":
                                    p "Maybe later. Now I want to fuck her!"
                            $ renpy.transition(dissolve)
                            show mei2p1
                            mei "...."
                            $ renpy.transition(dissolve)
                            hide mei2p1
                            show mei2p2
                            mei "...."
                            $ renpy.transition(dissolve)
                            hide mei2p2
                            show mei2p3
                            p "Nothing?"
                            $ renpy.transition(dissolve)
                            hide mei2p3
                            show mei2p4
                            hide mei2nop
                            show mei2nok
                            mei "OOooo...*moaning*"
                            p "Finally!"
                            $ renpy.transition(dissolve)
                            hide mei2p4
                            show mei2p3
                            p "It fells good..."
                            $ renpy.transition(dissolve)
                            hide mei2p3
                            show mei2p2
                            mei "*moaning*"
                            $ renpy.transition(dissolve)
                            hide mei2p2
                            show mei2p3
                            p "Yeah..."
                            $ renpy.transition(dissolve)
                            hide mei2p3
                            show mei2p4
                            hide mei2nok
                            show mei2norg
                            show mei2drop
                            p "Fuck I am almost..."
                            menu:
                                "Cum in":
                                    p "I just....*splurt*"
                                    $ renpy.transition(dissolve)
                                    show mei2spi1
                                    mei "*moan squirt*"
                                    $ renpy.transition(dissolve)
                                    show mei2spi2
                                    p "Awesome....."
                                    mei "*moan drip*"
                                    p "And it is easier to hold you under mind control."
                                    p "Now you can clean yourself and get dressed."
                                    $ renpy.transition(dissolve)
                                    hide mei2spi1
                                    hide mei2spi2
                                    hide mei2
                                    hide mei2p4
                                    hide mei2norg
                                    hide mei2drop
                                    p "..."
                                    $ renpy.transition(dissolve)
                                    show meia
                                    show meinok
                                    p "Your pussy is full now... Time to go home."
                                    $ day = day + 1
                                    scene black with circleirisin
                                    show dharem0 with circleirisout
                                    jump dharem

                                "Cum out":
                                    mei"Oooo..*pant*"
                                    $ renpy.transition(dissolve)
                                    hide mei2p4
                                    show mei2p3
                                    p "So close..."
                                    $ renpy.transition(dissolve)
                                    hide mei2p3
                                    show mei2p2
                                    p "I just....*splurt*"
                                    $ renpy.transition(dissolve)
                                    hide mei2p2
                                    show mei2p1
                                    show mei2spo1
                                    mei "....*Heavy breathing*"
                                    $ renpy.transition(dissolve)
                                    show mei2spo2
                                    p "!!!"
                                    mei "*moan drip*"
                                    p "Looks good on you..."
                                    p "You should drink it all..."
                                    $ renpy.transition(dissolve)
                                    hide mei2spo1
                                    mei "*glog*"
                                    p "And get dressed."
                                    $ renpy.transition(dissolve)
                                    hide mei2spo1
                                    hide mei2spo2
                                    hide mei2
                                    hide mei2p1
                                    hide mei2norg
                                    hide mei2drop
                                    p "Yeah, drink it all..."
                                    $ renpy.transition(dissolve)
                                    show meia
                                    show meinok
                                    p "Good girl that was your dinner..."
                                    $ day = day + 1
                                    scene black with circleirisin
                                    show dharem0 with circleirisout
                                    jump dharem



                    "From behind":

                            p "I want to take you from behind.."
                            p "You know what to do from here..."
                            $ renpy.transition(dissolve)
                            hide meib
                            hide meinop
                            show meic
                            show meinok
                            p "Nice... Now show me your ass..."
                            $ renpy.transition(dissolve)
                            hide meic
                            hide meinok
                            show mei1a
                            show mei1nsad
                            p "I just like that position. Time to have some fun..."
                            mei "...."
                            p "I just wonder if your boobs can be bigger..."
                            menu:
                                "Use expansion scroll":
                                    if expscroll == 0:
                                        p "Need to buy an expansion scroll for that."
                                        p "Ok... I just fuck her..."
                                    else:
                                        p "Time to  try it on Mei!"
                                        p "Expansion scroll - activated!"
                                        $ renpy.transition(dissolve)
                                        hide mei1a
                                        hide mei1nsad
                                        show mei1b
                                        show mei1nok
                                        mei "Argg...*pant*"
                                        p "Yes they are bigger now!"
                                        p "But I should try it one more time!"
                                        if meipick ==8:
                                            $ meipick = 9
                                        p "Expansion scroll - 2nd activation!"
                                        $ renpy.transition(dissolve)
                                        hide mei1b
                                        hide mei1nok
                                        show mei1c
                                        show mei1norg
                                        mei "!!!!*pain*"
                                        p "Huh... Not a big change... Maybe it is not so easy in this position."
                                        p "I will try to make them bigger later... Now is time to fuck her..."


                                "Just fuck her":
                                    p "Maybe later... Now is time to... *zip*"

                            $ renpy.transition(dissolve)
                            show mei1p1
                            p "I really want to fuck your ass!"
                            $ renpy.transition(dissolve)
                            hide mei1p1
                            show mei1p2
                            hide mei1norg
                            hide mei1nsad
                            show mei1nop
                            mei "Argg!!! *pain*"
                            p "Yeah... I forgot again."
                            $ renpy.transition(dissolve)
                            hide mei1p2
                            show mei1p1
                            hide mei1nop
                            show mei1clop
                            p "*Spit* This should be better..."
                            $ renpy.transition(dissolve)
                            hide mei1p1
                            show mei1p2
                            hide mei1clop
                            show mei1clok
                            mei "mmm....*moan*"
                            $ renpy.transition(dissolve)
                            hide mei1p2
                            show mei1p3
                            p "Yes, she love it!"
                            $ renpy.transition(dissolve)
                            hide mei1p3
                            show mei1p4
                            hide mei1clok
                            show mei1nsad
                            p "Good..."
                            $ renpy.transition(dissolve)
                            hide mei1p2
                            show mei1p3
                            "*Slap!*" with hpunch
                            $ renpy.transition(dissolve)
                            hide mei1p2
                            show mei1p3
                            hide mei1nsad
                            show mei1nhap
                            show mei1h1
                            p "Yeah... This is hot..."
                            $ renpy.transition(dissolve)
                            hide mei1p3
                            show mei1p4
                            mei "Arrggg....*moan*"
                            $ renpy.transition(dissolve)
                            hide mei1p4
                            show mei1p3
                            p "So.. good!"
                            $ renpy.transition(dissolve)
                            hide mei1p3
                            show mei1p2
                            hide mei1nhap
                            show mei1nop
                            p "..."
                            $ renpy.transition(dissolve)
                            hide mei1p2
                            show mei1p3
                            mei "Oooo...*moan*"
                            menu:
                                "Slap her more":
                                    "*Slap*" with hpunch
                                    $ renpy.transition(dissolve)
                                    hide mei1p3
                                    show mei1p4
                                    show mei1h2
                                    mei "Arggg...*pant*"
                                    $ renpy.transition(dissolve)
                                    hide mei1p4
                                    show mei1p3
                                    "*Slap*" with hpunch
                                    $ renpy.transition(dissolve)
                                    hide mei1p3
                                    show mei1p2
                                    show mei1h3
                                    hide mei1nop
                                    show mei1norg
                                    mei "Ooooo...*pain*"
                                    $ renpy.transition(dissolve)
                                    hide mei1p2
                                    show mei1p3
                                    p "Yeah!*splurt*"
                                    $ renpy.transition(dissolve)
                                    hide mei1p3
                                    show mei1p4
                                    show mei1spi1
                                    mei "!!!"
                                    $ renpy.transition(dissolve)
                                    show mei1spi2
                                    p "Yeah! *drip*"
                                    p "That was pretty fun right?"
                                    $ renpy.transition(dissolve)
                                    hide mei1norg
                                    show mei1nhap
                                    mei "...."
                                    p "You look happy..."
                                    if meipick ==6:
                                        $ meipick = 7
                                    p "But you should clean yourself now..."
                                    mei "...."
                                    $ renpy.transition(dissolve)
                                    hide mei1nhap
                                    hide mei1a
                                    hide mei1c
                                    hide mei1p4
                                    hide mei1spi1
                                    hide mei1spi2
                                    hide mei1h3
                                    hide mei1h2
                                    hide mei1h1
                                    p "...."
                                    $ renpy.transition(dissolve)
                                    show meia
                                    show meinhappy
                                    p "Nice... It looks like you enjoy it right?"
                                    mei "*smile*"
                                    p "Lol just..."
                                    p "Meh... Maybe next time..."
                                    $ day = day + 1
                                    scene black with circleirisin
                                    show dharem0 with circleirisout
                                    jump dharem



                                "Use clone":
                                    p "I want more fun - Shadow clone!"
                                    $ renpy.transition(dissolve)
                                    hide mei1p3
                                    show mei1p4
                                    show mei1p0
                                    mei "mmmm..."
                                    $ renpy.transition(dissolve)
                                    hide mei1p4
                                    show mei1p3
                                    p "Hehe...."
                                    $ renpy.transition(dissolve)
                                    hide mei1p3
                                    show mei1p2
                                    hide mei1nop
                                    show mei1norg
                                    mei "Aaaa...*moaning*"
                                    $ renpy.transition(dissolve)
                                    hide mei1p2
                                    show mei1p3
                                    p "I will cover your body with cum!"
                                    $ renpy.transition(dissolve)
                                    hide mei1p3
                                    show mei1p2
                                    mei "Yesss... Cum.....*moan*"
                                    $ renpy.transition(dissolve)
                                    hide mei1p2
                                    show mei1p1
                                    p "Fuck! *splurt*"
                                    $ renpy.transition(dissolve)
                                    show mei1spo1
                                    mei "mmmm....*moan*"
                                    $ renpy.transition(dissolve)
                                    show mei1spo2
                                    p "Yeah! *drip*"
                                    mei "....."
                                    p "Take it all!!!*splurt*"
                                    $ renpy.transition(dissolve)
                                    show mei1sp1
                                    mei "...."
                                    $ renpy.transition(dissolve)
                                    show mei1sp2
                                    p "...."
                                    $ renpy.transition(dissolve)
                                    hide mei1norg
                                    show mei1nhap
                                    hide mei1sp1
                                    hide mei1sp2
                                    hide mei1spo1
                                    hide mei1spo2
                                    show mei1spo1
                                    show mei1spo2
                                    show mei1sp2
                                    show mei1sp1
                                    mei "So much sperm..."
                                    if meipick ==7:
                                        $ meipick = 8
                                    p "Yeah I heard that before... You can swallow it all.."
                                    mei "....*slurp*"
                                    $ renpy.transition(dissolve)
                                    hide mei1nhap
                                    hide mei1a
                                    hide mei1c
                                    hide mei1p4
                                    hide mei1spo1
                                    hide mei1spo2
                                    hide mei1sp1
                                    hide mei1sp1
                                    hide mei1p1
                                    hide mei1p0
                                    hide mei1sp2
                                    p "Good kage..."
                                    $ renpy.transition(dissolve)
                                    show meia
                                    show meinhappy
                                    p "Nice... You are clean right?"
                                    mei "*smile*"
                                    p "Hope you didn't forget any place of your body... Nah who cares..."
                                    p "See you next time..."
                                    $ day = day + 1
                                    scene black with circleirisin
                                    show dharem0 with circleirisout
                                    jump dharem




                    "Henge no jutsu":
                            p "You know what to do, right?"
                            mei "..."
                            $ renpy.transition(dissolve)
                            hide meib
                            hide meinop
                            show meic
                            show meinok
                            p "Good... Now change yourself a little."
                            mei "....henge no jutsu!..."
                            $ renpy.transition(dissolve)
                            hide meic
                            hide meinok
                            show mei3a
                            show mei3hcl
                            show mei3nop
                            p "You look pretty different now..."
                            mei "...."
                            p "Maybe I can change your appearenc too."
                            menu:
                                "NO change":
                                    p "No... this is fine... I just fuck you."
                                "Medium size":
                                    p "Ok, time for some expansion technique."
                                    p "Expansion scroll - activated!"
                                    $ renpy.transition(dissolve)
                                    hide mei3a
                                    hide mei3hcl
                                    hide mei3nop
                                    show mei3b
                                    show mei3hhap
                                    show mei3nop
                                    mei "Yesssss....*moaning*"
                                    p "Good, One more time!"
                                    p "Expansion scroll - 2nd activation!"
                                    $ renpy.transition(dissolve)
                                    hide mei3b
                                    hide mei3hhap
                                    hide mei3nop
                                    show mei3c
                                    show mei3hhap
                                    show mei3nop
                                    p "Yeah... That is the size I like!"
                                    p "Back to your pussy!"

                                "Extreme size":
                                    p "I wonder how big they can be."
                                    if meipick ==11:
                                        $ meipick =12
                                    p "Expansion scroll - activated!"
                                    $ renpy.transition(dissolve)
                                    hide mei3a
                                    hide mei3hcl
                                    hide mei3nop
                                    show mei3b
                                    show mei3hhap
                                    show mei3nop
                                    mei "Yesssss....*moaning*"
                                    p "Still too small!"
                                    p "Expansion scroll - 2nd activation!"
                                    $ renpy.transition(dissolve)
                                    hide mei3b
                                    hide mei3hhap
                                    hide mei3nop
                                    show mei3c
                                    show mei3hhap
                                    show mei3nop
                                    p "That is better, but  I want more!"
                                    p "Expansion scroll - 3rd activation!"
                                    $ renpy.transition(dissolve)
                                    hide mei3c
                                    hide mei3hhap
                                    hide mei3nop
                                    show mei3d
                                    show mei3hop
                                    show mei3cl
                                    mei "ARgg....*pain*"
                                    p "Looks like she is in pain right now..."
                                    p "I hope she can take it."
                                    p "Expansion scroll - uge size!"
                                    $ renpy.transition(dissolve)
                                    hide mei3d
                                    hide mei3hop
                                    hide mei3cl
                                    show mei3e
                                    show mei3hop
                                    show mei3nshock
                                    mei "Auuuuuchh!!!*heavy pain*"
                                    p "....."
                                    p "It worked..."
                                    mei "*panting*"
                                    p "You did great Mei!"
                                    p "Here is your reward..."

                            $ renpy.transition(dissolve)
                            show mei3p1
                            p "Time for your pussy...."
                            $ renpy.transition(dissolve)
                            hide mei3p1
                            show mei3p2
                            mei "Mmmm...*moan*"
                            $ renpy.transition(dissolve)
                            hide mei3p2
                            show mei3p3
                            p "Yesss... So warm!"
                            $ renpy.transition(dissolve)
                            hide mei3p3
                            show mei3p4
                            hide mei3nshock
                            hide mei3hop
                            hide mei3hhap
                            hide mei3hcl
                            show mei3hop
                            hide mei3nop
                            show mei3nop
                            mei "OOooooo...*pant*"
                            $ renpy.transition(dissolve)
                            hide mei3p4
                            show mei3p3
                            p "That opened mouth give me an idea!"
                            $ renpy.transition(dissolve)
                            hide mei3p3
                            show mei3p2
                            menu:
                                "Use clone":
                                    p "Shadow clone!"
                                    $ renpy.transition(dissolve)
                                    hide mei3p2
                                    show mei3p3
                                    show mei3b1
                                    p "Time to suck my cock!"
                                    $ renpy.transition(dissolve)
                                    hide mei3p3
                                    show mei3p4
                                    hide mei3b1
                                    show mei3b2
                                    hide mei3nop
                                    show mei3nshock
                                    mei "Mgmmmgm...*pant*"
                                    $ renpy.transition(dissolve)
                                    hide mei3p4
                                    show mei3p3
                                    hide mei3b2
                                    show mei3b3
                                    p "And deeper!"
                                    $ renpy.transition(dissolve)
                                    hide mei3p3
                                    show mei3p2
                                    hide mei3nshock
                                    show mei3cl
                                    hide mei3b3
                                    show mei3b4
                                    mei "*Gag slurp*"
                                    $ renpy.transition(dissolve)
                                    hide mei3p2
                                    show mei3p3
                                    p "Yeah!!!"
                                    $ renpy.transition(dissolve)
                                    hide mei3p3
                                    show mei3p4
                                    hide mei3b4
                                    show mei3b3
                                    p "Yes! Just like that!"
                                    menu:
                                        "Cum in":
                                            p "Amazing!*splurt*"
                                            $ renpy.transition(dissolve)
                                            hide mei3b3
                                            show mei3b2
                                            show mei3spin1
                                            mei "mmhmgmmm*cough*"
                                            $ renpy.transition(dissolve)
                                            hide mei3b2
                                            show mei3b3
                                            show mei3spin2
                                            mei "Grgg... *gag cough*"
                                            $ renpy.transition(dissolve)
                                            hide mei3b3
                                            show mei3b4
                                            hide mei3cl
                                            show mei3nshock
                                            show mei3bin1
                                            mei "*Slurp cough gag*"
                                            $ renpy.transition(dissolve)
                                            show mei3bin2
                                            "Puff..."
                                            $ renpy.transition(dissolve)
                                            hide mei3b4
                                            hide mei3p1
                                            hide mei3cl
                                            hide mei3nshock
                                            show mei3nop
                                            hide mei3bin1
                                            hide mei3bin2
                                            show mei3bin1
                                            show mei3bin2
                                        "Cum out":
                                            $ renpy.transition(dissolve)
                                            hide mei3p4
                                            show mei3p3
                                            hide mei3b3
                                            show mei3b2
                                            mei "*gag Moan*"
                                            $ renpy.transition(dissolve)
                                            hide mei3p3
                                            show mei3p2
                                            hide mei3b2
                                            show mei3b3
                                            p "Yeah! *splurt*"
                                            $ renpy.transition(dissolve)
                                            hide mei3p2
                                            show mei3p1
                                            hide mei3b3
                                            show mei3b4
                                            show mei3spout1
                                            mei "*slurp gag cough*"
                                            $ renpy.transition(dissolve)
                                            hide mei3b4
                                            show mei3b3
                                            hide mei3cl
                                            hide mei3nshock
                                            show mei3nop
                                            show mei3spout2
                                            p "Awesome!"
                                            $ renpy.transition(dissolve)
                                            hide mei3b3
                                            show mei3b2
                                            mei "*Gag*"
                                            $ renpy.transition(dissolve)
                                            hide mei3b2
                                            show mei3b1
                                            show mei3bout1
                                            p "*splurt*"
                                            $ renpy.transition(dissolve)
                                            show mei3bout2
                                            "Puff..."
                                            $ renpy.transition(dissolve)
                                            hide mei3b1


                                    p "Looks like that clone enjoy a lot of fun."
                                    p "I mean I enjoy... Ehm...."
                                    p "Time to clean all mess..."
                                    $ renpy.transition(dissolve)
                                    hide mei3a
                                    hide mei3c
                                    hide mei3e
                                    hide mei3p1
                                    hide mei3p4
                                    hide mei3bin1
                                    hide mei3bin2
                                    hide mei3spout1
                                    hide mei3spout2
                                    hide mei3bout1
                                    hide mei3bout2
                                    hide mei3spin1
                                    hide mei3spin2
                                    hide mei3hop
                                    hide mei3nop
                                    p "Do it properly!"
                                    with fade
                                    p "More mess... More time to clean it all..."
                                    $ renpy.transition(dissolve)
                                    show meia
                                    show meinok
                                    p "Finally! You are clean..."
                                    p ".... I am tired...."
                                    $ day = day + 1
                                    scene black with circleirisin
                                    show dharem0 with circleirisout
                                    jump dharem



                                "Use tools":
                                    p "Time to test some tools..."
                                    $ renpy.transition(dissolve)
                                    hide mei3p2
                                    show mei3p1
                                    p "Maybe some kind of note would be nice..."
                                    $ renpy.transition(dissolve)
                                    hide mei3p1
                                    show mei3text
                                    hide mei3nop
                                    show mei3cl
                                    p "Good... But still you miss something..."
                                    p "Maybe..."
                                    mei "???"
                                    $ renpy.transition(dissolve)
                                    hide mei3p1
                                    show mei3dildo
                                    hide mei3cl
                                    show mei3nshock
                                    mei "Arggg...*pant*"
                                    p "Yeah that is good..."
                                    $ renpy.transition(dissolve)
                                    show mei3p1
                                    p "Time to fuck your pussy."
                                    $ renpy.transition(dissolve)
                                    hide mei3p1
                                    show mei3p2
                                    mei "Mmmm...*moan*"
                                    $ renpy.transition(dissolve)
                                    hide mei3p2
                                    show mei3p3
                                    hide mei3hop
                                    show mei3hhap
                                    hide mei3nshock
                                    show mei3nop
                                    p "You are so wet down here..."
                                    $ renpy.transition(dissolve)
                                    hide mei3p3
                                    show mei3p4
                                    mei "Aahhhh...*moaning*"
                                    $ renpy.transition(dissolve)
                                    hide mei3p4
                                    show mei3p3
                                    hide mei3nop
                                    show mei3cl
                                    p "Nice..."
                                    $ renpy.transition(dissolve)
                                    hide mei3p3
                                    show mei3p2
                                    p "...."
                                    $ renpy.transition(dissolve)
                                    hide mei3p2
                                    show mei3p3
                                    mei "MMmm...*moan*"
                                    $ renpy.transition(dissolve)
                                    hide mei3p3
                                    show mei3p4
                                    p "Come one! Make some noice!"
                                    $ renpy.transition(dissolve)
                                    hide mei3p4
                                    show mei3p3
                                    mei "Ahhhh....*pant*"
                                    $ renpy.transition(dissolve)
                                    hide mei3p3
                                    show mei3p2
                                    p "Yes this is good!"
                                    $ renpy.transition(dissolve)
                                    hide mei3p2
                                    show mei3p3
                                    hide mei3cl
                                    show mei3nop
                                    menu:
                                        "Cum in":
                                            p "Take it all!"
                                            $ renpy.transition(dissolve)
                                            hide mei3p3
                                            show mei3p4
                                            "*splurt*"
                                            $ renpy.transition(dissolve)
                                            show mei3spin1
                                            mei "More....*heavy moaning*"
                                            $ renpy.transition(dissolve)
                                            show mei3spin2
                                            p "Yeah!"
                                            mei "mmmm...*drip*"
                                            p "Nice..."
                                            $ renpy.transition(dissolve)
                                            hide mei3p4
                                            show mei3spin3
                                            p "It is flowing away..."
                                            mei "....."
                                            $ renpy.transition(dissolve)
                                            hide mei3nop
                                            show mei3cl
                                            p "Look at you...."
                                            mei "*moaning*"
                                            p "Ok, I enjoy it."
                                            p "You can dress now..."
                                            p "Cancel that henge, And maybe clean yourself..."
                                            $ renpy.transition(dissolve)
                                            hide mei3spin1
                                            hide mei3spin2
                                            hide mei3spin3
                                            hide mei3hhap
                                            hide mei3cl
                                            hide mei3a
                                            hide mei3c
                                            hide mei3e
                                            hide mei3text
                                            hide mei3dildo
                                            p "Ok... Time to sleep..."
                                            $ day = day + 1
                                            scene black with circleirisin
                                            show dharem0 with circleirisout
                                            jump dharem

                                        "Cum out":
                                            p "I will..."
                                            $ renpy.transition(dissolve)
                                            hide mei3p3
                                            show mei3p2
                                            p "Yeah! *splurt*"
                                            $ renpy.transition(dissolve)
                                            hide mei3p2
                                            show mei3p1
                                            show mei3spout1
                                            mei "...."
                                            $ renpy.transition(dissolve)
                                            show mei3spout2
                                            p "!!!!"
                                            mei "mmmm...*drip*"
                                            p "You look nice now..."
                                            $ renpy.transition(dissolve)
                                            hide mei3p1
                                            p "Your whole body is now different..."
                                            mei "....."
                                            $ renpy.transition(dissolve)
                                            hide mei3nop
                                            show mei3cl
                                            p "Look at you...."
                                            mei "*moaning*"
                                            p "You definitely need a bath."
                                            p "Try to look same as when I use Namigan on you."
                                            $ renpy.transition(dissolve)
                                            hide mei3spin1
                                            hide mei3spin2
                                            hide mei3spin3
                                            hide mei3spout1
                                            hide mei3spout2
                                            hide mei3hhap
                                            hide mei3cl
                                            hide mei3a
                                            hide mei3c
                                            hide mei3e
                                            hide mei3text
                                            hide mei3dildo
                                            p "This will take some time..."
                                            with fade
                                            p "Maybe...."
                                            p "Ahhh... I need to sleep now..."
                                            $ day = day + 1
                                            scene black with circleirisin
                                            show dharem0 with circleirisout
                                            jump dharem


        "Go back to the map":
            scene black with circleirisin
            show nharem0 with circleirisout
            jump nharem




################################ nharemforest1
################################ nharemforest1
################################ nharemforest1
################################ nharemforest1
################################ nharemforest1

label nharemforest1 :
    menu:
        "Look arround":
            if temamission <=11:
                "This forest is really scary."
                "You didn't find anything useful."
                scene black with circleirisin
                show nharem0 with circleirisout
                jump nharem
            else:
                $ renpy.transition(dissolve)
                show temd
                show temnok
                ti "..."
                p "Nice..."
                p "And now is time for..."
                menu temanam4a:
                    "Playtime":
                        p "First, take off your clothes..."
                        $ renpy.transition(dissolve)
                        hide temd
                        show tema
                        hide temnok
                        show temnok
                        p "Hmmm.. Nice... But sometihing need to change..."
                        p "Boob expansion!!!"
                        $ renpy.transition(dissolve)
                        hide tema
                        show temb
                        hide temnok
                        show temnop
                        ti "*moan*"
                        p "I think this is not maximal size..."
                        p "Boob expansion!!!"
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
                        p "I will come back later..."
                        $ day = day + 1
                        scene black with circleirisin
                        show dharem0 with circleirisout
                        jump dharem

                    "Pain train":
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
                            p "OK... Now I will leave you..."
                            p "Prepare yourself for your next visit."
                            $ day = day + 1
                            scene black with circleirisin
                            show dharem0 with circleirisout
                            jump dharem

                    "Blowjob":
                            p "Yes... This is good... Take off your clothes."
                            $ renpy.transition(dissolve)
                            hide temok
                            hide temnok
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
                                    p "See you later..."
                                    $ day = day + 1
                                    scene black with circleirisin
                                    show dharem0 with circleirisout
                                    jump dharem

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
                                    ti "...."
                                    p "No reaction... *sigh* bye..."
                                    $ day = day + 1
                                    scene black with circleirisin
                                    show dharem0 with circleirisout
                                    jump dharem

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
                                    p "That was good right???"
                                    ti "...."
                                    p "OK... Bye..."
                                    $ day = day + 1
                                    scene black with circleirisin
                                    show dharem0 with circleirisout
                                    jump dharem





                    "Fuck her":
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
                                    p "hehe..."
                                    p "It is still fun..."
                                    $ day = day + 1
                                    scene black with circleirisin
                                    show dharem0 with circleirisout
                                    jump dharem

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
                                    p "Ok..."
                                    ti "..."
                                    p "Prepare yourself for next visit..."
                                    $ day = day + 1
                                    scene black with circleirisin
                                    show dharem0 with circleirisout
                                    jump dharem

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
                                    ti "..."
                                    p "Good... But now I need some rest..."
                                    $ day = day + 1
                                    scene black with circleirisin
                                    show dharem0 with circleirisout
                                    jump dharem

        "Go back to the map":
            scene black with circleirisin
            show nharem0 with circleirisout
            jump nharem

# SpaceNET Credits


label credits:
    
    stop music fadeout 1.0
    

    hide spacenet_logo

    hide screen main_menu
    
    show screen termfx
    

    if game_end == False:
        call end_background
        with Dissolve(2)

        
    
    pause 1
    
    call music_outro


    show text "A game by\nVincent Rateau" at truecenter
    with Dissolve(2)
    
    pause 2
    
    hide text
    with Dissolve(2)


    
    show text "www.spacenet.sonejo.net" at truecenter
    with Dissolve(2)
    
    pause 2
    
    hide text
    with Dissolve(2)
    

    
    
    
    
    # music
    $ showtext = """
- Music -

Frank Nora
Kevin McLeod
BoringXtreme
Alexander Nakarada
Rafael Krux
Vincent Rateau

freepd.com



- Sounds -

niallbrady
wim
hiriak
razrox
jackjames-tomknevitt
jaredi
progic35
quistard
vehicle
bird-man
inspectorj
hoerspielgerrit
pillonoise
jamesgilsenan
fullmetaljedi
inspectorj
ingeos
black-boe
walter-odington
davidworksonline,
sergenious
lorenzosu
cgeffex
anton
soulman-90
vhlam
pawsound
noirenex
drminky
gmarchisio
iankath
nickrave
trebblofang
lloydevans09
littlebrojay
blueneon
the-very-real-horst
alaskarobotics
kaumodaki
sophiehall3535
themusicalnomad
daenerys
pan14
viznoman
limitsnap-creations
vumseplutten1709
benagain
daveofdefeat2248
galeku
steshystesh
hoerspielwerkstatt-hef
vegapomme27
proaudioninja
anoesj
frankelmedico
yevgverh

freesound.org


    """
            
    show text Text(showtext,text_align=0.5):
        anchor (0.5, 1)
        pos (400, 480)
        linear 30 pos (400, -1340) 

    
    
    pause 30
    hide text


    # spacenet logo
    show spacenet_logo
    call sound_hyperspace
    #call sound_title
    with Dissolve(2)
    
    pause
    
    stop music fadeout 1.0
    
    #call music_space
    
    call sound_take_off
    #call sound_scan
    
    $ renpy.music.play("music/space.ogg", channel="music", fadein=1, fadeout=0, tight=True, if_changed=True)
    
    with pixellate
    
    jump _invoke_main_menu
    
    

    
    
        
    
    
    
    
# surface engine (from sfioscroll)

#image surface = "images/surfaces/surface1.jpg"

## -> create a condition switch with all surfaces


image surface:
    ConditionSwitch(
        "planet=='xylo'", "images/surfaces/surface1.png",
        "planet=='demo'", "images/surfaces/surface1.png",
        "planet=='cargo'", "images/surfaces/surface_cargo.png",
        "planet=='isc'", "images/surfaces/surface_isc.png")


#######


init:

    $ shippos = (200,200)
    $ direction = 0
    $ ingame = False
    $ landing = False
    
    

#surface
    $ direction = 0
    $ targetdir = 0
    
    
    $ airport1 = (0,0)
    $ airportname1 = ""
    
    $ airport2 = (0,0)
    $ airportname2 = ""
    
    $ airport3 = (0,0)
    $ airportname3 = ""
    
    $ airport4 = (0,0)
    $ airportname4 = ""
   





label surface:
    $ pnc_nodes_visible = False
    
    $ inventory_select = ""
    
    
    stop atmo
    #call atmo_spaceship_hum
    call music_intro
    
    
    
    # hide inventory button
    $ inventory_button = False
    
    scene bgcolor
    
    if planet == "cargo" or planet == "isc":
        call show_space
    
    
    if shadow_enable == 1:
        show shadow at truecenter
    
    $ ingame = False
    
    jump scroll


label scroll:
    
    show screen setpos
    
    if ingame == False:
        show surface behind spaceship, shadow:
            anchor shippos
        show spaceship:
            rotate direction
    else:
        show surface behind spaceship, shadow:
            easein 2 anchor shippos
            
    if space_anim == True:
        call landing_fromspace_anim

    show spaceship:
        pos (0.5,0.5)
        zoom 0.5


    
    #call movescroll
    call rotation
    
    
    call airport 
    
    $ ingame = True
    

   
    #set direction to targetdir
    $ direction = targetdir
    
    #wait for click
    window hide
    pause
    
    call sound_propulsion
    
    
    call movescroll

    jump scroll
    



 

label movescroll:
    
    # surface border warning
    if shippos[0] == 0 and mousepos[0] < 300:
        call surface_borders
    if shippos[0] == 1400 and mousepos[0] > 500: #1200
        call surface_borders
    if shippos[1] == 0 and mousepos[1] < 140:
        call surface_borders
    if shippos[1] == 1600 and mousepos[1] > 340: #1400
        call surface_borders

    
    # set new position if position is not over bg boundaries 
    if mousepos[0] < 300 and shippos[0] > 100:
        $ shippos = (shippos[0]-200 , shippos[1])

    if mousepos[0] > 500 and shippos[0] < 1400: #1200
        $ shippos = (shippos[0]+200 , shippos[1])
        
    if mousepos[1] < 140 and shippos[1] > 100:
        $ shippos = (shippos[0] , shippos[1]-200)

    if mousepos[1] > 340 and shippos[1] < 1600: #1400
        $ shippos = (shippos[0] , shippos[1]+200)
        
    
    return
    




# rotate
label rotation:
    

    #direction from mouse position
    if mousepos > (500,340) :
        $ targetdir = 135
        
    if mousepos < (300,140) :
        $ targetdir = 315
        
        
    if mousepos[0] > 500 and mousepos[1] < 140 :
        $ targetdir = 45
        
    if mousepos[0] < 300 and mousepos[1] > 140 :
        $ targetdir = 225
        

    if 270 < mousepos[0] < 530 and mousepos[1] < 140:
        $ targetdir = 0
        
    if 270 < mousepos[0] < 530 and mousepos[1] > 340:
        $ targetdir = 180
        
        
    if mousepos[0] < 300 and 170 < mousepos[1] < 320:
        $ targetdir = 270
        
    if mousepos[0] > 500 and 170 < mousepos[1] < 320:
        $ targetdir = 90
        


## direction correction
    if targetdir <= 90 and direction >= 270:
        show spaceship:
            rotate (direction-360)
            
    if targetdir >= 270 and direction <= 90:
        show spaceship:
            rotate (direction+360)
    


## rotation    
    if ingame == True:
        show spaceship:
            linear 0.5 rotate targetdir
    
    
    return


    


label airport:
    
    if shippos == airport1 and ingame == True:
        call airport_name(airportname1)
        call landing
    
    if shippos == airport2 and ingame == True:
        call airport_name(airportname2)
        call landing
        
    if shippos == airport3 and ingame == True:
        call airport_name(airportname3)
        call landing
        
    if shippos == airport4 and ingame == True:
        call airport_name(airportname4)
        call landing
        
    return





label airport_name(i):
    pause 2
    show screen notify(i)
    return 




# landing to spaceports
label landing:
 
    menu:
        "take off to space":
            $ pnc_nodes_visible = False
            $ ingame = False
            jump takeoff_tospace_anime
            
        "start landing":
            $ pnc_nodes_visible = True
            $ ingame = False
            
            if planet == "demo":
                $ startpos = 44
                jump map6
                
            
            if planet == "xylo":
                # xylo spaceport
                if shippos == (400,0):
                    $ startpos = 44
                    jump xylo_spaceport
                
                # xylo mine
                if shippos == (200,400):
                    $ startpos = 44
                    jump xylo_mine
                    
                # xylo mountain
                if shippos == (200,1200):
                    $ startpos = 44
                    jump xylo_mountain1
                    
                    
                # xylo sea colony
                if shippos == (1200,1400):
                    $ startpos = 44
                    jump xylo_map6spaceport
                    
            
            if planet == "cargo":
                if shippos == (800,1200):
                    #m "it seems to be closed right now..."
                    $ startpos = 44
                    jump cargo_anim_down
                    
            if planet == "isc":
                if shippos == (0,1000):
                    #m "it seems to be closed right now..."
                    $ startpos = 44
                    jump isc_interchange
                if shippos == (1000,800):
                    #m "it seems to be closed right now..."
                    $ startpos = 44
                    jump isc_city_spaceport
        
        "exit":
            $ ingame = False
            pass
            
    return
    

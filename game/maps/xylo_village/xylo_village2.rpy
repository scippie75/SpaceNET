# MAPS

############################################


init:
    $ xylo_village_mirror_state = 0 #(0= not in place, 1= in place)


label xylo_village2:
    
    call atmo_spaceship_hum
    
    image xylo_village2 = imagemapsdir + "xylo_village2.png"
    
    scene bgcolor
    #show screen notify("xylo's colony village"
    show xylo_village2
    

    show warningfloor:
        anchor (0.5,0.5)
        pos (455,242)
        rotate 90

    image laser:
        "images/laser.png"
        anchor (0,0)
        yzoom 2.0
        choice:
            linear 0.1 alpha 0.1
        choice:
            linear 0.1 alpha 1.0
        choice:
            linear 0.1 alpha 0.3
        choice:
            linear 0.1 alpha 0.8
        repeat
    
    
    # left
    show laser:
        pos (356, 36)
        
    show laser as laser2:
        pos (356, 243)
        
    # right
    show laser as laser3:
        pos (762, 36)
        
    show laser as laser4:
        pos (762, 243)
        
    # top
    show laser as laser5:
        rotate -90
        rotate_pad False
        pos (356, 37)
        
    show laser as laser6:
        rotate -90
        rotate_pad False
        pos (560, 37)
        
    # bottom
    show laser as laser7:
        rotate -90
        rotate_pad False
        pos (356, 444)
        
    show laser as laser8:
        rotate -90
        rotate_pad False
        pos (560, 444)
        


    image xylo_village2b = imagemapsdir + "xylo_village2b.png"
    show xylo_village2b

    # check if spaceship is landing on this map or not
    # $ landing = False
    # $ landing = True
    #call landing_anim
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (36, 264)
    $ nodeB = (320, 85)
    $ nodeC = (322, 170)
    $ nodeD = (391, 170)

    $ nodeAA = (560, 345)
    $ nodeBB = (516, 88)
    $ nodeCC = (698, 127)
    $ nodeDD = (669, 230)

    $ pathA = (nodeA, nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = (nodeA, nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathD = ((0, 0), (0, 0), nodeC, nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
     
    $ pathAA = ((0, 0), (0, 0), (0, 0), nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathBB = ((0, 0), (0, 0), nodeC, nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    
    
    if xylo_village_mirror_state == 1:
        call xylo_village2_mirror
        
    if xylo_village_mirror_state == 0:
        $ pathD = ((0, 0), (0, 0), (0, 0), nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
        $ pathBB = ((0, 0), (0, 0), (0, 0), nodeD, nodeAA, nodeBB, (0, 0), (0, 0))


label loop_xylo_village2:

    # start "move through the map" loop
    call startpos


    # do something at node?
    if exitpos == 1:       #if at node A
        $ startpos = 44    # stay in A
        jump xylo_village1     # map loop to jump to
        
    
    if exitpos == 2:
        if startpos == 2:    #info
            call xylo_village2_info
            
        $ startpos = 2
        jump loop_xylo_village2
        
    
    if exitpos == 3:
        if startpos == 3  and inventory_select != "mirror" and xylo_village_mirror_state == 0:
            call sound_electroshock
            with hpunch
            m "This is a laser fence! {w=1} {nw}"
            m "It looks really dangerous... {w=1} {nw}"
            
            
        if startpos == 3  and xylo_village_mirror_state == 1:
            
            m "There is a mirror disturbing the laser. {w=2} {nw}"
            call xylo_village2_mirror_take
            
      
            
        if inventory_select == "mirror" and xylo_village_mirror_state == 0:
            
            m "A laser and a mirror, that's a good idea!{w=2} {nw}"
            m "I'm looking forward to see the result... {w=2} {nw}"
            call use_and_keep_item
            
            call sound_electroshock
            with flash
            call xylo_village2_mirror

            
        $ startpos = 3
        jump loop_xylo_village2
        
        
        
    if exitpos == 4:
        if startpos == 4  and xylo_village_mirror_state == 1:
            
            m "Now I'm inside thanks to this mirror! {w=2} {nw}"
            call xylo_village2_mirror_take
            jump loop_xylo_village2 
            
        if inventory_select == "mirror" and xylo_village_mirror_state == 0:
            call use_and_keep_item
            call sound_electroshock
            with flash
            call xylo_village2_mirror


        if inventory_select == "" and xylo_village_mirror_state == 0:
            call sound_electroshock
            with hpunch
            m "There is a laser fence! {w=1.5} {nw}"
            m "I can't pass through. {w=1.5} {nw}"

        
        $ startpos = 4
        jump loop_xylo_village2 
        

    #exits routing "got to map and set position for next map"
    if exitpos == 11:
        
        if startpos == 11 and inventory_select != "accesscard":
            call dialog_closed
            m "There is a slot for an access card... {w=2.5} {nw}"
            $ startpos = 11
            jump loop_xylo_village2


        if startpos == 11 and inventory_select == "accesscard":
            call use_and_keep_item
            call sound_collect
            pause 1.5
            $ startpos = 4 
            call sound_door
            jump xylo_village_spacenet
        
        $ startpos = 11
        jump loop_xylo_village2

        
    if exitpos == 22:
        if startpos == 22:
            m "This area is really well protected with this laser fence... {w=2} {nw}"
            m "This seams to be important... {w=1.5} {nw}"
            m "Interesting! {w=1.5} {nw}"
            
            if xylo_village2_cash > 0:
                m "... {w=1.5} {nw}"
                m "There is something on the floor... {w=2} {nw}"
                call io_cash(xylo_village2_cash)
                $ xylo_village2_cash = 0
                
                
        $ startpos = 22
        jump loop_xylo_village2
        
    if exitpos == 33:
        $ startpos = 33
        jump loop_xylo_village2
        
    if exitpos == 44:
        $ startpos = 44
        jump loop_xylo_village2





label xylo_village2_mirror_take:
    menu:
        "take it":
            
            hide laser
            hide lasermirror
            hide mirror
            show laser behind xylo_village2b:
                pos (356, 36)
                
            $ xylo_village_mirror_state = 0
            
            if "mirror" not in inventory:
                $ inventory.append("mirror")
                
            
            call sound_collect
            #with flash
            $ inventory_select = "mirror"
            call inventory_notify
            
            $ pathC = (nodeA, nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
            $ pathD = ((0, 0), (0, 0), (0, 0), nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
            $ pathBB = ((0, 0), (0, 0), (0, 0), nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
            
        
            
        "leave it":
            pass
    return



label xylo_village2_mirror:
    
    $ xylo_village_mirror_state = 1
    
    if "mirror" in inventory:
        $ inventory.remove("mirror")
        
    call use_item
    
    $ pathC = (nodeA, nodeB, nodeC, nodeD, (0, 0), nodeBB, (0, 0), (0, 0))
    $ pathD = ((0, 0), (0, 0), nodeC, nodeD, (0, 0), nodeBB, (0, 0), (0, 0))
    $ pathBB = ((0, 0), (0, 0), nodeC, nodeD, (0, 0), nodeBB, (0, 0), (0, 0))
    
    image mirror:
        "images/buttonscreen.png"
        rotate -45
        anchor (0.5,0.5)
    show mirror:
        pos (357,210)
        
    show laser:
        pos (356, 208)
        yzoom 0.12
        
    show laser as lasermirror:
        rotate -90
        rotate_pad False
        pos (356, 208)
        yzoom 2.5
    
    return




label xylo_village2_info:
    
    $ info_panel_symbol = "laser"

    $ showtext = """
    
    
- Restricted Area -


This area is dangerous, do not approach !

    """
    
    # {font=marvosym.ttf}{size=70}haj{/size}{/font}
    # {font=symbolx.ttf}{size=70}bpr{/size}{/font}
    
    call info_panel # in animations
    
    
    return

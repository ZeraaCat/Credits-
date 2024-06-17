screen about():
    tag menu
    
    use game_menu(_("About"),
                scroll=("vpgrid" if gui.history_height else "viewport"),
                yinitial=0.0):
        
        viewport:
            style_prefix "about"
            viewport_xsize 1200
            viewport_ysize 3000
            child_size (1200, 3000)
            yalign 0.0
            xpos 0.08
            scrollbars "vertical"
            draggable True

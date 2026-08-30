import sys
import os
import traceback

try:
    import pygame
    from pygame.locals import *

    pygame.init()
    pygame.font.init()
    surface = pygame.display.set_mode((640, 480))

    width = surface.get_width()
    height = surface.get_height()
    font = pygame.font.SysFont(None, 24, bold=True)

    # 1. Load Selection Indicator (Ender)
    ball = pygame.image.load("LastEnder2.png")
    ball = pygame.transform.smoothscale(ball, (100, 100))
    ballrect = ball.get_rect()
    ballrect.center = (width // 2, height // 2)

    # Glide physics
    target_x, target_y = ballrect.centerx, ballrect.centery
    glide_speed = 0.15 

    # 2. Base Background Layer (With structural safety fallback if image is missing)
    default_bg = "Screenshot_20260828_131345_Dolphin Emulator.jpg"
    try:
        if os.path.exists(default_bg):
            background_img = pygame.image.load(default_bg)
        else:
            background_img = pygame.Surface((width, height))
            background_img.fill((40, 40, 40))
    except pygame.error:
        background_img = pygame.Surface((width, height))
        background_img.fill((40, 40, 40))

    background_img = pygame.transform.rotate(background_img, 270)
    background_rect = background_img.get_rect() 
    active_frame_name = default_bg

    # 3. Interactive Interface Button Sizes and Layout Positioning
    btn_size = (80, 80)
    buttons_on_top = True # Tracking position state toggled by the Flip Button

    # Create dummy surfaces to use if local placeholder textures fail to load
    fallback_surf = pygame.Surface(btn_size)
    fallback_surf.fill((100, 100, 100))

    def create_button_rects(top_row=True):
        """Generates dynamic bounding rect positions across the screen layout bounds."""
        y_pos = 10 if top_row else (height - 90)
        # Positions: Far-Left, Mid-Left, Mid-Right, Far-Right
        return [
            pygame.Rect(10, y_pos, *btn_size),
            pygame.Rect(170, y_pos, *btn_size),
            pygame.Rect(390, y_pos, *btn_size),
            pygame.Rect(width - 90, y_pos, *btn_size)
        ]

    # Initialize button layout structures
    rect_opt1, rect_flip, rect_drag, rect_opt2 = create_button_rects(buttons_on_top)

    # --- DATA POOLS & SYSTEM TRACKING STATES ---
    known_actions = [
        ["option1", "Screenshot_20260826_095342_Instagram.jpg"],
        ["option1", "Screenshot_20260826_095342_Instagram.jpg"]
    ]
    touchpos = []
    
    # Drag state tracking parameters
    drag_mode_active = False
    pending_drag_point = None

    madden_dir = "Madden04"
    frame_index = 0
    frame_delay = 5 
    frame_timer = 0
    cooldown = 0  

    clock = pygame.time.Clock()
    touched = False

    print("Interface initialized successfully.")

    while True:
        # Re-verify and maintain current box boundary alignment maps
        rect_opt1, rect_flip, rect_drag, rect_opt2 = create_button_rects(buttons_on_top)
        
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                touched = True
                target_x, target_y = ev.pos
                
                # CRITICAL GUARD: Only log touch coordinates if click falls completely clear of interface boxes
                if not (rect_opt1.collidepoint(ev.pos) or rect_flip.collidepoint(ev.pos) or 
                        rect_drag.collidepoint(ev.pos) or rect_opt2.collidepoint(ev.pos)):
                    
                    if drag_mode_active:
                        # Secondary drag point logging sequence target
                        if pending_drag_point is not None:
                            # Complete structural bundle: [first_x, first_y], frame_name, label, [drag_x, drag_y]
                            touchpos.append([pending_drag_point, active_frame_name, "drag_move", [target_x, target_y]])
                            print(f"Logged DRAG sequence: From {pending_drag_point} to [{target_x}, {target_y}]")
                            pending_drag_point = None
                            drag_mode_active = False # Automatically restore standard sequence mode
                        else:
                            # Cache the initial starting coordinate pair
                            pending_drag_point = [target_x, target_y]
                            print(f"Logged primary drag start at: {pending_drag_point}. Touch destination next.")
                    else:
                        # Standard tracking structure execution line
                        touchpos.append([target_x, target_y, active_frame_name])
                        print(f"Logged Standard Click: X:{target_x} Y:{target_y} on [{active_frame_name}]")
                
            elif ev.type == pygame.MOUSEBUTTONUP:
                touched = False
            elif ev.type == pygame.MOUSEMOTION:
                if touched:
                    target_x, target_y = ev.pos
                    
        clock.tick(60)
        surface.fill((0, 0, 0))
        
        if cooldown > 0:
            cooldown -= 1
        
        # Apply smooth slider physics constraints
        ballrect.centerx += (target_x - ballrect.centerx) * glide_speed
        ballrect.centery += (target_y - ballrect.centery) * glide_speed
        
        if ballrect.left < 0: ballrect.left = 0
        if ballrect.right > width: ballrect.right = width
        if ballrect.top < 0: ballrect.top = 0
        if ballrect.bottom > height: ballrect.bottom = height
            
        # --- INTERACTIVE APP OPTION CONTROL REGIONS ---
        
        # 1. OPTION 1 AREA (FAR LEFT): Log serialization flush
        if rect_opt1.collidepoint(ballrect.center) and cooldown == 0:
            for action in known_actions:
                if action[0] == "option1":
                    try:
                        with open('touchpos.py', 'w') as fk:
                            fk.write('touchpos=' + str(touchpos))
                        print("Saved updated tracking variables cleanly to touchpos.py")
                        cooldown = 45  
                        break 
                    except Exception:
                        pass

        # 2. FLIP UTILITY BUTTON (MID LEFT): Shift layout positions to opposite edge
        if rect_flip.collidepoint(ballrect.center) and cooldown == 0:
            buttons_on_top = not buttons_on_top
            print(f"Interface shifted. Menu tracking placement top alignment = {buttons_on_top}")
            cooldown = 30 # Half-second protection buffer
            
        # 3. EXTRA DRAG POINT BUTTON (MID RIGHT): Prepare system for dual coordinate map
        if rect_drag.collidepoint(ballrect.center) and cooldown == 0:
            drag_mode_active = True
            pending_drag_point = None
            print("Drag Mode Primed! Touch starting spot, then touch target destination spot.")
            cooldown = 30

        # 4. OPTION 2 AREA (FAR RIGHT): Dynamic Background File Cycler
        if rect_opt2.collidepoint(ballrect.center):
            if os.path.exists(madden_dir):
                frames = sorted([f for f in os.listdir(madden_dir) if f.endswith(('.jpg', '.jpeg', '.png'))])
                if frames:
                    frame_timer += 1
                    if frame_timer >= frame_delay:
                        frame_timer = 0
                        frame_index = (frame_index + 1) % len(frames)
                        
                    try:
                        active_frame_name = frames[frame_index]
                        target_frame_path = os.path.join(madden_dir, active_frame_name)
                        cyclist_img = pygame.image.load(target_frame_path)
                        background_img = pygame.transform.rotate(cyclist_img, 270)
                    except pygame.error:
                        # Smooth frame protection skip if texture data corrupts
                        pass
            
        # Draw background layer stack
        surface.blit(background_img, background_rect) 
        
        # Draw Control Box Interfaces
        pygame.draw.rect(surface, (200, 50, 50), rect_opt1)   # Red Box
        pygame.draw.rect(surface, (50, 200, 50), rect_flip)   # Green Box
        pygame.draw.rect(surface, (50, 50, 200), rect_drag)   # Blue Box
        pygame.draw.rect(surface, (200, 200, 50), rect_opt2)  # Yellow Box
        
        # Render Text Identifiers Over Buttons for ease of calibration
        surface.blit(font.render("SAVE", True, (255,255,255)), (rect_opt1.x+15, rect_opt1.y+30))
        surface.blit(font.render("FLIP", True, (255,255,255)), (rect_flip.x+15, rect_flip.y+30))
        surface.blit(font.render("DRAG", True, (255,255,255)), (rect_drag.x+15, rect_drag.y+30))
        surface.blit(font.render("CYCLE", True, (255,255,255)), (rect_opt2.x+10, rect_opt2.y+30))
        
        # Draw selection tracker indicator
        surface.blit(ball, ballrect)
        
        # If drag registration sequence is primed, draw active warning note text
        if drag_mode_active:
            state_text = "DRAG ACTIVE: NEED DESTINATION" if pending_drag_point else "DRAG ACTIVE: NEED START"
            surface.blit(font.render(state_text, True, (255, 100, 0)), (20, height // 2))
        
        pygame.display.flip()

except Exception as e:
    error_message = traceback.format_exc()
    print("\n--- INTERNAL CRASH LOGGER TRIGGERED ---")
    print(error_message)
    with open("newerror.py", "w+") as error_file:
        error_file.write(f'# Madden Inspect Error Log\nerror = """{error_message}"""')
    pygame.quit()
    sys.exit()

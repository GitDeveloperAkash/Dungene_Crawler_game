import pygame
import config
import character
import weapon
import damageText as D

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Dungene Crawler")


clock = pygame.time.Clock()

bow_image = pygame.image.load("images/weapons/bow.png").convert_alpha()
arrow_image = pygame.image.load("images/weapons/arrow.png").convert_alpha()


character_list = []
character_type = ["elf", "big_demon", "goblin", "imp", "skeleton", "muddy", "tiny_zombie" ]
for Character in character_type:
    animation_frames = []
    for i in range(4):
        img = pygame.image.load(f"images/character/{Character}/run/{i}.png").convert_alpha()
        animation_frames.append(img)
    character_list.append(animation_frames)


player = character.player(character_list, 0)
bow = weapon.weapon(bow_image, arrow_image)
arrow_group = pygame.sprite.Group()

damage_text_group = pygame.sprite.Group()   

enemy_list = []
enemy = character.player(character_list, 3)
enemy_list.append(enemy)

Run = True
Moving_left = False
Moving_right = False
Moving_up = False
Moving_down = False


while Run:

    clock.tick(config.FPS)
    screen.fill(config.GRAY)
    x, y = 0, 0
    if Moving_left:
        x -= config.SPEED
    if Moving_right:
        x += config.SPEED
    if Moving_up:
        y -= config.SPEED
    if Moving_down:
        y += config.SPEED

    player.move(x, y) 
    player.update()
    arrow = bow.update(player)
    if arrow:
        arrow_group.add(arrow)
    
    player.drow(screen)
    bow.draw(screen)

    player.display_health(screen)

    for arrow in arrow_group:
        arrow.drow(screen)
        damage, enemy_pos = arrow.update(enemy_list)
        if damage:
            damage_text = D.damageText(enemy_pos.centerx, enemy_pos.y, damage)
            damage_text_group.add(damage_text)

        
    for damage_text in damage_text_group:
        damage_text.update()

    for enemy in enemy_list:
        enemy.update()
        enemy.drow(screen)
        enemy.display_health(screen)
    
    damage_text_group.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Game closed")
            Run = False

        if event.type == pygame.KEYDOWN:            
            if event.key == pygame.K_a:
                Moving_left = True
            if event.key == pygame.K_d:
                Moving_right = True
            if event.key == pygame.K_w:
                Moving_up = True
            if event.key == pygame.K_s:
                Moving_down = True

        if event.type == pygame.KEYUP:            
            if event.key == pygame.K_a:
                Moving_left = False
            if event.key == pygame.K_d:
                Moving_right = False
            if event.key == pygame.K_w:
                Moving_up = False
            if event.key == pygame.K_s:
                Moving_down = False
        
    pygame.display.update()
pygame.quit()    
    
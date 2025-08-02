import pygame
import player
import ray
import wall
import snipets
run = True
display = pygame.display.set_mode((snipets.screen_size_x, snipets.screen_size_y))
pygame.display.set_caption("Raytracing")
player = player.Player((snipets.screen_size_x / 4, snipets.screen_size_y / 2), 15, "blue", snipets.player_group)
def draw():
    display.fill((0,0,0))
    pygame.draw.line(display, (255,255,255), (snipets.screen_size_x/2,0), (snipets.screen_size_x/2, snipets.screen_size_y), 2 )
    snipets.player_group.draw(display)
    snipets.wall_group.draw(display)
    snipets.ray_group.draw(display)
    draw_3d()
    pygame.display.update()

def player_facing():
    for i in range(-66, 66):
        direction = player.direction.rotate(i)
        ray.Ray(player.rect.center, direction, 200, 20, snipets.ray_group, i)

def cast_ray(starting_pos, direction, max_distance, speed=5):
    current_position = starting_pos
    distance = 0
    while distance < max_distance:
        current_position += direction * speed
        distance += speed

        collision_rect = pygame.Rect(current_position[0], current_position[1], 2, 2)
        pygame.draw.rect(display, (255,255,255), collision_rect)
        pygame.display.update()
        if any(one_wall.rect.colliderect(collision_rect) for one_wall in snipets.wall_group):
            return current_position

    return None

def create_map():
    for y, row in enumerate(wall.map):
        for x, cell in enumerate(row):
            if cell == "W":
                wall.Wall((snipets.wall_size, snipets.wall_size), (x * snipets.wall_size, y * snipets.wall_size), snipets.wall_group)

def draw_3d():

    for ray in snipets.ray_group:
        if ray.hit_position:
            if ray.hit_distance == 0:
                wall_height = snipets.real_wall_height
            else:
                wall_height = int(snipets.wall_height_scale / ray.hit_distance)

            x = (snipets.screen_size_x * 3 / 4) + ray.index * snipets.slice_width
            y_top = snipets.camera_height - wall_height // 2
            y_bottom = snipets.camera_height + wall_height // 2

            pygame.draw.line(display, "blue", (x, y_top), (x, y_bottom))
            ray.kill()


create_map()
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    player_facing()
    snipets.player_group.update()
    snipets.ray_group.update()
    draw()
pygame.quit()
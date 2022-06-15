import pygame


class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size, size))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 3
        self.motion = 1


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, motion, speed=7):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.motion = motion
        self.speed = speed

    def update(self):
        if self.rect.x > 700 or self.rect.x < 0 or self.rect.y > 700 or self.rect.y < 0:
            self.kill()
        if self.motion == 1:
            self.rect.y -= self.speed
        if self.motion == 2:
            self.rect.x += self.speed
        if self.motion == 3:
            self.rect.y += self.speed
        if self.motion == 4:
            self.rect.x -= self.speed


pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Tank")

tank = Tank(40, 40, 40)

bullet_group = pygame.sprite.Group()

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                bullet_group.add(Bullet(tank.rect.centerx, tank.rect.centery, tank.motion))

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        tank.rect.x -= tank.speed
        tank.motion = 4
    if key[pygame.K_RIGHT]:
        tank.rect.x += tank.speed
        tank.motion = 2
    if key[pygame.K_UP]:
        tank.rect.y -= tank.speed
        tank.motion = 1
    if key[pygame.K_DOWN]:
        tank.rect.y += tank.speed
        tank.motion = 3

    bullet_group.update()

    screen.fill((0, 255, 255))
    screen.blit(tank.image, tank.rect)
    bullet_group.draw(screen)
    pygame.display.flip()
    pygame.time.delay(20)

pygame.quit()

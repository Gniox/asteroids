import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass
    
    def hasCollided(self, asteroid):
        ## pythagorean theorem to get distance between centers
        ## compare to the sum of radiuses
        ## return true if distance is less or equal
        ## return false otherwise
        distance = pygame.math.Vector2.distance_to(self.position, asteroid.position)
        
        if(distance <= self.radius + asteroid.radius):
            return True

        return False

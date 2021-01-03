class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.mass = 2.5
        self.depth = 0.05

    def asf_mass(self):
        print(f'Для покрытия всего дорожного полотна необходимо', round(self.length * self.width * self.mass * self.depth, 2), 'т асфальта.')

road = Road(5000, 20)
road.asf_mass()

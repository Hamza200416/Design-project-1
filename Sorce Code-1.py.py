class SimpleSelfDrivingCar:
    def __init__(self):  # Fix here: double underscores for __init__
        self.x = 0
        self.y = 0
        self.direction = "North"
    
    def move_forward(self):
        if self.direction == "North":
            self.y += 1
        elif self.direction == "South":
            self.y -= 1
        elif self.direction == "East":
            self.x += 1
        elif self.direction == "West":
            self.x -= 1
        print(f"Moved forward to ({self.x}, {self.y})")
    
    def turn_left(self):
        directions = ["North", "West", "South", "East"]
        self.direction = directions[(directions.index(self.direction) + 1) % 4]
        print(f"Turned left. Now facing {self.direction}")
    
    def turn_right(self):
        directions = ["North", "East", "South", "West"]
        self.direction = directions[(directions.index(self.direction) + 1) % 4]
        print(f"Turned right. Now facing {self.direction}")

# Create a car instance
car = SimpleSelfDrivingCar()

# Simulate some movements
car.move_forward()  # Moved forward to (0, 1)
car.turn_right()    # Turned right. Now facing East
car.move_forward()  # Moved forward to (1, 1)
car.turn_left()     # Turned left. Now facing North
car.move_forward()  # Moved forward to (1, 2)

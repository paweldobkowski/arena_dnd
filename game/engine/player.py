class Player:
    def __init__(self, starting_position='1;1', speed=1):
        self.current_position = starting_position
        self.previous_position = starting_position
        self.speed = speed
        self.available_moves = None

    def move(self, new_position, available_moves):
        if new_position in available_moves:
            self.previous_position = self.current_position
            self.current_position = new_position

    def get_position(self):
        return self.current_position


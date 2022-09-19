class Player:
    def __init__(self, starting_position='1;1', speed=1):
        self.starting_position = starting_position
        self.speed = speed
        self.current_position = starting_position
        self.available_moves = None

    def move(self, new_position, available_moves):
        if new_position in available_moves:
            self.current_position = new_position

    def get_position(self):
        return self.current_position


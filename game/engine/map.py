class Map:
    def __init__(self, wall_size, levels=1, pyramid=False):
        self.wall_size = wall_size
        self.levels = levels
        self.pyramid = pyramid
        self.game_map = None

    def create_map(self, player_position):
        game_map = []

        for r in range(1, self.wall_size+1):
            row = []

            for c in range(1, self.wall_size+1):
                tile = f'{c};{r}'
                row.append(tile)
            
            game_map.append(row)

        self.game_map = game_map

        return game_map

    # def refresh_map(self):
    #     for row in self.game_map:
    #         if player.current_position in row

    def list_available_moves(self, position, player_speed=1):
        available_moves = []

        max_pos = self.wall_size

        position = position.split(';')

        start_col = int(position[0])
        start_row = int(position[1])

        if start_col > max_pos or start_col < 1:
            return 'out of map'

        if start_row > max_pos or start_row < 1:
            return 'out of map'

        # print(f'start col: {start_col}, start row: {start_row}')

        for step in range(1, player_speed + 1):
            down = start_row + step if start_row + step <= max_pos else start_row
            up = start_row - step if start_row - step > 0 else start_row
            right = start_col + step if start_col + step <= max_pos else start_col
            left = start_col - step if start_col - step > 0 else start_col

            # same tile
            available_moves.append(f'{start_col};{start_row}')

            # move up
            available_moves.append(f'{start_col};{up}')

            # move down
            available_moves.append(f'{start_col};{down}')

            # move right
            available_moves.append(f'{right};{start_row}')

            # move left
            available_moves.append(f'{left};{start_row}')

            # # diagonal left up
            # available_moves.append(f'{left};{up}')

            # # diagonal left down
            # available_moves.append(f'{left};{down}')

            # # diagonal right up
            # available_moves.append(f'{right};{up}')

            # # diagonal right down
            # available_moves.append(f'{right};{down}')

            available_moves = set(available_moves)
            available_moves = list(available_moves)

        return available_moves

    def get_map(self):

        return self.game_map

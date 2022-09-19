from django.shortcuts import render

from game.engine.map import Map
from game.engine.player import Player



player = Player()
game_map = Map(5)
game_map.create_map(player.current_position)

def index(request):

    val = request.GET.get('tile')
    available_moves = game_map.list_available_moves(player.current_position, player.speed)
    player.move(val, available_moves)

    game_map.update_map(player.current_position)

    print(f'player current position: {player.current_position}')

    context = {
        'game_map': game_map.get_map(),
        'wall_size': game_map.wall_size,
        }

    return render(request, 'index.html', context=context)
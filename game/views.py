from django.shortcuts import render

from game.engine.map import Map
from game.engine.player import Player



player = Player(speed=1)
game_map = Map(10)
game_map.create_map(player.current_position)

def index(request):

    val = request.GET.get('tile')
    available_moves = game_map.list_available_moves(player.current_position, player.speed)
    player.move(val, available_moves)

    game_map.update_map(player.previous_position, player.current_position)

    context = {
        'game_map': game_map.get_map(),
        'wall_size': game_map.wall_size,
        }

    return render(request, 'index.html', context=context)
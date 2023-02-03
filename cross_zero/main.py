import game
import board

game.set_player_names()

while True:
    if game.game_turn():
        break
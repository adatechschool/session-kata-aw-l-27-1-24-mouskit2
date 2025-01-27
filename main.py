     
from awele import Awele
from playeur import Playeur


if __name__ == '__main__':
    game = Awele()
    game.display()
    print(f"le jeu et il vide = {game.is_empty()}")
    playeur1 = Playeur(game)
    playeur2 = Playeur(game)
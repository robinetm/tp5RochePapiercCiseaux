# crée par 2023/05/03
# crée le mathis robinet
# tp4 (cercle bouge/couleur aleatoire)
from enum import Enum
import arcade

class AttackType(Enum):
   """
   Simple énumération pour représenter les différents types d'attaques.
   """
   ROCK = 0,
   PAPER = 1,
   SCISSORS = 2

class AttackAnimation(arcade.Sprite):
   ATTACK_SCALE = 0.50
   ANIMATION_SPEED = 5.0



#rock1 = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)
#rock2= arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)
#coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)
#coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)
#coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)
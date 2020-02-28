from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    first_player = models.ForeignKey(User,
                                     related_name="games_first_player", on_delete=models.CASCADE)
    second_player = models.ForeignKey(User,
                                      related_name="game_second_player", on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    """Add a default value the database 
    table has already been created
    """
    status = models.CharField(max_length=1,default='F')

class Move(models.Model):
    x = models.IntegerField()
    y = models.BigIntegerField()
    comment = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField()

    game = models.ForeignKey(Game, on_delete=models.CASCADE)


    """If this game getts deleted so does all the 
        associated data
        """
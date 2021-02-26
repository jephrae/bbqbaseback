from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    # meattype = models.CharField(max_length=100)
    CHICKEN = 'CK'
    BEEF = 'BF'
    PORK = 'PK'
    FISH = 'FH'
    GAME = 'GM'
    MEAT_TYPE_CHOICES =[
        (CHICKEN, 'Chicken'),
        (BEEF, 'Beef'),
        (PORK, 'Pork'),
        (FISH, 'Fish'),
        (GAME, 'Game'),
    ]
    meat_type = models.CharField(
        max_length =2,
        choices=MEAT_TYPE_CHOICES,
        default=BEEF,
    )
    meat_cut = models.CharField(max_length=100)
    cooktime = models.CharField(max_length=100)
    temp = models.CharField(max_length=100)
    credit = models.CharField(max_length=100)
    photo_url = models.TextField()
    desc = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.name
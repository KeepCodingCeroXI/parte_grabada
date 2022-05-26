from random import randint

def dice_launch(faces=6):
    return randint(1, faces)

def dices_launch(num=2, faces=6):
    return tuple([dice_launch(faces) for i in range(num)])


                
#!/usr/bin/env python3
# Created By: Boluwatife Dada
# Date: May 22, 2025
# This program is the "space Aliens" program on the pybadge

import ugame
import stage


def game_scene():
    # this function is the main game scene

    # image banks for circuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # set the background to image 0 in the image bank
    #  and the size (10x8 titles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # create a stage for the background to show up on
    #  and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in folder
    game.layers = [ship] + [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # redraw sprites
        game.render_block()
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()

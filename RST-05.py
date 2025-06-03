#!/usr/bin/env python3
# Created By: Boluwatife Dada
# Date: May 22, 2025
# This program is the "space Aliens" program on the pybadge

import ugame
import stage


import constants

def game_scene():
        # this function is the main game scene

        # image banks for CircuitPython
        image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
        image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

        # sets the background to image 0 in the image bank
        # and the sie (10x8 tiles of 16x16)
        background = stage.Grid(image_bank_background, 10, 8)

        ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

        # create a stage for the background to show up on
        # and set the frame rate to 60fps
        game = stage.Stage(ugame.display, 60)
        # set the layers, items show up in order
        game.layers = [ship] + [background]
        # render the background and initial location of sprite list
        # most likely you will only render background once per scene
        game.render_block()
        # repeat forever, game loop
        while True:
            # get user input
            keys = ugame.buttons.get_pressed()


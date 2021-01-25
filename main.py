def on_overlap_tile(sprite, location):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.builtin.ocean_sand13,
    on_overlap_tile)

myCorg = corgio.create(SpriteKind.player)
myCorg.horizontal_movement()
myCorg.vertical_movement()
myCorg.update_sprite()
myCorg.follow()
tiles.set_tilemap(tiles.create_tilemap(hex("""
            1400080000000000000000000000000000000000000000020000000000000000000000000000000000000002000000000000000000000000000000000000000200000000000000000000000000000000000000020001010101010101010100000000000000000002000000000000000000000001010101010101000200000000000000000000000000000000000000020101010101010101010101010101010101000002
        """),
        img("""
            . . . . . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . . . . . .
            . 2 2 2 2 2 2 2 2 2 . . . . . . . . . .
            . . . . . . . . . . . 2 2 2 2 2 2 2 . .
            . . . . . . . . . . . . . . . . . . . .
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 . . .
        """),
        [myTiles.transparency16,
            sprites.builtin.ocean_depths0,
            sprites.builtin.ocean_sand13],
        TileScale.SIXTEEN))
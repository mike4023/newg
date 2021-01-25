scene.onOverlapTile(SpriteKind.Player, sprites.builtin.oceanSand13, function on_overlap_tile(sprite: Sprite, location: tiles.Location) {
    game.over(true)
})
let myCorg = corgio.create(SpriteKind.Player)
myCorg.horizontalMovement()
myCorg.verticalMovement()
myCorg.updateSprite()
myCorg.follow()
tiles.setTilemap(tiles.createTilemap(hex`
            1400080000000000000000000000000000000000000000020000000000000000000000000000000000000002000000000000000000000000000000000000000200000000000000000000000000000000000000020001010101010101010100000000000000000002000000000000000000000001010101010101000200000000000000000000000000000000000000020101010101010101010101010101010101000002
        `, img`
            . . . . . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . . . . . .
            . 2 2 2 2 2 2 2 2 2 . . . . . . . . . .
            . . . . . . . . . . . 2 2 2 2 2 2 2 . .
            . . . . . . . . . . . . . . . . . . . .
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 . . .
        `, [myTiles.transparency16, sprites.builtin.oceanDepths0, sprites.builtin.oceanSand13], TileScale.Sixteen))

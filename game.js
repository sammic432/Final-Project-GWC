window.onload = function() {
    game.load.image('woman', 'woman.png');

    }

    var myimage;
    function create() {
        game.add.image(0, 0, 'background');
        background = game.add.tileSprite(0, 0, 1400, 500, 'background');
        myimage = game.add.sprite(50,game.world.height-200, 'woman');myimage.scale.setTo(0.4,0.4);
        game.world.setBounds(-500, 0, 1400, 500);
        background = game.add.tileSprite(-700, 0, 1400, 500, 'background');

        myimage = game.add.sprite(50 ,game.world.height-200, 'woman');
        myimage.scale.setTo(0.4,0.4);
        
        myimage.anchor.setTo(0.5, 0.5);

    }

    function update() {
        background.tilePosition.x -= 1;

        
        if (game.input.keyboard.isDown(Phaser.Keyboard.RIGHT))
        {
            myimage.x += 4;
        }

        

    
    }

};
\ No newline at end of file
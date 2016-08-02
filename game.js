window.onload = function() {

    //  Note that this html file is set to pull down Phaser 2.5.0 from the JS Delivr CDN.
    //  Although it will work fine with this tutorial, it's almost certainly not the most current version.
    //  Be sure to replace it with an updated version before you start experimenting with adding your own code.

    var game = new Phaser.Game(700, 500, Phaser.AUTO, '', { preload: preload, create: create, update: update });

    var background;
    function preload() {
        game.load.image('background', 'office.jpg');
        game.load.image('woman', 'woman.png');

    }
    var myimage;
    function create() {
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
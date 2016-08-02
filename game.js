window.onload = function() {

    //  Note that this html file is set to pull down Phaser 2.5.0 from the JS Delivr CDN.
    //  Although it will work fine with this tutorial, it's almost certainly not the most current version.
    //  Be sure to replace it with an updated version before you start experimenting with adding your own code.

    var game = new Phaser.Game(700, 500, Phaser.AUTO, '', { preload: preload, create: create, update: update, render: render });
    
    s = myimage
    
    var background;
    
    var player;


    var tween;

    var body = "woman.png"

    var woman = "woman.png"

    function preload() {
        game.load.image('background', 'office.jpg');
        game.load.image('woman', 'woman.png');

    }

    var myimage;

    function create() {
        game.world.setBounds(-500, 0, 1400, 500);
        background = game.add.tileSprite(-700, 0, 1400, 500, 'background');

        myimage = game.add.sprite(50 ,game.world.height-150, 'woman');
        myimage.scale.setTo(0.4,0.4);
        
        myimage.anchor.setTo(0.5, 0.5);
        // s = game.add.sprite(game.world.centerX, game.world.centerY, 'woman');
        // s.anchor.setTo(0.5, 0.5);
        // s.scale.setTo(2, 2);

        myimage.animations.add('run');
        myimage.animations.play('run', 10, true);

        game.camera.follow(player);

    }

    function update() {
        background.tilePosition.x -= 1;

        
        if (game.input.keyboard.isDown(Phaser.Keyboard.RIGHT)){
            while myimage.x>0 {
                myimage.x += 4;
            // tween.delay(0);
            }
        }

        if (game.input.keyboard.isDown(Phaser.Keyboard.LEFT)){
            while myimage.x>0 {
                myimage.x -= 4;
            // tween.delay(0);
            }
        }

        // if (game.input.keyboard.isDown(Phaser.Keyboard.SPACEBAR)){
        //     myimage.y -= 4;
        //     myimage.x += 2;
        //     myimage.y += 4;
        // }

        // if (game.input.keyboard.isDown(Phaser.Keyboard.SPACEBAR)){
        //     player.body.velocity.y = -350;
        // }

    }


    function render() {

    }

};


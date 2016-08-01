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

    function create() {
        game.add.image(0, 0, 'background');
        background = game.add.tileSprite(0, 0, 1400, 500, 'background');
        myimage = game.add.sprite(50,game.world.height-200, 'woman');myimage.scale.setTo(0.4,0.4);
    }

    function update() {
        background.tilePosition.x -= 1;
    }

};
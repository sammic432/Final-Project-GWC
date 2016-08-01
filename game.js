window.onload = function() {

    //  Note that this html file is set to pull down Phaser 2.5.0 from the JS Delivr CDN.
    //  Although it will work fine with this tutorial, it's almost certainly not the most current version.
    //  Be sure to replace it with an updated version before you start experimenting with adding your own code.

    var game = new Phaser.Game(700, 500, Phaser.AUTO, '', { preload: preload, create: create, update: update });

    var background;
    function preload() {
        game.load.image('background', 'background.jpg');
        game.load.image('woman', 'woman.png');

    }

    function create() {
        game.add.image(0, 0, 'background');
        background = game.add.tileSprite(0, 0, 1400, 500, 'background');
        var test = game.add.sprite(20, 100, 'woman');
    }

    function update() {
        background.tilePosition.x -= 1;
    }

};
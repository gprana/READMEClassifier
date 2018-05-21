# PixImGen

Pixel graphics library for PHP.

## Installation

Add this to your composer.json:

```JSON
{
	"require": {
		"thekonz/piximgen": "1.0.*@dev"
	}
}
```

Then run `composer install` or `composer update`.

## Example app

Wanna try it out? Take a look at the [example app](https://github.com/thekonz/piximgengui).

## General usage (salute!)

* Load the composer autoloader.

```PHP
require_once 'vendor/autoload.php';
```

* Create a new instance of PixImGen.

```PHP
$image = new \thekonz\PixImGen();
```

* Set the settings for the image (the constructor also accepts settings as a parameter). You don't have to set the settings at all, there are default settings.

```PHP
$image->setSettings([
	'seed' => 'GitHub rocks!'
]);
```

* Set the header.

```PHP
header('content-type: image/png');
```

* Display the image.

```PHP
echo $image->getImage();
```

* Look at your image!

![Image](http://imgur.com/yMS6L7W.png)

If you play around with the settings (especially the saturation settings), you can get some pretty cool images. 

## Complete list of settings

| Setting | Explanation | Default value |
| --- | --- | --- |
| seed | Starting value for the random generator. Just like in Minecraft. | System time (`time()`) |
| blocksize | The width of each block (pixel). | 15 |
| width | The amount of blocks on the X-axis of the image. | 10 |
| height | The amount of blocks on the Y-axis of the image. | 10 |
| minredsaturation | The minimum saturation of the color red. | 0 |
| maxredsaturation | The maximum saturation of the color red. | 255 |
| mingreensaturation | The minimum saturation of the color green. | 0 |
| maxgreensaturation | The maximum saturation of the color green. | 255 |
| minbluesaturation | The minimum saturation of the color blue. | 0 |
| maxbluesaturation | The maximum saturation of the color blue. | 255 |

## Further manipulation of the image

Since the method **getImage()** returns an Imagick object, you can use all of the [Imagick methods](http://php.net/manual/en/book.imagick.php).

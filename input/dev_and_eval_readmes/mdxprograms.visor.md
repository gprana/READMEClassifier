# <img src="_demo/logo.png" width="35" alt="Visor logo">&nbsp;Visor

A simple admin overlay to get to the relevant areas of the Craft CMS control panel.

## Demo
![Visor Demo](_demo/demo.gif)

### Screengrab
![Visor screengrab](_demo/screengrab.png)

## Installation

To install Visor, follow these steps:

1. Download & unzip the file and place the inner `visor` directory in your `craft/plugins` folder
2. Install plugin in the Craft Control Panel under Settings > Plugins
3. The plugin folder should be named `visor` for Craft to recognize it.
4. Add `{% hook "addVisor" %}` to any templates it should display on. Ideally this should be right before the `</body>` tag in your `_layout.html` file.

### Keyboard Shortcuts
You can activate Visor by clicking the gear icon or using the following keyboard shortcuts:

| Key            | Description                 |
|----------------|-----------------------------|
| <code>`</code> | Toggles Visor open or close |
| `ESC`          | Closes Visor (if open)      |

## Customizing Visor

### Overriding styles

Visor has a class of `craft-visor--override` on the outer `<section>` element. To change any of the default styles, simply start your styles with `.craft-visor.craft-visor--override`. This will make your styles more specific without resorting to `!important` madness.

### Overriding icons

Visor also uses inline SVGs for all graphics. This:

- Reduces HTTP requests
- Looks crisp at any pixel density
- Allows you to re-style the icons using `fill` in your CSS

### Overriding background

If you'd prefer to replace purple with a different color you can change this by targeting `.craft-visor__modal`.

## Browser compatibility
This has been tested on Chrome, Firefox, Safari and IE 10+, but [drop in an Issue](https://github.com/trendyminds/visor/issues/new) if you notice any strangeness.

## Contributing
We welcome anyone and everyone who would like to improve Visor to fork it and send in pull requests. To start developing Visor:

0. Ensure you have Node version 5.x.x running on your machine
1. Clone the repo to your computer
2. Run `npm install`
3. Run `npm run build` to compile the `_styles` and `_scripts` files into the main `visor/` directory

## Visor Changelog

### 1.0.0 -- 2016.09.16

* Initial release

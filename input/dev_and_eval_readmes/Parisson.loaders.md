## loaders

> AudioBuffer loader and other loader utilities module

### Example

Load loaders.js in your html file by using:

```html
    <script src="loaders.js"></script>
```

```js
  // We need an audio context to decode the file
  // By default,the loaders search for audioContext in the window.
  var audioContext = new AudioContext();

  // Load the file passing the path
  var myAudioBufferLoader = new loaders.AudioBufferLoader();
  myAudioBufferLoader.progressCallback = function(obj){
    // Do something with the progress value obj
    // obj: {value:.., total:..., loaded:...}
    // value is loaded/total
  }
  myAudioBufferLoader.load('sound/file/url').then(
      function(buffer){
        // Do something with the loaded audio buffer
      },
      function(error){
        // Catch an error during the loading or decodeAudioData process
      }
  );

```

Use the same ```load``` method to load multiple files, by passing
an array of urls ['url/to/file1', 'url/to/file2', ...].
The progress is then an object, eg. {index: 4, value: 0.2, total:999, loaded:1},
where index corresponds to the file index in the array of files,
and value, between 0.0 and 1, corresponds to the file loading progress.

### Tests

Install all dependencies in the module folder

```bash
$ npm install
```

Run the test suite

```bash
$ npm test
```

It should launch a browser, run the tests in it, and generate the coverage report in the coverage folder.

### Status

This library is under heavy development and subject to change.
Every new API breaking change we will be adding snapshots to the repository so you can always fetch a working copy.

## License
This module is released under the [BSD-3-Clause license](http://opensource.org/licenses/BSD-3-Clause).

## Acknowledgments
This code is part of the [WAVE project](http://wave.ircam.fr),
funded by ANR (The French National Research Agency),
_ContInt_ program,
2012-2015.

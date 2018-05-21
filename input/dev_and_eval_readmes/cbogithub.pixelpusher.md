pixelpusher
===========

Generative and audio-controlled LED patterns for openpixelcontrol

The pixelpusher project is a suite of Python modules to generate
artistic LED patterns. Generated patterns are piped to LED hardware
via zestyping's [openpixelcontrol](https://github.com/zestyping/openpixelcontrol).

![pixelpusher block diagram](https://raw2.github.com/headrotor/pixelpusher/master/docs/pixelpusher-block.png)

All code is pure python.

The generative.py module contains subclasses that implement several
iterative algorithms for generating patterns on a 2D grid. Parameters and boundary conditions can be changed in real-time, for example by using OSC (Open Sound Control) GUIs from a smartphone. 

The audiomunger module uses PyAudio bindings to PortAudio for audio
input, and NumPy FFT to compute the short-term power spectral
density. These can be used to generate a running spectrogram display
or patched in to control other generative patterns.

Current status is **EXTREMELY ALPHA** and while I'm working on it I've checked it in more for backup than for sharing. I will let you know when that changes!

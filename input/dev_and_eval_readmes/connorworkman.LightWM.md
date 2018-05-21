# LightWM
A lightweight window manager for the X window system.

Dependencies:
The example xinitrc file provided makes calls to launch X clients within the window manager.  Therefore, these X clients need to be already installed on your system: xeyes, xclock, xterm.
In order to run the window manager as a client in your current window manager, you'll need xephyr and scons.


There are two options for using this X window manager.
Option 1 is to compile the program by installing scons and running the ./build_and_run.sh file without xephyr by setting it as your native window manager (you can use the provided xinitrc file to replace ~/.xinitrc).
Option 2 is to install scons, and use xephyr to run the window manager from within your current X session.   It is assumed that the program will be tested before use, so this is the default setting for the build_and_run.sh script. 

Execution:
Execute the build_and_run.sh file to Make and connect the window manager to the X server as an X client.

./build_and_run.sh

Once scons compiles our program, xephyr launches a few programs inside of the new window manager.

Congratulations on making it this far! If you had problems installing LightWM see the toubleshooting section at the end of this readme.

Commands:

Close (kill) a window: ALT + Q

Move a window: Hold ALT and select a window with the mouse. Drag to reposition. Release mouse to stop.

Launch a new xterm window as a child process: ALT + Enter

Cycle top window focus: ALT + Tab

And of course, feel free to launch any program via xterm.

Troubleshooting:
Make sure to install xorg-xeyes, xorg-xclock, xterm, xephyr (unless using lightWM as primary window manager), and scons with your operating system's package manager.
LightWM does not support multiple monitor X configurations, and may be unable to load xorg.conf configuration files with multiple screens.

Restart My Fox
==============

Download this addon from [addons.mozilla.org] (https://addons.mozilla.org/en-US/firefox/addon/restart-my-fox)

Source Code Repository For Restart My Fox

Source code released under [MPL 2.0] (https://www.mozilla.org/MPL/2.0/)


#### What it does: 

Adds to `appMenu (Legacy)` or `ToolsMenu` or `Tool-bar`, The Restart Browser menu item or Button that allows 
users to easily restart the web browser without losing current open pages.

### About this Add-on:

- Allows users to easily restart the web browser.
- Keep all open pages.
- Great if a plugin has stopped working and a restart is required to re-enable it.
- Good when a script on a page causes multiple errors in the browser.
- Excellent for when browser ram usage is really high.

Allows you to clear the browsers fast restart cache.


###  To build (Platform):

- `Windows:` __CTRL + SHIFT + B__
- `Linux:` __CTRL + SHIFT + B__
- `Mac:` __CMD + SHIFT + B__


#### Task Runner (Visual Studio Code):

- `Windows:` __CTRL + SHIFT + P__
- `Linux:` __CTRL + SHIFT + P__
- `Mac:` __CMD + SHIFT + P__

| Task | Command | Result |
|----------|:-------------:|------:|
| Build | task build | Builds addon *.xpi |

##### You must set the version number in the arguments field of tasks.json when bumping the XPI package version.


#### Build Notes (Visual Studio Code) (Platform):

- `Windows:` You must have __python 2.7__ or higher installed to run the build script.
- `Linux:` You must on the __`build.py`__ set in its properties permissions tab, To allow execution or __`EACCESS`__ error will ensue.

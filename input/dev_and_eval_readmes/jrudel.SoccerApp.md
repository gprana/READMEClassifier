Blank HTML App Designer Template for Building Packaged Mobile Web Apps
======================================================================

Copyright © 2012-2015, Intel Corporation. All rights reserved.

See [LICENSE.md](<LICENSE.md>) for license terms and conditions.

Use this template as a starting point for an Intel XDK App Designer project that
will be distributed as a *packaged mobile web app*. The file named `init-dev.js`
included as part of this project contains init code that generates an
`app.Ready` event; which is used as a way to normalize how App Designer starts
its own code. This technique allows App Designer to use a standard init sequence
regardless of the specific package type (a *packaged web app* or a *Cordova web
app*).

The `icon.png` and `screenshot.png` files are not required by your project. They
are included for use by the Intel XDK template/demo panel and have no use within
a real app. You can safely delete them from your project directory.

You can build a *packaged Cordova web app* from this template that can be
submitted to a store using the "Cordova Hybrid Mobile App Platforms” build tiles
(for Crosswalk, Android, iOS and Windows). The `intelxdk.config.additions.xml`
file can be used to include options that control your *packaged Cordova web app*
builds. For example, you can set the splash screen display time for a packaged
Android or Crosswalk Cordova app using this file.

Do not be alarmed if you see a "*Failed to load resource:
net::ERR\_FILE\_NOT\_FOUND*" message caused by the `cordova.js` script in your
`index.html` file. The `cordova.js` script is *only required* if you choose to
convert your "Standard HTML5 Project" into a "Standard HTML5 + Cordova Project."

You can:

-   safely ignore the "*Failed to load resource: net::ERR\_FILE\_NOT\_FOUND*"
    error message

or

-   comment out this script line if you will not be converting your project into
    a Cordova app that uses Cordova APIs.

The `cordova.js` script will be needed if you choose to convert your project to
a *Cordova project* and enhance your app with Cordova APIs. It is not required
to build a *Cordova packaged web app* for distribution via the Android, iOS and
Windows stores *if that app does not utilize Cordova APIs*.

This blank template does not require any Cordova APIs. If you would like to add
Cordova APIs to your application (via Cordova plugins) you must first convert
your project into a Cordova project. You can do this by clicking the Cordova
icon in the *Project Info* section on the **Projects** tab. Or, you can create a
new Cordova project using a Cordova blank template or a Cordova demo or sample
app as a starting point.

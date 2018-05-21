# Q

    Q is a community playlist app that allows users to share and manage a music playlist together in a group setting. With Q, a designated host can create a room in which other users can join. In this room, users and the host can collaborate on a playlist by searching for songs on Soundcloud and adding them to a playlist queue. The host has the ability to play, pause, skip, and delete songs on the playlist. Audio is only played through the hosts computer or device. You and the people around you can all use Q's server to search for music and manage the playlist together in REAL-TIME.

## Team

    Product Owner: Harun Davood
    Scrum Master: Joan Xie,
    Development Team Members: Spencer Gulbronson, Jaylum Chen

## Table of Contents

    1. [Usage](#Usage)
    2. [Requirements](#requirements)
    3. [Development](#development)
        3a. [Installing Dependencies](#installing-dependencies)
        3b. [Tasks](#tasks)
    4. [Team](#team)
    5. [Contributing](#contributing)

## Usage
    For Q to work properly, a designated host needs to login by clicking 'CREATE ROOM' on the login page and entering 'test' as the password. The host also needs to login before any other user adds a song to the queue; this is a known issue and flawed feature. Users who are not the host must click 'ENTER ROOM' to join the host's room. 

    Multiple rooms for different hosts is a feature that has not yet been developed. Ideally, a host should be able to create a room which will have a distinct URL has that the host can give to other users. Other users can use this url to access the host's playlist. 

    It was also concious decsion to enhace user experience to not handle strict authentication for users to make it easy and effortless for users to join and create rooms.

    TO start Q's server, first start mongodb server (mongod) and run npm start inside the project's main directory.

    Q uses soundcloud's API.  In the current implementation, we had the client ID visible in the front end, but in later iterations, this searching should be moved to and hidden in the backend.
    
    **Q uses ionic framework to enhance UI for mobile users: http://ionicframework.com/**

## Requirements

    npm modules----------------
    "bower": "^1.3.3",
    "body-parser": "^1.14.2",
    "express": "^4.13.3",
    "mongoose": "^4.3.4",
    "socket.io": "^1.4.0"

    bower-----------------------
    "ionic": "driftyco/ionic-bower#v1.1.1"
    "angular": "1.4.3",
    "angular-animate": "1.4.3",
    "angular-sanitize": "1.4.3",
    "angular-ui-router": "0.2.13"

## Development
(file structure: view in sublime or raw to see formatted structure)<br>
Q <br>
├── bower.json (bower components: installed in client/www/lib)<br>
├── client<br>
│   ├── config.xml (ionic config file x)<br>
│   ├── ionic.project (for ionic x)<br>
│   ├── scss<br>
│   │   └── ionic.app.scss (for ionic x)<br>
│   └── www<br>
│       ├── css<br>
│       │   └── style.css (main css file for custom styles)<br>
│       ├── img<br>
│       │   ├── icon2.png (main logo)<br>
│       │   ├── icon.png (alternative logo)<br>
│       │   ├── ionic.png (ionic logo)<br>
│       │   ├── logoQ.png (large main logo)<br>
│       │   ├── notavailable.gif (image unavailable soundcloud image)<br>
│       │   ├── notavailable.jpg (image unavailable soundcloud image)<br>
│       │   ├── notavailable.png (image unavailable soundcloud image)<br>
│       │   └── playing.gif<br>
│       ├── index.html (main index file)<br>
│       ├── js<br>
│       │   ├── angular-soundmanager2-Q.js (soundplayer with socket config)<br>
│       │   ├── app.js (font-end main js)<br>
│       │   ├── controllers.js <br>
│       │   └── services.js<br>
│       ├── lib<br>
│       │   └── angular-soundmanager2<br>
│       │       └── dist<br>
│       │           └── angular-soundmanager2-Q.js (original untouched)<br>
│       └── templates<br>
│           ├── landingPage.html (landing page)<br>
│           └── playlist.html (playlist index)<br>
├── _CONTRIBUTING.md<br>
├── _.editorconfig<br>
├── _.gitattributes<br>
├── _.gitignore<br>
├── _.jshintrc<br>
├── package.json<br>
├── _PRESS-RELEASE.md<br>
├── Procfile<br>
├── _README.md<br>
├── server<br>
│   ├── db<br>
│   │   ├── dbConfig.js<br>
│   │   ├── userController.js<br>
│   │   └── userModel.js<br>
│   ├── README.txt<br>
│   ├── routes.js (server routing)<br>
│   ├── server.js (main server)<br>
│   └── test.html (not used)<br>
├── _STYLE-GUIDE.md<br>
└── _.travis.yml<br>


## Installing Dependencies

    From within the root directory:
    sudo npm install -g bower
    npm install
    bower install
    run bower install

## Roadmap

        View the project roadmap www.github.com/mightychondria/Q/issues


## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

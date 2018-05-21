# Blackjack

This is a simple blackjack server over WebSockets that leverages the Simple Text Oriented Messaging Protocol (STOMP). You will need to create a client in order to interface with the blackjack server. The server is written using Java 8, so if you wish to run this locally, you'll need to have Java 8 or greater installed.

## Purpose

The server was written as an entrance exercise for potential intern candidates and test their critical thinking, coding skill, ability to parse messages and leverage APIs, and competitiveness by putting their clients up against other interns' clients. But most importantly, it's written with the idea to have fun!

The goal of the challenge is to create a working client that can run through several hands against the dealer without any hiccups. Once you have a basic client working, if time allows, try to add strategy to your player to improve its performance and beat other clients.

## Blackjack Resources and Strategy

NOTE: The below link may not work. You can refer to that page [here](https://docs.google.com/document/d/1pPEeLRDnpuYQH7r22RZn7h4Qkxr7_YzSbjSUzMNt42k/edit)

If you are unfamiliar with blackjack, try starting [here](http://wizardofodds.com/games/blackjack/basics/#toc-Rules). Hint: Even if you do know all the rules, the website is VERY useful for all kinds of strategy and tips. In fact, it would be beneficial to take advantage of everything the website has to offer.

## Requirements 
* Git
	* You could of course just download this source code directly if you don't want have time to download git.
	* If you don't have git installed, you can download it [here](https://git-scm.com/download/)
* Java 8 or greater
	* You can test this by running `java --version` in your terminal to tell what java version, if any, is installed on your computer
	* NOTE: Java 8 is only required if you would like to run the server locally for testing purposes. If not, don't fret! There will be test servers you can use to test if you don't have Java 8 installed.

## Blackjack Client Code
You won't be changing any code on the server. Instead, you will have a client that you'll need to implement logic for in order to interact with the server. Luckily for you, the websocket configuration part is already done, all you need to do is write the logic to register into the game, make bets, and act on your hand. There are two versions of the client that you can find here:

  * Java: [https://github.com/chadtomas/BlackjackClient](https://github.com/chadtomas/BlackjackClient)
  * Python: [https://github.com/chadtomas/PythonBlackjackClient](https://github.com/chadtomas/PythonBlackjackClient)

## Quick'n'Dirty Server Startup
If you plan on running this locally, be sure you meet all the requirements above so that it will run properly.
* Locate the .jar file located in the `target/` folder.
* From the terminal, you can run `java -jar {jar_name}.jar`. This starts the server on an embedded Tomcat instance on port 8080. If you'd like to change the default port on startup, you can append `--server.port={desired port number}` at the end of java command.
* Once the server is started up, you can hit the UI at localhost:8080, where you can either connect to the server and manually play blackjack or connect your client and watch it communicate with the server.

## Rules
Here are the current rules that are enforced by the blackjack server:
* Two Deck Blackjack
* Blackjack Pays 3:2
* Support for up to 4 players
* Cut Card with ~70% Penetration
* Players start with $1000 in chips
* If you lose all your money, you are done
* Bet increments of $10 with no upper betting limit
* Dealer Stands on Soft 17
* No Insurance
* Surrender Allowed on First Two Cards (including after splitting)
* Dealer Peeks for Blackjack
* Aces Split Only Once
* Split up to Four Hands (except Aces)
* Double After Splitting Allowed (except Aces)

## Subscriptions

WebSockets allow for two-way communication between the server and clients. When a message is received by the server from any clients, it will send back a response to different subscription destinations. The most important message destinations are described below:

* `/topic/game` The main destination for all game info. Any messages sent from here is broadcasted to all clients currently connected to the server. Messages sent to this destination will usually be triggered from clients sending their bets and players sending their actions.
* `/queue/player` Messages sent here are only sent to the client that sent a message to an endpoint on the server whose message destination is here. This will be especially important to listen to when your client first registers to play blackjack. During registration, you'll be assigned a secret playerId which is sent to only you, and you'll need to keep track of this playerId to perform any actions and play any hands.
* `/queue/errors` If your client sent an invalid message (such as betting when a hand is already in progress or attempting an invalid action on a hand), an error code and an error message will be sent to this queue, which is only sent to the offending client. You may want to consider handling various errors in case your client commits an invalid message. Any unhandled errors committed by your client will hold up the game and could result in a disqualification of the hand or even the game. Possible error messages will be discussed in a later section.

## API Reference

### /register
#### Attempts to register a player into the current game

##### Expects: 
```json
{
   "name":"Zangief"
}
```
This is the name that you will register into the game with. Choose wisely as you won't be able to change this.

##### Returns:
```json
{  
   "playerId":"2f658c62-89c2-4a2d-8839-fa56343d5f0d",
   "name":"Zangief",
   "seatNum":1,
   "chips":1000,
   "active":true
}
```
The most important field in the return object is the `playerId`. This is your secret key that's given to you and only you! Guard this with your life and make sure you store it somewhere or you'll never be able to play a hand. The `active` field should always be true. It is only set to false when you no longer have enough chips to play another hand or an admin sets it manually if your client isn't behaving normally.

### /unregister
#### Attempts to unregister a player from the current game

##### Expects:
```json
{
   "playerId":"2f658c62-89c2-4a2d-8839-fa56343d5f0d"
}
```

### /bet
#### Attempts to place a bet on the next hand for a player

##### Expects:
```json
{
   "playerId":"a2bfc615-6a30-4cc2-b172-771e10ae5e66",
   "betAmount":450
}
```
Use the player id that was given to you. `betAmount` is the amount you want to place on your next hand.

### /action
#### Attempts to send an action to be executed on a given hand

##### Expects:
```json
{
   "playerId":"a2bfc615-6a30-4cc2-b172-771e10ae5e66",
   "action":"HIT",
   "handNum":0
}
```
The `action` is an enum that tells the server what action you want to perform on a given hand. Possible actions include `HIT`, `STAND`, `SURRENDER`, `DOUBLE`, `SPLIT`. Refer to the Rules section of this guide to determine when you can perform these actions. `handNum` is the index (zero-based) in that player's `hand` array that you want to perform the action on. For example, if you want to hit on your original hand, `handNum` would be 0. The only time `handNum` will not be 0 is you've split a hand and want to act on the second hand after a split. In which case, `handNum` would be 1 in that specific case, but could be anywhere between 0 and 3.

##### Returns:
```json
{
   "players":[
      {
         "name":"Blanka",
         "seatNum":1,
         "chips":550,
         "hands":[
            {
               "betAmount":450,
               "cards":[
                  {
                     "rank":"THREE",
                     "suit":"DIAMONDS",
                     "cardValue":3,
                     "alias":"3"
                  },
                  {
                     "rank":"FOUR",
                     "suit":"HEARTS",
                     "cardValue":4,
                     "alias":"4"
                  },
                  {
                     "rank":"JACK",
                     "suit":"SPADES",
                     "cardValue":10,
                     "alias":"J"
                  }
               ],
               "result":null,
               "handStatus":"IN_PLAY",
               "turn":true,
               "handValue":17
            }
         ],
         "handsPlayed":1,
         "betInForNextRound":false,
         "active":true
      }
   ],
   "dealer":null,
   "dealerUpCard":{
      "rank":"TEN",
      "suit":"DIAMONDS",
      "cardValue":10,
      "alias":"T"
   },
   "gameStatus":"HAND_IN_PROGRESS",
   "lastAction":{
      "playerName":"Blanka",
      "action":"HIT"
   },
   "cardsLeftInDeck":99
}
```
You'll see there's a lot going on in this return object. Most of these are self-explanatory, but I'll go through some of the most important fields:
* `players` is an array of all the currently registered players in the order they were seated. Each `player` object has some useful info.
    * `hands` is an array associated to each player with all the hands (up to 4) that he's currently playing. There should only be one hand per player unless they performed a split.
        * The `result` in each `hand` object is null if the hand is currently in progress. After the hand is over and the hand is evaluated, it'll either be `WIN`, `PUSH`, or `LOSE`
        * The `handStatus` field in each `hand` object represents the current status of the hand. It is `IN_PLAY` if the hand has not busted, `BUST` if the hand value is over 21, `BLACKJACK` if you were dealt a blackjack, and `SURRENDER` if you decided to surrender for half your bet.
        * `turn` is a boolean that determines if it's that hand's turn to be acted on.
    * `betInForNextRound` is a boolean that will be set to `false` if a hand is currently in progress. This is used during a betting round to determine if that player has placed a bet for the upcoming hand, in which case, would be set to `true`.
* `dealer` will be null if the hand is in progress as it holds information on what cards are in the dealer's hand. During the hand, you can refer to the `dealerUpCard` field to see what his top card is. After everyone has acted on their hand, the `dealer` object will be present with information about the dealer and his hand, and the game status will then change to `BETTING_ROUND`
* `gameStatus` This will either be `HAND_IN_PROGRESS` or `BETTING_ROUND`. During the betting round, you can place bets. During a hand, only actions on the current hand to act will be accepted.

## Error Messages

There may be instances where a client will send an invalid message to the server, and the server will respond with an error message to the offending client with what caused the error to be sent. The entire list of errors is encompassed in the `BlackjackErrorCode.java` file. For convenience, here's a list of what each error code means and why you may have gotten the error.

* BJ1xx - Error codes in the 100's represent betting errors
    * `BJ101` - The bet amount being sent is more than what the player can afford
    * `BJ102` - You've already made a bet for the current hand
    * `BJ105` - You can't place a bet at this time because there is already a hand in progress
    * `BJ110` - Bet must be in increments of 10
* BJ5xx - Error codes in the 500's represent player errors
    * `BJ500` - The game is at max capacity and cannot register another player
    * `BJ550` - Unable to process an action due to an invalid player id
    * `BJ570` - Unable to place a bet because the player's status is currently Inactive. It is only sent to Inactive by the admin, and can only be switched back to Active by an admin
* BJ7xx - Error codes in the 700's represent in-game action errors
    * `BJ700` - You send an action for a hand, but it is the betting round
    * `BJ701` - The hand number you want to act on does not exist for the given player
    * `BJ720` - You attempted to double down on a hand that was not eligible for a double down
    * `BJ730` - You attempted to surrender a hand that was not eligible for a surrender
    * `BJ740` - You attempted to split a hand that was not eligible for a split
    * `BJ799` - You are attempting to act on a hand when it is not your turn to act
* BJ9xx - Error codes in the 900's are reserved for the Trebek admin panel and should never be sent to clients. If you see an error in the 900's, you're probably accessing endpoints you shouldn't be hitting

## What is Trebek?

While perusing the source code for the Blackjack server, you may notice references to Trebek and might be wondering what it is in the first place. Trebek is the admin panel for the blackjack server that has access to override hands and kick players out of the game. The endpoints and logic is intentionally left out of Git since it should only be used by those administering the exercise (although if you're resourceful enough, you could find these endpoints and use them, but please don't). Any illegal use of Trebek could result in disqualification. If you are administrating the Blackjack server and need the source code for the Trebek panel, please contact Chad Tomas.

## Final Thoughts

Depending on time at the end of the exercise, the idea would be to have four clients at a time going up against each other for a certain number of hands or a certain amount of time. At the end of the given time, the two highest earning clients in that session advance to the next round. The process will repeat until we have 4 clients left, and the highest earner in that final session wins. Note: Winning does not guarantee an internship, but it could be taken into consideration, so try your best.

As far as blackjack strategy goes, take advantage of the internet and any other sources you can get your hands on in the allotted time. As a hint, you should consider looking into implementing basic strategy once your client can play the game. Then if there's time, you might even look into card counting and betting strategies. If you're reading this and writing a client, chances are you're a potential intern candidate. Meaning you're probably in Vegas. There will be people in the room who live and breathe blackjack including myself, so feel free to ask questions on strategy or programming.

With all that being said, the server is not fool-proof. It was written by one engineer in the span of a week. Meaning, things haven't been fully tested and may have sparse documentation due to time constraints. So, if you look hard enough, you may find some loop holes in the source code that might give you an advantage in one way or another. Use whatever you can to gain an advantage, but also consider the ethics of the situation before doing anything that could critically make the game less fun for everyone else.

If you have any questions regarding the project, feel free to contact me. And lastly...

### Have fun!

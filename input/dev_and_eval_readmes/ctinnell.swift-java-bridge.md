# swift-java-bridge
Execute Java Code from a Swift Cocoa Application 

## Overview 
This project demonstrates using a Cocoa Application to execute queries against a remote database.  This sample Cocoa application will launch a JVM, import DB2 JDBC drivers into the classpath, and communicate through JNI using C to a Java class that connects to a DB2 database and executes queries.  The Cocoa application is written in Swift, but accesses Objective-C methods to connect and execute the queries.

## Disclaimer
Any project that mixes Cocoa, C, Java, JNI, JDBC, Objectice-C, and Swift has to be fun, right?  This project isn't really meant to be used for anything yet other than to demonstrate how these technologies can be used together to do powerful things.  My frustration with the lack of database connectivity in Cocoa may drive me to package this up in a nice framework some day.

## License
Copyright (c) 2015 Clay Tinnell.

Use of the code provided on this repository is subject to the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

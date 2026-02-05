---
title: "Script Writing Lesson 1: Compacting FileMaker Scripts - Making Your Code More Readable By Humans"
pubDate: "2013-01-22T16:36:40+00:00"
updatedDate: "2018-07-23T21:29:55+00:00"
author: "Agnes Riley"
tags: ["Blog"]
permalink: /compacting-filemaker-scripts/
---

We could discuss at length what we should and what we should not do while writing a FileMaker script. If you’re an expert you have your own opinion on this, if you’re a newbie, you can be overwhelmed with all the opinions the experts have. Not to fear, I’m not here to argue points or overwhelm the newbies (which I was at some point and I did find a lot of things overwhelming). This post is simply there to remind you of some best practices in script writing and help you get your scripts:

  1. a little more compact
  2. more readable and
  3. easier to debug (if you have FileMaker Pro Advanced, you can use the debugger and data viewer to see what your script does).



The script below uses functions from the [24U SimpleDialog](https://24usoftware.com/SimpleDialog "SimpleDialog") Plug-in, which I use often to produce dialogs, because it extends dialog capabilities in FileMaker beyond the basics. First and foremost, pay attention to the first couple of lines. For your own, but especially for other developer’s sake, use some space at the top to introduce your script and let people know who wrote it and when. If you make significant cahnges later, it might help to fill out the “modified by” section, as well. I capture the errors, so in case I need to do some error logging, I can do that. I perhaps will talk in anther post about error logging. Every section in the script has a note on it, so I can tell later what exactly each section is for. This is not a crazy long script. I’ve seen scripts that took literally so long to debug that I forgot what it did by the time I got to the end. BAD, BAD, BAD. Ok, so I’ll let you read through the script and see you when you’re done. (It’s only 4 pages; hopefully it won’t take you too long.)

  * ![](/wp-content/uploads/2013/01/script_example_tfi2.jpg)

  * ![](/wp-content/uploads/2013/01/script_example_tfi.jpg)

  * ![](/wp-content/uploads/2013/01/script_example_tfi3.jpg)

  * ![](/wp-content/uploads/2013/01/script_example_tfi4.jpg)




[Previous](index.html#prev)[Next](index.html#next)

[1](index.html#1)[2](index.html#2)[3](index.html#3)[4](index.html#4)

So, what do you think? My brother and I threw this script together for one of our clients. The goal was to be able to guide users to generate a list based on certain criteria and then let then choose an output method, then generate a file. Simple, right? I don’t believe the above is a bad script. Not because I’m bias, but rather because I’ve written and seen long scripts. A long script is also not necessarily a bad script. A bad script is one that doesn’t function well or leaves room for error. A long script is just hard to read, decode and hard to debug. Imagine a 1000-line script where you just want to test something on line 900. You’d have to either ignore the first 899 lines and put a marker in (in which case you don’t know if things are happening as they supposed to be.)
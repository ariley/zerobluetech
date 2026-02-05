---
title: "Getting Data From WordPress To FileMaker II"
description: "In my previous post, Getting Data from a WordPress to FileMaker I detailed how you can get mySQL data (that perhaps comes from a WordPress form submission) into FileMaker. This time I’ll write about…"
pubDate: "2015-04-16T12:00:03+00:00"
updatedDate: "2015-07-15T20:14:42+00:00"
heroImage: "/wp-content/uploads/2015/04/Screen-Shot-2015-04-15-at-6.45.02-PM-300x24.png"
author: "Agnes Riley"
tags: ["Advanced", "Developer", "Skill Set", "Tips & Tricks"]
permalink: /getting-data-from-wordpress-to-filemaker-ii/
---

In my previous post, [Getting Data from a WordPress to FileMaker](../getting-data-from-wordpress-to-filemaker/index.html "Getting Data from WordPress to FileMaker") I detailed how you can get mySQL data (that perhaps comes from a WordPress form submission) into FileMaker.

  
  


This time I’ll write about how you get that data into your own FileMaker table.

  
  


I recommend “importing” the data from the mySQL database into a temporary table. We called ours APPLICANTI_TEMP. It contains the same exact fields as the mySQL database and it is there so you can identify records in between the two tables. So in my case the fields are text fields, just like in the mySQL DB (even the timestamp). But then we added a timestamp field that is a regular FileMaker TimeStamp and when we run the scripts we set this with the proper FM TimeStamp.  
  
  


I added two calculations:

  1. One that checks whether the record we are viewing exists in the mySQL table and
  2. Another one that checks whether we have added the record to our APPLICANT table.



  
  


[![Screen Shot 2015-04-15 at 6.45.02 PM](/wp-content/uploads/2015/04/Screen-Shot-2015-04-15-at-6.45.02-PM-300x24.png)](/wp-content/uploads/2015/04/Screen-Shot-2015-04-15-at-6.45.02-PM.png)

  
  


These calculations are quite limited but in my case achieve the wanted result. I am not too worried about someone modifying the records in the mySQL table, because I’m the only one with access to it. But you’ll have to make decisions based on what’s best for you. I, however wanted to make sure I’m not creating the same record several times in the APPLICANT table. Well, we still are, because people apparently fill out and submit the form (sometimes with mismatched information?!?) several times. So at the end of the day you’ll still need a human to identify if a second record has a misspelled last name or it is, indeed a different applicant. But in case you have a scenario that disallows record deletion based on some criteria, you’ll need to develop a more refined logic.

  
  


I have already converted my SQL TimeStamp to a FileMaker readable timestamp, but if you don’t do that in your Query you’ll have to do that in FileMaker. Bring Dunning’s Custom Functions collections is always a good place to start looking for handy custom functions.

  
  


[![Screen Shot 2015-04-15 at 7.07.08 PM](/wp-content/uploads/2015/04/Screen-Shot-2015-04-15-at-7.07.08-PM-300x241.png)](/wp-content/uploads/2015/04/Screen-Shot-2015-04-15-at-7.07.08-PM.png)  
  
  


We have a set of scripts that perform the data move (because it’s not really an import). They loop through a set of fields on a layout record by record and create the record in the TEMP table, then the APPLICANT table. These scripts are run from the server every 15 minutes. You set your time interval based on your own process.  
  
  


The first step is to refresh the data from the mySQL database, because unless you do that any new submissions from the web (in my case) will now show in FileMaker:

  
  


[![Screen Shot 2015-04-15 at 7.10.51 PM](/wp-content/uploads/2015/04/Screen-Shot-2015-04-15-at-7.10.51-PM-300x215.png)](/wp-content/uploads/2015/04/Screen-Shot-2015-04-15-at-7.10.51-PM.png)

  
  


Before running scripts from the server, always make sure you test the hell out of them locally first. [Here’s](../filemaker-server-side-scripting/index.html "FileMaker Server-side Scripting") an article on server-side scripts in general. I always recommend adding a LOG table, and put in error checking in your scripts, especially when you’re running them from the server. You DO NOT have a debugger on server. And who wants to code blindly?!

  
  


And if you’re lucky—like us—you’ll have to parse the data into different tables, because you’re dealing with parents, addresses and phone numbers. You’d obviously want to do that from the TEMP table record.

Hope this covers it all. Any questions, feel free to ask.
---
title: "Importing RSS Feed Into FileMaker with XSLT"
description: "Per popular request I am revisiting this article. I made some edits and also now you can download the the demo file. Someone sent an email to our FileMaker group to request information about importing…"
pubDate: "2009-02-24T07:49:40+00:00"
updatedDate: "2015-06-08T15:35:07+00:00"
heroImage: "/wp-content/uploads/2009/02/rss-example-1024x595.png"
author: "Agnes Riley"
tags: ["Advanced", "Blog"]
permalink: /importing-rss-feed-into-filemaker-with-xslt/
---

## Update:

Per popular request I am revisiting this article. I made some edits and also now you can [download](https://zerobluetech.com/docs/MarketNews.fp7 "MarketNews.fp7") the the demo file.

Someone sent an email to our FileMaker group to request information about importing RSS feed into FileMaker. Since I have done this and it’s actually quite easy, I thought I’d post the method here.

#### Ingredients

  1. FileMaker (8.5 or later because you need Web Viewer);
  2. A FileMaker database ;
  3. An [XSLT style sheet](https://zerobluetech.com/docs/rss2fmp.xsl "Right-click to download the file"); (I found this style sheet somewhere some time ago; didn’t write it myself)
  4. A web host where you can post the XSLT file;
  5. An RSS feed that actually works with this (e.g. Yahoo Stocks: https://rss.news.yahoo.com/rss/stocks);
  6. A script that pulls the info (which now can be run on server if you have FMS 9 or 10);
  7. A table in your DB for storing the RSS feeds;
  8. A portal on your layout that shows the list of RSS feeds;
  9. A web viewer in your database that can display the resulted web page;
  10. A script that tells the web viewer to show the requested article.



#### [![](/wp-content/uploads/2009/02/rss-example-1024x595.png)](/wp-content/uploads/2009/02/rss-example.png)

#### Directions

  1. Create a new table called ‘RSS_Feed’ in your solution (since this only works in FM 8.5 and later, there’s no need for a separate file). Create the following fields: ID, Title, Description, Link, PubDate, SelectedLink;
  2. Link the new table to your preferred table (Global, Solution, etc.) by showing all records (‘x’ symbol);
  3. Create a new layout in your solution, place a portal on it showing the records from the RSS Feed table (link and description fields, minimum). Place a web viewer next to it. Name your web viewer object “article”;
  4. Create a script similar to this example to refresh the feed (you can run this script from a button on your layout or at certain intervals from the server):


    
    
    Go to Layout [ "Layout Name" (Table Name) ] Enter Browse Mode Show All Records Delete All Records [ No dialog ] Import Records [ XML (from http): https://rss.news.yahoo.com/rss/stocks; XSL (from http): https://www.website.com/folder/rss2fmp.xsl ] [ No dialog ] Go to Layout [ original layout ] 

  1. Create a script for showing the article:


    
    
     Set Field [ RSS_Feed::SelectedLink; RSS_Feed::Link ] Set Web Viewer [ Object Name: "article"; URL: RSS_Feed::SelectedLink ] 

  1. Turn your title field on your portal into a button and link to perform the script above.



This is most likely not the only method; it may not be the best method either. It is, however a working method.

Any questions, suggestions, feel free to respond.
---
title: "FileMaker and PHP: Link to A Record Using Redirect"
description: "In this article we’ll look at how you can link to a record using redirect with FileMaker and PHP. In later versions of FileMaker we have Snapshot Links. When you work in a database you can always give…"
pubDate: "2015-04-22T12:00:41+00:00"
updatedDate: "2015-06-08T16:41:18+00:00"
author: "Agnes Riley"
tags: ["Advanced", "Developer", "Skill Set"]
permalink: /filemaker-and-php-link-to-a-record-using-redirect/
---

## Let’s Learn How We Can Link to A Record Using Redirect

In this article we’ll look at how you can link to a record using redirect with FileMaker and PHP.

In later versions of FileMaker we have Snapshot Links. When you work in a database you can always give someone a Project number when you need to refer to a Project. Or we can script generating a Snapshot Link. The problem with the Snapshot link is that you’ll have to remove it once you spit it out to the Desktop. AppleScript can help with that.

Another method is the [fmpURL protocol](https://www.filemaker.com/help/12/fmp/html/sharing_data.16.7.html). You can generate nice links such as this:

> fmp://localhost.com/SomeDB.fmp12?script=open_project_link&param=PROJECTID

Then if you copy and paste this into apps it’ll open the database. If you’re on a Mac and use Messages or email this is great!

But then I ran into a problem where my client’s law firm relies on Gmail for their primary communication AND they are using it from a web browser. Now, Gmail DOT NOT know what to do with the FMP protocol so it just breaks the URL and funky things happen. I’m sure Gmail is not the only party here that does not know what to do with it.

So one—fairly simple method—of tackling the problem is referring to good old, creating a link to a record in FileMaker with PHP. I know, this is not a novel method but when I was looking for it I couldn’t find a comprehensive article on how to achieve what I want.

#### What you need:

  1. A web server
  2. A PHP file
  3. A script in FM that will know what to do with the parameter it receives
  4. A button on the layout to run another script to generate the appropriate link to call your redirect PHP



Any web server anywhere will do. You just need to place a very simple redirect PHP file on it. Name it “redirect.php and place it in the appropriate document folder of the web server. Make sure the file has the proper (read, execute) permissions.

#### The PHP file:

> <?php
> 
> //gets the query string for the value of ‘project’
> 
> $project=$_GET[‘project’];
> 
> //concats url with ID from query string.
> 
> $url = “fmp://YOUR_FM_SERVER/Database.fmp12?script=SOME_SCRIPT&param=” . $project;
> 
> //redirects to new page.
> 
> header(“Location: ” . $url);
> 
> ?>

#### The FileMaker Scripts

  1. You need a simple script that the PHP file will call. It will need to define the received parameter and perhaps search for the aforementioned project by ID. Obviously the script can do more, depending on your business process.
  2. And the script that calls your redirect.php on the webserver. It should generate and copy your link to the clipboard:  


> https://YOUR_WEB_SERVER/redirect.php?project=PROJECTID




Then that link can be pasted anywhere and will be clickable.
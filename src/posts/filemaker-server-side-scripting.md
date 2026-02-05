---
title: "FileMaker Server-side Scripting"
description: "Running scripts from FileMaker Server can dramatically reduce execution time. I have been an avid fan of server-side scripting since it was introduced in FileMaker 9. Now, with the introduction of…"
pubDate: "2010-07-28T09:44:30+00:00"
updatedDate: "2015-06-08T15:26:38+00:00"
author: "Agnes Riley"
tags: ["Advanced", "Blog"]
permalink: /filemaker-server-side-scripting/
---

Running scripts from **FileMaker Server** can dramatically reduce execution time. I have been an avid fan of server-side scripting since it was introduced in FileMaker 9. Now, with the introduction of [FileMaker Go ](../filemaker-go.html) it is more important to take the burden away from the client and do as much processing on the server as possible. There’s no need to bog down a client when the server can take care of the task in the fraction of the time it takes to run from client. You can use server side scripting to automate record updates from external sources, prepare those pesky Monday morning reports so they are printed by the time everyone comes in or simply use it to update stored data instead of using calculations.

You can run **FileMaker** scripts or**System Level Scripts** or even combine them to run a script sequence now! This article deals with FileMaker scripting.

We tend to think, now that we have this feature, we can just build our scripts, run them from server and be done. This isn’t quite true…we have to follow up with the all-important troubleshooting period. At least in my experience, there is no server-proof script that can be installed on a server without further testing and digging and modifications.

So, I collected some pointers from my–and fellow FileMaker developers’–experience that might help you speed up your development when running scripts from server. Don’t be discouraged. You will be happy with the results. Jump in and put some of those tedious scripts on the server, so you and your users can forget about them.

#### Things to know:

  * Make sure all your script steps are server compatible (choose “Server” under “Show Compatibility”–bottom left corner of “Manage Scripts”).
  * The server runs the opening and closing routines, so you might want to revise your “onOpen” and “onClose” script to bypass some steps that are not relevant to the server.*
  * Globals are set. This may not be an issue, but might be worth paying attention to.
  * No need to script opening a new window, because the server does not execute the scripts from physical windows, but rather a virtual space.
  * If you are referring to an external file in Manage/External Data Sources, folder names have to be hard-coded in the string (such as file:/folder name/folder name/file name.fp7 or filewin:/ if you are on Windows Server).
  * Import locations can only be either: 
    * the **Documents** folder within the Data folder under the FileMaker Server root on your server machine (you can use Get ( DocumentsPath) to get you the right path; Windows users, don’t forget to use the “filewin” prefix);
    * the **Temp folder**(you can use Get ( TemporaryPath) and see the notes above).
  * Watch the log after you set your script to run, it can only help you!
  * Set up notification emails so you can be aware if something went wrong (you can turn these off after awhile).
  * Errors reported are FileMaker errors, not server errors.



#### Some caveats:

  * Lack of instant feedback. Even though you test until death locally, new problems can arise when running from server. Put in error checking after every step. I would also highly recommend logging script times.
  * You have to disconnect the client that runs the server script if a script hangs.
  * The script will hang if you forget to put in the “Perform Find” script step (possibly other actions or lack of them can hang the script, as well).



That’s it for now, but I will be adding to this article, so feel free to check back on occasion.

* I usually set up an account called “fmserver” to run the scheduled scripts with. Then I edit my onOpen script to bypass the opening routine if the account is fmserver. That can cut down on time and avoid unnecessary script steps.

Credit: Steven Blackwell, Todd Geist
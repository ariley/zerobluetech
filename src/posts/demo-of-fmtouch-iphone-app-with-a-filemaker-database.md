---
title: "Demo of the FMTouch iPhone App with a FileMaker database"
description: "Photo by Sandy Hechtman December 11, 2008: Agnes Riley presented a FileMaker-made-mobile solution to the members of the New York Motion Picture Collective and the New York FileMaker Developer Group."
pubDate: "2008-12-31T08:29:26+00:00"
updatedDate: "2015-06-08T15:35:41+00:00"
heroImage: "/images/2008/12/agnes-riley-fmtouch-presentation-300x228.png"
author: "Agnes Riley"
tags: ["Blog", "General"]
permalink: /demo-of-fmtouch-iphone-app-with-a-filemaker-database/
---

[![](/images/2008/12/agnes-riley-fmtouch-presentation-300x228.png)](/images/2008/12/agnes-riley-fmtouch-presentation.png)

Photo by [Sandy Hechtman](https://www.sandyhechtman.com)

**December 11, 2008** : [Agnes Riley](../agnes-riley/index.html) presented a FileMaker-made-mobile solution to the members of the New York Motion Picture Collective and the New York FileMaker Developer Group. The presentation demonstrated bringing a database from FileMaker to the iPhone through the use of **[FMTouch](https://www.fmtouch.com)**.

Click the images below to get a closer look:

[![](/images/2008/12/picture-1.png)](/images/2008/12/picture-1.png)

[![](/images/2008/12/picture-2.png)](/images/2008/12/picture-2.png)

[![](/images/2008/12/picture-3.png)](/images/2008/12/picture-3.png)

[![](/images/2008/12/picture-4.png)](/images/2008/12/picture-4.png)

[![](/images/2008/12/picture-5.png)](/images/2008/12/picture-5.png)

Click the image below to see the video:

[![](https://www.agiriley.com/images/FMTouchmovie.png)](https://www.agiriley.com/videos/FMTouchDemo3.mov)

Now, let’s look at how this is done. To get started with porting your own database to the iPhone or iPod Touch, you will need the following:

  * FileMaker Pro or Advanced 8-9;
  * An IPhone or iPod Touch (2.0 firmware);
  * [FMTouch](https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewSoftware?id=286468161&mt=8);
  * A Database Developer Report (DDR) of the file you intend to use. If you don?t have FileMaker Advanced, you can [use this solution](https://www.fmtouch.com/DDR);
  * [The sync plug-in](https://www.fmtouch.com/sync);
  * [The FMTouch User Guide](https://www.fmgateway.com/download/FMTouchUserGuide.pdf);
  * [FMTouch Style Guide and starter database for reference](https://www.fmpug.com/members_download.php?filename=FMTouchStyleGuide_v2.zip&free=true);
  * A pinch of patience.



It may seem daunting at first, but these simple steps will allow you to begin:

  1. Design your layouts you would like to use on the iPhone according to the style guide;
  2. [Buy FMTouch form the iTunes Store](https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewSoftware?id=286468161&mt=8);
  3. Download the synch plug-in and place it in your FileMaker?s extension folder, then restart FileMaker.
  4. Make sure the plug-in is enabled.
  5. Set up synching to your database on the iPhone (check the User?s Guide for more on this);
  6. Transfer DDR to iPhone;
  7. Name your Database;
  8. Initialize DDR;
  9. Choose the layouts you want to see;
  10. Re-initialize;
  11. Synch your database to get the data from the computer;
  12. Open your database.



Congratulations! Now that you have a FileMaker database working on an iPhone or iPod Touch, here is a list of tips and tricks that might be helpful to you, as well as observations to be mindful of as you move forward in your own development.

#### **LAYOUT DESIGN  
**

* You can design the layouts based on the example DB and provided style guide. Make sure you pay attention to scrolling with fingers. If you don?t want editable fields to get in the way of scrolling, make sure to lock them down.  
* With FMTouch you can show layouts in ?portrait? (vertical), ?landscape? (horizontal) or ?both? modes. The iPhone is not able to differentiate between layouts whether they are designed for portrait or landscape modes. So you cannot simply rotate the phone in the hope that it will switch to a different layout. So, at this point you?re better off locking FMTouch to either vertical or horizontal mode, which you can do if you go to ?Settings? after you click on the little ?i? on the bottom right.  
* Every time you change the layouts you would like to show, you have to reinitialize your solution.

#### **LABELS  
**

FMTouch is currently unable to show more than one line in a label showing text on the layout. You can, however, use two different workarounds:

  * You can type every line of text into a new label;
  * Or you can create a calculation field with the text you would like to show and place that on the layout.



#### **FIELDS  
**

You can use container fields in layouts, but they can only show a reference to an image. Only import the reference when you import an image; it will not show in FMTouch otherwise.

#### **SCRIPTING  
**

You can use the following script steps attached to a button on a layout:

  * Go to Layout*
  * Go to Record
  * New Record
  * Delete Record
  * Set Field
  * Go to related record.



* Note: You can use the ?GoToLayout? script step directly from a button, but you cannot use this script step as part of a script, because ?Perform Script? is not a supported script step.

Special thanks to Christina Tsao for her help with the database layouts.

[Downnload the instructions (PDF)  
](/images/2008/12/filemaker-and-fmtouch.pdf)

I hope this has been helpful.
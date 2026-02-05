---
title: "Clean Data in FileMaker"
description: "This is something I’ve bee dealing with for years. It hit me like a large hammer in the chest when one of my users replaced the contents of one field in about 5000 records with HTML she copied from…"
pubDate: "2015-03-31T12:00:08+00:00"
updatedDate: "2015-08-23T15:57:48+00:00"
heroImage: "/images/2015/03/03-27-2015-exhibit-a-300x242.png"
author: "Agnes Riley"
tags: ["Blog"]
permalink: /clean-data-in-filemaker/
---

## Achieving clean data in a FileMaker database is important

This is something I’ve bee dealing with for years. It hit me like a large hammer in the chest when one of my users replaced the contents of one field in about 5000 records with HTML she copied from the web. This was done accidentally, and clearly she felt so bad that she didn’t even tell me. This happened about 9 years ago.

I realized I had to put in some measures so this won’t happen EVER again. Now, you can think of every possible measure you can take and users can still surprise you. It’s similar to spam online. We keep getting smarter at how to deflect spam but spammers are always a step ahead.

Below are some things you can put in place to make sure your (their) data is as clean as it possibly can be.

#### Custom Menus

  1. Create a custom menu (or more) for certain situations (Exhibit A) 
     1. One menu for everyday use (and different menus for different levels of users);
     2. Another menu for when printing;
     3. Another menu for a layout that handles sensitive data.
  2. On every custom menu 
     1. Remove “Replace Field Contents” so users cannot accidentally replace records in fields
     2. Replace “Paste” with a script you write. The script should use Paste with remove style checked. (Exhibit B)



When you create a custom menu name it appropriately so you know what it is for.

#### Clean Your Field

  1. If you’re dealing with phone numbers you might want to format the phone number. You might even want to reject data that is not entered properly. So, e.g. phone numbers are 10 digits in the US, zip codes are always 5. So, the phone number field you can format to accept numbers and dashes only. The Filter function is great for this. The zip codes you need to lock down to allow 5 digits only (if the country is US) and no other characters but numbers.
  2. Use a custom function (or write it in a script but the custom function (Exhibit C) is easier) to strip off anything you don’t want, such as additional space, carriage returns and formatting (Exhibit D). Users have the tendency to hit enter after filling out a field. This is probably just a habit they picked up when working with Excel.
  3. When you’re generating reports, badly formatted data can drop off or look really strange (e.g. large letters in red). So whether you format your field nicely to Helvetica 10 on a report, if the data is messed up in the fields you’re not getting the proper result. The best thing? You’ll only know about this months down the line when the user complains that the report looks messed up.



[![03-27-2015-exhibit-a](/images/2015/03/03-27-2015-exhibit-a-300x242.png)](/images/2015/03/03-27-2015-exhibit-a.png)

Exhibit A

[![03-27-2015-exhibit-b](/images/2015/03/03-27-2015-exhibit-b-300x250.png)](/images/2015/03/03-27-2015-exhibit-b.png)

Exhibit B

[![03-27-2015-exhibit-c](/images/2015/03/03-27-2015-exhibit-c-300x250.png)](/images/2015/03/03-27-2015-exhibit-c.png)

Exhibit C

[![03-27-2015-exhibit-d](/images/2015/03/03-27-2015-exhibit-d-300x279.png)](/images/2015/03/03-27-2015-exhibit-d.png)

Exhibit D

Exhibit D shows Ray Cologon’s [Trim 4](https://www.briandunning.com/cf/166 "Trim 4 Custom Function") Custom function.  
  
Just to recap, clean data in FileMaker is as important as having a nice structure or a slick interface, if not more important, since we actually build the database for the users, not ourselves.
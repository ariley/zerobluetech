---
title: "Getting Data From WordPress To FileMaker"
description: "How many times we find ourselves presented with a new challenge when working in FileMaker? I will say this: more often than not. I like challenges. They make you learn and keep you on your toes."
pubDate: "2015-03-04T05:07:00+00:00"
updatedDate: "2015-06-08T16:33:28+00:00"
heroImage: "/images/2015/02/Screen-Shot-2015-02-26-at-11.18.51-AM-1024x595.png"
author: "Agnes Riley"
tags: ["Advanced", "Blog", "Developer", "Tips & Tricks"]
permalink: /getting-data-from-wordpress-to-filemaker/
---

How many times we find ourselves presented with a new challenge when working in FileMaker? I will say this: more often than not. I like challenges. They make you learn and keep you on your toes.

My client has a website for a new school which we built in WordPress: www.yalowcharter.org. He was interested in getting data from WordPress to FileMaker. The school is accepting applications for students. He needs the applications to be in a FileMaker database so we can keep their information (children names, parents, etc.)

[![Screen Shot 2015-02-26 at 11.18.51 AM](/images/2015/02/Screen-Shot-2015-02-26-at-11.18.51-AM-1024x595.png)](/images/2015/02/Screen-Shot-2015-02-26-at-11.18.51-AM-1024x595.png)

I’m using the ContactForm7 plug-in to collect the information. Visitors can fill out the form and submit the info. The great thing is the plug-in works well, it even has a CAPTCHA element (separate plug-in required) so you won’t get spammed by bots. It however can only email the data from the form collecting all the data and dumping in the body of the email. That is as far from a relational database as it can be.

So after a little digging I found another plug-in (Contact Form DB) that can dump the collected data into a MySQL database. I was excited like a little kid. Then came the next hurdle: all the fields with their data created a new record. And the MySQL timestamp, of course is not oh so delightful. By the way, I use Navicat for working with SQL tables, but you can use PHPmySQL, and that will do the job, as well.

[![Screen Shot 2015-02-25 at 11.38.06 AM](/images/2015/02/Screen-Shot-2015-02-25-at-11.38.06-AM-1024x707.png)](/images/2015/02/Screen-Shot-2015-02-25-at-11.38.06-AM.png)

Turns out all I had to do is write a SQL query to turn that into a nice VIEW and now I have columns and rows with a properly formatted timestamp. So here’s one query that can help you write one:

> SELECT  
>  DATE_FORMAT(FROM_UNIXTIME(submit_time), ‘%b %e, %Y %l:%i %p’) AS Submitted,  
>  MAX(IF(field_name=’first_name’, field_value, NULL )) AS ‘first_name’,  
>  MAX(IF(field_name=’last_name’, field_value, NULL )) AS ‘last_name’,  
>  MAX(IF(field_name=’email’, field_value, NULL )) AS ’email’,  
>  MAX(IF(field_name=’cell’, field_value, NULL )) AS ‘cell’,  
>  MAX(IF(field_name=’website’, field_value, NULL )) AS ‘website’,  
>  MAX(IF(field_name=’service_provided’, field_value, NULL )) AS ‘service_provided’,  
>  MAX(IF(field_name=’address1′, field_value, NULL )) AS ‘address1’,  
>  MAX(IF(field_name=’adress2’, field_value, NULL )) AS ‘address2′,  
>  MAX(IF(field_name=’city’, field_value, NULL )) AS ‘city’,  
>  MAX(IF(field_name=’state’, field_value, NULL )) AS ‘state’,  
>  MAX(IF(field_name=’zip’, field_value, NULL )) AS ‘zip’  
>  FROM wp_cf7dbplugin_submits  
>  WHERE  
>  form_name = ‘Individual Membership Form’  
>  AND  
>  form_name = ‘Student Membership Form’  
>  GROUP BY submit_time  
>  ORDER BY submit_time DESC

And that produces something like this. If you have errors Navicat will let you know.

**Note** : Make sure you use straight quotes, aka not curly (or smart) quotes such as the ones text editors use.

[![Screen Shot 2015-02-25 at 11.38.39 AM](/images/2015/02/Screen-Shot-2015-02-25-at-11.38.39-AM-1024x165.png)](/images/2015/02/Screen-Shot-2015-02-25-at-11.38.39-AM.png)

The next step is using the [Actualtech](https://www.actualtech.com "Actual Technologies") plug-in (ODBC connector) on the FM server to set up a DSN so you can access this data. You’ll have to define your database (tables, view, username and password).

**Note** : Make sure you select “view”, as well because it is not an actual table you need but the view you created with the SQL query.

After that you create a new external data source in your FileMaker database and create your table occurrence from it.

[![Screen Shot 2015-03-03 at 4.33.45 PM](/images/2015/02/Screen-Shot-2015-03-03-at-4.33.45-PM-272x300.png)](/images/2015/02/Screen-Shot-2015-03-03-at-4.33.45-PM.png)

You can actually just display this data in your database but it’s much more sophisticated and safer to bring that data over to FileMaker. Of course you can do this in different ways. I have to parse the data into multiple tables because we are dealing with related data (kids to parents, phone numbers to parents). I will just run a server script that will check for new records and create them on the FileMaker side when new records show up.

One last important thing to pay attention to is that just because a form is submitted and a record is created in the MySQL database the record will not show up automatically in the FileMaker database. So you’ll have to refresh.

Now, of course when you’re dealing with data you’ll have to put in some checks and balances. Data can be submitted twice because of computer or human error into the MySQL database but we don’t need that twice in our FileMaker database.

I think this is a pretty simple and easy way to get data into FileMaker from a WordPress site.

Update: We’ve published a follow-up article, you can read here: [](../getting-data-from-wordpress-to-filemaker-ii/index.html "Getting Data From WordPress To FileMaker II")
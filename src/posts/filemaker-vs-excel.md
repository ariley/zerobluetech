---
title: "Differences Between FileMaker And Excel"
description: "Everyone I know is familiar with Microsoft Excel to some extent. Some people are more well-versed than others and can do complex data management. Not long ago I met with a consulting company who is…"
pubDate: "2012-03-26T18:45:48+00:00"
updatedDate: "2015-06-05T16:11:42+00:00"
heroImage: "/wp-content/uploads/2012/03/1332787688_application-vnd.ms-excel.png"
author: "Agnes Riley"
tags: ["Blog", "General", "Skill Set", "Tips & Tricks"]
permalink: /filemaker-vs-excel/
---

Everyone I know is familiar with Microsoft Excel to some extent. Some people are more well-versed than others and can do complex data management. Not long ago I met with a consulting company who is working with one of the largest companies in the country to install hardware nation-wide.

[![](/wp-content/uploads/2012/03/1332787688_application-vnd.ms-excel.png)](/wp-content/uploads/2012/03/1332787688_application-vnd.ms-excel.png)

The original process is so cumbersome that they now have a lot of things fall through the crack. By the time an order goes through the myriads of departments and processes, the requirements change and the parts required, as well. But the warehouse doesn’t know how to handle that. So they called in a consultant to help. The consultant doesn’t know FileMaker, so they created a giant web of Excel sheets that actually do a really nice job at filling in the gaps and getting the orders straightened out. FileMaker could’ve given them reports and live dashboard so they can see which orders have mismatched elements or which orders need to be fulfilled in the near future. But at this point they invested quite a lot in Excel, so I doubt they will have the time and energy to redo it in FileMaker.

To those who have not put too much effort into Excel or finding it cumbersome to manage their day-to-day activities, the below will give some incentives to use FileMaker instead of Excel to manage contacts, products, inventory, documents, and events. [Contact us](../contact.html) if you need help deciding. Learn more about [FileMaker development](../custom-filemaker-development.html).

### Strengths of a spreadsheet

  * Storing and analyzing data in lists
  * Analyzing and modeling data
  * Producing charts and graphs
  * Building a financial model
  * Creating basic reports
  * Controlling who can open or modify a file



### Strengths of a FileMaker database

  * Viewing information in list, form, or table view
  * [Storing](../document-management-in-filemaker-supercontainer-and-docubin.html) and managing virtually any type of information (words, images, numbers, files and more)
  * Creating and publishing customized forms and reports
  * Connecting related information such as inventory and sales
  * Connecting to and from [websites](https://zerobluetech.com/mobile)
  * Access by multiple people at the same time
  * [Mobile](https://zerobluetech.com/mobile) access through FileMaker Go or web
  * Set up recurring imports from Excel



#### Tip:

**Use FileMaker to normalize data headers in Excel**. This past weekend I was working on my new web store (ssh!) and I had to export/import products. When importing into the new system I encountered an error: “data headers are duplicated”. Well, I looked through the header row in Excel and I couldn’t see anything duplicated, but when you have a lot of columns you shouldn’t rely on your eyes. I did a quick web search and I couldn’t find an easy method to figure this out. Then I realized, why not use FileMaker? So, I quickly converted my Excel sheet to a FileMaker database (drag and drop) and I had all the fields and data in FileMaker. Clearly, FileMaker didn’t have an issue with the fields, so there was no duplication; the web app lied. So, even though I was back to square one, I figured the web app might not like the file format of the CSV file I was trying to import. So I converted it to another format (Windows of all things) and the import went through just fine. **Moral of the story** : I could’ve spent more time trying to figure out how to get rid of the non-existent duplicated headers in Excel. But instead, I called FileMaker to the rescue, and it solved my problem in 2 seconds.
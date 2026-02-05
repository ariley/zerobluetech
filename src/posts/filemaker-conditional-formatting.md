---
title: "FileMaker Conditional Formatting"
pubDate: "2012-02-06T06:34:03+00:00"
updatedDate: "2018-07-23T21:29:57+00:00"
author: "Agnes Riley"
tags: ["Blog", "Developer", "Tips & Tricks"]
permalink: /filemaker-conditional-formatting/
---

When the **conditional formatting** feature was announced by FileMaker some of us screamed “yeehaw”. No, really. It was a long-awaited feature and right away we knew there are no limits to its usefulness.

If you do not know what conditional formatting is, here’s an excerpt from FileMaker Inc.’s website.

> You can set Conditional Formatting for text fields, FileMaker Web Viewer objects, merge fields, text-based buttons or layout symbols (e.g. date, time, page number, etc.). Choose how objects display by modifying fonts, styles, size, text color, and fill color. Pick from a list of 20 pre-defined conditions or create your own with a calculation for enhanced reporting. Conditional Formatting settings affect only the way data is displayed or printed and not how data is stored in the database.

So, in other words, you can basically emphasize or hide data on a layout with conditional formatting.

I would like to share a handful of examples with you, some of which you may know and use (and have seen on other blogs), but the goal here is simply to put some ideas on one page and spark more ideas. A lot of times my inspiration comes from looking at something that was not intended for its current use.

### The Problem

We all had users call us and say “I’ve been entering records and now they’re all gone”.

### The Solution

Place text “You are in FIND MODE” in the same color as your background. Formula: Get ( WindowMode ); set the color to bright orange or red. Get ( WindowMode ) window modes: 0 for Browse mode 1 for Find mode 2 for Preview mode 3 if printing is in progress.

![](/wp-content/uploads/2012/02/Find-Mode.png)

### The Problem

User cannot easily identify which field they clicked in.

### The Solution

Simply use “1” as a formula (assign the color white to it). I normally set the field to a light yellow fill color on the layout.

![](/wp-content/uploads/2012/02/Tab.png)

### The Problem

A selected portal row needs to be visually differentiated from the other portal rows.

### The Solution

Place a text object over your fields. Make sure it matches the edges of the row by pixel, then send it backward until all of your fields are in the front. Apply conditional formatting to it so when that row is selected your objects gets a darker fill color color (however your row is selected depends on your database rules). Now do the same for your text fields, making sure your text gets white (or contrasting light color) when the same condition applies.

![](/wp-content/uploads/2012/02/Portal.png)

### The Problem

Information in a field needs to be highlighted based on action. In the example below paid invoces get a green color.

### The Solution

Apply conditional formatting to a field or a set of fields. The condition in my case is Paid = 1, then assign color green to my field.

![](/wp-content/uploads/2012/02/Portal.png)

### The Problem

Users need to be reminded to fill out certain fields on a layout.

### The Solution

When the field is empty [IsEmpty (field)] set the fill color to red and the text white (again, contrasting colors). Also, make the text size 500 points. You could make it 1, too, but then you’s see a spec of white, and that’s not pretty.

![](/wp-content/uploads/2012/02/Sheet.png)

### The Problem

#### 

A field has data with variable length. You, however, don’t have the space to make the field very long. In my example, my field width is 138 pixels and my font is Helvetica, 13pts.

### The Solution

#### 

Apply conditional formatting formula to the text size in the following manner:
    
    
     Length ( Self ) > 20 (Set text to 12pt) Length ( Self ) > 23 (Set text to 11 points) 

Depending on your real estate on the layout you’ll need to choose the appropriate length and font size.

![](/wp-content/uploads/2012/02/Portal3.png)

#### 

This has hopefully wet your appetite to use conditional formatting if you havent yet. Feel free to share examples of your own.
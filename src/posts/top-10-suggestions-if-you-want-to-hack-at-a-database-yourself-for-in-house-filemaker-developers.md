---
title: "Top 10 Suggestions If You Want To Hack At A Database Yourself - For In-house FileMaker Developers"
description: "All FileMaker developers start somewhere, and that place is definitely not being a certified independent developer. I started by being an in-house developer. Working in a busy environment…"
pubDate: "2011-05-02T08:00:00+00:00"
updatedDate: "2015-06-08T15:12:28+00:00"
author: "Agnes Riley"
tags: ["Beginner", "Blog", "General", "Tips & Tricks"]
permalink: /top-10-suggestions-if-you-want-to-hack-at-a-database-yourself-for-in-house-filemaker-developers/
---

All FileMaker developers start somewhere, and that place is definitely not being a certified independent developer. I started by being an in-house developer. Working in a busy environment, all you have time for is cranking out the features that your boss needs, right away. Nobody has time to think about consequences. My job was to get that report done, no matter how many calculations I had to add so I can produce the results. Or getting that extra layout in so we can show the data on a different list. All of these things add up, and eventually they make your file larger and/or slow your database down.

As an independent developer, you start from a different perspective: data and system integrity are most important. Over the last 4 years since I’ve been developing independently I have learned a lot from fellow FileMaker developers. I had learn to to rethink how I develop and incorporate planning, design, testing and other steps to my routine. It wasn’t so much reinventing the wheel so much as making it better.

One great thing about FileMaker (aside from it being agile) is that anyone can become a developer. If you feel like you have enough skills to create what you need, feel free to get started. You can [purchase volume licenses](https://zerobluetech.com/licensing) with great discounts even for a small office from us. And if you get in trouble, you can always consult with us during your project or even years later, when you realize that it’s actually far from where it could be.

Here are some conventions to follow if you start on your own. These will help you greatly down the line. Follow [@zerobluetech](https://www.twitter.com/zerobluetech) on Twitter to ask questions.

  1. #### Be minimalistic:

Create what’s needed, not more but not less. A lot of times we don’t think about the effects of what we do; what’s another calculation, right? Think again. The more calculation fields you have on a layout, the slower the layout loads. We’ve all seen layouts that said “summarizing” for over minutes. This is easily avoidable by storing data in indexed fields.

  2. #### Break your scripts into smaller chunks.

Don’t write scripts that would print on several pages. By the time you write it you’ll forget what the beginning was all about.

  3. #### Follow a naming schema.

There are a lot of them out there, but you can certainly invent your own. Stick to it.

  4. #### Comment your code.

Comment calculations, scripts and even layouts if needed. You (and others) need to know what’s what at a later time, too.

  5. #### Implement strict security features.

Steven Blackwell ([@filemakersecure](https://www.twitter.com/filemakersecure)) cannot say this enough but people are still not listening. 🙂 If you have strict control over who can access your data, you have a much better chance of avoiding disasters.

  6. #### Use custom menus for controlling access.

Take away “delete all records” from all users–then you won’t have to restore thousands of records (and lose the ones that weren’t captured in the last backup).

  7. #### Talking about backups:

Back up, back up, back up. Every 30 minutes or ever hour (depending on your storage space), but at least once a day, week and month. Save clones of your working database. In case database corruption, you can export the data and get it imported to an earlier clone and you’re back in business. Compact the clones to save disk space.

  8. #### Do not store images in FileMaker container fields.

Contrary to popular belief, your database will get large and clumsy over time. Use [SuperContainer and now DocuBin](../document-management-in-filemaker-supercontainer-and-docubin.html) to manage files.

  9. #### Stay away from a lot of graphics.

Do not paste large images on your layouts: they will just slow your database down. Create 75 dpi PNGs if you can. They will also preserve transparency. Or put them into container fields so the dataabse will have to load them once, as opposed to on any layout. Here I’m talking about your layout design (header, buttons), not your records!

  10. #### Use forums, mailing lists and friends.

Don’t spend time reinventing the wheel. Someone already did it.




Hope this will save you guys a lot of time. Had anyone broken things down into digestible chunks I certainly would’ve not spent a lot of my evenings at work recovering data other people lost accidentally or rebuilding features because my database got corrupted. Glitches can still happen and they will happen. You can, however reduce the opportunity for things going bad.

You will run into walls, we all do. But don’t be afraid. Start working on something or modify any of the FileMaker starter files.

If you need help, feel free to [contact us](../contact.html); we provide consulting services in the New York, New Jersey area, or to any region where screen sharing apps are accepted. First hour of consulting is free.

Also, check out our [services](../services.html), [portfolio](../category/results/index.html) and [products](../products.html).
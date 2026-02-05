---
title: "Converting Files to FileMaker Pro 12"
description: "As you may know by now FileMaker 12 is out. A lot of articles have been written about the various features, so I’m not going to bore you with that. FileMaker 12 for iOS is free, so if you haven’t…"
pubDate: "2012-05-15T12:10:16+00:00"
updatedDate: "2015-06-05T15:56:31+00:00"
author: "Agnes Riley"
tags: ["Advanced", "Beginner", "Blog", "Developer", "General", "Skill Set", "Tips & Tricks"]
permalink: /converting-files-to-filemaker-pro-12/
---

As you may know by now **FileMaker 12** is out. A lot of articles have been written about the various features, so I’m not going to bore you with that. FileMaker 12 for iOS is free, so if you haven’t grabbed a copy, go get it. It comes with some demo files to play with to learn about the new features.

With every new release the question comes up: should I wait or should I convert? I think this question should be answered separately whether you’re a developer or a user. Users tend to jump in a lot faster. I have users who just announced they converted their database. Once it’s done—and you start using the database— it’s hard to go back. Developers I talked to are wary about converting, so we have two different groups with one goal: data integrity, however, their patience levels are different.

> FileMaker Pro 12 can directly convert your existing FileMaker Pro 11, 10, 9, 8 and 7 databases. All other versions of FileMaker Pro will require a multiple product conversion. Review the information below to determine whether your files will directly convert to FileMaker Pro 12, or if they will need to be converted multiple times.

More info can be found in the [FileMaker KnowledgeBase](https://help.filemaker.com/app/answers/detail/a_id/10571/~/converting-files-to-filemaker-pro-12 "Converting files to FileMaker Pro 12").

So, before jumping in, let’s look at a couple of things.

#### If You Are A User

First and foremost discuss the conversion process with your developer, if you have one. It’s a new file format, you’ll need to upgrade the server, as well as the file(s). If you don’t have a developer, take a look at your dataset. I heard complaints about issues with scrolling in list view. This may not affect you if you don’t use list view, but it’s worth knowing. I, for one, never use list view in the solutions I develop. I use portals that can be filtered in many ways instead, so you don’t have to work with large sets of data at any given time.

Take a moment to consider how mission-critical your solution is. If you’re a small shop (couple of people) with a one-file solution you may be able to just jump in and bite the bullet. You may never have any issues. And you may love a lot of the new features FileMaker 12 offers including the new layout themes. I’d still make a copy of the new database and run FileMaker 12 parallel to your FileMaker 11 (yes you can) and test the new database for a good couple of days. Run scripts, create records, check the mission-critical processes.

If you’re a larger shop or your database is mission critical, I’d take a copy of the file, convert it, put it in a test environment. Put in on a new server (different machine than your FileMaker 11 server). Test your new database thoroughly for about a week. Test systematically. Test for as many processes you can.

#### If You Are A Developer

Then it is your duty and responsibility to manage client expectations and not let them commit suicide. The same applies to you as the large shops who have a test environment and can perform lots of tests. But you also need to consider that FieMaker 12 has changes that affect the developer, as well. One example the new layout tools. Test the development features, as well, to make sure you will be comfortable developing on the new version.

We’ve been waiting awhile for FileMaker 12 and we are all excited. I love the new Insert from URL function, for example, but when I developed a database for the iPad for a client, I noticed that getting XML takes 5 minutes on an iPad2 in FileMaker 12. This is not a concern for my client, I believe, but it can be a concern for more mission-critical environments.

It’s possibly best to convert, while your users are not using the database. A weekend might be a good time if you can’t set up a test environment. But as you know, we have 4 weekends in a month, so don’t schedule more conversions than you can handle.

[Talk to us](../contact.html "Talk to Us"), if you need help converting your FileMaker files or have questions about development.
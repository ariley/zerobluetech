---
title: "Coding Principles And How They Apply In FileMaker"
description: "When I dabbled in development first time I had no idea I actually was developing. I was just adding a few fields here and there. Mostly I just wanted a way to record information on tracking film…"
pubDate: "2015-04-07T11:00:46+00:00"
updatedDate: "2015-06-08T16:23:33+00:00"
heroImage: "/wp-content/uploads/2015/03/clean-field-script-300x245.png"
author: "Agnes Riley"
tags: ["Advanced", "Beginner", "Developer", "General", "Skill Set"]
permalink: /coding-principles-and-how-they-apply-in-filemaker/
---

#### Coding Principles in general

When I dabbled in development first time I had no idea I actually was developing. I was just adding a few fields here and there. Mostly I just wanted a way to record information on tracking film materials, dubbing, etc. And for the next decade I did the same: I hacked my way to getting things done for the boss. And while I tried to protest, the boss always won and said “but I need it now.” That leaves zero time for planning or building architecture. So I was more of a firefighter than developer. The next decade I spent learning development from scratch and I keep learning.

**Simplicity is the most important consideration in a design**

Whether you’re a hard core coder who eats, sleeps and breathes code or a school teacher turned FileMaker developer, you sure have some principles that you abide by (and if you don’t you should). We live by principles, so why shouldn’t we code by principles? And when you code, you often ask yourself “is this the best possible way to solve the problem?” In FileMaker there are at least three ways to do the same things. And there’s a different

Since this blog is mostly dedicated to FileMaker development (at this point), I’ll just take a stab at some coding principles and see how they apply to us, FileMaker developers.

#### YAGNI (You Ain’t Gonna Need It)

The idea is that you should code with the goal in mind to program for what you need not what you might need. XP co-founder Ron Jeffries has written:

> “Always implement things when you actually need them, never when you just foresee that you need them.”

The temptation—to create something—is large for a developer. It is like putting a knife in a surgeon’s hand or giving a pencil to the architect; they will want to do what they _do best_. We want to add bells and whistles and we want to blow the client away. But just like furniture shopping at IKEA, we can end up with a lot more than we can take home. **It’s better to code for what the client needs than what the client wants**. Personally, I’m an advocate for this and I always tell my clients: “I will give you what you need but not what you want.”

#### Worse Is Better

Aptly, also called also called “ _**New Jersey style”.**_ [And if anyone ever wants to mock Jersey, again, they will meet my fist.] The idea behind it is that “quality does not necessarily increase with functionality”. So what this does is it uses a scale to measure which one is heavier and says _simple_ is **_heavier_** than _correct_. So to me this boils down to **getting a solution off the ground and into the users’s hand rather than making it perfect**. You need to cover as many aspects as you can to make it practical. Your design needs to be consistent but simple. So, buttons, element placement and font sizing should be consistent from layout to layout. Luckily we have FileMaker 13 now so if you use a built-in template (or build your own)it’s hard to go wrong.

#### KISS (Keep It Simple Stupid) principle

This acronym is a design principle noted by the U.S. Navy. **Achieving simplicity should be the goal at all times** , and avoid unnecessary complexity. Design your layouts with fewer buttons and make sure they do the most important functions. Then you can take the user to a different tab or layout to give them further info. Give them a drop-down menu with further options if you must.

#### Don’t repeat yourself (DRY)

When FileMaker gave us variables, it became possible to start writing universal scripts. If you’re still not using variables you’re missing out on something great! They allow you to compact your code. You can write one script to create, delete, modify a record and give parameters to tell what layout you are coming from, what your table is, where you need to end up when you’re done. Of course, there will be variations which you can put in an if statement if you need it. But **if you can create something once and reuse it, you’re golden. **Below is a script we use to [strip fields (after a user adds data that) from unnecessary garbage](https://zerobluetech.com/keeping-your-data-clean "Keepig Your Data Clean").

  
  


[![clean-field-script](/wp-content/uploads/2015/03/clean-field-script-300x245.png)](/wp-content/uploads/2015/03/clean-field-script.png)

Clean Field Universal Script

  
  


More useful coding principles: [Wikipedia](https://en.wikipedia.org/wiki/Category:Programming_principles "Programming Principles")
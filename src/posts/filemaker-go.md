---
title: "FileMaker Go and Barcode Scanning - A Workaround"
pubDate: "2013-07-10T17:52:57+00:00"
updatedDate: "2018-07-23T21:29:54+00:00"
author: "Agnes Riley"
tags: ["Advanced", "Beginner", "Blog", "Developer", "General", "Tips & Tricks"]
permalink: /filemaker-go/
---

We all know that there are differences when dealing with FileMaker Go vs. FileMaker on a desktop. I think I can speak for all of us when I say we’re grateful that FileMaker Go exists, but we have to admit it has caveats. But we’re resourceful developers, right? We will sit and try ti tackle any given problem, because that’s what out clients/bosses pay us for. Most importantly, we cannot sleep until we figure the issues out because it just bothers us when we’re presented with a problem that we cannot find a solution for.

We sell barcode scanners. We make sure all of our scanners work with FileMaker, and all of our Bluetooth scanners work with FileMaker Go (and, of course, Android and other devices that sport Bluetooth connectivity). So far so good, right?

I’ve been getting complains that it’s impossible to scan into FileMaker Go. When things dont work like they’re supposed to out of the box.

### The Problem

In FileMaker Pro you can script the scanning process to show a dialog that you scan into. This is great, because all the scanners you can program (which is usually the default anyway) to send a carriage return (enter) at the end of scanning. Which means that when the scanner is done scanning your code, the “Ok” button will be pressed automatically and your script can continue what it’s supposed to do, whether that is the bring up the dialog to scan another code or do some crazy magic and analyze data. You, however cannot achieve the same result in FileMaker Go, because you cannot get the cursor into the dialog. Now, we can ask questions like ‘why’ and spend hours and days cracking our heads open and even email FileMaker Inc. to see why this is not working. Or we can simply create a workaround.

### The Solution

You can [download](https://cloud.zerobluetech.com/2N3S3S1d251I "demo file") a simple file that demonstrates how you can get around the problem with barcode scanning in FileMaker Go. I used a field to scan into instead of the dialogue and two triggers so you can create records and keep on scanning. There’s one field and one button on this layout. Obviously, you will have to scrip the rest of your process.

We can take the load off of you by doing the heavy lifting. Scripting can be cumbersome, when all you want to do is just scan an item and manage your inventory. Let us help.

We sell a wide selection of Bluetooth Laser Barcode Scanners that work with FileMaker Go out of the box . Pair, connect and scan right into a field. Want to use the iOS keyboard? No problem, push the small button and the keyboard will pop up.
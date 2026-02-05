---
title: "Trojan On Macs - What To Do"
description: "I wish I could write about FileMaker 12 (which I will, soon) but there’s a more eminent issue right now: there’s apparently a new trojan out there attacking our Macs. When I read something like this…"
pubDate: "2012-04-05T15:45:56+00:00"
updatedDate: "2015-06-05T15:57:19+00:00"
author: "Agnes Riley"
tags: ["Blog", "General", "News", "Tips & Tricks"]
permalink: /trojan-on-macs-what-to-do/
---

I wish I could write about FileMaker 12 (which I will, soon) but there’s a more eminent issue right now: there’s apparently a new trojan out there attacking our Macs. When I read something like this, I generally just ignore it (because I have not seen a virus, malware or trojan for Mac OS X), but I have done my research and it seems several large websites picked it up, such as Gizmodo and PC Magazine, so it would be unwise to just ignore it. According to sources, 600,000 Macs have been affected. That’s a large number to ignore. Read below, check and fix if you have it.

No worries, F-Secure has a fix for the problem.

Gizmodo has a method to check your computer; you can find it [here](https://gizmodo.com/5899352/mac-flashback-trojan-find-out-if-youre-one-of-the-600000-infected).

I ran their check and I’m clean:

new-host-3:~ ariley$ defaults read /Applications/Safari.app/Contents/Info LSEnvironment  
2012-04-05 11:39:23.355 defaults[24956:707]  
The domain/default pair of (/Applications/Safari.app/Contents/Info, LSEnvironment) does not exist  
new-host-3:~ ariley$ defaults read ~/.MacOSX/environment DYLD_INSERT_LIBRARIES  
2012-04-05 11:39:41.692 defaults[24958:707]  
The domain/default pair of (/Users/ariley/.MacOSX/environment, DYLD_INSERT_LIBRARIES) does not exist

The check is easy; all you have to do is issue two commands in the Terminal. I highly recommend that you do it.

Also, install the Java upgrade Apple just released. Go to Software Update under the black Apple in the upper left corner and check for updates; it will show up.
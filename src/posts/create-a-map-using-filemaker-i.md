---
title: "Create A Map Using FileMaker I"
description: "Today I was asked to create a map using FileMaker to show all the students that are accepted to my client’s school. The client said the Department of Education needs to map out the bus routed for the…"
pubDate: "2015-07-15T19:51:08+00:00"
updatedDate: "2017-01-21T15:52:20+00:00"
heroImage: "/wp-content/uploads/2015/07/Screen-Shot-2015-07-15-at-1.12.44-PM.png"
author: "Agnes Riley"
tags: ["Beginner", "Blog", "Developer", "General", "Skill Set", "Tips & Tricks"]
permalink: /create-a-map-using-filemaker-i/
---

Today I was asked to create a map using FileMaker to show all the students that are accepted to my client’s school. The client said the Department of Education needs to map out the bus routed for the students. He said he DOE may not want to provide buses for a child if he/she lives too far, and we need to make an argument that the child should be bused to the school.”

So at first I thought about what software/plug-in I should use, then I realized I can create a map with Google Maps with layers. Especially, since this map we can’t just have in the database but rather we need to share it with the DOE. Turns out this was the easiest task, ever, so I thought I’d share the steps.

  1. Export the data you want to be mapped in CSV format. I wanted to see kids and their location (full name, address, city, zip);
  2. Create a Google Map here: <https://www.google.com/maps/d/u/0/>;
  3. Add a new layer, name it whatever you want to import your data into;
  4. Import the CSV file. It will ask you to dedicate the data for the pins (address) and the next step is to dedicate a column for your label (full name);
  5. Change the color of the pins;
  6. Add more layers with more data if needed (in my case my school is the other layer).



And here is the finished product:

[![Screen Shot 2015-07-15 at 1.12.44 PM](/wp-content/uploads/2015/07/Screen-Shot-2015-07-15-at-1.12.44-PM-300x201.png)](/wp-content/uploads/2015/07/Screen-Shot-2015-07-15-at-1.12.44-PM.png)
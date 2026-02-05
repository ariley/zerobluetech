---
title: "Adding Weather and Air Quality Data in FileMaker"
description: "With the current COVID-19 epidemic, life as we knew it has changed. You know what that means for you. Some inconvenient but some changes are probably good and maybe they are here to stay."
pubDate: "2020-10-08T11:30:00+00:00"
updatedDate: "2020-10-08T03:42:57+00:00"
heroImage: "/wp-content/uploads/2020/10/Screen-Shot-2020-10-07-at-2.10.17-PM.png"
author: "Agnes Riley"
tags: ["Blog"]
permalink: /adding-weather-and-air-quality-data-in-filemaker/
---

With the current COVID-19 epidemic, life as we knew it has changed. You know what that means for you. Some inconvenient but some changes are probably good and maybe they are here to stay. Like washing your hands every time you enter a household or office.

Also, in California, we have been weathering fires ignited by dry-lightning and other issues. And of course, that brings a lot of smoke, ash, and soot. It helps to know when to stay indoors or whether going home from work you will need a mask with a filter for smoke.

I thought it would be apropos to add some data to our splash page. Luckily www.purpleair.com provides all of what I needed, and it was super easy to implement.

[![](/wp-content/uploads/2020/10/Screen-Shot-2020-10-07-at-2.10.17-PM.png)](/wp-content/uploads/2020/10/Screen-Shot-2020-10-07-at-2.10.17-PM.png)

If you go to their website (https://www.purpleair.com/map), you need to find the closest sensor to your location. If you click on “Get this widget” you can get the sensor’s ID number. Then you go to https://www.purpleair.com/json?show= and append the aforementioned ID. It should load the JSON with the data relevant to that particular sensor.

Now you can use the **Insert From URL** script step and insert the JSON from the URL. (If you’re working with FileMaker 17 or higher you can insert the data into a variable.) So now that you have inserted the JSON into a variable named $json, you’ll just have to parse it out. You would use **JSONGetElement** and get whatever element you desire. E.g. JSONGetElement ( $json ; “temp_f” ) will give you the temperature value. I got the temperature, humidity, air quality index, and pressure just for fun. If you want to take this a step further you can add conditional formatting to show the color Purple Air is showing for the AQI, aka green for healthy, yellow, or red or purple for higher levels.

Happy FileMaking!
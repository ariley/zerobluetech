---
title: "FileMaker Image Management - Container Field Behavior and Much More"
description: "One of my clients called this week and told me his logo got inverted when printing to a PDF. Also, the PDF file size doubled. Previously it did not occur to me to check the file he received from his…"
pubDate: "2011-09-07T17:51:58+00:00"
updatedDate: "2015-06-08T15:00:45+00:00"
heroImage: "/images/2011/09/Screen-shot-2011-09-01-at-5.29.14-PM-300x252.png"
author: "Agnes Riley"
tags: ["Beginner", "Blog", "Developer", "General", "Tips & Tricks"]
permalink: /filemaker-image-management/
---

One of my clients called this week and told me his logo got inverted when printing to a PDF. Also, the PDF file size doubled. Previously it did not occur to me to check the file he received from his designer, because I wrongfully assumed the designer gave him the appropriate file. But this brings up some interesting points about what files we should use with FileMaker and how we should use them. So, I gathered some useful information. Hope this helps you with handing your images in FileMaker and FileMaker Go.

### General Image Handling

There are several different ways you can show images on a FileMaker layout:

  * Container field (Insert/Picture)
  * Place image on the layout (copy and paste from another source)
  * Show from another source in a webviewer (i.e. using [SuperContainer or DocuBin](../document-management-in-filemaker-supercontainer-and-docubin.html))



**1\. Container Field**

**Advantages** :

  1. Quick and easy. You insert an image, and voila it’s right there. If you store the file as a reference only (suggested use if you have constant access to the hard drive the files reside on and do not plan to move or delete them) you will not bloat your database;
  2. Anyone can export it from there by right-clicking on the image and choosing “Export Field Contents”;
  3. The image can be swapped out just by inserting another image;
  4. Scan directly into a container field (by using a plug-in);
  5. You can export or email the image (file) as an attachment;
  6. Images can be cropped or resized (pay attention to maintaining proportion).



**Disadvantages** :

  1. You cannot do too much manipulation without a plug-in;
  2. Your database file size gets large by every image you inserted (unless stored as a reference only), therefore eventually your database will get slower;
  3. Global container fields save on close, so your file must be accessed locally, if you’d like to save a change;
  4. You can’t find or sort records, so you need to set up a calc field. See **_Exhibit A;_**
  5. You can only print the image as it is on the layout.



[![](/images/2011/09/Screen-shot-2011-09-01-at-5.29.14-PM-300x252.png)](/images/2011/09/Screen-shot-2011-09-01-at-5.29.14-PM.png)

**2\. Place Image on Layout:** Placing an image on the layout is not generally a good idea, unless it is your logo or layout design (i.e. you are creating a header), but even so it’s best to use a global container field in an interface table or an image table where you load the images from when your database starts. Although, I have to mention that I see image quality differences between a referenced image in a field vs. an image pasted on the layout: in my opinion, image quality of the pasted image will be superior.

**3 . Web Viewer**

  * Web viewers are great for images. You can show images from a website or SuperContainer. PDF (and certain image*) files can be viewed from a web viewer. PDFs can even be manipulated (zoom, next page, etc.) on Macs. Files are not stored in the FileMaker database.
  * You cannot print from the web viewer. You can print the layout, but that’s agains, any decent designer’s instincts.
  * There’s a great article by Geoff Coffey on [Scaling Images in a Web Viewer](https://sixfriedrice.com/wp/scaling-images-in-a-web-viewer/).



### Instant Web Publishing

  * Container field data cannot be entered or modified from IWP.
  * Complex or layered pictures are not rendered properly.
  * SuperContainer works with IWP.



### Image Management Helpers (Plug-Ins and Tools)

  * [SuperContainer](../document-management-in-filemaker-supercontainer-and-docubin.html "Document Management in FileMaker – SuperContainer and DocuBin") (File and image management. The images are NOT stored in the FileMaker database, rather stored on a file server (can be your local computer). Has the ability to upload/download, version files.
  * [CNS Image](https://filemaker-plugins.com/cns-image) (An all-round plug-in for image handling.)
  * [InsideScan](https://www.powersolutions.it) (Scan directly into a container field.)
  * [ExifPlugIn](https://www.jensteich.de) (Get EXIF data from pictures taken with a camera.)
  * [ScriptMaster](https://www.360works.com/scriptmaster/) (Has basic functions for cropping, rotating, watermarking, etc.)
  * [Theme Library](https://filemakerthemes.com/) (Themes, buttons, image manipulation)



### Supported Formats for Container Fields

FileMaker Pro supports the following picture, QuickTime, and sound formats (_**Exhibit B**_)

[![FileMaker Supported Image Formats](/images/2011/09/Screen-shot-2011-09-08-at-11.30.42-AM-300x163.png)](/images/2011/09/Screen-shot-2011-09-08-at-11.30.42-AM.png)

General Image Suggestions

**Print Quality** : 300 DPI CMYK or Grayscale JPG or TIFF (if you need large, good-quality photos)

**Screen Quality** : 75 DPI RGB or B&W

**Transparency** : If you plan to use transparency, FileMaker suggests using TIFF, PNG, or JPG images. FileMaker does not recommend using the PICT (.pct) format with transparency.)

**Caveats** : For proper image handling, QuickTime installation is suggested on Windows.

### Image Resizing and Cropping

The Preview app on Mac OS X can manipulate images: you can crop, resize, even convert them to a different format (JPG, GIF, PNG, TIFF, etc.) (_**Exhibit C**_). Some plug-ins and the Theme Library can enhance your image manipulation experience.

[![Image Resizing in Preview](/images/2011/09/Screen-shot-2011-09-08-at-11.33.52-AM-300x251.png)](/images/2011/09/Screen-shot-2011-09-08-at-11.33.52-AM.png)

### FileMaker Go

FileMaker Go has now the following functions for container fields (_**Exhibit D**_):

  * Choose From Library
  * Take Photo (iOS device with camera required)
  * Get Signature
  * Paste
  * Open
  * Email



[![Container Field Options on FileMaker Go](/images/2011/09/photo-200x300.png)](/images/2011/09/photo.png)

SuperContainer works with FileMaker Go without programming changes. Because SuperContainer thumbnail file sizes are a tiny fraction of the full-size images, they **load much faster, especially over a 3G connection.**

* You can view any image that your browser (Safari on Mac and Internet Explorer on Windows) supports.
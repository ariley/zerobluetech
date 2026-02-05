---
title: "Protecting Customer Data – Solutions For A FileMaker Developer"
description: "In the process of creating solutions for their clients, FileMaker developers often find it easier to put the client’s database(s) on their own desktops, notebooks or servers rather than connecting to…"
pubDate: "2010-11-03T16:14:38+00:00"
updatedDate: "2015-06-08T15:26:13+00:00"
author: "Agnes Riley"
tags: ["Blog", "General"]
permalink: /protecting-customer-data-solutions-for-a-filemaker-developer/
---

In the process of creating solutions for their clients, FileMaker developers often find it easier to put the client’s database(s) on their own desktops, notebooks or servers rather than connecting to a remote computer. A lot of clients I deal with don’t pay too much attention to security, and it’s our job as developers to keep their data secure, whether it’s in the database or we’re talking about the database itself, especially during development. My take on this is very simple: if others mean harm, no security measures will keep them away from attaining their goal. However, as a technology specialist, it’s my duty to take measures to keep customer data safe. In this article, I am concentrating on three topics:

  1. **Securing your computer**
  2. **Securing your FileMaker data**
  3. **Secure backups**



The purpose of this article is not to cover anything and everything under the sun, but to remind you of best practices and give you some ideas about how to approach things. Also, I use a Mac, so if any of these things don’t work on Windows or if you’d need to do things differently, feel free to comment.

### **Securing Your Computer**

  1. **Assign a Password**. While your sister’s computer may not need a password to log in with, as a developer I highly recommend you disable automatic login and give yourself a nice, at least 12 character-long, secure password. Secure means that you do not use the same password everywhere. If you need a tool to help you manage and keep passwords and even generate secure passwords for you, 1Password is the best I’ve seen.
  2. **Eikon Fingerprint reader**. If you need stronger security than a password for your notebook, I highly recommend the [UPEK Eikon to Go Digital Privacy Manager for Mac](https://store.apple.com/us_smb_338040/product/TS342LL/A?fnode=MTY1NDA2OA&mco=MTY4NzU2OA&s=newest). It’s a portable security device that fits on your keychain and can be with you wherever you go.
  3. **Securing your passwords**. Whether you are logging into a web site to pay your taxes or logging in to manage your email preferences from a newspaper, it is important to have secure password. In this age of increasing identity theft, this is getting to be more and more important. Below are a couple of tips on achieving this: 
     1. **Choose passwords that don’t contain personal informatio** n but are easily remembered. How do I know if my password is secure? If you have at least 12 characters and at least one number and a special character and your password does not read a full word in English, you’re onto a good start. There is a lot of literature on choosing passwords out there; here’s a good one from [Microsoft](https://www.microsoft.com/protect/fraud/passwords/create.aspx.).
     2. **Don’t reuse your passwords**. Make sure the websites for your bank accounts and credit cards have different login information. Don’t make it easy for people to gain access to one password and take everything from you.
     3. **Use****[1Password](https://www.shareasale.com/r.cfm?b=144312&u=422261&m=19222&urllink=&afftrack=)** (or a similar utility) that is available for both Mac and Windows, iPhone/iPad and now Android, as well. Take your information with you securely, so you don’t have to remember all this useless information; instead, look them up when you need them. 1Password can also generate and store secure random passwords for you. Its keychain file can be synced to multiple machines (and the Android app) via Dropbox, so you can maintain your info on one device and it’ll be available to you on all of your devices (where applicable).
     4. **Change your passwords every couple of months**. Don’t be lazy about it. If someone gets hold of your information, it takes longer to get your money back from a bank than to change and store your password.



### **Securing your FileMaker Data**

  1. **Have a server**(hosted or local). Have your files not be accessible to anyone locally but the FileMaker developers. This means not having the files on your File Server and **NOT sharing the files with File Sharing**. This can cause serious corruption in your database if a hosted file is opened locally and renders your file unusable.
  2. Convince your clients (yourself) to **use privilege sets/accounts and passwords** to manage the data in their FileMaker databases. People might not think it’s important but prevention is the best security measure. Give people access to what they need, no more and no less, to reduce human error.
  3. **Make sure all of your FileMaker databases have passwords**. This is especially important if you use the Data Separation Model. If you leave your data file unprotected, why bother putting a password on your interface file?
  4. Try to **make sure users cannot set up an external file to have access to all your data in your main file**. FileMaker Pro/Advanced 11 really helps with this. Previous versions allowed you to create references to your file. FileMaker 11 gives you an option to prohibit access with older versions of FileMaker and to require full access when creating references to your file. If security is important in your environment, it’s worth upgrading just for this.



### **Securing your FileMaker Backups**

**Backup, backup, backup**. One can never emphasize this enough. Decide based on your server how often it can handle backups without causing serious hiccups in your environment. Let me give you an example. I used to have a FileMaker Server on an older XServe in an office environment. We did backups every hour and the databases paused for minutes, every hour on the hour so the backup can be performed. It was painful for 40 employees. I purchased a new XServe, moved the files to a RAID, and when the backup schedule ran every 30 minutes, nobody even noticed it. You can find a lot of literature on how to do backups. I suggest that you backup hourly, daily and weekly. Then move some of those backups offsite. One of the offsite solutions is [Amazon AWS](https://aws.amazon.com/), but there are others. I use Amazon AWS in conjunction with 30Works’ [SafetyNet](https://360works.com/filemaker-offsite-backup/). All my clients’ files that are stored on my server for development are backed up every night, so I can sleep well. The service is cheap and setup is a breeze. If anything happens, all you have to do is install SafetyNet on a different machine (anywhere in the world) and you can get back to work in minutes.

  1. **Test your backups**. It’s not enough to just have them sit somewhere. Open them up on occasion and test them to make sure there is no visible corruption. Don’t wait until something happens and then you realize your backups from the last 3 months are corrupt.
  2. **Create clones** on a regular basis of your healthy files. Same reason as above.
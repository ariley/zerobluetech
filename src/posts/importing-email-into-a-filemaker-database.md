---
title: "Importing Email Into A FileMaker Database"
pubDate: "2011-12-30T05:11:16+00:00"
updatedDate: "2018-07-23T21:29:57+00:00"
author: "Agnes Riley"
tags: ["Advanced", "Blog", "Developer"]
permalink: /importing-email-into-a-filemaker-database/
---

Email is a hairy subject. Not just because we have POP, IMAP and SMTP servers to deal with, but also ports, authentication, port restrictions by ISPs, syncing problems, etc.

I generally tell users to sick to their email programs, if that’s an option.

There are certainly some times when it’s worth dealing with it and that call, my friend, you will have to make. I can tell you I once implemented HTML sending for mass-mailing purposes, and it worked really well, we even tagged the client we sent the email for and kept the campaigns, as well as created join records for the email recipients so we could track history. Of course, this was before the day of [MailChimp](https://www.mailchimp.com "MailChimp") (which we are using). I love MailChimp and there’s no need to reinvent the wheel so I can reproduce something in FileMaker.

I however, have a client who wanted to see emails sent to and received from clients’ contacts for all employees of the firm, also see them from the job’s perspective: because the previous software (DayLite) he was using did integrate email with his project management. So, I looked at different options and decided to use [mail.it](https://www.dacons.net/fmplugins/mailit5/ "mail.it").

There are [other options ](https://filemaker-plugins.com/compare/email-plugins/ "compare email plug-ins")out there, but I used mail.it before so I stuck with it and I do not regret it. I had a couple of gotchas along the way (e.g. deleting emails from the server for multiple servers), but all’s well that ends well. Customer support at dacons.net is also excellent with a support forum. Their turn-around was not the quickest, but that’s not really their fault, because we have a 6 hour time-difference.

I think, at the end I accomplished creating an interface that acts and looks like an email client. I am using the webviewer to show the message as HTML. Attachments show up, and you have two options: 1. you can hold down the option key to view them in a new window or you can download them. Attachments are NOT stored in the database. Attachment handling is accomplished with [SuperContainer](https://www.360works.com/SuperContainer) by 360 Works.

![](/images/2011/12/email_view-1024x6851.png)

Of course, email receiving will be accomplished from the server side. It will run at a 5-minutes interval, just as if you had it in an email client.
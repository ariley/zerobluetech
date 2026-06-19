---
title: "New FileMaker Hosting Types: Why We Chose LXC"
description: "ZeroBlue's updated FileMaker hosting plans use LXC-based isolation for predictable FileMaker Server operations, and now include an Apprentice FMDojo for supported teams."
pubDate: "2026-06-18T09:00:00-07:00"
updatedDate: "2026-06-18T09:00:00-07:00"
author: "Agnes Riley"
tags: ["Blog", "FileMaker", "Hosting", "FMDojo"]
categories: ["Blog"]
permalink: /filemaker-hosting-lxc-apprentice-fmdojo/
---

FileMaker hosting has changed a lot since the days when the default answer was simply "put it on a Mac mini and monitor it closely." That model still works in the right situation, but it is no longer the only good option. Modern FileMaker systems need better isolation, cleaner upgrades, repeatable server builds, and a support model that helps teams understand what is happening in their environment.

That is why we are expanding our hosting types and standardizing new managed FileMaker hosting around LXC-based server isolation where it makes sense.

The short version: LXC gives us many of the operational benefits people associate with containers, while still behaving much more like a real Linux server. For FileMaker Server, that difference matters.

## The New Hosting Shape

Our hosting plans are moving toward clearer operational categories:

- **Shared FileMaker hosting** for smaller systems that need reliable managed hosting without a dedicated server footprint.
- **Dedicated FileMaker hosting** for teams that need their own server resources, custom configuration, or tighter operational control.
- **LXC-isolated FileMaker hosting** for Linux-based FileMaker Server environments where isolation, repeatability, and resource control matter.
- **Specialized companion hosting** for services such as SuperContainer or related application components that support a FileMaker deployment.

The goal is not to make hosting sound more complicated. It is to match the hosting architecture to the way the FileMaker system is actually used.

A small departmental app does not need the same isolation model as a business-critical system with scheduled server-side scripts, WebDirect users, API traffic, external integrations, and strict backup requirements. A mature FileMaker deployment often has more in common with a line-of-business application stack than with a simple database file sitting on a server.

## Why LXC Instead of Docker?

Docker is excellent for many application workloads. We use and respect it. It is a strong choice when an application is built from small stateless services, has a clean image-based deployment process, and expects its runtime to be replaced frequently.

FileMaker Server is different.

FileMaker Server is not just a single stateless process. It is a managed server environment with persistent databases, scheduled scripts, SSL certificates, plug-ins, logs, backups, Admin Console configuration, WebDirect, Data API, OData, and operating-system-level expectations. It benefits from isolation, but it also benefits from looking and behaving like a normal server.

That is the reason we chose LXC for this hosting layer.

LXC, or Linux Containers, provides operating-system-level virtualization. An LXC container has its own process space, filesystem, network configuration, resource limits, and service management, but it runs on the host's Linux kernel. From an administrator's point of view, it feels much closer to managing a lightweight virtual machine than packaging one process into a Docker image.

For FileMaker Server, that gives us a practical balance:

- Stronger isolation than putting multiple workloads directly on one host.
- Less overhead than a full virtual machine.
- A server-like environment that works well with system services, logs, certificates, backups, and operational tooling.
- Cleaner separation between customers, projects, or environments.
- More predictable management for long-running stateful services.

## LXC vs. Docker for FileMaker Hosting

| Area | LXC | Docker |
| --- | --- | --- |
| Best fit | Long-running, server-like workloads | Application services packaged as images |
| Operating model | Feels like a lightweight Linux server | Feels like an application container |
| FileMaker Server fit | Good fit for persistent services, logs, backups, SSL, and admin workflows | Possible, but often awkward for full server lifecycle management |
| Persistence | Natural fit for durable files, mounted storage, and server state | Works with volumes, but the image model encourages disposable runtime containers |
| Service management | Works well with system services and conventional Linux administration | Usually expects one main process per container |
| Upgrades | Can be handled like a managed server upgrade with snapshots and rollback planning | Often pushes toward rebuilding images and replacing containers |
| Isolation | Strong OS-level isolation with resource controls | Strong process/application isolation with image boundaries |
| Operational feel | Similar to a small VM without the same overhead | Similar to deploying an app artifact |

The important point is not that LXC is "better" than Docker in every context. It is not. The important point is that LXC is a better fit for how we want to operate FileMaker Server.

FileMaker hosting is a stateful, support-heavy workload. The database files matter. Backup windows matter. Scheduled scripts matter. Certificate renewals matter. Plug-ins and external services matter. Logs matter when something fails at 2 AM. We want an environment that treats those things as first-class operational concerns instead of forcing them into a pattern designed for disposable app containers.

## What This Means in Practice

For clients, the architecture should mostly show up as a better support experience.

LXC-based hosting lets us isolate environments cleanly while still managing them with familiar server operations. We can control resources, snapshot environments, separate services, and reduce the blast radius of one workload affecting another. It also gives us a cleaner path for testing upgrades before applying them to a production FileMaker Server.

That matters because FileMaker systems are often quietly business-critical. They may handle quoting, inventory, research data, scheduling, shipping, grant management, school operations, production workflows, or customer records. Hosting should be boring in the best way: predictable, monitored, backed up, and understandable.

The choice of LXC supports that goal.

## Apprentice FMDojo Is Now Included

The other change is just as important: our hosting plans now include an **Apprentice FMDojo**.

Hosting should not stop at keeping the server online. FileMaker teams also need help understanding their systems, improving scripts and calculations, planning changes, and troubleshooting safely. FMDojo gives hosted teams a FileMaker-aware assistant that understands the platform much better than a general-purpose AI chatbot.

With Apprentice FMDojo included, hosted clients have a practical place to ask FileMaker-specific questions, work through script logic, reason about calculations, review schema decisions, and get help with the kinds of day-to-day development questions that come up around a live system.

That pairs naturally with managed hosting. The server provides the stable foundation; FMDojo helps the team work more confidently on the solution running there.

## Why This Combination Matters

Good FileMaker hosting is not just hardware. It is the combination of:

- A server architecture that fits FileMaker's stateful nature.
- A backup and monitoring strategy that respects production data.
- Operational isolation that makes support and maintenance cleaner.
- Development guidance that helps teams make better decisions inside the platform.

LXC handles the hosting architecture side. Apprentice FMDojo handles the day-to-day FileMaker support and learning side.

Together, they reflect where we think FileMaker hosting should go: less mystery, less fragile infrastructure, more practical support, and a hosting environment designed around how FileMaker actually runs in the real world.

If you are planning a new FileMaker deployment, moving an older server, or trying to decide whether shared, dedicated, or LXC-isolated hosting is the right fit, [contact us](/contact/) and we can help map the hosting type to the way your system is actually used.

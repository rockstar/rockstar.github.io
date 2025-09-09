Title: Yes Chef! — Everything in its place
Date: 2025-09-12 12:00:00 -0600
Slug: 
Status: draft

![A kitchen organized and ready for service[^1]]({attach}/images/mise-en-place-1.jpg)


Before the first ticket prints, a good cook in a professional culinary kitchen knows exactly where everything is. This isn’t by accident. To describe the order and organization of their kitchen, the French use the phrase _mise en place_, meaning “to put in place” or, more colloquially accepted, “everything in its place.” _Mise en place_ isn’t about neatness–it’s about survival.

When a line cook can’t find a spoon to stir the sauce, or there aren’t a stack of plates ready to plate food, it doesn’t cost one second: it costs ten steps, three interruptions, and a break in flow. Each departure from a normal flow is a potential accident that has a snowball effect. In a kitchen, the efficiency of your movements is the difference between a 15 minute ticket time and a 30 minute ticket time–_mise en place_ is the antidote to “wasted motion.”

In software development practices, we often lack that _mise en place_, and we shrug it off as “technical debt.” In code, _mise en place_ looks like clear ownership, working development environments, interfaces that are simple to understand, and documentation that is easy to locate and clear and concise. It may not be glamorous, but it’s the difference between flow and frustration.

What we often miss in our haste to consistently deliver value in software engineering is this: chaos compounds. In a kitchen, cooks may have to stop to dice more onions because the prep team didn’t prep enough; in software, bugs pile up while someone digs through tribal knowledge. Disorder multiplies faster than the workload, and eventually that disorder becomes all there is.

> If you let your mise en place run down, get dirty and disorganized, you’ll quickly find yourself spinning in place and calling for back up. That’s what the inside of your head looks like now. Work clean! —Anthony Bourdain, Kitchen Confidental

Consider the following example, which may be painfully familiar: Krista, a new engineer is tasked with fixing a bug in the production build pipeline. They track down the bug to an image catalog service, open slack and says “What team own the image catalog service?” “Oh, that was owned by Steven’s team, but when he left, that team got dissolved and the members were split up to other teams.” Krista’s task has just become immensely more complex. Now we have to get managers and organizations involved, we have to find resources to bring an orphaned service 

The team James is on becomes the new owner of the image catalog service, and James is assigned to work with Krista on the bug. “Where are the docs for this interface,” he asks. “They’re on the wiki.” James types “image catalog service” into the wiki search box and gets 45 results, six of which claim to be api design doc, but all describe a slightly different interface, none of which appear to be correct.

Days (or weeks) later, the cause of the defect ends up being an unused attribute from the serialized data sent to the service, and the fix is a single line change. When James asks for time to update the documentation for the issue, he’s told there isn’t time, and he’ll just have to “make do.” Four months later, James accepts a role at a competing company, and that domain knowledge is lost to the org. This pattern will repeat itself when an issue comes up again[^2].

Often times, managers, whether people, project, or product management, shrug off requests to get organized almost as a developer trope, as if these “Keep the Lights On” tasks are optional nice-to-haves. The familiar refrain is something like “the perfect is the enemy of the good,” as though a platitude could be successfully used as a cudgel. But when you organize, you’re not just helping yourself — you’re making sure your teammates don’t waste time hunting for tools, docs, or ownership. Order is a form of respect.

In a kitchen, every hour spent sharpening the knives and setting the station pays back in smoother service. In software, the same is true: organization isn’t overhead. It’s how you protect flow.

——

[^1]: <a href=“https://www.vecteezy.com/free-photos/commercial-kitchen”>Source</a>
[^2]: I have come to call this phenomenon “Just Enough Development.” It’s the equivalent of a finger in the dam: it’s easy to think “oh, we’ve plugged the hole, so we should be good for a bit.” The issue here is that the plug was someone’s proverbial finger, someone’s mental cycles, etc. Now you have to keep that specific person around, and hope (a) they are a particular brand of neurodiverse, and (b) aren’t the type to hoard that information in the name of “job security,” because those types aren’t healthy in your org.
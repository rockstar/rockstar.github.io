Title: Move Fast and Brake Things
Date: 2022-12-22 10:00:00 -0600
Status: draft
> Unless you are breaking stuff, you are not moving fast enough. -Mark Zuckerberg

In 2009, when [we first heard "Move fast and break things,"](https://www.businessinsider.com/mark-zuckerberg-innovation-2009-10) I can understand how that sounded innovative. At the time, AWS was only a few years old, many of the technologies that we would consider "modern" didn't even exist. Most companies were still experimenting with Agile Software Development™. Netflix was still sending DVDs in the mail! "Move fast and break things" sounded innovative and bold. Even established enterprise organizations were embracing the idea.

![Felix  Sargent tweets "'Move fast and break shit' is why we have so much broken shit]({attach}/images/felix-sargent-move-fast.png)

Of course, in all-to-familiar fashion, we seemed to spend a lot of time taking the wrong lessons from that. [We sent it too hard](https://www.youtube.com/watch?v=_PVOuZ21-Dg), almost recklessly, and the products we produced felt improvised and careless. If one _didn't_ break something, it was a fluke, because broken things were the default. Our tools were broken, our 

I'm not suggesting we go back to waterfall development, or we start to consider VC-flavored hot takes as anything more than off-the-cuff, thoughtless platitudes that reek of privilege. I do think that if we want to talk about going fast, we should consider what makes fast people fast: brakes. There's a joke in motorsports racing where people might say "I'm all gas, no brakes." There are definitely folks who say that seriously, and those people are the ones most likely to get quite hurt. Anyone who aspires to be the fastest, i.e. to win the race, knows that _the fastest people use their brakes the most_.

![Kenny Coolbeth uses his rear brakes so much his rotor glows red]({attach}/images/coolbeth-move-fast.png)

That sounds counter-intuitive, I know. Slow down to go fast? Yes. Racing is about following an ideal line, about going through corners and down straightaways on a precise path. Using the brakes engages the suspension, changes the weight distribution, pushes the tires into the ground, and (ideally) keeps one headed in the right direction. Analysts and talking heads will use phrases like "blow the corner," "left the door open," and "miss the apex" to talk about how a racer might fall off line. Falling off the line may end up being detrimental to going fast and "losing a second" could cost you the race. The racing line is so important that racers who are a lap down when faster traffic is coming through are usually instructed to move "off line" so that those faster pilots can continue on unimpeded[^1]. 

In software development process, we want to go fast. We want to quickly deliver fixes for defects. We want to ship features quickly. We want to delight our users, but we also want to _feel_ successful. That success often comes in the form of delivering quality at a good pace[^2]. The only way to keep pace, to stay "on line," to be headed in the right direction, is to value the tools we have that keep us headed in the right direction.

So what are the brakes in the software development process?

The easy (lazy?) answer is tests. Any mature piece of software will have someone griping about how the tests slow them down for whatever reason. Done carefully[^3], tests enforce your contracts between APIs, ensures existing functionality continues to function as designed, etc. However, it also reduces the cognitive load required to make changes. You don't have to know how `FooClass` interacts with `BarClass` if you're only working on the interface between `FooClass` and `BazClass`. If something breaks, the tests will tell you. Without the tests, you'll either have to manually test in failure-prone ways, i.e. not going fast at all, or your users will tell you when something breaks, causing you to have to suddenly slow down to context switch to fixing something instead of planned work.

We see more "brakes", however, in our modern CI/CD. Rust projects may have enforcement on formatting, `clippy` checks, and benchmark assertions. Python has `mypy` (you are using types in python, right?). These tools don't have _technical_ value; usually, they allow teams to have a shared context, and to have expectations for how things are. These things are still important, and allow the team, collectively, to go fast. The collective team going fast is the sweet spot; in racing, it is often advantageous to work with other racers in a race, even if it means going slower sometimes, to give yourself a better chance of going faster in long-term. Prioritizing the team's needs over an individual's needs is going fast.

The last series of brakes that I think we often overlook is _process_. Sprint planning, retrospectives, design meetings[^4], all of these things slow down the tangible work product, get the vehicle pointed in the right direction, and collectively decide when it's appropriate to apply throttle again. I personally race on dirt more than asphault, which is less predictable and constantly changing, so I have to think constantly about what's working and what's not when considering line choice. The same goes for much of software development. The landscape will change, the priorities will shift, the deadlines will loom, and scope will be cut. This process is the _ultimate_ in "software braking technology," as it allows us to be critical of our direction, of our line, and to constantly re-evaluate. _Can we be faster?_

So yes, move fast. This industry moves so fast that the landscape is unrecognizable from the original quote. But let's be responsible, and build things that last. Move fast, and brake things.

[^1]: Racers who are lap traffic are usually shown some variation of a blue flag (sometimes it's blue and yellow). There is a common saying that if you get a blue flag, it means "there's a race going on, and you're not in it."
[^2]: The dopamine hit from delivering, from releasing features, that's what keeps me going. That's the thing I want put directly in my veins. The quicker and more often I get that hit, the better off I am. It's probably not the healthiest thing, but I've spent a lot of time chasing that feeling, which has helped me understand what works and what doesn't.
[^3]: As with all things, we can misuse our tests, our tools, our _brakes_ in a way that not only slows us down, but actively sabotages us. The analogy can break down if we try and be too complete with it, so we'll leave that for another racing analogy.
[^4]: One of the best design meetings I've ever attended (and that I thought was a waste of time) was to get everyone on board with vocabulary. Are we all using the same words to mean different things? Can we agree on common vocabulary that all means the same thing? When writing this post, I kept coming back to that memory and realizing that not only were we not "on line," we all had a different idea of what "on line" was, and where we should be headed.
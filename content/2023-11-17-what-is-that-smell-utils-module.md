Title: What’s that smell? The utils module
Date: 2023-10-16 12:00:00 -0600
Status: draft

![The junk drawer, where you put things you want to hold onto but don’t have a place for]({attach}/images/IMG_0061.jpeg)

You’ve started a new project and you’re feeling excited. The code is well-factored, it does the minimum viable thing. You’ve shipped 0.1. Maybe you’ve even released a few different features to production.

Inevitably, a feature request comes in that requires some work that’s unrelated to your core product. Maybe it’s a one-off integration with a third party service or a function that you’ll call in a number of places that are unrelated. You stare at your editor and think about where you’ll put this code.

You type `touch utils.py` (or `.c` or `.rs` or, if you’re unlucky in life[^1], `.go`). This is good; it’s a utility, right? You put your code in there, deliver your feature on time, and continue on with your life.

Your biggest customer asks for a feature that seems pretty unrelated to your product, but they’re willing to give you a bunch of money, so you put the feature in your roadmap. When the time comes, your favorite coworker takes the task. Where do they put their seemingly unrelated code? Oh, `utils` seems like a good place.

Fast forward a year, and `utils` is 3500 lines of code. You think “I’ll break these up into smaller modules inside utils.” Now you’re grouping functionality and giving structure to the unstructured. Now your code is much more organized.

Fast forward another six months, and you realize that _most_ of the logic for your application is found in `utils`. Everything you thought would just be a quick bolt-on is now a basic primitive that you’re building features on regularly. Most of your business logic lives there.

The moment your project creates a `utils` module/package, you’ve reduced the amount of thought that is required in figuring how to categorize your work. At best, you’ve now got a “junk drawer,” and at worst, you’ve become lazy in one of the places where it’s not going to benefit you to be lazy.

`utils` is a smell, and if you leave it your fridge, it’s not going to end well for everything else in the fridge.

[^1] I kid, I kid. If you’re into it, get at it.
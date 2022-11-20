Title: Don't Put Code There
Date: 2020-03-20 10:00:00 -0600
> "...created a new python package, and then, you know, created the dunder init file..."
> "Yeah, don't put code there" -JP Calderone, in conversation with me at PyCon 2009

In most modern programming languages with package/module formats that use filesystem path as module path, there's an artifact that they all share: the file signaling 

The weird thing about programming "best practice" guidance is that there will always be someone claiming to have found an exception. Yes, there will always be exceptions, but there's n
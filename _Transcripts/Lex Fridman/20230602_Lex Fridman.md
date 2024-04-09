---
Date Generated: April 08, 2024
Transcription Model: whisper medium 20231117
Length: 12843s
Video Keywords: ['agi', 'ai', 'ai podcast', 'artificial intelligence', 'artificial intelligence podcast', 'c++', 'chris lattner', 'hardware', 'learning', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'machine', 'mit ai', 'mojo', 'programming', 'python', 'software']
Video Views: 1499816
Video Rating: None
---

# Chris Lattner: Future of Programming and AI | Lex Fridman Podcast #381
**Lex Fridman:** [June 02, 2023](https://www.youtube.com/watch?v=pdJQ8iVTwj8)
*  On one access you have more hardware coming in on the other hand you have an explosion of innovation and AI.
*  And so what happened with both TensorFlow and PyTorch is that the explosion of innovation and AI has led to it's not just about matrix multiplication and convolution these things have now like 2000 different operators.
*  On the other hand you have I don't know how many pieces of hardware out there are there it's a lot part of my thesis for my belief of where computing goes if you look out 10 years from now it's not gonna get simpler.
*  This isn't going back to where we came from it's only get weirder from here on out right and so to me the exciting part about what we're building is it's about building that universal platform which world can continue to get weird again I don't think it's avoidable it's physics.
*  But we can help lift people scale do things with it and they don't have to rewrite their code every time a new device comes out and I think that's pretty cool.
*  The following is a conversation with Chris Latner his third time on this podcast as I've said many times before he's one of the most brilliant engineers in modern computing having created LLM compiler infrastructure project the clan compiler the swift programming language a lot of key contributions to TensorFlow and TPUs as part of Google.
*  He served as vice president of autopilot software at Tesla was a software innovator and leader at Apple and now he co created a new full stack AI infrastructure for distributed training inference and deployment.
*  On all kinds of hardware called modular and a new programming language called mojo that is a superset of Python giving you all the usability of Python but with the performance of C C++.
*  In many cases mojo code has demonstrated over 30,000 X speed up over Python if you love machine learning if you love Python you should definitely give mojo a try.
*  This programming language this new AI framework and infrastructure and this conversation with Chris is mind blowing I love it.
*  It gets pretty technical at times so I hope you hang on for the ride this is the Lex treatment podcast to support it please check out our sponsors in the description and now your friends here's Chris Latner.
*  It's been I think two years since we last talked and in that time you somehow went and co created a new programming language called mojo so it's optimized for AI it's a superset of Python.
*  Let's look at the big picture what is the vision for mojo.
*  From mojo well so I mean I think you have to zoom out so i've been working on a lot of related technologies for many many years so i've worked on LVM and a lot of things and mobile and servers and things like this.
*  But the world's changing and what's happened with AI is we have new GPUs and new.
*  Machine learning accelerators and other ASICs and things like that that make AI go real fast at Google I worked on TPUs that's one of the biggest large scale deployed systems that exist for AI and really what you see is if you look across all of the things are happening in the industry there's this new compute platform coming and it's not just about.
*  CPUs or GPUs or TPUs or NPUs or IPUs or whatever all the PUs right it's about how do we program these things.
*  Right and so for software folks like us right it doesn't do us any good if there's this amazing hardware that we can't use and one of the things you find out really quick is that.
*  Having the theoretical capability of programming something and then having the world's power and the innovation of all the all the smart people in the world get unleashed on something can be quite different.
*  And so really where Mojo came from was starting from a problem of we need to be able to take machine learning take the infrastructure underneath it and make it way more accessible way more usable way more understandable by.
*  Normal people and researchers and other folks that are not themselves like experts in GPUs and things like this and then through that journey we realize hey we need some tax for this we need to do programming language.
*  So one of the main features of language I say so fully ingest is that it allows you to have the file extension to be an emoji or the fire emoji which is one of the first.
*  Emojis used as a file extension I've ever seen in my life and then you ask yourself the question why in the 21st century are we not using Unicode for file extensions.
*  This I mean it's an epic decision I think clearly the most important decision made the most but you could also just use Mojo as the file extension.
*  Also okay so take a step back I mean come on Max you think that the world's ready for this this is a big moment in the world right.
*  This is where we release this onto the world this is innovation.
*  I mean it really is kind of brilliant emojis is such a big part of our daily lives why is it not in programming.
*  Well and like you take a step back and look look at what file extensions are right there basically metadata right and so why are we spending all the screen space on them and all the stuff also you know you have them stacked up next text files and PDF files and whatever else like.
*  If you're gonna do something cool you want to stand out right emojis are colorful they're visual they're beautiful.
*  Right what's been the response so far from is there support on like windows on operating system in displaying like file explorer.
*  Yeah the one problem I've seen is that get doesn't escape it right and so it thinks that the fire emoji is unprintable and so it like prints out weird hex things if you use the command line get tool but everything else as far as I'm aware works fine and I have faith that get can be important.
*  So I'm not sure how it's fine get up is fine yeah get up is fine visual studio code windows like all this stuff totally ready because people have internationalization in their normal part of their past.
*  So it's just like taking the next step right somewhere between oh wow that makes sense cool I like any things to oh my god you're killing my baby like what are you talking about this can never be like I can never have it was how am I going to type this.
*  Like all these things and so this is something where I think that the world will get there you don't have to bet the whole farm on this I think we can provide both paths but I think it'll be great.
*  When can we have emojis as part of the code I wonder.
*  Yeah so I mean lots of languages provide that so I think that we have partial support for that it's probably not fully done yet but.
*  I think that we have partial support for that it's probably not fully done yet but but yeah you can you can do that for example in swift you can do that for sure so an example we give gave it apple was the dog cow.
*  Yeah so it's a classical Mac heritage thing and so use the dog and the cow emoji together and that could be your variable name but of course the internet went and made pile of poop for everything yeah so you know if you want to name your function pile of poop then you can totally go to town and see how that gets through code review.
*  Okay so let me just ask a bunch of random questions so is mojo primarily designed for a eyes or is it a general purpose program good question so it's a first and so is driving a lot of the requirements and so.
*  Modular is building and designing and driving mojo forward and it's not because it's an interesting project theoretically to build it's because we need it.
*  So modular we're really tackling the AI infrastructure landscape and the big problems in AI and the reasons that is so difficult to use and scale and.
*  Adopt and deploy and like all these big problems in AI and so we're coming out from that perspective now when you do that when you start tackling these problems you realize that the solution to these problems isn't actually an AI specific solution.
*  And so what we're doing this rebuilding mojo to be a fully general programming language and that means that you can.
*  Obviously tackle GPUs and CPUs and like these AI things but it's also a really great way to build.
*  NumPy and other things like that or you know just if you look at what many Python libraries are today often they're a layer of Python for the API and they end up being C and C++ code underneath them.
*  That's very true in AI that's true in lots of other demands as well and so anytime you see this pattern that's an opportunity for mojo to help simplify the world and help people have one thing.
*  To optimize through simplification.
*  By having one thing so you mentioned modular mojo is the programming language modular is the whole software stack.
*  So just over a year ago we started this company called modular yeah yeah what modular is about is it's about taking AI and up leveling it.
*  Into the next generation right and so if you take a step back what's gone on in the last five six seven eight years is that we've had things like tensorflow and pytorch and these other systems come in you've used them you know this.
*  And what's happened is these things have grown like crazy and they get tons of users it's in production deployment scenarios it's being used to power so many systems and AI is all around us now now it used to be controversial years ago but now it's a thing.
*  But the challenge with these systems is that they haven't always been.
*  Thought out with current demands in mind and so you think about it when where were LLMS eight years ago.
*  Well they didn't exist right AI has changed so much and a lot of what people are doing today are very different than when these systems were built.
*  And meanwhile the hardware side of this has gotten into a huge mess there's tons of new chips and accelerators and every every big companies announcing a new chip every day it feels like.
*  And so between that you have like this moving system on one side moving system on the other side and it just turns into this gigantic mess which makes it very difficult for people to.
*  Actually use AI particularly in production deployment scenarios and so what modular is doing is we're helping build out that software stack to help solve some of those problems so then people can be more productive and get more AI research into production.
*  Now what mojo does is it's a really really really important piece of that and so that is part of that engine and part of the technology that allows us to solve these problems.
*  So mojo is a programming language that allows you to do a high level programming the low level programming they do all kinds of programming in that spectrum that gets you closer and closer to the hardware.
*  So take a step back so what do you love about python.
*  Oh boy where do I begin what is love what do I love about python.
*  You're you're guy knows love I know this.
*  Yes.
*  How intuitive it is.
*  How it feels like I'm writing natural language English.
*  How when I can not just write but read other people's code somehow I can understand it faster it's more condensed than other languages like ones I'm really familiar with like C plus plus and C.
*  There's a bunch of sexy little features.
*  Yeah.
*  We'll probably talk about some of them but list comprehension and stuff like this.
*  Also and don't forget the entire ecosystem of all the.
*  Oh yeah that's probably huge there's always something if you want to do anything there's always a package.
*  Yeah so it's not just the ecosystem of the packages and the ecosystem of the humans that do it that that's a really that's an interesting dynamic.
*  I think something about the usability and the ecosystem makes the thing viral it grows and then it's a virtuous cycle.
*  Well there's many things that went into that like so I think that ML was very good for python and so I think that TensorFlow and PyTorch systems embracing python really took and help python grow but I think that the major thing underlying it is that pythons like the universal connector.
*  I really helps bring together lots of different systems so you can compose them and build out larger systems without having to understand how it works but then what is the problem with python.
*  Well I guess you could say several things but probably that is slow.
*  I think that's usually what people complain about right and so so I mean other people complain about tabs and spaces versus curly braces or whatever but I mean those people are just wrong because it is actually just better to use indentation.
*  Wow strong words actually a small tangent let's take that let's take all kinds of tangents.
*  Oh come on Lex you can push me on it I can take it.
*  Design design listen I've recently left emacs for VS code the kind of hate mail I had to receive because on the way to doing that I also said I've considered Vim and chose not to and went with VS code and just on deep religions right.
*  Anyway tabs is an interesting design decision and so you really written a new programming language here yes it is a superset of python but you can make a bunch of different interesting decisions here and you chose actually to stick with python as a.
*  In terms of some of the syntax.
*  Well so let me explain why right so.
*  I mean you can explain this in many rational ways I think that the indentation is beautiful but that's not a rational explanation right so but I can defend it rationally right so first of all python one.
*  Has millions of programmers is huge it's everywhere owns machine learning right so actually it is the thing right second of all if you look at it.
*  C code C++ code Java whatever Swift curly brace languages also run through formatting tools and get indented.
*  And so if they're not indented correctly first of all it will twist your brain around it can lead to bugs and there's notorious bugs that have happened across time where the indentation was wrong or misleading and it wasn't formatted right and so.
*  Turn into an issue right and so what ends up happening in modern large scale code bases people run automatic formatters so now we end up with this indentation and curly braces.
*  What we're gonna have.
*  You know the notion of grouping why not have one thing right and get rid of all the clutter and have a more beautiful thing right also you look at many of these languages like okay well you can have curly braces or you can omit them if there's one statement or you just like enter this entire world of.
*  Complicated design space that objectively you don't need if you have python silent indentation so yeah I would love to actually see statistics on errors made because of indentation.
*  I call many errors are made in python versus in c++ that have to do with basic formatting all that kind of stuff I would love to see I think it's probably pretty minor because once you get.
*  Like your use vs code I do too so if you get vs code set up it does the indentation for you generally right and so you don't you know it's actually really nice to not have to fight it and then what you can see is the editors telling you how your code will work by indenting it which I think is pretty cool.
*  I honestly don't think.
*  I've ever I don't remember having an error in python because I intended stuff wrong.
*  So I mean I think that there's again this is a religious thing and so I can joke about it and I love I love to kind of.
*  You know I realize that this is such a polarizing thing and everyone wants to argue about it and so I like poking at the bear a little bit right but but frankly right come back to the first point python one like it's huge it's an AI it's the right thing for us like we see mojo's being an incredible part of the python ecosystem.
*  We're not looking to break python or change it or quote unquote fix it we love python for it is our view is the python is just not done yet.
*  And so if you look at you know you mentioned python being slow well there's a couple of different things go into that which we can talk about if you want but one of them is it just doesn't have those features that you would use to do see like programming.
*  And so if you say okay well I'm forced out of python and to see for certain use cases.
*  Well then what we're doing is we're saying okay well why why is that can we just add those features that are missing from python back up to mojo and then you can have everything that's great about python all the things you're talking about the love.
*  Plus not be forced out of it when you do something a little bit more computationally intense or weird or hardware or whatever it is you're doing.
*  Well a million questions on ask what high level again is it compiled or is an interpreter language so python is just in time compilation what's what's mojo.
*  So mojo a complicated answer does all the things so it's interpreted as chip compiled and it's technically compiled.
*  And so this is for a variety of reasons so one of the things that makes python beautiful is that it's very dynamic and because it's dynamic one of the things they added is that it has this powerful metaprogramming feature.
*  And so if you look at something like pi torch or tensor flow or or I mean even a simple simple use case like you'd find a class that has the plus method.
*  You can overload the dunder methods like dunder ad for example and then the plus method works on your class and so it has very nice and very expressive dynamic metaprogramming features.
*  In mojo we want all those features come in like we don't want to break python we want all the work but the problem is is he can't run those super dynamic features on an embedded processor.
*  Or on a gpu or if you could you probably don't want to just because of the performance and so we entered this question of saying okay how do you get the power of this dynamic metaprogramming.
*  Into a language that has to be super efficient in specific cases and so what we did was we said okay we'll take that interpreter python has an interpreter in it right take the interpreter and allow to run it compile time.
*  And so now you get is you get compile time metaprogramming and so this is super interesting super powerful because.
*  One of the big advantages you get is you get python style expressive api's you get the ability to have overloaded operators and if you look at what happens inside of like pytorch for example with automatic differentiation and eager mode like all these things.
*  They're using these really dynamic and powerful features at runtime but we can take those features and lift them so they run a compile time.
*  So your c++ metaprogramming with templates.
*  It's super messy it's always it was accidentally I mean different people have different interpretations my interpretation is that it was made accidentally powerful it was.
*  Not designed to be touring complete for example but that was discovered kind of along the way accidentally and so there have been a number of languages in the space and so I usually have templates code instantiation code copying features of various sorts.
*  Some more modern languages or some more newer newer languages let's say like you know they're fairly unknown like zig for example says okay well let's take all of those types you can run it all those things you can do a runtime and allow them to happen at compile time.
*  And so one of the problems with c++ I mean which is one of one of the problems with c++.
*  Is wrong words.
*  It's okay I mean everybody hates me for a variety of reasons anyways I'm sure right.
*  I've written enough the way they show love I've written enough c++ code to earn a little bit of grumpiness with c++ but.
*  But one of the problems with it is that the metaprogramming system templates it's just a completely different universe from the normal runtime programming world and so if you do metaprogramming and programming.
*  Different concepts different stuff going on and so again one of our goals with mojo is to make things really easy to use easy to learn and so there's a natural stepping stone.
*  And so as you do this you say okay well I have to do programming at runtime after programming at compile time.
*  Why are these different things how hard is that to pull it out because that sounds to me as a fan of metaprogramming.
*  Why are these different things how hard is that to pull it out because that sounds to me as a fan of metaprogramming in c++ even.
*  How hard is it to pull that off that sounds really really exciting because you can do the same style programming a compile time and runtime that's really really exciting.
*  And so I mean in terms of the compiler implementation details it's hard.
*  I won't be shy about that it's super hard it requires I mean what mojo has underneath the covers is a completely new approach to the design of the compiler itself and so this builds on these technologies like mlr the invention.
*  But also includes other like caching and other interpreters and jit compilers and other stuff like that like an interpreter inside the within the compiler yes.
*  And so it really takes the standard model of programming languages and kind of.
*  Twist it and unifies it with the runtime model right which I think is really cool and to me the value of that is that again many of these languages have metaprogramming features like they grow macros or something right list right.
*  Yes I know your roots right you know and this is a powerful thing right and so you know if you go back to list one of the most powerful things about it is that it said that the metaprogramming the programming are the same.
*  Right and so that made it way simpler way more consistent way easier to understand reason about and it made it more composable so if you build a library you can use it both at runtime and compile time which is pretty cool yeah and then for machine learning I think metaprogramming.
*  I think we could generally say is extremely useful and so you get features I mean I'll jump around but there's the feature of auto tuning and adaptive compilation just blows my mind yeah well so okay so let's come back to that alright so what is what is what is machine learning like what or what is a machine learning model like you take a pie torch model off there right.
*  It's really interesting to me because what a pipe what pie torch and what tends to flow and all these frameworks are kind of pushing compute into is they're pushing into like this abstract specification of a compute problem.
*  Which then gets mapped in a whole bunch of different ways right and so this is why it became a metaprogramming problem is that you want to be able to say cool I have I have this neural net now run with batch size a thousand right do do do a do a mapping across batch.
*  Or okay I want to take this problem now running across a thousand cpus or gpus right and so like this this problem of like.
*  Describe the compute and then map it and do things and transform it or are like actually it's very profound and that's one of the things that makes machine learning systems really special.
*  Maybe can you describe auto tuning and how do you pull off I mean I guess adaptive compilation is what we're talking about metaprogramming yeah how do you pull off auto to it means that is that as profound as I think it is it seems like a really like.
*  Like you know we'll mention list comprehension to me from a quick glance at mojo which by the way I have to absolutely like dive in.
*  As I realize how amazing this is I absolutely must have and it dad looks like just an incredible feature for machine learning people yeah well so what is auto change to take a step back.
*  Auto tuning is a feature in mojo it's not so very very little of what we're doing is actually research like many of these ideas.
*  Have existed in other systems and other places and so we're doing is we're pulling together good ideas remixing them and making them into hopefully a beautiful system right.
*  Auto tuning the observation is that turns out hardware systems algorithms are really complicated.
*  Turns out maybe you don't actually want to know how the hardware works right a lot of people don't right and so.
*  There are lots of really smart hardware people I know a lot of them where they know everything about okay that the cash size is this and the number of registers is that and if you use this what like the vector is going to be super efficient because it maps directly on to what it can do and like.
*  All this concept for the GPU has SM's and has a warp size of whatever right all the stuff that goes into these things with the title size of a TPU is 128 like these these factoids right.
*  My belief is that most normal people and I love her people also I'm not trying to find literally everybody in the internet but most programmers.
*  Actually don't want to know the stuff right and so if you come at it from perspective of how do we allow people to build both more abstracted but also more portable code.
*  Because you know could be that the vector length changes of the cash size changes it could be that the title size of your matrix changes or the number you know in a 100 versus an H100 versus a Volta versus a whatever GPU have different characteristics right.
*  A lot of the algorithms you run are actually the same but the parameters these magic numbers you have to fill in and up being really fiddly numbers that an expert has to go figure out and so what auto tuning does it says okay well guess what there's a lot of compute out there.
*  Right so instead of having humans go randomly try all the things or do a grid search or go search some complicated multi dimensional space.
*  How about we have computers do that right and so auto tuning does is you can say hey here's my algorithm.
*  If it's a matrix operation or something like that you can say okay I'm going to carve it up into blocks I'm going to do those blocks in parallel and I want to this this with 128 things that I'm running on I want to cut it this way or that way or whatever.
*  And you can say hey go see which one's actually empirically better on the system.
*  And then the result of that you cash for that system.
*  And so come back to twisting your compiler brain right so not only does the compiler have an interpreter that she used to do metaprogramming that compiler that interpreter that metaprogramming now has to actually take your code and go run it on a target machine.
*  See see which one likes the best and then stitch it in and then keep going right.
*  So part of the compilation is machine specific.
*  Yeah well so I mean this is an optional feature I see you don't have to use it for everything but yeah if you're if you're so one of one of the things that were in the quest of is ultimate performance.
*  Yes right ultimate performance is important for a couple of reasons right so if you're an enterprise you're looking to save costs and compute and things like this ultimate performance translates to you know fewer servers.
*  If you care about the environment better performance leads to more efficiency I mean you could joke and say like you know Python is bad for the environment.
*  And so if you move to mojo it's like at least 10x better just out of the box and keep going right.
*  But but performance is also interesting because at least a better products and so in the space of machine learning right if you reduce the latency of a model.
*  So runs faster so every time you query the server and the model it takes less time well then the product team can go and make the model bigger.
*  Well that's actually makes it so you have a better experience as a customer and so a lot of people care about that.
*  So for auto tuning for like tile size you mentioned one twenty for GPU you would specify like a bunch of options to try just in the code.
*  Just simple statement and then you just set and forget and know depending what wherever it compiles it'll actually be the fastest.
*  Exactly the beauty of this is that it helps you know a bunch of different ways right so if you're building.
*  So often what will happen is that you know you've written a bunch of software yourself right you you wake up one day say I have an idea I'm going to go cut up some code I get to work.
*  I forget about it.
*  Move on with life I come back six months or a year or two years or three years later you dust it off and you go use it again and new environment.
*  And maybe your GPU is different maybe you're running on a server instead of a laptop maybe whatever right.
*  And so the problem now is you say OK well I mean again not everybody cares about performance but if you do you say OK well I want to take advantage of all these new features.
*  I don't want to break the old thing though right and so the typical way of handling this kind of stuff before is you know if you're talking about people's templates are you talking about.
*  See with macros you end up with if deaths you get like all these weird things get layered in make the code super complicated and then how do you test it.
*  It becomes this crazy complexity multidimensional space you have to worry about and you know that just doesn't scale very well.
*  Actually we just jump around if I go to some specific features like the increase in performance here that we're talking about can be just insane.
*  You write them moja can provide a thirty five thousand X speed up over python how does it do that.
*  Yeah so I can even do more but we'll get to that so.
*  So first of all when we say that we're talking about what's called CPython it's the default Python that everybody uses when you type Python three that's like typically the one you use right CPython is an interpreter.
*  And so interpreters they have an extra layer of like byte codes and things like this that they have to go read parse interpret and make some kind of slow from that perspective and so one of the first things we do is we move to a compiler.
*  And so just moving to a compiler getting the interpreter out of the loop is two to five to ten X speed up depending on the code so just out of the gate.
*  She's in more modern techniques right now if you do that one of the things you can do is you can start to look at how CPython started to lay out data.
*  And so one of the things that CPython did and this isn't part of the Python spec necessarily but this is just sets of decisions is that.
*  If you take an integer for example it'll put it in an object because in Python everything's an object and so they do the very logical thing of keeping the memory representation of all objects the same.
*  So all objects have a header they have like payload data they and what this means is that every time you pass around an object you're passing around a pointer to the data.
*  Well this has over it turns out that modern computers don't like chasing pointers very much and things like this it means you have to allocate the data.
*  You have to reference count it which is another way of the Python uses keep track of memory and so this has a lot of overhead and so if you say okay let's try to get that out of.
*  The heap out of a box out of an indirection and into the registers.
*  That's that's another 10 X.
*  So it adds up if you if you're reference counting every single every single thing you create that as up.
*  Yep and if you look at you know people complain about the Python Gill this is one of the things that hurts parallelism that's because the reference.
*  Right and so the Gill and reference counting are very tightly intertwined in Python it's not the only thing but it's very tightly intertwined and so then you lean into this and say okay cool well.
*  Modern computers they can do more than one operation at a time and so they have actors what is a vector well vector allows you to take one instead of taking one piece of data doing an add or multiply and then.
*  Pick up the next one you can now do a four or eight or 16 or 32 at a time right well Python doesn't expose that because of reasons and so now you can say okay well you can adopt that.
*  Now you have threads you have like additional things like you can control memory and so what module allows you to do is it allows you to start taking advantage of.
*  All these powerful things have been built into the hardware over time and it gives the library gives very nice features so you can say just parallel as a student parallel.
*  Right so it's very very powerful weapons against slowness which is why people have been I think having fun like just taking code and making go fast because it's.
*  Just kind of an adrenaline rush to see like how fast you can get things.
*  Before I talk about some of the interesting stuff with parallelization all that let's let's first talk about like the basics we talked to indentation right so this thing looks like Python.
*  It's sexy and beautiful like Python as I mentioned is it a typed language so what's the role of types yeah good question so Python has types.
*  It has strings as integers it has dictionaries and like a lot of stuff but they all live at runtime right and so.
*  Because all those types of runtime and Python you never you don't have to spell them Python also has like this whole typing thing going on now and a lot of people use it yeah.
*  I'm not talking about that that's that's kind of a different thing we can go back to that if you want but but typically the.
*  You know you just say I take I have a deaf and my deaf takes two parameters on your call them a and B and I don't have to write a type okay so that.
*  Is great but what that does is that forces what's called a consistent representation so these things have to be a pointer to an object with the object header and they all have to look the same.
*  And then when you dispatch a method you go through all the same different paths no matter what the the receiver whatever that type is.
*  So what mojo does is it allows you to have more than one kind of type and so what it does is allows you to say okay cool I have I have an object.
*  Objects behave like Python does and so it's fully dynamic and that's all great and for many things classes like that's all very powerful and very important.
*  But if you want to say hey it's an integer and it's 32 bits or 64 bits or whatever it is or it's a floating point value.
*  64 bits well then the compiler can take that and it can use that to do way better optimization and turns out again getting rid of the interactions it's huge.
*  And you can get better code completion because you have because compiler knows what the type is and so it knows what operations work on it and so that's actually pretty huge.
*  And so what mojo does allows you to progressively adopt types into your program and so you can start again it's compatible.
*  With Python and so then you can add however many types you want wherever you want them and if you don't want to deal with it you don't have to deal with it.
*  And so one of one of you know our opinions on this is it's not that types are the right thing or the wrong thing it's that they're a useful thing.
*  Which was kind of optional it's not strict typing you don't have to specify type exactly.
*  Okay so starting from the thing that Python is kind of reaching towards right now with trying to inject types into it.
*  What yeah with a very different approach but yes yeah what's the different approach i'm actually one of the people.
*  They have not been using types very much in Python.
*  So why did you say.
*  It just well because I know the importance it's like adults use strict typing and so I refuse to grow up in that sense it's a it's a kind of rebellion but I just know that.
*  It probably reduces the amount of errors even just for forget about performance improvements it probably reduces errors of when you do strict typing.
*  Yes I mean I think it's interesting if you look at that right and the reason I'm giving you a hard time is that that there's this.
*  This cultural norm this pressure this like there has to be a right way to do things like you know only grown ups only do it one way and if you have to do that you should feel bad.
*  Right like some people feel like it pythons a guilty pleasure or something and it's like when it gets serious I need to go rewrite it right.
*  Well I mean cool I understand history and I understand kind of where this comes from but I don't think it has to be a guilty pleasure yeah.
*  If you look at that you say why do you have to rewrite it we have to rewrite it to deploy.
*  Well why do you want to deploy well you care about performance you care about predictability or you want you know tiny thing on the server that has no dependencies or you know you have objectives you're trying to attain.
*  So what if python can achieve those objectives so if you want types well maybe you want types because you want to make sure you're passing the right thing sure you can add a type.
*  If you don't care you're prototyping some stuff you're hacking some things out you're like pulling some ram code off the internet it should just work.
*  Right and you shouldn't be like pressured you shouldn't feel bad about doing the right thing or the thing that feels good now.
*  If you're in a team right you're working at some massive internet company and you have 400 million lines of python code.
*  Well they may have a house rule that you use types yeah right because it makes it easier for different humans to talk to each other and understand what's going on and bugs at scale right.
*  And so there are lots of good reasons why you might want to use types but that doesn't mean that everybody should use them all the time right so what mojo does is it says cool well.
*  Allow people to use types and if you use types you get nice things out of it right you get better performance and things like this right but mojo is a full compatible superset of python.
*  Right and so that means it has to work without types it has to support all the dynamic things has support all the packages has support.
*  For comprehension list comprehensions and things like this right and so that that that starting point I think is really important and I think that.
*  Again you can look at why I care so much about this and there's many different aspects of that one of which is the world went through a very challenging migration from python 2 to python 3.
*  Right this is this migration took many years and it was very painful for many teams right and there's a lot of a lot of things that went on in that.
*  I'm not an expert in all the details I honestly don't want to be I don't want the world to have to go through that.
*  Right and you know people can ignore mojo and if it's not their thing that's that's cool but if they want to use mojo I don't want them to have to rewrite all their code.
*  I mean this okay the superset part is.
*  There's just so much brilliant stuff here that definitely is is incredible we'll talk about that yeah first of all how's the typing implemented differently in in python versus mojo so this heterogeneous flexibility you said it's definitely implemented.
*  Yeah so i'm not a full expert in the whole backstory and types in python so i'll give you i'll give you that I can give you my understanding.
*  My understanding is basically like many dynamic languages the ecosystem went through a phase where people went from writing scripts to writing large scale.
*  Huge code bases in python and at scale kind of helps have types people want to be able to reason about interfaces what do you expect string or an inch or like what these basic things right.
*  And so what the python community started doing is it started saying okay let's have tools on the side checker tools right to go and like enforce invariance check for bugs try to identify things these are called static analysis tools generally and so these tools run over your code and try to look for bugs.
*  What ended up happening is there's so many of these things so many different weird patterns and different approaches on specifying the types and different things going on that the python community realize and recognize hey hey hey there's a thing here.
*  And so what they started to do is they started to standardize the syntax for adding types to python.
*  Now one of the challenges that they had is that they're coming from kind of this fragmented world where there's lots of different tools they have different trade-offs and interpretations and the types mean different things and so.
*  If you look at types in python according to the python spec the types are ignored.
*  Right so according to python spec you can write pretty much anything in a type position okay and.
*  You can technically you can write any expression okay now that's beautiful because you can extend it you can do cool things you can write build your own tools you can build your own house linter or something like that right.
*  But it's also a problem because any existing python program may be using different tools and they have different interpretations and so if you adopt somebody's package into your ecosystem try around the tool you prefer.
*  It may throw out tons of weird errors and warnings and problems just because it's incompatible with how these things work also because they're added late and they're not checked by the python interpreters always kind of more of a hint than it is a requirement.
*  Also the CPython implementation can't use them for performance and so it's really that's a big one right so you can't utilize the for the compilation for the just in time compilation okay exactly and this this all comes back to the design principle of its.
*  It's kind of the kind of hints they're kind of the definitions a little bit murky it's unclear exactly the interpretation in a bunch of cases and so because of that you can't actually.
*  Even if you want to it's really difficult to use them to say like it is going to be an intent if it's not it's a problem right a lot of code would break if you did that.
*  So so in mojo right so you can still use those kind of type annotations it's fine but in mojo if you declare a type and you use it, then it means it is going to be that type.
*  And the compiler helps you check that enforce it and it's safe and it's not it's not a like best effort and kind of a thing so if you try to show the string type thing into an integer you get an error.
*  From the compiler compile time.
*  Nice okay what kind of basic types are there yeah so mojo is pretty hardcore in terms of what it tries to do in the language.
*  Which is the philosophy there is that we.
*  If you if you look at python right that's a beautiful language because it's so extensible right and so all of the different things in python like for loops and plus and like all these things can be.
*  Access through these underbar methods okay so you have to say okay if I make something that is super fast I can go all the way down to the metal why do I need to have integers built into the language.
*  And so what mojo does is says okay well we can have this notion of structs so you have classes in python now you can have structs classes are dynamic structure static.
*  Cool we can get high performance we can write c++ kind of code with structs if you want these things mix and work beautifully together.
*  But what that means is that you can go and implement strings and instance floats and arrays and all that kind of stuff in the language.
*  Right and so that's really cool because you know to me as a ideal idealizing compile compiler language type of person right what I want to do is I want to get magic out of the compiler.
*  And put in the libraries because if somebody can you know if we can build an integer that's beautiful and it has an amazing API it does all the things you'd expect an integer to do.
*  We don't like it maybe you want a big integer maybe you want to like sideways integer I don't know like what what all the space of integers are.
*  Then then you can do that and it's not a second class citizen.
*  And so if you look at certain other languages like c++ one I also love and use a lot.
*  Int is hard code in the language but complex is not.
*  And so isn't it kind of weird that you have this STD complex class but you have int and complex tries to look like a natural numeric type and things like this.
*  But integers and floating point have these like special promotion rules and other things like that that are magic and they're hacked into the compiler and because of that you can't actually make something that works like the built in types.
*  Is there something provided as a standard because you know because it's AI first you know numerical types are so important here so is there something like a nice standard implementation of integer and flow.
*  Nice standard implementation of integer and flow.
*  Yes, so we're still building all that stuff out so we provide interest and floats and all that kind of stuff we also provide like buffers and tensors and things like that they'd expect in an ML context.
*  Honestly, we need to keep designing and redesigning and working with the community to build that out and make that better that's not our strength right now.
*  Give us six months or a year and I think it'll be way better but.
*  But the power of putting in the library means we can have teams of experts that aren't compiler engineers that can help us design and refine and drive us forward.
*  So one of the exciting things we should mention here is that this is this is new and fresh this cake is unbaked it's almost baked you can tell is delicious.
*  But it's not fully ready to be consumed.
*  Yep that's very fair it is very useful but it's very useful if you're super low level programmer right now and what we're doing is we're working our way up the stack and so the way I would look at mojo today in may and 2023.
*  Is it it's like a 0.1 so I think that you know a year from now it's gonna be way more interesting to a variety of people but what we're doing is we're we decided to release it early so that people can get access to and play with them we can build with the community we.
*  Have a big road map fully published being transparent about this and a lot of people are involved in this stuff and so what we're doing is we're really optimizing for building the same the right way.
*  And building the right way is kind of interesting working with the community because everybody wants it yesterday and so it's sometimes it's kind of you know there's some dynamics there but yeah I think it's the right thing so there's a discord also so the dynamics is pretty interesting.
*  Sometimes the community probably can be very chaotic.
*  And introduce a lot of stress we don't famously quit over the stress of the walrus operator I mean yeah you know broke.
*  Maybe that was exactly and so like it could be very stressful to develop but you can you just add tangent upon a tangent is it stressful to to.
*  To work through the design of various features here given that the community so richly involved also so i've been doing open development and community stuff for decades now somehow this has happened to me.
*  So i've i've learned some tricks but the the thing that always gets me is I want to make people happy right and so this is this is maybe not all people all happy all the time but generally I want I want people to be happy right and so the challenge is that.
*  Again we're tapping into some long some deep seated long tensions and pressures both in the the python world but also in the world in the hardware world and things like this and so people just want us to move faster right and so.
*  Again our decision was let's release this early let's get people used to it or access to and play with it and like let's let's build in the open which we could have.
*  You know I had the the language monk sitting in the cloister up on the hilltop like beavering away trying to build something but in my experience you get something that's way better if you work with the community.
*  I and so yes it can be frustrating can be challenging for lots of people involved and you know if you I mean if you mentioned our discord we have over 10,000 people on the discord 11,000 people or something keep in mind we released mojo like two weeks ago.
*  So it's very cool but what that means is that you know 10,000 people all will want something different right and so what we've done is we've tried to say okay cool here's our roadmap.
*  Here in the roadmap isn't completely arbitrary it's based on here's the logical order in which to build these features or add add these capabilities and things like that and what we've done is we spun really fast on like bug fixes and so we actually have very few bugs which is.
*  Cool I mean actually for a project in the state but then what we're doing is we're dropping in features very deliberately.
*  I mean this is fun to watch because you got the two gigantic communities of like hardware like systems engineers and then you have the machine learning python people that are like higher level and it's just too like like army like.
*  They've been at war.
*  Yeah they've been at war.
*  Right and so so here's a.
*  Token novel or something.
*  So here's the test again like it's super funny for for something that's only been out for two weeks right people are so impatient right but okay cool let's fast forward a year like in a year's time mojo will be actually quite amazing and solve tons of problems and be very good.
*  People still have these problems right and so you look at this you say and the way I look at this at least is to say okay well we're solving big long standing problems.
*  To me I again working on many different problems I want to make sure we do it right right there's like a responsibility you feel because if you mess it up.
*  There's very few opportunities to do projects like this and have them really have impact on the world if we do it right then maybe we can take those feuding armies and actually heal some of those wounds.
*  Yeah this is like this feels like this feels like a speech by George Washington or Abraham something.
*  And you look at this it's like okay well how different are we yeah we all want beautiful things we all want something that's nice we all want to be able to work together we all want our stuff to be used right and so if we can help heal that now i'm not optimistic that.
*  All people will use mojo and they'll stop using c++ like that's not my goal right but but if we can heal some of that I think that'd be pretty cool yeah and we start by putting the people who like braces into the gulag no.
*  So there are proposals for adding braces to mojo and we just all which is thing we tell them no okay.
*  Yeah anyway so there's a lot of amazing features on the road map and those ready implemented it'd be awesome I could just ask you a few things so so the the other performance improvement comes from immutability so what's the what's this bar and this let thing that we got going on.
*  What's the mutability yeah so one of the things that is useful and it's not always required but it's useful is knowing whether something can change out from underneath you right and so and python you have a pointer to an array.
*  Right and so you pass that pointer to an array around two things.
*  If you pass into a function they may take that and scrolled away in some other data structure and so you get your array back and you go to use it now somebody else is like putting stuff in your array.
*  How do you reason about that because to be very complicated at least lots of bugs right and so one of the things that you know again this is not something mojo forces on you but something that mojo enables is a thing called value semantics.
*  What value semantics do is they take collections like arrays like dictionaries.
*  Also tensors and strings and things like this that are much higher level and make them behave like proper values and so it makes it look like if you pass these things around you get a logical copy of all the data.
*  If I pass you an array to array you can go do what you want to it you're not gonna hurt my array now that is an interesting and very powerful design principle defines a way a ton of bugs you have to be careful to implement it in an efficient way.
*  Is there a performance hit that's significant.
*  Generally not if you implement the right way but it requires a lot of very low level getting the language right bits.
*  I assume there'd be a huge performance hit because it's a really nice the benefit is really nice because you don't get into absolutely well the trick is is you can't do you can't do copies.
*  So you have to provide the behavior of copying without doing the copy.
*  Yeah.
*  I do that is it how do you do that it's not magic it's just it's actually pretty cool well so first before we talk about how that works let's talk about how it works in python right so in python.
*  You define a person class or maybe a person class is a bad idea you define a database class right and database class has an array of records something like that right.
*  And so the problem is that if you pass in a record or a class instance into database it'll take a hold of that object and then it assumes it has it.
*  And if you're passing an object and you have to know that that database is going to take take it and therefore you shouldn't change it after you put in the database right this is this is kind of have to know that you just have to kind of know that right.
*  And so you roll out version one of the database you just kind of have to know that of course Lex uses his own database right yeah right because you built it you understand this works right.
*  Somebody else joins the team they don't know this yes right and so now they suddenly get bugs you're having to maintain the database you shake your fist.
*  You argue the 10th time this happens you're like okay we have to do something different right and so we do is you go change your python code.
*  And you change your database class to copy the record every time you add it and so what ends up happening is you say okay I will do what's called a defensive copy.
*  Inside the database and then that way if somebody passes something in I will have my own copy of it and they can go do whatever and they're not going to break my thing.
*  Okay this is usually the two design patterns if you look in pytorch for example this is cloning a tensor like there's a specific thing and you have to know where to call it if you don't call in the right place you get these bugs and this is state of the art right.
*  So a different approach so it's used in many languages so I work with it in swift.
*  Is you say okay well let's provide value semantics and so we want to provide the view that you get a logically independent copy but we want to do that lazily.
*  And so what what we do is you say okay if you pass something into a function it doesn't actually make a copy what actually does is it just increments the reference to it.
*  If you passed around you stick in your database it can go into the database you own it and then you come back out of the stack nobody's copied anything.
*  You come back out of the stack and then the caller let's go of it well then you've just handed it off to the database you've transferred it and there's no copies made.
*  Now on the other hand if you know your co-worker goes and hands you a record and you pass it in you stick in the database and then you go to town and you start modifying it what happens is you get a copy lazily on demand.
*  And so what this does is gives you copies only when you need them and it also so it defines where the bugs but also generally reduces the number of copies in practice and so but the implementation details are tricky here.
*  So this is yes something with reference counting but to make it performant across a number of different kinds of objects.
*  Yeah so you need a couple of things and so there's many so this concept has existed in many different worlds and so again it's not novel research at all right.
*  The magic is getting the design right so that you can do this in a reasonable way right and so there's a number of components that go into this one is when you're passing around so you were talking about python and reference counting and the expense of doing that.
*  When you're passing values around you don't want to do extra reference counting for no good reason and so you have to make sure that you're efficient and you transfer ownership instead of duplicating references and things like that which is a very low level problem.
*  You also have to adopt this and you have to build these data structures and so if you say you know mojo has to be compatible with python so of course the default list is a reference semantic list that works the way you'd expect in python but then you have to design a value semantic list.
*  And so you just have to implement that and then you implement the logic within and so the the role of the language here is to provide all the low level hooks that allow the option to do that.
*  The role of the language here is to provide all the low level hooks that allow the author of the type to be able to get and express this behavior without forcing into all cases or hard coding this into the language itself.
*  But there's a ownership so you're constantly tracking who owns the thing.
*  Yes and so there's a whole system called ownership and so this is related to work done in the rust community also the swift community has done a bunch of work and there's a bunch of different other languages that have all kind of c++ actually has copy constructors and destructors and things like that and so.
*  I mean c++ has everything so as move constructors and has like this whole world of things and so this is this is a body of work that's kind of been developing for many many years now and so mojo takes some of the best.
*  Ideas out of all these systems and remixes in a nice way so that you get the power of something like the rust programming language but you don't have to deal with it when you don't want to which is a major thing in terms of teaching and learning and being able to use and scale these systems.
*  How does that play with argument conventions what are they why they important how does the value semantics how does the transfer ownership work with with the arguments when they're passing.
*  Yeah so if you go deep into systems programming land this isn't again it's not something for everybody but if you go deep into systems programming land what you encounter is you encounter these types that get weird.
*  So if you're used to python you think about everything I can just copy it around I can go change it and mutate and do these things and it's all cool.
*  If you get into systems programming land you get into these things like I have an atomic number or I have a mutex or I have a uniquely owned database handle things like this right.
*  So these types you can't necessarily copy sometimes you can't necessarily even move them to different address.
*  And so what mojo allows you to do is it allows you to express hey I don't want to get a copy of this thing I want to actually just get a reference to it.
*  And by doing that what you can say is you can say okay if I'm defining something weird like a atomic number or something it's like it has to be so it's an atomic number is a.
*  An area in memory that multiple threads can access at a time without synchronous without without locks right and so.
*  And so like the definition of atomic numbers multiple different things have to be poking it that therefore they have to agree on where it is.
*  Can't just like move it out from underneath one because it kind of breaks what it means and so that's that's an example of a type that you can't even.
*  You can't copy you can't move it like once you create it has to be where it was right now if you look at many other examples like a database handle right so okay well what happens.
*  How do you copy database handled you copy the whole database that's not something you necessarily want to do.
*  The there's a lot of types like that where you want to be able to say that they are uniquely owned so there's always one of this thing.
*  And or if if I create a thing I don't copy it and so what mojo allows you to do is it allows you to say hey I want to pass around a reference to the same without copying it and so has.
*  Borrowed conventions, so you can say you can use it, but you don't get to change it you can pass it by mutable reference and so if you do that, then you can.
*  You get a reference to it, but you can change it and so it manages all that kind of stuff so it's just a really nice implementation of my C++ has.
*  You know the reference has a pointers yeah smart smart different different kinds of applications of smart pointers you can explicitly define this allows you but you're saying that's more like.
*  The weird case versus the common case was it depends on where I mean I mean I don't I don't think i'm a normal person so I mean I want to call other people weird.
*  But the but you know if you talk to a normal Python typical Python programmer you're typically not thinking about this right, this is a lower level of abstraction now if you talk to a C++ programmer.
*  Certainly, if you talk to a rust programmer again they're not weird they're delightful like these are all good people right those those folks will think about all the time.
*  Right and so I look at this as there's a spectrum between very deep low level systems i'm going to go poke the bits and care about how they're laid out in memory.
*  All the way up to application and scripting and other things like this and so it's not that anybody's right or wrong it's about how do we build one system that scales.
*  By the way, the idea of an atomic number has been something that always brought me deep happiness because.
*  The flip side of that the idea that.
*  threads can just modify stuff.
*  Asynchronously the whole idea of concurrent programming is a source of interest for me.
*  Well, so this is where you jump into.
*  You know, again you zoom out and get out of programming languages or compilers you just look what the industry has done.
*  My mind is constantly blown by this right and you look at what you know Moore's law Moore's law has this idea that like computers for a long time.
*  Single thread performance got faster and faster and faster and faster for free but then physics.
*  And other things intervened and power consumption like other things started to matter, and so what ended up happening is we went from single core computers to multi core.
*  Then we went to accelerators and this this trend towards specialization of hardware is only going to continue and so.
*  For years us programming language nerds and compiler people have been saying okay well, how do we tackle multi core right for a while it was like multi course the future, we have to get on top of this thing.
*  Then it was multi course the default what are we doing with this thing and then it's like there's chips with hundreds of course in them.
*  And so.
*  I'm super inspired by the fact that you know, in the face of this, you know those machine learning people invented this idea of a tensor.
*  Right and was the tensor tensor isn't.
*  Like an arithmetic and algebraic concept it's like an abstraction around a gigantic parallelizable data set right.
*  And because of that and because of things like tens of one pie torch we're able to say okay we'll express the math.
*  Of the system enables you to on Mac differentiations enables you to like all these cool things and and it's it's an abstract representation because you have that abstract representation you can now map it onto these parallel machines without having to.
*  Control okay put that right here put that right there put that right there and this has enabled an explosion in terms of AI compute accelerators like all the stuff and so that's super super excited.
*  What about the deployment the execution across multiple machines so.
*  You write that the modular compute platform dynamically partitions models with billions of parameters and distributes their execution across multiple machines enabling unparalleled efficiency.
*  Whether the use of unparalleled in that sentence anyway enabling unparalleled efficiency scale and the reliability for the largest workloads so how do you do this.
*  Abstraction of distributed deployment of large yeah so what one of the really interesting tension so there's a whole bunch of stuff that goes into that i'll pick a random walk through it.
*  If you if you go back and replay the history of machine learning right i mean the brief the brief most recent history machine learning because this is as you know very deep.
*  I knew Lex when he had an AI podcast.
*  Right yeah.
*  So so if you look at just TensorFlow and PyTorch which is pretty recent history in the big picture right but.
*  TensorFlow is all about graphs PyTorch I think pretty unarguably ended up winning and why did it win mostly because the usability.
*  Right and the usability of PyTorch is I think huge and I think again that's a huge testament to the power of taking abstract theoretical technical concepts and bring it to the masses right.
*  The challenge with what the TensorFlow versus the PyTorch design points was that TensorFlow is kind of difficult to use for researchers but was actually pretty good for deployment.
*  PyTorch is really good for researchers it kind of not super great for deployment right and so I think that we as an industry have been struggling and if you look at what deploying a machine learning model today means is that you'll have researchers who are I mean wicked smart of course but they're wicked smart at.
*  Model architecture and data and calculus like they're wicked smart in various domains they don't want to know anything about the hardware deployment or C++ or things like this right and so what's happened is you people who train the model they throw over throw it over the fence and they have people that try to deploy the model.
*  Well every time you have a team a does X they throw it over the fence and team Y does some team B does Y like you have a problem because of course it never works the first time and so you throw over the fence they figure out okay it's too slow won't fit doesn't use the right operator.
*  The tool crashes whatever the problem is then they have to throw it back over the fence and every time you throw it over the fence it doesn't work.
*  And so what we've seen today is that getting models in production can take weeks or months like it's not a typical right I talked to lots of people and you talk about like VP of software some internet company trying to pull a model and like why do I need a team of 45 people.
*  It's so easy to train a model why why can't I deploy it right and if you dig into this every layer is problematic so if you look at the language piece I mean this is tip of the iceberg it's a very exciting tip of the iceberg for folks but you've got python one side and C++ on the other side python doesn't really deploy.
*  I mean can theoretically technically in some cases but often a lot of production teams will want to get things out of python because they get their performance and control and whatever else so mojo can help with that.
*  If you look at serving so you talk about gigantic models well a gigantic model won't fit on one machine right and so now you have this model it's written python it has to be written in C++ now it also has to be carved up so that half of it runs on one machine half of it runs on one machine.
*  Or maybe it runs on 10 machines also now suddenly the complexity is exploding right and the reason for this is that if you if you look into TensorFlow PyTorch these systems they weren't really designed for this world right they were designed for you know back in the day when we were designing the
*  where it was a different much simpler world right and so now you have this model it's written python it has to be written in C++ now it also has to be carved up so that half of it runs on one machine half of it runs on another machine.
*  Or maybe it runs on 10 machines also now suddenly the complexity is exploding right and the reason for this is that if you if you look into TensorFlow PyTorch these systems they weren't really designed for this world right they were designed for you know back in the day when we were starting and doing things.
*  Where it was a different much simpler world like you want to run ResNet 50 or some ancient model architecture like this it was just a it was a completely different world than.
*  Train on one GPU exactly doing Alex net.
*  Yeah Alex net right in the major breakthrough and and the world has changed right and so now the challenge is that TensorFlow PyTorch these systems they weren't actually designed for LLM so like that was not that was not a thing.
*  And so what we're tens of actually has amazing power in terms of scale and deployment and things like that and i think google is.
*  I mean maybe not unmatched but they're like incredible in terms of their capabilities and gigantic scale.
*  Many researchers using PyTorch right and so PyTorch doesn't have the same capabilities and so modular can do is it can help with that now if you take a step back and say like what is.
*  Modular doing right so modular has like a a bitter enemy they were fighting against in the industry and it's one of these things where everybody knows it but nobody is usually willing to talk about it.
*  The bitter enemy the bitter thing that we have to destroy that we're all struggling with and it's like all right it's like fish can't see water is complexity.
*  Sure yes complexity right that was very philosophical of you.
*  And so if you look at it yes it is on the hardware side yes all these all these accelerators all these software stacks that go with the accelerator all these like there's massive complexity over there you look at.
*  What's happening on the modeling side massive amount of complexity like things are changing all the time people are inventing turns out the research is not done.
*  Right and so people want to be able to move fast transformers are amazing but there's a diversity even within transformers and what's the next transformer.
*  Right and you look into serving also huge amounts of complexity turns out that all the cloud providers right have all their.
*  Very weird but very cool hardware for networking all this kind of stuff and it's all very complicated people aren't using it you look at.
*  Classical serving right there there's this whole world of people who know how to write high performance servers with zero copy networking and like all all this fancy.
*  Asynchronous IO and like all these fancy things in the in the serving community very little that has pervaded into the machine learning world.
*  Right and why is that well it's because again these systems have been built up over many years they haven't been rethought there hasn't been a first principles approach to this and so what modular is doing is we're saying okay.
*  We've built many of these things like so i've worked on tens of flow and tpus and things like that other folks on our team like our work on pytorch core.
*  We've worked on onyx one time we've worked on many of these other systems and so built the systems like the apple accelerators and all that kind of stuff like our team is quite amazing and so one of the things that.
*  Roughly every modular is grumpy about is that when you're working on one of these projects you have a first order goal.
*  Get the hardware to work get the system to enable one more model get this product out the door enable the specific workload or make it.
*  Solve this problem for this this product team right and nobody's been given a chance to actually do that step back.
*  So we as an industry we didn't take two steps forward we took like 18 steps forward in terms of all this really cool technology across compilers and systems and runtimes and heterogeneous computer like all this kind of stuff and like all this technology has been.
*  You know i wouldn't say beautifully designed but it's been proven in different quadrants like you know you look at google with tpus massive huge exaflops of compute.
*  Strap together and into machines that researchers are programming in python in a notebook that's huge that's amazing that's incredible right it's incredible and so you look at the technology that goes into that and the the algorithms are actually quite general.
*  And so lots of other hardware out there and lots of other teams out there don't have the specification or that maybe the the years working on it or the the budget or whatever the google does right and so they should be getting access same algorithms but they just don't have that right and so what modular students are saying.
*  Cool this is not researching more like we've we've built auto tuning in many systems we've built programming languages right and so like have have you know implemented c++ have implemented swift have implemented many of these things.
*  And so you know this is hard but it's not research and you look at accelerators well we know there's a bunch of different weird kind of accelerators but they actually cluster together.
*  Right and you look at gpus well there's a couple of major vendors of gpus and they maybe don't always get along but their architectures are very similar.
*  You look at cpus cpus are still super important for the deployment side of things you see new new architectures coming out from all the cloud providers and things like this and they're all super important.
*  To the world right but they don't have the 30 years of development that the entrenched people do right and so what modular can do is we're saying okay all this complexity like it's not it's not bad complexity it's actually.
*  Innovation right and so it's innovation that's happening and it's for good reasons but I have sympathy for the poor software people.
*  Right I mean again I'm a generally software person to I love her but software people want to build applications and products and solutions that scale over many years.
*  They don't want to build a solution for one generation of hardware with one vendors tools right and because of this they need something that scales with them they need something works on cloud and mobile.
*  Right because you know their product manager said hey I want to be have lower latency and it's better for personalization or whatever they decide right products evolve and so.
*  The challenge with the machine learning technology in the infrastructure we have today in the industry is that it's all these point solutions.
*  And because they're all these point solutions it means that as your product evolves you have to like switch from technology stacks or switch to different vendor and what that does is that slows down progress.
*  So basically a lot of things we've developed in those little silos for machine learning tasks you want to make that the first class citizen of general purpose programming language that can then be compiled across all these kinds of hardware.
*  Well so it's not really about a programming language I mean the program language is a component of the mission right and the mission is are not literal but our joking mission is to save the world from terrible software.
*  Excellent.
*  So so you know if you look at this mission you need a syntax.
*  So that's the so yes you need programming language right and and like we wouldn't have to build the programming language of one existed.
*  I saw python was already good enough then cool we were just used it right we're not just doing very large scale expensive engineering projects for the sake of it like it's to solve a problem right it's also about.
*  Accelerators it's also about exotic numerics and be float sixteen and matrix multiplications and convolutions like this this kind of stuff within the stack there are things like kernel fusion.
*  It's a esoteric but really important thing that leads to much better performance and much more general research hack ability together.
*  And that that's enabled by the a six that's enabled by certain hardware was like where's the dance between.
*  Me several questions here like how do you add a piece of hardware to the stack.
*  Yeah if you need pieces like if I have this genius invention of a specialized accelerator yeah how do I add that to the module framework and also how does modular as a standard start to define the kinds of hardware that should be developed.
*  Yeah so let me take a step back and talk about status quo okay and so if you go back to tens of the one pie torch one this kind of time frame.
*  And these all evolving on way more complicated so let's go back to the the glorious simple days right these things basically were cpus and kuda.
*  And so what you do is you say go do a dense layer and a denser has a matrix multiplication right and so when you say that you say go do this big operation matrix multiplication.
*  And if it's on a gpu kick off kuda kernel it's on cpu go do.
*  Like an intel algorithm or something like that with the intel mk lk now that's really cool if you're either video or intel right but then more hardware comes in.
*  And and on one access you have more hardware coming in on the other hand you have an explosion of innovation and so what happened with both tense flow and pie torches that.
*  The explosion of innovation and ai has led to it's not just about matrix multiplication and convolution these things have now like 2000 different operators.
*  And on the other hand you have I don't know how many pieces of hardware out there are there it's a lot.
*  Okay it's it's not it's not even hundreds it's probably thousands okay and across all of edge and across like all all the different things that are used at scale.
*  Yeah exactly I mean it's not just like everywhere yeah it's not a handful of tpu alternatives it's it's it's every phone often with many different.
*  Right chips inside of it from different vendors right like it's ai is everywhere it's a thing right why are they all making their own chips like what why is everybody making their own thing.
*  Well so because that's a good thing for so so chris's philosophy on hardware yeah right so my philosophy is that there isn't one right solution.
*  Right and so I think that again we're at the end of Moore's law specialization happens yeah if you if you're building if you're training GPT five.
*  He wants some crazy supercomputer data center thingy if you're making a smart camera that runs on batteries you want something that looks very different.
*  For building a phone you want something looks very different if you have something like a laptop you want something that looks.
*  Maybe similar but a different scale right and so ai ends up touching all of our lives robotics right and like lots of different things and so as you look into this.
*  These have different power envelopes there's different trade offs in terms of the algorithms there's new innovations and sparsity and other data formats and things like that and so.
*  Hardware innovation I think is a really good thing right and what I'm interested in is unlocking the innovation there's also like analog and quantum and like although the.
*  The really weird stuff right and so if somebody can come up with a chip that uses analog computing and it's 100x more power efficient.
*  Think what that would mean in terms of the daily impact on the products we use that'd be huge now if you're building an analog computer you may not be a compiler specialist.
*  These are different skill sets right and so you can hire some compiler people if you're running a big company maybe but it turns out these are really.
*  Like exotic new generation of compilers like this is a different thing right and so if you if you take a step back out and come back to it was the status quo.
*  If you're in total your Nvidia you continue your keep up with the industry and you chase and okay there's 1900 now there's 2000 now there's 2100 and you have a huge team of people that are like trying to keep up and tune and optimize and.
*  Even when one of the big guys comes out with a new generation of their chip they have to go back and rewrite all these things.
*  Right so really it's only powered by having hundreds of people that are all like frantically trying to keep up and what that does is that keeps out the little guys.
*  And sometimes not so little guys the big guys that are also just not not in those dominant positions and so.
*  And so what has been happening and so a lot of you talk about the rise of new exotic crazy accelerators people been trying to turn this from a let's go write lots of special kernels problem into a compiler problem.
*  And so we and I contributed to this as well we as an industry went to it like let's go make this compiler problem.
*  Phase let's call it and much of the industry still in this phase by the way so it's not I wouldn't say this phase is over and so the idea is to say look okay.
*  What a compiler does is it provides a much more general extensible.
*  Hackable interface for dealing with the general case right and so.
*  Within machine learning algorithms for example people figured out that hey if I do a matrix multiplication I do a relu right the classic activation function.
*  It is way faster to do one pass over the data and then do the relu on the output when I'm writing out the data because really is just a maximum operation right Max zero and so.
*  It's amazing optimization take that more relu squished together one operation now I have Matt more relu well wait a second if I do that now I just went from having you know two operators to three.
*  But now I figure out okay well there's a lot of activation functions about.
*  Leaky rally what about like a million things that are out there right and so as I start using these in.
*  Now I get permutations of all these algorithms right and so with the compiler people says they said hey cool I will go and you may all the algorithms and I will enumerate all the pairs and I will actually generate a kernel for you.
*  And I think that this has been very very useful for the industry this is one of the things that powers Google TPUs.
*  I'm trying to use like rolling out really cool compiler stuff with Triton this other technology and things like this and so the compiler people are kind of coming into their for and saying like awesome this is a compiler problem will compiler it.
*  Here's the problem not everybody's a compiler person I love compiler people trust me right but not everybody can or should be a compiler person turns out that there are people.
*  That no analog computers really well they know some GPU internal architecture thing really well or they know some crazy sparse numeric interesting algorithm.
*  That is the cusp of research but they're not compiled people and so one of the challenges with this new wave of technology trying to turn everything into a compiler.
*  Is again is excluded a ton of people and so you look at what is mojo do what is the modular stack do is brings programmability back into this world like it enables.
*  I would say normal people but like a new you know different kind of delightful nerd that cares about numerics or cares about hardware cares about things like this to be able to express that in the stack and extend the stack without having to actually go hack the compiler itself.
*  So extend the stack on the on the algorithm side yeah and then on the hardware side yeah so again go back to like the simplest example of it right and so what both swift and mojo and other things like this did is we said okay pull magic out of the compiler and put it in the standard library.
*  And so much is still in with the engine that are providing and like this this very deep technology stack right which goes into heterogeneous runtimes and like a whole bunch of really cool really cool things.
*  This this whole stack allows that stack to be extended and hacked and changed by researchers and by hardware innovators and by people who know things that we don't know because you know much less than smart people we don't have all the smart people turns out.
*  What are heterogeneous runtimes yeah so.
*  So what is what is heterogeneous right so heterogeneous just means many different kinds of things together and so the simple simplest example you might come up with is a CPU and a GPU.
*  And so it's a simple heterogeneous computer to say I will run my data loading and pre processing and other algorithms on the CPU.
*  And then,
*  And so you've got now what are effectively two computers a CPU and a GPU talking to each other working together in a heterogeneous system.
*  But that was 10 years ago.
*  Okay look at a modern cell phone modern cell phone you've got CPUs and they're not just CPUs there's like big dot little CPUs and so there's multiple different kinds of CPUs are working together there are multi core you've got GPUs you've got neural network computers.
*  You've got dedicated hardware blocks for for media so for video decode and JPEG code and things like this and so you've got this massively complicated system and this isn't just cell phones every laptop these days is doing the same thing.
*  And all these blocks can be used to do the same thing and so you've got a lot of different kinds of things that you can do.
*  Dedicated hardware blocks for for media so for video decode and JPEG code and things like this and so you've got this massively complicated system and this isn't just cell phones every laptop these days is doing the same thing and all these blocks can run at the same time.
*  And need to be choreographed right and so again one of the cool things about machine learning is it's moving things to like data flow graphs and higher level abstractions and tensors and these things that it doesn't specify here's how to do the algorithm.
*  It gives the system a lot more flexibility in terms of how to translate or map or compile it onto the system you have and so what you need you know the bottom is part of the layer there is a way for all these devices talk to each other.
*  And so this is one thing that you know I'm very passionate about I mean you know I'm a nerd but.
*  All these all these machines all these systems are effectively parallel computers running at the same time sending messages to each other and so they're all fully asynchronous.
*  Well this is actually a small version of the same problem you have in a data center right in a data center you now have multiple different machines sometimes very specialized sometimes with.
*  GPUs or TPUs in one known sometimes with disks and other notes and so you get a much larger scale heterogeneous computer and so what ends up happening is you have this like multi layer abstraction.
*  Of hierarchical parallelism hierarchical asynchronous communication and making that again the enemy my enemy is complexity.
*  By getting that away from being different specialized systems every different part of the stack and having more consistency in uniformity I think we can help lift the world and make it much simpler actually get used.
*  But how do you leverage like the strengths of the different specialized systems so we're looking inside the smartphone yeah thank you there's just what I don't know 56 computers essentially is that a smartphone how do you.
*  Without trying to minimize the explicit.
*  Making it explicit which which computers must be a full operation yeah so there's there's a pretty well known algorithm and what you're doing is you're looking at two factors you're looking at the factor of.
*  Sending data from one thing to another right so it takes time to get it from that side of the chip to that side of the chip and.
*  And things like this and they're looking at what is the time it takes to do an operation on a particular block so take cpus cpus are.
*  Fully general they can do anything right but then you have a neural net accelerator that's really good at matrix multiplications.
*  And so you say OK well if my workload is all matrix multiplications I start up I send the data over the neural net thing it goes and does matrix multiplications when it's done it sends me back the result.
*  All is good right and so the simplest thing is just saying do matrix do matrix operations over there right.
*  But then you realize you get a little bit more complicated because you can do matrix multiplications on a GPU you can do it on.
*  And neural net accelerator you can do on CPU and they'll have different trade offs and costs and it's not just matrix multiplication and so what you actually look at is you look at.
*  I have generally a graph of compute I want to do a partitioning I want to look at the communication the bisection bandwidth and like the overhead and the sending of all these different things and and build a model for this and then decide OK it's an optimization problem where do I want to place this compute.
*  So the old school theoretical computer science problem of scheduling and then how does.
*  Presumably it's possible to somehow magically include auto tune into this.
*  Absolutely so I mean in my opinion this is an opinion this is not not everybody agree with this but in my opinion the world benefits from simple and predictable systems at the bottom you can control.
*  But then once you have a predictable execution layer you can build lots of different policies on top of it right and so one policy can be that.
*  The human programmer says do that here do that here do that here do that here and like fully manually controls everything.
*  And the systems just do it right then you quickly get in the mode of like I don't want to have to tell it to do it yeah and so the next logical step that people typically take is they write some terrible heuristic.
*  If it's a major location dude over there or if it's floating point dude on the GPU if it's integer do on CPU like something like that right and.
*  And then you then get into this mode of like people care more and more and more and you say OK well it's actually.
*  Like make the heuristic better let's get into auto tune let's actually do a search of the space to decide well what is actually better right well then you get into this problem where you realize this is not a small space this is a many dimensional.
*  hyperdimensional space that you cannot exhaustively search.
*  So do you know of any algorithms are good at searching very complicated spaces for.
*  Don't tell me you're going to turn this into a machine learning problem so then you turn into a machine learning problem and then you have a space of genetic algorithms and reinforcement learning and like all these all these.
*  Can you include that into the stack into the into the module stack yeah yeah and where's the sit where's the live is a separate thing or is it part of the compilation.
*  So you start from simple and predictable models and so you can have full control and you can have coarse grain knobs like nudge nudge system so you don't have to do this but if you really care about getting the best you know the last ounce out of a problem.
*  Then you can use additional tools and they're the cool thing is you don't want to do this every time you run a model you want to figure out the right answer and then cash it.
*  Once you do that you can get you can say okay cool I can get up and running very quickly I can get good execution out of my system.
*  I can decide if something's important and if it's important I can go through a bunch of machines at it and do a big expensive search over the space using whatever technique I feel like it's.
*  Really up to the problem and then when I get the right answer cool I can just start using it.
*  And so you can get out of this this trade off between okay am I going to like spend forever doing a thing or do I get up and running quickly and as a quality result like these these are actually not in contention with each other if the system's designed to scale.
*  You started and did a little bit of a whirlwind overview of how you get 35,000 X speed up or more over python.
*  Over python Jeremy Howard is a really great presentation about sort of the basic like look at the code here's how you get the speed up like you said that's something we could.
*  Probably developers can do for their own code to see how you can get this gigantic speed up but can you maybe speak to the machine learning task in general how do you how do you make some of this code fast and specific like what would you say is the main bottleneck.
*  For machine learning tasks are we talking about met mall matrix multiplication how do you make that fast so I mean if you just look at the python problem right you can say how do I make python faster.
*  There's been a lot of people have been working on the okay I don't make python to access or 10 access or something like that right and there've been a ton of projects in that vein right mojo started from the what can the hardware do.
*  Like what is the limit of physics yeah what is the speed of light how fast can this thing go and then how do I express that yeah right and so it wasn't well it wasn't anchored relatively on make python a little bit faster it's saying cool I know what the hardware can do let's unlock that right now.
*  Can you just say how how gutsy that is to be in the meeting and as opposed to try to see how do we get the improvement it's like what can the physics do.
*  I mean maybe I'm a special kind of nerd but you look at that what is the limit of physics how fast can these things go right when you start looking at that typically it ends up being a memory problem right and so today.
*  Particularly with these specialized accelerators the problem is that you can do a lot of math within them but you get bottleneck sending data back and forth the memory whether it be local memory or distant memory or disk or whatever it is.
*  And that bottleneck particularly is the training sizes get large as you start doing tons of inferences all over the place like that becomes a huge bottleneck for people right.
*  So again what happened is we went through a phase of many years where people took the special case and hand tuned it.
*  Tweaked it and checked out and they knew exactly how the hardware worked and they knew the model and they made it they made it fast.
*  Didn't generalize and so you can make you know resident 50 or some or Alex net or something inception be one like you can you can do that right because the models are small.
*  They fit in your head right but as the models get bigger more complicated as the machines get more complicated it stops working right and so this is where things like current fusion come in.
*  So what is current fusion this is this idea of saying let's avoid going to memory and let's do that by building a new hybrid.
*  Colonel and numerical algorithm that actually keeps things in the accelerator instead of having right all the way out to memory.
*  What's happened with with these accelerators now is you get multiple levels of memory like in a GPU for example you'll have global memory and local memory and like all these things.
*  If you zoom way into how hardware works the register file is actually a memory so the registers are like an L0 cash and so a lot of taking advantage of the hardware ends up being.
*  Full utilizing the full power in all this capability and this has a number of problems right one of which is again the complexity disaster right there's too much hardware.
*  Even if you just say let's look at the chips from one line of vendor like apple or intel or whatever it is.
*  Each version of the chip comes out with new features and they change things so that it takes more time or less time to do different things and you can't rewrite all the software whenever new chip comes.
*  Right this is where you need a much more scalable approach and this is what mojo and what the modular stack provides is it provides.
*  This infrastructure in the system for factoring all this complexity and then allowing people to express algorithms you talk about auto tuning for example.
*  Express algorithms in a more portable way so that when a new chip comes out you don't have to rewrite it all.
*  So to me like you know I kind of joke like what is a compiler well there's many ways to explain that you convert thing and thing be and you convert source code to machine code like you can talk about many many things that compilers do.
*  But to me it's about a bag of tricks it's about a system and a framework you can hang.
*  Complexity it's a system that can then generalize and it can work on problems that are bigger than fit in one human said.
*  Right and so what that means what a good stack and what the modular stack provides is the ability to walk up to it with a new problem and will generally work quite well.
*  And that's something that a lot of machine learning infrastructure and tools and technologies don't have.
*  Typical state of the art today as you walk up to click your deploying if you walk up with a new model you try to push it through the converter and the converter crashes.
*  That's crazy the state of ML tooling today is not anything that a C programmer ever accept right and it's always been this kind of flaky set of tooling that's never been integrated well and it's been.
*  Never worked together and because it's not designed together it's built by different teams is built by different hardware vendors is built by different systems is built by different Internet companies are trying to solve their their problems right and so that means that we get this fragmented terrible mess of complexity.
*  So any specifics of any Jeremy showed this there's the vector eyes function which I guess is.
*  Built in to the into mojo vector eyes as he showed is built into the library into the library library vector eyes paralyze.
*  Which vector eyes is more low level paralyzes high level there's the tiling thing which is how he demonstrated the.
*  Autotune I think so so think of think about this in like levels hierarchical levels of abstraction right and so it.
*  At the very if you zoom all the way into a computer problem you have one floating point number right and so then you say okay I want to be I can do things one at a time in an interpreter.
*  So I can get to doing one one at a time in a compiler I can see that I can get to doing for eight or 16 at a time with factors that's called vectorization.
*  Then you can say hey I have a whole bunch of different you know what what a multi core computer is this basically a bunch of computers.
*  Right so they're all independent computers that can talk to each other and they share memory and so now what parallelize does it says okay run multiple instances on different computers.
*  And now they can all work together on a problem right and so what you're doing is you're saying keep going out to the next level out.
*  And as you do that how do I take advantage of this so tiling is a memory optimization right and says okay let's make sure that we're keeping the data close to the compute part of the problem.
*  Instead of sending it all back and forth through memory every every time I load a block and size of the block sizes as all that's how you get to the auto tune to make sure it's optimized.
*  Yeah well so all of these the details matter so much to get good performance this is another funny thing about machine learning and high performance computing that is very different than.
*  C compilers we all grew up grew up with where you know if you get a new version of GCC or a new version of clang or something like that you know maybe something will go 1% faster.
*  Right and so compiler ensures work really really really hard to get half a percent out of your C code something like that.
*  But when you're talking about an accelerator or an application or you're talking about these kinds of algorithms.
*  If you get it wrong it's not 5% or 1% it could be 2x or 10x right if you think about it you really want to make use of the full memory you have the cash for example.
*  But if you use too much space it doesn't fit in the cash now you're going to be thrashing all the way back out to main memory.
*  And these can be 2x 10x major performance differences and so this is where getting these magic numbers and the sounds right is really actually quite important.
*  So you mentioned that mojo is a superset of python.
*  Can you run python code.
*  As if it's mojo code.
*  Python.
*  Can you run python code.
*  As if it's mojo code.
*  Yes yes so and so and this has two sides of it so mojo is not done yet so I'll give you a disclaimer mojo is not done yet but already we see people that take small pieces of python code move it over they don't change it and you can get 12x speed ups.
*  Like somebody's just tweeting about that yesterday which is pretty cool right and again interpreters compilers right and so without changing a code without.
*  Also this is not with this is not jit compiling or do anything fancy this is just basic stuff move it straight over.
*  Now mojo will continue to grow out and as it grows out it will have more and more and more features and our north star is to be a full superset of python and so you can bring over.
*  Basically arbitrary python code and have it just work and it may not always be 12x faster but but it should be at least as fast and way faster in many cases is the goal right.
*  Now take time to do that and python is a complicated language there's not just the obvious things but there's also.
*  Non obvious things that are complicated like we have to be able to talk to see python packages to talk to the CPI and there's a bunch of there's a bunch of pieces.
*  So you have to just to make explicit the obvious may not be so obvious until you think about it so you know to run python code that means you have to run all the python packages and libraries yeah yeah so that means what.
*  What's the relationship between mojo and see python the the interpreter that's presumably would be task was getting those packages to work so in the fullness of time mojo will solve for all the problems and you'll be able to move python packages over and run them in mojo.
*  Without the CPI without CPI some day yeah right it's not today but someday and that'll be a beautiful day because then you'll get a whole bunch of advantages and you'll get massive speed ups and things like this.
*  You can do that one at a time right you can move packages one exactly but but we're not willing to wait for that python is too important the ecosystem is too broad.
*  We want to be able to build mojo out we also want to do it the right way without time like in without intense time pressure we're obviously moving fast but and so what we do is we say okay well let's make it so you can import an arbitrary existing package.
*  Arbitrary including like you write your own on your local disk whatever it's not it's not like a standard like an arbitrary package and import that using CPI.
*  CPI on our runs all packages right and so what we do is we built an integration layer where we can actually use CPI on again I'm practical and to actually just load and use all the existing packages as they are.
*  The downside of that is you don't get the benefits of mojo for those packages right and so the run as fast as they do in the traditional CPI on way.
*  But what that does is that gives you an incremental migration path and so if you say hey cool well here's a you know the python ecosystem is vast I want all of it to just work.
*  But there's certain things are really important and so if I if I'm doing weather forecasting or something well.
*  I want to load all the data on your work with it and I have my own crazy algorithm inside of it well normally I'd write them C++.
*  I can write mojo and have one system that scales well that's way easier to work with.
*  Is it hard to do that to have that layer that's running CPI on because is there some communication back and forth.
*  Yes it's complicated I mean this is this is what we do so I mean we make it look easy but it is it is complicated but what we do is we use.
*  The CPI on existing interpreter so it's running its own byte codes and that's how it provides full compatibility and then it gives us CPI on objects.
*  And we use those objects as it is and so that way we're fully compatible with all the CPI on objects and all the.
*  The you know it's not just the python part is also the C packages the C libraries underneath them because they're often hybrid.
*  And so we can fully run and we're fully compatible with all that and the way we do that is that we have to play by the rules right and so we keep objects in that representation when they're coming from that world.
*  What's the representation that's being used in memory would have to know a lot about how the CPI on interpreter works.
*  It has for example reference counting but also different rules on how to pass pointers around and things like this super low level fiddly and it's not like python it's like.
*  How the interpreter works and so that gets all exposed out and then you have to define wrappers around the low level C code.
*  Right and so what this means is you have to know not only C.
*  Which is a different role from python obviously not only python but the rappers but the interpreter and the rappers and the implementation details and the conventions and it's just this really complicated mess.
*  And when you do that now suddenly you have a debugger that bugs python they can't step into C code.
*  So you have this two world problem right and so by pulling this all into mojo what you get is you get one world you get the ability to say cool I have untyped very dynamic beautiful simple code.
*  Okay I care about performance for whatever reason right there's lots of reasons you could you might care and so then you add types you can parallelize things you can factorize things you can use these techniques which are.
*  General techniques to solve problem and then you can do that by staying in the system and if you're you have that that one python package is really important to you can move to mojo you get massive performance benefits on that and that and other other advantages you know if you like sec types it's nice they're enforced.
*  Some people like that right rather than being hints so there's other advantages to and then.
*  And then you can do that incrementally as you go.
*  So one different perspective on this will be.
*  Why mojo instead of making see python faster redesigning see python yeah well I mean you can argue mojo is redesigning see python but but but why not make see python faster and better and other things like that there's lots of people working on it.
*  So actually there's a team at Microsoft that is really improving I think see python 3.11 came out in October something like that and it was you know 15% faster 20% faster across the board which is pretty huge given how mature python is and things like this and so that's awesome I love it.
*  Doesn't run on GPU it doesn't do AI stuff like doesn't do vectors doesn't do things I'm 20% good 35,000 times better right so like they're they're they're they're definitely I'm a huge fan of that work by the way and it composes well with what we're doing and so it's not.
*  It's not like we're fighting or anything like that it's actually just general it's goodness for the world but it's just a different path right and again we're not working forwards from making python a little bit better we're working backwards from what is the limit of physics.
*  What's the process of porting python code to mojo is there.
*  What's involved in that process is there tooling for that and not yet so we're missing some basic features right now and so we're continuing to drop out new features like on a weekly basis but you know at the fullness of time give us a year and a half maybe two years is it an automatable process so when we're ready it will be very automatable.
*  Yes is it automatable automate like is it possible to automate.
*  In the general case the python to mojo conversion yeah well you're saying it's possible well so and this is why I mean among other reasons why we use tabs yes right so first of all by being a superset yeah you can it's like C versus C++ can you move C code to C++.
*  Yes yeah right and you move you can move C code to C++ and then you can adopt classes you can add up templates you can adopt other references or whatever C++ features you want after you move C code to C++ like you can't use templates in C.
*  Right and so if you leave it a C fine you can't use the cool features but it still works right and C and C++ code work together and so that's the analogy right now.
*  Here right you you you there's not a python is bad and the mojo is good right mojo just gives you superpowers right and so if you want to stay with python that's cool but the tooling should be actually very beautiful and simple because we're doing the hard work of defining a superset.
*  Right so you're right so there's several things to say there but also the conversion tooling should probably give you hints as to like how you can improve the code and then you exactly once you're in the new world then you can build all kinds of cool tools to say like hey should you adopt this feature or like.
*  And we haven't built those tools yet but I fully expect those tools will exist and then you can like you know quote quote modernize your code or however you want to look at it right so I mean one of the things that I think is really interesting about mojo is that.
*  There have been a lot of projects to improve python over the years everything from you know getting python around the Java virtual machine.
*  Hi which is a jit compiler there's tons of these projects out there that have been working on improving python in various ways they found a one or two camps.
*  So hi is a great example of a camp that is trying to be compatible with python.
*  Even there not really doesn't work with all the C packages and stuff like that but but they're trying to be compatible with python there's also another category of these things where they're saying well python is too complicated.
*  And you know I'm gonna cheat on the edges and it's you know like integers in python can be an arbitrary size integer.
*  If you care about fitting in a going fast in a register in a computer that's really annoying right and so you can you can choose to pass on that right you can say well people don't really use big integers that often therefore I'm gonna just not do it and it will be fine.
*  Not not a python superset or you can do the hard thing and say okay this is python you can't be a superset of python without.
*  Being a superset of python and that's a really hard technical problem but it's in my opinion worth it right and it's worth it because.
*  It's not about anyone packages about this ecosystem it's about what python means for the world and it also means we don't want to repeat the python to python three transition like we want we want people to be able to adopt this stuff quickly and so by doing that work we can help lift people.
*  Yeah the challenge it's really interesting technical philosophical challenge of.
*  Really making a language a superset of another language.
*  that's breaking my brain a little bit well it paints you into corners so again i'm very happy with python I saw joking all joking aside I think that the annotation thing is not.
*  The actual important part of the problem yes right but the fact that python has amazing dynamic metaprogramming features and they translate to beautiful static programming features I think is profound.
*  I think that's huge right and so python I've talked with guido about this it's like it was not designed to do what we're doing and that was not the reason they built it this way but because they really cared and they're very thoughtful about how they designed the language.
*  It scales very elegantly in the space but if you look at other languages for example c and c++.
*  Right if you're building a superset you get stuck with the design decisions of the subset.
*  Right and so you know c++ is way more complicated because of c in the legacy then it would have been if they would have theoretically designed a from scratch thing.
*  And there's lots of people right now they're trying to make c++ better and recent tax c++ is going to be great we'll just change all the syntax but if you do that now suddenly you have zero packages.
*  You don't have compatibility so what what are the if you could just linger on that what are the biggest challenges of keeping a superset status what are the things you're struggling with is it all boiled down to having a big integer.
*  No I mean it's it's it's one of the other things usually it's the it's a long tail of weird things so let me give you a war story so war story in the space is you go way back in time project I worked on is called clang.
*  Clang what it is is the cc++ parser right and when I started working on clang.
*  That's been like 2006 or something was when I was in 2007 2006 when I first started working on it right it's funny how time flies.
*  Yeah the I started that project and I'm like okay well I want to build a c parser c++ parser for lvm it's going to be the word gcc is yucky you know this is me and earlier times it's yucky it's unprincipled it has all these weird features like all these bugs like.
*  It's yucky so I'm going to build a standard compliance c and c++ parser it's going to be beautiful it'll be amazing well engineered all the cool things that engineer wants to do.
*  And so I start implementing building it out building on building out and then I got to include standard io dot h.
*  And all of the headers in the world use all the gcc stuff.
*  Okay this is in so again come back away from theory back to reality right I had I was at a fork on the road I could have built an amazingly beautiful academic thing that nobody would ever use.
*  Or I could say well it's yucky in various ways all these design mistakes accents of history the legacy at that point gcc was like over 20 years old.
*  Which by the way now lvm is over 20 years old funny how time catches up to you right and so you say okay well.
*  What what is easier right I mean as an engineer it's it's actually much easier for me to go implement.
*  Long tail compatibility weird features even if they're distasteful and just do the hard work and like figure it out reverse engineer understand what it is right a bunch of test cases like try to understand behavior.
*  It's way easier to do all that work as an engineer than it is to go talk to all C programmers and get argue with them and try to get them to rewrite their code.
*  Right and that breaks a lot more things yeah and you have realities like nobody actually understands how the code works because it was written by the person who quit 10 years ago.
*  Right and so this is this software is kind of frustrating that way but it's that's how the world works.
*  Yeah unfortunately can never be this perfect beautiful thing.
*  Well there there are occasions in which you get a bill like you know you invent a new.
*  Data structure or something like that or there's this beautiful algorithm that's like makes you super happy night I love that moment but but when you're working with people.
*  You're working with code and dusty decode bases and things like this right.
*  It's not about what's theoretically beautiful it's about what's practical what's real what people actually use and.
*  I don't meet a lot of people that say I want to rewrite all my code.
*  Just for the sake of it.
*  By the way that could be interesting possibilities and we'll probably talk about it where AI can help rewrite some code that might be.
*  Farther out future but it's a really interesting one how that could create more.
*  Be a tool in the battle against this monster of complexity that you mentioned.
*  Yeah.
*  You mentioned we know the the benevolent dictator for life of python what does he think about module.
*  They talked so much about it I have talked with him about it he found it very interesting we actually talked with we know before it launched and so he was aware of it before it went public.
*  I have a ton of respect for greater for a bunch of different reasons you talk about walrus operator and.
*  Like we know it's pretty amazing in terms of steering such a huge and diverse community and.
*  And like driving forward and I think python is what it is thanks to him right and so to me it was really important starting to work on mojo to get his feedback and get his input and get his eyes on this right.
*  A lot of what we do was is wasn't is I think inserted about is have we not fragment the community we don't want to python to python three thing like that was that was really painful for everybody involved.
*  And so we spent quite a bit of time talking about that and some of the tricks I learned from swift for example zone and the migration from swift we managed to like not just convert.
*  Objective C into a slightly pretty objective C which we did we then converted not entirely but almost an entire community to completely different language.
*  Right and so there's a bunch of tricks you learn along the way they're directly relevant to what we do and so this is where for example the leverage see python.
*  Will bring up the new thing like that that approach is I think proven and then comes from experience and so guido was very interested in like okay cool like.
*  I think the python is really his legacy it's his baby I have tons of respect for that incidentally I see mojo as a member of the python family not trying to take python away from guido and from the python community.
*  And so to me it's really important that we're a good member of that community and so yeah I think that again you would have to ask we do this but I think that he was very interested in this notion of like cool python gets beaten up for being slow.
*  Maybe there's a path out of that.
*  Right and that you know if the future is python right I mean look look at the the far outside.
*  Case on this right and i'm not saying this is guido's perspective but you know there's this path of saying like okay well suddenly python can suddenly go all the places it's never been able to go before.
*  Right and that means the python can go even further and can have even more impact on the world.
*  So in some sense mojo could be seen as python 4.0.
*  I would not say that I think that would drive a lot of people really crazy because of the PTSD of the 3.0 to what i'm willing to annoy people about emacs versus them versus spaces that one I don't know that might be a little bit far even for me.
*  The point is the step to being a superset and allowing all these capabilities I think is the evolution of a language it feels like an evolution of a language.
*  So he he's interested by the ideas that you're playing with but also concerned about the fragmentation so how what are the ideas you've learned what are you thinking about how we avoid fragmenting the community where the.
*  I don't know what to call the mojo people.
*  Magicians.
*  Magicians I like it can coexist happily and share code and basically just have these big code bases that are using c python and more and more moving towards mojo.
*  Well so again these are lessons I learned from swift and and I think that's a great way to do it.
*  And swift you have objective c super dynamic.
*  They're very different syntax right but you're talking to people who have large scale code bases I mean apples got the biggest largest scale code base of objective c code right and so you know none of the companies that are using code bases are using code bases.
*  Scale code base of objective c code right and so you know none of the companies none of the ios developers none of the other developers want to rewrite everything all at once and see one be able to adopt things piece at a time.
*  And so a thing that I found that worked very well in the swift community was saying okay cool and this is when such as very young as you say okay you have a million line of code objective c app.
*  Don't rewrite it all but when you implement a new feature to implement that new class.
*  Using swift right and so now this turns out is a very wonderful thing for an app developer.
*  What is a huge challenge for this compiler team and the systems people that are implementing this right and this comes back to what is this trade off between doing the hard thing that.
*  The naval scale versus doing the theoretically pure and ideal thing right and so swift had adopted and built a lot of different machinery to deeply integrate with the objective runtime and we're doing the same thing with python right now what happened in the case of swift is that.
*  What is language got more and more and more mature over time right and instantly mojo is a much simpler language since left in many ways and so I think that mojo will develop way faster than swift for a variety of reasons.
*  But as a language gets more mature and parallel with that you have new people starting new projects.
*  Right and so when the language is mature and somebody starting a new project that's when they say okay cool i'm not dealing with.
*  A million lines of code i'll just start and use the new thing for my whole stack now the problem is again you come back to work communities and we're.
*  People that work together you build new subsystem or new feature a new thing in swift or you build a new thing in mojo.
*  Then you want to be in and up being used on the other side.
*  Right and so then you need to work on integration back the other way and so it's not just mojo talking python it's also python talking to mojo.
*  Right and so what I would love to see the I don't want to see this next month right but when I want to see over the course of time is.
*  I would love to see people that are building these packages like you know numpy or you know tensorflow or what you know these packages that are half python half c++.
*  And if you say okay cool I want to get out of this python c++ world into a unified world and so I can move to mojo but I can't give up on my python clients.
*  They're like these libraries get used by everybody and they're not all going to switch every all you know all once and maybe never right well so the way we should do that is we should bend python interfaces to the mojo types.
*  And that's what we did in swift and work great I mean it was a huge implementation challenge for the compiler people right but.
*  There's only a dozen of those compiler people and there are millions of users and so it's a very expensive capital intensive like.
*  Skill set intensive problem but once you solve that problem it really helps adoption and really helps the community progressively adopt technologies and so I think that this approach will work quite well with with the python in the mojo world.
*  So for a package ported to mojo and then create a python interface.
*  Yep.
*  So how do just to linger on these packages numpy pytorch tensorflow yeah how do they play nicely together so is mojo supposed to be let's talk about the machine learning ones.
*  Is mojo kind of vision to replace pytorch tensorflow to incorporate it what's what's the relationship in this.
*  So take a step back so I wear many hats so you're you're you're angling in on the mojo side.
*  Mojo is a programming language and so it can help solve the C C++ python feud that's happening the fire mojo got me i'm sorry we should be talking about modular yes yes okay so the fire mojo is amazing I love it.
*  The other side of this is the fire mojo is in service of solving some big AI problems right and so the big AI problems are again this fragmentation this hardware nightmare this this explosion of new potential but that's not getting.
*  Felt by the industry right and so when you look at how does the modular engine help tensorflow and pytorch right it's not replacing them right in fact when I talk to people again they're not replacing them.
*  Right in fact when I talk to the people again they don't like to rewrite all their code you have people that are using a bunch of pytorch a bunch of tensorflow.
*  That models that they've been building over the course of many years right and when I talk to them there's a few exceptions but generally they don't want to rewrite all their code.
*  Right and so what we're doing is we're saying okay well you don't have to rewrite all your code what happens is the modular engine goes in there and goes underneath tens of them pytorch.
*  It's fully compatible and just provides better performance better predictability better tooling it's a better experience that helps lift tons of flow and pytorch and make them even better.
*  I love python I love tensorflow I love pytorch right this is about making the world better because we need a to go further.
*  But if I have a process that trains a model and have a process that performs inference on that model and have the model itself what should I do with that in the long arc of history.
*  In terms of if I use pytorch to train it should I rewrite stuff in mojo with that if I care about performance.
*  Also, I mean again it depends so if you care about performance then writing in and mojo is going to be way better than writing in python but if you look at.
*  If you look at lm companies, for example, you look at open AI rumored and you look at many of the other folks that are working on many of these.
*  Many of these many of these lms and other like innovative machine learning models on the one hand they're innovating and the data collection and the model billions of parameters in the model architecture and the.
*  RLHF and the like all the all the cool things that people are talking about but on the other hand they're spending a lot of time writing kuda curls.
*  Right and so you say wait a second how much faster could all this progress go if they were not having to handwrite all these kuda curls.
*  Right and so there are a few technologies that are out there and people have been working on this problem for a while and and they're trying to solve subsets of the problem again can fragment in space and so what mojo provides for these kinds of companies is the ability to say cool I can have a unifying theory.
*  Right again this the the better together the unifying theory the the two world problem or the three world problem or the end world problem like this is the thing that is slowing people down and so as we help solve this problem I think it'll be very helpful for making this whole cycle go faster.
*  So obviously we talked about the transition from objective C to swift if design this programming language and you've also talked quite a bit about the use of swift for machine learning context.
*  Why have you decided to move away from.
*  Maybe an intense focus on swift for the machine learning context versus of deciding a new programming language that happens to be a superset.
*  The desert and did you meditate on it okay all right no it was bold it was bold and needed and I think I mean it's just bold and sometimes to take those leaps is a difficult leap to take.
*  Yeah well so okay I mean I think there's a couple of different things so actually I left Apple back in 2017 like January 2017 so it's been a number of years that I left Apple and the reason I left Apple was to do AI.
*  Okay so and again I won't come on Apple and AI but the at the time right I want to get into and understand and understand the technology understand the applications workloads and so I'm going to go dive deep into applied and AI and then the technology underneath it right.
*  I found myself a Google.
*  And that was like when TPUs were waking up.
*  Exactly and so I found myself at Google and Jeff Dean who's a rockstar as you know right and the and 2017 TensorFlow is like really taking off and doing incredible things and I was attracted to Google to help them with the TPUs right and TPUs are an innovative hardware accelerator platform.
*  Have now I mean I think proven massive scale and like done incredible things right and so one of the things that this led into is a bunch of different projects which I'll skip over right one of which was this so for TensorFlow project.
*  Right and so that project was a research project and so the idea of that is say okay well let's look at innovative new programming models where we can get a fast programming language we can get automatic differentiation into language let's push the boundaries of these things in a research setting.
*  Now that project I think lasted two three years there's some really cool outcomes of that so one of the one of the things that's really interesting is.
*  I published a talk at an LVM conference in 2018 and this seems like so long ago about graph program abstraction which is basically the thing that's in pytorch 2.
*  And so pytorch 2 with all this dynamic real thing it's all about this graph program abstraction thing from python byte codes and so a lot of the research that was done.
*  Ended up pursuing and going out through the industry and influencing things and I think it's super exciting and awesome to see that.
*  But the support has to project itself did not work out super well and so there's a couple of different problems with that one of which is that you may have noticed so if it's not python.
*  There's a few people that write python code yes and so it turns out that all of them all is pretty happy with python it's actually a problem.
*  Other programming languages have as well that they're not python will probably maybe briefly talk about Julia was a very interesting beautiful programming language but it's not python exactly well and so if you're saying.
*  I'm gonna solve a machine learning problem where all the programmers are python programmers and you say the first thing you have to do is switch to a different language.
*  Well your new thing maybe good or bad or whatever but if it's a new thing the adoption barrier is massive.
*  It's still possible still possible yeah absolutely the world changes and evolves and there's definitely room for new new and good ideas but it just makes it so much harder right and so.
*  Lesson learned so if it's not python and people are not always in search of like learning anything for the sake of learning anything and if you want to be compatible with all the world's code turns out.
*  Meet the world where it is right second thing is that you know a lesson learned is that swift as a very fast and efficient language kind of like mojo but different different take on it still.
*  Really worked well with eager mode and so eager mode is something that pie torch does and it proved out really well and it enables really expressive and dynamic and easy to debug programming.
*  TensorFlow at the time was not set up for that.
*  Let's say that was not the timing is also important in this world yeah yeah intensive flows a good thing and it has many many strengths but.
*  You can say so potential is a good idea except for the swift and except for the tens of the part.
*  So because it's not python intensive flow because it's not it wasn't set up for you at the time yeah there's one point exactly and so one of the so one of the things about that is in the context of it being a research project i'm very happy with the fact that.
*  I think the ideas went on to have influence of other systems like pie torch few people use that I hear right and so I think that's super cool and for me personally I learned so much from it.
*  Right and I think a lot of the engineers that worked on it also learned a tremendous amount and so you know I think that.
*  That's just really exciting to see and and you know i'm sorry that the project didn't work out I wish it did of course right but.
*  But you know it's it's it's a research project and so you're there to learn from it.
*  What's interesting to think about.
*  The evolution of programming as we come up with these whole new set of algorithms and machine learning and artificial intelligence and what's going to win out because it could be a new programming language yeah it could be a new programming language.
*  I mean we just mentioned Julia I think there's a lot of ideas behind Julia that.
*  Mojo shares what are your thoughts about Julia in general.
*  So I would I will have to say that when we launched mojo the.
*  One of the biggest things I didn't predict was the response from the Julia community and so I was not I mean I've let me take a step back.
*  They were there an adopter of LVM a long time ago they've been pushing state of the art in a bunch of different ways Julia is a really cool system.
*  I had always thought of Julia's being mostly a scientific computing focused environment right and and I thought that was its focus I neglected.
*  To understand that one of their missions is to like help make python work end to end and so I think that was my my error for not understanding that and so I could have been maybe more sensitive to that but.
*  But there's major differences between what mojo is doing and what Julie is doing so as you say Julia is not python right and so one of the things that a lot of the Julia people are doing is they're trying to make it work.
*  Right and so one of the things that a lot of the Julia people came out and said is like okay well if we put a ton of more energy and talk 10 more money or engineering or whatever into Julia.
*  Maybe that would be better than starting mojo right well I mean maybe that's true but it still wouldn't make Julia into python.
*  So if you've worked backwards from the goal of let's build something for python programmers without requiring them to relearn syntax.
*  Then Julia just isn't there right I mean that's a different thing right and so if you anchor on I love Julia and I want Julie to go further then you can you can look at it from a different lens but the lens we're coming at it was.
*  Hey everybody is using python python isn't syntax isn't broken let's take what's great about python make it even better and so it's just a different starting point so I think Julie's great language the communities of lovely community they're doing really cool stuff but it's just a different slightly different angle.
*  But it does seem that python is quite sticky is there some.
*  The soft comas thing you could say about why python by many measures seems to be the most popular programming language in the world.
*  I can tell you things I love about it maybe that's one way to answer the question right so huge package ecosystem super lightweight and easy to integrate it has very low startup time.
*  So what startup time you mean like my curve or what yeah so if you if you look at certain other languages that you say like go and it just takes a like Java for example takes a long time to compile all the things and and then the the VM starts up in the garbage collectors kicks in and then it revs its engines and then it can plow through a lot of internet stuff or whatever right.
*  Python is like scripting it's it just goes right python has very low compile time.
*  That's not sitting there waiting python integrates in a notebooks in a very elegant way that makes exploration super interactive and it's awesome right python is also it's like.
*  Almost the glue of computing because it has such a simple object representation a lot of things plug into it that dynamic metaprogramming thing we're talking about also enables really expressive and beautiful api's.
*  So there's lots of reasons you can look at technical things that python is done and say like okay well this is actually a pretty amazing thing and anyone of those you can neglect people all just talk about indentation and ignore like the fundamental things but then you also look at the community side right so python owns machine learning.
*  She learns pretty big yeah and it's growing it's growing right and it's growing in importance right and so and there's a reputation of prestige to machine learning to where like if you're a new program or you're thinking about like.
*  Which programming language do I use well I should probably care about machine learning therefore let me try python and kind of builds and builds and builds and even go go back before that like my kids learn python.
*  Right now because i'm telling learn python but because they were that against you or what.
*  Well they also learn scratch right and things like this too but it's because python is taught everywhere because it's easy to learn right and because it's pervasive right and there's my day we learn java and c++.
*  Yeah uphill both directions but yes i guess python is the main language of teaching software engineering schools now yeah well if you look at if you look at this there's these growth cycles right if you look at what causes things to become popular.
*  And then gain in popularity there's reinforcing feedback loops and things like this and i think python is done.
*  Again the whole community is a really good job of building those growth loops and help propel the ecosystem and i think that again you look at what you can get done with just a few lines of code it's amazing.
*  So this kind of self building loop is interesting to understand because when you look at mojo what it stands for some of the features.
*  It seems sort of clear that this is a good direction for programming languages to evolve in the machine learning community but still not obvious that will because of this whatever the engine of popularity of virality is there something you could speak to like how how do you get people to switch.
*  Yeah well i mean i think that the the the the viral growth loop is to switch people to unicode.
*  Yes i think the unicode file extensions are what i'm betting on i think that's going to be the thing yeah tell the kids you can use the fire emoji exactly exactly well in all seriousness like i mean i think there's really i'll give you two opposite answers one is.
*  I hope if it's useful if it solves problems and people care about this problem being solved they'll adopt the tech.
*  That's that's kind of simple answer and when you're looking to get tech adopted the question is is it solving an important problem people need solved and is the adoption cost low enough that they're willing to make the switch and cut over and do do the pain up front so that they can actually do it right.
*  And so hopefully mojo will be that for a bunch of people and you know people building these hybrid packages are suffering it's really painful and so i think that we have a good shot of helping people.
*  But the other side is like it's okay if people don't use mojo like it's not my job to say like everybody should do this like i'm not saying python is bad like i hope python.
*  See python like all these implementations cuz python ecosystems not just see python it's also a bunch of different implementations with different trade offs in this ecosystem is really powerful and exciting.
*  As our other programming languages it's not like typescript or something is gonna go away right and so it's not there's not a winner take all thing and so i hope that mojo is exciting and useful to people but if it's not that's also fine.
*  But i also wonder what the.
*  The use case for why you should try mojo would be.
*  So practically speaking yeah it seems like.
*  So there's entertainment there's a dopamine hit of saying holy shit this is 10 times faster.
*  This little piece of code is sent as faster and mojo.
*  Out of the box before you get to 35000 exactly i mean just even that i mean that's the dopamine hit that.
*  Every programmer sort of dreams of is the optimization it's it's also the drug they can pull you in and have you waste way too much of your life optimizing and over optimizing right.
*  But so what would he see it would be like comedy is this very hard to predict of course but.
*  You know if you look 10 years from now mojo is super successful what do you think would be the thing.
*  What people like try and then use it regularly and it kind of grows and grows and grows and grows.
*  Also you talk about dopamine hit and so what again humans are not one thing and.
*  Some people love rewriting their code and learning new things and throwing themselves in the deep end and try out anything in my experience most people don't.
*  Like they're too busy they have other things going on by number most people don't like this i want to rewrite all my code.
*  But even those people that you busy people the people that don't actually care about the language that just care about getting stuff done those people do like learning new things.
*  Right and so you talk about the dopamine rush of 10x faster wow that's cool i want to do that again what's also like here's here's the thing i've heard about in a different domain and i don't have to read on my code i can learn a new trick.
*  Right well that's called growth.
*  Right well that's called growth and so and so one thing that i think is cool about mojo and again those will take a little bit of time for.
*  For example the blog post and the books and like all that kind of stuff develop in the language needs to get further along but what we're doing you talk about types like you can say look you can start with the world you already know.
*  Can you can progressively learn new things and adopt them where it makes sense if you never do that.
*  That's cool you're not a bad person if you if you get really excited about one go all the way in the deep end and rewrite everything and really quit ever that's cool right but i think the middle path is actually the more likely one where.
*  That's you know you you come out with a new a new idea and you discover a while that makes my code way simpler way more beautiful way faster way whatever and i think that's what people like now.
*  If you fast forward and you said like 10 years out right i can give you a very different answer on that which is i mean if you go back and look at what computers look like 20 years ago.
*  Every 18 months they got faster for free.
*  I had to ask faster every 18 months it was like clockwork it was it was free right you go back 10 years ago and we entered in this world where suddenly we had multi core cpus and we had gpus.
*  And if you squint and turn your head where gpus is just a many core very simple cpu thing kind of right and so and 10 years ago it was cpus and gpus and graphics.
*  Today we have cpus gpus graphics.
*  And a because it's so important because the compute is so demanding because of the smart cameras and the watches and all the different places that I need to work in our lives it's caused this explosion of hardware.
*  And so part of my thesis part of my belief of where computing goes if you look out 10 years from now it's not going to get simpler.
*  This isn't going back to where we came from it's only going to get weirder from here on out right and so to me the exciting part about what we're building.
*  Is it's about building that universal platform which the world can continue to get weird because again i don't think it's avoidable it's physics.
*  But we can help lift people scale do things with it and they don't have to rewrite their code every time a new device comes out.
*  And i think that's pretty cool and so if mojo can help with that problem then i think that it will be hopefully quite interesting quite useful to wide range of people.
*  Because there's so much potential and like there's some you know maybe analog computers will become a thing or something right and we need to be able to get into a mode where we can move this programming model forward but do so in a way where we're lifting people and and growing them instead of forcing them to write all their code and exploding them.
*  Do you think there'll be a few major libraries that go mojo first.
*  Well so i mean the modular engines all mojo so i can't come back to like we're not building mojo because it's fun we're building mojo because we had to to solve these accelerators.
*  That's the origin story but i mean ones that are currently in python.
*  Yes so i think that a number of these projects will and so one of the things again this is just my best guess like each of the package maintainers also has i'm sure plenty of other things going on people don't like really don't like rewriting code just for the sake of rewriting code.
*  But sometimes like people are excited about like adopting a new idea yeah it turns out that while rewriting code is generally not people's first thing turns out that redesigning something while you rewriting code is not the first thing that you rewriting code.
*  So rewriting something while you rewrite it and using a rewrite as an excuse to redesign can lead to the 2.0 of your thing that's way better than the 1.0.
*  Right and so i have no idea i can't predict that but there's a lot of these places where again if you have a package that is half c and half python.
*  Right you just solve the pain make it easier to move things faster make it easy to debug and evolve your tech adopting mojo kind of makes sense to start with and then it gives you this opportunity to rethink these things.
*  So the two big gains are that the there's a performance gain and then there's the portability to all kinds of different devices and their safety right so you talk about real types.
*  I mean not saying this is for everybody but that's actually a pretty big thing right types are and so there's a bunch of different aspects of what you know what value mojo provides.
*  And so i mean it's funny for me like i've been working on these kinds of technologies and tools for too many years now but you look at swift right and we talked about swift for tens of flow but swift as a programming language right for swifts now.
*  13 years old from when i started it yeah so because i started in 2010 if i remember and so.
*  That that project and i was involved with it for 12 years or something right that that project has gone through zone really interesting story right and it's a mature successful used by millions of people system right.
*  Certainly not dead yet right but but also going through that story arc i learned a tremendous amount about building languages about building pilars about working with community.
*  And things like this and so that experience like i'm helping channel and bring directly in a mojo and you know other systems same thing like apparently i like building.
*  Building an iterating and evolving things and so you look at this lvm thing i worked on 20 years ago you look at mlr right and so a lot of the lessons learned in lvm.
*  Got fed into mlr and i think that mlr is a way better system than lvm was and you know it's swift is a really good system and it's it's it's amazing but i hope that mojo will take the next step for.
*  Step forward in terms of design.
*  In terms of running mojo people can play with it what's mojo playground yeah and.
*  From the interface perspective and from the hardware perspective what's this incredible thing running on.
*  Yeah so right now so here we are two weeks after launch yes we decided that okay we're we have this incredible set of technology that we think might be good but we have not given it to.
*  Lots of people yet and so we're very conservative and said let's put it in a workbook so if it crashes we can do something about it we can monitor and track that right and so.
*  Again things are still super early but we're having like one person a minute sign up with over 70,000 people who extend is kind of crazy.
*  So you can send out to mojo playground and you can use it in the cloud yeah in your browser.
*  And so what that's running on a book yeah what that's running on is that's running on cloud vms and so you share a machine with a bunch of other people but.
*  Turns out there's a bunch of them now because there's a lot of people and so what you're doing is getting free compute and you're getting to play with the same and kind of a limited controlled way so that we can make sure that it doesn't.
*  Totally crash and be embarrassing right here so now a lot of feedback we've gotten is people want to download it around locally so we're working on that right now and so that's the goal that we have to download local yeah that's what everybody expects and so we're working on that right now and so we just want to make sure that we do it right and.
*  I think this is this is one of the lessons I learned from swift also by the way is that when we launched swift.
*  I mean it was super exciting I and we the team had worked on swift for a number of years in secrecy okay and we four years into this development roughly of work on the same.
*  At that point about 250 people at apple knew about it yeah okay so secret apples good secrecy and it was a secret project and so we launched this at wwc a bunch of hoopla and excitement and said.
*  Developers are going to be able to develop and submit apps the app store in three months yeah well several interesting things happened right so first of all we learned that a had a lot of bugs.
*  It was not actually production quality and it was extremely stressful in terms of like trying to get it working for a bunch of people and so what happened was we went from zero to.
*  You know I don't know how many developers apple had at the time but a lot of developers overnight and they ran into a lot of bugs and it was really embarrassing and it was very stressful for everybody involved right it was also very exciting because everybody was.
*  Excited about that the other thing I learned is that when that happened roughly every software engineer who did not know about the project at apple.
*  Their head exploded when it was launched because they didn't know it was coming and so they're like wait what is this I I don't know what this is but.
*  I didn't know it was coming and so they're like wait what is this I I signed up to work for apple because I love objective C why is there a new thing right and so.
*  Now what that meant practically is that the push from launch to first of all the fall but then to two dot on three dot on like all the way forward was.
*  Super painful for the engineering team and myself it was very stressful the developer community was very grumpy about it because they're like okay well wait a second you're changing and breaking my code and like we have to fix the bugs and it was just like a lot of tension and friction on all sides.
*  There's a lot of technical debt in the compiler because we have to run really fast you have to go implement the thing and unblock the use case and do the thing and.
*  And you know it's not right but you never have time to go back and do it right and i'm very proud of the swift team because they've come.
*  I mean we but they came so far and made so much progress over over this time since launch it's pretty incredible and so it is a very very good thing but I still want to do that again right and so.
*  More iterate more through the development process and so what we're doing is we're not launching it when it's hopefully is there dot nine with no testers we're launching it and saying it's zero dot one.
*  Right and so we're saying expectations of saying like okay well don't use this for production right if you're interested in what we're doing we'll do in an open way and we can do it together.
*  But don't use in production yet like we'll get there but let's let's do it the right way and i'm also saying we're not in a race the thing that I want to do is build the world's best thing yeah right because if you do it right and it lifts the industry.
*  Doesn't matter for takes an extra two months yeah like two months is worth waiting and so doing it right and not being overwhelmed with technical debt and things like this is like again war wounds.
*  Lessons learned whatever you want to say I think is absolutely the right thing to do even though right now people are very frustrated that you know you can't download it or it doesn't have feature X or something like this.
*  What have you learned in the in a little bit of time since it's been released into the wild that people have been complaining about feature X or Y or Z what have they been complaining about what they have been.
*  Excited about like yeah almost like detailed things versus I think everyone would be very excited about the big vision yeah yeah well so I mean I've been very pleased I mean in fact I mean we've been massively overwhelmed with response which is.
*  A good problem to have it's kind of like a success disaster yeah in a sense right and.
*  So I mean if you go back in time when we started modular which is just not yet a year and a half ago so it's still a pretty new company new team.
*  Small but very good team of people like we started with extreme conviction that there's a set of problems that we need to solve and if we solve it then people will be interested in what we're doing right.
*  But but again you're building in basically secret right you're trying to figure it out it's the creations a messy process you're having to go through different paths and understand what you want to do and how to explain it often when you're doing disruptive and new kinds of things.
*  Just knowing how to explain it is super difficult right and so when we launched we hope people would be excited.
*  But you know i'm i'm an office but i'm also like don't want to get ahead of myself and so when people found out about mojo i think their heads exploded a little bit.
*  Right and you know here's a i think a pretty credible team that has built some languages and some tools before and so they have some lessons learned.
*  Enter tackling some of the deep problems in the python ecosystem and giving it the love and attention that it should be getting.
*  And i think people got very excited about that and so, if you look at that i mean i think people are excited about ownership and taking a step beyond rust right there's people that are very excited about that there's people that are excited about.
*  You know just like i made game of life go 400 times faster right and things like that and that that's really cool there are people that are really excited about the okay i really hate writing stuff in c++ save me.
*  Like systems in your they're like stepping up like yeah yes.
*  So that's that's that's that's me by the way also i want to stop writing c++ but the i get third person excitement when people tweet.
*  He made this code game of life or whatever faster you're like yeah yeah and also like.
*  I would also say that let me let me cast blame out to people who deserve it sure these terrible people who convinced me to do some of this yes Jeremy Howard yes that guy.
*  Well he's been pushing for this kind of thing he's been for years yeah he's wanted this for a long long time for years and so people don't know Jeremy Howard he's like one of the most legit people in the machine learning community he's a grassroots.
*  He really teaches he's an incredible educator is incredible teacher but also legit in terms of a machine learning engineer himself yeah he's been running the fast dot AI and looking i think for exactly what you exactly and so and so i mean.
*  The first time so i met Jeremy pretty early on but the first time i sat up and i'm like.
*  This guy is ridiculous is when i was at google and we're bringing up tpus and we had a whole team of people and we're there's this competition called Don bench of who can train.
*  Image net yeah fastest right yes and Jeremy and one of his researchers crushed google.
*  Not through sheer force of the amazing amount of compute and the number of tpus and stuff like that that he just decided that progressive imagery sizing was the right way to train the model and if you're a pox faster and.
*  Make the whole thing go go vroom right and i'm like this guy is incredible right and so you can say anyways come back to you know where's mojo coming from Chris finally listen to Jeremy.
*  Is a kind of very.
*  Refreshing pragmatic view that he has about machine learning that.
*  I don't know if it's like this mix of desire for efficiency but ultimately grounded and desire to make a machine learning more accessible to a lot of people i don't know what that is i guess that's coupled with efficiency and performance.
*  But it's not just obsessed about performance so a lot of AI and AI research ends up being that it has to go fast enough to get scale.
*  So a lot of people don't actually care about performance particular on the research side until it allows them to have more a bigger data set.
*  Right and so suddenly now you care about distributed compute and like all these exotic HPC like you don't actually want to know about that you just want.
*  To be able to do more experiments faster and do so with bigger data sets right and so Jeremy has been really pushing limits and one of the things i'll say about Jeremy.
*  And there's many things i could say about your makes i'm a fanboy of his but he fits in his head.
*  In Germany actually takes the time where many people don't to really dive deep into why is the beta parameter of the atom optimizer equal to this.
*  Yeah right and he'll go survey and understand what are all the activation functions in the trade offs and why is it that everybody that does.
*  You know this model pick that thing so the why not just trying different values like really what is going on here right and so as a consequence of that like he's always he again he makes time but he.
*  Spends time to understand things that a depth that a lot of people don't and as you say he then brings it and teaches people.
*  And he's his mission is to help lift you know his website says making a i on cool again like it's about like forget about the high plus it's actually practical and useful let's teach people how to do this right.
*  Now the problem Jeremy struggled with is that he's pushing the envelope.
*  Right research isn't about doing the thing that is staying on the happy path or the the well-paid road right and so a lot of the systems today have been these really fragile fragile fragmented things are special case in this happy path and if you fall off the happy path getting by an alligator.
*  So.
*  What about so Python has this giant ecosystem of packages and as a package repository do you have ideas of how to do that well from mojo.
*  Yeah how to do a repository packages well so that's another really interesting problem that I knew about but I didn't understand how big of a problem it was Python packaging.
*  A lot of people have very big pain points and a lot of scars with Python packaging.
*  I mean this is a several things building and distributing managing dependencies and versioning and all this stuff so from the perspective of if you want to create your own package yes and then or you want to build on top of a bunch of other people's packages and then they get updated.
*  Now I'm not an expert in this so I don't know the answer I think this is one of the reasons why it's great that we work as a team and there's other really good and smart people involved the but one of my.
*  One of the things I've heard from smart people who've done a lot of this is that the packaging becomes a huge disaster when you get the Python and see together.
*  And so if you have this problem where you have code split between Python and see now not only do you have to package the C code you have to build the C code.
*  C doesn't have a package manager right C doesn't have a dependency versioning management system right and so I'm not experienced in the state of the art and.
*  All the different Python package managers but my understanding is that's a massive part of the problem and I think mojo solves that part of the problem directly heads on.
*  Now one of the things I think we'll do with the Community and this isn't again we're not solving all the world's problems at once we have to be kind of focused start with.
*  Is that I think that we will have an opportunity to reevaluate packaging right and so I think that we can come back and say okay well.
*  Given the new tools and technologies and the cool things we have that we've built up because we have not just syntax we have an entirely new compiler stack that works in a new way maybe there's other innovations we can bring together and maybe we can help solve that problem.
*  So almost a tangent to that question from the user perspective of packages.
*  It was always surprising to me.
*  That it was not easier to sort of explore and find packages.
*  That you know with with pip install and it just it feels it's an incredible ecosystem here just.
*  Interesting there wasn't made it still I think not made easier to discover packages to do like.
*  Search and discovery.
*  Well I mean it's kind of funny because this is one of the challenges of these like intentionally decentralized communities and so I don't know what the right answer is for Python I mean there are many people that.
*  Where I don't know the right answer from mojo.
*  So there are many people that would have much more informed opinions and I do but but it's interesting if you look at this right open source communities.
*  You know there's get get is a fully decentralized anybody can do it anyway they want but then there's get hub.
*  Right and get hub centralized commercial in that case right thing really help pull together and help solve some of the discovery problems and help build a more.
*  Consistent community and so maybe there's opportunities for something like a get help for yeah although even get help my maybe wrong on this but the the search and discovery for get help is not that great I guess still use Google search.
*  Yeah well I mean maybe that's because get up doesn't want to replace Google search right and I think there is room for specialized solutions to specific problems but.
*  Sure I don't know I don't know the right answer for get hub either that's they can go figure that out.
*  But the point is to have an interface that's usable that's accessible to people of all different skill levels.
*  Well and again like what are the benefit of standards right standards allow you to build these next level up ecosystem and next level of infrastructure and next level of things and so.
*  Again come back to a complexity see see plus python is complicated it makes everything more difficult to deal with it makes it difficult to port move code around work with all these things get more complicated and so.
*  I mean I'm not an expert but maybe mojo can help a little bit by helping reduce the amount of see in this ecosystem and make it there for scale but so any kind of packages that hybrid in nature would be a natural fit to move to mojo.
*  Which is a lot of them.
*  A lot of them especially they're doing some interesting stuff competition wise.
*  Let me ask you about some features yeah so we talked about obviously indentation that is the type language or optionally typed that the right way to say it.
*  See that optionally or progressively or aggressively I think so so so people have very strong opinions on the right word to use yeah I don't know I look forward to your letters.
*  So there's the the var versus let but let is for constants.
*  Var is an optional yeah var var makes it mutable so you can resign okay.
*  Then there's a.
*  function overloading oh okay yeah there's I mean there's a lot of source of happiness for me but function overloading that's.
*  I guess, is that it is that for performance or is that why does python not have function overloading.
*  As I can speculate so python is a dynamic language the way it works is the.
*  Python and objective see are actually very similar worlds if you ignore syntax.
*  And so objective see is straight line derived from small talk.
*  It really venerable interesting language that much of the world has forgotten about but the people that remember it love it generally.
*  And the way that small talk works is that every object has a dictionary in it and the dictionary maps from the name of a function or the name of a value within an object.
*  To its implementation and so the way you call a method and objective sees you say go look up the way I call food was I go look up food I get a pointer to the function back and then I call it.
*  Okay that's how python works right and so now the problem with that is that the dictionary within a python object all the keys or strings.
*  And it's a dictionary so you can only have one entry per name using it's as simple as that I think it's as simple as that and so now why do they never fix this like why do they not change it to not be dictionary.
*  Like do other things well you don't really have to in python because it's dynamic and so you can say I get into the function.
*  Now I got past an integer do some dynamic test for it if it's a string or do another thing.
*  There's another additional challenge which is even if you did support overloading you're saying okay well here's a version of a function for integers and a function for strings.
*  We'd have even if you could put it in that dictionary you'd have to have the caller do the dispatch and so every time you call the function you'd have to say like is an injures string and so you have to figure out where to do that test and so in a dynamic language.
*  Overloading something you don't have to have so.
*  But now you get into a type language and you know in python if you subscript with an integer.
*  Then you get typically one element out of a collection if you subscript with a range you get a different thing out right and so often in type languages you want to be able to express the fact that cool I have.
*  Different behavior depending on what I actually pass into this thing if you can model that it can make it safer and more predictable and faster and like all these things.
*  It somehow feels safer yes but also feels empowering make it in terms of clarity like you don't have to design hold different functions.
*  Yeah well this is also one of the challenges with the existing python typing systems is that in practice like you take subscript like in practice a lot of these functions.
*  They don't have one signature and they actually have different behavior in different cases and so this is why it's difficult to like retrofit this into existing python code and make it.
*  Play well typing you can have to design for that okay so there's a interesting distinction that people the program python might be interested in is deaf versus FN.
*  So it's two different ways to define a function and FN is a stricter version of deaf what's the coolness that comes from the strictness.
*  So here you get into what is the trade off with the superset yes okay so superset you have to are you really want to be compatible like if you're doing a superset you've decided.
*  Compatibility with existing code is the important thing even if some of the decisions they made were maybe not what you choose.
*  So that means you put a lot of time in compatibility and it means that you get locked into decisions of the past.
*  Even if they may not have been a good thing right now systems programmers typically like to control things.
*  Right and they want to make sure that you know not not all cases of course and even systems programmers are not one thing right but but often you want predictability and so one of one of the things that python has for example,
*  as you know is that if you define a variable you just say X equals four I have a variable named X.
*  Now I say some long method some long name equals seventeen print out some long name oops by typo dip right well the compiler the python compiler doesn't know.
*  In all cases what you're defining what you're using and did you type out the use of it or the definition right and so for people coming from type languages.
*  Again I'm not saying the right wrong but that drives them crazy because they want the compiler to tell them you type out the name of the thing right and so what FN does is it turns on as you say it's a strict mode and so it says okay well you have to actually declare intentionally declare variables for use them.
*  That gives you more predictability more error checking and things like this but you don't have to you don't have to use it.
*  And this is a way that mojo is both compatible because deaths work the same way that deaths have already always worked but provides a new alternative that gives you more control and allows certain kinds of people that have a different philosophy to be able to express that and get that.
*  We usually if you're writing mojo code from scratch you'll be using FN.
*  It depends again depends on your mentality right it's not it's not the death is python and FN is mojo mojo has both and it loves both right it really depends on.
*  Yeah exactly are you are you playing around and scripting something out is it a one off throwaway script cool like python is great at that I will still be using FN but yeah well so I love strictness okay well so control power you also like suffering.
*  Yes go hand in hand.
*  How many how many pull ups.
*  I've lost count at this at this point so that's cool I love you for that yeah some and I love other people like strict things right but I don't want to say that that's the right thing because python is also very beautiful for hacking around and doing stuff and research and these other cases where you may not want that.
*  Yeah I just feel like maybe I'm wrong that but it feels like strictness least the faster debugging so in terms of going from.
*  Even on a small project from zero to completion it just I guess it depends how many bugs you generally usually.
*  Also I mean it's again lessons learned and looking at the ecosystem it's really.
*  I think it's if you study some of these languages over time like the Ruby community for example now Ruby is a pretty well developed pretty established community but along their path they really invested in unit testing.
*  I think that the Ruby community is really push forward the state of the art of testing because they didn't have a type system that caught a lot of bugs and compile time right and so.
*  You can have the best both worlds can have good testing and good types and things like this but but I thought that that was really interesting to see how certain challenges get solved and in python for example.
*  The interactive notebook kind of experiences and stuff like this are really amazing if you type of something it doesn't matter it just tells you that's fine right and so I think that the trails are very different if you're building a.
*  You know large scale production system versus you're building and exploring a notebook and.
*  Speaking of control the hilarious thing if you look at code I write just for myself for fun it's like littered with asserts everywhere.
*  It's a kind of yeah you'd like to.
*  It's basically saying.
*  In a dictatorial way this should be true now otherwise everything stops.
*  Well and that is the sign I can't I love you man but that is a sign of somebody who likes control yeah and so yes I think that you'll like.
*  If I had this turn into I think you're like mojo.
*  Therapy session yes I definitely will.
*  Speaking of asserts exceptions are called errors why is it called errors.
*  So we I mean we use the same word the same as python right but we implement a very different way right and so if you look at other languages like we'll pick on c++ our favorite right.
*  c++ has a thing called zero cost exception handling okay so this is.
*  In my opinion something to learn lessons from.
*  It's a nice play with and so and so zero cost exception handling the way it works is that it's called zero cost because if you don't throw an exception there's supposed to be no overhead for the non error code and so it takes the error path out of the the common path.
*  It does this by making throwing an error extremely expensive and so if you actually throw an error with a c++ compiler using exceptions has to go look up and tables on the side and do all this stuff and so throwing an error can be like 10,000 times more expensive than referring for a function right.
*  Also it's called zero cost exceptions but it's not zero cost by any stretch of the imagination because it massively blows out your code your binary.
*  It also adds a whole bunch of different paths because of destructors and other things like that that exist in c++ and it reduces the number of optimizations it has like all these effects and so this thing that was called zero cost exceptions.
*  It really ain't okay now if you fast forward to newer languages and then this includes swift and rust and go and now mojo.
*  Well in pythons a little bit different because it's interpreted and so like it's got a little bit of a different thing going on but if you look at it if you look at compiled languages.
*  Many newer languages say okay well let's not do that zero cost exception handling thing let's actually treat and throwing an error the same as returning.
*  A variant returning either the normal result or an error now programmers generally don't want to deal with all the typing machinery and like pushing around a variant and so you use all the syntax that python gives us for example try and catch.
*  Functions that raise and things like this you can put a raises decorator on your functions stuff like this and if you want to control that and then the language can provide syntax for but under the hood the way the computer executes it throwing errors basically as fast as returning something.
*  What you think just exactly the same way to look a pilot perspective and so this is actually I mean it's fairly nerdy thing right which is why I love it but the this has a huge impact on the way you design your api's.
*  Right so in c++ huge communities turn off exceptions because the cost is just so high right and so the zero cost cost is so high right and so that means you can't actually use exceptions in many libraries.
*  Right thing and even for the people that do use it well okay how and when do you want to pay the cost if i try to open a file try throw an error.
*  Well what if i'm probing around looking for something right i'm looking up and made from pass with this really slow to do that maybe i another function.
*  That doesn't turn error turns an error code instead and i have two different versions the same thing and so it causes you to fork your api's and so.
*  You know one of the things i learned from apple and i still love is the art of api design is actually really profound i think this is something that python's also done a pretty good job that in terms of building.
*  How to start skill package ecosystem is about having standards and things like this and so you know we wouldn't want to enter a mode where.
*  You know there's this theoretical feature that exists in language but people don't use it in practice now also say one of the other really cool things about.
*  This implementation approach is that it can run on gpus and accelerators and things like this and that standard.
*  Zero cost exception thing would never work on an accelerator and so this is also part of how much you can scale all the way down to like little embedded systems and to bring on gpus and things like that.
*  Can you actually say about the.
*  Maybe.
*  Is there some high level way to describe the challenge of exceptions and how they work in code during compilation.
*  Is just this idea of percolating up a thing.
*  An error yeah yeah so the way the way to think about is think about a function that doesn't return anything just as a simple case right and so you have.
*  Function one calls function to cause function three calls function for along that call stack that are try blocks.
*  Right and so if you have function one calls function to function to as a try block and then within it it calls function three right well what happens if function three throws.
*  Well actually start simpler what happens if it returns well if it returns is supposed to go back out and continue executing and then fall off the bottom of the try block and keep going and it all is good.
*  If the function throws you're supposed to exit the current function and then get into the accept clause right and then do whatever codes there and then keep falling on and going on.
*  And so the way that a compiler like mojo works is that the call to that function which happens in the except block cause a function and then instead of returning nothing it actually returns you know a variant between nothing and an error and so if you return normally off the bottom to return.
*  You return nothing and if you throw throw an error you.
*  Return the variant that is I'm an error right so when you get to the call you say okay cool I called a function hey I know locally I'm in a try block.
*  Right and so I I call the function and then I check to see what it returns a half is that everything jump to the except block.
*  And that's all done for you behind the scenes exactly and so the competitors all this for you and I mean one of the things if you dig into how this stuff works in python it gets a little bit more complicated because you have finally blocks which now need you need to go into do some stuff and then those can also throw and return.
*  What.
*  Like this stuff matters compatibility like there's a nest of there's with clauses and so with clauses are kind of like finally blocks of some special stuff going on and so there's nothing in general nothing of anything that's thing of functions should be illegal.
*  It just feels like it has a level of complexity.
*  I'm merely an implementer and so this is again one of the one of the one of the trade offs you get when you decide to build a superset is you get to implement a full fidelity implementation of the thing that you decided is good and so.
*  yeah I mean we can we can complain about the reality of the world and shake our fist but.
*  It always feels like you shouldn't be a lot to do that like to declare functions and send functions inside functions.
*  Wait wait wait what happened to the list guy.
*  No I understand that but list is what I used to do in college.
*  So now you've grown up.
*  You know we've all done things in college are not part of.
*  Love list I love.
*  Okay yeah I was gonna say you're afraid of me you're taking.
*  I love this it's it worked it worked as a joke in my head and.
*  Yeah right so so so so message functions are joking aside actually really great and for certain things right and so these are also called closures closures are pretty cool and you can pass callbacks there's a lot of good patterns and so.
*  So speaking of which I don't think you have.
*  I'm not sure if nested functions implemented yet in mojo we don't have lambda syntax but we do have.
*  There's a few things on the road map they have that it'd be cool to sort of just fly through because it's interesting to see you know how many features there are in a language small and big.
*  Yep they have to implement yeah so first of all there's tuple support and that has to do with some very specific aspects of it like the parentheses are not parentheses that.
*  Yes just a totally syntactic things.
*  A syntactic thing okay there's but it's cool still.
*  So keyword arguments and functions.
*  Yeah so this is where in python you can say call a function X equals four yeah and X is the name of the argument that's a nice sort of documenting self documenting feature.
*  Yeah I mean and again this isn't rocket science to implement this just the laundry shift on the list.
*  The bigger features are things like traits.
*  So traits are when you want to define abstract so when you get into type languages you need the ability to write generics.
*  And so you want to say I want to write this function and now I want to work on all things that are arithmetic like.
*  What is arithmetic like mean well arithmetic like is a categorization of a bunch of types and so again you can define many different ways and I'm not going to go into ring theory or something.
*  But the you know you can say it's arithmetic like if you can add subtract multiply divide it for example right and so what you're saying is you're saying.
*  There's a set of traits that apply to a broad variety of types.
*  And so there are all these types arithmetic like all these tensors and floating point integer and like there's this category of types and then I can define on an orthogonal axis algorithms that then work against types that have those properties.
*  And so this is a again it's a widely known thing it's been implemented in swift and rust and many languages so it's not Haskell.
*  Which is where everybody learns learns their tricks from but the but we need to implement that and that'll enable a new level of expressivity.
*  Also classes yeah classes are big deal that's a big deal still to be implemented.
*  You said lambda syntax and there's like detail stuff like whole module import.
*  Support for top level code at file scope so and then global variables also.
*  So being able to have variables outside of a top level and so this comes back to the where mojo came from and the fact that 0.1 right and so.
*  we're building so modular is building an AI stack right and AI stack has a bunch of problems working with hardware and.
*  Writing high performance kernels and doing this kernel fusion thing I was talking about and getting the most out of the hardware and so we've really prioritized and built mojo to solve modules problem.
*  Right now our North star is build out and support all the things and so we're making incredible progress by the way mojo is only like seven months old.
*  So that's another interesting thing I mean part of the reason I wanted to mention some of these things is like there's a lot to do and it's pretty cool how you just kind of.
*  Sometimes you take for granted how much there is in a programming language how many cool features you kind of rely on, and this is kind of a nice reminder when you lay it as its do list.
*  yeah and so I mean but also you look into it's it's amazing how much is also there and you take it for granted that.
*  A value if you define it it will get destroyed automatically like that little feature itself is actually really complicated.
*  Given the way the ownership system has to work and the way that works within mojo is a huge step forward from what rust and swift have done, but can you say that again when value.
*  You define it gets destroyed on yeah so like say you have a string right so you just find a string on the stack okay or whatever that means like in your local function.
*  Right and so you say like whether it be in a deaf one so you just say X equals hello world right well if your string type requires you to have a string type.
*  Well if your string type requires you to allocate memory then was destroyed you have to do you like it so in python and mojo you define that with the del method right where does that get run.
*  Well it gets run sometime between the last use of the value and.
*  The end of the program I can this you now get into garbage collection you can to like all these long debated you talk about religions and and trade offs and things like this this is a hugely hotly contested world.
*  If you look at c++ the way this works is that if you define a variable or a set of variables within a function they get destroyed in a last in first out order so it's like nesting.
*  This has a huge problem because if you define you have a big scope and you find a whole bunch of values at the top and then you use them and then you do a whole bunch of code that doesn't use them.
*  They don't get destroyed until the very end of that scope right and so it's also destroys tail calls so good functional programming right this this has a bunch of different impacts on.
*  You know you talk about reference counting optimizations and things like this a bunch of very low level things and so what mojo does is it has a different approach on that from any language i'm familiar with where it destroys them as soon as possible.
*  And by doing that you get better memory use get better predictability you get tail calls that work you get a bunch of other things you better ownership tracking there's a bunch of these very simple things.
*  That are very fundamental that are already built in there and mojo today that are the things that nobody talks about generally but when they don't work right you find out you have to complain about is it trivial to know.
*  What's the soonest possible to delete a thing that's not going to be used again yeah well I mean it's generally trivial it's it's after the last use of it so if you define the access to string and then you have some use of X somewhere in your code within that scope.
*  You mean within the scope that is accessible it's yeah exactly so you can only use something within its scope and so then it doesn't wait until the end of the scope to delete it it destroys it after the last use so there's kind of some very eager machine that's just sitting there and deleting.
*  And it's all in the compiler so it's not at runtime which is also cool and so yeah and so what and this is actually non trivial because you have control flow and so it gets complicated pretty quickly and so like getting this right was not.
*  You have to insert delete like in a lot of places potentially yeah exactly so the compiler has to reason about this and this is where again it's experience building languages and not getting this right so again you get another chance to do it and you get.
*  Basic things like this right but it's extremely powerful when you do that right and so there's a bunch of things like that that kind of combined together.
*  And this comes back to the you get a chance to do it the right way do it the right way and make sure that every brick you put down is really good so that when you put more bricks on top of it they stack up to something that's beautiful.
*  What is also.
*  How many.
*  Design discussions do there have to be about particular details like implementation of particular small features because the features that seems small I bet some of them might be like.
*  Really require really big design decisions yeah well so I mean let me give you another example this Python has a feature called a sink away so it's a new feature I mean in the long history.
*  It's a relatively new feature right that allows way more expressive asynchronous programming okay again this is this is a Python is a beautiful thing and they did things are great for mojo for completely different reasons.
*  The reason that a sink away got added to Python as far as I know is because Python doesn't support threads.
*  Okay and so Python doesn't support threads but you want to work with networking and other things like that that can block I mean Python does support threads it's just not its strength and so.
*  And so they added this feature called a sink away it's also seen in other languages like Swift and JavaScript and many other places as well.
*  It's a great and mojo is amazing we have a high performance heterogeneous compute runtime underneath the covers that then allows non blocking ios you get full use of your accelerator.
*  That's huge turns out it's actually really important part of fully utilizing machine you talk about design discussions.
*  I took a lot of discussions right and it probably will require more iteration and so my philosophy with mojo is that you know we have a small team of really good people that are pushing forward and they're very good at.
*  The extremely deep knowing how the compiler and runtime and like all the low level stuff works together.
*  But they're not perfect same thing as the swift team right, and this is where one of the reasons we released mojo much earlier is so we can get feedback and we've already like renamed a keyword data community feedback and join.
*  We use an ampersand and now it's named in out we're not we're not renaming existing Python keywords because that breaks compatibility right we're naming things we're adding.
*  And making sure that they are designed well we get usage experience we iterate and work with the community because.
*  Again if you scale something really fast and everybody writes all their code and they start using it in production then it's impossible to change and so you want to learn from people you want to iterate and work on that early on, and this is where design discussions it's it's actually quite important.
*  Could you could you incorporate an emoji like into the language into the main language like a like a like a do you have a favorite one.
*  Like the do you have a favorite one.
*  Why really like interest of humor like raw full whatever rolling on the floor laughing so that could be like.
*  What would that be the use case for that like an exception thrown exception of some sort I should totally file feature requests.
*  Or maybe a hard one it has to be a hard one.
*  People have told me that i'm insane so this is this is this is i'm liking this.
*  I'm gonna i'm gonna use the viral nature of the internet to to actually get this to get this past.
*  I mean it's funny you come back to the flame emoji file extension right the.
*  You know we have the option to use the flame emoji which just even that concept cause for example the people that get up say now i've seen everything.
*  Yeah there's something it kind of is reinvigorating it's like.
*  It's like oh that's possible that's really cool that for some reason that makes everything else.
*  The world is ready for this stuff and so you know when we have a package manager will clearly have to innovate by having the compiled package saying be the little box with the bow on it right I mean.
*  It has to be done it has to be done is there some stuff on the road map that you're particularly stressed about or excited about that you're thinking about a lot.
*  I mean as a today snapshot which will be obsolete tomorrow the lifetime stuff is really exciting and so lifetimes give you safe references to memory without dangling pointers.
*  This has been done in languages like rust before and so we have a new approach which is really cool i'm very excited about that that'll be out to the community very soon.
*  The traits feature is really a big deal and so that's blocking a lot of API design and so there's that i think that's really exciting.
*  A lot of it is these kind of table stakes features one of the things that is again also lessons learned with swift.
*  Is that programmers in general like to add syntactic sugar.
*  And so it's like oh well this annoying thing like like in python you have to spell it on our ad why can't I just use plus.
*  Def plus come on why can't I just do that right and so trivial bit of syntactic sugar it makes sense it's beautiful it's obvious we're trying not to do that and so.
*  For two different reasons one of which is that again lesson learned with swift swift has a lot of syntactic sugar.
*  Which may or may be a good thing maybe not I don't know but but because it's such an easy and addictive thing to do sugar like make sure blood get crazy right.
*  Like the Community will really dig into that and want to do a lot of that and I think it's very distracting from building the core abstractions second is we want to be a good member of the python community.
*  Right and so we want to work with the broader python community and yeah we're pushing forward a bunch of systems programming features and we need to build them out to understand them.
*  But once we get a long ways forward I want to make sure that we go back to the python community and say okay let's do some design reviews let's actually talk about this stuff let's figure out how we want this stuff all to work together and syntactic sugar just makes all that more complicated so.
*  And yeah list comprehension is yet to be implemented and my favorite day I mean dictionaries.
*  Yeah there's some basic 0.1 0.1 but nonetheless it's actually still quite interesting and useful as you mentioned modular is very new.
*  Mojo is very new it's a relatively small team yeah there's building up this gigantic stack it's incredible stack that's going to perhaps define the future of development of our AI overlords.
*  We just hope it will be useful.
*  As do all of us so what what have you learned from this process of building up a team maybe one question is how do you hire.
*  Yeah great programmers great people that operate in this compiler hardware machine learning software interface design space yeah and maybe are a little bit fluid yeah what they can do so okay so I was designed to.
*  So building a company is just as interesting in different ways is building a language like different skill sets different things but super interesting and I built a lot of teams a lot of different places.
*  If you zoom in from the big problem into recruiting well so here's our problem okay I'll just I'll be very straightforward about this.
*  We started modular with a lot of conviction about we understand the problems we understand the customer pain points we work backwards from the suffering in the industry and if we solve those problems we think will be useful for people.
*  The promise is that the people we need to hire as you say are all these super specialized people that have jobs at big tech.
*  Big tech world right and you know we I don't think we have product market fit in the way that a normal startup.
*  Does we don't have product market fit challenges because right now everybody's using AI and so many of them are suffering and they want help and so again we started with strong conviction now.
*  Again you have to hire and recruit the best and the best all have jobs and so what we've done is we said okay well let's build an amazing culture.
*  Start with that that's usually not something a company starts with usually you hire a bunch of people and then people start fighting and it turns into a gigantic mess and then you try to figure out how to improve your culture later.
*  My co founder Tim in particular is super passionate about making sure that that's right and we've spent a lot of time early on to make sure that we can scale.
*  Can you comment sorry before we get to the second yeah what makes for a good culture.
*  So I mean there's made different cultures and I have learned many things from a lot of several very unique almost famously need cultures and some of them I learned what to do and some of them and learned what not to do get and so.
*  We want an inclusive culture I believe in like amazing people working together and so I've seen cultures where people have amazing people and they're fighting each other.
*  I see amazing people and they're told what to do like doubt shout line up and do what I say it doesn't matter if it's the right thing do it right.
*  And neither of these is the and I've seen people that have no direction they're just kind of floating in different places and they want to be amazing they just don't know how and so a lot of it starts with have a clear vision.
*  So we have a clear vision what we're doing and so I kind of grew up at Apple in my engineering life right and so a lot of the Apple DNA rubbed off on me.
*  Micro founder Tim also is like a strong product guy and so what we learned is you know I was taught at Apple that you don't work from building cool technology.
*  You don't work from like come up with cool product and think about the features you'll have in the big check boxes and stuff like this because if you go talk to customers they don't actually care about your product.
*  They don't care about your technology what they care about is their problems.
*  And if your product can help solve their problems well hey they might be interested in that right and so if you speak to them about the problems if you understand you have compassion you understand what people are working with then you can work backwards to building an amazing product.
*  So the visions and then you can run the problem and then you can work backwards in solving technology and at Apple like it's I think pretty famously said that you know for every.
*  You know there's a hundred nos for every yes I would find that say that there's a hundred not yet for every yes but famously if you go back to the iPhone for example right the iPhone one I read I mean many people laughed at it because it didn't have 3G it didn't have copy and paste.
*  Right and then a year later okay finally has 3G but it still doesn't have copy and paste it's a joke nobody will ever use this product blah blah blah blah blah blah right.
*  Your three had copy and paste and people stop talking about it right and so and so being laser focus and having conviction understanding what the core problems are and giving the team the space to be able to build the right tech is really important.
*  Also I mean you come back to recruiting you have to pay well.
*  Right so we have to pay industry leading salaries and have good benefits and things like this that's a big piece we're a remote first company and so we have to.
*  So remote first has a very strong set of pros and cons, on the one hand, you can hire people from wherever they are and you can attract amazing talent, even if they live in strange places or unusual places on the other hand, you have time zones.
*  On the other hand, you have like everybody on the Internet will fight if they don't understand each other and so we've had to learn how to.
*  Like have a system where we actually fly people in and we get the whole company together periodically and then we get work groups together and we plan and execute together and there's like an intimacy to the in person brainstorming.
*  I guess you lose but maybe you don't maybe if you get to know each other well and you trust each other, maybe you can do that.
*  Also when the pandemic first said I mean i'm curious about your experience to the first thing I missed was having whiteboards yeah.
*  Right those design discussions are like I can high high intensity work through things get things done work through the problem of the day understand where you're on figure out and solve the problem and move forward.
*  But we figured out ways to work around that now with you know all these screen sharing and other things like that that we do the thing I miss now is sitting down a lunch table with the team yeah.
*  The spontaneous things like those the coffee the coffee bar things and the and the bumping into each other and getting to know people outside of the transactional solve a problem over zoom.
*  And I think there's there's just a lot of stuff that i'm not an expert at this I don't know who is hopefully there's some people but there's stuff that somehow is missing on zoom.
*  Even with the whiteboard if you look at that.
*  If you have a room with one person at the whiteboard and there's like three other people at a table.
*  There's a first of all there's a social aspect to that where you're just shooting the shit a little bit almost like yeah as people just kind of coming in and yeah that but also while.
*  Like it's a breakout discussion that happens for like seconds at a time maybe an inside joke or like this interesting dynamic that happens that zoom your bonding your bonding your bonding but through that bonding.
*  Your bonding your bonding but through that bonding you get the excitement there's certain ideas are like complete bullshit and you'll see that in the faces of others that you won't see necessarily on zoom and like something it feels like that should be possible to do without being in person.
*  Well I mean being in person is a very different thing it's worth it but you can't always do it and so again we're still learning and we're also learning is like humanity with this new reality right.
*  But but what we found is that getting people together whether it be a team or the whole company or whatever is worth the expense because people work together and are happier.
*  After that like it just it just like there's a massive period time where you like go out and things start getting afraid pull people together and then you realize that we're all working together we see things the same way we work through the disagreement or the misunderstanding we're talking.
*  Cross each other and then you work much better together and so things like that I think are really quite important what about.
*  People that are kind of specialize in very different aspects of the stack working together what are some interesting challenges there yeah well so I mean I mean there's lots of interesting people as you can tell I'm you know.
*  You know hard to deal with to but you are the most lovable the.
*  So one of the so there's different philosophies in building teams for me and so some people say hire 10x programmers and that's the only thing that whatever that means right.
*  What I believe in is building well balanced teams.
*  Teams that have people that are different in them like if you have all generals and no troops were all troops and no generals or you have all people that think in one way and not the other way what you get is you get a very biased and skewed and weird situation where people end up being unhappy.
*  And so what I like to do is I like to build teams of people where they're not all the same you know we do have teams and they're focused on like runtime or compiler GPU or whatever the speciality is.
*  But people bring a different take and have a different perspective and I look for people that complement each other and particularly if you look at leadership teams and things like this you don't want.
*  Everybody thinking the same way you want people bringing different perspectives and experiences and so I think that's really important.
*  That's team but what about building a company as ambitious as modular so what some interesting questions there.
*  I mean so many like so one of the things I love about okay so modular is the first company I built from scratch.
*  One of the first things that was profound was I'm not cleaning up somebody else's mess.
*  Right and so if you look at that liberating this and it's super liberating and and also many of the projects I've built in the past have not been core to the product of the company.
*  Swift is not Apple's product right MLA are is not Google's revenue machine or whatever right it's not it's it's important.
*  But it's like working on the accounting software for you know the retail giant or something right it's it's it's it's like enabling infrastructure and technology and so modular the tech we're building is.
*  Here to solve people's problems like it is directly the thing we're giving to people and so this is a really big difference and what it means for me as a leader but also for many of our engineers is they're working on the thing that matters.
*  And that's actually pretty I mean again for for compiler people and things like that that's that's usually not the case right and so that's that's also pretty exciting and and quite nice but the.
*  One of the ways that this manifest is it makes it easier to make decisions and so one of the challenges I've had in other worlds is it's like okay well.
*  Community matters somehow for the goodness of the world like or open source matters theoretically but I don't want to pay for a t-shirt.
*  Right or some swag like well t-shirts cost 10 bucks each you can have 100 t-shirts for a thousand dollars to a mega corporate thousand dollars is uncountably can't count that low right but justifying it and getting a t-shirt by the way if you'd like a t-shirt.
*  Why would 100% like a t-shirt are you joking.
*  A fire moji t-shirt that I will I will treasure this is that a good I will pass it down to my grandchildren and so you know it's it's very liberating side I think that we should have a t-shirt.
*  Right and it becomes very simple because I like Lex this this this is awesome.
*  So.
*  I have to ask you about the.
*  One of the interesting developments with large language models.
*  Is that they're able to generate code recently really well.
*  Yes to a degree that maybe.
*  I don't know if you understand but I have I struggled to understand because it forces me to ask questions about the nature of programming of the nature of thought.
*  The nature of thought because the language models are able to predict the kind of code I was about to write so well.
*  That it makes me wonder like how unique my brain is and where the valuable ideas actually come from like how much to contribute in terms of.
*  Ingenuity innovation to code I write or design and that kind of stuff.
*  When you stand on the shoulders of giants are you really doing anything and what LLMs are.
*  Helping you do is they help you stand on the shoulders of giants in your program there's mistakes they're interesting that you learn from but I just it would love to get your opinion first high level of what you think about this impact of larger language models when they do programs and this is when they generate code.
*  Yeah well so.
*  I don't know where it all goes yeah I'm an optimist and I'm a human optimist I think that things I've seen are that a lot of the LLMs are really good at crushing leak code projects and they can reverse the link list like crazy.
*  Well it turns out there's a lot of instances of that on the internet and it's a pretty stock thing and so if you want to see.
*  Standard questions answered LLMs can memorize all the answers and that can be amazing and also they do generalize out from that and so there is good work on that but.
*  But I think that if you in my experience building things building something like you talk about mojo or you talk about these things you talk about building an applied solution to a problem it's also about working with people.
*  What's about understanding the problem what is the product you want to build what are the use case where the customers can't just go survey all the customers because they'll tell you that they want a faster horse maybe they need a car right and so a lot of it comes into.
*  I don't feel like we have to compete with LLMs I think they'll help automate a ton of the mechanical stuff out of the way and just like you know I think we all try to scale through delegation and things like this delegating wrote things to an LLM I think is extremely valuable and.
*  Approach that will help us all scale and be more productive but I think it's a fascinating companion but I'd say I don't think that means that we're going to be done with coding.
*  But there's power in it as a companion and from there I could I would love to zoom in on to mojo a little bit do you think.
*  Do you think about that do you think about LLMs generating mojo code.
*  And helping sort of like we design new programming language it almost seems like it would be nice to sort of.
*  Almost as a way to learn how I'm supposed to use this thing for them to be trained on some of them yeah good so I do lead an AI company so maybe there will be a mojo LLM at some point.
*  But if your question is like how do we make a language to be suitable for LLMs yeah I think that the.
*  I think the cool thing about LLMs that you don't have to right and so if you look at what is English or any of these other terrible languages that we as humans deal with on a continuous basis they're never designed for machines.
*  And yet there are the intermediate representation there the exchange format that we humans use to get stuff done right and so these programming languages there an intermediate representation between.
*  The human and the computer or the human in the compiler roughly right and so I think the LLMs will have no problem learning whatever keyword we pick maybe the five moji is going to maybe that's going to break it doesn't tokenize note the.
*  Reverse of that it will actually enable it because one of the issues I could see with being a superset of Python is there be confusion by the gray area so be mixing stuff.
*  But I'm a human optimism also an LLM optimist I think that will solve that problem was the edge but the but but you look at that and you say okay well.
*  Reducing the rote thing right turns out compilers are very particular and they really want things they really want the indentation be right they really want the colon to be there on your else or else it'll complain right I mean can buy this can do better at this but.
*  LLMs can totally help solve that problem and so I'm very happy about the new predictive coding and copilot type features and things like this because I think it'll all just make us more productive it's still messy and fuzzy and uncertain unpredictable so.
*  But is there a future you see given how big of a leap GPT four was where you start to see something like LLMs inside a compiler or no I mean you could do that yeah absolutely I mean I think that'd be interesting is that wise well I mean it'd be very expensive.
*  So compilers run fast and they're very efficient and LLMs are currently very expensive there's on device LLMs and there's other things going on and so maybe there's an answer there.
*  I think that one of the things that I haven't seen enough of is that so LLMs to me are amazing when you tap into the creative potential of the hallucinations.
*  Right and so if you're building doing creative brainstorming or creative writing or things like that the hallucinations working your favor.
*  If you're writing code that has to be correct cuz you're gonna ship in production then maybe that's not actually a feature and so I think that there has been research and there has been work on building.
*  Algebraic reasoning systems and kind of like figuring out more things that feel like proofs and so I think that there could be interesting work in terms of building more reliable scale systems and that could be interesting.
*  But if you chase that rabbit hole down the question then becomes how do you express your intent of the machine.
*  And so maybe you want LLM to provide the spec but you have a different kind of net that then actually implements the code.
*  Right so it's a use that is documentation and inspiration versus the actual implementation.
*  Since a successful modular will be the thing that runs I say so jokingly our AI overlords but AI systems that are used across.
*  I know it's a cliche term but in and of things so cost so I'll joke and say like a GI should be written in mojo yeah a GI should be in mojo you're joking but it's also possible that it's not a joke.
*  That a lot of the ideas behind mojo is seems like the natural set of ideas that would enable at scale training and inference of AI systems.
*  So just have to ask about the big philosophical question about human civilization so folks like Eliezer it cost you're really concerned about the threat of AI.
*  The threat of AI do you think about the good.
*  And the bad that can happen at scale deployment of AI systems.
*  Also I've I've thought a lot about it and there's a lot of different parts to this problem everything from job displacement to sky nut things like this and so you can zoom into some parts of this problem.
*  I'm not super optimistic about a GI being solved next year.
*  I don't think that's gonna happen personally so you have a kind of Zen like calm about is there's a nervousness because the leap of GPT for seem so big.
*  Sure it's like we're almost where there's some kind of transitionary period you're thinking well so I mean there's a couple of things going on there one is.
*  I'm sure GPT 5 and 7 and 19 will be also huge leaves they're also getting much more expensive to run and so there may be a limiting function terms of just expense on one hand and train like that that could be a limiter that slows things down.
*  But I think the bigger limiter outside of like sky that takes over and I don't spend time thinking about that because it's kind of takes over and kills us all then I'll be dead so I don't worry about that.
*  So you know I mean that's just okay other things worry about I'll just focus on yeah I'll focus and not worry about that one but I think that the other thing I'd say is that.
*  I'm as quickly but humans move slowly and we adapt slowly and so what I expect to happen is just like any technology diffusion.
*  Like the promise and then the application takes time to roll out and so I think that I'm not even too worried about autonomous cars defining way all the taxi drivers remember autonomy is supposed to be solved by 2020.
*  Boy do I.
*  So and and so like I think that on the one hand we can see amazing progress but on the other hand we can see that.
*  You know the reality is a little bit more complicated and it may take longer to roll out than than you might expect well that's in the physical space I do think in the digital space is a.
*  The stuff that's built on top of LLMS that runs.
*  You know the millions of apps that can be built on top of them and they could be run on millions of devices millions of types of devices.
*  I just think.
*  That the rapid effect it has on human civilization could be truly transformative to it yeah.
*  One so that.
*  One and there I think it depends on are you an optimist or pessimist or masochist.
*  Just to clarify.
*  Optimist about human civilization.
*  And so I look at that as saying okay cool well I do right and so some people say oh my God is going to try so how do we prevent that I kind of look at it from a is it going to unlock us all right you talk about coding is going to make so I don't have to do all the repetitive stuff.
*  Well suddenly that's a very optimistic way to look at it and you look at what a lot of a lot of these technologies have done to improve our lives and I want that to go faster.
*  What do you think the future programming looks like in the next 10 20 30 50 years.
*  The LMS and.
*  With with mojo with modular like the vision for devices the hardware to the compilers to this to the different stacks of software.
*  Well so what I want I mean coming coming back to my arch nemesis right it's complexity right so again me being the optimist if we drive down complexity we can make these tools these technologies these cool hardware widgets accessible to way more people.
*  Right and so what I'd love to see is more personalized experiences more things the research getting into production instead of being lost it nurops.
*  Right and so and like the these things that impact people's lives by entering products and so one of the things that I'm a little bit concerned about is right now.
*  The big companies are investing huge amounts of money and are driving the top line of AI capability for really quickly.
*  But if it means that you have to have a hundred million dollars to train a model or more hundred billion dollars right well that's going to make it very concentrated with very few people.
*  In the world that can actually do this stuff I'd much rather see lots of people across the industry be able to participate in uses.
*  Lots of people across the industry be able to participate in uses and you look at this you know I mean a lot of great research has been done in the health world and looking at.
*  Like detecting pathologies and doing radiology with AI and like doing all these things well the problem today is that to deploy and build these systems you have to be an expert in radiology and expert in AI.
*  And if we can break down the barriers so that more people can use AI techniques and it's more like programming python.
*  Which roughly everybody can do if they want to write then I think that will get a lot more practical application these techniques and a lot more niche year.
*  Cool but narrower domains I think that's that's gonna be really cool.
*  You think we'll have more or less programmers in the world and now.
*  Well so I think we'll have more more programmers but they may not consider themselves to be programmers.
*  Maybe a different name for you right I mean do you consider somebody that uses you know I think that arguably the most popular programming language is excel.
*  Yeah.
*  Right yeah and so do they consider themselves to be programmers maybe not I mean some of them make crazy macros and stuff like that but but but what what.
*  You mentioned Steve jobs is it's the bicycle for the mind the laws you go faster right and so I think that as we look forward right what is a I look at it is.
*  Hopefully a new programming paradigm it's like object oriented programming right if you want to write a cat detector you don't use for loops.
*  Turns out that's not the right tool for the job right and so right now unfortunately because I mean it's not unfortunate but it's just kind of where where things are.
*  Yeah is this weird different thing that's not integrated into programming languages and normal tool chains and all the technologies really weird and doesn't work right and you have to babysit it and.
*  Every time you switch your words different shouldn't be that way when you change that when you fix that suddenly again the tools technologies can be way easier to use you can start using them for many more things and so that's that's why I would be excited about.
*  What kind of advice could you give to somebody in high school right now or maybe early college who's curious about programming.
*  And feeling like the world is changing really quickly here yeah what kind of stuff to learn what kind of stuff to work on should they finish college they go work at a company should they're build a thing what do you think.
*  Also I mean one of the things I'd say is that you'll be most successful if you work on something you're excited by.
*  And so don't get the book and read the book cover to cover and study and memorize and recite and flash card and go build something.
*  Like a solve a problem go build the thing that you want to exist go build an app go build train a model like go build something actually is it and set a goal for yourself and if you do that then you'll.
*  You know there's a success is the adrenaline rush there's the achievement there's the unlock that I think is where you know if you keep setting goals and you keep doing things and building things learning by building is really powerful.
*  In terms of career advice I mean everybody's difference very hard to give generalized experience generalized advice all speak as you know a compiler nerd if everybody's going.
*  Left sometimes it's pretty cool to go right yeah and so just because everybody's doing a thing it doesn't mean.
*  You have to do the same thing and follow the herd in fact I think that sometimes the most exciting past or life lead to being curious about things that nobody else actually focuses on right and turns out that understanding deeply.
*  Parts of the problem that people want to take for granted makes you extremely valuable and specialize in ways that the herd is not and so.
*  Again I mean there's lots of rooms for specialization lots of rooms for generalist there's lots of room for different kinds and parts of the problem but.
*  But I think that it's you know just because everything everybody's doing one thing doesn't mean you should necessarily do it.
*  And now the herd is using python so if you want to be a rebel go check out mojo and help chris and the rest of the world fight the arch nemesis of complexity because simple is beautiful there you go.
*  This is an incredible person you've you've been so kind to me ever since we met even extremely supportive i'm forever grateful for that thank you for being who you are for being legit for being kind for fighting this.
*  Really interesting problem of how to make a accessible to huge number of people huge number of devices.
*  Yeah well so lecture pretty special person to write and so I think that you know one of the funny things about you is that besides being curious and pretty damn smart you're actually willing to push on things and you're you're I think that you've got an agenda to like make the world think.
*  Which I think is a pretty good agenda it's a pretty good one thank you so much for talking to Chris yeah thanks.
*  Thanks for listening to this conversation with Chris Lattner to support this podcast please check out our sponsors in the description and now let me leave you some words from Isaac Asimov I do not fear computers I fear the lack of them.
*  Thank you for listening and hope to see you next time.

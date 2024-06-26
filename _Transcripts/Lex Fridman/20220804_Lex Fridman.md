---
Date Generated: April 10, 2024
Transcription Model: whisper medium 20231117
Length: 18890s
Video Keywords: ['agi', 'ai', 'ai podcast', 'artificial intelligence', 'artificial intelligence podcast', 'doom', 'id software', 'john carmack', 'john romero', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'meta', 'metaverse', 'mit ai', 'programming', 'quake', 'vr', 'wolfenstein']
Video Views: 1557342
Video Rating: None
---

# John Carmack: Doom, Quake, VR, AGI, Programming, Video Games, and Rockets | Lex Fridman Podcast #309
**Lex Fridman:** [August 04, 2022](https://www.youtube.com/watch?v=I845O57ZSy4)
*  I remember the reaction where he had drawn these characters and he was slowly moving around and like people had no experience with 3D navigation.
*  It was all still keyboard. We didn't even have mice.
*  I am set up at that time, but slowly moving going up, picked up a key, go to a wall.
*  The wall disappears in a little animation and there's a monster like right there and he practically fell out of his chair.
*  It was just like, ah, and games just didn't do that.
*  You know, the games were the God's eye view.
*  You were a little invested in your little guy.
*  You can be like, you know, happy or sad when things happen, but you just did not get that kind of startle reaction.
*  You weren't inside your face, something in the back of your brain.
*  Some reptile brain thing is just going, oh shit, something just happened.
*  And that was one of those early points where it's like, yeah, this is going to make a difference.
*  This is going to be powerful and it's going to matter.
*  The following is a conversation with John Carmack, widely considered to be one of the greatest programmers ever.
*  He was the co-founder of id Software and the lead programmer on several games that revolutionized the technology,
*  the experience and the role of gaming in our society, including Commander Keen, Wolfenstein 3D, Doom and Quake.
*  He spent many years as the CTO of Oculus VR, helping to create portals into virtual worlds and to define the technological path to the metaverse and meta.
*  And now he has been shifting some of his attention to the problem of artificial general intelligence.
*  This was the longest conversation on this podcast at over five hours.
*  And still I could talk to John many, many more times.
*  And we hope to do just that.
*  This is the Lex treatment podcast.
*  To support it, please check out our sponsors in the description.
*  And now, dear friends, here's John Carmack.
*  What was the first program you've ever written?
*  Do you remember?
*  Yeah, I do.
*  So I remember being in a radio shack going up to the TRS-80 computers
*  and learning just enough to be able to do 10 print John Carmack.
*  And it's kind of interesting how, of course, I, you know, Carnegie and Ritchie kind of standardized Hello World as the first thing that you do in every computer programming language and every computer.
*  But not having any interaction with the cultures of Unix or any other standardized things, it was just like, well, what am I going to say?
*  I'm going to say my name.
*  And then you learn how to do Go to 10 and have it scroll all off the screen.
*  And that was definitely the first thing that I wound up doing on a computer.
*  Can I ask you a programming advice?
*  I was always told in the beginning that you're not allowed to use Go to statements.
*  That's really bad programming.
*  Is this correct or not?
*  Jumping around code.
*  Can we look at the philosophy and the technical aspects of the Go to statement that seems so convenient?
*  But it's supposed to be bad programming.
*  So certainly back in the day in basic programming languages, you didn't have proper loops.
*  You didn't have four whiles and repeats.
*  That was the land of Pascal for people that kind of generally had access to it back then.
*  So you had no choice but to use Go tos.
*  And as you made what were big programs back then, which were a thousand line basic program is a really big program.
*  They did tend to sort of degenerate into madness.
*  You didn't have good editors or code exploration tools.
*  So you would wind up fixing things in one place, add a little patch.
*  And there's reasons why structured programming generally helps understanding.
*  But Go tos aren't poisonous.
*  Sometimes they're the right thing to do.
*  Usually it's because there's a language feature missing like nested breaks or something where it can sometimes be better to do a Go to clean up or Go to error rather than having multiple flags, multiple if statements littered throughout things.
*  But it is rare.
*  If you grep through all of my code right now, I don't think any of my current code bases would actually have a Go to.
*  But deep within sort of the technical underpinnings of a major game engine, you're going to have some Go tos in a couple of places probably.
*  Yeah, the infrastructure on top of like the closer you get to machine code, the more Go tos you're going to see, the more of these like hacks you're going to see because the set of features available to you in low level programming languages is not is limited.
*  So print John Carmack, when is the first time if we could talk about love that you fell in love with programming?
*  You said like this, this is really something special.
*  It really was something that was one of those love at first sight things where just really from the time that I understood what a computer was, even I mean, I remember looking through old encyclopedias at the black and white photos of the IBM mainframes at the reel to reel tape decks.
*  And for people nowadays, it can be a little hard to understand what the world was like then from information gathering, where I would go to the libraries and there would be a couple books on the shelf about computers and they would be very out of date even at that point.
*  Just not a lot of information, but I would grab everything that I could find and devour everything.
*  Whenever Time or Newsweek had some article about computers, I would cut it out with scissors and put it somewhere.
*  It just it felt like this magical thing to me, this idea that the computer would just do exactly what you told it to.
*  I mean, and there's a little bit of the genie monkey's paw sort of issues there where you'd better be really, really careful with what you're telling it to do.
*  But it wasn't going to backtalk you.
*  It wasn't going to have a different point of view.
*  It was going to carry out what you told it to do.
*  And if you had the right commands, you could make it do these pretty magical things.
*  And so what kind of programs did you write at first?
*  So beyond the print, John Carmack.
*  So I can remember as going through the learning process where you find at the start, you're just learning how to do the most basic possible things.
*  And I can remember stuff like a Superman comic that Radio Shack commissioned to have.
*  It's like Superman had lost some of his super brain and kids had to use Radio Shack TRS-80 computers to do calculations for it to help him kind of complete his heroics.
*  And I'd find little things like that and then get a few basic books to be able to kind of work my way up.
*  And again, it was so precious back then.
*  I had a couple books that would teach me important things about it.
*  I had one book that I could start to learn a little bit of assembly language from, and I'd have a few books on basic and some things that I could get from the libraries.
*  But my goals in the early days was almost always making games of various kinds.
*  I loved the arcade games and the early Atari 2600 games, and being able to do some of those things myself on the computers was very much what I aspired to.
*  And it was a whole journey where if you learn normal basic, you can't do any kind of an action game.
*  You can write an adventure game. You can write things where you say, what do you do here?
*  Get sword, attack troll, that type of thing.
*  And that can be done in the context of basic.
*  But to do things that had moving graphics, there were only the most limited things you could possibly do.
*  You could maybe do breakout or pong or that sort of thing in low resolution graphics.
*  And in fact, one of my first sort of major technical hacks that I was kind of fond of was on the Apple II computers.
*  They had a mode called low resolution graphics, where of course all graphics were low resolution back then.
*  But regular low resolution graphics, it was a grid of 40 by 40 pixels normally, but they could have 16 different colors.
*  And I wanted to make a game kind of like the arcade game Vanguard, just a scrolling game.
*  And I wanted to just kind of have it scroll vertically up.
*  And I could move a little ship around. You could manage to do that in basic, but there's no way you could redraw the whole screen.
*  And I remember at the time just coming up with what felt like a brainstorm to me, where I knew enough about the way the hardware was controlled,
*  where the text screen and the low resolution graphics screen were basically the same thing.
*  And all those computers could scroll their text screen reasonably.
*  You could do a listing and it would scroll things up.
*  And I figured out that I could kind of tweak just a couple things that I barely understood to put it into a graphics mode.
*  And I could draw graphics and then I could just do a line feed at the very bottom of the screen.
*  And then the system would scroll it all up using an assembly language routine that I didn't know how to write back then.
*  So that was like this first great hack that sort of had analogs later on in my career for a lot of different things.
*  So I found out that I could draw a screen, I could do a line feed at the bottom, we would scroll it up once.
*  I could draw a couple more lines of stuff at the bottom.
*  And that was my first way to kind of scroll the screen,
*  which was interesting in that that played a big part later on in the id software days as well.
*  So do efficient drawing where you don't have to draw the whole screen,
*  but you draw from the bottom using the thing that was designed in the hardware for text output.
*  Yeah. Where so much of, until recently, game design was limited by what you could actually get the computer to do.
*  Where it's easy to say, like, OK, I want to scroll the screen.
*  You just redraw the entire screen at a slight offset.
*  And nowadays that works just fine. Computers are ludicrously fast.
*  But up until a decade ago or so, there were all these things everybody wanted to do.
*  But if they knew enough programming to be able to make it happen, it would happen too slow to be a good experience,
*  either just ridiculously slow or just slow enough that it wasn't fun to experience it like that.
*  So so much of kind of the first couple decades of the programming work that I did was largely figuring out how to do something that everybody knows how they want it to happen.
*  It just has to happen two to ten times faster than sort of the straightforward way of doing things would make it happen.
*  And it's different now because at this point, lots of things you can just do in the most naive possible way.
*  And it still works out. You know, you don't have nearly the creative limitations
*  or the incentives for optimizing on that level. And there's a lot of pros and cons to that.
*  But I do generally, you know, I'm not going to do the the angry old man shaking my fist at the clouds bit where back in my day programmers had to do real programming.
*  It's it's amazing that you can just kind of pick an idea and go do it right now.
*  And you don't have to be some assembly language wizard or deep GPU arcanist to be able to figure out how to make your wishes happen.
*  Well, there's still see that's true.
*  But let me put on my old man with a fist hat and say that probably the thing that will define the future still requires you to operate at the limits of the current system.
*  So we'll probably talk about this.
*  But if you talk about building the metaverse and building a VR experience that's compelling, it probably requires you to not to go to assembly or maybe not literally,
*  but sort of spiritually to go to the limits of what the system is capable of.
*  And that really was why virtual reality was specifically interesting to me, where it had all the ties to you could say that even back in the early days,
*  I have some old magazine articles that's talking about doom as a virtual reality experience back when just seeing anything in 3D.
*  So you could say that we've been trying to build those virtual experiences from the very beginning.
*  And in the modern era of virtual reality, especially on the mobile side of things, when it's standalone,
*  you're basically using a cell phone chip to be able to produce these very immersive experiences.
*  It does require work.
*  It's not at the level of what an old school console game programmer would have operated at where you're looking at hardware registers and you're scheduling all the DNA accesses.
*  But it is still definitely a different level than what a web developer or even a PC Steam game developer usually has to work at.
*  And again, it's great.
*  There's opportunities for people that want to operate either into that spectrum there and still provide a lot of value to the world.
*  Let me ask you sort of a big question about preference.
*  What would you say is the best programming language?
*  Your favorite, but also the best you've seen throughout your career.
*  You're considered by many to be the greatest programmer ever.
*  I mean, it's so difficult to place that label on anyone.
*  But if you put it on anyone, it's you.
*  So let me ask you these kind of ridiculous questions of what's the best band of all time.
*  But in your case, what's the best programming language?
*  Everything has all the caveats about it.
*  So what I use so nowadays I do program a reasonable amount of Python for AIML sorts of work.
*  That's I'm not a native Python programmer.
*  It's something I came to very late in my career.
*  I understand what it's good for.
*  You don't dream in Python.
*  I do not.
*  And it has some of those things where there are some amazing stats.
*  When you say if you just start if you make a loop, you know, a triply nested loop and start doing operations in Python,
*  you can be thousands to potentially a million times slower than a proper GPU tensor operation.
*  And these are staggering numbers.
*  You know, you can be as much slower as we've almost gotten faster in our pace of progress and all this other miraculous stuff.
*  So your intuitions about inefficiencies within the Python sort of keeps hitting me upside the face where it just it's gotten to the point.
*  Now I understand it's like, OK, you just can't do a loop if you care about performance in Python.
*  You have to figure out how you can reformat this into some big vector operation or something that's going to be done completely within a C++ library.
*  But the other hand is it's it's amazingly convenient.
*  And you just see stuff that people are able to cobble together by you just import a few different things and you can do stuff that nobody on Earth could do 10 years ago.
*  And you can do it in a little cookbook thing that you copy paste it out of a website.
*  So that is really great.
*  When I'm sitting down to do what I consider kind of serious programming, it's still in C++.
*  And it's really kind of a C flavored C++ at that where I'm not big into the modern template metaprogramming sorts of things.
*  I see a lot of train wrecks coming from some of that over abstraction.
*  I spent a few years really going kind of deep into the kind of the historical Lisp work and the Haskell and some of the functional programming sides of things.
*  And there's there is a lot of value there in the way you think about things.
*  And I changed a lot of the way I write my C and C++ code based on what I learned about the value that comes out of not having this random mutable state that you kind of lose track of.
*  Because something that many people don't really appreciate till they've been at it for a long time is that it's not the writing of the program initially.
*  It's the whole lifespan of the program.
*  And that's when it's not necessarily just how fast you wrote it or how fast it operates, but it's how can it bend and adapt as situations change.
*  And then the thing that I've really been learning in my time at Meta with the Oculus and VR work is it's also how well it hands off between the continuous kind of revolving door programming.
*  And how the programmers taking over maintenance and different things and how you get people up to speed in different areas.
*  And there's all these other different aspects of it.
*  So C++ is a good language for handover between engineers.
*  Probably not the best.
*  And there's some really interesting aspects to this where in some cases languages that are not that are not generally thought well of for many reasons like C is derided pretty broadly that yes,
*  obviously all of these security flaws that happen with the memory and unsafeness and buffer overruns and the things that you've got there.
*  But there is this underappreciated aspect to the language is so simple anyone can go and if you know C you can generally jump in someplace and not have to learn what paradigms they're using because there just aren't that many available.
*  I think there's some really, really well written C code.
*  I think it's I find it great that if I'm messing around with something in OpenBSD say I mean I can be walking around in the kernel and I'm like I understand everything that's going on here.
*  It's not hard for me to figure out what's I you know what I need to do to make whatever change that I need to while you can have more significant languages like the downside of Lisp where I don't regret the time that I spent with Lisp.
*  I think that it I it did help you know help my thinking about programming in some ways.
*  But the people that are the biggest defenders of Lisp are saying how malleable of a language it is that if you write a huge list program you've basically invented your own kind of language and structure because it's not the primitives of the language you're using very much.
*  It's all of the things you've built on top of that.
*  And then a language like Racket kind of one of the more modern Lisp versions.
*  It's essentially touted as a language for building other languages and I understand the value of that for a tiny little project.
*  But the idea of that for one of these long term supported by lots of people kind of horrifies me where all of those abstractions that you're like OK you can't touch this code till you educate yourself on all of these things that we've built on top of that.
*  And it was interesting to see how when Google made go a lot of the criticisms of that are it's like wow this is not a state of the art language.
*  This language is just so simple and almost crude and you could see the programming language people just looking down at it.
*  But it does seem to be quite popular as basically saying this is the good things about C.
*  Everybody can just jump right in and use it.
*  You don't need to restructure your brain to write good code in it.
*  So I wish that I had more opportunity for doing some work in go.
*  Rust is the other modern language that everybody talks about that I'm not fit to pass judgment on.
*  I've done a little bit beyond Hello World.
*  I wrote some like video decompression work in Rust just as an exercise.
*  But that was a few years ago and I haven't really used it since.
*  You know the best programming language is the one that works generally that you're currently using because that's another trap is in almost every language.
*  In almost every case I've seen when people mixed languages on a project.
*  That's a mistake.
*  I would rather stay just in one language so that everybody can work across the entire thing.
*  And we have like it.
*  Meta we have a lot of projects that use kind of react framework.
*  So you've got JavaScript here and then you have C plus plus for real work and then you may have Java interfacing with some other part of the Android system.
*  And those are all kind of horrible things.
*  And that was one thing that I remember talking with with Boz at Facebook about it where like man I wish we could have just said we're only hiring C plus plus programmers.
*  I am and he just thought from the from the Facebook meta perspective what we just wouldn't be able to find enough.
*  I you know with the thousands of programmers they've got there it is not necessarily a dying breed but you can sure find a lot more Java JavaScript programmers.
*  And I kind of mentioned that to Elon one time and he was kind of flabbergasted about that.
*  It's like well you just you go out and you find those programmers and you don't hire the other programmers that don't do the languages that you want to use.
*  But right now I guess they're using JavaScript on a bunch of the SpaceX work for the UI side of things when you go find UI programmers their JavaScript programmers.
*  I wonder if that's because there's a lot of JavaScript programmers because I do think that great programmers are rare that it's not you know if you just look at statistics of how many people are using different programming languages that doesn't tell you the story of what the great programmers are using.
*  And so you have to really look at what you were speaking to which is the fundamentals of a language.
*  What does it encourage you how does it encourage you to think what kind of systems does it encourage you to build.
*  There is something about C++ that has elements of creativity but forces you to be an adult about your programming.
*  It expects you to be an adult.
*  It's not worse you do.
*  And so it brings out people that are willing to be creative in terms of building large systems and coming up with interesting solutions but at the same time have the sort of the good software engineering practices that amend themselves to real world systems.
*  Let me ask you about this other language JavaScript.
*  So if we you know aliens visit in thousands of years and humans are long gone something tells me that most of the systems they find will be running JavaScript.
*  I kind of think that if the simulator for living this simulations really it's written in JavaScript.
*  JavaScript.
*  You know for the longest time even still JavaScript didn't get any respect.
*  And yet it runs so much of the world and an increasing number of the world is it possible that all everything will be written in JavaScript one day.
*  So the engineering under JavaScript is really pretty phenomenal.
*  The systems that make JavaScript run as fast as it does right now are kind of miracles of modern engineering in many ways.
*  It does feel like it is not an optimal language for all the things that it's being used for or an optimal distribution system to huge to build huge apps in something like this without type systems and so on.
*  But I think for a lot of people it does reasonably the necessary things.
*  It's still a sea flavored language.
*  It's still a braces and semicolon language.
*  It's not hard for people to be trained in JavaScript and then understand the roots of where it came from.
*  I think garbage collection is unequivocally a good thing for most programs to be written in.
*  It's funny that I still just this morning I was on I was seeing a Twitter thread of a bunch of really senior game dev people arguing about the virtues and costs of garbage collection.
*  You will run into some people that are top notch programmers that just say no this is literally not a good thing.
*  Because it makes you lazy.
*  Yes.
*  That it makes you not think about things.
*  And I do disagree.
*  I think that there is so much objective data on the vulnerabilities that have happened in C and C++ programs sometimes written by the best programmers in the world.
*  It's like nobody is good enough to avoid ever shooting themselves in the foot with that you write enough C code.
*  You're going to shoot yourself in the foot.
*  And garbage collection is a very great thing for the vast majority of programs.
*  It's only when you get into the tightest of real time things that you start saying it's like no the garbage collection has more costs than it has benefits for me there.
*  But that's not 99 plus percent of all the software in the world.
*  So JavaScript is not terrible in those ways.
*  And I am and so much of programming is not the language itself.
*  It's the infrastructure around every you know that surrounds it all the libraries that you can get and the different stuff that you can ways you can deploy it.
*  I am the portability that it gives you.
*  And JavaScript is really strong on a lot of those things where for a long time and it still does if I look at it.
*  But the web stack about everything that has to go when you do something really trivial in JavaScript and it shows up on a web browser to kind of X ray through that and see everything that has to happen for your one little JavaScript.
*  Statement to turn into something visible in your web browser.
*  It's very, very disquieting just the depth of that stack and the fact that so few people can even comprehend all of the levels that are going on there.
*  But it's again I have to caution myself to not be the in the good old days old man about it because clearly there's enormous value here.
*  The world does run on JavaScript to a pretty good approximation there and it's not falling apart.
*  There's a bunch of scary stuff where you look at console logs and you just see all of these bad things that are happening but it's still kind of limping along and nobody really notices.
*  But so much of my systems design and systems analysis goes around.
*  You should understand what the speed of light is like what would be the best you could possibly do here.
*  And it sounds horrible but in a lot of cases you can be a thousand times off your speed of light velocity for something and it's still be okay and in fact it can even sometimes still be the optimal thing in a larger system standpoint where there's a lot of things that you don't want to have to parachute in someone like me to go in and say make this.
*  This web page run a thousand times faster you know make this web app into a hardcore native application that starts up in thirty seven milliseconds and everything responds in less than one frame latency that's just not necessary and if somebody wants to go pay me millions of dollars to do software like that when they can take somebody right out of a boot camp and say spin up an application for this.
*  Often being efficient is not really the best metric and it's like there's that applies in a lot of areas where it's kind of interesting how a lot of our appliances and everything are all built around energy efficiency sometimes at the expense of robustness in some other ways or higher costs in other ways where there's interesting things where energy or electricity could become much cheaper in a future world and that could change our engineering trade-offs for the way we build certain things where we can actually
*  get more benefits that actually matter. That's one of my you know I one of the directions I was considering swerving into was nuclear energy when I was kind of like what do I want to do next it was either going to be cost-effective nuclear fission or artificial general intelligence and one of the one of my pet ideas there is like you know people don't understand how cheap nuclear fuel is and there would be ways that you know people would be able to get more
*  high you could be a quarter the efficiency or less but if it wound up making your plant 10 times cheaper that could be a radical innovation and something like that so there's like some of these thoughts around like direct fission for energy conversion fission fragment conversion that
*  you know maybe you build something that doesn't require all the steam turbines and everything even if it winds up being less efficient so that applies a lot in programming where
*  There's always it's always good to know what you could do if you really sat down and took it took it far because sometimes there's discontinuities like around user reaction times there are some points where the difference between operating in one second and 750 milliseconds I not that huge you'll see it in web page statistics but most usability stuff not that great but if you get down to 50 milliseconds then all of a sudden this just feels amazing you know it's just like doing your bidding instantly rather than
*  you're giving it a command twiddling your thumbs waiting for it to respond so sometimes it's important to really crunch hard to get over some threshold but there are there are broad basins in the value metric for lots of work where it just doesn't pay to even go that extra mile
*  And their craftsman that you know they just don't want to buy that and more power to them you know if somebody just wants to say no I'm going to be I'm my pride is in my work I'm never going to do something that's not as good as I could possibly make it I respect that and sometimes I am that person but I try to focus more on the larger value picture and you do pick your battles and you deploy your resources in the play that's going to give you sort of the best user value in the end
*  Well if you look at the evolution of life on earth as a kind of programming effort it's it seems like efficiency isn't the thing that's being optimized for like natural selection is very inefficient but it kind of adapts and through the process of adaptations building more and more complex systems that are more and more intelligent the final result is kind of pretty interesting and so I think of JavaScript the same way
*  It's like this giant mess that you know things naturally die off if they don't work and they if they if they're become useful to people they kind of naturally live and then you build this community large community of people that are generating code and some code is sticky some is not and nobody knows the
*  The inefficiencies of the efficiencies or the breaking points like how reliable this code is and you kind of just run it assume it works and then get unpleasantly surprised and then that's very kind of the evolutionary process
*  So that's a really good analogy and we can go a lot of places with that where in the earliest days of programming when you had finite you could count the bytes that you had to work on this you had all the kind of hackers playing code golf to be one less instruction than the other person's multiply routine to kind of get through and it was so perfectly crafted it was a crystal piece of artwork when you had a program
*  Because there just were not that many you couldn't afford to be lazy in different ways and in many ways I see that as akin to the symbolic I work where again if you did not have the resources to just say well we're gonna do billions and billions of programmable weights here you have to turn it down into something that is symbolic and crafted like that but that's definitely not the way DNA and life and biological evolution and things work I know on the one hand it's.
*  It's almost humbling how little programming code is in our bodies you know we've got a couple billion base pairs and it's like this all fits on the thumb drive for years now and then our brains are even a smaller section of that you got maybe fifty megabytes and this is not like Shannon limit perfectly information dense.
*  Conveyance is here it's like these are messy codes you know they're broken up into amino acids a lot of them don't do important things or they do things in very awkward ways.
*  What is this process of just accumulation on top of things and you need.
*  You need scale both you need scale for the population for that to work out and in the early days in the fifties and sixties the kind of ancient era of computers where you could count when they say like when the internet started even in the seventies there are eighteen hosts or something on it was this small finite number.
*  And you were still optimizing everything to be as good as you possibly could be but now it's billions and billions of devices and everything going on and you can have this very much natural evolution going on where.
*  Lots of things are tried lots of things are blowing up venture capitalists lose their money on I when a startup invested in the wrong tech stack and things completely failed or fail the scale.
*  But you know but good things do come out of it and it's interesting to see the the mimetic evolution of the way different things happen like mentioning hello world at the beginning it's funny how some little thing like that where everybody every programmer knows hello world now and that was a completely arbitrary sort of decision that just came out of the dominance of unix and see an early examples of things like that so.
*  Millions of experiments are going on all the time but some things do kind of rise to the top and win the fitness war for whether it's mine space or programming techniques or anything like there's a site on stack exchange called.
*  Code golf where people compete to write the shortest possible program for particular task in all the different kinds of languages and it's really interesting to see.
*  Folks kind of.
*  Their masters of their craft really play with the limits of programming languages it's really beautiful to see and across all the different programming languages you get to see.
*  Some of these weird programming languages and mainstream ones difference between python two and three you get to see the difference between cnc plus plus and java and you get to see javascript all of that and it's kind of.
*  Inspiring to see how much depth of possibility there is within programming languages that code golf kind of tasks reveal most of us if you do any kind of programming you kind of do boring kind of.
*  Very vanilla type of code that's the way to build large systems but it's nice to see that the possibility of creative genius is still within those languages it's.
*  Given that given that you are once again one of the greatest programmers ever what do you think makes a good programmer maybe a good modern programmer.
*  So I just gave a long rant slash lecture at meta to the TPM organization and my my biggest point was everything that we're doing really should flow from user value you know and I think that's the biggest thing that we're doing.
*  Point was everything that we're doing really should flow from user value you know all the good things that we're doing it's like we're we're not technical people it's like.
*  You shouldn't be taking pride just in the specific thing like code golf is the sort of thing it's a fun puzzle game but that really should not be a major motivator for you.
*  It's like we're solving problems for people are we're providing entertainment to people were doing something of value to people that's displacing something else in their life so we want to be providing a net value over what they could be doing.
*  I but instead they're choosing to use our products and that's where it sounds trider corny but I fundamentally do think that's how you make the world a better place if you have given more value to people than it took you and your team to create.
*  Then the world's a better place people have I've they've gone from something of lesser value chosen to use your product and their life feels better for that and if you produce that economically that's that's a really good thing.
*  I'm on the other hand if you spent ridiculous amounts of money you just kind of shoveled a lot of cash into a wood chipper there and you should maybe you know not feel so good about what you're doing so.
*  Being proud about like a specific architecture specific technology or specific code sequence that you've done it's great to get a little smile like tiny little dopamine hit for that but the top level metrics should be that you're building things of value.
*  Now you can get in the argument about how you know what is user value how do you actually quantify that and there can be big arguments about that but it's easy to be able to say okay this pissed off user there is not getting value from what you're doing
*  this user over there with a big smile on their face i am the moment of delight when something happened there's a value that happened there i mean if you have to at least accept that there is a concept of user value even if you have trouble exactly quantifying it
*  you can usually make relative arguments about it well this was better than this we've improved things so you know being a.
*  No being a servant to the user is your job when you're doing when you're a developer you want to be producing something that i have other people are going to find valuable.
*  And if you are technically inclined then finding the right levers to be able to pull to be able to make a design that's going to produce the most value for the least amount of effort and it always has to be i kind of divide the ratio there where you.
*  It's a problem at the big tech companies you know whether it's meta google apple microsoft amazon companies that have almost infinite money i mean i know.
*  Their cfo will complain that it's not infinite money but from most developer standpoint it really does feel like it and it's almost counterintuitive that.
*  If you're working hard as a developer on something there's always this thought if only i had more resources more people more ram more megahertz i then by product will be better and that sense that.
*  At certain points it's certainly true that if you are really hamstrung by this removing an obstacle will will make a better product make more value.
*  What if you're not making your core design decisions in this fiercely competitive high way where you're saying feature a or feature b you can't just say let's do both.
*  I because then you're not making a value judgment about them you're just saying well they both seem good i don't want to necessarily have to pick out which one is better how much better and tell team be that i'm sorry we're not gonna do this because a is more important.
*  But that i am that notion of always having really critically value what you're doing your time the resources you expand even the opportunity cost of doing something else that's you know super important.
*  What is your about this the big debates that you're mentioning of how to measure value.
*  Is it possible to measure it kind of.
*  Numerically.
*  Or can you do this sort of johnny i've the designer route of imagining.
*  Sort of somebody using a thing and imagining a smile on their face imagining the experience of love and joy that you have when you use the thing that's from a design perspective or if you're building more like a low lower level thing for like linux you imagine a developer that might come across this and use it and become.
*  Happy and better off because of it so where do you land on those things is a measurable so i imagine like meta and google will probably try to measure the thing they'll try to it's like you try to optimize engagement or something let's measure engagement and then i think there is a kind of.
*  I mean i admire the designer ethic of like think of a future is this immeasurable and you try to make somebody in that future that's different from today happy.
*  So i do usually favor if you can get any kind of a metric that's good by all means listen to the data but you can go too far there where we've had problems where it's like hey we had a performance regression because our.
*  Fancy new telemetry system is doing a bazillion file rights i had to kind of archive this stuff because we needed to collect information to determine if we were doing you know if our plans were good so when information is available you should never ignore it i mean all the actual users using the thing
*  human beings using the thing large number of human beings and you get to see sort of at one problem of when you're doing something really new you do kind of have to make a guess but
*  one of the points that i've been making it meta is we have more than enough users now that anything somebody wants to try in vr we have users that will be interested in that you do not get to make a completely greenfield blue sky pitch and say i'm going to do this because i think it might be interesting i challenge everyone
*  There are going to be people whether it's you know working in vr on your i am i like on your desktop replacement or communicating with people in different ways or playing the games.
*  There are going to be probably millions of people or at least in the if you pick some tiny niche that we're not in right now there's still going to be thousands of people out there that have the headsets
*  That would be your target market and i tell people pay attention to them don't invent fictional users don't you know make an alice bob charlie i that fits whatever matrix of tendencies that you want to break the market down to because it's a mistake to think about imaginary users when you've got real users that you could be working with.
*  But you know on the other hand there is there is value to having a kind of wholeness of vision for a product and i'm companies like meta have.
*  You know they understand the trade-offs where you can have a company like space x or apple and the steve jobs era where you have a very powerful leading personality that high
*  you know they can micromanage at a very low level and can say it's like no that handle needs to be different or that i that icon needs change the tent there
*  and they clearly get a lot of value out of it they also burn through a lot of employees that have a horror stories to tell about working there afterwards.
*  My position is that you're at your best when you got a leader that is at their limit of what they can kind of comprehensive everything below them i and they can have an informed opinion about everything that's going on
*  can you take somebody it's you gotta believe that somebody that has thirty forty years of experience
*  You would hope that they've got wisdom that the just out of boot camp person i contributing doesn't have and that if they're like well that's wrong there you probably shouldn't do it that way or even just don't do it that way do it another way.
*  So there's value there but it can't go beyond a certain level i am i have steve jobs stories of him saying things that are just wrong right in front of me about technical things because he was not operating at that level.
*  What when it does work and you do get that kind of passionate leader that's thinking about the entire product and just really deeply cares about not letting anything slip through the cracks.
*  I think that's got a lot of value but the other side of that is the people saying that well we want to have these independent teams that are bubbling up the ideas because i like it's almost anti capitalist anti free market to say it's like i want my grand my great leader to go ahead and dictate all these points there were
*  clearly free markets bring up things that you don't expect like in vr we we saw a bunch of things like it didn't turn out at all the way the early people thought we're gonna be the key applications and things that you would not have been approved by
*  you know the dark cabal making the decisions about what gets into the store turnout did some cases be extremely successful so.
*  Yeah i definitely kind of wanted to be there's a point where i did make a pitch it's like hey make me vr dictator and i'll go in get shit done i am and that's just it's not in the culture and meta you know and they they understand the trade offs they i and that's just not the way that's not the company that they want the team that they that they want to do.
*  It's fascinating because vr and we'll talk about it more it's still it's still unclear to me.
*  In what way vr will change the world because it does seem clear that vr will somehow fundamentally transform this world and it's unclear to me how yeah and it's let me know when you want to get into that.
*  Who will hold on a second so in the stick to the you being the best programmer ever okay in the early days when you didn't have when you didn't have adult responsibilities of leading teams and all that kind of stuff and you can focus on just.
*  Being a programmer what did the productive day in the life of john karmak look like how many hours of the keyboard how much sleep what was the source of calories that fueled the brain.
*  What was it like what times you wake up.
*  So i was able to be remarkably consistent about what was good working conditions for me for a very long time.
*  I was never one of the programmers that i that would do all nighters going through work for 20 hours straight it's like my brain generally starts turning to mush after 12 hours or so.
*  I am but the hard work is really important and i would work for decades i would work 60 hours a week i would work a 10 hour day 6 days a week and try to be productive at that.
*  Now my schedule shifted around a fair amount when i was young without any kids i am any other responsibilities i was on one of those cycling schedules where i'd kind of get in an hour later each day and roll around through the entire time and.
*  I'd wind up kind of pulling in at two or three in the afternoon sometimes and then working again past midnight or two in the morning and that was i am.
*  When it was just me trying to make things happen i am and i was usually isolated off in my office people generally didn't bother me much i added and i could get a lot of programming work done that way.
*  I did settle into a more normal schedule when i was taking kids to school and things like that.
*  So kids were the forcing function that got you wake up at the same time.
*  It's not clear to me that there was a much of a difference in the productivity with i with that where i kind of feel if i just get up when i feel like it it's usually a little later each day but.
*  I just recently made the focusing decision to try to push my schedule back a little bit earlier to getting up at eight in the morning and trying to to shift things around like i'm.
*  I'm often doing experiments with myself about what should i be doing to to be more productive and one of the things that i did realize was happening in recent months where.
*  I would i would go for a walk or a run i cover like four miles a day and.
*  And i would usually do that just as the sun's going down at here in texas now and it's still really damn hot but i'd go out at eight thirty or something and.
*  Cover the time there and then the showering and it was putting a hole in my day where i would have still a couple hours after that sometimes my best hours were at night when nobody else is around nobody's bothering me.
*  What that hole in the day was a problem so just a couple weeks ago i made the change to go ahead and say alright i'm gonna get up a little earlier i'm gonna do a walker get out there first so i can have more uninterrupted time so i'm still playing with factors like this as i kind of optimize my.
*  My work efforts but it's always been.
*  It was sixty hours a week for a very long time to some degree i had a little thing in the back of my head where i was almost jealous of some of the programmers that would do these marathon sessions and i had like dave taylor one of the guys that he had he would be one of those people that would fall asleep under his desk sometimes all the the kind of classic hacker tropes about things and.
*  A party was like always a little bothered that that wasn't me that i wouldn't go program.
*  Twenty hours straight because i just i'm falling apart not being very effective after twelve hours i mean yeah i can't programing that's fine when you're doing that but.
*  It never you're not doing smart work much after at least i'm not but there's a range of people and that's something that a lot of people don't.
*  Really get in their gut where there are people that work on four hours of sleep and are smart and can continue to good work but then there's a lot of people that just fall apart.
*  So i do tell people that i always try to get eight hours of sleep it's not this you push yourself harder get up earlier i just do worse work where.
*  I know there's you can work a hundred hours a week and still get eight hours of sleep if you just kind of prioritize things correctly but i do believe in working hard working a lot i am.
*  There was a comment that game dev made that.
*  That i know there's a backlash against really hard work in a lot of cases and i get into online arguments about this all the time but it was basically saying yeah forty hours a week that's kind of a part time job and.
*  If you are really in it you're doing what you think is important what you're passionate about working more gets more done and i it's just really not.
*  Possible to argue with that if you've been around the people that that work with that level of intensity and just say it's like no they should just stop and we had.
*  I kind of came back around to that a couple years ago where i was using the fictional example of.
*  Alright some people say they'll say with a straight face i think no you you are less productive if you work more than forty hours a week.
*  And they're generally misinterpreting things where your your marginal productivity for an hour after eight hours is less than in one of your peak hours but you're not literally getting less done there is a point where you start breaking things and getting worse.
*  Worse behavior and everything out of it where you're literally going backwards but it's not an eight or ten or twelve hours and the fictional example i would use was imagine there's an asteroid.
*  Coming to impact you know to crash into earth destroy all of human life i do you want.
*  Elon musk or the people working at space x that are building the interceptor that's going to to deflect the asteroid do you want them to clock out at five because damn it they're just gonna go do worse work if they work another couple hours and you know it seems absurd.
*  Add that the hypothetical though and everyone can dismiss that but then when coronavirus was hitting and you have all of these medical personnel that are clearly pushing themselves really really hard.
*  And i'd say it's like okay do you want all of these scientists working on treatments and vaccines and caring for all of these people are they really screwing everything up by working more than eight hours a day.
*  And of course people say i'm just an asshole to say something like that but it's i know it's the truth working longer gets more done.
*  What so that's kind of the layer one but i'd like to also say that.
*  At least i believe depending on the person depending on the task working more and harder will make.
*  You better for the for the next week in those peak hours so there's something about a deep dedication to a thing.
*  That's kind of gets deep in you so the hard work isn't just about the raw hours of productivity it's the.
*  It's the thing it does to you in the in the weeks and months after to your tempering yourself in some ways.
*  And i think you know it's like your dreams of sushi if you really dedicate yourself completely to making the sushi like to really putting in the long hours day after day after day.
*  You become a true craftsman of the thing you're doing now there's of course discussions about are you sacrificing a lot of personal relationships are you sacrificing a lot of other possible.
*  Things you could do with that time but if you're talking about purely being a master or craftsman of your art that's more hours isn't just about.
*  Doing more it's about becoming better at the thing you're doing and i don't gain say anybody that wants to work the minimum amount they've got other priorities in their life my only argument that i'm making it's not that everybody should work hard.
*  It's that if you want to accomplish something working longer and harder is the path to getting it accomplished.
*  Let me ask you about this then why the mythical work life balance.
*  Is the foreign engineer it seems like that's one of the professions in the for programmer where.
*  Working hard does lead to greater productivity in it but it also raises the question of.
*  What is personal relationships and all that kind of stuff family and.
*  How are you able to find work life balance is there advice you can give maybe even outside yourself have you been able to arrive at any wisdom on this part in your so years of life i do think that there's a wide range of people where different people have different needs it's not a one size fits all i am certainly what works for me i can tell enough that.
*  I'm you know i'm different than a typical average person in the way things impact me that you know the things that i want to do my goals are different and sort of the levers to impact things are different where.
*  No i have literally never felt burn out and i know there's lots of brilliant smart people that that do world leading work that get burned out and it's never hit me i'm you know i've never been at a point where.
*  I'm like i'm i just don't care about this i don't want to do this anymore but i've always had the flexibility to work on lots of interesting things you know i can always just turn my gaze to something else and have a great time working on that and so much of that.
*  So much of the ability to actually work hard is the ability to have multiple things to choose from and to use use your time on the most appropriate thing like there are.
*  There are time periods where i am it's the best time for me to read a new research paper that i need to really be thinking hard about it then there's a time that maybe i should just scan and organize my old notes because my i'm just not on top of things then there's the time that alright let's go.
*  You know bang out a few hundred lines of code for something so switching between them has been real valuable.
*  So you always have kind of join your heart for all the things you're doing and that that is the kind of work life balance as a first sort of step yeah i do you're always happy i do.
*  While happy yeah i mean that's like i a lot of people would say that often i look like kind of a grim person you know with just sitting there with a neutral expression or even like knitted brows and a frown on my face as i'm staring at something.
*  That's what happiness looks like for you.
*  Yeah it's it's kind of true where that that's like okay i'm pushing through this i'm making progress here i am you know i know that doesn't work for everyone i know it doesn't work for most people i am.
*  But what i am always trying to do in those cases is i don't want to let somebody that might be a person like that be told by someone else that no don't try it don't even try that out as an option where.
*  I have you know work life balance balance versus kind of your life's work where there's a small subset of the people that can be very happy being obsessive about things and you know obsession can often get things done that just practical prudent pedestrian work won't or at least won't for a very long time.
*  There's legends of your nutritional intake in the early days what can you say about sort of as a you know being a programmer as a kind of athlete so what what was the nutrition that fuels.
*  I have never been that great on I on really paying attention to it where i'm good enough that i don't eat a lot you know i've never been like a big heavy guy but.
*  It was interesting where one of the things that i can remember being an unhappy teenager not having enough money and like one of the things that bothered me about not having enough money is i couldn't buy pizza whenever i wanted to so i got rich and then i bought a whole lot of pizza.
*  That was defining like that's what being rich.
*  There was a lot of little things like i could buy all the pizza and comic books and video games that that i wanted to and it really didn't take that much but the pizza was one of those things and it's absolutely true that for a long time it did software.
*  I had a pizza delivered every single day you know the delivery guy knew me my name and i didn't find out until years later that apparently i was such a good customer that they just never raised the price on me and i was using this six year old price for the pizzas that they were still kind of sending my way every day.
*  So you were doing eating once a day or were you it would be spread out you know you have a few pieces of pizza you have some more later on and i'd maybe have something at home.
*  I it was one of the nice things that facebook meta is they do they feed you quite well you get a different i guess now it's door dash sorts of things delivered but they take care of making sure that everybody does get well fed and i probably had better food those.
*  Six years that i was working in the meta office there then i used to before but i it's worked out okay for me my health has always been good i get a pretty good amount of exercise and i don't eat to excess and i avoid a lot of other.
*  Kind of not so good for you things so i'm still doing quite well at my age did you have a.
*  I kind of i don't know spiritual experience with food or coffee or any of that kind of stuff i mean you know the programming experience you know with music and or or like i listen to brown noise on a program or like the creating an environment.
*  And the things you take into your body just everything you construct can become a kind of ritual that empowers the whole process the program did you have that relationship with pizza or.
*  It would really be with diet coke there still is that sense of you know drop the can down crack open the can of diet coke all right now i mean business we're getting to work here.
*  Still to this day is diet coke is still part yeah probably eight or nine a day.
*  Nice okay what about your setup how many screens what kind of keyboard is there something interesting what kind of i i d e e max vim or something modern.
*  Linux what operating system laptop or any interesting thing that brings you joy.
*  So i kind of migrated cultures where early on through all of game dev there was sort of one culture there which was really quite distinct from the more the silicon valley venture you know culture for things it's there different groups and they have pretty different mores and the way they think about things where.
*  And i still do think a lot of the big companies can learn i can learn things from the hardcore game development side of things where it still boggles my mind how.
*  I am how hostile to debuggers and i d e s that so much of them the kind of big money get billions of dollars silicon valley venture backed funds are.
*  All this is interesting sorry so you're saying like like big companies at google and meta are hostile to.
*  They are not big on debuggers and i d e s like so much of it is like e max vim for things and we just assume that debuggers don't work most of the time I have for the systems and a lot of this comes from a sort of Linux bias on a lot of things where.
*  I did come up through the personal computers and then the dos and then I am windows and and it was Borland tools and then visual studio and.
*  Do you appreciate the buggers.
*  Very much so i mean a debugger is how you get a view into a system that's too complicated understand i mean anybody that thinks just read the code and think about it.
*  That's an insane statement in the you can't even read all the code on a big system you have to do experiments on the system.
*  And doing that by adding log statements recompiling and rerunning it is an incredibly inefficient way of doing it i mean yes you can always.
*  Get things done even if you're working with stone knives and you know in bearskins that's that is the mark of a good programmer is that given any tools you will figure out a way to get it done.
*  What it's amazing what you can do with sometimes much much better tools where instead of just going through this iterative compile run debug cycle.
*  You have the you have the old list direction of like you got a rebel and you're working interactively and doing amazing things there but.
*  In many cases a debugger as a very powerful user interface that can stop examine all the different things in your program set all these different breakpoints and of course you can do that with gdb or whatever there but.
*  This is one of the user interface fundamental principles where when something is complicated to do you won't use it very often there's people that will break out gdb when they're at their wits end and they just have beat their head against a problem for so long.
*  But for somebody that kind of grew up in game dev it's like they were running into the debugger anyways before they even knew there was a problem and you would just stop and see you know what was happening and sometimes you could fix things even before you.
*  Even for you did one compile cycle you could be in the debugger and you'd say well i'm just going to change this right here and yep that did the job and fix it and go on and for people don't know gdb is a popular i guess linux debugger.
*  Of primarily for c++ they handle most of the languages but it's you know it's based on c as the original kind of unix heritage but in it's kind of like command line it's not user friendly it's not it doesn't allow for clean visualizations and you're exactly right so that you're using this kind of debugger usually.
*  When you're at wits end and there's a problem that you can't figure out why by just looking at the codes if to find it that's how I guess normal programmers use it but you're saying there should be tools that kind of.
*  Visualize and help you as part of the programming process just a normal programming process to understand the code deeper when i'm working on like my cc++ code i'm always running it from the debugger you know just i type in the code i i run it many times the first thing i do after writing code is.
*  Set a breakpoint and step through the function now other people say it's like oh i do that in my head well your head is a faulty interpreter of all those things there and i've written brand new code i want to step in there and i'm going to single step through that examine lots of things and see if it's actually doing what i expected it to.
*  It is a kind of companion the debugger like it you're you're now coding in an interactive way with another being a debugger is a kind of dumb being but reliable being that is an interesting question of what role does a i play in that kind of with codex and these kind of.
*  Ability to generate code that might be you might start having tools that understand the code in interesting deep ways that can work with you.
*  There's a whole spectrum there from static code analyzers and various kind of dynamic tools they're up to ai that can conceivably grok these programs that no he literally no human can understand their their too big to intertwine into interconnected
*  but it's not beyond the possibility of understanding it's just beyond what we can hold in our heads as kind of mutable state while we're working on things.
*  And i'm a big proponent again of things like static analyzers and some of that stuff where you'll find some people that don't like being scolded by a program for how they've written something where it's like oh i know better and sometimes you do but that was something that.
*  I was it was very very valuable for me when i'm not too many people get an opportunity like this to have this is almost one of those spiritual experiences as a programmer and awakening to.
*  I am the software code bases were a couple million lines of code and at one point i used a few of the different analysis tools but i made a point to really go through and scrub the code base using every tool that i could find.
*  And it was i opening where we had a reputation for having some of the most robust strongest code you know where there were some great things that i remember hearing from microsoft telling us about crashes on xbox and we had this tiny number that they said were
*  where probably literally hardware errors and then you have other significant titles that just have millions of faults that are getting recorded all the time so i was proud of our code on a lot of levels but when i took this
*  Code analysis squeegee through everything it was it was shocking how many errors there were in their things that you can say okay this was this was a copy paste not changing something right here lots of things that were the most the most common problem was something in a
*  Printf format string that was the wrong data type that could cause crashes there and you know you really want the warnings for things like that and the next most common was missing a check for null that could actually happen that could blow things up and those are obviously like top cc plus plus things everybody has those problems.
*  What the long tail of all of the different little things that could go wrong there and we had good programmers and my own code so that i be looking at it like oh i wrote that code that's definitely wrong we've been using this for a year and it's this
*  summary know this mine sitting there waiting for us to step on and it was humbling it was and i reach the conclusion that.
*  Anything that can be syntactically allowed in your language if i am.
*  It's gonna show up eventually in a large enough code base i you're not gonna good intentions aren't going to keep it from happening you need automated tools and guardrails for things and those start with things like static types and your even type hints in the more dynamic languages but.
*  The people that rebel against that that basically say that slows me down doing that there's something to that i get that i've written you know i cobbled things together in a notebook i
*  i'm like wow this is great that it just happened but yeah that's kinda sketchy but it's working fine i don't care it does come back to that that value analysis where sometimes it's right to not care.
*  But when you do care if it's going to be something that's going to live for years and it's gonna have other people working on it i and it's gonna be deployed to millions of people.
*  Then you wanna use all of these tools you wanna be told it's like no you screwed up here here and here and that does require kind of an ego check about things where you have to.
*  To be open to the fact that everything you're doing is just littered with flaws it's not that you occasionally have a bad day it's just whatever stream of code you output there's going to be a statistical regularity of things that you just make mistakes on.
*  And i am and i do think there's the whole argument about test driven design and unit testing versus kind of analysis and different things.
*  I am more in favor of the analysis and the stuff that just like you can't run your program until you fix this rather than you can run it and hopefully a unit test will catch it in some way.
*  Yeah in my private code I have asserts everywhere yeah it just there's something pleasant to me pleasurable to me about sort of the dictatorial rule of like this should be true at this point.
*  In too many times.
*  I've made mistakes that shouldn't have been made and I would assume I wouldn't be the kind of person would make that mistake but I keep making that mistake therefore and assert really catches me really helps all the time so my.
*  I would say like 10 to 20% of my private code just for personal use is probably asserts their active comments and one of those things that they don't.
*  They don't make any difference to the program and if it was all operating the way you expected it would be then I they will never fire but even if you have it right and you wrote the code right initially.
*  Then circumstances change the world outside your program changes and in fact that's that's one of the things where i'm kind of fond in a lot of cases of static array size declarations where i went through this period where it's like okay now we have general collection classes we should just make everything variable i
*  because i had this history of in the early days you get doom which had some fix limits on it then everybody started making crazier and crazier things and they kept bumping up the different limits this many lines this many sectors
*  I and it seemed like a good idea well we should just make this completely generic it can go kind of go up to whatever and.
*  There's cases where that's the right thing to do but it also the other aspect of the world changing around you is it's good to be informed when the world has changed more than you thought it would and if you got a continuously growing collection you're never going to find out you might have this quadratic slowdown on something where you thought oh I'm only ever going to have a handful of these.
*  But something changes and there's a new design style and all of a sudden you've got ten thousand of them so i kind of like in many cases.
*  Picking a number some nice brown power of two number and setting it up in there and having an assert saying it's like hey you hit the you hit this limit you should probably think are the choices that you've made around all of this still relevant if somebody's using ten times more than you thought they would.
*  Yeah this code was originally written with this kind of world view with this kind of set of constraints you were you were you were thinking of the world in this way if something breaks that means you got to rethink the initial stuff and that's it's nice for it to for for to do that is there any stuff like keyboard or.
*  Or monitor is fairly pedestrian on a lot of that where I I did move to triple monitors like in the last several years ago I had been dual monitor for a very long time and I am and it was one of those things where.
*  Probably years later than I should have I'm just like well the video cards now generally have three output ports I should just put the third monitor up there that's been a that's been a pure win I've been very happy with that.
*  I am but no I don't have fancy keyboard or mouse or anything really good things is an idea that has helpful debuggers has helpful tools does not the email and then die cook.
*  Yeah so I did spend you know I spent one of my week long retreats where I'm like okay I'm gonna make myself use I is actually classic VI which I know people will say you should never have done that you should just use them directly but.
*  You know I gave it the good try it's like okay I'm being in kind of classic Unix developer mode here and I worked for a week on it I used Anki to like teach myself the different little key combinations for things like that and in the end it was just like.
*  Alright this was kind of like my civil war reenactment phase you know it's like I'm going out there doing it like they used to in the old days and it was kind of fun in that regard so many people right now.
*  But it was screaming as they're listening to this again the out is this is not modern Vim but still I yes I was very happy to get back to my visual studio at the end yeah I'm actually I struggle with this a lot because.
*  So use a kinesis keyboard and I use emacs primarily.
*  And I feel like I can exactly as you said I can understand the code I can navigate the code there's a lot of stuff you could build with an emacs with using list you can customize a lot of things for yourself to help you.
*  Introspect the code like to help you understand the code and visualize different aspects of the call you can even run the buggers but it's it's work.
*  And the world moves past you and the better and better ideas are constantly being built and that that puts a kind of I need to take the same kind of retreat as you're talking about but now I'm still fighting the civil war I need to kind of move into the 21st century.
*  And it does seem like the world is or a large chunk of the world is moving towards visual studio code which is kind of interesting to me again it's the javascript ecosystem on the one hand and.
*  Ideas are one of those things that you want to be infinitely fast you want them to just kind of immediately respond.
*  And like I mean heck I've got there's someone I know I'm an old school game dev guy that still uses visual studio six and on a modern computer everything is just absolutely instant on something like that because it was made to work on a computer that's.
*  Ten thousand or a hundred thousand times slower so just everything happens immediately and all the modern systems just feel.
*  No they feel so crufty when it's like oh why is this refreshing the screen and moving around and updating over here and something blinks down there and you should update this and there's.
*  You know there there are things that we've lost with that incredible flexibility but.
*  Lots of people get tons of value from it and I am super happy that that seems to be winning over even a lot of the old them and he max people that they're kind of like.
*  A visual studio codes maybe you know not so bad I am that may be the final peacekeeping solution where everybody is reasonably happy with I with something like that.
*  So can you explain what a dot plan file is and what role that played in your life does it still continue to play a role.
*  Back in the early early days of it software i one of our big things it was unique with what we did is i had adopted next stations or kind of next step systems from i steve jobs is out in the woods away from apple company.
*  And i am they were basically it was kind of interesting because i did not really have a background with the unix system so many of the people they get i immersed in that in college and i am you know that's.
*  You know that sets a lot of cultural expectations for them and i didn't have any of that but i knew that.
*  My background was i was a huge apple to fanboy i am i was always a little suspicious of the mac i am was not really what i what kind of i wanted to go with.
*  When steve jobs left apple and started next this computer did just seem like one of those amazing things from the future where it had all of this cool stuff in it and we were still back in those days working on dos everything blew up you had reset buttons because your computer would just freeze if you doing development work.
*  Literally dozens of times a day your computer was just rebooting constantly.
*  And so this idea of yes any of the unix workstations would have given a stable development platform where you don't crash and reboot all the time but next also had this really amazing graphical interface and it was great for building tools and it used objective see as the kind of an interesting.
*  Wow next was unix based instead of check to see so there's a lot of the elements that became mac i mean the kind of reverse acquisition of apple by next where that took over and became what i what the modern mac system and define some of the developer.
*  Like the tools and the whole community and you've still got if you're programming on apple stuff now there's still all these in s somethings which was originally next step objects of different kinds of things.
*  But one of the aspects of those old those unix systems was they had this notion of a dot plan file where you know dot file is a you know an invisible file you in less usually in your home directory or something and there was a trivial server running on most unix systems at the time.
*  That i am that when somebody ran a trivial little command called finger you could do finger and then somebody's address it could be anywhere on the internet if you were connected correctly.
*  Then all that server would do was read the dot plan file in that users home directory and then just spit it out to you and originally the idea was that could be.
*  When you're on vacation what your current project was supposed to be like the plan of what you're doing and people would use it for no various purposes but all it did was dump that file over time to the terminal of whoever issued the finger command and.
*  You know at one point i started just keeping a list of what i was doing in there which would be what i was working on in the day and i would have this little i'm syntax i kind of got to myself about
*  i hear something i'm working on a star when i finish it i can have a few other little bits of punctuation and at the time it was it started off as being just like my to do list and it would be these
*  trivial obscure little things like i
*  no fix something with collision detection code made him fireball do something different and just little one liners that people that were following the games could kind of decipher but i did wind up.
*  Starting to write much more in depth things i would have i little notes of thoughts and insights and then i would eventually start having little essays i would sometimes dump into the dot plan files interspersed with the work logs of things that i was doing
*  so in some ways it was like a super early proto blog where i was just kind of dumping out what i was working on but it was interesting enough that there were a lot of people.
*  That i am that were interested in this so most of the people didn't have unix workstation so there were the websites back in the day that would follow the doom and quake development that would i would
*  basically make a little service that would go grab all the changes and then people could just get it with a web browser
*  and there was a period where like all of the little kind of dallas gaming diaspora of people that were at all in that orbit there were a couple dozen plan files going on which was
*  in this was some years before blogging really became kind of a thing and it was kind of a i am a premonition of sort of the way things would go and there was
*  it's all been collected it's available online in different places and it's kind of fun to go back and look through what i was thinking i what i was doing in the different areas have you had a chance to look back is there some interesting very low level specific
*  to do items maybe things you've never completed all that kind of stuff and high level philosophical essay type of stuff that there's some yeah there's some good stuff on both where
*  a lot of it was low level nitpicky details about game dev and i am you know i've learned enough things where there's no project that i worked on that i couldn't go back and do a better job on now i mean you just you learn things hopefully if you're doing it right you learn things as you get older and you should be able to do a better job
*  at all of the early things there's stuff in wolfenstein doom quake that like oh clearly i could go back and do a better job at this whether it's something in the rendering engine side or how i implemented the monster behaviors or managed resources you see the laws you're thinking now
*  yeah i do i mean sometimes i'll get the you know i'll look at and say yeah i had a pretty clear view of i was doing good work there and i haven't really hit the point where there was another programmer graham divine who was i if he had worked at id and seventh guest and and he made some comment one time where he said he looked back at some of his old notes he was like wow i was really smart back then and i i don't hit that so much where i mean i look at it and i always know that yeah
*  there's all the you know with aging you get certain changes in in how you you're able to work problems but all of the problems that i've worked i i'm you know i'm sure that i could do a better job on all of them oh wow so you can still step right in if you could travel back in time and talk to that guy you would teach him a few things yeah absolutely
*  that's awesome i'm what about the high level philosophical stuff is there some insights that stand out do you remember there's things that that i was understanding about development and i'm you know in the industry and so on that were in a in a more primitive stage where
*  i am i definitely learned a lot more in the later years about business and organization and team structure there were.
*  I mean there were definitely things that i was not the best person or even a very good person about managing like how i a team should operate internally how people should work together i was just i am you know that.
*  Just get out of my way and let me work on the code and do this and more and more i've learned how.
*  In the larger scheme of things how sometimes relatively unimportant some of those things are where it is this user value generation that's the overarching importance for all of that and i didn't necessarily have my eye on that ball correctly through a lot of my you know my earlier years and there's things that.
*  You know i could have i could have gotten more out of people handling things in different ways i am you know i could have made.
*  In some ways more successful products by following things in different ways there's mistakes that we made that we couldn't really have.
*  Have known how things would have worked out but it was interesting to see in later years companies like activision showing that hey you really can just do the same game make it better every year and you can look at that from a negative standpoint and say it's like oh that's just being derivative and all that.
*  But if you step back again and say it's like no are the people buying it still enjoying it are they enjoying it more than what they might have bought otherwise.
*  And you can say no that's that's actually a great value creation engine to do that if you're in a position where you can i don't be forced into reinventing everything just because you think that you need to i am.
*  You know lots of things about.
*  Business and team stuff that could be done better but the technical work that the kind of technical visionary type stuff that i late i laid out i still feel pretty good about there are some classical ones about my defending of open gl vs d3d i am which.
*  I turned out to be one of the more probably important momentous things there where.
*  It never it was always a rear guard action on windows where microsoft was just not gonna let that win.
*  But when i look back on it now that fight to keep open gl relevant for a number of years there.
*  Man that open gl was there when mobile started happening and open gl yes was the thing that drove all of the acceleration of the mobile industry.
*  And it's really only in the last few years as apples moved to metal and some of the other companies have moved to vulcan that that's moved away but.
*  Really stepping back and looking at it's like yeah i sold tens of millions of games for different things.
*  But billions and billions of devices wound up with an appropriate capable graphics api do in no small part to me thinking that that was really important that we not just i don't give up and use microsoft's i am.
*  At that time really terrible api know the thing about microsoft is the api don't stay terrible they were terrible at the start but a few versions on they were actually quite good and there was a completely fair argument to be made.
*  That by the time dx nine was out it was probably a better programming environment than open gl but it was still.
*  A wonderful good thing that we had an open standard that could show up on linux and android ios and eventually webgl still to this day so that was.
*  That was one that would be on my greatest hits list of things that that i kind of push back that had on billions of devices yes.
*  So let's talk about it can you tell the origin story of it software.
*  Again one of the greatest game developer companies ever it created wolfstein 3d games that define my life also in many ways.
*  As a thing that made me realize what computers are capable of in terms of graphics in terms of performance it just unlocked something deep.
*  In me and understanding what these machines are all about those games can do that so wolfstein 3d doom quake and just all the incredible engineering innovation that went into that so how did it all start.
*  So i'll caveat upfront that i usually don't consider myself the historian of the software side of things i usually do i kind of point people at john romero for stories about the early days where.
*  I know i've never been like i've commented that i'm a remarkably unsentimental person in some ways where i don't really spend a lot of time unless i'm explicitly prodded to go back and and think about the early days of things and i didn't.
*  I didn't necessarily make the effort to archive everything exactly in my brain and the more that i work on machine learning and ai and the aspects of memory and how when you go back and polish certain things it's not necessarily exactly the way it happened but.
*  Having said all of that from from my view the way everything happened that led up to that was.
*  After i was an adult kind of taking a few college classes deciding to drop out i was doing i was hardscrabble contract programming work really struggling to kind of keep groceries and pay my rent and things.
*  And the company that i was doing the most work for was a company called soft disk publishing which.
*  Add the sounds bizarre now business model of monthly subscription software before there was an internet that people connect to and get software you would pay.
*  You know certain amount in every month they would send you a disk that had some random software on it and people that were in the computers thought this was kind of cool and different ones for apple to the two gs the pc the mac the amiga lots of different things here so quirky little business but i was doing a lot of contract programming for them where i'd write tiny little games and sell them for three hundred five hundred dollars and one of the things that.
*  That i was doing again to keep my head above water here was i decided that i could make one program and i could port port it to multiple systems i would write a game like dark designs are catacombs and i would develop it on the apple to the two gs and the ibn pc.
*  Which apparently was the thing that really kind of peak the attention of the people working down there like jay wilbur was my primary editor and tom hall was a secondary editor.
*  And they kept asking me it's like hey you should come down and work for us here.
*  And i pushed it off a couple times because i was really enjoying my freedom of being off on my own even if i was barely getting by i loved it i was doing nothing but programming all day.
*  But i did have enough close scrapes with like damn i'm just really out of money that maybe i should get an actual job rather than contracting these kind of one at a time things and and jay wilbur was great he was like fed exing me the checks when i would need them.
*  To kind of get over whatever hump i was at so i took the i finally took him up on their offer to come down to shreveport louisiana i was in kansas city at the time.
*  Drove down to through the osiris and everything down to louisiana and saw the soft disc offices went through talk to a bunch of people met the people i've been working with remotely at that time.
*  But the most important thing for me was i met two programmers there john romero and lane roth that for the first time ever i had met programmers that.
*  New more cool stuff than i did where the world was just different back then i was in kansas city it was one of those smartest kid in the school does all the computer stuff the teachers don't have anything to teach him.
*  But all i had to learn from was these few books at the library it was not much at all and there were some aspects of programming that were kind of black magic to me like it's like oh he knows how to format a track on the i am on a low level drive programming interface.
*  And this was i was still not at all sure i was gonna take the job but i met these awesome programmers that were doing cool stuff and my room had worked at origin systems and he had done like you know so many different games ahead of time.
*  That i did kind of quickly decides like you i'll go take the job down there and i am settled down there moved in and started working on more little projects and the first.
*  Kind of big change that happened down there was the company wanted to make a gaming focused a pc gaming focused subscription just like all their other same formula that they used for everything.
*  Pay a monthly fee and you'll get a disc with one or two games just every month and no choice in what you get but we think it'll be fun.
*  And that was the model they were comfortable with and said all right we're gonna start this gamers edge department and.
*  All of us that were interested in that like me from arrow i'm tom hall was kind of helping us from from his side of things jay would peek in and we had a few other programmers.
*  Working with us at the time and we were going to just start making games just the same model i am and we dive in and it was fantastic you have to make new games every month every month yeah.
*  And this in retrospect looking back at it that sense that i don't all this contract programming and john romero had done.
*  Like far more of this where he had done one of his teaching himself efforts was he made a game for every letter of the alphabet that sense of like i'm just gonna go make twenty six different games given a different theme.
*  And you learn so much when you go through and you crank crank these things out like on a bi weekly monthly basis something like that finish it's not like an aid just an idea it's not just.
*  It from from the very beginning to the very end is done it has to be done there's no delaying is done and you've got deadlines and that kind of i rapid iteration pressure cooker environment.
*  Was super important for all of us developing the skills that i you know that brought us to where we eventually went to i mean people would say like.
*  I can the history of the Beatles like it wasn't them being the Beatles it was them playing all of these other i am your early works that that opportunity to craft all of their skills before they were famous.
*  That was very critical to their later successes and i think there's a lot of that here where we did these games that nobody remembers lots of little things that contributed to building up the skill set for the things that eventually did make us famous.
*  Yeah just the yusky wrote the gambler to write it in a month just make money and nobody remembers that probably because he had to figure out because it's literally.
*  He didn't have enough time to write it fast enough so you have to come up with hacks literally.
*  It comes down to that point where pressure and limitation of resources is surprisingly important and it's counterintuitive in a lot of ways where you just think that if you've got all the time in the world and you've got all the resources in the world of course you're going to get something better.
*  But sometimes it really does work out that the innovations mother necessity and you know where you can are resource constraints and you have to do things when you don't have a choice it's surprising what you can do is there any good games written in that time would you say.
*  Some of them are still fun to go back and play where you get the they were they were all about kind of the more modern term is game feel about how just the exact feel that things it's not the grand strategy of the design but how running and jumping and shooting and those things I feel in the in the moment.
*  And some of those are still you sat down on you kind of go it's a little bit different it doesn't have the same movement feel but you move over and you're like bang jump bang it's like hey that's kind of cool still.
*  So you can get lost in the rhythm of the game like that is that we mean by feel just like there's something about it that pulls you in.
*  Nowadays again people talk about compulsion loops and things where it's that I am that sense of exactly what you're doing what your fingers are doing on the keyboard what your eyes are seeing and they're going to be the sequences of things grab the loot shoot the monster jump over the obstacle get to the end of the level these are eternal aspects of game design in a lot of ways.
*  But there are better and worse ways to do all of them and we did so many of these games that it was I we got a lot of practice with it so one of the kind of weird things that was happening at this time is john romero was getting some us some strange fan mail and back in the days this is before email so we literally got letters sometimes and telling him it's like oh I want to talk to you about your games on a reach out different things.
*  And I eventually turned out that these were all coming from scott miller at apogee software and he was reaching out through he didn't think he could contact john directly that he would get intercepted so he was trying to get him to contact him through like.
*  Back channel fan mail because he basically was saying hey I'm making all this money on shareware games I want you to make sure where games because he had seen some of the games that were marrow had done.
*  And you know we looked at scott miller's games and we didn't think they were very good I am we're like that can't be making the kind of money that he's saying he's making ten grand or something I am.
*  Off of this game we really thought that he was full of shit that it was a lie trying to get to get him into this but so that was kind of going on at I am you at one level he was.
*  And it was funny the moment when we're mera realize that he had some of these letters pinned up on his wall like all of his fans and then we noticed that they all had the same return address with different names on them which was a little bit of a two edged sword there.
*  Trying to figure out the puzzle laid out before him yeah what happened after I kind of coincident with that was I was working on a lot of the new technologies where.
*  I was now full on the IBM PC for the first time where I was really a long holdout on Apple to forever and I've you know I love my Apple to was the computer I was wished I had when I was growing up and when I finally did have one I was I was kind of clinging on to that well past it's sort of good use by the best computer ever made.
*  I wouldn't make judgments like that about it but it was positioned in such a way especially in the school systems that it impacted a whole lot of American programmers at least where.
*  There was programs that the Apple to got into the schools and they had enough capability that lots of interesting things happened with them you know in Europe it was different you had your Amigas and Tari's and.
*  No I'm acorns in the UK and things that that had different things but in the United States it was probably the Apple to made the most impact for.
*  A lot of programmers of my generation but so I was really digging into the IBM and this was.
*  Even more so with the total focus because I moved to another city where I didn't know anybody that I wasn't working with I had a little apartment and then at soft disk again the things that.
*  The drew me to it I had a couple programmers that knew more than I did and they had a library they had a set of books and a set of magazines a couple years of magazines the old doctor jobs journal and all of these magazines that had information about things and so.
*  I was just in total immersion mode it was eat breathe sleep computer programming particularly the IBM for.
*  Everything that I was doing and I was digging into a lot of these low level hardware details that people weren't usually paying attention to the way that the IBM EGA cards worked I am.
*  Which was fun for me I hadn't had experience with things at that level and back then you could get hardware documentation just down at the register levels this is where the CRTC register is this is how the color registers work and how the different things are applied and they were designed for a certain.
*  Reason they were designed for an application they were had an intended use in mind but I was starting to look at other ways that they could perhaps be exploited that they weren't initially intended for.
*  Did you comment on like first of all what operating system was there what what instructions that was it like what what what are the what are we talking about this was Dawson x86 so 16 bit 8086 the two 86 were there and three 86 existed they were rare.
*  We had a couple for development systems but we were still targeting the more broad I am.
*  It was all dos 16 bit none of this was kind of dos extenders and things how different is it from the systems of today's it's kind of the precursor that's similar very little if you open up command.
*  I dot E on or com on windows you see some of the remnants of all of that but it was a different world it was the 640 K is enough world and nothing was protected crashed all the time you had.
*  T srs or terminate and stay resident hacks on top of things that would cause configuration problems all the hardware was manually configured in your auto exec so it was a very different world but the code is still the same similar.
*  You would you could still write my earliest code there was written in Pascal that was what I had learned I am kind of earlier so between basic and C++ there's Pascal when basic assembly language and some of my stuff back my intermediate stuff was well you had to for performance basic was just too slow so.
*  Most of the work that I was doing as a contract programmer in my teenage years was was assembly language when I wrote games in assembly yeah complete games in in assembly language.
*  Add its thousands and thousands of lines of three letter acronyms for them the instructions that's you don't earn the once again greatest programmer ever label without being able to write a game in assembly okay that's good everybody wrote their everybody serious wrote their games in assembly language it was kind of a serious.
*  It was an outlier to use Pascal a little bit where there was one famous program called wizardry it was like one of the great early role playing games that was written in Pascal but it was almost nothing used Pascal there but I did learn Pascal.
*  And I remember doing all of my like to this day I sketch in data structures when I'm thinking about something I'll you know I'll I'll open up a file and I'll start writing struct definitions for how data is going to be laid out.
*  And Pascal was kind of formative to that because I remember designing my RPGs in Pascal record structures and things like that and so I had gotten the Pascal compiler for the apple to GS that I could work on in the first IBM game that I developed I did in Pascal and that's actually kind of an interesting story again talking about the constraints and resources.
*  Where I had an apple to GS I didn't have an IBM PC I wanted to port my applications to IBM because I thought I could make more money on it so what I wound up doing is I rented a PC for a week and bought a copy of turbo Pascal.
*  And so I had a hard one week and this was cutting into what minimal profit margin I had there but I had this computer for a week I had to get my program ported before I had to return the PC and that was kind of what the first thing that I had done on the IBM PC and what led me to the taking the job at soft disk.
*  And turbo Pascal how's that different from regular Pascal is a different compiler something like that was it was a product of Borland which before Microsoft kind of killed them they were they were the hot stuff developer tools company had Borland turbo Pascal turbo C and.
*  Prologue I mean all the different things but what they did was they took a supremely pragmatic approach of making something useful it was one of these great examples where Pascal was an academic language and you had things like the UCSDP system that wizardry was actually written in that they did they did manage to make a game with that.
*  But it was not a super practical system while turbo Pascal was it was called turbo because it was blazingly fast to compile I mean really ridiculously 10 to 20 times faster than most other compilers at the time but it also had very pragmatic access to look you can just poke at the hardware in these different ways and we have libraries that let you do things and it was a pretty good it was a perfectly good way to write games and this is one of those things where people have talked about different paths that could be used to write games.
*  And that was not a foregone conclusion at all and people can make real reason rational arguments that the world might have been better if it had gone to Pascal route I'm somewhat agnostic on that where I do know from experience it was perfectly good enough to do that and had some fundamental improvements like it had range checked arrays as an option there which could have been a good option.
*  There which could avoid many of sees real hazards that happened in a security space but see one they were basically operating at about the same level of abstraction it was a systems programming language but we said Pascal had more emphasis on data structures actually I in the tree of languages to Pascal come before see.
*  They were contemporaneous so Pascal's lineage went to modular to eventually over on which was another Nicholas word I am I am kind of experimental language but they were all good enough at that level now some of the classic academic oriented Pascal's were just missing fundamental things like oh you can't access this core system thing because we're just using it to teach students.
*  But I turbo Pascal show that only modest changes to it really did make it a completely capable language and it had some reasons why you can implement it as a single pass compiler so it could be way way faster although less scope for optimizations if you do it that way.
*  I did have some range checking options it had a little bit better typing capability have properly type enum sorts of things and other stuff that see lacked but you know see was also clearly good enough and it wound up with a huge inertia from the unix ecosystem.
*  And everything didn't have garbage collection no it was not garbage collecting kind of thing to see a manual so you could still have your use after freeze and all those other problems but over I am just getting rid of array overruns at least if you were compiled with that debugging option certainly would have avoided a lot of problems and could have a lot of benefits but so anyways that was the next thing I had to learn see because see was where it seemed like most of the most of the things were going so I abandoned Pascal and I started working in see I started hacking on these hardware things.
*  I was dealing with the graphics controllers and the EGA systems and what we most wanted to do so at that time we had we were sitting in our darkened office playing all the different console video games and we're figuring out what do we want to kind of what games do we want to make for gamers edge product there and so we had one of the one of the first super nintendo's sitting there and we had a an older nintendo looking at all those games and the core thing that those consoles did that you just didn't get on the PC game.
*  What is this ability to have a massive scrolling world where most of the games that you would make on the PC and early earlier personal computers would be a static screen you move little things around on it.
*  And you interact like that maybe you go to additional screens as you move but arcade games and consoles had this wonderful ability to just have a big world that you're slowly moving your window through
*  And that was for those types of games that kind of action exploration adventure games that was a super super important thing and PC games just didn't do that.
*  And what I had had come across was a couple different techniques for implementing that on the PC and they're not hard complicated things they want to explain them now they're they're they're pretty straightforward nobody was doing it sound like Einstein describing his five papers is pretty straightforward I understand.
*  But they're nevertheless revolution society scrolling is a game changer.
*  Yeah it's a genius invention either vertical and some of the consoles had different limitations about you could do one but not the other and I and there were similar things going on as advancements even in the console space where you'd have.
*  Like the original Mario game was I like just horizontal scrolling and then later Mario games added vertical aspects to it and different things that I that you were doing to explore you know kind of expand the capabilities there and so much of the early game design for decades was removing limitations letting you do things that you envisioned as a designer you wanted the player to experience but the hardware just couldn't really or you didn't know how to make it happen it felt impossible.
*  You can imagine that you want to create like this big world through which you can size scroll like through which you can walk and then you ask yourself a question how do I actually build that in a way that's like the latency is low enough the hardware can actually deliver that in such a way that is a compelling.
*  Yeah and we knew what we wanted to do because we were we were playing all of these console games playing all these Nintendo games and arcade games clearly there is a whole world of awesome things there that we just couldn't do on the PC at least initially.
*  Because every programmer can tell it's like if you want to scroll you can just redraw the whole screen but then it turns out well you're going five frames per second I that's not an interactive fun experience you want to be going.
*  30 or 60 frames per second or something and it just didn't feel like that was possible it felt like the PCs had to get five times faster for you to make a playable game there.
*  And interestingly I wound up with two completely different solutions for the scrolling problem and this is I'm.
*  This is a theme that runs through everything where all of these big technical advancements it turns out there's always a couple different ways of doing them and it's not like you found the one true way of doing it and we'll see this as we go into 3D games and things later.
*  But so the scrolling the first set of scrolling tricks that I got was.
*  There was the hardware had this ability to you could shift like inside the window of memory I am so the EGA cards at the time had 256 kilobytes of memory and it was awkwardly set up in this planer format where instead of having 256 or 24 million colors you had 16 colors which is 4 bits so you had 4 bit planes 64 K a piece of course 64 K is a nice round number for 16 bit addresses.
*  So your graphics card had a 16 bit window that you could look at and you could tell it to start the video scan out anywhere inside there so there were a couple games that had taken this approach if you could make a 2 by 2 screen or a 1 by 4 screen and you could do scrolling really easily like that you could just lay it all out.
*  And just pan around there but you just couldn't make it any bigger because that's all the memory that was there.
*  I the first insight to the scrolling that I had was well if we make a screen that's just one tile larger you know we usually had tiles that were 16 pixels by 16 pixels the little classic Mario block that you run into lots of art gets drawn that way and your screen is a certain number of tiles but if you had one little buffer region.
*  Outside of that you could easily pan around inside that 16 pixel region that could be perfectly smooth but then what happens if you get to the edge and you want to keep going.
*  The first way we did scrolling was what I called adaptive tile refresh which was really just a matter of you get to the edge and then you go back to the original point and then only change the tiles
*  That have actually that are different between where it was in most of the games at the time if you think about sort of your classic Super Mario Brothers game you've got big fields of blue sky.
*  Long rows of the same brick texture and there's a lot of commonality it's kind of like a data compression thing if you take the screen and you set it down on top of each other in general only about 10% of the tiles were actually different there so this was a way to.
*  Go ahead and say well i'm gonna move it back and i'm only going to change those 1020 whatever percent tiles there and that meant that it was essentially five times faster than if you were redrawing all of the tiles.
*  And that worked well enough for us to do a bunch of these games for high for gamers edge we had a lot of the scrolling games like slurred acts and shadow nights and things like that that we were cranking out at this high rate that had the scrolling effect on it.
*  And it worked well enough there were design challenges there where if you made the worst case if you made a checkerboard over the entire screen you scroll over one and every single tile changes and your frame rates now five frames per second because it had to redraw everything.
*  So the designers had a little bit that they had to worry about they had to make these relatively plain looking levels but it was still pretty magical it was something that we hadn't seen before.
*  And the first thing that we wound up doing with that was I had just gotten this working and Tom Hall was sitting there with me and we were looking over at our super Nintendo on the side there with Super Mario 3 running and we had the technology we had the tool set up there and we stayed up all night and we basically cloned the first level of Super Mario Brothers.
*  Performance wise as well.
*  Yeah and so it and we had our little character running and jumping in there it was you know it wasn't it was close to pixel accurate as far as all the backgrounds and everything but the gaming was just stuff that we cobbled together from previous games that I had written I just kind of like really kit bashed the whole thing together to make this demo.
*  And that was one of the rare cases when I said I don't usually do these all night programming things there's probably only two memorable ones that I can think about you know one was the all nighter to go ahead and get I am to get our dangerous Dave and copyright infringement is how we titled it because we had a game called dangerous Dave was running around with the shotgun shooting things.
*  I and we were just taking our most beloved game at the time there the Super Mario 3 and sort of sticking Dave inside that with this new scrolling technology that was going perfectly smooth for.
*  I am you know for them as it ran and Tom and I just kind of bleary the next morning kind of left and we left a disk on I you know on the desk for John Romero and Jay Wilbur to see it just said run this and we eventually made it back in later in the day and it was.
*  You like they grabbed us and pulled us in the old pull this into the room and that was the point where they were like we gotta do something with this you know we're we're gonna make a company we're gonna go make our own games where this was something that.
*  We were able to just kind of hit them with a hammer of an experience like wow this is just like so much cooler than what we thought was possible there.
*  And initially we tried to get Nintendo to to let us make Super Mario 3 on the PC that's really what we wanted to do we're like hey we can finish this it's line of sight for this will be great.
*  And we sent something to Nintendo and we heard that it did get looked at in Japan and they just weren't interested in that I but that's another one of those life could have gone a very different way where we could have been like Nintendo's house PC team I you know at that point.
*  What was dying and do McQuay could have been a Nintendo creation.
*  So at the same time that we were just doing our first scrolling demos I am we reached out to Scott Miller at Apogee and said it's like hey we do want to make some games you know these things that you think you want those are those are nothing what do you see what we can actually do now this is gonna be amazing.
*  And he just like popped right up and send a check to us where we at that point we still thought he might be a fraud that he was just lying about all of this but he was totally correct on how much money he was making with his shareware titles.
*  And this was his his kind of real brainstorm about this where shareware was this idea that software doesn't have a fixed price if you use it you send out of the goodness of your heart some money to the creator.
*  And there were a couple utilities that did make some significant success like that but for the most part it didn't really work there wasn't much software in a pure shareware model that that was successful.
*  The Apogee innovation was to take something call it shareware split it into three pieces you always made a trilogy.
*  And you would put the first piece out but then you buy the whole trilogy for some shareware amount which in reality it meant that the first part was a demo where you kind of like the demo went everywhere for free and you paid money to to get the whole set but it was still played a shareware and we were happy to have the first one go everywhere and it wasn't a crippled demo where the first episode of all these trilogies it was a real complete game and probably.
*  20 times as many people played that part of it thought they had a great game had found fond memories of it but never paid us a dime but enough people were happy with that where it was really quite successful at these early games that we didn't think very much of compared to commercial quality games but they were doing really good business some fairly crude things and people.
*  It was good business people enjoyed it and it wasn't like you're taking a crap shoot on what you were getting you just played a third of the experience and you loved it enough to handwrite out a check and put it in an envelope and address it and send it out to apogee.
*  To get the rest of them so it was a really pretty feel good business prospect there because everybody was happy you know they knew what they were getting I am when they send it and they would send in fan mail if you're going to the trouble of
*  addressing a letter and i have to fill out an envelope you write something in it and there were just the literal bags of fan mail for the shareware i am games people loved him i should mention that for you the definition of wealth is being able to.
*  Have pizza whenever you want for me there was a dream.
*  That will play shareware games over and over the the part that's free over and over and it was very deeply fulfilling experience but you know i i dreamed of a time when i could actually.
*  Afford the full experience and this is kind of this dreamland beyond beyond the horizon when you could you could find out what else is there in some sense.
*  Even just playing the shareware was.
*  Is the limitation of that you know life is is limited eventually all die in that way shareware was like.
*  Somehow really fulfilling to have this kind of mysterious thing beyond what's free always there it's kind of I don't know that was the main maybe it's because a part of my childhood is playing the shareware games that was a really fulfilling experience it's so interesting how that model still brought joy.
*  To so many people yeah and i 20x people that played it i felt very good about that i would run into people it's like they would say oh i love that game you know that you had early on commander keen whatever and i am and no they they meant just the first episode that they got to see everywhere.
*  That's me i played the crap out of.
*  And that was that was all good yeah yeah so we were in this position where Scott Miller was just fronting us cash saying yeah make you know make a game but.
*  I we did not properly pull the trigger and say all right we're going to we're quitting our jobs we were like we're going to do both we're going to keep working at soft disk working on this and then we're going to go ahead and make a new game for apogee at the same time.
*  Add this eventually did lead to some legal problems and we had we had trouble it all got worked out in the end but it was not a good call at the time there.
*  Your legal mind at the time was not stellar you you are not thinking in terms of the illegal no i definitely wasn't none of us were.
*  And in hindsight yeah it's like how did we think we were going to get away with like even using our work computers to write write software for you know our our breakaway.
*  I knew company it was not a good plan how to come in and come to be.
*  So the design process we would start from we had some idea what we wanted to do we wanted to do a mario like game it was going to be a side scroller i was going to use the technology we.
*  We had some sense of what it would have to look like because of the limitations of this adaptive tile refresh technology it had to have fields of relatively constant tiles you couldn't just paint up a background and then move that around.
*  I have the early design or all the design for commander keen really came from tom hall where.
*  He was kind of the main creative mind for the early and software stuff where we had an interesting division of things where.
*  Tom was all creative and design i was all programming john romero was an interesting bridge where he was both a very good programmer and also a very good designer and artist and kind of straddle between the areas.
*  But commander keen was very much tom hall's baby and i came up with all the design and backstory for the different things of kind of a mad scientist little kid with i am you.
*  Building a rocket ship and zap gun and visiting alien worlds and doing all this that the background that we lay the game inside of and there's not a whole lot to any of these things you know design for us was always just what we needed to do to make the game that was going to be so much fun to play.
*  And we made our we laid out our first trilogy of games you know the shareware formula is going to be three pieces and make matter keen one two and three and we just really started.
*  Busting on all that work and it went together really quickly it was like three months or something that while we were still making games every month for.
*  I for gamers edge we were sharing technology between that i'd write a bunch of code for this and we just kind of use it for both again not a particularly good idea that had consequences for us.
*  But in three months we got our first our first game out and all of a sudden it was three times as successful as the most successful thing apogee had had before and we're making like thirty thousand dollars a month in immediately from the commander keen stuff.
*  And that was again a surprise to us it was more than we thought that was gonna that that was gonna make and we said well we're gonna certainly roll into another set of titles from this.
*  And in that three months i'd come up with a much better way of doing the scrolling technology that was not the adaptive tile refresh which in some ways was even simpler and these things.
*  So many of the great ideas of technology are things that are back of the envelope designs i make this comment about modern machine learning where.
*  All the things that are really important practically in the last decade are each of them fits on the back of an envelope there are these simple little things they're not.
*  Super dense hard to understand i'm technologies and so that the second scrolling trick was just a matter of like okay we know we've got this sixty four k window.
*  And the question was always like well you could make a two by two but you can't go off the edge.
*  But i finally asked well what actually happens if you just go off the edge if you take your start and you say it's like okay i can move over i'm scrolling i can move over i can move down i'm scrolling.
*  I get to what should be the bottom of the memory window like well what if i just keep going and i say i'm gonna start at i know what happens if i start at.
*  FFF E at the very end of the sixty four k block and it turns out it just wraps back around to the top of the block and i'm like oh well this makes everything easy you can just scroll the screen everywhere all you have to draw is just one new line of tiles.
*  Which everything you expose it might be on the line off various parts of the screen memory but it just works that no longer had the problem of you had to have fields of the similar colors because.
*  You doesn't matter what you're doing you could be having a completely unique world and you're just drawing the new strip as it comes on it might be like you said on the line.
*  So it can be all over the place and it turns out it doesn't matter i would have to page flipped screens as long as they didn't overlap they moved in series through this.
*  I two dimensional window of graphics and that was one of those like well this is so simple this just i this just works it's faster i am there it seemed like there was no downside.
*  Funny thing was i it turned out after we shipped titles with this there were what they called super vga cards the cards that would allow higher resolutions and i and different features that the standard ones didn't.
*  And on some of those cards this was a weird compatibility cork again because nobody thought this was not what it was designed to do and some of those cards had more memory they had more than just two hundred fifty six k and four planes they had five twelve k or a megabyte.
*  And on some of those cards.
*  I scroll my window down and then it goes into an initialize memory that actually exist there rather than wrapping back around to the top.
*  And then i was in the tough position of do i have to track every single one of these and it was a madhouse back then with there were twenty different video card vendors with all slightly different implementations of their non standard functionality
*  So either i needed to natively program all of the vga cards there to map in that memory and keep scrolling down through all of that.
*  Or i kind of punted and took the easy solution of when you finally did run to the edge of the screen i accepted a hitch and just copied the whole screen up there so on some of those.
*  Those cards it was a compatibility mode in the normal ones when it all worked fine everything was just beautifully smooth but if you had one of those cards where it did not wrap the way i wanted it to you'd be scrolling around scrolling around and then eventually you'd have a little hitch where.
*  Two hundred milliseconds or something that was not super smooth as it froze a little bit and this is the binary thing is it one of the standard screens or is it one of the weird ones the super vga ones yeah.
*  Okay and so we would default to and i think that was one of those that changed over the kind of course of deployment where early on we would have a normal mode and then you would have you would enable the compatibility flag if your screen did this crazy flickery thing when you got to a certain point in the game.
*  And then later i think it probably got enabled by default as just more and more of the cards i kind of did not do exactly the right thing and that's the two edge sort of doing.
*  Unconventional things with technology where you can find something that nobody thought about doing that kind of scrolling trick when they set up those cards but the fact that nobody thought that was the primary reason when i was relying on that then i wound up being broken on some of the later cards.
*  Let me take a bit of attention but.
*  Ask about the hacker ethic because you mentioned share where it's an interesting world the world of people that make money business and the people that build systems the engineers and.
*  What is the hacker ethic you've been a man of the people and you've embodied at least the part of that i think what does it mean what did it mean to you at the time what does it mean to you today.
*  So steven levy's book hackers was a really formative book for me as a teenager i read it several times and there was.
*  All of the great lore of the early m.i.t. era of hackers and you ending up at the end with.
*  It kind of went through the early m.i.t. hackers and the silicon valley hardware hackers and then the game hackers in part three and at that time as a teenager.
*  I really was kind of bitter in some ways like i thought i was born too late i thought i missed the window there and i really thought i belonged in that third section of that book with the game hackers and they were talking about.
*  The williams at sierra and origin systems with richard gary at and and it's like.
*  I really wanted to be there and i knew that was that was now a few years in the past it was i know it was not to be but.
*  The early days especially the early m.i.t. hacker days talking a lot about this sense of the hacker ethic that there is this sense that.
*  It was about sharing information being good not keeping it to yourself and that it's not a zero sum game that you know you can share something with another programmer and it doesn't take it away from you you know you you then have somebody else doing something.
*  And i also think that there's an aspect of it where is this ability to take joy and other people's accomplishments where it's not the cutthroat bit of like i have to be first i have to be recognized as the one that did this in some way but.
*  Being able to see somebody else some do something and say holy shit that's amazing you know i'm just taking joy in the ability to have something amazing that somebody else does.
*  And the the big thing that i was able to do through id software was this ability to eventually release the source code for most of our like all of our really seminal game titles and that was a it was a stepping stone process where.
*  We were kind of surprised early on where i people were able to hack the existing games and of course i had experience with that i remember hacking my copies of ultima so i give myself you know 9999 gold and raise my levels and.
*  You know break out the sector editor and so i was familiar with all of that so it was just it was with a smile when i started to see people doing that to our games i am you know making level editors for commander keen or hacking up Wolfenstein 3D.
*  But i made the pitch internally that we should actually release our own tools for like what we did what we use to create the games.
*  And that was you know that was a little bit debatable about well you know will this let other will give people leg up it's always like what's that going to mean for the competition.
*  But the really hard pitch was to actually release the full source code for the games and it was a balancing act with the other people inside the company where.
*  It's interesting how the programmers generally did get certainly i am the people that i work closely with they did kind of get that hacker ethic bit where you wanted to share your code you were you were proud of it you wanted other people to take it do cool things with it.
*  But i am interested in the the broader game industry is a little more hesitant to embrace that then like the group of people that we happen to have at id software where it was always a little interesting to me seeing how.
*  A lot of people in the game modding community were very possessive of their code they did not want to share their code they wanted to be there is it was there.
*  No claim to fame and that was much more like what we tended to see with artists where the artists understand something about credit and i you know wanting it to be known as their work and a lot of the game programmers.
*  Help a little bit more like artists than like hacker programmers in that it was about building something that maybe felt more like art to them than the more tool based an exploration based kind of hacking culture side of things.
*  It's so it's so interesting that this kind of.
*  Fear that credit will not be sufficiently attributed to you and that's one of the things that i do bump into a lot because.
*  I try not to go clean i mean it's easy for me to say because so much credit is heaped on me for the id software side of things but when people come up and that they want to pick a fight and say no it's like that wasn't where first person gaming came from and you can point to.
*  You can point to some of like things on obscure titles that i was never aware of or like the old playdoh systems or you know each personal computer had something that was 3D ish and moving around.
*  And i'm you know and i'm happy to say it's like no i mean i saw battle zone and star wars in the arcades i had seen 3D graphics i had seen all these things there.
*  Standing on the shoulders of lots of other people but sometimes these examples they pull out i didn't know that existed i mean there.
*  I never heard of that before then that didn't contribute to what i made but there's plenty of stuff that did and you know i.
*  I think there's good cases to be made that obviously doom and quake and wolfenstein were were formative examples for what.
*  Everything that came after that but i don't feel the need to go fight and say claim primacy or initial invention of anything like that but a lot of people do want to.
*  I think when you fight for the credit in that way and it does go against the hacker ethic.
*  You destroy something fundamental about the culture about the community that builds cool stuff i think credit ultimately.
*  Also i had this sort of there's a famous wrestler and freestyle wrestling called.
*  The vice-president.
*  And he always preach that you should just focus on the art of the wrestling and let people.
*  Write your story however they want the the the highest form of the artist just focusing on the art and that's something that is something about the hacker ethicist.
*  Focus on building cool stuff sharing it with other cool people and credit will get assigned correctly.
*  In the long arc of history.
*  Yeah and i generally think that's true and you've got.
*  I am you know i like there's some things there is there's a graphics technique that got labeled car max reverse i am you know literally named it and it turned out that i wasn't the first person to to figure that out like most.
*  Scientific things are mathematical things you might have like oh this other person had actually done that somewhat before.
*  And then there's things that get attributed to me like the inverse square root hack that i actually didn't do i flat out that wasn't me and it's like it's weird how the mimetic power of the internet i cannot.
*  You're like the mark of programming yes it's just everything just gets attributed to you now even though you've never sought that the credit of things i mean.
*  But part of the fact that the humility behind that is what attracts the attributions.
*  let's talk about a game in me one of the greatest games ever made I know you could talk about doing quake and so on, but to me wolfstein 3D was like wow.
*  It blew my mind that the world like this could exist so how do wolfstein 3D come to be.
*  In terms of the programming in terms of the design in terms of some of the memorable technical challenges.
*  And also actually just something you haven't mentioned.
*  You know how did these ideas come to be inside your mind the adaptive side scrolling so the solutions to these technical challenges.
*  So i usually can introspectively pull back pretty detailed accounts of how technology solutions and design choices on my part came to be where.
*  I technically we had done two games 3D games like that before where hover tank was the first one which had flat shaded walls but did have the scaled enemies inside it and then catacombs 3D which had textured walls scaled enemies and some more.
*  I'm some more functionality like the disappearing walls and some other stuff but what's really interesting from a game development standpoint is.
*  Those games catacombs 3D hover tank and wolf and stein they literally used the same code for a lot of the character behavior that a 2D game that I had made earlier called catacombs did.
*  Where it was an overhead view game kind of like gauntlet you're running around and you can open up doors pick up items basic game stuff.
*  And the thought was that this exact same game experience just presented in a different perspective it could be literally the same game just with a different view into it would have a dramatically different impact on the players.
*  So it wasn't it wasn't a true 3D you're saying that you can kind of take it you can like scale enemies meaning things that are farther away you can make them smaller.
*  So from the game was a 2D map like all of our games use the same tool for creation we use the same map editor for creating keen as wolf and stein and have her tank and catacombs and all this stuff.
*  So the game was a 2D grid made out of blocks and you could say well these are walls these are where the enemy start then they start moving around.
*  And these early games like catacombs you played it strictly in a 2D view it was a scrolling 2D view that was kind of using an adaptive tile refresh at the time to build to do something like that.
*  And then the thought that these early games all it did was take the same basic enemy logic but instead of seeing it from the god's eye view on top you were inside it and turning from side to side yawing your view and moving forwards and backwards inside decide.
*  I and it's a striking thing where you always talk about wanting to isolate factor changes in values and this was one of those most pure cases there where.
*  The rest of the game changed very little it was our normal kind of change the colors on something and draw different picture for it but it's kind of the same thing but the perspective changed in a really fundamental way.
*  And it was dramatically different i can remember the reactions where the artist adrian that had been drawing the pictures for we had a cool big troll thing in catacombs 3D and we had these walls that you could get a key and.
*  You could make the blocks disappear get really simple stuff blocks could either be there or not there so our idea of a door was being able to make a set of blocks just disappear.
*  And i remember the reaction where he had drawn these characters and he was slowly moving around and like people had no experience with 3D navigation was all still keyboard we didn't have mice.
*  I am set up at that time but slowly moving going up picked up a key go to a wall the wall disappears in a little animation and there's a monster like right there any practically fell out of his chair was just like.
*  And games just didn't do that you know the games were the gods i view you were a little invested in your little guy you can be like you know happy or sad when things happen but you just did not get that kind of startle reaction you weren't inside your face something in the back of your brain some reptile brain thing is just going oh shit something just happened.
*  And that was one of those early points where it's like yeah this is gonna make a difference this is going to be powerful and it's gonna matter we able to imagine that in the idea stage or no so.
*  Not that exact thing so we had cases like the arcade games battle zone and star wars that you could kind of see a 3D world and things coming at you.
*  And you get some sense of it but nothing had done the kind of worlds that we were doing and the sort of action based things 3D at the time was really largely about the simulation thoughts.
*  And this is something that really might have trended differently if not for the software approach in the games where.
*  There were flight simulators there were driving simulators yet like hard drive in and microsoft flight simulator and these were doing 3D and general purpose 3D and ways that were more flexible than what we were doing with our games but they were looked at a simulations.
*  They weren't trying to necessarily be fast or responsive I am letting you do kind of exciting maneuvers because they were trying to simulate reality and they were taking their cues from the big systems the evans and southerlands and the silicon graphics that were doing things.
*  But we were taking our cues from the console and arcade games you know we wanted things that were.
*  The sort of quarter eaters that were doing fast pace things that you could smack you around rather than just smoothly gliding you from place to place so quarter yeah.
*  And you know a funny thing is so much that that built into us that Wolfenstein still had lives and you had like one of the biggest power ups in all these games like was an extra life because you started off with three lives and you lose your lives and then it's game over.
*  And there were saved games in i in most of this stuff it was it sounds almost crazy to say this but it was an innovation in doom to not have lives you know you can just play doom as long as you wanted you just restart at the start of the level and why not this is like.
*  We are trying to take people's quarters they've already paid for the entire game we want them to have a good time and you would have some.
*  I know some old timer purists that might think that there's something to the epic journey of making it to the end having to restart all the way from the beginning after a certain number of tries but now more fun is had when you just let people kind of keep trying when they're stuck rather than having to go all the way back and and learn different things.
*  So you recommended the book game engine black book Wolfenstein 3D for technical exploration of the game so looking back 30 years what are some memorable technical innovations that made this perspective shift into this world that's so immersive that scares you when a monster appears or some things you have to solve.
*  So one of the interesting things that come back to the theme of deadlines and resource constraints the game catacombs 3D.
*  We shipped we were supposed to be shipping this for gamers edge on a monthly cadence and I had slipped I was actually late it slipped like six weeks because this was texture map walls doing stuff that I hadn't done before.
*  And at the 6 week point it was still kind of glitchy and buggy there were things that I knew that if you had a wall that was like almost edge on you could slide over to it you could see some things freak out or vanish or not work and I hated that I but I was up against the wall we had to ship the game.
*  I was still a lot of fun to play was novel nobody had seen it gave you that startle reflex I reaction so it was worth shipping but it had these things that I knew were kind of flaky and janky and not not what I was really proud of so one of the things that I did very differently in Wolfenstein.
*  I was I went catacombs used almost a conventional thing where you had segments that were one dimensional polygons basically that were clipped and I'm back faced and done kind of like a very crude 3D engine from the professionals but I wasn't getting it done right I was not doing a good enough job I didn't really have line of sight to.
*  I am to fix it right there stuff that of course I look back it's like it's obvious how to do this do the math right do you're clipping right I check all of this how you handle the precision but I did not know how to do that at that time and I had the first 3D engine you wrote catacombs 3D.
*  You hover tank had been a little bit before that but that had the flat shaded walls so the texture mapping on the walls was what was bringing in some of these challenges that was that was hard for me and I couldn't solve it right at the time can you describe what flat shading isn't texture mapping so in the the walls were solid color one of sixteen colors I'm in hover tank so that's easy it's fast you just.
*  Draw the solid color for everything texture mapping is what we all see today where you have an image that is stretched and distorted onto the walls of the surfaces that you're working with.
*  And it was it was a long time for me to just figure out how to do that without it distorting in the wrong ways and and I did not get it all exactly right in catacombs and I had these flaws.
*  So that was important enough to me that rather than continuing to bang my head on that when I wasn't positive I was going to get it I went with a completely different approach for drawing for figuring out where the walls were which was a ray casting approach.
*  Which I had done in catacombs 3D I had a bunch of C code trying to make this work right and it wasn't working right in Wolfenstein I wound up going to a very small amount of assembly code so in some ways they should be a slower way of doing it.
*  But by making it a smaller amount of work that I could more tightly optimize it worked out and Wolfenstein 3D was just absolutely rock solid you know it was.
*  You know nothing glitched in there the game just was pretty much flawless through all of that I was super proud of that.
*  What eventually like in the later games I went back to the more span based things where I could get more total efficiency once I really did figure out how to do it.
*  So there were two sort of key technical things to Wolfenstein one was this ray casting approach which you still to this day you see people go and say let's write a ray casting engine because it's an understandable way of doing things that lets you make games.
*  Very much like that so you see ray casters in javascript ray casters in python people that are are basically going and re implementing that that approach to to taking a tiled world and casting out into it it works pretty well but it's not the fastest way of doing it.
*  Can you describe what ray casting is.
*  So you start off and you got your screen which is 320 pixels across at the time if you haven't sized down the window for for greater speed and at every pixel there's going to be an angle from you got your position in the world and you're going to just run along that angle and keep going until you hit a block.
*  So up to 320 times across there it's going to throw a cast array out into the world from wherever your origin is until it runs into a wall and then it can figure out exactly where on the wall it hits the performance challenge of that is as it's going out every block it's crossing it checks is this a solid wall.
*  So that means that in like the early wolfenstein levels you're in a small jail cell going out into a small hallway it's super efficient for that because you're only stepping across three or four blocks but then if somebody makes a room that covers our maps were limited to sixty four by sixty four blocks if you made one room that was nothing but walls at the far space it would go pretty slow because it would be stepping across.
*  80 tile tests or something along the way by the way the physics of our universe seems to be competing this very thing so this maps nicely to the actual physics of our world yeah you get a little bit of something like steven wolfram's work on I've interconnected network information states of that and that's it's beyond what I can have an informed opinion on it but it's interesting that people are considering things like that and have and have things that can back it up.
*  Yeah there's whole different sets of interesting stuff there so wolf is time to the had raycast ray casting and then the other kind of key aspect was what i called compiled scalars where the idea of.
*  I am you saw this in the earlier classic arcade games like space harrier and stuff where you would take a picture which is normally drawn directly on the screen
*  And then if you have the ability to make it bigger or smaller big chunky pixels are physically small drop sample pixels that's the fundamental aspect of what are characters were doing in these three games you would have just like you might have drawn a tiny little character but now we can make a really big make a really small move it around.
*  That was the limited kind of three d that we had for characters to make a turn there were literally eight different views of them you didn't actually have a three d model that would rotate you just had these cardboard cutouts.
*  What was good enough for that startle fight reaction and it was kind of what we had to do deal with their.
*  So a straightforward approach to do that you could just write out your doubly nested loop of.
*  You've got your stretch factor and like you got a point you stretch by a little bit it might be on the same pixel it might be on the next pixel might skip to pixel.
*  I am you can write that out but it's not gonna be fast enough where special you get a character for that right in your face monster covering almost the entire screen doing that with a general purpose scaling routine.
*  Would have just been much too slow it would work when there's small characters but then it would get slower and slower as they got closer to you until right at the time when you most care about having a fast reaction time the game would be chunking down.
*  So the fastest possible way to draw pixels at that time was to i am.
*  Instead of saying i got a general purpose i am version that can handle any scale i made i used a program to make essentially a hundred or more separate little programs that was optimized for i will take an image and i will draw it twelve pixels tall i'll take an image i'll draw fourteen pixels tall
*  Up by every two pixels even for that so you would have the most optimized code so that in the normal case where most of the world is fairly large i like the pixels are big you know we did not have a lot of memory.
*  So in most cases that meant that you would load a pixel color and then you would store it multiple times so that was faster than even copying an image in a normal conventional case because most of the time the image is expanded.
*  So instead of doing one read one write for a simple copy you might be doing one read and three or four rights as it got really big and that had the beneficial aspect of just when you needed the performance most when things are covering the screen it was giving you the most acceleration for that.
*  By the way we able to understand this through thinking about it or you testing like the right speed and.
*  This again comes back to i can find the antecedents for things like this so in i am back in the apple two days and i am the graphics were.
*  Essentially single bits at a time and if you wanted to make your little spaceship if you wanted to make it smoothly go across the world if you just took the image and you drew it out at the next location you would move by seven pixels at a time so it go chunk chunk chunk.
*  If you wanted to make it move smoothly you actually had to make seven versions of the ship that were pre shifted you could write a program that would shift it dynamically but on a one megahertz processor that's not going anywhere fast.
*  So if you wanted to do a smooth moving fast action game you made separate versions of each of these sprites now there are a few more tricks you could pull that if it still wasn't fast enough you could make a compiled shape where instead of.
*  This program that normally copies an image and says like get this bite from here store here get this bite store this bite if you've got the memory space you could say i'm going to write the program that does nothing but draw this shape.
*  It's going to be like i'm going to load the immediate value twenty five you know which is some bit pattern and then i'm going to store that at this location.
*  I rather than loading something from memory that will involve indexing registers and this other slow stuff you could go ahead and say no i'm gonna hard code the exact values of all of the image right into the program.
*  This was always a horrible trade off there but you didn't have much memory and you didn't have much speed but if you had something that you wanted to go really fast you could turn it into a program.
*  And that was you know knowing about that technique is what made me think about some of these unwinding it for the pc where people that didn't come from that background were less likely to think about that.
*  I mean there's some deep parallels probably to human cognition as well there's something about.
*  Optimizing and compressing.
*  The the processing of a new information that requires you to predict the possible ways in which the game or the world might unroll and you have something like compiled scalers always there so you have like optimize.
*  Give a prediction of how the world will unroll and you have some kind of optimized data structure for that prediction and then you can modify if the world turns out to be different you can modify a slight way as far as building out techniques so much of the brain is about the associative context you know there.
*  Just when you learn something it's in the context of something else and you can have faint tiny little hints of things and I do think there are some deep things that you are around like sparse distributed memories and boosting that's like if you can just be slightly above the noise floor of having some hint of something you can have things refined into pulling the memory back up so.
*  Having a being a programmer and having a toolbox of like all of these things that things that I did in all of these previous lives of programming tasks that still matters to me about how I'm able to pull up some of these things like in that case it was something I did on the apple to then being relevant for the PC.
*  And I have still cases when I would when I would work on mobile development then be like okay I did something like this back in the doom days but now it's a different environment but I still had that tie I can bring it in and I can transform it into what the world needs right now.
*  And I do think that's actually one of the very core things with human cognition and brain like I you know brain like functioning is finding these ways about you got your brain is kind of everything everywhere all at once you know it's it is just a set of all of this stuff that is just fetched back by these queries that go into it and they can just be slightly above the noise floor with random noise in your neurons and synapses that are affecting exactly what gets pulled up.
*  So you're saying some of these very specific solutions for different games you find that there's a kernel of an a deep idea that's generalizable to other to other things you can't predict what it's going to be but that idea of like I called out that compiled shaders in the forward that I wrote for that the game engine black book as you know this is it's kind of an endpoint of unrolling code but that's one of those things that thinking about that and having that in your mind and I'm sure there are some programmers that
*  hear about that think about it a little bit it's kind of the mind blown moment it's like oh you can just turn all of that data into code and nowadays you know you have instruction cash issues and that's not necessarily the best idea but there are different.
*  It's an idea that has power and has probably relevance in some other areas maybe it's in a hardware point of view that there's a way you approach building hardware that has that same you don't even have to think about it or you just bake everything all the way into it in one place.
*  What is the story of how you came to program doom what is some memorable technical challenges or innovations within that game.
*  So the path that we went after after Wolfenstein got out and we were on this crazy arc where keen one through three more success than we thought keen four through six even more success Wolfenstein even more success so we were on this this crazy trajectory for things.
*  So I saw first box commercial project was a commander keen I am game but then Wolfenstein was going to have a game called a sphere of destiny which was a commercial version sixty new levels so the rest of the team took the game engine pretty much as it was and started working on that we got new monsters but it's.
*  Basically reskins of the things there there's a really interesting aspect about that that I didn't appreciate until much much later about how Wolfenstein clearly did tap out its limit about what you want to play.
*  All the levels and a couple of our license things there was a hard creative wall that you did not really benefit much by continuing to beat on it.
*  But I game like doom and other more modern games like minecraft or something there's kind of a touring completeness level of design freedom that you get in games that Wolfenstein really sat on one side of you know all the creative people in the world could not go and do a masterpiece just with the technology that Wolfenstein had Wolfenstein could do Wolfenstein but you really couldn't do something crazy and different but it didn't take that much more capability to get to Wolfenstein with the free form lines and I had a little bit more.
*  Artistic freedom to get to the point where people still announce new doom levels today all these years after without having completely tapped out the creativity how did you how did you put it touring complete design space design space like you know we have the kind of computational universality on a lot of things.
*  But yeah things where a box can be too small but above a certain point you're kind of are at the point where you you really have almost unbounded creative ability there and do was the first time you cross that line where there were thousands of doom levels created and some of them still have something new and interesting to say to the world about it is that line.
*  Can you introspect what that line was is in the design space is it something about the programming capabilities that you were able to add to the game.
*  So the graphics fidelity was a necessary part because the block limitations in Wolfenstein what we had right there was was not enough the full scale blocks although minecraft I really did show that perhaps blocks I stacked in 3D and at one quarter the scale of that one 8th in volume is then sufficient to have all of that but the.
*  The wall size blocks that we had in Wolfenstein was too much of a creative limitation we license the technology to a few other teams none of them made too much of a of a dent with that it just wasn't enough creative ability.
*  But a little bit more whether it was the variable floors and ceilings and arbitrary angles in doom or the smaller box of blocks in minecraft is that enough to open it up to just worlds and worlds of new capabilities.
*  What is binary space partitioning.
*  So the one one of the technologies around a little bit on the on the story path there so while the team was working on spirit destiny for Wolfenstein I am I had we had met another development team raven software while we were in Wisconsin.
*  And I'm they were doing they had RPG background and I still kind of love that and I offered to do a game engine for for them to let them do a 3D rendered RPG instead of the.
*  Most RPG games were kind of hand drawn they made it look kind of 3D but it was done just all with artist work rather than a real engine.
*  And after Wolfenstein this was still a tile based world but I added floors and ceilings and some lighting and the ability to have some sloped floors in different areas that was my intermediate step for game called shadow caster.
*  And it is slow down enough it was not fast enough to do our type of action things so that they had the screen crop down a little bit so you couldn't go the full screen with like we would try to do in Wolfenstein.
*  I am but i learned a lot i got the floors and ceilings and lighting and it looked great they were great artists up there and it was it was an inspiration for us to look at some of that stuff.
*  What i had learned enough from that that i had the plan for a new faster ways to do that the lighting and shadowing and i wanted to do this free form geometry i wanted to break out of this tile based i am ninety degree world limitations.
*  So we had that was when we got our next stations and we were working with these higher powered systems and i we built an editor that let us draw kind of arbitrary line segments and i was working hard to try to make something that could render this fast enough.
*  I was pushing myself pretty hard i am and we were we were at a point where we could see some things that looked amazingly cool but it wasn't really fast enough for the way i was doing it i.
*  For this flexibility it was no longer i couldn't just ray cast into it and i had these very complex sets of lines and simple little worlds were okay but the cool things that we wanted to do just work quite fast enough.
*  Add i wound up taking a break at that point and i did the port i did two ports of.
*  Our games i wolfenstein to the i to the super nintendo it was i it was a crazy difficult thing to do which was an even slower processors like to put i couple megahertz processor and it had been this whole thing where we had farmed out the i.
*  The work and it wasn't it wasn't going well and i took it back over and trying to make it go fast on there where it really did not have much processing power of the pixels were stretched up hugely and it's it was pretty ugly when you looked at it but in the end it did come out fast enough to play and still be kind of fun from that.
*  But that was where i started using bsp trees are binary space partitioning trees it was one of those things i had to make it faster there it was a stepping stone where it was reasonably easy to understand in the grid world of wolfenstein where was all still ninety degree angles.
*  Bsp trees were i eased myself into it with that and it was a big success i am then when i came back to working on doom i had this new tool in my toolbox it was going to be a lot harder with the arbitrary angles of doom this was where i really started grappling with epsilon problems and just.
*  You know up until that point i hadn't really had to deal with the fact that i am so many numeric things this almost felt like a betrayal to me where people had told me that i had mathematicians up on a bit of a pedestal where i was people think i'm a math wizard and i'm not i really everything that i did was really done with a solid high school math understanding i'm you know algebra to trigonometry and i'm.
*  That was what got me all the way through doom and quake and all of that of just understanding basics of matrices and knowing it well enough to do something with it was the epsilon problems you ran into so i when you wind up taking a like a sloped line and you say i'm going to intersect it with another sloped line.
*  I am then you wind up with something that's not going to be on these nice grid boundaries with the wolfenstein tile maps all you got is horizontal and vertical lines looking at it from above and if you cut one of them it's just obvious the other one gets cut exactly at that point.
*  But when you have angled lines you're doing a kind of a slope intercept problem and you wind up with rational numbers there where things that are not going to evenly land on an integer or even on any fixed point value that you've got so everything winds up having to snap to some fixed point value so the line slightly change their angle you wind up if you cut something here this one's gonna bend a little this way and it's not gonna be completely straight and then you come down to all these questions of well this one is.
*  Is is a point on an angled line you can't answer that in finite precision unless you're doing something with actual rational numbers and later on i did waste far too much time chasing things like that how do you do precise arithmetic with rational numbers and it always blows up eventually you know exponentially as you do.
*  So these are these kind of things are impossible with computers so they're they're possible again there are paths to do the doing it but you can't fit them conveniently and any of the numbers you need to start using big nums and different factor trackings and different things so you you have to if you have any elements of OCD and you want to do something perfectly you're screwed if you're working with floating point yeah so so you had to deal with this for the first time and there was there were lots of challenges there about like okay they build this cool thing and the
*  way the BSP trees work is it basically takes the walls and it carves other walls by those walls in this clever way that you can then take all of these fragments and then you can for sure from any given point get an ordering of everything in the world and you can say this goes in front of this goes in front of this all the way back to the last thing and that's super valuable for graphics where.
*  I kind of a classic graphics algorithm would be painters algorithm you paint the furthest thing first and then the next thing and the next thing and then it comes up and it's all perfect for you that slow because you don't want to have to have drawn everything like that but you can also flip it around and drop the closest thing to you and then if you're clever about it you can figure out what you need to draw that's visible beyond that and that's what these trees allow you to do.
*  Yeah so it's combined with a bunch of other things but it gives you that ordering it's a clever way of doing things and I remember I had learned this from I've one of my graphics Bible at the time about called fully in Van Damme and again it was a different world back there there was a small integer number of books and this book yeah.
*  This book that was it was big fat college textbook that I had I had read through many times I didn't understand everything in it some of it wasn't useful to me but they had the little thing about I finite orderings of you draw little T shaped thing and you can say you can you can make a fixed ahead of time order from this and you can generalize this with the BSP trees and I got a little bit more information about that it was kind of fun later while I was working on quake I got to meet Bruce Naylor who is one of the original researchers that developed
*  those technologies I you know as for academic literature and that was kind of fun but I was very much just finding a tool that can help me solve what I was doing and I was using it in this very crude way in a two dimensional fashion rather than the general 3D the Epsilon problems got much worse and quake and three
*  dimensionals when things angle in every way but eventually I did sort out the sort out how to do it reliably on doom there were still a few edge cases in doom that were not absolutely perfect where they even got terminologies in the communities like when you got to something where it was messed up it was a hall of mirrors effect because you sweep by and it wouldn't draw something there and you would just wind up with the leftover remnants as you flipped between the two pages but BSP trees were important for it but it's again worth noting that
*  after we did doom our major competition came from Ken Silverman is build engine which was used for Duke Nukem 3D and some of the other games for 3D realms and he used a completely different technology nothing to do with I'm with BSP trees so there's not just a one true way of doing things I'm there were critical things about to make any of those games fast you had to you had to separate your drawing into you drew vertical lines and you drew horizontal lines just kind of
*  changing exactly what you would draw with them that was critical for the technologies I at that time and like all the games that were kind of like that wound up doing something similar but there were still a bunch of other decisions that could be made and we made good enough decisions on everything on doom we.
*  We brought in multiplayer significantly and it was our first game that was designed to be modified by the user community where we had this whole set up of our wad files and p wads and things that people could could build with tools that we released to them and they eventually rewrote to be better than what we released but they could build things and you can add it to your game without destructively modifying it which is what you had to do in all the early games you literally hacked the data files or the executable before while doom was set up in this flexible way so that
*  you could just say run the normal game with this added on on top and it would overlay just the things that you wanted to there would you say that doom was kind of the first true 3D game you created so no it's still doom would usually be called a two and a half D game where it had three dimensional points on it and this is another one of these kind of pedantic things that people love to argue about about what was the first 3D game I still like I'm like every month probably I hear from somebody about well was doom really a
*  3D game or something I and you know I give the point where characters had three coordinates so you had like an X Y and Z the cacodemian could be coming in very high income you know and come down towards you I have the walls had three coordinates on them so on some sense it's a 3D game engine but it was not a fully general 3D game engine you could not I you could not build a pyramid in doom because you couldn't make a sloped wall I which was slightly different where in that
*  previous shadow caster game I couldn't have vertexes and have a sloped floor there but the changes that I made for doom to get higher speed and a different set of flexibility traded away that ability but you literally couldn't make that you could not I you could make different heights of passages but you could not make a bridge over another area you could not go over and above it so that's still add some 2d limitations to it that's more about the building versus the actual experience because the experiences felt like things would come at you but again you
*  couldn't look up either I am right you know you could only pitch it was four degrees of freedom rather than six degrees of freedom you did not have the ability to tilt your head this way or pitch up and down so that takes us to quake what was the leap there what was some fascinating technical challenges and there were a lot or not challenges but innovations that you've come up with so quake was kind of the first thing where I did have to kind of come face to face with but my limitations
*  where it was the first thing where I really did kind of give it my all and still come up a little you know come up a little bit short in terms of what and when I wanted to to get it done and the company rent had some serious stresses through the whole project and
*  we we bid off a lot so the things that we set out to do was it was going to be really a true 3d engine where it could do six degree of freedom you could have all the all the viewpoints you could model anything it had a really remarkable new lighting model with the surface caching and things that was one of those where it was starting to do some things that they weren't doing even on the very high end systems and it was going to be completely programmable on the surface
*  in the modding standpoint where the thing that you couldn't do and do you could replace almost all of the media but you couldn't really change the game i there were still some people that were doing the hex setting of the executable the de hacked things where you could change a few things about rules and people made
*  some early capture the flag type things by hacking the executable but it wasn't really set out to do that quake was going to have its own programming language that the game was going to be implemented and that would be able to be overwritten just like any of the media code was going to be data for that and you would be able to
*  have expansion packs that changed fundamental things and mods and so on and the the multiplayer was going to be playable over the internet it was going to support i client server rather than peer to peer so we had the possibility of supporting larger numbers of players in disparate locations with this full flexibility of the programming overrides with full six degree of freedom modeling and viewing and with this fancy new light mapped kind of surface caching side
*  it was a lot and this was one of those things that if i could go back and tell i am you know tell younger me to do something differently it would have been to split those innovations up into two phases in two separate game will be phase one of his so it probably would have been taking the doom rendering engine and bringing in the tcp ip client server focusing on the multiplayer and the quake c would have been doomed c programming language there so i would have split that into programming language
*  networking with the same doom engine rather than forcing everybody to go towards the pen the other quake engine which really met getting a pentium while it ran on a forty six it was not a great experience there we could have made more people happier and gotten two games done in fifty percent more time i was speaking of people happier mutual friend jill rogan it seems like his the most important moment of his life is is centered around quake.
*  So is it was a definitive part of his life so would he agree with your thinking that they should split so he is a person who loves quake and played quake a lot would he agree that you should have done the doom engine with and focus on the multiplayer for phase one or in your looking back it is the three world that quake created was also fundamental to the the environment.
*  I would say that what would have happened is you would have had a doom looking but quake feeling game eight months earlier and then maybe six months after quake actually shipped then there would have been the full running on a pentium six degree of freedom graphics engine type things there so it's not that it wouldn't have been there it would have been something amazingly cool earlier and then something even cooler somewhat later where i would
*  much rather in have gone and done two one year development efforts i cycle them through i be a little more pragmatic about that rather than killing us ourselves on the whole quake development but i say it's obviously things worked out well in the end but looking back and saying how would i optimize and do things differently that did seem to be a clear case where
*  I going ahead and we had enormous momentum on doom you know we did doom to as the kind of commercial box version after our shareware success with the original but we could have just made another doom game adding those new features in it would have been huge we would have learned all the same lessons but faster and it would have given six degree of freedom and pentium class systems a little bit more time to get mainstream because we did cut out a lot of people with the hardware requirements for quake.
*  Was there any dark moments for you personally psychologically in having in having such harsh deadlines and having this also mean difficult technical challenges.
*  So I've never really had really dark black places I mean I it I can't necessarily put myself in anyone else's shoes but I understand a lot of people have you have significant challenges with kind of their their mental health and well being and I've been I've been super stressed I've been unhappy as a teenager in various ways but I've never.
*  But I've never really gone to a very dark place.
*  I just seem to be largely immune to what really wrecks people.
*  I mean, I've had plenty of time when I'm very unhappy and miserable about something,
*  but it's never hit me like I believe it winds up hitting some other people.
*  I've borne up well under whatever stresses have fallen on me.
*  I've always coped best on that when all I need to do is usually just kind of bear down on my work.
*  I pull myself out of whatever hole I might be slipping into by actually making progress.
*  I mean, maybe if I was in a position where I was never able to make that progress,
*  I could have slid down further, but I've always been in a place where,
*  okay, a little bit more work, maybe I'm in a tough spot here,
*  but I always know if I just keep pushing, eventually I break through and I make progress.
*  I feel good about what I'm doing.
*  And that's been enough for me so far in my life.
*  Have you seen in the distance ideas of depression or contemplating suicide?
*  Have you seen those things far?
*  So it was interesting.
*  When I was a teenager, I was probably on some level a troubled youth.
*  I was unhappy most of my teenage years.
*  I wanted to be on my own doing programming all the time.
*  As soon as I was 18, 19, even though I was poor, I was doing exactly what I wanted.
*  I was very happy, but high school was not a great time for me.
*  And I had a conversation with the school counselor and they're kind of running their script.
*  It's like, okay, it's kind of a weird kid here.
*  Let's carefully probe around.
*  It's like, do you ever think about ending it all?
*  I'm like, no, of course not.
*  Never, not at all.
*  This is temporary.
*  Things are going to be better.
*  I'm and that's always been kind of the case for me.
*  And obviously that's not that way for everyone.
*  Other people do react differently.
*  What was your escape from the troubled youth?
*  Like, you know, music, video games, books.
*  How did you escape from a world that's full of cruelty and suffering and that's absurd?
*  Yeah, I mean, I was not a victim of cruelty and suffering.
*  It's like I was an unhappy, somewhat petulant youth in my point where I'm not
*  putting myself up with anybody else's suffering, but I was unhappy objectively.
*  And the things that I did that very much characterized my childhood were I had books,
*  comic books, Dungeons and Dragons, arcade games, video games.
*  Like some of my fondest childhood memories are the convenience stores,
*  the 7-elevens and quick trips because they had a spinner rack of comic books and they
*  had a little side room with two or three video games, arcade games in it.
*  And that was very much my happy place.
*  You know, if I could, I get my comic books and if I could go to a library and, you know,
*  go through those little zero zero zero section where computer books were supposed to be.
*  And there are a few sad little books there, but still just being able to sit down and
*  go through that.
*  I read a ridiculous number of books, both fiction and nonfiction as a teenager.
*  My rebelling in high school was just sitting there with my nose in a book,
*  ignoring the class, and through lots of it.
*  Teachers had a range of reactions to that, some more accepting of it than others.
*  I'm with you on that.
*  So let us return to Quake for a bit with the technical challenges.
*  What, everything together from the networking to the graphics, what are some things you
*  remember that were innovations you had to come up with in order to make it all happen?
*  Yeah, so there were a bunch of things on Quake where on the one hand, the idea that I built my
*  own programming language to implement the game in, looking back, and I try to tell people,
*  it's like every, every high level programmer sometime in their career goes through and they
*  invent their own language.
*  It just seems to be a thing that's pretty broadly done.
*  People will be like, I'm going to go write a computer programming language.
*  I don't regret having done it, but after that, I switched from Quake C, my quirky little
*  pseudo object orienter entity oriented language there.
*  Quake 2 went back to using DLLs with C, and then Quake 3, I implemented my own C interpreter
*  or compiler, which was a much smarter thing to do that I should have done originally for Quake.
*  Building my own language was an experience.
*  I learned a lot from that.
*  And then there was a generation of game programmers that learned programming with Quake C,
*  which I feel kind of bad about because we give JavaScript a lot of crap, but
*  Quake C was nothing to write home about there.
*  But it allowed people to do magical things.
*  You get into programming not because you love the BNF syntax of a language, it's because the
*  language lets you do something that you cared about.
*  And here's very much you could do something in a whole beautiful three dimensional world.
*  And the idea and the fact that the code for the game was out there, you could say,
*  I like the shotgun, but I want it to be more badass.
*  You go in there and say, okay, now it does 200 points damage.
*  And then you go around with a big grin on your face blowing up monsters all over the game.
*  So yeah, it's, you know, it is not what I would do today going back with that language,
*  but that was a big part of it.
*  Learning about the networking stuff.
*  Because it's interesting where I learn these things by reading books.
*  So I would get a book on networking and find something I read all about and learn, okay,
*  packets, they can be, you know, out of order, lost or duplicated.
*  These are all the things that can theoretically happen to packets.
*  So I wind up spending all this time thinking about how do we deal about all of that?
*  And it turns out, of course, in the real world, those are things that, yes,
*  theoretically can happen with multiple routes, but they really aren't things that your 99.999%
*  of your packets have to deal with.
*  So there was learning experiences about lots of that, like why when TCP is appropriate versus UDP
*  and how if you do things in UDP, you wind up reinventing TCP badly in almost all cases.
*  So, you know, there's good arguments for using both for different game technology,
*  different parts of the game process, transitioning from level to level and all.
*  But the graphics were the showcase of what Quake was all about.
*  It was this graphics technology that nobody had seen there.
*  And it was a while before, you know, there were competitive things out there.
*  And it went a long time internally, really not working where we were even building levels where
*  the game just was not at all shippable with large fractions of the world, like disappearing,
*  not being there, or being really slow in various parts of it.
*  And it was this act of faith. It's like, I think I'm going to be able to fix this.
*  I think I'm going to be able to make this work.
*  And lots of stuff changed where the level designers would build something and then have
*  to throw it away as something fundamental in the kind of graphics or level technology change.
*  So there were two big things that contributed to making it possible at that time frame.
*  I am two new things. There was certainly hardcore optimized low level assembly language.
*  This was where I had hired Michael Abrash away from Microsoft.
*  And he had been one of my early inspirations where that back in the soft disk days,
*  the library of magazines that they had, some of my most treasured ones were Michael Abrash's
*  articles in Dr. Dobbs Journal. And it was amazing after all of our success in Doom,
*  we were able to kind of hit him up and say, hey, we'd like you to come work at id Software.
*  And he was in the senior technical role at Microsoft. And he was on track for,
*  and this was right when Microsoft was starting to take off. And I did eventually convince him
*  that what we were doing was going to be really amazing with Quake. It was going to be something
*  nobody had seen before. It had these aspects of what we were talking about. We had Metaverse talk
*  back then. We had read Snow Crash and we knew about this. And Michael was big into the science
*  fiction and we would talk about all that and kind of spin this tale. And it was some of the same
*  conversations that we have today about the Metaverse, about how you could have different
*  areas linked together by portals and you could have user generated content and changing out all
*  of these things. So you really were creating the Metaverse with Quake.
*  And we talked about things like- Philosophically.
*  Used to be advertised as a virtual reality experience. The first wave of virtual reality
*  was in the late 80s and early 90s, you had like the Lawn Mower Man movie and you had time in
*  Newsweek talking about the early VPL headsets. And of course, that cratered so hard that people
*  didn't want to look at virtual reality for decades afterwards where it was just, it was
*  smoke and mirrors. It was not real in the sense that you could actually do something
*  real and valuable with it. But still, we had that kind of common set of talking points and
*  we were talking about what these games could become and how you'd like to see people building
*  all of these creative things. Because we were seeing an explosion of work with Doom at that time
*  where people were doing amazingly cool things. Like we saw cooler levels that we had built coming
*  out of the user community and then people finding ways to change the characters in different ways.
*  And it was great. And we knew what we were doing in Quake was removing those last things. There
*  was some quirky things with a couple of the data types that didn't work right for overriding and
*  then the core thing about the programming model. And I was definitely going to hit all of those
*  in Quake. But the graphics side of it was still, I knew what I wanted to do and it was one of these
*  hubris things where it's like, well, so far I've been able to kind of kick everything that I set
*  out to go do. But Quake was definitely a little bit more than could be comfortably chewed at that
*  point. But Michael was one of the strongest programmers and graphics programmers that I knew.
*  And he was one of the people that I trusted to write assembly code better than I could.
*  And there's a few people that I can point to about things like this where I'm a world-class
*  optimizer. I mean, I make things go fast, but I recognize there's a number of people that can
*  write tighter assembly code, tighter SIMD code or tighter CUDA code than I can write. My best
*  strengths are a little bit more at the system level. I mean, I'm good at all of that, but
*  the most leverage comes from making the decisions that are a little bit higher up where you figure
*  out how to change your large scale problems so that these lower level problems are easier to do
*  or it makes it possible to do them in a uniquely fast way. So most of my big wins in a lot of ways
*  from all the way from the early games through VR and the aerospace work that I'm doing or did,
*  and hopefully the AI work that I'm working on now is finding an angle on something that means you
*  trade off something that you maybe think you need, but it turns out you don't need. And by
*  making a sacrifice in one place, you can get big advantages in another place.
*  Is it clear at which level of the system those big advantages can be gained?
*  It's not always clear. And that's why the thing that I try to make one of my core values and I
*  proselytize to a lot of people is trying to know the entire stack, trying to see through everything
*  that happens. And it's almost impossible on the web browser level of things where there's so many
*  levels to it, but you should at least understand what they all are even if you can't understand
*  all the performance characteristics at each level. But it goes all the way down to literally the
*  hardware. So what is this chip capable of and what is this software that you're writing capable of
*  and then what is this architecture you put on top of that, then the ecosystem around it, all the
*  people that are working on it. So there are all these decisions and they're never made in a
*  globally optimal way, but sometimes you can drive a thread of global optimality through it. You can't
*  look at everything. It's too complicated, but sometimes you can step back up and make a different
*  decision. And we kind of went through this on the graphics side on Quake where in some ways it was
*  kind of bad where Michael would spend his time writing. I'd rough out the basic routines like,
*  okay, here's our span rasterizer. And he would spend a month writing this beautiful cycle
*  optimized piece of assembly language that does what I asked it to do. And he did it faster than
*  my original code would do or probably what I would be able to do even if I had spent that month on it.
*  But then we'd have some cases when I'd be like, okay, well, I figured out at this higher level,
*  instead of drawing these in a painter's order here, I do a span buffer and it cuts out
*  30% or 40% of all of these pixels, but it means you need to rewrite kind of this interface of
*  all of that. And I could tell that wore on him a little bit, but in the end it was the right thing
*  to do where we wound up changing that rasterization approach and we wound up with a super optimized
*  assembly language core loop and then a good system around it, which minimized how much that had to be
*  called. And so in order to be able to do this kind of system level thinking, whether we're talking
*  about game development, aerospace, nuclear energy, AI, VR, you have to be able to understand the
*  hardware, the low level software, the high level software, the design decisions, the whole thing,
*  the full stack of it. Yeah. And that's where a lot of these things become possible. When you're
*  really, when you're bringing the future forward, I mean, there's a pace that everything just kind
*  of glides towards where we have a lot of progress that's happening at such a different, so many
*  different ways you kind of slide towards progress, just left to your own programs, just get faster.
*  For a while, it wasn't clear if they were going to get fatter more than they get quicker than they
*  get faster and it cancels out, but it is clear now in retrospect, no programs just get faster and have
*  gotten faster for a long time. But if you want to do something like back at that original, talking
*  about scrolling games, say what, this needs to be five times faster. Well, we can wait six years
*  and just, it'll naturally get that much faster at that time. Or you come up with some really clever
*  way of doing it. So there are those opportunities like that in a whole bunch of different areas.
*  Now, most programmers don't need to be thinking about that. There's not that many, you know,
*  there's a lot of opportunities for this, but it's not everyone's workaday type stuff. So everyone
*  doesn't have to know how all these things work. They don't have to know how their compiler works,
*  how the processor chip manages cache eviction and all these low-level things. But sometimes
*  there are powerful opportunities that you can look at and say, we can bring the future five years
*  faster. We can do something that, wouldn't it be great if we could do this? Well, we can do it today
*  if we make a certain set of decisions. And it is in some ways, smoke and mirrors, where you say it's
*  like, doom was a lot of smoke and mirrors where people thought it was more capable than it actually
*  was. But we picked the right smoke and mirrors to deploy in the game, where by doing this, people
*  will think that it's more general if we are going to amaze them with what they've got here. And they
*  won't notice that it doesn't do these other things. So smart decision-making at that point,
*  that's where that kind of global, holistic, top-down view can work. And I'm really a strong
*  believer that technology should be sitting at that table having those discussions. Because you do
*  have cases where you say, well, you want to be the Jonathan Ivey or whatever, where it's a pure design
*  solution. And in some cases now, where you truly have almost infinite resources, like if you're
*  trying to do a scrolling game on the PC now, you don't even have to talk to a technology person.
*  You can just have any intern can make that go run as fast as it needs to there. And it can be
*  completely design-based. But if you're trying to do something that's hard, either that can't be done
*  for resources like VR on a mobile chipset, or that we don't even know how to do yet, like artificial
*  general intelligence, it's probably going to be a matter of coming at it from an angle. I mean,
*  for AGI, we have some of the Hutter principles about how you can, you know, AXA or some of that.
*  There are theoretical ways that you can say, this is the optimal learning algorithm that can solve
*  everything, but it's completely impractical. You just can't do that. So clearly, you have to make
*  some concessions for general intelligence. And nobody knows what the right ones are yet. So
*  people are taking different angles of attack. I hope I've got something clever to come up with
*  in that space. It's been surprising to me. And I think perhaps it is a principle of progress
*  that smoke and mirrors somehow is the way you build the future. You kind of fake it till you
*  make it and you almost always make it. And I think that's going to be the way we achieve AGI. That's
*  going to be the way we build consciousness into our machines. There's philosophers debate about
*  the Turing test is essentially about faking it till you make it. You start by faking it.
*  And I think that always leads to making it. Because if you look at history, arguments,
*  when as soon as people start talking about qualia and consciousness and Chinese rooms and things,
*  it's like, I just check out. I just don't think there's any value in those conversations. It's
*  just like, go ahead, tell me it's not going to work. I'm going to do my best to try to make it
*  work anyways. I don't know if you work with legged robots. There's a bunch of these.
*  They sure as heck make me feel like they're cautious in a certain way that's not here today.
*  You could see the kernel. It's like the flame, the beginnings of a flame. We don't have line of sight,
*  but there's glimmerings of light in the distance for all of these things. Yeah, I'm hearing
*  murmuring in a distant room. Well, let me ask you a human question here. In the game design space,
*  you've done a lot of work throughout, but in terms of game design, you have changed the world. And
*  there's a few people around you that did the same. So famously, there's some animosity,
*  there's much love, but there's some animosity between you and John Romero. What is at the core
*  of that animosity and human tension? So there really hasn't been,
*  for a long time, and even at the beginning, it's like, yes, I did push Romero out of the company.
*  And this is one of the things that I look back. If I could go back telling my younger self some
*  advice about things, the original founding kind of corporate structure of id software
*  really led to a bunch of problems. We started off with us as equal partners, and we had a buy-sell
*  agreement because we didn't want outsiders to be telling us what to do inside the company.
*  And that did lead to a bunch of the problems where I was sitting here going, it's like, all right,
*  I'm working harder than anyone. I'm doing these technologies nobody's done before, but we're all
*  equal partners. And then I see somebody that's not working as hard. I can't say I was the most
*  mature about that. I was 20-something years old, and it did bother me when I'm like, everybody,
*  okay, we need to all pull together, and we've done it before. Everybody, we know we can do this if we
*  get together and we grind it all out, but not everybody wanted to do that for all time.
*  I was the youngest one of the crowd there. I had different sets of backgrounds and motivations,
*  and left at that point where it was, all right, either everybody has to be contributing up to
*  this level or they need to get pushed out. That was not a great situation. And I look back on it,
*  and no, we pushed people out of the company that could have contributed if there was a different
*  framework for them. And the modern Silicon Valley, let your stock vest over a time period,
*  and maybe it's non-voting stock and all those different things. We knew nothing about any of
*  that. We didn't know what we were doing in terms of corporate structure or anything.
*  So if you think the framework was different, some of the human tension could have been a little bit.
*  It almost certainly would have. I look back at that, and it's like even trying to summon up
*  in my mind, it's like I know I was really, really angry about Romero not working as hard as I wanted
*  him to work or not carrying his load on the design for Quake and coming up with things there. But he
*  was definitely doing things. He made some of the best levels there. He was working with some of
*  our external teams like Raven on the licensing side of things. But there were differences of opinion
*  about it. But he landed right on his feet. He got $20 million from Eidos to go do Ion Storm,
*  and he got to do things his way and spun up three teams simultaneously. Because that was always one
*  of the challenging things in it, Id, where we were doing these single string one project after
*  another. And I think some of them wanted to grow the company more. And I didn't because I knew people
*  that were saying that, oh, companies turn to shit when you got 50 employees. It's just a different
*  world there. And I loved our little dozen people working on the projects. But you can look at it
*  and say, well, business realities matter. It's like you're super successful here. And we could
*  take a swing and a miss on something, but you do it a couple times and you're out of luck.
*  There's a reason companies try to have multiple teams running at one time. And so I was thinking
*  on something I didn't really appreciate back then. So if you look past all that, you did create some
*  amazing things together. What did you love about John Romero? What did you respect and appreciate
*  about him? What did you admire about him? What did you learn from him?
*  When I met him, he was the coolest programmer I had ever met. He had done all of this stuff. He
*  had made all of these games. He had worked at one of the companies that I thought was the coolest at
*  Origin Systems. And he knew all this stuff. He made things happen fast. And he was also kind of
*  a polymath about this, where he could do, he drew his own art, he made his own levels, as well as
*  we worked on sound design systems on top of actually being a really good programmer.
*  And we went through a little, it was kind of fun where one of the early things that we did,
*  where there was kind of the young buck bit going in where I was the new guy and he was the top man
*  programmer at the soft disk area. And eventually we had sort of a challenge over the weekend that
*  we were going to like race to implement this game, to port one of our PC games back down to the Apple
*  2. And that was where we finally kind of became clear. It's like, okay, Carmack stands a little
*  bit apart on the programming side of things. And, but Romero then very gracefully moved into, well,
*  he'll work on the tools, he'll work on the systems, do some of the game design stuff, as well as
*  contributing on starting to lead the design aspects of a lot of things. So he was enormously
*  valuable in the early stuff and so much of Doom and even Quake have his stamp on it in a lot of
*  ways. But I am, you know, he wasn't at the same level of focus that I brought to the work that
*  we were doing there. And he really did, we hit such a degree of success that it was all in the
*  press about that. The rock star game programmers. Yeah. I mean, it's the Beatles problem. Yeah. I
*  mean, and you know, he ate it up and he did personify, there was the whole game developers
*  with, you know, with Ferraris that we had there. And I thought that, you know, that led to some
*  challenges there. But so much of the, you know, the stuff that was great in the games did come
*  from him. And I would certainly not take that away from him. And even after we parted ways and he
*  took his swing with IDOS, in some ways he was like, he was ahead of the curve with mobile gaming as
*  well, where one of his companies after IDOS was working on feature phone game development. And
*  I wound up doing some of that just before the iPhone crossing over into the iPhone phase there.
*  And that was something that clearly did turn out to be a huge thing, although he was too early for
*  what he was working on at that time. You know, we've had pretty cordial relationships where I was
*  happy to talk with him anytime I'd run into him at a conference. I haven't actually had some other
*  people just say it's like, oh, you shouldn't, you know, you shouldn't go over there and give him the
*  time of day or felt that Masters of Doom was, you know, like portrayed, played things up in a way
*  that I shouldn't be too happy with, but I'm okay with all of that. And I know-
*  So you still got love in your heart. Yeah. I mean, I just talked with him like
*  last year, or I guess it was even this year about mentioning that I'm going off doing this AI stuff.
*  I'm going big into artificial intelligence. And he had a bunch of ideas for how AI is going to
*  play into gaming and, you know, asked if I was interested in collaborating. And it's not in line
*  with what I'm doing, but I do, you know, I wish almost everyone the best. I mean, I know I may
*  not have partnered on the best of terms with some people, but I was thrilled to see Tom Hall writing
*  VR games. Now he wrote, I worked on a game called Denio, which is really an awesome VR game. It's
*  like Dungeons and Dragons. We all used to play Dungeons and Dragons together. That was one of
*  the things that was what we did on Sundays in the early days. I would Dungeon Master and they'd all
*  play. And I, you know, so it really made me smile seeing Tom involved with an RPG game in virtual
*  reality. You were the CTO of Oculus VR since 2013 and maybe less than a year involved in a bit.
*  In 2019, Oculus was acquired by Facebook now Meta in 2014. You've spoken brilliantly about both the
*  low level details, the experimental design and the big picture vision of virtual reality.
*  Let me ask you about the metaverse. The big question here, both philosophically and technically,
*  how hard is it to build the metaverse? What is the metaverse in your view? You started with
*  discussing and thinking about Quake as a kind of a metaverse. As you think about it today,
*  what is the metaverse, the thing that could create this compelling user value, this experience that
*  will change the world and how hard is it to build it? So the term comes from Neil Stevenson's book,
*  Snow Crash, which many of us had read back in the nineties. It was one of those kind of formative
*  books. There was this sense that the possibilities and the freedom and unlimited capabilities to
*  build a virtual world that does whatever you want, whatever you ask of it, has been a powerful draw
*  for generations of developers, game developers specifically and people that are thinking about
*  more general purpose applications. We were talking about that back in the doom and quake days about
*  how do you wind up with an interconnected set of worlds that you kind of visit from one to another
*  and as web pages were becoming a thing, you start thinking about what is the interactive 3D based
*  equivalent of this? There were a lot of really bad takes. You had like, vermal, virtual reality,
*  markup languages, and there's aspects like that that came from people saying, well, what kind of
*  capabilities should we develop to enable this? And that kind of capability first work has usually
*  not panned out very well. On the other hand, we have successful games that started with things
*  like doom and quake and communities that formed around those and whether it was server lists in
*  the early days or literal portaling between different games and then modern things that
*  are on completely different order of magnitude like Minecraft and Fortnite that have 100 million
*  plus users. I still think that that's the right way to go to build the metaverse is you build
*  something that's amazing that people love and people wind up spending all their time in
*  because it's awesome and you expand the capabilities of that. Even if it's a very basic experience.
*  Minecraft is an amazing case study in so many things. What's been able to be done with that
*  is really enlightening. And there are other cases where like right now Roblox is basically
*  a game construction kit aimed at kids and that was a capability first play and it's achieving
*  scale that's on the same order of those things. So it's not impossible, but my preferred bet would be
*  you make something amazing that people love and you make it better and better. And that's where I
*  could say we could have gone back and followed a path kind of like that in the early days. If you
*  just kind of take the same game whether it's when Activision demonstrated that you could make Call
*  of Duty every year and not only is it not bad, people kind of love it and it's very profitable.
*  The idea that you could have taken something like that, take a great game, release a new version
*  every year that lets the capabilities grow and expand to start saying it's like okay it's a game
*  about running around and shooting things, but now you can have, bring your media into it, you can
*  add persistence of social signs of life or whatever you want to add to it.
*  I still think that's quite a good position to take and I think that while Meta is doing a bottoms
*  up capability approach with Horizon Worlds where it's a fairly general purpose, creators can build
*  whatever they want in their sort of thing, it's hard to compare and compete with something like
*  Fortnite which also has enormous amounts of creativity even though it was not designed
*  originally as a general purpose sort of thing. So there's, we have examples on both sides,
*  me personally I would have bet on trying to do entertainment, valuable destination first
*  and expanding from there. So can you imagine the thing that will be kind of, if we look back a
*  couple of centuries from now and you think about the experiences that marked the singularity,
*  the transition where most of our world moved into virtual reality, what do you think those
*  experiences will look like? So I do think it's going to be kind of like the way the web
*  slowly took over where you're the frog in the pot of water that's slowly heating up where having
*  lived through all of that, I remember when it was shocking to start seeing the first website
*  address on a billboard when you're like, hey, my computer world is infecting the real world,
*  this is spreading out in some way but there's still, when you look back and say, well, what
*  made the web take off? And it wasn't a big bang sort of moment there, it was a bunch of little
*  things that turned out not to even be the things that are relevant now that brought them into it.
*  I wonder if, like you said, you're not a historian, so maybe there's a historian
*  out there that could really identify that moment, data-driven way, it could be like MySpace or
*  something like that, maybe the first major social network that really reached into
*  non-geek world or something like that. I think that's kind of the fallacy of historians though,
*  looking for some of those kind of primary dominant causes where so many of these things are,
*  like we see an exponential curve but it's not because one thing is going exponential, it's
*  because we have hundreds of little sigmoid curves overlapped on top of each other and they just
*  happen to keep adding up so that you've got something kind of going exponential at any given
*  point but no single one of them was the critical thing, there were dozens and dozens of things.
*  Seeing the transitions of stuff like as obviously MySpace giving way to other things but even like
*  blogging giving way to social media and getting resurrected in other guises and the things that
*  happened there. And the memes with the dancing baby GIF or whatever, all your base not belong to us,
*  whatever those early memes that led to the modern memes and the humor on the different evolution of
*  humor on the internet that I'm sure the historians will also write books about from the different
*  website that support to create the infrastructure for that humor like Reddit and all that kind of
*  stuff. So people will go back and they will name firsts and critical moments but it's probably
*  going to be a poor approximation of what actually happens and we've already seen like in the VR
*  space where it didn't play out the way we thought it would in terms of what was going to be like
*  the modern era of VR basically started with my E3 demo of Doom 3 on the Rift prototype. So we're
*  like first person shooters in VR, match made in heaven, right? And that didn't work out that way
*  at all. They have the most comfort problems with it and then the most popular virtual reality app
*  is Beat Saber which nobody predicted back then. What's that make you like from the first principles
*  if you were to like reverse engineer that? Why are these like silly fun games the most?
*  It actually makes very clear sense when you analyze it from hindsight and look at the
*  engineering reasons where it's not just that it was a magical quirky idea, it was something that
*  played almost perfectly to what turned out to be the real strengths of VR where the one thing that
*  I really underestimated importance in VR was the importance of the controllers. I was still thinking
*  we could do a lot more with the game pad and just the amazingness of taking any existing game,
*  being able to move your head around and look around that was really amazing. But the controllers
*  were super important but the problem is so many things that you do with the controllers just
*  suck. It feels like it breaks the illusion like trying to pick up glasses with the controllers
*  where you're like oh use the grip button when you're kind of close and it'll snap into your hand.
*  All of those things are unnatural actions that you do them and it's still part of the VR experience
*  but Beat Saber winds up playing only to the strengths. It completely hides all the weaknesses
*  of it because you are holding something in your hand, you keep a solid grip on it the whole time,
*  it slices through things without ever bumping into things. You never get into the point where
*  you know I'm knocking on this table but in VR my hand just goes right through it.
*  So you've got something that slices through so it's never your brain telling you oh I should
*  have hit something. You've got a lightsaber here, it's just you expect it to slice through everything.
*  Audio and music turned out to be a really powerful aspect of virtual reality where you're blocking
*  the world off and constructing the world around you and being something that can run efficiently
*  on even this relatively low-powered hardware and can have a valuable loop in a small amount of time
*  where a lot of modern games you're supposed to sit down and play it for an hour just to get
*  anywhere. Sometimes a new game takes an hour to get through the tutorial level and that's not good
*  for VR for a couple reasons. You do still have the comfort issues if you're moving around at all
*  but you've also got just you know discomfort from the headset, battery lifespan on the mobile versions.
*  So having things that do break down into three and four minute windows of play that turns out to be
*  very valuable from a gameplay standpoint. So it winds up being kind of a perfect storm of all of
*  these things that are really good. It doesn't have any of the comfort problems, you're not navigating
*  around, you're standing still, all the stuff flies at you. It has placed audio strengths,
*  it adds the whole fitness in VR. Nobody was thinking about that back in the at the beginning
*  and it turns out that that is an excellent daily fitness thing to be doing. If you go play
*  an hour of Beat Saber or Supernatural or something that is legit solid exercise
*  and it's more fun than doing it just about any other way there.
*  So that's kind of the arcade stage of things. If I were to say with my experience with VR,
*  the thing that I think is powerful is the, maybe it's not here yet, but the degree to which it is
*  immersive in the way that Quake is immersive. It takes you to another world. For me, because I'm a
*  fan of role playing games, the Elder Scrolls series, like Skyrim or even Daggerfall, it just
*  takes you to another world. And when you're not in that world, you miss not being there.
*  And then you just, you kind of want to stay there forever because life is shitty.
*  The whole point of my pitch for VR is that there was a time when we were kind of asked to come up
*  with like, what's your view about VR? And my pitch was that it should be better inside the
*  headset than outside. It's the world as you want it. And everybody thought that was dystopian and
*  oh, you're just going to forget about the world outside. And I don't get that mindset where the
*  idea that if you can make the world better inside the headset than outside, you've just improved the
*  person's life that has a headset that can wear it. And there are plenty of things that we just
*  can't do for everyone in the real world. Everybody can't have Richard Branson's private island,
*  but everyone can have a private VR island and it can have the things that they want on it.
*  And there's a lot of these kind of rivalrous goods in the real world that VR can just be
*  better at. We can do a lot of things like that that can be very, very rich. So yeah, I want the,
*  I think it's going to be a positive thing, this world where people want to go back into their
*  headset, where it can be better than somebody that's living in a tiny apartment, can have a
*  palatial estate in virtual reality. They can have all their friends from all over the world come over
*  and visit them without everybody getting on a plane and meeting in some place and dealing with
*  all the other logistics hassles. There is real value in the presence that you can get for remote
*  meetings. It's all the little things that we need to sort out, but those are things that we have line
*  of sight on. People that have been in a good VR meeting using workrooms where you can say,
*  oh, that was better than a Zoom meeting. But of course, it's more of a hassle to get into it.
*  Not everyone has the headset. Interoperability is worse. You can't have, you cap out at a certain
*  number. There's all these things that need to be fixed, but that's one of those things you can look
*  at and say, we know there's value there. We just need to really grind hard, file off all the rough
*  edges and make that possible. So you do think we have line of sight because there's a reason like
*  I do this podcast in person, for example, doing it remotely, it's not the same. And if you're
*  somebody who would ask me why it's not the same, I wouldn't be able to write down exactly why.
*  But you're saying that it's possible, whatever the magic is for in-person interaction,
*  that immersiveness of the experience, we are almost there.
*  Yes. So the idea of like, I'm doing a VR interview with someone. I'm not saying it's here right now,
*  but you can see glimmers of what it should be. And we largely know what would need to be fixed
*  and improved to, like you say, there's a difference between a remote interview, doing a podcast over
*  Zoom or something and face to face. There's that sense of presence, that immediacy, the super low
*  latency responsiveness, being able to see all the subtle things there, just occupying the same field
*  of view. And all of those are things that we absolutely can do in VR. And that simple case of
*  a small meeting with a couple of people, that's the much easier case than everybody thinks the
*  Ready Player One multiverse with a thousand people going across a huge bridge to amazing places.
*  That's harder in a lot of other technical ways. Not to say we can't also do that, but that's
*  further away and has more challenges. But this small thing about being able to have a meeting
*  with one or a few people and have it feel real, feel like you're there, like you have the same
*  interactions and talking with them, you get subtle cues as we start getting eye and face tracking and
*  some of the other things on high end headsets. A lot of that is going to come over. And it doesn't
*  have to be as good. This is an important thing that people miss where there was a lot of people
*  that, especially rich people, that would look at VR and say, it's like, oh, this just isn't that
*  good. And I'd say it's like, well, you've already been courtside backstage and on pit row and you've
*  done all of these experiences because you get to do them in real life. But most people don't get to.
*  And even if the experience is only half as good, if it's something that they never would have gotten
*  to do before, it's still a very good thing. And as we can just, we can push that number up over time,
*  it has a minimum viable value level when it does something that is valuable enough to people,
*  as long as it's better inside the headset on any metric than it is outside and people choose to go
*  there, we're on the right path. And we have a value gradient that I'm just always hammering on. We can
*  just follow this value gradient, just keep making things better rather than going for that one,
*  close your eyes, swing for the fences, kind of silver bullet approach.
*  Well, I wonder if there's a value gradient for in-person meetings, because if you get that right,
*  I mean, that would change the world. You don't need Ready Player One. But I wonder if there's
*  that value gradient you can follow along. Because if there is and you follow it, then there'll be a
*  certain like phase shift, a certain point where people will shift from Zoom to this. I wonder,
*  what are the bottlenecks? Is it software? Is it hardware? Is it all about latency?
*  So I have big arguments internally about strategic things like that, where I, like the next headset
*  that's coming out that we've made various announcements about is going to be a higher
*  end headset, more expensive, more features. Lots of people want to make those tradeoffs. I,
*  you know, we'll see what the market has to say about the exact tradeoffs we've made here.
*  But if you want to replace Zoom, you need to have something that everybody has.
*  So you like cheaper.
*  I like cheaper because also lighter and cheaper wind up being a virtuous cycle there where
*  expensive and more features tends to also lead towards heavier. And it just kind of goes,
*  it's like, let's add more features. The features are not, you know, they have physical presence
*  and weight and draw from batteries and all of those things. So I've always favored a lower
*  end, a cheaper, faster approach. That's why I was always behind the mobile side of VR rather than
*  the higher end PC headsets. And I think that's, you know, that's proven out well. But there's,
*  you know, ideally we have a whole range of things, but if you've only got one or two things,
*  it's important that those two things cover the, you know, the scope that you think is most
*  important. When we're in a world when it's like cell phones and there's 50 of them on the market
*  covering every conceivable ecological niche you want, that's going to be great, but we're not
*  going to be there for a while. Where are the bottlenecks? Is it the hardware or the software?
*  Yeah. So right now you can play, you can get work rooms on Quest and you can set up these things
*  and it's a pretty good experience. It's surprisingly good. I haven't tried it. It's surprisingly good.
*  Yeah. The voice latency is better on that than a lot better than a zoom meeting. So you've got a
*  better sense of immediacy there. The expressions that you get from the current hardware with just
*  kind of your controllers and your head is pretty realistic feeling. You've got a pretty good sense
*  of being there with someone with it. Are these like avatars of people? Like do you get to see
*  their body? Yeah. And they're sitting around a table? Yeah. And it feels better than zoom?
*  Yeah. Better than you'd expect for that. It is definitely, yeah, I'd say it's quite a bit better
*  than zoom when everything's working right, but there's still all the rough edges of the reason
*  zoom became so successful is because they just nailed the usability of everything. It's high
*  quality with a absolutely first rate experience and we are not there yet with any of the VR stuff.
*  I'm trying to push hard to get, I keep talking about it's like, it needs to just be one click
*  to make everything happen. And we're getting there in our home environment, not the whole
*  workroom's application, but the main home where you can now kind of go over and click and invite.
*  And it still winds up taking five times longer than it should, but we're getting close to that
*  where you click there, they click on their button and then they're sitting there in this good
*  presence with you. But latencies need to get a lot better. User interface needs to get a lot better.
*  Ubiquity of the headsets needs to get better. We need to have a hundred million of them
*  out there just so that everybody knows somebody that uses this all the time.
*  Well, I think it's a virtuous cycle because I do think the interface is the thing that makes or
*  breaks this kind of revolution. It's so interesting how like you said one click,
*  but it's also like how you achieve that one click. I don't know what is, can I ask a dark question?
*  Maybe let's keep it outside of Metta, but this is about Metta, but also Google and big company.
*  Are they able to do this kind of thing? It seems like, let me put on my cranky old man hat,
*  they seem to not do a good job of creating these user friendly interfaces as they get bigger and
*  bigger as a company. Like Google has created some of the greatest interfaces ever early on.
*  Creating Gmail, just so many brilliant interfaces and it just seems to be getting crappier and
*  crappier at that. Same with Metta, same with Microsoft. It seems to get worse and worse at
*  that. I don't know what it is because it becomes more conservative, careful, risk averse. Is that
*  why? Can you speak to that? It's been really eye opening to me working inside a tech titan where
*  I had my small companies and then we're acquired by a mid-sized game publisher and then
*  Oculus getting acquired by Metta and Metta has grown by a factor of many just in the
*  eight years since the acquisition. I did not have experience with this and it was interesting
*  because I remember previously my benchmark for use of resources was some of the government
*  programs I interacted with on the aerospace side and I remember thinking there was an
*  Air Force program and they spent $50 million and they didn't launch anything. They didn't even
*  build anything. It was just like they made a bunch of papers and had some parts in a warehouse and
*  nothing came of it. It's like $50 million. I've had to radically recalibrate my sense of how much
*  money can be spent with the over resources where on the plus side, VR has turned out. We've built
*  pretty much exactly what we just passed the 10-year mark then from my first demo of the Rift.
*  If I could have said what I wanted to have, it would have been a standalone inside out tracked
*  4K resolution headset that could still plug into a PC for high-end rendering and that's
*  exactly what we've got on Quest 2 right now. First of all, let's pause on that with me
*  being cranky and everything. What Metta achieved with Oculus and so on is incredible.
*  I mean, when I thought about the future of VR, this is what I imagined in terms of hardware,
*  I would say, and maybe in terms of the experience as well, but it's still not there somehow.
*  On the one hand, we did achieve it and win and we're a success right now, but the amount of
*  resources that have gone into it, it winds up getting cluttered up in accounting where Mark
*  did announce that they spent $10 billion a year on Reality Labs. Now, Reality Labs covers a lot.
*  VR was not the large part of it. It also had Portal and Spark and the big AR research efforts
*  and it's been expanding out to include AI and other things there where there's a lot going on
*  there, but $10 billion was just a number that I had trouble processing. I feel sick to my stomach
*  thinking about that much money being spent, but that's how they demonstrate commitment to this
*  where it's not more so than like Google goes and cancels all of these projects, different things
*  like that while Meta is really sticking with the funding of VR and AR is still further out with it.
*  There's something to be said for that. It's not just going to vanish, the work's going in.
*  All those resources could be applied more effectively because I see all these cases,
*  I point out these examples of how a third party that we're competing with in various ways,
*  there's a number of these examples and they do work with a tenth of the people that we do
*  internally. A lot of it comes from yes, the small company can just go do it while in a big company
*  you do have to worry about is there some SDK internally that you should be using because
*  another team's making it, you have to have your cross-functional group meetups for different
*  things, you do have more concerns about privacy or diversity and equity and safety of different
*  things, parental issues and things that a small startup company can just kind of cowboy off and
*  do something interesting. There's a lot more that is a problem that you have to pay attention to in
*  the big companies but I'm not willing to believe that we are within even a factor of two or four
*  of what the efficiency could be. I am constantly kind of crying out for it's like we can do better
*  than this. Yeah and you wonder what the mechanisms to unlock that efficiency are.
*  There is some sense in a large company that like an individual engineer might not believe that they
*  can change the world maybe you delegate a little bit of the responsibility to be the one who
*  changes the world in a big company I think but the reality is like the world will get changed
*  by a single engineer anyway so if whether inside Google or inside a startup it doesn't matter it's
*  just like Google and Metta needs to help those engineers believe they're the ones that are going
*  to decrease that latency. It'll take one John Carmack like the 20 year old Carmack that's inside
*  Metta right now to change everything. And I try to point that out and push people it's like try to
*  go ahead and when you see some because there is you get the silo mentality where you're like okay I
*  know something's not right over there but that's I'm staying in my lane here and there's a couple
*  people that I can you know I can think about that are willing to just like hop all over the place
*  and man I treasure them the people that are just willing to they're fearless you know they will go
*  over and they will go rebuild the kernel and change this distribution and go in and hack the
*  firmware over here to to get something done right and that is relatively rare you know there's
*  thousands of developers and you've got a small handful that are willing to operate at that level
*  and you know and it's potentially risky for them the the politics are you know are real in a lot
*  of that and I'm in the you know very much the privileged position of I am you know I'm more
*  or less untouchable there where I've been dinged like twice for it's like you said something
*  insensitive in that post and I and you should probably not say that I am but for the most part
*  yes I you know I get away with I every week I'm posting something you know pretty loud and
*  opinionated in you know internally and I think that's useful for the company but I'm yeah it's
*  not it's rare to have a position like that and I can't necessarily offer advice for how someone
*  can do that I've well you could offer advice to a company in general to give a little bit of freedom
*  for the young wild like the wildest ideas come from the young minds and so you need to give the
*  young minds freedom to think big and wild and crazy and for that they have to be opinionated
*  they have to be they have to think crazy ideas and thoughts and pursue them with a full passion
*  without being slowed down by bureaucracy or managers and all that kind of stuff
*  obviously startups really empower that but big companies could too and that's that's a design
*  challenge for company for big companies to see how can you enable that how can you empower that
*  big company there are so many resources there and they do you know amazing things do get
*  accomplished but there's so much more that could come out of that and you know I'm hope I'm always
*  hopeful I'm an optimist in almost everything you know I think things can get better I think that
*  they can improve things that you go through a path and you're learning kind of what does and doesn't
*  work and I'm not I'm not ready to be fatalistic about the kind of the outcome of any of that
*  Me neither I know too many good people inside of those large companies that are incredible
*  you have a friendship with Elon Musk often when I talk to him he'll bring up how incredible of an
*  engineer and just a big picture thinker you are his huge amount of respect for you I just I've
*  never been a fly in the wall between a discussion between the two of you I just wonder is there
*  something you guys debate argue about discuss is there some interesting problems that the two of you
*  think about you come from different worlds maybe there's some intersection
*  in the in aerospace maybe there's some intersection in your new efforts in artificial
*  intelligence in terms of thinking is there something interesting you could say about sort
*  of the debates the two of you have so I think in some ways we do have a kind of similar background
*  where we're almost exactly the same age and we had kind of similar programming backgrounds on
*  the personal computers and you know even some of the the books that we would read and things that
*  would kind of turn us into the people that we are today and I think there is a degree of
*  sensibility similarities where you know we kind of call bullshit on the same things and kind of see
*  the same opportunities in different technology and there's that sense of you know I always talk about
*  the speed of light solutions for things and he's thinking about kind of minimum manufacturing and
*  engineering and operational standpoints for things and so I mean I first met Elon right at the start
*  of the aerospace era where I wasn't familiar with you know I was still in my game dev bubble I really
*  wasn't familiar with all the startups that were going and being successful and what went on with
*  PayPal and all of his different companies but you know I met him as I was starting to do armadillo
*  aerospace and you know he came down with kind of his right hand propulsion guy and we talked about
*  rockets you know what can we what can we do with this and it was kind of specific things about
*  like how are how are our flight computers set up what are different propellant options
*  and you know what can happen with different different ways of putting things together
*  and then in some ways he was certainly the biggest player in the sort of alt space community that was
*  going on in the early 2000s he was the most well funded although you know his funding in the larger
*  scheme of things compared to a like a NASA or something like that was really tiny it was a
*  lot more than I had at the time I but it was interesting I had a point years later when I
*  realized okay my like my financial resources at this point are basically what Elon's was when he
*  went all in on SpaceX and Tesla and there's I think in many corners he does not get the respect
*  that he should about being a wealthy person that could just retire and he went all in where he was
*  really going to you know he could have gone bust and there's plenty of people you look at the
*  you know the sad athletes or entertainers that had all the money in the world and blew it he
*  could have been the the business case example of that but I'm you know the the things that he was
*  doing space exploration electrification of transportation on solar city type things these
*  are big world level things and I have a great deal of admiration that he was willing to throw
*  himself so completely into that because you know in contrast with myself I was doing armadillo
*  aerospace with this tightly bounded it was John's crazy money at the time that had a finite limit
*  on it it was never going to impact me or my family if it completely failed and I was still
*  hedging my bets working at id software at the time when he had been you know really all in there
*  and I have a huge amount of respect for that and people do not the other thing I get irritated
*  with is people that say it's like oh Elon's just just a business guy you know he just got
*  like he was gifted the money and he's just kind of investing in all of this when he was really
*  deeply involved in a lot of the decisions you know not all of them were perfect but I you know he
*  cared very much about engine material selection propellant selection and I feel for years he'd
*  be kind of telling me it's like get off that hydrogen peroxide stuff it's like you know liquid
*  oxygen is the you know is the only proper oxidizer for this and I am you know and like the times that
*  I've gone through the factories with him we're we're talking very detailed things about like how
*  this weld is made you know how this sub assembly goes together I you know what are like startup
*  shut down behaviors of the different things so he is you know really in there at a very detailed
*  level and I think that he is the the best modern example now of someone that tries to that can
*  effectively micromanage some decisions on things on both tesla you know and space x to some degree
*  where he cares enough about it I worry a lot that he stretched too thin that you get boring company
*  and neurolink and twitter and all the other possible things there where I know I've got I've got limits
*  on how much I can pay attention to that I have to kind of box off different amounts of time
*  and I look back at like at my aerospace side of things it's like I did not go all in on that I
*  did not commit myself at a level that it would have taken to be successful there and I yeah and
*  it's kind of a weird thing just like having a discussion with he's the richest man in the
*  world right now but he I you know he operates on you know on a level that is still very much in
*  my wheelhouse on a technical side of things so they're doing that systems level type of thinking
*  where you can go to the low level details and go up high to the big picture do you think in the
*  aerospace arena in the next five ten years do you think we're going to put a human on mars like what
*  do you think is the interesting no idea in fact I made a bet with someone with a group of people
*  kind of this about whether boots on mars by 2030 and this was kind of a fun you know a fun story
*  because I was at an intel sponsored event and we had a bunch of just world-class brilliant people
*  and we were talking about computing stuff but the after dinner conversation was like what are some
*  other things how they're going to go in the future and one of the ones tossed up on the whiteboard
*  was like boots on mars by 2030 and most of the people in the room thought yes you know they
*  thought that like space x is kicking ass we've got all this possible stuff i seems likely that
*  it's going to go that way and i said no i think less than 50 chance that it's going to make it
*  there and people you know were kind of like oh i you know why the pessimism or whatever and of
*  course i'm an optimist at almost everything but for me to be the the one kind of outlier saying
*  no i don't think so then i started saying some of the things i said well let's be concrete about it
*  let's bet ten thousand dollars that it's not going to happen and this was this was really
*  a startling thing to see that i again room full of brilliant people but as soon as like money came
*  on the line and they were like do i want to put ten thousand and i was not the richest person in
*  the room there are people much better off than there's a spectrum but i am you know as soon as
*  they started think it's like oh i could lose money by by keeping keeping my position right now
*  and all these engineers they engage their brain they started thinking it's like okay
*  launch windows uh launch delays like how many times would it take to get this right what
*  historical precedents do we have and i and then it mostly came down to it's like well what about
*  in transit by 2030 and then i if you know what about i you know different things or would you
*  have would you go for 2032 but one of the people did go ahead and was optimistic enough to make a
*  bet with me so i i have a ten thousand dollar bet that by 2030 i think it's going to happen
*  shortly thereafter i think there will probably be infrastructure on mars by 2030 but i don't
*  think that we'll have humans on mars on 2030 i think it's possible but i think it's less than
*  a 50 chance so i felt safe making that bet well i think you had an interesting point uh correct
*  me if i'm wrong that's a dark one that's um that should perhaps help people appreciate elon musk
*  which is in this particular effort elon is a critical is critical to the success spacex seems
*  to be uh critical to 20 you know uh humans on mars by 2030 or thereabouts so if something
*  happens to you on um then all of this collapses and this is in contrast to the the other ten
*  thousand dollar bet i made kind of recently and that was self-driving cars at like a level five
*  running around uh cities and people have kind of nitpicked that that we probably don't mean
*  exactly level five but the guy i'm having the bet with i is we're going to be we know what we mean
*  about this jeff fatwood yeah coding horror and stackover flow and all but i yeah i mean it's just
*  he doesn't think that people are going to be riding around in robo taxis in 2030 i in major
*  cities just like like you take an uber now and i think it will you think it will and i think and
*  the difference is everybody looks at this it's like oh but tesla's been wrong for you they've
*  been promising it for years and it's not here yet and the reason this is different than the
*  bet with mars is mars really is more than is comfortable a bet on elon musk i am you know that
*  is you know that is his thing and he is really going to move heaven and earth to try to to make
*  that happen and perhaps not even space x yeah perhaps just elon muck yeah because if if elon
*  went away and space x went public and got a board of directors i there are more profitable things
*  they could be doing than focusing on human presence on mars so this really is a sort of
*  personal thing there and in contrast with that self-driving cars have a dozen credible companies
*  working really hard and while yes it's going slower than most people thought it would
*  betting against that is a bet against almost the entire world in terms of all of these companies
*  that have all of these incentives it's not just you know one guy's passion project i and i do think
*  that it is solvable i although there's i recognize it's not 100 chance because it's possible the long
*  tail of self-driving problems winds up being an a gi complete problem i think there's plenty of
*  value to mine out of it with narrow ai and i think that it's you know it's going to happen probably
*  more so than people expect but it's that whole sigmoid curve where you over you know you overestimate
*  the near-term progress you underestimate the long-term progress and i think self-driving is
*  going to be like that and i think 2030 is still a pretty good bet yeah unfortunately
*  self-driving is a problem that is safety critical meaning that if if you don't do it well people get
*  hurt but the other side of that is people are terrible drivers so it is not going to be that's
*  probably going to be the argument that gets it through is like we can save 10 000 lives a year
*  by taking imperfect self-driving cars and letting them take over a lot of driving responsibilities
*  it's like was it 30 000 people a year die in auto accidents right now in america and a lot of those
*  are preventable and the problem is you'll have people that every time a tesla crashes into
*  something you've got a bunch of people that literally have vested interests shorting tesla
*  to come out and make it the worst thing in the world and people will be fighting against that but
*  optimist in me again i think that we will have systems that are statistically safer than human
*  drivers and we will be saving thousands and thousands of lives every year when we can hand
*  over more of those responsibilities to it i do still think as a person who studied this problem
*  deeply from a human side as well it's still an open problem how good slash bad humans are driving
*  it's a kind of funny thing we say about each other all humans suck at driving
*  um everybody except you of course like we think we're good at driving but i after really studying it
*  i i think you start to notice you know because i watched uh hundreds of hours of humans driving
*  with the projects of this kind of thing you've noticed that even with the distraction even with
*  everything else humans are able to to do some incredible things with the the with the attention
*  even when you're just looking at the smartphone just to get cues from the environment to make
*  last second decisions to use instinctual type of decisions that actually save your ass time and
*  time and time again and are able to do that with so much uncertainty around you in such tricky
*  dynamic environments i don't know i don't i don't know exactly um how hard is it to beat that kind
*  of skill of common sense reasoning this is one of those interesting things that there have been a
*  lot of studies about how experts in their field usually underestimate the progress that's going
*  to happen because an expert thinks about all the problems they deal with and they're like damn i'm
*  going to have a hard time solving all of this and they filter out the fact that they are one expert
*  in a field of thousands and you know you think about yeah i can't do all of that and you sometimes
*  forget about the scope of the the ecosystem that you're embedded in and if you think back eight
*  years very specifically the state of ai and machine learning where was that we we had just gotten
*  resnets probably at that point and you look at all the amazing magical things that have happened
*  in eight years and they do kind of seem to be happening a little faster in recent years also
*  and you project that eight more years into the future where again i think there's a 50% chance
*  we're going to have signs of life of a gi you know which we can put through driver's ed if we need to
*  to actually build self-driving cars and i think that the narrow systems are going to to have real
*  value demonstrated well before then so signs of life in a gi you've mentioned that okay first of all
*  you're one of the most brilliant people on this earth you could be solving a number of different
*  problems as you've mentioned your mind was attracted to nuclear energy obviously virtual
*  reality with the metaverse is something you could have a tremendous impact on so i do want to say a
*  quick thing about nuclear energy where i you know this is something that i really this so precisely
*  feels like aerospace before spacex where from everything that i know about all of these i the
*  physics of this stuff hasn't changed and the reasons why things are expensive now are not
*  fundamental i somebody should be going into i really hard elon musk style at vision economical
*  vision not fusion where the fusion is the kind of the the darling of people that want to go and
*  do nuclear because it doesn't have the taint that vision has in a lot of people's minds
*  but it's an almost absurdly complex thing where nuclear fusion as you look at the the tokamaks
*  or any of the things that people are building and it's doing all of this infrastructure just at the
*  end of the day to make something hot to that you can then turn into energy through a conventional
*  power plant and all of that work which we think we've got line of sight on but even if it comes
*  out then you have to do all of that immensely complex expensive stuff just to make something
*  hot where nuclear fission is basically you put these two rocks together and they get hot all by
*  themselves that is just that much simpler it's just orders of magnitude simpler and the actual
*  rocks the refined uranium is not very expensive it's a couple percent of the the cost of electricity
*  that's why i made that point where you could have something which was five times less efficient
*  than current systems and if the rest of the plant was a whole bunch cheaper you could still be
*  super super valuable so how much of the pie do you think could be solved by nuclear energy by
*  fission so how how much could it become the primary source of energy on earth it could be most of it
*  like the reserves of uranium as it stands now could not power the whole earth but i am you know
*  you get into breeder reactors and thorium and things like that that you do for conventional
*  fission there is enough for for everything now i mean solar photovoltaic has been amazing you know
*  it's i i one of my current projects is working on an off-grid system and it's been fun just kind of
*  again putting my hands on all the stripping the wires and wiring things together and doing all
*  of that and just having followed that a little bit from the outside over the last couple decades
*  there's been semiconductor like magical progress in what's going on there so i'm all for all of
*  that but it doesn't solve everything and nuclear really still does seem like the smart money bet
*  for what you should be getting for baseband on a lot of things and solar may be cheaper for
*  i you know peeking over air conditioning loads during the summer and things that you can push
*  around in different ways but it's one of those things that's it's just strange how we've had
*  the technology sitting there but these non-technical reasons on the social optics of it
*  has been this major forcing function for something that you know really should be at the the
*  cornerstone of all of the world's concerns with energy it's interesting how the non-technical
*  factors have really dominated something that is so fundamental to kind of the existence of the human
*  race as we know it today and much of the troubles of the world including wars in different parts of
*  the world like ukraine is energy-based and uh yeah it's just sitting right there to be solved
*  that said uh i mean to me personally i think it's clear that if a gi were to be achieved that would
*  change the course of human history so a gi wise i was you know i was making this decision about
*  what do i want to focus on after vr and i'm still working on vr regularly i spend a day a week
*  uh kind of consulting with meta and i you know boz styles me the consulting cto is kind of like
*  the sherlock holmes that comes in and consults on some of the specific tough issues and i'm still
*  pretty passionate about all of that uh but i have been figuring out how to compartmentalize and i
*  force that into a smaller box to work on some other things and i did come down to this decision
*  between working on uh economical nuclear fission or artificial general intelligence
*  and uh the fission side of things i've i've got a bunch of interesting things going that way
*  but it would take that would be a fairly big project thing to do i don't think it needs to
*  be as big as people expect i do think something original spacex sized i you build it power your
*  building off of it and then the government i think will come around to what you need to
*  everybody loves an existence proof i think it's possible somebody should be doing this
*  but it's going to involve some politics it's going to involve decent sized teams and a bunch
*  of this cross-functional stuff that i don't love while the artificial general intelligence side of
*  things um it seems to me like this is the highest leverage moment for potentially a single individual
*  potentially in the history of the world where the things that we know about the brain about
*  what we can do with artificial intelligence uh nobody can say absolutely on any of these things
*  but i am not a madman for saying that it is likely that the code for artificial general intelligence
*  is going to be tens of thousands of lines of code not millions of lines of code this is code that
*  conceivably one individual could write unlike writing a new web browser operating system
*  and based on the progress that ai has machine learning has made in the recent decade it's likely
*  that the important things that we don't know are relatively simple there's probably a handful of
*  things and my bet is that i think there's less than six key insights that need to be made each
*  one of them can probably be written on the back of an envelope we don't know what they are but
*  when they're put together in concert with gpus at scale and the data that we all have access to
*  that we can make something that behaves like a human being or like a living creature and that
*  can then be educated in whatever ways that we need to get to the point where we can have universal
*  remote workers where anything that somebody does mediated by a computer and doesn't require
*  physical interaction that an agi will be able to do we can already simulate the you know the
*  equivalent of the zoom the zoom meetings with avatars and synthetic deep fakes and whatnot
*  we can definitely do that we have superhuman capabilities on any narrow thing that we can
*  that we can formalize and make a loss function for but there's things we don't know how to do now
*  but i don't think they are unapproachably hard now that's incredibly hubristic to say that
*  it's like but i think that what i said a couple years ago is a 50 chance that somewhere there will
*  be signs of life of agi in 2030 and i've probably increased that slightly i may be at 55 60 now
*  because i do think there's a little sense of acceleration there so i wonder what the and by
*  the way you also written that i i bet with hindsight we will find that clear antecedents of all the
*  critical remaining steps for a gi are already buried somewhere in the vast literature of today
*  so the ideas are already there i think that's likely the case one of the things that appeals
*  to so many people including me about the promise of a gi is we know that we're only drinking from
*  a straw from the the fire hose of all the information out there i mean you look at just in a
*  very narrowly bounded field like machine learning like you can't read all the papers that that come
*  out all the time you can't go back and read all the clever things that people did in the 90s or
*  earlier that people have forgotten about because they didn't pan out at the time when they were
*  trying to do them with 12 neurons and so that this idea that yeah i think there are gems buried in
*  some of the older literature that was not the path taken by everything and you can see a kind of herd
*  mentality on the things that happen right now it's almost funny to see like oh google does
*  something and open ai does something meta does something and you know they're the same people
*  that all talk to each other and they all one-upping each other and they're all capable of implementing
*  each other's work given a month or two after somebody has an announcement of that but there's
*  a there's a whole world of possible approaches to machine learning and i think that we probably will
*  in hindsight go back and see it's like yeah that was kind of clearly predicted by this early paper
*  here you know and this turns out that if you do this and this and take this result from
*  animal training and this thing from neuroscience over here and put it together and set up this
*  curriculum for them to learn in that that's kind of what it took you don't have too many people now
*  that are still saying it's not possible or it's going to take hundreds of years and 10 years ago
*  you would get you would collect get a collection of experts and you would have a decent chunk on
*  the margin that either say not possible or a couple hundred years might be centuries
*  and the median estimate would be like 50 70 years and it's been coming down and i know with me saying
*  eight years for something that still puts me on the optimistic side but it's not crazy out in the
*  fringes and just being able to look at that at a meta level about the trend of the the trend of the
*  predictions going down there the idea that something could be happening relatively soon
*  now i do not believe in fast takeoffs you know that's one of the safety issues that people say
*  it's like oh it's going to go boom and the ai is going to take over the world there's a lot of
*  reasons i don't think that's a credible position and i think that we will go from a point where
*  we start seeing things that that credibly look like look like animals behaviors and i have a
*  human voice box wired into them it's like i tried to get elon to say it's like your your
*  pig at neurolink give it a human voice box and let it start learning human words i think that
*  you know i think animal intelligence is closer to human intelligence than a lot of people like to
*  think and i think that culture and modalities of io are make the gulf seem a lot bigger than
*  it actually is there's just that smooth spectrum of how the brain developed and
*  cortexes and scaling of different things going on there cultural modalities of ios yes language is
*  sort of lost in translation conceals a lot of intelligence and so you're when you think about
*  signs of life or a gi you're thinking about human interpretable signs so the example i give it if
*  we get to the point where you've got a learning disabled toddler some some kind of real special
*  needs child that can still interact with their favorite tv show and video game and can be trained
*  and learn in some appreciably human-like way at that point you can deploy an army of engineers
*  cognitive scientist education developmental developmental education people and you've got
*  so many advantages there unlike real education where you can do rollbacks and ab testing and you
*  can find a golden path through a curriculum of different things if you get to that point
*  learning disabled toddler i think that it's i it's going to be a done deal do you think we'll
*  we'll know when we see it so there's there's been a lot of really interesting general learning
*  progress from deep mind open the eye a little bit too i tend to believe that tesla autopilot
*  deserves a lot more credit than it's getting for making progress on the general on sort of
*  on the doing the multitask learning thing and increasing the number of tasks and automating that
*  uh process of uh sort of learning from the edge discovery in edge cases and learning from the edge
*  cases that is it's really approaching from a different angle the general learning problem
*  of a gi but the more clear approach comes from deep mind where you have these kind of game
*  situations and you build systems there but i don't know people seem to be quite
*  um there will always be people that just won't believe it and i fundamentally don't care i mean
*  i don't care if they don't believe it i you know when it starts doing people's jobs and i mean
*  i don't care about the philosophical zombie argument at all absolutely but will you do you
*  think you will notice that something special has happened here and or um because to me i've been
*  noticing a lot of special things i think a lot of credit should go to deep mind for alpha zero
*  that was truly special the self-play mechanisms achieve sort of solve problems that used to be
*  thought unsolvable like the game of go also i mean protein folding starting to get into that space
*  where learning is doing at first there's not it wasn't end-to-end learning and now it's end-to-end
*  learning of the of a very difficult previously thought unsolvable problem of protein folding
*  and so um yeah do where where do you think would be a really magical moment for you
*  there have been incredible things happening in recent years like you say all of the things from
*  deep mind and open ai that have been huge showpiece things but when you really get down to it
*  you read the papers and you look at the way the models are going you know it's it's still like a
*  feed forward you push something in something comes out i on the end i mean maybe there's
*  diffusion models or montecarlo tree rollouts and different things going on but it's not a being
*  it's not close to a being i am that's that's going through a you know a lifelong learning process
*  do you want something that kind of gives signs of a being like what's the difference between
*  a neural network a feed forward neural network and a being was where's the fundamentally the brain
*  is a recurrent neural network generating an action policy i mean it's implemented on a biological
*  substrate and and it's interesting thinking about things like that where we know fundamentally the
*  brain is not a convolutional neural network or a transformer those are specialized things that
*  that are very valuable for what we're doing but it's not the way the brain's doing now
*  i do think consciousness and ai in general is a substrate independent mechanism where it doesn't
*  have to be implemented the way the brain is but if you've only got one existence proof there's
*  certainly some value in caring about what it says and does i am and so the the idea that anything
*  that can be done with a narrow ai that you can quantify up a loss function for a reward mechanism
*  you're almost certainly going to be able to produce something that's more resource effective
*  to train and deploy and use in an inference mode you know train a whole lot using an inference but
*  i a living being is going to be something that's a continuous lifelong learned task agnostic thing
*  and so the lifelong learning is really important too and the long-term memory so memory is a
*  as a big part of that puzzle and we've got you know again i have all the respect in the world
*  for the amazing things that are being done now but sometimes they can be taken a little bit out
*  of context with things like like there's some smoke and mirrors going on like the gato the recent
*  work the multi-task learning stuff you know it's amazing that it's the one it's one model that
*  plays all the atari games i am as well as doing all of these other things but i of course it didn't
*  learn to do all of those it was instructed in doing that by other reinforcement learners going
*  through and doing that and even in the case of all the games it's still going with a specific
*  hand coded reward function in each of those atari games where it's not that you know how does it
*  it just wants to spend its summer afternoon playing atari because that's the most interesting thing
*  for it so it's again not a general it's not learning the way humans learn and there's i
*  believe a lot of things that are challenging to make a loss function for that you can train
*  through these existing conventional things we're going to chip away at all the things that people
*  do i am that we can turn into narrow ai problems and billions of probably trillions of dollars of
*  value are going to be created by that but there's still going to be a set of things and we've got
*  questionable cases like the self-driving car where it's possible it's not my bet but it's
*  it's plausible that the long tail could be problematic enough that that really does require
*  a full-on artificial general intelligence i the counter argument is that data solves almost
*  everything is an interpolation problem if you have enough data and tesla may be able to get enough
*  data from all of their deployed stuff to be able to work like that but maybe not and there are all
*  the other problems about like say you want to have a strategy meeting and you want to go ahead and
*  bring in all of your remote workers and your consultants and you want a world where some of
*  those could be ai's that are you know that are talking and interacting with you in a an area
*  that is too murky to have a crisp loss function but they still have things that on some level
*  they're they're rewarded on some internal level for building a valuable to humans kind of life
*  and ability to interact with things see i still think that uh self-driving car solving that
*  problem will take us very far towards a gi you might not need a gi but i am really inspired by
*  what autopilot is doing oh waymo so these some of the other companies i think waymo leads the way
*  there is also really interesting but they don't have quite as ambitious of an effort in terms of
*  learning-based sort of data hungry approach to driving which i think is very close to the kind
*  of thing that would take us far towards a gi and it's a it's a funny thing because as far as i can
*  tell elon is completely serious about all of his concerns about a gi you know being an existential
*  threat and you know i i tried to draw him out to talk about ai and he just didn't want to and i
*  think that you know i get that little fatalistic sense from him it's weird because his company
*  could very well be the leading company leading towards a lot of that where i tesla being a super
*  pragmatic company that's doing things because they really want to solve this actual problem it's a
*  different vibe than the the research oriented companies where it's a great time to be an ai
*  researcher you've got your pick of trillion dollar companies that will you know that will pay you to
*  kind of work on the problems you're interested in but that's not necessarily driving hard towards
*  the the core problem of a gi is something that's going to produce a lot of value by doing things
*  that you know that people currently do or would like to do i mean i have a million questions to you
*  about your ideas about a gi but do you think it needs to be embodied do you think it needs
*  to have a body to start to notice the signs of life and to develop the kind of system that's able
*  to reason perceive the world in the way that an a gi should and uh act in the world so should we
*  be thinking about robots or can this be achieved in a purely digital so i have a clear opinion on
*  that and that's that no it does not need to be embodied in the physical world where you could
*  say most of my career is about making simulated virtual worlds you know in games or virtual reality
*  and so on a fundamental level i believe that you can make a simulated environment that provides
*  much of the value of what the real environment does and restricting yourself to operating at
*  real time in the physical world with physical objects i think is an enormous handicap i mean
*  that's one of the real lessons driven home by all my aerospace work is that i you know reality is a
*  bitch in so many ways there we're dealing with all the mechanical components like everything fails
*  murphy's law even if you've done it right before on your fifth one it might come out differently
*  so yeah i think that anybody that that is all in on the embodied aspect of it they are tying a
*  huge weight to their ankles and i think that i i would almost count them out anybody that's making
*  that a cornerstone of their belief about it i would almost write them off as being worried
*  about them getting to a gi first i was very surprised that elon's big on the uh the humanoid
*  robots i mean like the nasa robonaut stuff was always almost a gag line like what are you doing
*  people well that's very interesting because i he has a very pragmatic view of that that's just the
*  uh a way to solve a particular problem in a factory now i do think that once you have an agi
*  robotic bodies humanoid bodies are going to be enormously valuable i just don't think they're
*  helpful getting to agi well he has a very sort of practical view which i disagree with and argue
*  with him but it's a practical view that there's you know you could transfer the the problem of
*  the problem of driving to the problem of uh robotic manipulation because so much of it is
*  perception it's perception and action and it's just a different context and so you can apply all the
*  same kind of data engine learning processes to a different environment and so why not you apply
*  to the humanoid robot environment but um i think i i do think that there's a certain magic to the
*  body robot that may be the thing that finally convinces people yes but again i don't really
*  care that much about convincing people you know the the world that i'm looking towards is you know
*  you i you you go to the website and say i want five frank 1a's to you know to work on my team
*  today and they all spin up and they start showing up in your zoom meetings to push to push back but
*  also to agree with you but first to push back i do think you need to convince people for them to
*  welcome that thing into your into their life i think there's enough businesses that operate on
*  an objective kind of profit loss sort of basis that i mean if you look at how many things again
*  talking about the the world as an evolutionary space there when you do have free markets and
*  you have entrepreneurs uh you are going to have people that are going to be willing to go out and
*  try whatever crazy things and when it proves to be beneficial you know there's fast followers in all
*  sorts of places yeah and and you're saying that i mean you know quake and vr is a kind of embodiment
*  but just in a digital world and if if you're able to demonstrate if you're able to do something
*  productive in that kind of digital reality uh then then a gi doesn't need to have a body yeah
*  it's like one of the really practical technical questions that i kind of keep arguing with myself
*  over if you're doing a training and learning and you've got like you can watch sesame street you
*  can play master system games or something is it enough to have just a video feed that that is that
*  video coming in or should it literally be on a virtual tv set in a virtual room even if it's
*  you know a simple room just to have that sense of you're looking at a 2d projection on a screen
*  versus having the screen beamed directly into your retinas and i you know i think it's possible to
*  maybe get past some of these signs of life of things with the uh just kind of projected
*  directly into the receptor fields but eventually for more uh kind of human emotional connection
*  for things probably having some vr room with a lot of screens in it for the ai to be learning in
*  is likely helpful it may be a world of different ai's interacting with each other self-play i do
*  think is one of the critical things where socialization wise one of the other limitations i set
*  for myself thinking about thing these is i i need something that is at least potentially real time
*  because i want it's nice you can always slow down time you can run on a subscale system and
*  and test an algorithm at some lower level and if you've got extra horsepower running it faster
*  than real time is a great thing but i want to be able to i am to have the ai's either socially
*  interact with each other or critically with actual people your sort of child development
*  psychiatrist that comes in and and interacts and does the the good boy bad boy sort of thing i as
*  they're going through and exploring different things and it's nice to i come back to the value
*  of constraints in a lot of ways and if i say well one of my constraints is real time operation i
*  mean it might still be a huge data center full of computers but it should be able to interact on a
*  zoom meeting with people and that's how you also do start convincing people even if it's not a robot
*  body moving around which eventually gets to irrefutable levels but if you can go ahead and
*  not just type back and forth to a gpt bot on something but you're literally talking to them
*  in an embodied over zoom form and working through problems with them or exploring situations
*  having conversations that are fully stateful and learned i think that i think that that's a
*  valuable thing so i do keep all of my eyes on on things that can be implemented within sort of
*  that 30 frames per second i kind of work and i think that's feasible do you think the most
*  compelling experiences that first will be for pleasure or for business as they ask in airports
*  so uh meaning is is it if it's interacting with ai agents will it be sort of uh like friends
*  um entertainment almost like a therapist or whatever that kind of interaction or is it in
*  the business setting something like you said brainstorming different ideas sort of this is
*  all a different formulation of kind of a touring test or the spirit of the original touring test
*  where do you think the biggest benefit will first come so it's going to start off hugely expensive
*  i mean you're gonna if we're still all guessing about what compute is going to be necessary i
*  fall on the side of i don't think you run the numbers and you're like 86 billion neurons 100
*  trillion synapses i don't think those all need to be weights i don't think we need models that are
*  quite that big evaluated quite that often you know i based that on we've we've got reasonable
*  estimates of what some parts of the brain do we don't have the we don't have the neocortex
*  formula but we kind of get some of the other sensory processing and it doesn't feel like we
*  need to we can simulate that in computers for less weights but still it's probably going to be
*  thousands of gpus to be running you know a human level a gi depending on how it's implemented that
*  might give you sort of a clan of 128 kind of run in batch people depending on whether there's
*  sparsity in the way the the weights and things are set up if it is a reasonably dense thing then just
*  the memory bandwidth trade-offs means you get 128 of them at the same time and either it's all
*  feeding together learning in parallel or kind of all running together kind of talking to a bunch
*  of people but still if you've got thousands of gpus necessary to run these things it's going to
*  be kind of expensive where it might start off on thousand dollars an hour for your you know even
*  post development or something for that which would be something that you would only use for a business
*  if you know something where you think they're going to help you make a strategic decision
*  or point out something super important but i also am completely confident that we will have another
*  factor of a thousand in cost performance increase in a gi type calculations not in general computing
*  necessarily but there's so much more that we can do with packaging making those right trade-offs
*  all those same types of things that in the couple next couple decades thousand x easy and then you're
*  down to a dollar an hour and then you're kind of like well i should have an entourage of ai's that
*  are you know following me around helping me out on anything that i want them to do that's one
*  interesting trajectory but i'll i'll i'll push back because i have um so uh for in that case if
*  you want to pay thousands of dollars it should actually provide some value i think it's easier
*  for cheaper to provide for uh to provide value via a dumb ai uh that will take us towards a gi
*  to just have a friend i think there's an ocean of loneliness in the world and i think an effective
*  friend that doesn't have to be perfect that doesn't have to be intelligent that has to be empathic
*  having emotional intelligence having ability to remember things having ability to listen most of
*  us don't listen to each other one of the things that love and when you care about somebody when
*  you love somebody is when you listen and that is something we treasure about each other and
*  if an ai can do that kind of thing um i think that provides a huge amount of value and very importantly
*  provides value in its ability to listen and understand versus provide really good advice
*  i think providing really good advice is very different is is another next level step that would
*  i think is just easier to to do companionship yeah i wouldn't disagree i mean i think that
*  there's very few things that i would argue can't be reduced to a i some kind of a narrow ai i think
*  we can do trillion dollars of value easily and all the things that can be done there and a lot of it
*  can be done with smoke and mirrors without having to go the whole thing i mean there's going to be
*  the equivalent of the doom i the doom version for the a gi that's not really a gi it's all
*  smoke and mirrors but it happens to do another valuable things that it's enormously useful and
*  valuable to people but at some point you do want to get to the point where you have the fully
*  general thing and you stop making bespoke specialized systems for each thing and you wind up
*  start using the higher level language instead of writing everything in assembly language
*  what about consciousness the c word do what do you think that's fundamental to solving a gi or is
*  it a quirk of human cognition so i think most of the arguments about consciousness don't have a
*  whole lot of merit i think that consciousness is kind of the way the brain feels when it's operating
*  i am yes and this idea that you know i do generally subscribe to sort of the pandemonium
*  theories of consciousness where there's all these things bubbling around and i think of them as
*  kind of slightly randomized sparse distributed memory bit strings of things that are kind of
*  happening recalling different associative memories and eventually you get some level of consensus and
*  it bubbles up to the point of being a conscious thought there and the little bits of stochasticity
*  that are sitting on in high in this as it cycles between different things and recalls different
*  memory that's largely our imagination and creativity um so i don't think there's anything
*  deeply magical about it certainly not symbolic i think it is generally the flow of these
*  associations drawn up with stochastic stochastic noise overlaid on top of them i think so much of
*  that is like it depends on what you happen to have in your field of view as some other thought was
*  occurring to you that overlay and blend into the next key that queries your memory for things and
*  that kind of determines how you know how your chain of consciousness goes so that's kind of
*  the qualia the subjective experience of it is not is not essential for intelligence i don't think so
*  i don't think there's anything really important there what about some other human qualities like
*  fear of mortality and stuff like that like um the fact that this ride ends is that is that important
*  like you you know we talked so much about this conversation about the value of deadlines and
*  constraints um do you think that's important for intelligence that's actually a super interesting
*  angle that i that i don't usually take on that about has death being a deadline that forces you
*  to make better decisions because i have heard people talk about how if you have immortality
*  people are going to stop stop trying and working on things because they've got all the time in the
*  world um but i would say that i don't expect it to be a super critical thing that that a sense of
*  mortality and death impending death is necessary there because those are things that they do wind
*  up providing reward signals to us and we will be in control of the reward signals and there
*  there will have to be something fundamental that causes that engenders curiosity and goal setting
*  and all of that i am something is going to play in there at the reward level i am you know whether
*  it's positive or negative or both i don't have any strong opinions on exactly what it's going to be
*  i am but that's that type of thing where i doubt that might be one of those half dozen key things
*  that has to be sorted out on exactly what the master reward that's the meta reward over all of
*  the uh the local task specific rewards have to be that could be that big negative reward of death
*  maybe not death but ability to walk away from an interaction so it bothers me when people treat
*  ai systems like servants so it doesn't bother me but i mean it it's it really is drawing the line
*  between what an a system could be it's limiting the possibility of what an a system could be is
*  treating them as justice tools now that's of course for from a narrow ai perspective there's
*  so many problems that narrow ai could solve just like you said as in in its form of a tool
*  but it could also be a being which is much more than a tool and to be a to become a being you have
*  to respect that thing for being a being and for that it has to be able to have
*  to make its own decisions to walk away to say i had enough for you i would like to break up with
*  you now uh you've not treated me well and i would like to move on so uh i think that actually that
*  choice to end things so i i have a couple things on that so on the one hand
*  i it is kind of disturbing when you see people being like people that are mean to robots and
*  you know mean to alexa whatever and that seems to speak badly about humanity but there's also the
*  exact opposite side of that where you have so many people that imbue humanity in inanimate objects
*  or things that are toys or that are are relatively limited so i think there may even be more more
*  danger about people putting more emotional investment into a lot of these proto ai's in
*  different ways yeah um and then the ai would manipulate that but but as far as like the ai
*  and the sides of things i really stay away from any of those discussions or even really thinking
*  about it it's similar with the safety things where i think it's just premature and there's a certain
*  class of people that enjoy thinking about impractical things things that are not in the world
*  and you know of pragmatic effect around you and i think that begin again because i don't think
*  there's going to be a fast take off i think we actually will have time to have these debates
*  when we know the shape of what we're debating and some people do take a principled approach that
*  they think it's going to go too fast that you really do need to get ahead of it that you need
*  to be thinking about this because we have slow processes of coming to any kind of consensus or
*  even coming up with ideas about this and maybe that's i maybe that's true i wouldn't put any of
*  my money or funding into something like that because i don't think it's a problem yet and i
*  think that we will have these signs of life when when we've got our learning disabled toddler we
*  should really start talking about some of the safety and ethics issues but probably not before
*  then can you elaborate briefly about why you don't think there'll be a fast takeoff is there some
*  deep intuition you have about it this is because it's grounded in the physical world or why yeah so
*  it is my belief that we're going to start off with something that requires thousands of gpus and i
*  i don't know if you've tried to go get a thousand gpu instance on a cloud anytime recently but these
*  are not things that you can just go spin up hundreds of i there are real challenges to i mean these
*  things are going to take data centers and data centers take years to build you know and the last
*  few years we've seen a few of them kind of coming up going in different places they're big engineering
*  efforts you can hear people bemoan about the fact that i know the the network was wired all wrong
*  and it took them a month to go unwire it and rewire it the right way these aren't things that you can
*  just magic into existence and the ideas of i am like the old tropes about it's going to escape
*  onto the internet and take over other systems there's the fast takeoff ones are clearly nonsense
*  because you just can't open tcp connections above a certain rate no matter how smart you are even if
*  you have perfect hacking ability that take over the world in an instant sort of thing just isn't
*  plausible at all and even if you had access to all of the resources these are going to be specialized
*  systems where you're going to wind up with something that is architected around exactly
*  this chip with this interconnect and it's not just going to be able to be plopped somewhere else now
*  interestingly it is going to be something that the entire um the entire code for all of it will
*  easily fit on a thumb drive that's total spy movie thriller sorts of things where you could have hey
*  we cracked the secret a gi and it fits on this thumb drive and anyone could steal it now they're
*  still gonna have to build the right data center to deploy it and have the right kind of life
*  experience curriculum to take it up to the point where it's valuable but the real core of it the
*  magic that's going to happen there is going to be very small you know it's again tens of thousands
*  of lines of code not millions of lines of code it is possible to imagine a world as you mentioned
*  in the spy thriller view if it's if it's just a few lines of code we can imagine a world where
*  the surface of computation is growing maybe growing exponentially meaning there's you know
*  the refrigerators start getting a gpu and uh just every first of all the smartphones the
*  billions of smartphones but maybe if there become highways through which code can spread across the
*  entirety of the computation surface then you don't any longer have to book aws
*  um gps real fundamental issues there when you start getting down to taking an actual problem
*  and putting it on an abstract machine like that that has not worked out well in practice and the
*  idea that there was always like it's always been easy to come up with ways to get compute faster
*  to say more flops or more more giga ops or whatever there that's usually the easy part but
*  you then have interconnect and then memory for what goes into it and when you talk about saying
*  well cell phones well you're limited to like a 5g connection or something on that and if you say
*  how if you take your your calculation you factor it across a million cell phones instead of a
*  thousand gpus in a warehouse you might be able to have some kind of a substrate like that but it
*  could be operating then at one one thousandth the speed and so yes you could get you could have an
*  agi working there but it wouldn't be a real-time agi it would be something that is operating at
*  really a snail's pace you know much much slower than kind of human level thought for things
*  i'm not worried about that problem you're transferring the problem into the interconnect
*  the communication the shared memory the the collective intelligence aspect of it which is
*  extremely difficult as well yeah i mean it's back to the the very earliest days of supercomputers
*  you still have the the balance between bandwidth storage and computation and sometimes they're
*  easier to get one or the other but it's been remarkably constant across all those years that
*  you still need all three what do your efforts now you mentioned to me that you're really committing
*  to ai at this stage what what do you see your life in the next few months years look like
*  what do you hope to achieve achieve here so i literally just this week signed a term sheet
*  to to take some investment money for my company where the last two years i had backed off from
*  meta and i was still doing my consulting cto role there but i had styled it as i was going to take
*  the victorian gentleman scientist route where i was going to be the you know the wealthy person
*  that was going to go pursue science and learn about this and do experiments and honestly i'm
*  surprised there aren't more people like that that are like me technical people that made a bunch of
*  money and are interested in some of these possibly the biggest leverage point in human history i mean
*  i know of i've heard of a couple organizations that are basically led by one rich techie guy that
*  gets a few people around him to try to work on this but i'm surprised that there's not more that
*  there aren't like a dozen of them i i mean maybe people are still think that it's an unapproachable
*  problem that it's kind of beyond their ability to to get a wrench on and have some effect on like
*  whatever startups they've run before but i that was my kind of like with all the stuff i've learned
*  whether it's gaming aerospace whatever i i go through a larval phase where i'm like okay i'm
*  sucking up all of this information trying to see is this something that i can actually do
*  i is this something that's practical to devote a large chunk of my life to and i've gone through
*  that with the uh with the ai machine learning space of things and i and i think i've got my
*  arms around it i've got the measure of it where some of the most brilliant people in the world
*  are working on this problem but nobody knows exactly the path that it's going on we're throwing
*  a lot of things at the wall and seeing what sticks i but i have a you know another interesting thing
*  just learning about all of this the the contingency of your path to knowledge and talking about the
*  associations and the context that you have with them where people that learn in the same path
*  will have similar thought processes and i think it's useful that i come at this from a different
*  background a different history than the people that have had the largely academic backgrounds
*  for this where i have huge blind spots that that they could easily point out but i have a different
*  set of experiences in history and approaches to problems and systems engineering that i am you
*  know that might turn out to be useful and i can afford to take that bet where i'm not going to be
*  destitute i am i was you know i've been i have enough money to fund myself working on this for
*  the rest of my life but what i was finding is that i was i was still not committing where i had a foot
*  firmly in the vr and meta side of things where in theory i've got i've got a very nice position
*  there i only have to work one day a week for my my consulting role but but i was engaging every day
*  i'd still be like my computer's there i'd be going and checking the workplace and notes and
*  testing different things and communicating with people but but i did make the the decision
*  recently that no i'm gonna get serious i'm still gonna keep my ties with meta but i am seriously
*  going for the a gi side of things and it's actually a really interesting point because a lot of
*  the machine learning the ai community is quite large but really basically almost everybody has
*  taken the same trajectory through life in that community and it's so interesting to have somebody
*  like you which are with a fundamentally different trajectory and that's where the big solutions can
*  come because there is a kind of silo and it's it is a bunch of people kind of following the same
*  kind of set of ideas and i was really worried that i didn't want to come off as you know like
*  an arrogant outsider for things where i have all the respect in the world for the work that's you
*  know it's been a miracle decade it's we're in the midst of a scientific revolution happening now and
*  everybody doing this is i you know these are the the einsteins and boars and whatever's of our
*  modern era i am and i was really happy to see that the the people that i sat down and talked with
*  everybody does seem to really be quite great about just happy to talk about things willing
*  to acknowledge that we don't know what we're doing we're figuring it out as we go along
*  and i mean i've got a you know a huge debt on this where this all really started for me because
*  sam altman basically tried to recruit me to open ai and it was at a point when i didn't know anything
*  about what was really going on in machine learning and in fact it's funny how the first time you
*  reached out to me it's like four years ago for your ai podcast yeah for people yeah for people
*  who uh uh listening to this should know that first of all obviously i've been a huge fan of
*  yours for the longest time but we've agreed to talk like yeah like four years ago back when this
*  was called the artificial intelligence podcast we wanted to do a thing and we said you said yes and
*  then i said it's like i don't know anything about modern ai that's right i said i could kind of take
*  an angle on machine perception because i'm you know i'm doing a lot of that with the sensors and
*  the virtual reality but we could probably find something to talk about and then so i mean and
*  that's where when did sam talk to you about open ai around the same time no it was a little bit it
*  was a bit after that so i had done the the most basic work i had kind of done the neural networks
*  from scratch where i'd i'd gone and written it all in c just to make sure i understood back
*  propagation at the at the lowest level and my my nuts and bolts approach but but after sam approached
*  me i you know it was flattering to think that he thought that i i could be useful at open ai
*  largely for kind of like systems optimization sorts of things i am you know without being an
*  expert but i asked i you know ilia sets cover to give me a reading list and he gave me a you know
*  a binder full of all the papers that like okay these are the important things if you really
*  read and understand all of these you'll know like 80 of what most of the you know the machine
*  language researchers work on and and i went through and i read all those papers multiple
*  times and highlighted them and went through and kind of figured the things out there and then
*  started branching out into my own sets of research on things and i actually started writing my own
*  experiments and doing kind of figuring out you know finding out what i what i don't know what
*  the limits of my knowledge are and starting to get some of my angles of attack on things the things
*  that i think are a little bit different from uh from what people are doing and i've had a couple
*  years now like two years since i i kind of left the full-time position at meta and now i've kind
*  of pulled the trigger and said i'm gonna get serious about it but some of my lessons all the
*  way back to armadillo aerospace about how i know i need to be more committed to this where there is
*  that you know it's both a freedom and the cost in some ways when you know that you're wealthy enough
*  to say it's like this doesn't really mean anything i can i can spend you know i can spend a million
*  dollars a year for the rest of my life and it doesn't mean anything it's fine uh but that is
*  an opportunity to just kind of meander and i could see that in myself when i'm doing some things it's
*  like oh this is a kind of interesting curious thing let's look at this for a little while let's
*  look at that it's not really bearing down on the problem so there's a few things that that i've
*  done that are kind of tactics for myself to make me more effective like one thing i noticed i was
*  not doing well is i had a google cloud account with uh to get gpus there and i was finding i
*  was very rarely doing that for no good psychological reasons where i'm like oh i can always think of
*  something to do other than to spin up instances and run an experiment i can you know keep working
*  on my local titans or something uh but it was really stupid i mean it was not a lot of money
*  i should have been running more experiments there so i thought to myself well i'm going to go buy a
*  quarter million dollar dgx station i'm going to just like sit it right there and it's going to
*  mock me if i'm not using it if the fans aren't running on that thing i'm not properly utilizing
*  it and that's been helpful you know i've done a lot more experiments since then it's been it's
*  been interesting where i thought i'd be doing all this low level envy link optimized stuff but 90%
*  of what i do is just spin up four instances of an experiment with different hyper parameters on it
*  always just you are you're doing like really sort of building up intuition by doing ml experiments
*  of different kinds but so the next big thing though is i am you know i decided that i was going to
*  take some take some investor money because i i have an overactive sense of responsibility about
*  other people's money i am and it's like i i don't want i mean a lot of my my push and my passionate
*  entreaties for things at meta or it's like i don't want zuck to have wasted his money investing in
*  oculus i want it to work out i want it to change the world i want it to be worth all of this time
*  money and effort going into it and i expect that it's going to be that like that with my
*  with my company where it's a huge forcing function this investment investors that are are going to
*  expect something of me now we've all had the conversation that this is a low probability
*  long-term bet it's not something that there's a million things i could do that i would have line
*  of sight on the value proposition for this isn't that i think there are there are unknown unknowns
*  in the way but it's one of these things that it's you know it's hyperball but it's potentially one
*  of the most important things humans ever do and it's something that i think is within our lifetimes
*  if not within a decade to happen so yeah this is just now happening like term sheet like the ink
*  virtual links barely dry drying i mean as i mentioned you offline like somebody i admire
*  somebody you know andre capote i think the two of you different trajectories in life but
*  approach problems similarly in that he codes stuff from scratch up all the time and i he's
*  created a bunch of little things outside of even outside the course at stanford that had been
*  tremendously useful to build up intuition about stuff but also to help people and they're all in
*  the realm of ai do you see yourself potentially doing things like this or building you know not
*  necessarily solving a gigantic problem but on the journey on the path to that building up intuitions
*  and sharing code or ideas or systems that give inklings of a gi but also kind of are useful to
*  people in some way so yeah first of all andre is awesome i learned a lot when i was going through
*  my larval phase from his blog posts and his stanford course and you know super valuable
*  i got to meet him first a couple years ago when i was first kind of starting off on my gentleman
*  scientist bit and just a just a couple months ago when he went out on his sabbatical he stopped by
*  in dallas and we talked for a while and i had a great time with him and then when i heard he
*  actually left tesla i did of course along with a hundred other people say hey if you ever want to
*  work with me it would be an honor yeah so i'm he thinks that he's going to be doing this educational
*  work but i think someone's going to make him an offer he can't refuse before he gets too far along
*  on it oh his current his current interest is education is that yeah um he's a special mind
*  is there something you could speak to what makes him so special so you understand like he did
*  he was very much a programmer's programmer that was doing machine learning work rather than
*  it's a different feel than an academic where you can see it in papers sometimes where somebody
*  that's really a mathematician or a statistician at heart and they're they're doing something with
*  machine learning but i you know andres about getting something done and you could see it in
*  like all of his earliest approaches to it's like okay here's how reinforcement learning works here's
*  how recurrent neural networks work here's how transformers work here's how i am you know crypto
*  works and i am and yeah it's just he's a hacker's you know one of his old posts was like a hacker's
*  guide to machine learning yeah and you know he deprecated that and said don't really pay attention
*  to what's in here but it's that thought that that carries through in a lot of it where it is that
*  back again to that hacker mentality and the hacker ethic with what he's doing and in sharing all of
*  it yeah and a lot of his approach to a new thing like like you said larva stage is let me code up
*  the simplest possible thing to build up intuition about it yeah like i say i i sketch with structs
*  and things when i'm just thinking about a problem i'm thinking in some degree of code
*  you are also among many things a martial artist both judo and jiu-jitsu how has this helped make
*  you the person you are so i mean i was a competent club player in judo and grappling i mean i was
*  you know by no means any kind of a superstar but it was i went through a few phases with it where
*  i did some i when i was quite young a little bit more when i was 17 i am and then i got into it
*  and then i got into it kind of seriously in my mid-30s and you know i went pretty far with it
*  and i was you know pretty good at some of the things that i was doing and i did appreciate it
*  quite a bit where i mean on the one hand it's always if you're going to do exercise or something
*  it's a more motivating form of exercise if someone is if someone is crushing you you are
*  like motivated to to do something about that to up your attributes and be better about
*  getting out of attributes yes but there's also that sense that i'm you know i was not i was not
*  a sports guy i did do wrestling in i in junior high and i often wish that i think i would have
*  i would have been good for me if i'd carried that on into high school and had a little bit more of
*  that i mean it's like i i you know filch a little bit of wrestling vibe with all was going on about
*  embracing the grind and like that push that i associate with the wrestling team that that i
*  in hindsight i wish i had gone through that and pushed myself that way but even getting back into
*  judo and jiu-jitsu in in my mid-30s as usually the old man on the mat with that there was still the
*  you know the sense that i you know working out with the the group and having the the guys that
*  you're beating beating each other up with it but you just feel good coming out of it and i can
*  remember those driving home aching in various ways and just thinking it's like oh that was
*  that was really great and i you know it's mixing with a bunch of people that had nothing to do with
*  any of the things that uh that i worked with you know every once in a while someone would be like
*  oh you're the doom guy and i but for the most part it was just different slice of life i you
*  know a good thing and i i made the call when i was 40 that's like maybe i'm getting a little
*  old for this i had i had separated a rib and tweaked a few things and i got out of this
*  without any really bad injuries and it was like have i dodged enough bullets should i you know
*  should i hang it up i went back i've i've gone a couple times in the last decade trying to get my
*  kids into it a little bit i didn't really stick with any of them but it was fun to get back on
*  the mats i really hurts for a while when you haven't gone i gone for a while but i still
*  debate this pretty constantly my brother's only a year younger than me and he's going kind of hard
*  in jujitsu right now and i you know he was just he won a few medals at the last tournament he was
*  at he's competing yeah and i was thinking yeah i guess we're in the executive division if you're
*  over 50 you know we're over 45 or something and it's not out of the question that i go back at
*  some point to do some of this but again i'm just reorganizing my life around more focus probably
*  not going to happen i'm pushing my exercise around to give me longer uninterrupted intellectual
*  focus time pushing it to the beginning or the end of the running and stuff like that walking
*  yeah yeah running in calisthenics and some things like that but it allows you to still think about
*  a problem and but if you go into a judo club or something you're you've got it fixed it's going
*  to be seven o'clock or whatever 10 o'clock on saturday i although i talked about this a little
*  bit when i was on rogan and shortly after that carlos machado did reach out and i had trained
*  with him for years i back in the day and he was like hey we've got kind of a small private club
*  with a bunch of kind of executive type people and it gets it does tempt me yeah i don't know if you
*  know him but john nana heard moved here to austin uh with gordon ryan and a few other folks and he
*  has a very interesting way very deep systematic way of thinking about jiu-jitsu that reveals the
*  the chest of it the the the like the the science of it and i do think about that more as kind of
*  an older person considering the martial arts where i can remember the the very earliest days
*  getting back into judo and i'm like teach me submissions right now you know it's like learn
*  the armbar learn the choke i but as you get older you start thinking more about it's like okay i
*  really do want to like learn the entire canon of judo it's like are all the different things there
*  and like all the different approaches for it not just the you know if you want to compete there's
*  just a handful of things you learn really really well but sometimes there's interest in learning
*  a little bit more of the scope there and figuring some things out from you know at one point i had
*  it wasn't exactly a spreadsheet but i did have a you know a big long text file with like here's
*  the things that i learned and here are like ways you chain this together and while when i went back
*  a few years ago it was good to see that i i whipped myself back into reasonable shape about
*  doing the basic grappling but i know there was a ton of the subtleties that were just that were
*  gone but could probably be brought back reasonably quickly and there's also the benefit i mean you're
*  exceptionally successful now um you're brilliant and the problem the old problem of the ego yeah
*  is uh i still pushed kind of harder than i should i mean that was i was one of those people that i
*  yeah i'm i'm on the smaller side for uh for a lot of the people competing and i would you know i'd
*  go with all the big guys and i'd go hard and i pushed myself a lot and that would be one of those
*  where yeah i would i you know i i'd be dangerous to anyone for the first five minutes but then
*  sometimes after that i'm already dead and i knew it was terrible for me because it it made the
*  you know it meant i got less training time with all of that when you go and you just gas out
*  you know relatively quickly there and i like to think that i would be better about that where
*  after i gave up judo i started doing the half marathons and tough butters and things like that
*  and so when i did go back to the the local judo kai club i thought it's like oh i should have
*  better cardio for this because i'm i'm a runner now and i do all of this and didn't work out that way
*  it was the same old thing where just push really hard strain really hard and and of course when i
*  worked with good guys like carlos it's like he just the whole flow like water thing is real and he's
*  just like that's true with judo too some of the best people like i've i've trained with olympic
*  gold medalists and for some reason with them everything's easier everything is you actually
*  start to feel the science of it the music of it the dance of it and it's everything is effortless
*  um you understand that there's an art to it it's not just an exercise it was interesting where i
*  did go to the kodakon in japan i kind of the birthplace of judo and everything and i remember i
*  rolled with one old guy i didn't you know didn't start standing just started on groundwork niawaza
*  and it was striking how different it was from carlos he was still he was better than me and
*  he got my arm and i you know i had to tap there but it was a completely different style where i
*  just felt like i could do nothing he was just enveloping me and just like slowly ground it down
*  put my arm and bent it while with carlos you know he's just loose and free and you always thought
*  like oh you're just going to go grab something but never had any chance to do it but it was very
*  different feeling that's a good summary of the difference between jiu-jitsu and judo in jiu-jitsu
*  there's it is a dance and you feel like there's a freedom and actually um anybody i tried like
*  gordon ryan one of the best the best grappler in the world nogi grappler in the world
*  there's a feeling like you can do anything but when you actually try to do something you can't
*  just magically doesn't work but with the best judo players in the world yeah it does feel like
*  there's a blanket that weighs a thousand pounds on top of you and there's not a feeling like you
*  can do anything you just you're trapped and that's a that's a style that's a difference
*  in the style of martial arts but it's also uh once you start to study you understand it all
*  has to do with human movement and the physics of it and the leverage and all that kind of stuff
*  and that's like that's super fascinating at the end of the day for me the biggest benefit is in
*  the humbling aspect when another human being um kind of tells you that you know there's a hierarchy
*  or there's a um you're not that special and in the most extreme case when you tap to a
*  choke you are basically living because somebody lets you live and that's that is one of those if
*  you think about it that is a closer brush with mortality than than most people consider
*  and that kind of humbling act is good to take to your work then where it's harder to get humbled
*  you know yeah because nobody's nobody that does any martial art is coming out thinking i'm the
*  best in the world at anything because everybody loses let me ask you for advice what advice would
*  you give to young people today about life about career how they can have a job how they can have
*  an impact how they can have a life they can be proud of so it was kind of fun i got invited to
*  give the commencement speech back at the i went to college for two semesters and and dropped out
*  and went on to do my tech stuff but they still wanted me to come back and give a commencement
*  speech and i i've got that pinned on my twitter account i still feel good about everything that i
*  said there and you know my my biggest point was that the path for me might not be the path for
*  everyone and in fact the advice the path that i took and even the advice that i would give based
*  on my experience and learnings probably isn't the best advice for everyone because what i did was
*  all about this knowledge in depth it was about not just having this surface level ability to make
*  things do what i want but to really understand them through and through to let me do the systems
*  engineering work and to sometimes find these inefficiencies that can be bypassed and and that
*  the whole world doesn't need that you know most programmers don't need or engineers of any kind
*  don't necessarily need to do that they need to do a little job that's been parceled out to them
*  be reliable let people depend on you do quality work with all of that but people that do have
*  an inclination for wanting to to know know things deeper and learn things deeper i'm you know the
*  there are just layers and layers of things out there and it it's amazing it's if you're the
*  right person that is excited about that i the world's never been like this before it's better
*  than ever i mean everything that was wonderful for me is still there and there's whole new
*  worlds to explore on the different things that you can do and that i am you know it's hard work
*  embrace the grind with it and understand as much as you can and then be be prepared for
*  opportunities to present themselves where you can't just say this is my goal in life and just push
*  at that i mean you might be able to do that but you're going to make more total progress if you
*  say i'm preparing myself with this broad set of tools and then i'm being aware of all the
*  way things are changing as i move through the world and as the whole world changes around me
*  and then looking for opportunities to deploy the tools that you've built and there's going to be
*  more and more of those types of things there where an awareness of what's happening where the
*  inefficiencies are what things can be done what's possible versus what's current practice and then
*  finding those areas where you can go and make an adjustment and make something that may affect
*  millions or billions of people in the world make it better when maybe from your own example how
*  were you able to recognize this about yourself that you saw the layers in in a particular thing
*  and you were drawn to discovering deeper and deeper truths about it is that something that
*  was obvious to you that you couldn't help or is there some actions you had to take to actually
*  allow yourself to dig deep so in the earliest days of personal computers i remember the the
*  reference manuals and the very early ones even had schematics of computers in the background in the
*  in the back of the books as well as firmware listings and things and i could look at that
*  and at that time when i was a younger teenager i didn't understand a lot of that stuff how the
*  different things worked i was pulling out the information that i could get but i always wanted
*  to know all of that there was like kind of magical information sitting down there it's like the elder
*  lore that some graybeard wizard i knew is the keeper of and so i always felt that pull for
*  wanting to know more wanting to explore the the mysterious areas there and you know and that
*  followed right in through all the things that got the value exploring the video cards leading to the
*  i'm you know the scrolling advantages you know exploring some of the academic papers and things
*  learning about bsp trees and the different things that that i could do i'm you know with those
*  systems and just the the huge larval phases going through aerospace just reading bookshelves full of
*  books i mean again that point where i have enough money i can buy all the books i want it was it was
*  so valuable there where i was terrible with my money when i was a kid my mom thought i would
*  always be broke because you know i'd buy my comic books and just be out of money but it was like all
*  the pizza i want all the diet coke i want video games and then books books and it didn't take that
*  much as soon as i was making 27k a year i i felt rich and i was just getting all the things that
*  that i wanted but that sense of you know that books have always been magical to me and that was one of
*  the things that really made me smile is i andre had said he found you know when he came over to
*  my house he said he found my library inspiring just like that and it was great to see you know
*  i still look at him he's kind of a younger guy i sometimes wonder if younger people these days
*  have the same relationship with books that i do where they were such a cornerstone for me in so
*  many ways but that sense that yeah i always wanted to know it all i know i can't and that was like
*  one of the last things i said you know you can't know everything but you should convince yourself
*  that you can know anything you know any one particular thing it was created and discovered
*  by humans you can learn it you can find out what you need on there and you can learn it deeply yeah
*  you can drive a nail down through whatever layer cake problem space you've got and learn a cross
*  section there and not only can you have an impact doing that you can just you can attain happiness
*  doing that there's something so fulfilling about becoming a craftsman of a thing yeah and i don't
*  want to tell people that look this is a a good career move just you know grit your teeth and
*  you know and bear it i you know you want people you want to and i do think it is possible sometimes
*  to find the joy in something like it might not immediately appeal to you but i had told people
*  early on like in software times that i you know it a lot of game developers are in it just because
*  they are so passionate about games but i was always really more flexible in what appealed to me where
*  i said i think i could be quite engaged doing operating system work or even database work i
*  would find the interest in that i because i think most things that are significant in the world
*  have a lot of layers and complexity to them and a lot of opportunities hidden within them
*  uh so that would probably be the most important thing to encourage to people is that
*  i am you can it's like weaponized curiosity you can deploy your curiosity to find i to kind of
*  like make things useful and valuable to you even if they don't immediately appear that way deploy
*  your curiosity yeah that's very true uh we've mentioned this debate point whether mortality
*  or fear of mortality is fundamental to creating an a gi but let's talk about whether it's fundamental
*  to human beings do you think about your own mortality i really don't and and you probably
*  always have to like take with a grain of salt anything somebody says about fundamental things
*  like that i am but i don't think about really aging impending death legacy with with my children
*  things like that and clearly it seems most of the world does a lot a lot more than i do yeah i so
*  i mean i think i'm an outlier in that where it's yeah it doesn't wind up being a real part of my
*  my thinking and motivation about things so daily existence is about sort of the people you love
*  and the problems before you i'm very much focused on what i'm working on right now i i do take that
*  back there's one aspect where the the kind of finiteness of the life does impact me and that
*  is about thinking about the scope of the problems that i'm working on when i you know when i decided
*  to work on when i was like nuclear fission or a gi these are big ticket things that i that are
*  impact large fractions of the world and i was thinking to myself at some level that okay i
*  mean i've i may have a couple more swings at bat with me at full capability but yes my my mental
*  abilities will decay with age you know mostly inevitably i i don't think it's a zero percent
*  chance that we will address some of that before it becomes a problem for me i think exciting
*  medical stuff in the next couple decades but i do have this kind of vague plan that when i'm not at
*  the top of my game and i don't feel that i'm you know in a position to put a dent in the world
*  some way that i'll probably wind up doing some kind of recreational retro programming or i'll
*  you know i'll i'll work on some i'm you know something that i would not devote my life to
*  now but i can while away my time as the old man gardening in the code worlds
*  and then to step back even bigger let me ask you about why we're here we human beings
*  what's the meaning of it all what's the meaning of life john karmak so very similar with that
*  last question i know a lot of people fret about this question a lot and i just really don't i
*  really don't give it no we are i you know we are biological creatures that happenstance of
*  evolution i you know we have innate drives that evolution crafted for survival and passing on of
*  genetic codes i am i don't i don't find a lot of value in trying to go much deeper than that i
*  have my motivations some of which are you know some of which are probably genetically coded and
*  many of which are contingent on my upbringing and the path that i've had through my life
*  i i don't run into like spates of depression or ennui or anything that that winds up being
*  a challenge and forcing a degree of soul searching with things like that i seem to be okay i'm you
*  know kind of without that um as a brilliant ant in the ant colony without looking up to the sky
*  wondering why the hell am i here again so the the why of it the incredible
*  mystery of the fact that we started first of all the origin of life on earth and from that from
*  single cell organisms the entirety of the evolutionary process took us somehow to this
*  incredibly intelligent thing that is able to build wolfenstein 3d and doom and quake and uh take a
*  crack at the problem of a gi and create things that eventually supersede human beings that doesn't
*  the why of it is um it's been my experience that people that focus on that don't focus on the here
*  and now right in front of them tend to be less effective i mean it's not 100 you know vision
*  matters to some people but i it doesn't seem to be a necessary motivator for me and i think that
*  the process of getting there is usually done again it's like the magic of gradient descent
*  people just don't believe that just looking locally gets you to all of these spectacular things
*  that's been you know the decades of looking at i am really some of the smartest people in the
*  world that would just push back forever against this idea that it's not this grand sophisticated
*  vision of everything but little tiny steps local information winds up leading to all the best
*  answers so the meaning of life is uh following locally wherever the gradient descent takes you
*  this was an incredible conversation officially the longest conversation i've ever done on the podcast
*  which means a lot to me because i get to do it with one of my heroes john i can't tell you how
*  much it means to me that you would sit down with me you're an incredible human being um i can't
*  wait what you do next but you've already changed the world you're an inspiration to so many people
*  and again we haven't covered like most of what i was playing to talk about so i hope we get a
*  chance to talk someday in the future i can't wait to see what you do next thank you so much again
*  for talking to me thank you very much thanks for listening to this conversation with john karmak
*  to support this podcast please check out our sponsors in the description and now let me leave
*  you with some words from john karmak himself focused hard work is the real key to success
*  keep your eyes on the goal and just keep taking the next step towards completing it
*  if you aren't sure which way to do something do it both ways and see which works better
*  thank you for listening and hope to see you next time

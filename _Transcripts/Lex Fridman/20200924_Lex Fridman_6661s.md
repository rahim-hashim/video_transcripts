---
Date Generated: April 13, 2024
Transcription Model: whisper medium 20231117
Length: 6661s
Video Keywords: ['james gosling', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 396207
Video Rating: None
---

# James Gosling: Java, JVM, Emacs, and the Early Days of Computing | Lex Fridman Podcast #126
**Lex Fridman:** [September 24, 2020](https://www.youtube.com/watch?v=IT__Nrr3PNI)
*  The following is a conversation with James Gosling, the founder and lead designer behind the Java programming language, which in many indices is the most popular programming language in the world, or as always, at least in the top two or three.
*  We only had a limited time for this conversation, but I'm sure we'll talk again several times in this podcast.
*  Quick summary of the sponsors, public goods, better help and express VPN.
*  Please check out the sponsors in the description to get a discount and to support this podcast.
*  As a side note, let me say that Java is the language with which I first learned object oriented programming and with it, the art and science of software engineering.
*  Also, early on in my undergraduate education, I took a course on concurrent programming with Java.
*  Looking back at that time before I fell in love with neural networks, the art of parallel computing was both algorithmically and philosophically fascinating to me.
*  The concept of a computer in my mind before then was something that does one thing at a time.
*  The idea that we could create an abstraction of parallelism where you could do many things at the same time while still guaranteeing stability and correctness was beautiful.
*  While some folks in college took drugs to expand their mind, I took concurrent programming.
*  If you enjoy this thing, subscribe on YouTube, review it with five stars and up a podcast, follow on Spotify, support on Patreon or connect with me on Twitter at Lex Friedman.
*  As usual, I'll do a few minutes of ads now and no ads in the middle.
*  I try to make these interesting, but I do give you timestamps.
*  So go ahead and skip, but please do check out the sponsors by clicking the links in the description.
*  It's the best way to support this podcast.
*  This show sponsored by Public Goods, the one stop shop for affordable, sustainable, healthy household products.
*  I take their fish oil and use their toothbrush, for example.
*  Their products often have a minimalist black and white design that I find to be just beautiful.
*  Some people ask why I wear this black suit and tie.
*  There's a simplicity to it that to me focuses my mind on the most important bits of every moment of every day.
*  Pulling only at the thread of the essential in all that life has to throw at me.
*  It's not about how I look.
*  It's about how I feel.
*  That's what design is to me, creating an inner conscious experience, not an external look.
*  Anyway, Public Goods plants one tree for every order placed, which is kind of cool.
*  Visit publicgoods.com slash Lex or use code Lex at checkout to get 15 bucks off your first order.
*  This show is also sponsored by Better Help, spelled H E L P help.
*  Check it out at better help dot com slash flex.
*  They figure out what you need and match it with a licensed professional therapist in under 48 hours.
*  I chat with the person on there and enjoy it.
*  Of course, I also regularly talk to David Goggins these days, who is definitely not a licensed professional therapist, but he does help me meet and talk to people.
*  He does help me meet his and my demons and become comfortable to exist in their presence.
*  Everyone is different, but for me, I think suffering is essential for creation, but you can suffer beautifully in a way that doesn't destroy you.
*  I think therapy can help in whatever form that therapy takes, and I do think that Better Help is an option worth trying.
*  They're easy, private, affordable and available worldwide.
*  You can communicate by text anytime and schedule weekly audio and video sessions.
*  Check it out at better help dot com slash flex.
*  This show is also sponsored by ExpressVPN.
*  You can use it to unlock movies and shows that are only available in other countries.
*  I did this recently with Star Trek Discovery and UK Netflix, mostly because I wonder what it's like to live in London.
*  I'm thinking of moving from Boston to a place where I can build the business I've always dreamed of building.
*  London is probably not in the top three, but top 10 for sure.
*  The number one choice currently is Austin for many reasons that I'll probably speak to another time.
*  San Francisco, unfortunately, dropped out from the number one spot, but it's still in the running.
*  If you have advice, let me know.
*  Anyway, check out ExpressVPN.
*  It lets you change your location to almost 100 countries, and it's super fast.
*  Go to ExpressVPN dot com slash Lex pod to get an extra three months of ExpressVPN for free.
*  That's ExpressVPN dot com slash Lex pod.
*  And now here's my conversation with James Gosling.
*  I've read somewhere that the square root of two is your favorite irrational number.
*  I have no idea where that got started.
*  Is there any truth to it?
*  Is there anything in mathematics or numbers that you find beautiful?
*  Oh, there's lots of things in math that's really beautiful.
*  You know, I used to consider myself really good at math, and these days I consider myself really bad at math.
*  I never really had a thing for the square root of two.
*  But when I was a teenager, there was this book called The Dictionary of Curious and Interesting Numbers,
*  which for some reason I read through and damn near memorized the whole thing.
*  And I started this weird habit of when I was like filling out checks, you know, or, you know, paying for things with credit cards.
*  I would want to make the receipt add up to an interesting number.
*  Is there some numbers that stuck with you that just kind of make you feel good?
*  They all have a story.
*  And fortunately, I've actually mostly forgotten all of them.
*  Are they so like 42?
*  Well, yeah, I mean, that one 42 is pretty magical.
*  And then the rationals.
*  I mean, but is there a square root of two story in there somewhere?
*  How did it get started?
*  It's like the only number that has destroyed religion.
*  In which way?
*  Well, the the Pythagoreans, they believe that all numbers were perfect and you could represent anything as a rational number.
*  And in that time period, this proof came out that there was no rational fraction whose value was equal to the square root of two.
*  And that means nothing in this world is perfect, not even mathematics.
*  Well, it means that your definition of perfect was imperfect.
*  Well, then there's the Gertl's incompleteness theorems in the 20th century that ruined it once again for everybody.
*  Yeah, although Gertl's theorem, you know, the lesson I take from Gertl's theorem is not that, you know, there are things you can't know, which is fundamentally what it says.
*  But, you know, people want black and white answers.
*  They want true or false.
*  But if you if you allow a three state logic that is true, false or maybe.
*  Then then life's good.
*  I feel like there's a parallel to modern political discourse in there somewhere.
*  But, yeah, let me let me ask.
*  So with your kind of early love or appreciation of the beauty of mathematics, do you see a parallel between that world and the world of programming?
*  You know, programming is all about logical structure, understanding the patterns that.
*  Come out of computation, understanding sort of.
*  I mean, it's often like, you know, the path through the graph of possibilities to find a short, a short route.
*  Meaning like, find a short program that gets the job done.
*  Yeah, I think.
*  But so then on the topic of irrational numbers, do you see do you see programming?
*  You just painted it so cleanly.
*  It's a little this trajectory to find like a nice little program.
*  But do you see it as fundamentally messy?
*  Maybe unlike mathematics?
*  I don't think of it as I mean, I mean, you know, you watch somebody who's good at math do math.
*  And.
*  You know, often it's it's fairly messy.
*  Sometimes it's kind of magical.
*  When I was a grad student, one of the students, his name was Jim Sachs, was.
*  He had this this this this.
*  This reputation of being sort of a walking, talking, human theorem proving machine.
*  And if you were having a hard problem with something, you could just like a costume in the hall and say, Jim.
*  And he would do this this this funny thing where he would stand up straight.
*  His eyes would kind of defocus.
*  He'd go, you know, just just like, you know, like like something in today's movies.
*  He's just.
*  And then straighten up and say and log in and walk away.
*  And you go, well, OK, so and log in is the answer.
*  How did he get there?
*  By which time he's down the hallway somewhere.
*  Yeah.
*  It's just the Oracle, the black box is gives you the answer.
*  Yeah.
*  I think in one of the videos I watched, you mentioned Don Knuth.
*  Well, at least recommending is, you know, his book is something people should read.
*  Oh, yeah.
*  But in terms of, you know, theoretical computer science.
*  Do you see something beautiful that has been inspiring to you?
*  Speaking of N log N, I think it's a great book.
*  Something beautiful that has been inspiring to you.
*  Speaking of N log N in your work on programming languages,
*  that's in the in the whole world of algorithms and complexity and, you know,
*  these kinds of more formal mathematical things.
*  Or did that not really stick with you in your programming life?
*  It did stick pretty clearly for me because one of the things that I care about is being able to.
*  Sort of look at a piece of code and be able to prove to myself that it works.
*  And.
*  You know, so for example, I find that.
*  I'm.
*  I'm at odds with many of the people around me over issues about like how you lay out a piece of software.
*  Right.
*  You know, so software engineers get really cranky about how they format the documents that are the programs,
*  you know, where they put new lines and where they put, you know, the braces.
*  The braces and all the rest of that.
*  Right.
*  And.
*  I tend to go for a style that's very dense.
*  Minimize the white space.
*  Yeah, well, to maximize the amount that I can see at once.
*  Right.
*  So I like to be able to see a whole function and to understand what it does
*  rather than have to go scroll, scroll, scroll and remember.
*  Right.
*  Yeah, I'm with you on that.
*  Yeah, that's and people don't like that.
*  Yeah, I've had, you know, multiple times when engineering teams have
*  staged what was effectively an intervention.
*  You know where they invite me to a meeting and everybody's arrived before me
*  and they sort of all look at me and say, James, about your coding style.
*  I'm sort of an odd person to be programming because I don't think very well verbally.
*  I am just naturally a slow reader.
*  I'm what most people would call a visual thinker.
*  So when you think about a program, what do you see?
*  I see pictures.
*  Right.
*  So when I look at a piece of code on a piece of paper,
*  it very quickly gets transformed into a picture.
*  And, you know, it's almost like a piece of machinery with,
*  you know, this connected to that and like these gears.
*  And yeah, yeah, I see them more like that than I see.
*  The sort of verbal structure or the lexical structure of letters.
*  So then when you look at the program, that's why you want to see it all in the same place.
*  Then you could just map it to something visual.
*  Yeah, and it just kind of like it leaps off the page at me.
*  Yeah. What are the inputs?
*  What are the outputs?
*  What the heck is this thing doing?
*  Yeah.
*  Getting a whole vision of it.
*  Can we go back into your memory?
*  Long-term memory access.
*  What's the first program you've ever written?
*  Oh, I have no idea what the first one was.
*  I mean, I know the first machine that I learned to program on.
*  What is it?
*  Was a PDP-8 at the University of Calgary.
*  Do you remember the specs?
*  Oh, yeah. So the thing had 4K of RAM, 12-bit words.
*  The clock rate was about a third of a megahertz.
*  Oh, so you didn't even get to the M, okay.
*  Yeah. Yeah. So we're like 10,000 times faster these days.
*  And was this kind of like a super computer, like a serious computer for?
*  No, the PDP-8i was the first thing that people were calling like mini computer.
*  Got it.
*  They were sort of inexpensive enough that a university lab could maybe afford to buy one.
*  And was there time sharing, all that kind of stuff?
*  There actually was a time sharing OS for that, but it wasn't used really widely.
*  The machine that I learned on was one that was kind of hidden in the back corner
*  of the computer center.
*  And it was bought as part of a project to do computer networking.
*  But they didn't actually use it very much.
*  It was mostly just kind of sitting there.
*  And it was kind of sitting there and I noticed it was just kind of sitting there.
*  And so I started fooling around with it.
*  And nobody seemed to mind, so I just kept doing that.
*  And it had a keyboard and like a monitor?
*  Oh, this was way before monitors were common.
*  So it was literally a Model 33 teletype with a paper tape reader.
*  Okay, so the user interface wasn't very good.
*  Yeah.
*  And it was a very, very simple thing.
*  It was the first computer ever built with integrated circuits.
*  But by integrated circuits, I mean that they would have like
*  10 or 12 transistors on one piece of silicon.
*  Not the 10 or 12 billion that the machines have today.
*  So what was the first computer ever built with integrated circuits?
*  So what does that feel like if you remember those?
*  Did you have kind of inklings of the magic of exponential kind of improvement of Moore's law,
*  of the potential of the future that was at your fingertips kind of thing?
*  No, no.
*  Or was it just a cool thing to play with?
*  It was just a toy.
*  I had always liked building stuff.
*  But one of the problems with building stuff is that you need to have parts.
*  You need to have pieces of wood or wire or switches or stuff like that.
*  And those all cost money.
*  And here you could build...
*  You could build arbitrarily complicated things and I didn't need any physical materials.
*  It required no money.
*  That's a good way to put programming.
*  You're right.
*  If you love building things, it's completely accessible.
*  You don't need anything.
*  Anybody from anywhere could just build something really cool.
*  Yeah.
*  If you've got access to a computer, you can build all kinds of crazy stuff.
*  And when you were somebody like me who had really no money,
*  and I remember just lusting after being able to buy a transistor.
*  A transistor.
*  And when I would do electronics kind of projects, they were mostly made done by
*  dumpster diving for trash.
*  One of my big hauls was discarded relay racks from the back of the phone company switching center.
*  Oh, nice.
*  That was the big memorable treasure.
*  Oh, yeah.
*  Yeah.
*  That was a...
*  What do you use that for?
*  I built a machine that played tic-tac-toe.
*  Nice.
*  Out of relays.
*  Of course, the thing that was really hard was that all the relays required a specific voltage,
*  but getting a power supply that would do that voltage was pretty hard.
*  And since I had a bunch of trash television sets, I had to
*  cobble together something that was wrong but worked.
*  So I was actually running these relays at 300 volts.
*  And none of the electrical connections were properly sealed off.
*  I'm surprised you survived that period of your life.
*  Oh, for so many reasons.
*  For so many reasons.
*  I mean, it's pretty common for teenage geeks to discover,
*  oh, thermite, that's real easy to make.
*  Yeah.
*  Well, I'm glad you did.
*  But do you remember what program in Calgary that you wrote, anything that stands out?
*  And what language?
*  Well, so mostly anything of any size was assembly code.
*  And actually, before I learned assembly code, there was this programming language on the
*  PDP-8 called Focal 5.
*  And Focal 5 was kind of like a really stripped down Fortran.
*  And I remember building programs that did things like play blackjack or solitaire.
*  And for some reason, one of the things that I really liked were ones where
*  they were just like plotting graphs.
*  So something with a function or a data, and then you'd plot it.
*  Yeah.
*  I did a bunches of those things and went, oh, pretty pictures.
*  And so this would print out, again, no monitors.
*  Right. So it was like on a teletype.
*  Yeah.
*  So using something that's kind of like a typewriter, and then using those to plot functions.
*  So I apologize to romanticize things, but when did you first fall in love with programming?
*  What was the first programming language?
*  Like, is it serious?
*  Maybe software engineer?
*  What were you thought?
*  This is a beautiful thing.
*  I guess I never really thought of any particular language as being beautiful,
*  because it was never really about the language for me.
*  It was about what you could do with it.
*  And even today, people try to get me into arguments about
*  particular forms of syntax for this or that, and I'm like, who cares?
*  It's about what you can do, not how you spell the word.
*  And so back in those days, I learned PL1 and Fortran and COBOL.
*  And by the time that people were willing to hire me to do stuff, it was mostly assembly code,
*  and PDP8 assembly code, and Fortran code, and control data assembly code for the CDC 6400,
*  which was an early, I guess, supercomputer.
*  Even though that supercomputer has less compute power than my phone,
*  by a lot.
*  And that was mostly, like you said, Fortran world.
*  That said, you've also showed appreciation for the greatest language
*  ever that I think everyone agrees is Lisp.
*  Well, Lisp is definitely on my list of the greatest ones that have existed.
*  Is it at number one?
*  Or I mean, or you, I mean.
*  The thing is that it's, I wouldn't put it number one, no.
*  Is it the parentheses?
*  What do you not love about Lisp?
*  Well, I guess the number one thing to not love about it is so freaking many parentheses.
*  On the love thing is, out of those tons of parentheses, you actually get an interesting
*  language structure.
*  And I've always thought that there was a friendlier version of Lisp hiding out there somewhere.
*  But I've never really spent much time thinking about it.
*  So, like, up the food chain for me from Lisp is Simula, which a very small number of people
*  have ever used.
*  But a lot of people, I think you had a huge influence, right?
*  Yeah.
*  The programming, but Simula, I apologize if I'm wrong on this, but is that one of the
*  first functional languages?
*  No, it was the first object-oriented programming language.
*  It's really where object-oriented and languages sort of came together.
*  And it was also the language where coroutines first showed up as a part of the language.
*  So you could have a programming style that was, you could think of it as
*  multi-threaded with a lot of parallelism.
*  Really?
*  There's ideas of parallelism in there?
*  Yeah.
*  Yeah.
*  So that was back, you know, so the first Simula spec was Simula 67.
*  Like 1967?
*  Yeah.
*  Wow.
*  So it had coroutines, which are almost threads.
*  The thing about coroutines is that they don't have true concurrency, so you can get away
*  without really complex locking.
*  You can't useably do coroutines on the multi-core machine.
*  Or if you try to do coroutines on the multi-core machine, you don't actually get to use the
*  multiple cores.
*  Either that or you start then having to get into the universe of semaphores and locks
*  and things like that.
*  But in terms of the style of programming, you could write code and think of it as being
*  multi-threaded.
*  The mental model was very much a multi-threaded one.
*  And all kinds of problems you could approach very differently.
*  To return to the world of Lisp for a brief moment, at CMU you wrote a version of Emacs
*  that I think was very impactful in the history of Emacs.
*  What was your motivation for doing so?
*  At that time, that was in like 85 or 86.
*  I had been using Unix for a few years.
*  Most of the editing was this tool called ED, which was sort of an ancestor of VI.
*  Is it a pretty good editor?
*  Not a good editor?
*  Well, if your input device is a teletype, it's pretty good.
*  It's certainly more humane than TECO, which was kind of the common thing in a lot of the
*  DEC universe at the time.
*  TECO is spelled T-K?
*  No, TECO.
*  So many features.
*  The original Emacs came out as...
*  Emacs stands for editor macros.
*  TECO had a way of writing macros.
*  The original Emacs from MIT started out as this little tool called TECO.
*  MIT sort of started out as a collection of macros for TECO.
*  But then the sort of Emacs style got popular originally at MIT.
*  And then people did a few other implementations of Emacs that were...
*  The code base was entirely different, but it was sort of the philosophical style
*  of the original Emacs.
*  What was the philosophy of Emacs?
*  And by the way, were all the implementations always in C?
*  And then how does Lisp fit into the picture?
*  So the very first Emacs was written as a bunch of macros for the TECO text editor.
*  Wow, that's so interesting.
*  The macro language for TECO was probably the most ridiculously obscure format
*  if you just look at a TECO program on a page, you think it was just random characters.
*  It really looks like just line noise.
*  So it's kind of like LaTeX or something.
*  Way worse than LaTeX.
*  Way, way worse than LaTeX.
*  But if you use TECO a lot, which I did, TECO was completely optimized for touch typing
*  at high speed.
*  So there were no two-character commands, or there were a few, but mostly they were just one
*  character.
*  So every character on the keyboard was a separate command.
*  And actually every character on the keyboard was usually two or three commands because
*  you could shift and control and all of those things.
*  It's just a way of very tightly encoding it.
*  And mostly what Emacs did was it made that visual.
*  One way to think of TECO is use Emacs with your eyes closed, where you have to maintain
*  a mental model of a mental image of your document.
*  You have to go, okay, so the cursor is between the A and the E, and I want to exchange those,
*  so I do these things.
*  Right?
*  So it was almost exactly the Emacs command set.
*  Well, it's roughly the same as Emacs command set, but using Emacs with your eyes closed.
*  Right.
*  So part of what Emacs added to the whole thing was being able to visually see what you were
*  editing in a form that matched your document.
*  And a lot of things changed in the command set because it was programmable.
*  It was really flexible.
*  You could add new commands for all kinds of things.
*  And then people rewrote Emacs multiple times in Lisp.
*  There was one done at MIT for the Lisp machine.
*  There was one done for Multics.
*  And one summer I got a summer job to work on the Pascal compiler for Multics.
*  And that was actually the first time I used Emacs.
*  To write the compiler.
*  So you've worked in compilers too.
*  It's fascinating.
*  Yeah, so I did a lot of work.
*  I spent a really intense three months working on this Pascal compiler,
*  basically living in Emacs.
*  And it was the one written in Maclus by Bernie Greenberg.
*  And I thought, wow, this is just a way better way to do editing.
*  And then I got back to CMU where we had kind of one of everything
*  and two of a bunch of things and four of a few things.
*  Since I mostly worked in the Unix universe and Unix didn't have an Emacs,
*  I decided that I needed to fix that problem.
*  So I wrote this implementation of Emacs in C
*  because at the time C was really the only language that worked on Unix.
*  And you were comfortable with C as well at that point?
*  Yeah, at that time I had done a lot of C coding.
*  This was in like 86.
*  And it was running well enough for me to use it to edit itself within a month or two.
*  And then it kind of took over the university.
*  And it spread outside?
*  Yeah, and then it went outside.
*  And largely because Unix kind of took over the research community.
*  And Emacs was kind of the best editor out there.
*  It kind of took over.
*  And there was actually a brief period where I actually had login IDs
*  on every non-military host on the ARPANET.
*  Because people would be like, oh, I'm going to be a great editor.
*  And I would be like, oh, well, yeah, but you'll need some help.
*  The days when security wasn't...
*  When nobody cared.
*  Nobody cared.
*  Can I ask briefly what were those early days of ARPANET and the internet like?
*  Did you, again, sorry for the silly question, but could you have possibly imagined
*  that the internet would look like what it is today?
*  Some of it is remarkably unchanged.
*  So one of the things that I noticed really early on
*  when I was at Carnegie Mellon was that a lot of social life became centered around the ARPANET.
*  So things like between email and text messaging.
*  Because text messaging was a part of the ARPANET really early on.
*  There were no cell phones, but you're sitting at a terminal and you're typing stuff.
*  So essentially email.
*  Well, just like a one-line message.
*  Oh, cool.
*  So like chat.
*  Like chat.
*  So it's like sending a one-line message to somebody.
*  And so pretty much everything from arranging lunch to going out on dates was all driven
*  by social media.
*  Right?
*  In the 80s.
*  Easier than phone calls, yeah.
*  And my life had gotten to where I was living on social media from the early mid-80s.
*  And so when it sort of transformed into the internet and social media explodes,
*  I was kind of like, what's the big deal?
*  Yeah.
*  It's just a scale thing.
*  Right.
*  The scale thing is just astonishing.
*  Yeah.
*  But the fundamentals in some ways remain the same.
*  The fundamentals have hardly changed.
*  The technology behind the networking have changed significantly.
*  The watershed moment of going from the ARPANET to the internet.
*  And then people starting to just scale and scale and scale.
*  The scaling that happened in the early 90s and the way that so many vested interests
*  fought the internet.
*  Oh, interesting.
*  Because you can't really control the internet.
*  Yeah.
*  Who fought the internet?
*  So fundamentally, the cable TV companies and broadcasters and phone companies,
*  at the deepest fibers of their being, they hated the internet.
*  But it was often kind of a funny thing because
*  so think of a cable company.
*  Most of the employees of the cable company, their job is getting TV shows, movies, whatever,
*  to their customers.
*  They view their business as serving their customers.
*  But as you climb up the hierarchy in the cable companies, that view shifts because
*  really the business of the cable companies had always been selling eyeballs to advertisers.
*  Right.
*  And that view of a cable company didn't really dawn on most people who worked at the cable
*  companies.
*  But I had various dust-ups with various cable companies where you could see in the stratified
*  layers of the corporation that this view of the internet is changing.
*  View of the reason that you have cable TV is to capture eyeballs.
*  They didn't see it that way.
*  Most of the people who worked at the cable companies, their view was that their job was
*  getting delightful content out to their customers, and their customers would pay for that.
*  Higher up, they viewed this as a way of attracting eyeballs to them.
*  And then what they were really doing was selling the eyeballs that were glued to their content
*  to the advertisers.
*  To the advertisers, yeah.
*  And so the internet was a competition in that sense.
*  Right.
*  They were right.
*  Well, yeah.
*  I mean, there was one proposal that we sent, one detailed proposal that we
*  wrote up back at Sun in the early 90s that was essentially like,
*  look, with internet technologies, anybody can become provider of content.
*  So you could be distributing home movies to your parents or your cousins who are anywhere else.
*  Anybody can become a publisher.
*  Wow. You were thinking about that already.
*  Yeah.
*  Netflix.
*  Yeah. That was like in the early 90s.
*  And we thought this would be great.
*  You could, and the kind of content we were thinking about at the time was like
*  home movies, kids' essays, stuff from like grocery stores or a restaurant
*  that they could actually start sending information about.
*  That's brilliant.
*  And the reaction of the cable companies was like, fuck no.
*  Because then we're out of business.
*  What is it about companies that, because they could have just,
*  they could have been ahead of that wave.
*  They could have listened to that and they could have...
*  They didn't see a path to revenue.
*  You know, somewhere in there, there's a lesson for like big companies, right?
*  To listen, to try to anticipate the renegade, the out there, out of the box,
*  people like yourself in the early days writing proposals about what this could possibly be.
*  Well, and that, you know, it wasn't...
*  You know, if you're in a position where you're making truckloads of money
*  off of a particular business model,
*  you know, the whole thought of like leaping the chasm, right?
*  You know, you can see, oh, new models that are more effective are emerging, right?
*  So like digital cameras versus film cameras.
*  You know, I mean...
*  Why take the leap?
*  Why take the leap?
*  Because you're making so much money off of film.
*  And, you know, in my past at Sun, one of our big customers was Kodak
*  and I ended up interacting with folks from Kodak quite a lot.
*  And they actually had a big digital camera research and, you know, digital imaging business.
*  Or development group.
*  And they knew that, you know, you just look at the trend lines and you look at,
*  you know, the emerging quality of these, you know, digital cameras.
*  And, you know, you can just plot it on the graph, you know?
*  And it's like, you know, sure, film is better today.
*  But, you know, digital is improving like this.
*  The lines are going to cross.
*  And, you know, at the point at which the lines cross is going to be a collapse in their business.
*  And they could see that, right?
*  They absolutely knew that.
*  The problem is that, you know, up to the point where they hit the wall,
*  they were making truckloads of money, right?
*  And when they did the math, it never started to make sense for them to kind of lead the charge.
*  And part of the issues for a lot of companies for this kind of stuff is that, you know,
*  if you're going to leap over a chasm like that, like with Kodak going from film to digital,
*  that's a transition that's going to take a while, right?
*  We had fights like this with people over like smart cards.
*  The smart cards fights were just ludicrous.
*  But that's where visionary leadership comes in, right?
*  Yeah, somebody needs to roll in and say, then take the leap.
*  Well, it's partly take the leap, but it's also partly take the hit.
*  Take the hit in the short time.
*  Right. So you can draw the graphs you want that show that, you know, if we leap from here,
*  you know, on our present trajectory, we're doing this and there's a cliff.
*  If we force ourselves into a transition and we proactively do that, we can be on the next wave.
*  But there will be a period when we're in a trough.
*  And pretty much always there ends up being a trough as you leap the chasm.
*  But the way that public companies work on this planet, they're reporting every quarter.
*  And the one thing that a CEO must never do is take a big hit.
*  Take a big hit.
*  Over some quarter. And many of these transitions involve a big hit for a period of time,
*  you know, one, two, three quarters. And so you get some companies and, you know, like
*  Tesla and Amazon are really good examples of companies that take huge hits.
*  But they have the luxury of being able to ignore the stock market for a little while.
*  And that's not so true today, really. But, you know, in the early days of both of those companies,
*  you know, like they both did this thing of, you know,
*  I don't care about the quarterly reports. I care about how many happy customers we have.
*  Right. And having as many happy customers as possible can often be an enemy of the bottom line.
*  Yeah. So how do they make that work? I mean, Amazon operated in the negative for a long time.
*  It's like investing into the future. Right. But, you know, so Amazon and Google and Tesla
*  and Facebook, a lot of those had what amounted to patient money.
*  Often because there's like a charismatic central figure who has a really large block of stock
*  and they can just make it so.
*  So on that topic, maybe it's still a small tangent, but you've gotten the chance to work with some
*  pretty big leaders. What are your thoughts about Tesla side, Elon Musk, leadership,
*  on the Amazon side, Jeff Bezos, all of these folks with large amounts of stock and vision
*  in their company? I mean, they're founders, either complete founders or like early on folks.
*  And Amazon have taken a lot of leaps.
*  That probably at the time people would criticize as like, what is this bookstore thing?
*  Why? Yeah. And Bezos had a vision and he had the ability to just follow it.
*  Lots of people have visions and the average vision is completely idiotic and you crash and burn.
*  The Silicon Valley crash and burn rate is pretty high. And they don't necessarily crash and burn
*  because they were dumb ideas, but often it's just timing and luck. And you take companies like Tesla
*  and really the original Tesla pre-Elon was kind of doing sort of okay,
*  but he just drove them. And because he had a really strong vision, he would make calls
*  that were always, well, mostly pretty good. I mean, the Model X was kind of a goofball thing to do.
*  But he did it boldly anyway. There's so many people that just said like, there's so many
*  people that oppose them on the Falcon one door, like the door from the engineering perspective,
*  those doors are ridiculous. It's like, yeah, they are a complete travesty,
*  but they're exactly the symbol of what great leadership is, which is like you have a vision
*  and you just go like, yeah, I'm going to do something stupid, make it really stupid. Yeah.
*  And go all in. Yeah. And to Tim's credit, he's a really sharp guy. So going back in time a little
*  bit to Steve Jobs, Steve Jobs was a similar sort of character who had a strong vision and was
*  really, really smart. And he wasn't smart about the technology parts of things, but he was really
*  sharp about the sort of human relationship between, you know, the relationship between
*  humans and objects. But he was a jerk. Can we just linger on that a little bit?
*  Like people say he's a jerk. Is that a feature or a bug?
*  Well, that's the question, right? So you take people like Steve, who was really hard on people.
*  And so the question is, was he needlessly hard on people or was he just making people reach
*  to meet his vision? And you could kind of spin it either way.
*  Well, the results tell a story. You know, he's, he, through whatever jerk ways he had,
*  he made people often do the best work of their life.
*  Yeah. Yeah. And that was absolutely true. And, you know, I interviewed with him several times
*  I did, you know, various negotiations with him. And even though kind of personally I liked him,
*  I could never work for him. Why do you think that, can you put into words the kind of
*  tension that you feel would be destructive as opposed to constructive?
*  Oh, he'd yell at people. He'd call them names.
*  And you don't like that?
*  No, no, I don't think you need to do that. And, you know, I think, you know, there's
*  pushing people to excel. And then there's too far. And I think he was on the wrong side of the
*  line. And I've never worked for Musk. I know a number of people who have, many of them have said,
*  and it's, you know, shows up in the press a lot that Musk is kind of that way. And one of the
*  things that I sort of loathe about Silicon Valley these days is that a lot of the high-flying
*  successes are run by people who are complete jerks. But it seems like there's been become this,
*  there's come this sort of mythology out of Steve Jobs that the reason that he succeeded was because
*  he was super hard on people. And in a number of corners, people start going,
*  oh, if I want to succeed, I need to be a real jerk. And that for me just does not compute.
*  I mean, I know a lot of successful people who are not jerks, who are perfectly fine people.
*  They tend to not be in the public eye.
*  The general public somehow lifts the jerks up into the hero status.
*  Right. Well, because they do things that get them in the press. And the people who
*  Yeah.
*  And, you know, the people who, you know, don't
*  do the kind of things that spill into the press.
*  Yeah, I just talked to Chris Lattner for the second time. He's a super nice guy.
*  Just an example of this kind of kind of individual that's in the background.
*  I feel like he's behind like a million technologies, but he also talked about
*  the jerkiness of some of the folks.
*  Yeah. Yeah. And the fact that being a jerk has become your required style.
*  But one thing I maybe want to ask on that is maybe to push back a little bit. So there's the jerk
*  side, but there's also, if I were to criticize what I've seen in Silicon Valley, which is almost
*  the resistance to working hard. So on the jerkiness side is,
*  so Poste jobs and Elon kind of push people to work really hard to do. And there's a question
*  whether it's possible to do that nicely. But one of the things that bothers me, maybe I'm just
*  Russian and just kind of, you know, romanticize the whole suffering thing, but I think working
*  hard is essential for accomplishing anything interesting, like really hard. And in the parlance
*  of Silicon Valley, it's probably too hard. This idea of the issue, work smart, not hard often
*  to me sounds like you should be lazy because of course you want to be to work smart. Of course
*  you would be a maximally efficient, but in order to discover the efficient path, like we're talking
*  about with the short programs. Yeah. Well, you know, the smart hard thing isn't an either or,
*  it's an and. It's an and, yeah. Right. And you know, the people who say you should work smart,
*  not hard, they pretty much always fail. Yeah. Thank you. Right. I mean, that's just a recipe
*  for disaster. I mean, there are counter examples, but they're more people who benefited from luck.
*  And you're saying, yeah, exactly. Luck and timing, like you said, is often an essential thing,
*  but you're saying, you know, you can push people to work hard and do incredible work without
*  without, without being nasty. Yeah. Without being nasty. I think
*  Google is a good example of the leadership of Google throughout its history has been
*  pretty good example of not being nasty and being, being kind. Yeah. I mean, the, the, the, the twins,
*  Larry and Sergey are both pretty nice people. Sondra Pichaz, very nice. Yeah.
*  Yeah. And, you know, it's, it's a cultural of people who work really, really hard.
*  Let me ask maybe a little bit of a tense question. We're talking about Emacs. It seems like you've
*  done some incredible work. So outside of Java, you've done some incredible work that didn't
*  become as popular as it could have because of like licensing issues and open source and like
*  the issues. What are your thoughts about the, the, that entire mess? Like what's
*  about open source now in retrospect, looking back about licensing, about open sourcing,
*  do you think open source is a good thing, a bad thing? Do you have regrets? Do you have
*  wisdom that you've learned from that whole experience? So in general, I'm a big fan of,
*  of open source. The way that it, it, it can be used to build communities and promote the development
*  of things and promote collaboration and all of that is really pretty grand. When open source
*  turns into a religion that says all things must be open source. I get kind of weird about that
*  because it's sort of like saying, you know, some, some versions of that end up saying that, that,
*  that all, all software engineers must take a vow of poverty. Right. Right. As though.
*  Um, it's unethical to have money. Yeah. To build a company to, uh, right.
*  And, you know, there's a, there's a, there's a slice of me that actually kind of buys into that.
*  Right. Because, you know, people who make billions of dollars off of like a patent
*  and the patent came from like, you know, literally a, a stroke of lightning that,
*  that, that hits you as you lie half awake in bed. Yeah, that's lucky. Good for you.
*  The way that that sometimes sort of explodes into something that looks to me a lot like exploitation.
*  You know, you see a lot of that in, in, in like the, the drug industry. Um,
*  you know, when, you know, when you've got a, got, got medications that cost,
*  you know, cost you like a hundred dollars a day. And it's like, no.
*  Yeah. So the, the, the interesting thing about the sort of open source,
*  what bothers me is when it, something is not open source and because of that, it's a
*  worst product. Yeah. So like, I mean, if I look at your, just implementation of e-max,
*  like that could have been the dominant implementation. Like I use e-max. That's
*  my main ID. I apologize to the world, but I still love it. Uh, and you know, I could have been using,
*  your implementation of e-max and why aren't I. So are you using the GNU e-max? I guess the
*  default on Linux is that GNU. Yeah. And, and that through a strange passage started out as the one
*  that I wrote. Exactly. So it's, it still has, uh, right. Yeah. Right. Well, and, and part of that
*  was because, you know, in, you know, the last couple of years of grad school, it, it became
*  really clear to me that I was either going to be Mr. E-max forever or I was going to graduate.
*  Got it. I couldn't actually do both. Was that a hard decision? That's so interesting to think
*  about you as a, like it's a different trajectory that could have happened. Yeah. That's fascinating.
*  Um, you know, and maybe, you know, I could be fabulously wealthy today if I had become Mr.
*  E-max and e-max had mushroomed into a series of text processing applications and all that.
*  And, you know, I would have, you know, but I have a long history of financially suboptimal decisions
*  because I didn't want that life. Right. And, you know, I went to grad school because I wanted to
*  graduate. Um, and, you know, you know, being Mr. E-max for a while was kind of fun and then it
*  kind of became not fun, not fun. Um, and you know, when it was not fun and I was, you know, there
*  was no way to go about it. I was, I was, I was, I was, I was, I was, I was, I was, I was, I was, I was,
*  and I was, you know, there was no way I could, you know, pay my rent.
*  Right. Yeah. And, and I was like, okay, do I carry on as a grad student as a,
*  you know, I, you know, I had a research assistantship and I was sort of living off of
*  that and I was trying to do my, you know, I was doing all my RA work, all my RA, you know,
*  being grad student work and being Mr. E-max all at the same time. Um, and, and I, I decided to
*  pick one. And one of the things that I did at the time was I went around, you know, all the people
*  I knew on the, the ARPANET who might be able to, to, to take over looking after E-max and, um,
*  pretty much everybody said, eh, I got a day job. So, so I actually found, you know,
*  two folks and a couple of folks in a garage in New Jersey, um, complete with a dog,
*  um, who were willing to take it over, but they were going to have to charge money.
*  Um, but my deal with them was that they would, um, only that they would make it free for
*  universities and schools and stuff. And they said, sure. And you know, that upset some people.
*  So you have some, now I don't know the full history of this, but I think it's kind of,
*  uh, interesting. You have some tension with Mr. Richard Stallman, um,
*  over the, and he kind of represents this kind of like, like you mentioned, free software,
*  uh, sort of a dogmatic focus on. Yeah. All, all, all information must be free.
*  Must be free. So what, is there an interesting way to paint a picture of the disagreement you
*  have with Richard through the years? My basic opposition is that, you know,
*  when you say information must be free, uh, to a really extreme form that turns into, you know,
*  all people whose job is the production of
*  everything from movies to software. Um, they must all take a vow of poverty
*  because information must be free. And that doesn't work for me. Right. And, and I, and I don't,
*  I don't want to be wildly rich. I am not wildly rich. Um, I do okay.
*  Do okay. Um, but I do actually, you know, you know, I've, you know, I can feed my children.
*  Yeah. I totally agree with you. It does just make me sad that sometimes the closing of the source,
*  for some reason that people that like a bureaucracy begins to build and sometimes
*  it doesn't, it hurts the product. Oh, absolutely. Absolutely. It's always sad.
*  And there's, and there is a, there is a balance in there. There's a balance. Um, and you know, it's,
*  it's not hard, hard over, you know, rapacious capitalism and, and it's,
*  and it's not hard over in the other direction. Um, and you know, a lot of the, the open source
*  movement, they, they, they have been managing to find a path to, um, actually making money.
*  Right. So doing things like service and support works for a lot of people. Um,
*  you know, and there are some, some ways where it's, it's kind of, um,
*  some of them are, are, are a little, a little perverse, right? So as,
*  you know, a part of things like this Sarbanes-Oxley Act and various people's
*  interpretations of all kinds of accounting principles. Um, and this is kind of a worldwide
*  thing, but if you've got a, a corporation that is depending on some piece of software, um,
*  you know, the often, you know, various accounting and reporting standards say,
*  if you don't have a support contract on this thing that, that your business is depending on,
*  then that's bad. You know, so, so, so, you know, if you've got a, if you've got a database,
*  you need to pay for support. And, and so, but there's a difference between,
*  you know, the, the sort of support contracts that, you know, the average open source database, uh,
*  producer charges and what somebody who is truly rapacious, like Oracle charges.
*  Yeah. So it's a, it's a balance. It is, it is, it is absolutely a balance.
*  And, you know, there are, there are a lot of, a lot of different ways to make, you know, the math
*  workout for everybody. Um, and, you know, the, the very, you know,
*  uh, unbalanced sort of, you know, like, like the winner takes all thing that,
*  that happens in so much of, of modern commerce. Um, that just doesn't work for me either.
*  I know you've talked about this in quite a few places, but you have created one of the most
*  popular programming languages in the world. Uh, this is the programming language that I first
*  learned about object oriented programming with. Uh, you know, I think it's a programming language
*  that a lot of people use in a lot of different places and millions of devices today, Java.
*  So the absurd question, but can you tell the origin story of Java?
*  So long time ago at Sun in about 1990, there was a group of us who were kind of worried that,
*  that there was stuff going on in the universe of computing that the computing industry was missing
*  out on. Um, and so, uh, uh, a few of us started this project at Sun. And we were, we were, we
*  were talking about this project at Sun. The really got going. I mean, we started talking about it in
*  1990 and it really got going in 91. Um, and it was all about, you know, what was happening
*  in terms of, you know, computing hardware, you know, processors and networking and all of that,
*  outside of the computer industry. And that was everything from the,
*  the, the, the sort of early glimmers of cell phones that were happening then to, you know,
*  you look at elevators and locomotives and process control systems and factories and
*  and all kinds of audio, audio equipment and video equipment. Um, they all had processors in them
*  and they were all doing stuff with them. And, and it, and it sort of felt like
*  there was something going on there that we needed to understand.
*  And so C and C plus plus was in the air already. Oh no, C and C plus plus absolutely owned the
*  universe at that time. Everything was written in C and C plus plus. So where was the hunch that
*  there was a need for a revolution? Well, so the, the need for a revolution was not about the
*  lang, a language. It was about, it was just as simple and vague as there are things happening
*  out there. We need to understand them. We need to understand them. And, and so, um, a few of us
*  went on several, um, somewhat epic road trips. Um, literal road trips, literal road trips. It's like
*  get on an airplane, go to Japan, visit, you know, Toshiba and Sharp and Mitsubishi and Sony and all
*  of these folks. And, you know, because we worked for Sun, we had, you know, folks who were willing
*  to like give us introductions. You know, we, we visited, you know, Samsung and, um, you know,
*  bunch of Korean companies and we went all over Europe. We went to, you know, places like, like
*  Phillips and Siemens and Thompson. And what did you see there? You know, for me, the, one of the
*  things that sort of leapt out was that they were doing all the usual computer, computer things that
*  people had been doing like 20 years before. The thing that really leapt out to me was that they
*  were sort of reinventing computer networking and they were making all the mistakes that people in
*  the computer industry had, had made. And since I had been doing a lot of work in the, in the
*  networking area, you know, you know, we'd go and, you know, visit, you know, Company X, they'd
*  describe this networking thing that they were doing. And just without any thought, I could,
*  I could tell them like the 25 things that were going to be complete disasters with that thing
*  that they were doing. Um, and I don't know whether that had any impact on any of them, but, but, but
*  that particular story of, you know, sort of repeating the disasters of the computer science
*  industry, um, was there. And we, and one of the things we thought was, well, maybe we could do
*  something useful here with like bringing them forward somewhat, but, but also at the same time,
*  um, we learned a bunch of things from, from these, you know, mostly consumer electronics companies.
*  Um, and, you know, high on the list was that
*  they viewed their like relationship with the customer as sacred. Um, they, they were never,
*  ever willing to make trade-offs between, for, for safety. All right. So one of the things that
*  had always made me nervous in the computer industry was that, um,
*  people were willing to make trade-offs in reliability to get performance. Um, you know,
*  the, you know, they want faster, faster breaks a little more often because it's fast. You know,
*  you, maybe you run it a little hotter than you should, or like, like the one that always blew
*  my mind was the way that, um, the folks at, at, at Cray supercomputers got their division to be
*  really fast was that they did Newton-Raphson approximations.
*  And so, you know, the bottom several bits of, you know, A over B were essentially random numbers.
*  Um, what could possibly go wrong? What could go wrong? Right. And, you know,
*  just figuring out how to nail the bottom bit, um, how to make sure that, you know,
*  if you put a piece of toast in a toaster, it's not going to kill the customer.
*  It's not going to burst into flames and burn the house down.
*  So those are, I guess those are the principles that were inspiring, but how did, uh, from the days of,
*  from the days of, uh, Java is called Oak because of a tree outside the window story
*  that a lot of people know, how did it become this incredible, like powerful language?
*  Well, so it was, it was a bunch of things. So we, you know, after all that we started,
*  you know, the way that we decided that we could understand things better
*  was by building a demo, building a prototype of something. So, um, kind of because it was easy
*  and fun, we decided to build a control system for some home electronics, you know, TV, VCR,
*  that kind of stuff. And as we were building it, we, you know, we, we, we sort of discovered that
*  there were some things about standard practice and C programming that, um,
*  we're really getting in the way. And, and it wasn't, it wasn't exactly, you know,
*  because we were writing this, all the C code and C plus plus code that, that we couldn't write it
*  to do the right thing, but that, um, one of the things that was weird in the group was that we had,
*  um, a guy who's, who's, who's, you know, his sort of top level job was he was a business guy.
*  You know, he was, he was sort of an MBA kind of person, you know, think about business plans
*  and all of that. And, you know, there were a bunch of things that were kind of, you know,
*  and we would talk about things that were going wrong and, um, or things that were going wrong,
*  things that were going right. And, you know, as we thought about, you know, things like,
*  like the requirements for security and safety, um, some low level details in C, like naked pointers.
*  Yeah.
*  And, you know, so, so back in the early nineties, um, it was well understood that, you know, the
*  number one source of like security vulnerabilities.
*  As pointers.
*  Was just pointers, was just bugs.
*  Yeah.
*  Right. And it was like, you know, 50, 60, 70% of all security vulnerabilities were bugs and the
*  vast majority of them were like buffer overflows.
*  So you're like, we have to fix this.
*  We have to make sure that this cannot happen. And that was kind of the original
*  thing for me was this cannot, this cannot continue. And one of the things I find really
*  entertaining this year was, um, I forget which rag published it, but there was this article that
*  came out that was, um, an examination. It was sort of the result of, of an examination of all the
*  security vulnerabilities in Chrome. And Chrome is like a giant piece of C++ code.
*  And 60 or 70% of all the security vulnerabilities were stupid pointer tricks.
*  And I thought, it's 30 years later and we're still there.
*  Still there.
*  And we're still there. And you know, I, you know, that's one of those, you know,
*  slap your forehead and, and, and just, just, just want to cry.
*  Would you attribute, uh, or is that too much of a simplification, but would you attribute the
*  creation of Java to, uh, to C pointers? Obvious problem.
*  Well, I mean, that was, that was one of the, the trigger points.
*  And currency you've mentioned.
*  Concurrency was a big deal. Um, and you know, because when you're interacting with people,
*  you know, the last thing you ever want to see is, is the thing like waiting and, you know,
*  issues about the software development process, you know, when faults happen, can you recover from them?
*  What can you do to make it easier to create and eliminate complex data structures?
*  What can you do to fix, you know, the, one of the most common C problems, which is storage leaks.
*  And it's, it's evil twin, the, um, the, the freed, but still being used
*  piece of, piece of memory. You know, you, you free something and then you keep using it.
*  Oh yeah.
*  You know, so, so when I was originally thinking about that, I was thinking about that in terms of,
*  of sort of safety and security issues. And one of the things I sort of came to believe,
*  came to understand was that it wasn't just about safety and security, but it was about, um,
*  developer velocity. Right. So, and I got really religious about this because at that point,
*  I had spent an ungodly amount of my life hunting down mystery pointer bugs.
*  And you know, like, like two thirds of my time as a software developer was, you know, because the
*  mystery pointer bugs tend to be the hardest to find because they tend to be very, very statistical.
*  The ones that hurt, you know, they are, you know, they're like a one in a million chance.
*  And.
*  But nevertheless, create an infinite amount of suffering.
*  Right. Because when you're doing a billion operations a second,
*  you know, I'm one in a million chance means it's going to happen.
*  And, and so I got really religious about this thing, about, you know, making it so that if
*  something fails, it fails immediately and visibly. And, you know, one of the, the, the things that
*  was a real attraction of Java to lots of development shops was that, you know, we get our code up and
*  running twice as fast. You mean like the entirety of the development process, the bugging, all that
*  kind of stuff. Yeah. If you, you know, so, so if you measure time from, you know, you've, you've
*  first touch fingers to keyboard until you get your first demo out.
*  Not much different, but if you look from fingers touching keyboard to
*  solid piece of software that you could release in production, it would be way faster.
*  And I think what people don't often realize there's, yeah, there's things that really
*  slow you down. Like the hard to catch bugs probably is, is the thing that really slows down.
*  That is really slows things down. But, but also there were, you know, one of the things that you
*  get out of object oriented programming is a strict methodology about, you know, what are the
*  interfaces between things and being really clear about how parts relate to each other.
*  And what that helps with is so many times what people do is they kind of like sneak around the
*  side. So if you've built something and people are using it and then, and you say, and you say,
*  well, okay, you know, I built this thing, you use it this way. And then you change it in such a way
*  that, that it still does what you said it does. It just does it a little bit different. But then
*  you find out that somebody out there was sneaking around the side. They sort of tunneled in a back
*  door and this person, their code broke. And because they were sneaking through a side door
*  and, and normally the attitude is, dummy. But a lot of times, you know, you can't get away,
*  you can't just slap their hand and tell them to not do that. Because, you know, it's, you know,
*  somebody's, you know, some banks, you know, account reconciliation system that, you know,
*  some developer decided, oh, I'm lazy. You know, I'll just sneak through the back door.
*  And because the language allows it, I mean, you can't even mad at them.
*  And so one of the things I did that, that, that on the one hand upset a bunch of people
*  who was, I made it so that you really couldn't go through back doors. Right. So,
*  so the whole point of that was to say, if you need, you know, if the interface here isn't right,
*  the wrong way to deal with that is, is to go through a back door. The right way to deal with
*  it is to walk up to the developer of this thing and say, uh, change the interface, fix it.
*  Yep. Right. And so it was kind of like a social engineering thing. Yeah. And, um,
*  it's brilliant. And people ended up discovering that that really made a difference, um, in terms
*  of, you know, and, and, and, and, and a bunch of this stuff, you know, if you're just like screwing
*  around writing your own, like, you know, class project scale stuff, um, a lot of stuff doesn't,
*  isn't quite so, so important because, you know, you're, you know, both sides of the interface.
*  But, you know, when you're building, you know, sort of larger, more complex pieces of software
*  that have a lot of people working on them, and especially when they like span organizations,
*  um, you know, having, having really clear, having clarity about how that gets structured,
*  saves your life. Yeah. Um, and, you know, especially, you know, there's so much
*  software that is fundamentally untestable, you know, and, you know, until you do the real thing.
*  Right. It's better to write good code in the beginning as opposed to writing crappy code
*  and then trying to fix it and trying to scramble and figure out and through testing, figure out
*  where the bugs are. Yeah. It's like, it's like, it's like, which shortcut caused that rocket to
*  not get where it was needed to go. So I think one of the most beautiful ideas, uh, philosophically
*  and technically is, uh, of a virtual machine, the Java virtual machine. Um, again, apologize
*  to romanticize things, but, uh, uh, how did the idea of the JVM come to be? How do you radical
*  of an idea it is? Cause it seems to me to be just a really interesting idea in the history of
*  programming. So, and what is it? So the Java virtual machine, you can think of it in different ways.
*  Um, because it was carefully designed to have different ways of viewing it.
*  So one view of it that most people don't really realize is there is that you can, um, view it as
*  sort of an encoding of the abstract syntax tree in reverse Polish notation.
*  Um, I don't know if that makes any sense at all. I could explain it and that would blow all over
*  time. Um, but the other way to think of it, um, and the way that it ends up being explained is that
*  it's, it's like the, the instruction set of an abstract machine that's designed such that you can
*  translate that abstract machine to a physical machine. And the reason that that's important.
*  So if you wind back to the early nineties, when we were talking to all of these,
*  these companies doing consumer electronics and you talk to the purchasing people,
*  there were interesting conversations with purchasing. Um, so if you look at how, you know,
*  these, you know, these devices come together, their sheet metal and gears and circuit boards
*  and capacitors and resistors and stuff. And everything you buy has multiple sources,
*  right? So you can buy a capacitor from here. You can buy a capacitor from there.
*  And you've got kind of a market. So, you know, so that the,
*  you can actually get a decent price for a capacitor. Um, but
*  CPUs and particularly in the early nineties, um, CPUs were all different and all proprietary.
*  So if you use the chip from Intel, you had to be an Intel customer for the end of, till the end of
*  time, because if you wrote a bunch of software, you know, when you wrote software using, you know,
*  whatever technique you wanted and C was particularly bad about this big, because
*  there was a lot of properties of the underlying machine that came through.
*  So you were stuck. So the code you wrote, you were stuck to that particular machine.
*  You were stuck to that particular machine, which meant that they couldn't decide, you know,
*  Intel is screwing us. Um, I'll, I'll start buying chips from, you know, Bob's better chips.
*  This drove the, like the purchasing people absolutely insane
*  that, that they would, they were welded into this decision.
*  And it would have, they would have to make this decision before the first line of software was
*  written. That's funny that you're talking about the purchasing people. So that's one perspective,
*  right? It's, you could, there's a lot of other perspectives that all probably hated this idea.
*  Right. But from a technical aspect, just like the creation of an abstraction layer that's, uh,
*  agnostic to the underlying machine, uh, from the perspective of the developer, I mean, that's
*  brilliant. Right. Well, and, and, and, and, you know, so that's like across the spectrum of,
*  of providers of chips, but then there's also the, the time thing, because, um, you know,
*  as you went from one generation to the next generation to the next generation, they were
*  all different and you would often have to rewrite your software. I mean, if the generations of, uh,
*  CP of machines of different kinds. Yeah. So, so like, like, like, like one of the things that
*  sucked about a year out of my life was when son went from the Motorola 68010 processor to the
*  68020 processor, then they had a number of differences and one of them hit us really hard
*  and I ended up being the, the point guy on the worst case of where
*  the new instruction cache architecture hurt us.
*  Well, okay. So, I mean, so when, when did this idea, I mean, okay. So yeah, you, you articulate
*  a really clear fundamental problem in all of computing, but how, where do you get the guts
*  to think we can actually solve this? You know, in our conversations with, you know, all these
*  vendors, you know, these, these problems started to show up and I kind of had this epiphany
*  because it reminded me of a summer job that I had had in grad school.
*  So back in grad school, my thesis advisor, well, I had two thesis advisors for bizarre reasons.
*  One of them was a guy named Raj Reddy. The other one was Bob Sproul and Raj,
*  I love both of them. So the, the department had bought a bunch of
*  like early workstations from a company called Three Rivers Computer Company.
*  And Three Rivers Computer Company was a bunch of electrical engineers who wanted to do as little
*  software as possible. So they knew that they'd need to have like compilers and an OS and stuff
*  like that. And they didn't want to do any of that. And they wanted to do that for as close to zero
*  money as possible. So what they did was they, they built a machine whose instruction set was
*  the, was literally the bytecode for UCSD Pascal, the P code. And so we had a bunch of software
*  that was, that was written for this machine. And for various reasons, you know, the company
*  wasn't doing terrifically well. We had all this software on these machines and we wanted it to
*  run on other machines, principally the VAX. And so Raj asked me if I could come up with a way
*  to port all of this software from the, from, from, from the, the, the, the Perk machines to VAXs.
*  And I think he, you know, what he had in mind was something that would translate from like Pascal
*  to C or Pascal to, actually at those times, pretty much it was, you could translate to C or C.
*  And if you didn't like translate to C, you could translate to C.
*  There was, you know, it's, you know, it's like the Henry Ford, you know, any color you want,
*  just as long as it's black. And, and I went, that's really hard. And I noticed that, you know, and I
*  was like looking at stuff and I went, ooh, I bet I could rewrite the P code into VAX assembly.
*  The P code into VAX assembly code. And, and then I started to realize that, you know, there were
*  some properties of P code that made that really easy. Some properties that made it really hard.
*  So I ended up writing this thing that translated from, from P code on the three rivers Perks into
*  assembly code on the VAX. And I actually got higher quality code than the C compiler.
*  And so, so everything just got really fast. It was really easy. It was like,
*  wow, I thought that was a sleazy hack because I was lazy. And in actual fact, it worked really well.
*  And, and I, and I tried to convince people that that was maybe a good thesis topic.
*  Yeah. And nobody was, was, you know, it was like, nah.
*  Really? That's, I mean, yeah, it's kind of a brilliant idea, right?
*  Maybe you didn't have the, you weren't able to articulate the big picture of it.
*  Yeah. And I think, you know, that was a, a key part, but so then, you know, clock comes forward
*  a few years and it's like, we've got to be able to, you know, the, you know, the, you know,
*  if they wanted to be able to switch from, you know, this weird microprocessor to that
*  weird and totally different microprocessor, how do you do that? And I kind of went, oh,
*  maybe by doing something kind of in the space of, you know, Pascal P code, you know, I could do
*  like multiple translators. And I spent some time thinking about that and thinking about,
*  you know, what worked and what didn't work when I did the, the, the, the P code to Vax translator.
*  And I talked to some of the folks who were involved in small talk because small talk also
*  did a white code. And, and, and then I kind of went, yeah, let's that I want to do that.
*  Yeah.
*  Cause that acts, you know, and, and it had the, the other advantage that
*  you could either interpret it or compile it. And interpreters are usually easier to do,
*  but not as fast as a compiler. And so I figured good, I can be lazy again.
*  You know, sometimes I think that most of my good ideas are driven by laziness. And often I find
*  that some of people's stupidest ideas are because they're insufficiently lazy.
*  Yeah.
*  They just want to build something really complicated. It's like, it doesn't need to be that complicated.
*  Yeah. And so, and so that's how that came out. And, and, and I think that's, that's the, that's
*  the, you know, but that also turned into kind of a, you know, almost a religious position on my part,
*  which was, which got me in, in several other fights. So like, like one of the things that was a real
*  difference was the way that arithmetic worked.
*  You know, once upon a time there were, you know, it wasn't always just to complement arithmetic.
*  There were some machines that had one's complement arithmetic, which was like almost anything built by
*  CDC. And occasionally there were machines that were decimal arithmetic. And I was like, this is crazy.
*  You know, pretty much two's complement integer arithmetic has one. So just-
*  Let's just do that.
*  Just do that. One of the other places where there was a lot of variability was in the way
*  that floating point behaved. And that was causing people throughout the software industry much pain
*  because you couldn't do a numerical computing library that would work on CDC and then have it
*  work on an IBM machine and work on a deck machine. And as a part of that whole struggle,
*  there had been this big body of work on floating point standards. And this thing emerged that
*  came to be called IEEE 754, which is the floating point standard that pretty much has taken over
*  the entire universe. And at the time I was doing job, it had pretty much completed taking over the
*  universe. There were still a few pockets of holdouts, but I was like, you know, it's important to be
*  able to say what two plus two means. And so I went that. And one of the ways that I got into fights
*  with people was that there were a few machines that did not implement IEEE 754 correctly.
*  Of course, that's all short-term kind of fights. I think in the long term,
*  I think this vision is one out.
*  Yeah. And I think it's, you know, and it worked out over time. I mean, the biggest fights were
*  with Intel because they had done some strange things with rounding. They had done some strange
*  things with their transcendental functions, which turned into a mushroom cloud of, you know,
*  weirdness.
*  They had the name in the name of optimization, but from the perspective of the developer,
*  that's not good.
*  Well, their issues with transcendental functions were just stupid.
*  Okay. So that's not even a trade off. That's just absolutely.
*  Yeah. They were doing range reduction for sine and cosine using a slightly wrong value for pi.
*  Got it. We've got 10 minutes. So in the interest of time, two questions. So one about Android and
*  one about life. So one, I mean, we could talk for many more hours. I hope eventually we might talk
*  again, but I got to ask you about Android and the use of Java there because it's one of the many
*  places where Java just has a huge impact on this world. Just on your opinion, is there things that
*  make you happy about the way and Java is used in the Android world? And are there things that
*  you wish were different?
*  I don't know how to do a short answer to that, but I have to do a short answer to that. So,
*  you know, I'm happy that they did it. Java had been running on cell phones at that time for
*  quite a few years and it worked really, really well. There were things about how they did it
*  and in particular, various ways that they kind of violated all kinds of contracts. The guy who
*  led it, Andy Rubin, he crossed a lot of lines. There's some lines crossed. Yeah, lines were
*  crossed that have since, you know, mushroomed into giant court cases.
*  And, you know, they didn't need to do that. And in fact, it would have been so much cheaper for them
*  to not cross lines. I mean, I suppose they didn't anticipate the success of this whole endeavor.
*  Or do you think at that time it was already clear that this is going to blow up?
*  I guess I sort of came to believe that it didn't matter what Andy did. It was going to blow up.
*  Okay.
*  I kind of started to think of him as like a manufacturer of bombs.
*  Yeah. Some of the best things in this world come about through a little bit of
*  explosive. Well, and some of the worst. And some of the worst, beautifully put. But is there,
*  and like you said, I mean, does that make you proud that the Java is in millions? I mean,
*  it could be billions of devices. Yeah. Well, I mean, it was in billions of phones before Android
*  came along. And, you know, I'm just as proud as, you know, of the way that like the smart card
*  standards adopted Java. And they did a, they, you know, everybody involved in that did a really good
*  job. And that's, you know, billions and billions. That's crazy. The SIM cards, you know, the SIM
*  cards in your pocket. Yeah. I mean, it's not outside of that world for a decade. So
*  I don't know how that has evolved, but, you know, it's just been crazy.
*  So on that topic, let me ask, again, there's a million technical things
*  we could talk about, but let me ask the absurd, the old philosophical question about life.
*  What do you hope when you look back at your life and people talk about you, write about you 500
*  years from now, what do you hope your legacy is? People not being afraid to take a leap of faith.
*  I mean, I, you know, I've got this, this kind of weird history of doing weird stuff and.
*  It worked out pretty damn well.
*  It worked out, right. And I think some of the weirder stuff that I've done
*  has been the coolest and some of it, some of it crashed and burned and,
*  you know, I think well over half of the stuff that I've done has crashed and burned.
*  Which has occasionally been really annoying.
*  But still you kept doing it.
*  But yeah. Yeah. Yeah. And, you know, there, you know, even when things crash and burn,
*  you at least learn something from it.
*  By way of advice, you know, people, developers, engineers, scientists, or just people who are
*  young to look up to you, what advice would you give them? How to, how to, you know,
*  to approach their life? Don't be afraid of risk.
*  It's okay to do stupid things once. Maybe a couple of times.
*  You know, you, you know, you get, you get a pass on the first time or two that you do something
*  stupid, you know, the third or fourth time. Yeah. Not so much. Yeah.
*  Um, but also, you know, I don't know why, but really early on, I started to think about
*  ethical choices in my life. And because I, a big science fiction fan,
*  um, I, I, I got to thinking about like just about every technical decision I make
*  in terms of how do you want, you know, are you building Blade Runner or Star Trek?
*  Which one's better?
*  Which, which future would you rather live in?
*  You know, so what's the, what's the answer to that?
*  Well, I would say I would sure rather live in the universe of Star Trek.
*  Yeah. That opens up a whole topic about AI, but that's a really interesting. Yeah. Yeah.
*  Yeah. It's a really interesting idea. So your favorite AI system would be data
*  from, from Star Trek as a most favorite would easily be Skynet.
*  Yeah. Beautifully put. I don't think there's a better way to end it. James,
*  I can't say enough how much of an honor it is to meet you to talk to you. Thanks so much
*  for wasting your time with me today.
*  Not a waste at all.
*  Thanks James.
*  All right. Thanks.
*  Thanks for listening to this conversation with James Gosling.
*  And thank you to our sponsors, Public Goods, BetterHelp and ExpressVPN.
*  Please check out these sponsors in the description to get a discount and to support this podcast.
*  If you enjoy this thing, subscribe on YouTube, review it with five stars on Apple Podcast,
*  follow on Spotify, support on Patreon, or connect with me on Twitter at Lex Friedman.
*  And now let me leave you with some words from James Gosling.
*  One of the toughest things about life is making choices.
*  Thank you for listening and hope to see you next time.

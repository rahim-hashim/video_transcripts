---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 6189s
Video Keywords: ['brian kernighan', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 441675
Video Rating: None
Video Description: Brian Kernighan is a professor of computer science at Princeton University. He co-authored the C Programming Language with Dennis Ritchie (creator of C) and has written a lot of books on programming, computers, and life including the Practice of Programming, the Go Programming Language, his latest UNIX: A History and a Memoir. He co-created AWK, the text processing language used by Linux folks like myself. He co-designed AMPL, an algebraic modeling language for large-scale optimization.

Support this podcast by supporting our sponsors:
- Eight Sleep: https://eightsleep.com/lex
- Raycon: http://buyraycon.com/lex

EPISODE LINKS:
Brian's website: https://www.cs.princeton.edu/~bwk/
Unix: A History and a Memoir (book): https://amzn.to/3fFJ1yM
Understanding the Digital World (book): https://amzn.to/30ktBJI

PODCAST INFO:
Podcast website:
https://lexfridman.com/podcast
Apple Podcasts:
https://apple.co/2lwqZIr
Spotify:
https://spoti.fi/2nEwCF8
RSS:
https://lexfridman.com/feed/podcast/
Full episodes playlist:
https://www.youtube.com/playlist?list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4
Clips playlist:
https://www.youtube.com/playlist?list=PLrAXtmErZgOeciFP3CBCIEElOJeitOr41

OUTLINE:
0:00 - Introduction
4:24 - UNIX early days
22:09 - Unix philosophy
31:54 - Is programming art or science?
35:18 - AWK
42:03 - Programming setup
46:39 - History of programming languages
52:48 - C programming language
58:44 - Go language
1:01:57 - Learning new programming languages
1:04:57 - Javascript
1:08:16 - Variety of programming languages
1:10:30 - AMPL
1:18:01 - Graph theory
1:22:20 - AI in 1964
1:27:50 - Future of AI
1:29:47 - Moore's law
1:32:54 - Computers in our world
1:40:37 - Life

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Brian Kernighan UNIX, C, AWK, AMPL, and Go Programming  Lex Fridman Podcast #109
**Lex Fridman:** [July 18, 2020](https://www.youtube.com/watch?v=O9upVbGSBFo)
*  The following is a conversation with Brian Kernigan, a professor of computer science at
*  Princeton University. He was a key figure in the computer science community in the early Unix days
*  alongside Unix creators Ken Thompson and Dennis Ritchie. He co-authored the C programming language
*  with Dennis Ritchie, the creator of C, and has written a lot of books on programming, computers,
*  and life including the practice of programming, the Go programming language, and his latest Unix,
*  a history, and a memoir. He co-created Auck, the text processing language used by Linux folks like
*  myself. He co-designed Ample, an algebraic modeling language that I personally love and have used a
*  lot in my life for large-scale optimization. I think I can keep going for a long time with
*  his creations and accomplishments, which is funny because given all that, he's one of the most humble
*  and kind people I've spoken to on this podcast. Quick summary of the ads, two new sponsors,
*  the amazing self-cooling 8 Sleep mattress and Raycon earbuds. Please consider supporting the
*  podcast by going to 8sleep.com slash Lex and going to buyraycon.com slash Lex. Click the links,
*  buy the stuff. It really is the best way to support this podcast and the journey I'm on.
*  If you enjoy this thing, subscribe on YouTube, review it with Firestars and Apple Podcasts,
*  support it on Patreon, or connect with me on Twitter at Lex Friedman. As usual, I'll do a few
*  minutes of ads now and never any ads in the middle that can break the flow of the conversation.
*  This show is sponsored by 8 Sleep and its incredible Pod Pro mattress that you can check out at
*  8sleep.com slash Lex to get $200 off. The mattress controls temperature with an app
*  and can cool down to as low as 55 degrees. Research shows that temperature has a big impact
*  on the quality of our sleep. Anecdotally, it's been a game changer for me. I love it. The
*  Pod Pro is packed with sensors that track heart rate, heart rate variability, and respiratory rate,
*  showing it all on their app once you wake up. Plus, if you have a partner, you can control
*  the temperature of each side of the bed. I don't happen to have one, but the 8 Sleep app reminds
*  me that I should probably get on that. So ladies, if a temperature controlled mattress isn't a good
*  reason to apply, I don't know what is. The app's health metrics are amazing, but the cooling alone
*  is honestly worth the money. As some of you know, I don't always sleep, but when I do,
*  I choose the 8 Sleep Pod Pro mattress. Check it out at 8sleep.com slash Lex to get $200 off.
*  This show is also sponsored by Raycon Earbuds. Get them at buyraycon.com slash Lex. They've
*  quickly become my main method of listening to podcasts, audiobooks, and music when I run,
*  do the push-ups and pull-ups that I've begun to hate at this point, or just living life. In fact,
*  I often listen to brown noise with ease when I'm thinking deeply about something.
*  It helps me focus the mind. They're super comfortable, pair easily, great sound,
*  great bass, six hours of playtime. In fact, for fun, I have one of the earbuds in now,
*  and I'm listening to Europa by Santana, probably one of my favorite guitar songs.
*  It kind of makes me feel like I'm in a music video. So they told me to say that a bunch of
*  celebrities use these like Snoop Dogg, Melissa Etheridge, and Cardi B. I don't even know who
*  Cardi B is, but her earbud game is on point. To mention celebrities I actually care about,
*  I'm sure if Richard Feynman was still with us, he'd be listening to the Joe Rogan experience
*  with Raycon Earbuds. Get them at buyraycon.com slash Lex. It's how they know I sent you,
*  and increases the chance that he'll support this podcast in the future.
*  So for all of the sponsors, click all of the links. It really helps this podcast.
*  And now here's my conversation with Brian Kernigan.
*  Unix started being developed 50 years ago. It'd be more than 50 years ago. Can you tell the story,
*  like you describe in your new book, of how Unix was created?
*  Ha, if I can remember that far back, it was some while ago. So I think the gist of it is that at
*  Bell Labs in 1969, there were a group of people who had just finished working on the Multics
*  project, which was itself a follow-on to CTSS. So we can go back sort of an infinite regress in time,
*  but the CTSS was a very, very, very nice time sharing system. It was very nice to use. I
*  actually used it as that summer I spent in Cambridge in 1966. What was the hardware there?
*  So what's the operating system? What's the hardware there? What's the CTS look like?
*  So CTSS looked like kind of like a standard time sharing system. Certainly at the time,
*  it was the only time sharing. Let's go back to the basic. What's the time sharing system?
*  Okay. In the beginning was the word and the word was... And then there was time sharing systems.
*  Yeah. If we go back into, let's call it the 1950s and early 1960s, most computing was done on very
*  big computers, physically big, although not terribly powerful by today's standards, that were maintained
*  in very large rooms and you used things like punch cards to write your programs on, talk to them. So
*  you would take a deck of cards, write your program on it, send it over a counter, hand it to an
*  operator and some while later back would come something that said, oh, you made a mistake and
*  then you'd recycle. And so it was very, very slow. So the idea of time sharing was that you take
*  basically that same computer, but connect to it with something that looked like an electric typewriter.
*  They could be a long distance away, it could be close, but fundamentally what the operating
*  system did was to give each person who was connected to it and wanting to do something,
*  a small slice of time to do a particular job. So I might be editing a file, so I would be typing.
*  And every time I hit a keystroke, the operating system would wake up and said, oh, he typed
*  character. Let me remember that. And then it'd go back to doing something else. So it'd be going
*  around and around a group of people who were trying to get something done, giving each a small
*  slice of time and giving them each the illusion that they pretty much had the whole machine to
*  themselves. And hence time sharing, that is sharing the computing time resource of the computer among
*  a number of people who were doing it. Without the individual people being aware that there's others
*  in a sense, the illusion, the feelings that the machine is your own. Pretty much that was the idea.
*  Yes, if it were well done and if it were fast enough and other people weren't doing too much,
*  you did have the illusion that you had the whole machine to yourself and it was very much better
*  than the punch card model. And so CTSS, the compatible time sharing system, was I think
*  arguably the first of these. It was done, I guess, technically in 64 or something like that. It ran
*  on an IBM 7094, slightly modified to have twice as much memory as the norm. It had two banks of
*  32K words instead of one. So 32K words. Each word was 36 bits. So call it about 150 kilobytes
*  times two. So by today's standards, that's down in the noise. But at the time that was a lot of
*  memory and memory was expensive. So CTSS was just a wonderful environment to work on. It was done
*  by the people at MIT, led by Fernando Corbatov, Corby, who died just earlier this year, and a
*  bunch of other folks. And so I spent the summer of 66 working on that. Had a great time, met a lot
*  of really nice people and indirectly knew of people at Bell Labs who were also working on a follow-on
*  to CTSS that was called Multics. So Multics was meant to be the system that would do everything
*  that CTSS did but do it better for a larger population. All the usual stuff.
*  Now the actual time sharing, the scheduling, what's the algorithm that performs the scheduling?
*  What's that look like? How much magic is there? What are the metrics? How does it all work in
*  the beginning? So the answer is I don't have a clue. I think the basic idea was nothing more than
*  who all wants to get something done. Suppose that things are very quiet in the middle of the night,
*  then I get all the time that I want. Suppose that you and I are contending at high noon for something
*  like that, then probably the simplest algorithm is a round robin one that gives you a bit of time,
*  gives me a bit of time. And then we could adapt to that. Like what are you trying to do? Are you
*  text editing or are you compiling or something? And then we might adjust the schedule or according
*  to things like that. So okay, so Multics was trying to just do some of the
*  cleaning up a little bit. Well, it was meant to be much more than that. So Multics was the
*  multiplexed information and computing service and it was meant to be a very large thing that would
*  provide computing utility. Something that where you could actually think of it as just a plug in
*  the wall service. Sort of like cloud computing today. Same idea, but 50 odd years earlier.
*  And so what Multics offered was a richer operating system environment, a piece of hardware that
*  was better designed for doing the kind of sharing of resources and presumably lots of other things.
*  Do you think people at that time had the dream of what cloud computing is starting to become now,
*  which is computing is everywhere that you can just plug in almost, you know, and you never know how
*  the magic works. You just kind of plug in at your little computation that you need to perform and
*  it does it. Was that the dream? I don't know where that was the dream. I wasn't part of it
*  at that point. I remember I was an intern for summer, but my sense is given that it was over
*  50 years ago, yeah, they had that idea that it was an information utility, that it was something where
*  if you had a computing task to do, you could just go and do it. Now I'm betting that they didn't have
*  the same view of computing for the masses, let's call it the idea that, you know,
*  your grandmother would be shopping on Amazon. I don't think that was part of it, but if your
*  grandmother were a programmer, it might be very easy for her to go and use this kind of utility.
*  What was your dream of computers at that time? What did you see as the future of computers?
*  Could you have predicted what computers are today?
*  Oh, short answer, absolutely not. I have no clue. I'm not sure I had a dream. It was a dream job
*  in the sense that I really enjoyed what I was doing. I was surrounded by really, really nice
*  people. Cambridge is a very fine city to live in in the summer, less so in the winter when it snows,
*  but in the summer it was a delightful time. And so I really enjoyed all of that stuff
*  and I learned things. And I think the good fortune of being there for summer led me then to get a
*  summer job at Bell Labs the following summer. And that was going to useful for the future.
*  So this Bell Labs is this magical, legendary place. So first of all, where is Bell Labs?
*  And can you start talking about that journey towards Unix at Bell Labs?
*  Yeah, so Bell Labs is physically scattered around at the time, scattered around New Jersey. The
*  primary location was in a town called Murray Hill, or a location called Murray Hill is actually
*  across the boundary between two small towns in New Jersey called New Provenance and Berkeley
*  Heights. Think of it as about 15, 20 miles straight west of New York City,
*  and therefore about an hour north of here in Princeton. And at that time it had,
*  make up a number, three or four thousand people there, many of whom had PhDs and mostly doing
*  physical sciences, chemistry, physics, materials kinds of things, but very strong math and
*  rapidly growing interest in computing as people realized you could do things with computers.
*  That you might not have been able to do before. You could replace labs with computers that had
*  worked on models of what was going on. So that was the essence of Bell Labs. And again,
*  I wasn't a permanent employee there. That was another internship. I got lucky in internships.
*  I mean, if you could just link in a little bit, what was in the air there? Because some of this,
*  the number of Nobel prizes, the number of Turing Awards and just legendary computer scientists
*  that come from their inventions, including developments, including UNIX, it's just,
*  it's unbelievable. So was there something special about that place?
*  Oh, I think there was very definitely something special. I mentioned the number of people,
*  so very large number of people, very highly skilled and working in an environment where
*  there was always something interesting to work on because the goal of Bell Labs,
*  which was a small part of AT&T, which provided basically the country's phone service,
*  the goal of AT&T was to provide service for everybody. And the goal of Bell Labs was to
*  try and make that service keep getting better. So improving service. And that meant doing
*  research on a lot of different things, physical devices like the transistor or fiber optical
*  cables or microwave systems, all of these things the labs worked on. And it was kind of just the
*  beginning of real boom times in computing as well. When I was there, I went there first in 66.
*  So computing was at that point fairly young. And so people were discovering that you could
*  do lots of things with computers. So how was UNIX born?
*  So Multics, in spite of having an enormous number of really good ideas, lots of good people working
*  on it, fundamentally didn't live up at least in the short run, and I think ultimately really ever,
*  its goal of being this information utility. It was too expensive and certainly what was promised
*  was delivered much too late. And so in roughly the beginning of 1969, Bell Labs pulled out of
*  the project. The project at that point had included MIT, Bell Labs, and General Electric.
*  General Electric made computers. So General Electric was the hardware operation. So Bell Labs,
*  realizing this wasn't going anywhere on a time scale, they cared about, pulled out of the project.
*  And this left several people with an acquired taste for really, really nice computing environments,
*  but no computing environment. And so they started thinking about what could you do if you're going
*  to design a new operating system that would provide the same kind of comfortable computing
*  as CTSS had, but also the facilities of something like Multics brought forward.
*  And so they did a lot of paper design stuff. And at the same time, Ken Thompson found what
*  is characterized as a little used PDP-7, where he started to do experiments with file systems,
*  just how do you store information on a computer in a deficient way. And then this famous story
*  that his wife went away to California for three weeks, taking their one-year-old son,
*  and three weeks, and he sat down and wrote an operating system, which ultimately became Unix.
*  So software productivity was good in those days.
*  So PDP, what's a PDP-7? So it's a piece of hardware.
*  Yeah, it's a piece of hardware. It was one of early machines made by Digital Equipment Corporation
*  deck. And it was a mini computer, so called. I would have to look up the numbers exactly,
*  but it had a very small amount of memory, maybe 16K, 16 bit words or something like that, relatively
*  slow. Probably not super expensive. Maybe again, making this up, I'd have to look it up $100,000
*  or something like that. Which is not super expensive in those days, right?
*  It was expensive. It was enough that you and I probably wouldn't be able to buy one,
*  but a modest group of people could get together. But in any case, it came out, if I recall, in 1964.
*  So by 1969, it was getting a little obsolete. And that's why it was a little used.
*  If you can sort of comment, what do you think it's like to write an operating system like that?
*  So that process that Ken went through in three weeks, because you were, I mean,
*  you're a part of that process. You contributed a lot to Unix's early development. So what
*  do you think it takes to do that first step, that first kind of, from design to reality on the PDP?
*  Well, let me correct one thing. I had nothing to do with it. So I did not write it. I have never
*  written operating system code. And so I don't know. Now, an operating system is simply code.
*  And this first one wasn't very big, but it's something that lets you run processes,
*  of some, let you execute some kind of code that has been written. It lets you store information
*  for periods of time so that it doesn't go away when you turn the power off or reboot or something
*  like that. And there's a kind of a core set of tools that are technically not part of an operating
*  system, but you probably need them. In this case, Ken wrote an assembler for the PDP-7 that worked.
*  He did a text editor so that he could actually create text. He had the file system stuff that
*  he had been working on. And then the rest of it was just a way to load things, executable code
*  from the file system into the memory, give it control, and then recover control when it was
*  finished or in some other way quit. What was the code written in the primarily the programming
*  language? Was it in assembly? Yeah, PDP-7 assembler that Ken created. These things were assembly
*  language until probably the, call it 1973 or 74, something like that. Forgive me if it's a dumb
*  question, but it feels like a daunting task to write any kind of complex system in assembly.
*  Absolutely. It feels like impossible to do any kind of what we think of as software engineering
*  with assembly, to work on a big picture. I think it's hard. It's been a long time since I wrote
*  assembly language. It is absolutely true that in assembly language, if you make a mistake,
*  nobody tells you. There are no training wheels whatsoever. And so stuff doesn't work. Now what?
*  And there's no debuggers. Well, there could be debuggers, but that's the same problem, right?
*  How do you actually get something that will help you debug it? So part of it is an ability to
*  see the big picture. Now these systems were not big in the sense that today's pictures are. So the
*  big picture was in some sense more manageable. I mean, then realistically there's an enormous
*  variation in the capabilities of programmers. And Ken Thompson, who did that first one, is kind of
*  the singularity in my experience of programmers with no disrespect to you or even to me. He's
*  several leagues removed. I know there's levels. It's a fascinating thing that there are
*  unique stars in particular in the programming space and at a particular time. The time matters
*  too, the timing of when that person comes along. And a wife does have to leave. There's this weird
*  timing that happens that in an all of a sudden something beautiful is created. I mean, how does
*  it make you feel that there's a system that was created in three weeks or maybe you can even say
*  on a whim, but not really. But of course quickly that is now you could think of most of the computers
*  in the world run on a Unix like system. Right. How do you like if you kind of zoom from the
*  alien perspective, if you were just observing earth, that all of a sudden these computers took
*  over the world and they started from this little initial seed of a Unix. How does that make you
*  feel? It's quite surprising. And you asked earlier about prediction. The answer is no, there's no way
*  you could predict that kind of evolution. And I don't know whether it was inevitable or just a
*  whole sequence of blind luck, I suspect more of the latter. And so I look at it and think,
*  gee, that's kind of neat. I think the real question is what does Ken think about that?
*  Cause he's the guy arguably from whom it really came, tremendous contributions from Dennis Richie
*  and then others around in that Bell Labs environment. But if you had to pick a single
*  person, that would be Ken. So you've written a new book, Unix, a history and a memoir. Are there
*  some memorable human stories funny or profound from that time that just kind of stand out?
*  Oh, there's a lot of them in a sense. And again, it's a question of can you resurrect them
*  in real time? Why does memory fails? But I think part of it was that Bell Labs at the time was a
*  very special kind of place to work because there were a lot of interesting people and the environment
*  was very, very open and free. It was a very cooperative environment, very friendly environment.
*  And so if you had an interesting problem, you go and talk to somebody and they might help you with
*  the solution. And it was a kind of a fun environment too, in which people did strange things and
*  often tweaking the bureaucracy in one way or another.
*  So rebellious in certain kinds of ways.
*  In some ways, yeah, absolutely. I think most people didn't take too kindly to the bureaucracy
*  and I'm sure the bureaucracy put up with an enormous amount that they didn't really want to.
*  So maybe to linger on it a little bit, do you have a sense of what the philosophy that
*  characterizes Unix is? The design, not just the initial, but just carry through the years,
*  being there, being around it? What's the fundamental philosophy behind the system?
*  I think one aspect, the fundamental philosophy was to provide an environment that made it easy
*  to write or easier productive to write programs. So it was meant as a programmer environment. It
*  wasn't meant specifically as something to do some other kind of job. For example, it was used
*  extensively for word processing, but it wasn't designed as a word processing system. It was
*  used extensively for lab control, but it wasn't designed for that. It was used extensively as a
*  front end for big other systems, big dump systems, but it wasn't designed for that.
*  It was meant to be an environment where it was really easy to write programs. So the programmers
*  could be highly productive. And part of that was to be a community. And there's some observation
*  from Dennis Ritchie, I think at the end of the book, that says that from his standpoint,
*  the real goal was to create a community where people could work as programmers on a system.
*  I think in that sense, certainly for many, many years, it succeeded quite well at that. And part
*  of that is the technical aspects of because it made it really easy to write programs, people did
*  write interesting programs. Those programs tended to be used by other programmers. And so it was
*  kind of a virtuous circle of more and more stuff coming out that was really good for programmers.
*  And you were part of that community of programmers. So what was it like writing
*  programs on that early UNIX? It was a blast. It really was.
*  I liked to program. I'm not a terribly good programmer, but it was a lot of fun to write
*  code. And in the early days, there was an enormous amount of what you would today,
*  I suppose, called low hanging fruit. People hadn't done things before. And this was this
*  new environment and the whole combination of nice tools and very responsive system
*  and tremendous colleagues made it possible to write code. You could have an idea in the morning,
*  you could do an experiment with it. You could have something limping along that night or the
*  next day and people would react to it and they would say, Oh, that's wonderful. But you're really
*  screwed up here. And the feedback loop was then very, very short and tight. And so a lot of things
*  got developed fairly quickly that in many cases still exist today. And I think that was part of
*  what made it fun because programming itself is fun. It's puzzle solving in a variety of ways,
*  but I think it's even more fun when you do something that somebody else then uses. Even
*  if they whine about it not working, the fact that they used it is part of the reward mechanism.
*  And what was the method of interaction, the communication, that feedback loop?
*  I mean, this is before the internet. Certainly before the internet. It was mostly
*  physical right there. Somebody would come into your office and say something.
*  So these places are all close by, like offices are nearby, so you're really lively interaction.
*  Yeah. Bell Labs was fundamentally one giant building and most of the people were involved
*  in this unique stuff. We're in two or three quarters and there was a room. Oh, how big was it?
*  Probably call it 50 feet by 50 feet. Make up a number of that, which had some access to computers
*  there as well as in offices and people hung out there and it had a coffee machine.
*  And so it was mostly very physical. We did use email, of course, but it was fundamentally
*  for a long time all on one machine. So there was no need for internet.
*  It's fascinating to think about what computing would be today without Bell Labs.
*  It seems so many people being in the vicinity of each other,
*  sort of getting that quick feedback, working together, so many brilliant people.
*  I don't know where else that could have existed in the world given how that came together.
*  How does that make you feel that little element of history?
*  Well, I think that's very nice, but in a sense it's survivor bias. And if it hadn't happened
*  at Bell Labs, there were other places that were doing really interesting work as well. Xerox Park
*  is perhaps the most obvious one. Xerox Park contributed an enormous amount of good material.
*  And many of the things we take for granted today in the same way came from Xerox Park experience.
*  I don't think they capitalized in the long run as much. Their parent company was perhaps not
*  as lucky in capitalizing on this. Who knows? But that's certainly another place where there
*  was a tremendous amount of influence. There were a lot of good university activities. MIT was
*  obviously no slouch in this kind of thing, and others as well.
*  Unix turned out to be open source because of the various ways that AT&T operated.
*  The focus was on telephones.
*  I think that's a mischaracterization in a sense. It absolutely was not open source. It was very,
*  definitely proprietary, licensed. But it was licensed freely to universities in source code
*  form for many years. And because of that, generations of university students and their
*  faculty people grew up knowing about Unix. And there was enough expertise in the community that
*  it then became possible for people to go off in their own direction and build something that
*  looked Unix-like. The Berkeley version of Unix started with that licensed code and gradually
*  picked up enough of its own code contributions, notably from people like Bill Joy, that
*  eventually it was able to become completely free of any AT&T code. Now, there was an enormous amount
*  of legal jockeying around this in the late, early to late 80s, early 90s, something like that.
*  And then I guess the open source movement might've started when Richard Stallman started to think
*  about this in the late 80s. And by 1991, when Torvalds decided he was going to do a
*  Unix-like operating system, there was enough expertise in the community that first he had
*  a target. He could see what to do because the kind of the Unix system call interface and the
*  tools and so on were there. And so he was able to build an operating system that at this point,
*  when you say Unix, in many cases, what you're really thinking is Linux.
*  Linux, yeah. But it's funny that from my distant perception, I felt that Unix was open source
*  without actually knowing it. But what you're really saying, it was just freely licensed.
*  It was freely licensed.
*  So it felt open source because universities are not trying to make money. So there,
*  it felt open source in a sense that you can get access if you want it.
*  Right. And a very, very, very large number of universities had the license and they were
*  able to talk to all the other universities who had the license. And so technically not open,
*  technically belonging to AT&T, pragmatically pretty open.
*  And so there's a ripple effect that all the faculty and the students then all grew up and
*  they went throughout the world and permeated in that kind of way. So what
*  kind of features do you think make for a good operating system?
*  If you take the lessons of Unix, you said, make it easy for programmers. That seems to be
*  an important one. But also Unix turned out to be exceptionally robust and efficient.
*  So is that an accident when you focus on the programmer or is that a natural outcome?
*  I think part of the reason for efficiency was that it began on extremely modest hardware,
*  very, very, very tiny. And so you couldn't get carried away. You couldn't do a lot of
*  complicated things because you just didn't have the resources, either processor speed or memory.
*  And so that enforced a certain minimality of mechanisms and maybe a search for generalizations
*  so that you would find one mechanism that served for a lot of different things rather
*  than having lots of different special cases. I think the file system in Unix is a good example
*  of that. The file system interface in its fundamental form is extremely straightforward.
*  And that means that you can write code very, very effectively for the file system. And then
*  one of those generalizations is that, gee, that file system interface works for all kinds of other
*  things as well. And so in particular, the idea of reading and writing to devices is the same as
*  reading and writing to a disk that has a file system. And then that gets carried further in
*  other parts of the world. Processes become in effect files in a file system. And the Plan 9
*  operating system, which came along, I guess, in the late 80s or something like that, took a lot
*  of those ideas from the original Unix and tried to push the generalization even further so that in
*  Plan 9, a lot of different resources are file systems. They all share that interface. So that
*  would be one example where finding the right model of how to do something means that an awful
*  lot of things become simpler. And it means therefore that more people can do useful,
*  interesting things with them without having to think as hard about it.
*  So you said you're not a very good programmer.
*  That's true.
*  You're the world's most modest human being. Okay. But you'll continue saying that.
*  I understand how this works. But you do radiate a sort of love for programming.
*  So let me ask, do you think programming is more an art or a science? Is it creativity or
*  kind of rigor?
*  I think it's some of each. It's some combination. Some of the art is figuring out what it is that
*  you really want to do. What should that program be? What would make a good program? And that's
*  some understanding of what the task is, what the people who might use this program want.
*  And I think that's art in many respects. The science part is trying to figure out how to do
*  it well. And some of that is real computer science-y stuff, like what algorithm should we use at some
*  point, mostly in the sense of being careful to use algorithms that will actually work properly,
*  scale properly, avoiding quadratic algorithms when a linear algorithm should be the right thing.
*  That kind of more formal view of it. Same thing for data structures. But also it's, I think,
*  an engineering field as well. And engineering is not quite the same as science because engineering
*  you're working with constraints. You have to figure out not only what is a good algorithm
*  for this kind of thing, but what's the most appropriate algorithm given the amount of time
*  we have to compute, the amount of time we have to program, what's likely to happen in the future
*  with maintenance, who's going to pick this up in the future, all of those kind of things that if
*  you're an engineer you get to worry about. Whereas if you think of yourself as a scientist, well,
*  you can maybe push them over the horizon in a way. And if you're an artist, what's that?
*  So just on your own personal level, what's your process like of writing a program? Say
*  small and large, sort of tinkering with stuff. Do you just start coding right away and just kind
*  of evolve iteratively with a loose notion? Or do you plan on a sheet of paper first and then kind
*  of design what they teach you in the kind of software engineering courses in undergrad or
*  something like that? What's your process like? It's certainly much more the informal incremental.
*  First, I don't write big programs at this point. It's been a long time since I wrote a program that
*  was more than, I call it a few hundred or more lines, something like that. Many of the programs
*  I write are experiments for either something I'm curious about or often for something that
*  I want to talk about in a class. And so those necessarily tend to be relatively small.
*  A lot of the kind of code I write these days tends to be for sort of exploratory data analysis,
*  where I've got some collection of data and I want to try and figure out what on earth is going on
*  in it. And for that, those programs tend to be very small. Sometimes you're not even programming,
*  you're just using existing tools like counting things. Or sometimes you're writing OCK scripts
*  because two or three lines will tell you something about a piece of data. And then when it gets
*  bigger, well, then I will probably write something in Python because that scales better. Up to,
*  call it a few hundred lines or something like that. And it's been a long time since I wrote
*  programs that were much more than that. Speaking of data exploration and OCK, first, what is OCK?
*  So OCK is a scripting language that was done by myself, Al Ajo and Peter Weinberger. We did
*  that originally in the late seventies. It was a language that was meant to make it really easy to
*  do quick and dirty tasks like counting things or selecting interesting information from basically
*  all text files, rearranging it in some way or summarizing it. It runs a command on each line
*  of a file. I mean, it's still exceptionally widely used today. Oh, absolutely. Yeah.
*  And it's so simple and elegant. Sort of the way to explore data. Turns out you can just write a
*  script that does something seemingly trivial in a single line. And that giving you that slice of
*  the data somehow reveals something fundamental about the data. And that keeps, that seems to work
*  still. Yeah. It's very good for that kind of thing. And that's sort of what it was meant for.
*  I think what we didn't appreciate was that the model was actually quite good for a lot of data
*  processing kinds of tasks and that it's kept going as long as it has. Cause at this point,
*  it's over 40 years old and it's still, I think, a useful tool. And well, this is paternal interest,
*  I guess, but I think in terms of programming languages, you get the most bang for the buck
*  by learning Auck. And it doesn't scale the big programs, but it does pretty darn well on these
*  little things where you just want to see all the somethings in something. So yeah, I find,
*  I probably write more Auck than anything else at this point. So what kind of stuff do you love
*  about Auck? Like is there, if you can comment on sort of things that give you joy when you can,
*  in a simple program, reveal something about the data? Is there something that stands out
*  from particular features? I think it's mostly the selection of default behaviors that you sort of
*  hinted at it a moment ago. What Auck does is to read through a set of files and then within each
*  file, it writes through each of the lines. And then on each of the lines, it has a set of patterns
*  that it looks for. That's your Auck program. And if one of the patterns matches, there is a
*  corresponding action that you might perform. And so it's kind of a quadruply nested loop or
*  something like that. And that's all completely automatic. You don't have to say anything about
*  it. You just write the pattern and the action and then run the data by it. And so that paradigm
*  for programming is a very natural and effective one. And I think we captured that reasonably
*  well in Auck. And it does other things for free as well. It splits the data into fields so that on
*  each line there is fields separated by white space or something. And so it does that for free. You
*  don't have to say anything about it. And it collects information as it goes along. Like what
*  line are we on? How many fields are there on this line? So lots of things that just make it so that
*  a program, which in another language, let's say Python, would be five, 10, 20 lines in Auck is one
*  or two lines. And so because it's one or two lines, you can do it on the shell. You don't have to open
*  up another whole thing. You can just do it right there in the interaction with the operative.
*  Is there other shell commands that you love over the years that you really enjoy using?
*  Yeah, grep does everything. So grep is a simpler version of Auck, I would say.
*  In some sense, yeah, right. Because- What is grep?
*  So grep is it basically searches the input for particular patterns, regular expressions,
*  technically, of a certain class. And it has that same paradigm that Auck does. It's a pattern
*  action thing. It reads through all the files and then all the lines in each file, but it has a
*  single pattern, which is the regular expression you're looking for, and a single action printed
*  if it matches. So in that sense, it's a much simpler version and you could write
*  grep in Auck as a one liner. And I use grep probably more than anything else at this point,
*  just because it's so convenient and natural. Why do you think it's such a powerful tool, grep,
*  knock? Why do you think operating systems like Windows, for example, don't have it?
*  Sort of, you can, of course, I use the, which is amazing now, there's a Windows for Linux,
*  like which you could basically use all the fun stuff like Auck and grep inside of Windows,
*  but Windows naturally sort of as part of the graphical interface, the simplicity of grep,
*  sort of searching through a bunch of files and just popping up naturally. Why don't you think
*  that- Why do you think that's unique to the Linux environment?
*  I don't know. It's not strictly unique, but it's certainly focused there. And I think some of it's
*  the weight of history that Windows came from MS-DOS. MS-DOS was a pretty pathetic operating
*  system, although common on an unboundedly large number of machines. But somewhere in roughly the
*  90s, Windows became a graphical system. And I think Microsoft spent a lot of their energy on
*  making that graphical interface what it is. And that's a different model of computing.
*  It's a model of computing that where you point and click and sort of experiment with menus.
*  It's a model of computing works rather well for people who are not programmers.
*  You just want to get something done. Whereas teaching something like the command line
*  to non-programmers turns out to sometimes be an uphill struggle. And so I think Microsoft
*  probably was right in what they did. Now you mentioned Whistle or whatever it's called,
*  the Linux. I wonder what it's pronounced. W-S-L is what,
*  I've never actually pronounced the whistle. I like it.
*  I have no idea. But there have been things like that for long. SigWin, for example,
*  which is a wonderful collection of take all your favorite tools from Unix and Linux and just make
*  them work perfectly on Windows. And so that's something that's been going on for at least 20
*  years, if not longer. And I use that on my one remaining Windows machine routinely because
*  if you're doing something that is batch computing, suitable for command line,
*  that's the right way to do it because the Windows equivalents are, if nothing else,
*  not familiar to me. But I would definitely recommend to people
*  to, if they don't use SigWin, to try Whistle. Yes.
*  I've been so excited that I could use Bash, write scripts quickly in Windows. It's changed my life.
*  Okay. What's your perfect programming setup? What computer, what operating system,
*  what keyboard, what editor? Yeah. Perfect is too strong a word.
*  It's way too strong a word. What I use by default, I have at this point a 13-inch MacBook Air,
*  which I use because it's kind of a reasonable balance of the various things I need. I can carry
*  it around. It's got enough computing horse bars, screen's big enough, keyboard's okay.
*  And so I basically do most of my computing on that. I have a big iMac in my office that I use
*  from time to time as well, especially when I need a big screen, but otherwise it tends not to be
*  used that much. Editor.
*  I use mostly SAM, which is an editor that Rob Pike wrote long ago at Bell Labs.
*  And did that, sorry to interrupt, does that precede VI?
*  It posts, it post dates both VI and eMax. It is derived from Rob's experience with ED and VI.
*  That's the original Unix editor. Oh, wow.
*  Dated probably before you were born. So what's, actually what's the history of editors? Can you
*  briefly, this is such a fact, I use eMax, I'm sorry to say, sorry to come out with that. But
*  what's the kind of interplay there? So in ancient times, call it the first time sharing systems,
*  going back to what we were talking about, there were editors, there was an editor on CTSS that
*  I don't even remember what it was called, it might've been edit, where you could type text,
*  program text and it would do something or document text.
*  You could save the text.
*  And save it. You could edit it. The usual thing that you would get in an editor.
*  And Ken Thompson wrote an editor called QED, which was very, very powerful. But these were all
*  totally a command-based, they were not most, or cursor-based because it was before mice and
*  even before cursors because they were running on terminals that printed on paper. Okay. No CRT type
*  displays, let alone LEDs. And so then when Unix came along, Ken took QED and stripped it way,
*  way, way, way down. And that became an editor that he called ED. It was very simple, but it was a
*  line-oriented editor. And so you could load a file and then you could talk about the lines one
*  through the last line and you could print ranges of lines. You could add text, you could delete
*  text, you could change text, or you could do a substitute command that would change things within
*  a line or within groups of lines. So you can work on the parts of a file essentially. Yeah.
*  You could work on any part of it, the whole thing or whatever, but it was entirely
*  command line-based and it was entirely on paper. Okay. Paper. And that meant that you changed-
*  Actual paper.
*  Yeah, right. Real paper. And so if you changed the line, you had to print that line using up
*  another line of paper to see what change caused. Okay. Yeah. So when CRT displays came along,
*  then you could start to use cursor control and you could sort of move where you were on the screen
*  without reprinting every time.
*  Without reprinting. And there were a number of editors there. The one that I was most familiar
*  with and still use is VI, which was done by Bill Choi. And so that dates from probably the late
*  70s as a guess. And it took full advantage of the cursor controls. I suspected EMAX was
*  roughly at the same time, but I don't know. I've never internalized EMAX. So I use, at this point,
*  I stopped using EDL, although I still can. I use VI sometimes and I use SAM when I can.
*  And SAM is available on most systems?
*  It was, it is available. You have to download it yourself from typically the Plan 9 operating
*  system distribution. It's been maintained by people there. And so I'll get home tonight.
*  I'll try it. It's cool. It sounds fascinating. Although my love is with Lisp and EMAX, I've
*  went into that hippie world of-
*  I think it's a lot of things. What religion were you brought up with?
*  Yeah, that's true. That's right. Most of the actual programming I do is C, C++ and Python,
*  but my weird sort of, yeah, my religious upbringing is in Lisp. So can you take on
*  the impossible task and give a brief history of programming languages from your perspective?
*  So I guess you could say programming languages started probably in what, the late
*  40s or something like that. People used to program computers by basically putting in
*  zeros and ones using something like switches on a console. And then, or maybe holes in paper tapes,
*  something like that. So extremely tedious, awful, whatever. And so I think the first
*  programming languages were relatively crude assembly languages where people would
*  basically write a program that would convert mnemonics like add add into whatever the bit
*  pattern was that corresponded to an add instruction. And they would do the clerical work of figuring
*  out where things were. So you could put a name on a location in a program and the assembler would
*  figure out where that corresponded to when the thing was all put together and dropped into
*  memory. And early on, and this would be the late 40s and very early 50s, there were assemblers
*  written for the various machines that people used. You may have seen in the paper just a couple days
*  ago, Tony Berker died. He did this thing in Manchester called the, called auto code, a language
*  which I knew only by name. But it sounds like it was a flavor of assembly language, sort of a little
*  higher in some ways. And it replaced a language that Alan Turing wrote, which you put in zeros and
*  ones, but you put them in backwards order because that was a hardware word. Very strict.
*  That's right. Yeah, yeah, that's right. Backwards.
*  So assembly languages, then let's call that the early 1950s. And so every different flavor
*  of computer has its own assembly language. So the Edsac had its and the Manchester had its
*  and the IBM, whatever, 7090 or 704 or whatever had its and so on. So everybody had their own
*  assembly language. And assembly languages have a few commands, additions, subtraction, then
*  branching of some kind if then type of situation. Right. They have exactly in their simplest form,
*  at least one instruction per or one assembly language instruction per instruction in the
*  machines repertoire. And so you have to know the machine intimately to be able to write programs
*  in it. And if you write an assembly language program for one kind of machine, and then you
*  say, geez, it's nice. I'd like it in a different machine. Start over. Okay. So very bad. And so
*  what happened in the late fifties was people realized you could play this game again, and you
*  could move up a level in writing or creating languages that were closer to the way that real
*  people might think about how to write code. And there were, I guess, arguably three or four at
*  that time period. There was Fortran, which came from IBM, which was formula translation meant to
*  make it easy to do scientific and engineering computation. I just know that formula translation.
*  That's what I stood for. I was COBOL, which is the common business oriented language that
*  Grace Hopper and others worked on, which was aimed at business kinds of tasks.
*  There was ALGOL, which was mostly meant to describe algorithmic computations.
*  I guess you could argue basic was in there somewhere. I think it's just a little later.
*  And so all of those moved the level up. And so they were closer to what you and I might think
*  of as we were trying to write a program. And they were focused on different domains, Fortran for
*  formula translation, engineering computations, let's say COBOL for business, that kind of thing.
*  And still used today, at least Fortran probably.
*  Oh yeah, COBOL too. But the deal was that once you moved up that level, then you,
*  let's call it Fortran, you had a language that was not tied to a particular kind of hardware
*  because a different compiler would compile for different kinds of hardware. And that meant
*  two things. It meant you only had to write the program once, which was very important.
*  And it meant that you could, in fact, if you were a random engineer, physicist, whatever,
*  you could write that program yourself. You didn't have to hire a programmer to do it for you.
*  Might not be as good as you'd get with a real programmer, but it was pretty good.
*  And so it democratized and made much more broadly available the ability to write code.
*  So it puts the power of programming into the hands of people like you.
*  Yeah. Anybody who wants to, who is willing to invest some time in learning a programming
*  language and is not then tied to a particular kind of computer. And then in the seventies,
*  you get system programming languages of which C is the survivor.
*  What does system programming languages mean?
*  Programs that, programming languages that would take on the kinds of things that would
*  necessary to write so-called system programs, things like text editors or assemblers or compilers
*  or operating systems themselves, those kinds of things. And Fortran-
*  Feature rich. They have to be able to do a lot of stuff, a lot of memory management,
*  access processes, and all that kind of stuff.
*  It's a different flavor of what they're doing. They're much more in touch with the actual
*  machine in a, but in a positive way. That is you can talk about memory in a more controlled way.
*  You can talk about the different data types that the machine supports and the way they're,
*  and more ways to structure and organize data. And so the system programming languages,
*  there was a lot of effort in that in the, call it the late sixties, early seventies.
*  C is, I think, the only real survivor of that. And then what happens after that,
*  you get things like object-oriented programming languages, because as you write programs in a
*  language like C, at some point scale gets to you and it's too hard to keep track of the pieces.
*  And there's no guardrails or training wheels or something like that to prevent you from doing
*  bad things. So C++ comes out of that tradition. And then it took off from there. I mean,
*  there's also a parallel, slightly parallel track with a little bit of functional stuff with Lisp
*  and so on. But I guess from that point, it's just an explosion of languages. There's the
*  Java story. There's the JavaScript. There's all the stuff that the cool kids these days are doing
*  with Rust and all that. So what's to you? You wrote a book, C Programming Language.
*  And C is probably one of the most important languages in the history of programming languages.
*  If you kind of look at impact, what do you think is the most elegant or powerful part of C?
*  Why did it survive? Why did it have such a long lasting impact?
*  I think it found a sweet spot of expressiveness, that you could really write things in a pretty
*  natural way, and efficiency, which was particularly important when computers were
*  not nearly as powerful as they are today. You've got to put yourself back 50 years,
*  almost in terms of what computers could do. And that's roughly four or five generations,
*  decades of Moore's law. So expressiveness and efficiency and, I don't know, perhaps the
*  environment that it came with as well, which was Unix. So it meant if you wrote a program,
*  it could be used on all those computers that ran Unix. And that was all of those computers,
*  because they were all written in C. And that was Unix, the operating system itself was portable,
*  as were all the tools. So it all worked together, again, in one of these things where
*  things fed on each other in a positive cycle. What did it take to write sort of a definitive
*  book, probably definitive a book on all of programs? It's more definitive to a particular
*  language than any other book on any other language. And did two really powerful things, which is
*  popularized the language, at least from my perspective, maybe you can correct me. And
*  second is created a standard of how this language is supposed to be used and applied. So what did
*  it take? Did you have those kinds of ambitions in mind when working on that?
*  Is this some kind of joke? No, of course not.
*  It's an accident of timing skill and just luck.
*  A lot of it is, clearly timing was good. Now, Dennis and I wrote the book in 1977.
*  Dennis Ritchie.
*  Yeah, right. And at that point, Unix was starting to spread. I don't know how many there were,
*  but it would be dozens to hundreds of Unix systems. And C was also available on other
*  kinds of computers that had nothing to do with Unix. And so the language had some potential.
*  And there were no other books on C. And Bell Labs was really the only source for it. And Dennis,
*  of course, was authoritative because it was his language. And he had written the reference manual,
*  which is a marvelous example of how to write a reference manual. Really, really very, very
*  well done. So I twisted his arm until he agreed to write a book and then we wrote a book.
*  And the virtue or advantage, at least, I guess, of going first is that then other people have to
*  follow you if they're going to do anything. And I think it worked well because Dennis was a
*  superb writer. I mean, he really, really did. And the reference manual in that book is his, period.
*  I had nothing to do with that at all. So just crystal clear prose and very, very well expressed.
*  And then he and I, I wrote most of the expository material. And then he and I sort of did the usual
*  ping-ponging back and forth, refining it. But I spent a lot of time trying to find examples that
*  would sort of hang together and that would tell people what they might need to know at about the
*  right time that they should be thinking about needing it. And I'm not sure it completely
*  succeeded, but it mostly worked out fairly well. What do you think is the power of example? I mean,
*  you're the creator, at least one of the first people to do the Hello World program,
*  which is like the example. If aliens discover our civilization hundreds of years from now,
*  it'll probably be Hello World programs, just like a half-broken robot communicating with them with
*  the Hello World. And that's a representative example. So what do you find powerful about examples?
*  I think a good example will tell you how to do something and it will be representative of,
*  you might not want to do exactly that, but you will want to do something that's at least in that
*  same general vein. And so a lot of the examples in the C book were picked for these very, very
*  simple straightforward text processing problems that were typical of Unix. I want to read input
*  and write it out again. There's a copy command. I want to read input and do something to it
*  and write it out again. There's a grab. And so that kind of find things that are representative
*  of what people want to do and spell those out so that they can then take those and see the
*  core parts and modify them to their taste. And I think that a lot of programming books that I
*  don't look at programming books a tremendous amount these days, but when I do, a lot of them
*  don't do that. They don't give you examples that are both realistic and something you might want
*  to do. Some of them are pure syntax. Here's how you add three numbers. Well, come on, I could figure
*  that out. Tell me how I would get those three numbers into the computer and how we would do
*  something useful with them and then how I put them back out again, neatly formatted.
*  Especially if you follow that example, there is something magical of doing something that
*  feels useful. Yeah, right. And I think it's the attempt, it's absolutely not perfect,
*  but the attempt in all cases was to get something that was going to be either directly useful or
*  would be very representative of useful things that a programmer might want to do. But within that vein
*  of fundamentally text processing, reading text, doing something, writing text.
*  So you've also written a book on Go language. I have to admit, so I worked at Google for a while
*  and I've never used Go. You missed something. Well, I know I missed something for sure. So Go and
*  Rust are two languages that I hear spoken very highly of and I wish I would like to try. Well,
*  there's a lot of them. There's Julia, there's all these incredible modern languages. But if
*  you can comment before, well maybe comment on what do you find, where does Go sit in this broad
*  spectrum of languages? And also how do you yourself feel about this wide range of powerful,
*  interesting languages that you may never even get to try to explore because of time?
*  So I think, so Go first comes from that same Bell Labs tradition in part, not exclusively,
*  but two of the three creators, Ken Thompson and Rob Pike.
*  So literally the people.
*  Yeah, the people. And then with this very, very useful influence from the European school,
*  in particular the Claude Spier influence through Robert Griezmer, who was I guess a second
*  generation down student at ETH. And so that's an interesting combination of things. And so some ways
*  Go captures the good parts of C. It looks sort of like C. It's sometimes characterized as C for
*  the 21st century. On the surface it looks very, very much like C. But at the same time it has some
*  interesting data structuring capabilities. And then I think the part that I would say is
*  particularly useful, and again, I'm not a Go expert, in spite of co-authoring the book,
*  about 90% of the work was done by Alan Donovan, my co-author, who is a Go expert.
*  But Go provides a very nice model of concurrency. It's basically the cooperating,
*  communicating sequential processes that Tony Hoare set forth, geez, I don't know, 40 plus years ago.
*  And Go routines are, to my mind, a very natural way to talk about parallel computation. And in the
*  few experiments I've done with them, they're easy to write and typically it's going to work,
*  and very efficient as well. So I think that's one place where Go stands out, that that model
*  of parallel computation is very, very easy and nice to work with.
*  Just a comment on that. Do you think C foresaw, or the early Unix days foresaw,
*  threads and massively parallel computation?
*  I would guess not really. I mean, maybe it was seen, but not at the level where it was something
*  you had to do anything about. For a long time, processors got faster, and then processors stopped
*  getting faster because of things like power consumption and heat generation. And so what
*  happened instead was that instead of processors getting faster, there started to be more of them.
*  And that's where that parallel thread stuff comes in.
*  So if you can comment on all the other languages,
*  is it break your heart that you'll never get to explore them? Or how do you feel about the full
*  variety? It's not break my heart, but I would love to be able to try more of these languages.
*  The closest I've come is in a class that I often teach in the spring here. It's a programming class
*  and I often give, I have one sort of small example that I will write in as many languages
*  as I possibly can. I've got it in 20 odd languages at this point. And that's so I do a minimal
*  experiment with a language just to say, okay, I have this trivial task, which I understand the
*  task and it should, it takes 15 lines in OCK and not much more in a variety of other languages.
*  So how big is it? How fast does it run? And what pain did I go through to learn how to do it?
*  And that's like, it's like, it's very, very, very narrowly.
*  I like that term. So yeah, but still it's a little sample because you get to,
*  I think the hardest step of the programming language is probably the first step, right?
*  So there you're taking the first step.
*  Yeah. And so my experience with some languages is very positive, like Lua, a scripting language I
*  never used. And I took my little program. The program is a trivial formatter. It just takes
*  in lines of text of varying lengths and it puts them out in lines that have no more than 60
*  characters on each line. So think of it as just kind of the flow of process in a browser or
*  something. So it's very short program. And in Lua, I downloaded Lua and in an hour I had it working,
*  never having written Lua in my life, just going with online documentation. I did the same thing
*  in Scala, which you can think of as a flavor of Java, equally trivial. I did it in Haskell.
*  It took me several weeks, but it did run like a turtle. And I did it in Fortran,
*  90. And it was painful, but it worked. And I tried it in Rust and it took me several days to get it
*  working because the model of memory management was just a little unfamiliar to me. And the problem
*  I had with Rust, and it's back to what we were just talking about, I couldn't find good consistent
*  documentation on Rust. Now this was several years ago and I'm sure things have stabilized,
*  but at the time everything in the Rust world seemed to be changing rapidly. And so you would
*  find what looked like a working example and it wouldn't work with the version of the language
*  that I had. So it took longer than it should have. Rust is a language I would like to get back to,
*  but probably won't. I think one of the issues, you have to have something you want to do.
*  If you don't have something that is the right combination, if I want to do it and yet I have
*  enough disposable time, whatever, to make it worth learning a new language at the same time,
*  it's never going to happen. So what do you think about another language of JavaScript?
*  Well, let me just sort of comment on what I said. When I was brought up,
*  sort of JavaScript was seen as probably like the ugliest language possible. And yet it's quite
*  arguably, quite possibly taking over not just the front end, the backend of the internet,
*  but possibly in the future taking over everything because they've now learned to make it very
*  efficient. And so what do you think about this? Yeah, well, I think you captured it in a lot of
*  ways. When it first came out, JavaScript was deemed to be fairly irregular and an ugly language. And
*  certainly in the academy, if you said you were working on JavaScript, people would ridicule you.
*  It was just not fit for academics to work on. I think a lot of that has evolved. The language
*  itself has evolved and certainly the technology of compiling it is fantastically better than it
*  was. And so in that sense, it's absolutely a viable solution on backends as well as the frontends.
*  Used well, I think it's a pretty good language. I've written a modest amount of it and I've
*  played with JavaScript translators and things like that. I'm not a real expert and it's hard
*  to keep up even there with the new things that come along with it. So I don't know whether it
*  will ever take over the world. I think not, but it's certainly an important language and
*  worth knowing more about. There's maybe to get your comment on something, which JavaScript and
*  actually most languages, Python, such a big part of the experience of programming with those languages
*  includes libraries. So of using building on top of the code that other people have built.
*  I think that's probably different from the experience that we just talked about from Unix
*  and C-Days when you're building stuff from scratch. What do you think about this world of
*  essentially building up libraries on top of each other and leveraging them?
*  Yeah, that's a very perceptive kind of question. One of the reasons programming was fun in the old
*  days was that you were really building it all yourself. The number of libraries you had to
*  deal with was quite small. Maybe it was printf or the standard library or something like that.
*  That is not the case today. If you want to do something in, you mentioned Python and JavaScript
*  and those are the two fine examples, you have to typically download a boatload of other stuff and
*  you have no idea what you're getting. Absolutely nothing. I've been doing some playing with machine
*  learning over the last couple of days and gee, something doesn't work. Well, you pip install
*  this and down comes another gazillion megabytes of something and you have no idea what it was.
*  If you're lucky, it works. If it doesn't work, you have no recourse. There's absolutely no way
*  you could figure out which in these thousand different packages. I think it's worse in the
*  NPM environment for JavaScript. I think there's less discipline, less control there.
*  There's aspects of not just not understanding how it works, but there's security issues,
*  there's robustness issues. You don't want to run a nuclear power plant using JavaScript essentially.
*  Probably not. Speaking to the variety of languages, do you think that variety is good or do you
*  hope, think that over time we should converge towards one, two, three programming languages?
*  You mentioned to the Bell Lab days when people could sort of, the community of it and the more
*  languages you have, the more you separate the communities. There's the Ruby community,
*  there's the Python community, there's C++ community. Do you hope that they'll unite
*  one day to just one or two languages? I certainly don't hope it. I'm not sure that that's right
*  because I honestly don't think there is one language that will suffice for all the programming
*  needs of the world. Are there too many at this point? Well, arguably, but I think if you look at
*  the distribution of how they are used, there's something called a dozen languages that probably
*  account for 95% of all programming at this point and that doesn't seem unreasonable.
*  Then there's another, well, 2000 languages that are still in use that nobody uses
*  and or at least don't use in any quantity. I think new languages are a good idea in many respects
*  because they're often a chance to explore an idea of how a language might help. I think that's one
*  of the positive things about functional languages. For example, they're a particularly good place
*  where people have explored ideas that at the time didn't seem feasible, but ultimately have wound up
*  as part of mainstream languages as well. I mean, just go back as early as recursion and Lisp and
*  follow forward functions as first class citizens and pattern-based languages and
*  gee, I don't know, closures and just on and on and on. LAMBDAs, interesting ideas that showed up first
*  in let's call it broadly the functional programming community and then find their way into mainstream
*  languages. Yeah, it's a playground for rebels. Yeah, exactly. And so I think the languages in
*  the playground themselves are probably not going to be the mainstream, at least for some while,
*  but the ideas that come from there are invaluable. So let's go to something that when I found out
*  recently, so I've known you've done a million things, but one of the things I wasn't aware of
*  that you had a role in Ample and before you interrupt me by minimizing your role in it,
*  which you're- Ample is for minimizing functions.
*  Yeah, minimizing functions, right, exactly. Can I just say that the elegance and abstraction power
*  of Ample is incredible? When I first came to it about 10 years ago or so, can you describe what
*  is the Ample language? Sure. So Ample is a language for mathematical programming, technical term,
*  think of it as linear programming, that is setting up systems of linear equations that are
*  some sort of system of constraints so that you have a bunch of things that have to be less than
*  this, greater than that, whatever, and you're trying to find a set of values for some decision
*  variables that will maximize or minimize some objective function. So it's a way of solving a
*  particular kind of optimization problem, a very formal sort of optimization problem,
*  but one that's exceptionally useful. And it specifies, so there's objective
*  function constraints and variables that become separate from the data it operates on.
*  Right. So that kind of separation allows you to
*  put on different hats. One put the hat of an optimization person and then put another hat
*  of a data person and dance back and forth and also separate the actual solvers, the optimization
*  systems that do the solving, that you can have other people come to the table and then build
*  their solvers, whether it's linear or nonlinear, convex, non-convex, that kind of stuff. So
*  what is the, do you as, maybe you can comment how you got into that world and
*  what is the beautiful or interesting idea to you from the world of optimization?
*  Sure. So I preface it by saying I'm absolutely not an expert on this and most of the important
*  work in Ample comes from my two partners in crime on that, Bob Forer, who was a professor of,
*  in the industrial engineering and management science department at Northwestern,
*  and my colleague at Bell Labs, Dave Gay, who was numerical analyst and optimization person.
*  So the deal is linear programming. Preface this by saying-
*  Let's stay with linear programming.
*  Yeah. Linear programming is the simplest example of this. So linear programming as it's taught
*  in school is that you have a big matrix, which is always called A, and you say AX is less than
*  or equal to B. So B is a set of constraints, X is the decision variables, and A is how the decision
*  variables are combined to set up the various constraints. So A is a matrix and X and B are
*  vectors. And then there's an objective function, which is just the sum of a bunch of Xs and some
*  coefficients on them. And that's the thing you want to optimize. The problem is that in the real
*  world, that matrix A is a very, very, very intricate, very large and very sparse matrix
*  where the various components of the model are distributed among the coefficients in a way that
*  is totally unobvious to anybody. And so what you need is some way to express the original model,
*  which you and I would write, we'd write mathematics on the board, the sum of this is greater than the
*  sum of that kind of thing. So you need a language to write those kinds of constraints. And Bob
*  Forer for a long time had been interested in modeling languages, languages that made it
*  possible to do this. There was a modeling language around called GAMS, the General Algebraic Modeling
*  System, but it looked very much like FORTRAN, it was kind of clunky. And so Bob spent a sabbatical
*  year at Bell Labs in 1984. And he and, there's something in the office across from me and
*  it's always geography. And he and Dave Gay and I started talking about this kind of thing. And
*  he wanted to design a language that would make it so that you could take these algebraic
*  specifications, you know, summation signs over sets, and that you would write on the board and
*  convert them into basically this A matrix. And then pass that off to a solver, which is an
*  entirely separate thing. And so we talked about the design of the language. I don't remember any of
*  the details of this now, but it's kind of an obvious thing. You're just writing out mathematical
*  expressions in a FORTRAN like, or sorry, an algebraic, but textual like language. And I wrote
*  the first version of this AMPLE program, my first C++ program. And-
*  That's written in C++?
*  Yeah. And so I did that fairly quickly. We wrote, it was 3000 lines or something, so it wasn't very
*  big, but it sort of showed the feasibility of it that you could actually do something that was easy
*  for people to specify models and convert it into something that a solver could work with. At the
*  same time, as you say, the model and the data are separate things. So one model would then work with
*  all kinds of different data in the same way that lots of programs do the same thing, but with
*  different data.
*  So one of the really nice things is the specification of the models, human, just kind of like, as you say,
*  it's human readable. Like I literally, I remember on stuff I worked, I would send it to colleagues
*  that I'm pretty sure never programmed in their life, just to understand what the optimization
*  problem is. I think, how hard is it to convert that? You said there's a first prototype in C++,
*  to convert that into something that could actually be used by the solver.
*  It's not too bad because most of the solvers have some mechanism that lets them import a model in a
*  form. It might be as simple as the matrix itself in just some representation, or if you're doing
*  things that are not linear programming, then there may be some mechanism that lets you provide things
*  like functions to be called or other constraints on the model. So all Ample does is to generate
*  that kind of thing, and then solver deals with all the hard work. And then when the solver comes back
*  with numbers, Ample converts those back into your original form, so you know how much of each thing
*  you should be buying or making or shipping or whatever. So we did that in 84, and I haven't had
*  a lot to do with it since, except that we wrote a couple of versions of a book on it.
*  Which is one of the greatest books I've ever written. I love that book. I don't know why.
*  It's an excellent book. Bob Forer wrote most of it, and so it's really, really well done. He must
*  be a dynamite teacher. And typeset in LaTeX.
*  No, no, no. Are you kidding? I remember liking the typography, so I don't know.
*  We did it with T-Rof. I don't even know what that is.
*  Yeah, exactly. You're too young. Think of T-Rof as a predecessor to the tech family of things. It's
*  a formatter that was done at Bell Labs in this same period of the very early 70s that predates
*  tech and things like that by five to ten years. But it was nevertheless, I'm going by memories.
*  It was a memory of being beautiful. Yeah, it was nicely done.
*  Outside of Unix, C, Awe, Golang, all the things we talked about,
*  all the amazing work you've done, you've also done work in graph theory.
*  Let me ask this crazy out there question. If you had to make a bet, and I had to force you
*  to make a bet, do you think P equals NP? The answer is no, although I'm told that somebody
*  asked Jeff Dean if that was the key, under what conditions P would equal NP, and he said either
*  P is zero or N is one. Or vice versa, I've forgotten. This is why Jeff Dean is a lot smarter than I am.
*  Yeah. But your intuition is?
*  I have no intuition, but I've got a lot of colleagues who've got intuition and their betting is no.
*  That's the popular bet. Okay, so what is computational complexity theory?
*  And do you think these kinds of complexity classes, especially as you've taught in this
*  modern world, are still useful way to understand the hardness of problems?
*  I don't do that stuff. The last time I touched anything to do with that-
*  Many, many years ago.
*  ... was before it was invented. It's literally true. I did my PhD thesis on-
*  Before Big O notation.
*  Absolutely. I did this in 1968, and I worked on graph partitioning, which is this question.
*  You've got a graph that is a nodes and edges kind of graph, and the edges have weights,
*  and you just want to divide the nodes into two piles of equal size so that the number of edges
*  that goes from one side to the other is as small as possible.
*  You developed, so that problem is hard.
*  Well, as it turns out, I worked with Shen Lin at Bell Labs on this, and we were never able to
*  come up with anything that was guaranteed to give the right answer. We came up with heuristics that
*  worked pretty darn well, and I peeled off some special cases for my thesis, but it was just hard.
*  And that was just about the time that Steve Cook was showing that there were classes of problems
*  that appeared to be really hard, of which graph partitioning was one. But my expertise, such as it
*  was, totally predates that development. Oh, interesting. So the heuristic, which now
*  carries the two of your names for the traveling salesman problem and for the graph partitioning,
*  that was like how did you, you weren't even thinking in terms of classes. You were just trying to-
*  There was no such idea.
*  A heuristic that kind of does the job pretty well.
*  You were trying to find something that did the job, and there was nothing that you would call,
*  let's say, a closed form or algorithmic thing that would give you a guaranteed right answer.
*  I mean, compare graph partitioning to max flow min cut or something like that. That's the same
*  problem, except there's no constraint on the number of nodes on one side or the other of the cut.
*  And that means it's an easy problem, at least as I understand it. Whereas the constraint that says
*  the two have to be constrained in size makes it a hard problem.
*  Yeah. So the Robert Frost says that poem where you have to choose two paths. So why did you,
*  is there another alternate universe in which you pursued the Don Knuth path of algorithm design?
*  Sort of-
*  Not smart enough.
*  Not smart enough. You're infinitely modest, but so you pursued your kind of love of programming.
*  I mean, when you look back to those, I mean, just looking into that world, does that just seem like
*  a distant world of theoretical computer science? Then is it fundamentally different from the world
*  of programming?
*  I don't know. I mean, certainly in all seriousness, I just didn't have the talent for it. When I got
*  here as a grad student to Princeton and I started to think about research at the end of my first
*  year or something like that, I worked briefly with John Hopcroft, who was absolutely,
*  you mentioned during award winner, et cetera, a great guy. And it became crystal clear I was
*  not cut out for this stuff, period. Okay. And so I moved into things where I was more cut out for it
*  and that tended to be things like writing programs and then ultimately writing books.
*  You said that in Toronto as an undergrad, you did a senior thesis or a literature survey
*  on artificial intelligence. This was 1964.
*  Correct.
*  What was the AI landscape, ideas, dreams at that time?
*  I think that was one of the, well, you've heard of AI winters. This is whatever the opposite was,
*  AI summer or something. It was one of these things where people thought that, boy, we could do
*  anything with computers, that all these hard problems, computers will solve them. They will
*  do machine translation. They will play games like chess. They will do proof theorems in geometry.
*  There were all kinds of examples like that where people thought, boy, we could really do those
*  sorts of things. And I read the Kool-Aid in some sense. I still have this wonderful collection of
*  papers called Computers and Thought that was published about that era and people were very
*  optimistic. And then of course it turned out that what people had thought was just a few years
*  down the pike was more than a few years down the pike. And some parts of that are more or less now
*  sort of under control. We finally do play games like Go and chess and so on better than people do,
*  but there are others. Machine translation is a lot better than it used to be, but that's
*  50, close to 60 years of progress and a lot of evolution in hardware and a tremendous amount
*  more data upon which you can build systems that actually can learn from some of that.
*  The infrastructure to support developers working together like an open source movement,
*  the internet period is also empowering. But what lesson do you draw from that,
*  the opposite of winter, that optimism?
*  Well, I guess the lesson is that in the short run it's pretty easy to be too pessimistic or
*  maybe too optimistic and in the long run you probably shouldn't be too pessimistic. I'm not
*  saying that very well. It reminds me of this remark from Arthur Clarke, a science fiction author who
*  says when some distinguished but elderly person says that something is possible, he's probably
*  right. And if he says it's impossible, he's almost surely wrong. But you don't know what
*  the time scale is. The time scale is critical, right? So what are your thoughts on this new
*  summer of AI now in the work with machine learning in neural networks? You've kind of mentioned that
*  you started to try to explore and look into this world that seems fundamentally different from the
*  world of heuristics and algorithms like search, that it's now purely sort of trying to take huge
*  amounts of data and learn from that data, right? Programs from the data.
*  Yeah. Look, I think it's very interesting. I am incredibly far from an expert. Most of what I know
*  I've learned from my students and they're probably disappointed in how little I've learned from them.
*  But I think it has tremendous potential for certain kinds of things. Games is one where it
*  obviously has had an effect on some of the others as well. I think there's, and this is speaking from
*  definitely not expertise, I think there are serious problems in certain kinds of machine learning at
*  least because what they're learning from is the data that we give them. And if the data we give
*  them has something wrong with it, then what they learn from it is probably wrong too. And the
*  obvious thing is some kind of bias in the data. That the data has stuff in it like, I don't know,
*  women aren't as good as men at something, okay? That's just flat wrong. But if it's in the data
*  because of historical treatment, then that machine learning stuff will propagate that.
*  And that is a serious worry. The positive part of that is what machine learning
*  does is reveal the bias in the data and puts a mirror to our own society. And in so doing helps
*  us remove the bias, helps us work on ourselves, puts a mirror to ourselves. Yeah. That's an
*  optimistic point of view. And if it works that way, that would be absolutely great. And what I
*  don't know is whether it does work that way or whether the AI mechanisms or machine learning
*  mechanisms reinforce and amplify things that have been wrong in the past. And I don't know,
*  but I think that's a serious thing that we have to be concerned about.
*  Let me ask you an out there question, okay? I know nobody knows, but what do you think it takes to
*  build a system of human level intelligence? That's been the dream from the sixties.
*  We talk about games, about language, about image recognition, but really the dream is to create
*  human level or superhuman level intelligence. What do you think it takes to do that? And are we close?
*  I haven't a clue and I don't know, roughly speaking. I mean, this was trying to trick
*  you into a hypothesis. Yeah. I mean, Turing talked about this in his paper on machine
*  intelligence back in, geez, I don't know, early fifties or something like that. And he had the
*  idea of the Turing test and I don't know whether the Turing test is a good test of intelligence.
*  I don't know. It's an interesting test. At least it's in some vague sense objective,
*  whether you can read anything into the conclusions is a different story.
*  Do you have worries, concerns, excitement about the future of artificial intelligence? So there's
*  a lot of people who are worried and you can speak broadly than just artificial intelligence. It's
*  basically computing taking over the world in various forms. Are you excited by this future,
*  this possibility of computing being everywhere or are you worried?
*  It's some combination of those. I think almost all technologies over the long run are for good,
*  but there's plenty of examples where they haven't been good either over a long run for some people
*  or over a short run. And computing is one of those and AI within it is going to be one of
*  those as well, but computing broadly. I mean, for just a today example is privacy, that the use of
*  things like social media and so on means that, and the commercial surveillance means that there's an
*  enormous amount more known about us by people, other businesses, government, whatever, than perhaps
*  one ought to feel comfortable with. So that's an example.
*  So that's an example of a possible negative effect of computing being everywhere. It's an
*  interesting one because it could also be a positive if leveraged correctly.
*  There's a big if there.
*  So I have a deep interest in human psychology and humans seem to be very paranoid about this data
*  thing. But that varies depending on age group. It seems like the younger folks, so it's exciting
*  to me to see what society looks like 50 years from now that the concerns about privacy might
*  be flipped on their head based purely in human psychology versus actual concerns or not.
*  What do you think about Moore's law? You said a lot of stuff we've talked about with programming
*  languages in their design and their ideas are come from the constraints in the systems they
*  operate. And do you think Moore's law, the exponential improvement of systems will continue
*  indefinitely? There's a mix of opinions on that currently. Or do you think there'll be a plateau?
*  Well, the frivolous answer is no exponential can go on forever. You run out of something.
*  Just as we said, timescale matters. So if it goes on long enough, that might be all we need.
*  Yeah, right. It won't matter to us. So I don't know. We've seen places where Moore's law has
*  changed. For example, mentioned earlier, processors don't get faster anymore. But you use that same
*  growth of ability to put more things in a given area to grow them horizontally instead of vertically
*  as it were. So you can get more and more processors or memory or whatever on the same chip.
*  Is that going to run into a limitation? Presumably, because at some point you get down to the
*  individual atoms. And so you've got to find some way around that. Will we find some way around that?
*  I don't know. I just said that if I say it won't, I'll be wrong. Perhaps we will.
*  I just talked to Jim Keller and he says, he actually describes, he argues that the Moore's
*  law will continue for a long, long time because you mentioned the atom. We actually have,
*  I think, a thousand fold increase, decrease in transistors size still possible before we get to
*  the quantum level. So there's still a lot of possibilities. He thinks it'll continue and
*  definitely, which is an interesting, optimistic viewpoint. But how do you think
*  the programming languages will change with this increase? Whether we hit a wall or not,
*  do you think there'll be a fundamental change in the way programming languages are designed?
*  I don't know about that. I think what will happen is continuation of what we see in some areas,
*  at least, which is that more programming will be done by programs than by people and that more
*  will be done by sort of declarative rather than procedural mechanisms where I say,
*  I want this to happen. You figure out how. And that is in many cases at this point, domain of
*  specialized languages for narrow domains, but you can imagine that broadening out. And so I
*  don't have to say so much in so much detail, some collection of software, let's call it languages
*  or programs or something, will figure out how to do what I want to do.
*  Oh, interesting. So increased levels of abstraction.
*  Yeah.
*  And one day getting to the human level, we're going to just use natural language.
*  Could be possible.
*  So Utah still teach a course, Computers in Our World, here at Princeton, that introduces
*  computing and programming to non-majors. Just from that experience, what advice do you have for
*  people who don't know anything about programming but are kind of curious about this world or
*  programming seems to become more and more of a fundamental skill that people need to be at least
*  aware of? Yeah. Well, I can recommend a good book.
*  What's that?
*  The book I wrote for the course. I think this is one of these questions of should everybody know
*  how to program? And I think the answer is probably not, but I think everybody should at least
*  understand sort of what it is. So that if you say to somebody, I'm a programmer, they have a notion
*  of what that might be. Or if you say this is a program, or this was decided by a computer
*  running a program, that they have some vague intuitive understanding and accurate understanding
*  of what that might imply. So part of what I'm doing in this course, which is very definitely
*  for non-technical people, I mean, typical person in it is a history or English major,
*  try and explain how computers work, how they do their thing, what programming is, how you write
*  a program, and how computers talk to each other, and what do they do when they're talking to each
*  other. And then I would say nobody, very rarely, and does anybody in that course go on to become
*  a real serious programmer, but at least they've got a somewhat better idea of what all this stuff
*  is about, not just the programming, but the technology behind computers and communications.
*  Do they write a, do they try and write a program themselves?
*  Oh yeah, yeah, a very small amount. I introduced them to how machines work at a level below
*  high level languages, so we have a kind of a toy machine that has a very small repertoire,
*  a dozen instructions, and they write trivial assembly language programs for that.
*  Wow, that's interesting. So can you, just if you were to give a flavor to people of
*  the programming world, of the computing world, what are the examples they should go with? So a
*  little bit of assembly to get a sense at the lowest level of what the program is really doing?
*  Yeah, I mean in some sense there's no such thing as the lowest level because you can keep going
*  down, but that's the place where I drew the line. So the idea that computers have a fairly small
*  repertoire of very simple instructions that they can do, like add and subtract and branch and so
*  on, as you mentioned earlier, and that you can write code at that level and it will get things
*  done. And then you have the levels of abstraction that we get with higher level languages, like
*  Fortran or C or whatever, and that makes it easier to write the code and less dependent on
*  particular architectures. And then we talk about a lot of the different kinds of programs that
*  they use all the time that they don't probably realize are programs, like they're running
*  macOS on their computers or maybe Windows, and they're downloading apps on their phones,
*  and all of those things are programs that are just what we just talked about, except at a grand scale.
*  It's easy to forget that they're actual programs that people program. There's engineers that wrote
*  those things. Yeah, right. And so in a way, I'm expecting them to make an enormous conceptual
*  leap from their five or 10 line toy assembly language thing that adds two or three numbers
*  to something that is a browser on their phone or whatever, but it's really the same thing.
*  So if you look at the broad strokes of history,
*  how do you think the world changed because of computers? It's hard to sometimes see the
*  big picture when you're in it, but I guess I'm asking if there's something you've noticed over
*  the years that, like you mentioned, the students are more distracted looking at their, now there's
*  a device to look at. Right. Well, I think computing has changed a tremendous amount, obviously, but I
*  think one aspect of that is the way that people interact with each other, both locally and far
*  away. And when I was the age of those kids, making a phone call to somewhere was a big deal because
*  it costs serious money, and this was in the 60s, right? And today, people don't make phone calls,
*  they send texts or something like that. So there's an up and down in what people do.
*  People think nothing of having correspondence, regular meetings, video, whatever, with friends
*  or family or whatever in any other part of the world, and they don't think about that at all.
*  And so that's just the communication aspect of it. And-
*  Do you think that brings us closer together or does it take us away from the closeness of human
*  contact? I think it depends a lot on all kinds of things. So I trade mail with my brother and sister
*  in Canada much more often than I used to talk to them on the phone. So probably every two or three
*  days, I get something or send something to them. Whereas 20 years ago, I probably wouldn't have
*  talked to them on the phone nearly as much. So in that sense, that's brought my brother and sister
*  and I closer together. That's a good thing. I watch the kids on campus and they're mostly
*  walking around with their heads down, fooling with their phones to the point where I have to duck them.
*  I don't know that that has brought them closer together in some ways. There's sociological
*  research that says people are in fact not as close together as they used to be. I don't know
*  where that's really true, but I can see potential downsides and kids where you think, come on,
*  wake up and smell the coffee or whatever. That's right. But if you look at, again,
*  nobody can predict the future, but are you excited? Kind of touched this a little bit with AI, but
*  are you excited by the future in the next 10, 20 years that computing will bring? You were there
*  when there was no computers really, and now computers are everywhere, all over the world,
*  and Africa and Asia, and just every person, almost every person in the world has a device.
*  So are you hopeful, optimistic about that future?
*  It's mixed, if the truth be told. I think there are some things about that that are good. I think
*  there's the potential for people to improve their lives all over the place, and that's obviously
*  good. At the same time, at least in the short run, you can see lots and lots of bad as people
*  become more tribalistic or parochial in their interests, and there's an enormous amount more
*  us and them, and people are using computers in all kinds of ways to mislead or misrepresent or flat
*  out lie about what's going on, and that is affecting politics locally and I think everywhere in the
*  world. Yeah. The long-term effect on political systems and so on, it's
*  who knows. Who knows indeed.
*  The people now have a voice, which is a powerful thing. People who are oppressed have a voice,
*  but also everybody has a voice, and the chaos that emerges from that is fascinating to watch.
*  Yeah, it's kind of scary. If you can go back and relive a moment in your life,
*  one that made you truly happy outside of family, or was profoundly transformative,
*  is there a moment or moments that jump out at you from memory?
*  I don't think specific moments. I think there were lots and lots and lots of good times at Bell Labs
*  where you would build something and it worked. Jeez, it worked.
*  So the moment it worked.
*  Yeah, and somebody used it and they said, gee, that's neat. Those kinds of things
*  happened quite often in that sort of golden era in the 70s when Unix was young,
*  and there was all this low-hanging fruit and interesting things to work on. A group of people
*  who kind of, we were all together in this, and if you did something, they would try it out for you.
*  I think that was in some sense a really, really good time.
*  And Auk, was Auk an example of that?
*  Yeah, sure.
*  Then when you built it and people used it?
*  Yeah, absolutely.
*  And now millions of people use it.
*  And all your stupid mistakes are right there for them to look at, right? So it's mixed.
*  Yeah, it's terrifying and vulnerable, but it's beautiful because it does have a
*  positive impact on so, so many people. So I think there's no better way to end it. Brian,
*  thank you so much for talking to me. It was an honor.
*  Okay. My pleasure. Good fun.
*  Thank you for listening to this conversation with Brian Kernigan, and thank you to our sponsors,
*  8 Sleep Mattress and Raycon Earbuds. Please consider supporting this podcast by going to
*  8sleep.com slash Lex and to buy Raycon.com slash Lex. Click the links, buy the stuff.
*  These both are amazing products. It really is the best way to support this podcast and
*  the journey I'm on. It's how they know I sent you and increases the chance that they'll actually
*  support this podcast in the future. If you enjoy this thing, subscribe on YouTube,
*  review it with Firestars and Apple Podcasts, support it on Patreon or connect with me on
*  Twitter at Lex Friedman spelled somehow miraculously without the letter E, just F R I D M A N because
*  when we immigrated to this country, we were not so good at spelling. And now let me leave you with
*  some words from Brian Kernigan. Don't comment bad code. Rewrite it. Thank you for listening
*  and hope to see you next time.

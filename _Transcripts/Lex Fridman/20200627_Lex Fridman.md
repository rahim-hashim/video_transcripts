---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 6591s
Video Keywords: ['david patterson', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 148750
Video Rating: None
Video Description: David Patterson is a Turing award winner and professor of computer science at Berkeley. He is known for pioneering contributions to RISC processor architecture used by 99% of new chips today and for co-creating RAID storage. The impact that these two lines of research and development have had on our world is immeasurable. He is also one of the great educators of computer science in the world. His book with John Hennessy "Computer Architecture: A Quantitative Approach" is how I first learned about and was humbled by the inner workings of machines at the lowest level.

Support this podcast by signing up with these sponsors:
- Jordan Harbinger Show: https://jordanharbinger.com/lex/
- Cash App - use code "LexPodcast" and download:
- Cash App (App Store): https://apple.co/2sPrUHe
- Cash App (Google Play): https://bit.ly/2MlvP5w

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
3:28 - How have computers changed?
4:22 - What's inside a computer?
10:02 - Layers of abstraction
13:05 - RISC vs CISC computer architectures
28:18 - Designing a good instruction set is an art
31:46 - Measures of performance
36:02 - RISC instruction set
39:39 - RISC-V open standard instruction set architecture
51:12 - Why do ARM implementations vary?
52:57 - Simple is beautiful in instruction set design
58:09 - How machine learning changed computers
1:08:18 - Machine learning benchmarks
1:16:30 - Quantum computing
1:19:41 - Moore's law
1:28:22 - RAID data storage
1:36:53 - Teaching
1:40:59 - Wrestling
1:45:26 - Meaning of life

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# David Patterson Computer Architecture and Data Storage  Lex Fridman Podcast #104
**Lex Fridman:** [June 27, 2020](https://www.youtube.com/watch?v=naed4C4hfAg)
*  The following is a conversation with David Patterson,
*  Touring Award winner and professor of computer science at Berkeley.
*  He's known for pioneering contributions to risk processor architecture used by 99% of new chips today,
*  and for co-creating RAID storage.
*  The impact that these two lines of research and development have had in our world is immeasurable.
*  He's also one of the great educators of computer science in the world.
*  His book with John Hennessy is how I first learned about and was humbled by the inner workings of machines at the lowest level.
*  Quick summary of the ads.
*  Two sponsors, the Jordan Harbinger Show and Cash App.
*  Please consider supporting the podcast by going to JordanHarbinger.com slash Lex and downloading Cash App and using code LexPodcast.
*  Click on the links. Buy the stuff.
*  It's the best way to support this podcast and in general, the journey I'm on in my research and startup.
*  This is the Artificial Intelligence Podcast.
*  If you enjoy it, subscribe on YouTube, review it, the five stars on Apple Podcast,
*  support it on Patreon or connect with me on Twitter at Lex Friedman, spelled without the E, just F-R-I-D-M-A-N.
*  As usual, I'll do a few minutes of ads now and never any ads in the middle that can break the flow of the conversation.
*  This episode is supported by the Jordan Harbinger Show.
*  Go to JordanHarbinger.com slash Lex.
*  It's how he knows I sent you.
*  On that page, there's links to subscribe to it on Apple Podcasts, Spotify and everywhere else.
*  I've been binging on this podcast.
*  It's amazing. Jordan is a great human being.
*  He gets the best out of his guests, dives deep, calls them out when it's needed and makes the whole thing fun to listen to.
*  He's interviewed Kobe Bryant, Mark Cuban, Yelda Gras Tyson, Garry Kasparov and many more.
*  I recently listened to his conversation with Frank Abagnale, author of Catch Me If You Can,
*  and one of the world's most famous con men.
*  Perfect podcast length and topic for a recent long distance run that I did.
*  Again, go to JordanHarbinger.com slash Lex.
*  Thanks for giving my love and to support this podcast.
*  Subscribe also on Apple Podcasts, Spotify and everywhere else.
*  This show is presented by Cash App, the greatest sponsor of this podcast ever and the number one finance app in the App Store.
*  When you get it, use code LexPodcast.
*  Cash App lets you send money to friends, buy Bitcoin and invest in the stock market with as little as one dollar.
*  When Cash App allows you to buy Bitcoin, let me mention that cryptocurrency in the context of the history of money is fascinating.
*  I recommend The Scent of Money as a great book on this history.
*  Also, the audiobook is amazing.
*  Debits and credits on Ledger started around 30,000 years ago.
*  The US dollar created over 200 years ago and the first decentralized cryptocurrency released just over 10 years ago.
*  So given that history, cryptocurrency is still very much in its early days of development,
*  but it's still aiming to and just might redefine the nature of money.
*  So again, if you get Cash App from the App Store, Google Play and use the code LexPodcast, you get $10.
*  And Cash App will also donate $10 to FIRST, an organization that is helping to advance robotics system education for young people around the world.
*  And now here's my conversation with David Patterson.
*  Let's start with the big historical question.
*  How have computers changed in the past 50 years at both the fundamental architectural level and in general in your eyes?
*  Well, the biggest thing that happened was the invention of the microprocessor.
*  So computers that used to fill up several rooms could fit inside your cell phone.
*  And not only did they get smaller, they got a lot faster.
*  So they're a million times faster than they were 50 years ago.
*  And they're much cheaper and they're ubiquitous.
*  You know, there's 7.8 billion people on this planet.
*  Probably half of them have cell phones right now, which is remarkable.
*  There's probably more microprocessors than there are people.
*  Sure. I don't know what the ratio is, but I'm sure it's above one.
*  Maybe it's 10 to one or some number like that.
*  What is a microprocessor?
*  So a way to say what a microprocessor is, is to tell you what's inside a computer.
*  So a computer forever has classically had five pieces.
*  There's input and output, which kind of naturally, as you'd expect, is input is like speech or typing and output is displays.
*  There's a memory and like the name sounds, it remembers things.
*  So it's integrated circuits whose job is you put information in and when you ask for it, it comes back out.
*  That's memory. And the third part is the processor, where the microprocessor comes from.
*  And that has two pieces as well.
*  And that is the control, which is kind of the brain of the processor and the what's called the arithmetic unit.
*  It's kind of the brawn of the computer.
*  So if you think of the as a human body, the arithmetic unit, the thing that does the number crunching is the is the body and the control is the brain.
*  So those five pieces, input, output, memory, arithmetic unit and control are have been in computers since the very dawn.
*  And the last two are considered the processor.
*  So a microprocessor simply means a processor that fits on a microchip.
*  And that was invented about, you know, 40 years ago, was the first microprocessor.
*  It's interesting that you refer to the arithmetic unit as the like you connected to the body and the controllers of the brain.
*  So I guess I never thought of it that way.
*  It's a nice way to think of it, because most of the actions the microprocessor does in terms of literally sort of computation with the microprocessor does computation,
*  it process information.
*  And most of the thing it does is basic arithmetic operations.
*  What are the operations, by the way?
*  It's a lot like a calculator.
*  So there are add instructions, subtract instructions, multiply and divide.
*  And kind of the brilliance of the invention of the of the of the computer or the processor is that it performs very trivial operations,
*  but it just performs billions of them per second.
*  And what we're capable of doing is writing software that can take these very trivial instructions and have them create tasks that can do things better than human beings can do today.
*  Just looking back through your career, did you anticipate the kind of how good we would be able to get at doing these small basic operations?
*  How many surprises along the way were you just kind of set back and said, wow, I didn't expect it to go this fast, this good?
*  Well, the fundamental driving force is what's called Moore's Law, which was named after Gordon Moore, who's a Berkeley alumnus.
*  And he made this observation very early in what are called semiconductors.
*  And semiconductors are these ideas.
*  You can build these very simple switches and you can put them on these microchips.
*  And he made this observation over 50 years ago.
*  He looked at a few years and said, I think what's going to happen is the number of these little switches called transistors is going to double every year for the next decade.
*  And he said this in 1965.
*  And in 1975, he said, well, maybe it's going to double every two years.
*  And that what other people since named that Moore's Law guided the industry.
*  And when Gordon Moore made that prediction, he wrote a paper back in, I think, in the 70s and said, not only is this going to happen, he wrote, what would be the implications of that?
*  And in this article from 1965, he shows ideas like computers being in cars and computers being in something that you would buy in the grocery store and stuff like that.
*  So he kind of not only called his shot, he called the implications of it.
*  So if you were in the computing field and if you believed Moore's prediction, he kind of said what would be happening in the future.
*  So it's not kind of it's at once since this is what was predicted and you could imagine it was easy to believe that Moore's Law was going to continue.
*  And so this would be the implications.
*  On the other side, there are these shocking events in your life.
*  Like I remember driving in Marin across the bay in San Francisco and seeing a bulletin board at a local civic center and it had a URL on it.
*  And it was like for the people at the time, these first URLs and that's the, you know, WWW select stuff with the HDP.
*  People thought it looked like alien writing, right?
*  You'd see these advertisements and commercials or bulletin boards that had this alien writing on it.
*  So for the laypeople, it's like, what the hell is going on here?
*  And for those people in industry, it's oh my God, this stuff is getting so popular, it's actually leaking out of our nerdy world into the real world.
*  So that I mean, there was events like that.
*  I think another one was I remember with the early days of the personal computer when we started seeing advertisements in magazines for personal computers, like it's so popular that it made the newspaper.
*  So at one hand, you know, Gordon Moore predicted it and you kind of expected it to happen.
*  But when it really hit and you saw it affecting society, it was it was shocking.
*  So maybe taking a step back and looking both the engineering and philosophical perspective, what what do you see as the layers of abstraction in the computer?
*  Do you see a computer as a set of layers of abstractions?
*  Yeah, I think that's one of the things that computer science fundamentals is these things are really complicated in the way we cope with complicated software and complicated hardware is these layers of abstraction.
*  And that simply means that we, you know, suspend disbelief and pretend that the only thing you know is that layer and you don't know anything about the layer below it.
*  And that's the way we can make very complicated things.
*  And probably it started with hardware.
*  That's the way it was done.
*  But it's been proven extremely useful.
*  And, you know, I would say in a modern computer today, there might be 10 or 20 layers of abstraction.
*  And they're all trying to kind of enforce this contract is all you know is this interface.
*  There's a set of commands that you can are allowed to use and you stick to those commands that we will faithfully execute that.
*  And it's like peeling the layers of a London onion.
*  You get down. There's a new set of layers and so forth.
*  So for people who want to study computer science, the exciting part about it is you can keep peeling those layers.
*  You take your first course and you might learn to program in Python and then you can take a follow on course and you can get it down to a lower level language like C.
*  And you can go and if you want to, you can start getting into the hardware layers and you keep getting down all the way to that transistor that I talked about that Gordon Moore predicted.
*  And you can understand all those layers all the way up to the highest level application software.
*  So it's a very kind of magnetic field.
*  If you're interested, you can go into any depth and keep going.
*  In particular, what's happening right now or it's happened in software last 20 years recently in hardware, there's going to be open source versions of all of these things.
*  So what open source means is what the engineer, the programmer designs.
*  It's not secret, the belonging to a company.
*  It's out there on the worldwide web so you can see it.
*  So you can look at for lots of pieces of software that you use.
*  You can see exactly what the programmer does if you want to get involved.
*  That used to stop at the hardware recently has been an effort to make open source hardware and those interfaces open so you can see that.
*  So instead of before you had to stop at the hardware, you can now start going layer by layer below that and see what's inside there.
*  So it's a remarkable time that for the interested individual can really see in great depth what's really going on in the computers that power everything that we see around us.
*  Are you thinking also when you say open source at the hardware level, is this going to the design architecture instruction set level or is it going to literally the manufacturer of the actual hardware,
*  of the actual chips, whether that's ASICs specialized to a particular domain or the general?
*  Yeah, so let's talk about that a little bit.
*  So when you get down to the bottom layer of software, the way software talks to hardware is in a vocabulary.
*  And what we call that vocabulary, we call that the words of that vocabulary called instructions in the technical term for the vocabulary is instruction set.
*  So those instructions are like we talked about earlier, there can be instructions like add, subtract and multiply divide.
*  There's instructions to put data into memory, which is called a store instruction and to get data back, which is called the load instructions.
*  And those simple instructions go back to the very dawn of computing.
*  And in 1950, the commercial computer had these instructions.
*  So that's the instruction set that we're talking about.
*  So up until I'd say 10 years ago, these instruction sets were all proprietary.
*  So a very popular one is owned by Intel, the one that's in the cloud and in all the PCs in the world.
*  Intel owns that instruction set.
*  It's referred to as the x86.
*  There have been a sequence of ones that the first number was called 8086.
*  And since then, there's been a lot of numbers, but they all end in 86.
*  So there's been that kind of family of instruction sets.
*  And that's proprietary.
*  And that's proprietary.
*  The other one that's very popular is from ARM that kind of powers all the cell phones in the world, all the iPads in the world,
*  and a lot of things that are so-called Internet of Things devices.
*  ARM and that one is also proprietary.
*  ARM will license it to people for a fee, but they own that.
*  So the new idea that got started at Berkeley kind of unintentionally 10 years ago is early in my career,
*  we pioneered a way to do these vocabularies instruction sets that was very controversial at the time.
*  At the time, in the 1980s, conventional wisdom was these vocabularies instruction sets should have powerful instructions,
*  so polysyllabic kind of words, you can think of that.
*  And so instead of just add, subtract, and multiply, they would have polynomial, divide, or sort a list.
*  And the hope was of those powerful vocabularies that make it easier for software.
*  So we thought that didn't make sense for microprocessors.
*  There was people at Berkeley and Stanford and IBM who argued the opposite.
*  And we called that was a reduced instruction set computer.
*  And the abbreviation was RISC and typical for computer people, we use the abbreviation start pronouncing it.
*  So risk was the thing.
*  So we said for microprocessors, which with Gordon's Moore is changing really fast,
*  we think it's better to have a pretty simple set of instructions, reduced set of instructions.
*  That that would be a better way to build microprocessors since they're going to be changing so fast due to Moore's law.
*  And then we'll just use standard software to generate more of those simple instructions.
*  And one of the pieces of software that's in that software stack going between these layers of abstractions is called a compiler.
*  And it's basically translates. It's a translator between levels.
*  We said the translator will handle that.
*  So the technical question was, well, since there are these reduced instructions, you have to execute more of them.
*  Yeah, that's right. But maybe you can execute them faster. Yeah, that's right.
*  They're simpler, so they go faster, but you have to do more of them.
*  So what's what's that trade off look like?
*  And it ended up that we ended up executing maybe 50 percent more instructions, maybe a third more instructions, but they ran four times faster.
*  So so this risk, controversial risk ideas proved to be maybe factors of three or four better.
*  I love that this idea was controversial and almost kind of like rebellious.
*  So that's in the context of what was more conventional is the complex instructional set computing.
*  So how would you pronounce that? CISC. CISC versus risk versus CISC.
*  And and believe it or not, this sounds very, very, you know, who cares about this?
*  Right. It was it was violently debated at several conferences.
*  It's like, what's the right way to go?
*  Is is and people thought risk was, you know, was a de-evolution.
*  We're going to make software worse by making those instructions simpler and fierce debates at several conferences in the 1980s.
*  And then later in the 80s, it kind of settled to these benefits.
*  It's not completely intuitive to me why risk has for the most part won.
*  Yeah. So why did that happen?
*  Yeah, yeah. And maybe I can sort of say a bunch of dumb things that could lay the land for further commentary.
*  So to me, this is this is kind of interesting thing.
*  If you look at C++ versus C with modern compilers, you really could write faster code with C++.
*  So relying on the compiler to reduce your complicated code into something simple and fast.
*  So to me, comparing risk, maybe this is a dumb question, but why is it that focusing the definition,
*  the design of the instruction set on very few simple instructions in the long run provide faster execution versus coming up with,
*  like you said, a ton of complicated instructions that over time, you know, years, maybe decades,
*  you come up with compilers that can reduce those into simple instructions for you.
*  Yes. Let's try and split that into two pieces.
*  So if the compiler can do that for you, if the compiler can take a complicated program and produce simpler instructions,
*  then the programmer doesn't care, right?
*  Programmer, I don't care just how fast is the computer I'm using, how much does it cost.
*  And so what happened kind of in the software industry is right around before the 1980s,
*  critical pieces of software were still written not in languages like C or C++.
*  They were written in what's called assembly language, where there's this kind of humans writing exactly at the instructions at the level that a computer can understand.
*  So they were writing add, subtract, multiply, you know, instructions.
*  It's very tedious.
*  But the belief was to write this lowest level of software that that people use, which are called operating systems.
*  They had to be written in assembly language because these high level languages were just too inefficient.
*  They were too slow or the the programs would be too big.
*  So that changed with a famous operating system called Unix, which is kind of the the grandfather of all the operating systems today.
*  So Unix demonstrated that you could write something as complicated as an operating system in a language like C.
*  So once that was true, then that meant we could hide the instruction set from the programmer.
*  And so that meant then it didn't really matter.
*  The programmer didn't have to write lots of these simple instructions.
*  That was up to the compiler.
*  So that was part of our arguments for risk is if you were still writing assembly language, there's maybe a better case for SysConstructions.
*  But if the compiler can do that, it's going to be that's done once the computer translates it once.
*  And then every time you run the program, it runs at this this potentially simpler instructions.
*  And so that that was the debate, right, is because people would acknowledge that the simpler instructions could lead to a faster computer.
*  You can think of monosyllabic instructions. You could say them.
*  You know, if you think of reading, you probably read them faster or say them faster than long instructions.
*  The same thing. That analogy works pretty well for hardware.
*  And as long as you didn't have to read a lot more of those instructions, you could win.
*  So that's that's that's the basic idea for risk.
*  But it's interesting that in that discussion of Unix and C, that there's only one step of levels of abstraction from the code.
*  That's really the closest to the machine, to the code that's written by human.
*  It's at least to me, again, perhaps a dumb intuition, but it feels like there might have been more layers, sort of different kinds of humans stacked on top of each other.
*  So what's true and not true about what you said is.
*  Several of the layers of software.
*  Like so the if you hear two layers would be suppose we just talk about two layers, that would be the operating system like you get from from Microsoft or from Apple, like iOS or the Windows operating system.
*  And let's say applications that run on top of it, like Word or Excel.
*  So both the operating system could be written in C and the application could be written in C.
*  But you could construct those two layers and the applications absolutely do call upon the operating system.
*  And the change was that both of them could be written in higher level languages.
*  So it's one step of a translation, but you can still build many layers of abstraction of software on top of that.
*  And that's how things are done today.
*  So still today, many of the layers that you'll you'll deal with, you may deal with debuggers, you may deal with linkers.
*  There's libraries.
*  Many of those today will be written in C++, say, even though that language is pretty ancient and even the Python interpreter is probably written in C or C++.
*  So lots of layers there are probably written in these some old fashioned, efficient languages that still take one step to produce these instructions, produce risk instructions.
*  But they're composed.
*  Each layer of software invokes one another through these interfaces and you can get 10 layers of software that way.
*  So in general, the risk was developed here at Berkeley?
*  It was kind of the three places that were these radicals that advocated for this against the rest of the community were IBM, Berkeley and Stanford.
*  You're one of these radicals.
*  And how radical did you feel?
*  How confident did you feel?
*  How doubtful were you that risk might be the right approach?
*  Because it may you can also into it that is kind of taking a step back into simplicity, not forward into simplicity.
*  Yeah, no, it was easy to make.
*  Yeah, it was easy to make the argument against it.
*  Well, this was my colleague, John Hennessy at Stanford and I, we were both assistant professors.
*  And for me, I just believed in the power of our ideas.
*  I thought what we were saying made sense.
*  Morris law is going to move fast.
*  The other thing that I didn't mention is one of the surprises of these complex instruction sets.
*  You could certainly write these complex instructions if the programmers writing them themselves.
*  It turned out to be kind of difficult for the compiler to generate those complex instructions.
*  Kind of ironically, you'd have to find the right circumstances that just exactly fit this complex instruction.
*  It was actually easier for the compiler to generate these simple instructions.
*  So not only did these complex instructions make the hardware more difficult to build, often the compiler wouldn't even use them.
*  And so it's harder to build.
*  The compiler doesn't use them that much.
*  The simple instructions go better with Morris law.
*  That's the number of transistors is doubling every every two years.
*  So we're going to have the you want to reduce the time to design the microprocessor.
*  That may be more important than these number of instructions.
*  So I think we believed in the that we were right that this was the best idea.
*  Then the question became in these debates.
*  Well, yeah, that's a good technical idea.
*  But in the business world, this doesn't matter.
*  There's other things that matter.
*  It's like arguing that if there's a standard with the railroad tracks and you've come up with a better with but the whole world is covered railroad tracks.
*  So you'll your ideas have no chance of success.
*  Commercial success.
*  It was technically right.
*  But commercially, it'll be insignificant.
*  Yes.
*  It's kind of sad that this world, the history of human civilization is full of good ideas that lost because somebody else came along first with a worse idea.
*  And it's good that in the computing world, at least some of these have well, you could I mean, there's probably still CISC people that say, yeah, there still are.
*  Well, and what happened was what was interesting.
*  Intel, a bunch of the CISC companies with CISC instruction sets of vocabulary, they gave up, but not Intel.
*  What Intel did to its credit, because Intel's vocabulary was in the in the personal computer.
*  And so that was a very valuable vocabulary, because the way we distribute software is in those actual instructions.
*  It's in the instructions of that instruction set.
*  So they you don't get that source code, what the programmers wrote, you get after it's been translated into the lowest level.
*  That's if you were to get a floppy disk or download software, it's in the instructions that instruction set.
*  So the x86 instruction set was very valuable.
*  So what Intel did cleverly and amazingly is they had their chips in the hardware do a translation step.
*  They would take these complex instructions and translate them into essentially in RISC instructions in hardware on the fly, you know, at at gigahertz clock speeds.
*  And then any good idea that RISC people had, they could use and they could still be compatible with this with this really valuable PC software, software base and which also had very high volumes, you know, 100 million personal computers per year.
*  So the CISC architecture in the business world was actually one in this PC era.
*  So just going back to the the time of designing RISC, when you design an instruction set architecture, do you think like a programmer?
*  Do you think like a microprocessor engineer?
*  Do you think like a artist, a philosopher?
*  Do you think in software and hardware?
*  I mean, is it art?
*  Is it science?
*  Yeah, I'd say I think designing a good instruction set is an art.
*  And I think you're trying to balance the simplicity and speed of execution with how well easy it will be for compilers to use it.
*  Right.
*  You're trying to create an instruction set that everything in there can be used by compilers.
*  There's not things that are missing that'll make it difficult for the program to run.
*  They run efficiently, but you want it to be easy to build as well.
*  So it's that kind of.
*  So you're thinking, I'd say you're thinking hardware, trying to find a hards for software compromise that'll work well.
*  And it's, you know, it's, you know, it's a matter of taste.
*  Right.
*  It's kind of fun to build instruction sets.
*  It's not that hard to build an instruction set, but to build one that catches on and people use, you know, you have to be, you know, fortunate to be the right place in the right time or have a design that people really like.
*  Are you using metrics?
*  So is it quantifiable?
*  Because you kind of have to anticipate the kind of programs that people write ahead of time.
*  So is that, can you use numbers?
*  Can you use metrics?
*  Can you quantify something ahead of time?
*  Or is this again, that's the hard part where you're kind of.
*  No, it's a big, a big change.
*  Kind of what happened, I think from Hennessy's and my perspective in the 1980s, what happened was going from kind of really, you know, taste and hunches to quantifiable.
*  And in fact, he and I wrote a textbook at the end of the 1980s called Computer Architecture, a Quantitative Approach.
*  I heard of that.
*  And it's the thing that it had a pretty big impact in the field because we went from textbooks that kind of listed.
*  So here's what this computer does, and here's the pros and cons, and here's what this computer does and pros and cons to something where there were formulas and equations where you could measure things.
*  So specifically for instruction sets, what we do and some other fields do is we agree upon a set of programs, which we call benchmarks.
*  And a suite of programs, and then you develop both the hardware and the compiler and you get numbers on how well your computer does, given its instruction set and how well you implemented it in your microprocessor and how good your compilers are.
*  And in computer architecture, we, you know, using professors terms, we grade on a curve rather than grade on absolute scale.
*  So when you say, you know, this these programs run this fast, well, that's kind of interesting.
*  But how do you know it's better?
*  Well, you compare it to other computers at the same time.
*  So the best way we know how to make turned into a kind of more science and experimental and quantitative is to compare yourself to other computers of the same era that have the same access, the same kind of technology on commonly agreed benchmark programs.
*  So maybe to toss up two possible directions, we can go one is what are the different trade offs in designing architectures?
*  We've been already talking about Sysc and Risk, but maybe a little bit more detail in terms of specific features that you were thinking about.
*  And the other side is what are the metrics that you're thinking about when looking at these trade offs?
*  Yeah, let's talk about the metrics.
*  So during these debates, we actually had kind of a hard time explaining, convincing people the ideas.
*  And partly we didn't have a formula to explain it.
*  And a few years into it, we hit upon a formula that helped explain what was going on.
*  And I think if we can do this, see how it works orally.
*  So the is if I can do a formula orally.
*  So the so fundamentally, the way you measure performance is how long does it take a program to run a program?
*  If you have 10 programs, typically these benchmarks were sweet because you'd want to have 10 programs so they could represent lots of different applications.
*  So for these 10 programs, how long did it take to run?
*  Well, now, when you're trying to explain why it took so long, you could factor how long it takes a program to run into three factors.
*  One of the first one is how many instructions did it take to execute?
*  So that's the that's the what we've been talking about, you know, the instructions of alchemy.
*  How many did it take? All right.
*  The next question is how long did each instruction take to run on average?
*  So you multiply the number of instructions times how long it took to run and that time.
*  OK, so that's but now let's look at this metric of how long did it take the instruction to run?
*  Well, it turns out the way we could build computers today is they all have a clock.
*  And you've seen this when you if you buy a microprocessor, it'll say three point one gigahertz or two point five gigahertz and more gigahertz is good.
*  Well, what that is, is the speed of the clock.
*  So two point five gigahertz turns out to be four billionths of instruction or four nanoseconds.
*  So that's the clock cycle time.
*  But there's another factor, which is what's the average number of clock cycles it takes per instruction?
*  So it's number of instructions, average number of clock cycles and the clock cycle time.
*  So in these risks, this debates, we would they would concentrate on but risk needs to take more instructions.
*  And we'd argue what maybe the clock cycle is faster.
*  But what the real big difference was, was the number of clock cycles per instruction.
*  Per instruction, that's fascinating.
*  What about the mess of the beautiful mess of parallelism in the whole picture?
*  Parallelism, which has to do with, say, how many instructions could execute in parallel and things like that.
*  You could think of that as affecting the clock cycles per instruction because it's the average clock cycles per instruction.
*  So when you're running a program, if it if it took 100 billion instructions and on average, it took two clock cycles per instruction and they were four nanoseconds, you could multiply that out and see how long it took to run.
*  And there's all kinds of tricks to try and reduce the number of clock cycles per instruction.
*  But it turned out that the way they would do these complex instructions is they would actually build what we would call an interpreter in a simpler, a very simple hardware interpreter.
*  But it turned out that for the SysConstructions, if you had to use one of those interpreters, it would be like 10 clock cycles per instruction, where the risk instructions could be two.
*  So there'd be this factor of five advantage in clock cycles per instruction.
*  We have to execute, say, 25 or 50 percent more instructions.
*  So that's where the win would come.
*  And then you could make an argument whether the clock cycle times are the same or not.
*  But pointing out that we could divide the benchmark results, time per program, into three factors.
*  And the biggest difference in risk consists was the clock cycles per, you execute a few more instructions, but the clock cycles per instruction is much less.
*  And that was what this debate was.
*  Once we made that argument, then people said, OK, I get it.
*  And so we went from it was outrageously controversial in 1982 that maybe probably by 1984 or so people said, oh, yeah, technically they've got a good argument.
*  What are the instructions in the risk instruction set?
*  Just to get an intuition.
*  OK, 1995, I was asked to predict the future of what microprocessor future.
*  So I and I had seen these predictions and usually people predict something outrageous just to be entertaining.
*  And so my prediction for 2020 was, you know, things are going to be pretty much they're going to look very familiar to what they are.
*  And they are. And if you were to read the article, you know, the things I said are pretty much true.
*  The instructions that that have been around forever are kind of the same.
*  And that's the outrageous prediction, actually.
*  Yeah. Given how fast computers are.
*  Well, you know, Moore's law was going to go on, we thought, for 25 more years.
*  You know, who knows? But kind of the surprising thing.
*  In fact, you know, Hennessy and I, you know, won the ACM, A.M.
*  Touring Award for both the risk construction set contributions and for that textbook I mentioned.
*  But, you know, we are surprised that here we are 35, 40 years later after we did our work.
*  And the conventionalism of the best way to do instruction sets is still those risk
*  construction sets that look very similar to what we looked like, you know, we did in the 1980s.
*  So those surprisingly, there hasn't been some radical new idea, even though we have, you know, a million times as many
*  transistors as we had back then.
*  But what are the basic instructions and how do they change over the years?
*  So we're talking about addition, subtract, these are the specific.
*  So the things that are in a calculator are in a computer.
*  So any of the buttons that are in the calculator in the computer.
*  So the button. So if there's a memory function key.
*  And like I said, those are turns into putting something in memory is called a store, bring something back to load.
*  Just a quick tangent.
*  When you say memory, what does memory mean?
*  Well, I told you there were five pieces of a computer.
*  And if you remember in a calculator, there's a memory key.
*  So you want to have an intermediate calculation and bring it back later.
*  So you'd hit the memory plus key, M plus maybe, and it would put that into memory.
*  And then you'd hit an RM like recurrent instruction and then bring it back into the display.
*  So you don't have to type it.
*  You don't have to write it down and bring it back again.
*  So that's exactly what memory is.
*  You can put things into it as temporary storage and bring it back when you need it later.
*  So that's memory and loads and stores.
*  But the big thing, the difference between a computer and a calculator is that the computer can make decisions.
*  And amazingly, decisions are as simple as is this value less than zero or is this value bigger than that value?
*  So there's those instructions, which are called conditional branch instructions, is what give computers all its power.
*  If you were in the early days of computing before what's called the general purpose microprocessor, people would write these instructions kind of in hardware.
*  But it couldn't make decisions.
*  It would just it would do the same thing over and over again.
*  With the power of having branch instructions, it can look at things and make decisions automatically.
*  And it can make these decisions billions of times per second.
*  And amazingly enough, we can get, you know, thanks to advanced machine learning, we can we can create programs that can do something smarter than human beings can do.
*  But if you go down that very basic level, it's the instructions are the keys on the calculator, plus the ability to make decisions.
*  These conditional branch instructions.
*  And all decisions fundamentally can be reduced down to these branch instructions.
*  Yeah. So in fact, and so, you know, going way back in the stack back to we did four RISC projects.
*  At Berkeley in the 1980s, they did a couple at Stanford in the 1980s.
*  In 2010, we decided we wanted to do a new instruction set learning from the mistakes of those RISC architectures in the 1980s.
*  And that was done here at Berkeley almost exactly 10 years ago.
*  And the people who did it, I participated, but other Kristo Sanovic and others drove it.
*  They called it RISC 5 to honor those RISC, the four RISC projects of the 1980s.
*  So what is RISC 5 involved?
*  So RISC 5 is another instruction set vocabulary.
*  It's learned from the mistakes of the past, but it still has if you look at the there's a core set of instructions is very similar to the simplest architectures from the 1980s.
*  And the big difference about RISC 5 is it's open.
*  So I talked early about proprietary versus open and open source software.
*  So this is an instruction set.
*  So it's a vocabulary.
*  It's not it's not hardware, but by having an open instruction set, we can have open source implementations, open source processors that people can use.
*  Where do you see that going?
*  It's a really exciting possibilities, but you're just like in the Scientific American, if you were to predict 10, 20, 30 years from now, that kind of ability to utilize open source instruction set architectures like RISC 5.
*  What kind of possibilities might that unlock?
*  Yeah. And so just to make it clear, because this is confusing, the specification of RISC 5 is something that's like in a textbook.
*  There's books about it.
*  So that's what that's defining an interface.
*  There's also the way you build hardware is you write it in languages that are kind of like C, but they're specialized for hardware that gets translated into hardware.
*  And so these implementations of this specification are what are the open source.
*  So they're written in something that's called Verilog or VHDL, but it's put up on the web just like you can see the C++ code for Linux on the web.
*  So that's the open instruction set enables open source implementations of RISC 5.
*  So you can literally build a processor using this instruction set.
*  People are. People are.
*  So what happened to us that the story was this was developed here for our use to do our research and we made it.
*  We licensed under the Berkeley Software Distribution license.
*  Like a lot of things get licensed here.
*  So other academics use it.
*  They wouldn't be afraid to use it.
*  And then about 2014, we started getting complaints that we were using it in our research and in our courses.
*  And we got complaints from people in industry is why did you change your instruction set between the fall and the spring semester?
*  And while we get complaints from industrial time, why the hell do you care what we do with our instruction set?
*  And then when we talked to them, we found out there was this thirst for this idea of an open instruction set architecture.
*  And they had been looking for one.
*  They stumbled upon ours at Berkeley, thought it was, boy, this looks great.
*  We should use this one.
*  And so once we realized there is this need for an open instruction set architecture, we thought that's a great idea.
*  And then we started supporting it and tried to make it happen.
*  So this was kind of we accidentally stumbled into this and to this need and our timing was good.
*  And so it's really taking off.
*  There's universities are good at starting things, but they're not good at sustaining things.
*  So like Linux has a Linux foundation, there's a RISC-V foundation that we started.
*  There's there's an annual conferences and the first one was done, I think, January 2015.
*  And the one that was just last December in it, you know, it had 50 people at it.
*  And this one last December had, I don't know, 1700 people were at it and the companies excited all over the world.
*  So if predicting into the future, you know, if we were doing 25 years, I would predict that RISC-V will be, you know,
*  possibly the most popular instruction set architecture out there because it's a pretty good instruction set architecture and it's open and free.
*  And there's no reason lots of people shouldn't use it.
*  And there's benefits just like Linux is so popular today compared to 20 years ago.
*  And, you know, the fact that you can get access to it for free, you can modify it, you can improve it for all those same arguments.
*  And so people collaborate to make it a better system for everybody to use.
*  And that works in software. And I expect the same thing will happen in hardware.
*  So if you look at ARM, Intel, MIPS, if you look at just the lay of the land, and what do you think?
*  Just for me, because I'm not familiar how difficult this kind of transition would,
*  how much challenges this kind of transition would entail.
*  Do you see? Let me ask my dumb question in another way.
*  No, that's I know where you're headed.
*  Well, there's a bunch. I think the thing you point out, there's there's these very popular proprietary instruction sets, the x86.
*  And so how do we move to risk five potentially in sort of in the span of five, 10, 20 years, a kind of unification?
*  And given that the devices, the kind of way we use devices, IOT, mobile devices and the cloud keeps changing.
*  Well, part of it, a big piece of it is the software stack.
*  And what right now, looking forward, there seem to be three important markets.
*  There's the cloud.
*  And the cloud is simply companies like Alibaba and Amazon and Google, Microsoft having these giant data centers with tens of thousands of servers in maybe a hundred of these data centers all over the world.
*  And that's what the cloud is.
*  So the computer that dominates the cloud is the x86 instruction set.
*  So the instructions are the instruction sets used in the cloud or the x86.
*  Almost almost 100% of that today is x86.
*  The other big thing are cell phones and laptops.
*  Those are the big things today.
*  I mean, the PC is also dominated by the x86 instruction set, but those sales are dwindling.
*  You know, there's maybe 200 million PCs a year and there's one and a half billion phones a year.
*  There's numbers like that.
*  So for the phones, that's dominated by ARM.
*  And now, and a reason that I talked about the software stacks and the third category is Internet of Things, which is basically embedded devices, things in your cars and your microwaves everywhere.
*  So what's different about those three categories is for the cloud, the software that runs in the cloud is determined by these companies, Alibaba, Amazon, Google, Microsoft.
*  So they control that software stack.
*  For the cell phones, there's both for Android and Apple, the software they supply, but both of them have marketplaces where anybody in the world can build software.
*  And that software is translated or compiled down and shipped in the vocabulary of ARM.
*  So that's what's referred to as binary compatible because the actual instructions are turned into numbers, binary numbers and shipped around the world.
*  So just a quick interruption.
*  So ARM, what is ARM?
*  ARM is an instruction set, like a risk based...
*  Yeah, it's a risk based instruction set.
*  It's a proprietary one.
*  ARM stands for Advanced Risk Machine.
*  ARM is the name where the company is.
*  So it's a proprietary risk architecture.
*  So, and it's been around for a while and is, you know, surely the most popular instruction set in the world right now.
*  Every year, billions of chips are using the ARM design in this post PC era.
*  Was it one of the early risk adopters of the risk idea?
*  The first ARM goes back, I don't know, 86 or so.
*  So Berkeley and Stad did their work in the early 80s.
*  The ARM guys needed an instruction set and they read our papers and it heavily influenced them.
*  So getting back to my story, what about Internet of Things?
*  Well, software is not shipped in Internet of Things.
*  It's the embedded device.
*  People control that software stack.
*  So the opportunities for RISC-V, everybody thinks, is in the Internet of Things, embedded things, because there's no dominant player like there is in the cloud or the
*  smartphones.
*  And, you know, it doesn't have a lot of licenses associated with and you can enhance the instruction set if you want.
*  And people have looked at instruction sets and think it's a very good instruction set.
*  So it appears to be very popular there.
*  It's possible that in the cloud, people, those companies control their software stacks.
*  So it's possible that they would decide to use RISC-V if we're talking about 10 and 20 years in the future.
*  The one that would be harder would be the cell phones, since people ship software in the ARM instruction set, that you'd think be the more difficult one.
*  But if RISC-V really catches on, you know, in a period of a decade, you can imagine that's changing over too.
*  Do you have a sense why RISC-V or ARM has dominated?
*  You mentioned these three categories.
*  Why did ARM dominate?
*  Why does it dominate the mobile device space?
*  And maybe my naive intuition is that there are some aspects of power efficiency that are important that somehow come along with RISC.
*  Well, part of it is for these old SysC instructions, that's like in the x86.
*  It was more expensive to these for, you know, they're older, so they have disadvantages in them because
*  they were designed 40 years ago, but also they have to translate in hardware from SysC instructions to RISC instructions on the fly.
*  And that costs both silicon area, the chips are bigger to be able to do that, and it uses more power.
*  So ARM has, which has followed this RISC philosophy, is seen to be much more energy efficient.
*  And in today's computer world, both in the cloud and cell phone and things, it isn't
*  the limiting resource isn't the number of transistors you can fit in the chip.
*  It's how much power can you dissipate for your application?
*  So by having a reduced instruction set, that's possible to have simpler hardware, which is more energy efficient.
*  And energy efficiency is incredibly important in the cloud.
*  When you have tens of thousands of computers in a data center, you want to have the most energy efficient ones there as well.
*  And of course, for embedded things running off of batteries, you want those to be more energy efficient in the cell phones too.
*  So I think it's believed that there's an energy disadvantage of using these more complex instruction set architectures.
*  So the other aspect of this is if we look at Apple, Qualcomm, Samsung, Huawei, all use the ARM architecture.
*  And yet the performance of the systems varies.
*  I mean, I don't know whose opinion you take on, but, you know, Apple for some reason seems to perform better in terms of these.
*  Implementation these architectures. So where's the magic?
*  Enter the picture.
*  How's that happen?
*  Yeah, so what ARM pioneered was a new business model, as they said, well, here's our proprietary instruction set.
*  And we'll give you two ways to do it.
*  Either we'll give you one of these implementations written in things like C called Verilog, and you can just use ours.
*  Well, you have to pay money for that.
*  Not only will we license you to do that, or you could design your own.
*  And so we're talking about numbers like tens of millions of dollars to have the right to design your own since the instruction set belongs to them.
*  So Apple got one of those, the right to build their own.
*  Most of the other people who build like Android phones just get one of the designs from ARM to do it themselves.
*  So Apple developed a really good microprocessor design team.
*  They acquired a very good team that was building other microprocessors and brought them into the company to build their designs.
*  So the instruction sets are the same, the specifications are the same, but their hardware design is much more efficient than I think everybody else's.
*  And that's given Apple an advantage in the marketplace in that the iPhones tend to be faster than most everybody else's phones that are there.
*  It'd be nice to be able to jump around and kind of explore different little sides of this.
*  But let me ask one sort of romanticized question.
*  What to you is the most beautiful aspect or idea of RISC instruction set or instruction sets?
*  Well, I think I was always attracted to the idea of small is beautiful.
*  Is that the temptation in engineering, it's kind of easy to make things more complicated.
*  It's harder to come up with a, it's more difficult surprisingly to come up with a simple, elegant solution.
*  And I think there's a bunch of small features of RISC in general that, you know, where you can see this examples of keeping it simpler makes it more elegant.
*  Specifically in RISC 5, which, you know, I was kind of the mentor in the program, but it was really driven by Krista Sanovic and two graduate students, Andrew Waterman and Yann Sipley.
*  Is they hit upon this idea of having a subset of instructions, a nice simple subset instructions like 40-ish instructions that all software, the software staff for RISC 5 can run just on those 40 instructions.
*  And then they provide optional features that could accelerate the performance instructions that if you needed them could be very helpful, but you don't need to have them.
*  And that's a new, really a new idea. So RISC 5 has right now, maybe five optional subsets that you can pull in, but the software runs without them.
*  If you just want to build the just the core 40 instructions, that's fine. You can do that.
*  So this is fantastic educationally is you can explain computers, you only have to explain 40 instructions and not thousands of them.
*  Also, if you invent some wild and crazy new technology like, you know, biological computing, you'd like a nice simple instruction set.
*  And you can RISC 5 if you implement those core instructions, you can run really interesting programs on top of that.
*  So this idea of a core set of instructions that the software stack runs on and then optional features that if you turn them on, the compilers were used, but you don't have to.
*  I think it's a powerful idea. What's happened in the past for the proprietary instruction sets is when they add new instructions, it becomes required piece.
*  And so that all all microprocessors in the future have to use those instructions.
*  So it's kind of like for a lot of people as they get older, they gain weight, right?
*  Is that weight and age are correlated? And so you can see these instruction sets get getting bigger and bigger as they get older.
*  So RISC 5 lets you be as slim as you are as a teenager and you only have to add these extra features if you're really going to use them rather than you have no choice.
*  You have to keep growing with the instruction set.
*  I don't know if the analogy holds up, but that's a beautiful notion that there's it's almost like a nudge towards here's the simple core.
*  That's the essential.
*  Yeah, I think the surprising thing is still if we if we brought back the pioneers from the 1950s and showed them the instruction set architectures, they'd understand it.
*  They'd say, wow, that doesn't look that different.
*  Well, you know, I'm surprised. And it's there's it may be something, you know, talk about philosophical things.
*  I mean, there may be something powerful about those 40 or 50 instructions that all you need is these commands like these instructions that we talked about.
*  And that is sufficient to build to bring about artificial intelligence.
*  And so it's a remarkable.
*  Surprising to me that is complicated as it is to build these things, you know, microprocessors where the line widths are narrower than the wavelength of light, you know, is this amazing technology is at some fundamental level.
*  The commands that software executes are really pretty straightforward and haven't changed that much in in decades, which what a surprising outcome.
*  So underlying all computation, all Turing machines, all artificial intelligence systems perhaps might be a very simple instruction set like like a risk five or it's.
*  Yeah, I mean, that's kind of what I said.
*  I was interested to see I had another more senior faculty colleague and he he had written something in Scientific American and, you know, his 25 years in the future and his turned out about when I was a young professor and he said, yep, I checked it.
*  I was interested to see how that was going to turn out for me and it's pretty held up pretty well.
*  But yeah, so there's there's probably there's some, you know, there's there must be something fundamental about those instructions that were capable of creating intelligence from pretty primitive operations.
*  And just doing them really fast.
*  You kind of mentioned a different, maybe radical computational medium like biological and there's other ideas.
*  So there's a lot of space in a six domain specific and then there could be quantum computers.
*  And so we can think of all those different mediums and types of computation.
*  What's the connection between swapping out different hardware systems in the instruction set?
*  Do you see those as disjoint or they fundamentally coupled?
*  Yeah, so what's so kind of if we go back to the history.
*  You know, when Moore's Law is in full effect and you're getting twice as many transistors every couple of years, you know, kind of the challenge for computer designers is how can we take advantage of that?
*  How can we turn those transistors into better computers faster, typically?
*  And so there was an era.
*  I guess in the 80s and 90s where computers were doubling performance every 18 months.
*  And if you weren't around, then what would happen is you had your computer and your friend's computer, which was like a year or year and a half newer.
*  And it was much faster than your computer.
*  And you he he or she could get their work done much faster than your time because you were so people took their computers perfectly good computers.
*  And threw them away to buy a newer computer because the computer one or two years later was so much faster.
*  So that's what the world was like in the 80s and 90s.
*  Well, with the slowing down of Moore's Law, that's no longer true, right?
*  Even now with not not desk side computers with the laptops, I only get a new desk laptop when it breaks, right?
*  How damn the disk broke or this display broke.
*  I got to buy a new computer.
*  But before you would throw them away because it just they were just so sluggish compared to the latest computers.
*  So that's a huge change of what's gone on.
*  So but since this lasted for decades, kind of programmers and maybe all of society is used to computers getting faster regularly.
*  We now now believe those of us who are in computer design, it's called computer architecture, that the path forward is instead is to add accelerators that only work well for certain applications.
*  So since Moore's Law is slowing down, we don't think general purpose computers are going to get a lot faster.
*  So the Intel processes of the world are not going to haven't been getting a lot faster.
*  They've been barely improving like a few percent a year.
*  It used to be doubling every 18 months, and now it's doubling every 20 years.
*  So it was just shocking.
*  So to be able to deliver on what Moore's Law used to do, we think what's going to happen, what is happening right now is people adding accelerators to their microprocessors that only work well for some domains.
*  And by sheer coincidence, at the same time that this is happening, has been this revolution in artificial intelligence called machine learning.
*  So with, as I'm sure your other guests have said, you know, AI had these two competing schools of thought is that we could figure out artificial intelligence by just writing the rules top down, or that was wrong.
*  You had to look at data and infer what the rules are, the machine learning, and what's happened in the last decade or eight years is machine learning has won.
*  And it turns out that machine learning, the hardware you build for machine learning is pretty much multiply.
*  The matrix multiply is a key feature for the way people, machine learning is done.
*  So that's a godsend for computer designers.
*  We know how to make matrix multiply run really fast.
*  So general purpose microprocessors are slowing down.
*  We're adding accelerators for machine learning that fundamentally are doing matrix multiplies much more efficiently than general purpose computers have done.
*  So we have to come up with a new way to accelerate things.
*  The danger of only accelerating one application is how important is that application.
*  Turns out, it turns out machine learning gets used for all kinds of things.
*  So serendipitously, we found something to accelerate that's widely applicable.
*  And we don't even we're in the middle of this revolution of machine learning.
*  We're not sure what the limits of machine learning are.
*  So this has been kind of a godsend.
*  If you're going to be able to excel, deliver on improved performance, as long as people are moving their programs to be embracing more machine learning,
*  we know how to give them more performance, even as Morris Law is slowing down.
*  And counterintuitively, the machine learning mechanism, you can say is domain specific, but because it's leveraging data, it's actually could be very broad in terms of.
*  In terms of the domains that could be applied in.
*  Yeah, that's exactly right.
*  Sort of it's almost sort of people sometimes talk about the idea of software 2.0.
*  We're almost taking another step up in the abstraction layer in designing.
*  Machine learning systems, because now you're programming in the space of data in the space of hyper parameters is changing fundamentally the nature of programming.
*  And so the specialized devices that that accelerate the performance, especially neural network based machine learning systems, might become the new general.
*  Yes, so the thing that's interesting point out, these are not tied together.
*  The enthusiasm about machine learning, about creating programs driven from data that we should figure out the answers from data rather than kind of top down, which classically the way.
*  Most programming is done in the way artificial intelligence used to be done.
*  That's a movement that's going on at the same time.
*  Coincidentally, and the first word machine learning is machines, right?
*  So that's going to increase the demand for computing because instead of programmers being smart writing those things down, we're going to instead use computers to examine a lot of data to kind of create the programs.
*  That's the idea.
*  And remarkably, this gets used for all kinds of things very successfully.
*  The image recognition, the language translation, the game playing, and it gets into pieces of the software stack like databases and stuff like that.
*  We're not quite sure how general purpose is, but that's going on independent of this hardware stuff.
*  What's happening on the hardware side is Moore's law is slowing down right when we need a lot more cycles.
*  It's failing us.
*  Right when we need it, because there's going to be a greater increase in computing.
*  And then this idea that we're going to do so-called domain specific.
*  Here's a domain that your greatest fear is you'll make this one thing work and that'll help 5% of the people in the world.
*  Well, this looks like it's a very general purpose thing.
*  So the timing is fortuitous that if we can perhaps if we can keep building hardware that will accelerate machine learning, the neural networks, that'll beat the timing will be right.
*  That neural network revolution will transform software, the so-called software 2.0.
*  And the software of the future will be very different from the software of the past.
*  And just as our microprocessors, even though we're still going to have that same basic risk instructions to run a big pieces of the software stack like user interfaces and stuff like that,
*  we can accelerate the kind of the small piece that's computationally intensive.
*  It's not lots of lines of code, but it takes a lot of cycles to run that code.
*  That that's going to be the accelerator piece.
*  And so that's what makes this from a computer designer's perspective, a really interesting decade.
*  But Hennessy and I talked about in the title of our Turing Warrant speech is a new golden age.
*  We we see this as a very exciting decade, much like when we were assistant professors and the risk stuff was going on.
*  That was a very exciting time was where we were changing what was going on.
*  We see this happening again.
*  Tremendous opportunities of people because we're fundamentally changing how software is built and how we're running it.
*  So which layer of the abstraction do you think most of the acceleration might be happening?
*  If you look in the next 10 years, Google is working on a lot of exciting stuff with the TPU.
*  So if there's a closer to the hardware, there could be optimizations around the closer to the instruction set.
*  There could be optimization at the compiler level.
*  It could be even at the higher level software stack.
*  Yeah, it's going to be if you think about the old RISC-SYS debate, it was both it was software hardware.
*  It was the compiler's improving as well as the architecture improving.
*  And that's likely to be the way things are now with machine learning.
*  They they're using domain specific languages.
*  The languages like TensorFlow and PyTorch are very popular with the machine learning people.
*  So that those are raising the level of abstraction.
*  It's easier for people to write machine learning in these domain specific languages like PyTorch and TensorFlow.
*  So where the most optimization might happen.
*  Yeah. And so and so there'll be both the compiler piece and the hardware piece underneath it.
*  So as you kind of the fatal flaw for hardware people is to create really great hardware but not have brought along the compilers.
*  What we're seeing right now in the marketplace because of this enthusiasm around hardware for machine learning is getting, you know,
*  probably billions of dollars invested in startup companies.
*  We're seeing startup companies go belly up because they focus on the hardware but didn't bring the software stack along.
*  We talked about benchmarks earlier.
*  So I participated in machine learning, didn't really have a set of benchmarks.
*  I think just two years ago they didn't have a set of benchmarks.
*  And we've created something called MLPerf, which is machine learning benchmark suite.
*  And pretty much the companies who didn't invest in software stack couldn't run MLPerf very well.
*  And the ones who did invest in software stack did.
*  And we're seeing, you know, like kind of in computer architecture, this is what happens.
*  You have these arguments about risk versus this.
*  People spend billions of dollars in the marketplace to see who wins.
*  And it's not it's not a perfect comparison, but it kind of sorts things out.
*  And we're seeing companies go out of business and then companies like like there's a company in Israel called Habana.
*  They came up with machine learning accelerators.
*  They had good MLPerf scores.
*  Intel had acquired a company earlier called Nirvana a couple of years ago.
*  They didn't reveal their MLPerf scores, which was suspicious.
*  But a month ago, Intel announced that they're canceling the Nirvana product line.
*  And they bought Habana for two billion dollars.
*  And Intel is going to be shipping Habana chips, which have hardware and software and run the MLPerf programs pretty well.
*  And that's going to be their product line in the future.
*  Brilliant. So maybe just a linker briefly.
*  I'm MLPerf. I love metrics.
*  I love standards that everyone can gather around.
*  What are some interesting aspects of that portfolio of metrics?
*  Well, one of the interesting metrics is, you know, what we thought it was, you know,
*  I was involved in the start.
*  You know, we Peter Mattson is leading the effort from Google.
*  Google got it off the ground.
*  But we had to reach out to competitors and say,
*  there's no benchmarks here.
*  This we think this is bad for the field.
*  It'll be much better if we look at examples like in the risk days,
*  there was an effort to create a for the the people in the risk community got together.
*  Competitors got together, building risk microprocessors to agree on a set of benchmarks that were called spec.
*  And that was good for the industry is rather before the different risk architectures were arguing,
*  well, you can believe my performance others, but those other guys are liars.
*  And that didn't do any good.
*  So we agreed on a set of benchmarks.
*  And then we could figure out who was faster between the various risk architectures.
*  But it was a little bit faster.
*  But that grew the market rather than people were afraid to buy anything.
*  So we argued the same thing would happen with MLPerf.
*  You know, companies like Nvidia were maybe worried that it was some kind of trap.
*  But eventually we all got together to create a set of benchmarks and do the right thing.
*  Right. And we agree on the results.
*  And so we can see whether TPUs or GPUs or CPUs are really faster and how much the faster.
*  And I think from an engineer's perspective, as long as the results are fair, you can live with it.
*  OK, you know, you kind of tip your hat to your colleagues at another institution.
*  Boy, they did a better job than this.
*  What you what you hate is if it's it's false.
*  They're making claims and it's just marketing bullshit and, you know, and that's affecting sales.
*  So from an engineer's perspective, as long as it's a fair comparison and we don't come in first place, that's too bad.
*  But it's fair. So we wanted to create that environment for MLPerf.
*  And so now there's 10 companies, I mean, 10 universities and 50 companies involved.
*  So pretty much MLPerf has is the is the way you measure machine learning performance.
*  And and it didn't exist even two years ago.
*  One of the cool things that I enjoy about the Internet has a few downsides.
*  But one of the nice things is people can see through BS a little better with the presence of these kinds of metrics.
*  So it's really nice companies like Google and Facebook and Twitter.
*  Now, it's the cool thing to do is to put your engineers forward and to actually show off how well you do on these metrics.
*  There's not sort of it.
*  Well, there's less of a desire to do marketing, less so in my in my sort of naive.
*  No, I think I was trying to understand that, you know, what's changed from the 80s in this era, I think because of things like social
*  networking, Twitter and stuff like that, if you if you put up, you know, bullshit stuff, right, that's just, you know,
*  purposely misleading, you know, that you can get a violent reaction in social media pointing out the flaws in your arguments.
*  Right. And so from a marketing perspective, you have to be careful today that you didn't have to be careful that there'll be people who put out the flaw.
*  You can get the word out about the flaws in what you're saying much more easily today than in the past.
*  You used to be it used to be easier to get away with it.
*  And the other thing that's been happening in terms of showing off engineers is just in the software side, people have largely embraced open source
*  software. It was 20 years ago, it was a dirty word at Microsoft.
*  And today, Microsoft is one of the big proponents of open source software.
*  The kind of that's the standard way most software gets built, which really shows off your engineers, because you can see if you look at the
*  source code, you can see who are making the commits, who's making the improvements, who are the engineers at all these companies who are
*  are really great programmers and engineers and making really solid contributions, which enhances their reputations and the reputation of the companies.
*  So, but that's, of course, not everywhere, like in the space that I work more in is autonomous vehicles, and there's still
*  the machinery of hype and marketing is still very strong there, and there's less willingness to be open in this kind of open source way and sort of
*  benchmarks. So MLPerf represents the machine learning world is much better being open source about holding itself to standards of different, the amount of
*  incredible benchmarks in terms of the different computer vision, natural processing, tasks is incredible.
*  You know, historically, it wasn't always that way. I had a graduate student working with me, David Martin. So for in computer in some fields,
*  benchmarking is been around forever. So computer architecture, databases, maybe operating systems, benchmarks are the way you measure progress.
*  But he was working with me and then started working with Jitendra Malik and he's in computer vision space,
*  I guess you've interviewed Jitendra. And David Martin told me they don't have benchmarks. Everybody has their own vision algorithm and the way
*  here's my image, look at how well I do. And everybody had their own image. So David Martin,
*  back when he did his dissertation, figured out a way to do benchmarks. He had a bunch of graduate students
*  identify images and then ran benchmarks to see which algorithms run well. And that was, as far as I know, kind of the first time
*  people did benchmarks in computer vision and which was predated all the things that eventually led to
*  ImageNet and stuff like that. But then, you know, the vision community got religion and then once we got as far as ImageNet, then
*  that let the guys in Toronto be able to win the ImageNet competition and then, you know, that changed the whole world.
*  It's a scary step actually, because when you enter the world of benchmarks, you actually have to be good to participate.
*  As opposed to, yeah, you can just believe you're the best in the world.
*  And I think the people, I think they weren't purposely misleading. I think if you don't have benchmarks, I mean, how do you know?
*  You know, you could have your intuition. It's kind of like the way we did just do computer architecture.
*  Your intuition is that this is the right instruction set to do this job. I believe,
*  in my experience, my hunch is that's true. We had to get to make things more quantitative
*  to make progress. And so I just don't know how, you know, in fields that don't have benchmarks,
*  I don't understand how they figure out how they're making progress.
*  We're kind of in the vacuum tube days of quantum computing. What are your thoughts in this wholly
*  different kind of space of architectures? You know, I actually, you know, quantum computing
*  is, idea's been around for a while and I actually thought, well, I sure hope
*  I retire before I have to start teaching this. I'd say because I talk about, give these talks about
*  the slowing of Moore's law and, you know, when we need to change by doing domain specific accelerators,
*  common questions say, what about quantum computing? The reason that comes up, it's in the news all the
*  time. So I think the key, the hard thing to keep in mind is quantum computing is not right around
*  the corner. There have been two national reports, one by the National Campus of Engineering, another
*  by the Computing Consortium, where they did a frank assessment of quantum computing and
*  both of those reports said, you know, as far as we can tell, before you get error corrected
*  quantum computing, it's a decade away. So I think of it like nuclear fusion, right? There have been
*  people who've been excited about nuclear fusion a long time. If we ever get nuclear fusion, it's
*  going to be fantastic for the world. I'm glad people are working on it, but you know, it's not
*  right around the corner. Those two reports to me say probably it'll be 2030 before quantum computing
*  is something that could happen. And when it does happen, you know, this is going to be big science
*  stuff. This is micro Kelvin, almost absolute zero things that if they vibrate, if truck goes by,
*  it won't work, right? So this will be in data center stuff. We're not going to have a quantum
*  cell phone. And it's probably a 2030 kind of thing. So I'm happy that our people are working on it,
*  but just, you know, it's hard with all the news about it, not to think that it's right around the
*  corner. And that's why we need to do something as Moore's Law is slowing down to provide the
*  computing, keep computing getting better for this next decade. And, you know, we shouldn't be betting
*  on quantum computing or expecting quantum computing to deliver in the next few years.
*  It's probably further off. You know, I'd be happy to be wrong. It'd be great if quantum computing
*  is going to commercially viable, but it will be a set of applications. It's not a general purpose
*  computation. So it's going to do some amazing things, but there'll be a lot of things that
*  probably, you know, the old fashioned computers are going to keep doing better for quite a while.
*  And there'll be a teenager 50 years from now watching this video saying,
*  look how silly David Patterson was saying.
*  I said 2030. I didn't say never.
*  We're not going to have quantum cell phones. So he's going to be watching it.
*  Well, I mean, I think this is such a, you know, given that we've had Moore's Law, I just, I feel
*  comfortable trying to do projects that are thinking about the next decade. I admire people who are
*  trying to do things that are 30 years out, but it's such a fast moving field. I just don't know
*  how to, I'm not good enough to figure out what's the problem is going to be in 30 years. You know,
*  10 years is hard enough for me. So maybe if it's possible to untangle your intuition a little bit,
*  I spoke with Jim Keller. I don't know if you're familiar with Jim and he is trying to sort of
*  be a little bit rebellious and to try to think that he quotes me as being wrong.
*  Yeah. So this is-
*  What are your, wait, wait, wait, wait, for the record,
*  Jim talks about that he has an intuition that Moore's Law is not in fact dead yet and that it
*  may continue for some time to come. What are your thoughts about Jim's ideas in this space?
*  Yeah, this is just, this is just marketing. So what Gordon Moore said is a quantitative prediction.
*  We can check the facts, right? Which is doubling the number of transistors
*  every two years. So we can look back at Intel for the last five years and ask him,
*  let's look at DRAM chips six years ago. So that would be three two-year periods. So then our DRAM
*  chips have eight times as many transistors as they did six years ago. We can look up Intel
*  microprocessors six years ago. If Moore's Law is continuing, it should have eight times as many
*  transistors as six years ago. The answer in both those cases is no. The problem has been
*  because Moore's Law was kind of genuinely embraced by the semiconductor industry is they would make
*  investments in similar equipment to make Moore's Law come true.
*  Semiconductor improving and Moore's Law in many people's minds are the same thing. So when I say,
*  and I'm factually correct that Moore's Law is no longer holds, we are not doubling transistors
*  every year's years. The downside for a company like Intel is people think that means it's stopped,
*  that technology has no longer improved. And so Jim is trying to
*  counteract the impression that semiconductors are frozen in 2019 are never going to get better.
*  So I never said that. All I said was Moore's Law is no more. And I'm strictly looking at the
*  number of transistors that could that. That's what Moore's Law is. There's the, I don't know,
*  there's been this aura associated with Moore's Law that they've enjoyed for 50 years about,
*  look at the field we're in, we're doubling transistors every two years. What an amazing
*  field, which is amazing thing that they were able to pull off. But even as Gordon Moore said,
*  no exponential can last forever. It lasted for 50 years, which is amazing. And this is a huge
*  impact on the industry because of these changes that we've been talking about. So he claims,
*  because he's trying to act, he claims, you know, Patterson says Moore's Law is no more and look at
*  it's still going. And TSMC, they say it's no longer, but there's quantitative evidence that
*  Moore's Law is not continuing. So what I say now to try and, okay, I understand the perception
*  problem when I say Moore's Law has stopped. Okay, so now I say Moore's Law is slowing down. And
*  I think Jim, which is another way of, if he's, if it's predicting every two years and I say it's
*  slowing down, then that's another way of saying it doesn't hold anymore. And I think Jim wouldn't
*  disagree that it's slowing down because that sounds like it's things are still getting better,
*  just not as fast, which is another way of saying Moore's Law isn't working anymore.
*  It's still good for marketing, but what's your, you're not, you don't like expanding the definition
*  of Moore's Law sort of naturally. Well, it's an educator, you know,
*  it's just like modern politics. Does everybody get their own facts? Or do we have, you know,
*  Moore's Law was a crisp, you know, a more, it was Carver Mead looked at his,
*  Moore's conversations, a drawing on a log, log scale, a straight line. And that's what the
*  definition of Moore's Law is. There's this other, what Intel did for a while, interestingly,
*  before Jim joined them, they said, oh no, Moore's Law isn't the number of doubling,
*  isn't really doubling transistors every two years. Moore's Law is the cost of the individual
*  transistor going down, cutting in half every two years. Now that's not what he said, but they
*  reinterpreted it because they believed that the cost of transistors was continuing to drop, even
*  if they couldn't get twice as many ships. Many people in industry have told me that's not true
*  anymore. That basically in more recent technologies that got more complicated,
*  the actual cost of transistor went up. So even the corollary might not be true, but certainly,
*  you know, Moore's Law, that was the beauty of Moore's Law. It was a very simple, it's like
*  equals MC squared, right? It was like, wow, what an amazing prediction. It's so easy to understand.
*  The implications are amazing. And that's why it was so famous as a prediction. And this
*  reinterpretation of what it meant and changing is revisionist history. And I'd be happy.
*  And they're not claiming there's a new Moore's Law. They're not saying, by the way, instead of
*  every two years, it's every three years. I don't think they want to say that. I think what's going
*  to happen is new technology emissions, each one is getting a little bit slower. So it is slowing
*  down, the improvements won't be as great. And that's why we need to do new things.
*  Yeah, I don't like that the idea of Moore's Law is tied up with marketing. It would be nice if-
*  Whether it's marketing or it's, well, it could be affecting business, but it could also be
*  affecting the imagination of engineers. If Intel employees actually believe that we're frozen in
*  2019, well, that would be bad for Intel. Not just Intel, but everybody. Moore's Law is inspiring
*  to everybody. But what's happening right now, talking to people who have working in national
*  offices and stuff like that, a lot of the computer science community is unaware that this is going
*  on. That we are in an era that's going to need radical change at lower levels that could affect
*  the whole software stack. If you're using cloud stuff and the servers that you get next year are
*  basically only a little bit faster than the servers you got this year, you need to know that. And we
*  need to start innovating to start delivering on it. If you're counting on your software,
*  you're software going to have a lot more features, assuming the computers are going to get faster.
*  That's not true. So are you going to have to start making your software stack more efficient? Are you
*  going to have to start learning about machine learning? So it's a warning or call for arms that
*  the world is changing right now. And a lot of computer science PhDs are unaware of that.
*  So a way to try and get their attention is to say that Moore's Law is slowing down and that's going
*  to affect your assumptions. And we're trying to get the word out. And when companies like TSMC
*  and Intel say, oh, no, no, no, Moore's Law is fine, then people think, okay, I don't have to
*  change my behavior. I'll just get the next servers. And if they start doing measurements,
*  they'll realize what's going on. It'd be nice to have some transparency and metrics for the lay
*  person to be able to know if computers are getting faster and not to forget. Yeah, there are a bunch
*  of most people kind of use clock rate as a measure of performance. It's not a perfect one. But if
*  you've noticed, clock rates are more or less the same as they were five years ago. Computers are
*  a little better than they aren't. They haven't made zero progress, but they've made small progress. So
*  there's some indications out there. And then our behavior, right? Nobody buys the next laptop
*  because it's so much faster than the laptop from the past. For cell phones, I think, I don't know
*  why people buy new cell phones, you know, because of the new ones announced. The cameras are better,
*  but that's kind of domain specific, right? They're putting special purpose hardware to make
*  the processing of images go much better. So that's the way they're doing it. They're not
*  particularly, it's not that the ARM processor in there is twice as fast as much as they've
*  added accelerators to help the experience of the phone. Can we talk a little bit about one other
*  exciting space, arguably the same level of impact as your work with risk is
*  RAID. In 1988, you co-authored a paper, A Case for Redundant Arrays of Inexpensive Disks, hence
*  RAID. So that's where you introduced the idea of RAID. Incredible that that little, I mean,
*  little, that paper kind of had this ripple effect and had a really revolutionary effect.
*  So first, what is RAID? So this is work I did with my colleague, Randy Katz, and a star graduate
*  student, Garth Gibson. So we had just done the fourth generation RISC project. And Randy Katz,
*  which had an early Apple Macintosh computer, at this time, everything was done with floppy disks.
*  Which are old technologies that could store things that didn't have much capacity. And you had to
*  get any work done, you're always sticking your little floppy disk in and out because they didn't
*  have much capacity. But they started building what are called hard disk drives, which is magnetic
*  material that can remember information storage for the Mac. And Randy asked the question when he saw
*  this disk next to his Mac, gee, these are brand new small things. Before that, for the big computers,
*  the disk would be the size of washing machines. And here's something the size of a kind of the
*  size of a book or so. He says, I wonder what we could do with that. Well, Randy was involved in
*  the fourth generation RISC project here at Berklin in the 80s. So we figured out a way how to make
*  the computation part, the processor part go a lot faster. But what about the storage part?
*  Can we do something to make it faster? So we hit upon the idea of taking a lot of these disks
*  developed for personal computers and Macintoshes and putting many of them together instead of one
*  of these washing machine size things. And so we wrote the first draft of the paper and we'd have
*  40 of these little PC disks instead of one of these washing machine size things. And they would
*  be much cheaper because they're made for PCs and they could actually kind of be faster because
*  there was 40 of them rather than one of them. And so we wrote a paper like that and sent it to one
*  of our former Berkeley students at IBM. And he said, well, this is all great and good, but what
*  about the reliability of these things? Now you have 40 of these devices, each of which are kind
*  of PC quality. So they're not as good as these IBM washing machines. IBM dominated the storage
*  industries. So the reliability is going to be awful. And so when we calculated it out, instead
*  of it breaking on average once a year, it would break every two weeks. So we thought about the
*  idea and said, well, we got to address the reliability. So we did it originally for performance,
*  but we had to do reliability. So the name redundant array of inexpensive disks is array of these
*  disks, inexpensive like for PCs, but we have extra copies. So if one breaks, we won't lose
*  all the information. We'll have enough redundancy that we could let some break and we can still
*  preserve the information. So the name is an array of inexpensive disks. This is a collection of
*  these PCs and the R part of the name was the redundancy. So they'd be reliable. And it turns
*  out if you put a modest number of extra disks in one of these arrays, it could actually not only be
*  as faster and cheaper than one of these washing machine disks, it could be actually more reliable
*  because you could have a couple of breaks even with these cheap disks, whereas one failure with
*  the washing machine thing would knock it out. Did you have a sense just like with risk that in the
*  30 years that followed, RAID would take over as a mechanism for storage?
*  I'd say I think I'm naturally an optimist, but I thought our ideas were right. I thought kind of
*  like Morris Law, it seemed to me if you looked at the history of the disk drives, they went from
*  washing machine size things and they were getting smaller and smaller and the volumes were with the
*  smaller disk drives because that's where the PCs were. So we thought that was a technological trend
*  that disk drives, the volume of disk drives was going to be getting smaller and smaller devices,
*  which were true. They were the size of a, I don't know, eight inches diameter, then five inches,
*  then three inches diameters. And so that it made sense to figure out how to deal things with an
*  array of disks. So I think it was one of those things where logically we think the technological
*  forces were on our side that it made sense. So we expected it to catch on, but there was that same
*  kind of business question. IBM was the big pusher of these disk drives. In the real world,
*  where the technical advantage get turned into a business advantage or not, it proved to be true.
*  We thought we were sound technically and it was unclear whether the business side, but we kind of,
*  as academics, we believed that technology should win and it did. And if you look at those 30 years,
*  just from your perspective, are there interesting developments in the space of storage
*  that have happened in that time? Yeah, the big thing that happened, well, the couple of things
*  that happened, what we did had a modest amount of storage. So as redundancy, as people built bigger
*  and bigger storage systems, they've added more redundancy so they could add more failures.
*  And the biggest thing that happened in storage is for decades it was based on things physically
*  spinning called hard disk drives. We used to turn on your computer and it would make a noise.
*  What that noise was, was the disk drives spinning and they were rotating at like 60 revolutions per
*  second. And it's like, if you remember the vinyl records, if you've ever seen those, that's what it
*  looked like. And there was like a needle like on a vinyl record that was reading it. So the big drive
*  change is switching that over to a semiconductor technology called flash. So within the last,
*  I'd say about decade is increasing fraction of all the computers in the world are using semiconductor
*  for storage, the flash drive, instead of being magnetic, their optical, their semiconductor
*  writing of information very densely. And that's been a huge difference. So all the cell phones
*  in the world use flash. Most of the laptops use flash. All the embedded devices use flash instead
*  of storage. Still in the cloud, magnetic disks are more economical than flash, but they use both in
*  the cloud. So it's been a huge change in the storage industry. The switching from primarily
*  disk to be primarily semiconductor. For the individual disk, but still the RAID mechanism
*  applies to those different kinds of disks. Yes. The people will still use RAID ideas because it's
*  kind of what's different, kind of interesting kind of psychologically, if you think about it,
*  people have always worried about the reliability of computing since the earliest days. So kind of,
*  but if we're talking about computation, if your computer makes a mistake and the computer says,
*  the computer has ways to check and say, oh, we screwed up, we made a mistake. What happens is
*  that program that was running, you have to redo it, which is a hassle. For storage, if you've
*  sent important information away and it loses that information, you go nuts. This is the worst,
*  oh my God. So if you have a laptop and you're not backing it up on the cloud or something like this
*  and your disk drive breaks, which it can do, you'll lose all that information and you just
*  go crazy. So the importance of reliability for storage is tremendously higher than the importance
*  of reliability for computation because of the consequences of it. So yes, so RAID ideas are
*  still very popular even with the switch of the technology. Although flash drives are more reliable,
*  if you're not doing anything like backing it up to get some redundancy so they handle it,
*  you're taking great risks. You said that for you and possibly for many others, teaching and research
*  don't conflict with each other, as one might suspect, and in fact, they kind of complement
*  each other. So maybe a question I have is, how has teaching helped you in your research or just in your
*  entirety as a person who both teaches and does research and just thinks and creates new ideas
*  in this world? Yes, I think what happens is when you're a college student, you know there's this
*  kind of tenure system in doing research. So kind of this model that is popular in America, I think
*  America really made it happen, is we can attract these really great faculty to research universities
*  because they get to do research as well as teach. And that, especially in fast moving fields,
*  this means people are up to date and they're teaching those kinds of things. So, but when you
*  run into a really bad professor, a really bad teacher, I think the students think, well this guy
*  must be a great researcher because why else could he be here? So, after 40 years at Berkeley, we had
*  a retirement party and I got a chance to reflect and I looked back at some things. That is not my
*  experience. I saw a photograph of five of us in the department who won the Distinguished Teaching
*  Award from campus. A very high honor, you know, I've got one of those, one of the highest honors.
*  So there are five of us on that picture. There's Manuel Blum, Richard Karp, me, Randy Cass, and
*  John Osterhout, contemporaries of mine. I mentioned Randy already. All of us are in the National
*  Academy of Engineering. We've all run the Distinguished Teaching Award. Blum, Karp, and I
*  are all have touring awards. Touring awards, right. You know, the highest award in computing.
*  So, that's the opposite, right? What happens is they're highly correlated. So, probably,
*  the other way to think of it, if you're very successful people, maybe successful at everything
*  they do, it's not an either or. But it's an interesting question whether specifically,
*  that's probably true, but specifically for teaching. If there's something in teaching that,
*  it's the Richard Feynman idea, is there something about teaching that actually makes your research
*  makes you think deeper and more outside the box and more successful?
*  Absolutely. I was going to bring up Feynman. I mean, he criticized the Institute of Advanced
*  Studies. So, the Institute of Advanced Studies was this thing that was created near Princeton
*  where Einstein and all these smart people went. And when he was invited, he thought it was a
*  terrible idea. This is a university. It was supposed to be heaven, right? A university without any
*  teaching. But he thought it was a mistake. It's getting up in the classroom and having to explain
*  things to students and having them ask questions like, well, why is that true? Makes you stop and
*  think. So, he thought, and I agree, I think that interaction between a great research university
*  and having students with bright young minds asking hard questions the whole time is synergistic.
*  And a university without teaching wouldn't be as vital and exciting a place. And I think it helps
*  stimulate the research. Another romanticized question, but what's your favorite concept or
*  idea to teach? What inspires you or you see inspire the students? Is there something that
*  pops to mind or puts the fear of God in them? I don't know, whichever is most effective.
*  I mean, in general, I think people are surprised. I've seen a lot of people who don't think they
*  like teaching come give guest lectures or teach a course and get hooked on seeing the lights turn
*  on, right? You can explain something to people that they don't understand and suddenly they get
*  something that's important and difficult and just seeing the lights turn on is a real satisfaction
*  there. I don't think there's any specific example of that. It's just the general joy of seeing them.
*  I have to talk about this because I've wrestled. I do martial arts. Of course, I love wrestling.
*  I'm Russian. I've talked to Dan Gable on the podcast. Dan Gable is my era kind of guy.
*  You wrestled at UCLA among many other things you've done in your life, competitively in sports and
*  science and so on. You've wrestled, maybe again, continuing the romanticized questions, but
*  what have you learned about life and maybe even science from wrestling or from?
*  In fact, I wrestled at UCLA, but also at El Camino Community College. Just right now,
*  in the state of California, we were state champions at El Camino. In fact, I was talking to my mom
*  and I got into UCLA, but I decided to go to the community college, which is much harder to go to
*  UCLA than the community college. I asked, why did I make the decision? Because I thought it was
*  because of my girlfriend. She said, well, it was the girlfriend and you thought the wrestling team
*  was really good. We were right. We had a great wrestling team. We actually wrestled against UCLA
*  at a tournament and we beat UCLA as a community college, which is just freshmen and sophomores.
*  And part of the reason I brought this up is they've invited me back at El Camino to give
*  a lecture next month. And so, my friend who was on the wrestling team that we're still together,
*  we're right now reaching out to other members of the wrestling team if we can get together for a
*  reunion. But in terms of me, it was a huge difference. The age cut off, it was December 1st
*  and so I was almost always the youngest person in my class. And I matured later on, you know,
*  our family matured later. So I was almost always the smallest guy. So, you know, I took kind of
*  nerdy courses, but I was wrestling. So wrestling was huge for my, you know, self-confidence in high
*  school. And then, you know, I kind of got bigger at El Camino and in college. And so I had this kind
*  of physical self-confidence and it's translated into research self-confidence. And also kind of,
*  I've had this feeling even today in my 70s, you know, if something going on in the streets that
*  is bad physically, I'm not going to ignore it, right? I'm going to stand up and try and
*  straighten that out. And that kind of confidence just carries through the entirety of your life.
*  Yeah. And the same thing happens intellectually. If there's something going on where people are
*  saying something that's not true, I feel it's my job to stand up just like I would in the street.
*  If there's something going on, somebody attacking some woman or something, I'm not standing by and
*  letting that get away. So I feel it's my job to stand up. So it's kind of ironically translates.
*  The other things that turned out for both, I had really great college and high school coaches and
*  they believed even though wrestling is an individual sport, that we would be more successful
*  as a team if we bonded together, do things that we would support each other rather than everybody,
*  you know, in wrestling it's a one-on-one and you could be everybody's on their own, but he felt if
*  we bonded as a team, we'd succeed. So I kind of picked up those skills of how to form successful
*  teams and how to, from wrestling. And so I think one of, most people would say one of my strengths
*  is I can create teams of faculty, large teams of faculty, grad students, pull all together for a
*  common goal and, you know, and often be successful at it. But I got both of those things from
*  wrestling. Also, I think I heard this line about if people are in kind of, you know, collision,
*  you know, sports with physical contact like wrestling or football and stuff like that,
*  people are a little bit more, you know, assertive or something. And so I think that also comes
*  through is, you know, I didn't shy away from the risk-sys debates, you know, I enjoyed taking on
*  the arguments and stuff like that. So it was, I'm really glad I did wrestling. I think it was really
*  good for my self-image and I learned a lot from it. So I think that's, you know, sports done well,
*  you know, there's really lots of positives you can take about it, leadership,
*  you know, how to form teams and how to be successful. So we've talked about metrics a lot.
*  There's a really cool, in terms of bench press and weightlifting, pound years metric that you've
*  developed that we don't have time to talk about, but it's a really cool one that people should look
*  into. It's rethinking the way we think about metrics and weightlifting. But let me talk about
*  metrics more broadly, since that appeals to you in all forms. Let's look at the most ridiculous,
*  the biggest question of the meaning of life. If you were to try to put metrics on a life well lived,
*  what would those metrics be? Yeah, a friend of mine, Randy Katz said this, he said,
*  you know, when it's time to sign off, the measure isn't the number of zeros in your bank account,
*  it's the number of inches in the obituary in the New York Times, as he said it. I think, you know,
*  having, you know, this is a cliche, is that people don't die wishing they'd spent more time in the
*  office, right? As I reflect upon my career, there have been, you know, a half a dozen, a dozen things
*  say I've been proud of. A lot of them aren't papers or scientific results. Certainly my family,
*  my wife, we've been married more than 50 years, kids and grandkids, that's really precious.
*  Education things I've done, I'm very proud of, you know, books and courses. I did some help
*  with underrepresented groups that was effective. So it was interesting to see what were the things
*  I reflected. You know, I had hundreds of papers, but some of them were the papers,
*  like the risk and rate stuff that I'm proud of, but a lot of them were or not those things. So
*  people who are just spend their lives, you know, going after the dollars or going after all the
*  papers in the world, you know, that's probably not the things that are afterwards you're going to
*  care about. When I was a, just when I got the offer from Berkeley, but before I showed up,
*  I read a book where they interviewed a lot of people in all works of life. And what I got out
*  of that book was the people who felt good about what they did was the people who affected people,
*  as opposed to things that were more transitory. So I came into this job,
*  assuming that it wasn't going to be the papers, it was going to be relationships with the people
*  over time that I would value. And that was a correct assessment, right? It's the people you
*  work with, the people you can influence, the people you can help is the things that you feel
*  good about towards into your career. It's not the stuff that's more transitory.
*  I don't think there's a better way to end it than talking about your family,
*  the over 50 years of being married to your childhood sweetheart.
*  What I think I could add is how to, when you tell people you've been married 50 years,
*  they want to know why. How? Why?
*  I can tell you the nine magic words that you need to say to your partner to keep a good relationship.
*  And the nine magic words are, I was wrong. You were right. I love you. Okay. And you got to say
*  all nine. You can't say, I was wrong. You were right. You're a jerk. You know, you can't say that.
*  So yeah, I freely acknowledging that you made a mistake. The other person was right. And that
*  you love them really gets over a lot of bumps in the road. So that's what I pass along.
*  Beautifully put. David, it is a huge honor. Thank you so much for the book you've written,
*  for the research you've done, for changing the world. Thank you for talking today.
*  Thanks for the interview.
*  Thanks for listening to this conversation with David Patterson. And thank you to our sponsors,
*  The Jordan Harbinger Show and Cash App. Please consider supporting this podcast by going to
*  JordanHarbinger.com slash Lex and downloading Cash App and using code LexPodcast. Click the links,
*  buy the stuff. It's the best way to support this podcast and the journey I'm on.
*  If you enjoy this thing, subscribe on YouTube, review it with five stars and have a podcast,
*  support it on Patreon or connect with me on Twitter at Lex Friedman spelled without the E.
*  Try to figure out how to do that. It's just F R I D M A N. And now let me leave you with some words
*  from Henry David Thoreau. Our life is fitted away by detail. Simplify, simplify.
*  Thank you for listening and hope to see you next time.
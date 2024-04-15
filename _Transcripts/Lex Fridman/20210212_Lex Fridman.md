---
Date Generated: April 13, 2024
Transcription Model: whisper medium 20231117
Length: 10759s
Video Keywords: ['agi', 'ai', 'ai podcast', 'artificial intelligence', 'artificial intelligence podcast', 'brendan eich', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'mit ai']
Video Views: 831542
Video Rating: None
---

# Brendan Eich: JavaScript, Firefox, Mozilla, and Brave | Lex Fridman Podcast #160
**Lex Fridman:** [February 12, 2021](https://www.youtube.com/watch?v=krB0enBeSiE)
*  The following is a conversation with Brendan Eich,
*  creator of the JavaScript programming language,
*  co-founder of Mozilla, which created the Firefox browser,
*  and now co-founder and CEO of Brave Software,
*  which has created the Brave browser.
*  Each of these are revolutionary technologies.
*  JavaScript is one of the most widely used
*  and impactful programming languages in the world.
*  Firefox pioneered many browser ideas that we love today,
*  or even take for granted today.
*  And Brave is looking to revolutionize not only the browser,
*  but content creation online and the nature of the internet
*  to make it fundamentally about respecting people's control over their data.
*  Quick mention of our sponsors.
*  The Jordan Harbinger Show,
*  Sound Basket Meal Delivery Service,
*  Better Help Online Therapy,
*  and 8 Sleep Self-Cleaning Mattress.
*  Click the sponsor links to get a discount and to support this podcast.
*  As a side note, let me say that there's a tension between theory and engineering
*  that I've been thinking a lot about.
*  I tweeted something like,
*  Good execution is more important than a good idea, but one helps the other.
*  I think the wording of that sucks, but what I mean is a good idea is a must.
*  But in my experience, good ideas are in abundance.
*  Good execution, on the other hand, is rare.
*  I think some mix of good timing, good idea, and good execution is essential.
*  Getting that mix right is tough.
*  And Brendan, somehow, multiple times in his career, did just that.
*  I'm starting to believe it's more art than science,
*  like most interesting things in life.
*  If you enjoy this thing, subscribe on YouTube,
*  review an Apple podcast, follow on Spotify,
*  support on Patreon, or connect with me on Twitter at Lex Friedman.
*  And now, here's my conversation with Brendan Icke.
*  When did you first fall in love with programming?
*  I didn't program a lot when I was in high school,
*  but I had a friend who had a Commodore PET.
*  And after we saw Star Wars, he said,
*  Hey, let's make a basic program that does the Death Star trench run.
*  And it was just simple 2D graphics.
*  And I didn't know what I was doing,
*  so I just helped him out on the math and stuff like that.
*  I was a math and science kid.
*  I was really into the HP calculators of the early mid-70s.
*  These were the RPN.
*  They were really strongly built.
*  It's all right, goldfinger.
*  Instead of gold, divinely heavy.
*  There's probably some gold in them too, gold metalization.
*  But they were awesome calculators,
*  and they had all the scientific functions,
*  so I was really into that.
*  So I aimed towards physics.
*  I was a little late for the 20th century golden age,
*  and I read a lot of science fiction.
*  So I was like, yeah, it's on the typewriters and warp drives.
*  And physics was not going to get there quickly.
*  And I started hacking on computers while I was studying physics
*  as an undergraduate at Santa Clara University.
*  And I dodged the Fortran bullet because I was in the science department
*  instead of the engineering department,
*  where they still did Fortran card decks.
*  I think they had an autocollator.
*  But we were using Pascal,
*  and I got one of the first portable C compilers
*  ports to the deck mini computers we were using.
*  And I fell in love with programming just based on
*  procedural abstraction, Pascal,
*  what now would be considered old school structured programming from the 70s.
*  Niklaus Wirth, the creator of Pascal,
*  was a good writer and a good pedagogue.
*  He always at ETH would do these courses where it's like build your own computer,
*  build your own compiler, build your own operating system.
*  From scratch.
*  Yeah, kind of.
*  And I know some people who are grad students under him
*  said he would torture the students with things like this custom email system
*  that had 25 word limit and things like that.
*  I unfortunately dodged both the Pascal and the Fortran bullets.
*  Could you maybe linger on the Pascal?
*  What kind of programming language was it?
*  What is it reminiscent of today?
*  Because it sounds like it may have had an impact on your own trajectory.
*  Yeah, it was in the Algo family.
*  And Algo was the big successful language design and compiler project in the 60s.
*  It had a successor called Algo 68, which was ambitious but not as successful.
*  But Pascal was kind of wordy procedures and functions language.
*  It distinguished between functions with return of value and procedures which don't,
*  which just compute.
*  And you could say that whole Algo family went into Ada.
*  Pascal had a second life thanks to Borland with Turbo Pascal, which was hugely successful.
*  I think in large part due to Anders Halsberg who then went to Microsoft and did C Sharp
*  and done that with his team there and has done really well doing TypeScript, TypeJavaScript.
*  So yeah, there's a lineage here.
*  But I was also interested in C and Unix by the time I was an undergrad
*  because people were bringing Unix up on all sorts of hardware.
*  I had some friends who were doing their own wire wrap computers, 6820 maybe.
*  And I was wire wrapping for my engineering course,
*  6809 or something simpler, building a computer on a board.
*  And I wanted to build a more ambitious one and port Unix to it, but I picked the wrong
*  processor.
*  I picked the National Semiconductor NS16032, which was this amazing CISC,
*  complex instruction set computer.
*  And not the reduced instructions that computers that were just being contemplated into the mid-80s.
*  And RISC ultimately won out.
*  RISC won in some ways.
*  You have both.
*  Now you have these superscalar architectures where
*  Intel has kept probably too much backward compatibility at the instruction level.
*  But there's a front end that parses that into these wide internal instructions.
*  So the very long instruction word research that was also interesting at the time became
*  the microarchitecture inside the backward compatible Intel.
*  But I picked the National Semi chip and it never got made successfully.
*  It was full of bugs and I never could have brought it up.
*  But I went out of physics after three years into math computer science.
*  And like I said, I did it because I was being childlike and naive about physics.
*  And I thought, meanwhile, the Valley is go-go for computers.
*  The Apple II, the PC, the Intel 8086, 8088 based PC.
*  The IBM gave Microsoft the future for in a somewhat fishy deal.
*  So it was wide open in the computing space, but in physics,
*  you were as optimistic about physics as...
*  No, I mean, I was one of three brothers who were all in the same grade.
*  I have a twin and a younger brother who skipped second grade and was with us the whole time after that.
*  And he went on.
*  He actually studied under Kip Thorne at Caltech.
*  But he also ended up at software.
*  Does it make you sad that theoretical physics, even with string theory,
*  hasn't really had any foundational breakthroughs in the latter part of the 20th century?
*  Yeah. In fact, I'd say the problem is theory over experiment.
*  I would say we need more Aristotle and less Plato.
*  Mathematics is not all physical.
*  There are lots of mathematics that cannot be realized as far as I know in this world.
*  So to understand the world, you need to do experiments.
*  You need to not just dream up inductive theories that could have lots of alternative theories
*  competing with them with no way to decide between them except aesthetics,
*  which is not a good guide in my opinion.
*  I don't know if you are friends with or have a relationship with Elon Musk.
*  In terms of what you would love to see our society investing in building up,
*  is it closer to Elon or is it closer to Feynman and Einstein and those?
*  Those gentlemen are no longer with us.
*  And I think that's noticed.
*  So like I said, the real glory days of physics, the famous pictures from Germany
*  before the second war were just a fantastic assembly of brains, Schrodinger and Einstein.
*  And physics, I think, took a wrong turn that maybe all of, I would say,
*  Western science took in going for models over reality.
*  You see this in all sorts of fields.
*  Now, we can build models that are very predictive and generative and then we build
*  actual devices or semiconductors, things like that.
*  That's good. I'm not dismissing that.
*  We need good models.
*  We need to experiment and prove them and test them.
*  But the problem I've seen in physics, which you see certainly in economics,
*  the dismal science, and you see surprisingly in other so-called hard sciences is models that
*  don't really have to be tested against reality.
*  They can instead become policy tools or they can become, like I said,
*  one of a large family of alternate theories that could be as predictive,
*  but nobody's doing the winnowing out.
*  That's such an interesting tension in society.
*  You see this in even the softer sciences, which I have a deep love for, like psychology.
*  You see this in epidemiology, not with the virus.
*  Absolutely.
*  It's this tension of how much of the world can we understand through just a beautifully fit model?
*  And then at the same time, my main work is in machine learning
*  where it's like there is no provable thing usually.
*  It's all about just getting the right data set and getting tricks and so on.
*  And there's this tension even in my own soul of like I grew up on theoretical computer science.
*  I loved approximation algorithms, all of that different complexity classes, just these little
*  puzzles. I mean, I don't know.
*  To you as somebody who was in math and computer science and then ended up going into places where
*  you engineered some of the most impactful things in this world, do you see the P versus NP,
*  all that whole space as interesting at all?
*  It's not that useful in practice.
*  People are using it with sort of crypto analysis or asymptotic arguments about,
*  can we have a quantum resistant crypto algorithm, things like that, which may not be practical.
*  If you follow Mikhail Diakonov or Gil Kalai, there are big questions about how quantum computing will
*  scale up, how practical it will be.
*  Is that something that you think about quantum computing?
*  Not for a spare time.
*  Like you said, I'm not using this kind of computer science in practice because
*  almost everything now is engineering and finding ways to get computers to be more useful for people,
*  which goes from design problems, which are really kind of an art.
*  Like you said, anything you can't automate is an art.
*  Well, we can have machine learning, composed music, and it can imitate.
*  You can train it and it can sound kind of decent, but maybe lacking that genus aqua.
*  But user interface still, I think, requires human art.
*  Speaking of things that didn't follow a perfect theory and model, JavaScript,
*  so there's two things.
*  One had an impact on the world at a huge scale, obviously, and it's also still is one of
*  probably the most popular programming language in the world.
*  So can we go back to the origin story?
*  Can you tell the story of how JavaScript was created?
*  Yeah, I was at Silicon Graphics after graduate school for seven years,
*  and it got to be big and successful and divisionalized and political.
*  And I thought kind of boring.
*  And a friend who'd been there went to one of the last of the super companies,
*  super startups in the early 90s.
*  There were several, I suppose General Magic was a little after that around the same time.
*  But Micro Unity was that company that I went to.
*  And it was because my friend, Jeff Weinstein, had gone there from Silicon Graphics.
*  He recruited me and Micro Unity was doing everything.
*  So this was like the ultimate sort of pretend grad school.
*  It was doing a new fab, new semiconductor process.
*  It was doing new analog and digital circuits on the same very large but not wafer scale chip.
*  Originally, it was five centimeters on a side.
*  It was really hot too.
*  So I needed a water cooler.
*  It was a Craig Hiller.
*  And then they shrunk it and they tried to do a home sort of media processor that was
*  essentially a barrel processor.
*  But you could think of trying to do all the things that we now see in modern architectures
*  with short vector instructions and sort of wide instructions for multiple issue.
*  And doing a lot of the stuff in software because the second iteration,
*  the set-top box, was really for avoiding the cost to the cable company of rolling the trucks out
*  to replace your garbage General Atlantic set-top box with a slightly newer, less garbagey one.
*  So if you could have software gradable set-top boxes, the cable companies
*  thought they could save a lot of money and add features.
*  As an assembly?
*  Or which level of the software?
*  It was like we were writing in, we were using GCC.
*  We were writing C++ and C.
*  Somebody I worked with there, really a very smart guy, hired from a sort of Wall Street
*  hotshot programming consultancy, did his own hardware design as well as software.
*  We were working on how to make not only short vector units but general bit shufflers and
*  permuters so you could do things like crypto algorithms efficiently.
*  And you could do demodulation of the cable complex quadrature amplitude modulated signal.
*  So you're basically taking A to D converters, dumping things in buffers,
*  and then doing the rest in software.
*  All the framing and the Reed Solomon and Viterbi and all that error correction.
*  So that was really great learning experience, but it was not going to work.
*  It was doing too many risky things at once.
*  Jim Clark said to me when I hopped to Netscape after three years at MicroUnity, he said,
*  oh yeah, you do 10 things each, one in 10 odds, it's going to be one in 10 billion.
*  The multiplication principle.
*  So Netscape was already a rocket and I passed the chance to go there in 1994.
*  I knew the founders because I worked at SGI Clark's company.
*  Could you pause for a second?
*  Sure.
*  Netscape, when was the launch of this rocket?
*  1994.
*  94 was the launch of Netscape?
*  And I went there in early 95 in April.
*  Okay. So you said you missed the launch.
*  Well, I missed the first floor employment opportunity, but the IPO was August 1995.
*  So I was there for that.
*  How obvious was it that Netscape was world changing?
*  Was Netscape one of the first big browsers?
*  Yes. So when I was at MicroUnity still in 93, we saw a browser called Mosaic.
*  And up till then we'd used email and we'd used Usenet, the NNTP protocol.
*  We'd use newsreaders.
*  We used FTP.
*  We used all these old internet protocols, all relying on the DNS and TCPIP and UDP for that
*  matter. When I was at Silicon Graphics, we brought up the whole stack, right?
*  We had to discover how to find the Ethernet addresses on your network and then find IP
*  addresses for them, ARP protocol, all that stuff.
*  And it was great because nobody knew in the 80s what was going to win.
*  All the proprietary stacks like IBM, SNA and DECnet and all these other protocols were saying,
*  we're going to do it or it's going to be heterogeneous future.
*  And instead it was, you know, Berkeley Unix and the TCPIP stack that dated back to the ARPANET
*  that won. And I think we knew it. We all knew it at SGI, but the salespeople didn't.
*  And so they kept trying to get multiple network stacks interoperating.
*  But in the end, it won. And so that was the internet and it was email and texty.
*  And it was used very texty. And then Tim Berners-Lee did his thing,
*  but I don't think I was paying attention. And I think the date when he first did it,
*  or when he wrote the famous emails, was pushed back to 89.
*  But I noticed a mosaic in 93 because one of the things that Mark Andreessen
*  and Eric Bina did at NCSA was they innovated on the early HTML standard.
*  In particular, Mark sent this email saying, hey everybody, we think you should be able to
*  put an image in a page. And you know when he sent that Eric Bina had already written the code.
*  And, you know, I talked to Tim Berners-Lee more recently, just a few years ago,
*  and he was like, oh, we had another way of doing it. And it didn't work out because Mark shipped
*  his in mosaic. And this convinced me of several things. One, the internet meant there was a huge
*  first mover advantage and being fast, getting on first mattered a lot. And so, you know, Richard
*  Gabriel scheme and poetry fame has written about this. The famous...
*  Poetry? What's poetry?
*  Well, he's a poet. Richard's a poet.
*  Oh, actual poetry. He's talking about some kind of something.
*  No, no. I mean, he's the founder of Lucid, which is where Jamie Zawinski worked before Netscape.
*  And Lucid was doing compilers and Lucid Emacs, which was a fork of Emacs,
*  famously Jamie fighting against Richard Stallman, Stalmax. And so Richard Gabriel,
*  very, very brainy computer guy, but also a poet. But he wrote a nice essay that gets abused all the
*  time. In fact, Jamie's put a kind of warning in front of his version of it on his site,
*  JWC.org, called Worse is Better. And this is about survival advantage of software in the network
*  world, in my opinion. It's about Unix. It started out being framed as Unix and Lisp, good news, bad
*  news, because all the Lisp people, the MIT people were like, oh, you know, the crown jewel scheme,
*  this Fabergé egg or common list, this giant cathedral, of course we're going to win. This
*  is civilization. And those farmers in New Jersey, to borrow from the Sopranos, those
*  hicks down at Bell Labs, there's nothing to sound there. It's all hacking. Well, guess what won?
*  Wow. So you're saying this is a fundamental principle of the internet is moving fast wins.
*  You could say in almost any network system, like in biological evolution, you see successful,
*  allele-sweet populations and they don't always have, they aren't free of flaws,
*  heterozygous advantage. You can get both parents give you the gene variant and you get sickle cell
*  anemia. But if one of them does, you're more resistant to malaria. And so this isn't a
*  beautiful process except at large scale. And then you realize that because it moves fast and can
*  adapt, it can win. And people still struggle with this. I used to struggle with this because
*  JavaScript was done in such a hurry and the force of web compatibility meant early mistakes couldn't
*  be fixed. And even the standards process injected new mistakes, as it will. But often standards
*  bodies go back and making compatible changes. You can't do that with the web. It's more like,
*  again, like biology, you preserve what still works. You don't want to break ATP metabolism
*  or whatever. So you have to kind of resign yourself to the reality of worse is better
*  being enshrined in actual design points you might not like. And that happened with JavaScript. And
*  I'm way over it, but it also, I think was a huge advantage. That's why JavaScript has kind of swept
*  a lot of programming domains. People will say, oh, it's not because of merit. Well, you're right.
*  But we also improved it over time in the standards body. I spent 20 years doing that.
*  And you don't get that choice. It's like, I'm not saying that that was the best language. I'm just
*  saying that was the right time to do it. And I like to say the alternative was not to do it. I
*  could have told Netscape, I can't do this. It's too rushed. And it would have been visual basic
*  script. And it would have been bad. So that's a good way to present the alternative. But so
*  it was a Netscape and you have written it in how many days and why was it only that many days? And
*  what was the goal and underlying principles in your mind? So the whole, I'm sort of describing
*  worse is better in a frenetic way because it fit the model of Netscape. When it was known that Jim
*  Clark and Mark and Jason were founding Netscape and they did the first release in 1994, that browser
*  took over from Mosaic. In fact, that's why Mozilla is called that. It's the Mosaic killer. It's like
*  the giant monster that kills Mosaic. It's awesome. And they knew that, you know, it wasn't that,
*  again, it's not like you're doing advanced scientific research that is changing the world.
*  You're more like taking down the last iteration in the browser Mark did, which had images
*  and other affordances before he stopped working on it. And you're making Netscape, the new thing
*  that has images, plugins, which was the way to do video back in the day. It had something that's
*  kind of died now for tiled windows called frames and frame sets. It had HTML tables. That was new.
*  Eric Bina did tables in Netscape 1.1. So when I got there, they were heading toward IPO. Clark
*  wanted to IPO early. I think his instinct was right. And that kicked off the whole dot com era.
*  Right. There was a recession in the US in 91. You can see old law and order reruns where they talk
*  about the recession and how hard it's hitting New Yorkers. And after that, Greenspan really
*  goose things at the Federal Reserve and technology had been sort of fermenting in a way that came
*  together with the internet. And Netscape made it possible to do pets.com, to do eBay, to get people
*  to recognize a URL on a billboard and then type it in when they get home. And that was huge. That
*  was so fast moving a rocket that Mark and the engineering team there thought we need to make
*  this a programmable browser, not just a document viewer, not just a video.
*  It was all HTML with images and tables and also, like you said, frames. There's no dynamic element
*  at all. Yeah. The most dynamism you get was from a plugin, which there are a few of them then.
*  Flash didn't exist at that point. It was, I think- Java Applet yet or no?
*  Well, that's the thing. We did the deal with Sun. In fact, I was recruited to go do Scheme in the
*  browser. Remember Guy Steele and Gerald Suspman's beautiful Lisp variant. I was going to do it in
*  the browser because my friends from SGI thought, hey, we like Scheme. You like Scheme. And I'm like,
*  I hardly ever use Scheme. It's not really used in industry except in sort of silos.
*  But I like it. Okay. I'll come do Scheme in the browser. I have a slide from my 2017 talk where
*  I have Bruce Wallace crawling through the duct in Die Hard. He's like, come out to the coast,
*  have a lot of fun. Come on, do Scheme in the browser. But when I got there, there was no Scheme in
*  the browser because they'd started a deal with Sun Microsystems. And my best contact there was
*  Bill Joy who I admired as a Berkeley Unix founder and Sun founder. And Bill got the idea of making
*  the browser programmable too. And so the main idea was to put the Java VM, which at that point was
*  not really easy to embed into Netscape, including the Netscape version on Windows that was still
*  most popular, which was the 16-bit Windows 3.1, which was going away. Microsoft was coming out
*  with Windows 95 and everyone was afraid they were going to do Internet Explorer, I guess,
*  two at that point, three the next year. They already bought or invested in somehow Spyglass,
*  this other company that shot out from NCSA at University of Illinois. And in fact,
*  Microsoft had tried to buy Netscape in late 94 before I got there. And I heard about this later.
*  I heard they offered way too little money. And so Jim Barksdale and Jim Clark said, get out of here,
*  but then they realized, oh, this is going to hurt us because now they're going to copy us.
*  Didn't happen right away. I'm not sure when Gates Internet Title Wave memo was written.
*  That's the famous memo he wrote when Bill Gates realized that Microsoft was going down this old
*  copy AOL path or copy CompuServe path, a project called Blackbird, presumably after the SR71.
*  I don't know. But they were going to make a dial-up service with a custom content language stack and
*  custom rendering. It wasn't the web. They could have content partners. They have a lot of money.
*  But it still wasn't to scale the web. It wasn't going to be compelling. And Gates realized this,
*  and he turned the company on a dime and they couldn't buy Netscape. Again, I'm not sure the
*  timing, so they decided to copy it. And once we realized that, everybody inside Netscape felt
*  even more urgency and more frenetic mood. And so my chance to do Scheme disappeared when the Java
*  deal started brewing. But there was still a chance to do a companion language to Java because Java
*  is a compiled language. It's evolved and improved quite a lot since then too, but it was for
*  serious advanced programmers that cost a certain salary or hourly rate. And Bill Joy observed,
*  and Mark Andreessen and I observed that in a mature stack like Microsoft, you really benefit
*  from having a scripting language like Visual Basic, which became Visual Basic Script in IE3,
*  but didn't take over and kill JavaScript, that you need two languages. One is for the
*  component writers who are higher price and more expert. And the other is for
*  scripters, certified public accountants, designers, graphic designers with some
*  programming inclination, anybody, amateurs, doesn't matter. There's a much more demotic
*  approach there for programming the components together, gluing them together. Some people say
*  duct tape language, which I don't really like. But we saw that Bill Joy and Mark Andreessen and I,
*  we saw the need for companion language. And Gleam and I, I was to call it JavaScript,
*  though I didn't like it. That was marketing's plan. Mark called it Mocha, which I liked.
*  Netscape Marketing, I think, didn't like that. So they said, oh, there's some trademark and some
*  software somewhere that uses Mocha, so we can't use that. And they tried LiveScript in August,
*  and that didn't last. And then finally, we got the trademark license in December, 1995.
*  But the work I did to prove that it could be done was important because I came in in April,
*  and even then Netscape was growing so fast that they couldn't find an open hiring requisition
*  in the client team for me. So they hired me into the server team. And I worked for a month on server
*  team on what became HTTP 1.1. So I was actually, I had done protocol work at Silicon Graphics with
*  Greg Chesson, former Bell Labs intern, grad student intern who knew all the Unix founders.
*  And Greg was very interested in taking protocols to the next level with VLSI, because he thought
*  that CPUs wouldn't scale up. He was mistaken in that, unfortunately. Moore's Law more than
*  kept up, and you have gigabit ethernet running with conventional processors. But I worked on
*  protocols at SGI, as well as Unix kernel hacking and NFS and things like that. So I came into
*  Netscape to work on the server side for a month. But I was thinking the whole time, what should
*  this language be like? Should it be easy to use? Might its syntax even be more like natural language,
*  like Hyper Talk, which is Bill Atkinson's language in Hypercard, if you've ever used
*  Hypercard on an early Mac. And I thought, well, I'd like to do that. But my management is saying,
*  make it look like Java, which looks like C from a distance. What does that mean? Is it braces?
*  We're talking about visually? Does it mean like, what is management? Do they understand what they
*  don't marketing? Didn't know. But management did. Like Rick Schell, the VP of engineering knew.
*  And we had a plan even that was, if you have this companion language, you're going to glue
*  things together between Java and JavaScript. So you're going to have commerce in memory,
*  in the heap with data types. So you're going to want some of the data types in Java to reflect
*  in the JavaScript. You're going to want the primitive types that Java unfortunately separated
*  from objects. So at least some of them number, double, let's call it in Java's terms, from the
*  C term for double precision floating point or strings or Booleans and objects. And so
*  right away there was this constraint that looking like Java meant kind of a C curly brace syntax,
*  but also some of the data types and objects. Like objects and so on. All the kind of stuff.
*  I thought it called. Comparison operator. Garbage collection. All that stuff. Yeah.
*  Even the bitwise operators and the shift operators, including the unsigned right shift,
*  which Java had because it didn't have unsigned integer types. It said if you want to do unsigned
*  operations, use an operator. And that turned out to be important much later. I'll tell that story
*  five times. But JavaScript inherited a set of operators, the expression grammar, the statement
*  grammar up to a point from Java. But I wanted a functional language. I wanted scheme, a little
*  bit of scheme, even though it wasn't as clean as scheme. You had a love for scheme and list,
*  that functional language. Yes. I wanted first class functions because I saw the need for callbacks
*  in the browser where it's a single threaded program. All the early browsers were single
*  threaded and it's the right model for users. Most users weren't ready for mutual exclusion and
*  threading. So in a single threaded world, you cannot block the user interface. So you have to
*  use a callback and run later. And without getting too fancy and trying to capture the continuation
*  like call CC does in scheme, I thought I'll just make it easy to have fun arcs, first class
*  functions you pass downward and it can call back, it can be called back. And Java didn't have that
*  at the time. It took forever to get proper first class functions, lambdas now into Java, Java 7
*  or 8, I think. It did have concurrency, right? Yes. From the very beginning. But you were thinking
*  that a JavaScript in the browser would not have the luxury of being concurrent. That's right. And
*  the reason was Java was going to run the plugins. We could fork threads and go to town. But the main
*  action in the browser was in a single threaded program, single Unix process on Unix or Windows.
*  And it was where you had to service the event loop and then go do things, respond to the network,
*  lay out some HTML, render it, turn widths into heights by filling containers, boxes, the early
*  what became the CSS box model and run scripts to make the thing livelier, respond to user input.
*  And all that event driven programming was in part like HyperCard because HyperCard had this on
*  event name syntax. And so that's why you have in JavaScript on click run together as the name of
*  the event handler. And there's some funny ones on mouse over and on mouse out. People still
*  complain about those, but you know, there are many more events now over the years standardized, but
*  it was a mix of event driven single threaded programming because it had to run in the main
*  thread of the browser where the action is. And Java never got there, which meant Java could not
*  interact easily or quickly or in a nested way with the document, with the objects reflected from the
*  HTML document, with the tables and forms and so on. And that is one of the reasons I think JavaScript
*  survived and Java kind of died. Java was in this plugin prison. It essentially was confined to a
*  rectangle, the app rectangle. And while we even built next year, Nick Thompson, a friend from SGI,
*  who was an intern grad student at CMU at the time, built the first version of live connect to glue
*  Java and JavaScript together to deliver on that vision where you do have commerce between the
*  data types and the heap. Did it work? It worked, but Java was in charge. JavaScript was in charge
*  and Java was just these components, these helper objects. You might as well do everything in
*  JavaScript. And what happened over time, it's like an evolutionary filter, just kind of who needs the
*  plugin. And in fact, Sun mismanaged Java as a plugin. They thought, oh, Netscape is giving
*  us the distribution vehicle and we don't care about the browser. It's just about getting Java
*  out there. And that was a big miscalculation. They then tried, because Microsoft's killing Netscape
*  after years, they tried getting into Microsoft. And you may remember there was a Sun-Microsoft deal,
*  which famously blew up. And Microsoft kicked Java out of Windows. And that's when they really pulled
*  the trigger. I think they already evaluated it and liked it on Anders Helzberg's .NET and C sharp
*  and decided we're going to just not have Java. We don't want any of that Sun stuff. We don't want
*  the patent risk. I'm not sure what the fights were about. There was some patent angle to it, I think.
*  And up till then, Microsoft had been using Java components like in Outlook Web Access,
*  which had a lot of JavaScript to be a webmail, hotmail-like user interface. They had to call
*  the mail server through HTTP and they used a Java object to do this. And when they gave the boot
*  to Sun, the left-hand gave the boot and the right-hand said, we better do something else in Outlook
*  Web Access. What are we going to do? And they said, let's just add an ActiveX component,
*  which is their own native way of embedding things in languages. And it'll be what became
*  XML HTTP request, which is now a web standard for calling asynchronously. And it's been replaced
*  by the fetch API in HTML5 or HTML living document. But this whole lineage goes back to Java being
*  successively the loser and getting kicked out. And after Microsoft kicked it out, it was a plugin
*  and you would find it required for like smart card banking in the Nordic countries where
*  that was mandated by law, but really didn't get used much. Or there were pilots who used it for
*  flight information. But Flash, which Netscape could have bought, but fortunately didn't.
*  What year were we talking about with Flash? I think after the IPO, so it was probably late 95.
*  And Flash was around. Was it Adobe? No, it was called Future Splash and it was these brothers,
*  Jonathan Gay, I think his name was. And he came knocking and the marketing guy at Netscape,
*  who was screening the technology partners or wannabe acquisitions was brutal and just
*  everybody wanted to get in on the Netscape stock gravy train and he sent them packing.
*  And they ended up selling to Macromedia and Macromedia was where Flash was created.
*  And the good thing about Macromedia was it was a tool company. So it invested in the best ideas,
*  I think, which are still somewhat lost to us of Flash. The timeline animation has sort of been
*  immutable function over time. They had the tooling around that too, like that Dreamweaver,
*  there's a Flash director. There were a bunch of them. Yeah, I mean, yeah, that was a great.
*  Flash Builder was one of the last ones. These tools were used by real artists and special effects
*  people and designers. All the restaurant websites around 2005 were done in Flash, which was,
*  we were trying to do HTML5 at the same time that was the Firefox era. We were trying to make
*  the web capable enough. You didn't need Flash, but if you recall, you go to a restaurant and it's like,
*  this is kind of like a game or something. It's like a Flash. All the font looks small.
*  You didn't like Flash from the beginning. You're like, this doesn't feel right.
*  Not really. I actually admire Flash's technology. I'm pretty pragmatic about these things. And I
*  realized that it doesn't matter if you're dealt a bad hand, like JavaScript was a rush job,
*  or if you have Flash as a plugin and you can invest in the tools and make it pretty good.
*  You should make it better for your users and grow it as best you can. And what happened with the
*  browser due to Microsoft's monopoly abuse for which they were convicted. And even after that,
*  until I think Firefox and then Chrome was people kept saying, oh, the web can't do X, can't do Y.
*  We'll have to have a plugin. We'll have to have a new approach. We'll clean the slate and have a
*  new web. And everyone who said that failed. And the reason they failed is because there's too much
*  value in the web, this huge network. And the worst is better principle means that you can not only
*  start bad, which they all sneer at, but get on first and get wide distribution, get sort of
*  evolutionary advantage in priority of place, but you can also improve it over time. And so if you're
*  going to improve Flash and for some reason Flash is now at a favor, Steve Jobs said you can't have
*  Flash on the iPhone. That was probably the death now. Put your energy into JavaScript. And that
*  happened. So we did things at Mozilla with Adobe to improve, which bought my Macromedia, to improve
*  Flash and to improve the version of JavaScript that was in Flash. We tried to standardize that.
*  Oh, that's right. I'm getting ahead of myself.
*  You can program Flash.
*  Yeah.
*  That's right. Can we just rewind to the magical, like, you know, it's a special moment in the
*  history of all of computing. We'll talk about it later, but it's arguable. It's possible that
*  the entirety of the world will run on JavaScript at some point. So like, it's like those days,
*  it would be interesting if you could just describe actually zooming in on the, how the cake was baked
*  from the, you know, the several days that you were working on it. What was on your mind?
*  How much coffee were you drinking? Were you nervous? Why freaking out?
*  I'll try to remember it. I mean, you're right. There are these pregnant moments you see in
*  hindsight. Maybe they're overrated, but like Hegel sees Napoleon on horseback at Jena and says there's
*  the world spirit on horse. And I knew that there was a chance to do it. Mark knew, and he was my,
*  you know, executive sponsor. And he was the one, you know, sort of brainstorming how the
*  JavaScript should be right there in the page. That was important for him to say that. Cause I
*  thought so too, but a lot of people were like, well, you can't write programming language in the
*  middle of the markup. And indeed there are problems. If you did it naively, you'd see the code
*  laid out as like random gibberish. So I had to figure out how to hide that. That was a challenge.
*  Is that a breakthrough idea? I mean, so you and Mark thinking about this idea that you just inject
*  code in the middle of the markup. Of the webpage. Yeah. It was considered kind of
*  heretical. There was an SGML guru, I forget his name, but he corresponded with me. And at first
*  he was angry. He's like, you should have used a marked section. Why didn't you use a marked
*  section? And I said, well, SGML marked sections are not part of HTML by the way, and they're not
*  supported in the browser. And so I did some hack that was equivalent and over time you could do
*  the proper SGML thing, but he eventually came around and it was again sort of evolutionary
*  necessity. It was almost like introgression. Like, like, you know, the idea, um, which, uh,
*  Lynn Margulies, I think helped get across that, uh, we have to consider mutualism biology that
*  maybe, you know, mitochondria were ancient, uh, prokaryotes that got into the cell and became
*  beneficial. Um, somehow, uh, the, the same sort of thinking applies. Uh, you have to embed
*  JavaScript in HTML. It's going to be a good virus. It won't. So the code, the code becomes data in
*  a sense that just gets carried, carried, carried along. But is there, is there the side of the,
*  you were focusing on the Netscape at that time. Doesn't the browser have to support,
*  interpret correctly this mix of HTML and whatever code? I had to hide it from old browsers,
*  including Netscape one one, which was predominant then. So I used, uh, an HTML comment,
*  but the inside the container that comment lived in the script tag, which is a new element, I could
*  make different semantics in Netscape too, where those HTML comment delimiters, instead of being
*  multi-line brackets became one line or essentially one line. So you wrote the JavaScript was written,
*  the programming language was written as a comment, a comment for old browsers in a set of brackets
*  that were ignored with real code for new. And it was this two way comment hiding hack, as I called
*  it, that was absolutely necessary for us to get off the ground. We couldn't have bootstrapped
*  JavaScript without it. We didn't have scripts that were loaded from a separate file. The only scripts
*  in that skip to were in line in the document. What were the challenges here? What, what, like what,
*  uh, you know, typing, uh, uh, what were the choices you were thinking about garbage collection?
*  I didn't have time to write a garbage collector. So I just, I didn't at first. So the thing was
*  using essentially arenas or what new calls object pools and just would run out of memory eventually.
*  And I added reference counting in a hurry after the 10 days in which I had. So after I was in
*  the server team doing HTTP one one and thinking about the language, I finally got transferred
*  to the client team in early May. And that's when I, you know, I got the go sign from Mark and it was
*  like, we can't wait because people inside Netscape are doubting. Even people inside sun are definitely
*  doubting. Bill joy was the champion, but he was like alone in that in seeing that there was a role
*  for JavaScript as the, the, as I call it, the sidekick language, Robin, the boy hostage,
*  Frank Miller put it in the dark night returns, um, that, uh, there was this silly little language
*  that would be the glue language and it could become important over time. And you were better
*  off having that complimentarity, that pairing of languages, just like Microsoft stacked it with
*  visual C plus plus and visual basic. So what was the big moment of, uh, I'm done.
*  So I had to do a demo. I forget the dates. I think I, for a history of programming languages paper,
*  Alan Worsbrock did with my health. He did a lot of the writing. Um, I think it was the 10 days from
*  like Thursday evening through to the following weeks, you know, the whole of that week and then
*  into the Monday. You get sleep. Not, not, not enough. And I was really, uh, going fast because
*  I'd already used a lot of, um, C compiler and front end compiler knowledge that I'd gained from
*  undergraduate school. When I started getting into computing, uh, as a Renegade physics major, uh,
*  people were formalizing more efficient, uh, bottom up grammars, parsers for bottom languages, uh,
*  really, uh, LALR one was the big thing. And I studied all this and learned how to parse them.
*  And in the end, uh, if you're doing C languages, you often do what, um, but what, uh, Dennis Richey
*  did anyway, which is recursive descent, uh, parser, you can hand code it. And, um, I did that for
*  JavaScript in a blazing hurry. Mostly got it right. I didn't, you know, have precedence inversion
*  problems or other bugs, but I copied a lot from Java and C and I tried to keep things simple,
*  like the equality operator in those 10 days sprint between two objects of different dynamic
*  type said, no, they're not equal. Their types are different. And then after that, I had internal
*  early adopters and they were using JavaScript to like match a number against a database field that
*  had been stringized. And they said, oh, can we just have implicit conversion? And like an idiot,
*  I agreed. I gave them what they wanted. I was trying to please them and get adoption. And that,
*  you know, broke what, what equivalence relation, um, nature there was to the double equal, you know,
*  there's some edge cases with not a number that break that too, but it really broke it. Um,
*  having an implicit conversions in that operator is something that people still roast me over.
*  So let's, let's talk about two things. One, it sounds like the comparison operator,
*  the equality operator is the thing that you regret. So maybe making it sloppy, making it sloppy. So
*  what is the biggest thing you regret in those 10 days? And what is the biggest thing you're proud
*  of? So that, that making it sloppy came after the 10 days. And my lesson there, which I've tweeted is
*  when people come to you saying, can you please make it sloppy or add this cute feature?
*  The answer should be no. And I should have known that because I think Nicholas, one of my heroes
*  said the essence of design is leaving things out. Um, but during the 10 days, I also, like I said,
*  I was in such a hurry, I left out garbage collection, came back to haunt me, but I got
*  reference counting in, in time that people, uh, weren't running out of memory right away on,
*  on long live job. What happens when you don't have garbage collection, you have objects.
*  Well, you just run out of memory. And, you know, at first you write a short script and the page
*  doesn't last long or it doesn't do a lot. It's okay. Oh, I see. Yeah. But if you're writing a
*  game or something and you're doing event based allocation, you run out of memory. And this was
*  noticed in the summer of 1985 and people were like, what's going on? I, oh yeah, I got to get,
*  I got better. Go back and do reference counting. And then the rep problem, the reference counting
*  is you're writing the language in the runtime in C and unsafe language. And if you're reference
*  counting and you overflow the counter, you mismanage it. So it goes high, it gets stuck high.
*  You leak memory again and you run out. If you underflow it, you pre-memory that's still in use.
*  And even then we knew what all the security hackers came to know that you therefore have a
*  potentially a remote code execution vulnerability. Cause this was before things like, um,
*  non-executable, um, heap memory and, um, staff defenses against taking over memory.
*  So if you can, from the remote side, write some HTML and JavaScript that just happens to exploit
*  a bug in memory safety, like causes JavaScript to underflow reference counter. And the script
*  still has its hands on that object and it's trying to call a method on it. And there's some kind of
*  lookup function table in the object, but you've managed to stuff the heap with strings that
*  forge their own lookalike for the function table. You can call some other code.
*  And this was a problem right away. So security, you know, JavaScript up the ante. Java had this
*  problem too, but in its own VM. And it just was, you know, a separate headache for son to worry
*  about. We had this problem in Netscape right away. So Netscape two came out after my 10 days. And
*  after these, you know, follow on work to embed, um, JavaScript better in the browser and to add
*  garbage collection through reference counting. Really I call it reference counting and get it
*  shipped. We had a bunch of dot releases where we fixed security bugs like maniacs.
*  But what is the thing you're, you know, when you sit back on a porch and just look out into the
*  sunset, what are you most proud of from those 10 days? I think the first class functions shines.
*  I think especially since Java didn't have it and it was somewhat unusual. Scheme made it in somehow.
*  At the end of the day, people complain because Scheme has, you know, minimalism. It has, you know,
*  six or seven special forms. It has hygienic macros. It has call CC. It has sort of a beautiful,
*  complete, um, set of forms to make the lambda calculus pleasant to use in practice. Um, and
*  JavaScript is, you know, kind of a multi paradigm or shambolic,
*  just in a small tangent, you mentioned Mark Andreessen. It sounds like in Bill Joy, but
*  staying on Mark, it sounds like he had an impact on you in that he sort of believed in what you
*  were doing there. Can you, can you talk about like what role Mark had in your life? Yeah,
*  we would meet at the, um, the pencil creamery in downtown Palo Alto and Mark was just fresh out of,
*  you know, grad school or whatever he was doing and he was big dude and he got fitter later.
*  He had hair. He, he would order giant milkshakes and burgers and we would meet there and brainstorm
*  about what to do. And it was very direct because we didn't have much time. The, the sort of,
*  we didn't talk about it, but the implication was Microsoft's coming after us. Mark was saying
*  things boldly, a pre IPO like Netscape plus Java kills windows, right? This is ambitious. Make a
*  browser programmable. It becomes the new runtime for programs. It's the meta OS or it's the
*  replacement. Oh, S um, but he still saw value in JavaScript. Yes. Even though he was saying that
*  in Java was the big name, hence the trademark license. Uh, he saw JavaScript as important
*  and he even thought, what if we got, I told this in other interviews, I can say it. He thought,
*  what if we had, uh, my friend, Kip Hickman, who'd been at Netscape from the beginning and who was a
*  Colonel hacker at SGI when I joined, he started writing his own JVM before we consummated the
*  Sun deal and got our hands on their code. And the Java compiler, Java C, which Arthur Van Hoff had
*  written very nice code was all written in Java. It was self-hosted or so-called bootstrap. And so
*  we could use that as soon as Kip's Java VM could run the byte code from the Sun, uh, JVM running
*  the self-hosted compiler to emit the byte code. So once we could bootstrap into Kip's VM, we
*  wouldn't need Sun. And Mark was like, well, maybe we can just ditch Sun. Well, if Kip's Java VM,
*  well, if you're a JavaScript VM, we now we need graphics. So Mark was thinking far ahead because
*  he knew you could do things with HTML and images, but at some point you really want
*  like this. Yeah. Like even SGI had already started its downfall because the first four
*  to VLSI team there had gone off to do 3DFX and all these other companies that made the graphics
*  card on your PC, right? Doom was, was big and Quake. And so you were, we were all playing Quake. I
*  was old, so I was terrible. Um, but why not put that graphics capability on the web? And in fact,
*  it finally happened at Mozilla with Firefox era with Vlad Vukicovich taking OpenGL ES and reflecting
*  it as WebGL, but OpenGL ES is the mobile version of OpenGL, which is a standard based on SGI GL.
*  So there's this whole lineage of graphics libraries or really graphics languages for what became the
*  GPU. And Mark was thinking ahead. He's like, we need graphics too. And I thought, okay, I can try
*  to get somebody I knew at SGI, but he's a grad student at MIT. He was studying under Barbara
*  Liskov. He laughed when he heard about this later, Andrew Myers. He's at Cornell long time. I think
*  he's a full professor and Mark said, great, we'll get him. I'm not sure he's going to come. We'll
*  throw money, you know, stock options. We never did it. And they did the Sun deal. So Kip Nobly
*  put aside his own JVM and we used the Sun JVM. So that was an ambitious period. And Mark was
*  very generative because he was pushing hard. He was ambitious and he wanted to have Netscape
*  possibly be in control of the ball. Maybe you could speak to this dance of Netscape versus
*  Internet Explorer. You've thrown some loving words towards Microsoft throughout this conversation,
*  but that's a theme with, I mean, Steve Jobs had a similar sort of commentary from a big sort of
*  philosophical principle perspective. Can you comment on like the approach that Microsoft has
*  taken with Internet Explorer from IE1 to Edge today? Is there something that you see as valuable
*  that they're doing in the occasional copying and that kind of stuff? Or is the world worse off
*  because Internet Explorer exists? So I'm going to segment this into historical areas because I think
*  Microsoft today is quite a different company and what they're doing with Edge is different.
*  But back then, Gates, you know, aggressive character, not really original in my view,
*  not an originator. Steve Jobs famously said once, he doesn't have any taste. And I don't mean this
*  in a small way. He has no taste. You can see this. Apple at the time had beautiful typography and
*  ligatures and kerning and the fonts looked great. And Windows had this sort of ugly system font that
*  was carefully aligned with pixels so it didn't get anti-anguished. What is it? I'm sorry to keep
*  interrupting, but why was Internet Explorer winning throughout the history of these
*  competitions? Distribution. Distribution matters more than anything. And this is why, you know,
*  even now we're seeing in the browser wars Edge doing better because it's being foisted on people
*  of Windows. We have Windows 10 boxes at home. We have some Windows 7 boxes or laptops we keep
*  running to because we don't connect them to the internet generally. But once you have that operating
*  system to hold, you can force Edge. And Apple did it with Safari too. It's not unique to Microsoft.
*  That's sad. But distribution matters. And that's why I think IE was going to win. That's why
*  everybody at Netscape felt we're doomed. This was something Michael Toy and Jamie Woodson were doomed.
*  But for a while there, we had a chance and we innovated in Netscape too. We did a big platform
*  push. Java and JavaScript and plugins, more plugins and more HTML table features and really
*  started making a programmable stack out of what were pretty static web languages. And even in the
*  beta releases in Netscape too, people were using JavaScript to build what you would call single page
*  applications like Gmail. And they were using JavaScript locally to compute things and to call
*  the server on a hidden frame in the background. So it was prefiguring a lot of what came later as
*  Ajax or dynamic JavaScript, dynamic HTML. So people saw that. I mean, even then they saw it.
*  That's kind of, I don't know, from my perspective, that seems quite brilliant. It seems like really
*  innovative that you would have code run in the browser. It did impress me with something
*  which I learned later about from Eric Von Hippel of MIT, which is user innovation networks,
*  lead user effects. That throwing out JavaScript, even though we weren't doing open source, we were
*  doing beta releases early and permissively with Netscape. Getting early developer feedback,
*  absolutely critical. I loved it. I did some of that with SGI with some of the products I worked on,
*  but it really came to the fore in Netscape. And that culminated in Mozilla where you're dealing
*  with developers all the time and early adopters, lead users. But the lead users helped improve
*  JavaScript even in those last few betas where I could hardly change things. I was under pretty
*  rigid change control. So we're talking about just a small collection of individuals that are just
*  upfront. A guy named Bill Dorch. You can find his work in the web archives still from 1996.
*  It's a single page application. It's an artist gallery of mountain art. He doesn't quite work.
*  He uses JavaScript locally. He uses a local database. What you would think of now is JSON,
*  but it's all pure JavaScript code, a bunch of objects being constructed. That's so cool.
*  So how is, if you can do sort of a big sweeping progress of JavaScript, how has
*  JavaScript changed over the years? Any of you from those early 10 days with a quick
*  added addition of garbage collection and fixes around security? How has this evolution that
*  now it's taken over the world? It's been a bumpy ride because the standards body got shut down
*  after Microsoft, I think, took over the web and then felt punished by the US v Microsoft
*  antitrust case. Can you speak to the standard body? That was a fun ride too, because Netscape had
*  taken the lead with the web and HTML innovations like frames and framesets tables. The W3C was
*  sort of off even then sort of an SGML land heading toward XML lala land. I'm going to be a little
*  harsh on it. What's this? I'm sorry. SML was the precursor markup language to HTML, or it was sort
*  of the more extensible standard generalized markup language. It was a XML like 20 brackets, but it
*  had all sorts of elaborate syntax for doing different semantics. This is why I think TBL
*  and others who wanted to do the semantic web then took XML forward. They had this, or some of them
*  anyway, had this strange idea they could replace the web with XML or that they would upgrade the
*  web to be XML. It couldn't be done. Worse is better had concrete meaning. The web was very forgiving
*  of HTML, including sort of minor syntax errors that could be error corrected. Error correction
*  isn't generally done in programming languages. That's another amazing thing about HTML. It's
*  more like biology than programming. Yeah, exactly. And so XML was in its standard form, super strict
*  and could never have admitted the kind of users who were committing these errors. The funniest part
*  was Microsoft said, hey, we're doing XML, but the way they put it in Internet Explorer under the
*  default media type, put it through the HTML error corrector. So they kind of bastardized it to make
*  it popular and usable and accessible. And so XML as a pure thing was never going to take over.
*  W3C was kind of not fully functional because Nestcape wasn't cooperating with them. We thought
*  about where to take JavaScript and we realized our standards guru, Carl Cargill realized there was a
*  European standards body that had already given Microsoft fits by standardizing parts of the
*  Windows 3.1 API, which European governments insisted on. They said, Microsoft, we can't
*  use your operating system without some standards. And Microsoft said, here's our docs. And the
*  government said, no, we need a European standard. So this body called the European Computer
*  Manufacturers Association, ECMA, which eventually became global and became a proper noun instead of
*  an acronym. Right. It's just one capital E now with a lowercase CMA. Right. And as one of the
*  early Microsoft guys I met when we first convened a working group to talk about JavaScript said,
*  it sounds like a skin disease. But it gave, I mean, maybe you'll speak to that, but it gave the name
*  to JavaScript of ECMA script. That was the standard name because Java was a trademark of sons. They
*  were so aggressive. They were sending cease and desist letters to people whose middle European
*  heritage meant their surname was Javanco and they called their website, Javanco.com. And son
*  would send them a letter saying, you're using J-A-V-A at the start of your domain name. You must cease
*  and desist. I love marketing more than anything else in this world. So ECMA script and now is
*  popularly named as ES plus version. I would say people use JS more than anything. People still
*  say JavaScript. JavaScript is in all the books. So I mean, when you're referring to it's usually
*  JavaScript. And when you want to refer to a version of JavaScript, you'll say ES six, ES five.
*  Yes. Or now they've gone to years, which is kind of confusing because it's an offset of
*  2009. ES six is ES 2016. Yeah. It doesn't match the years perfectly. Yeah. So what were the choices
*  made and how did JavaScript evolve here? So we took this new standards body, which had, we thought,
*  sort of a proven record of standing up to Microsoft, but Microsoft sent a lot of people.
*  They sent some people who were pretty good. And then when they realized that I was there
*  and Netscape was not going to just bend over and do whatever they wanted, they sent somebody really
*  good. And he was a smart guy. He did a lot of the work on the first draft of the spec. Sean
*  Katzenberger, he's left Microsoft. He even did what I sort of did. He told his bosses, stop bugging me
*  to do other things. I'm focused on this because it took a lot of focused work to create the first
*  draft of the spec. And I was still holding, I was spinning almost all the plates. I had like
*  part-time help in certain areas. And on the front end integrations, I had the front end guys,
*  but I couldn't take as much time as Sean was to write the draft spec, but I had to participate
*  because I was essentially helping write down what the language did and in areas where we didn't like
*  what it did. And Microsoft didn't agree. We sometimes got away with slight changes. And
*  that's the story of standards. You have different implementations and depending on their market
*  power, they interoperate where you have agreement and where they don't, the dominant one usually
*  sets the de facto standard. And then you should probably reflect that into the de jure standard.
*  And this happened with JavaScript over time as Netscape went down and Microsoft went up.
*  We did the first edition of the standard codified in 1997 in France. We had a trip to Nice,
*  which was very memorable. For any interesting reason or just because it's nice? And ECMA's
*  European and IBM and others were there. Mike Kalashaw and IBM fellow was a British.
*  The guy who ran ECMA at the time, Jan van den Bell was quite a
*  raconteur and a very fun guy. And he had us out for the great,
*  Fouet de Mer, the bouillabaisse.
*  Was the standardization process beautiful or painful that those early days, you as a designer?
*  It was painful because it was rushed. Now, Guy Steele was contributed by son. So even more than
*  Sean, you had this giant brain guy steel helping bringing some of that scheme magic.
*  He even brought Richard Gabriel for funding. Richard wrote the fourth clause of the ECMA standard,
*  which is kind of an intro to what JavaScript is all about. So we had some really good people and
*  we didn't fight too much. There were some tension where I was fixing bugs and I was late to a
*  meeting and Sean Katzenberger, Microsoft was actually mad. Like, where is he? We need him.
*  And when I got there, I saw that only he saw this sort of off by one bug and somewhere in the spec.
*  And then I saw it too. And I said, there's a fence post bug there. And then we kind of locked
*  eyes and we realized we were on the same page and we kind of, he wasn't mad anymore.
*  What were the features that are being struggled over and debated and thought about?
*  It was mainly writing down what worked and what we thought should work in the edge cases that
*  didn't interoperate or that seemed wrong. But we were already laying the groundwork for the future
*  additions that I was already implementing. I was still trying to lead the standard by using the
*  dominant market power to write the code that actually shipped. So the de facto standard would
*  lead the de jure standard. And I was putting in the missing function forms that I didn't have time
*  for in the 10 days. So this is the engineering mindset versus the theoretician. So you didn't
*  want to create the perfect language, but one that was the popular and shipped and all that kind of
*  stuff. And you could say there was, I was standing on the shoulders of giants. So there was a staged
*  process where I had to hold back things that were well designed by others in other languages that I
*  could imitate, but I couldn't do them all in the 10 days. So they came in 1996 and 97. And they
*  came into the third edition of the standard, which was finalized in 1999. But at that point,
*  Netscape had been sold to AOL, which was a decent exit considering and had previously been
*  mercilessly crushed. Netscape was selling the browser along with server software that it
*  acquired after its IPO and Microsoft was just underpricing it. So there was no way to compete
*  with that. Microsoft was also making Internet Explorer the default browser in Windows,
*  which is called tying and antitrust law. And they were doing even more brutal things. There's a
*  famous investor, he did very well on Google. So he's a billionaire, Ram Sriram, and he was sales guy
*  or head of sales at Netscape. And he got off the phone looking ashen faced after Compaq called and
*  said, Microsoft just told us they're going to pull our Windows license if we ship Netscape as
*  the default browser. Wow. So there is some bullying going on. There was totally material in the
*  antitrust case. But JavaScript escaped into the standard setting where there was fairly good
*  cooperation. Microsoft had a really good guy on it and Guy Steele was there for a time and there
*  was some good work. But after the antitrust case and Netscape dissolving into AOL and not really
*  going anywhere quickly, Mozilla took years to really bring up, the standard froze. And by 2003,
*  even though they've been sort of noodling around with advanced versions, JavaScript 2,
*  had given the keys to the kingdom to another MIT grad, Baltimore Horwatt. Very big brain,
*  and still at Google, I think. He won the Putnam in 86. He's very mathematical.
*  Legit. He designed this successor language, JavaScript 2, but it only showed up in
*  mutated form in Microsoft's ASP.NET server side and it didn't last there. And it showed up in
*  Flash and that's what became ActionScript 3. Ah, ActionScript. Interesting. And then Flash,
*  of course, declined. And so how did we arrive at ES6 where it's like there's so many...
*  Okay, there's this history of JavaScript that people were just like, cool, when you're having
*  beers to talk crap about JavaScript, everyone loves to hate. People who are married say,
*  ah, marriage sucks. They just want to let off some steam even though everyone uses the language.
*  But ES6, it's become this repute. It fixed major pain points, I think.
*  It added things to the language and added something that was already ES5 strict mode, but
*  made it implicit in class bodies and module bodies. It was a big jump, but it accumulated
*  some of the ES4 designs that we'd done with Adobe for what we hoped would be the fourth edition of
*  ECMAScript that were supposed to fold in some of these old JavaScript 2 ideas that had come into
*  ActionScript 3. So you look at the family tree and you see these forks and the main ones are
*  the ones that go into Adobe Flash acquired from Macromedia and the one that went into the server
*  side of Microsoft's stack, which kind of died. And then trying to bring them back into the standard
*  and not quite succeeding, ES4 was mothballed. But all the good parts that everyone liked made it into
*  ES6. And so that was a success. And I said earlier, I had the wrong year. I think it's 2015, so it's off by
*  4, ES6. Yeah, it was done, finalized in 2015. It took a little longer than we hoped, but
*  because ES5 was 2009 and that was a smaller increment from ES3. We skipped 4 again, we
*  mothballed it. And we had a split in the committee where some people said, ES4 is too big. We're
*  going to work on incremental improvements, no new syntax in particular, they promised.
*  Not quite true, but they added a bunch of interesting APIs. Alan Weir-Sprock, my co-author
*  of the Hubble paper. And he was at Microsoft at the time. I ended up hiring Mozilla. He wanted to
*  get to Mozilla and keep doing the editor job of the JavaScript standard, ECMAScript.
*  And when we got ES6 done, it was a little late, 2015, and we switched to year numbers. So people
*  still call it ES6. I call it ES6. But if you remember, off by 9 plus 2000. Yeah, I mean,
*  ES6 is such a big job. I mean, like you said, there's a thought that connects all of it, but ES6 is
*  when it became this language that almost feels ready to take over the world completely. More
*  programming and the large features, more features you need for larger teams. Software engineering.
*  Microsoft did something smart too. Anders and company, Luke Hoban, who's left Microsoft,
*  also did TypeScript. And they realized something I think that Gilad Bracca is also popularized,
*  and he was involved in Dart at Google. If you don't worry about soundness in the type system,
*  you don't try to enforce the type checks at runtime in particular, just use it as sort of
*  a warning system, a tool time type system. You can still have a lot of value for developers,
*  especially in large projects. So TypeScript has been a roaring success for Microsoft.
*  What do you think about TypeScript? Is it adding confusion or is it ultimately beneficial?
*  I think it's beneficial. Now it's technically a superset of JavaScript. So of course I love it.
*  The shortest JavaScript program is still a TypeScript program. Any JavaScript program
*  is a TypeScript program, which is brilliant because then you can start incrementally adding
*  type annotations, getting warnings, learning how to use them. Microsoft had to kind of look around
*  corners at the standards body and guess how their version of modules or decorators should work.
*  And the standards body then may change things a bit. So I think they're obligated with TypeScript
*  either to carry their own version or to bring it back with incompatible changes
*  towards the standard over time. And I think they've played generally fair there. There's
*  some sentiment that why don't they standardize TypeScript? Well, they've been clear they don't
*  want to. They have a proprietary investment. It's valuable. They have control of the ball.
*  And in some ways you can say the same thing to any of the other big companies in the standards
*  body. Why doesn't Google standardize its stuff? So you think it'll continue being like a kind of
*  a dance partner to JavaScript, to the base JavaScript? There's a hope that at some point,
*  if they keep reconverging it and the standard doesn't break them and goes in a good direction,
*  we will get at least the annotation syntax and some semantics around them. Because when you're
*  talking about type annotations, they're generally on parameters and return values and variable
*  declarations. They're cast operators. You want that syntax to be reserved and you want it to
*  work the same in all engines. And this is where ideas like Gilad's pluggable type systems might
*  be good, though then you could create the same problem you have with Lisp and Scheme where
*  there's a bunch of macro libraries and they don't agree and you have conflicts between them. But
*  pluggable type systems could be one way to standardize this. What do you think about the
*  giant ecosystem of frameworks in JavaScript? It feels like because, I mean, this is a side effect
*  of how many people use JavaScript. A lot of entrepreneurial spirit create their own JavaScript
*  frameworks and they're actually awesome in all different ways. And this is an interesting
*  question about almost like philosophically about biological system and evolution,
*  all that kind of stuff. Do you see that as good or should it like, should some of them die out
*  quicker? I think that maybe they should. Now jQuery was a very clever thing. John Resig made this
*  library that was sort of query and do and blended sort of CSS selector syntax with JavaScript sort
*  of object graph or DOM querying and made it very easy for people to do things almost like they were
*  learning jQuery as its own language, domain specific language. And that I think reflected
*  in part the difficulty of using the document object model. These APIs that were originally
*  designed in the 90s for Java as well as JavaScript, they're very object oriented or even procedural.
*  They're very kind of verbose. And it took like a constructor call and three different hokey pokey
*  dances to do something, whereas in jQuery, it's just one line. So that fed back finally into the
*  standards. It didn't mean we standardized jQuery. It wasn't quite that concise, but
*  you find now with the modern standards that we were working on in the HTML5 sort of effort,
*  that things became simpler. The fetch API and the query selector API, document query selector.
*  A lot of things can be done now in raw JavaScript that you would make more concise and terse in
*  jQuery, but it's not bad. It's pretty good. Whereas in the old DOM of 15 years ago,
*  it was just too verbose. So maybe the frameworks were born
*  because JavaScript lacks some of the features of jQuery. And so now that JavaScript is swallowing
*  what jQuery was, then the frameworks will only the ones that truly add value will stick around and
*  the other ones will die out. And that highlights this division between the core language JavaScript,
*  which can show up in other places like Node.js on the server side and the browser specific APIs
*  or the document object model APIs, which are even managed by the W3C, the standards body
*  that was off an XML land when we were doing real JavaScript standards in ECMA.
*  And you have this division of labor, division of responsibility and division of style and sort of
*  aesthetics and also speed. So the document object model really stagnated after Microsoft kind of
*  de-invested in the web. And Microsoft did something in their haste in the spirit of Netscape,
*  doing things quickly and getting on first called DHTML. And some of their innovations
*  that were like an alternative document object model didn't really get standardized until
*  HTML5 when we pragmatists at Opfer at the time, Ian Hickson, who went to Google, Apple and Mozilla
*  said, let's, XML is not going to replace HTML. HTML4 is too old. Let's standardize HTML5 based on
*  all this good stuff, including that DHTML variant dynamic HTML5.
*  It feels like to me, maybe you can correct me, like a beautiful piece of design work.
*  It's not often with web stuff. You have this breath of just like, oh, whoever did this,
*  this just feels good. What are your thoughts about HTML? Am I being too romantic?
*  A little bit.
*  Are there flaws, fundamental flaws to it that I'm just not aware of?
*  I'm, you know, my old friend Hicks, he did a great job. He was another renegade physics
*  student. And he was basically a QA guy at Opera. But he obviously is a trained physics, you know,
*  student and someone who could write British or he, he developed test suites and he started
*  thinking about them more axiomatically. Now, this is, this can be good because you can sort
*  of systematize in a way that makes a better HTML, or you can get caught in the pragmatism of saying,
*  well, we have to handle all of these edge cases. So we're just going to have sort of a test matrix.
*  And if the matrix is large, it will not be beautiful by many people's lights. Everyone
*  likes to minimize along their preferred dimensions, the seven special forms in scheme or whatever.
*  But, but reality is HTML needs to be big. It's kind of shambolic. It's a creative
*  multi-paradigm. And Hicks, he did a good job, I would say with a bunch of it.
*  Other people came in in the spirit of Ian Hicks and to do HTML5 work and they've carried on that
*  effort. And it's a, so it's a mix of pragmatism, de facto standards from the past being sort of
*  combined or written down for the first time, and then rethought in a way that has a simpler
*  syntax, like the fetch API instead of XML HTTP request. This video too, as well. It's ultimately,
*  it feels like maybe you can correct me. It feels like it was the nail in the coffin of flash.
*  Steve Jobs saying no flash on the iPhone, in my opinion, was the actual
*  state through the heart. But, but well, I'm not sure what trope you want to use this.
*  Flash was a zombie for until just this year, right? Or last year. I think last year was the
*  end of flash in main browsers. But jobs really did the death blow. And yeah, you're right. We
*  had to make HTML5 competitive. I still don't think we got that beautiful timeline animation.
*  The timeline thing. So you like the time. I mean, me from, you know, I used to animate all kinds
*  of stuff inside flash. Plus there's a programming element. It was a little bit, I don't know if you
*  comment on that, but to me it was a little bit like go to statement, like in a sense that
*  there's a little bit too chaotic. Like it didn't, that OCD part of me as a programmer wasn't
*  satisfied by flash. It feels like there was bugs that were introduced through the animation process
*  that I couldn't debug easily. Yes, I heard that too. I didn't use it. So I'm doing the grass is
*  greener thing here. The thing I liked about the animation model was that it was this immutable
*  function of time. So you could time warp and you could, if you dodge these bugs or worked carefully,
*  you could really make it sing in ways that I think still a little challenging with web
*  animation standards, but, or just using raw canvas and WebGL. But there's so many tools now that
*  maybe it doesn't matter. And yet we had to, you know, do video, we had to do WebGL and then
*  evolve it. We had to do web audio. But once we did all these things that helped flash die,
*  thanks to Steve Gupp's, we had something that people didn't realize. We had that vision that
*  Mark and I have this graphics capable to the metal portable runtime. And we at Mozilla realized this
*  and we saw JavaScript was something that you could compile to. Adobe had somebody in the
*  Adobe labs doing this too. He had a project called Alchemy. We had somebody who's now at Google,
*  Alon Zakai, who did his own LLVM based compiler that would take C or C++ and it would emit
*  JavaScript. And you would think this is crazy. You're going from this sort of machine types,
*  low level, you know, controlled memory allocation language to this garbage collected, dynamically
*  typed high level, higher level language. But Alon sort of just phenomenologically carved nature of
*  the joint and found the forms that were fast in JavaScript. And then with Dave Herman, who I'd
*  recruited from Northeastern University, who was a type theorist and Luke Wagner, who's still at
*  Mozilla, who was the compiler guy and the JIT guy, they figured out how to codify what Alon had done
*  into a typed subset of JavaScript called Asm.js. And this is a strange thing to think about because
*  it doesn't have new syntax. The types are casts that occur in dominator positions in the control
*  flow graph. So it's like a hack on JavaScript and it's a subset and it uses those bitwise operators
*  that I talked about copying from Java to basically cast numeric types, which are double precision
*  flowing point into integers. And so inside JavaScript in the kernel semantics are integers.
*  And if you use these operators, if a compiler emits them in the right places, you can then treat them
*  as typed values, typed memory locations, and you can type check your program. You can not only type
*  check it, you can compile it. This is all in sort of linear time. You can compile it to have
*  deterministic performance. It doesn't touch the garbage collector. It calls a bunch of functions
*  that come from the C functions or C++ code that you're compiling. And you can make the
*  Epic Unreal Engine go in 30 frames a second. And when we did this in 2013 in the fall,
*  Tim Sweeney and I met, didn't think it could be done quickly. Thought it would take years.
*  And the team went to Raleigh to Epic and in four days they had Unreal Engine ported by pressing a
*  compile button. But they had to have WebGL, which came from OpenGL, ES came to OpenGL,
*  which came from Silicon Graphics GL. They had to have Web Audio so they could map OpenAL,
*  which was another audio library standard to Web Audio, which was kind of a Chrome idiosyncratic
*  thing. But they could make it work. And they had to have Asm.js for fast C++ to JavaScript.
*  And if you didn't have that fast compiler step, the JavaScript you'd write by hand trying to do
*  an Unreal game would be too big and too slow. It would touch the garbage collector. It would not
*  keep up with 30 frames a second on the hardware, 2013 hardware. So we demoed that at, this was
*  in fall 2012 now, I think about it, because we demoed it at GDC, Game Developer Conference 2013.
*  And people were stunned. It's like Unreal Engine, Unreal Tournament running in my browser window.
*  No plugin, no flash, no Java, no- So were those the early days of,
*  because JavaScript now is able to run basically on par with a lot of the C++.
*  Yeah. And even before then you had the fast JavaScript VMs in 2008 when Chrome came out.
*  Just before it came out Mozilla, my friend Andreas Gall and I and others hacked out TraceMonkey,
*  our Trace-based JIT. The Squirrel Fish Extreme team at Apple did their JIT. And we were all competing
*  on these crazy performance benchmarks. It was a little bit too much tuning to the benchmark,
*  but JavaScript started getting fast and developers started noticing it. But it was still kind of
*  its own high-level language with garbage collection. The Asim.js step helped us go further because
*  until we really proved the concept, people were still saying, well, JavaScript's okay. It's
*  getting faster thanks to V8. Everybody gave Google credit, especially Google. But we need
*  something to kill flash. Let's use the portable native client code that Google had acquired,
*  native client, which is a separate lineage for taking basically C code, compiling it into a
*  software fault isolated container of some sort using some kind of virtualization technique.
*  And maybe it can even be in process and still be memory safe. That would be awesome. But they ended
*  up using process isolation too. And that kind of weakened it. And in the end, it was like portable
*  native client. Okay, meet the new boss, same as the old boss. This is the Google flash, right?
*  But when we did Asim.js and we showed Unreal Engine working, I think it was only a matter
*  of time before Google threw in the towel. And in fact, everybody agreed in spring of 2015,
*  we're going to take what was proven by Asim.js and make a new syntax, a binary syntax, it's efficient
*  that loads into the same JavaScript VM that JavaScript loads into. So there'll be two source
*  languages, one VM, very important, one garbage collector, one memory manager, one set of compiler
*  stages. And that's called WebAssembly. And that's the successor to Asim.js. And it's important that
*  it have binary syntax because at the end of the day, especially on mobile, if you're downloading
*  JavaScript, even if you're using LZ compression on the wire, that's cool. But you've got to blow
*  it out into memory and then parse the silly eight character function keyword that I picked.
*  When I should have used something shorter, I picked it because of awk, the Unix tool. So anyways.
*  I want to, but I'm not following the awk thread. But is it surprising to you that how damn fast
*  JavaScript is these days? I mean, like, because you've been through the whole journey. I know
*  every step of the way, but is it like, I mean, it feels incredible.
*  It does. But I knew it. So the funny thing is computer science is this big karmic wheel,
*  right? Wheel of Fortuna. And in the, it's about the 97, I was loaned by Netscape to do due
*  diligence for Sun in their acquisition of Anamorphic, which was David Unger and friends,
*  people, Craig, I'm forgetting his name. He went to Microsoft. These Stanford language buffs who
*  had taken small talk and then David created self as a simpler sort of small talk language.
*  And made really fast just in time, compiling VMs for them. And they, you know, well ahead of
*  Java hotspot or JavaScript V8 or any of these modern VMs, figure out how to make dynamic code
*  fast because small talk is dynamic language, right? It has classes. It has, I think more lockdown
*  declarative syntax and JavaScript, but it's fundamentally dynamic. You don't declare the
*  types. But you could infer the types as the program runs and you start to form these
*  ideas about what types are actually flowing through key operations. And you form little
*  so-called polymorphic inline caches that are optimized machine code. The cache is the machine
*  code that assumes it does a quick check to make sure the type is right. And if it's not right,
*  it bails to the interpreter. And if it is right, you go pretty fast. And that short test is a
*  predicted branch. So things are, things are pretty quick. All that amazing stuff I knew about in the
*  nineties. And I, I didn't have time to do it. And Anamorphic got bought by Sun and they did
*  hotspot. And you needed that even in Java, because at scale Java has some dynamic aspects due to
*  invoke interface. You can have basically collections of Java code where you don't know at the time,
*  each module or package is compiled exactly what's being called, what subclass or what implementation
*  of an interface is being called. And so you want to optimize using this sort of dynamic
*  polymorphic caching there too. And they did that and hotspot. It's amazing, amazing beast.
*  I've met like 13 people who all claim they created it. I think, I think one of them may deserve
*  credit more than others. But I didn't get to do that in JavaScript. And when we knew that, that
*  Google was going to do their own browser, which we knew it was around 2006. I also met the team that
*  did V8 and it turns out it was Lars Bach, who was one of the young engineers from Anamorphic,
*  got acquired by Sun. And so Lars is like the, one of the world's expert on these kinds of virtual
*  machines. And he picked my brains about JavaScript and I could tell he didn't like it at the time,
*  but he had to do it. And- Oh, really interesting.
*  Yeah. In 2006 launch at Google's campus. And then I had another friend who was DevRel at Chrome and
*  he said, yeah, we don't know what they're doing. This is getting 2007 to fall, getting toward 2008.
*  We're trying to get Chrome out and we don't know what's going on with the V8 team. They're often
*  Denmark rewriting their engine four times, which is good. That's the right way to do this kind of
*  development. They were learning JavaScript, including all its quirks, which they came to
*  hate the fire of a thousand suns, which is one of the reasons that Lars and company did dart
*  their own language, but they also made the language fast. And meanwhile, we knew this was
*  happening. So we got our act together with Tracemonkey, our tracing JIT at Mozilla and
*  Apple, I think was also aware. And so they were doing their own JIT. So the era of jitted fast
*  JavaScript in 2008 had this prehistory going back to small talk and self and anamorphic.
*  And the, again, the lineage is interesting because you had Lars and anamorphic and then he ends up
*  at Google. Yeah. And today we have an incredibly fast language that, like you said, still, you know,
*  without hate, you can't have love. So I think there's both love and hate for this dance,
*  this rich complex dance of JavaScript throughout its history. There's a dialectic of sure. For
*  sure. Today, JavaScript is the most popular language in the world. Why by many measures?
*  Why do you think that is? Is it, is there some fundamental ideas that you've already
*  spoke to a little bit, but sort of broader that you think is the most popular language in the world?
*  So I think I did, you know, by doing first class functions and taking the good parts of the C
*  operator hierarchy and just keeping things simple enough, maybe it could have been simpler, but
*  had to make it look like Java and interoperate with Java, that there was, you know, inherent
*  goodness, Aristotelian quality there. And people perceive that even through all the quirks and
*  warts. And then over time, working on it with the standards body, working on it, not only in
*  as a core language, but in the context of HTML5 and making the browser better,
*  listening to the developers, thinking about, this is something that Nick Thompson wrote nicely about
*  on the Hacker News. I was very flattered. He said, Java was this thing where the experts were
*  writing the code and it was compiled and you had to declare all your types. And some didn't really
*  give a damn about, you know, the average programmer who wanted to build real web apps, dynamic things.
*  And I was in there, meanwhile, doing a bunch of people's jobs, making JavaScript
*  survive those early years when it was kind of touch and go, right? JavaScript was considered
*  Mickey Mouse language. It was for annoyances like the scrolling text at the bottom of the
*  browser in the status bar. But I kept listening to developers, working with them and trying to make
*  it run in that single threaded event loop in a useful way. And I think that
*  forged something that people have come to love. Now you don't always love, you know, the best thing,
*  right? I talked about Shakespeare, sonnet about, I mistrace eyes or nothing like the sun or, you know,
*  the scene from Josh Whedon's film, Serenity at the end where the actual piece in the score
*  by David Newman is called Love, where Captain Mal is teaching River Tam about how to pilot the ship.
*  And she's a super genius, super soldier. She knows how to do it already. And he's basically talking
*  about how you have to love the ship because if you don't, it's going to kill you. And then the
*  piece falls off the ship. It's kind of like JavaScript. You have to love it. You have to
*  love it because now people say we're stuck with it because it got this priority of place.
*  But there's love underpinning that. And actually the listening to developers,
*  that's kind of beautiful. There's most successful products in this world with all the messes,
*  with all the flaws, perhaps the flaws themselves are actual features, but that's a whole other.
*  That's a discussion about love. But underneath it, there's something that just connects with people.
*  And it has to keep connecting. If JavaScript kind of went off in this,
*  people sometimes complain about ES6. Oh, you put classes in JavaScript. I hate classes. You've
*  ruined it. But it's not true. It's a dynamic language. Smalltalk had classes. Python has classes.
*  There are lots of Lisp variants that have classy systems.
*  So people who don't reject it based on some sort of fashion judgment do use it and do interact with
*  the standards body. The standards body is competing browser vendors mainly, but also now
*  big companies that use JavaScript heavily, the Paypal's and other such companies, Salesforce.
*  And they have to cater to web developers. They have to hire developers who know JavaScript. They
*  have to keep their engines up to the latest standard. And this creates all this sort of
*  social structure around JavaScript that is unusual. I mean, you get C++ buffs that follow the
*  inner workings of C++. What is it now? 21 something. I don't know. I've lost track.
*  But it's a more rarefied group. It's more like the old language, gray hairs,
*  where as JavaScript is a younger and more vibrant large crowd.
*  There's a community feel to it. There's echoes. Perhaps I don't want to draw too many similarities.
*  Maybe you can comment on it. C++ is like Wall Street and JavaScript is like Wall Street bets
*  from the recent events. It's like there's a chaotic community of all and there's some power
*  from that distributed crowd of people that ultimately- It's more thematic. It's more of
*  the people. It lets people in without requiring these credentials. I remember in the late 90s
*  into the noughties, people were all getting Java credentials. And I knew people and friends knew
*  people who became Java programmers. And you knew they really should have been like nature guides
*  or pilots. They hated programming, but they thought, I got to make money. I'm going to become
*  a Java programmer. Do you have some- Because it's such a monumental moment in our current history,
*  as a quick aside, do you have thoughts about this huge distributed crowd sourced financial happenings
*  with Wall Street bets? That's like nobody could have, well, you could have predicted, but the
*  scale and the impact of this kind of emergent behavior from independent parties that could
*  happen. Like I said, my own experience with the dismal science, as with physics, led me to reject
*  a lot of bad models. And economics was always compromised by politics, political economy.
*  You could also argue that it used to be a branch of moral philosophy, so it was concerned with the
*  good. And it became divorced and became sort of in this quasi-Newtonian way, just about everything's
*  just running by itself. Don't worry about it. This monopoly is crushing your Netscape company,
*  but that's just nature. And economics couldn't, or doesn't really have good models for the Wall
*  Street bets subreddit. They know how to squeeze a short, right? So the amazing thing is you have
*  Robinhood app, which was again, supposedly for the demos, for the people, and eliminated the fee
*  through various kinds of straddles or some kind of spread operation that helped them eliminate
*  the fee or eat the fee. And in fact, as a broker in these days, because it takes two days to settle,
*  there's counterparty risk, as they found out. And so the Wall Street bets people, the memes
*  are like the Terminator robot with the $600 Stimmi check and the hedge funds, the little girl hiding
*  under the desk. There is a problem, which I talked about in the recent podcast, which I'm conscious
*  of from the history of the web. And that is, you could say it's monopoly, which antitrust wasn't
*  enforced after US through Microsoft for a long time. And a lot of this was due to the money
*  interests buying control of politicians. And in Plato's five regimes, that's oligarchy.
*  That's where we are. And now we're seeing a fight against the oligarchs. I don't know if it'll work,
*  but you're definitely seeing it. And it's also kind of hackerish, right? It's got a hacker ethos.
*  Hey, Robin Hood, no fees. Oh, interesting. Hey, I can buy a fraction of a share in this thing,
*  or I can keep buying with my stimulus check. So I mentioned Hegel seeing Napoleon on the horse.
*  Hegel also talked about the cunning of reason that you have the sort of God sees history in full.
*  And if you believe in God, or we don't know the future, but there's always this sort of
*  flying the ointment, this unintended consequence that confounds the best plans of the powers that
*  be. And we're living through it. I'm glad it's not street warfare or mechanized warfare, because it
*  has been in the past. It's more like soft power. And people are fighting back.
*  Do you think it's possible? So JavaScript used to be for the front end of the web.
*  It's now increasingly so being used for back end, like running stuff that's like behind the scenes.
*  And it's also starting to be used quite a bit for things like TensorFlow.js. So starting to actually
*  use like these heavy duty applications that are using neural networks, machine learning,
*  and so on in the browser. Is it possible in 10, 20, 30 years that basically most of the world runs
*  on JavaScript? This is a dystopia and a nightmare to some people. When we did Asm.js and Web
*  Assembly, I would joke and meme people with scenes like Neo waking up in his pod in the matrix,
*  and he's all skinny and weak and hairless. And you realize in the future that you're living in some
*  simulation, it's all running on JavaScript, and you just scream forever. It's possible. Gary Bernhard
*  does these funny talks. He did What.js, and then he did this life and death of JavaScript. I think
*  it's called where he took some clever ideas that actually have a thread of credibility to them.
*  I mentioned software fault isolation. In the old days when we were using computers, we said,
*  we're going to use the Unix monolithic monitor. And it's the privileged program.
*  This is before you even had hardware rings of protection. Some of the early 60s operating
*  systems used hardware protection zones. But Unix is privileged, and the program that runs
*  user code in a process is hosted. It's the guest in the host, and you get to suspend it. You get
*  to kill it. If it crashes, it doesn't take down the whole OS. It's a wonderful idea.
*  But the call into the kernel is expensive. The system call, so-called. And this has even been
*  optimized now for things like getting the time of day so it doesn't actually enter the kernel.
*  And meanwhile, hardware architectures and virtualization techniques have gone in a
*  different direction, even to the point where you can do software fault isolation very cheaply
*  without entering the operating system kernels. You get unikernels and exokernels and very
*  lightweight VMs. And so Gary took this idea and said, JavaScript will take over computing because
*  the system call boundaries too expensive. So everything ends up in JavaScript with these
*  lighter weight isolation enforcement mechanisms. It's not totally beyond belief. It'd be Web
*  Assembly too. It's nice to ask you for advice. There's so many people that are interested in
*  starting to learning about programming, getting into this world. Is there some number of languages,
*  three to five programming languages that you would recommend people learn, or maybe
*  a broader advice on how to get started in programming?
*  Well, so you asked about machine learning and JavaScript is a general purpose language,
*  and it's a language that's not that great for doing matrix operations or doing parallel
*  programming, I would say, without using some extensions or some libraries that have some
*  magic in them. So if someone wanted to learn, there are amazing languages in the APL family
*  that are very useful for, I would say, linear algebra, which gets to a lot of the kernels
*  in machine learning. And so APL had like J and then K and their K variants because the guy that
*  did K is still going and he's the proprietary, but he's still innovating there. Python is used.
*  So people talk about TensorFlow.js. Well, it's not that surprising because Python was heavily used
*  for machine learning. And Python was always, they didn't have this fast just-in-time compiler
*  tradition. There were some projects that tried this and some of them were interesting.
*  PyPy was interesting. But the philosophy of Python was, oh, you need to go faster, write a C plugin
*  and drop into C code. So I think people should look at multiple languages because there are
*  different tools in the belt. If you're trying to do supervision or rapid prototyping, you want a
*  dynamic language, you want to throw things together and see what works. If you're trying to go down
*  to the metal very fast, well, I'm an old C hacker, but I was also the executive sponsor of Rust
*  at Mozilla. And Rust has now escaped from that sort of nest where it was born to be adopted by
*  a bunch of companies that have a foundation in the works. Some of the key core team members are
*  working now at Amazon and other places. So it looks like Rust has reached escape velocity.
*  Rust is an interesting language because one of our goals there, one of the reasons I sponsored it was
*  we were all tired of seeing those remote code execution vulnerabilities due to C and C++.
*  And we thought, can we have a safety property through a type and effect system or an ownership
*  system? And Rust has that. And that ownership system is interesting because it doesn't just
*  give you memory safety. There's a sort of theorem for free, a dual that falls out for
*  protection against data races. So Rust is better for low-level programming. You delimit your unsafe
*  code where you do have to be unsafe. And you can prove certain facts about memory safety and race
*  condition avoidance. And so I think people should learn these new languages. I think Go is a great
*  language I admire. The Unix people who did that, Ken Stoll was involved, Rob Pike, of course,
*  David, what's his name, and other people. Go is a huge success, really on the server side,
*  anywhere you have a lot of networking to do. And it's garbage collected, but it's also very
*  pragmatic. It has that sort of C flavor. As an old C hacker, I can't get used to the fact that they
*  swap the type and declarator in the declaration order. I haven't used Rust, but this is one of
*  the most respected and loved languages currently. So it's- Yeah, and it's still young. You look at
*  these things, JavaScript is now considered old. It's gone through so many versions that you can
*  fall in love with it all over again. 25 plus years, it's an adult. It should be out of the house.
*  But it could be around another 25 years. Cannot rule it out. So Rust will be around for a long
*  time. The longer you're around, the more likely you're Lindy and you're around your half-life.
*  A lot of people ask me, I'm often torn between recommending either Python or JavaScript as the
*  first language to play with. Because it's difficult because it's so easy to do JavaScript
*  incorrectly. It's much easier to do it correctly these days or well, learn about programming.
*  But the cool thing about JavaScript is that you can create stuff that will put a smile on your
*  face. As a developer, you can create stuff and it'll visually look like something and it'll do
*  stuff. It makes you feel good. It makes you fall in love with programming. With Python,
*  you could do the same. It's a little slower. With C++, it takes five to 10 years to write a program
*  that actually does something. So there's that tension between is JavaScript the right first
*  step or is it Python? I've been going back and forth on those two. My Python, it came from a
*  lineage of ABC, which was a pedagogical language in the Netherlands. It was a good teaching
*  language too. I think it is a good teaching language and it's a little more restrictive in
*  that if you misspell something in a way that JavaScript might let run, let reach runtime,
*  it'll get stopped at syntax check in Python. That's good for beginners. I think the sloppiness
*  that some people object to, people were just tweeting at me having just learned JavaScript.
*  They said, I can take a number and I can index into it and get undefined out of it as a property.
*  And why is that? A number is not an object. And I explained why it is because in Java,
*  the primitive types, which unfortunately are not objects, can be automatically boxed or wrapped
*  by an object. And I made that implicit. In Java, it's typed and you have to declare things and
*  you'll get type errors. But there are cases in Java where you get auto boxing or auto wrapping
*  because you've declared that you want it. In JavaScript, it just happens. So once I explained
*  it, I'm like, oh, wow, I get it. But it also means that you can commit a blunder that just-
*  You don't get punished for it, you don't detect.
*  You get an undefined value and you don't know where it came from.
*  I've been reading a lot about military history recently. And one way to paint the picture of
*  browsers, internet browsers, is through the various wars throughout its history. I don't know if
*  that's a useful way to look at it, but we've already talked a little bit about Netscape and
*  Internet Explorer in the early days. Can you tell the story of the different wars, if that's at all
*  an interesting way to look at it, of the 90s and to today?
*  Yeah. So I mentioned that Microsoft, which was convicted for it, did abuse its monopoly,
*  but they had a pretty good team by the time they did IE4. And Netscape, unfortunately,
*  I was like the second floor and I was friends with all the first floor people, the front end guys who
*  did the JavaScript event hookup and things like that. That team was fairly burnt out. And
*  I think having gone public, the upper management wanted to buy a bunch of companies to try to go
*  head to head with Microsoft. Didn't work, but buying a bunch of companies usually doesn't work.
*  I think the modern approach roughly is like Mark Zuckerberg took, which is to keep them at
*  arm's length and let them do their thing. And now that he's pulling WhatsApp in and people are
*  fleeing it because it's tied into the ad surveillance. But for a while, they're keeping
*  it separate. It really does work because you bought it for its value. It's complimentary and
*  you're not messing with it. With Netscape, when they bought a bunch of companies, they had some
*  of the first floor people or the founders burned out. They had newcomers who wanted their turn to
*  do the browser and they hadn't really done browsers or understood them. And so Netscape 4
*  was originally supposed to be three and it was so late they re-numbered it. We did a three release.
*  Jamie and a few others put some extra effort into. Secure Mime was supported in the built-in mail
*  program. And Netscape 4 was late and it was only on Windows at first. And Microsoft had really
*  started doing better like they do. They copy and the first version is trash and the second one,
*  you're starting to feel a little threatened. The third one, you can tell what's going to happen.
*  And the fourth one's good. And plus there's the benefit, like you said, that it comes as a
*  default browser. Yes. And yet Netscape screwing it up and Microsoft really putting some quality
*  people on it. IE4 was good. On Windows, it was good. And they did the dynamic HTML innovations.
*  The Scott Isaacs, my old buddy, a former accountant who programmed in basic and became what Microsoft
*  calls a program manager, which is kind of an elevated position. You can be a programmer or
*  an engineer track, but you switch to it and you sort of lead a lot of design and standards efforts.
*  And so Scott Isaac put in a lot of those funky HTML APIs that didn't quite have the same flavor
*  as the stuff that I did. And neither of them was like the later sort of verbose Java like DOM W3C
*  standardized, but IE4 was pretty darn good. I remember a friend, Scott Furman and I got
*  invited by Scott Isaacs to Gordon Beers since San Jose. They were doing a preview of IE4. This must
*  have been 1997. And Scott said, yeah, we've got, here's the new graphics stuff we're doing. We've
*  got something like your Netscape layers. We've got VML, a vector markup language. We can do
*  virtual reality. And Scott and I looked at each other and said, we're doomed.
*  Microsoft was starting to fire on all cylinders. So I have to give them credit for that,
*  even though they've used their market power. And maybe I shouldn't give them credit for having
*  the resources to hire talented people, but they did a credible job on IE4. What really was bad was
*  that phase of the browser wars ended with monopoly. And perhaps due to the antitrust case,
*  perhaps due to regulation in Europe, perhaps just due to Microsoft not liking dealing with
*  standardization, they let it rot. They just abandoned it IE5, IE5, IE6 later, but these were
*  not well maintained. They had a lot of security bugs. Browsers really closed and outdated too,
*  even though it was getting updated. It's just weird. Browsers like Mozilla and then Firefox
*  were adding tabs. Opera had a version of tabs and they didn't add tabs. And they pop up blocking,
*  something I should have done from the start. People realized that you can tell when the user
*  clicks something and it goes in JavaScript to open a little window that you can sort of inspect the
*  stack and see that the click originated that and it's probably okay. Whereas if you're just
*  loading a script and it opens a new window, that's a spam technique and you should block it.
*  Tabs were a brilliant innovation. Like you said, Opera had it, but I remember
*  fully switched to Firefox the moment. I remember the moments of first using tabs on Firefox
*  and not liking it for the first few minutes and then like, wait a minute.
*  You get the groove, yeah.
*  You get the groove and you understand. So that timing, what year was this? Because also as an
*  aspiring web designer, I used Table. We didn't mention Layout or CSS much. There's also a change
*  in the way the frames were going away. So there's a change in the way websites looked and behaved
*  and all that kind of stuff.
*  CSS finally, which Microsoft embraced with IE4 and Netscape and never really did right,
*  CSS became a better standard over time for doing Table Layout that relieved you of the need to use
*  what are called spacer GIFs, spacer GIFs, right? Images you would throw into space out tables.
*  The typographic power of the web has gotten better, but it's still not on the level of PDF
*  and you can't do advanced typography, but it's gotten really better. And even then tables were
*  getting better. If you were using Firefox, that would have been 2004 because it was called Firebird
*  until earlier that year.
*  Five. No, yeah, I think it wasn't. Well, I don't remember. It was a Firebird, which had tabs?
*  We had tabs the whole way. So it started out as Mozilla slash browser in 2002, became Phoenix.
*  There's a BIOS that has an embedded version of IE and they said, we're called Phoenix technologies.
*  You can't use Phoenix. And so we said, okay, we'll call it Firebird. And then this Australian
*  centered open source database project started really like in the true Mad Max style, just
*  screaming at us saying, you can't use Firebird. And I had to sort of be the ambassador and say,
*  okay, we're going to rename it. We don't believe you. You shouldn't have used it. We hate you.
*  And then we renamed it to Firefox. And they're like, ah, we love you. And then I don't haven't
*  heard of them ever since. But Firefox was a clever name. We had to think of something
*  distinctive. We wanted to keep the fire going. And it turns out there's a red panda, right?
*  It's a nickname for. So that's the second set of browser. Second browser wars. So what, how did
*  you, how was Firefox born? How's Mozilla born? Is there a
*  long story there too? So Netscape got acquired by AOL, which as I say was a reasonable happy ending
*  for a lot of people because Netscape otherwise was going to go out of business because Microsoft was
*  just killing its market. There was no way to charge for a browser. Windows came with IE.
*  IE4 was pretty good and Netscape 4 wasn't that good. It took a while to get better.
*  But the Netscape executive said, let's do an open source escape pod. And like in Star Wars,
*  A New Hope, the gunner won't shoot it because there's no life forms on board, right? It's not
*  a threat. And so we did Mozilla in 1998 and it looked like it was going to initially just give
*  the world an open source browser. But it's really hard to get people to work on this sort of hairball
*  that had been hacked up over by that point four years. It also couldn't have the crypto module
*  for secure sockets, so-called or now transport layer security. That was an electronic munition.
*  We were not allowed to release that in the full 1024 bit key strength. And yet people,
*  one of whom I happened to meet previously at SGI when I went on a sales support engineering trip,
*  Tim Hudson in Brisbane, Australia and Eric A. Young did what became OpenSSL. It was called SSL
*  EAY after Eric's initials. And Tim and Eric took their OpenSSL outside of the purview of the NSA
*  and the Department of Commerce and they stuck it into Mozilla's code. And that was perhaps the
*  best hack that was done in the first few months after we open sourced the browser.
*  We had other problems. The politics inside Netscape were riven by these acquisitions.
*  So the one acquisition that kind of messed up Netscape for also wanted to keep doing a proprietary
*  mail and groupware program, not Jamie Zawinski's mail program that was in Netscape two and three.
*  And they held it back from open source. We didn't have a mail program. It was just a browser.
*  We didn't know what AOL would do to us. Turns out they didn't interfere with us for a long time.
*  But Netscape wasn't the best steward of Mozilla. We were operating Mozilla as a pirate ship
*  without a legal entity. So most of us worked for Netscape under a separate organization.
*  And initially, the first engineering manager, Tom Paquin of Netscape, was the Mozilla
*  founding manager. But he left pretty quickly and he left me as the acting manager,
*  which is more like method acting in my case. And that was my first management stint. But then
*  someone who'd written the licenses, Mitchell Baker, she was a lawyer at Netscape. She was
*  involved in the open source license decision making and the actual writing and construction
*  of those licenses. That was Mitchell's job. Netscape public license and the truly open Mozilla
*  public license. And there were two because Netscape needed, because of some encumbered
*  code, needed some special rights. But that went away over time. Mitchell was always interested
*  in Mozilla and she came back from maternity leave and she said, I'll be the manager if you want.
*  And Jamie and I said, sure. And then Jamie quit. He quit after a year. He said, this didn't work.
*  I'm sorry. He acted like it was a total failure because Mozilla didn't restart the browser market.
*  But there's no way it could have. Netscape was still shipping variants of Netscape 4,
*  which was based on the old code. Mozilla was trying to re-architect code to make green
*  field for developers. It was one of my big goals. It wasn't a technical goal so much as,
*  again, a social goal. People wanted a more standard spaced browser. They wanted less of a hairball
*  that had been hacked on by ex-grad students starting four years prior. So we said, we're
*  going to make a modular code base. We're going to use a variant or an open source version of
*  Microsoft's component object model. It has reference counting and standardized VTables,
*  virtual calls and C++. And we're going to use JavaScript. We're going to have a bridge between
*  those two so you can script those components just like Java components. We're going to make a
*  portable front end with a markup language for the user interface. Not tables, not HTML, but custom
*  menus and drop downs and toolbars. And that was called Zool, XML user interface language.
*  And some real talent on the Netscape side delivered that. Dave Hyatt, who was instrumental in Zool,
*  Chris Watterson, Joe Hewitt, Blake Ross. Blake was an intern. He was like a high school aged
*  intern in Netscape. And at some point, we were innovating rapidly in the Mozilla world,
*  and Netscape was still caught up in this management mess from these acquisitions.
*  And it wasn't delivering. And every year they were wondering if AOL was going to come and start
*  beheading the executives because it doesn't do anything useful. And there was a thought you
*  should take the Netscape browser engine and put it in the Windows AOL client, which was the dial-up
*  client that all the increasingly aging users of AOL were using. Never happened. It would have been
*  a bit too big a change. So it wasn't clear why AOL bought Netscape. But as I said, they left it alone.
*  But Netscape didn't leave Mozilla alone. And so in 2001, Mitchell called me up and said,
*  I'm no longer employed. And I was like, what? You quit? No, no, this wasn't my choice.
*  And there was a layoff, which maybe accidentally or on purpose got rid of Mitchell. But the funny
*  thing was we had an open source project. We had a lot of the engineers on staff on our side. And we
*  had people we'd hired through the Mozilla community who were top notch. They'd risen, they came in
*  high quality, they knew the code, and they actually were better than the average or median hire of
*  Netscape. And so the funny thing was the executive who thought they'd gotten rid of Mitchell in the
*  layoff on the next week's community call around Mozilla and what to do, there's Mitchell.
*  And so this showed you can kind of transcend your boundaries of corporate open source if you get a
*  project that has enough loyalty, even among the paid staff. Because we had outside people
*  contributing. We had people at Red Hat and a few other places, but the majority of the hackers
*  were employed by Netscape. But a lot of them at that point had come from the community and others
*  got the community and wanted to work with it. And it was really the weakest engineers at Netscape who
*  didn't like Mozilla and didn't like the crucible of competing with the better programmers.
*  So if the project is good enough, it will rise, the Phoenix will rise out of the-
*  That's exactly right. And so we had this Mozilla code base that was getting better. In fact,
*  I think at some point in 2002 when we declared Mozilla 1.0, I engineered a roadmap that
*  successively through similar sort of six week, five week releases, like we all do with browser
*  releases nowadays, Chrome does and Firefox braves of three weeks. We got to a point where we said,
*  you know what? It doesn't suck. This is like the 1.0 that you want to release because if you hold
*  it back any longer to polish it, you're denying others the ability to use it. It's like pro
*  engineer, the mechanical CAD tool embedded the code. They embedded the layout engine.
*  And Mozilla 1.0 was like a Netscape communication suite. We had at that point gotten
*  male people to reintegrate male news and we had an editor for HTML and it felt like a 90s suite,
*  suiteware. And it felt kind of bloated and the people who were taking that Mozilla open source
*  and then adding Netscape flavor to it were not calling the shots right. And they were also under
*  ALS thumb a little bit and that they said, well, we should probably put the AL instant
*  messenger chiclet on the toolbar and we should put the ICQ, the other messaging system that AL
*  had acquired. We should put the ICQ button on the toolbar. And pretty soon Netscape looked like
*  a bit of a NASCAR, a badged version of Mozilla. And that also made Mozilla more popular. And yet
*  they had contrived to fire or lay off the leader and we carried on with an open source structure
*  where Mozilla was still, Mitchell was calling sort of management or project level shots and I was
*  calling technical shots. And we had a popular suite, but we thought, why not make it just a browser?
*  Because it'll be simpler. It'll do one job well. And even then we can strip it down by having
*  extensions. So Dave Hyatt and Blake Ross, the high school aged intern, did the first version,
*  which was called Mozilla slash browser. It was very small group of us, Ian Hicks and Asa Dotsler,
*  me, Joe Hewitt and Hyatt and Blake. And Hyatt was really the senior hacker. He'd done all these
*  things like amazing cross-platform menus through the user interface market language. And he knew
*  how to do tab browsing. He implemented it natively on Mac OS at the time in Camino,
*  originally called Camera. He'd written multiple rotations, which was a thing programmers should
*  do. It's like the VA team did for those missing years when the rest of the Chrome team's like,
*  where's V8? In fact, Dave's wife, Rebecca told me a story about when they were at UIUC,
*  they were also University of Illinois grad students. There was an assignment. It was a
*  programming assignment. It was supposed to be due at the end of the semester. And Dave's friend
*  was this, I'm going to go think and I'm going to design and I'm going to make this platonic,
*  perfect form of the program. And then I'm going to write it at the end when it's due. And Hyatt
*  just went in and started hacking. And he wrote one version, he wrote a second version, a third
*  version. End of the semester comes around. The friend's not doing too well. It wasn't perfect
*  and it wasn't written. I'm not sure how that story ended for him, but Dave's version was a
*  fifth iteration. It was great. And so he'd done that with everything you need in a tab browser.
*  And this really showed well in Phoenix, what we called Phoenix and I had to rename two more times.
*  And Blake went to Stanford. He became a Stanford student and couldn't work on it.
*  Dave Hyatt went to Apple in 2001. He was one of the founding Safari team members.
*  Interesting. Wow. But he was still blogging about tab browsing. I think Apple at some point said-
*  Safari have tab browsing?
*  Yeah. But it was because of Hyatt. Hyatt was quite a feather in their cap. Don Melton,
*  who had been the engineering manager for Safari from the beginning, had been in that same also.
*  And so this is diaspora of talent. And yet Hyatt was still kind of writing blog posts about how
*  to do tabs. And at some point, Apple said, don't blog about that. That's our proprietary tab
*  technology. And it's like, no, it's not. It was an opera and I've refined it. So we had to replace
*  people and we had Ben Goodger, a New Zealander we hired at Netscape. And he stepped in to be the
*  Firefox lead. And we also had this weird circumstance where AOL finally did notice that
*  Netscape was kind of an albatross, that they bought it for no particular benefit.
*  And even then the AOL politics were also heinous, sort of East Coast politics. I remember taking two
*  trips there because I was a principal engineer. And so us principal engineers got trotted out to
*  do dog and pony shows in Dulles, Virginia. And the AOL Opera Management was very East Coast in
*  flavor. And they were at that time merging with Time Warner, which did not go well. So one of these
*  years we went out there and we were all doing dog and pony shows and there were these characters
*  that were sort of like marketing guys. One of them was wearing a cravat and one was named Reggie. And
*  they were very you rather than non you. Or they were like what's Stoneman's Metropolitan film,
*  UHB, urban haute bourgeoisie. They were funny and they were kind of useless and kind of preppy.
*  And then the next year we went back and I said, where's Reggie? And it's like, oh, Reggie's not
*  here anymore because Time Warner realized that the merger wasn't in their interest either. And then
*  the sort of knives came out. And these mergers rarely work, right? This is very difficult. You
*  get these giant companies and they think there's going to be synergy. That was the late 90s watch
*  word. And there wasn't synergy with AOL buying Netscape and there wasn't synergy with Time Warner.
*  But did AOL ever really work? Was it ever really cool? Like the same kind of fire and excitement
*  that Firefox eventually created, was that ever there in AOL? AOL was the right time to do a dial
*  up service that got distribution by basically leaflet bombing compact disks on the country.
*  And they beat out CompuServe and the other ones, Prodigy, and then the web happened. And so you had
*  almost like this isolated continent, like some of the evolutionary biologists I follow make fun of
*  the the funny large mammal, marsupial mammals of Australia, how silly they are. And so AOL is like
*  Australian. And you saw it over time because they kept aging and they were using AOL to get online
*  and they couldn't really use a web browser. And it became sort of a
*  valued cohort because they still have relatively high socioeconomic status and they have grandchildren,
*  but it's going away. It's dying at some point. Towards the end of the aughts, that decade and
*  then to the decade 2010 plus that Firefox became this incredible. I forget when Chrome came out,
*  but 2008, September 2008. But Firefox was the sexy, cool thing that represented a lot of the
*  cutting edge technologies and all that kind of stuff. It was amazing. Tim O'Reilly and John
*  Battelle did the first Web2 conference, which eventually became huge and they split it. But
*  that was in 2004. That's right. When Firefox was out, Craigslist was huge. It was killing classified
*  revenue for newspapers. But there was just this ferment. People starting Wikipedia along there.
*  Gmail was already done and it was an impressive web mail. There were others before it like Hotmail,
*  but Gmail was really impressive from Google and Google Maps. People started seeing what could be
*  done. They thought, how can you drag the map around and how does that work? It was all JavaScript
*  and images. Gmail was 2003, 2004? Yeah, it actually started quite early. It might have been 2002 or
*  2003. But by the time we started dealing with Google and Firefox to get the search deal,
*  which was the main revenue source for Mozilla and still is, 2004, early Sergey Brin's, one of his
*  trusted engineer guys, Fritz Schneider, made contact with me at Mozilla. We started talking
*  and we realized search and browser need each other. This is deeply true. This is still true.
*  This is why a lot of the search engines have their own browsers. Yeah. In case people don't know,
*  the main revenue source for the browser is the default search engine, which is incredible to
*  think about that that is a revenue source. It's a little bit sad. Yeah. It leads to this capture
*  or kill effect where you have the search engine own its own browser and other browsers may struggle
*  to get the distribution we talked about earlier. You said you've figured out that Google is working
*  on its own browser at some point there. 2006, yeah. 2006. Would you say Firefox versus,
*  was Internet Explorer part of the war here or was it Firefox versus Chrome?
*  Firefox didn't quite cause Microsoft to reconvene IE. They did do IE 7. I remember being on a plane
*  back from a JavaScript standards meeting from Seattle, from Redmond. There was some Microsoft
*  guy in front of me. Turns out my wife knew him from her past life before we married. He was just this
*  bearded big guy and he was like, we should have just killed Firefox in the cradle. All we needed
*  to do was add pop-up blocking in tabs and we could have made Internet Explorer kill Firefox.
*  It's like, should have, could have, would have, pal. I was right behind him, oh, hearing this.
*  But they didn't. They were slow and IE 7 wasn't that great. What really got them started, I think,
*  was Chrome. I talked to Larry Page in 2005. I think I said, we're talking about the Firefox
*  relationship, but he was also saying, what about WebKit? This was Apple's version of the old KHTML
*  engine from Linux, the KDE side of Linux that was used in the Conqueror browser, all spelled with
*  K's that Apple had forked. In 2005 was when Apple's principals, including Dave Hyatt,
*  Maciej Stokowiak, some of my friends who are still there said, we must stop patch bombing this poor
*  KHTML project. We should make a proper Mozilla-like organization, WebKit.org. Now, it wasn't a
*  separate nonprofit or anything. It was still Apple. It was Apple controlled, but they made their fork
*  first class and they made it be something that they all worked in and lived in. That was before
*  Chrome. Then, Chrome, Larry Page said, what about WebKit? I said, yeah, it's nice. I have friends
*  who work on it. You might use that if you do your own browser. Why don't you do your own browser?
*  Don't worry about Firefox. You should do your own browser. You can have your own opinion of how it
*  should work. Sure enough, they did. By 2006, we knew they'd been working on it. Some of my friends
*  who'd been at Netscape did the original demo. The demo wasn't what you thought. It didn't have the
*  fast JavaScript yet that was still off in Denmark and on a farm. Did it have tabs? It had tabs
*  because all browsers had tabs at this point. It had this software fault isolation I mentioned.
*  It was through process isolation. In theory, each tab has some operating system process.
*  What's going to take your tab down? Well, WebKit has bugs that can crash it, but Flash was still
*  big then. All the restaurant sites remember, and Flash crashed a lot. The demo that I heard about
*  my friends at Netscape, as a lot of people did, inside Google was the sad tab. They showed an
*  early version of Chrome, which is just this bare bones tab browser. They loaded a site with a known
*  flash vault, and then suddenly Flash crashes. Everyone expected the whole browser to go down,
*  but instead you got this little sad face in the tab. You could reload it, and there it is again.
*  This was an improvement. It was a real move for security. It was based on a company they acquired
*  called Green Border. They had some really big brains like Olfar Erlingson, I think, was involved.
*  They had done some exotic security stuff, but they ended up simplifying it to this process isolation.
*  It was good. Firefox didn't have it at the time, so we were still struggling with security bugs.
*  We knew Chrome was coming, but it took two more years to come out.
*  And we were still getting the Google search revenue. We were still making Google the default
*  engine, and Firefox was still growing. Firefox grew, I think, until 2011. That was when it peaked.
*  As it started falling, it was because of Chrome. Chrome came out in 2008, and it had a comic book
*  that leaked accidentally that showed some of the people who worked on it. Lars Bock was in there,
*  and so on. It was kind of a soft launch because they didn't market it heavily. They didn't push
*  distribution, but Google had reason to worry about distribution because Microsoft was
*  doing a search engine, Bing, since 2007. In fact, when they came out with Bing,
*  Google was worried that Microsoft would just brute force switch the default browser in
*  everyone's Internet Explorer or even Firefox on Windows to Bing from Google.
*  Microsoft wasn't, I think, ready to dare the antitrust cops that way, even though they'd
*  gone to sleep. I don't think Bing was ready either. But just in case it happened, Sundar
*  Pichai, who rose very well based on this work, was in charge of getting distribution deals.
*  He got Google Toolbar and Google Desktop Search distribution. If you remember those pieces of
*  software, those were like desktop extensions, toolbars or operating system extensions for
*  doing desktop search in your local files. That's right.
*  Mac OS Spotlight. Sadly, I doubt it.
*  It all died. There were some features that we still missed that didn't make it into Chrome.
*  But Sundar got OEMs to bundle those. Then he got enough of those deals that by 2007 or eight,
*  Google felt, well, if Microsoft does the worst and tries to force Bing, we can reach in and reset it
*  with that point of presence. That was good for Sundar's career, and it was good for Google,
*  but it never came to pass that they had to defend. Microsoft was still slow. By the time they saw
*  Chrome come out, then they did what would have been IE9. Then they said, we're going to have a
*  fast JavaScript engine to Chakra, Chakra Core. They did okay. They were another process isolated,
*  fast JavaScript browser, tab browser. It sounds like there's a deep fundamental
*  coupling of search engine and browser that's mixing this whole thing up. Obviously, Firefox
*  doesn't have a search engine. You're partnering with somebody with a search engine, with Yahoo,
*  or with Google, or so on. They tried Yahoo. That was unfortunate because I think
*  even though Marissa Mayer talked about it, she never pulled it off. They never restored the search
*  team that had been laid off. I believe Carol Bartz was running Yahoo when Carol said,
*  I've got to get rid of one of the three expensive things. I'm going to get rid of search.
*  Those researchers went to Google and Microsoft. There was no way to put Yahoo search back together.
*  When Firefox tried switching all their users who'd stuck with a default from Google to Yahoo,
*  it was mid-December 2014, a bunch of users said, what just happened to my Firefox? Others didn't
*  notice right away, but over time they did. Over the next year, the traffic just went away for Yahoo.
*  Yet they were obliged, I understand it. I don't have inside knowledge, but this is leaked out.
*  Danny Sullivan has written about it, Search Engine Land. I think the deal was fixed payments to Mozilla.
*  Mozilla was getting a bunch of money for traffic that wasn't staying because users were
*  resetting their default. This shows how defaults are important, but they have to be good enough
*  that the user doesn't override them. A lot of the commercial value in popular apps is what are the
*  default settings? What is the default search? Oftentimes there's something just like you said,
*  if there's something compelling, that also can beat out the default, like tab browsing and so on.
*  We'll talk about Brave browser. It feels like now we're in this third stage where there's Chrome,
*  Firefox, Edge, I guess it's called, and Brave. These all seem like really exciting, I don't know,
*  innovative browsers. They're all copying off of each other, picking up the good stuff.
*  There's evolution again, especially on tracking protection. Privacy is this global
*  wave that's rising. I like to call it a wave because it's a large, somewhat chaotic structure.
*  It's not a unitary good. You can't say, I'm buying privacy for $3. I'm paying $3 for privacy.
*  Some people think a VPN does this and are disappointed when it fails them, but
*  often people use VPNs for region unlocking video or getting the US Netflix catalog.
*  Exactly. Privacy is not a unitary good. It's complex and people are understanding it only
*  over time and as they get burned, but there's a genie that's not going back in the bottle there.
*  People are fed up. Apple has responded to this. Apple was always making Safari, I think, more
*  of a privacy branded browser from the very beginning. I think this is probably Steve Jobs.
*  Safari had private windows, private tabs before Firefox did. These are only private in the sense
*  that they don't leave local traces if you don't want them to. Turns out Safari does keep them
*  around between shutdown. The canonical model is no local traces after you close the private window.
*  No leftover traces that you went to some site that you were embarrassed by or
*  bought a gift for somebody you wanted to keep secret.
*  But there's still some level of tracking.
*  There's network tracking. Network privacy is not guaranteed at all because you're using the same
*  internet and ISP as a public window, a non-private window. But, Safari had that early on. They also
*  had a cookie blocking policy that might take a little explaining. If you know what a cookie is,
*  it's a little bit of storage in the browser indexed by the name of the site. It's really
*  only the main name of the site like bofa.com or something like npr.org. Every site can store
*  some information in a cookie. Every time it's contacted by the browser, the previous version
*  is sent back and in the response from the server, the cookie is updated. It's this little bit of
*  storage in the browser that the site can keep updating and it can store an encrypted version
*  of your login credentials with a timestamp so you can stay logged in without having to retype your
*  password every time you navigate, which is how it would be if you didn't have cookies.
*  The web protocols, especially in the 90s, are so-called stateless protocols. So,
*  you go to your bank, you log in, you go from your login confirmed page to your account view.
*  If you didn't have a cookie, you'd be logging in again.
*  Every time you type in a password.
*  So, that was a great thing about cookies. Lou Montulli did it in a hurry in 1994 before I joined
*  that scape and he did it for really holding that kind of credential. But even then, there was the
*  image element embedded in the page and the image gets fetched possibly from a different server
*  and that request carries the last cookie, which could be empty at first,
*  and the response carries the updated cookie. So, just by having images and cookies, you got
*  tracking because that image server can be serving a little one by one pixel and they still use the
*  word pixel in AdTech. And that pixel can be served from the same server embedded differently with
*  different URL spellings in the New York Times and ESPN. And as you go from one to the other,
*  the image server can say, I haven't got a cookie for you. It's empty initially. I'm going to assign
*  you user number 1234. I'm going to put a database entry in. And I see, by the way, I always fetched
*  the name of the path part of the URL that I was in the New York Times. So, you're a New York Times
*  reader. And then you hit ESPN, same thing. And the database gets updated and the number,
*  user 1234 indexes in the database to a profile of you. You've been tracked. This was not intended.
*  And it was too late to undo by the time I got the Netscape. I think Lou wanted to do Twinkies,
*  he called them. And he was trying to solve several problems. He wanted them to be bigger
*  because initially cookies had a short size limit. I think he wanted to solve the third party problem.
*  But Tom Paquin, the engineering manager said, nope, no Twinkies, just cookies. We're done.
*  You're done, son. And that's how a lot of that stuff was. That's how JavaScript got frozen like
*  a flying amber in some ways with that sloppy quality operator that I made because of the
*  early adopters. And the cookie got stuck with this tracking hazard. And then because JavaScript's
*  can be like images, they're embedded in the page. By the time of Netscape 3, I made that work.
*  You can get a request with the last cookie value and the response updates it. That's a tracking
*  mechanism. And that's why you don't even need images to track. Now you just use scripts.
*  So this whole tracking economy evolved and it depended on these accidents of the 90s,
*  these unintended consequences. Well, it created some of the richest companies in the world.
*  Right. I mean, it's the social media. All I got was t-shirts.
*  All I got is this crappy t-shirt. Yeah. I mean, so that's the fundamental problem the world is
*  facing now. They're looking at what social media has created and they're looking at,
*  and like a world is looking at itself in the mirror and seeing that privacy is actually
*  something as opposed to like a nice thing to have. It's something that is actually should be
*  fundamental to the way we interact with the world as part of our tooling. And that's where
*  the brave browser comes in. And I suppose others as well are playing with this idea,
*  but brave is at the forefront of that. So maybe can you like describe what brave is and what are
*  its key principles and what's broken? What is it brave trying to fix?
*  So when I realized that these accidents, like the third party cookie, the image or script that's
*  tracking you or the JavaScript that can do it invisibly now, that all this stuff wasn't intended
*  and that Firefox had supported extensions that block some of these things, I thought
*  probably we should have browsers just block some of these things by default. These were not intended
*  and they're now unsafe. They're tracking you. There could be data breaches, the malware distribution,
*  bullying and PSY ops and other attacks on people. Block that stuff. Block that JavaScript. I'm Dr.
*  Frankenstein. I've got to deal with a monster here. But obviously you go to Gmail, there's so much
*  a script there to make that amazing web client. That's okay. That's first party JavaScript.
*  So how do you tell the first from the third party? And it's not easy. It's not a matter of just
*  what's embedded from a different server because a lot of publishers use benign scripts from
*  unrelated domains or apparently unrelated domains. So you end up having to develop a human and machine
*  learning practice around blocking. And at Brave, we did that from the start and built a research
*  team to help drive it and automate it. We realized that protecting people needed machine learning.
*  And around 2017 spring, I talked to my friends at Apple about this too, and they were also doing
*  what they call intelligent tracking prevention, which uses local machine learning in the browser.
*  And the funny thing is, you know, great minds think alike, they were taking their third party
*  cookie blocker that was in Safari from the old days and making it not have a big loophole. Because
*  what they did was in 2003 when Safari came out, they said, we're going to block cookies that are
*  from those third party embedded elements where you've never visited that site before. So I'm
*  going to pick an ad company that got sold to AT&T, so I'm not picking on anybody unfairly,
*  appnexus.com. Have you ever been to appnexus.com? Nope. I've never been there, but I guarantee you
*  10 years ago, you probably had, if you were using Firefox, you had a cookie, third party cookie,
*  because you were being tracked by them. And they were using that cookie to build up a profile of
*  you. In Safari, as long as the user never went to appnexus, that cookie would not be set. And that
*  was a real move for privacy early on when jobs were still around in Safari. But it had this loophole
*  that if you do go to appnexus, then why it's okay to be a third party cookie. And so appnexus did
*  something very naughty. They took their ad partners to put the actual ad you click on.
*  And they said, hey, add a little script so that when somebody clicks on the ad, before it goes to
*  your landing page, redirect to appnexus, and we'll redirect to the landing page. And by doing that,
*  they set a first party cookie and they got whitelisted. So it was a loophole they exploited.
*  Intelligent tracking prevention in Safari was sophisticated enough to counteract this,
*  and it did other things. And it's evolved since they did it. And we've evolved Brave too. And so
*  when I say machine and human learning, there's a real set of techniques here. They have to fight.
*  This is a fascinating problem.
*  Fingerprinting, right? Anytime you have a little bit of storage in the browser associated with
*  a website, if the bad guy can get 32 websites, each one has a bit of storage, that's 32 bits.
*  You can turn the bit on or off. You can make 4 billion numbers. You can make an identifier.
*  It's called a super cookie sometimes. There are weaker ways that are statistical.
*  They're called fingerprinting. You have to block all of them. And you have to not only automate,
*  you want to work in the web standards body to put privacy in by default, by design, from the get-go,
*  not add it as an afterthought, or go hog wild with new web APIs that add a bunch more local storage
*  or fingerprint surface area. And that's been a struggle too, because guess who's the new Microsoft
*  in the standards body? It's Google. And they're not in favor of privacy first. They want to do
*  privacy their way only under, I would say, market pressure. But with Apple and with Brave leading
*  the way, we block third-party cookies almost without exception. So we just block them. And
*  that gives us a very strong privacy benefit, but it also means some sites just don't work right,
*  embedded YouTube videos might not work right. So we're adapting in a similar way to Apple's
*  done with ITP to make third-party cookies blocked, but to sort of simulate what looks like a working
*  third-party cookie for the site. It essentially tries to partition each site and its third parties
*  into its own sort of cookie jar. Got it. And so, like you said, is this both like a human
*  fine-tuning issue and a machine learning problem? Yes. And as the humans learn, then they train the
*  machine learning. But maybe Google aside or including Google, there's millions of dollars,
*  if not billions of dollars to be made from fighting the ways of Brave. That's right. And it's been an
*  interesting change from when we started in 2015. When we started,
*  ad blocking extensions, AdBlock Plus was one of the big ones that started on Firefox in 2006,
*  I believe, had gotten to a certain level of use around the world. And browsers like UC Web, UC
*  browser in Asia had some amount of ad blocking built in and on by default. So a PageFair was a
*  startup and they measured ad blocking adoption and they tried to say, hey, publishers, you're,
*  you know, 30% of the visitors to Pitchfork or Wired to Con and NAS properties are using ad
*  blockers. If we can somehow convince them to lower their ad blocking for your site, that could be
*  like a 43% lift, right? And you have three sevenths. Well, that's easier said than done.
*  And PageFair and others source point that many others tried to either smuggle ads through or
*  cajole the user into letting ads appear. And it didn't really work. And meanwhile, the ad blocking
*  adoption has just continued, intelligent tracking prevention in Safari in 2017, Brave from 2016 on
*  with very strong cookie blocking and other protections. And this is not going away. The
*  publishers used to rage against it. Like we would try to say, we can help you. You're dealing with
*  users who are already blocking all your ads. We can try to put back some economics that help the
*  user and you that led to the basic attention token that we started with Bitcoin. We can be your friend.
*  Don't just fingerprint us as an ad blocker and treat us as an enemy. But in 2015 or 16, it was
*  like, ah, you're an ad blocker. Get out of here. I hate you. And by 2017 or 18, it's like something's
*  happening. The ad blocking is not stopping and we're all getting sort of pulled on the Google's
*  plantation through AMP, AMP or we're getting killed by the Google ad system we use because
*  it's taking all the revenue or it's permitting or some other vendors we use are permitting ad fraud.
*  And so a fake New York Times is getting paid by the marketer running an ad that a bot clicks on.
*  And the real New York Times that's supposed to get the ad doesn't get it.
*  And there's something really broken about that kind of system.
*  That fraud is mediated through Google's ad exchange, which is the biggest of them all.
*  And Google takes a fee. There's a flip side of that, which is malware distribution,
*  malvertising where fake advertisers put malware payloads or exploit kit loaders in JavaScript and
*  they smuggle them in ads onto real publisher pages. The ad exchange takes the fee. Now,
*  I'm not a lawyer. I'm not going to say this is a RICO predicate, but why is the ad exchange
*  facilitating fraud and malware distribution and taking a fee? It's not right.
*  As opposed to just fighting. This is the really interesting thing about Brave is
*  as opposed to just fighting and then being treated like an ad blocker, you're providing an alternate.
*  There's a philosophical idea here that might change the nature of the internet with a basic
*  attention token. Yes. Maybe what is basic attention token BAT and how does it work?
*  Okay. I'll tell the story first by saying how I came to it. I realized for a long time at Firefox,
*  we were dependent on this Google search deal and I thought, now that Chrome's out, maybe that's
*  going to go away. At some point, Google will say, Firefox, like old Yeller, you saved me from the
*  rabid beast. Now you have to shoot you in the head. Done your job. Sad but true. Goodbye.
*  What could we do? And I think Mozilla doesn't know what to do. This is something that
*  I couldn't solve there and I don't think they can solve. But I thought, why is the browser the
*  sort of passive servant of these big tech companies? Why is it a blind runtime for
*  ad tech JavaScripts, including from Google? Why doesn't it block some? And if it blocks some,
*  why can't it reconnect users, readers, fans with publishers, creators, websites?
*  Why can't it help people make direct payments or even possibly get an ad revenue share for private
*  ads that are placed in the browser? The ads are all placed in the browser. Some people have this
*  sort of model that the server's painting the ad into some flash combined package or into some
*  giant image and then it all gets sent down. That's not how it works. All the ads you see on the web
*  are placed in your browser by calling out to various ad tech partners and Google's among them.
*  And so if you block those scripts, you break the advertising flow of money from the brands
*  and their agencies to the publishers. And if you want to reconnect it directly with the user,
*  you have limited choices. The user generally isn't going to sign up with a
*  ACH bank connection or a credit card. The publisher isn't going to sign up the user
*  except as a subscriber and then they're going to overcharge you because they want you to cross
*  up size all the content and buy more than you read and all that stuff. And how many, people
*  are doing great who are big names like New York Times and The Washington Post, but how many
*  subscriptions are you as a user going to pay for? This is why startups like Tony Hale's
*  Scroll are trying to do a portable subscription system. But by the way, just on a small tangent
*  there, even The New York Times is really annoying how difficult it is to subscribe.
*  There's way too many clicks. They don't make it easy. I had friends a few years ago, I think they
*  fixed this, who would pay for the paper and then they'd go online and they get upcharged for the
*  digital and there was no break. There was no connection between them. But publishers are not
*  that technical and they can't all get you to subscribe. You can't have a thousand subscriptions.
*  So for a long time people talked about micro payments. There was Blendle in the Netherlands,
*  which came to the US but didn't grow. And I thought if you have just a browser and it's
*  protecting you by blocking all this ad tech tracking chunk, it can provide you an option
*  that uses cryptocurrency to let you support your favorite sites and even YouTube channels.
*  And that way, prototype with Bitcoin. And that meant the user had to be of means to contribute
*  and willing to contribute. But it could be done on the Bitcoin blockchain and it could be fairly
*  efficient even though Bitcoin went through a period when we had this prototype running in 2016
*  into 2017 where Bitcoin was very congested and very slow to confirm and the fees got very high.
*  And a lot of users who were not Bitcoin maximalist or even experienced,
*  we helped them out by embedding a Coinbase buy widget and they had the income to buy,
*  but it was hard. It was like, do I buy $5 a month? But the fee is like 450. I better buy in larger
*  batches. And they're like, I don't want to own that much Bitcoin. So it became this painful thing.
*  And the real idea that I had of private ads that pay the user a rev share couldn't be realized
*  alone in that kind of system. In these cryptocurrency systems, especially with the
*  blockchain we switched to Ethereum, you can have smart contracts. The Bitcoin system is not turn
*  complete. So what you can do with the script is more limited, but you can still do sort of clever
*  things even with Bitcoin script. What we wanted to do was sort of a three-sided ecosystem. We
*  wanted users, creators or publishers and advertisers. And we wanted the advertisers to put money in just
*  like they do today, but without going through the Googles and the app nexuses and all these other
*  ad tech companies, because those companies take out a huge cut. The Guardian in the UK once did an
*  experiment for a month. They bought out their own ad space. They put in a pound and they were paid
*  30 pence. 70% was coming out to the intermediary vendors they were using. And that's like the
*  opposite of what the app store does. The app store takes 30% and gives the publisher 70%. So
*  pretty broken. In the old days of the Superstation TBS, the media owner would get 85%. So these splits
*  have become really unbalanced and the middle players, the ad tech vendors are taking out way
*  too much money. And they're doing something worse, which has been noticed. They're letting
*  not just the malware vendors, but also the ad fraud side, which fakes the publishers,
*  and clickbait merchants come in and steal traffic from good sites. Because once you have a certain
*  audience identified at one site, Jason Calconis told me this about his experience with, I guess
*  it was Engadget, which site he was running. But once he started using an ad partner that was
*  sharing his audience information across multiple sites, he saw his competitors stealing all his
*  traffic. And then what's worse is the clickbait sites that just have much cheaper rates steal all
*  that traffic. And that facilitates fraud, it facilitates fake news, all sorts of problems.
*  So Grape blocks it and then we give users the ability to give back. And because we invented the
*  basic attention token in Ethereum, we can do this three-way split and we can give users a share of
*  the revenue. And if they want to take it out, they can. Now, unfortunately for us and for all
*  blockchain, the regulators are saying, we're going to have to know who you are. There's the
*  Treasury Department's FinCEN agency, there's the Office of Foreign Asset Controls, OFAC,
*  there's the other regulators in the federal government that take a very dark look at things
*  like money laundering and sending money to someone named Osama Bin Laden. So
*  compliance starts to come in and even now they're threatening for pure Bitcoin sending to some
*  address. If you're a Coinbase, you're going to have to know who's at that address.
*  You're going to make the actual identities of people involved.
*  Yeah. Now with Coinbase members, you sign up and they know you and they comply with
*  regulations. They're a regulated money services business. But if somebody's using their own
*  so-called self-custodial wallet where they have the hardware private key and they're not named
*  and they want to send to that address, our friends in the federal government are talking
*  about requiring at some threshold knowing who that is. So some threshold that's unreasonable.
*  It's not that big. Yeah. I don't know how this will play out. I think crypto is here to stay.
*  I think the beauty of being able to send peer to peer without any bank in the middle without any
*  huge wire charge and two-day delay and all that nonsense is beautiful. And I've used it and I
*  love it. But we're pragmatistic brave about crypto and we realized that anything like a revenue split,
*  we can't facilitate without being licensed in a certain way and it requires knowing who the user
*  is. So our default mode doesn't know who the user is. It instead imputes to the user's browser
*  some of the revenue and allows that browser to steer it back to the creators. And we do
*  have to identify the creators. But as things improve and who knows how it'll play out,
*  there should come a day when this full vision can be done more fully on a blockchain. But
*  regulations and the practicalities of today's blockchains, which are not that fast
*  and not anonymous over time, you fingerprint yourself over time. We do some of this with
*  the browser. So one of the ideas of the basic attention token is to make a hybrid system that's
*  stronger than blockchain alone. It's the browser and the blockchain. And the browser is this trusted
*  endpoints software. It's this universal app. Everyone uses browsers. The bigger the screen,
*  the more you're in the browser and the less you install, you know, fat clients for things.
*  I use Slack on Mac OS and it's like a browser. It's based on an electron framework we use to use.
*  And it's just, it's not that great. Some people at Brave use Slack in Brave as a-
*  In the browser. Yeah.
*  In the browser. Yeah. I use that often. Yeah.
*  And I noticed on the iPad, I use apps less. The smaller the screen,
*  the browser got handicapped by Apple and Android both. And it also can be slower or not have the
*  right affordances, the interface with the security limited APIs. But in principle,
*  with the right permissioning, you can make the web browser just as good as any app. You make it be a
*  super app. And that's part of our mission at Brave. So we want to have the economics that got captured
*  by these big tech companies through tracking and through social networks. We want to block that for
*  your own safety and then let you opt into a cleaner world where you keep your data defended in your
*  browser and you can actually realize value from it. So the way our ad system works,
*  I mentioned it being private, but how does that work? We don't see your data at all.
*  All browsers are sort of the mother of all data feeds, your history,
*  all your searches at all engines. Each engine sees the queries you send to it,
*  but it doesn't see the others, but the browser sees them all. Machine learning in the browser
*  that you can opt into can study all that in a very complete way and do a better job than Google does.
*  Google has cookie and scripts across the web from acquiring DoubleClick. They have YouTube,
*  they have Android, they have Search, which is still their big revenue layer,
*  but they don't see everything. The browser sees everything. And if it can do a good job locally,
*  and this is not advanced machine learning, this is not TensorFlow, this is like SVMs now, NaiveBay,
*  then you can match intense signals from those data feeds, the searches, the queries, the history,
*  how much you're scrolling down a page, how much you redid a search. It's all blind browser
*  algorithm. We don't see that data. And then pick the best ad from a fixed catalog per day.
*  And the catalog is fixed across a large population per day, and it only updates once a day because
*  new offers come in and old ones expire, sometimes every week or every month. And that catalog,
*  and there can be many such catalogs, is sold by our direct sales team. And so we're making
*  anonymous audience available to advertisers without the advertisers tracking them. Instead,
*  each browser is a little machine learning system that's picking the best catalog entry. Now,
*  the catalog is not the ads. Those are big. It's a video or a webpage. It's just the link to an
*  edge cache. And there are many such edge caches. We're not trying to protect them from seeing your
*  IP address. It's not really feasible. We could use Tor, but we don't yet. And some keywords about
*  the ad. So it's basically like metadata and a link. And that's what the catalog consists of,
*  and that's what the machine learning pick. And the machine learning is learning about
*  you specifically locally in order to choose from the catalog of different ads. Couldn't this
*  possibly be like a multi-billion dollar? Isn't this taken on the Google ad? So like what,
*  I mean, one question to ask that there seems to be some really profound ideas here that are
*  different than what the internet has grown up to be. If brave or something like brave,
*  the ideas, the fundamental philosophical ideas underlying brave win out and runs 95% of the
*  internet. How does that change? What are the major things that changes about the internet?
*  So social networks and then the creatives like YouTube creators and all that kind of stuff.
*  So let's talk about that. First of all, if brave gets 95%, I'm going to demand a recount because
*  I won't believe it. I don't know. I think we're trying to put things into web standards that
*  can be standardized across browsers. So the main value of brave will be the trust users have in us
*  and our ability to give the best deal to users. So 70% of the gross ad revenue we give to the user.
*  And if they go through that KYC process, as I mentioned, they can take it out. They can also
*  give it back. They can take some out, give the rest back. They can add basic attention tokens
*  to give back. Some of them turn off the ads because just don't like ads, but they put in $20 a month.
*  So I believe Zucco of ZCash frame does that. And that's very generous because the browser is just
*  anonymously based on his browsing, sort of keeping score on how much time he spent on this video,
*  on that website. And if those sites verify in sort of like getting a domain certificate fashion,
*  they can get paid. They can get part of his $20 a month. So that vision could go big. And if it does,
*  I hope it's across multiple browsers. I don't know that they'll all compete well on the quality of the
*  ads, the quality of the ad blocking and tracking protection. Those are subject to competition.
*  It'll take a while to standardize them. But I think that would be a better world. It would have
*  less counterparty risk, fewer fee takers in the middle, really just the browser. We're taking 30%
*  sort of the app store split. And if we get bigger, maybe we can take even less.
*  Social networks, creators. If you look at YouTubers, a lot of them are the indies that are
*  getting some size are getting sponsorship deals. They're using Patreon. They're encouraging people
*  to subscribe and give them regular money through Patreon. But that's centralized your Patreon. So
*  there's censorship hazards. There's a 5% fee. What if that were a web standard? What if Brave
*  pioneered at first and we took 3% and we did it in a way that was through your browser so we couldn't
*  censor it? That's brilliant. Yeah. Do you think it could be standardized across browsers? Can like
*  Internet Explorer come in again? And protocols are easy to copy and that they're meant to be
*  interoperable. So there's a risk there and the loyal users might be tricked into leaving you or
*  they might because of that distribution power, you might end up getting stomped. I don't know. I can't
*  predict the future. I think antitrust is back on the case finally in the US and certainly in Europe,
*  DG Comp is doing its thing. So I'm hopeful that we'll have a period of innovation.
*  People were talking like Elizabeth Warren was talking about breaking up the tech companies very
*  clearly. Now she didn't win and I suspect that won't happen. But I also suspect that Google might
*  be smart enough to see they should do something more than just put privacy perfume on Chrome.
*  They should maybe get rid of DoubleClick or something, divest something. I don't know. It
*  might happen. So Brave might inspire Google to completely change the way they're doing things.
*  They're already doing something you may have read about called the privacy sandbox or
*  flock, which they have this bird metaphor going, turtle dove,
*  fledge. But these systems have been very googly, over engineered and yet depending on differential
*  privacy, which has weakness over time if you know how that works, it's injecting
*  noise to hide you in a crowd, but over time an adversary can pull you out of the crowd.
*  This doesn't look like it's going to become a standard. Apple, Brave, Mozilla, we're not going
*  to just say, oh, Google, you saved us. You've invented the privacy sandbox, so we'll all just
*  adopt it. Not going to be that easy. It's going to be more like pieces of what we do in Brave,
*  the synonymous ad matching or the blind signature cryptography we use to confirm the ad
*  impressions. That's David Chow's invention. That could get standardized. In fact, some of that is
*  being standardized. Even Google's in favor of so-called trust tokens, which are Chowmy and
*  blind signature certs, but they're not using them for ad confirmations because they don't want to
*  blow up their own business. And they need to let some of the publishers they serve have other ad
*  ad tech scripts on the page. And so they're kind of caught. And this is something I realized doing
*  Brave. I thought, what's Google's innovators dilemma apart from just being mature and having
*  trouble innovating? It's that they have come to depend on this ad tech system that has all these
*  vendors that publishers rely on because publishers aren't technical enough.
*  And I feel for the publishers, but I realized the users have to come first. And if you give the users
*  a better browser that's faster, then you'll get enough users to give back or support publishers.
*  The speed and the battery savings and the data plan savings are significant. There's so much
*  bad JavaScript involved in ad tech. If you block it, you sort of chop off what's called the
*  programmatic waterfall, which chains a bunch of requests. Yeah, that's one of the incredible
*  things about Brave. I guess you're saying you should attribute it to the fact that the messy
*  JavaScript, no offense, is, I mean, Brave just feels faster. I mean, Chrome was fast. One of the
*  things that it was like impressive is it showed that browsers could be really fast and Brave is
*  even faster than that, which is incredible. Because we've blocked so much and it saves
*  the network, which means data plan, it saves battery because the radio consumes your battery
*  when it's running more to do those requests. And it's just stunning how many there are. Some of
*  my Google friends were like, oh, that's just that bad site. They'll fix it. And you actually do a
*  survey of web pages. That's mostly like that. I know Google engineers could make everything
*  super efficient, but they can't, especially in antitrust court, do it. They cannot take over
*  all the publishers and do that. They're trying with accelerated mobile profile,
*  AMP. They're trying to pull publishers. They're like, oh, you poor publishers don't know how to
*  make your pages fast. Put them on our AMP system. We'll give you extra placement in the search
*  carousel. That's an antitrust problem for one, but it's also publishers we talked to hate it
*  because it degrades their brand. Now they look like a gig writer wrote a piece that's got
*  Google's framing an AMP URL on top of it. And they're trying to fix that too. But it just looks like
*  Google's borgifying all these publishers and they don't want to be plugged into the Borg cube. They
*  want to build up their own brand and have loyal readers. So I'm in favor of giving the users
*  power to help all the publishers and the little platoons and the creators. And so we talked about
*  Patreon. What about social networks? Well, they're inherently like search, a global algorithm. You're
*  trying to find friends of friends. You're doing the transitive closure of a graph induced by this
*  friend of relation, but you should own your friend relation. You should own your posts. They shouldn't
*  be owned by somebody else who can take them down or censor them. And your friend relations, you
*  should be able to find those friends on other networks. And so I've tweeted about this. I haven't
*  built it yet. What if the browser could keep track of those for you? What if the browser could
*  maybe combine Facebook and Twitter and you could find your friends on both and you could
*  have a sort of more- So that relationship is not owned by Facebook or Twitter. It's owned by you
*  through the browser. They'll have terms of use and they'll say they own it. But if they zap you on one
*  and you're still on the other, your friends find you and the browser could
*  preserve a combined view. You could resurrect almost across networks.
*  It's something I want to maybe quickly ask you about. On that front, there's been quite a lot of
*  centralized- We talked about Wall Street Bets and then Robinhood. There's been centralized banning
*  of different accounts and removing like Parler, for example, from AWS and this kind of overreach
*  of centralized control. What are your thoughts about that in general? And is it possible to
*  create tools that give individual people the power to fight back against overreach of such control?
*  So we're talking about oligarchy, I do think. And if it controls a nation-state, that's formidable.
*  It's the tax and the police power, the military power. It means that you may have the Great
*  Firewall of China. You may have people in China who are jailed because of their tweets. This is
*  a serious threat. I can't minimize it or say that we'll win. I don't know how it's going to go.
*  But I do think, like I said earlier about the cunning of reason, people find ways around things.
*  The internet routes around censorship. And this is not to endorse any particular bad faction.
*  One of the things that happens when you try to wave the free speech flag too much,
*  you say, I'm not going to censor anything and you get colonized by terrible, terrible people.
*  I don't care if you call them neo-Nazi, some of them could be doing illegal things.
*  And you don't want them colonizing because it'll ruin your reputation and destroy your business.
*  So what you really want is that kind of user-first subsidiarity, that subjectivity. I want my social
*  networks to be composited in some multi-social user interface where I don't lose track of people
*  across networks. And if they leave one or they get banned from one, I can find them on another.
*  I can still sort of thread them together. Yeah, that's brilliant.
*  And this didn't happen because browsers got captured by the central powers.
*  Why did they get captured? Mostly because of search. And search is a central algorithm.
*  So Larry Page said this too many years ago. He said, with search, you're giving up a little
*  privacy by handing the query over to us. And we'll error correct it. Alan used to be a Google
*  executive. He said, oh yeah, we used to laugh. They'd all be doing typos and they'd be typing
*  the wrong word. And we're like, no, dummy, type that query. And it's like, okay, Google,
*  you might want to dial back that ego a little bit. But yes, you do see all the queries and you
*  can improve them and you can find the best results. And that was Google's forte. When we
*  did the Firefox deal in 2004, Google was really good. And over time, SEO, which is an adversarial
*  game, and Google itself buying all these companies and crowding its own results page with its own
*  tied in stuff. The YouTube. It's the slippery slope that happens when you have control over
*  these kinds of really important mechanisms. Yeah. Monopoly capitalism or cartel. You get this with
*  the Robin Hoods and the hedge funds. You get sort of the money interests take over and kind of abuse
*  their power and wear out their welcome. So how do you get around that? You have to have either
*  new land to go to, which some people's ancestors, not mine, did to found the country.
*  I'm mostly Irish-German. You have new virtual space people go to and that requires an ISP
*  or a Colo Center or Amazon to host you. It requires domain name registrar who will not strike you.
*  And so when Parler was taken down, I thought that was egregious. Parler, it was not well designed
*  and I tried it out because I tried all these things, but I didn't use it. And I also felt they
*  were being unfairly scored for not moderating because you can find tweets to this day that
*  are horrendous and threaten all sorts of violence. Whereas Twitter, why isn't Twitter being taken
*  down? But so it was very selective. It was the insiders who have the power are going to take out
*  the newcomer and it looked bad. Sort of like the hedge funds sorting GameStop. It looked bad.
*  You're seeing a piece in Time Magazine this week that's like basically saying, yeah, we interfere
*  with the election, but it was great. Aren't we good? I don't know if you've seen this piece yet.
*  If you tried to say that as a Trump supporter in November after the election, you get banned from
*  Twitter. But now Time in its Twitter account is saying, we saved the day. It's AFL-CIO and
*  big business, the Better Business Bureau got together and kept Trump from spreading fake news.
*  So the country's kind of broken. I don't know how to fix that. The oligarchs have run wild,
*  in my opinion. And Big Tech is in the antitrust dock. What's going to happen? I don't think they
*  get out. I think some of the DOJ and certainly the state cases because there's separate cases
*  are not going to go away just because somebody got elected differently. And these are career
*  prosecutors and they have a strong case. And Google Smart, Microsoft almost got split up.
*  The judge, Thomas Penfield Jackson, he overreached. He didn't hold a hearing about the remedy. He just
*  said, I'm going to break you up. And Microsoft appealed and the higher level court said,
*  go back and figure this out. You're not breaking them up. You didn't even hold a hearing.
*  And when they got back, Microsoft said, let's settle. Let's settle. We don't want to get
*  broken up because Jackson was going to make the Opsco, the operating system company and the
*  Opsco office, Word and Excel. And that would have been a huge blow to Microsoft. But ultimately,
*  I don't know if you're optimistic or cynical about the possibility of breaking out Big Tech.
*  To me, I'm optimistic that tools like Brave, I love the idea of owning your friendships and
*  users more and more owning the stuff is the only real way. Unfortunately, it's like the Wall Street
*  bad subreddit is the only real way to fight the centralized power. You can't break them up. The
*  regulation is very difficult. Certainly, I don't want to wait for the law. Netscape was long dead
*  or acquired by AOL and effectively dead. It was only Mozilla that returned Firefox to the market
*  by the time that the USB Microsoft case was finally settled and the penalties were put in place.
*  And yet, antitrust has a role to play. Those penalties caused Microsoft to kind of turn away
*  from the web. They did Windows Vista and they thought the web's too painful. We got punished
*  in court and we had to standardize things with those icky standards people. So they ran back
*  to proprietary lock-in and Windows Vista flopped. It was late, it was bloated, Longhorn. Now,
*  I was going to say, Google's smart enough. They won't get split up. They'll split something out
*  to get off the hook, I think. This is a complicated subject, but I myself was so,
*  I decided to journey out from the world of being a researcher at MIT and potentially doing a startup
*  myself. And I've been thinking of, you know, I wanted to come to Silicon Valley to do so.
*  It's the land of the entrepreneur. And there's a lot of my friends, a lot of them are successfully
*  have been entrepreneurs themselves, have said, do not come to Silicon Valley.
*  You've started, you ran amazing teams of engineers. You started a lot of successful businesses.
*  I wondered if you could comment on why a lot of people are leaving California. Is there something
*  that could be fixed about California? If you were starting a business today, would you consider
*  somewhere else like Austin or some other place or is Silicon Valley still, is it just a little
*  lull? Everybody's being overdramatic during this particular year of the coronavirus and so on?
*  I think, you know, even Austin's getting overheated, I hear. And I've had relatives and
*  friends move to Texas within the last few months. So Texas as a whole is a big place. And, you know,
*  people are moving to Florida. There's a big movement toward Miami, Peter Teelke,
*  these people. The mayor has been very business friendly about it, which I think is just good
*  politics. America is fundamentally a commercial republic. So you would think this would be what's
*  happening. For a long time, California was the golden state. I came here in late 76 when I was
*  a teenager. It's in crushing debt due to the lockdowns. It's got the highest taxes. That's
*  got to matter. People will do high taxes. It's got likely fires every year because of the dead fall.
*  It's not global warming. It's because the forests weren't managed like they had been in the first
*  part of the 20th century. Just, I would say corruption at all levels, especially up to the
*  governor who, you know, famously was eating at the French Laundry and claimed to be outside. It was
*  inside and they were out in masks off and it was great. Do what I say, not what I do. Rules for
*  the, but not for me. When you see that in leadership, people either run or they get
*  rid of the leadership. So there's a recall drive, which is about to reach the threshold.
*  Or in the old days, they get their guns, right? You don't put up with this junk.
*  But ultimately the thing that made Silicon Valley a special place, it gave freedom to like young
*  kids, entrepreneurs, young minds, brave minds to think bold, to try different stuff. I mean,
*  even if the taxes are high, so outside of financial stuff, outside of all of that.
*  Housing super expensive.
*  Housing super expensive. So it's hard. Okay. Everything about startups is
*  narrow and they didn't plan the roads, right? They got rid of public transportation in LA,
*  like the Who Framed Roger Rabbit cartoon show. They used to have trolley cars,
*  Portland too. The oil companies and the DoD conspired to build highways and make cars dominant.
*  And the rights of way are long gone. Like Elon's going to go underground.
*  And I've researched it well. That's probably the only way to do it now.
*  But is it still a place, do you think it's possible that Silicon Valley is still a place
*  where magic happens? Where the next Google is built? Where the next, I mean, Brave is built?
*  I think all good things come to an end. I think the problem is Silicon Valley had strong network
*  effects through Stanford, through the angel investor networks and the wealth effect. And
*  originally you have to give the federal government credit. Like the ARPANET was a government
*  project. Let's not kid ourselves. This wasn't wild free market, libertarian capitalism. This was all
*  Cold War stuff. Out of the academia, you had Shockley and then the Trader's Aid and Fairchild
*  and Intel. But now, when's the last fab that was built in the valley? Micro-Unity might have been
*  the last fab. I don't know. I haven't followed it. We built a fab in Sunnyvale in Micro-Unity
*  in the early nineties. And now the fabs are overseas. And the one thing that I would say
*  the oligarchs have intentionally done in both parties is labor and environmental protection law
*  arbitrage by going where the labor is cheaper and the environmental laws aren't as strict.
*  And that's polluted the hell out of parts of China, but it's made things, you can make cheaper junk.
*  And this is not a story that's over yet. So what is Silicon Valley for now? It's for the network
*  effect, the brain trust of who you know, the parties, the Stanford network. That's fragile
*  too over time, I'm afraid. Stanford, a lot of good professors are like, they still filter mainly based
*  on socioeconomic status, but it's kind of a skate school. I had a friend hired out of Harvard 20
*  years ago at Netscape. And we talked about Harvard and he said, yeah, they're still professors who
*  grade on the curve. And I said, oh yeah, I don't think they're any doing that at Stanford anymore.
*  And he said, yo, it was shocking. Some of the students got C's and D's and they were crying.
*  It's like, yes, that's right. The precious deers can't take that at Stanford. So they get A's and
*  B's. Now you look at China and people say what you all about China. They prove Russia too, a lot of
*  math science training, a lot of engineering, a lot of people who are doing their coursework to get the
*  A's and B's. So I'm an American. I'm born on the 4th of July.
*  Really? 4th of July.
*  Yeah. And America, as I say, fundamentally is a commercial republic. You can try to make it
*  something else. You can say it's the new Atlantis and mystify it. You could talk about it in a more,
*  I think, correct way, which is 13 colonies that grew. And then there's a lot of local
*  or original design anyway, the federalist papers talk about this, there's a lot of
*  subsidiarity, but that's been eroded over time. And like I say, a lot of the offshoring has hurt.
*  So what happened with coronavirus? People working from home. And at first it was funny,
*  because I have friends at Google who used to grumble that not only did they have to come
*  into the office, if they joined a different team that was centered in a different office,
*  they had to move. Or if the VA team was reconstituted in Munich, which it was after Lars
*  Bach got tired of JavaScript, that they hired in Munich or they hired PhDs in Germany and moved
*  them to Munich. With coronavirus, everyone's working from home and it's like, what a relief,
*  I can work for Google from home. But then the next few dropped and people started asking
*  Mark Zuckerberg, hey, can I move to my hometown in the Midwest? And he said, okay. And they said,
*  oh, can I keep getting my Silicon Valley pay? No. We're going to figure out what your cost of living
*  there is and we're going to adjust your pay accordingly. And these colonies and these little
*  mini experiments that all combined to the big giant experiment. I have a, I don't know, I have
*  this vision of America, which the country, I was born in Russia, like I said here, and this is truly
*  a wonderful country. I wasn't born on the 4th of July, but I might as well be. People still flee here.
*  I still, and I'm a red blooded American at this point. And I have a sense that we figured it out
*  somehow. If Silicon Valley burns, another place will come up in this place that even more
*  innovation and people will move. And the remote work might change fundamentally how we work
*  or might not. It might just give you the freedom to then create many other small Silicon Valleys
*  throughout the place, like Austin included, but other places as well. And we somehow figure it,
*  figure it out. And I think that's, that's true that there will be more mobility and maybe new
*  places that come up. I don't know if Silicon Valley has, you know, passed some sell by date
*  because it did hurt the coronavirus hurt the lockdowns hurt in the fact, in the sense that
*  part of what keeps things going is social. And so a lot of young people, even before coronavirus
*  moved to San Francisco, it was very strange to watch because in the eighties, we all lived in
*  the Valley and it was less populated in San Francisco was grungier. It was more like dirty
*  Harry in the seventies. But, but by the nineties and Jamie runs a nightclub there, and he's talked
*  about this, you had sort of wealthy tech people moving in south of market, fancy townhouses being
*  built. And that's continued in such a point that it's almost like what's the movie by the
*  South African director Nels Jody Foster up in the space colony. Matt Damon is the guy on the earth
*  who gets to go up. And anyway, it's about the stratification. It's about the great inequality
*  that people in the space station have like amazing medical autodocs that can extend their life or
*  save them cure cancer. People on earth are all suffering ground down in poverty. And, you know,
*  that sort of happened while I was here. You saw a lot of money drive prices up along the narrow
*  peninsula and the single people wanted nightlife. So they were in the city and the condos in the
*  city got super expensive. And you, I know even Google friends who are, you know, socially
*  responsible say we should have more housing built. We should have, yes, in my backyard, not, not in
*  my backyard, but that's not happening as far as I can tell. And from the government to the incumbent,
*  you know, landowners and renters, it's just not happening. And that has to drive people away.
*  I appreciate that people come here and you should wait for the prices to moderate. They will. But,
*  but a lot of people are going to go where the prices are lower.
*  You, and sorry for silly questions here, but just looking back, you have created things,
*  have been part of creating things that have transformed this world, the world of technology,
*  perhaps more than almost anything else. But you're still a human being.
*  And unfortunately this ride ends. Do you ever think about your own mortality?
*  Not too much. I mean, I'm, I'm, I'm a Roman Catholic, so I am not afraid of death. I think
*  a lot of people who have problems with death are suffering from some lack of either faith in their
*  transcending death or maybe they don't have children or they feel like, you know, they get
*  later in life and they feel like they they've missed opportunities to do something that endures.
*  And I sympathize with all that because I, I'm old, I got married fairly old. So I understand all that.
*  Nothing human is alien to me as Terrence said. But I don't fear it. No.
*  What do you hope your legacy is?
*  It's going to be JavaScript. I think, no, I think, you know, my legacy has more to do with
*  my children and their children. I think it also has to do with web standards. It has to do with
*  things like Brave. The things we did with Firefox when we did, you know, I'm not going to over sell
*  Brave, but I think Brave is important and we will continue to prove this in a way that counts for
*  many decades to come. But even Firefox, whatever its future fortune showed you can restart the
*  browser market. This thing you said about people opting out and routing around, you don't need
*  everybody to do that. It's more like Taleb's stubborn minorities that do that. It's the lead
*  users, Eric Von Hippel's lead users. You can be a few percent, you can tilt the market. And that
*  can be done in spite of the incumbents, the moneyed interests not being in favor of what you're doing.
*  I think what we do with Firefox won't be forgotten and it needs to be done more.
*  And we're doing it with Brave and you could argue that other projects are doing it. In some ways,
*  blockchain is doing it. The Robinhood take down the use of Robinhood by the Wall Street Betts kids.
*  Yeah.
*  Similar. So yeah, that kind of spirit endures. And I think in some ways it's American, right? It's
*  not hard revolutionary. It's not trying to burn the past and destroy everything. It's more like
*  we have these certain, let's say, rights. We have duties too. So there's some debate about
*  which comes first in American jurisprudence and the founding documents. But as long as things
*  are working, we'll be like pragmatic Americans like the Tocqueville described in his writings.
*  But if things get too out of whack for one reason or another, too unequal, too oligarchic and
*  abusive, we're going to assert our rights. And even a few of us can do it. And even in the
*  American Revolution, it was a minority who fought and put their lives, treasure and sacred honor at
*  stake. It was a bunch of people went to Upper Canada, I think it was called, Ontario.
*  Yeah. That's a beautiful, I mean, that is at the core where your work stands for is that a few
*  people can have the power to transform society with just a few radical ideas, with just a little
*  bit of code, change the world. Got to do it. And that's empowering. And that is the American way.
*  That's why this country is, I believe, the greatest country. I know that's not over-romanced,
*  says it too much, but I think some special things have already happened in this country and will
*  continue to happen. And that's- And that spirit can continue no matter who comes here. They can
*  adopt those folk ways and that spirit. Brandon, I can't tell you how much, I was freaking out
*  how much of an honor it is to talk to you. You're an incredible human being. It's one of my favorite
*  conversations ever. Thank you so much for wasting all this time with me. I really appreciate it.
*  Oh, it seems like a breeze. My pleasure. Thank you for listening to this conversation with
*  Brandon Icke. And thank you to our sponsors, Jordan Harberage Show, Sun Basket Meal Delivery
*  Service, Better Help Online Therapy, and Eight Sleep Self-Cooling Mattress. Click the sponsor links
*  to get a discount and to support this podcast. And now let me leave you with some words from Jeff
*  Atwood. Any app that can be written in JavaScript will eventually be written in JavaScript. Thank
*  you for listening and hope to see you next time.

---
Date Generated: April 13, 2024
Transcription Model: whisper medium 20231117
Length: 9555s
Video Keywords: ['agi', 'ai', 'ai podcast', 'artificial intelligence', 'artificial intelligence podcast', 'jim keller', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'mit ai']
Video Views: 1050050
Video Rating: None
---

# Jim Keller: The Future of Computing, AI, Life, and Consciousness | Lex Fridman Podcast #162
**Lex Fridman:** [February 18, 2021](https://www.youtube.com/watch?v=G4hL5Om4IJ4)
*  The following is a conversation with Jim Keller, his second time in the podcast.
*  Jim is a legendary microprocessor architect and is widely seen as one of the greatest
*  engineering minds of the computing age. In a peculiar twist of space-time in our simulation,
*  Jim is also a brother-in-law of Jordan Peterson. We talk about this and about computing,
*  artificial intelligence, consciousness, and life. Quick mention of our sponsors. Athletic Green's
*  All-in-One nutrition drink, Brooklyn and Cheats, ExpressVPN, and Belcampo grass-fed meat. Click
*  the sponsor links to get a discount and to support this podcast. As a side note, let me say that Jim
*  is someone who, on a personal level, inspired me to be myself. There was something in his words,
*  on and off the mic, or perhaps that he even paid attention to me at all, that almost told me,
*  you're alright kid. A kind of pat on the back that can make the difference between a mind that
*  flourishes and a mind that is broken down by the cynicism of the world. So I guess that's just my
*  brief few words of thank you to Jim and in general, gratitude for the people who have given me a chance
*  on this podcast, in my work, and in life. If you enjoy this thing, subscribe on YouTube,
*  review it on Apple Podcasts, follow on Spotify, support it on Patreon, or connect with me on
*  Twitter, Alex Friedman. And now, here's my conversation with Jim Keller. What's the value
*  and effectiveness of theory versus engineering, this dichotomy, in building good software or
*  hardware systems? Well, it's good designs both. I guess that's pretty obvious. By the engineering,
*  do you mean reduction of practice of known methods? And then science is the pursuit of
*  discovering things that people don't understand, or solving unknown problems. Definitions are
*  interesting here, but I was thinking more in theory, constructing models that kind of generalize
*  about how things work. And engineering is actually building stuff, the pragmatic, like,
*  okay, we have these nice models, but how do we actually get things to work? Maybe economics is
*  a nice example. Economists have all these models of how the economy works and how different policies
*  will have an effect. But then there's the actual, let's call it engineering of actually deploying
*  the policies. So computer design is almost all engineering and reduction of practice of known
*  methods. Now, because of the complexity of the computers we built, you could think you're,
*  well, we'll just go write some code and then we'll verify it and then we'll put it together.
*  And then you find out that the combination of all that stuff is complicated. And then you have to
*  be inventive to figure out how to do it. So that definitely happens a lot. And then every so often,
*  some big idea happens, but it might be one person. And that idea is in what,
*  in the space of engineering or is it in the space of-
*  Well, I'll give you an example. So one of the limits of computer performance is branch prediction.
*  So, and there's a whole bunch of ideas about how good you could predict a branch. And people said,
*  there's a limit to it, it's a nice metodic curve. And somebody came up with a better way to do
*  branch prediction. It was a lot better. And he published a paper on it and every computer in
*  the world now uses it. And it was one idea. So the engineers who build branch prediction hardware
*  were happy to drop the one kind of training array and put it in another one. So it was a real idea.
*  And branch prediction is one of the key problems underlying all of sort of the lowest level of
*  software. It boils down to branch prediction. Boils down to uncertainty. Computers are limited by,
*  single thread computer is limited by two things. The predictability of the path of the branches
*  and predictability of locality of data. So we have predictors that now predict both of those
*  pretty well. So memories, a couple hundred cycles away, local cache is a couple cycles away.
*  When you're executing fast, virtually all the data has to be in the local cache.
*  So a simple program says, add one to every element and array. It's really easy to see what the stream
*  of data will be. But you might have a more complicated program that says, get an element
*  of this array, look at something, make a decision, go get another element. It's kind of random.
*  And you can think that's really unpredictable. And then you make this big predictor that looks
*  at this kind of pattern and you realize, well, if you get this data and this data, then you probably
*  want that one. And if you get this one and this one and this one, you probably want that one.
*  And is that theory or is that engineering? Like the paper that was written, was it asymptotic kind
*  of discussion or is it more like, here's a hack that works well?
*  It's a little bit of both. Like there's information theory in it, I think somewhere.
*  Okay. So it's actually trying to prove some kind of stuff.
*  Once you know the method, implementing it is an engineering problem. Now there's a flip side of
*  this, which is in a big design team, what percentage of people think their plan or their life's work is
*  engineering versus inventing things. So lots of companies will reward you for filing patents.
*  Many big companies get stuck because to get promoted, you have to come up with something new.
*  And then what happens is everybody's trying to do some random new thing,
*  99% of which doesn't matter. And the basics get neglected. Or there's a dichotomy that you think
*  like the cell library and the basic CAD tools, or basic software validation methods.
*  That's simple stuff. They want to work on the exciting stuff. And then they spend lots of
*  time trying to figure out how to patent something. And that's mostly useless.
*  But the breakthroughs are on the simple stuff.
*  No, no. You have to do the simple stuff really well. If you're building a building out of bricks,
*  you want great bricks. So you go to two places that sell bricks. So one guy says,
*  yeah, they're over there in a ugly pile. And the other guy is like lovingly tells you about the
*  50 kinds of bricks and how hard they are and how beautiful they are and how square they are.
*  Which one are you going to buy bricks from? Which is going to make a better house.
*  So you're talking about the craftsman, the person who understands bricks,
*  who loves bricks, who loves the varieties.
*  That's a good word. Good engineering is great craftsmanship.
*  And when you start thinking engineering is about invention, and set up a system that rewards
*  invention, the craftsmanship gets neglected. Okay, so maybe one perspective is the theory,
*  the science overemphasizes invention, and engineering emphasizes craftsmanship.
*  It doesn't matter what you do, theory or engineering.
*  Well, everybody does. Read the tech rags. They're always talking about some breakthrough
*  or innovation and everybody thinks that's the most important thing.
*  But the number of innovative ideas is actually relatively low. We need them,
*  right? And innovation creates a whole new opportunity. Like when some guy invented the
*  internet, right? Like that was a big thing. The million people that wrote software against that
*  were mostly doing engineering software writing. So the elaboration of that idea was huge.
*  I don't know if you know, Brendan and I, he wrote JavaScript in 10 days.
*  That's an interesting story. It makes me wonder, and it was famously for many years considered to
*  be a pretty crappy programming language. It still is perhaps. It's been improving sort of consistently.
*  But the interesting thing about that guy is he doesn't get any awards.
*  You don't get a Nobel Prize or a Fields Medal.
*  For inventing a crappy piece of software code.
*  That is currently the number one programming language in the world and now is
*  increasingly running the back end of the internet.
*  Does he know why everybody uses it? That would be an interesting thing.
*  Was it the right thing at the right time? Because when stuff like JavaScript came out,
*  there was a move from writing C programs and C++ to what they call managed code frameworks,
*  where you write simple code. It might be interpreted. It has lots of libraries.
*  Productivity is high. You don't have to be an expert.
*  Java was supposed to solve all the world's problems. It was complicated.
*  JavaScript came out after a bunch of other scripting languages. I'm not an expert on it.
*  Was it the right thing at the right time or was there something clever? Because he
*  wasn't the only one. There's a few elements.
*  Maybe if he figured out what it was, then he'd get a prize.
*  Like that. Constructive theory.
*  Yeah. Maybe his problem is he hasn't defined this or he just needs a good promoter.
*  Well, I think there was a bunch of blog posts written about it, which is like,
*  wrong is right, which is like doing the crappy thing fast.
*  Just like hacking together the thing that answers some of the needs
*  and then iterating over time, listening to developers, like listening to people who
*  actually use the thing. This is something you can do more in software, but the right time,
*  like you have to sense, you have to have a good instinct of when is the right time for the right
*  tool and make it super simple and just get it out there. The problem is this is true with hardware.
*  This is less true with software is there's backward compatibility that just drags behind you as,
*  you know, as you try to fix all the mistakes of the past. But the timing
*  was good. There's something about that. It wasn't accidental. You have to like,
*  give yourself over to the, you have to have this like broad sense of what's needed now,
*  both scientifically and like the community. And just like this, it was obvious that there was no,
*  the interesting thing about JavaScript is everything that ran in the browser at the time,
*  like Java and, and I think other like scheme, other programming languages, they were all in a
*  separate external container. And then JavaScript was literally just injected into the webpage.
*  It was the dumbest possible thing running in the same thread as everything else. And like,
*  uh, it was inserted as a comment. So JavaScript code is inserted as a comment in the HTML code.
*  And it was, I mean, there's, it's either genius or super dumb, but it's like,
*  right. So it has no apparatus for like a virtual machine and container.
*  It just executed in the framework of the program that's already running.
*  And it was, and then, uh, because something about that accessibility, the ease of its use,
*  uh, resulted in then developers innovating of how to actually use it. I mean, I don't even know what
*  to make of that, but it does seem to echo across different software, like stories of different
*  software. PHP has the same story, really crappy language. It just took over the world.
*  Well, let's have a joke that the random length instructions, that variable length instruction
*  that's always one, even though they're obviously worse. Like nobody knows why x86 is arguably the
*  worst architecture, you know, on the planet is one of the most popular ones. Well, I mean, isn't,
*  isn't that also the story of risk or just, I mean, is that simplicity? There's something
*  about simplicity that are us in this evolutionary process is valued. If it's simple, it gets,
*  it spreads faster. It seems like, or is that not always true? That's always true. Yeah. It could be
*  simple is good, but too simple is bad. So why did risk win you think so far? Did risk win
*  in the long archivist tree? We don't know. So who's going to win? What's risk? What's this?
*  And who's going to win in that space? Even these instruction sets, right? AI software is going to
*  win, but there'll be little computers that run little programs like normal all over the place.
*  But, but we're, we're going through another transformation. So you think instruction sets
*  underneath it all will change. Yeah, they evolve slowly. They don't matter very much.
*  They don't matter very much. Okay. I mean, the limits of performance are, you know, predictability
*  of instructions and data. I mean, that's the big thing. And then the usability of it is some, you
*  know, quality of design, quality of tools, availability. Like right now, x86 is proprietary
*  with Intel and AMD, but they can change it any way they want independently, right? ARM is proprietary
*  to ARM and they won't let anybody else change it. So it's like a sole point and risk five is open
*  source. So anybody can change it, which is super cool. But that also might mean it gets changed in
*  too many random ways that there's no common subset of it that people can use. Do you like open or do
*  you like closed? Like if you were to bet all your money on one or the other risk five versus it?
*  No idea. It's case dependent. Well, x86, oddly enough, when Intel first started developing it,
*  they licensed it like seven people. So it was the open architecture. And then they move faster than
*  others and also bought one or two of them. But there was seven different people making x86,
*  because at the time there was 6502 and z80s and, you know, 8086. And you could argue everybody
*  thought z80 was the better instruction. But that was proprietary to one place. Oh, and the 6800.
*  So there's like four or five different microprocessors. Intel went open, got the
*  market share because people felt like they had multiple sources from it. And then over time,
*  it narrowed down to two players. So why you as a historian? Why did Intel win for so long
*  with with their processors? I mean, they were great. Their process development was great.
*  So it's just looking back to JavaScript and like is Microsoft and Netscape and all these
*  internet browsers. Microsoft won the browser game because they aggressively stole other people's
*  ideas. Like right after they did it. You know, I don't know if Intel was stealing other people's
*  ideas. They started making good way stealing. They started making rams, random access memories.
*  And then at the time when the Japanese manufacturers came up, you know, they were
*  getting out competed on that and they pivoted the microprocessors and they made the first,
*  you know, integrated microprocessor programs. It was the 4004 or something.
*  Who was behind that pivot? That's a hell of a pivot. Andy Grove. And he was great.
*  That's a hell of a pivot. And then they led semiconductor industry. Like they were just a
*  little company, IBM, all kinds of big companies had boatloads of money and they out innovated
*  everybody. Out of innovated. OK, yeah. Yeah. So it's not like marketing. It's not any other stuff.
*  Their processor designs were pretty good. I think the, you know, core two was probably the
*  first one I thought was great. It was a really fast processor and then Haswell was great.
*  What makes a great processor in that? Oh, if you just look at its performance versus everybody else,
*  it's, you know, the size of it, the usability of it.
*  So it's not specific, some kind of element that makes you beautiful. It's just like literally just
*  raw performance. Is that how you think of bioprocessors? It's just like raw performance?
*  Of course. It's like a horse race. The fastest one wins. Now you don't care how.
*  Well, there's the fastest in the environment. Like, you know, for years you made the fastest
*  one you could, and then people started to have power limits. So then you made the fastest at the
*  right PowerPoint. And then, and then when we started doing multi processors, like,
*  if you could scale your processors more than the other guy, you could be 10% faster on
*  like a single thread, but you have more threads. So there's lots of variability. And then ARM
*  really explored like, you know, they have the A series and the R series and the M series,
*  like a family of processors for all these different design points from like unbelievably small and
*  simple. And so then when you're doing the design, it's sort of like this big palette of CPUs,
*  like they're the only ones with a credible, you know, top to bottom palette.
*  What do you mean a credible top to bottom?
*  Well, there's people who make microcontrollers that are small, but they don't have a fast one.
*  There's people who make fast processors, but don't have a little, a medium one or a small one.
*  Is it hard to do that full palette? That seems like a...
*  It's a lot of different.
*  So what's the difference between the ARM folks and Intel in terms of the way they're approaching
*  this problem?
*  Well, Intel, almost all their processor designs were, you know, very custom high end, you know,
*  for the last 15, 20 years.
*  For the fastest horse possible.
*  Yeah.
*  In one horse's hands.
*  Yeah. And the architecture, they're really good, but the company itself was fairly insular to
*  what's going on in the industry with CAD tools and stuff. And there's this debate about custom
*  design versus synthesis and how do you approach that? I'd say Intel was slow on getting to
*  synthesized processors. ARM came in from the bottom and they generated IP, which was a very
*  So they had very little say in how the customer implemented their IP. So ARM is super friendly
*  to the synthesis IP environment. Whereas Intel said, we're going to make this great client chip
*  or server chip with our own CAD tools, with our own process, with our own, you know, other
*  supporting IP and everything only works with our stuff.
*  So is that, is ARM winning the mobile platform space in terms of processing?
*  And so in that way you're describing is why they're winning.
*  Well, they had lots of people doing lots of different experiments. So they controlled the
*  processor architecture and IP, but they let people put in lots of different chips and there was a
*  lot of variability in what happened there. Whereas Intel, when they made their mobile,
*  their foray into mobile, they had one team doing one part, right? So it wasn't 10 experiments.
*  And then their mindset was PC mindset, Microsoft software mindset. And that brought a whole bunch
*  of things along that the mobile world and embedded world don't do.
*  Do you think it was possible for Intel to pivot hard and win the mobile market?
*  That's a hell of a difficult thing to do, right? For a huge company to just pivot.
*  I mean, so interesting to, because we'll talk about your current work. It's like,
*  it's clear that PCs were dominating for several decades, like desktop computers and then mobile,
*  it's unclear.
*  It's a leadership question. Like Apple under Steve Jobs, when he came back, they pivoted multiple
*  times. They built iPads and iTunes and phones and tablets and great Macs. Like who knew computers
*  should be made out of aluminum? Nobody knew that. But they're great. It's super fun.
*  Those Steve?
*  Yeah, Steve Jobs. Like they pivoted multiple times. And, you know, the old Intel, they did
*  that multiple times. They made DRAMs and processors and processes.
*  I gotta ask this. What was it like working with Steve Jobs?
*  I didn't work with him.
*  Did you interact with him?
*  Twice. I said hi to him twice in the cafeteria.
*  What did he say? Hi?
*  He said, Hey fellas. He was friendly.
*  He was friendly. He was wandering around and with somebody, he couldn't find the table
*  because the cafeteria was packed. And I gave him my table. But I worked for Mike Colbert,
*  who talked to, like Mike was the unofficial CTO of Apple and a brilliant guy. And he worked
*  for Steve for 25 years, maybe more. And he talked to Steve multiple times a day.
*  And he was one of the people who could put up with Steve's, let's say, brilliance and intensity.
*  And Steve really liked him. And Steve trusted Mike to translate the shit he thought up into
*  engineering products that work. And then Mike ran a group called Platform Architecture. And I was
*  in that group. So many times I'd be sitting with Mike and the phone would ring. Maybe Steve and
*  Mike would hold the phone like this because Steve would be yelling about something or other.
*  And then he would translate it.
*  And he translated it. And then he would say, Steve wants us to do this.
*  So was Steve a good engineer or no?
*  I don't know. He was a great idea guy.
*  Idea person.
*  He's a really good selector for talent.
*  Yeah, that seems to be one of the key elements of leadership, right?
*  And then he was a really good first principles guy. Like, like somebody say something couldn't be
*  done and he would just think that's obviously wrong. Right. But, you know, maybe it's hard to
*  do. Maybe it's expensive to do. Maybe we need different people. You know, there's like a whole
*  bunch of, you know, if you want to do something hard, you know, maybe it takes time. Maybe you
*  have to iterate. There's a whole bunch of things you could think about, but saying it can't be done
*  is stupid.
*  How would you compare? So it seems like Elon Musk is more engineering centric, but is also,
*  I think he considered himself a designer too. He has a design mind. Steve Jobs feels like he is
*  much more idea space, design space versus engineering. Just make it happen. Like the
*  world should be this way. Just figure it out.
*  But, but he used computers, you know, he had computer people talk to him all the time.
*  Like Mike was a really good computer guy. He knew what computers could do.
*  Computer meaning computer hardware, like hardware, software, all the pieces.
*  And then he would, you know, have an idea about what could we do with this next.
*  That was grounded in reality. It wasn't like he was, you know, just
*  finger painting on the wall and wishing somebody would interpret it. Like, so he had this
*  interesting connection because, you know, he wasn't a computer architect or designer,
*  but he had an intuition from the computers we had to what could happen.
*  And essentially you say intuition because it seems like he was pissing off a lot of engineers
*  in his intuition about what can and can't be done.
*  Those like the, what is all these stories about like floppy disks and all that kind of stuff?
*  Yeah. So in Steve, the first round, like he'd go into a lab and look at what's going on and hate it
*  and, and, uh, fire people or ask somebody in the elevator, what they're doing for Apple,
*  and, you know, not be happy when he came back. My impression was,
*  is he surrounded himself with this relatively small group of people and didn't really interact
*  outside of that as much. And then the joke was you'd see like somebody moving a prototype through
*  the quad with a, with a black blanket over it. And that was cause it was secret, you know, partly
*  from Steve, cause they didn't want Steve to see it until it was ready. Yeah. The dynamic with Johnny
*  Ive and Steve is interesting. It's like, you don't want to, he ruins as many ideas as he generates.
*  Yeah. Yeah. It's a dangerous kind of line to walk. I don't know if you have a lot of ideas,
*  like Gordon Bell was famous for ideas, right? And it wasn't that the percentage of good ideas
*  was way higher than anybody else. It was, he had so many ideas and he was also good at talking to
*  people about it and getting the filters right. And, you know, seeing through stuff. Whereas
*  Elon was like, Hey, I want to build rockets. So Steve was hired by two rocket guys and Elon
*  would go read rocket manuals. So Yon is a better engineer, a sense like, or like more, uh,
*  like a love and passion for the manuals and the details, the crossmanship too. Right. Well,
*  I guess Steve had crossmanship too, but of a different kind. What do you make of the,
*  just the standard for just a little longer, what do you make of like the anger and the passion and
*  all that, the, the firing and the mood swings and the madness, the, you know, being emotional and
*  all of that, that's Steve and I guess Elon too. So what is that a, is that a bug or a feature?
*  It's a feature. So there's a graph, which is, uh, Y axis productivity, X axis at zero, it's chaos
*  and infinity, it's complete order. Right. So as you go from the, you know, the origin,
*  as you improve order, you improve productivity. And at some point, productivity peaks and then
*  it goes back down again. Too much order. Nothing can happen. Yes. But the question is, is how close
*  to the chaos is that? No, no, no. Here's the thing is once you start moving in the direction
*  of order, the force vector to drive you towards order is unstoppable. Oh, so it's a slippery
*  every organization will move to the place where their productivity is stymied by order. So you
*  need a question is who's the counterforce like, cause it also feels really good as you get more
*  organized and productivity goes up. The organization feels it. They oriented towards it, right?
*  To hire more people. They get more guys who can run process. You get bigger. Right. And then
*  inevitably the organization gets captured by the bureaucracy that manages all the processes.
*  Right. And then humans really like that. And so if you just walk into a room and say, guys,
*  love what you're doing, but I need you to have less order.
*  If you don't have some force behind that, nothing will happen.
*  I can't tell you on how many levels that's profound. So,
*  so that's why I'd say it's a feature. Now, could you be nicer about it? I don't know. I don't know
*  any good examples of being nicer about it. Well, that the funny thing is to get stuff done. You
*  need people who can manage stuff and manage people because humans are complicated. They need lots of
*  care and feeding that you need to tell them they look nice and they're doing good stuff and pat
*  them on the back. Right. I don't know. You tell me, is that, is that needed? Oh, yeah. I had a friend,
*  he started a magic group and he said, I figured it out. You have to praise them before they do
*  anything. I was waiting until they were done and they're always mad at me. Now I tell them what a
*  great job they're doing while they're doing it. But then you get stuck in that trap. Cause then
*  when you're not doing something, how do you confront these people? I think a lot of people
*  that had trauma in their childhood would disagree with you. Successful people that you need to first
*  do the rough stuff and then be nice later. I don't know. Okay. But you know, engineering companies
*  are full of adults who had all kinds of range of childhoods and you know, most people had okay
*  childhoods. Well, I don't know if, uh, I know lots of people only work for praise, which is weird.
*  You mean like everybody. I'm not that interested in it, but, uh, well you, you're, you're probably
*  looking for somebody's approval. Even still. Yeah, maybe I should think about that. Maybe somebody
*  who's no longer with us kind of thing. I don't know. I used to call up my dad and tell him what
*  I was doing. He was, he was very excited about engineering and stuff. You've got his approval.
*  Yeah, a lot. I was lucky. Like he, he decided I was smart and unusual as a kid and that was okay
*  when I was really young. So when I did like did poorly in school, I was dyslexic. I didn't read
*  until I was third or fourth grade and they didn't care. My parents were like, Oh, he'll be fine.
*  So I was lucky. That was cool. Is he still with us? You miss him?
*  Sure. Yeah. He had Parkinson's and then cancer. His last 10 years were tough
*  and I killed him, killed a man like that's hard. The mind. Well, it's pretty good. Um,
*  Parkinson's causes slow dementia and, uh, the chemo therapy, I think accelerated it,
*  but it was like hallucinogenic dementia. So he was clever and funny and interesting and
*  was, it was pretty unusual. Do you remember conversations? Uh, from that time? Like what,
*  do you have fond memories of the guy? Yeah. Oh yeah. Anything come to mind?
*  A friend told me one time I could draw a computer on the whiteboard faster than anybody you'd ever
*  met. And I said, you should meet my dad. Like when I was a kid, he'd come home and say, I was driving
*  by this bridge and I was thinking about it. And he pulled out a piece of paper and he draw the
*  whole bridge. He was a mechanical engineer and he would just draw the whole thing. And then he
*  would tell me about it and to tell me how he would have changed it. And he had this, you know, idea
*  that he could understand and conceive anything. And I just grew up with that. So that was natural.
*  So, you know, like when I interview people, I ask them to draw a picture of something they did on
*  a whiteboard and it's really interesting. Like some people draw a little box, you know, and then
*  they'll say, and then this talks to this and I'll be like, oh, this is frustrating. And I had this
*  other guy come in one time. He says, well, I designed a floating point in this chip, but I'd
*  really like to tell you how the whole thing works and then tell you how the floating point works.
*  And so I do, do you mind if I do that? And he covered two whiteboards in like 30 minutes.
*  I hired him. Like he was great. This craftsman. I mean, that's the craftsmanship to that.
*  Yeah. But also the mental agility to understand the whole thing, right? Put the pieces in contacts,
*  like, you know, real view of the balance of how the design worked. Because if you don't understand
*  it properly, when you start to draw it, you'll fill up half the whiteboard with like a little
*  piece of it. And, you know, like your ability to lay it out in an understandable way, it takes a
*  lot of understanding. So. And be able to so zoom into the detail and then zoom out to the big picture.
*  Zoom out really fast. And what about the impossible thing? You see your dad
*  believed that you can do anything. That's a weird feature for a craftsman. Yeah.
*  It seems that that echoes in your own behavior. Like that's, that's the. Well, it's not that
*  anybody can do anything right now. Right. It's that if you work at it, you can get better at it
*  and there might not be a limit. And they did funny things like, like he always wanted to play piano.
*  So at the end of his life, he started playing the piano when he had Parkinson's and he was terrible.
*  But he thought if he really worked out in this life, maybe the next life, he'd be better at it.
*  He might be onto something. Yeah. He enjoyed doing it. Yeah. So that's pretty funny.
*  Do you think the perfect is the enemy of the good in hardware and software engineering?
*  It's like we were talking about JavaScript a little bit and the messiness of the 10 day
*  building process. Yeah. It's, you know, creative tension, right?
*  So creative tension is you have two different ideas that you can't do both.
*  Right. And then, and, but the fact that you want to do both causes you to go try to solve that
*  problem. That's the creative part. So if you're building computers, like some people say,
*  we have the schedule and anything that doesn't fit in the schedule, we can't do. Right. And so they
*  throw out the perfect cause they have a schedule. I hate that. Then there's other people to say,
*  we need to get this perfectly right. And no matter what, you know, more people, more money, right.
*  And there's a really clear idea about what you want. Some people are really good at articulating
*  it. Right. So let's call that the perfect. Yeah. Yeah. All right. But that's also terrible because
*  they never ship anything and never hit any goals. So now you have the, now you have your framework.
*  You can't throw out stuff because you can't get it done today. Cause maybe you've got it done
*  tomorrow or the next project, right? You can't. So you have to, I work with a guy that I really
*  like working with, but he overfilters his ideas. Overfilters? He'd start thinking about something
*  and soon as he figured out what's wrong with it, he'd throw it out. And then I start thinking
*  about it and like, you know, you come up with an idea and then you find out what's wrong with it.
*  And then you give it a little time to set. Cause sometimes, you know, you figure out how to tweak
*  it or maybe that idea helps some other idea. So idea generation is really funny. So you have to
*  give your idea space, like spaciousness of mind is key, but you also have to execute programs and
*  get shit done. And then it turns out computer engineering is fun because it takes, you know,
*  a hundred people to build a computer, 200 to 300, whatever the number is. And people are so variable
*  about, you know, temperament and, you know, skillsets and stuff that in a big organization,
*  you find the people who love the perfect ideas and the people that want to get stuff done yesterday.
*  And people like to come up with ideas and people like to, let's say shoot down ideas. And it takes
*  the whole, it takes a large group of people. Some are good at generating ideas. Some are good at
*  filtering ideas. And then in that giant mess, you're somehow, I guess the goal is for that
*  giant mess of people to find the perfect path through the tension, the creative tension.
*  But like, how do you know when you said there's some people good at articulating what perfect
*  looks like, what a good design is? Like if you're sitting in a room and you have a set of
*  ideas about like how to design a better processor, how do you know this is something special here?
*  This is a good idea. Let's try this. Have you ever brainstormed idea with a couple of people
*  that were really smart and you kind of go into it and you don't quite understand it and you're
*  working on it. And then you start, you know, talking about it, putting it on the whiteboard,
*  maybe it takes days or weeks, and then your brain starts to kind of synchronize. It's really weird.
*  And like you start to see what each other is thinking.
*  And it starts to work. Like you can see work. Like my talent in computer design is I can see
*  how computers work in my head, like really well. And I know other people can do that too.
*  And when you're working with people that can do that, like it is kind of an amazing experience.
*  And then, and every once in a while you get to that place and then you find the flaw,
*  which is kind of funny because you can fool yourself.
*  The two of you kind of drifted along into a direction that was useless.
*  Yeah, that happens too. Like you have to, because you know, the nice thing about computer design
*  is always reduction of practice. Like you come up with your good ideas. And I know some architects
*  who really love ideas and then they work on them and they put it on the shelf and go work on the
*  next idea and put it on the shelf. They never reduce the practice. So they find out what's good
*  and bad. Because almost every time I've done something really new, by the time it's done,
*  like the good parts are good, but I know all the flaws.
*  Yeah. Would you say your career, just your own experience, is your career defined by
*  mostly by flaws or by successes?
*  Like if again, there's great tension between those. If you haven't tried hard,
*  right? And done something new, right? Then you're not going to be facing the challenges
*  when you build it. Then you find out all the problems with it.
*  But when you look back, you see problems or?
*  Okay.
*  When I look back, I think earlier in my career, like EB5 was the second alpha chip.
*  I was so embarrassed about the mistakes. I could barely talk about it. And it was in the Guinness
*  Book of World Records and it was the fastest processor on the planet.
*  And at some point I realized that was really a bad mental framework to deal with, like doing
*  something new. We did a bunch of new things and some worked out great and some were bad.
*  We learned a lot from it. And then the next one, we learned a lot.
*  EB6 also had some really cool things in it. I think the proportion of good stuff went up,
*  but it had a couple of fatal flaws in it that were painful.
*  And then, yeah.
*  You learned to channel the pain into like pride.
*  Not pride, really. Just realization about how the world works or how that kind of idea set works.
*  Life is suffering. That's the reality.
*  What?
*  No, it's not. I know the Buddhist said that and a couple other people are stuck on it.
*  No, there's this kind of weird combination of good and bad,
*  light and darkness that you have to tolerate and deal with.
*  There's definitely lots of suffering in the world.
*  Depends on the perspective. It seems like there's way more darkness,
*  but that makes the light part really nice.
*  What computing hardware or just any kind of even software design do you find beautiful
*  from your own work, from other people's work? We were just talking about the
*  battleground of flaws and mistakes and errors, but things that were just beautifully done.
*  Is there something that pops to mind?
*  Well, when things are beautifully done, usually there's a well-thought-out set of abstraction
*  layers.
*  So the whole thing works in unison nicely.
*  Yes. When I say abstraction layer, that means two different components when they work together.
*  They work independently. They don't have to know what the other one is doing.
*  So that decoupling.
*  Yeah. The famous one was the network stack. There's a seven-layer network stack, data
*  transport and protocol and all the layers. The innovation was when they really got that right.
*  Networks before that didn't define those very well.
*  The layers could innovate independently, and occasionally the layer boundary, the interface
*  would be upgraded. That let the design space breathe. You could do something new in layer
*  seven without having to worry about how layer four worked. So good design does that. You see it in
*  processor designs. When we did the Zen design at AMD, we made several components very modular.
*  And my insistence at the top was I wanted all the interfaces defined before we wrote the RTL
*  for the pieces. One of the verification leads said, if we do this right, I can test the pieces
*  so well independently when we put it together, we won't find all these interaction bugs because
*  the floating point knows how the cache works. And I was a little skeptical, but he was mostly right.
*  That the modularity of the design greatly improved the quality.
*  Is that universally true in general? Would you say about good designs, the modularity is
*  like usually modular? Well, we talked about this before. Humans are only so smart.
*  And we're not getting any smarter. But the complexity of things is going up.
*  A beautiful design can't be bigger than the person doing it. It's just their piece of it.
*  The odds of you doing a really beautiful design of something that's way too hard for you is low.
*  Right? If it's way too simple for you, it's not that interesting. It's like, well, anybody could
*  do that. But when you get the right match of your expertise and mental power to the right design
*  size, that's cool. But that's not big enough to make a meaningful impact in the world. So now you
*  have to have some framework to design the pieces so that the whole thing is big and harmonious.
*  But when you put it together, it's sufficiently interesting to be used. So that's what a beautiful
*  design is. Matching the limits of that human cognitive capacity to the module you can create
*  and creating a nice interface between those modules and thereby do you think there's a limit to the
*  beautiful complex systems we can build with this modular design? If we build increasingly
*  more complicated... You can think of the internet. Okay, let's scale it down. You can think of social
*  network, like Twitter as one computing system. But those are little modules.
*  Yeah. But it's built on so many components nobody at Twitter even understands. So if an alien showed
*  up and looked at Twitter, he wouldn't just see Twitter as a beautiful, simple thing that everybody
*  uses, which is really big. You would see the network, it runs on the fiber optics, the data
*  is transported, the computers. The whole thing is so bloody complicated, nobody at Twitter understands
*  it. You think that's what the alien would see? So yeah, if an alien showed up and looked at Twitter,
*  or looked at the various different network systems that you can see on Earth.
*  So imagine they were really smart and they could comprehend the whole thing. And then they sort of
*  evaluated the human and thought, this is really interesting. No human on this planet
*  comprehends the system they built. No individual. Well, would they even see individual humans?
*  Like we humans are very human-centric, entity-centric. And so we think of us as the
*  central organism and the networks as just a connection of organisms. But from a perspective
*  of an alien, from an outside perspective, it seems like. Yeah, I get it. We're the ants and
*  it's the ant colony. The ant colony, yeah. Or the result of production of the ant colony, which is
*  like cities. And in that sense, humans are pretty impressive, the modularity that we're able to,
*  and how robust we are to noise and mutation, all that kind of stuff. Well, that's because it's
*  stress tested all the time. Yeah. You build all these cities with buildings and you get earthquakes
*  occasionally. Wars. You know, wars, earthquakes. Viruses every once in a while. Changes in business
*  plans for shipping or something. As long as it's all stress tested, then it keeps adapting to the
*  situation. So that's a curious phenomenon. Well, let's go, let's talk about Moore's Law a little bit.
*  At the broad view of Moore's Law, where it's just exponential improvement of computing capability,
*  like OpenAI, for example, recently published this kind of papers looking at the exponential
*  improvement in the training efficiency of neural networks for like ImageNet and all that kind of
*  stuff. We just got better on this. This is purely software side, just figuring out better tricks and
*  algorithms for training neural networks. And that seems to be improving significantly faster than
*  the Moore's Law prediction. So that's in the software space. What do you think, if Moore's Law
*  continues or if the general version of Moore's Law continues, do you think that comes mostly
*  from the hardware, from the software, some mix of the two, some interesting totally,
*  so not the reduction of the size of the transistor kind of thing, but more in the
*  totally interesting kinds of innovations in the hardware space, all that kind of stuff?
*  Well, there's like a half a dozen things going on in that graph. So one is there's initial
*  innovations that had a lot of headroom to be exploited. So the efficiency of the networks
*  has improved dramatically. And then the decomposability of those, they started running
*  on one computer, then multiple computers, then multiple GPUs, and then arrays of GPUs, and
*  they're up to thousands. And at some point, so it's sort of like they were going from like a
*  single computer application to a thousand computer application. So that's not really a Moore's Law
*  thing. That's an independent vector. How many computers can I put on this problem? Because the
*  computers themselves are getting better on like a Moore's Law rate, but their ability to go from
*  one to 10 to 100 to a thousand was something. And then multiplied by the amount of compute it took
*  to resolve like AlexNet to ResNet to transformers. It's been quite steady improvements.
*  But those are like S-curves, aren't they? That's the exactly kind of S-curves that are underlying
*  Moore's Law from the very beginning. So what's the biggest, what's the most productive,
*  rich source of S-curves in the future, do you think? Is it hardware, is it software?
*  So hardware is going to move along relatively slowly. Like, you know, double performance every
*  two years. There's still, I like how you call that slow. Yeah, that's the slow version.
*  The snail's pace of Moore's Law. Maybe we should trademark that one.
*  Whereas the scaling by number of computers, you know, can go much faster. You know, I'm sure at
*  some point Google had, you know, their initial search engine was running on a laptop, you know,
*  like, and at some point they really worked on scaling that. And then they factored the indexer
*  from, you know, this piece and this piece and this piece, and they spread the data and more and more
*  things. And, you know, they did a dozen innovations. But as they scaled up the number of computers on
*  that, it kept breaking, finding new bottlenecks in their software and their schedulers and
*  and made them rethink. Like, it seems insane to do a scheduler across a thousand computers to
*  schedule parts of it and then send the results to one computer. But if you want to schedule a
*  million searches, that makes perfect sense. So there's the scaling by just quantity is probably
*  the richest thing. But then as you scale quantity, like a network that was great on 100 computers,
*  maybe completely the wrong one, you may pick a network that's 10 times slower on 10,000 computers,
*  like per computer. But if you go from 100 to 10,000, that's 100 times. So that's one of the things
*  that happened when we did internet scaling. This efficiency went down, not up. The future of
*  computing is inefficiency, not efficiency. But scales, inefficient scale. It's scaling faster
*  than inefficiency bites you. And as long as there's, you know, dollar value there, like scaling costs
*  lots of money. Yeah. But Google showed, Facebook showed, everybody showed that the scale was where
*  the money was at. So it was worth it financially. Do you think, is it possible that like basically
*  the entirety of earth will be like a computing surface? Like this table will be doing computing,
*  this hedgehog will be doing computing, like everything really inefficient, dumb computing
*  will be leveraged. In science fiction books they call it computronium. Computronium? We turn everything into
*  computing. Well, most of the elements aren't very good for anything. Like you're not going to make a
*  computer out of iron. Like, you know, silicon and carbon have like nice structures. You know,
*  we'll see what you can do with the rest of it. People talk about, well, maybe we can turn the sun
*  into computer, but it's hydrogen and a little bit of helium. So what I mean is more like actually
*  just adding computers to everything. Oh, okay. So you're just converting all the mass of the
*  universe into computer. No, no, no. So not using. That'd be ironic from the simulation point of view
*  is like the simulator build mass to simulate. Yeah. I mean, yeah. So, I mean, ultimately this
*  is all heading towards a simulation. Yeah. Well, I think I might've told you this story. At Tesla,
*  they were deciding, so they want to measure the current coming out of the battery and they
*  decided between putting the resistor in there and putting a computer with a sensor in there.
*  And the computer was faster than the computer I worked on in 1982. And we chose the computer
*  because it was cheaper than the resistor. So, so sure. This hedgehog, you know, it costs $13 and
*  we can put a, you know, an AI that's as smart as you in there for five bucks. It'll have one,
*  you know, so computers will be, you know, be everywhere. I was hoping it wouldn't be
*  smarter than me because well, everything's going to be smarter than you, but you were saying it's
*  inefficient. I thought it was better to have a lot of dumb. Well, Moore's law will slowly compact
*  that stuff. So even the dumb things will be smarter than us. The dumb things are going to be
*  smart or they're going to be smart enough to talk to something that's really smart.
*  You know, it's like, well, just remember like a big computer chip. Yeah. You know,
*  it's like an inch by an inch and you know, 40 microns thick. It doesn't take very much,
*  very many atoms to make a high power computer. Yeah. And 10,000 of them can fit in the shoebox.
*  But, you know, you have the cooling and power problems, but you know, people are working on
*  that, but they still can't write a compelling poetry or music or understand what love is or
*  have a fear of mortality. So, so we're still winning. Neither can most of humanity. So,
*  well, they can write books about it. So, uh, but, but speaking about this, uh, uh, this walk
*  this walk along the path of innovation towards, uh, the dumb things being smarter than humans,
*  you are now the CTO of, uh, of, uh, 10 store and two, as of two months ago,
*  they, uh, build hardware for deep learning. Uh, how do you build scalable and efficient
*  deep learning? This is such a fascinating space. Yeah. Yeah. So it's interesting. So, um,
*  up until recently, I thought there was two kinds of computers. There are serial computers,
*  that run like C programs, and then there's parallel computers. So the way I think about it is,
*  you know, parallel computers have given parallelism, like GPUs are great because
*  you have a million pixels and modern GPUs run a program on every pixel. They call it the shader
*  program, right? So, or like finite element analysis, you, you build something, you know,
*  you make this into little tiny chunks, you give each chunk to a computer. So you're given all
*  these chunks, you have parallelism like that, but most C programs, you write this linear narrative
*  and you have to make it go fast. To make it go fast, you predict all the branches,
*  all the data fetches, and you run that more in parallel, but that's found parallelism.
*  AI is, I'm still trying to decide how fundamental this is. It's a given parallelism problem,
*  but the way people describe the neural networks and then how they write them in PyTorch,
*  it makes graphs. Yeah. That might be fundamentally different than the GPU kind of-
*  Parallelism. Yeah, it might be because the, when you run the GPU program on all the pixels,
*  you're running, you know, depends, you know, this group of pixels say it's background blue and it
*  runs a really simple program. This pixel is, you know, some patch of your face. So you have some
*  really interesting shader program to give you an impression of translucency,
*  but the pixels themselves don't talk to each other. There's no graph,
*  right? So you, you do the image and then you do the next image and you do the next image.
*  And you run 8 million pixels, 8 million programs every time and modern GPUs have like 6,000
*  thread engines in them. So, you know, to get 8 million pixels, each one runs a program on,
*  you know, 10 or 20 pixels. And that's how, that's how they work. There's no graph.
*  But you think graph might be a totally new way to think about hardware.
*  So Rajik and Dori and I have been having this good conversation about given versus found parallelism.
*  And then the kind of walk is we got more transistors, like, you know, computers way back
*  when did stuff on scalar data. Then we did on vector data, famous vector machines. Now we're
*  making computers that operate on matrices, right? And then the category we said that was next was
*  spatial. Like imagine you have so much data that, you know, you want to do the compute on this data.
*  And then when it's done, it says send the result to this pile of data on some software on that.
*  And it's better to think about it spatially than to move all the data to a central processor and
*  do all the work. So spatially, I mean, moving in the space of data as opposed to moving the data.
*  You know, you have a petabyte data space spread across some huge array of computers.
*  And when you do a computation somewhere, you send the result of that computation or maybe
*  a pointer to the next program to some other piece of data and do it. But I think a better
*  word might be graph and all the AI neural networks are graphs. Do some computations and
*  the result here, do another computation, do a data transformation, do a merging, do a pooling,
*  do another computation. Is it possible to compress and say how we make this thing
*  efficient, this whole process efficient, this different? So first, the fundamental elements
*  in the graphs are things like metrics, multiplies, convolutions, data manipulations, and data
*  movements. So GPUs emulate those things with their little singles, you know, basically running a
*  single threaded program. And then there's an Nvidia calls it a warp, where they group a bunch
*  of programs that are similar together. So for efficiency and instruction use. And then at a
*  higher level, you kind of, you take this graph and you say this part of the graph is a matrix
*  multiplier which runs on these 32 threads. But the model at the bottom was built for
*  running programs on pixels, not executing graphs. So it's emulation. Yes. So it's impossible to build
*  something that natively runs graphs. Yes. So that's what 10Store and did. So where are we on that?
*  How like in the history of that effort? Are we in the early days? Yeah, I think so. 10Store and
*  started by a friend of mine, LaBeesha Bajaj and I, I was his first investor. So I've been, you know,
*  so I've been, you know, kind of following him and talking to him about it for years. And in the
*  fall, when I was considering things to do, I decided, you know, we held a conference last year
*  with a friend organized it. And we wanted to bring in thinkers and two of the people were Andre
*  Capasi and Chris Latner. And Andre gave this talk, it's on YouTube called software 2.0, which I think
*  is great, which is we went from programs computers where you write programs to data program computers,
*  you know, like the futures, you know, of software as data programs, the networks. And I think that's
*  true. And then Chris has been where he worked on LLVM, the low level virtual machine, which became
*  the intermediate representation for all compilers. And now he's working on another project called
*  MLIR, which is mid level intermediate representation, which is essentially under the graph about how do
*  you represent that kind of computation and then coordinate large numbers of potentially heterogeneous
*  computers. And I would say technically, tense torrents, you know, two pillars of those, those,
*  those two ideas, software 2.0 and mid level representation, but it's in service of executing
*  graph programs. The hardware is designed to do that. So it's including the hardware piece.
*  Yeah. And then the other cool thing is for a relatively small amount of money, they did a
*  test chip and two production chips. So it's like a super effective team. And, and unlike some AI
*  startups where if you don't build the hardware to run the software that they really want to do,
*  then you have to fix it by writing lots more software. So the hardware naturally does
*  matrix multiply, convolution, the data manipulations, and the data movement between
*  processing elements that, that you can see in the graph, which I think is all pretty clever. And
*  that's, that's what I'm working on now. So the, I think it's called the grace call processor
*  introduced last year. It's, you know, there's a bunch of measures of performance. We're talking
*  about horses. It seems to outperform 368 trillion operations per second seems to
*  outperform Nvidia's Tesla T four system. So these are just numbers. What do they
*  actually mean in real world performance? Like what are the metrics for you that you're chasing
*  in your horse race? Like what do you care about? Well, first, the, so the, the native language of,
*  you know, people who write AI network programs is PyTorch now, PyTorch, TensorFlow. There's a couple
*  others. The PyTorch is one over TensorFlow. It's just, I'm not an expert on that. I know many
*  people have switched from TensorFlow to PyTorch. Yeah. And there is technical reasons for it. And
*  I use both. Both are still awesome. Both are still awesome. But the deepest love is for PyTorch
*  currently. Yeah. There's more love for that. And that may change. So the first thing is when they
*  write their programs, can the hardware execute it pretty much as it was written, right? So PyTorch
*  turns into a graph. We have a graph compiler that makes that graph. Then it fractions the graph
*  down. So if you have big matrix multiply, we turn it into the right size chunks to run on the
*  processing elements. It hooks all the graph up. It lays out all the data. There's a couple of
*  mid-level representations of it that are also simulatable so that if you're writing the code,
*  you can see how it's going to go through the machine, which is pretty cool. And then at the
*  bottom, it schedules kernels like math, data manipulation, data movement kernels,
*  which do this stuff. So we don't have to write a little program to do matrix multiply because
*  we have a big matrix multiplier. There's no SIMD program for that. But there is scheduling for
*  that. So one of the goals is if you write a piece of PyTorch code that looks pretty reasonable,
*  you should be able to compile it and run it on the hardware without having to tweak it and
*  do all kinds of crazy things to get performance. There's not a lot of intermediate steps.
*  It's running directly as written. Like on a GPU, if you write a large matrix multiply naively,
*  you'll get 5 to 10% of the peak performance of the GPU. And then there's a bunch of people
*  publish papers on this. And I read them about what steps do you have to do? And it goes from
*  pretty reasonable, well, transpose one of the matrices. So you do row ordered, not column
*  ordered, block it so that you can put a block of the matrix on different SMs, groups of threads.
*  But some of it gets into little details. Like you have to schedule it just so you don't have
*  register conflicts. So they call them Cuda ninjas. Cuda ninjas. I love it. To get to the optimal
*  point, you either use a pre-written library, which is a good strategy for some things,
*  or you have to be an expert in micro architecture to program it.
*  Right. So the optimization step is way more complicated with the GPU.
*  So our goal is if you write PyTorch, that's good PyTorch, you can do it. Now as the networks are
*  evolving, they've changed from convolutional to matrix multiply. People are talking about
*  conditional graphs. They're talking about very large matrices. They're talking about sparsity.
*  They're talking about problems that scale across many, many chips. So the native
*  data item is a packet. So you send the packet to a processor, it gets processed,
*  it does a bunch of work, and then it may send packets to other processors. And they execute
*  like a data flow graph kind of methodology. Got it.
*  We have a big network on chip, and then the second chip has 16 Ethernet ports to hook lots of them
*  together. And it's the same graph compiler across multiple chips.
*  So that's where the scale comes in.
*  So it's built to scale naturally. Now, my experience with scaling is as you scale,
*  you run into lots of interesting problems. So scaling is a mountain of climb.
*  So the hardware is built to do this, and then we're in the process of...
*  Is there a software part to this with Ethernet and all that?
*  Well, the protocol at the bottom, we send, it's an Ethernet PHY, but the protocol
*  basically says send the packet from here to there, it's all point to point. The header bit
*  says which processor to send it to. And we basically take a packet off our on chip network,
*  put an Ethernet header on it, send it to the other end, strip the header off and send it to
*  the local thing. It's pretty straightforward.
*  Human-to-human interaction is pretty straightforward too, but when you get a million of us,
*  we do some crazy stuff together.
*  Yeah, it can be fun.
*  So is that the goal is scale? So for example, I have been recently doing a bunch of robots at
*  home for my own personal pleasure. Am I going to ever use TestTorrent or is this more for...
*  There's all kinds of problems. There's small inference problems or small training problems
*  or big training problems.
*  What's the big goal? Is it the big training problems or the small training problems?
*  One of the goals is to scale from 100 milliwatts to a megawatt. So really have some range on the
*  problems and the same kind of AI programs work at all different levels. So that's the goal.
*  Since the natural data item is a packet that we can move around, it's built to scale,
*  but so many people have small problems.
*  Right.
*  Like inside that phone is a small problem to solve. So do you see TestTorrent potentially
*  being inside a phone?
*  Well, the power efficiency of local memory, local computation and the way we built it
*  is pretty good. And then there's a lot of efficiency on being able to do conditional
*  graphs and sparsity. I think for complicated networks that want to go in a small factor,
*  it's going to be quite good. But we have to prove that that's a fun problem.
*  And that's the early days of the company, right? It's a couple of years, you said.
*  But you think you invested, you think they're legit as you join.
*  Well, it's also, it's a really interesting place to be. Like the AI world is exploding,
*  and I looked at some other opportunities like build a faster processor, which people want,
*  but that's more on an incremental path than what's going to happen in AI in the next 10 years.
*  So this is kind of an exciting place to be part of.
*  The revolutions will be happening in the very space at TestTorrent.
*  And then lots of people are working on it, but there's lots of technical reasons why some of
*  them aren't going to work out that well. And that's interesting. And there's also the same
*  problem about getting the basics right. Like we've talked to customers about exciting features,
*  and at some point we realized that, we realized they want to hear first about memory bandwidth,
*  local bandwidth, compute intensity, programmability. They want to know the basics,
*  power management, how the network ports work, where the basics, do all the basics work.
*  Because it's easy to say we got this great idea, you know, the crack GPT-3.
*  But the people we talked to want to say, if I buy the, so we have a PCI Express card
*  with our chip on it. If you buy the card, you plug it in your machine, you download the driver.
*  How long does it take me to get my network to run? Right. No, that's a real question.
*  It's a very basic question. So yeah. Is there an answer to that yet?
*  Or is it trying to get to it? Our goal is like an hour.
*  Okay. When can I buy a test? Pretty soon.
*  For my, for the small case training. Yeah, pretty soon. Month.
*  Good. I love the idea of you inside a room with Carpathy, Andre Carpathy and Chris Ladner.
*  Very, very interesting, very brilliant people, very out of the box thinkers,
*  but also like first principles thinkers. Well, they both get stuff done. They only
*  get stuff done to get their own projects done. They talk about it clearly. They educate large
*  numbers of people and they've created platforms for other people to go do their stuff on.
*  Yeah. The clear thinking that's able to be communicated is kind of impressive.
*  It's kind of remarkable though. Yeah, I'm a fan.
*  Well, let me ask, cause I talked to Chris actually a lot these days. He's been one of the,
*  just to give him a shout out in the, he's been so supportive as a human being. So everybody's
*  quite different. Like great engineers are different, but he's been like sensitive to
*  the human element in a way that's been fascinating. Like he was one of the early people on this
*  stupid podcast that I do to say like, don't quit this thing and also talk to whoever the hell you
*  want to talk to that kind of from a legit engineer to get like props and be like, you can do this.
*  That was, I mean, that's what a good leader does, right? It's just kind of
*  let a little kid do his thing. Like go, go do it. Let's see, let's see, see what turns out
*  that that's a, that's a pretty powerful thing. But what do you, what's your sense about, he used to
*  be, he now I think stepped away from Google, right? He said sci-fi, I think. What's really
*  impressive to you about the things that Chris has worked on? Cause it's, we mentioned the optimization,
*  the compiled design stuff, the LLVM. Then there's, he's also at Google worked at the TPU stuff.
*  He's obviously worked on Swift. So the programming language side, talking about people that work in
*  the entirety of the stack. What, from your time interacting with Chris and knowing the guy,
*  what's really impressive to you? It just inspires you. Well, well, like LLVM became,
*  you know, the platform, the de facto platform for, you know, compilers, like it's, it's amazing.
*  And, you know, it was good code quality, good design choices. He hit the right level of abstraction.
*  There's a little bit of the right time, the right place. And then he built a new programming
*  language called Swift, which, you know, after, you know, let's say some adoption resistance became
*  very successful. I don't know that much about his work at Google, although I know that, you know,
*  that, you know, that was a typical, they started TensorFlow stuff and they, you know, it was new,
*  it was, you know, they wrote a lot of code and then at some point it needed to be refactored
*  to be, you know, because it, its development slowed down, why PyTorch started a little later
*  and then passed it. So he did a lot of work on that. And then his idea about MLIR, which is
*  what people started to realize is the complexity of the software stack above the low level IR
*  was getting so high that forcing the features of that until a level was, was putting too much of
*  a burden on it. So he's splitting that into multiple pieces. And that was one of the
*  inspirations for our software stack where we have several intermediate representations that are all
*  executable and you can look at them and do transformations on them before you lower the level.
*  So that was, I think we started before MLIR really got, you know, far enough along to use.
*  But we're interested in that.
*  He's really excited about MLIR. That's his like little baby. So he, he, and there seems to be
*  some profound ideas on that that are really useful.
*  So, so each one of those things has been, as the world of software gets more and more complicated,
*  how do we create the right abstraction levels to simplify it in a way that people can now work
*  independently on different levels of it. So I would say all, all three of those projects, LLVM,
*  Swift and MLIR did that successfully. So I'm interested in what he's going to do next in
*  the same kind of way.
*  Yes. On either the TPU or maybe the Nvidia GPU side, how does Tencent, you think,
*  or the ideas underlying it, does it have to be Tencent or just this kind of graph focused,
*  uh, graph centric hardware, deep learning centric hardware,
*  beat Nvidia's? Do you think it's possible for it to basically overtake Nvidia?
*  Sure.
*  What's, what's that process look like? What's that journey look like you think?
*  Well, GPUs were built to run shader programs on millions of pixels, not to run graphs.
*  Yes.
*  So there's a hypothesis that says the way the graphs, you know, are built is going to be really
*  interesting to be inefficient on computing this. And then the, the primitives is not a SIMD program,
*  it's matrix multiply convolution. And then the data manipulations are fairly extensive about,
*  like how do you do a fast transpose with a program? I don't know if you've ever written
*  a transpose program. They're ugly and slow, but in hardware you can do really well.
*  I got to give you an example. So when GPU accelerators first started doing triangles,
*  like, so you have a triangle, which maps on the set of pixels. So you build, it's very easy,
*  straightforward to build a hardware engine that'll find all those pixels. And it's kind of weird
*  because you walk along the triangle to get to the edge and then you have to go back down to the next
*  row and walk along. And then you have to decide on the edge. If the line of the triangle is like
*  half on the pixel, what's the pixel color? Cause it's half of this pixel and half the next one.
*  That's called rasterization. You're saying that can be done in a, in hardware.
*  That's an example of that operation as a software program is really bad. I've written a program that
*  did rasterization. The hardware that does it, it's actually less code than the software program
*  that does it. And it's way faster. Right. So there are certain times when the abstraction you have
*  rasterize a triangle, execute a graph, components of a graph, the right thing to do in the hardware
*  software boundary is for the hardware to naturally do it. And so the GPU is really optimized for the
*  rasterization of triangles. Well, no, that's just, well, like in a modern, that's a small piece of
*  modern GPUs. What they did is that they still rasterize triangles when you're running the game.
*  But for the most part, most of the computation here, the GPU is running shader programs,
*  but there's single threaded programs on pixels, not graphs.
*  That's to be honest, let's say I don't actually know the, the math behind shader,
*  shading and lighting and all that kind of stuff. I don't know what.
*  They look like little simple floating point programs or complicated ones. You can have
*  8,000 instructions in a shader program, but I don't have a good intuition. Why it could be
*  parallelized so easily. No, it's because you have 8 million pixels in every single. So when you have
*  a light, right. Yeah. That comes down the angle, you know, the amount of light, like, like say this
*  is a line of pixels across this table, right? The amount of light on each pixel is subtly different.
*  And each pixel is responsible for figuring out what. Figure it out. So that pixel says,
*  I'm this pixel. I know the angle of the light. I know the occlusion. I know the color I am
*  like every single pixel here is a different color. Every single pixel gets a different
*  amount of light. Every single pixel has a subtly different translucency. So to make it look realistic,
*  the solution was you run a separate program on every pixel. See, but I thought there's like
*  reflection from all over the place is every pixel. Yeah, but there is. So you build a reflection map,
*  which also has some pixelated thing. And then when the pixels looking at the reflection map has to
*  calculate what the normal of the surface is. And it does it per pixel. By the way, there's both loads
*  of hacks on that. You know, like you may have a lower resolution light map, reflection map. There's
*  all these, you know, tax they do. But at the end of the day, it's per pixel computation.
*  And it's so happening. You can map graph light computation onto the this pixel central
*  competition. You can do floating point programs on convolutions and matrices.
*  And Nvidia invested for years in CUDA, first for HPC. And then they got lucky with the AI trend.
*  But do you think they're going to essentially not be able to
*  hardcore pivot out of their? We'll see. That's always interesting.
*  How often the big companies hardcore pivot occasionally.
*  How much do you know about Nvidia, folks? Some. Some. Well, I'm curious as well. Who's ultimately
*  as a well, they've innovated several times, but they've also worked really hard on mobile. They
*  worked really hard on radios. You know, you know, they're fundamentally a GPU company.
*  Well, they tried to pivot. It's an interesting little
*  game and play in autonomous vehicles, right? With or semi-autonomous, like playing with Tesla and
*  so on and seeing that's a dipping a toe into that kind of pivot. They came out with this platform,
*  which is interesting technically. Yeah. But it was like a 3000 watt,
*  you know, 1000 watt, 3000 dollar, you know, GPU platform.
*  I don't know if it's interesting. Technically, it's interesting philosophically. I
*  technically, I don't know if it's the execution that craftsmanship was there.
*  I'm not sure that I didn't get a sense. They were repurposing GPUs for an automotive solution.
*  Right. It's not a real pivot. They didn't. They didn't build a ground up solution.
*  Like the like the chips inside Tesla are pretty cheap. Like mobile has been doing this.
*  They're doing the classic work from the simplest thing. You know, they were building 40 square
*  millimeter chips and Nvidia, their solution had two 800 millimeter chips and two 200 millimeter
*  chips. And, you know, like boatloads are really expensive DRAMs. And, you know, it's a really
*  different approach. Mobile, I fit the, let's say automotive cost and form factor. And then they
*  added features as it was economically viable. And Nvidia said, take the biggest thing and we're
*  going to go make it work. You know, and that's also influenced like Waymo. There's a whole bunch of
*  autonomous startups where they have a 5,000 watt server in their trunk.
*  Right. And, but that's, that's because they think, well, 5,000 watts and, you know, $10,000 is okay
*  because it's replacing the driver. Elon's approach was that port has to be cheap enough
*  to put it in every single Tesla, whether they turn on autonomous driving or not,
*  which and Mobileye was like, we need to fit in the bomb and, you know, cost structure that car
*  companies do. So they may sell you a GPS for 1500 bucks, but the bomb for that's like $25.
*  Well, and for Mobileye, it seems like neural networks were not first-class citizens. Like
*  the computation, they didn't start out as a- Yeah, it was a CB problem. Yeah. And they did classic
*  CV and found stoplights and lines and they were really good at it. Yeah. And they never, I mean,
*  I don't know what's happening now, but they never fully pivoted. I mean, it's like, it's the Nvidia
*  thing. And then as opposed to, so if you look at the new Tesla work, it's like neural networks
*  from the ground up. Right. Yeah. And even Tesla started with a lot of CV stuff in it and Andre's
*  basically been eliminating it. Move, move everything into the network. So, uh, without,
*  this isn't like confidential stuff, but you sitting on a porch, looking over the world,
*  looking at the work that Andre is doing, that Elon's doing with Tesla autopilot.
*  Do you like the trajectory of where things are going on the hardware side? Well, they're making
*  serious progress. I like the videos of people driving the beta stuff. Like it's taken some
*  pretty complicated intersections and all that, but it's, it's still an intervention per drive.
*  I mean, I have autopilot, the current autopilot, my Tesla, I use it every day. Do you have full
*  self driving beta or no? So you like where this is going? They're making progress. It's taken
*  longer than anybody thought. You know, my, my wonder was, is, you know, hardware three, is it
*  enough computing off by two, off by five, off by 10, off by a hundred. Yeah. And, and I thought
*  it probably wasn't enough, but they're doing pretty well with it now. Yeah. And one thing is
*  because the data set gets bigger, the training gets better. And then there's this interesting
*  thing is you sort of train and build an arbitrary size network that solves the problem. And then you
*  refactor the network down to the thing that you can afford the ship. Right. So the goal isn't to
*  build a network that fits in the phone. It's to build something that actually works. And then,
*  then how do you make that most effective on the hardware you have? And they seem to be doing that
*  much better than a couple of years ago. Well, the one really important thing is also what they're
*  doing well is how to iterate that quickly, which means like, it's not just about one time deployment
*  one building. It's constantly hearing the network and trying to automate as many steps as possible.
*  Right. And that's actually the principles of the software 2.0. Like you mentioned with Andre is,
*  it's not just, I mean, I don't know what the actual, his description of software 2.0 is,
*  if it's just high level philosophical or their specifics, but the interesting thing about
*  what that actually looks in the real world is it's that what I think Andre calls the data engine.
*  It's like, it's the iterative improvement of the thing. You have a neural network that does stuff,
*  fails on a bunch of things and learns from it over and over and over. So you constantly
*  discovering edge cases. So it's very much about like data engineering, like figuring out.
*  It's kind of what you were talking about with 10 store is you have the data landscape.
*  They have to walk along that data landscape in a way that is constantly improving the
*  the neural network. And that feels like that's the central piece of it.
*  And there's two pieces of it. Like you find edge cases that don't work and then you define
*  something that goes get your data for that. But then the other constraint is whether you have to
*  label it or not. Like the amazing thing about like the GPT-3 stuff is it's unsupervised.
*  So there's essentially infinite amount of data. Now there's obviously infinite amount of data
*  available from cars of people who are successfully driving. But the current pipelines are mostly
*  running on labeled data, which is human limited. So when that becomes unsupervised,
*  right, it'll create unlimited amount of data, which then they'll scale. Now the networks that
*  may use that data might be way too big for cars. But then there'll be the transformation from now
*  we have unlimited data, I know exactly what I want. Now can I turn that into something that fits in
*  the car? And that process is going to happen all over the place. Every time you get to the place
*  where you have unlimited data. That's what software 2.0 is about, unlimited data training networks to
*  do stuff without humans writing code to do it. And ultimately also trying to discover like you're
*  saying the self supervised formulation of the problem. So the unsupervised formulation of the
*  problem. Like, you know, in driving, there's this really interesting thing, which is you look at a
*  scene that's before you, and you have data about what a successful human driver did in that scene,
*  you know, one second later, it's a little piece of data that you can use just like with GPT-3 as
*  training. Currently, even though Tesla says they're using that, it's an open question to me,
*  how much, how far can you, can you sell all of the driving with just that self supervised piece
*  of data? And like, I think that's what ComaEye is doing. That's what ComaEye is doing. But the
*  question is how, how much data, so what ComaEye doesn't have is as good of a data engine, for
*  example, as Tesla does. That's where the, like the organization of the data, I mean, as far as I know,
*  I haven't talked to George, but they do have the data. The question is how much data is needed?
*  Because we say infinite very loosely here. It's, it's, and then the other question, which you said,
*  I don't know if you think it's still an open question is, are we on the right order of magnitude
*  for the compute necessary? That is, is this, is it like what Elon said, this chip that's in there now
*  is enough to do full self driving or do we need another order of magnitude? I think nobody actually
*  knows the answer to that question. I like the confidence that Elon has, but.
*  Yeah, we'll see. There's another funny thing is you don't learn to drive with infinite amounts of
*  data. You learn to drive with an intellectual framework that understands physics and color and
*  horizontal surfaces and laws and roads and, you know, all your, your experience from manipulating
*  your environment. Like, look, there's so many factors go into that. So then when you learn to drive,
*  like driving is a subset of this conceptual framework that you have.
*  Right. And so with self driving cars right now, we're, we're teaching them to drive with driving
*  data. You never teach a human to do that. You teach a human all kinds of interesting things, like
*  language, like don't do that, you know, watch out, you know, there's all kinds of stuff going on.
*  This is where you, I think previous time we talked about, where you poetically, uh,
*  disagreed with my naive notion about humans. I just think that humans will make this whole
*  driving thing really difficult. Yeah. All right. I said, he was not moved that slow.
*  It's a ballistics problem. It's a ballistic, humans are ballistics problem, which is like poetry to
*  me. It's very, it's very possible that in driving, they're indeed purely a ballistics problem. I,
*  and I think that's probably the right way to think about it, but I still, they still continue
*  to surprise me. Those damn pedestrians, the cyclists, other humans in other cars.
*  And yeah, but it's going to be one of these compensating things. So the,
*  like when you're driving, you have an intuition about what humans are going to do, but you don't
*  have 360 cameras and radars and you have an attention problem. So you, so, so the self-driving
*  car comes in with no attention problem, 360 cameras, right? You know, a bunch of other
*  features. So they'll wipe out a whole class of accidents, right? And, you know, you know,
*  emergency braking with radar and especially as it gets, you know, AI enhanced will eliminate
*  collisions. Right. But then you have the other problems of these unexpected things where,
*  you know, you think your human intuition is helping, but then the cars also have,
*  you know, a set of hardware features that you're not even close to.
*  And the key thing of course is if you wipe out a huge number of kind of accidents, then it might
*  be just way safer than a human driver, even though, even if humans are still a problem,
*  that's hard to figure out. Yeah, that's probably what happens. Autonomous cars will have a small
*  number of accidents humans would have avoided, but the wipe they'll get rid of the bulk of them.
*  What do you think about, uh, like Tesla's dojo efforts or it can be bigger than Tesla in general.
*  It's kind of like the tense torrent, uh, trying to innovate. Like this is the dichotomy. Like
*  should a company try to from scratch build its own neural network training hardware?
*  Well, first of all, I think it's great. So we need lots of experiments, right? And there's lots of
*  startups working on this and they're pursuing different things.
*  Now I was there when we started dojo and it was sort of like, what's the unconstrained
*  computer solution to go do very large training problems. And then there's fun stuff. Like,
*  you know, we said, well, we have this 10,000 watt board to cool. Well, you go talk to guys at SpaceX
*  and they think 10,000 watts is a really small number, not a big number. And, and there's
*  brilliant people working on it. I'm curious to see how it'll come out. I couldn't tell you,
*  you know, I know it pivoted a few times since I left. So the cooling does seem to be a big
*  problem. I do like what Elon said about it, which is like, we don't want to do the thing
*  unless it's way better than the alternative, whatever the alternative is. So it has to be
*  way better than like racks of GPUs. Yeah. And the other thing is just like, you know,
*  you know, the Tesla autonomous driving hardware, it was only serving one software stack
*  and the hardware team and the software team were tightly coupled. You know, if you're building a
*  general purpose AI solution and you know, there's so many different customers with so many different
*  needs. Now something Andre said is, I think this is amazing. 10 years ago, like vision,
*  recommendation, language were completely different disciplines. He said the people
*  literally couldn't talk to each other. And three years ago, it was all neural networks,
*  but the very different neural networks. And recently it's converging on one side of the
*  networks. They vary a lot in size. Obviously they vary in data, vary in outputs, but the technology
*  has converged a good bit. Yeah. The transformers behind GPT-3, it seems like they could be applied
*  to video. They could be applied to a lot of, and it's like, and they're all really simple.
*  It was like to literally replace letters with pixels. It does vision. It's amazing.
*  And then size actually improves the thing. So the bigger it gets, the more compute you throw at it,
*  the better it gets. And the more data you have, the better it gets. So then you start to wonder,
*  well, is that a fundamental thing or is this just another step to some fundamental understanding
*  about this kind of computation, which is really interesting. Us humans don't want to believe that
*  that kind of thing will achieve conceptual understanding, as you were saying. Like you'll
*  figure out physics, but maybe it will. Maybe. Probably will. Well, it's worse than that.
*  It'll understand physics in ways that we can't understand. I liked your Stephen Wolfram talk
*  where he said, you know, there's three generations of physics. There was physics by reasoning. Well,
*  big things should fall faster than small things, right? That's reasoning. And then there's physics
*  by equations. But the number of programs in the world that are solved with the single equations
*  relatively low. Almost all programs have more than one line of code, maybe 100 million lines of code.
*  So he said, then now we're going to physics by equation, which is his project, which is cool.
*  I might point out that there was two generations of physics before reasoning, habit. Like all animals,
*  no things fall and birds fly and predators know how to solve a differential equation to cut off an
*  accelerating, curving animal path. And then there was the gods did it.
*  There's five generations. Now, software 2.0 says programming things is not the last step.
*  Data. So there's going to be a physics by Stephen Wolfram's concession.
*  That's not explainable to us.
*  And actually, there's no reason that I can see why that even that's the limit.
*  Like there's something beyond that. I mean, usually when you have this hierarchy, it's not like,
*  well, if you have this step and this step and this step and they're all qualitatively different
*  and conceptually different, it's not obvious why, you know, six is the right number of
*  hierarchy steps and not seven or eight or. Well, then it's probably impossible for us
*  to comprehend something that's beyond the thing that's not explained.
*  But the thing that understands the thing that's not explainable to us
*  conceives the next one. And like, I'm not sure why there's a limit to it.
*  Click your brain hearts. That's a sad story.
*  If we look at our own brains, which is an interesting illustrative example,
*  in your work with Tess and trying to design deep learning architectures, do you think about
*  the brain at all? Maybe from a hardware designer perspective, if you could change
*  something about the brain, what would you change or do?
*  Funny question.
*  How would you do?
*  So your brain is really weird. Like, you know, your cerebral cortex, where we think we do most
*  of our thinking is what, like six or seven neurons thick.
*  Yeah.
*  Like that's weird. Like all the big networks are way bigger than that,
*  like way deeper. So that seems odd. And then, you know, when you're thinking if it's, if,
*  if the input generates a result, you can lose, it goes really fast. But if it can't,
*  that generates an output. That's interesting, which turns into an input. And then your brain
*  into the point where you mull things over for days and how many trips through your brain is that,
*  right? Like it's, you know, 300 milliseconds or something to get through seven levels of neurons.
*  I forget the number exactly, but then it does it over and over and over as it searches.
*  And the brain clearly is, looks like some kind of graph because you have a neuron with,
*  you know, connections and it talks to other ones and it's locally very computationally intense,
*  but it's also does sparse computations across a pretty big area.
*  There's a lot of messy biological type of things. And it's, it's meaning like, first of all,
*  there's mechanical, chemical and electrical signals. It's all that's going on.
*  Then the, there's the, the asynchronicity of signals. And there's like, there's just a lot
*  of variability. It seems continuous and messy and just a mess of biology. And it's unclear whether
*  that's a good thing or it's a bad thing. Because if it's a good thing, then we need to run the
*  entirety of the evolution. Well, we're going to have to start with basic bacteria to create some,
*  imagine we could control, you could build a brain with 10 layers. Would that be better or worse?
*  Or more, more connections or less connections or, you know, we don't know to what level our brains
*  are optimized. But if I was changing things, like, you know, you can only hold like seven
*  numbers in your head. Like why not a hundred or a million? And why can't, like, why can't we have
*  like a floating point processor that can compute anything we want, like, and see it all properly?
*  Like that would be kind of fun. And why can't we see in four or eight dimensions?
*  Like, look, it's, you know, 3D is kind of a drag. Like all the hard math transforms are up in
*  multiple dimensions. So there's the, you know, you could imagine a rain architecture that,
*  you know, you could enhance with a whole bunch of features that would be,
*  you know, really useful for thinking about things.
*  It's possible that the limitations you're describing are actually essential for like,
*  the constraints are essential for creating like the depth of intelligence like that,
*  the ability to reason, you know.
*  Yeah, it's hard to say because like your brain is clearly a parallel processor,
*  you know, you know, 10 billion neurons talking to each other at a relatively low clock rate.
*  But it produces something that looks like a serial thought process,
*  it's a serial narrative in your head.
*  That's true.
*  But then there are people famously who are visual thinkers, like, I think I'm a relatively
*  visual thinker. I can imagine any object and rotate it in my head and look at it.
*  And there are people who say they don't think that way at all.
*  And recently I read an article about people who say they don't have a voice in their head.
*  They can talk, but when they, you know, it's like, well, what are you thinking?
*  They'll describe something that's visual.
*  So that's curious.
*  Now, if you're saying, if we dedicated more hardware to holding information like, you know,
*  10 numbers or a million numbers, like, would that just distract us from our ability to form this
*  kind of singular identity?
*  Like it dissipates somehow.
*  Right. But maybe, you know, future humans will have many identities that have some higher level
*  have some higher level organization, but can actually do lots more things in parallel.
*  Yeah. There's no reason if we're thinking modularly, there's no reason we can't have
*  multiple consciousnesses in one brain.
*  And maybe there's some way to make it faster so that the area of the computation could
*  still have a unified feel to it while still having way more ability to do parallel stuff
*  at the same time. Could definitely be improved.
*  Could be improved?
*  Yeah.
*  Well, it's pretty good right now.
*  Actually, people don't give it enough credit.
*  The thing is pretty nice.
*  The, you know, the fact that the right ends seem to be give a nice like spark of beauty to the whole
*  experience.
*  I don't know.
*  I don't know if it can be improved easily.
*  It could be more beautiful.
*  I don't know how I, what do you mean?
*  What do you mean how all the ways you can't imagine?
*  No, but that's the whole point.
*  I wouldn't be able to imagine the fact that I can imagine ways in which it could be more beautiful.
*  Means that, you know, you know, Ian Banks, his stories, so the super smart AIs there
*  live mostly live in the world of what they call infinite fun because they can create
*  arbitrary worlds.
*  So they interact and, you know, the story has it.
*  They interact in the normal world and they're very smart and they can do all kinds of stuff.
*  And, you know, a given mind can, you know, talk to a million humans at the same time
*  because we're very slow and for reasons, you know, artificial to the story, they're
*  interested in people and doing stuff, but they mostly live in this, this other land of thinking.
*  My inclination is to think that the ability to create infinite fun will, will not be so fun.
*  That's sad.
*  Why there are so many things to do.
*  Imagine being able to make a star, move planets around.
*  Yeah.
*  Yeah.
*  But because we can imagine that as why life is fun.
*  If we can, if we actually were able to do it, it'd be a slippery slope where fun would
*  even have a meaning because we just consistently desensitize ourselves by the infinite amounts
*  of fun we're having and the sadness, the dark stuff is what makes it fun.
*  I think that could be the Russian.
*  It could be the, could be the fun makes it fun and the sadness makes it bittersweet.
*  Yeah, that's true.
*  Fun could be the thing that makes it fun.
*  So what do you think about the expansion?
*  Not through the biology side, but through the BCI, the brain computer interfaces.
*  Now you got a chance to check out the new link stuff.
*  It's super interesting.
*  Like, like humans, like, like our thoughts to manifest this action, you know, like,
*  like as a kid, you know, like shooting a rifle was super fun driving a mini bike, doing things.
*  And then computer games, I think for a lot of kids became the thing where they,
*  you know, they can do what they want.
*  They can fly a plane, they can do this, they can do this.
*  Right.
*  But you have to have this physical interaction.
*  Now imagine, you know, you could just imagine stuff and it happens.
*  Right.
*  Like really richly and interestingly, like we kind of do that when we dream, like dreams are funny
*  because like if you have some control or awareness in your dreams, like it's very
*  realistic looking or not realistic depends on the dream, but you can also manipulate that.
*  And, you know, what's possible there is, is odd.
*  And the fact that nobody understands it's hilarious.
*  But do you think it's possible to expand that capability through computing?
*  Sure.
*  Is there some interesting, so from a hardware designer perspective, is there
*  do you think it'll present totally new challenges in the kind of hardware required that like,
*  so this hardware isn't standalone computing?
*  Well, this is not working with the brain.
*  So today computer games are rendered by GPUs.
*  Right.
*  Right. So, but you've seen the GAN stuff.
*  Yep.
*  Right. Where trained neural networks render realistic images, but there's no pixels,
*  no triangles, no shaders, no light maps, no nothing.
*  So the future of graphics is probably AI.
*  Right.
*  Now that AI is heavily trained by lots of real data.
*  Right. So if you have an interface with an AI renderer, right.
*  So if you say render a cat, it won't say, well, how tall is the cat and how big it,
*  you know, it'll render a cat.
*  You might say, oh, a little bigger, a little smaller, you know,
*  make it a tabby shorter hair, you know, like you could tweak it.
*  Like the amount of data you'll have to send to interact with a very powerful AI renderer
*  could be low.
*  But the question is, if we're brain computer interfaces, we'd need to render not onto a
*  screen, but render onto the brain and like directly.
*  So there's a ban.
*  Well, it could do it both ways.
*  I mean, our eyes are really good sensors.
*  It could render onto a screen and we could feel like we're participating in it.
*  You know, they're going to have, you know, like the Oculus kind of stuff.
*  It's going to be so good when a projection to your eyes, you think it's real.
*  You know, they're slowly solving those problems.
*  And I suspect when the renderer of that information into your head is also AI mediated,
*  they'll be able to give you the cues that, you know, you really want for depth and all
*  kinds of stuff.
*  Like your brain is partly faking your visual field.
*  Right.
*  Like your eyes are twitching around, but you don't notice that.
*  Occasionally they blank.
*  You don't notice that, you know, there's all kinds of things like you think you see
*  over here, but you don't really see there.
*  It's all fabricated.
*  A peripheral vision is fascinating.
*  So if you have an AI renderer that's trained to understand exactly how you see
*  and the kind of things that enhance the realism of the experience could be super real, actually.
*  So I don't know what the limits that are, but obviously if we have a brain interface
*  that goes in inside your visual cortex in a better way than your eyes do, which is
*  possible, it's a lot of neurons.
*  Maybe that'll be even cooler.
*  But the really cool thing is that it has to do with the infinite fun that you're referring
*  to, which is our brains seem to be very limited.
*  And like you said, computations.
*  Also very plastic.
*  Very plastic.
*  Yeah.
*  So it's a interesting combination.
*  The interesting open question is the limits of that neuroplasticity.
*  Like how flexible is that thing?
*  Because we haven't really tested it.
*  We know about that.
*  The experiments where they put like a pressure pad on somebody's head and had a visual
*  transducer pressurize it and somebody slowly learned to see.
*  Yep.
*  Especially at a young age, if you throw a lot at it, like what can it
*  arbitrarily expand it with computing power, so get connected to the internet directly
*  somehow.
*  Yeah, the answer's probably yes.
*  So the problem with biology and ethics is like there's a mess there.
*  Like us humans are perhaps unwilling to take risks into directions that are full of
*  uncertainty.
*  So it's like.
*  90% of the population is unwilling to take risks.
*  The other 10% is rushing into the risks unaided by any infrastructure whatsoever.
*  And that's where all the fun happens in society.
*  There's been huge transformations in the last couple thousand years.
*  Yeah, it's funny.
*  I mean, I got an opportunity to interact with this Matthew Johnson from Johns Hopkins.
*  He's doing this large scale study of psychedelics.
*  It's becoming more and more.
*  I've gotten a chance to interact with that community of scientists working on psychedelics,
*  but because of that, that opened the door to me to all these, what do they call?
*  Psychonauts, the people who, like you said, the 10% who are like, I don't care.
*  I don't know if there's a science behind this.
*  I'm taking this spaceship to.
*  If I'm be the first on Mars, I'll be the, you know, psychedelics interesting in the
*  sense that in another dimension, like you said, it's a way to explore the limits of
*  the human mind.
*  Like, what is this thing capable of doing?
*  Cause you kind of like when you dream, you detach it.
*  I don't know exactly in your science of it, but you detach your like reality from what
*  your mind, the images your mind is able to conjure up and your mind goes into weird places.
*  Entities appear somehow Freudian type of like trauma is probably connected in there somehow,
*  but you start to have like these weird vivid worlds that like.
*  So do you actively dream?
*  Do you, why not?
*  I have like six, six hours of dreams and it's like really useful time.
*  I know I haven't.
*  I don't for some reason.
*  I just knock out and I have sometimes like anxiety inducing kind of like very pragmatic
*  like nightmare type of dreams, but not nothing fun, nothing, nothing fun, nothing fun.
*  I, I try, I, I unfortunately have mostly have fun in the waking world, which is very limited
*  in the amount of fun you can have.
*  It's not that limited either.
*  Yeah, that's why we'll have to talk.
*  Yeah, I need instructions.
*  Yeah.
*  Well, there's like a manual for that.
*  You might want to.
*  I looked it up.
*  I'll ask you on what, uh, what did you dream?
*  You know, years ago and I read about, you know,
*  like, you know, a book about how to have, you know, become aware of your dreams.
*  I worked on it for a while.
*  Like there's this trick about, you know, imagine you can see your hands and look out and,
*  and I got somewhat good at it.
*  Like, but my mostly when I'm thinking about things or working on problems, I, I,
*  I prep myself before I go to sleep.
*  It's like, I pull into my mind, all the things I want to work on or think about.
*  And then that let's say greatly improves the chances that I'll,
*  I'll work on that while I'm sleeping.
*  And then, and then I also, you know, basically asked to remember it.
*  And I often remember very detailed within the dream or outside the dream.
*  Well, to bring it up in, in my dreaming and then remember when I wake up,
*  it's just, it's more of a meditative practice to say, you know, the prepare yourself to do that.
*  Like if you go to, you know, the sleep, still gnashing your teeth about some random thing
*  that happened that you're not that really interested in, you'll dream about it.
*  That's right.
*  That's really interesting.
*  Maybe you can direct your dreams somewhat by prepping.
*  Yeah. I wanted to try that.
*  It's really interesting.
*  Like the most important, the interesting, not like, uh, what, what did this guy send
*  an email kind of like stupid worries stuff, but like fundamental problems.
*  You're actually concerned about prepping and interesting things you're worried about
*  or books you're reading or, you know, some great conversation you had or some,
*  some adventure you want to have.
*  There's a lot of space there and, and it seems to work that, you know,
*  my percentage of interesting dreams and memories went up.
*  Is there, uh, is that the source of, uh, if you were able to deconstruct,
*  like where some of your best ideas came from, is there a process that's at the core of that?
*  Like, so some people, you know, walk and think some people like in the shower,
*  the best ideas hit them.
*  If you talk about like Newton, Apple hitting them on the head.
*  No, I, I, I found out a long time ago.
*  I'm, I, I process things somewhat slowly.
*  So like in college, I had friends who could study at the last minute, get an A next day.
*  I can't do that at all.
*  So I always front loaded all the work.
*  Like I do all the problems early, you know, for finals, like the last three days,
*  I wouldn't look at a book because I want, you know, cause like a new fact,
*  the day before finals may screw up my understanding of what I thought I knew.
*  So my, my, my goal was to always get it in and, and give it time to soak.
*  And I used to, you know, I remember when we were doing like 3d calculus,
*  I would have these amazing dreams of 3d surfaces for normal, you know, calculating the gradient.
*  And this is like all come up.
*  This would be so, it was like really fun, like very visual.
*  And, and if I got cycles of that, that was useful.
*  And the other is, is don't over filter your ideas.
*  Like I like that process of brainstorming where lots of ideas can happen.
*  I like people who have lots of ideas and then there's a, then there's a, yeah,
*  I'll let them sit and let it breathe a little bit and then reduce it to practice.
*  Like at some point you really have to, does it really work?
*  Like, you know, is this real or not?
*  Right.
*  But you, but you have to do both.
*  There's great attention there.
*  Like how do you be both open and, you know, precise.
*  Have you had ideas that you just, that sit in your mind for like years before the, sure.
*  It's an interesting way to just generate ideas and just let them sit,
*  let them sit there for a while.
*  I think I have a few of those ideas.
*  You know, it was so funny.
*  Yeah.
*  I think that's, you know, creativity discipline or something.
*  For the slow thinkers in the, in the room, I suppose.
*  As I, some people, like you said, are just like, like the.
*  Yeah, it's really interesting.
*  We like, there's so much diversity in how people think, you know, how fast or slow they are,
*  how well they remember it.
*  Don't look, you know, I'm not super good at remembering facts, but processes and methods.
*  Like in our engineering, I went to Penn State and almost all our engineering
*  tests were open book.
*  I could remember the page and not the formula,
*  but as soon as I saw the formula, I could remember the whole method if I, if I'd learned it.
*  Yeah.
*  No, so it's, it's a funny, where some people could, you know, I just watched friends like
*  flipping through the book, trying to find the formula, even knowing that they'd done just as
*  much work.
*  And I would just open the book and I was on page 27, bottom half.
*  I could see the whole thing visually.
*  Yeah.
*  And you know.
*  And you have to learn that about yourself and figure out what the, what the function
*  optimally.
*  I had a friend who, who was always concerned.
*  He didn't know how he came up with ideas.
*  He had lots of ideas, but he said they just sort of popped up.
*  Like you'd be working on something, have this idea and like, where does it come from?
*  But you can have more awareness of it.
*  Like, like, like, like how you, how your brain works is a little murky as you go down from
*  the voice in your head or the obvious visualizations.
*  Like when you visualize something, how does that happen?
*  Yeah.
*  If I say, you know, visualize volcano, it's easy to do, right?
*  You can.
*  And what does it actually look like when you visualize it?
*  I can visualize to the point where I don't see very much out of my eyes and I see the
*  colors of the thing I'm visualizing.
*  Yeah.
*  But there's like a, there's a shape, there's a texture, there's a color, but there's also
*  conceptual visualization.
*  Like what are you actually visualizing when you're visualizing a volcano, just like with
*  peripheral vision, you think you see the whole thing.
*  Yeah.
*  Yeah.
*  Yeah.
*  That's a good way to say it.
*  You have this kind of almost peripheral vision of your visualizations.
*  They're like these ghosts, but if you know, if you, if you work on it, you can get a pretty
*  high level of detail.
*  And somehow you can walk along those visualizations that come up in the night.
*  Yeah.
*  Which is weird.
*  But when you're thinking about solving problems, like you're, you're putting information in,
*  you're exercising the stuff you do know, you're sort of teasing the area that you don't understand
*  and don't know, but you can almost feel that process happening.
*  That's how I like, like, like I know sometimes when I'm working really hard on something,
*  like, like I get really hot when I'm sleeping and it's like, we got the blank throw, I wake
*  up with all the blanks are on the floor.
*  And every time it's while I wake up and think, wow, that was great.
*  Are you able to, to reverse engineer what the hell happened there?
*  Sometimes it's vivid dreams.
*  And sometimes it's just kind of like you say, like shadow thinking that you sort of have
*  this feeling you're, you're going through this stuff, but it's, it's not that obvious.
*  Isn't that so amazing that the mind just does all these little experiments.
*  I never, you know, I thought, I always thought it's like a river that you can't, you're just
*  there for the ride, but you're right.
*  If you prep it,
*  No, it's all understandable.
*  Meditation really helps.
*  You got to start figuring out you need to learn the language of your own mind.
*  And there's been multiple levels of it, but the abstractions again, right?
*  It's somewhat comprehensible and observable and feelable or whatever the right word is.
*  Yeah.
*  You're not long for the ride.
*  You are the ride.
*  I have to ask you, hardware engineer working on your own networks now,
*  what's consciousness?
*  What the hell is that thing?
*  Is that, is that just some little weird quirk of our particular computing device?
*  Or is it something fundamental that we really need to crack open it for to,
*  to build like good computers?
*  Do you ever think about consciousness?
*  Like why it feels like something to be?
*  I know it's, it's, it's really weird.
*  So, yeah, I mean, everything about it is weird.
*  First is to half a second behind reality.
*  Right.
*  It's a post-hoc narrative about what happened.
*  You've already done stuff by the time you're conscious of it.
*  And your consciousness generally is a single threaded thing,
*  but we know your brain is 10 billion neurons running some crazy parallel thing.
*  And there's a really big sorting thing going on there.
*  It also seems to be really reflective in the sense that
*  you create a space in your head.
*  Like, like we don't really see anything, right?
*  Like photons hit your eyes, it gets turned into signals,
*  it goes through multiple layers of neurons.
*  You know, like I'm so curious at the, you know,
*  that looks glassy and that looks not glassy.
*  Like, like how the resolution of your vision is so high
*  yet to go through all this processing.
*  Where for most of it, it looks nothing like vision.
*  Like, like there's no theater in your mind.
*  Right.
*  So we, we have a world in our heads.
*  We're literally just isolated behind our sensors,
*  but we can look at it, speculate about it,
*  speculate about alternatives, problem solve, what if, you know,
*  there's so many things going on and that process is lagging reality.
*  And it's single threaded, even though the underlying thing is like massively parallel.
*  So it's so curious.
*  So imagine you're building an AI computer.
*  If you wanted to replicate humans, well, you'd have huge arrays of neural networks
*  and apparently only six or seven deep, which is hilarious.
*  They don't even remember seven numbers,
*  but I think we can upgrade that a lot.
*  Right.
*  And then somewhere in there, you would train the network to create
*  basically the world that you live in.
*  Right.
*  So it tells stories to itself about the world that it's perceiving.
*  Well, create the, create the world, tell stories in the world,
*  and then have many dimensions of, you know, like side jobs to it.
*  Like we have an emotional structure, like we have a biological structure.
*  And that seems hierarchical too.
*  Like, like if you're hungry, it dominates your thinking.
*  If you're mad, it dominates your thinking.
*  Like, and we don't know if that's important to consciousness or not,
*  but it certainly disrupts, you know, intrudes in the consciousness.
*  Like, so there's lots of structure to that.
*  And we like to dwell on the past.
*  We like to think about the future.
*  We like to imagine.
*  We like to fantasize.
*  Right.
*  And the somewhat circular observation of that is the thing we call consciousness.
*  Now, if you created the computer system, did all things,
*  created worldviews, created future alternate histories,
*  you know, and dwell on past events, you know, accurately or semi-accurately,
*  you know, it's, it's.
*  Will consciousness just spring up like naturally?
*  Well, with that feel, look and feel conscious to you.
*  Like you seem conscious to me, but I don't.
*  External observer sense.
*  Do you think a thing that looks conscious is conscious?
*  Like, do you, again, this is like an engineering kind of question, I think, because.
*  Like, if we want to engineer consciousness,
*  is it okay to engineer something that just looks conscious?
*  Or is that, is there a difference between?
*  Well, we have all consciousness because it's a super effective way to manage our affairs.
*  Yeah.
*  It's the social element.
*  Yeah.
*  Well, it gives us the planning system.
*  You know, we have a huge amount of stuff.
*  Like when we're talking, like the reason we can talk really fast is we're modeling
*  each other a really high level of detail.
*  And consciousness is required for that.
*  Well, all those components together manifest consciousness.
*  Right.
*  So if we make intelligent beings that we want to interact with that were like,
*  you know, wondering what they're thinking, you know, you know, looking for the scene,
*  them, you know, when they interact with them, they, they're interesting, surprising.
*  You know, fascinating, you know, they will probably feel conscious like we do and
*  we'll perceive them as conscious.
*  I don't know why not, but never know.
*  Another fun question on this, because in, in, uh, from a computing perspective,
*  we're trying to create something that's human-like or superhuman-like.
*  Let me ask you about aliens.
*  Hmm.
*  Aliens.
*  Uh, do you think there's intelligent alien civilizations out there?
*  And do you think their, um, technology, their computing, their AI bots, their, uh,
*  their chips are of the same nature as ours?
*  Yeah, I got no idea.
*  I mean, if there's lots of aliens out there, they've been awfully quiet.
*  You know, there's, there's speculation about why there seems to be.
*  There seems to be more than enough planets out there.
*  There's a lot.
*  There's intelligent life on this planet that seems quite different.
*  You know, like, you know, dolphins seem like plausibly understandable.
*  Octopuses don't seem understandable at all.
*  If they live longer than a year, maybe they would be running the planet.
*  They seem really smart and their neural architecture is completely different than ours.
*  Now who knows how they perceive things.
*  I mean, that's the question is for us intelligent beings, we might not be able to perceive other
*  kinds of intelligence if they become sufficiently different than us.
*  So we live in the current constrained world, you know, it's three-dimensional geometry and
*  the geometry defines a certain amount of physics.
*  And, you know, you know, there's like how time work seems to work.
*  There's so many things that seem like a whole bunch of the input parameters to the, you know,
*  another conscious being or the same.
*  Yes.
*  Like if it's biological, biological things seem to be in a relatively narrow temperature range,
*  right?
*  Because, you know, organics don't, aren't stable, too cold or too hot.
*  You know, so there's, if you specify the list of things that input to that,
*  but as soon as we make really smart, you know, beings and they go solve about how to think
*  about a billion numbers at the same time and how to think in n dimensions.
*  There's a funny science fiction book where the, all the society had uploaded into this matrix.
*  And at some point, some of the beings in the matrix thought,
*  I wonder if there's intelligent life out there.
*  So they had to do a whole bunch of work to figure out like how to make a physical thing
*  because their matrix was self-sustaining.
*  And they made a little spaceship and they traveled to another planet.
*  When they got there, there was like life running around, but there was no intelligent life.
*  And then they figured out that there was these huge,
*  you know, organic matrix all over the planet.
*  Inside there were intelligent beings had uploaded themselves into that matrix.
*  So everywhere intelligent life was, as soon as it got smart, it upleveled itself into something
*  way more interesting than 3D geometry.
*  And yeah, it escaped whatever this is.
*  No, not escaped.
*  Upload was better.
*  Yeah.
*  The essence of what we think of as an intelligent being, I tend to like the thought experiment of
*  the organism, like humans aren't the organisms.
*  I like the notion of like Richard Dawkins and memes that ideas themselves are the organisms
*  like that are just using our minds to evolve.
*  So like we're just like meat receptacles for ideas to breed and multiply and so on.
*  And maybe those are the aliens.
*  Yeah.
*  So Jordan Peterson has a line that says, you know, you think you have ideas, but ideas have you.
*  Yeah.
*  Right.
*  Good line.
*  Which, and then we know about the phenomenon of group think.
*  And there are so many things that constrain us, but I think you can examine all that and not be
*  completely owned by the ideas and completely sucked into group think.
*  And part of your responsibility as a human is to escape that kind of phenomena, which isn't,
*  you know, it's one of the creative tension things again.
*  You're constructed by it, but you can still observe it and you can think about it and you
*  can make choices about to some level how constrained you are by it.
*  And, you know, it's useful to do that.
*  But at the same time, and it could be by doing that, you know, the group and society you're
*  part of becomes collectively even more interesting.
*  So, you know, so the outside observer will think, wow, you know, all these lexes running around
*  with all these really independent ideas have created something even more interesting
*  in the aggregate.
*  So, I don't know.
*  Those are lenses to look at the situation, but that'll give you some inspiration,
*  but I don't think they're constraints.
*  Right.
*  You know, as a small little quirk of history, it seems like you're related to Jordan Peterson.
*  Like you mentioned, he's gone through some rough stuff now.
*  Is there some comment you can make about the roughness of the human journey, the ups and downs?
*  Well, I became an expert in benzo withdrawal,
*  like which is you took benzos aspenes and at some point, they interact with GABA circuits,
*  you know, to reduce anxiety and do a hundred other things.
*  Like there's actually no known list of everything they do because they interact with so many parts
*  of your body.
*  And then once you're on them, you habituate to them and you have a dependency.
*  It's not like you're a drug dependency.
*  We're trying to get high.
*  It's a metabolic dependency.
*  And then if you discontinue them, there's a funny thing called kindling,
*  which is if you stop them and then go, you know, you'll have a horrible withdrawal symptoms.
*  If you go back on them at the same level, you won't be stable.
*  And that unfortunately happened to him.
*  Because it's so deeply integrated into all the kinds of systems in the body.
*  It literally changes the size and numbers of neurotransmitter sites in your brain.
*  So there's a process called the Ashton protocol where you taper it down slowly over two years.
*  The people go through that go through unbelievable hell.
*  And what Jordan went through seemed to be worse because
*  on advice of doctors, you know, we'll stop taking these and take this.
*  It was a disaster and he got some, yeah, it was pretty tough.
*  He seems to be doing quite a bit better intellectually.
*  You can see his brain clicking back together.
*  I spent a lot of time with him.
*  I've never seen anybody suffer so much.
*  Well, his brain is also like this powerhouse, right?
*  So I wonder, does a brain that's able to think deeply about the world
*  suffer more through these kinds of withdrawals?
*  I don't know.
*  I've watched videos of people going through withdrawal.
*  They all seem to suffer unbelievably.
*  And, you know, my heart goes out to everybody.
*  And there's some funny math about this.
*  Some doctor said, as best he can tell, you know, there's the standard recommendations,
*  don't take them for more than a month and then taper over a couple of weeks.
*  Many doctors prescribe them endlessly, which is against the protocol, but it's common.
*  And then something like 75% of people when they taper, it's, you know,
*  half the people have difficulty, but 75% get off okay.
*  20% have severe difficulty and 5% have life-threatening difficulty.
*  And if you're one of those, it's really bad.
*  And the stories that people have on this is heartbreaking and tough.
*  So you put some of the fault that the doctors, they just not know what the hell they're doing.
*  I don't know.
*  It's hard to say.
*  It's one of those commonly prescribed things.
*  Like one doctor said, what happens is if you're prescribed them for a reason
*  and then you have a hard time getting off the protocol, basically,
*  the protocol basically says you're either crazy or dependent.
*  And you get kind of pushed into a different treatment regime.
*  You're a drug addict or a psychiatric patient.
*  And so like one doctor said, you know, I prescribed them for 10 years thinking
*  I was helping my patients and I realized I was really harming them.
*  And, you know, the awareness of that is slowly coming up.
*  The fact that they're casually prescribed to people is horrible.
*  And it's bloody scary.
*  And some people are stable on them, but they're on them for life.
*  Like once you know, it's another one of those drugs that,
*  but benzos long range have real impacts on your personality.
*  People talk about the benzo bubble where you get
*  disassociated from reality and your friends a little bit.
*  It's really terrible.
*  The mind is terrifying.
*  We were talking about how the infinite possibility of fun,
*  but like it's the infinite possibility of suffering too,
*  which is one of the dangers of like expansion of the human mind.
*  It's like, I wonder if all the possible human experiences
*  that intelligent computer can have, is it mostly fun or is it mostly suffering?
*  So like if you, if you brute force expand the set of possibilities,
*  like are you going to run into some trouble in terms of like torture and suffering and so on?
*  Maybe our human brain is just protecting us from much more possible pain and suffering.
*  Maybe the space of pain is like much larger than we could possibly imagine.
*  And that the world's in a balance, you know, all the, all the literature on religion and stuff is,
*  you know, the struggle between court, good and evil is,
*  is balanced for very finely tuned for reasons that are complicated.
*  But that's all, that's a long philosophical conversation.
*  Speaking of balance, that's complicated. I wonder, because we're living through one of the more
*  important moments in human history with this particular virus, it seems like pandemics
*  have at least the ability to kill off most of the human population at their worst.
*  And there, there's this fascinating because there's so many viruses in this world.
*  There's so many, I mean, viruses basically run the world in a sense that they've been around
*  very long time. They're everywhere. They seem to be extremely powerful and they're just in
*  the distributed kind of way. But at the same time, they're not intelligent and they're not even
*  living. Do you have like high level thoughts about this virus that like in terms of you being
*  fascinated or terrified or someone between? So I believe in frameworks, right? So like one of
*  them is evolution. Like we're evolved creatures, right? And one of the things about evolution is
*  it's hyper competitive and it's not competitive out of a sense of evil. It's competitive in a sense of
*  there's endless variation and variations that work better when, and then over time, there's so many
*  levels to that competition. Like multisodial life partly exists because of the competition between
*  different kinds of life forms. And we know sex partly exists to scramble our genes so that we have
*  genetic variation against the invasion of the bacteria and the viruses. And it's endless.
*  Like I've read some funny statistic, like the density of viruses and bacteria in the ocean
*  is really high. And one third of the bacteria die every day because the virus is invading them.
*  Like one third of them. Wow. Like, I don't know if that number is true, but it was like,
*  like there's like the amount of competition and what's going on is stunning.
*  And there's a theory as we age, we slowly accumulate bacterias and viruses and as our
*  immune system kind of goes down, you know, that's what slowly kills us. And it just feels so peaceful
*  from a human perspective when we sit back and are able to have a relaxed conversation.
*  And there's wars going on out there. Like right now, you're you're harboring how many bacteria
*  you know, the ones, many of them are parasites on you. And some of them are helpful and some
*  of them are modifying your behavior. And some of them are, you know, it's just really, it's really
*  wild. But you know, this particular manifestation is unusual, you know, in the demographic, how it
*  hit and the political, you know, response that engendered and you know, the health care response
*  that engendered and the technology that's gendered, it's kind of wild. And the communication on Twitter
*  that it led to all that kind of stuff. I'd ever every single level. Yeah.
*  Pete Slauson But what usually kills life, the big extinctions are caused by meteors and volcanoes.
*  Jeffery Sarr That's the one you're worried about as opposed to
*  human created bombs that we launch each other.
*  Pete Slauson Solar flares are another good one. You know, occasionally solar flares hit the planet.
*  Jeffery Sarr So it's nature.
*  Pete Slauson Yeah, it's all pretty wild.
*  Jeffery Sarr On another historic moment, this is perhaps outside,
*  but perhaps within your space of frameworks that you think about that just happened,
*  I guess a couple of weeks ago is, I don't know if you're paying attention at all, is the GameStop
*  and Wall Street Bets. So it's really fascinating. There's kind of a theme to this conversation
*  we have today, because it's like neural networks. It's cool how there's a large number of people in
*  a distributed way, almost having a kind of fund, were able to take on the powerful elites,
*  elite hedge funds, centralized powers, and overpower them. Do you have thoughts on this whole saga?
*  Pete Slauson I don't know enough about finance, but it was like the Elon,
*  you know, Robin Hood guy when they talked.
*  Jeffery Sarr Yeah, what did you think about that?
*  Pete Slauson Well, the Robin Hood guy didn't know how the finance system worked. That was clear.
*  He was treating the people who settled the transactions as a black box. And suddenly,
*  somebody called him up and said, hey, black box calling you. Your transaction volume means you
*  need to put out $3 billion right now. And he's like, I don't have $3 billion. Like, I don't even
*  make any money on these trades. Why do I owe $3 billion while you're sponsoring the trade?
*  So there was a set of abstractions that, you know, I don't think either, like now you understand it.
*  This happens in chip design. Like, you buy wafers from TSMC or Samsung or Intel,
*  and you know, they say it works like this, and you do your design based on that, and then chip
*  comes back and doesn't work. And then suddenly, you start having to open the black boxes. Like,
*  the transistors really work like they said, you know, what's the real issue? So, there's a whole
*  set of things that created this opportunity and somebody spotted it. Now, people spot these kinds
*  of opportunities all the time. There's been flash crashes. There's always short squeezes
*  are fairly regular. Every CEO I know hates the shorts because they're trying to manipulate their
*  stock in a way that they make money and, you know, deprive value from both the company and the
*  investors. So, the fact that, you know, so many stocks were so short, it's hilarious,
*  I guess, that this hasn't happened before. I don't know why. And I don't actually know why
*  some serious hedge funds didn't do it to other hedge funds. And some of the hedge funds actually
*  made a lot of money on this. So, my guess is we know 5% of what really happened and that a lot
*  of the players don't know what happened. And people who probably made the most money aren't the people
*  that they're talking about. Yeah. Do you think there was something, I mean, this is the
*  cool kind of Elon, you're the same kind of conversationalist, which is like first principles
*  questions of like, what the hell happened? Just very basic questions of like, was there something
*  shady going on? What, you know, who are the parties involved? It's the basic questions
*  that everybody wants to know about. Yeah. So, like we're in a very competitive, hyper competitive
*  world, right? But transactions like buying and selling stock is a trust event. You know,
*  I trust the company represented themselves properly. You know, I bought the stock because
*  I think it's going to go up. I trust that the regulations are solid. Now, inside of that,
*  there's all kinds of places where, you know, humans over trust. And, you know, this this exposed,
*  let's say some weak points in the system. I don't know if it's going to get corrected. I don't know
*  if the, I don't know if we have close to the real story. My suspicion is we don't. And listen to
*  that guy, he was like a little wide eyed about it. And then he did this and then he did that. And it
*  was like, I think you should know more about your business than that. But again, there's many
*  businesses when like this layer is really stable, you stop paying attention to it. You pay attention
*  to the stuff that's bugging you or new. You don't pay attention to the stuff that just seems to work
*  all the time. You just, you know, sky's blue every day, California. And every once in a while,
*  I think it rains. And everybody's like, what do we do? Somebody go bring in the lawn furniture.
*  You know, like it's getting wet. You don't know why it's getting wet. Yeah, it doesn't always work.
*  I was blue for like 100 days and now it's, you know, so. But part of the problem here with Vlad,
*  the CEO of Robinhood is the scaling. Because what we've been talking about is there's a lot of
*  unexpected things that happen with the scaling and you have to be,
*  I think the scaling forces you to then return to the fundamentals.
*  Well, it's interesting because when you buy and sell stocks, the scaling is, you know, the stocks
*  only move in a certain range. And if you buy a stock, you can only lose that amount of money.
*  On the short market, you can lose a lot more than you can benefit. Like it has a weird cause,
*  you know, cost function or whatever the right word for that is. So he was trading in a market
*  where he wasn't actually capitalized for the downside. If it got outside a certain range.
*  Now, whether something nefarious has happened, I have no idea. But at some point, the financial
*  risk to both him and his customers was way outside of his financial capacity. And his
*  understanding how the system work was clearly weak or he didn't represent himself. You know,
*  I don't know the person. When I listened to him, Nick, it could have been the surprise question was
*  like, and then these guys called and, you know, it sounded like he was treating stuff as a black
*  box. Maybe he shouldn't have, but maybe his whole pile of experts somewhere else. And it was going
*  on. I don't know. Yeah. I mean, this is, this is one of the qualities of a good leader is under fire.
*  You have to perform and that means to think clearly and to speak clearly. And he dropped the ball on
*  those things because and understand the problem quickly, learn and understand the problem. Like
*  at this like basic level, like what the hell happened. And my guess is, you know, at some level
*  it was amateurs trading against, you know, experts slash insiders slash people with, you know, special
*  information. Outsiders versus insiders. Yeah. And the insiders, you know, my guess is the next time
*  this happens, we'll make money on it. The insiders always win. Well, they have more tools and more
*  incentive. I mean, this always happens. Like the outsiders are doing this for fun. The insiders
*  are doing this 24 stop, but there's numbers in the outsiders. This is the interesting thing.
*  There's numbers on the insiders too. Like different kind of numbers. Yeah. But this could be a new
*  era because I don't know, at least I didn't expect that a bunch of redditors could, you know, there's
*  you know, millions of people get to rise attack. The next one will be a surprise,
*  but don't you think the crowd, the people are planning the next attack?
*  We'll see. But it has to be a surprise. Can't be the same game.
*  And so the, like it could be, there's a very large number of games to play and they can be
*  agile about it. I don't know. I'm not an expert. Right. That's a good question. How the space of
*  games, how restricted is it? Yeah. And the system is so complicated. It could be relatively
*  unrestricted. And also like, you know, during the last couple of financial crashes, you know,
*  what set it off was, you know, sets of derivative events where, you know, Nassim Tlaib's,
*  you know, saying is they're trying to lower volatility in the short run, but creating tail
*  events. And the system's always evolved towards that. And then they always crash. Like the S curve
*  is the, you know, star low ramp plateau crash. It's a hundred percent effective.
*  In the long run, let me ask you some advice to put on your profound hat.
*  There's a bunch of young folks who listen to this thing for no good reason whatsoever.
*  Undergraduate students, maybe high school students, maybe just young folks, young at heart,
*  looking for the next steps to take in life. What advice would you give to a young person today?
*  Well, life, maybe career, but also life in general. Get good at some stuff. Well,
*  get to know yourself, right? Get good at something that you're actually interested in. You have to
*  love what you're doing to get good at it. You really got to find that. Don't waste all your time
*  doing stuff that's just boring or bland or numbing. Right. Don't let old people screw you.
*  Well, people get talked into doing all kinds of shit and racking up huge student deaths.
*  There's so much crap going on. And then drains your time and drains your energy.
*  The Eric Weinstein thesis that the older generation will let go.
*  They're trapping all the young people. Do you think there's some truth to that?
*  Yeah, sure. Just because you're old doesn't mean you stop thinking. I know lots of really original
*  old people. I'm an old person. But you have to be conscious about it. You can fall into the ruts and
*  then do that. When I hear young people spouting opinions that sounds like they come from Fox News
*  or CNN, I think they've been captured by group thinking, memes.
*  They're supposed to think on their own.
*  If you find yourself repeating what everybody else is saying, you're not going to have a good life.
*  Like that's not how the world works. It seems safe, but it puts you at great jeopardy for
*  well, being boring or unhappy.
*  How long did it take you to find the thing that you have fun with?
*  I don't know. I've been a fun person since I was pretty little.
*  I've gone through a couple of periods of depression in my life.
*  For a good reason or for a reason that doesn't make any sense?
*  Yeah. Some things are hard. You go through mental transitions in high school.
*  I was really depressed for a year. I think I had my first midlife crisis at 26.
*  I kind of thought, is this all there is? I was working at a job that I loved,
*  but I was going to work and all my time was consumed.
*  What's the escape out of that depression? What's the answer to is, is this all there is?
*  Well, a friend of mine, I asked him because he was working his ass off. I said,
*  what's your work-life balance? There's work, friends, family, personal time.
*  He bounced in that and he said, work 80%, family 20%. I tried to find some time to sleep.
*  There's no personal time. There's no passionate time.
*  Young people are often passionate about work. I was sort of like that.
*  But you need to have some space in your life for different things.
*  And that's, that creates, that makes you resistant to the whole, the deep dips into
*  depression kind of thing. Yeah. Well, you have to get to know yourself too. Meditation helps.
*  Something physically intense helps. Like the weird places your mind goes kind of thing.
*  And why does it happen? Why do you do what you do?
*  Like triggers, like the things that cause your mind to go to different places kind of thing or
*  events like your upbringing for better or worse, whether your parents are great people or not,
*  you come into adulthood with all kinds of emotional burdens. And you can see some people
*  are so bloody stiff and restrained and they think the world's fundamentally negative.
*  Like you, maybe you have unexplored territory. Yeah. Or you're afraid of something.
*  Definitely afraid of quite a few things. Then you gotta go face them.
*  Like, like what's the worst thing that can happen? You're going to die, right?
*  Like that's inevitable. You might as well get over that. Like a hundred percent death rate.
*  Like people were worried about the virus, but you know, the human condition is pretty deadly.
*  There's something about embarrassment that's, I've competed a lot of my life. And I think the,
*  if I'm to introspect it, the thing I'm most afraid of is being like humiliated.
*  I think nobody cares about that. Like you're the only person on the planet that cares about
*  you being humiliated. So it can really useless thought. It is. It's like,
*  you're humiliated. Something happened in a room full of people and they walk out and they didn't
*  think about it one more second. Or maybe somebody told a funny story to somebody else.
*  Now I know it too. I mean, I've been really embarrassed about shit that nobody cared about
*  myself. It's a funny thing. So the worst thing ultimately is just, yeah, but that's a cage and
*  then you have to get out of it. Like once you, here's the thing. Once you find something like that,
*  you have to be determined to break it. Cause otherwise you'll just, you know, so you accumulate
*  that kind of junk and then you die is a, you know, a mess. So the goal, I guess it's like a
*  cage within a cage. I guess the goal is to die in the biggest possible cage. Well, ideally you'd
*  have no cage. You know, people do get enlightened. I've met a few. It's great. You found a few.
*  There's a few out there. I don't know. Of course there are. Either that or they have, you know,
*  it's a great sales pitch. There's like enlightened people write books and doing all kinds of stuff.
*  It's a good way to sell a book. I'll give you that. You've never met somebody you just thought
*  they just kill me. Like this, like mental clarity, humor. No, 100%. But I just feel like they're
*  living in a bigger cage. They have their own. You still think there's a cage. There's still a cage.
*  You secretly suspect there's always a cage. There's no, there's nothing outside the, the
*  universe. There's nothing outside the cage.
*  You were, you were, you worked in a bunch of companies. You led a lot of amazing teams.
*  I don't, I'm not sure if you've ever been like in the early stages of a startup, but do you have
*  advice for somebody that wants to do a startup or build a company, like build a strong team of
*  engineers that are passionate and just want to solve a big problem? Like, is there a more
*  specifically on that point? You have to be really good at stuff. If you're going to lead and build
*  a team, you better be really interested in how people work and think. The people or the solution
*  to the problem. So there's two things, right? One is how people work and the other is the
*  fact that there's quite a few successful startups. It's pretty clear. The founders don't know anything
*  about people. Like the idea was so powerful that it propelled them, but I suspect somewhere early,
*  they hired some people who understood people because people really need a lot of care and
*  feeding the collaborate and work together and feel engaged and work hard. You know, like startups,
*  it was all about out producing other people. Like you're nimble because you don't have any legacy.
*  You don't have, you know, a bunch of people who are depressed about life, you know, just showing up.
*  You know, so startups have a lot of advantages that way.
*  Do you like the, Steve Jobs talked about this idea of A players and B players. I don't know if you
*  know this formulation.
*  Yeah, no. Organizations that get taken over by B player leaders
*  often really underperform the hierarchy players. That said, in big organizations,
*  there's so much work to do. Like, and there's so many people who are happy to do what, you know,
*  like the leadership or the big idea people would consider menial jobs. And, you know, you need a
*  place for them, but you need an organization that both values and rewards them, but doesn't let them
*  take over the leadership of it. Got it. But so, so you need to have an organization that's
*  resistant to that. But in the early days, the, the notion with, with Steve was that like one B
*  player in a room of A players will be like destructive to the whole. I've seen that happen.
*  I don't know if it's like always true. Like, you know, you, you run into people who clearly
*  B players, but they think they're A players. And so they have a loud voice at the table and they
*  make lots of demands for that. But there's other people are like, I know who I am. I just want to
*  work with, you know, cool people on cool shit and just tell me what to do and I'll go get it done.
*  Yeah. You know, so you have to, again, this is like people skills, like
*  what kind of person is it? You know, I've met some really great people I love working with that
*  weren't the biggest ID people, they're most productive ever, but they show up, they get it
*  done. You know, they, they create connection and community that people value. It's, it's, it's
*  pretty diverse. I don't think there's a recipe for that. I got to ask you about love. I heard
*  you into this now into this love thing. Yeah. Is this, is you think this is your solution to
*  your depression? No, I'm just trying to, like you said, delight in people on occasion, trying to
*  sell a book. I'm writing a book about love. You're writing a book about love. No, I'm not. I'm not.
*  A friend of mine, he's gonna, he said, you should really write a book about that. You're,
*  your management philosophy said it'd be a short book.
*  Well, that one was all pretty well. What role do you think love, family, friendship, all that kind
*  of human stuff play in a successful life? You've been exceptionally successful in the space of
*  like running teams, building cool shit in this world, creating some amazing things. What did
*  love get in the way? Did love help the family get in the way? Did family help friendship?
*  You want the engineer's answer? Please. So like first love is functional, right?
*  It's functional. Yeah. So we habituate ourselves to the environment. And actually Jordan told me,
*  Jordan Peterson told me this line. So you go through life and you just get used to everything,
*  except for the things you love. They, they, they remain new. Like this is really useful for,
*  like other people's children and dogs and trees. You just don't pay that much attention to your
*  own kids. You monitor them really closely. Like, and if they go off a little bit because you love
*  them, if you're smart, if you're going to be a successful parent, you notice it right away.
*  You don't habituate to just things you love. And if you want to be successful at work, if you don't
*  love it, you're not going to put the time in somebody else. There's somebody else that loves
*  it. Like, cause it's new and interesting and that lets you go to the next level.
*  So it's the thing, it's just a function that generates newness and novelty and surprises,
*  you know, all those kinds of things. It's really interesting. And there's people figured out lots
*  of frameworks for this. Like, like humans seem to go in partnership, go through, you know,
*  interests. Like somebody, suddenly somebody's interesting and then you're infatuated with them
*  and then you're in love with them. And then you, you know, different people have ideas about
*  parental love or mature love. Like you go through a cycle of that, which keeps us together and it's,
*  you know, super functional for creating families and creating communities and
*  making you support somebody despite the fact that you don't love them. Like, and,
*  and it can be really enriching. You know, no, no, in the work life balance scheme,
*  if all you do is work, you think you may be optimizing your work potential,
*  but if you don't love your work or you don't have family and friends and things you care about,
*  your brain isn't well balanced. Like everybody knows the experience of your works on something
*  all week. You went home and took two days off and you came back in the odds of you working on the
*  thing, picking up right where you left off is zero. Your brain refactored it. But being above is great.
*  It's like changes the color of the light in the room. It creates a spaciousness that's,
*  that's different. It helps you think. It makes you strong.
*  Bukowski had this line about love being a fog that dissipates with the first light of reality
*  in the morning. That's depressing. I think it's the other way around.
*  It lasts. Well, you, like you said, it's a function. It's a thing that generates.
*  It can be the light that actually enlivens your world and creates the interest and the
*  power and the strengths and the, to go do something. Well, it's like, look, like that sounds like,
*  you know, there's like physical love, emotional love, intellectual love, spiritual love, right?
*  Isn't it all the same thing kind of nope. You should differentiate that. Maybe that's your
*  problem in your book. You should, you should refine that a little bit.
*  The different chapters. Yeah, there's different chapters.
*  What's the, what's these are, aren't these just different layers of the same thing or the stack
*  physical people, people, some people are addicted to physical love and they have no
*  idea about emotional or intellectual love. I don't know if they're the same things. I think
*  they're different. That's true. They could be different. I had to be, I guess the ultimate
*  goals for it to be the same. Well, if you want something to be
*  bigger and interesting, you should find all its components and differentiate them, not
*  clobber together. People do this all the time. They, yeah. And the modularity,
*  get your abstraction layers right. And then you can, you have room to breathe.
*  Well, maybe you can write the forward to my book about love or the afterwards.
*  You really tried. I feel like this has made a lot of progress in this book.
*  Well, you have things in your life that you love.
*  Yeah. Yeah. And they are, you're right. They're modular.
*  It's quite well there. And you can have multiple things with the same person or the same thing.
*  And yeah, but yeah, depending on the moment of the day.
*  Like what Bukowski described is that moment you go from being in love to having a different kind of
*  love. Yeah. Right. And that's a transition. But when it happens, if you read the owner's manual
*  and you believed it, you would have said, oh, this happened. It doesn't mean it's not love.
*  It's a different kind of love. But maybe there's something better about that. As you grow old, if
*  all you do is regret how you used to be, it's sad. Right. You should have learned a lot of things
*  because like who you can be in your future self is actually more interesting and possibly
*  delightful than being a mad kid in love with the next person. That's super fun when it happens, but
*  that's 5% of the possibility. Yeah, that's right. There's a lot more fun to be had in
*  the long lasting stuff. Yeah. Or meaning, if that's your thing. Meaning, which is a kind of fun.
*  It's a deeper kind of fun. And it's surprising. The thing I like is surprises.
*  You just never know what's going to happen. But you have to look carefully and you have to work at it.
*  You have to think about it. Yeah. You have to see the surprises when they happen. You have to be
*  looking for it. From the branching perspective, you mentioned regrets.
*  Do you have regrets about your own trajectory? Oh yeah, of course.
*  Some of it's painful, but you want to hear the painful stuff.
*  I'd say in terms of working with people, when people did stuff I didn't like, especially if
*  it was a bit nefarious, I took it personally and I also felt it was personal about them.
*  But a lot of times, most humans are a mess. And then they act out and they do stuff.
*  And the psychologist I heard a long time ago said, you tend to think somebody does something to you.
*  But really what they're doing is they're doing what they're doing while they're in front of you.
*  It's not that much about you. And as I got more interested in,
*  when I work with people, I think about them and probably analyze them and understand them a little
*  bit. And then when they do stuff, I'm way less surprised. And if it's bad, I'm way less hurt.
*  And I react way less. I sort of expect everybody's got their shit.
*  Yeah. And it's not about you as much.
*  It's not about me that much. It's like you do something and you think you're embarrassed,
*  but nobody cares. And somebody's really mad at you. The odds of it being about you,
*  no, they're getting mad the way they're doing that because of some pattern they learned.
*  And maybe you can help them if you care enough about it. Or you could see it coming and step
*  out of the way. I wish I was way better at that. I'm a bit of a hothead.
*  And you regret that? You said with Steve, that was a feature, not a bug.
*  Yeah. Well, he was using it as the counter for orderliness that would crush his work.
*  You were doing the same.
*  Maybe. I don't think my vision was big enough. It was more like I just got pissed off and did stuff.
*  I'm sure that's what Steve... Yeah.
*  I don't know if it had the... It didn't have the amazing effect of creating a trillion dollar
*  company. It was more like I just got pissed off and left or made enemies that he shouldn't have.
*  Yeah, it's hard. I didn't really understand politics until I worked at Apple,
*  where Steve was a master player of politics and his staff had to be or they wouldn't survive him.
*  And it was definitely part of the culture. And then I've been in companies where they say it's
*  political, but it's all fun and games compared to Apple. And it's not that the people at Apple are
*  bad people. It's just they operated politically at a higher level. It's not like, oh, somebody
*  said something bad about somebody else, which is most politics. It's they had strategies about
*  accomplishing their goals, sometimes over the dead bodies of their enemies. With sophistication...
*  Yeah, more game of Thrones than sophistication and like a big time factor rather than a...
*  You know...
*  Wow, that requires a lot of control over your emotions, I think,
*  to have a bigger strategy in the way you behave.
*  Yeah. And it's effective in the sense that coordinating thousands of people to do really
*  hard things, where many of the people in there don't understand themselves, much less how they're
*  participating, creates all kinds of drama and problems that our solution is political in nature.
*  How do you convince people? How do you leverage them? How do you motivate them? How do you get
*  rid of them? There's so many layers of that that are interesting. And even though some of it,
*  let's say, may be tough, it's not evil. Unless you use that skill to evil purposes, which some
*  people obviously do. But it's a skill set that operates. And I wish I'd... I was interested in
*  it, but it was sort of like, I'm an engineer, I do my thing. And there's times when I could have
*  way bigger impact if I knew how to... If I paid more attention and knew more about that.
*  About the human layer of the stack.
*  Yeah, that human political power expression layer of the stack, which is complicated.
*  And there's lots to know about it. I mean, people are good at it or just amazing.
*  And when they're good at it, and let's say, relatively kind and oriented in a good direction,
*  you can really feel... You can get lots of stuff done and coordinate things that you never thought
*  possible. But all people like that also have some pretty hard edges because, you know, it's a heavy
*  lift. And I wish I'd spent more time like that when I was younger. But maybe I wasn't ready.
*  I was a wide-eyed kid for 30 years.
*  Still a bit of a kid.
*  Yeah, I know.
*  What do you hope your legacy is when there's a book, like a Hitchhiker's Guide to the Galaxy,
*  and there's like a one-sentence entry by Jim Miller from like that guy lived at some point.
*  There's not many people who'll be remembered. You're one of the sparkling little human creatures
*  that had a big impact on the world. How do you hope you'll be remembered?
*  My daughter was trying to get... She edited my Wikipedia page to say that I was a legend
*  and a guru. But they took it out, so she put it back in. She's 15. I think that was probably
*  the best part of my legacy. She got her sister, and they were all excited. They were like trying
*  to put it in the references because there's articles in that on the title.
*  Calling you that? So in the eyes of your kids, you're a legend.
*  Well, they're pretty skeptical because they hope you're better than that. They're like,
*  Dad. So yeah, that kind of stuff is super fun. In terms of the big legends stuff, I don't care.
*  They don't care.
*  Legacy on it. I don't really care.
*  You're just an engineer.
*  Yeah. I've been thinking about building a big pyramid.
*  So I had a debate with a friend about whether pyramids or craters are cooler. And he realized
*  there's craters everywhere, but they built a couple pyramids 5,000 years ago.
*  And they remember you for a while.
*  We're still talking about it. So I think that would be cool.
*  Those aren't easy to build.
*  Oh, I know. And they don't actually know how they built them, which is great.
*  It's either AGI or aliens could be involved. So I think you're going to have to figure out
*  quite a few more things than just the basics of civil engineering.
*  So I guess you hope your legacy is pyramids.
*  That would be cool. And my Wikipedia page, you know, getting updated by my daughter periodically.
*  Like those two things would pretty much make it.
*  Jim, it's a huge honor talking to you again. I hope we talk many more times in the future.
*  I can't wait to see what you do with Tense Torrent. I can't wait to use it.
*  I can't wait for you to revolutionize yet another space in computing.
*  It's a huge honor to talk to you. Thanks for talking to me.
*  This was fun.
*  Thanks for listening to this conversation with Jim Keller. And thank you to our sponsors,
*  Athletic Greens All-in-One Nutrition Drink, Brooklyn and Sheets, ExpressVPN,
*  and Bell Campbell Grass-Fed Meat. Click the sponsor links to get a discount and to support
*  this podcast. And now let me leave you with some words from Alan Turing.
*  Those who can imagine anything can create the impossible.
*  Thank you for listening and hope to see you next time.

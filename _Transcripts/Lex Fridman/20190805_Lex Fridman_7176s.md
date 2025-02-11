---
Date Generated: April 14, 2024
Transcription Model: whisper medium 20231117
Length: 7176s
Video Keywords: []
Video Views: 837166
Video Rating: None
---

# George Hotz: Comma.ai, OpenPilot, and Autonomous Vehicles | Lex Fridman Podcast #31
**Lex Fridman:** [August 05, 2019](https://www.youtube.com/watch?v=iwcYp-XT7UI)
*  The following is a conversation with George Hotz. He's the founder of Kama AI,
*  a machine learning based vehicle automation company. He is most certainly an outspoken
*  personality in the field of AI and technology in general. He first gained recognition for
*  being the first person to carrier unlock an iPhone. And since then, he has done quite a
*  few interesting things at the intersection of hardware and software. This is the Artificial
*  Intelligence podcast. If you enjoy it, subscribe on YouTube, give it five stars on iTunes,
*  support it on Patreon, or simply connect with me on Twitter at Lex Friedman spelled F R I D M A N.
*  And I'd like to give a special thank you to Jennifer from Canada for her support of the
*  podcast on Patreon. Merciful Jennifer. She's been a friend and an engineering colleague for many
*  years since I was in grad school. Your support means a lot and inspires me to keep this series
*  going. And now here's my conversation with George Hotz. Do you think we're living in a simulation?
*  Yes, but it may be unfalsifiable. What do you mean by unfalsifiable? So if the simulation is
*  designed in such a way that they did like a formal proof to show that no information can get in and
*  out. And if their hardware is designed to for the anything in the simulation to always keep the
*  hardware in spec, it may be impossible to prove whether we're in a simulation or not.
*  So they've designed it such that it's a closed system, you can't get outside the system.
*  Well, maybe it's one of three worlds. We're either in a simulation, which can be exploited.
*  We're in a simulation, which not only can't be exploited, but like the same thing is true
*  about VMs. A really well designed VM, you can't even detect if you're in a VM or not.
*  That's brilliant. So we're it's Yeah, so the simulation is running on a virtual machine.
*  Yeah. But now in reality, all VMs have ways to the fact. That's the point. I mean, is it you've
*  done quite a bit of hacking yourself. And so you should know that really any complicated system
*  will have ways in and out. So this isn't necessarily true going forward.
*  I spent my time away from comma, I learned a cock is a dependently typed like,
*  it's a language for writing math proofs. And if you write code that compiles in a language like
*  that, it is correct by definition, the types check it's correctness. So it's possible that
*  the simulation is written in a language like this, in which case, yeah, but that can't be
*  sufficiently expressive a language like that. Oh, it can. It can be. Yeah. Okay. Well, so
*  all right, so the simulation doesn't have to be tearing complete if it has a scheduled end date.
*  Looks like it does actually with entropy. I mean, I don't think that a simulation that results in
*  something as complicated as the universe would have a formal proof of correctness.
*  Right. It's possible, of course, we have no idea how good their tooling is. And we have no idea
*  how complicated the universe computer really is. It may be quite simple. It's just very large,
*  right? It's very, it's definitely very large. But the fundamental rules might be super simple. Yeah,
*  Conway's going to like kind of stuff. Right. So if you could hack, so imagine the simulation
*  that is hackable, if you could hack it, what would you change about the like, how would you approach
*  hacking a simulation? The reason I gave that talk, I've by the way, I'm not familiar with the talk
*  you gave, I just read that you talked about escaping the simulation or something like that.
*  So maybe you can tell me a little bit about the theme and the message there, too.
*  It wasn't a very practical talk about how to actually escape a simulation. It was more about
*  a way of restructuring an us versus them narrative. If we continue on the path we're going with
*  technology, I think we're in big trouble, like, as a species, and not just as a species, but even as
*  me as an individual member of the species. So if we could change rhetoric to be more like,
*  to think upwards, like to think about that we're in a simulation and how we could get out,
*  already we'd be on the right path. What you actually do once you do that, well, I assume I
*  would have acquired way more intelligence in the process of doing that. So I'll just ask that.
*  So the thinking upwards, what kind of ideas, what kind of breakthrough ideas do you think
*  thinking in that way could inspire? And why did you say upwards? Upwards? Into space? Are
*  you thinking sort of exploration in all forms? The space narrative that held for the modernist
*  generation doesn't hold as well for the postmodern generation. What's the space narrative? Are we
*  talking about the same space? The three dimensional space? No, no, space, like going up space,
*  like building like Elon Musk, like we're going to build rockets, we're going to go to Mars,
*  we're going to colonize the universe. And the narrative you're referring, I was born in the
*  Soviet Union, you're referring to the race to space. The race to space, yes. Explore, okay.
*  That was a great modernist narrative. It doesn't seem to hold the same weight in today's culture.
*  I'm hoping for good postmodern narratives that replace it. So think, let's think, so you work
*  a lot with AI. So AI is one formulation of that narrative. There could be also, I don't know how
*  much you do in VR and AR. Yeah. That's another, I know less about it, but every time I play with
*  it in our research, it's fascinating, that virtual world. Are you interested in the virtual world?
*  I would like to move to virtual reality. In terms of your work? No, I would like to physically move
*  there. The apartment I can rent in the cloud is way better than the apartment I can rent in the
*  real world. Well, it's all relative, isn't it? Because others will have very nice apartments
*  too, so you'll be inferior in the virtual world as well. No, but that's not how I view the world.
*  It's a very almost zero-sum-ish way to view the world. Say my great apartment isn't great
*  because my neighbor has one too. No, my great apartment is great because look at this dishwasher,
*  man. You just touch the dish and it's washed. And that is great in and of itself if I have
*  the only apartment or if everybody had the apartment. I don't care. So you have fundamental
*  gratitude. The world first learned of George Hottes in August 2007, maybe before then, but
*  certainly in August 2007 when you were the first person to unlock, carry unlock an iPhone. How did
*  you get into hacking? What was the first system you discovered vulnerabilities for and broke into?
*  So that was really kind of the first thing. I had a book in 2006 called Greyhat Hacking,
*  and I guess I realized that if you acquired these sort of powers, you could control the world.
*  But I didn't really know that much about computers back then. I started with electronics.
*  The first iPhone hack was physical. You had to open it up and pull an address line high.
*  It was because I didn't really know about software exploitation. I learned that all in the next few
*  years and I got very good at it. But back then, I knew about how memory chips are connected to
*  processors and stuff. You knew about software and programming. You just didn't know. Oh really? So
*  your view of the world and computers was physical, was hardware. Actually, if you read the code that
*  I released with that in August 2007, it's atrocious. What language was it? C. Nice.
*  And in a broken sort of state machine-esque C. I didn't know how to program. So how did you
*  learn to program? What was your journey? Because I mean, we'll talk about it. You've live streamed
*  some of your programming. This chaotic, beautiful mess. How did you arrive at that? Years and years
*  of practice. I interned at Google the summer after the iPhone unlock. I did a contract for them
*  where I built hardware for Street View and I wrote a software library to interact with it.
*  It was terrible code. For the first time, I got feedback from people who I respected saying,
*  don't write code like this. Now, of course, just getting that feedback is not enough.
*  The way that I really got good was I wanted to write this thing that could emulate and then
*  visualize arm binaries because I wanted to hack the iPhone better. And I didn't like that. I
*  couldn't see what the... I couldn't single step through the processor because I had no debugger
*  on there, especially for the low level things like the boot run and the bootloader. So I tried to
*  build this tool to do it. And I built the tool once and it was terrible. I built the tool second
*  times. It was terrible. I built the tool third time. By the time I was at Facebook, it was kind
*  of okay. And then I built the tool fourth time when I was a Google intern again in 2014. And
*  that was the first time I was like, this is finally usable. How do you pronounce this? Kira? Kira,
*  yeah. So it's essentially the most efficient way to visualize the change of state of the computer
*  as the program is running. That's what you mean by debugger. Yeah, it's a timeless debugger. So you
*  can rewind just as easily as going forward. Think about if you're using GDB, you have to put a watch
*  on a variable if you want to see if that variable changes. In Kira, you can just click on that
*  variable and then it shows every single time when that variable was changed or accessed.
*  Think about it like Git for your computer's run log. So there's like a deep log of the state of the
*  computer as the program runs and you can rewind. Why isn't that? Maybe it is. Maybe you can educate
*  me. Why isn't that kind of debugging used more often? Because the tooling is bad. Well, two things.
*  One, if you're trying to debug Chrome, Chrome is a 200 megabyte binary that runs slowly on desktops.
*  So that's going to be really hard to use for that. But it's really good to use for like CTFs and for
*  boot ROMs and for small parts of code. So it's hard if you're trying to debug like massive systems.
*  What's the CTF and what's the boot ROM? Boot ROM is the first code that executes the minute you
*  give power to your iPhone. And CTF were these competitions that I played capture the flag.
*  Capture the flag. I was going to ask you about that. What are those? Look, I watched a couple
*  videos on YouTube. Those look fascinating. What have you learned about maybe at the high level
*  vulnerability of systems from these competitions? I feel like in the heyday of CTFs, you had
*  all of the best security people in the world challenging each other and coming up with new
*  toy exploitable things over here. And then everybody, okay, who can break it? And when
*  you break it, there's like a file on the server called flag. And then there's a program running,
*  listening on a socket that's vulnerable. So you write an exploit, you get a shell,
*  and then you cat flag. And then you type the flag into like a web-based scoreboard and you get points.
*  So the goal is essentially to find an exploit in the system that allows you to run shell,
*  to run arbitrary code on that system. That's one of the categories. That's like the PONable category.
*  PONable? Yeah, PONable. It's like, you know, you PON the program. It's a program.
*  Yeah. You know, first of all, I apologize. I'm going to say it's because I'm Russian, but
*  maybe you can help educate me. Some video game like Misspelled own way back in the day.
*  Yeah. And it's just, I wonder if there's a definition. I'll have to go to urban dictionary
*  for it. It'll be interesting to see what it says. Okay. So what was the heyday of CTL, by the way?
*  What decade are we talking about? I think like, I mean, maybe I'm biased because it's the era
*  that I played, but like 2011 to 2015, because the modern CTF scene is similar to the modern
*  competitive programming scene. You have people who like do drills. You have people who practice.
*  And then once you've done that, you've turned it less into a game of generic computer skill and
*  more into a game of, okay, you drill on these five categories. And then before that, it wasn't,
*  it didn't have like as much attention as it had. I don't know. They were like, I won $30,000
*  once in Korea for one of these competitions. Holy crap. Yeah, they were, they were. So that means,
*  I mean, money is money, but that means there was, there was probably good people there. Exactly.
*  Yeah. Are the challenges human constructed or are they grounded in some real flaws and real systems?
*  Usually they're human constructed, but they're usually inspired by real flaws.
*  What kind of systems are imagined is really focused on mobile. Like what has vulnerabilities
*  these days? Is it primarily mobile systems like Android? Oh, everything does. Yeah, of course.
*  The price has kind of gone up because less and less people can find them. And what's happened
*  in security is now if you want to like jailbreak an iPhone, you don't need one exploit anymore.
*  You need nine. Nine chained together. What would it mean? Yeah. Wow. Okay. So it's really,
*  so what's the, what's the benefit that's speaking higher level philosophically about hacking?
*  I mean, it sounds from everything I've seen about you, you just love the challenge
*  and you don't want to do anything. You don't want to bring that exploit out into the world and do
*  any actual, let it run wild. You just want to solve it and then you go on to the next thing.
*  Oh yeah. I mean, doing criminal stuff is not really worth it. And I'll actually use the same
*  argument for why I don't do defense for why I don't do crime. If you want to defend a system,
*  say the system has 10 holes, right? If you find nine of those holes as a defender, you still lose
*  because the attacker gets in through the last one. If you're an attacker, you only have to find one
*  out of the 10. But if you're a criminal, if you log on with a VPN nine out of the 10 times,
*  but one time you forget, you're done. Because you're caught. Okay. Because you only have to
*  mess up once to be caught as a criminal. That's why I'm not a criminal.
*  But okay, let me, cause I was having a discussion with somebody just at a high level about nuclear
*  weapons, actually why we're having blown ourselves up yet. And my feeling is all the smart people in
*  the world, if you look at the distribution of smart people, smart people are generally good.
*  And then this other person, I was talking to Sean Carroll, the physicist, and he was saying, no,
*  good and bad people are evenly distributed amongst everybody. My sense was good hackers
*  are in general good people and they don't want to mess with the world. What's your sense?
*  I'm not even sure about that. Like
*  I have a nice life. Crime wouldn't get me anything.
*  But if you're good and you have these skills, you probably have a nice life too.
*  Right. Like you can use the father things, but is there an ethical, is there some,
*  is there a little voice in your head that says, well, yeah, if you could hack something
*  to where you could hurt people and you could earn a lot of money doing it though, not hurt
*  physically perhaps, but disrupt their life in some kind of way. It, isn't there a little voice that
*  says, um, well, two things. One, I don't really care about money. So like the money wouldn't be
*  an incentive. The thrill might be an incentive, but when I was 19, I read crime and punishment.
*  Right. And that was another, that was another great one that talked me out of ever really doing crime.
*  Cause it's like, that's going to be me. I'd get away with it, but it would just run to my head.
*  Even if I got away with it, you know, and then you do crime for long enough,
*  you'll never get away with it. That's right. In the end, that's a good reason to be good.
*  I wouldn't say I'm good. I would just say I'm not bad. You're a talented programmer and a hacker in
*  a good positive sense of the word word. You've played around, found vulnerabilities in various
*  systems. What have you learned broadly about the design of systems and so on from that,
*  from that whole process? You learn to not take things for what people say they are,
*  but you look at things for what they actually are. Yeah. I understand that's what you tell me it is,
*  but what does it do? Right. And you have nice visualization tools to really know what it's
*  really doing. Oh, I wish I'm a better programmer now than I was in 2014. I said, Kira, that was
*  the first tool that I wrote that was usable. I wouldn't say the code was great. I still wouldn't
*  say my code is great. So how was your evolution as a programmer, except practice, you want,
*  you started with C, at which point did you pick up Python? Cause you're pretty big in Python now.
*  Now, yeah. In college, I went to Carnegie Mellon when I was 22. I went back. I'm like,
*  I'm going to take all your hardest CS courses and we'll see how I do. Right. Like did I miss
*  anything by not having a real undergraduate education? Took operating systems, compilers,
*  AI, and they're like a freshman Weider math course. And some of those classes you mentioned
*  tough, actually. They're great. At least one of the 2012, circa 2012 operating systems and
*  compilers were two of the, they were the best classes I've ever taken in my life.
*  Cause you write an operating system and you write a compiler. I wrote my operating system in C and
*  I wrote my compiler in Haskell, but somehow I picked up Python that semester as well. I started
*  using it for the CTFs actually. That's when I really started to get into CTFs and CTFs, you're
*  all to race against the clock. So I can't write things and see, Oh, there's a clock component.
*  So you really want to use the programming language. Just so you can be fastest in 48 hours,
*  Pwn as many of these challenges as you can. Pwn. Yeah. You got like a hundred points of challenge,
*  whatever team gets the most. You were both at Facebook and Google for a brief stint with a
*  project zero actually at Google for five months where you develop Kara. What was project zero
*  about in general? Just curious about the security efforts in these companies.
*  Well, product zero started the same time I went there. What, what, what years are you there?
*  2015. 2015. So that was right at the beginning of project. It's small. It's Google's offensive
*  security team. I'll try to give, I'll try to give the best public facing explanation that I can. So
*  the idea is basically these vulnerabilities exist in the world. Nation states have them.
*  Some high powered bad actors have them. Sometimes people will find these vulnerabilities and submit
*  them in bug bounties to the companies. But a lot of the companies don't really care. They don't
*  even fix the bug. There's no, it doesn't hurt for there to be a vulnerability. So project zero is
*  like, we're going to do it different. We're going to announce a vulnerability and we're going to
*  give them 90 days to fix it. And then whether they fix it or not, we're going to drop the drop the
*  zero deck. Oh, wow. We're going to drop the weapon. That's so cool. That is so cool. I love that
*  deadlines. Oh, that's so cool. Give them real deadlines. Yeah. And I think it's done a lot for
*  moving the industry forward. I watched your coding sessions on the streamed online. You code things
*  up the basic projects, usually from scratch. I would say sort of as a programmer myself,
*  just watching you that you type really fast and your brain works in both brilliant and chaotic
*  ways. I don't know if that's always true, but certainly for the live streams. So it's, it's
*  interesting to me because I'm more, I'm much slower and systematic and careful and you just move. I
*  mean, probably in order of magnitude faster. So I'm curious, is there a method to your madness?
*  Is it just who you are? There's pros and cons. There's pros and cons to my programming style
*  and I'm aware of them. Like if you ask me to like, like get something up and working quickly with
*  like an API, that's kind of undocumented. I will do this super fast because I will throw things
*  at it until it works. If you ask me to take a vector and rotate it 90 degrees and then flip
*  it over the XY plane, I'll spam program for two hours and won't get it. Oh, because it's something
*  that you could just do with a sheet of paper, think through design and then just, do you really
*  just throw stuff at the wall and you get so good at it that it usually works? I should become better
*  at the other kind as well. Sometimes I'll do things methodically. It's nowhere near as
*  entertaining on the Twitch streams. I do exaggerate it a bit on the Twitch streams as well. The Twitch
*  streams, I mean, what do you want to see a game or you want to see actions per minute, right?
*  I'll show you APM for programming too. Yeah. I recommend people go to it. I think I watched,
*  I watched probably several hours of you, like I've actually left you programming in the background
*  while I was programming because you made me, it was like watching a really good gamer. It's like
*  energizes you because you're like moving so fast. It's so it's, it's awesome. It's inspiring. And
*  it's, it made me jealous that like, because my own programming is inadequate in terms of speed.
*  Oh, I was like, so I'm, I'm, I'm twice as frantic on the live streams as I am when I code without.
*  It's super entertaining. So I, I wasn't even paying attention to what you were coding,
*  which is great. It's just watching you switch windows and Vim, I guess.
*  Yeah. This is Vim and screen. I've developed the workflow at Facebook and to talk with it.
*  How do you learn new programming tools, ideas, techniques these days?
*  What's your like a methodology for learning new things?
*  So I wrote for comma the distributed file systems out in the world are extremely complex.
*  Like if you want to install something like, like, like Seth, Seth is I think the like open
*  infrastructure, uh, distributed file system, or there's like newer ones like seaweed FS,
*  but these are all like 10,000 plus line projects. I think some of them are even 100,000 line
*  and just configuring them as a nightmare. So I wrote, uh, I wrote one, um, it's 200 lines
*  and it's, it uses like engine X volume servers and has this little master server that I wrote and go.
*  And the way I go, this, if I would say that I'm proud per line of any code I wrote,
*  maybe there's some exploits that I think are beautiful. And then this, this is 200 lines.
*  And just the way that I thought about it, I think was very good. And the reason it's very good is
*  because that was the fourth version of it that I wrote. And I had three versions that I threw away.
*  You mentioned, did you say go? I wrote and go. Yeah. And go. So I, is that a functional
*  language? I forget what go is. Go is Google's language. Right. Um, it's not functional. It's
*  some, it's like in a way it's C plus plus, but easier. It's, it's strongly typed. It has a nice
*  ecosystem around it. When I first looked at it, I was like, this is like Python, but it takes twice
*  as long to do anything. Now that I've open pilot is migrating to see, but it still has large Python
*  components. I now understand why Python doesn't work for large code bases and why you want
*  something like go. Interesting. So why, why doesn't Python work for, so even most, uh,
*  speaking for myself, at least like we do a lot of stuff, basically demo level work with autonomous
*  vehicles and most of the work is Python. Why doesn't Python work for large code bases?
*  Because well, lack of type checking is, is, is a big error. Yeah. And like, you don't know
*  the compiler can tell you like nothing. Right. So everything is either, uh, you know,
*  like, like syntax errors. Fine. But if you misspell a variable in Python compiler,
*  we'll catch that there's like linters that can catch it. Some of the time there's no types.
*  This is really the biggest, uh, downside. And then we'll Python slow, but that's not related
*  to it. Well, maybe it's kind of related to it. So it's lack of, so what's, what's in your toolbox
*  these days? Is it Python? What else go? I need to move to something else. My adventure into
*  dependently typed languages. I love these languages. They just have like syntax from the eighties.
*  What do you think about JavaScript? The S six, like the modern type script,
*  JavaScript is the whole ecosystem is unbelievably confusing. Right. NPM updates a package from zero
*  two two to zero two five. And that breaks your babble linter, which translates your ES five into
*  yes. Six, which doesn't run on. So why do I have to compile my JavaScript again? Huh?
*  It may be the future though. You think about, I mean, uh, I've embraced JavaScript recently,
*  just because, uh, just like I've continually embraced PHP, it seems that these worst possible
*  languages live on for the longest. They cockroaches never die. Yeah. Well, it's in the browser and
*  it's fast. It's fast. Yeah. It's in the browser and compute might stay become, you know, the
*  browser it's unclear what the role of the browser is in terms of distributed computation in the future.
*  So JavaScript is definitely here to stay. Yeah. Um, it's interesting if autonomous vehicles will
*  run on JavaScript one day. I mean, you have to consider these possibilities. Well, all our debug
*  tools are JavaScript. Uh, we actually just open source them. Um, we have a tool explorer, which
*  you can annotate your disengagements and we have tool cabana, which lets you analyze the can traffic
*  from the car. So basically anytime you're visualizing something about the log, you're
*  using JavaScript. Well, the web is the best UI toolkit by far. Um, so, and then, you know what?
*  You're coding in JavaScript. We have a react guy. He's good. Reacts. Nice. Let's get into it. So
*  let's talk autonomous vehicles. Uh, you founded comma AI. Let's, uh, at a high level, uh, how did
*  you get into the world of vehicle automation? Can you also just, for people who don't know,
*  tell the story of common AI? Sure. So I was working at this AI startup and, uh, a friend approached me
*  and he's like, dude, I don't know where this is going, but the coolest applied AI problem today
*  is self-driving cars. I'm like, well, absolutely. Do you want to meet with, uh, Elon Musk? And, uh,
*  uh, he's looking for somebody to build a vision system for, uh, autopilot. This is when they were
*  still on AP one, they were still using mobile. I, Elon back then was looking for a replacement
*  and he brought me in and we talked about a contract where I would deliver something that
*  meets mobile eye level performance. Uh, I would get paid $12 million if I could deliver it tomorrow
*  and I would lose $1 million for every month I didn't deliver. Yeah. Um, so I was like, okay,
*  this is a great deal. This is a super exciting challenge. You know what? Even if it takes me 10
*  months, I get $2 million. It's good. Maybe I can finish up in five. Maybe I don't finish it at all
*  and I get paid nothing and I'll work for 12 months for free. So maybe, uh, just take a pause on that.
*  I'm also curious about this because I've been working in robotics for a long time and I'm
*  curious to see a person like you just step in and sort of, um, somewhat naive, but brilliant, right?
*  So that's the, that's the best place to be. Cause you basically full steam take on a problem. How
*  confident, how from that time, cause you know a lot more now at that time, how hard do you think
*  it is to solve all of autonomous driving? I remember I suggested to Elon in the meeting,
*  um, putting a GPU behind each camera to keep the compute local. This is an incredibly stupid idea.
*  I leave the meeting 10 minutes later and I'm like, I could have spent a little bit of time
*  thinking about this problem. Why is it a good idea? Oh, just send all your cameras to one big GPU.
*  You're much better off doing that. Oh, sorry. You said behind every camera,
*  every camera have a small GPU. I was like, Oh, I'll put the first few layers of my comms there.
*  Like, why'd I say that? That's possible. It's possible, but it's a bad idea.
*  It's not obviously a bad idea, but whether it's actually a bad idea or not. I left that meeting
*  with Elon, like beating myself up. I'm like, why did I say something stupid? Yeah. You haven't
*  like, you haven't at least like thought through every aspect fully. Yeah. He's very sharp too.
*  Like usually in life I get away with saying stupid things and then kind of course,
*  Oh, right, right away. He called me out about it. And like, usually in life I get away with
*  saying stupid things and then like people will, uh, you know, a lot of times people don't even
*  notice and I'll like correct it and bring the conversation back. But with Elon, it was like,
*  Nope. Like, okay, well, um, that's not at all why the contract fell through. I was much more
*  prepared the second time I met him. Yeah. But in general, how, how hard did you think it is like
*  12 months is a tough timeline. Oh, I just thought I'd clone Mobileye IQ3. I didn't think I'd solve
*  level five self-driving or anything. So the goal there was to do lane keeping, uh, good, good lane
*  keeping. I saw my friend showed me the outputs from a Mobileye and the outputs from a Mobileye
*  was just basically two lanes in a position of a lead car. I'm like, I can, I can gather a data
*  set and train this net in, in, in weeks. And I did. Well, first time I tried the implementation
*  of Mobileye and the test, I was really surprised how good it is. Uh, it's quite incredibly good
*  because I thought it's just cause I've done a lot of computer vision. I thought it'd be
*  a lot harder to create a system that that's stable. Uh, so I was personally surprised just,
*  you know, uh, have to admit it. Cause I was kind of skeptical before trying it. Cause I thought,
*  it would go in and out a lot more. It would get disengaged a lot more and it's pretty robust.
*  So what, how, how, how hard is the problem when you, when you tackled it?
*  So I think AP one was great. Like, uh, Elon talked about disengagement on the four or five
*  down in LA with like the lane marks are kind of faded. Um, and the Mobileye system would drop out.
*  Uh, like I had something up and working that I would say was like the same quality in three
*  months. Same quality. But how do you know? You, you, you say stuff like that confidently,
*  but you can't, and I love it, but, uh, well, the question is you can't,
*  you're kind of going by feel cause you're going to feel absolutely. Absolutely. Like, like I would
*  take, I hadn't, I borrowed my friend's Tesla. I would take AP one out for a drive and then I
*  would take my system out for a drive and seems reasonably like the same. So the four or five,
*  how hard is it to create something that could actually be a product that's deployed? I mean,
*  uh, I've, I've read an article where Elon this, uh, respondent said something about you saying that,
*  um, to build autopilot is, uh, is more complicated than a single George Hod's level job. How hard is
*  that job to create something that would work across the globally? Um, why don't think
*  globally is the challenge, but Elon followed that up by saying it's going to take two years
*  in a company of 10 people. And here I am four years later with a company of 12 people. And I
*  think we still have another two to go two years. So yeah. So what do you think, uh, what do you
*  think about, uh, how test is progressing with autopilot V2 V3? I think we've kept pace with them
*  pretty well. I think navigate and autopilot is terrible. We had some demo features internally of
*  the same stuff and we would test it. And I'm like, I'm not shipping this even as like open
*  source software to people. What do you think is terrible? Consumer reports does a great job
*  of describing it. Like when it makes a lane change, it does it worse than a human.
*  You shouldn't ship things like autopilot, open pilot. They lane keep better than a human.
*  If you turn it on for a stretch of a highway, like an hour long, it's never going to touch a
*  lane line. Human will touch probably a lane line twice. You just inspired me. I don't know
*  if you're grounded in data on that. I read your paper. Okay. But no, but that's interesting. Uh,
*  I wonder actually how often we touch lane lines, uh, in general, like a little bit. Cause it is,
*  I could, I could answer that question pretty easily with the common data side. Yeah. I'm curious.
*  I've never answered it. I don't know. I just too, is like my personal, it feels, it feels right.
*  That's interesting. Cause every time you touch a lane, that's a source of, um, a little bit of
*  stress and kind of lane keeping is removing that stress. That's all to me. The big, the biggest
*  value add honestly is just removing the stress of having to stay in lane. And I think honestly,
*  I don't think people fully realize first of all, that that's a big value add. Uh, but also that
*  that's all it is. And that not only, I find it a huge value add. I drove down when we moved to
*  San Diego, I drove down in an enterprise rent a car and I missed it. So I missed having the system
*  so much. It's so much more tiring to drive without it. It's, it is that lane centering.
*  That's the key feature. Yeah. And in a way it's the only feature that actually adds value to
*  people's lives in autonomous vehicles today. Waymo does not add value to people's lives.
*  It's a more expensive flow or slower Uber. Maybe someday it'll be this big cliff where it adds
*  value, but I don't usually, it's fascinating. I haven't talked to, cause that, uh, this is good.
*  I haven't, I have intuitively, but I think we're making it explicit now. I, I actually believe, um,
*  that really good lane keeping is a reason to buy a car will be a reason to buy a car. And it's a
*  huge value add. I've never, until we just started talking about it, I haven't really quite realized
*  it that I've felt with Elon's chase of level four is not the correct chase. It was, because you
*  should just say Tesla has the best as if from a Tesla perspective, say Tesla has the best
*  lane keeping. Comma AI should say Comma AI is the best lane keeping and that is it. Yeah. Yeah.
*  So do you think, um, you have to do the longitudinal as well. You can't just lane
*  keep. You have to do, uh, ACC, but ACC is much more forgiving than lane keep. Um,
*  especially on the highway. By the way, are you, um, Comma AI is camera only, correct?
*  Uh, no, we use the radar. Uh, we- From the car you're able to get the-
*  We can do a camera only now. It's gotten to the point, but we leave the radar there as like a,
*  it's, it's, it's fusion now. Okay. So let's maybe talk through some of the system specs on the
*  hardware. What, what's, what's the hardware side of, uh, what you're providing? What's the
*  capabilities on the software side with open pilot and so on? So open pilot as the, the, the box that
*  we sell that it runs on, it's a phone in a plastic case. Um, it's nothing special. We sell it without
*  the software. So you're like, you know, you buy the phone as it's just easy. It'll be easy set up,
*  but it's sold with no software. Open pilot right now is about to be 0.6. When it gets to 1.0,
*  I think we'll be ready for a consumer product. We're not going to add any new features. We're
*  just going to make the lane keeping really, really good. So what do we have right now?
*  It's a, uh, Snapdragon 820. It's a Sony IMX 298 forward facing camera, um, driver monitoring
*  camera. She's a selfie cam on the phone and, uh, uh, can transceiver. Maybe it was a little thing
*  called pandas and they talk over USB to the phone. And then they have three can buses that they talk
*  to the car. Uh, one of those can buses is the radar canvas. One of them is the main car canvas.
*  And the other one is the proxy camera canvas. We leave the existing camera in place so we don't turn
*  AEB off. Uh, right now we still turn AEB off if you're using our longitudinal, but we're going to
*  fix that before 1.0. Got it. Wow. That's cool. So and it's canned both ways. So
*  how are you able to control vehicles? So we proxy the vehicles that we work with already have a
*  lane keeping assist system. So lane keeping assist can mean a huge variety of things.
*  It can mean it will apply a small torque to the wheel after you've already crossed a lane line
*  by a foot, which is the system in the older Toyota's versus like, I think Tesla still calls
*  it lane keeping assist where it'll keep you perfectly in the center of the lane on the highway.
*  You can control like you with a joystick, the car, these, so these cars already have the capability
*  of drive by wire. So, uh, is it, is it trivial to convert a car that it operates with, uh, it, uh,
*  open pilot is able to control the steering? Oh, a new car or a car that we, so we have support now
*  for 45 different makes of cars. What are, what are the cars in general? Uh, mostly Honda's and
*  Toyota's. We support almost every Honda and Toyota made, uh, this year. And then a bunch of GMs,
*  bunch of Subarus, but it doesn't have to be like a Prius. It could be Corolla as well. Oh,
*  the 2020 Corolla is the best car with open pilot. It just came out there. The actuator has less lag
*  than the older Corolla. I think I started watching a video with your, I mean,
*  the way you make videos is awesome. Literally at the dealership streaming.
*  My friend, the phone, I'm like, I'm gonna stream for an hour. Yeah. And basically like if stuff
*  goes a little wrong, you're just like, you just go with it. Yeah. I love it. It's real. Yeah. It's
*  real. That's, that's, it's, that's so beautiful. And it's so in contrast to the way other companies
*  would put together a video like that. Kind of why I like to do it like that. Good. I mean, uh,
*  if you become super rich one day and successful, I hope you keep it that way because I think that's
*  actually what people love that kind of genuine. Oh, it's all that has value to me. Yeah. Money has
*  no, if I sell out to like make money, I sold out. It doesn't matter. What do I get? Yacht? I don't
*  want to go out. And I think, uh, Tesla's actually has a small inkling of that as well with
*  autonomy day. They did reveal more than, I mean, of course there's marketing communications. You
*  could tell, but it's more than most companies would reveal, which is, uh, I hope they go
*  towards that direction more other companies, GM Ford, Tesla is going to win level five. They really
*  are. So let's talk about it. You think, uh, you're focused on level two. Uh, currently,
*  currently we're going to be one to two years behind Tesla getting to level five. Okay.
*  We're Android, right? We're Android. You're Android. I'm just saying once Tesla gets it,
*  we're one to two years behind. I'm not making any timeline on when Tesla's that's right. You did.
*  That's brilliant. I'm sorry, Tesla investors. If you think you're going to have an autonomous
*  robotaxi fleet by the end of the year, I'll bet against that. So what do you think about this?
*  The most level four companies are kind of just doing their usual, uh, safety driver,
*  doing full autonomy kind of testing. And then Tesla does basically trying to go from lane keeping
*  to full autonomy. What do you think about that approach? How successful would it be?
*  It's a ton better approach because Tesla is gathering data on a scale that none of them are.
*  They're putting real users behind the, uh, behind the wheel of the cars.
*  It's, I think the only strategy that works the incremental. Well, so there's a few components
*  to test approach. That's, that's more than just the incremental. What you spoke with is the one is
*  the software. So over the air, air software updates necessity. I mean, Waymo had crews have
*  those two. Those aren't, but those differentiate things from the automakers, right? No lane keeping
*  assist systems have no cars with lane keeping system have that except Tesla. And, uh, the other
*  one is the data, the other direction, which is the ability to query the data. I don't think they're
*  actually collecting as much data as people think, but the ability to turn on collection and turn it
*  off. So I'm both in the robotics world and the, the psychology human factors world. Many people
*  believe that level two autonomy is problematic because of the human factor. Like the more
*  the task is automated, the more there's a vigilance decrement. You start to fall asleep.
*  You start to become complacent, start texting more and so on. Do you worry about that?
*  Cause if we're talking about transition from lane keeping to full autonomy, if you're spending 80%
*  of the time not supervising the machine, do you worry about what that means?
*  To the safety of the drivers? One, we don't consider open pilot to be 1.0 until we have
*  100% driver monitoring. You, you can cheat right now our driver monitoring system. There's a few
*  ways to cheat it. They're pretty obvious. Um, we're working on making that better before we ship a
*  consumer product that can drive cars. I want to make sure that I have driver monitoring that you
*  can't cheat. What's like a successful driving monitoring system look like it's keep it's,
*  is it all about just keeping your eyes on the road? Um, well, a few things. So that's what we
*  went with at first for driver monitoring. I'm checking. I'm actually looking at where your
*  head is looking. The camera's not that high resolution. Eyes are a little bit hard to get.
*  Well, head is this big. I mean, that's, that is good. And actually a lot of it just psychology
*  wise to have that monitor constantly there. It reminds you that you have to be paying attention,
*  but we want to go further. We just hired someone full time to come on to do the driver monitoring.
*  I want to detect phone in frame and I want to make sure you're not sleeping.
*  How much does the camera see of the body? This one, not enough. Not enough. The next one,
*  everything. Well, it's interesting. Uh, fish eye, cause we have, uh, we're doing just data collection,
*  not real time, but fish eyes, a beautiful, uh, being able to capture the body and the smartphone
*  is really like the biggest problem. I'll show you, I can show you one of the pictures from,
*  from our, our new system. Awesome. So you're basically saying the driver monitoring will be
*  the answer to that. Um, I think the other point that you raised in your paper is, is good as well.
*  You're not asking a human to, uh, supervise a machine, uh, without giving them the, they can
*  take over at any time. Right. Our safety model, you can take over. We, we disengage on both the
*  gas or the brake. Uh, we don't disengage on steering. I don't feel you have to, but, uh,
*  we disengage on gas or brake. So it's very easy for you to take over and it's very easy for you
*  to reengage. That switching should be super cheap. The cars that require, even autopilot requires a
*  double press. That's almost, I see. I don't like that. And then, then the cancel, um, to cancel in
*  autopilot, you either have to press cancel, which no one knows what that is. So they press the brake,
*  but a lot of times you don't actually want to press the brake. You want to press the gas. So
*  you should cancel on gas or wiggle the steering wheel, which is bad as well. Wow. That's brilliant.
*  I haven't heard anyone articulate that point, but it's all I think about. It's the, because I think,
*  I think actually Tesla has done a better job than most automakers at making that frictionless,
*  but you just described that it could be even better. I love super cruise as an experience
*  once it's engaged. Yeah. I don't know if you've used it, but getting the thing to try to engage
*  Yeah. I've used the super of a driven supercruise a lot. So what's your thoughts on the super good
*  system? You disengage super cruise and it falls back to ACC. So my car's like still accelerating.
*  It feels weird. Otherwise, when you actually have super cruise engaged on the highway,
*  it is phenomenal. We bought that Cadillac, we just sold it, but we bought it just to like experience
*  this. And I wanted everyone in the office to be like, this is what we're striving to build a GM
*  pioneering with the driver monitoring. You, you like their driving monitoring system?
*  It has some bugs. If there's a sun shining back here, it'll be blind to you.
*  But overall, mostly. Yeah. That's so cool that you know all this stuff. That's, I don't
*  often talk to people that because it's such a rare car, unfortunately, currently,
*  they bought one explicitly for us. We lost like, like 25 K in the deprecation, but I feel it's worth
*  it. I was very pleasantly surprised that GM system was so innovative and really wasn't
*  advertised much, wasn't talked about much. Yeah. And I was nervous that it would die,
*  that it would disappear. Well, I did. They put it on the wrong car. They should have put it on the
*  bolt and not some weird Cadillac that nobody bought. I think that's going to be into their
*  saying at least is going to be into their entire fleet. So what do you think about as long as we're
*  on the driver monitoring? What do you think about Elon Musk's claim that driving monitoring
*  is not needed? Normally I love his claims. That one is stupid. That one is stupid. And you know,
*  he's not going to have his level five fleet by the end of the year. Hopefully he's like,
*  okay, I was wrong. I'm going to add driver monitoring because when these systems get
*  to the point that they're only messing up once every thousand miles, you absolutely need driver
*  monitoring. So let me play because I agree with you, but let me play devil's advocate.
*  One possibility is that without driver monitoring, people are able to monitor
*  self-regulate monitor themselves. You know that your ideas, you've seen all the people sleeping
*  in in Tesla's. Yeah. Well, I'm a little skeptical of all the people sleeping in Tesla's because
*  I've stopped paying attention to that kind of stuff because I want to see real data.
*  There's too much glorified. It doesn't feel scientific to me. So I want to know,
*  you know, how many people are really sleeping in Tesla's versus sleeping. I was driving here,
*  sleep deprived in a car with no automation. I was falling asleep. I agree that it's hypey. It's
*  just like, you know what, if you want to put driver monitoring, I rented my last autopilot
*  experience was I rented a model three in March and drove it around. The wheel thing is annoying.
*  And the reason the wheel thing is annoying, we use the wheel thing as well, but we don't disengage
*  on wheel for Tesla. You have to touch the wheel just enough to trigger the torque sensor to tell
*  it that you're there, but not enough as to disengage it, which don't use it for two things.
*  Don't disengage on wheel. You don't have to that whole experience. Wow. Beautiful. But they,
*  all those elements, even if you don't have driver monitoring, that whole experience needs to be
*  better. Driver monitoring, I think would make, I mean, I think super cruise is a better experience
*  once it's engaged over autopilot. I think super cruises are transition to engagement and
*  disengagement are significantly worse. Yeah. There's a tricky thing because if I were to
*  criticize super cruise is it's a little too crude. And I think like six seconds or something, if you
*  look off road, it'll start warning you. It's some ridiculously long period of time. And just the way
*  I think it's basically, it's a binary. It should be adapted. Yeah. It needs to learn more about you.
*  It needs to communicate what it sees about you more. I'm not, you know, Tesla shows what it sees
*  about the external world. It would be nice if super cruise would tell us what it sees about the
*  internal world. It's even worse than that. You press the button to engage and it just says
*  super cruise unavailable. Yeah. Why? Why? Yeah. That transparency is good. We've renamed the
*  driver monitoring packet to driver state. Driver state. We have car state packet, which has the
*  state of the car and driver state packet, which has state of the driver. So what does it make their
*  BAC? What's BAC? Blood alcohol kind of. Do you think that's possible with computer vision? Absolutely.
*  To me, it's an open question. I haven't looked into it too much. Actually, I quite seriously
*  looked at the literature. It's not obvious to me that from the eyes and so on, you can tell.
*  You might need stuff from the car as well. Yeah. You might need how they're controlling the car,
*  right? And that's fundamentally at the end of the day, what you care about. But I think especially
*  when people are really drunk, they're not controlling the car nearly as smoothly as they
*  would look at them walking, right? The car is like an extension of the body. So I think you could
*  totally detect. And if you could fix people who are drunk, distracted, asleep, if you fix those three.
*  Yeah, that's huge. So what are the current limitations of OpenPilot? What are the main
*  problems that still need to be solved? We're hopefully fixing a few of them in 06. We're not
*  as good as Autopilot at stop cars. So if you're coming up to a red light at like 55,
*  so it's the radar stopped car problem, which is responsible to autopilot accidents,
*  it's hard to differentiate a stopped car from a sign post.
*  Yeah, static object. So you have to fuse. You have to do this visually. There's no way from
*  the radar data to tell the difference. Maybe you can make a map, but I don't really believe in
*  mapping at all anymore. Wait, wait, wait, what? You don't believe in mapping? No. So you basically,
*  the OpenPilot solution is saying react to the environment as you see it, just like human doing
*  beings do. And then eventually when you want to do navigate on OpenPilot, I'll train the net to
*  look at ways. I'll run ways in the background. I'll train a competent way. Are you using GPS at all?
*  We use it to ground truth. We use it to very carefully ground truth the paths.
*  We have a stack which can recover relative to 10 centimeters over one minute. And then we use that
*  to ground truth exactly where the car went in that local part of the environment, but it's all local.
*  How are you testing in general? Just for yourself, like experiments and stuff?
*  Where are you? Where are you located? San Diego, San Diego. Yeah. Okay. What? So you basically drive
*  around there and collect some data and watch performance. We have a simulator now and we have
*  our simulator is really cool. Our simulator is not, it's not like a unity-based simulator.
*  Our simulator lets us load in real estate. What do you mean? We can load in a drive and simulate
*  what the system would have done on the historical data. Ooh, nice. Interesting. So what? Yeah.
*  Right now we're only using it for testing, but as soon as we start using it for training,
*  that's it. That's all for testing. What's your feeling about the real world versus simulation?
*  Do you like simulation for training? If this moves to training? So we have to distinguish
*  two types of simulators, right? There's a simulator that like is completely fake. I could get my car
*  to drive around in GTA. I feel that this kind of simulator is useless. You're never, there's so
*  many. My analogy here is like, okay, fine. You're not solving the computer vision problem, but you're
*  solving the computer graphics problem. Right. And you don't think you can get very far by creating
*  ultra realistic graphics? No, because you can create ultra realistic graphics of the road.
*  Now create ultra realistic behavioral models of the other cars. Oh, well, I'll just use myself
*  driving. No, you won't. You need real, you need actual human behavior because that's what you're
*  trying to learn. The driving does not have a spec. The definition of driving is what humans do when
*  they drive. Whatever Waymo does, I don't think it's driving. Right. Well, I think actually Waymo
*  and others, if there's any use for reinforcement learning, I've seen it used quite well. I study
*  pedestrians a lot too, is try to train models from real data of how pedestrians move and try to use
*  reinforcement learning models to make pedestrians move in human-like ways. By that point, you've
*  already gone so many layers. You detected a pedestrian. Did you hand code the feature
*  vector of their state? Did you guys learn anything from computer vision before deep learning?
*  Well, okay. I feel like this is- So perception to you is the sticking point. What's the hardest
*  part of the stack here? There is no human understandable feature vector separating perception
*  and planning. That's the best way I can put that. There is no, so it's all together and it's a joint
*  problem. You can take localization. Localization and planning, there is a human understandable
*  feature vector between these two things. I mean, okay, so I have like three degrees position,
*  three degrees orientation and those derivatives, maybe those second derivatives. That's human
*  understandable. That's physical. Between perception and planning, Waymo has a perception stack and
*  then a planner. One of the things Waymo does right is they have a simulator that can separate those
*  two. They can replay their perception data and test their system, which is what I'm talking about
*  about the two different kinds of simulators. There's the kind that can work on real data and
*  there's the kind that can't work on real data. Now, the problem is that I don't think you can
*  hand code a feature vector. You have some list of like, oh, here's my list of cars in the scenes.
*  Here's my list of pedestrians in the scene. This isn't what humans are doing.
*  What are humans doing? Global.
*  You're saying that's too difficult to hand engineer.
*  I'm saying that there is no state vector. Given a perfect, I could give you the best team of
*  engineers in the world to build a perception system and the best team to build a planner.
*  All you have to do is define the state vector that separates those two.
*  I'm missing the state vector that separates those two. What do you mean?
*  So what is the output of your perception system?
*  Output of the perception system. It's, okay, well, there's several ways to do it. One is
*  the slam component is localization. The other is drivable area, drivable space.
*  And then there's the different objects in the scene. And different objects in the scene over
*  time, maybe to give you input to then try to start modeling the trajectories of those objects.
*  Sure. That's it.
*  I can give you a concrete example of something you missed.
*  So say there's a bush in the scene. Humans understand that when they see this bush,
*  that there may or may not be a car behind that bush. Drivable area and a list of objects does
*  not include that. Humans are doing this constantly at the simplest intersections.
*  So now you have to talk about occluded area.
*  But even that, what do you mean by occluded? Okay, so I can't see it. Well, if it's the other side
*  of a house, I don't care. What's the likelihood that there's a car in that occluded area? And
*  if you say, okay, we'll add that, I can come up with 10 more examples that you can't add.
*  Certainly occluded area would be something that a simulator would have because it's simulating
*  the entire, you know, the occlusion is part of it. Occlusion is part of a vision stack.
*  But what I'm saying is if you have a hand engineered, if your perception system output
*  can be written in a spec document, it is incomplete. Yeah, I mean, it's certainly, it's
*  a, it's hard to argue with that because in the end that's going to be true.
*  Yeah. And I'll tell you what the output of our perception system is. It's a
*  1024 dimensional vector. Oh, you're on that. No, no, it's the 1024 dimensions of who knows what.
*  Because it's operating on real data. Yeah. Yeah.
*  And that's the perception. That's the perception state, right? Think about an autoencoder for
*  faces, right? If you have an autoencoder for faces and you say it has 256 dimensions in the middle,
*  and I'm taking a face over here and projecting it to a face over here. Yeah. Can you hand label all
*  256 of those dimensions? Well, no, but those are generated automatically. But even if you tried to
*  do it by hand, could you come up with a spec for your, between your encoder and your decoder?
*  No, because that's how it is. It wasn't designed, but there-
*  No, no, no, but if you could design it, if you could design a face reconstructor system,
*  could you come up with a spec? No, but I think we're missing here a little bit. I think that
*  you're just being very poetic about expressing a fundamental problem of simulators,
*  that they're going to be missing so much that the feature vector will just look fundamentally
*  different from in the simulated world than the real world. I'm not making a claim about simulators.
*  I'm making a claim about the spec division between perception and planning, even in your system.
*  Just in general. Right? Just in general. If you're trying to build a car that drives,
*  if you're trying to hand code the output of your perception system, like saying, like,
*  here's a list of all the cars in the scene. Here's a list of all the people. Here's a list of the
*  occluded areas. Here's a vector of drivable areas. It's insufficient. And if you start to believe that,
*  you realize that what Waymo and Cruz are doing is impossible. Currently, what we're doing is the
*  perception problem is converting the scene into a chessboard. And then you reason some basic
*  reasoning around that chessboard. And you're saying that really there's a lot missing there.
*  First of all, why are we talking about this? Because isn't this a full autonomy? Is this
*  something you think about? Oh, I want to win self-driving cars. So you're really,
*  you see your definition of win includes level five. I don't think level four is a real thing.
*  I want to build, I want to build the AlphaGo of driving. So, so AlphaGo is really end to end.
*  End to end. Yeah. Is, yeah, it's end to end. And do you think this whole problem is also,
*  is that also kind of what you're getting at with the perception and the planning?
*  Is that this whole problem, the right way to do it is really to learn the entire thing.
*  I'll argue that not only is it the right way, it's the only way that's going to exceed human
*  performance. Well, certainly true for Go. Everyone who tried to hand code Go things built human
*  inferior things. And then someone came along and wrote some 10,000 line thing that doesn't know
*  anything about Go that beat everybody. It's 10,000 lines. True. In that sense, the open question then
*  that maybe I can ask you is driving is much harder than Go. The open question is how much harder.
*  So how, because I think the Elon Musk approach here with planning and perception
*  is similar to what you're describing, which is really turning into
*  not some kind of modular thing, but really do formulate as a learning problem and solve
*  the learning problem with scale. So how many years, I put one is how many years would it
*  take to solve this problem or just how hard is this freaking problem? Well, the cool thing is
*  I think there's a lot of value that we can deliver along the way. I think that you can build
*  lane keeping assist actually plus adaptive cruise control plus, okay, looking at ways extends to
*  like all of driving. Yeah, most of driving. Right. Oh, your adaptive cruise control treats red lights
*  like cars. Okay. So let's jump around. You mentioned that you didn't like navigate an autopilot.
*  Yeah. What advice, how would you make it better? Do you think as a feature that if it's done really
*  well, it's a good feature? I think that it's too reliant on like hand coded hacks for like, how
*  does navigate an autopilot do a lane change? It actually does the same lane change every time.
*  And it feels mechanical. Humans do different lane changes. Humans sometimes will do a slow one,
*  sometimes do a fast one navigate an autopilot. At least every time I use it, it is the identical
*  lane change. How do you learn? I mean, this is a fundamental thing actually is the braking and
*  then accelerating something that's still Tesla probably does it better than most cars, but it
*  still doesn't do a great job of creating a comfortable natural experience and navigate
*  an autopilot is just lane changes and extension of that. So how do you learn to do a natural lane
*  change? So we have it and I can talk about how it works. So I feel that we have the solution for
*  lateral, but we don't yet have the solution for longitudinal. There's a few reasons longitudinal
*  is harder than lateral. The lane change component, the way that we train on it very simply is like
*  our model has an input for whether it's doing a lane change or not. And then when we train the
*  end to end model, we hand label all the lane changes because you have to. I've struggled a
*  long time about not wanting to do that, but I think you have to. Or the training data.
*  For the training data. We actually have an automatic ground truth or which automatically
*  labels all the lane changes. Is that possible? To automatically label the lane changes? Yeah.
*  Yeah, just check the lane. I see when it crosses it. And I don't have to get that high percent
*  accuracy, but it's like 95 good enough. Okay. Now I set the bit when it's doing the lane change in
*  the end to end learning. And then I set it to zero when it's not doing a lane change. So now if I
*  want it to do a lane change at test time, I just put the bit to a one and it'll do a lane change.
*  Yeah. But so if you look at the space of lane change, you know, some percentage, not a hundred
*  percent that we make as humans is not a pleasant experience because we mess some part of it up.
*  It's nerve wracking to change the look, you have to see, does it accelerate? How do we label the
*  ones that are natural and feel good? You know, that's the cause that's your ultimate criticism.
*  The current navigate and autopilot just doesn't feel good. Well, the current navigate and autopilot
*  is a hand coded policy written by an engineer in a room who probably went out and tested it a few
*  times on the two 80. Probably a more, a better version of that. But yes, that's how we would
*  have written it to come. Yeah. Maybe Tesla, Tesla, they tested it in there.
*  Might've been two engineers. Yeah. No, but so if you learn the lane change,
*  if you learn how to do a lane change from data, just like, just like you have a label that says
*  lane change and then you put it in when you want it to do the lane change, it'll automatically do
*  the lane change. That's appropriate for the situation. Now to get at the problem of some
*  humans do bad lane changes. We haven't worked too much on this problem yet. It's not that much of
*  a problem in practice. My theory is that all good drivers are good in the same way and all bad
*  drivers are bad in different ways. And we've, we've seen some data to back this up.
*  Well, beautifully put. So you just basically, if that's true, hypothesis, then your task is to
*  discover the good drivers. The good drivers stand out because they're in one cluster and the bad
*  drivers are scattered all over the place and your net learns the cluster. Yeah. That's a,
*  so you just learn from the good drivers and they're easy to cluster. In fact, we learned from all of
*  them and the net automatically learns the policy. That's like the majority, but we'll eventually
*  probably have to filter. So if that theory is true, I hope it's true because the, the counter
*  theory is there is many clusters, maybe arbitrarily many clusters of good drivers
*  because if there's one cluster of good drivers, you can at least discover a set of policies. You
*  can learn a set of policies, which would be good universally. Yeah. That would be a nice,
*  that would be nice if it's true. And you're saying that there is some evidence that.
*  Let's say lane changes can be clustered into four clusters. Right. Right. There's this finite level.
*  I would argue that all four of those are good clusters. All the things that are random are
*  noise and probably bad. And which one of the four you pick, or maybe it's 10 or maybe it's 20,
*  you can learn that it's context dependent. It depends on the scene.
*  And the hope is it's not too dependent on the driver.
*  Yeah. The hope is that it all washes out. The hope is that there's that the distribution is
*  not bimodal. The hope is that it's a nice Gaussian. So what advice would you give to tell us how to
*  fix, how to improve navigating autopilot? That's the lessons that you've learned from common AI.
*  The only real advice I would give to Tesla is please put driver monitoring in your cars
*  with respect to improving it. You can't do that anymore. I said to interrupt,
*  but you know, there's a practical nature of many of hundreds of thousands of cars being produced
*  that don't have a good driver facing camera. The model three has a selfie cam. Is it not good
*  enough? Did they not have put IR LEDs for night? That's a good question. But I do know that it's
*  fisheye and it's relatively low resolution. So it's really not designed. It wasn't. It wasn't
*  designed for driver monitoring. You can hope that you can kind of scrape up and have something from
*  it. Yeah. But why didn't they put it in today? Put it in today. Put it in today. Every time I've
*  heard Carpathi talk about the problem and talking about like software 2.0 and how the machine
*  learning is gobbling up everything. I think this is absolutely the right strategy. I think that he
*  didn't write and have a get on autopilot. I think somebody else did and kind of hacked it on top of
*  that stuff. I think when Carpathi says, wait a second, why did we hand code this lane change
*  policy with all these magic numbers? We're going to learn it from data. They'll fix it. They already
*  know what to do there. Well, that's, that's Andre's job is to turn everything into a learning problem
*  and collect a huge amount of data. The reality is though, not every problem can be turned into a
*  learning problem in the short term. In the end, everything will be a learning problem. The reality
*  is like, if you want to build L5 vehicles today, it will likely involve no learning.
*  And that's, that's the reality is so at which point does learning start? It's the crutch statement
*  that LIDAR is a crutch. At which point will learning get up to part of human performance?
*  It's over human performance on ImageNet classification on driving. It's a question
*  still. It is a question. I'll say this. I'm, I'm here to play for 10 years. I'm not here to try to,
*  I'm here to play for 10 years and make money along the way. I'm not here to try to promise
*  people that I'm going to have my L5 taxi network up and working in two years. Do you think that
*  was a mistake? Yes. What do you think was the motivation behind saying that other companies
*  are also promising L5 vehicles with their different approaches in 2020, 2021, 2022?
*  If anybody would like to bet me that those things do not pan out, I will, I will bet you even money,
*  even money. I'll bet you as much as you want. So are you worried about what's going to happen?
*  Cause you're not in full agreement on that. What's going to happen when 2022, 21 come around and
*  nobody has fleets of autonomous vehicles? Well, you can look at the history. If you go back five
*  years ago, they were all promised by 2018 and 2017, but they weren't that strong of promises. I mean,
*  Ford really declared pretty, I think not many have declared as, as like definitively as they have now
*  these dates. Well, okay. So let's separate L4 and L5. Do I think that it's possible for Waymo to
*  continue to kind of like, like hack on their system until it gets to level four in Chandler,
*  Arizona? Yes. No safety driver? Chandler, Arizona. Yeah. By which year are we talking about?
*  Oh, I even think that's possible by like 2020, 2021, but level four Chandler, Arizona, not level
*  five, New York city. Level four, meaning some very defined streets. It works out really well.
*  Very defined streets. And then practically these streets are pretty empty. If most of the streets
*  are covered in Waymo's, Waymo can kind of change the definition of what driving is.
*  Right? If your self-driving network is the majority of cars in an area, they only need to be safe with
*  respect to each other and all the humans will need to learn to adapt to them. Now go drive in
*  downtown New York. Oh yeah. That's I mean, already you can talk about autonomy and like, like on
*  farms, it already works great because you can really just follow the GPS line. So what does
*  success look like for Comma AI? What, what are the milestones like where you can sit back with some
*  champagne and say, we did it boys and girls. Well, it's never over. Yeah, but you must drink
*  champagne and everything. So what is a good, what are some wins? A big milestone that we're hoping
*  for by mid next year is profitability of the company. And we're going to have to revisit the
*  idea of selling a consumer product, but it's not going to be like the Comma one. When we do it,
*  it's going to be perfect. OpenPilot has gotten so much better in the last two years.
*  We're going to have a few, a few features. We're going to have a hundred percent driver monitoring.
*  We're going to disable no safety features in the car. Actually, I think it'd be really cool. What
*  we're doing right now, our project this week is we're analyzing the dataset and looking for all
*  the AEB triggers from the manufacturer systems. We have a better data set on that than the
*  manufacturers. How much does, how many, does Toyota have 10 million miles of real world
*  driving to know how many times they're AEB triggered? So let me give you, cause you asked,
*  right? Financial advice. Yeah. Cause I work with a lot of automakers and one possible source of money
*  for you, which I'll be excited to see you take on is basically selling the data.
*  So, which is something that most people and not selling in a way where here, here at automaker,
*  but creating, we've done this actually at MIT, not for money purposes, but you could do it for
*  significant money purposes and make the world a better place by creating a consortia where
*  automakers would pay in and then they get to have free access to the data. And I think a lot of
*  people are really hungry for that and would pay significant amount of money for it.
*  Here's the problem with that. I like this idea all in theory, it'd be very easy for me to give
*  them access to my servers and we already have all open source tools to access this data. It's in a
*  great format. We have a great pipeline, but they're going to put me in the room with some business
*  development guy and I'm going to have to talk to this guy and he's not going to know most of
*  the words I'm saying. I'm not willing to tolerate that. Okay. Mick Jagger. No, no, no, no, no.
*  I think I agree with you. I'm the same way, but you just tell them the terms and there's no discussion
*  needed. If I could just tell them the terms and then like, all right, who wants access to my data?
*  I will sell it to you for, let's say, you want a subscription, I'll sell it to you for 100K a month?
*  Anyone? 100K a month. 100K a month. I'll give you access to the data subscription. Yeah. Yeah,
*  I think that's kind of fair. Came up with that number off the top of my head. If somebody sends
*  me like a three line email where it's like, we would like to pay 100K a month to get access
*  to your data. We would agree to reasonable privacy terms of the people who are in the data set. I
*  would be happy to do it, but that's not going to be the email. The email is going to be,
*  hey, do you have some time in the next month where we can sit down and we can,
*  I don't have time for that. We're moving too fast. Yeah. You could politely respond to that email,
*  but not saying I don't have any time for your bullshit. You say, oh, well, unfortunately,
*  these are the terms. And so this is what we try to, we brought the cost down for you in order to
*  minimize the friction and communication. Yeah, absolutely. Here's the, whatever it is, one,
*  two million dollars a year and you have access. And it's not like I get that email from like,
*  but okay, am I going to reach out? Am I going to hire a business development person who's going
*  to reach out to the automakers? No way. Yeah. Okay. I got you. If they reached into me,
*  I'm not going to ignore the email. I'll come back with something like, yeah, if you're willing to
*  pay 100K a month for access to the data, I'm happy to set that up. That's worth my engineering time.
*  That's actually quite insightful of you. You're right. Probably because many of the automakers
*  quite a bit of old school, there will be a need to reach out and they want it, but they,
*  there'll need to be some communication. You're right. Mobilize circa 2015 had the lowest R&D
*  spend of any chip maker. Like per, and you look at all the people who work for them and it's all
*  business development people because the car companies are impossible to work with.
*  Yeah. So you're, you have no patience for that and you're, you're legit Android, huh?
*  I have something to do, right? Like, it's not like, it's not like I don't need to like be a
*  dick and say like, I don't have patience for that, but it's like that stuff doesn't help us with our
*  goal of winning self-driving cars. If I want money in the short term, if I showed off like the actual,
*  like the learning tech that we have, it's somewhat sad. Like it's years and years ahead of everybody
*  else's, not to, maybe not Tesla's. I think Tesla has similar stuff to us actually. I think Tesla
*  similar stuff, but when you compare it to like what the Toyota research Institute has,
*  you're not even close to what we have. No comments. Well, but I also can't,
*  I have to take your comments. I intuitively believe you, but I have to take it with a grain
*  of salt because I mean, you, you are an inspiration because you basically don't care about a lot of
*  things that other companies care about. You don't try to bullshit in a sense,
*  make up stuff. So to drive a valuation, you're really very real and you're trying to solve the
*  problem and admire that a lot. What I don't necessarily fully can't trust you on with all
*  due respect is how good it is. Right. I can only, but I also know how bad others are.
*  And so I'll say, I'll say two things about don't trust, but verify, right? I'll say two things
*  about that. One is try, get in a 2020 Corolla and try open pilot 0.6 when it comes out next month.
*  I think already you'll look at this and you'll be like, damn, this is already really good.
*  And then I could be doing that all with hand labelers and all with like the same approach
*  that like Mobileye uses. When we release a model that no longer has the lanes in it,
*  that only outputs a path, then think about how we did that machine learning. And then right away,
*  when you see, and that's going to be an open pilot, that's going to be an open pilot before
*  1.0. When you see that model, you'll know that everything I'm saying is true. Cause how else
*  did I get that model? Good. You know what I'm saying is true about the simulator. Right. Yeah.
*  This super exciting. That's super exciting. And, but like, you know, I listened to your talk with
*  Kyle and Kyle was originally building the, the aftermarket system and he gave up on it because
*  of technical challenges. Yeah. Because of the fact that he's going to have to support 20 to 50 cars.
*  We support 45 because what is he going to do when the manufacturer ABS system triggers? We
*  have alerts and warnings to deal with all of that and all the cars. And how is he going to
*  formally verify it? Well, I got 10 million miles of data. It's probably better. It's probably better
*  verified than the spec. Yeah. I'm glad you're here talking to me. This is a, I'll remember this day
*  because it's interesting. If you look at Kyle's from, from Cruz, I'm sure they have a large
*  number of business development folks and you work with, he's working with GM. You could work
*  with Argo AI, working with Ford. It's interesting because chances that you fail business-wise like
*  bankrupt are pretty high. Yeah. And, and yet it's the underwear model is you're actually taking on
*  the problem. So that's really inspiring. I mean, well, I have a longterm way for common to make
*  money too. And one of the nice things when you really take on the problem, which is my hope for
*  autopilot, for example, is things you don't expect ways to make money or create value that you don't
*  expect will pop up. Oh, I've, I've known how to do it since kind of 2017 is the first time I sat at
*  which part to know how to do, how to do which part our longterm plan is to be a car insurance
*  company insurance. Yeah. I love it. Yep. Yep. I make driving twice as safe. Not only that I have
*  the best data such to know who statistically is the safest drivers and oh, oh, we see you,
*  we see you driving on safely. We're not going to ensure you. And that, that causes a like
*  bifurcation in the market because the only people who can't get common insurance or the bad drivers,
*  Geico can ensure them their premiums are crazy high or premiums are crazy low. We'll win car
*  insurance, take over that whole market. Okay. So, uh, if we win, if we win, but that's, I'm saying
*  like, how do you turn comma into a $10 billion company? It's that that's right.
*  So you Elon Musk, who else, uh, who else is thinking like this and working like this in your
*  view, who are the competitors? Are there people seriously? I don't think anyone that I'm aware of
*  is seriously taking on lane keeping, you know, like to where it's a huge business that turns
*  eventually into full autonomy that then creates. Yeah. Like that creates other businesses on top
*  of it and so on. Thanks. Insurance thinks all kinds of ideas like that. Do you know who anyone
*  else think like this? Not really. That's interesting. I mean, my, my sense is everybody turns to that in
*  like four or five years, like Ford, once the autonomy doesn't fall through, but at this time,
*  Elon's the iOS, by the way, he paved the way for all of us. I was not iOS. True. I would not be
*  doing comma AI today if it was not for those conversations with Elon. And if it were not for
*  him saying like, I think he said like, well, obviously we're not going to use LIDAR. We use
*  cameras. Humans use cameras. So what do you think about that? How important is LIDAR? Everybody else
*  is on L5 is using LIDAR. Uh, what are your thoughts on his provocative statement that LIDAR is a crunch?
*  See, sometimes they'll say dumb things like the driver monitoring thing, but sometimes they'll say
*  absolutely completely, 100% obviously true things. Yeah. Of course LIDAR is a crutch.
*  It's not even a good crutch. You're not even using it. Oh, they're using it for localization.
*  Yeah. Which isn't good in the first place. If you have to localize your car to centimeters in order
*  to drive. Like, yeah, they're not driving currently not doing much machine learning. I thought the
*  LIDAR data meaning like to help you in the task of general task of perception. The main goal of
*  those LIDARs on those cars, I think is actually localization more than perception, or at least
*  that's what they use them for. Yeah, that's true. If you want to localize to centimeters, you can't
*  use GPS. The fanciest GPS in the world can't do it, especially if you're under tree cover and stuff.
*  Yeah. Why they can do is pretty easily. So you really, they're not taking on, I mean, in some
*  research they're doing, they're using it for perception, but, and they're certainly not,
*  which sad they're not fusing it well with vision. They do use it for perception. I'm not saying they
*  don't use it for perception, but the thing that they have vision-based and radar-based perception
*  systems as well. You could remove the LIDAR and keep around a lot of the dynamic object perception.
*  You want to get centimeter accurate localization. Good luck doing that with anything else.
*  So what should a Cruz Waymo do? Like what would be your advice to them now? I mean, Waymo is actually,
*  they're serious. Waymo out of the ball of them are quite so serious about the long game.
*  If L5 is a lot, requires 50 years, I think Waymo will be the only one left standing at the end
*  with the, given the financial backing that they have.
*  They're a Google box. I'll say nice things about both Waymo and Cruz.
*  Let's do it. Nice is good.
*  Waymo is by far the furthest along with technology. Waymo has a three to five year lead on all the
*  competitors. If the Waymo looking stack works, maybe three year lead. If the Waymo looking
*  stack works, they have a three year lead. Now, I argue that Waymo has spent too much money
*  to gain back their losses in those three years. Also, self-driving cars have no network effect
*  like that. Uber has a network effect. You have a market, you have drivers, and you have riders.
*  Self-driving cars, you have capital and you have riders. There's no network effect. If I want to
*  blanket a new city in self-driving cars, I buy the off the shelf Chinese knockoff self-driving cars
*  and I buy enough of them in the city. I can't do that with drivers. And that's why Uber has a first
*  mover advantage that no self-driving car company will. Can you just entangle that a little bit?
*  Uber, you're not talking about Uber, the autonomous vehicle Uber. You're talking about the Uber car.
*  Okay. Yeah. I'm Uber. I open for business in Austin, Texas, let's say. I need to attract
*  both sides of the market. I need to both get drivers on my platform and riders on my platform.
*  And I need to keep them both sufficiently happy. Riders aren't going to use it if it takes more
*  than five minutes for an Uber to show up. Drivers aren't going to use it if they have to sit around
*  all day and there's no riders. So you have to carefully balance a market. And whenever you
*  have to carefully balance a market, there's a great first mover advantage because there's a
*  switching cost for everybody, right? The drivers and the riders would have to switch at the same
*  time. Let's even say that, let's say, a Luber shows up and Luber somehow agrees to do things at a
*  bigger... We've done it more efficiently, right? Luber only takes 5% of a cut instead of the 10%
*  that Uber takes. No one is going to switch because the switching cost is higher than that 5%. So you
*  actually can, in markets like that, you have a first mover advantage. Autonomous vehicles
*  of the level five variety have no first mover advantage. If the technology becomes commoditized,
*  say I want to go to a new city, look at the scooters. It's going to look a lot more like
*  scooters. Every person with a checkbook can blanket a city in scooters and that's why you
*  have 10 different scooter companies. Which one's going to win? It's a race to the bottom. It's
*  terrible market to be in because there's no market for scooters. The scooters don't get a say in
*  whether they want to be bought and deployed to a city or not. We're going to entice the scooters
*  with subsidies and deals. So whenever you have to invest that capital, it doesn't come back.
*  Yeah. That can't be your main criticism of the Waymo approach.
*  Oh, I'm saying even if it does technically work.
*  Even if it does technically work, that's a problem. I don't know if I were to say,
*  I would say you're already there. I haven't even thought about that, but I would say the
*  bigger challenge is the technical approach. So Waymo's cruise is-
*  And not just the technical approach, but creating value. I still don't understand how you
*  beat Uber, the human driven cars in terms of financially. It doesn't make sense to me that
*  people want to get in an autonomous vehicle. I don't understand how you make money
*  in the long term. Yes, like real long-term, but it just feels like there's too much
*  capital investment needed. Oh, and they're going to be worse than Uber's because they're going to
*  stop for every little thing everywhere. I'll say a nice thing about cruise. That was my nice thing
*  about Waymo. They're three years ahead of it. What was the nice- Oh, because they're three-
*  They're three years technically ahead of everybody. Their tech stack is great.
*  My nice thing about cruise is GM buying them was a great move for GM. For $1 billion, GM bought an
*  insurance policy against Waymo. They put cruise is three years behind Waymo. That means Google
*  will get a monopoly on the technology for at most three years. And if the technology works,
*  you might not even be right about the three years. It might be less.
*  Might be less. Cruise actually might not be that far behind. I don't know how much Waymo has
*  waffled around or how much of it actually is just that long tail.
*  Yeah. Okay. If that's the best you could say in terms of nice things,
*  that's more of a nice thing for GM that that's the smart insurance policy.
*  It's a smart insurance policy. I mean, I think that's how I can't see cruise working out any
*  other. For cruise to leapfrog Waymo would really surprise me. Yeah. So let's talk about the
*  underlying assumptions of everything. We're not going to leapfrog Tesla.
*  Tesla would have to seriously mess up for us because you're okay. So the way you leapfrog,
*  right, is you come up with an idea or you take a direction perhaps secretly that the other people
*  aren't taking. And so the cruise Waymo, even Aurora, I don't know Aurora. Zooks is the same
*  stack as well. They're all the same code base even in all the same DARPA urban challenge code base.
*  So the question is, do you think there's a room for brilliance and innovation there that will change
*  everything? Like say, okay, so I'll give you examples. It could be if revolution and mapping,
*  for example, that allow you to map things, do HD maps of the whole world, all weather conditions
*  somehow really well or revolution and simulation to where the way you said before becomes
*  incorrect. That kind of thing. Any room for breakthrough innovation? What I said before
*  about, oh, they actually get the whole thing. Well, I'll say this about, we divide driving into three
*  problems and I actually haven't solved the third yet, but I haven't had you do that yet. So I'll
*  say that's the first problem. So there's the static. The static driving problem is assuming
*  you are the only car on the road. And this problem can be solved 100% with mapping and localization.
*  This is why farms work the way they do. If all you have to deal with is the static problem
*  and you can statically schedule your machines, it's the same as statically scheduling processes.
*  You can statically schedule your tractors to never hit each other on their paths because they know
*  the speed they go at. So that's the static driving problem. Maps only helps you with the
*  static driving problem. Yeah. The question about static driving. You just made it sound like it's
*  really easy. Static driving is really easy. How easy? Well, because the whole drifting out of lane,
*  when Tesla drifts out of lane, it's failing on the fundamental static driving problem.
*  Tesla is drifting out of lane. The static driving problem is not easy for the world.
*  The static driving problem is easy for one route.
*  One route and one weather condition with one state of lane markings and like no deterioration,
*  no cracks in the road. I'm assuming you have a perfect localizer. So that's solved for the
*  weather condition and the lane marking condition. But that's the problem is how good you, how do
*  you have a perfect localizer? Perfect localizers are not that hard to build. Okay. Come on now.
*  With, with, with, with, with LIDAR. LIDAR. Yeah. Oh, with LIDAR. Okay. LIDAR. Yeah. But you use
*  LIDAR, right? Like use LIDAR, build a perfect localizer, building a perfect localizer without
*  LIDAR. It's going to be, it's going to be hard. You can get 10 centimeters without LIDAR. You can
*  get one centimeter with LIDAR. I'm not even concerned about the one or 10 centimeters. I'm
*  concerned if every once in a while you're just way off. Yeah. So this is why you have to carefully
*  make sure you're always tracking your position. You want to use LIDAR camera fusion, but you can
*  get the reliability of that system up to a hundred thousand miles. And then you write some fallback
*  condition where it's not that bad if you're way off, right? I think that you can get it to the
*  point. It's like as old D that you're, you're never in a case where you're way off and you don't know
*  it. Yeah. Okay. So this is brilliant. So that's the static. We can, especially with LIDAR
*  and good HD maps, you can solve that problem. Easy. No, I just, no, it's the static. It's
*  static. I'm so easy. Very typical for you to say something is easy. I got it. It's not as challenging
*  as the other ones. Okay. Well, it's okay. Maybe it's obvious how to solve it. The third one's the
*  hardest. So where do we get, and a lot of people don't even think about the third one and even see
*  it as different from the second one. So the second one is dynamic. The second one is like, say there's
*  an obvious example. It's like a car stopped at a red light, right? You can't have that car in your
*  map because you don't know whether that car is going to be there or not. So you have to detect
*  that car in real time and then you have to do the appropriate action. Right. Also that car is not a
*  fixed object. That car may move and you have to predict what that car will do. Right. So this is
*  the dynamic problem. Yeah. So you have to deal with this. This involves, again, like you're going to
*  need models of other people's behavior. Do you, are you including in that? I don't want to step on
*  the third one, but are you including in that your influence on people? Ah, that's the third one.
*  Okay. That's the third one. We call it the counterfactual. Yeah. And that I just talked to
*  Judea Pearl who's obsessed with counterfactuals. Oh yeah. Yeah. There's books. So the static and
*  the dynamic, our approach right now for lateral will scale completely to the static and dynamic.
*  The counterfactual, the only way I have to do it yet, the thing that I want to do once we have
*  all of these cars is I want to do reinforcement learning on the world.
*  I'm always going to turn the exploiter up to max. I'm not going to have them explore,
*  but the only real way to get at the counterfactual is to do reinforcement learning because the other
*  agents are humans. So that's fascinating that you break it down like that. I agree completely.
*  I've spent my life thinking about this. It's beautiful. So, and part of it,
*  because you're slightly insane, because not my life, just the last four years.
*  No, no, you have like some non-zero percent of your brain has a madman in it. That's a really
*  good feature, but there's a safety component to it that I think when there's sort of with counterfactuals
*  and so on that would just freak people out. How do you even start to think about just in general?
*  I mean, you've had some friction with NHTSA and so on. I am frankly exhausted by safety engineers,
*  the prioritization on safety over innovation to a degree where it kills, in my view,
*  kills safety in the long-term. So the counterfactual thing, they just actually exploring this world of
*  how do you interact with dynamic objects and so on. How do you think about safety?
*  You can do reinforcement learning without ever exploring. And I said that like, so you can think
*  about your, in reinforcement learning, it's usually called like a temperature parameter.
*  And your temperature parameter is how often you deviate from the argmax. I could always set that
*  to zero and still learn. And I feel that you'd always want that set to zero on your actual system.
*  Gotcha. But the problem is you first don't know very much and so you're going to make mistakes.
*  So the learning, the exploration happens through mistakes.
*  We're almost ready. Yeah, but okay. So the consequences of a mistake. Open pilot and
*  autopilot are making mistakes left and right. We have 700 daily active users,
*  a thousand weekly active users. Open pilot makes tens of thousands of mistakes a week.
*  These mistakes have zero consequences. These mistakes are, oh, I wanted to take this exit
*  and it went straight. So I'm just going to carefully touch the wheel.
*  The humans catch them. The humans catch them.
*  And the human disengagement is labeling that reinforcement learning in a completely
*  consequence free way. So driver monitoring is the way you ensure they keep paying attention.
*  How's your messaging? Say I gave you a billion dollars, you would be scaling it now.
*  Oh, if I could scale, I couldn't scale it with any amount of money. I'd raise money if I could,
*  if I had a way to scale it. Yeah, you're not focused on scaling.
*  I don't know how to do it. Oh, like I guess I could sell it to more people,
*  but I want to make the system better. Better, better.
*  And I don't know how to. But what's the messaging here?
*  I got a chance to talk to Elon and he basically said that the human factor doesn't matter.
*  The human doesn't matter because the system will perform. There'll be sort of a,
*  sorry to use the term, but like a singular, like a point where it gets just much better.
*  And so the human, it won't really matter, but it seems like that human catching the system when it
*  gets into trouble is like the thing which will make something like reinforcement learning work.
*  So how do you, how do you think messaging for Tesla, for you,
*  for the industry in general should change? I think my messaging is pretty clear, at least like
*  our messaging wasn't that clear in the beginning. And I do kind of fault myself for that.
*  We are proud right now to be a level two system. We are proud to be level two. If we talk about
*  level four, it's not what the current hardware, it's not going to be just a magical OTA upgrade.
*  It's going to be new hardware. It's going to be very carefully thought out. Right now,
*  we are proud to be level two and we have a rigorous safety model. I mean, not like, like,
*  okay, rigorous, who knows what that means, but we at least have a safety model and we make it
*  explicit is in safety.md and open pilot. And it says, seriously though, safety.md.
*  Oh, this is brilliant. This is so Android.
*  So, well, this is, this is the, this is the safety model. And I like to have conversations like,
*  if like, you know, sometimes people will come to you and they're like, your system's not safe.
*  Okay. Have you read my safety docs? Would you like to have an intelligent conversation about this?
*  And the answer is always no. They just like scream about it runs Python.
*  Okay. What? So you're saying that, that because Python's not real time,
*  Python not being real time never causes disengagement. Disengagement are caused by
*  the model is QM. But safety.md says the following. First and foremost, the driver must be paying
*  attention at all times. I don't con I do, I still consider the software to be alpha software until
*  we can actually enforce that statement, but I feel it's very well communicated to our users.
*  Two more things. One is the user must be able to easily take control of the vehicle at all times.
*  So if you step on the gas or brake with open pilot,
*  it gives full manual control back to the user or press the cancel button.
*  Step two, the car will never react so quickly. We define so quickly to be about one second
*  that you can't react in time. And we do this by enforcing torque limits,
*  breaking limits and acceleration limits. So we have like our torque limits way lower than Tesla's.
*  This is another potential. If I could tweak autopilot, I would lower their torque limit
*  and I would add driver monitoring. Because autopilot can jerk the wheel hard. Open pilot
*  can't. We limit and all this code is open source, readable. And I believe now it's all Mizzra C
*  compliant. What's that mean? Mizzra is like the automotive coding standard. At first, I've come
*  to respect, I've been reading the standards lately and I've come to respect them. They're actually
*  written by very smart people. Yeah, they're brilliant people actually. They have a lot of
*  experience. They're sometimes a little too cautious, but in this case, it pays off.
*  Mizzra is written by computer scientists and you can tell by the language they use. You can
*  tell by the language they use. They talk about whether certain conditions in Mizzra are decidable
*  or undecidable. And you mean like the halting problem? And yes. All right. You've earned my
*  respect. I will read carefully what you have to say and we want to make our code compliant with
*  that. All right. So you're proud level two. Beautiful. So you were the founder and I think
*  CEO of Kamei. Then you were the head of research. What the heck are you now? What's your connection
*  to Kamei? I'm the president, but I'm one of those like unelected presidents of like a small
*  dictatorship country, not one of those like elected presidents. Oh, so you're like Putin when he was
*  like the, yeah, I got you. So there's a, what's the governance structure? What's the future of
*  Kamei? I mean, yeah, it's a business. Do you want, are you just focused on getting things right now?
*  Making some small amount of money in the meantime. And then when it works, it works and you scale.
*  Our burn rate is about 200K a month and our revenue is about a hundred K a month.
*  So we need to forex our revenue, but we haven't like tried very hard at that yet. And the revenue
*  is basically selling stuff online. Yeah. We sell stuff shop.kama.ai. Is there other, well,
*  you'll have to figure out that's our only, see, but to me that's like respectable revenues.
*  We make it by selling products to consumers. We're honest and transparent about what they are.
*  Most actually level four companies, right? Cause you could easily start blowing up like smoke,
*  like overselling the hype and feeding into getting some fundraisers. Oh, you're the guy,
*  you're genius because you hacked the iPhone. Oh, I hate that. I hate that. Yeah. Well,
*  I can trade my social capital for more money. I did it once. I almost forgot. I regret it.
*  Well, on a small tangent, what's your, you seem to not like fame and yet you're also drawn to fame.
*  Yeah. Where have you, where are you on that currently? Have you had some introspection,
*  some soul searching? Yeah. I actually, I've come to a pretty stable position on that.
*  Like after the first time I realized that I don't want attention from the masses.
*  I want attention from people who I respect. Who do you respect? I can give a list of people.
*  So are these like Elon Musk type characters? Yeah. Or actually, you know what? I'll make it
*  more broad than that. I won't make it about a person. I respect skill. I respect people who
*  have skills. Right. And I would like to like be, I'm not going to say famous, but be like
*  known among more people who have like real skills. Who in cars do you think have skill,
*  not do you respect? Oh, Kyle Vogt has skill. A lot of people at Waymo have skill and I respect them.
*  I respect them as engineers. Like I can think, I mean, I think about all the times in my life
*  where I've been like dead set on approaches and they turned out to be wrong. So I mean,
*  this might, I might be wrong. I accept that. I accept that there's a decent chance that I'm
*  I'm wrong. And actually, I mean, having talked to Chris Ermson, Sterling Anderson, those guys,
*  I mean, I deeply respect Chris. I just admire the guy. He's legit. When you drive a car through the
*  desert, when everybody thinks it's impossible, that's legit. And then I also really respect the
*  people who are like writing the infrastructure of the world, like the Linus Torvalds and the Chris
*  Latimer. They were doing the real work. I know they're doing the real work.
*  Having talked to Chris, Chris Latimer, you realize, especially when they're humble,
*  it's like you realize, oh, you guys were just using your, oh yeah, the all the hard work that
*  you did. Yeah, that's incredible. What do you think, Mr. Anthony Lewandowski?
*  What do you, he's, he's another mad genius. Sharp guy. Oh yeah. What,
*  do you think he might long-term become a competitor? Oh, to comma? Well, so I think that he has the
*  other right approach. I think that right now there's two right approaches. One is what we're doing and
*  one is what he's doing. Can you describe, I think it's called Pronto AI. He started a new thing,
*  do you know what the approach is? I actually don't know. Embark is also doing the same sort
*  of thing. The idea is almost that you want to, so if you're, I can't partner with Honda and Toyota.
*  Honda and Toyota are like 400,000 person companies. It's not even a company at that point. Like I
*  don't think of it like, I don't personify it. I think of it like an object, but a trucker drives
*  for a fleet maybe that has like, some truckers are independent. Some truckers drive for fleets
*  with a hundred trucks. There are tons of independent trucking companies out there.
*  Start a trucking company and drive your costs down or figure out how to drive down the cost of
*  trucking. Another company that I really respect is Nauto. Actually, I respect their business model.
*  Nauto sells a driver monitoring camera and they sell it to fleet owners. If I, that's right. If
*  I owned a fleet of cars and I could pay 40 bucks a month to monitor my employees,
*  this is going to like reduces accidents 18%. It's so like that in the space,
*  that is like the business model that I like most respect because they're creating value today.
*  Yeah, which is, that's a huge one. How do we create value today with some of this?
*  The lane keeping thing is huge and it sounds like you're creeping in or full steam ahead on
*  the drive monitoring too, which I think actually where the short-term value, if you can get it right.
*  I still, I'm not a huge fan of the statement that everything has to have driver monitoring.
*  I agree with that completely, but that statement usually misses the point that to get the experience
*  of it right is not trivial. Oh no, not at all. In fact, like, so right now we have,
*  uh, I think the timeout depends on speed of the car. Um, but we want to depend on like the scene
*  state. If you're on like an empty highway, it's very different if you don't pay attention than
*  if like, you're like coming up to a traffic light. And long-term, it should probably learn from,
*  from the driver because that's to do. I watched a lot of video. We've built a smartphone detector
*  just to analyze how people are using smartphones and people are using it very differently.
*  This is, um, uh, so texting styles, there's watched nearly enough of the videos.
*  We have, I got, I got millions of miles of people driving cars. In this moment, I spent a large
*  fraction of my time just watching videos because it's never fails to, to learn like it never,
*  I've never failed from a video watching session to learn something I didn't know before. In fact,
*  I usually, um, like when I eat lunch, I'll sit, uh, especially when the weather is good and just
*  watch pedestrians, uh, with an eye to understand like from a computer vision eye, just to see,
*  can this model, can you predict what are the decisions made? And there's so many things that
*  we don't understand. This is what I mean about the state vector. Yeah, it's, uh, I'm trying to always
*  think like, cause I'm understanding in my human brain, how do we convert that into how hard is
*  the learning problem here? I guess is the fundamental question. So something that's, uh,
*  from a hacking perspective, this is always comes up, especially with folks. Well, first,
*  the most popular question is, uh, the trolley problem, right? So that's not a sort of a serious,
*  uh, problem. There are some ethical questions I think that arise. Uh, maybe you want to,
*  you want, do you, do you think there's any ethical serious ethical questions?
*  We have, we have a solution to the trolley problem at Comm. AI.
*  Well, so there is actually an alert in our code, ethical dilemma detected. It's not triggered yet.
*  We don't, we don't have yet to detect the ethical dilemmas, but we're a level two system. So we're
*  going to disengage and leave that decision to the human. You're such a troll. No, but the trolley
*  problem deserves to be trolled. Yeah. That's a beautiful answer. Actually. I know I gave it
*  to someone who was like, sometimes people ask, like you asked about the trolley problem. Like
*  you can have a kind of discussion about it. Like when you get someone who's like really like
*  earnest about it, because it's the kind of thing where if you ask a bunch of people in an office,
*  we should use a SQL stack or a no SQL stack. If they're not that technical, they have no opinion.
*  But if you ask them what color they want to paint the office, everyone has an opinion on that.
*  And that's why the trolley problem is. That's it. I mean, that's a beautiful answer. Yeah. We're
*  able to detect the problem and we're able to pass it on to the human. Wow. I've never,
*  never heard anyone say it. And this is your nice escape route. Okay. But, um, proud level two,
*  proud level two. I love it. So the other thing that people, you know, have some concern about
*  with AI in general is, uh, hacking. So how hard is it? Do you think to hack an autonomous vehicle
*  either through physical access or through the more sort of popular now, these adversarial
*  examples on the sensors? Okay. The adversarial examples one, you want to see some adversarial
*  examples that affect humans, right? Oh, well, there used to be a stop sign here, but I put a
*  black bag over the stop sign and then people ran it adversarial. Right? Like, like, like there's
*  tons of human adversarial examples too. Um, the question in general about like security, if you
*  saw something just came out today and like, they're always such hypey headlines about like how
*  navigate on autopilot was fooled by a GPS spoof to take an exit. Right. At least that's all they
*  could do was take an exit. If your car is relying on GPS in order to have a safe driving policy,
*  you're doing something wrong. If you're relying, and this is why Vita V is such a terrible idea,
*  Vita V now relies on both parties getting communication. Right. This is not even,
*  so I think of, uh, sec is safety. Uh, security is like a special case of safety, right? Safety is
*  like we put a little, you know, piece of caution tape around the hole so that people won't walk
*  into it by accident. Security is like put a 10 foot fence around the hole. So you actually
*  physically cannot climb into it with barbed wire on the top and stuff. Right. So like if you're
*  designing systems that are like unreliable, they're definitely not secure. Your car should always do
*  something safe using its local sensors. Right. And then the local sensor should be hardwired.
*  And then could somebody hack into your canvas and turn your steering wheel and your brakes? Yes.
*  But they could do it before comma AI too. So let's think out of the box and some things. So
*  do you think, uh, tele operation has a role in any of this? So remotely stepping in and, uh,
*  controlling the cars? No, I think that if safety, if, if, if the safety operation by design requires
*  a constant link to the cars, I think it doesn't work. So that's the same argument using for V2I,
*  V2V. Well, there's a lot of non-safety critical stuff you can do with V2I. I like V2I. I like
*  V2I way more than V2V because V2I is, is already like, I already have internet in the car, right?
*  There's a lot of great stuff you can do with V2I. Um, like for example, you can, well,
*  we already have V2, Waze is V2I, right? Waze can route me around traffic jams. That's a great
*  example of V2I. And then, okay, the car automatically talks to that same service.
*  Like improving the experience, but it's not a fundamental fall, fall back for safety. No,
*  if any of your, if any of your, uh, if any of your things that require wireless communication
*  are more than QM, like have an asl rating, you shouldn't. You previously said that life is work
*  and that you don't do anything to relax. So how do you think about hard work? Well, what is it,
*  what do you think it takes to accomplish great things? And there's a lot of people saying that
*  there needs to be some balance. You know, you need to, in order to accomplish great things,
*  you need to take some time off, you need to reflect and so on. And then some people are
*  just insanely working, burning the candle on both ends. How do you think about that?
*  I think I was trolling in the Siraj interview when I said that, um, off camera,
*  right before I smoked a little bit of weed, like, you know, come on, this is a joke, right? Like I
*  do nothing to relax. Look where I am. I'm at a party, right? Yeah, that's true. Um, so no,
*  of course I don't, um, when I say that life is work though, I mean that like, uh, I think that
*  what gives my life meaning is work. I don't mean that every minute of the day you should be working.
*  I actually think this is not the best way to maximize results. I think that if you're working
*  12 hours a day, you should be working smarter and not harder. Well, uh, so it gives work gives you
*  meaning for some people, uh, other sorts of meaning as personal relationships, uh, like family and so
*  on. You've also in that interview with Siraj or the trolling mentioned, uh, that one of the things
*  you look forward to in the future is AI girlfriends. Yes. So, uh, that's a topic that I'm very much
*  fascinated by not necessarily girlfriends, but just forming a deep connection with AI. Uh, what kind
*  of system do you imagine when you say AI girlfriend, whether you were trolling or not? No, that one I'm
*  very serious about. And I'm serious about that on both a shallow level and a deep level. Um, I think
*  that VR brothels are coming soon and are going to be really cool. Um, it's not cheating if it's a
*  robot. I see the slogan already. Um, but there's a, I don't know if you've watched or just watched
*  the black Mary episode. I watched the last one. Yeah. Yeah. Yeah. Um, oh, the, the, the Ashley
*  two one or the, uh, no, where there's a two friends were, uh, having sex with each other in,
*  oh, in the VR game, the VR game. Yeah. It's just two guys, but one of them was, was a female. Yeah.
*  Which is another mind blowing concept that in VR, you don't have to be the form. You can be two
*  animals having sex, sex. It's weird. I mean, I'll see how nice it, the software maps, the nerve
*  endings, right? Um, I mean, yeah, they, they sweep a lot of the fascinating, really difficult
*  technical challenges under the rock, like assuming it's possible to do the mapping of the nerve
*  endings. Uh, then I wish, yeah, I saw that the way they did it with the little like STEM unit on the
*  head that that'd be amazing. So, well, no, no, on a shallow level, like you could set up like almost
*  brothel with like real dolls and Oculus quests, right? Um, write some good software. I think it'd
*  be a cool novelty experience. Uh, but no, on a deeper, like emotional level, I mean, yeah,
*  I would really like to, to, to, to fall in love with, with, with the machine. Do you see yourself
*  having a long-term relationship of the kind, monogamous relationship that we have now
*  with a robot, with a AI system even, not even just the robot.
*  So I think about maybe my ideal future. When I was 15, I read, uh, Eliezer Yudkowski's early writings
*  on the singularity and like that AI is going to surpass human intelligence massively. Um,
*  he made some Moore's law based predictions that I mostly agree with.
*  And then I really struggled for the next couple of years of my life. Like why should I even bother
*  to learn anything? It's all going to be meaningless when the machines show up.
*  Right.
*  Maybe, maybe when I was, uh, that young, I was still a little bit more pure and really like clung
*  to that. And then I'm like, well, the machines ain't here yet, you know, and I seem to be pretty
*  good at this stuff. Let's, uh, let's try my best, you know, like what's the worst that happens.
*  But the best possible future I see is me sort of merging with the machine and the way that I
*  personify this is in a long-term monogamous relationship with a machine.
*  Oh, you don't think there's room for another human in your life if you really truly merge
*  with another machine.
*  I mean, I see merging. I see like the best interface to my brain
*  is like the same relationship interface to merge with an AI. Right. What does that merging feel
*  like? I've seen, I've seen couples who've been together for a long time and like, I almost think
*  of them as one person, like couples who spend all their time together. And that's fascinating.
*  You're actually putting, what does that merging actually looks like? It's not just a nice channel.
*  Like a lot of people imagine it's just an efficient link, search link to Wikipedia or something.
*  I don't believe in that.
*  But it's more, you're saying that there's the same kind of, the same kind of relationship,
*  you have one other human that's a deep relationship is that's what merging looks like.
*  That's, that's pretty, uh,
*  I don't believe that link is possible. Um, I think that that link, so you're like,
*  oh, I'm going to download Wikipedia right to my brain. Yeah. My reading speed is not limited
*  by my eyes. My reading speed is limited by my inner processing loop. And to like bootstrap that
*  sounds kind of unclear how to do it and horrifying. But if I am with somebody and I'll use a somebody
*  who is making a super sophisticated model of me and then running simulations on that model,
*  I'm not going to get into the question whether the simulations are conscious or not. I don't
*  really want to know what it's doing. Um, but using those simulations to play out hypothetical
*  futures for me, deciding what things to say to me, to guide me along a path. And
*  that's how I envision it. So on that path to AI of superhuman level intelligence,
*  you've mentioned that you believe in the singularity that singularity is coming.
*  Yeah. Again, could be trolling, could be not, could be part,
*  I don't know. All trolling has truth in it. I don't know what that means anymore. What is the
*  singularity? Yeah. So that's, that's really the question. How many years do you think before the
*  singularity award form do you think it will take? Does that mean fundamental shifts in capabilities
*  of AI? Does it mean some other kind of ideas? Um, uh, maybe this is just my roots, but so I can buy
*  a human being's worth of compute for like a million bucks today. It's about one TPU pod V3. I want like,
*  I think they claim a hundred pay to flops. That's being generous. I think humans are actually more
*  like 20. So that's like five humans. That's pretty good. Google needs to sell their TPUs. Um, but I
*  could buy, I could buy, I could buy GPUs. I could buy a stack of like, uh, I buy 10, 80 TIs, uh,
*  build data center full of them. And, uh, for a million bucks, I can get a human worth of, uh,
*  compute. But when you look at the total number of flops in the world, when you look at human flops,
*  which goes up very, very slowly with the population and machine flops, which goes up exponentially,
*  but it's still nowhere near. I think that's the key thing to talk about when the singularity
*  happened. When most flops in the world are silicon and not biological, that's kind of
*  the crossing point. Like they are now the dominant species on the planet.
*  And, uh, just looking at how technology is progressing, when do you think that could
*  possibly happen? You think it would happen in your lifetime? Oh yeah, definitely in my lifetime.
*  I've done the math. I like 2038 because it's the Unix timestamp rollover.
*  Yeah, beautifully put. Uh, so you've, uh, you've said that the meaning of life is to win.
*  If you look five years into the future, what does winning look like?
*  So, uh, there, there's a lot of, I can go into like technical depth to what I mean by that to win.
*  Um, it may not mean, I was criticized for that in the comments, like, doesn't this guy want to
*  like save the penguins in Antarctica or like, Oh man, you know, listen to what I'm saying. I'm
*  not talking about like, I have a yacht or something. I am an agent. I am put into this world
*  and I don't really know what my purpose is. But if you're a reinforcement, if you're,
*  if you're an intelligent agent and you're put into a world, what is the ideal thing to do?
*  Well, the ideal thing mathematically and go back to like Schmidhuber theories about this
*  is to, uh, build a compressive model of the world, to build a maximally compressive,
*  to explore the world such that your exploration function maximizes the derivative of compression
*  of the past. Schmidhuber has a paper about this and like, I took that kind of as like a personal
*  goal function. Um, so what I mean to win, I mean like, maybe, maybe this is religious, but like,
*  I think that in the future I might be given a real purpose or I may decide this purpose myself.
*  And then at that point, now I know what the game is and I know how to win. I think right now I'm
*  still just trying to figure out what the game is. But once I know. So you have, uh, you have, uh,
*  imperfect information. You have a lot of uncertainty about the reward function and you're
*  discovering it. Exactly. But the purpose is that's a better way to put it. So the purpose is to
*  maximize it while you have it, uh, a lot of uncertainty around it and you're both reducing
*  the uncertainty and maximizing at the same time. And, uh, so that's at the technical level.
*  What is the, if you believe in the universal prior, what is the universal reward function?
*  That's the better way to put it. So that when it's interesting, I think I speak for everyone
*  in saying that I wonder what that reward function is for you. And, uh,
*  I look forward to seeing that in five years and 10 years. I think a lot of people,
*  including myself, are cheering you on, man. So I'm, I'm happy you exist and, uh,
*  I wish you the best of luck. Thanks for talking to me, man. Thank you. This is a lot of fun.

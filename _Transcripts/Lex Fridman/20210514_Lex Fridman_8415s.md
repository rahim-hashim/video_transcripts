---
Date Generated: April 12, 2024
Transcription Model: whisper medium 20231117
Length: 8415s
Video Keywords: ['math', 'math olympiad', 'lex math', 'lex podcast']
Video Views: 267412
Video Rating: None
---

# Po-Shen Loh: Mathematics, Math Olympiad, Combinatorics & Contact Tracing | Lex Fridman Podcast #183
**Lex Fridman:** [May 14, 2021](https://www.youtube.com/watch?v=6z1JwZbX4dQ)
*  The following is a conversation with Po Shen Lo, a professor of mathematics at Carnegie Mellon
*  University, national coach of the USA International Math Olympia team, and founder of XP that does
*  online education of basic math and science. He's also the founder of Novid, an app that takes a
*  really interesting approach to contact tracing, making sure you stay completely anonymous
*  and it gives you statistical information about COVID cases in your physical network of interactions
*  so you can maintain privacy, very important, and make informed decisions. In my opinion,
*  we desperately needed solutions like this in early 2020 and unfortunately, I think, we will again
*  need it for the next pandemic. To me, solutions that require large-scale distributed coordination
*  of human beings need ideas that emphasize freedom and knowledge. Quick mention of our sponsors,
*  Jordan Harbinger Show, Onnit, BetterHelp, 8 Sleep, and Element. Check them out in the description to
*  support this podcast. As a side note, let me say that Po and I filmed a few short videos about
*  simple, beautiful math concepts that I will release soon. It was really fun. I really enjoyed Po
*  sharing his passion for math with me in those videos. I'm hoping to do a few more short videos
*  in the coming months that are educational in nature on AI, robotics, math, science, philosophy,
*  or if all else fails, just fun snippets into my life on music, books, martial arts,
*  and other random things, if that's of interest to anyone at all. This is the Lex Friedman Podcast
*  and here's my conversation with Po Shenlo. You know, you mentioned you really enjoy flying
*  and experiencing different people in different places. There's something about flying for me.
*  I don't know if you have the same experience that every time I get on an airplane,
*  it's incredible to me that human beings have actually been able to achieve this.
*  And when I look at like what's happening now with humans traveling out into space,
*  I see it as all the same thing. It's incredible that humans are able to get into a box and fly
*  in the air and safely and land. And everybody's taking it for granted. So when I observe them,
*  it's quite fascinating because I see that cleanly mapping to the world where we're now
*  in rockets and traveling to the moon, traveling to Mars. And at the same kind of way,
*  I can already see the future where we will all take it for granted.
*  So I don't know if you personally when you fly have the same kind of magical experience
*  of like how the heck did humans actually accomplish this?
*  So I do, especially when there's turbulence, which is, you know, like on the way here,
*  there was turbulence and the plane jiggled, even the flight attendant had to hold on to the side.
*  And I was just thinking to myself, it's amazing that this happens all the time
*  and the wings don't fall off, you know, like given how many planes are flying.
*  Given how many planes are flying. But then I often think about it and I'm like,
*  you know, a long time ago, I think people didn't trust elevators in a 40 story building in New York
*  City. And now we just take it completely for granted that you can step into this shaft,
*  which is 40 floors up and down, and it will just not fail.
*  Yeah, again, I'm the same way with elevators, but also buildings. When I'll stand on the 40th floor
*  and wonder how the heck are we not falling right now? Like how amazing it is with the high winds,
*  like structurally just the earthquakes and the vibrations, I mean,
*  natural vibrations in the ground. Like how is this, how are all of these, you go like New York City,
*  all of these buildings standing. I mean, to me, one of the most beautiful things,
*  actually mathematically too, is bridges. I used to build bridges in high school from like toothpicks,
*  just like out of the pure joy of like physics, making some structure really strong,
*  understanding like from a civil engineering perspective, what kind of structure will be
*  stronger than another kind of structure, like suspension bridges. And then you see that at
*  scale, humans being able to span a body of water with a giant bridge. And it's, I don't know,
*  it's so humbling. It makes you realize how dependent we are on each other. I talk about
*  love a lot, but there's a certain element in which we little ants have just a small amount
*  of knowledge about our particular thing. And then we're depending on a network of knowledge
*  that other experts hold. And then most of our lives, most of the quality of life we have has
*  to do with the richness of that network of knowledge, of that collaboration, and then
*  sort of the ability to build on top of it levels of abstractions. You start from like bits in a
*  computer, then you can have assembly, then you can have C++, or you have an operating system,
*  then you can have C++ and Python, finally some machine learning on top. All of these,
*  they're abstractions. And eventually we have AI that runs all of us humans. But anyway,
*  but speaking of abstractions and programming, in high school you wrote some impressive games
*  for Amistos. I got a chance to, in browser somehow, it's magic. I got a chance to play them.
*  Alien Attack 1, 2, 3, and 4. What's the hardest part about programming those games? And maybe
*  can you tell the story about building those games? Sure. I actually tried to do those in high school
*  because I was just curious if I could. It's a good starting point for anything, right? Yeah,
*  yeah, yeah. It's like, could you? But the appealing thing was also, it was a soup to nuts kind of
*  thing. So something that has always attracted me is I like beautiful ideas. I like seeing
*  beautiful ideas, but I actually also like seeing execution of an idea all the way from beginning
*  to end in something that works. So for example, in high school, I was lucky enough to grow up
*  in the late 90s when even a high school student could hope to make something
*  comparable to the shareware games that were out there. I say the word sort of, still quite far
*  away, but at least I didn't need to hire a 3D CG artist. There weren't enough pixels to draw
*  anyway, even I can draw, right? Bad art, of course. But the point is I wanted to know,
*  is it possible for me to try to do those things where back in those days you didn't even have an
*  easy way to draw letters on the screen in a particular font. You couldn't just say import
*  a font. It wasn't like Python. So for example, back then, if you play those games in the web
*  browser, which is emulating the old school computer, even the letters you see, those are
*  made by individual calls to draw pixels on the screen. So you built that from scratch, almost
*  building a computer graphics library from scratch? Yes. The primitive that I got to use was some code
*  I copied off of a book in assembly of how to put a pixel on a screen in a particular color.
*  And the programming language was Pascal? Yeah, the first one was in Pascal, but then the
*  other ones were in C++ after that. How's the emulation in the browser work, by the way? Is
*  that trivial? Because it's pretty cool. You get to play these games that have a very much 90s feeling
*  to them. So it's literally making an MS-DOS environment, which is literally running the old
*  .exe file. Wow. In a browser. That could be more amazing than the airplane. So it wasn't so much
*  about the video games. It was more about, can you build something really cool from scratch? Yes.
*  And you did a bunch of programming competitions. What was your interest, your love for programming?
*  What did you learn through that experience? Especially now that as much of your work has
*  taken a long journey through mathematics. I think I always was amazed by how computers
*  could do things fast. If I wanted to make it an abstract analysis of why it is that I saw some
*  power in the computer. Because if the computer can do things so many times faster than humans,
*  where the hard part is telling the computer what to do and how to do it. If you can master that
*  asking the computer what to do, then you could conceivably achieve more things.
*  And those contests I was in, those were the opposite in some sense of making a complete
*  product. Like a game is a product. Those contests were effectively write a function to do something
*  extremely efficiently. And if you are able to do that, then you can unlock more of the power of
*  the computer. But also doing it quickly. There's a time element from the human perspective to be
*  able to program quickly. There's something nice, so there's almost like an athletics component
*  to where you're almost like an athlete seeking optimal performance as a human being trying to
*  write these programs. And at the same time it's kind of art because the best way to write a program
*  quickly is to write a simple program. You still have a damn good solution. So it's not necessary
*  you have to type fast. You have to think through a really clean, beautiful solution. I mean,
*  what do you think is the use of those programming competitions? Do you think they're
*  ultimately something you would recommend for students, for people interested in programming,
*  or people interested in building stuff? Yes, I think so because especially with the work that
*  I've been doing nowadays, even trying to control COVID, something that was very helpful from day
*  one was understanding that the kinds of computations we would want to do, we could conceivably do on
*  like a four core cloud machine on Amazon Web Services out to a population which might have
*  hundreds of thousands or millions of people. The reason why that was important to have that back
*  of the envelope calculation with efficient algorithms is because if we couldn't do that,
*  then we would bankrupt ourselves before we could get to a big enough scale. If you think about how
*  you grow anything from small to big, if in order to grow it from small to big, you also already need
*  10,000 cloud servers, you'll never get to big. And also the nice thing about programming competitions
*  is that you actually build a thing that works. So you finish it. There's a completion thing and you
*  realize, I think there's a magic to it, where you realize that it's not so hard to build something
*  that works, to have a system that successfully takes in inputs and produces outputs and solves
*  a difficult problem and that directly transfers to building a startup essentially that can help
*  some aspect of this world as long as it's mostly based on software engineering.
*  Things get really tricky when you have to manufacture stuff. That's why people like
*  Elon Musk are so impressive that it's not just software. Tesla Autopilot is not just software,
*  it's like you have to actually have factories that build cars and there's like a million components
*  involved in the machinery required to assemble those cars and so on. But in software, one person
*  can change the world, which is incredible. But on the mathematics side, if you look back,
*  or maybe today, what made you fall in love with mathematics?
*  For me, I think I've always been very attracted to challenge, as I already indicated with writing
*  the program. I guess if I see something that's hard or supposed to be impossible, sometimes I
*  say maybe I want to see if I can pull that off. And with the mathematics, the math competitions
*  presented problems that were hard, that I didn't know how to start, but for which I could
*  conceivably try to learn how to solve them. There are other things that are hard called
*  get something to Mars, get people to Mars. And I still don't think that I'm able to solve that
*  problem. On the other hand, the math problems struck me as things which are hard and with
*  significant amount of extra work, I could figure it out. And maybe they would actually even be
*  useful. That mathematical skill is the core of lots of other things.
*  That's really interesting. Maybe you could speak to that because a lot of people say that math is
*  hard as a kind of negative statement. It always seemed to me a little bit like that's kind of a
*  positive statement, that all things that are worth having in this world, they're hard. I mean,
*  everything that people think about that they would love to do, whether it's sports, whether it's art,
*  music, and all the sciences, they're going to be hard if you want to do something special.
*  So is there something you could say to that idea that math is hard?
*  Should it be made easy or should it be hard?
*  So I think maybe I want to dig in a little bit onto this hard part and say, I think the interesting
*  thing about the math is that you can see a question that you didn't know how to start doing it before.
*  And over a course of thinking about it, you can come up with a way to solve it. And so you can move
*  from a state of not being able to do something to a state of being able to do something, where you
*  help to take yourself through that instead of somebody else spoon feeding you that technique.
*  So actually here I'm already digging into maybe part of my teaching philosophy also, which is that
*  I actually don't want to ever just tell somebody, here's how you do something.
*  I actually prefer to say, here's an interesting question. I know you don't quite know how to do it.
*  Do you have any ideas? I'm actually explaining another way that you could try to do teaching.
*  And I'm contrasting this to a method of watch me do this, now practice it 20 times.
*  I'm trying to say a lot of people consider math to be hard because maybe they can't remember
*  all of the methods that were taught. But for me, I look at the hardness and I don't think of it as
*  a memory hardness. I think of it as a, can you invent something, hardness? And I think that if
*  we can teach more people how to do that art of invention in a pure cognitive way, not as hard as
*  the actual hardware stuff, right? But like in terms of the concepts and the thoughts and the
*  mathematics, teaching people how to invent, then suddenly actually they might not even find math to
*  be that tiresome-ness hard anymore. But that rewarding-ness hard of, I have the capability
*  of looking at something which I don't know what to do and coming up with how to do it.
*  I actually think we should be doing that, giving people that capability.
*  So hard in the same way that invention is hard, that is ultimately rewarding. So maybe you can
*  dig in that a little bit longer, which is, do you see basically the way to teach math
*  is to present a problem and to give a person a chance to try to invent a solution
*  without, with minimal modern information first? Is that basically, how do you build that muscle
*  of invention in a student? Yes. So the way that, I guess I have two different sort of ways that I
*  try to teach. Actually, one of them is in fact this semester because all my classes were remotely
*  delivered. I even threw them all onto my YouTube channel. So you can see how I teach at Carnegie
*  Mellon. But I'd often say, hey everyone, let's try to do this. Any ideas? And that actually changes
*  my role as a professor from a person who shows up for class with a script of what I want to talk
*  through. I actually don't have a script. The way I show up for class is there's something that we
*  want to learn how to do and we're going to do it by improv. I'm talking about the same method
*  as improv comedy, which is where you tell me some ideas and I'll try to yes and them.
*  Then together we're going to come up with a proof of this concept where you were deeply involved
*  in creating the proof. Actually, every time I teach the class, we do every proof slightly
*  differently because it's based on how the students came up with it. That's how I do it when I'm in
*  person. I also have another line of courses that we make that is delivered online. Those things are
*  where I can't do it live, but the teaching method became also similar. It was just,
*  here's an interesting question. I know it's out of reach. Why don't you think about it?
*  And then automatic hints, we feed automatically hints through the internet to go and let the
*  person try to invent. So that's like a more rigorous prodding of invention. But you did mention
*  disease and COVID and you've been doing some very interesting stuff from a mathematical,
*  but also software engineering angle of coming up with ideas. It's back to the, I see a problem,
*  I think I can help. So you stepped into this world. Can you tell me about your work there
*  under the flag of Novid and both the software and the technical details of how the thing works?
*  Sure, sure. So first I want to make sure that I say this is actually team effort. I happen to be
*  the one speaking, but there's no way this would exist without an incredible team of people who
*  inspire me every day to work on this, but I'll speak on behalf of them. So the idea was indeed
*  that we stepped forward in March of last year when the world started to become, our part of the world
*  started to become, our part meaning the United States started to become paralyzed by COVID.
*  The shutdown started to happen. And at that time it started as a figment of an idea, which was
*  network theory, which is the area of math that I work in, could potentially be combined with
*  smartphones and some kind of health information anonymized. Exactly how? We didn't know yet. We
*  tried to crystallize it. And many months into this work, we ended up accidentally discovering
*  a new way to control diseases, which is now what is the main impetus of all of this work,
*  is to take this idea and polish it and hopefully have it be useful not only now,
*  but for future pandemics. The idea is really simple to describe. Actually, my main thing in
*  the world is I come up with obvious observations. So I'll explain it now. Einstein did the same
*  thing and he wrote a few short papers. But so the idea is like this. If we describe how usually
*  people control disease for a lot of history, it was that you would find out who was sick,
*  you'd find out who they've been around, and you try to remove all of those people from society
*  against their will. Now that's the problem. The against their will part gives you the wrong kind
*  of a feedback loop, which makes it hard to control the disease because then the people
*  you're trying to control keep getting other people sick. You can see already how I'm thinking and
*  talking about this feedback loops. This is actually related to something you said earlier
*  about even like how skyscrapers stay in the air. The whole point is control theory. You actually
*  want to, or even how an airplane stays, you need to have control loops which are feedbacking in
*  the right way. And what we observed was that the feedback control loop for controlling disease
*  by asking people to be removed from society against their will was not working. It was running
*  against human incentives and you suddenly are trying to control seven billion, eight billion
*  people in ways that they don't individually want to necessarily do. So here's the idea.
*  And this is inspired by the fact that at the core of our team were user experience designers.
*  That's actually the, in fact, the first thing I knew we needed when we started was to bring user
*  experience at the core. Okay. But so the idea was suppose there was a pent up,
*  suppose hypothetically there was a pandemic. What would you want? You would want a way to be able
*  to live your life as much as possible and avoid getting sick. Can we make an app to help you avoid
*  getting sick? Notice how I've just articulated the problem. It is not, can we make an app so that
*  after you are around somebody who's sick, you can be removed from society? It's can we make an app
*  so that you can avoid getting sick? That would run a positive, I don't know if I want to call it
*  positive or negative, but it would run a good feedback loop. Okay. So then how would you do this?
*  The only problem is that you don't know who's sick because especially with this disease,
*  if I see somebody who looks perfectly healthy, the disease spreads two days before you have any
*  symptoms. And so it's actually not possible. That's where the network theory comes in.
*  You caught it from someone. What if we change the paradigm and we said, whenever there's a sickness,
*  tell everybody how many physical relationships separate them from the sickness. That is the
*  trivial idea we added. The trivial idea was the distance between you and a disease is not measured
*  in feet or seconds. It's measured in terms of how many close physical relationships separate you,
*  like these six degrees of separation, like LinkedIn. Simple idea. What if we told everyone
*  that? It turns out that actually unlocks some interesting behavioral feedback loops, which,
*  for example, let me now jump to a non-COVID example to show why this maybe could be useful.
*  Actually, we think it could be quite useful. Imagine there was Ebola or some hemorrhagic fever.
*  Imagine it spread through contact, through the air, in fact. Pretend. That's a disastrous disease.
*  It has high fatality rate. And as you die, you're bleeding out of every orifice.
*  Yeah, not pleasant.
*  Not pleasant. So the question is, suppose that such a disease broke,
*  who would want to install an app that would tell them how many relationships away from them
*  this disease had struck? A lot of people.
*  A lot of people. In fact, I don't want to say almost everyone. That's a very strong statement,
*  but a very large number of people.
*  That's fascinating framing. The more deadly and transmissible the disease,
*  the stronger the incentive to install it in a positive sense, in the good feedback loop sense.
*  That's a really good example. It's a really good way to frame it because with COVID,
*  it was not as deadly as potential pandemics could have been, viruses could have been. So
*  it's sometimes muddled with how we think about it. But yeah, this is a really good framing.
*  If the virus was a lot more deadly, you want to create a system that has a set of additional
*  incentives. You want to create a system that has a set of incentives that
*  it quickly expresses a population where everybody is using it and is contributing in a positive way
*  to the system. Exactly. And actually, that point you just made, I don't take credit for that
*  observation. There was another person I talked to who pointed out that it's very interesting that
*  this feedback loop is even more effective when the disease is worse. And that's actually not a bad
*  characteristic to have in your feedback loop if you're trying to help civilization keep running.
*  Yeah, it's a really, it's dynamic. Like people figure out, they dynamically figure out how bad
*  the disease is. The more it spreads and the deadlier it is as the people observe it,
*  as long as the spread of information, like semantic information, natural language information,
*  is closely aligned with the reality of the disease, which is a whole nother conversation.
*  We, that's, we might, maybe we'll chat about that, how we sort of make sure there's not
*  misinformation, why there's accurate information. But that aside, okay, so this is a really nice
*  property. Right. And just going on on that, actually just talking more about what that could do and why
*  we're so excited about it. It's that not only would people want to install it, what would they do? If
*  you start to see that this disease is getting closer and closer, we surveyed informally people,
*  but they said, as we saw it getting closer, we would hide, we would try to not have contacts.
*  But now you notice what this has just achieved. The whole goal on this whole exercise was you got
*  the people who might be sick and you got everyone else, set A and set B. Set A is the people who
*  might be sick, set B is everyone else. And for the entirety of the past, contact tracing approaches,
*  you try to get set A to do things that might not be to their liking or their will, because that's
*  removing them from society. We found out that there's two ways to separate set A from set B.
*  You can also let the people at set B, at the fringe of set A, attempt to remove themselves
*  from this interface. It's just, it's the symmetry of A and B separation. Everyone was looking at A,
*  we look at B and suddenly B is in their incentive to do so.
*  Beautiful. So there's a virus that jumps from human to human. So there's a network,
*  sometimes called graph, of the spread of a virus. It hops from person to person to person in person.
*  And each one of us individuals are sitting or plopped into that network. We have close friends
*  and relations and so on. It's kind of fascinating to actually think about this network. And we can
*  maybe talk about the shapes of this kind of network. I was trying to think exactly this,
*  like how many people do I, well, so I'm kind of an introvert, not kind of, I'm very much an introvert.
*  But so can I be explicit about the kind of people I meet in regular life? Say when it was completely
*  opened up, there's no pandemic. There is a kind of network of, and there's maybe
*  in the graph, the erratic sense, there's some weights or something about how
*  close that relationship is in terms of the frequency of visits, the duration of visits,
*  and all of those kinds of things. So you're saying we might want to be, to create on top of that
*  network a spread of information to let you know as the virus travels through this network, how
*  close is it getting to you? And the number of hops away it is on that network is really powerful
*  information that creates a positive feedback loop where you can act essentially anonymously
*  and on your own. Like nobody's telling you what to do, which is really important, is decentralized.
*  And not whatever the opposite of authoritarian is. But you get to sort of the American way,
*  you get to choose to do it yourself, you have the freedom to do it yourself, and you're incentivized
*  to do it, and you're most likely going to do it to protect yourself against you getting the disease
*  as the closer it gets to you based on the information that you have. But can you maybe
*  elaborate, first of all, brilliant, whenever I saw the thing you're working on, so forget for COVID,
*  this is of course really relevant for COVID, but it's also probably relevant for future
*  disease as well. So that was the thing I'm nervous about, like if this whole, if our society shut
*  down because of COVID, like what the heck is going to happen when there's a much deadlier disease?
*  Like this, this is disappointing. The whole time, 2020, the whole time I'm just sitting like this,
*  like is the incompetence of everybody except the people developing vaccines. The biologists are the
*  only ones that got their stuff together. But in terms of institutions and all that kind of stuff,
*  it's just been terrible. But this is exactly the power of information and the power of information
*  that doesn't limit personal freedom. So your idea is brilliant. Okay. Mathematically, can you maybe
*  elaborate what are we talking about? Like how do you actually make that work? What's involved?
*  Sure. First, I'm going to reply to something you said about the freedom inside this, because
*  actually that was the idea. The idea is this is game theory, right? And effectively what we did is
*  analogous to free market economy as opposed to central planning. If you just line up the set of
*  incentives correctly so that people have in their purely selfish behavior are contributing to the
*  optimization of the global function, that's it. And the point of what we do, I guess in mathematics,
*  is we try to explore the search space to go and find out as many possibilities as there are. And
*  in this case, it's an applied search space. That's why the inputs from design, user experience
*  design, and actual people are important. But you asked about, I guess, the mathematical or
*  the technical things underpinning it. So I think the first thing I'll say is we wanted to make this
*  thing not require your personal information. And so in order to do that, what gave me the confidence
*  to lead our team to run at the beginning is we saw that this could be done without using GPS
*  information. So technically what's going on is if two smartphones, it's a smartphone app,
*  if two smartphones have this thing installed, they just communicate with each other by Bluetooth
*  to go and find out how far, they can detect nearby things by Bluetooth. And then they can find out
*  that these two phones were approximately such and such distance apart. And that kind of relative
*  proximity information is enough to construct this big network. Okay. So the physical network
*  is constructed based on proximity that's through Bluetooth and you don't have to specify
*  your exact location. It's the proximity. I'm not using the Pythagorean theorem, basically.
*  I mean, if I just knew the GPS coordinates, we could use the Pythagorean theorem too. Sorry,
*  that's just how I call it. Distance formula, whatever you want to call it.
*  Yeah. So we're not doing the old Pythagorean based violation of privacy. Okay.
*  So is that enough to give you enough information about physical connection to another human being?
*  Is there a time element there? Okay. That sounds like a really strong,
*  like low hanging fruit. Like if you have that, you could probably go really, really far.
*  My natural question is, is there extra information you can add on top of that?
*  Like the duration of the physical proximity? So first of all, we actually do estimate the
*  duration, but the way we estimate the duration is like how a movie is filmed in the sense that
*  every so often, every few minutes we check what's nearby. It's like how a movie is filmed. You take
*  lots of snapshots. So there's no way in a battery efficient way to really keep track of that
*  proximity. However, fortunately we're using probability. The fact is the paradigm that we're
*  using is it's not super important if you run into that person only for 10 minutes at the grocery
*  store. If that's a stranger that you run into 10 minutes in this grocery store, that's not going
*  to be relevant for our paradigm because our paradigm is not telling you who were you around
*  before and might therefore have gotten infected by already. Ours is about predicting the future.
*  We changed from, I mean the standard paradigm was what already happened, quick damage control.
*  Ours is predict the future. If you run into that person once in the grocery store today and never
*  see them again, it's irrelevant for predicting the future. And therefore for ours, what really
*  matters is the many hours around the other person, at which point if you're scanning every five to
*  eight minutes. That's going to come out in the probably like statistically speaking, it's going
*  to come out as a strong relationship and a person in the grocery store is going to wash out. That's
*  not an important physical relationship. I mean this is brilliant. How difficult is it to make
*  work? So you said one there's a mathematical component that we just kind of talked about
*  and then there's the user experience component. So how difficult is it to go just like you built
*  the video game Alien Attack from zero to completion? What's involved? How difficult is it?
*  So I'm going to answer that question in terms of building the product, but then I'm also going to
*  acknowledge that just having an app doesn't make it useful because that's actually maybe the easy
*  part. If you know what I mean, there's like all of this stuff about rollout adoption and awareness,
*  but let's focus on the app part first. So that's again why I said the team is incredible. So we
*  have a bunch of people who, let's just say that the technology that we use to make it is not the
*  standard way you make an app. If you think about a standard iOS app or Android app, those are a
*  user interface that contacts a web server and sends some information back and forth. We're doing some
*  stuff that has to hook into the operating system of saying let's go use Bluetooth for something it
*  wasn't really meant for. So there's that part. By the way, what is the app called? Oh it's called
*  Novid, COVID with an N. Very nice. So you have to hook into Bluetooth. You're saying you have to do
*  that beyond the permissions that are like at the very surface level provided on the phone? Well,
*  I don't want to call them permissions. I just want to say that's not what you usually do with
*  Bluetooth. Usually with Bluetooth you say do I have headphones nearby? Yes. Okay, I'm done. You
*  don't go and say do I have headphones nearby or do I have another phone nearby which is doing something
*  and then keep asking that same question. Right? So this is actually not easy and I mean there were
*  some parts of it which actually a lot of people had tried unsuccessfully. Actually it's known that
*  for example the UK was trying to do something similar and the problem they ran into was when
*  you program things on iOS, iOS is very good at making it hard to do things in the background
*  and so there was quite a lot of effort required to go and make this thing work. So the whole point
*  this thing would run in the background and iOS, I mean most Android probably as well, right? But
*  yeah iOS certainly makes it difficult for something to run in the background especially when it's to
*  eating up your battery, right? Ah well we wanted to make sure we didn't eat up the battery so that
*  one we can we actually are very proud of the fact that ours uses very little battery
*  actually even if compared to Apple's own system. So beautiful. So what else is required to make
*  this thing work? Right so the the key was that you had to do a significant amount of work on the
*  actual mobile app development which fortunately the team that we brought was this kind of general
*  thinkers where we would dig in deep into the operating system documentation and the API
*  libraries so we got that working. But there's another angle which is you also need the servers
*  to be able to compute fast enough which is tying back to this old school computer programming
*  competitions and math olympiads. In fact our team that was working on the algorithm and backend side
*  included several people who had been in these competitions from before which I happen to know
*  because I do coach the team for the math. And so we were able to bring people in to build servers
*  a server infrastructure in C++ actually so that we could support significant numbers of people
*  without needing tons of servers. Is there some distributed algorithms working here or you basically
*  have to keep in the same place the entire graph as it as it builds because especially the more and
*  more people use it the bigger the bigger the graph gets. I mean this is very difficult the scaling
*  problem right? Ah so that's actually why this computer algorithm competition stuff was handy
*  it's because there are only about seven to eight giga people in the world. Yeah that's not that
*  many so if you can make your algorithms linear time or almost linear time a computer operates
*  in gigahertz. I only need to do one run one one recalculation every hour in terms of telling
*  people how far away these dangers are. Yes. So I suddenly have 3600 seconds and my CPU cores are
*  running in gigahertz and at most they're eight giga people. Well you're skipping over the fact
*  that there's n squared potential connections between people so how do you get around the fact that
*  you know that we you know the potential set of relationship any one of us could have is
*  eight billion so it's eight billion times squared. That's the potential amount of data you have to be
*  storing and computing over and constantly updating. So the way we dealt with that is we actually
*  expect that the typical network is very sparse the technical term sparse would mean that the
*  average degree or the average number of connections that a person has is going to be at most like
*  a hundred strong connections that you care about. If you think of it almost in terms of the heavy
*  hitters actually in most people's lives a hundred if we just kept track of their top hundred
*  interactions that's probably most of the signal. Yeah yeah I'm saddened to think that I might not
*  be even in a double digits but oh I was intentionally giving a crazy number to account for college
*  students. You call oh those are the who you call in the heavy hitters the people who are like the
*  social butterflies yeah yeah yeah I need to uh I'd love to know that information about myself by the
*  way the that do you do you expose the graph like how many like about yourself how many connections
*  you have? We do expose to each person how many direct connections they have that's great but
*  for privacy purposes we don't tell anybody who their connections like how their connections are
*  interconnected yes gotcha but at the same time we do expose also to everyone an interesting chart
*  that says here's how many people you have that you're connected to directly here's how many at
*  distance two meaning via people and then here's how many at distance three and the reason we do
*  that is that actually ends up being a dynamic that also boosts adoption it drives another feedback
*  loop the reason is because we saw actually when we deployed this in some universities that when
*  people see on their app that they are indirectly connected to hundreds or thousands of other people
*  they get excited and they tell other people hey let's download this app yeah but you know we also
*  saw in those examples especially looking at the screenshots people gave that is hit as soon as the
*  typical person has two or three other direct connections on the system because that means
*  that our app has reached a virality or not of two to three the key is we were making a viral app to
*  fight a virus spreading on the same network that the virus spreads out so you're trying to out
*  virus that's right that's exactly right okay great what have you learned from this whole experience
*  in terms of let's say for covid but for future pandemics as well is it possible to
*  use the power information here of networked information as a virus spreads and travels
*  in order to basically keep the society open is it possible for for people to protect themselves with
*  this information or do you still have to have most like in this overarching policy of everybody
*  should stay at home all that kind of thing we are trying to answer that question right now so the
*  answer is we don't know yet but that's actually why we're very happy that now the idea has started
*  to become become more widely known and we're already starting to collaborate with epidemiologists
*  again i'm a math i'm just a mathematician right and a mathematician should not be the person who
*  is telling everybody this will definitely work but because of the potential power of this approach
*  especially the potential power of this being an end game for covid we have gotten the interest of
*  real researchers and we're now working together to try to actually understand the answer to that
*  question because you see there's a theory so what what i can share is the mathematics of here's why
*  there's some hope that this would work and that's because i'm talking about end game now end game
*  means you have very few cases but everywhere we're always thinking once there's few cases then does
*  that mean we now open up once you open up in the past then the cases go up again until you have to
*  lock down again and now when we talk about the dynamic process that makes it's guaranteeing you
*  always have cases until you have the great vaccines which is you know we both got vaccinated this is
*  this is good but at the same time why i'm thinking this is still important is because we know that
*  many vaccine makers have said they're preparing for the next dose next year and if we have a
*  perpetual thing where you just always need a new vaccine every year it could actually be beneficial
*  to make sure we have as many other techniques as possible for parts of the world that can't afford
*  for example that kind of distribution yeah so actually no matter no matter how deadly the
*  virus is no matter how many things whether you have a vaccine or not it's still useful to be
*  having this information yes is to stay home or not depending on how risk like i'm a big fan just
*  like you said of having the freedom for you to decide how risk-averse you want to be right and
*  depending on your own conditions but also on the state of like what you just how dangerously you
*  like to live so i think that actually makes a lot of sense and i also think that since we're when
*  you think of disease spreading it spreads in aggregate in the sense that if there are some
*  people who maybe are more risk tolerant because of other things in their life well there might
*  also be other people who are less risk tolerance and then those people decide to isolate but what
*  matters is in the aggregate that this are not of the infection spreading drops below one and so the
*  key is if you if you can empower people with that power to make that decision you might actually
*  still be able to drive that are not down below one yeah and also this is me talking i is people
*  get a little bit nervous i think with information somehow mapping to privacy violation but i
*  first of all in the approach you're describing that's respecting anonymity
*  but i would love to have information from the very beginning from march and april of last year
*  almost like a map of like where it's risky and where it's not to go and not map based on sort of
*  the exact location of people but where people usually hang out kind of thing just
*  and maybe not necessarily about actual location but just maybe activities like just to have
*  information about what is what is good to do and not you know in terms of like safety is it okay
*  to run outside and not is it okay to go to a restaurant and not i just feel like we're
*  operating the blind and then what you had is a very imperfect signal which is like basically
*  politicians desperately trying to make statements about what is safe and not they don't know what
*  the heck they're doing they have a bunch of smart scientists telling them stuff and the scientists
*  themselves also very important don't always know what they're doing epidemiology is not
*  is is as much an art as a science you're desperately trying to predict the future which
*  nobody can do and then you're trying to speak with some level of authority i mean if i were to
*  criticize scientists they spoke with too much authority it's okay to say i'm not sure but then
*  they think like if i say i'm not sure then there's going to be a distrust what they realize is when
*  you're wrong and you say i'm sure it's going to lead to more distrust so there's this imperfect
*  like just chaotic messy system of people trying to figure out with very little information and
*  what you're proposing is just a huge amount of information and information is power is there
*  challenges with adoption that you see in the future here so there's maybe we could speak to
*  there's approaches i guess from google there's different people that've tried similar kind of
*  ideas not in you have quite a novel idea actually but speaking the umbrella idea of contact tracing
*  is is there is there something you can comment about why their approaches haven't been fully
*  adopted is there challenges there is there is there reasons why novid might be a better idea
*  moving forward in general just about adoption yeah so first of all i want to say i always have
*  respect for the methods that other people use and so it's good to see the other people have been
*  trying but what we have noticed is that the difference between our value proposition to
*  the user and the value proposition to the user delivered by everything that was made before
*  is that unfortunately the action of installing a standard contact tracing app will then tell you
*  after you've already been exposed to the disease so that you can protect other people from you
*  and what that does to your own direct probability of getting sick if you think about it suppose you
*  were making the decision should i or should i not install one of those apps yeah what does that do
*  to your own probability of getting sick it's close to zero this is the sad thing you're
*  you're speaking to not sad i suppose it's the way of the world is the only incentive there is to
*  just help other people i suppose but a much stronger incentive is is anything that allows
*  you to help yourself yes so what i'm saying is that uh let's just say free market capitalism was
*  not based on altruism i think it's based on if you make a system of incentives so that everybody
*  trying to maximize their own situation somehow contributes to the whole that's a game theoretic
*  solution to a very hard problem and so this is actually basically mechanism design like we've
*  basically come up with a different mechanism different set of incentives which incentivizes
*  the adoption because actually whenever we've been rolling it out usually the first question we ask
*  people like say in the university is do you know what novid does and most of them have read about
*  the other apps and they say oh novid will tell you after you've been around someone so you can
*  quarantine and we have to explain to them actually novid never wants to ask you to quarantine yeah
*  that's not the principle our principle isn't based on that at all we just want to let you know if
*  something is coming close so that you can protect yourself if you want yeah if you want if you want
*  if you want and then the quarantine is like yes in that case if you're quarantining it's because
*  you're shutting the door from the inside if that makes sense yes exactly exactly i mean this is
*  brilliant but so what uh do you think the future looks like for future pandemics what's your plan
*  with novid what's your plan with these set of ideas i am actually still an academic and a
*  researcher so the biggest work i'm working on right now is to try to build as many collaborations
*  with other public health researchers at other universities to actually work on pilot deployments
*  together in various places that's the goal that's actually ongoing work right now and so for example
*  if anyone's watching this and you happen to be a public health researcher and you want to be involved
*  in something like this i'm just going to say i'm still incentive thinking there's something in it
*  for the researchers too this could open up an entire new way of controlling disease that's my
*  hope i mean it might actually be true and people who are involved in figuring out how to make this
*  work well it could actually be good for their careers too i always have to think like if a
*  researcher was getting involved what are they getting out of it oh so you mean like from a
*  research perspective you can uh like publications and sets of ideas about how to from a sort of uh
*  uh network theory perspective understand how we control the spread of a pandemic yes and this what
*  i'm doing right now is this is basically interdisciplinary research where maybe our side
*  is bringing the technology and the network theory and the missing parts are epidemiology and public
*  health expertise and if the two things start to join also because everywhere that you deploy
*  let's just say that the world is different in the philippines as it is in the united states
*  and just the natures of the of the locality would mean that someone like me should not be trying to
*  figure out how to do that but if we can work with the researchers who are based there now suddenly
*  we might come up with a solution that will help scale in parts of the world where they aren't all
*  getting the moderna and phizer vaccines which cost like 20 dollars a pop in the u.s so if they want
*  to participate who do they reach out to oh that would just be us i mean the nova.org website has
*  it has it has a feedback reach out form and actually we are i mean again this is the dna
*  of being a researcher i am actually very excited by the idea that this could contribute knowledge
*  that will outlast all of our generations like all of all of our lifetimes there you go reach out
*  uh to nova nova.org uh what about individual people should they install the app and try it
*  out or is this really geographically restricted oh yeah i didn't come on here to tell everyone
*  to install the app i did not come to tell everyone to install the app because it works best
*  if your local health authority is working with us gotcha there's a reason it's because this is
*  back to the game theory if anyone could just say i'm positive the high school senior prank
*  would be to say that we have a massive outbreak on finals week let's not have final exams so the
*  way that our system works it actually borrows some ideas not borrows we came up with them
*  independently but this idea is similar to what google and apple do which is that if the local
*  health authority is working with this they can for everyone who's positive give them a passcode that
*  expires in a short time so for ours if you're on the app and saying i'm positive you can either
*  just say that and that's called unverified or you can enter in one of these codes that you got from
*  the local health authority so basically for anyone who's watching this it's not that you should just
*  go and download it unless you want to go and look at it that's cool but if you on the other hand if
*  you happen to know anyone at the local health authority which is trying to figure out how to
*  handle covid well then i mean we'd be very happy to also work with you gotcha so the the verified
*  there is really important because you're you're maintaining anonymity and because of that you
*  have to have some source of verification in order to make sure that it's not possible to manipulate
*  because it's ultimately about trust and information and so it could be
*  um verification is really important there so basically individual people should
*  ask their local health authorities to to sign up to contact you
*  i hope this spreads i hope this spreads for future pandemics because i'm really
*  it's the amount the millions of people who are hurt by this i think our response to the virus
*  economically speaking the number of people who lost their dream lost their jobs but also lost
*  their dream entrepreneurs you know jobs often give meaning there's people who financially and
*  psychologically are suffering because of our i'll say incompetent response to the virus
*  across the world but certainly the united states that should be the beacon
*  of uh entrepreneurial hope for the world so
*  i hope that uh we'll be able to respond to these kinds of events much better in the future and
*  this is exactly the right kind of idea and now is the time to do the investment let's step back
*  to the beauty of of mathematics maybe ask the the big silly question first which is uh
*  what do you find beautiful about mathematics i think that being able to look at a complicated
*  problem which looks unsolvable and then to be able to change the perspective to come from a different
*  angle and suddenly see that there's a nice solution i don't mean that every problem in
*  math is supposed to be this way but i think that these reframings and changing of perspectives
*  that cause difficult things to get simplified and crystallized and factored in certain ways
*  is beautiful actually that's related to what we were just talking about with even this fighting
*  pandemics the the crystal idea was just quantify proximity by the number of relationships in the
*  in the physical network instead of just by the feet and meters right it's it's just that if
*  you change that perspective now all of these things follow and so mathematics to me is beautiful
*  in the pure sense just for that yeah it's quite interesting to see a human civilization as a
*  network as a graph and our relationships as kind of edges in that graph and to then do
*  outside of just pandemic do interesting inferences based on that
*  this this is true for like twitter social networks and so on how we expand the kind of things we talk
*  about think about sort of politically if you have this little bubble quote unquote of ideas that you
*  play with it's nice from a recommender system perspective how do you jump out of those bubbles
*  it's really fascinating youtube was working on that twitter is working on that but not always so
*  successfully but there's a lot of interesting work from a mathematical and a psychological
*  sociological perspective there in within those graphs but if we look at the cleanest formulation
*  of that of looking at a problem from a different perspective you're also involved with the
*  international mathematics olympiad which takes small clean problems that are really important
*  problems that are really hard but once you look at them differently can become easy but that little
*  jump of innovation is is is the entire trick so maybe at the high level can you say what is the
*  international mathematical olympiad sure so this is a the competition for people who aren't yet in
*  college math competition which is the most prestigious one in the entire world it's the
*  olympics of mathematics but only for people who aren't yet in college now the kinds of questions
*  that they ask you to do are not computational usually you're not supposed to find that the
*  answer is 42 right instead you're supposed to explain why something is true yes and the
*  the problem is that at the beginning when you look at each of the questions first of all you have
*  four and a half hours to solve three questions and this is one day and then you have a second day
*  which is four and a half hours three questions but when you look at the questions they're all
*  asking you explain why the following thing is true which you've never seen before and by the way even
*  though there are six questions if you solve any one of them you're a genius and you get an honorable
*  mention so this is this is hard to accept really hard problem so what about is it one person is it
*  a team ah so it's each country can send six people and the score of the country is actually
*  unofficial there's not an official country versus country system although everyone just adds up the
*  point scores of the six people and they say well now which country stacked up where yeah so maybe
*  as a side comment i should say that there's a bunch of countries including the former soviet
*  union and russia where i grew up where this is one of the most important competitions that the
*  country participates in like it was a source of pride for a lot of the country you look at the
*  olympic sports like uh wrestling weightlifting there's certain sports and hockey
*  that russia and the soviet union truly took pride in and actually the mathematical olympiad
*  it was one of them for many years it's still one of them and that's kind of fascinating we don't
*  think about it this way in the united states maybe you can correct me if i'm wrong but
*  it's not nearly as popular in the united states in terms of its integration into the culture
*  into uh just basic conversation into the pride like you know if you win an olympic gold medal
*  or if you win the super bowl you can walk around proud i think that was the case with the mathematical
*  olympiad in russia not not as much the case in the united states i think so i just want to give
*  that a little aside because beating anybody from russia from the eastern republic or from china is
*  very very difficult they're like if i remember correctly you know there's people this was a
*  multi-year training process they train hard and this is this is everything that they're focused
*  on my uh my dad was was uh was a participant and i said it's i mean it's uh it's as serious as
*  olympic sports you think about like gymnastics like young athletes participating gymnastics
*  is as serious as that if not more serious so i just want to give that a little bit of context
*  because we're talking about serious high level math athletics almost here yeah and actually i
*  also think that it made sense uh from the soviet union's perspective because if you look at what
*  these people do eventually even though let's look at the ussr's olympic international math olympiad
*  record even though they i say even though they won a lot of awards at the high school thing
*  many of them went on to do incredible things in research mathematics or research other things
*  and that's showing the generalization generalizability of what they were working on
*  because ultimately we're just playing with ideas of how to prove things and if you get pretty good
*  at inventing creative ways to turn problems apart split them apart observe neat ways to
*  turn messy things into simple crystals well if you're going to try to solve any real problem
*  in the real world that could be a really handy tool too so i don't think it was a bad investment
*  i think it clearly worked well for soviet union yeah so this this is interesting people sometimes
*  ask me you know you go up and under communism you know was there anything good about communism
*  and it's difficult for me to talk about it because it's not uh communism is one of those things
*  that's looked down on like without in absolutist terms currently but you could still in my
*  perspective talk about the actual forget communism or whatever the actual term is but you know certain
*  ways that the society function that we can learn lessons from and one of the things in the soviet
*  union that was highly prized is knowledge not even knowledge it's wisdom and the skill of invention
*  of innovation at a young age so we're not talking about a selection process where you pick the best
*  students in the school to do the mathematics or to read literature it's like everybody did it
*  everybody it was almost treated as if anyone could be the next einstein anybody could be the next
*  i don't know hemmingway james joys and so you're forcing an education on the populace and a rigorous
*  deep education like as opposed to kind of like oh we want to make sure we um we teach to the
*  weakest student in the class which american systems can sometimes do because we don't want
*  to leave anyone behind the the russian system was anyone can be the strongest student and we're
*  going to teach you the strongest student and we're going to just to pretend or force everybody even
*  the weakest student to be strong and what that results in it's obviously this is what people
*  talk about is a huge amount of pressure like it's psychologically very difficult this is why
*  people struggle when they go to mit this very competitive environment it can be very psychologically
*  difficult but at the same time it's bringing out the best out of people and that mathematics was
*  certainly one of those things and exactly what you're saying which kind of clicked with me just
*  now as opposed to kind of spelling bee in the united states which i guess you spell i'm horrible
*  at this but it's a competition about spelling which i'm not sure but you could argue it doesn't
*  generalize well to the future skills mathematics especially this kind of mathematics is essentially
*  formalized competition of invention of uh of creating new ideas and that generalizes really
*  really well so that's that's quite brilliantly put i didn't really think about that so this is not
*  just about the competition this is about developing minds that will come come to do some incredible
*  stuff in the future yeah actually i want to respond to a couple of things there the first one is one
*  which is this notion of whether or not that is possible in a non-authoritarian regime
*  i think it is and that's actually why i spent some of my efforts before the covet thing actually
*  trying to work towards there the reason is because if you think about it let's say in america lots of
*  people are pretty serious about training very hard for football or baseball or basketball basketball
*  is very very accessible but lots of people are doing that why well actually i think that what this
*  what what what was going on with the authoritarian thing was at least the message that was universally
*  sent was being a good thinker and a creator of ideas is a good thing yes exactly there's no reason
*  why that message can't be sent everywhere and i think it actually should be so that's the first
*  thing the second thing is what you you commented about this thing about um you know the generalizable
*  skill and what what could people do with olympiads afterwards so that's actually my interest in the
*  whole thing uh i don't i mean i i don't just coach students how to do problems in fact i'm not even
*  the best person for that i'm not the best at solving these problems uh there are other people
*  who are much better at making problems and teaching people how to solve problems in fact when i was
*  when the mathematical association of america which is the group which is in charge of the u.s
*  participation in these olympiads when they were deciding whether or not to put me in back in 2013
*  as the head coach i had a conversation with their executive director where i commented that we might
*  do worse because my position was i don't i mean i actually didn't want to focus on winning i said
*  if you're going to let me work with 60 very strong minds as picked through this system because the
*  coach works with these gets to run a camp for these students i said i'm actually not going to
*  define my success in terms of winning this contest i said i wanted to maximize the number of the
*  students that i read about in the new york times in 20 years oh yeah and the executive director of
*  the mathematical association of america was fully in support of this because that's also how their
*  philosophy is so in america the way we run this is we're actually not just training to win even
*  though the students are very good and they can win anyway one reason for example i went and even did
*  the covid thing involving quite a few of them is so that hopefully some of them get ideas because
*  in 20 30 years i won't have the energy or the insight to solve problems we'll have another
*  catastrophe and hopefully some of these people will step up and do it and ultimately have that
*  long-term impact i wonder if this is scalable to because that's such a great metric for education
*  not how to get an a on the test but how to have how to be on the cover of new york times
*  for inventing something new and do you think that's generalizable to education beyond just
*  this particular olympia like it's even you're saying this feels like a rare statement almost
*  like a radical statement as a goal for education so actually the way i teach my classes at carnegie
*  melon which i will admit right away is not equivalent to the average in the world but
*  it's already not it's already not just the top 60 in the country as picked by something
*  let me just explain i have exams in my class which are 90 of the great so the exams are the
*  whole thing or most of the whole thing and the way that i let students prepare for the exams is i
*  show them all the problems i've ever given on the previous exams and the whole the exam that they
*  will take is open notes they can take all the notes they want on the previous problems
*  and the guarantee is that the exam problems this time will have no overlap with anything you've
*  seen me give in the past as well as no overlap with anything i taught in the class so the entire
*  exam is invention wow but that's how i go right my point is i have explained to people when i teach
*  you i don't want you to have remembered a method i showed you i want you to have learned enough
*  about this area that if you face a new question which i came up with the night before by thinking
*  about like what could i ask that i have never asked before oh that's cute i wonder what the
*  answer is aha that's an exam problem that's exactly what i do before the exam and then that's what i
*  want them to learn yeah and the first exam usually people have a rough time because it's like what
*  what kind of crazy class is this the professor doesn't teach you anything for the exam but then
*  by the second or third and by the time they finish the class they have learned how to solve
*  anything in the area how to invent how to invent in that area yeah can we uh walk back to the the
*  the mathematical olympia yes what's the scoring and format like uh and also what does it take to win
*  so the way it works is that each of the six students uh do the problems and there are six
*  problems all the problems are equally weighted so each one's worth seven points that means that
*  your maximum score is six problems times seven points which is the nice number of 42 and now the
*  way that they're scored by the way is there's partial credit so the question is asking you
*  explain why this weird fact is true okay if you explain why you get seven points if you make
*  minor mistake maybe you get six points but if you don't succeed in explaining why but you explain
*  other true fact which is along the way of proving it then you get partial credit and and actually
*  now this is tricky because how do you score such a thing it's not like it was the answer was 72
*  and you wrote 71 and it's close right the answer is 72 and you wrote 36 oh but that's pretty close
*  because you were you know you that maybe you're just off by the way they're not numerical anyway
*  but i'm just giving some numerical analog to the way the scoring might work they are all essays
*  and that's where i guess i have some role as well as some other people who helped me in the us
*  delegation for coaches we actually debate with the country which is organizing it the country
*  which is organizing the olympiad brings about 50 people to help judge the written solutions
*  and you you know you schedule these half-hour appointments where the delegation from one country
*  sits down at a table like this opposite side is two or three people from the host country
*  and they're just looking over these exam papers saying well how many points is this worth based
*  on some rubric that has been designed and this is a negotiation process where we're not we're
*  not trying to bargain and get the best score we can in fact sometimes we go to this table and we
*  will say we think we want less than what you gave us this is how this is how our this these are our
*  principles if you give us too much we say no you gave us too much we do that however the reason why
*  this is an interesting process is because if you can imagine every country which is participating
*  has its own language and so if you're trying to grade the mongolian scripts and they're written
*  in mongolian now if you don't read mongolian which most people don't then the the coaches are
*  explaining to you this is what the student has written it's actually quite interesting process
*  it's almost like a jury yes you have you have in the american legal system you have a jury
*  that where they're deliberating but unlike a jury there's the members of the jury speaking
*  different languages sometimes yes fascinating but i mean it's it's hard to know what to do
*  because it's probably really really competitive but your sense is that ultimately people
*  like how do you prevent manipulation here right well we just hope that it's not happening
*  so so we write in english therefore everything that the u.s. does everyone can look at so it's
*  a it's very hard it's very hard for you to manipulate we don't manipulate we only hope
*  that other people aren't but at the same time as you see our philosophy was we want to use
*  this as a way to develop general talent and although we do this for the six people who go
*  to the international math olympiad we really want that everyone at any touch at any stage of
*  this process gets some skills that can help to contribute more later so i don't know if you can
*  uh say something insightful to this question but what do you think makes a really hard math problem
*  on on this olympiad maybe in the courses you teach or in general what makes for a hard problem
*  you've seen i'm sure a lot of really difficult problems what makes a hard math problem
*  so i could quantify it by the number of leaps of insight of changes of perspective that are along
*  the way and here's why it's this is like a very theoretical computer science bit of looking at it
*  okay it's the it's that each reframing of the problem and using of some tool i actually call
*  that a leap of insight when you say oh wow now i see i should kind of put these plugs into those
*  sockets like so yes and suddenly i get to use that machine oh but i'm not done yet now i need
*  to do it again each such step is a large possible large fan out in the search space the number of
*  these tells you the exponent the base of the exponent is like how big how many different
*  possibilities you could try and that's that's actually why like if you have a three insight
*  problem that is not three times as hard as a one insight problem because after you've made the one
*  insight it's not clear that that was the right track necessarily well unless you're still a
*  branching of possibly yeah
*  you're saying there's problems like on the math olympia that requires more than one insight yes
*  those are the hard ones and also i can tell you how how you can tell so this is how i also taught
*  myself math when i was in college so in if you are taking a not taught myself i was taking classes
*  of course but i was trying to read the textbook and i found out i was very bad at reading math
*  textbooks a math textbook has a long page of stuff that is all true which after you read the page you
*  have no idea what you just read yeah this is just a good summary of math textbook okay yeah because
*  it's it's not clear why anything was done that way and yes everything is true but how the heck
*  did anyone think of that so the way that i taught myself math eventually was the way i read a math
*  textbook is i would look at the theorem statement i would look at the length of the proof and then
*  i would close the book and attempt to reprove it myself yeah now that's brilliant the length of the
*  proof is telling you the number of insights because the length of the proof is linear in the number of
*  insights each insight takes space yeah and if i know that it's a short proof i know that there's
*  only one insight so when i'm doing my own way of solving the problem like finding the proof i quit
*  if i'm if i have to do too many plugins it's equivalent to a math contest in a math contest
*  look is it problem one two or three that tells me how many insights there are this is exactly
*  what i did that's brilliant linear in the number i don't know i think um well it's possible that
*  that's true approximately approximately yeah just i don't know be uh somebody out there is going to
*  try to formally prove this oh no i mean you're right there are cases where maybe it's not quite
*  linear but in general well some of it's notation too and some of it is uh style and all those kinds
*  of things but within a textbook within the same book within the same book with the same within the
*  same book on the same subject yeah this is what i was using that's hilarious because you know if
*  it's a two-page proof you just know this is going to be insane right that's the uh that's the scary
*  thing about insights you look like andrew wiles working on the fermat's last theorem
*  is you don't know something seems like a good idea and you have that idea and it feels like
*  this is a leap like a totally new way to see it but you have no idea if it's at all useful
*  uh even if you think it's correct you have no idea if this is like going to go down a path that's
*  completely kind of productive or not productive at all that's this that's a crappy thing about
*  invention is um like i have i'm sure you do i have a lot of really good ideas every single day
*  but like and then i'll go inside my head along them along that little trajectory
*  but it could be just a total waste and it's that i that you know what that feels like it just feels
*  like patience is required not to get excited at any one thing so i think this is interesting
*  because you raised andrew viles he spent seven years attacking the same thing yeah right and
*  and so i think that what attracts professional researchers to this is because even though it's
*  very painful but you keep fighting with something when you finally find the right insights and
*  string them together it feels really good so well there's also like short term it feels good to to
*  whether it's real or not to pretend like you've solved something in the sense like you have an
*  insight and there's a sense like this might be the insight that solves it so at least for me i
*  just enjoy that rush of positivity even though i know statistically speaking is probably going
*  to be a dead end i'm the same way i'm the same way in fact that's how i know whether i might want
*  to keep thinking about this general problem it's like if i still see that i'm getting some insights
*  i'm not at a dead end yet but that's also where i learned something from my phd advisor actually
*  he was a real big inspiration on my life his name is benny sudakov in fact he grew up in the former
*  soviet union excellent he was from georgia but he he he's an incredible person but one thing i
*  learned was choose the problems to work on that might matter if you sub if you succeed because
*  that's why for example we dug into covid it was just well suppose we succeed in finding some
*  interesting insight here well it actually matters then it's worth five yeah and i think covid
*  the way you're approaching covid has two interesting possibilities one it might help with the covid or
*  another pandemic but two i mean just this whole network theory space you might unlock some deep
*  understanding about the interaction of human beings that might have nothing to do with the
*  pandemic there's a there's a space of possible impacts that may be direct or indirect and the
*  same thing is with andrew wiles's proof i don't understand but apparently the pieces of it are
*  really impactful for for mathematics even if the main yes theorem is not so along the way the the
*  insights you have might be really powerful for unexpected reasons so i like what you said this
*  is something that i learned from another friend of mine who's also he's a very famous researcher
*  all these people are more famous than i am his name is jacob fox he's jacob fox at stanford also
*  a very big inspiration for me we were both grad students together at the same time well most
*  importantly you're good at selecting good friends ah yeah well that's that's that's the key you've
*  got to find good people to learn things from but his thing was he often said you know if you solve
*  a math problem and have this math proof math problem for him is like a proof right so suppose
*  you came up with this proof he always asks what have we learned from this that we could potentially
*  use for something else it's not just did you solve the problem that was supposed to be famous it was
*  and is there something new in the course of solving this that you had to invent that we could now use
*  as a tool elsewhere yeah there's this funny effect where just looking at different fields
*  where people discover parallels they'll they'll prove something you'll be telling your result
*  and then somebody later realizes this was already done 30 years ago in another discipline in another
*  way and it's really interesting now we did this offline another illustration he showed to me it's
*  interesting to see the different perspectives on a problem it kind of points like there's just like
*  very few novel ideas that everything else that most of us are just looking at different perspective
*  on the same idea and it makes you wonder this this this old silly question that i have to ask you
*  is do you think mathematics is discovered or invented do you think we're
*  creating new idea we're building a set of knowledge that's that's distinct from reality
*  or are we actually like it's math almost like a shovel where we're digging to like this core
*  set of truths that are that that were always there all along so i personally feel like it's
*  discovered but that's also because i guess the way that i like to choose what questions to work on
*  are questions that maybe we'll get to learn something about why is this hard i mean i'm
*  often attracted to questions that look simple but are hard right and what could you possibly
*  learn from that sort of like probably the attraction of from as last theorem as you
*  mentioned simple statement why is it so hard so i'm more on the discovered side and i also feel
*  like if we ever ran into an intelligent other species in the universe probably if we compared
*  notes there might be some similarities between both of us realizing that pi is important
*  because you might say why why humans do humans like circles more than others i think stars also
*  like circles i think planets like circles they're not perfect circles but nevertheless the concept
*  of a circle is just point and constant distance doesn't get any simpler than that it's possible
*  that like an alien species will have depending on different cognitive capabilities and different
*  perception systems will be able to see things that are much different than circles and so
*  so if it's discovered it would still be pointing at a lot of same geometrical concepts mathematical
*  concepts but it's interesting to think of how many things we would have to still align not just based
*  on notation but based on understanding like just the like some basic mathematical concepts like
*  how much work is there going to be in trying to find a common language i mean this is um i think
*  stephen wolfram and his son helped with the movie arrival like the developing an alien language like
*  how would aliens communicate with humans it's fascinating because like math seems to be the
*  most promising thing but even like math like how do you visualize mathematical ideas it feels like
*  there has to be an interactive component just like we have a conversation there has to be this
*  is something we don't i think think about often which is like with somebody who doesn't know
*  anything about math doesn't know anything about english or any other natural language
*  how would we describe we talked offline about visual proofs how would we through visual proofs
*  have a conversation where we say something here's the concept the way we see it
*  does that make sense to you and like can you mess with that concept to make it sense for you
*  and then go back and forth in this kind of way so purely through mathematics i'm sure it's possible
*  to have those kind of experiments with like tribes on earth that don't there's no common language
*  through math like draw a circle and see what they do with it right do some of these visual proofs
*  like the summation of the odds and the adds up to the squares yes i wonder how difficult that is
*  before one or the other species murders that's a good question i hope that the curiosity for
*  knowledge will overpower the greedy this is back to our game theory thing that the curiosity of
*  like discovering math together will overpower the desire for resources and uh ultimately like
*  you know willing to commit violence in order to gain those resources i think as we progress become
*  more and more intelligence as a species i'm hoping we would value more and more the knowledge
*  because we'll come up with clever ways to gain more resources so we won't be so resource starved
*  i don't know that's a hopeful message from when we finally meet aliens yeah yeah see the cool thing
*  about the math olympiad um i don't know if you know work from uh françois chalet from google
*  he come up he came up with this kind of um iq test slash it kind of has similar
*  aspects to it that also the math olympia does for for ai so he came up with these tests where
*  they're very simple for humans but very difficult for ai to illustrate exactly why we're just not
*  good at seeing a totally new problem uh we sorry ai systems are not good at
*  looking at a new problem that requires you to detect that there's a symmetry of some kind or
*  there's a pattern that's that hasn't it hasn't seen before the pattern is like obvious to us
*  humans but it's not so obvious to find that kind of it's you're inventing a pattern that's there
*  uh in order to then find a solution
*  so i don't know if you can comment on but from an ai perspective and from a math problem perspective
*  what do you think is intelligence what do you think is the thing that allows us to solve that
*  problem and how hard is it to build a machine to do that asking for a friend yeah well so i guess
*  you see because if i just think of the raw search space it's huge that's why you can't do it and if
*  i think about what makes somebody good at doing these things they have this heuristic sense it's
*  almost like a good chess player of saying let's not keep analyzing down this way because there's
*  some heuristic reason why that's a bad way to go yes where do they get that heuristic from now
*  that's a good question i don't know uh because that if you asked them to explain to you they
*  could probably say something in words that sounds like it makes sense yeah but i'm guessing that's
*  only a part of what's really going on in their brain of evaluating that position you know what
*  i mean if you ask gary caspar off what is good or why is this position good he will say something
*  yeah but it's probably not approximating everything that's going on inside so there's
*  basically a function being computed yeah but it's hard to articulate what that function is now the
*  question is could a computer get as good at computing these kinds of heuristic functions
*  maybe i i'm not enough of an expert to understand but one bit of me has always been a little bit
*  curious of whether or not the human brain has a particular tendency due to its wiring to come up
*  with certain kinds of things which is just natural due to the way that the topology of the neurons
*  and whatever is there for which if you tried to just build from scratch a computer to do it would
*  it naturally have different tendencies i don't know this is just me being completely ignorant
*  and just saying a few ideas well this is a good thing with that mathematics shows is we don't have
*  to be so math and physics or mathematical physics operates in a world that's different than our
*  descendants of a brain's operating so it allows us to to to have multiple many many dimensions
*  it allows us to work on on weird surfaces uh with like topology as a discipline is just weird to me
*  it's really complicated but it allows us to work in that space the differential geometry and all
*  those kinds of things where it's totally outside of our natural day-to-day four-dimensional experience
*  uh three d dimensional with time experience so math gives us gives me hope that we can
*  that we can see we can discover the processes of intelligence
*  uh outside the limited nature of our own like human experiences but you said that you're not
*  an expert it's kind of funny i i find that um we know so little about intelligence
*  that uh i think i honestly think like almost children are more expert at creating artificial
*  intelligence systems uh than than adults i feel like we know so little we really need to think
*  outside the box and those little i found people should check out france washer lay's little exams
*  but even just solving math problems i don't know if you've ever done this uh for yourself but
*  when you solve a math problem you kind of then trace back and try to figure out where did that
*  idea come from like what how do like what was i visualizing in my head how did i start visualizing
*  it that way how why did i start rotating that cube in my head in that way like what is that if
*  i were to try to build a program that does that what where did that come from so this is interesting
*  um so i try to do this to teach middle school students how to learn how to create and think
*  and invent and the way i do it is there are these math competition problems and i'm working in
*  collaboration with the people who run those and i will turn on my youtube live and for the first
*  time look at those questions and live solve them the reason i do this is to let the middle school
*  students and the high school students and the adults whoever wants to watch just see what exactly
*  goes on through someone's head as they go and attempt to invent what they need to do to solve
*  the question so i've actually thought about that it's i think that first of all as a teacher i
*  think about that because whenever i want to explain to a student how to do something i want to explain
*  how it made sense why it's intuitive to do the following things and why the wrong things are
*  wrong not just by this one short fast way well but why this is the right way if that makes sense
*  so my point is i'm actually always thinking about that um like how would you think about these
*  things and then i eventually decided the easiest way to expose this would just be to go live on
*  youtube and just say i've never seen any of these questions before here we go don't you get uh
*  man that's that's anxiety inducing for me uh don't you get trapped in a kind of like little
*  dead ends of confusion even on middle school problems yes that's what the comments are for
*  the live comments come in and students they try this oh wow it's actually pretty good and i'll
*  never get stuck i mean i'm willing to go on camera and say guess what pocherno can't do this that's
*  fine but then what ends up happening is you will then see how maybe somebody's saying something
*  and i look at the chat and i say aha that actually looks useful now that also shows how
*  not all ideas not all suggestions are the same power if that makes sense because if i actually
*  do get stuck i'll go fishing through the chat if anyone got any ideas i don't know if you can speak
*  to this but is there a moment for the middle school students maybe high school as well where
*  there's like a turning point for them where they maybe fall in love with mathematics or they or
*  they get it is there um is there something to be said about like discovering that moment and
*  and trying to grab them to get them to get them to understand that mathematics is
*  no matter what they want to do in life could be part of their life yes i actually do think
*  that the middle school is exactly the right time because that's the place where your mathematical
*  understanding gets just sophisticated enough that you can start doing interesting things
*  because if you're early on and counting i'm honestly not very good at teaching you new
*  insights my wife is pretty good at that but somehow once you get to this this part where
*  you know what a fraction is and when you know how to add and how to multiply and what the area of
*  a triangle is at that point to me the whole world opens up and you can start observing there are
*  really nifty coincidences the things that made the greek mathematicians and the ancient mathematicians
*  excited actually back then it was exciting to discover the pythagorean theory it wasn't just
*  homework so is there um what which discipline do you think has the most exciting coincidences so
*  is it geometry is it algebra um is it calculus well you see you're asking me and i'm the guy
*  who gets the most excited when the combinatorics shows up in the geometry is it okay so it's the
*  combinatorics in the geometry so first of all the nice thing about geometry this is the same
*  nice thing about computer vision is it's visual so geometry you can draw circles and triangles
*  and stuff so it naturally uh presents itself to to the visual proof right but also the nice thing
*  about geometry i think for me is the earliest class the earliest discipline where there's uh
*  that's most amenable to the exploration the invention through proofs the idea of proofs
*  i think is most easily shown in in geometry because it's so visual i guess so that that to
*  me is like uh if i were to think about when i first fell in love with math it would be geometry
*  and sadly enough that's not used geometry only has a little appears briefly in the journey
*  of of an um of a student and it kind of disappears and not until much later which
*  you know there may be like differential geometry i don't know where else it shows up for me in
*  computer science like you could start to think about like computational geometry or even graph
*  theory is the kind of geometry you could start to think about it visually although it's pretty
*  tricky but yeah it was always um that that was the most beautiful one everything else i guess
*  calculus can be kind of visual too that can that can be pretty beautiful but is there um
*  something you try to look for in the student to see like how can i inspire them at this moment
*  or is this like individual student to student is there something you could say there so first of
*  all i really think that every student can pick up all of this skill i really do think so i don't
*  think it's something only for a few and so if i'm looking for a student actually oftentimes what i'm
*  if i'm looking at a particular student the question is how can we help you feel like you have the
*  power to invent also because i think a lot of people are used to thinking about math as something
*  where the teacher will show you what to do and then you will do it yes so i think that the key
*  is to show that they have some let them see that they have some power to invent and at that point
*  it's often starting by trying to give a question that they don't know how to do you want to find
*  these questions that they don't know how to do that they can think about and then they can solve
*  and then suddenly they say my gosh i've had a situation i've had an experience where i didn't
*  know what to do and after a while i did is there um advice you can give on how to learn math
*  for people whether it's middle school whether it's somebody as an adult kind of gave up on math maybe
*  early on i actually think that these math competition problems middle school and high school
*  are really good they're actually very hard so if you if you haven't had this kind of experience
*  before and you grab a middle school math competition problem from the state level which is used to
*  decide who represents the state in the country in the united states for example those are pretty
*  tricky and even if you are a professional maybe not doing mathematical things and you're not a
*  middle school student you'll struggle so i find that these things really do teach you things by
*  trying to work on these questions is there a googleable term that you could use for the
*  organization for the state competitions ah yeah so there are a number of different ones that are
*  quite popular one of them is called math counts m-a-t-h-c-o-u-n-t-s and that's a big tournament
*  which actually has a state level there's also a math league dot org math league lea gu e dot org
*  also has this kind of tiered tournament structure there's also the american math competitions amc
*  eight amc also has amc 10 that's for 10th grade and below and amc 12 these are all run by the
*  mathematical association of america and these are always defined old questions
*  what about the daily challenges that you run what are those about we do that too but i mean the
*  difference was ours isn't that one's not free so so i should actually probably be careful the
*  things that i've just mentioned are also not free not all of those things i mentioned just now are
*  free either people can figure out what is free or not but yeah this is really nice to know what's
*  out there but can you speak a little bit to the daily challenges sure sure so that's actually what
*  we did when um i guess i was thinking about how would i try to develop that skill in people if we
*  had the power to architect the entire system ourselves so that's called the daily challenge
*  with pochandlo it's not free because that's actually how i pay for everything else i do
*  so so that's that was the idea but the the concept was aha now let's invent from scratch so if we're
*  going to go from scratch and we're going to use technology what if we made every single lesson
*  a something where first i say hey here's an interesting question recorded of course not live
*  but it's like i say hey here's an interesting question why don't we think about this but i
*  know you know i know you don't know how to do it so now you think and a minute later a hint pops on
*  the screen but you still think and a minute later a big hint pops on the screen you still think and
*  then finally after the three minutes hopefully you got some ideas you try to answer and then
*  suddenly there's like this pretty extended explanation of oh yeah so here's like multiple
*  different ways that you can do the question and by accident you also just learned this other concept
*  that's what we did so yeah is this targeted towards middle school students high school students it's
*  targeted towards middle school students with competitions but there's a lot of high school
*  students who didn't do competitions in middle school where they would also learn how to think
*  if you can see the whole concept was can we teach people how to think how would you do that you need
*  to give people the chance to on their own invent without that kid in the front row answering every
*  question in two seconds and people can find it i think what daily dot it's daily.pochandlo.com
*  but if you go to find my website you'll be able to find it beautiful can we zoom out a little bit
*  and so day to day week to week month to month year to year what does the lifelong educational
*  process look like do you think for for yourself but for for me what would you recommend
*  in in the world of mathematics or sort of as opposed to studying for a test but just like
*  lifelong expanding of knowledge and that skill for invention i think i often articulate this as
*  can you always try to do more than you could do in the past
*  yeah but that that comes in many ways that's and i will say it's great if one wants to build that
*  with mathematics but it's also great to use that philosophy with all other things in fact if i if
*  i just think of myself i just think what do i know now that i didn't know a year ago or a month ago
*  or a week ago and not just know but like what do i have the capability of doing yes and if you just
*  have that attitude it brings more see the thing is there's also a habit like it is a skill like
*  i've been using anki it's an app for helps you memorize things and i've actually this a few months
*  ago started doing this daily of setting aside time to think about an idea that's outside of my work
*  like let's say let's pick it's all over the place by the way but let's say politics like gun control
*  uh is it good to have a lot of guns or not in society and just i've set aside time every day
*  i do at least 10 minutes but i try to do 30 where i think about a problem and i kind of outline
*  them for myself from scratch from not looking anything up just thinking about it using common
*  sense and i think the practice of that is really important it's the daily routine of it it's the
*  discipline of it it's not just that i figured something out from that thinking about gun control
*  it's more that that muscle is built too it's that thinking muscle so i'm kind of interested in
*  you know math has because especially because i've gotten specialized into machine learning
*  and because i love programming so much i've lost touch with math a little bit to where i feel quite
*  sad about it and i want to fix that even just not math like pure knowledge math but math like these
*  middle school problems the challenges right is that something you see a person be able to do
*  every single day kind of just practice every single day for years so i can give an answer to
*  that that gives a practical way you could do it assuming you have kids so no i mean you can do it
*  yourself step one get kids no i'm just saying this because i'm just thinking out loud right now what
*  could i do what could i do to suggest because what i have noticed is that for example if you do have
*  kids who are in elementary school or middle school if you yourself go and look at those middle school
*  math problems to think about interesting ways that you can teach your elementary school or middle
*  school kid it works that's what my wife did she never did any of those contests before
*  but now she knows quite a lot about them i didn't teach her anything i don't i don't do that she just
*  was messing around with them and taught herself all of that stuff and that had the automatic daily i'm
*  always thinking how do you make it practical right yes and the way to make it practical is if the
*  the timer on the automatically daily is that you were going to automatically daily do something
*  with your own kid yes now it feeds back okay and that includes the whole lesson that if you want
*  to learn something you should teach it oh i strongly believe that yes i strongly believe that
*  so i currently don't have kids so that's uh maybe i should just get kids to help me with the math
*  thing but outside of that i i do want to do great math into daily practice so i'll definitely take
*  out i'll definitely check out the daily challenges and see because um what is it uh grants anderson
*  we talked about offline the three blue one brown he he speaks to this as well that his videos
*  aren't necessarily they don't speak to the thing that i'm referring to which is the daily practice
*  they're more almost tools of inspiration they kind of show you the beauty of a particular
*  of problem in mathematics but they're not a daily ritual and i'm in i'm in search of that daily
*  ritual mathematics it's not it's not trivial to find um but uh i hope i hope to find that because
*  i think math gives you a perspective on the world that enriches everything else so i like what you
*  said about the daily also because that's also one reason why i put my carnegie melon class online
*  it's not every day it was every it's every other day semester is almost over but the idea was
*  i guess my philosophy was if i'm already doing that the class let's just like put it there right
*  but i do know that there are people who have been following it who are not in my class at all who
*  have just been following it because yes it's combinatorics and the value of that is you could
*  you don't really need to know calculus to follow it if that makes sense so it's actually something
*  that people could follow so again and that one's free so that was just there on youtube well
*  speaking of combinatorics uh what is it what do you find interesting what do you find beautiful
*  about combinatorics so combinatorics to me is it's the study of things where
*  they might be more finite and more discrete what i mean is like if i look at a network actually a
*  lot of times the combinatorics will boil down to something and the combinatorics i think about
*  might be something related to graphs or networks and they're very discrete because if you have a
*  node it's not that you have 0.7 of a node and 0.3 of a node over there it's that you got one node
*  and then you jump one step to go to the next node so that that notion is different from say calculus
*  which is very uh continuous where you go and say i have this uh speed which is changing over time
*  and now what's the distance i've traveled that's the notion of an integral where you have to think
*  of subdividing time into very very small pieces so the the kinds of things that you do when you
*  reason about these finite discrete structures often might be iterative algorithmic inductive
*  these are ideas where i go from one step to the next step and so on and make progress i guess i
*  actually personally like all kinds of math my area of research just ended up in here because
*  i met a really interesting phd advisor potentially that's actually that's honestly the reason i went
*  into that direction i met a really interesting guy he seemed like he did good stuff interesting
*  stuff and he looked like he cared about students and i said let me just go and learn whatever you
*  do even though my prior practice and preparation before my phd was not combinatorics but analysis
*  the continuous stuff so the the annoying thing about combinatorics and discrete stuff
*  is uh it's often uh really difficult to solve uh from a sort of uh running time complexity perspective
*  uh is there could you speak to the idea of um complexity analysis of problems do you find it
*  useful to find it interesting do you define that lens of studying the difficulty of how difficult
*  the computer science problem is a useful lens onto the world oh very much so because um if you want
*  to make something practical which has large numbers of people using it the computational
*  complexity to me is almost question one and that's again that's at the origin of when we started
*  doing this stuff with disease control from the very beginning the deep questions that were running
*  through my mind were would we be able to support a large population with only one server and if the
*  answer is no we can't start because i don't have enough money
*  yeah and there the question is very much you know linear time versus anything
*  uh anything slower than linear time yep um it's a very specific thing you have a bunch of really
*  interesting papers if i could ask maybe we could pull out some cool insights at the high level
*  can you describe the data structure of a voting tree and what are some interesting results on it
*  you have a paper that i noticed on it yeah so this is an example of i guess um how in math we
*  might say here's an interesting kind of a question that we just can't seem to understand enough about
*  maybe there's something else going on here and the way to describe this is you could imagine
*  trying to hold elections where if you have only two candidates that's kind of easy you just run
*  them against each other and see who gets more votes but as you know once you have more candidates
*  it's very difficult to decide who wins the election and there's an entire like voting
*  theory around this so a theoretical question became what if you made a like a system of run-offs
*  like a system of heads uh head-to-head contests which you structure like a tree almost looking
*  like a circuit i'm using that way of thinking because it's sort of like a in electrical
*  engineering or computer science you might imagine having a bunch of leads that carry signal which
*  are going through and gates and or gates and whatnot and you manage to compute beautiful things
*  this is just from a purely abstract point of view what if the inputs are candidates
*  and for every two candidates it is known which of the candidates is more popular than the other
*  now can you build some kind of a circuit board which says first candidate number four will play
*  against five and see who wins and so on okay so now what would be a nice outcome right this is
*  a general question of could i make a big circuit board to feed an election into like maybe one
*  nice outcome would be whoever wins at least is preferred over a lot of people yes so for example
*  if you ran in 1024 candidates ideally we would like a guarantee that says that the winner beats
*  a lot of people actually in any uh system where there are 1024 candidates there's always a
*  candidate who beats at least 512 of the others this is a mathematical fact that there's actually
*  always a person who beats at least half of the other people i'm trying to make sense of that
*  mathematical fact is this supposed to be obvious uh no but i can explain it it's no no i can the
*  the way it works is that uh think of it this way every time i think imagine i have all these
*  candidates and everyone is competing is everyone is like compared with everyone else at some point
*  well think of it this way whenever there's a comparison somebody gets a point that's the one
*  who is better than the other one my claim is there's somebody whose score is at least half of how many
*  other people there are yeah i'm just trying to like my intuition is very close to that being true but
*  it's beautiful i didn't at first that's not an obvious fact no it's not and it's it feels like
*  a beautiful thing well let me explain it this way imagine that for every uh match you didn't
*  give one point but you gave two points you gave one point to each person now that's not what we're
*  really doing we really want to give one point to the winner of the match but instead we'll just
*  give two if you gave two points to everyone on every matchup actually everyone has the same
*  number of points and the number of points they get is how many other people there are
*  does that sort of make sense i'm just like saying no no everything everything you're saying makes
*  perfect sense okay so the point is if for every comparison between two people which i'm doing for
*  every two people i gave one point to each person your score everyone's score is the same it's how
*  many other people there are yes now we only make one change for each matchup you give one point
*  only to the winner so we're awarding half the points so now the deal is if in the original
*  if in the original situation everyone's score was equal which is how many other people there are
*  now there's only half the number of points to go around so what ends up happening is that there's
*  always going to be like the average number of points per person is going to be half of how many
*  other people there are and somebody is going to be above somebody's going to be at least average
*  yeah this is this is this notion of expected value that if i have a random variable which has an
*  expected value there's going to be some possibility in the probability space where you're at least as
*  big as the expected yeah when you describe it like that it's obvious but when you are first saying
*  in this little circuit that there's going to be one candidate better than uh than half that's not
*  obvious yeah it's not it's funny math this is nice uh okay so you have this but ultimately you want
*  you're trying to with a voting tree i don't know if you're trying this but uh to have a circuit
*  that's that's like compressed that's small well you'd like that achieves the the achieves the
*  the same kind of um i mean the smaller it is the if we look at practically speaking the the lower
*  the cost of running the election of running through of computing the circuit that is true but actually
*  at this point the the the reason the question was interesting is because the there was no good
*  guarantee that the winner of that circuit would have like have beaten a lot of people let me give
*  an example the best known circuit when we started thinking about this was the circuit called
*  candidate one plays against candidate two candidate three plays against four and then the
*  winners play against each other and then by the way five plays against six seven against eight
*  the winners play against each other you understand it's like a giant binary tree where yeah it's a
*  binary like a balanced binary tree okay it's a balanced binary tree one two three four up to
*  thousand twenty four everyone going up to find the winner beautiful well you know what there's a
*  system in the world where it could just be that there's a candidate called number one that just
*  beats like 10 other people just the 10 that they need to be on their way up and they lose to
*  everyone else but somehow they would get all the way up yes my point is it is possible to
*  outsmart that circuit in one weird way of the world which makes that circuit a bad one because
*  you want to say i will use this circuit for all elections and you might have a system of inputs
*  that go in there where the winner only beat 10 other people which is the people they had to
*  beat on the way up so you want to have a circuit where there's as many like the final result is
*  as strong as possible yes and so is there what what ideas do you have for that so we actually
*  only managed to improve it to square root of n so if n is the number of vertices n over two it would
*  be the ideal we got it to and we got it to square root of n versus log of n yeah exactly yeah
*  which is well that is halfway it could be a lot yeah it could be a big improvement so that's a
*  okay cool is there something you can say with words about what kind of circuit what that looks like
*  i can give an idea of one of the tools inside yeah but the actual execution ends up being more
*  complicated but one of the widgets inside this is building a system where you have like a candidate
*  who plays like the one part of the whole huge huge tree is that that same candidate let's call them
*  seven seven plays against somebody let's make up some numbers let's call the others like letters
*  so seven plays against a seven's also going to play against b separately
*  and the winners of each of those who play each other by the way seven's also going to play c
*  seven's going to play d and the winners are going to play each other and the winners are going to
*  going to play each other.
*  We call this seven against all.
*  Well, seven against everyone from a bunch of...
*  Got it.
*  So there's some nice overlap between the matchups that somehow has a nice feature to it.
*  Yes, and I can tell you the nice feature because if at the base of this giant circuit, like
*  this is a widget, we build the things out of widgets, so I'm just describing one widget,
*  but in the base of this widget, you have lots of things which are seven against someone,
*  seven against someone, seven against someone.
*  In fact, every matchup at the bottom is seven against someone.
*  What that means is if seven actually beat everyone they were matched up against, well,
*  seven would rise to the top.
*  So one possibility is if you see a seven emerge from the top, you know that seven actually
*  beat everyone they were against.
*  On the other hand, if anyone else is on top, let's call it F, if F is on top, how did F
*  get there?
*  Well, F beat seven on the way at the beginning.
*  So the point is the outcome of this circuit has a certain property.
*  If you see a seven, you know that the seven actually beat a bazillion people.
*  If you see anyone else, at least you know they beat seven.
*  Yeah, then you can prove that it has a nice property.
*  That's really interesting.
*  Is there something you can say, perhaps going completely outside of what we're talking about,
*  is how we may have mathematical ideas of improving the electoral process.
*  That one, no.
*  No, I can't give you that one.
*  Do you ever see as there being a lot of opportunities for improving how we vote?
*  Like from your, I don't know if you saw parallels, but you know, it seems like this actually
*  kind of maps to your sort of COVID work, which is there's a network effect, right?
*  It seems like we should be able to apply similar kind of effects of how we decide other things
*  in our lives.
*  And one of the big decisions we'll make is who represents us in government.
*  Do you ever think about like mathematically about those kinds of systems?
*  I think a little bit about those because where I went to college, the way we voted
*  for student government was based on this, is it called ranked choice where you eliminate
*  the bottom and there's runoff elections.
*  So that was the first time I ever saw that.
*  And I thought that made sense.
*  The only problem is it doesn't seem so easy to get something that makes sense adopted
*  as the new voting system.
*  That's a whole nother, that's not a math solution.
*  Well it's math in a sense, it's game theory.
*  You have to come up with incentive, it's mechanism design.
*  You have to figure out how to trick us despite our basic human nature to adopt solutions
*  that are better.
*  That's a whole nother conversation, I think.
*  Can you just, because it sounded really cool, talk a little bit about stochastic coalescence
*  and you have a paper showing that, you can describe what it is, but I guess it's super
*  linear, super logarithmic time and you came up with some kind of trick that makes it faster.
*  Can you just talk about it a little bit?
*  Yeah, so this was something which came up when I was at Microsoft Research for a summer.
*  And I'm putting that context because that shows that it has some practical motivation
*  at some point.
*  Actually, I think it's still fantastic.
*  It doesn't need to, it can be beautiful and it's alright.
*  Yeah, so the easiest way to describe this is suppose you got a big crowd of people and
*  everybody knows how many hours of sleep they got last night.
*  And you want to know how many total hours of sleep were gotten by this big crowd of
*  people.
*  At the beginning, you might say, that sounds like a linear time algorithm of saying, hey,
*  how many hours you got?
*  How many you got?
*  How many you got?
*  Add, add, add.
*  But there's a way to do this if you remember that there are people and they presumably
*  know how to add.
*  You could make a distributed algorithm to make this happen.
*  For example, while we're thinking of these trees, imagine you had 1024 people.
*  If you could just say, hey, person number one and person number two, you will add your
*  hours of sleep.
*  Person number two will go away and person number one is going to remember the sum.
*  Person three and four add up and person three takes charge of remembering it.
*  Person four goes away.
*  Now this like person one knows the sum of these two.
*  Person three knows the sum of those two.
*  They talk.
*  You see what I mean?
*  It's like you're going up this tree, same tree that we talked about earlier.
*  Built up a tree from the bottom up.
*  Yeah, built up a tree from the bottom up.
*  The beautiful thing is since everyone's doing stuff in parallel, the amount of time it
*  takes to get the total sum is actually just the number of layers in the tree, which is
*  10.
*  Now that's logarithmic time to add up the number of hours that people slept today.
*  Sounds fantastic.
*  There's only one problem.
*  How do you decide who's person number one and person number two?
*  Yes.
*  If, for example, we just went out into downtown and said, hey, get these thousand people,
*  go.
*  We're going to go and say, and by the way, you're one and you're two and you're three.
*  That's linear time.
*  Yes.
*  That's cheating.
*  Now the question is how to do this in a distributed way.
*  There were some people who proposed a very elegant algorithm and they wanted to analyze
*  it.
*  I came in onto the analyze side, but the elegant algorithm was like this.
*  It was like, well, we don't actually know what this big tree is.
*  There isn't any big tree.
*  What's going to happen is first, everyone is going to decide right now what one important
*  thing everyone is going to at the very beginning of the whole game.
*  They will have delegated responsibility to themselves as the one who knows the sum so
*  far.
*  So, so, so the point is there's, there's going to be people are all going to have like a
*  pointer which says, you are the one who knows my, you, you've taken care of my ticket, my
*  number.
*  Yeah.
*  They select the representative for this particular piece of knowledge.
*  And at the very beginning, you're your own representative.
*  The thing has to start simple.
*  So at the beginning, you're your own representative.
*  You're pointing to yourself.
*  Got it.
*  Yep.
*  And now the way this works is that at every time step, someone blares a ding dong on the
*  town clock or whatever.
*  And each person flips a coin themselves to decide, am I going to hunt for somebody to
*  give my number to and let them represent me?
*  Or am I going to sit here and wait for someone to come?
*  Okay.
*  Okay.
*  Well, they flipped their coin.
*  Some of the people start asking other people saying, Hey, I would like you to be my representative.
*  Here is my number.
*  But the problem is that there's limited bandwidth of the people who are getting asked.
*  It's like you can't get, you can't go out to prom with five people.
*  That is not what we're doing.
*  We're adding numbers.
*  Okay.
*  But you can only add one number.
*  So the person who has suddenly gotten asked by all these people, well, they'll have to
*  decide who they're going to take it from.
*  And they randomly just choose one.
*  When they randomly choose one, all the others are rejected and they don't get to delegate
*  anything in that round.
*  But now if this person has absorbed this one who said, okay, here, you take charge of my
*  number, this person now updates their pointer.
*  You're in charge.
*  And this person adds the two numbers.
*  That was the first round.
*  In the next round, when they do the coin flipping, this person doesn't flip anymore because they're
*  just delegating.
*  It's that anyone who has the pointers themselves, that's like a person who is in charge of some
*  number of information, they flip the coin to decide, should I find other people who
*  are agents or should I wait for people to ask me?
*  Yes.
*  Brilliant.
*  This is somebody else's idea.
*  And then now the idea is, okay, if you just keep doing this process, what ends up happening?
*  Oh yeah.
*  And also, by the way, if you decide that you want to go reach out to other people, here's
*  the catch.
*  You're one of these agents saying, okay, I'm going to go look for someone.
*  You have no idea who in this crowd is an agent or somebody who delegated it to someone else.
*  You just pick a random person.
*  When you pick the random person, if it lands on someone and the person says, oh, I actually
*  delegated it to someone, then you follow the point.
*  You walk up the delegation chain.
*  And you can do path compression in the algorithm to make it so you don't consistently do lots
*  of walking up.
*  But the bottom line is that what ends up happening is that you end up reaching out
*  whenever you're one of the ones reaching out, you can think of it as each agent is responsible
*  for some number of people.
*  It's almost like they're the leader of a bunch.
*  As the process is evolving, you have these lumps.
*  Each lump has an agent.
*  And when the agent reaches out, they reach out to another lump where the probability
*  of them hitting that lump is proportional to the size of the lump.
*  That is the one funny thing about this process.
*  This is not that they can reach out to a uniformly random lump where every lump has the same
*  chance of getting reached out to.
*  The bigger the lump is, the more likely it is that you end up reaching that lump.
*  Which is a problem?
*  Let me explain why that's a problem.
*  Because you see, you're hoping that this has a small number of steps, but here's a bad
*  situation that could happen.
*  Imagine if you had like, there are N people that you're adding up.
*  Imagine that you have exactly square root of N lumps left, of which almost all of them
*  are just one person who's still their own boss, their own manager.
*  Except one giant lump.
*  One giant one.
*  Now what's going to happen?
*  It's going to be a huge bottleneck because every round the giant one can only absorb
*  one of the others.
*  Yes.
*  And now you suddenly have time which is about square root of N. The square root of N is
*  chosen because that is one where the lumps are such that you really are limited by this
*  large one slowly sucking up the rest of them.
*  So the heart of the question became, well, but is that just so unusual that it doesn't
*  usually happen?
*  Because remember you start with everyone just being independent.
*  It's like a lot of lumps of size one.
*  How naturally do the big lumps emerge?
*  Yes.
*  And so what that heart of the proof was, was showing that that was a joint work with A.L.
*  Kavetsky.
*  That one was showing that actually in that thing, the lumps do kind of get out of whack.
*  And so it is not the purely logarithmic number of steps.
*  But if you make one very slight change, which is if you are one of the agents and you have
*  just been propositioned, possibly relayed along by a couple of different people, if
*  you just say, don't take a random one, but accept the smallest lump, that actually does
*  enough to even the lump size.
*  Yeah, that's I mean, yeah, it's fascinating how with the distributed algorithms, a little
*  yes, make all the difference in the world.
*  Yeah, actually, by the way, this does back to our voting conversation.
*  This makes me think of like these networking systems are so fascinating to study.
*  They immediately spring to mind ideas of how to have representation.
*  Maybe as opposed to me voting for a president, I want to vote for for like for you to represent
*  me maybe on a particular issue, and then you'll delegate that further.
*  And then we naturally construct those kinds of networks because that that feels like I
*  can have a good conversation with you and figure out that you know what you're doing
*  and I could delegate it to you in that way, construct a representative government, a
*  representative decision maker that feels that feels really nice as opposed to like us, like
*  a tree of height one or something where it's like everybody's just it feels like there's
*  a lot of room for layers of representation to form organically from the bottom up.
*  I wonder if there are systems like that.
*  This is the cool thing about the Internet and the digital space where we're so well
*  connected, just like with the Novid app to distribute information about the spread of
*  the disease, we can the same way in a distributed sense form anything like any kind of knowledge
*  basis that are formed in a decentralized way and in a hierarchical way as opposed to sort
*  of old way where there is no mechanism for large scale, fast, like distributed transactional
*  information.
*  This is really interesting.
*  This is where almost like network graph theory becomes practical.
*  Most of that exciting work was done in the 20th century, but most of the application
*  will be in the 21st, which is cool to think about.
*  Let me ask the most ridiculous question.
*  You think P equals NP?
*  Wow.
*  I don't know.
*  I mean, I would say.
*  I know there are enough people who have very strong interest in trying to show that it
*  is.
*  I'm talking about government agencies.
*  For security purposes.
*  And most computer scientists, which you'd say believe that P equals NP.
*  My question almost like this is back to our aliens discussion.
*  You want to think outside the box, the low probability event.
*  What kind of discoveries would lead us to prove that P does not equal to NP?
*  There could be giant misunderstandings or gaps in our knowledge about computer science,
*  about theoretical computer science, about computation, which allow us to think like
*  flatten all problems.
*  Yeah.
*  I don't know the answer to this question.
*  I think it's very interesting.
*  Let's put it this way.
*  By being at Carnegie Mellon and being around the theoretical computer scientists, I know
*  enough about what I don't know to say.
*  To be humble.
*  I'm the wrong person to answer this question.
*  It's a great one.
*  Well, Scott Aaronson, who's now here at UT Austin, he used to be at MIT, puts the probability
*  of P not equals to NP at 3%.
*  I always love it when you ask, it's very rare in science and academics because most folks
*  are humble in the face of the mystery, the uncertainty of everything around us.
*  To have both the humor and the guts to say, what are the chance that there's aliens in
*  our galaxy, intelligent alien civilizations?
*  As opposed to saying, I don't know, it could be zero.
*  It could be, depending on the fact you're saying, it's 2.5%.
*  There's something very pleasant about it.
*  It's the number thing.
*  This power to the number, it's just like 42.
*  It's like, why 40?
*  I don't know, but it's a powerful number.
*  This is the power of the human psychology is once you have the number 42, it's not that
*  the number has meaning, but because it's placed in a book with humor around it, it has the
*  meme effect of actually creating reality.
*  You could say that 42 has a strong contribution of helping us colonize Mars because it created,
*  it gave the whatever existential crisis to many of us, including Elon Musk when he was
*  young reading a book like that.
*  Now 42 is now part of his humor that he doesn't shut up about.
*  It's constantly joking about it.
*  That humor is spreading through our minds and somehow this silly number just had an
*  effect.
*  In that same way, after Scott told me the 3% chance, it stuck in my head and I think
*  it's been having a ripple effect in everybody else.
*  The believing that P is not equal to NP, Scott almost as a joke saying it's 3%, is actually
*  motivating a large number of researchers to work on it.
*  3% is high.
*  It's very high.
*  Because for the potential impact that that might have.
*  But then 3% is not that high because it's only, you know, we're not very good.
*  I feel like humans are only able to really think about like 1%, 50%.
*  I think a lot of people round 3% up to 50% in our minds.
*  Like 3%...
*  It could happen.
*  It could happen.
*  And it could happen.
*  It's like, yeah, like half the time it'll probably happen.
*  So we're not very good at that.
*  That's the other thing with the pandemic is we're not the exponential growth that we also
*  talked about offline is something that we can't quite intuit.
*  And that's something we probably should if we were to predict the future, to anticipate
*  the future and to understand how to create technologies that let us sort of control the
*  future.
*  Can I ask you for some recommendations, maybe for books or movies in your life long ago
*  when you were baby po or today that you found insightful or you learned a lot from what
*  you would recommend to others?
*  Yeah.
*  So I think I don't necessarily have an exact name of these old things, but I was generally
*  inspired by stories, true or fictional, of campaigns.
*  For example, like the Lord of the Rings.
*  That's a campaign, right?
*  But the thing that always inspired me was it could be possible for somebody who's crazy
*  enough to go up against adversity after adversity after adversity and it succeeds.
*  I mean, those are false.
*  Those are fictitious.
*  But I also spent a lot of time, I guess, reading about, I don't know, I was interested somehow
*  in World War II history for whatever reason.
*  That's a campaign which is much more brutal.
*  But nevertheless, the idea of difficulty, strategy, fighting even when things, in that
*  case it was really fighting, but just pushing on even when things are difficult.
*  I guess these are the kinds of general stories that made me want to work on things that would
*  be hard and where it could be a campaign.
*  It could be that you work on something for a year, multiple years, because that was the
*  point.
*  Yeah, it starts with a single person.
*  That's the interesting thing.
*  I've obviously been, don't shut up about it, recently about World War II, especially on
*  the Hitler side and the Stalin side.
*  Some of that has really affected my own family, the roots of my family very much.
*  It's interesting to think that it was just an idea and one person decided to do stuff
*  and it just builds and builds and builds.
*  You can truly have an impact on the world, both horrendous and exceptionally positive
*  and inspiring.
*  Yeah, it's like it's an agency of us individuals.
*  We're just reacting to the world, but we have the full power to actually change the world.
*  Is there advice you can give to young folks?
*  We give a bunch of advice on middle school, high school mathematics.
*  Is there more general advice you would give about how to succeed in life, how to learn
*  for high school students, for college students, career or life in general?
*  I think the first one would be to make sure that you're learning to invent and to make
*  sure you're not just learning how to mimic.
*  Because a lot of times you learn how to do X by watching somebody do X and then repeating
*  X many times with different inputs.
*  I'm just being very generic in explaining this.
*  But I guess this is just my own attitude towards the world.
*  I didn't like ever following anyone's directions exactly.
*  Even if you told me this is the way to do your homework is to write in pencil, I would
*  say, but I think pen is nice, let's try.
*  I've been that kind of a funny person.
*  But I do encourage that if you can learn how to invent as your core skill, then you can
*  do a lot.
*  But then the second piece that comes with that is something I learned from my PhD advisor,
*  which was, well, make sure that what you're working on is big enough.
*  And so in that sense, I usually advise to people once they have learned how to invent,
*  ideally, don't just try to settle for something comfortable.
*  Try to see if you can aim for something which is hard, which might involve a campaign, which
*  might be important, which might make a difference.
*  And it's more of, I guess, rather than worrying, what if you didn't achieve that?
*  There's also the regret of what if I didn't try?
*  See, that's how I operate.
*  I don't operate based on did I succeed or fail?
*  It was hard anyway.
*  If I did this novid thing and the whole thing failed, would I feel terrible?
*  No, it's a very hard problem.
*  But would I have had the regret of not jumping in?
*  Yes.
*  So it's that different mentality of don't worry about the failing part as much of the
*  make sure you give yourself the shot at those potentially unbounded opportunities.
*  You almost make it sound like there's a meaning to it all.
*  Let me ask the big ridiculous question.
*  What do you think is the meaning of life?
*  Or maybe the easier version of that is what brings your life joy?
*  So I'll just answer that one personally.
*  For me, I'm a little bit weird.
*  I sort of...
*  I guess you can tell by now.
*  See the pen and pencil discussion from earlier, yes.
*  Yeah, yeah.
*  So I mean, my thing is, I guess I personally just wanted to maximize a certain score, which
*  was for how many person years after I'm no longer here anymore, did what I do mattered?
*  And it didn't matter if it's necessarily attributed to me.
*  It's just like, did it matter?
*  And so that's what I wanted.
*  I guess that is very inspired by how scientists work.
*  It's like, why do we keep talking about Newton?
*  It's because Newton discovered some interesting things.
*  And so Newton's score is pretty high.
*  It's going to be infinity, right?
*  Well, let's hope it's infinity, but pretty high.
*  Ah, yes, yes.
*  So you're going for...
*  So person years, you're going for like triple digits.
*  You're going for...
*  So like Newton is like four digits probably, like a thousand years.
*  Or a person lifetimes.
*  How do you like to think about what are we...
*  Sorry, I meant people times years.
*  So then it's like, actually his is huge.
*  His is like going to be billions or trillions, right?
*  Trillions.
*  But I guess for me, I actually changed the metric after a while.
*  And the reason is because you may have seen, I found some simple way to solve quadratic
*  equations that is easier than every textbook.
*  So my score might already be not bad, which is why I decided then let's change it into
*  the number of hours in the lifetimes as well.
*  So the way I was doing it before is that if a person was sort of remembering or using
*  or appreciating what I had done for like 10 years of their life, that would count as 10.
*  So if there was one person who for 10 years remembered or appreciated something I did,
*  that counts as a score of 10 and we add up overall people.
*  And then, and that was with the hypothesis that the score would be very finite in the
*  sense that if I didn't come up with anything that might potentially help a lot of generations
*  in a forever way, then your score would be finite because at some point it's not...
*  People don't remember that you made like nice bottles or something, right?
*  But then after the quadratic equation thing, it was that there's some chance that that
*  actually might make it into textbooks.
*  And if it makes it in textbooks, the chance that there will be an easier way discovered
*  is actually quite small.
*  So in that case, then the score might get bigger.
*  I was just saying the score might actually already have been achieved in a non-trivial way.
*  Oh, I see.
*  I see.
*  Because...
*  It's fun to think about because it could be different.
*  You can achieve a high score by a small number of people using it for most of their lifetime
*  and then generations and generations.
*  Or you can have, if we do dissipate, if we do spread, colonize, become multi-planetary
*  species, you could have that little, a clever way to solve differential equations spread
*  through like trillions of people as they spread throughout the galaxy.
*  And they would only use it each one, a few hours in their lifetime, but the kids will
*  use it, the kids will use it, it will spread and you'll have that impact in that kind of
*  way.
*  Yes.
*  So that's why I renormalized it.
*  Because I was like, well, that's kind of dumb because what's the importance of that?
*  That will save people 15 minutes.
*  So what I meant is I didn't want to count that as the main score.
*  Well, I'm going to have to try to come up with some kind of device that everyone would
*  want to use maybe to make coffee because coffee seems to be the prevalent performance enhancing
*  chemical that everyone uses.
*  So I'll have to think about those kinds of metrics.
*  Yeah.
*  But you see, that's just, that's just giving an idea of, I guess, what I found meaningful
*  in general, like whether or not it's like, whether or not that quadratic thing is important
*  or not.
*  The general idea was I wanted to do things that would outlast me.
*  Yes.
*  And that was what inspired me.
*  And that's just how I choose what problems to work on.
*  And that's a kind of immortality is ideas that you've invented living on long after
*  you in the minds of others.
*  And humans are ultimately not, are like meat vehicles that carry ideas for brief for just
*  a few years.
*  It may not be the important thing.
*  It might be the ideas that we carry with us and invent new ones.
*  Like we get a bunch of baby ideas in our head.
*  We borrow them from others and then maybe we invent a new one.
*  And then you one might have a life of its own.
*  And it's fun.
*  It's fun to think about that idea of living for many centuries to come unless we destroy
*  ourselves.
*  But maybe AI will borrow it and we'll remember Po as like that one human that, that helped
*  us out before we of course killed him and the rest of human civilization.
*  On that note, well, this is a huge honor.
*  You're one of the great educators I've ever gotten a chance to interact with.
*  So it's truly an honor that you would talk with me today.
*  It means especially a lot that you would travel out to Austin to talk to me.
*  It really means a lot.
*  So thank you so much.
*  Keep on inspiring.
*  And I'm one of your many, many students.
*  Thank you so much for talking today.
*  Thank you.
*  Thank you.
*  It's actually a real honor for me to talk to you and to get this chance to have this
*  really intellectual conversation through all of these topics.
*  Thanks, bro.
*  Thanks for listening to this conversation with Po Shen Lo and thank you to Jordan Harmer
*  to show on it better help, eight sleep and element.
*  Check them out in the description to support this podcast.
*  And now let me leave you with some words from Isaac Newton.
*  I can calculate the motion of heavenly bodies, but not the madness of people.
*  Thank you for listening and hope to see you next time.

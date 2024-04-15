---
Date Generated: April 13, 2024
Transcription Model: whisper medium 20231117
Length: 9760s
Video Keywords: ['chris lattner', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 493977
Video Rating: None
---

# Chris Lattner: The Future of Computing and Programming Languages | Lex Fridman Podcast #131
**Lex Fridman:** [October 18, 2020](https://www.youtube.com/watch?v=nWTvXbQHwWs)
*  The following is a conversation with Chris Latner, his second time on the podcast.
*  He's one of the most brilliant engineers in modern computing, having created LLVM
*  Compiler Infrastructure Project, the Clang Compiler, the Swift Programming Language,
*  a lot of key contributions to TensorFlow and TPUs as part of Google. He served as Vice
*  President of Autopilot Software at Tesla, was a software innovator and leader at Apple,
*  and now is at Sci5 as Senior Vice President of Platform Engineering, looking to revolutionize
*  chip design to make it faster, better, and cheaper. Quick mention of each sponsor, followed by some
*  thoughts related to the episode. First sponsor is Blinkist, an app that summarizes key ideas from
*  thousands of books. I use it almost every day to learn new things or to pick which books I want
*  to read or listen to next. Second is Neuro, the maker of functional sugar-free gum and mints that
*  I use to supercharge my mind with caffeine, L-theanine, and B vitamins. Third is Masterclass,
*  online courses from the best people in the world on each of the topics covered, from rockets,
*  to game design, to poker, to writing, and to guitar. And finally, Cash App, the app I use to
*  send money to friends for food, drinks, and unfortunately lost bets. Please check out the
*  sponsors in the description to get a discount and to support this podcast. As a side note,
*  let me say that Chris has been an inspiration to me on a human level because he is so damn good as
*  an engineer and leader of engineers, and yet he's able to stay humble, especially humble enough to
*  hear the voices of disagreement and to learn from them. He was supportive of me and this podcast
*  from the early days, and for that I'm forever grateful. To be honest, most of my life no one
*  really believed that I would amount to much. So when another human being looks at me, it makes
*  me feel like I might be someone special. It can be truly inspiring. That's the lesson for educators.
*  The weird kid in the corner with a dream is someone who might need your love and support
*  in order for that dream to flourish. If you enjoy this thing, subscribe on YouTube,
*  review it with five stars on Apple Podcasts, follow on Spotify, support on Patreon, or connect
*  with me on Twitter at Lex Friedman. And now here's my conversation with Chris Latner.
*  What are the strongest qualities of Steve Jobs, Elon Musk, and the great and powerful
*  Jeff Dean since you've gotten the chance to work with each? You're starting with an easy question
*  there. These are three very different people. I guess you could do maybe a pairwise comparison
*  between them instead of a group comparison. So if you look at Steve Jobs and Elon, I worked a lot
*  more with Elon than I did with Steve. They have a lot of commonality. They're both visionary in
*  their own way. They're both very demanding in their own way. My sense is Steve is much more human
*  factor focused where Elon is more technology focused. What does human factor mean? Steve's
*  trying to build things that feel good, that people love, that affect people's lives,
*  how they live. He's looking into the future a little bit in terms of what people want.
*  Where I think that Elon focuses more on learning how exponentials work and predicting
*  the development of those. Steve worked with a lot of engineers. That was one of the things that are
*  reading the biography and how can a designer essentially talk to engineers and get their
*  respect? I think so. I did not work very closely with Steve. I'm not an expert at all. My sense is
*  that he pushed people really hard, but then when he got an explanation that made sense to him,
*  then he would let go. He did actually have a lot of respect for engineering,
*  but he also knew when to push. When you can read people well, you can know when they're holding
*  back and when you can get a little bit more out of them. I think he was very good at that.
*  I mean, if you compare the other folks, so Jeff Dean, right? Jeff Dean's an amazing guy. He's
*  super smart, as are the other guys. Jeff is a really, really, really nice guy. Well-meaning.
*  He's a classic Googler. He wants people to be happy. He combines it with brilliance so he can
*  pull people together in a really great way. He's definitely not a CEO type. I don't think he would
*  even want to be that. Do you know if he still programs? Oh yeah, he definitely programs. Jeff
*  is an amazing engineer today, and that has never changed. It's really hard to compare Jeff to
*  either of those two. I think that Jeff leads through technology and building it himself,
*  and then pulling people in and inspiring them. I think that that's one of the amazing things
*  about Jeff. Each of these people, with their pros and cons, all are really inspirational
*  and have achieved amazing things. I've been very fortunate to get to work with these guys.
*  For yourself, you've led large teams. You've done so many incredible difficult technical challenges.
*  Is there something you've picked up from them about how to lead?
*  I think leadership is really hard. It really depends on what you're looking for there.
*  I think you really need to know what you're talking about. Being grounded on the product,
*  on the technology, on the business, on the mission is really important.
*  Understanding what people are looking for, why they're there. One of the most amazing things
*  about Tesla is the unifying vision. People are there because they believe in clean energy and
*  electrification and all these kinds of things. The other is to understand what really motivates
*  people, how to get the best people, how to build a plan that actually can be executed. There's so
*  many different aspects of leadership and it really depends on the time, the place, the problems.
*  There's a lot of issues that don't need to be solved. If you focus on the right things
*  and prioritize well, that can really help move things.
*  Two interesting things you mentioned. One is you really have to know what you're talking about.
*  You've worked on a lot of very challenging technical things.
*  So I kind of assume you were born technically savvy, but assuming that's not the case,
*  how did you develop technical expertise? Even at Google, you worked on I don't know how many
*  projects, but really challenging, very varied. Compilers, TPUs, hardware, cloud stuff,
*  a bunch of different things. The thing that I've become comfortable with,
*  as I've gained experience, is being okay with not knowing. A major part of leadership is actually,
*  it's not about having the right answer, it's about getting the right answer.
*  If you're working in a team of amazing people, and many of these places, many of these companies
*  all have amazing people, it's the question of how do you get people together? How do you build trust?
*  How do you get people to open up? How do you get people to be vulnerable sometimes with an idea
*  that maybe isn't good enough, but it's the start of something beautiful? How do you
*  provide an environment where you're not just top down, that'll do the thing that I tell you to do,
*  right? But you're encouraging people to be part of the solution, and providing a safe space where
*  if you're not doing the right thing, they're willing to tell you about it.
*  So you're asking dumb questions?
*  Yeah, dumb questions are my specialty. So I've been in the hardware realm recently, and I don't
*  know much at all about how chips are designed. I know a lot about using them. I know some of
*  the principles and the ars technical level of this, but it turns out that if you ask a lot of
*  dumb questions, you get smarter really quick. And when you're surrounded by people that want to teach
*  and learn themselves, it can be a beautiful thing. So let's talk about programming languages,
*  at the highest absurd philosophical level.
*  Don't get romantic on me, Lex.
*  I will forever get romantic. Torch you, I apologize. Why do programming languages even matter?
*  Okay, well, thank you very much. You're saying why should you care about any one programming
*  language? Or why do we care about programming computers?
*  No, why do we care about programming language design, creating effective programming languages,
*  choosing one programming language versus another programming language, why we keep struggling and
*  improving through the evolution of these programming languages.
*  Sure, sure, sure. Okay, so I think you have to come back to what are we trying to do here,
*  right? So we have these beasts called computers that are very good at specific kinds of things,
*  and we think it's useful to have them do it for us, right? Now, you have this question of
*  how best to express that, because you have a human brain still that has an idea in its head,
*  and you want to achieve something. So, well, there's lots of ways of doing this. You can go
*  directly to the machine and speak assembly language, and then you can express directly
*  what the computer understands. That's fine. You can then have higher and higher and higher levels
*  of abstraction up until machine learning, and you're designing a neural net to do the work for you.
*  The question is where along this way do you want to stop, and what benefits do you get out of doing
*  so? And so programming languages in general, you have C, you have Fortran, Java, and Ada, Pascal,
*  Swift, you have lots of different things. They all have different trade-offs, and they're
*  tackling different parts of the problems. Now, one of the things that most programming languages do
*  is they're trying to make it so that you have pretty basic things like portability across
*  different hardware. So you've got, I'm going to run on an Intel PC, I'm going to run on a RISC-V PC,
*  I'm going to run on ARM phone or something like that. Fine. I want to write one program and have
*  it portable, and this is something that assembly doesn't do. Now, when you start looking at the
*  space of programming languages, this is where I think it's fun, because programming languages
*  all have trade-offs, and most people will walk up to them and they look at the surface level of
*  syntax and say, oh, I like curly braces, or I like tabs, or I like, you know, semi-colons or not,
*  or whatever, right? Subjective, fairly subjective, very shallow things. But programming languages,
*  when done right, can actually be very powerful. And the benefit they bring is expression. Okay.
*  And if you look at programming languages, there's really kind of two different levels to them. One
*  is the down in the dirt, nuts and bolts of how do you get the computer to be efficient,
*  stuff like that, how they work, type systems, compiler stuff, things like that. The other is
*  the UI. And the UI for programming language is really a design problem, and a lot of people don't
*  think about it that way. And the UI, you mean all that stuff with the braces and-
*  Yeah, all that stuff's the UI. And what it is, and UI means user interface. And so what's really
*  going on is it's the interface between the guts and the human. And humans are hard, right? Humans
*  have feelings, they have things they like, they have things they don't like. And a lot of people
*  treat programming languages as though humans are just kind of abstract creatures that cannot be
*  predicted. But it turns out that actually there is better and worse. Like, people can tell when
*  a programming language is good or when it was an accident, right? And one of the things with Swift
*  in particular is that a tremendous amount of time by a tremendous number of people have been put into
*  really polishing and making it feel good. But it also has really good nuts and bolts underneath it.
*  You said that Swift makes a lot of people feel good. How do you get to that point? So
*  how do you predict that tens of thousands, hundreds of thousands of people are going to enjoy
*  using this user experience of this programming language? Well, you can look at it in terms of
*  better and worse, right? So if you have to write lots of boilerplate or something like that,
*  you will feel unproductive. And so that's a bad thing. You can look at it in terms of safety.
*  If like C, for example, is what's called a memory unsafe language. And so you get dangling pointers,
*  and you get all these kind of bugs, but then you have spent tons of time debugging, and it's a real
*  pain in the butt, and you feel unproductive. And so by subtracting these things from the experience,
*  you get happier people. But again, keep interrupting. I'm sorry. But so hard to deal
*  with. If you look at the people, people that are most productive on Stack Overflow,
*  they have a set of priorities that may not always correlate perfectly with the experience of the
*  majority of users. If you look at the most upvoted, quote unquote, correct answer on Stack Overflow,
*  it usually really sort of prioritizes like safe code, proper code, stable code,
*  that kind of stuff. As opposed to like, if I want to use go to statements in my basic,
*  I want to use go to state. What if 99% of people want to use go to statements or use completely
*  improper, unsafe syntax? I don't think that people actually, like if you boil it down and
*  you get below the surface level, people don't actually care about go tos or if statements
*  or things like this. They care about achieving a goal. So the real question is, I want to set up a
*  web server and I want to do a thing, whatever. How quickly can I achieve that? And so from a
*  programming language perspective, there's really two things that matter there. One is what libraries
*  exist and then how quickly can you put it together and what are the tools around that look like?
*  Right? And when you want to build a library that's missing, what do you do? Now, this is where you
*  see huge divergence in the force between worlds. And so you look at Python, for example, Python is
*  really good at assembling things, but it's not so great at building all the libraries. And so you
*  get, because of performance reasons, other things like this, is you get Python layered on top of C,
*  for example. And that means that doing certain kinds of things, well, it doesn't really make
*  sense to do in Python. Instead, you do it in C and then you wrap it and then you have, you're living
*  in two worlds and two worlds never is really great because tooling and the debugger doesn't work
*  right. And like all these kinds of things. Can you clarify a little bit what you mean by Python is
*  not good at building libraries, meaning it doesn't make certain kinds of certain kinds of libraries?
*  No, but just the actual meaning of the sentence. Meaning like it's not conducive to developers to
*  come in and add libraries or is it the duality of the, it's a dance between Python and C and
*  Python?
*  Python's amazing. Python's a great language. I do not mean to say that Python is bad for libraries.
*  What I meant to say is there are libraries that Python's really good at that you can write in
*  Python, but there are other things like if you want to build a machine learning framework,
*  you're not going to build a machine learning framework in Python because of performance,
*  for example, or you want GPU acceleration or things like this. Instead, what you do is you
*  write a bunch of C or C++ code or something like that. And then you talk to it from Python.
*  Right. And so this is because of decisions that were made in the Python design and those
*  decisions have other counterbalancing forces. But the trick when you start looking at this
*  from a programming language perspective, you just sort of say, okay, cool. How do I build this
*  catalog of libraries that are really powerful and how do I make it so that then they can be assembled
*  into ways that feel good and they generally work the first time? Because when you're talking about
*  building a thing, you have to include the debugging, the fixing, the turnaround cycle,
*  the development cycle, all that kind of stuff into the process of building the thing. It's not
*  just about pounding out the code. And so this is where things like catching bugs at compile time
*  is valuable, for example. But if you dive into the details in this, Swift, for example, has certain
*  things like value semantics, which is this fancy way of saying that when you treat a variable like
*  a value, it acts like a mathematical object would. Okay. So you have used PyTorch a little bit.
*  In PyTorch, you have tensors. Tensors are n dimensional grid of numbers. Very simple. You can
*  do plus and other operators on them. It's all totally fine. But why do you need to clone a
*  tensor sometimes? Have you ever run into that? Yeah. Okay. And so why is that? Why do you need
*  to clone a tensor? It's the usual object thing that's in Python. So in Python, and just like
*  with Java and many other languages, this isn't unique to Python. In Python, it has a thing called
*  reference semantics, which is the nerdy way of explaining this. And what that means is you
*  actually have a pointer to a thing instead of the thing. Okay. Now this is due to a bunch of
*  implementation details that you don't want to go into. But in Swift, you have this thing called
*  value semantics. And so when you have a tensor in Swift, it is a value. If you copy it, it looks
*  like you have a unique copy. And if you go change one of those copies, then it doesn't update the
*  other one because you just made a copy of this thing. Right. So that's like highly error prone
*  in at least computer science, math centric disciplines about Python. Like the thing you
*  would expect to behave like math, like math. It doesn't behave like math. And in fact,
*  quietly doesn't behave like math and then can ruin the entirety of your exactly. Well, and then it
*  puts you in debugging land again. Yeah. Right. Now you just want to get something done. And you're
*  like, wait a second. Where do I need to put clone and what level of the stack, which is very
*  complicated, which I thought I was reusing somebody's library. And now I need to understand it to
*  know where to clone a thing. Right. And hard to debug by the way. Exactly. Right. And so this is
*  where programming languages really matter. Right. And so in Swift having value semantics so that
*  both you get the benefit of math working like math. Right. But also the efficiency that comes
*  with certain advantages there, certain implementation details that are really benefit you as a
*  programmer. Right. And so if I the value semantics, like how do you know that things should be treated
*  like a value? Yeah. So, so Swift has a pretty strong culture and good language support for
*  defining values. And so if you have an array, so tensors are one example that the machine
*  learning folks are very used to. Just think about arrays, same thing where you have an array, you
*  create an array, you put two or three or four things into it, and then you pass it off to
*  another function. What happens if that, that function adds some more things to it? Well,
*  you'll see it on the side that you pass it in. Right. This is called reference semantics. Now,
*  what if you pass an array off to a function, it scrolls it away in some dictionary or some other
*  data structure somewhere. Right. Well, it thought that you just handed it that array,
*  but then you return back and that, that, that reference to that array still exists in the
*  caller and they go and put more stuff in it. Right. The person you handed it off to may have
*  thought they had the only reference to that. And so they didn't know what they, that this was going
*  to change underneath the covers. And so this is where you end up having to do clone. So like I was
*  past a thing. I'm not sure if I have the only version of it. So now I have to clone it. So what
*  value semantics does is it allows you to say, Hey, I have a, so in Swift it defaults to value semantics.
*  Oh, so defaults to value semantics. And then because most things should end up being values,
*  then it makes sense for that to be the default. And one of the important things about that is
*  that arrays and dictionaries and all these other collections that are aggregations of other things
*  also have value semantics. And so when you pass this around to different parts of your program,
*  you don't have to do these defensive copies. And so this is, this is great for two sides,
*  right? That's great because you define away the bug, which is a big deal for productivity. The
*  number one thing most people care about, but it's also good for performance because when you're
*  doing a clone, so you pass the array down to the thing, it was like, I don't know if anybody else
*  has it. I have to clone it. Well, you just did a copy of a bunch of data. It could be big.
*  And then it could be that the thing that called you is not keeping track of the old thing. So you
*  just made a copy of it and you may not have had to. And so the way the value semantics work is in
*  Swift is that it uses this thing called copy on right, which means that you get, you get the
*  benefit of safety and performance. And it has another special trick because if you think certain
*  languages like Java, for example, they have immutable strings. And so what they're trying
*  to do is they provide value semantics by having pure immutability. Functional languages have pure
*  immutability in lots of different places. And this provides a much safer model and it provides
*  value semantics. The problem with this is if you have immutability, everything is expensive.
*  Everything requires a copy. For example, in Java, if you have a string X and a string Y,
*  you append them together. We have to allocate a new string to hold X, Y.
*  If they're immutable. Well, and strings and Java are immutable. And if there's optimizations for
*  short ones and it's complicated, but generally think about them as a separate allocation.
*  And so when you append them together, you have to go allocate a third thing
*  because somebody might have a pointer to either of the other ones. Right. And you can't go change
*  them. So you have to go allocate a third thing. Because of the beauty of how the Swift value
*  semantics system works out. If you have a string in Swift and you say, hey, put in X, right. And
*  they say append on Y, Z, W, W, W. It knows that there's only one reference to that. And so it can
*  do an in-place update. And so you're not allocating tons of stuff on the side. You're not, you don't
*  have all those problems. When you pass it off, you can know you have the only reference. If you pass
*  it off to multiple different people, but nobody changes it, they can all share the same thing.
*  So you get a lot of the benefit of, of purely immutable design. And so you get a really nice
*  sweet spot that I haven't seen in other languages. Yeah, that's interesting. Like I thought,
*  I thought there was going to be a, a philosophical like narrative here that you're going to have to
*  pay a cost for it. Cause it sounds like, uh, I think value semantics is beneficial for easing
*  of debugging or minimizing the risk of errors, like bringing the errors closer to the source,
*  um, bringing the symptom of the error closer to the source of the error. However you say that.
*  But you're saying there's not a performance cost either if you implement correctly.
*  Well, so there's, there's trade-offs with everything. And so if you are doing very
*  low level stuff, then sometimes you can notice costs. But then what you're doing is you're saying,
*  what is the right default? So, um, coming back to user interface, when you, when you talk about
*  programming languages, one of the major things that Swift does that makes people love it,
*  that is not obvious when it comes to designing a language is this UI principle of progressive
*  disclosure of complexity. Okay. So Swift, like many languages are, is very powerful.
*  The question is, when do you have to learn the power as a user? So Swift, like Python allows
*  you to start with like print hello world, right? Certain other languages, uh, start with like public
*  static void main classes, like all the ceremony, right? And so you go to teach, you teach a new
*  person, Hey, welcome, welcome to this new thing. Let's talk about public access control classes.
*  Wait, what's that string system dot out print land, like packages, like, right. And so instead,
*  if you take this and you say, Hey, we need, you need, we need packages, you know, modules,
*  we need, we need powerful things like classes, we need data structures, we need like all these
*  things. The question is, how do you factor the complexity and how do you make it so that the
*  normal case scenario is you're dealing with things that work the right way in the right way, give you
*  good performance, the right by default. But then as a power user, if you want to dive down to it,
*  you have full C C performance, full control over low level pointers. You can call Malik if you want
*  to call Malik. This is not recommended on the first page of every tutorial, but it's actually
*  really important when you want to get work done. Right. And so being able to have that is really
*  the design and programming language design and design is really, really hard. It's something that
*  I think a lot of people kind of outside of UI, again, a lot of people just think is subjective,
*  like there's nothing, you know, it's just like curly braces or whatever. It's just like somebody's
*  preference. But actually good design is something that you can feel.
*  And how many people are involved with good design? So if we look at Swift, we'll look at
*  historically, I mean, this might touch like, there's almost like a Steve Jobs question to like,
*  how much dictatorial decision making is required versus collaborative? And we'll talk about how
*  that can go wrong or right. Yeah, but yeah, well,
*  Swift, so I can't speak to in general, all design everywhere. So the way it works with
*  Swift is that there's a core team. And so core team is six or seven people ish, something like
*  that, that is people that have been working with Swift since very early days. And so
*  by early days is not that long ago. Okay. Yeah. So it became public in 2014. So it's been six years
*  public now. But, but so that's enough time that there's a story arc there.
*  Okay. Yeah. And there's mistakes have been made that then get fixed and you learn something and
*  then you, you know, and so that what the core team does is it provides continuity. And so you want to
*  have a, okay, well, there's a big hole that we want to fill. We know we want to fill it. So don't do
*  other things that invade that space until we fill the hole. Right. There's a boulder that's missing
*  here. We want to do, we will do that boulder, even though it's not today. Keep, keep out of that
*  space. And the whole team remembers of the, remembers the myth of the boulder that's there.
*  Yeah. Yeah. There's a general sense of what the future looks like in broad strokes and a
*  shared understanding of that combined with a shared understanding of what has happened in the past
*  that worked out well and didn't work out well. The next level out is you have the, what's called the
*  Swift evolution community. And you've got, in that case, hundreds of people that really care
*  passionately about the way Swift evolves. And that's like an amazing thing to, again, the core
*  team doesn't necessarily need to come up with all the good ideas. You got hundreds of people out
*  there that care about something and they come up with really good ideas too. And that provides this
*  like tumbling rock tumbler for ideas. And so the, the evolution process is, you know, a lot of people
*  in a discourse forum, they're like hashing it out and trying to like talk about, okay, well,
*  should we go left or right? Or if we did this, what would be good? And, you know, here you're
*  talking about hundreds of people, so you're not going to get consensus necessarily, not obvious
*  consensus. And so there's a proposal process that then allows the core team and the community to
*  work this out. And what the core team does is it aims to get consensus out of the community and
*  provide guardrails, but also provide long-term, make sure we're going in the right direction kind
*  of things. So does that group represent like the, how much people will love the user interface? Like
*  you think they're able to capture that? Well, I mean, it's something we talk about a lot. It's
*  something we care about. How well we, how well we do that for debate, but I think that we've done
*  pretty well so far. Is the beginner in mind? Yeah. Like you said, the progressive disclosure.
*  Yeah. So we care a lot about, a lot about that, a lot about power, a lot about efficiency, a lot
*  about there are many factors to good design and you have to figure out a way to kind of
*  work your way through that. And so if you like think about like the language I love is Lisp,
*  probably still because I use Emax, but I haven't done anything, any serious work in this, but
*  it has a ridiculous amount of parentheses. Yeah. I've also, you know, with Java and C plus plus
*  the braces, you know, I, I like, I enjoyed the comfort of being between braces, you know?
*  Yeah. Well, let's,
*  Python is really sorry to interrupt, just like, and last thing to me as a designer,
*  if I was a language designer, God forbid, is I would be very surprised that Python
*  with no braces would nevertheless somehow be comforting also. So like I can see arguments
*  for all of these. But look at this. This is evidence that it's not about braces versus tabs.
*  Right. Exactly. You're good. That's a good point. Right. So like, you know, there's, there's evidence
*  that, but see, like it's one of the most argued about things. Oh yeah. Of course. Just like tabs
*  and spaces, which it doesn't, I mean, there's one obvious right answer, but it doesn't, it doesn't
*  actually matter. What's that? Come on, we're friends. Like, what are you trying to do to me here?
*  People are going to, yeah, half the people are going to tune out. Yeah. So, so, so these,
*  you're able to identify things that don't really matter for the experience.
*  Well, no, no, no, it's, it's, it's always a really hard. So the easy decisions are easy, right? I mean,
*  you can find, those are not the interesting ones. The hard ones are the ones that are most
*  interesting, right? The hard ones are the places where, Hey, we want to do a thing.
*  Everybody agrees we should do it. There's one proposal on the table, but it has all these
*  bad things associated with it. Well, okay. What are we going to do about that? Do we just take it?
*  Do we delay it? Do we say, Hey, well, maybe there's this other feature that if we do that first,
*  this will work out better. How does this, if we do this, are we painting ourselves into a corner?
*  Right. And so this is where, again, you're having that core team of people that
*  has some continuity and has perspective, has some of the historical understanding is really valuable
*  because you get, it's not just like one brain, you get the power of multiple people coming together
*  to make good decisions. And then you get the best out of all these people. And you also can harness
*  the community around it. What about like the decision of whether like in Python having one type
*  or having, you know, a strict typing? Yeah. Okay. Yeah. Let's talk about this. So, so, um,
*  I like how you put that by the way, like, so, so many people would say that Python doesn't have
*  types. Doesn't have types. Yeah. But you're right. I've listened to you enough to where,
*  I'm a fan of yours and I've listened to way too many podcasts and videos. If you're talking about
*  this. Oh yeah. So I would argue that Python has one type. And so, um, so like when you import
*  Python and Swift, which by the way, works really well, you have everything comes in as a Python
*  object. Now here, there are trade-offs because, um, uh, you know, it depends on where you're
*  optimizing for. And Python is a super successful language for really good reason. Um, because it
*  has one type, uh, you get duck typing for free and things like this, but also you're pushing,
*  you're making it very easy to pound out code on one hand, but you're also making it very easy
*  to introduce, uh, complicated bugs that you have to debug. And you pass a string into something
*  that expects an integer and it doesn't immediately die. It goes all the way down the stack trace.
*  And you find yourself in the middle of some code that you really didn't want to know anything about
*  and it blows up and you're just saying, well, what did I do wrong? Right. And so types are good and
*  bad and they have trade-offs are good for performance and certain other things, depending on where
*  you're coming from, but it's all about trade-offs. And so this is, this is what design is, right?
*  Design is about weighing trade-offs and trying to understand the ramifications of the things
*  that you're weighing like types or not, or one type or many types. Um, but also within many types,
*  how powerful do you make that type system is another very complicated question, uh, with lots
*  of trade-offs. It's very interesting by the way. Uh, but, uh, but that's like one, one dimension.
*  And there's a bunch of other dimensions, JIT compiled versus static compiled garbage collected
*  versus reference counted versus memory, man, manual memory management versus, you know, like,
*  in like all these different trade-offs and how you balance them or what make a program language
*  good concurrency. Yep. So in all those things, I guess, uh, when you're designing the language,
*  you also have to think of how that's going to get all compiled down to.
*  If you care about performance. Yeah. Well, and go back to list, right? So list also, I would say
*  JavaScript is another example of a very simple language. Right. And so one of the, so I also love
*  Lisp. I don't use it as much as maybe you do or you did. No, I think we're both everyone who loves
*  Lisp. It's like you love, it's like, uh, I don't know. I love Frank Sinatra, but like, how often
*  do I seriously listen to Frank Sinatra? Sure. But, but, but you look at that or you look at
*  JavaScript, which is another very different, but relatively simple language. And there's certain
*  things that don't exist in the language, but there's, there is inherent complexity to the
*  problems that we're trying to model. And so what happens to the complexity in the case of, uh,
*  both of them, for example, you say, well, what about large scale software development? Okay.
*  Well, you need something like packages. Neither language has a language affordance for packages.
*  And so what you get is patterns. You get things like NPN, you get things like, you know, like these
*  ecosystems that get built around. And I'm a believer that if you don't, uh, model at least
*  the most important inherent complexity in the language, then what ends up happening is that
*  complexity gets pushed elsewhere. And when it gets pushed elsewhere, sometimes that's great
*  because often building things as libraries is very flexible and very powerful and allows you to evolve
*  and things like that. But often it leads to a lot of, uh, unnecessary divergence in the force and
*  fragmentation. And, and when that happens, you just get kind of a mess. And so the question is,
*  how do you, how do you balance that? Uh, don't put too much stuff in the language. Cause that's
*  really expensive and makes things complicated. But how do you model enough of the inherent
*  complexity of the problem that, um, you provide the framework and the structure for people to
*  think about? Well, so, so the, the, the, the key thing to think about with, uh, with programming
*  languages and you think about what a programming language is there for is it's about making a human
*  more productive. Right. And so like there's an old, I think it's a Steve jobs quote about, um,
*  it's a bicycle for the mind. Right. You can, you can, you can definitely walk,
*  but it'll get there a lot faster if you can bicycle on your way. And a programming language
*  is a bicycle for the mind. Yeah. Is it basically a, wow, that's a really interesting way to think
*  about it. But by raising the level of abstraction, now you can fit more things in your head by being
*  able to just directly leverage somebody's library. You can now get something done quickly. Um, in the
*  case of Swift, Swift UI is this new framework that Apple has released recently for doing UI programming
*  and it has this declarative programming model, which defines a way entire classes of bugs. It's
*  make it builds on value semantics and many other nice Swift things. And what this does is allows
*  you to just get way more done with way less code. And now your productivity as a developer is much
*  higher. Right. And so that that's really the, what programming languages should be about is it's not
*  about tabs versus spaces or curly braces or whatever. It's about how productive do you make
*  the person. And you can only see that when you have libraries that were built with the right
*  intention that the language was designed for. And with Swift, I think we're still a little bit early.
*  But Swift UI and many other things that are coming out now are really showing that. And I think that
*  they're opening people's eyes. It's kind of interesting to think about like how that, you know,
*  the knowledge of something of how good the bicycle is, how people learn about that, you know, so I've
*  used C plus plus. Now this is not going to be a trash talking session about C plus plus, but you
*  see plus plus for a really long, I feel like I spent many years without realizing like there's
*  languages that could, for my particular lifestyle, brain style, thinking style, there's languages
*  that could make me a lot more productive in the debugging stage, in the, just the development
*  stage and thinking like the bicycle for the mind that I could fit more stuff into my.
*  Python's a great example of that, right? I mean, a machine learning framework in Python is a great
*  example of that. It's just very high abstraction level. And so you can be thinking about things on
*  a like very high level algorithmic level instead of thinking about, okay, well, am I copying this
*  tensor to a GPU or not? Right. It's not, it's not what you want to be thinking about.
*  And as I was telling you, I mean, I guess the question I had is, you know, how does a person
*  like me or general people discover more productive, you know, languages like how I was,
*  as I've been telling you offline, I've been looking for like a project to work on in swift
*  so I can really try it out. I mean, my intuition was like doing a hello world is not going to get
*  me there to get me to experience the power of the language. You need a few weeks to change
*  your metabolism. Exactly. I didn't think that beautifully, but that's one of the problems with
*  people with diets. Like I, I'm actually currently to go in parallel, but in a small tangent is
*  I've been recently eating only meat. Okay. Okay. And okay. So most people are like,
*  the thing that's horribly unhealthy or whatever you have like a million,
*  whatever the science is, it just doesn't sound right.
*  Well, so, so back when I was in college, we did the Atkins diet. That was, that was a thing.
*  And similar. And, but if you, you have to always give these things a chance. I mean, with dieting,
*  I was not dieting, but it's just the things that you like. If I eat personally, if I eat meat,
*  just everything I can be super folk or more focused than usual. I just feel great. I mean,
*  I've been running a lot of, you know, doing pushups and posts and so on. And you Python is similar
*  in that sense for me. Where are you going with this? I mean, literally, I just, I felt I had like a
*  stupid smile on my face when I first started using Python, I could code up really quick things. Like,
*  I, like I, I would see the world. I'll be empowered to write a script to, to, you know, to do some
*  basic data processing, to rename files on my computer. Right. And like Pearl didn't do that for me.
*  Uh, uh, a little bit.
*  Well, and again, like none of these are about which, which is best or something like that,
*  but there's definitely better and worse here.
*  But it clicks. Right. Well, yeah.
*  If you look at Pearl, for example, you get bogged down in, uh, scalars versus arrays versus hashes
*  versus type globs and like all that kind of stuff. And, and Python's like, yeah, let's not do this.
*  And some of it is debugging. Like everyone has different priorities, but for me it's,
*  can I create systems for myself that empower me to debug quickly? Like I've always been
*  a big fan, even just crude, like asserts, like always, uh, stating things that should be true,
*  which in Python I found in myself do more because of type, all these kinds of stuff.
*  Well, you could think of types in a program language as being kind of assert.
*  Yeah. They get checked at compile time. Right. Um, so how do you learn anything? Well, so this,
*  or how do, how do people learn new things? Right. This, this is hard. Uh, people don't like to change.
*  People generally don't like change around them either. And so, uh, we're all very slow to adapt
*  and change. And usually there's a catalyst that's required to, to force yourself over the, over,
*  over this. So for learning a programming language, it really comes down to finding an excuse,
*  like build a thing that, that's, that the language is actually good for that the ecosystem's ready
*  for. Um, and so, um, and so if you were to write an iOS app, for example, that'd be the easy case.
*  Obviously you would, you would use Swift for that. Right. There are other,
*  Android, uh, so Swift runs on Android. Oh, does it? Oh yeah. Yeah. Swift runs in lots of places.
*  So, uh, okay. So Swift, Swift, Swift is built on top of LLVM. LLVM runs everywhere. LLVM,
*  for example, builds the Android kernel. Oh, okay. So yeah. Um, so I didn't realize this.
*  Yeah. So Swift, Swift is very portable, runs on windows. There's, it runs on lots of different
*  things. And, uh, Swift, sorry to interrupt, uh, Swift UI, and then there's a thing called UI kit.
*  So can I built an app with Swift? Uh, well, so that, that's the thing is the ecosystem is
*  what matters there. So Swift UI and UI kit are Apple technologies. Okay. Got it. And so they
*  happen to like Swift UI happens to be written in Swift, but it's an Apple proprietary framework
*  that, um, Apple loves and wants to keep on its platform, which makes total sense. You go to,
*  go to Android and you don't have that library. Right. And so Android has a different ecosystem
*  of things that hasn't been built out and doesn't work as well with Swift. And so you can totally
*  use Swift to do, uh, like arithmetic and things like this, but building UI with Swift on Android
*  is not, not, not a, not a great example right now. So, so if I wanted to, uh, so learn Swift,
*  what's the pro, I mean, the one practical different version of that is, um,
*  Swift for TensorFlow, for example. And one of the inspiring things for me with both TensorFlow and
*  PyTorch is how quickly the community can like switch from different libraries. Like you could
*  see some of the communities switching to PyTorch now, but it's very easy to see. And then TensorFlow
*  is really stepping up its game. And then there's no reason why I think the way it works is basically
*  there has to be one GitHub repo, like one paper steps up, gets people excited, gets people excited
*  and they're like, ah, I have to learn this Swift for what, what Swift again. And then they learn
*  and they fall in love with them. I mean, that's what happened. Yeah. There has to be a reason,
*  a catalyst. And so, and, and there, I mean, people don't like change, but it turns out that once
*  you've worked with one or two programming languages, the basics are pretty similar.
*  And so one of the fun things about learning programming languages, even, even maybe Lisp,
*  I don't know if you agree with this, is that when you start doing that, you start learning new things
*  because you have a new way to do things and you're forced to do them. And that forces you to explore
*  and it puts you in learning mode. And when you get in learning mode, your mind kind of opens a
*  little bit and you can, you can see things in a new way, even when you go back to the old place.
*  Right. Yeah. So it was Lisp was functional stuff, but I wish there was a kind of window.
*  Maybe you can tell me if there is a, there you go. This is a question to ask. What is the most
*  beautiful feature in a programming language? Before I ask it, let me say like with Python,
*  I remember I saw list comprehensions. It was like when I like really took it in. I don't know. I
*  just loved it. It was like fun to do. Like it was fun to do that kind of, um, uh, it was something
*  about it to be able to filter through a list and to create a new list on a single line was elegant.
*  I could all get into my head and it just made me, um, fall in love with the language. So is there,
*  let me ask you a question. Uh, is there what to use the most beautiful feature in, uh, in a program
*  language is that you've ever encountered in Swift maybe. And then outside of Swift.
*  I think the thing that I like the most from a programming language. So, so I think the thing
*  you have to think about with the programming language, again, what is the goal? You're trying
*  to get people to get things done quickly. And so you need libraries, you need high quality libraries,
*  and then you need a user base around them that can assemble them and do cool things with them.
*  Right. And so to me, the question is what enables high quality libraries?
*  Okay. Yeah. And there's a huge divide in the world between libraries who enable high quality
*  libraries versus, um, the ones that put special stuff in the language. So programming languages
*  that enable high quality libraries got it. So, so, and what I mean by that is expressive libraries
*  that then feel like a natural integrated part of the language itself. So, um, an example of this
*  in Swift is the int and float and also array and string, things like this. These are all part of
*  the library. Like int is not hard coded into Swift. And so what that means is that because
*  int is just a library thing to find in the standard library, along with strings and arrays and all the
*  other things that come with the standard library. Um, well, hopefully you do like int, but anything
*  that any language features that you needed to define int, you can also use in your own types.
*  So if you wanted to find a, uh, uh, quaternion or something like this, right. Um, well, it doesn't
*  come in the standard library. Um, there's a very special set of people that care a lot about this,
*  but those people are also important. It's not, it's not about classism, right? It's not about
*  the people who care about instant floats are more important than the people who care about
*  quaternions. And so to me, the beautiful things about programming languages is when you allow
*  those communities to build high quality libraries that feel native, that feel like they're built
*  into the built into the compiler without having to be. What does it mean for the int to be part
*  of a not hard coded in? So is it like how, so what isn't, what is an int? Okay.
*  It's just a integer. In this case, it's like a, you know, like a 64 bit integer or something like
*  this. But so like the 64 bit is hard coded or no, no, none of that's hard coded. So int,
*  if you go look at how it's implemented, it's just a struct and Swift. And so it's a struct.
*  And then how do you add two structs? Well, you define plus. And so you can define plus on int.
*  Well, you can define plus on your thing too. You can define, uh, int has like an is odd method or
*  something like that on it. And so, yeah, you can add methods on the things. Yeah. Uh, so you can,
*  you can find operators like how it behaves. That's used beautiful when there there's something about
*  the language, which enables others to create libraries, which are, um, not hacky. Yeah.
*  They feel, they feel native. And so one of the best examples of this is Lisp, right? Because in
*  Lisp, all like all the libraries are basically part of the language, right? You write term rewrite
*  systems and things like this. And so can you, as a counter example, provide what makes it difficult
*  to write a library that's native? Is it the Python C? Well, so, well, so one example,
*  I'll give you two examples, um, a Java and C plus plus there's Java and C. Um, they both allow you
*  to define your own types. Um, but int is hard coded in the language. Okay. Well, why? Well, in,
*  in Java, for example, coming back to this whole reference, manic value, semantic thing, um,
*  int gets passed around by value. Yeah. But if you, if you make, if you make like a pair or
*  something like that, a complex number, right? It's a, it's a class in Java and now it gets passed
*  around by reference by pointer. And so now you lose value semantics, right? You lost math. Okay.
*  Well, that's not great, right? If you, if you can do something with in, why can't I do it with my
*  type? Right. So that's, that's the, the negative side of the thing I find beautiful is when you
*  can solve that, when you can have full expressivity, where you, as a user of the language have
*  as much or almost as much power as the people who implemented all the standard built-in stuff,
*  because what that enables is that enables truly beautiful libraries.
*  You know, it's kind of weird because I've gotten used to that. Uh, that's one, I guess, other
*  aspect of program language design. You have to think, you know, the old first principles thinking
*  like, why are we doing it this way? By the way, I mean, I remember it because I was thinking about
*  the Wallace operator and I'll ask you about it later, but it hit me that like the equal sign for
*  assignment. Yeah. Like why are we using the equal sign? It's wrong. And that's not the only solution.
*  Right. So if you look at Pascal, they use colon equals or assignment and equals for, um, for
*  equality. And they use like less than greater than instead of the not equal. Yeah. Like there are
*  other answers here. So, but like, and yeah, like ask, ask you all, but how do you then decide,
*  uh, to break convention to say, you know what, everybody's doing it wrong. We're going to do it.
*  Right. Yeah. So, so it's like an ROI, like return on investment trade off. Right. So if you do
*  something weird, let's just say like, not like colon equal instead of equal for assignment,
*  that would be weird with today's aesthetic. Right. And so you'd say, cool, this is theoretically
*  better, but is it better in which ways? Like, what do I get out of that? Do I define away class of
*  bugs? Well, one of the class of bugs that C has is that you can use like, you know, if X equals
*  without equals equals F X equals Y. Yeah. Right. Well, it turns out you can solve that problem in
*  lots of ways. Clang, for example, GCC, all these compilers will detect that as a, as a likely bug,
*  produce a warning. Do they? Yeah. I feel like they didn't or clang. GCC didn't. Uh, it's like
*  one of the important things about programming language design is like, you're literally creating
*  suffering in the world. Okay. Like, like I feel like, I mean, one way to see it is the bicycle
*  for the mind, but the other way is to like minimizing suffering. Well, you have to decide
*  if it's worth it. Right. And so let's come back to that. Okay. But, um, but if you, if you look at
*  this and again, this is where there's a lot of detail that goes into each of these things. Um,
*  equal and C returns a value. Yep. That's messed up. That allows you to say X equals Y equals Z.
*  Like that works and see, um, is it messed up? You know, well, so that most people think it's
*  messed up. I think, uh, it is very by messed up. What I mean is it is very rarely used for good
*  and it's often used for bugs. Yeah. Right. And so that's a good definition of stuff. Yeah. You
*  could use, you know, it's, it's a, in hindsight, this was not such a great idea, right? Now,
*  one of the things with Swift that is really powerful and one of the reasons it's actually good,
*  versus it being full of good ideas is that, um, when, when we launched the phone, we announced
*  that it was public, people could use it, people could build apps, but it was going to change and
*  break. Okay. When Swift two came out, we said, Hey, it's open source. And there's this open
*  process, which people can, uh, help evolve and direct the language. So the community at large,
*  like Swift users can now help shape the language as it is. And what happened is that part as part
*  of that process is a lot of really bad mistakes got taken out. So for example, Swift used to have
*  the C style plus plus and minus minus operators. Like, what does it mean when you put it before
*  versus after? Right. Well, that got cargo culted from C into Swift or cargo culted,
*  cargo culted means, uh, brought forward without really considering, considering it. Okay. Um,
*  this is maybe not the most PC term, but, uh, look it up in urban dictionary. Yeah. Yeah. So it got
*  pulled, it got pulled into C without, or it got pulled into Swift without very good consideration.
*  And we went through this process and one of the first things got ripped out was plus plus and
*  minus minus because they lead to confusion. They have very little value over saying, you know,
*  X plus equals one and X plus equals one is way more clear. And so when you're optimizing for
*  teachability and clarity and bugs and this multidimensional space that you're looking at,
*  things like that really matter. And so being a first principles on where you're coming from
*  and what you're trying to achieve and being anchored on the objective is really important.
*  Well, let me ask you about, uh, the most, uh, sort of this, this, uh, this, this podcast isn't
*  about information. It's about drama. So let me talk to you about some drama. So you mentioned
*  Pascal and, uh, colon equals, uh, there's something that's called the walrus operator.
*  And, uh, Python, uh, in Python 3.8 added the walrus operator. And the reason I think it's
*  interesting, uh, it's not just because of the feature it does, it's, it has the same kind of
*  expression feature. You can actually see that it returns the value of the assignment. And maybe
*  you can comment on that in general, but on the other side of it, it's also the thing that, that,
*  uh, uh, toppled the dictator. Uh, so it finally drove Guido to, uh, step down from VDFL,
*  the toxicity of the community. So maybe, um, what do you think about the walrus operator in,
*  in Python? Is there an equivalent thing in Swift that really, uh, stress tested the community?
*  And, uh, and then on the flip side, what do you think about Guido stepping down over it?
*  Yeah. Well, if you, like, if I look past the details of the walrus, walrus operator,
*  one of the things that makes it most polarizing is that it's syntactic sugar.
*  Okay. What do you mean by syntactic sugar? It means you can take something that already exists
*  in language and you can express it in a more concise way. So, okay, I'm going to play a
*  double advocate. So, uh, this is great. Uh, is that objective or subjective statement? Like,
*  can you, can you argue that basically anything is syntactic sugar or not? Uh,
*  uh, no, you, not everything is syntactic sugar. So for example, um, the type system, like, can you
*  have classes versus, uh, versus, uh, like, do you have types or not? Right. So, so one type versus
*  many types is not something that affects syntactic sugar. And so if you say, I want to have the
*  ability to define types, I have to have all this like language mechanics to define classes and,
*  oh, now I have to have inheritance and I have like, I have all this stuff. That's just making
*  language more complicated. That's not, that's not about sugaring it. Um, Swift has the sugar.
*  So like Swift has this thing called if let, and it has, uh, various operators are used to concisify,
*  uh, specific use cases. So the problem with syntactic sugar, when you're talking about,
*  Hey, I have a thing that takes a lot to write and I have a new way to write it.
*  You have this like horrible trade-off, which becomes almost completely subjective, which is
*  how often does this happen and does it matter? And one of the things that is true about human
*  psychology, particularly when you're talking about introducing a new thing is that, uh, people over,
*  overestimate the burden of learning something. And so it looks foreign when you haven't gotten
*  used to it. But if it was there from the beginning, of course, it's just part of Python, like
*  unquestionably, like this is, this is just the thing I know. And it's not a new thing that you're
*  worried about learning. It's just part of, part of the deal. Now with Guido, uh, I don't know Guido
*  well. Um, yeah, have you passed across much? Yeah, I've met him a couple of times, but I don't know,
*  no Guido well, but the, the sense that I got out of that whole dynamic was that he had put the,
*  not just the decision maker weight on his shoulders, but it was so tied to his personal identity
*  that, um, he took it personally and he felt the need and he kind of put himself in the situation
*  of being the person instead of building a base of support around him. I mean, he, this is probably
*  not quite literally true, but by too much. So there's too much, too much concentrated on him.
*  Right. And so, and that can wear you down. Well, yeah, particularly because people then say Guido,
*  you're a horrible person. I hate this thing, blah, blah, blah, blah, blah, blah, blah. And sure,
*  it's like, you know, maybe 1% of the community that's doing that, but Python's got a big community
*  and 1% of millions of people is a lot of hate mail and that just from human factor will just
*  wear on you. What to clarify, it looked from just what I saw in the messaging for the, let's not look
*  at the million Python users, but at the Python core developers, it feels like the majority,
*  the big majority on a vote were opposed to it. Okay. I'm not that close to it. So, so, so this,
*  okay. So the situation is like literally, uh, yeah, I mean the majority of the core developers,
*  they're gonna repose it. So I, and they weren't, they weren't even like against it.
*  It was, uh, there was a few, well, they were against it, but the, the against it wasn't like,
*  this is a bad idea. They were more like, we don't see why this is a good idea.
*  And what that results in is there's a stalling feeling. Like you, you just slow things down.
*  Now, from my perspective, that you could argue this. And I think it's a very, it's very
*  interesting if we look at politics today and the way Congress works, it's slowed down everything.
*  It's a dampener. Yeah, it's a dampener, but like that's a dangerous thing too,
*  because if it dampens things like, you know, dampening results. What are you talking about?
*  Like it's a low pass filter, but if you need billions of dollars injected into the economy
*  or trillions of dollars, then suddenly stuff happens. Right. And so for sure. So you're
*  talking about, I'm not defending our political situation just to be clear, but you're talking
*  about like a global pandemic. I was hoping we could fix like the healthcare system and the
*  education system. Like, you know, I'm not, I'm not a politics person. I don't, I don't, I don't know.
*  When it comes to languages, the community is kind of right in terms of, it's a very high burden to
*  add something to a language. So as soon as you add something, you have a community of people building
*  on it and you can't remove it. Okay. And if there's a community of people that feel really
*  uncomfortable with it, then taking it slow, I think is, is, is an important thing to do. And
*  there's no rush, particularly if it was something that's 25 years old and is very established and,
*  you know, it's not like coming, coming into its own. What about features? Well, so I think that
*  the issue with, with Guido is that maybe this is a case where he realized that had outgrown him
*  and it went from being the language. So Python, I mean, Guido is amazing, but, but Python isn't
*  about Guido anymore. It's about the users. And to a certain extent, the users own it. And,
*  you know, Python, Guido spent years of his life, a significant fraction of his career on Python.
*  And from his perspective, I imagine he's like, well, this is my thing. I should be able to do
*  the thing I think is right, but you can also understand the users where they feel like,
*  you know, this is my thing. I use this like, and, and I don't know, it's, it's a hard,
*  it's a hard thing. But what, if we could talk about leadership in this, cause it's so interesting to
*  me, I'm going to, I'm going to make, I'm going to work. Hopefully somebody makes it. If not,
*  I'll make it a water. So I'll put it in a shirt because I think it represents to me,
*  maybe it's my Russian roots or something. You know, it's the burden of leadership, like,
*  I feel like to push back, I feel like progress can, like most difficult decisions, just like you said,
*  there'll be a lot of division, division in the solar, especially in the passionate community.
*  It just feels like leaders need to take those risky decisions that, that if you like listen,
*  that was some non-zero probability, maybe even a high probability will be the wrong decision,
*  but they have to use their gut and make that decision.
*  Well, this is like one of the things where you see amazing founders, the founders understand
*  exactly what's happened and how the company got there and are willing to say to, we have been
*  doing thing X the last 20 years, but today we're going to do thing Y and they make a major pivot
*  for the whole company. The company lines up behind them, they move and it's the right thing.
*  But then when the founder dies, the successor doesn't always feel that, that agency to be able
*  to make those kinds of decisions. Even though they're a CEO, they could theoretically do
*  whatever. There's two reasons for that, in my opinion, or in many cases, it's always different,
*  but one of which is they weren't there for all the decisions that were made. And so they don't
*  know the principles in which those decisions were made. And once the principles change,
*  you should be obligated to change what you're doing and change direction.
*  Right. And so if you don't know how you got to where you are, it just seems like gospel.
*  And you're not going to question it. You may not understand that it really is the right thing to
*  do. So you just may not see it. That's so brilliant. I never thought of it that way. Like this,
*  it's so much higher burden. When as a leader, you step into a thing that's already worked for a long
*  time. Yeah. Yeah. Well, and if you change it and it doesn't work out, now you're the person who
*  screwed it up. People always second guess that. Yeah. And the second thing is that even if you
*  decide to make a change, even if you're theoretically in charge, you're just a person
*  that thinks they're in charge. Meanwhile, you have to motivate the troops. You have to explain it
*  to them in terms of understand, you have to get them to buy into and believe in it. Because if
*  they don't, then they're not going to be able to make the turn. Even if you tell them, you know,
*  their bonuses are going to be curtailed. They're just not going to like buy into it, you know?
*  And so there's only so much power you have as a leader. And you have to understand what that
*  what those limitations are. Are you still BDFL? You've been a BDFL of some stuff.
*  You're very heavy on the B, the benevolent, benevolent, dictated for life. I guess LVM.
*  Yeah. So I still lead the LVM world. I mean, what's the role of so then on Swift,
*  you said that there's a group of people. Yeah. So if you contrast Python with Swift, right,
*  one of the reasons so everybody on the core team takes the role really seriously. And I think we
*  all really care about where Swift goes. But you're almost delegating the final decision making to the
*  wisdom of the group. And so it doesn't become personal. And also, when you're talking with the
*  community, so yeah, some people are very annoyed at certain decisions get made. There's a certain
*  faith in the process, because it's a very transparent process. And when a decision gets
*  made, a full rationale is provided, things like this, these are almost defense mechanisms
*  to help both guide future discussions and provide case law and like Supreme Court does about
*  this decision was made for this reason. And here's the rationale and what we want to see more of or
*  less of. But it's also a way to provide a defense mechanism. So that when somebody is griping about
*  it, they're not saying that person did the wrong thing. They're saying, well, this this thing sucks
*  and later they move on and they get over it. Yeah, the analogy of the Supreme Court, I think is really
*  is really good. But then, okay, not to get personal on the swift team. But like, is there is there a
*  division? Like, it just seems like it's impossible for their for division not to emerge. Well, each
*  of the humans on the swift core team, for example, are different. And the membership of the Swift
*  core team changes slowly over time, which is, I think a healthy thing. And so each of these
*  different humans have different opinions. Trust me, that's not it's not a singular consciousness
*  of by any stretch of the imagination. You've got three major organizations, including Apple, Google
*  and sci fi of all working together and, and it's a small group of people, but you need high trust,
*  you need again, it comes back to the principles of what you're trying to achieve, and understanding,
*  you know, what what you're optimizing for. And I think that starting with strong principles and
*  working towards decisions is always a good way to both make wise decisions in general, but then be
*  able to communicate them to people so that they can buy into them. And that that is hard. And so
*  you mentioned LVM LVM is gonna be 20 years old this December. So it's it's showing its own age.
*  Do you have like, like a like a like a dragon cake plan? Or do you have?
*  No, I should definitely do that. Yeah, if we can have a pandemic cake,
*  pandemic cake, everybody gets a slice of cake, and it gets, you know, sent through email.
*  But the but LVM has had tons of its own challenges over time, too, right. And one of the challenges
*  that the LVM community has, in my opinion, is that it has a whole bunch of people that
*  have been working on LVM for 10 years, right, because this happens somehow. And LVM has always
*  been one way, but it needs to be a different way. Right. And they've worked on it for like 10 years
*  is a long time to work on something. And, you know, you suddenly can't see the faults in the
*  thing that you're working on. And LVM has lots of problems, and we need to address them and we need
*  to make it better. And if we don't make it better than somebody else will come up with a better idea.
*  Right. And so it's just kind of of that age where the community is like in danger of getting too
*  calcified. And, and so I'm happy to see new projects joining and new things mixing it up,
*  you know, Fortran is now a new a new thing in the LVM community, which is various and good.
*  I've been trying to find on this little tangent, find people who program in Cobalt or Fortran,
*  Fortran, especially to talk to it. They're hard to find.
*  Yeah. Look to the scientific community. They still use Fortran quite a bit.
*  Interesting thing you kind of mentioned with LVM or just in general,
*  that if something evolved, you're not able to see the faults. So do you fall in love with the thing
*  over time or do you start hating everything about the thing over time?
*  Well, so my personal folly is that I see maybe not all, but many of the faults
*  and they grate on me and I don't have time to go fix them.
*  Yeah. And they get magnified over time.
*  Well, and they may not get magnified, but they never get fixed. And it's like sand underneath,
*  you know, this just like grating against you. And it's like sand underneath your fingernails
*  or something. It's just like, you know, it's there, you can't get rid of it.
*  Um, and so the problem is that if other people don't see it, right, nobody ever get like,
*  I can't go, I don't have time to go write the code and fix it anymore. But then, uh,
*  people are resistant to change. And so you say, Hey, we should go fix this thing. They're like,
*  Oh yeah, that sounds risky. Well, is it the right thing or not?
*  Are the challenges, uh, the group dynamics or is it also just technical? I mean,
*  some of these features like, yeah, I think, uh, as an observer is almost like a fan in, in the, uh,
*  you know, as a spectator of the whole thing, I don't often think about, you know, some things
*  might actually be technically difficult to implement. Example, this is we, we built this
*  new compiler framework called MLR. Yes. MLR is this a whole new framework. It's not many people
*  think it's about machine learning. The ML stands for multi-level because compiler people can't name
*  things very well. I guess we dig into what MLR is. Yeah. So when you look at compilers, compilers
*  have historically been solutions for a given space. So LLVM is a, it's really good for dealing with
*  CPUs. Let's just say at a high level and you look at, um, Java and Java has a JVM. The JVM is very
*  good for garbage collected languages that need dynamic compilation. And it's very optimized for
*  specific space. And so hotspot is one of the compilers that gets you in that space. And that
*  compiler is really good at that kind of stuff. Um, usually when you build these domain specific
*  compilers, you end up building whole thing from scratch for each domain. Uh, what's the domain?
*  So what, what, what's the, what's the scope of a domain? Well, so here I would say like, if you
*  look at Swift, there's several different parts to the Swift compiler. Um, one of which is covered by,
*  um, the LLVM part of it. There's also a high level piece that's specific to Swift and there's
*  a huge amount of redundancy between those two different infrastructures and a lot of re
*  re-implemented stuff that is similar but different. What is LLVM define? LLVM is effectively an
*  infrastructure. So you can mix and match it in different ways. It's built out of libraries.
*  You can use it for different things, but it's really good at CPUs and GPUs, CPUs and like the
*  tip of the iceberg on GPUs. It's not really great at GPUs. Okay. Um, but it turns out-
*  Bunch of languages that- That then use it to talk to CPUs.
*  Got it. Um, and so it turns out there's a lot of hardware out there that is custom accelerators.
*  So machine learning, for example, there are a lot of, uh, matrix multiply accelerators and things
*  like this. There, there's a whole world of hardware synthesis. So we're using MLIR to
*  build circuits. Okay. And so you're compiling for a domain of transistors.
*  And so what MLIR does is it provides a tremendous amount of compiler infrastructure that allows you
*  to build these domain specific compilers in a much faster way and have the result be good.
*  If we're, if we're thinking about the future, now we're talking about like ASICs. So anything.
*  Yeah. Yeah. So if we project into the future, it's very possible that the number of these kinds of
*  ASICs, very specific, uh, infrastructure thing, the architecture things, uh,
*  like multiplies exponentially. I hope so. Yeah. So that's MLIR.
*  So what MLIR, what MLIR does is it allows you to build these compilers very efficiently.
*  Right now, one of the things that coming back to the LLVM thing, and then we'll go to hardware
*  is, um, LLVM is a, is a specific compiler for specific domain. MLIR is now this very general,
*  very flexible thing that can solve lots of different kinds of problems. So LLVM is a subset of
*  what MLIR does. So MLIR is, I mean, it's an ambitious project then. Yeah. It's a very ambitious
*  project. Yeah. And so to make it even more confusing, MLIR has joined the LLVM umbrella
*  project. So it's part of the LLVM family. Right. Um, but where this comes full circle is now folks
*  that work on the LLVM part, the classic part that's 20 years old, um, aren't aware of all
*  the cool new things that have been done in the new, the new thing that, you know, MLIR was built by
*  me and many other people that knew a lot about LLVM. And so we fixed a lot of the mistakes that
*  lived in LLVM. I mean, now you have this community dynamic where it's like, well, there's this new
*  thing, but it's not familiar. Nobody knows it. It feels like it's new. And so let's not trust it.
*  And so it's just really interesting to see the cultural social dynamic that comes out of that.
*  And, you know, I think it's super healthy because we're seeing the ideas percolate and we're seeing
*  the technology diffusion happen as people get more comfortable with it. They start to understand
*  things in their own terms. And this just gets to the, it takes a while for ideas to propagate,
*  even though, um, they may be very different than what people are used to. Maybe let's talk about
*  that a little bit. The world of ASICs and well, actually you're, um, you're, you have a new role
*  at Sci5. What's that place about? What is the vision for their vision for, I would say the future
*  of computer. So I lead the engineering and product teams at Sci5. Sci5 is a company who's was founded
*  with this architecture called RISC-V. RISC-V is a new instruction set. Instruction sets are the
*  things inside of your computer that tell it how to run things. Um, x86 from Intel and ARM from
*  the ARM company and things like this or other instruction sets. I've talked to, sorry, I talked
*  to Dave Patterson, who's super excited about RISC-V. Dave is awesome. He's brilliant. Yeah.
*  The, uh, RISC-V is distinguished by not being proprietary. And so x86 can only be made by Intel
*  and AMD. ARM can only be made by ARM. They sell licenses to build arm ships to other companies,
*  things like this. MIPS is another instruction set that is owned by the MIPS company, now WAVE,
*  and then it gets licensed out, things like that. Um, and so RISC-V is an open standard that anybody
*  can build chips for. And so Sci5 was founded by three of the founders of RISC-V that designed
*  and built it in Berkeley, working with Dave. Um, and so that was the, the genesis of the company.
*  Sci5 today has some of the world's best RISC-V cores and we're selling them and that's really
*  great. They're going to tons of products. It's very exciting. Um, so they're taking this, uh,
*  thing that's open source and just being, uh, trying to be, or are the best in the world at
*  building these things. Yeah. So here it's the specifications open source. It's like saying
*  TCP IP is an open standard or C is an open standard, but then you have to build an
*  implementation of the standard. And so Sci5 on the one hand pushes forward and defined and pushes
*  forward the standard. On the other hand, we have implementations that are best in class for different
*  points in the space, depending on if you want a really tiny CPU or if you want a really big beef,
*  that, uh, is faster, but it uses more area and things like this. What about the actual manufacturer?
*  Which I'm still like, what, where does that all fit? I'm going to ask a bunch of dumb questions.
*  That's okay. This is how we learn. Right. Uh, and so, uh, what the, the way this works is that
*  there's generally a separation of the people who designed the circuits and then people who
*  manufacture them. And so you'll hear about fabs like TSMC and Samsung and things like this, that
*  actually produce the chips, but they take a design coming in and that design specifies how, um,
*  how the, you know, you turn, uh, code for the chip into, uh, little rectangles that then
*  use photo lithography to make, uh, mask sets and then burn transistors onto a chip or onto a,
*  onto silicon rather. So we're talking about mass manufacturing. So yeah, they're talking about
*  making hundreds of millions of parts and things like that. Yeah. And so the fab handles the volume
*  production, things like that. But, um, when you look at this problem, um, the interesting thing
*  about the space, when you look at it is that, um, these, the steps that you go from designing a chip
*  and writing the quote unquote code for it and things like Verilog and languages like that,
*  down to what you hand off to the fab is a really well studied, really old problem. Okay. Um, tons
*  of people have worked on it. Lots of smart people have built systems and tools. Um, these tools then
*  have generally gone through acquisitions. And so they've ended up at three different major companies
*  that build and sell these tools. They're called EDA tools, like for electronic design automation.
*  The problem with this is you have huge amounts of fragmentation, you have loose standards,
*  and the tools don't really work together. So you have tons of duct tape and you have tons of, uh,
*  lost productivity. Now these are, uh, these are tools for designing. So the risk five is a
*  instruction. Like what is risk five? Like how deep does it go? How, how, how much does it touch the
*  hardware? How much does it define how much of the hardware is? Yeah. So risk, risk five is all about,
*  um, given a CPU. So the, the, the processor and your computer, how does the compiler like the
*  Swift compiler, the C compiler, things like this, how does it make it work? So it's, what is the
*  assembly code? And so you write risk five assembly instead of XA six assembly, for example.
*  But it's a set of instructions as opposed to instructions. What do you say? It tells you how
*  the compiler works. Sorry. It's what the compiler talks to. Okay. Yeah. And then, uh, so the tooling
*  you mentioned that the disparate tools are for what for when you're building a specific chip.
*  So risk five in hardware, in hardware. Yeah. So, so risk five, you can buy a risk five core from
*  sci-five and say, Hey, I want to have a certain number of run a certain number of gigahertz.
*  I want it to be this big. I want to be, have these features. I want to have, um, like I want floating
*  point or not, for example. Um, and then what you get is you get a description of a CPU with those
*  characteristics. Now, if you want to make a chip and you want to build like an iPhone chip or
*  something like that, right? You have to take both the CPU, but then you have to talk to memory.
*  You have to have timers, IOs, a GPU, other components. And so you need to pull all those
*  things together into what's called an ASIC and application specific integrated circuits. So a
*  custom chip, and then you take that design and then you have to transform it into something that
*  the fabs like TSMC, for example, know how to turn, take to production. Got it. So, but yeah. And so
*  that process I will, I can't help but see it as is a big compiler. Yeah. It's a whole bunch of
*  compilers written without thinking about it through that lens. Isn't the universe of compiler
*  compilers do two things. They represent things and transform them. Yeah. And so there's a lot
*  of things that end up being compilers, but this is, this is a space where we're talking about
*  design and usability and the way you think about things, the way things compose correctly,
*  it matters a lot. And so sci-fi is investing a lot into that space. And we think that there's a lot,
*  lot of benefit that can be made by allowing people to design chips faster, get them to market quicker
*  and scale out because, you know, at the alleged more end of Moore's law, you've got this problem
*  of you're not getting free performance just by waiting another year for a faster CPU. And so
*  you have to find performance in other ways. And one of the ways to do that is with custom
*  accelerators and other things in hardware. And, and so what we'll talk a little about
*  a little more about ASICs, but do you see that a lot of people, a lot of companies will try to
*  have like different sets of requirements that this whole process to go for. So like,
*  like almost different car companies might use different and like different PC manufacturers.
*  Like, so is this like, is risk five and this whole process, is it potentially the future of
*  all computing devices? Yeah, I think that, so if you look at risk five and step back from the silicon
*  side of things, risk five is an open standard. And one of the things that has happened over the
*  course of decades, if you look over the long arc of computing, somehow became decades old.
*  Yeah. You have companies that come and go and you have instruction sets that come and go.
*  Like one example of this out of many is Sun with Spark. Yeah, someone way Spark still lives on it
*  if you just do, but we have HP had this instruction set called PA risk. So PA risk was this big server
*  business and had tons of customers. They decided to move to this architecture called Itanium from
*  Intel. Yeah, it didn't work out so well. Yeah. Right. And so you have this issue of you're making
*  many billion dollar investments on instruction sets that are owned by a company. And even companies
*  as big as Intel don't always execute as well as they could. They have their own issues. HP,
*  for example, decided that it wasn't in their best interest to continue investing in the space because
*  it was very expensive. And so they make technology decisions or they make their own business decisions.
*  And this means that as a customer, what do you do? You've sunk all this time, all this engineering,
*  all the software work, all these, you've built other products around them and now you're stuck.
*  Right. What risk five does is provide you more optionality in the space because if you buy
*  an implementation of risk five from sci-fi, and you should, they're the best ones. Yeah.
*  Um, uh, but if something bad happens to sci-fi in 20 years, right? Well, great. You can turn around
*  and buy risk five core from somebody else. And there's an ecosystem of people that are all making
*  different risk five cores with different trade-offs, which means that if you have more than one
*  requirement, if you have a family of products, you can probably find something in the risk five space
*  that fits your needs. Whereas with, if you're talking about XA six, for example, it's Intel's
*  only going to bother to make certain classes of devices. Right. I see. So, uh, maybe a weird
*  question, but like if sci-fi is, uh, like infinitely successful in the next 20, 30 years, what does the
*  world look like? So like, how does the world of computing change? So too much diversity in
*  hardware instruction sets, I think is bad. Like we have a lot of people that are using, um, lots of
*  different instruction sets, particularly in the embedded, the like very tiny microcontroller space,
*  the thing in your toaster, um, that, uh, that are just weird and different for historical reasons.
*  And so the compilers and the tool chains and the languages on top of them, uh, aren't there. And so
*  the developers for that software have to use really weird tools because the ecosystem that supports
*  is not big enough. So I expect that will change, right? People will have better tools and better
*  languages, better features everywhere that then can service many different points in the space.
*  And I think risk five will progressively, um, eat more of the ecosystem because it can scale up,
*  it can scale down sideways, left, right. It's very flexible and very well considered and well designed
*  instruction set. Um, I think when you look at sci-fi of tackling silicon and how people build
*  chips, which is a very different space, um, that's where you say, I think we'll see a lot more custom
*  chips. And that means that you get much more battery life. You get better, better tuned
*  solutions for your IOT thingy. You get, you get people that move faster. You get the ability to
*  have faster time to market, for example. So how many custom, so first of all,
*  on the IOT side of things, do you see the number of smart toasters increasing exponentially? So,
*  uh, and if you do like how much customization per toaster is there to all toasters in the world
*  around the same, uh, silicon, like the same design, or is it different companies have different
*  design? Like how much, how much customization is possible here? Well, a lot of it comes down to
*  cost, right? And so the way that chips work is you end up paying by the one, one of the factors is
*  the size of the chip. And so what ends up happening just from an economic perspective is
*  there's only so many chips that get made in any year of a given design. And so often what customers
*  end up having to do is they end up having to pick up a chip that exists, it was built for somebody
*  else so that they can then ship their product. And the reason for that is they don't have the
*  volume of the iPhone. They can't afford to build a custom chip. However, what that means is they're
*  now buying an off the shelf chip that isn't really good, isn't a perfect fit for their needs. And so
*  they're paying a lot of money for it because they're buying silicon that they're not using.
*  Well, if you now reduce the cost of designing the chip, now you get a lot more chips and the
*  more you reduce it, the easier it is to design chips. Um, the more the world keeps evolving
*  and we get more AI accelerators, we get more other things, we get more standards to talk to,
*  we get 6G, right? You get, you get, you get changes in the world that you want to be able
*  to talk to these different things. There's more diversity in the cross product of features that
*  people want. And, um, that drives differentiated chips in different, in another direction. And so
*  nobody really knows what the future looks like, but, um, but I think that there's a lot of silicon
*  in the future. Speaking of the future, uh, you said Moore's law allegedly is dead. So do you think,
*  do you agree with, uh, uh, Dave Patterson and, and many folks that Moore's law is dead,
*  or do you agree with Jim Keller who says, uh, who was, uh, standing at the helm of the pirate
*  ship saying it's, uh, still alive. It's still alive. Yeah. Well, so I agree with what they're
*  saying and different people are interpreting the end of Moore's law in different ways.
*  So Jim would say, you know, there's another thousand X left in physics and we can,
*  we can continue to squeeze the stone and make it faster and smaller and smaller geometries and all
*  that kind of stuff. Uh, he's right. So Jim, Jim is absolutely right that there's a ton of,
*  ton of progress left and we're not at the limit of physics yet. Um, uh, that's not really what
*  Moore's law is though. If you look at what Moore's law is, is that it's a very simple, uh,
*  evaluation of, okay, well you look at the cost per, um, I think it was cost per area and the
*  most economic point in that space. And if you go look at the, the, the now quite old paper that
*  describes this, um, Moore's law has a specific economic aspect to it. And I think this is
*  something that Dave and others often point out. And so on a technicality, that's right. Um, I look
*  at it from, so I can acknowledge both of those viewpoints. They're both right. They're both
*  right. I'll give you a third wrong viewpoint that may be right in its own way, which is, um,
*  single threaded performance doesn't improve like it used to. And it used to be back when you got a,
*  you know, a Pentium 66 or something. And the year before you had a Pentium 33 and now it's twice as
*  fast. Right? Well, it was twice as fast at doing exactly the same thing. Okay. Like literally the
*  same program ran twice as fast. You just wrote a check and waited a year, year and a half. Well,
*  so that's what a lot of people think about Moore's law. And I think that is dead. And so what we're
*  seeing instead is we're pushing, we're pushing people to write software in different ways. And
*  so we're pushing people to write CUDA so they can get GPU compute and the thousands of cores on GPU.
*  We're talking about C programmers having to use P threads because they now have, you know, a hundred,
*  a hundred threads or 50 cores in a machine or something like that. Um, you're now talking
*  about machine learning accelerators that are now domain specific. And when you look at these kinds
*  of use cases, you can still get performance. Um, and Jim will come up with cool things that,
*  uh, utilize the Silicon in new ways for sure, but you're also going to change the programming model.
*  Right. And now when you start talking about changing the programming model, that's when
*  you come back to languages and things like this too, because often what you see is, um, like you
*  take the C programming language, right? The C programming language is designed for CPUs.
*  And so if you want to talk to a GPU, now you're talking to its cousin CUDA. Okay. CUDA is a
*  different thing with a different set of tools, a different world, a different way of thinking.
*  And we don't have one world that scales. And I think that we can get there. We can have one world
*  that scales in a much better way. And the small tangent, then I think most programming languages
*  are designed for CPUs for single core, even just in their spirit, even if they allow for
*  parallelization. So what does it look like for programming language to have, um,
*  parallelization or massive parallelization as it's like first principle? So the canonical example
*  of this is the hardware design world. So Verilog, VHDL, these kinds of languages,
*  they're what's called a high level synthesis language. This is the thing people design chips in.
*  And where you're designing a chip, it's kind of like a brain where you have infinite parallelism.
*  Like you've got your, you're like laying down transistors, transistors are always running.
*  Okay. And so you're not saying run, run this transistor, then this transistor,
*  then this transistor. It's like your brain, like your neurons are always just doing something.
*  They're not clocked, right? They're just, they're just doing, they're, they're doing their thing.
*  And so when you design a chip or when you design a CPU, when you design a GPU, when you design,
*  when you're laying down the transistors, uh, similarly, you're talking about, well, okay,
*  well, how do these things communicate? And so these languages exist. Verilog is, um, a kind of
*  mixed example of that. None of these languages are really great. Very low level. Yeah. Yeah.
*  They're very low level and abstraction is necessary here. And there's different,
*  different approaches at that. And it's a, it's itself a very complicated world, but, um,
*  but it's implicitly parallel. And so having that as a, as the domain that you, uh, program towards
*  makes it so that by default, you get parallel systems. If you look at CUDA, CUDA is a point
*  halfway in the space where in CUDA, when you write a CUDA kernel for your GPU, it feels like
*  you're writing a scalar program. So you're like, you have ifs, you have for loops, stuff like this.
*  You're just writing normal, normal code. But what happens outside of that in your driver is that it
*  actually is running you on like a thousand things at once. Right. And so it's, it's parallel, but it
*  has pulled it out of the programming model. And so now you as a programmer are working at it,
*  a, uh, in a simpler world and it's solved that for you. Right. How do you take the language like
*  Swift? Um, you know, if we think about GPUs, but also ASICs, maybe if we can dance back and
*  forth between hardware and software, uh, is, you know, how do you design for these features to be
*  able to program, make it a first-class citizen to be able to do like Swift for TensorFlow,
*  to be able to do machine learning on current hardware, but also future hardware, like, uh,
*  TPUs and all kinds of ASICs that I'm sure will be popping up more. Yeah. Well, so,
*  so a lot of this comes down to this whole idea of having the nuts and bolts underneath the covers
*  that work really well. So you need, if you're talking to TPUs, you need, you know, MLIR or
*  XLA or one of these compilers that talks to TPUs to build on top of. Okay. And if you're talking
*  to circuits, you need to figure out how to lay down the transistors and how to organize it and
*  how to set up clocking and like all the domain problems that you get with, uh, circuits.
*  Then you have to decide how to explain it to a human. What is the UI? Right. And if, if you do
*  it right, that's a library problem, not a language problem. And that works if you have a library or
*  a language, which allows your library to write things that feel native in the language by
*  implementing libraries, because then you can innovate in programming models without having
*  changed your syntax again, and like you have to invent new code formatting tools and like all the
*  other things that languages come with. And this, this gets really interesting. And so, um, if you
*  look at the space, the interesting thing, once you separate out syntax becomes, what is that
*  programming model? And so do you want the CUDA style? I write one program and it runs many places.
*  The, um, do you want the implicitly parallel model? How do you reason about that? How do you give
*  developers, you know, chip architects, the, the ability to express their intent?
*  And that comes into this whole design question of how do you detect bugs quickly? So you don't
*  have to tape out a chip to find out what's wrong ideally, right? How do you, and, and, you know,
*  this is a spectrum. How do you make it so that people feel productive? So their turnaround time
*  is very quick. All these things are really hard problems. And, um, and this world, I think that
*  not a lot of effort has been put into that design problem and thinking about the layering and other
*  pieces.
*  Well, you've, uh, on the topic of concurrency, you've written the Swift concurrency manifest. I think
*  it's, it's kind of interesting. Anything that, uh, has the word manifesto in is very interesting.
*  Can you summarize the key ideas of, um, each of the five parts you've written about?
*  So what is a manifesto? Yes. How about we start there? Uh, so in the Swift community, we have this,
*  um, problem, which is on the one hand, you want to have relatively small proposals that you can
*  kind of fit in your head. You can understand the details at a very fine grain level that move the
*  world forward, but then you also have these big arcs. Okay. And often when you're working on
*  something that is a big arc, but you're tackling it in small pieces, you have this question of,
*  how do I know I'm not doing a random walk? Where are we going? Like, how does this add up?
*  Furthermore, when you start that first, the first small step, what terminology do you use?
*  How do we think about it? What is better and worse in the space? What are the principles? What are
*  we trying to achieve? And so what a manifesto in the Swift community does is it starts to say,
*  Hey, well, let's step back from the details of everything and let's paint a broad picture
*  to talk about how, what we're trying to achieve. Let's give an example design point. Let's try to
*  paint the big picture so that then we can zero in on the individual steps and make sure that we're
*  making good progress. And so the Swift concurrency manifesto is something I wrote three years ago.
*  It's been a while, maybe, maybe more, trying to do that for, for Swift and concurrency.
*  It starts with some fairly simple things like making the observation that
*  when you have multiple different computers or multiple different threads that are communicating,
*  it's best for them to be asynchronous. Right. And so you need things to be able to run separately
*  and then communicate with each other. And this means asynchronous. And this means that you need
*  a way to modeling asynchronous communication. Many languages have features like this. Async await is
*  a popular one. And so that's what I think is very likely in Swift. But as you start building this
*  tower of abstractions, it's not just about how do you write this, you then reach into the, how do
*  you get memory safety? Because you want correctness, you want the bug ability insanity for developers.
*  And how do you get that memory safety into into the language? So if you take a language like go or
*  C or any of these languages, you get what's called a race condition when two different threads or go
*  routines or whatever touch the same point in memory. Right. This is a huge like maddening
*  problem to debug because it's not reproducible generally. And so there's tools, there's a whole
*  ecosystem of solutions that built up around this, but it's a huge problem when you're writing
*  concurrent code. And so with Swift, this whole value semantics thing is really powerful there
*  because it turns out that math and copies actually work even in concurrent worlds. And so you get a
*  lot of safety just out of the box, but there are also some hard problems. And it talks about some
*  of that. When you start building up to the next level up and you start talking beyond memory safety,
*  you have to talk about what is the programmer model? How does a human think about this? So a
*  developer that's trying to build a program, think about this, and it proposes a really old model
*  with a new spin called actors. Actors are about saying we have islands of single threadedness
*  logically. So you write something that feels like it's one programming, one program running in a
*  unit, and then it communicates asynchronously with other other things. And so making that expressive
*  and natural feel good, be the first thing you reach for and being safe by default is a big part of the
*  design of that proposal. When you start going beyond that, now you start to say, cool, well,
*  these things that communicate asynchronously, they don't have to share memory. Well, if they
*  don't have to share memory and they're sending messages to each other, why do they have to be
*  in the same process? These things should be able to be in different processes on your machine.
*  And why just processes? Well, why not different machines? And so now you have a very nice gradual
*  transition towards distributed programming. And of course, when you start talking about the big
*  future, the manifesto doesn't go into it, but accelerators are async things you talk to
*  asynchronously by sending messages to them. And how do you program those? Well, that gets very
*  interesting. That's not in the proposal. So and how much do you want to make that explicit,
*  like the control of that whole process explicit to the program? Yeah, good question. So when you're
*  designing any of these kinds of features or language features, or even libraries, you have
*  this really hard trade off that you have to make, which is how much is it magic? Or how much is it
*  in the human's control? How much can they predict and control it? What do you do when the default
*  case is the wrong case? Okay. And so when you're designing a system, I won't name names, but there
*  are systems where you it's really easy to get started. And then you you jump it. So let's pick
*  like logo. Okay, so something like this. So it's really easy to get started is really designed for
*  teaching kids. But as you get into it, you hit a ceiling. And then you can't go any higher. And
*  then what do you do? Well, you have to go switch to a different world and rewrite all your code.
*  And this logo is a silly example here. This exists in many other languages. With Python,
*  you would say, like concurrency, right? So Python has the global interpreter block. So
*  threading is challenging in Python. And so if you if you start writing a large scale application
*  in Python, and then suddenly need concurrency, you're kind of stuck with a series of bad trade
*  offs, right? There's other ways to go where you say like, waste all the all the complexity on the
*  user all at once. Right. And that's also bad in a different way. And so what what I what I prefer
*  is building a simple model that you can explain that then has an escape hatch. So you get in,
*  you have guardrails, you memory safety works like this in Swift, where you can start with you like,
*  by default, if you use all the standard things, it's memory safe, you're not going to shoot your
*  foot off. But if you want to get a C level pointer to something, you can explicitly do that.
*  But by default, it's there's guardrails. There's guardrails. Okay, so but like, you know,
*  whose job is it to figure out which part of the code is parallelizable?
*  So in the case of the proposal, it is the human's job. So they decide how to architect their
*  application. And then the runtime in the compiler is very predictable. And so this this is in
*  contrast to like, there's a long body of work, including on Fortran for auto parallelizing
*  compilers. And this is an example of a bad thing. And my so as a compiler person, I can write on
*  compiler people. Often compiler people will say, cool, since I can't change the code, I'm going to
*  write my compiler that then takes this unmodified code and makes go way faster on this machine.
*  Okay, application development. So it does pattern matching, it does like really deep analysis,
*  compiler people are really smart. And so they like want to like do something really clever and
*  tricky. And you get like 10x speed up by taking like an array of structures and turn into a
*  structure of arrays or something because it's so much better for memory. Like there's bodies like
*  tons of tricks. They love optimization. Yeah, you love optimization. Everyone loves optimization.
*  And it's just this promise of build with my compiler and your thing goes fast. Yeah. Right.
*  But here's the problem. Lex, you write a program, you run it with my compiler, it goes fast, you're
*  very happy. Wow, so much faster than the other compiler. Then you go and you add a feature to
*  your program or you refactor some code. And suddenly you got a 10x loss in performance.
*  Well, why what just happened there? What just happened there is you the heuristic, the pattern
*  matching the compiler or whatever analysis was doing just got defeated because you didn't inline
*  a function or something right. As a user, you don't know you don't want to know that was the
*  whole point. You don't want to know how the compiler works. You don't want to know how the
*  memory hierarchy works. You don't want to know how it got parallelized across all these things.
*  You wanted that abstract away from you. But then the magic is lost as soon as you did something
*  and you fall off a performance cliff. And now you're in this funny position where what do I do? I
*  don't change my code. I don't fix that bug. It costs 10x performance. Now what do I do?
*  Well, this is the problem with unpredictable performance. If you care about performance,
*  predictability is a very important thing. And so and so what the what the proposal does is it
*  provides architectural patterns for being able to lay out your code gives you full control over
*  that makes it really simple so you can explain it. And then and then if you want to scale out in
*  different ways, you have full control over that. So in your sense, the intuition is for a compiler
*  is too hard to do automated parallelization. Like, you know, because the compilers do stuff
*  automatically. That's incredibly impressive for other things. Right. But for parallelization,
*  we're not even we're not close to there. Well, it depends on the programming model. So there's
*  many different kinds of compilers. And so if you talk about like a C compiler, a Swift compiler,
*  something like that, where you're writing imperative code, parallelizing that and
*  reasoning about all the pointers and stuff like that is very is a very difficult problem.
*  Now, if you switch domains, so there's this cool thing called machine learning.
*  Right. So machine the machine learning nerds, among other endearing things like, you know,
*  solving cat detectors and other things like that have done this amazing breakthrough of producing
*  a programming model operations that you compose together that has raised levels of abstraction
*  high enough that suddenly you can have auto parallelizing compilers. You can write a model
*  using TensorFlow and have it run on 1024 nodes of a TPU. Yeah, that's true. I didn't even think
*  about like, you know, because there's so much flexibility in the design of architectures that
*  ultimately boil down to a graph that's parallelizable for you, parallelized for you. And if you think
*  about it, that's pretty cool. That's pretty cool. Yeah. And you think about batching, for example,
*  as a way of being able to exploit more parallelism. Yeah. Like that's a very simple thing that now is
*  very powerful. That didn't come out of the programming language nerds, right? Those people,
*  like that came out of people that are just looking to solve a problem and use a few GPUs and
*  organically developed by the community of people focusing on machine learning.
*  And it's an incredibly powerful, powerful abstraction layer that enables the compiler
*  people to go and exploit that. And now you can drive supercomputers from Python. That's pretty
*  cool. That's amazing. Just to pause on that, because I'm not sufficiently low level, I forget to
*  admire the beauty and power of that. But maybe just to linger on it, like what, what does it take to
*  run in your network fast? Like how hard is that compilation? It's really hard. So we just skipped,
*  you said like, it's amazing that that's a thing, but how hard is that of a thing? It's hard. And
*  I would say that not all of the systems are really great, including the ones I helped out. So there's
*  a lot of work left to be done there. Is it the compiler nerds working on that or is it a whole
*  new group of people? Well, it's a full stack problem, including compiler people, including
*  APIs. So like Keras and the, the, the, the module API and PyTorch and Jax. And there's a bunch of
*  people pushing on all the different parts of these things, because when you look at it, it's both,
*  how do I express the computation? Do I stack up layers? Well, cool. Like setting up a linear
*  sequence of layers is great for the simple case, but how do I do the hard case? How do I do
*  reinforcement learning? Well, now I need to integrate my application logic in this, right?
*  Then it's, you know, the next level down of how do you represent that for the runtime? How do you
*  get hardware abstraction? And then you get to the next level down of saying like, forget about
*  abstraction. How do I get the peak performance out of my TPU or my iPhone accelerator or whatever,
*  right? And all these different things. And how, and so this is a layered problem with a lot of
*  really interesting design and work going on in the space and a lot of really smart people working on
*  it. Machine learning is a very well funded area of investment right now. And so there's a lot of
*  progress being made. So how much innovation is there on the lower level? So closer to the,
*  to the ASIC. So redesigning the hardware or redesigning concurrently compilers with that
*  hardware. Is that, like, if you were to predict the biggest, you know, the equivalent of Moore's law
*  improvements in the inference and the training of neural networks and just all of that, where is
*  that going to come from? You think? Sure. You get scalability, you have different things. And so you
*  get, you know, Jim Keller shrinking process technology, you get three nanometer instead of
*  five or seven or 10 or 28 or whatever. And so that, that marches forward and that provides
*  improvements. You get architectural level performance. And so the, you know, a TPU with
*  a matrix multiply unit and a systolic array is much more efficient than having a scalar core doing
*  multiplies and ads and things like that. You then get system level improvements. So how you
*  talk to memory, how you talk across a cluster of machines, how you scale out, how you have fast
*  interconnects between machines, you then get system level programming models. So now that you have
*  all this hardware, how to utilize it, you then have algorithmic breakthroughs where you say,
*  Hey, wow, cool. Instead of training in, you know, resident 50 and a week, I'm now training it in,
*  you know, 25 seconds. And it's a combination, it's a combination of, you know, new, new optimizers
*  and new, new, new, just training regimens and different, different approaches to train. And,
*  and all of these things come together to push the world forward.
*  That was a beautiful exposition. But if you were to force to bet all your money on one of these,
*  Why do we have to?
*  Unfortunately, we have people working on all this. It's an exciting time, right?
*  So, I mean, you know, opening, I did this little paper showing the algorithmic improvement you can
*  get has been, you know, improving exponentially. I haven't quite seen the same kind of analysis
*  on other layers of the stack. I'm sure it's also improving significantly. I just, it's a,
*  it's a nice intuition builder. I mean, there's a reason why Moore's law, that's the beauty of
*  Moore's laws. Somebody writes a paper that makes a ridiculous prediction. And it, you know, becomes
*  reality in a sense. There's, there's something about these narratives when you, when Chris Latner on a
*  silly little podcast makes, bets all this money on a particular thing, somehow it can have a ripple
*  effect of actually becoming real. That's an interesting aspect of it. Because like, it might
*  have been, you know, we focus with Moore's law, most of the computing industry really,
*  really focused on the hardware. I mean, software innovation, I don't know how much software
*  innovation there was in terms of what Intel giveth, Bill takes away. Yeah. I mean, compilers improved
*  significantly also. Well, not, not really. So actually, I mean, I'm joking about how
*  software has gotten slower, pretty much as fast as hardware got better, at least through the 90s.
*  There's another joke, another law in compilers, which is called, I think it's called Probstein's
*  law, which is compilers double the performance of any given code every 18 years.
*  So they move slowly. Yeah. Well, so well, yeah, it's exponential also.
*  Yeah, you're making progress. But there, again, it's not about the power of compilers is not just
*  about how you make the same thing go faster. It's how do you unlock the new hardware?
*  Right. A new chip came out. How do you utilize it? You say, oh, the programming model, how do we make
*  people more productive? How do we, how do we like have better error messages? Even such mundane
*  things like how do I generate a very specific error message about your code actually makes people
*  happy because then they know how to fix it. Right. And it comes back to how do you help people get
*  their job done? Yeah. And yeah. And then in this world of exponentially increasing smart toasters,
*  how do you expand computing to to all these kinds of devices? Do you see this world where
*  just everything's a competing surface? You see that possibility? Just everything's a computer?
*  Yeah, I don't see any reason that that couldn't be achieved. It turns out that
*  sand goes into glass and glass is pretty useful too. And, you know, like, why not?
*  So a very important question then if, if we're living in a simulation and the simulation is
*  running a computer, like what was the architecture of that computer? Do you think? So you're saying
*  is it a quantum system? Is it? Yeah, like this whole quantum discussion, is it needed or can
*  we run it on a, you know, with a risk five architecture, a bunch of CPUs?
*  I think it comes down to the right tool for the job. Yeah. And so, and what's the pilot?
*  Yeah, exactly. That's, that's my question. How do I get that job? Be the universe compiler.
*  And so there, as far as we know, quantum, quantum, quantum systems are the bottom of the
*  pile of turtles so far. And so we don't know efficient ways to implement quantum systems
*  without using quantum computers. Yeah. And that's totally outside of everything we've talked about.
*  Quantum. But who runs that quantum computer? Yeah. Right. So if it, if it, if we really are
*  living in a simulation, then is it bigger quantum computers? Is it different ones? Like how does that
*  work out? How does that scale? Well, it's, it's the same size. It's the same size. But then,
*  the thought of the simulation is that you don't have to run the whole thing that,
*  you know, we humans are cognitively very limited. Checkpoints. Checkpoints. Yeah. And, and if we,
*  the point at which we human, so you basically do minimal amount of, what is it? The Swift does
*  on right copy. Copy on right. So you only, you only adjust the simulation.
*  Parallel universe theories. Right. And so, and so every time a decision's made, somebody opens the
*  shortening your box, then there's a fork and then this could happen. And then, thank you for,
*  for considering the possibility. But yeah, so it may not require, you know, the entirety of the
*  universe is simulated, but it's interesting to think about as we create this, this higher and
*  higher fidelity systems. But I do want to ask on the, on the quantum computer side,
*  cause everything we've talked about with us, whether you work with sci-fi, with everything,
*  with compilers, none of that includes quantum computers, right? That's true. So
*  have you ever thought about what, you know, this whole serious engineering work
*  of quantum computers looks like of compilers, of architectures, all of that kind of stuff.
*  So I've looked at it a little bit. I'd know almost nothing about it,
*  which means that at some point I will have to find an excuse to get involved.
*  Cause that's what do you think? Do you think that's the thing to be like, is it with your little
*  tingly senses of the timing of one to be involved? Is it not yet? Well, so, so the thing I do really
*  well is I jump into messy systems and figure out how to make them figure out what the truth in the
*  situation is, try to figure out what, what the unifying theory is, how to like factor the
*  complexity, how to find a beautiful answer to a problem that has been well studied and lots of
*  people have bashed their heads against it. I don't know that quantum computers are mature enough and
*  accessible enough to be figured out yet. Right. And the, I think the open question with quantum
*  computers is, is there a useful problem that gets solved with quantum computer that makes it worth
*  the economic cost of like having one of these things and having, having legions of people that,
*  that, that set it up. You go back to the fifties, right? And there's the projections of the world
*  will only need seven, seven computers. Right. Well, and part of that was that people hadn't figured
*  out what they're useful for. What are the algorithms we want to run? What are the problems get solved?
*  And this comes back to how do we make the world better either economically or making somebody's
*  life better or like solving a problem that wasn't solved before things like this. And I think that
*  just we're a little bit too early in that development cycle because it's still like literally
*  a science project, not a negative connotation, right? It's literally a science project and
*  the progress there's amazing. And so I don't know if it's 10 years away, if it's two years away,
*  exactly where that breakthrough happens. But you look at machine learning, it, we went through a
*  few winners before the Alex net transition. And then suddenly it had its breakout moment.
*  And that was the catalyst that then drove the talent flocking into it. That's what drove the
*  economic applications of it. That's what drove the, the technology to go faster because you now have
*  more minds thrown at the problem. This is what caused like a serious knee and deep learning and
*  the algorithms that we're using. And, and so I think that's what quantum needs to go through.
*  And so right now it's in that, that formidable finding itself, getting the, the like literally
*  the physics figured out and, um, and then it has to figure out the application that makes
*  that's useful. Yeah, but I'm, I'm, I'm not skeptical that I think that will happen. I think it's just,
*  you know, 10 years away, something like that. I forgot to ask what programming language do
*  you think the simulation is written in? Ooh, probably Lisp. So not Swift. Like if you were to
*  bet, you weren't the best, uh, I'll just leave it at that. So I mean, we've mentioned that you
*  worked with all these companies with, we've talked about all these projects. It's kind of like, if we
*  just step back and zoom out about the way you did that work and we look at COVID times, this pandemic
*  we're living through that may, if I look at the way Silicon Valley folks are talking about it,
*  MIT is talking about it. This might last for a long time, not just the virus, but the,
*  the remote nature, the economic impact. I mean, all of it. Yeah. Yeah. It's, it's going to be a mess.
*  Do you think, uh, what's your prediction? I mean, from sci-fi to Google, to, uh, uh,
*  to just all the places you worked in just Silicon Valley, you're in the middle of it. What do you
*  think is, how is this whole place going to change? Yeah. So, I mean, I, I really can only speak to
*  the tech perspective. I am in that bubble. Um, I think it's gonna be really interesting because
*  the, you know, the zoom culture of being remote and on video chat all the time has really
*  interesting effects on people. So on the one hand, it's a great normalizer. It's a normalizer that I
*  think will help communities of people that have traditionally been underrepresented, uh, because
*  now you're taking in some cases a face off because you don't have to have a camera going.
*  Right. And so you can have conversations without physical appearance being part of the, part of
*  the dynamic, which is pretty powerful. You're taking remote employees that have already been
*  remote and you're saying you're now on the same level and foot footing as everybody else. Nobody
*  gets whiteboards. You're not going to be the one person that doesn't get to be participating in
*  the whiteboard conversation. And that's pretty powerful. Um, you've got, uh, you're forcing
*  people to think, uh, asynchronously in some cases because it's harder to just,
*  just get people physically together and the bumping into each other forces people to
*  find new ways to solve those problems. And I think that that leads to more inclusive behavior,
*  which is good. Um, on the other hand, it's also, it just sucks, right? And so, um,
*  the, the nature, the, the actual communication or it just sucks being not in, in with people like
*  on a daily basis and collaborating with them. Yeah. All of that. I mean, everything, this whole
*  situation is terrible. Um, what I meant primarily was the, um, I think that the most humans like
*  working physically with humans. I think this is something that not everybody, but many people are
*  programmed to do. And I think that we get something out of that, that is very hard to express,
*  at least for me. And so maybe this isn't true of everybody, but, um, and so the question to me is,
*  you know, when you get through that time of adaptation, right? You get out of March and
*  April and you get into December and you get into next March, if it's not changed, right?
*  It's already terrifying. Well, you think about that and you think about what is the nature of
*  work and how do, how do we adapt and humans are very adaptable species, right? We can,
*  we can learn things and when we're forced to, and there's a catalyst to make that happen.
*  And so what is it that comes out of this? And are we better or worse off? Right. I think that,
*  you know, you look at the Bay area, housing prices are insane. Well, why? Well, there's a high
*  incentive to be physically located because if you don't have proximity, you end up paying for it and
*  commute, right? And there's, there has been huge social, social pressure in terms of like, you will
*  be there for the meeting, right? Or whatever scenario it is. And I think that's going to be
*  way better. I think it's going to be much more than norm to have remote employees. And I think this is
*  going to be really great. Do you, do you have friends or do you hear of people moving?
*  I know one family friend that moved, they moved back to Michigan and, you know, they were a family
*  with three kids living in a small apartment and like we're going insane, right? And they're in tech,
*  husband works for Google. So first of all, friends of mine have, are in the process of, or are, have
*  already lost the business. The thing that represents their passion, their dream, it could be small
*  entrepreneurial projects, but it can be large businesses like people that run gyms, like restaurants,
*  like tons of things. Yeah. So, but also people like look at themselves in the mirror and ask the
*  question of like, what do I want to do in life? For some reason they don't, they haven't done it
*  until COVID. Like they really asked that question and that results often in moving or leaving the
*  company here with starting your own business or transitioning to different company. Do you think
*  we're going to see that a lot? Like in, I, I, well, I can't speak to that. I mean, we're definitely
*  going to see it at a higher frequency than we did before. Just because I think what you're trying to
*  say is there are decisions that you make yourself and big life decisions that you make yourself.
*  And like, I'm going to like quit my job and start a new thing. There's also decisions that get made
*  for you. Like I got fired from my job. What am I going to do? Right. And that's not a decision that
*  you think about, but you're forced to act. Okay. And so I think that those, you're forced to act
*  kind of moments where like, you know, global pandemic comes and wipes out the economy and now
*  your business doesn't exist. I think that does lead to more reflection, right? Because you're
*  less anchored on what you have and it's not a, what do I have to lose versus what do I have to
*  gain? AB comparison. It's more of a fresh slate. Cool. I could do anything now. Do I want to do the
*  same thing I was doing? Did that make me happy? Is this now time to go back to college and
*  take a class and learn, learn a new skill? Is this, is this a time to spend time with family? If you
*  can afford to do that, is this time to like literally move into the parents? Right. I mean,
*  all these things that were not normative before suddenly become, I think, very, the value system
*  has changed. And I think that's actually a good thing in the short term, at least because it leads
*  to, you know, there's kind of been an over optimization along one, one set of priorities
*  for the world. And now maybe we'll get to more balanced and more interesting world where people
*  are doing different things. I think it could be good. I think there could be more innovation
*  that comes out of it. For example, what do you think about the, all the social chaos in the middle
*  of like, it sucks. You think it's, let me ask you, I hope you think it's all going to be okay.
*  Well, I think humanity will survive the form of next stent. We're not all going to kill. Yeah.
*  Well, yeah, I don't think the virus is going to kill all the humans. I don't think all the
*  humans are going to kill all the humans. I think that's unlikely, but I look at it as
*  a catalyst, right? So, so you need, you need a reason for people to be willing to do things that
*  are uncomfortable. I think that the U S at least, but I think the world in general is a pretty
*  unoptimal place to live in for a lot of people. And I think that what we're seeing right now is
*  we're seeing a lot of unhappiness and because, because of all the pressure, because of all the
*  badness in the world that's coming together, it's really kind of igniting some of that debate that
*  should have happened a long time ago. Right? I mean, I think that we'll see more progress.
*  You're asking about offline, you're asking about politics and wouldn't it be great if politics
*  moved faster because there's all these problems in the world and we can move it. Well, people are
*  intentional or inherently a conservative. And so if you're talking about conservative people,
*  particularly if they have heavy burdens on their shoulders, because they represent
*  literally thousands of people, it makes sense to be conservative. But on the other hand,
*  when you need change, how do you get it? The global pandemic will probably lead to some change
*  and it's not a directed, it's not a directed plan, but I think that it leads to people asking really
*  interesting questions. And some of those questions should have been asked a long time ago. Well,
*  let me know if, if you've observed this as well, something that's bothering me
*  in the machine learning community, I'm guessing it might be prevalent in other places is something
*  that feels like in 2020 increase the level of toxicity. Like people are just quicker to pile on
*  to just be, they're just harsh on each other to, to like mob, pick a person that screwed up and like
*  make it a big thing. And is there something that we can like, yeah, have you observed that in other
*  places? Is there, is there some way out of this? I think there's an inherent thing in humanity that's
*  kind of an us versus them thing, which is that you want to succeed and how do you succeed? Well,
*  it's relative to somebody else. And so what's happening in, at least in some part is that
*  with the internet and with online communication, the world's getting smaller. Right. And so we're
*  having some of the social ties of like my name, my town versus your town's football team.
*  Right. Turn into much larger, larger and yet shallower problems. And people don't have time,
*  the incentives, clickbait and like all these things kind of really, really feed into this machine. And
*  I don't know where that goes. Yeah. I mean, the reason I think about that, I mentioned to you this
*  offline a little bit, but you know, I've a few difficult conversations scheduled, some of them
*  political related, some of them within the community, difficult personalities that went
*  through some stuff. I mean, one of them I've talked before, I will talk again is Yann LeCun.
*  He got off a little crap on Twitter for, for talking about a particular paper and the bias
*  within a data set. And then there's been a huge, in my view, and I'm willing, comfortable saying it,
*  irrational, over-exaggerated pylon on his comments, because he made pretty basic comments
*  about the fact that if there's bias in the data, there's going to be bias in the results.
*  So we should not have bias in the data, but people piled on to him because he said he trivialized the
*  problem of bias. Like it's a lot more than just bias in the data, but like, yes, that's a very
*  good point, but that's not what he was saying. It's not what he was saying. And the response,
*  like the implied response that he's basically sexist and racist is something that completely
*  drives away the possibility of nuanced discussion. One nice thing about like a podcast long form
*  conversation is you can talk it out, you can lay your reasoning out. And even if you're wrong,
*  you can still show that you're a good human being underneath it.
*  You know, your point about you can't have a productive discussion. Well, how do you get to
*  that point where people can turn, they can learn, they can listen, they can think, they can engage
*  versus just being a shallow like, like, and then keep moving. Right. And I don't think that
*  progress really comes from that. Right. And I don't think that one should expect that. I think that
*  you'd see that as reinforcing individual circles and the us versus them thing. And
*  I think that's fairly divisive. Yeah, I think there's a big role in like the people that
*  bother me most on Twitter when I observe things is not the people who get very emotional, angry,
*  like over the top. It's the people who like, prop them up. It's all the, it's, it's, I think what
*  should be the, we should teach each other is to be sort of empathetic. The thing that it's really
*  easy to forget, particularly on like Twitter or the internet or email, is that sometimes people
*  just have a bad day. Right. You have a bad day, or you're like, I've been in the situation where
*  it's like between meetings, like fire off a quick response to an email, because I want to like,
*  help get something unblocked. Phrase it really objectively wrong. I screwed up. And suddenly,
*  this is now something that sticks with people. And it's not because they're bad. It's not because
*  you're bad. Just psychology of like, you said a thing. It sticks with you. You didn't mean it
*  that way, but it really impacted somebody because the way they interpret it. And this is just an
*  aspect of working together as humans. And I have a lot of optimism in the long term, the very long
*  term about what we as humanity can do. But I think that's going to be, it's just always a rough ride.
*  You came into this by saying like, what is COVID and all the social strife that's happening right
*  now mean? And I think that it's really bad in the short term, but I think it'll lead to progress.
*  And for that, I'm very thankful. Yeah, it's painful in the short term, though.
*  Well, yeah. I mean, people are out of jobs. Like some people can't eat. Like it's horrible.
*  But, you know, it's progress. So we'll see what happens. I mean, the real question is when you
*  look back 10 years, 20 years, 100 years from now, how do we evaluate the decisions that are being
*  made right now? I think that's really the way you can frame that and look at it. And you say,
*  you integrate across all the short term horribleness that's happening and you look at
*  what that means. And is the improvement across the world or the regression across the world
*  significant enough to make it a good or bad thing? I think that's the question.
*  Yeah. And for that, it's good to study history. I mean, one of the big problems for me right now
*  is I'm reading the rise and fall of the Third Reich. Light reading. So as everything is just,
*  I just see parallels and it means you have to be really careful not to overstep it. But just the
*  thing that worries me the most is the pain that people feel when a few things combine, which is
*  economic depression, which is quite possible in this country, and then just being disrespected
*  in some kind of way, which the German people were really disrespected by most of the world
*  in a way that's over the top, that something can build up and then all you need is a charismatic
*  leader to go either positive or negative in both work, as long as they're charismatic.
*  And it's taking advantage of, again, that inflection point that the world's in
*  and what they do with it could be good or bad.
*  And so it's a good way to think about times now, like on an individual level, what we decide to do
*  is when history is written, 30 years from now, what happened in 2020, probably history is going
*  to remember 2020. Yeah, I think so. Either for good or bad. And it's like up to us to write it.
*  Well, one of the things I've observed that I find fascinating is most people act as though
*  the world doesn't change. You make decisions knowingly, you make a decision where you're
*  predicting the future based on what you've seen in the recent past. And so if something's always
*  been rained every single day, then of course you expect it to rain today too. On the other hand,
*  the world changes all the time, constantly, for better and for worse. And so the question is,
*  if you're interested in something that's not right, what is the inflection point that led
*  to a change? And you can look to history for this. What is the catalyst that led to that explosion,
*  that led to that bill, that led to the... You can kind of work your way backwards from that.
*  And maybe if you pull together the right people and you get the right ideas together, you can
*  actually start driving that change and doing it in a way that's productive and hurts fewer people.
*  Like a single person, a single event can turn all of this.
*  Absolutely. Everything starts somewhere and often it's a combination of multiple factors,
*  but yeah, these things can be engineered. That's actually the optimistic view that...
*  I'm a long-term optimist on pretty much everything and human nature.
*  We can look to all the negative things that humanity has, all the pettiness and all the
*  self-servingness and just the cruelty, the biases, the... Just humans can be very horrible.
*  But on the other hand, we're capable of amazing things. And the progress across 100-year chunks
*  is striking. And even across decades, we've come a long ways and there's still a long ways to go,
*  but that doesn't mean that we've stopped. Yeah. The kind of stuff we've done in the last
*  100 years is unbelievable. It's kind of scary to think what's going to happen in the next 100 years.
*  It's scary, like exciting. Scary in a sense that it's kind of sad that the kind of technology is
*  going to come out in 10, 20, 30 years. We're probably too old to really appreciate it because
*  you don't grow up with it. It'll be like kids these days with their virtual reality and their...
*  Their TikToks and stuff like this. Like, oh, there's this thing and like, come on,
*  give me my static photo. My Commodore 64. Yeah. Yeah, exactly.
*  Okay. Sorry, we kind of skipped over it. Let me ask on... The machine learning world has been kind of
*  inspired, their imagination captivated with GPT-3 and these language models. I thought it'd be
*  cool to get your opinion on it. What's your thoughts on this exciting world of...
*  It connects the computation actually, of language models that are huge and take
*  many, many computers, not just to train, but to also do inference on. Sure. Well, I mean,
*  it depends on what you're speaking to there, but I mean, I think that there's been a pretty well
*  understood maximum and deep learning that if you make the model bigger and you shove more data into
*  it, assuming you train it right and you have a good model architecture, that you'll get a better
*  model out. And so on the one hand, GPT-3 was not that surprising. On the other hand, a tremendous
*  amount of engineering went into making it possible. The implications of it are pretty huge. I think
*  that when GPT-2 came out, there was a very provocative blog post from OpenAI talking about,
*  we're not going to release it because of the social damage it could cause if it's misused.
*  I think that's still a concern. I think that we need to look at how
*  technology is applied and well-meaning tools can be applied in very horrible ways and they can have
*  very profound impact on that. I think that GPT-3 is a huge technical achievement. And what will GPT-4
*  be? It will probably be bigger, more expensive to train. Really cool architectural tricks.
*  Do you think, I don't know how much thought you've done on distributed computing.
*  Is there some technical challenges that are interesting that you're hopeful about exploring
*  in terms of a system that, like a piece of code that, with GPT-4, that might have, I don't know,
*  hundreds of trillions of parameters, which have to run on thousands of computers. Is there some hope
*  that we can make that happen? Yeah. Well, I mean, today you can write a check and get access to a
*  thousand TPU cores and do really interesting large-scale training and inference and things
*  like that in Google Cloud, for example. And so I don't think it's a question about scale,
*  it's a question about utility. And when I look at the transformer series of architectures that
*  the GPT series is based on, it's really interesting to look at that because they're
*  actually very simple designs. They're not recurrent. The training regimens are pretty simple.
*  And so they don't really reflect like human brains, right? But they're really good at learning
*  language models and they're unrolled enough that you can simulate some recurrence, right?
*  And so the question I think about is, where does this take us? So we can just keep scaling it,
*  have more parameters, more data, more things, we'll get a better result for sure. But are there
*  architectural techniques that can lead to progress at a faster pace? Right, this is when
*  right, this is when, you know, how do you get instead of just like making it a constant time
*  bigger, how do you get like an algorithmic improvement out of this, right? And whether
*  it be a new training regimen, if it becomes sparse networks, for example, human brain is sparse,
*  all these networks are dense. The connectivity patterns can be very different. I think this is
*  where I get very interested and I'm way out of my league on the deep learning side of this. But I
*  think that could lead to big breakthroughs. When you talk about large scale networks,
*  one of the things that Jeff Dean likes to talk about, and he's given a few talks on is this
*  idea of having a sparsely gated mixture of experts kind of a model where you have, you know, different
*  nets that are trained and are really good at certain kinds of tasks. And so you have this
*  distributor across a cluster. And so you have a lot of different computers that end up being
*  kind of locally specialized in different demands. And then when a query comes in, you
*  gate it and you use learn techniques to route to different parts of the network. And then
*  you utilize the compute resources of the entire cluster by having specialization within it.
*  And I don't know where that goes or if it starts to when it starts to work, but I think things like
*  that could be really interesting as well. And on the data side, too, if you can think of data
*  selection as a kind of programming. Yeah. I mean, essentially, if you look at like
*  Kropotty talked about software 2.0, I mean, in a sense, data is the program. Yeah. So I just so
*  let me try to summarize Andre's position really quick before I disagree with it. Yeah. So Andre
*  Kropotty is amazing. So this is nothing personal with him. He's an amazing engineer and also a good
*  blog post writer. Yeah. Well, he's a great communicator. He's just an amazing person.
*  He's also really sweet. So his basic premise is that software is suboptimal. I think we can all
*  agree to that. He also points out that deep learning and other learning based techniques
*  are really great because you can solve problems in more structured ways with less like ad hoc
*  code that people write out and don't write test cases for in some cases. And so they don't even
*  know if it works in the first place. And so if you start replacing systems of imperative code
*  with deep learning models, then you get a better result. Okay. And I think that he argues that
*  software 2.0 is a pervasively learned set of models and you get away from writing code.
*  And he's given talks where he talks about, you know, swapping over more and more and more parts
*  of a code to being learned and driven that way. I think that works. And if you're predisposed
*  to liking machine learning, then I think that that's definitely a good thing. I think this
*  is also good for accessibility in many ways because certain people are not going to write
*  C code or something. And so having a data-driven approach to do this kind of stuff, I think,
*  can be very valuable. On the other hand, there are huge trade-offs and it's not clear to me that
*  software 2.0 is the answer. And probably Andre wouldn't argue that it's the answer for every
*  problem either. But I look at machine learning is not a replacement for software 1.0. I look at it
*  as a new programming paradigm. And so programming paradigms, when you look across across domains is
*  they have structured programming where you go from go-tos to if-then-else or functional programming
*  from Lisp and you start talking about higher-order functions and values and things like this, or you
*  talk about object-oriented programming, you're talking about encapsulation, subclassing,
*  inheritance, you start talking about generic programming where you start talking about code
*  reuse through specialization and different type instantiations. When you start talking about
*  differentiable programming, something that I am very excited about in the context of machine
*  learning, talking about taking functions and generating variants like the derivative of
*  another function. That's a programming paradigm that's very useful for solving certain classes of
*  problems. Machine learning is amazing at solving certain classes of problems. You're not going to
*  write a cat detector or even a language translation system by writing C code. That's not a very
*  productive way to do things anymore. And so machine learning is absolutely the right way to do that.
*  In fact, I would say that learned models are really one of the best ways to work with the human world
*  in general. And so anytime you're talking about sensory input of different modalities, anytime
*  that you're talking about generating things in a way that makes sense to a human, I think that
*  learned models are really, really useful. And that's because humans are very difficult to
*  characterize. And so this is a very powerful paradigm for solving classes of problems.
*  But on the other hand, imperative code is too. You're not going to write a bootloader for your
*  computer with a deep learning model. Deep learning models are very hardware intensive. They're
*  very energy intensive because you have a lot of parameters and you can provably implement any
*  function with a learned model. Like this has been shown, but that doesn't make it efficient.
*  And so if you're talking about caring about a few orders of magnitudes worth of energy usage,
*  then it's useful to have other tools in the toolbox.
*  There's also robustness too.
*  I mean, yeah, exactly. All the problems of dealing with data and bias and data,
*  all the problems of software 2.0. And one of the great things that Andres is arguing towards,
*  which I completely agree with him, is that when you start implementing things with deep learning,
*  you need to learn from software 1.0 in terms of testing, continuous integration, how you deploy,
*  how do you validate all these things and building systems around that so that you're not just saying
*  like, oh, it seems like it's good, ship it. Right. Well, what happens when I regress something? What
*  happens when I make a classification that's wrong and now I hurt somebody, right? I mean,
*  the same she have to reason about. Yeah. But at the same time, the bootloader that works for
*  us humans is a looks awfully a lot like a neural network, right? Yeah. It's messy and you can cut
*  out different parts of the brain. There's a lot of this neuroplasticity work that shows that it's
*  going to adjust. It's a, I mean, it's a really interesting question. How much of the world's
*  programming could be replaced by software 2.0? Like with, oh, well, I mean, it's provably
*  true that you could replace all of it. Right. So then it's right. So anything that's a function,
*  you can. So it's not a question about if I think it's a economic question. It's a,
*  what kind of talent can you get? What kind of trade-offs in terms of maintenance,
*  right? Those kinds of questions, I think, what kind of data can you collect? I think one of the
*  reasons that I'm most interested in machine learning as a programming paradigm is that one
*  of the things that we've seen across computing in general is that being laser focused on one paradigm
*  often puts you in a box. It's not super great. And so you look at object-oriented programming,
*  like it was all the rage in the early eighties and like everything has to be objects and
*  people forgot about functional programming, even though came first. And then people rediscovered
*  that, hey, if you mix functional and object-oriented and structure, like you mix these
*  things together, you can provide very interesting tools that are good at solving different
*  problems. And so the question there is how do you get the best way to solve the problems?
*  It's not about whose tribe should win, right? It's not about, you know, that shouldn't be the
*  question. The question is how do you make it so that people can solve those problems the fastest
*  and they have the right tools in their box to build good libraries and they can solve these
*  problems. And when you look at that, that's like, you know, you look at reinforcement learning as
*  one really interesting subdomain of this reinforcement learning. Often you have to have
*  the integration of a learned model combined with your Atari or whatever the other scenario it is
*  that you're working in. You have to combine that thing with the robot control for the arm,
*  right? And so now it's not just about that one paradigm. It's about integrating that with
*  all the other systems that you have, including often legacy systems and things like this,
*  right? And so to me, I think that the interesting thing to say is like, how do you get the best out
*  of this domain and how do you enable people to achieve things that they otherwise couldn't do
*  without excluding all the good things we already know how to do? Right. But, okay, this is a crazy
*  question, but we talked a little about GPT-3, but do you think it's possible that these language models
*  that in essence, in the language domain, software 2.0 could replace some aspect of compilation,
*  for example, or do program synthesis replace some aspect of programming?
*  Yeah, absolutely. So I think that the learned models in general are extremely powerful and
*  I think the people underestimate them. Maybe you can suggest what I should do. So I have
*  you know, I have access to the GPT-3 API. Would I be able to generate Swift code, for example?
*  Do you think that could do something interesting and would work? So GPT-3 is not probably not
*  trained on the right corpus. So it probably has the ability to generate some Swift. I bet it does.
*  It's probably not going to generate a large enough body of Swift to be useful. But like taking the
*  next step further, like if you had the goal of training something like GPT-3 and you wanted to
*  train it to generate source code, right? It could definitely do that. Now the question is,
*  how do you express the intent of what you want filled in? You can definitely like write scaffolding
*  of code and say fill in the hole and sort of put in some for loops or put in some classes or whatever
*  and the power of these models is impressive. But there's an unsolved question, at least unsolved
*  to me, which is how do I express the intent of what to fill in? Right? And kind of what you'd
*  really want to have, and I don't know that these models are up to the task, is you want to be able
*  to say, here's a scaffolding and here are the assertions at the end. And the assertions always
*  pass. And so you want a generative model on the one hand, yes. That's fascinating. Yeah. Right.
*  But you also want some loop back, some reinforcement learning system or something
*  where you're actually saying like, I need to hill climb towards something that is more correct.
*  And I don't know that we have that. So it would generate not only a bunch of the code,
*  but like the checks that do the testing, it would generate the tests. I think the humans would
*  generate the tests, right? Oh, okay. The tests would be fascinating. Well, the tests are the
*  requirements. Yes. But the, okay. So because you have to express to the model what you want to,
*  you don't just want gibberish code. Look at how compelling this code looks. You want a story about
*  four horned unicorns or something. Well, okay. So exactly. But that's human requirements. But then
*  I thought it's a compelling idea that the GPT four model could generate checks like that are more
*  high fidelity that check for correctness because the code it generates, like say I ask it to
*  generate a function that gives me the Fibonacci sequence. Sure. I don't like,
*  so, so decompose the problem, right? So you have, you have two things you have,
*  you need the ability to generate syntactically correct Swift code that that's interesting,
*  right? I think GPT series of model architectures can do that, but then you need the ability to
*  add the requirements. So generate Fibonacci. Yeah. The human needs to express that goal.
*  We don't have that language that I know of. No, I mean, it can generate stuff. Have you seen with
*  GPT three can generate, you can say, I mean, there's a interface stuff like it can generate HTML.
*  It can generate a basic four loops that give you like, right. But pick HTML. How do I say I want
*  google.com? Well, no, you could say, or not, not literally google.com. How do I say I want a web
*  page that's got a shopping cart into this and that? It does that. I mean, so, okay. So just,
*  I don't know if you've seen these demonstrations, but you type in, I want a red button with the text
*  that says hello. And you type that in natural language and it generates the correct HTML.
*  Okay. Done this demo. This it's kind of compelling. So you have to prompt it with
*  similar kinds of mappings. Of course, it's probably handpicked. I got to experiment that probably,
*  but the fact that you can do that once, even out of like 20, is quite impressive. Again,
*  that's very basic. Like the HTML is kind of messy and bad. But yes, the intent is the idea is the
*  intent is specified in natural language. Okay. And so I've not seen that. That's really cool.
*  Yeah. Yeah. But the question is the correctness of that. Like visually you can check, oh,
*  the button is red, but the, for more, uh, for more complicated functions where the intent is
*  hard to check, this goes into like empty completeness kind of things. Like I want to know that this code
*  is correct and generous, a giant thing that, uh, does some kind of calculation. It seems to be
*  working. It's interesting to think like, should the system also try to generate
*  checks for itself for correctness? Yeah, I don't know. And this is, this is way beyond my experience.
*  The, uh, uh, the thing that I think about is that there doesn't seem to be a lot of
*  equation or reasoning going on, right? There's a lot of pattern matching and filling in and
*  kind of propagating patterns that have been seen before into the future and into the
*  generated result. And so if you want to get correctness, you kind of need to improving
*  kind of things and like higher level logic. And I don't know that you could talk to Yann about that
*  and see, and see what, uh, the, the bright minds are thinking about right now, but I don't think
*  the GPT is in that, that vein. It's still really cool. Yeah. And surprisingly, who knows, you know,
*  maybe reasoning is, is, uh, is overrated. Yeah. Right. I mean, do we reason? Yeah. How do you tell
*  right? Are we just pattern matching based on what we have and then reverse justify to ourselves?
*  Exactly. The reverse. So like, I think what the neural networks are missing and I think GPT
*  form might have is to be able to tell stories to itself about what it did.
*  Well, that's what humans do. Right. I mean, you talk about, uh, like network explainability,
*  right. And we give neural nets a hard time about this, but humans don't know why we make decisions.
*  We have this thing called the intuition. And then we try to like say, this feels like the right thing,
*  but why? Right. And, you know, you wrestle with that when you're making hard decisions and
*  is that science? Not really. Let me ask you about a few high level questions, I guess is, um,
*  you've done a million things in your life and been very successful. A bunch of young folks,
*  listen to this, ask for advice from successful people like you. Uh, if you were to give advice
*  to, uh, somebody, you know, another graduate student or some high school student about, uh,
*  pursuing a career in computing or just advice about life in general, is there,
*  is there some words of wisdom you can give them? So I think you come back to change and,
*  you know, profound leaps happen because people are willing to believe that change is possible
*  and that, um, the world does change and are willing to do the hard thing that it takes to
*  make change happen. And whether it be implementing a new programming language or employing a new
*  system or employing a new research paper, designing a new thing, moving the world forward in science
*  and philosophy, whatever, it really comes down to somebody who's willing to put in the work.
*  Right. And you have the, the work is hard for a whole bunch of different reasons. One of which is,
*  um, you, uh, it's work, right? And so you have to have the space in your life in which you can do
*  that work, which is why going to grad school can be a beautiful thing for certain people. Um,
*  but also there's a self doubt that happens. Like you're two years into a project, is it going
*  anywhere? Right. Well, what do you do? Do you, do you just give up because it's hard? Oh, no. I mean,
*  some people like suffering. Um, and so you plow through it. The secret to me is that you have to
*  love what you're doing and, and follow that passion because if, when you get to the hard times, that's
*  when, you know, if you, if you love what you're doing, you're willing to kind of push through. And
*  this is really, uh, hard because it's, it's hard to know what you will love doing until you start
*  doing a lot of things. And so that's why I think that particularly early in your career, it's good
*  to experiment, do a little bit of everything, go, go take the survey class on, you know, for the first
*  half of every class in your upper division, you know, lessons and, um, just get exposure to things
*  because certain things will resonate with you and you'll find out, wow, I'm really good at this.
*  I'm really smart at this. Well, it's just because it's, it works with the way your brain.
*  And when something jumps out, I mean, that's one of the things that people often ask about is like,
*  well, I think there's a bunch of cool stuff out there. Like, how do I pick the thing?
*  Like, uh, yeah. How do you, how do you hook in your life? How did you just hook yourself in and
*  stuck with it? Well, I got lucky, right? I mean, I think that many people, uh, forget that a huge
*  amount of it or most of it is luck, right? So, um, let's not forget that. Um, so for me, I fell in
*  love with computers early on because I'm, they, they spoke to me, I guess, uh, uh, basic, but the, uh,
*  but then it was just kind of following a set of logical progressions, but also, um, deciding
*  that something that was hard was worth doing and, and a lot of fun. Right. And so I think that that
*  is also something that's true for many other domains, which is if you find something that you
*  love doing, that's also hard. If you invest yourself in it and add value to the world,
*  then it will mean something generally. Right. And again, that can be a research paper, that can be
*  a software system, that can be a new robot, that can be, that there's many things that that is,
*  that can be, but a lot of it is like real value comes from doing things that are hard.
*  And that doesn't mean you have to suffer, but, um, it's hard. I mean, you don't often hear that
*  message. We talked about it this last time a little bit, but I, I, it's one of my, not enough
*  people talk about this. Uh, it's, um, it's beautiful to hear a successful person. Well,
*  in self doubt and imposter syndrome, and these, these are all things that, uh, successful people
*  suffer with as well. Uh, particularly when they put themselves in a point of being uncomfortable,
*  which, um, I like to do now and then just because it puts you in learning mode.
*  Like if you want to, if you want to grow as a person, put yourself in a room with a bunch of
*  people that know way more about whatever you're talking about than you do and ask dumb questions.
*  And guess what? Smart people love to teach often, not always, but often. And if you listen,
*  if you're prepared to listen, if you're prepared to grow, if you're prepared to make connections,
*  you can do some really interesting things. And I think that a lot of progress is made by
*  people who kind of hop between domains down then, because they bring, uh, they bring a perspective
*  into a field that nobody else has. If people have only been working in that field themselves.
*  We mentioned that the universe is kind of like a compiler, uh, you know, the entirety of it,
*  the whole evolution is kind of a kind of compilation. Maybe our, us human beings are
*  kind of compilers. Um, let me ask the, the old sort of question that I didn't ask you last time,
*  which is, uh, what's the meaning of it all? Is there a meaning? Like if you asked a compiler, why,
*  what would a compiler say? What's the meaning of life? What's the meaning of life? Uh, you know,
*  I'm prepared for not to mean anything. Here we are all biological things programmed to survive
*  and, and propagate our, our DNA. Um, and maybe the universe is just a, just a computer and
*  you just go until entropy takes over the world and takes over the universe and then you're done.
*  Um, I don't think that's a very productive way to live your life if so.
*  And so I prefer to bias towards the other way, which is saying the world has,
*  the universe has a lot of value. And I take, uh, I take happiness out of other people.
*  And a lot of times part of that's having kids, but also the relationships you build with other
*  people. And so, uh, the way I try to live my life is like, what, what can I do that has value? How
*  can I move the world forward? How can I take what I'm good at and like bring it, bring it into the
*  world? And how can I, I'm one of these people that likes to work really hard and be very focused on
*  the things that I do. And so if I'm going to do that, how can it be in a domain that actually will
*  matter? Because a lot of things that we do, we find ourselves in the cycle of like, okay,
*  I'm doing a thing. I'm very familiar with it. I've done it for a long time. I've never done
*  anything else, but I'm not really learning. I'm not really, you know, I'm keeping things going,
*  but there's a, there's a younger generation that can do the same thing, maybe even better than me.
*  Right. Maybe if I actually step out of this and jump into something I'm less comfortable with,
*  it's scary. But on the other hand, um, it gives somebody else a new opportunity. It also then
*  puts you back in learning mode. And that can be really interesting. And one of the things I've
*  learned is that, uh, when you go through that, that first year deep into imposter syndrome,
*  but when you start working your way out, you start to realize, Hey, well, there's actually a method
*  to this. And, and now I'm able to add new things because they bring different perspective. And this
*  is one of the, the good things about bringing different kinds of people together. Diversity of
*  thought is really important. And, um, if you can pull together people that are coming at things
*  from different directions, you often get innovation. And I love to see that, that aha moment
*  where you're like, Oh, we've like really cracked. This is something that nobody's ever done before.
*  And then if you can do it in the context where it adds value, other people can build on it,
*  it helps move the world. Then that's what, that's what really excites me.
*  So the, that kind of description of the magic of the human experience, do you think we'll ever
*  create that in like an AGI system? You think we'll be able to create, uh, give, uh, give AI
*  systems a sense of meaning where they operate in this kind of world exactly in the way you've
*  described, which is they interact with each other. They interact with us humans.
*  Sure. Sure. Well, so, I mean, I, why, why are you being so a speciesist? Right. All right. So,
*  so AGI is versus bio net. So, you know, versus bio nets, um, you know, uh, what are we about
*  machines? Right. We're just programmed to run our, we have our objective function that we were
*  optimized for. Right. And so we're doing our thing. We think we have purpose, but do we really?
*  Yeah. Right. I'm not prepared to say that those newfangled AGI's have no soul just because we
*  don't understand them. Right. And I think that would be, um, when that, when they exist, uh,
*  that would be very premature to, uh, uh, look at a new thing through your own lens without
*  fully understanding it. Um, you might be just saying that because AI systems in the future
*  will be listening to this and then, oh, yeah, exactly. You don't want to say, please be nice
*  to me. You know, when Skynet, Skynet kills everybody, please spare me. So why is, why is,
*  uh, look ahead thinking. Yeah. But I mean, I think that people will spend a lot of time worrying
*  about this kind of stuff. And I think that what we should be worrying about is how do we make the
*  world better? And the thing that I'm most scared about with AGI's is not that, um, that necessarily
*  the Skynet will start shooting everybody with lasers and stuff like that to, to use us for our
*  calories. The thing that I'm worried about is that, um, humanity, I think needs a challenge.
*  And if we get into a mode of not having a personal challenge, not having a personal contribution,
*  whether that be like, you know, your kids and seeing what they grow into and helping,
*  helping guide them, whether it be, um, your community that you're engaged in, you're driving
*  forward, whether it be your work and the things that you're doing and the people you're working
*  with and the products you're building and the contribution there, if people don't have a
*  objective, I'm afraid what that means. And, um, I think that this would lead to a rise of the worst
*  part of people, right? Instead of people striving together and trying to make, uh, the world better,
*  could degrade into a very unpleasant world. But, but I don't know. I mean, we hopefully have a long
*  ways to go before we discover that. Unfortunately, we have pretty on the ground problems with the
*  pandemic right now. And so I think we should be focused on that as well. Yeah. Ultimately,
*  just as you said, you're optimistic. I think it helps for us to be optimistic.
*  Cause that's a fake it until you make it. Yeah. Well, and why not? What's the other side? Right.
*  So, I mean, uh, uh, I'm not personally a very religious person, but I've heard people say like,
*  oh yeah, of course I believe in God. Of course I go to church because if God's real,
*  I want to be on the right side of that. And if it's not real, it doesn't matter. Yeah. It doesn't
*  matter. And so, you know, that's, that's a fair way to do it. Um, yeah. I mean, the same thing with,
*  uh, with nuclear deterrence, all, you know, global warming, all these things, all these threats,
*  natural engineer pandemics, all these threats we face. I think it's, uh, uh, it's paralyzing
*  to be terrified of all the possible ways we could destroy ourselves. I think it's much better,
*  or at least productive to be hopeful and to engineer defenses against these things, to, uh,
*  engineer a future where like, you know, see like a positive future and engineer that future. Yeah.
*  Well, and I think that's other, another thing to think about as, you know, a human, particularly
*  if you're young and trying to figure out what it is that you want to be when you grow up, like I am.
*  Um, I'm always looking for that. Uh, the, the question then is how do you want to spend your
*  time? And right now there seems to be a norm of being a consumption culture. Like I'm going to
*  watch the news and, and revel in how horrible everything is right now. I'm going to go find
*  out about the latest atrocity and find out all the details of like the terrible thing that happened
*  and be outraged by it. Um, you can spend a lot of time watching TV and watching the new sitcom or
*  whatever people watch these days. I don't know. Um, uh, but that's a lot of hours, right? And those
*  are hours that if you're turned into being productive, learning, growing, experiencing,
*  you know, when the pandemic's over going, exploring, right? He leads to more growth.
*  And I think it leads to more optimism and happiness because you're, you're, you're building,
*  right? You're building yourself, you're building your capabilities, you're building your viewpoints,
*  you're building your perspective. And, um, I think that a lot of the cons the consuming of other
*  people's messages leads to kind of a negative viewpoint, which you need to be aware of what's
*  happening because that's also important, but there's a balance that, um, I think focusing on
*  creation is, is a very valuable thing to do. Yeah. So what you're saying is people should
*  focus on, uh, working on the sexiest field of them all, which is compiler design. Exactly.
*  Hey, you can go work on machine learning and be crowded out by the thousands of graduates popping
*  out of school. They'd all want to do the same thing, or you could work in the place that people
*  overpay you because there's not enough smart people working in it. And, uh, here at the end
*  of Moore's law, according to some people, uh, actually the software is a hard part too.
*  Yeah. Uh, I mean, optimization is, is truly, uh, truly beautiful. And also on the YouTube side or
*  education side, uh, you know, it's, there's, um, it'd be nice to have some material that shows the
*  beauty of compilers. Yeah. Yeah. That's, that's something. So that's a call for, uh, for people
*  to create that kind of content as well. Chris, uh, you're one of my favorite people to talk to. I,
*  uh, it's such a huge honor that you would waste your time talking to me. Uh, I've always appreciated.
*  Thank you so much for talking to me today. The, the, the, the truth of it is you spent a lot of time
*  talking to me just on, you know, walks and other things like that. So it's, it's great to catch up.
*  Thanks, man. Thanks for listening to this conversation with Chris Latner. And thank you
*  to our sponsors, Blinkist, an app that summarizes key ideas from thousands of books, Neuro, which is
*  a maker of functional gum and mints that supercharge my mind, Masterclass, which are
*  online courses from world experts. And finally Cash App, which is an app for sending money to
*  friends. Please check out these sponsors in the description to get a discount and to support this
*  podcast. If you enjoy this thing, subscribe on YouTube, review it with five stars on Apple podcast,
*  follow on Spotify, support on Patreon, connect with me on Twitter, Alex Friedman. And now let
*  me leave you with some words from Chris Latner. So much of language design is about trade-offs
*  and you can't see those trade-offs unless you have a community of people that really represent
*  those different points. Thank you for listening and hope to see you next time.

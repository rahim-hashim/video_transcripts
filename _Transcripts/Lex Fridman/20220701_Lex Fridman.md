---
Date Generated: April 10, 2024
Transcription Model: whisper medium 20231117
Length: 7839s
Video Keywords: ['agi', 'ai', 'ai podcast', 'alphafold', 'alphazero', 'artificial intelligence', 'artificial intelligence podcast', 'biology', 'consciousness', 'deepmind', 'demis hassabis', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'mit ai', 'muzero']
Video Views: 1394759
Video Rating: None
---

# Demis Hassabis: DeepMind - AI, Superintelligence & the Future of Humanity | Lex Fridman Podcast #299
**Lex Fridman:** [July 01, 2022](https://www.youtube.com/watch?v=Gfr50f6ZBvo)
*  The following is a conversation with Demis Hasabis, CEO and co-founder of DeepMind,
*  a company that has published and built some of the most incredible artificial intelligence systems
*  in the history of computing, including AlphaZero that learned all by itself to play the game of Go
*  better than any human in the world and AlphaFold2 that solved protein folding. Both tasks considered
*  nearly impossible for a very long time. Demis is widely considered to be one of the most brilliant
*  and impactful humans in the history of artificial intelligence and science and engineering in general.
*  This was truly an honor and a pleasure for me to finally sit down with him for this conversation
*  and I'm sure we will talk many times again in the future. This is the Lux Free From The Podcast. To
*  support it, please check out our sponsors in the description. And now, dear friends, here's Demis
*  Hasabis. Let's start with a bit of a personal question. Am I an AI program you wrote to interview
*  people until I get good enough to interview you? Well, I'd be impressed if you were. I'd be
*  impressed with myself if you were. I don't think we're quite up to that yet, but maybe you're from
*  the future, Lex. If you did, would you tell me? Is that a good thing to tell a language model
*  that's tasked with interviewing that it is in fact AI? Maybe we're in a kind of meta-turing test.
*  Probably it would be a good idea not to tell you so it doesn't change your behavior, right? This is a
*  kind of—Eisenberg uncertainty principle situation. If I told you you behave differently, maybe that's
*  what's happening with us, of course. This is a benchmark from the future where they replay 2022
*  as a year before AIs were good enough yet and now we want to see, is it going to pass? Exactly.
*  If I was such a program, would you be able to tell, do you think? So to the Turing test question,
*  you've talked about the benchmark for solving intelligence. What would be the impressive thing?
*  You've talked about winning a Nobel Prize in AI system, winning a Nobel Prize, but I still return
*  to the Turing test as a compelling test. The spirit of the Turing test is a compelling test.
*  Yeah, the Turing test, of course, it's been unbelievably influential and Turing's one of
*  my all-time heroes. But I think if you look back at the 1950 paper, his original paper,
*  and read the original, you'll see I don't think he meant it to be a rigorous formal test. I think
*  it was more like a thought experiment, almost a bit of philosophy he was writing if you look
*  at the style of the paper. You can see he didn't specify it very rigorously. For example,
*  he didn't specify the knowledge that the expert or judge would have, how much time would they have to
*  investigate this. So these are important parameters if you were going to make it a true
*  formal test. By some measures, people claim the Turing test passed several decades ago. I
*  remember someone claiming that with a very bog standard, normal logic model because they
*  pretended it was a kid. So the judges thought that the machine was a child. So that would be
*  very different from an expert AI person interrogating a machine and knowing how it was built and so on.
*  So I think we should probably move away from that as a formal test and move more towards
*  general tests where we test the AI capabilities on a range of tasks and see if it reaches human
*  level or above performance on maybe thousands, perhaps even millions of tasks eventually,
*  and cover the entire sort of cognitive space. So I think for its time, it was an amazing thought
*  experiment and also 1950s, obviously, it was barely the dawn of the computer age. So of course,
*  he only thought about text and now we have a lot more different inputs. So yeah, maybe the better
*  thing to test is the generalizability across multiple tasks. But I think it's also possible
*  as systems like Gado show that eventually that might map right back to language. So you might be
*  able to demonstrate your ability to generalize across tasks by then communicating your ability
*  to generalize across tasks, which is kind of what we do through conversation anyway, when we jump
*  around. Ultimately, what's in there in that conversation is not just you moving around
*  knowledge. It's you moving around like these entirely different modalities of understanding
*  that ultimately map to your ability to operate successfully in all of these domains,
*  which you can think of as tasks. Yeah, I think certainly we as humans use language as our main
*  generalization communication tool. So I think we end up thinking in language and expressing
*  our solutions in language. So it's going to be very powerful mode in which to explain, you know,
*  the system to explain what it's doing. But I don't think it's the only modality that matters.
*  So I think there's going to be a lot of, you know, there's a lot of different ways to express
*  capabilities, other than just language. Yeah, visual, robotics, body language.
*  Yeah, actions, the interactive aspect of all that. That's all part of it.
*  But what's interesting with GATO is that it's sort of pushing prediction to the maximum in terms of
*  like, you know, mapping arbitrary sequences to other sequences and sort of just predicting
*  what's going to happen next. So prediction seems to be fundamental to intelligence.
*  And what you're predicting doesn't so much matter.
*  Yeah, it seems like you can generalize that quite well. So obviously, language models predict the
*  next word. GATO predicts potentially any action or any token. And it's just the beginning, really.
*  It's our most general agent, one could call it so far. But, you know, that itself can be scaled up
*  massively more than we've done so far. And obviously, we're in the in the middle of doing that.
*  But the big part of solving AGI is creating benchmarks that help us get closer and closer,
*  sort of creating benchmarks that test the generalizability. And it's just still
*  interesting that this fella, Alan Turing, was one of the first and probably still one of the
*  only people that was trying, maybe philosophically, but was trying to formulate a benchmark that could
*  be followed. It is, even though it's fuzzy, it's still sufficiently rigorous to where you can run
*  that test. And I still think something like the Turing test will, at the end of the day,
*  be the thing that truly impresses other humans so that you can have a close friend who's an AI
*  system. For that friend to be a good friend, they're going to have to be able to play Star
*  Crafts. And they're going to have to do all of these tasks, get you a beer, so the robotics tasks,
*  play games with you, use language, humor, all those kinds of things. But that ultimately can
*  boil down to language. It feels like not in terms of the AI community, but in terms of the actual
*  impact of general intelligence on the world, it feels like language will be the place where
*  it truly shines. I think so, because it's such an important kind of input-output for us. I think
*  you're right. I think the Turing test, the kind of the philosophy behind it, which is the idea of,
*  can a machine mimic the behaviors of a human? And I would say wider than just language and text,
*  then in terms of actions and everything else, creativity, all these things, then
*  if it can sort of match or exceed human cognitive capabilities, then I think we have a true
*  intelligence. So from that perspective, you're right. I think he did formulate the right kind
*  of setup. I think there'll be a kind of humor in the AI systems of the future, looking back to this
*  conversation and thinking about the Turing test and also thinking about by that time,
*  they would know which year they were finally able to sort of cross the threshold of human-level
*  intelligence and think how funny it is that we humans were still confused about this whole problem
*  that's been long ago been solved. Well, hello to the AI agents of the future. Anyway, so going
*  back to your journey, when did you fall in love with programming first?
*  Well, I was pretty young age, actually. So I started off, actually games was my first love,
*  so starting to play chess when I was around four years old. And then it was actually with
*  winnings from a chess competition that I managed to buy my first chess computer when I was about
*  eight years old. It was a ZX Spectrum, which was hugely popular in the UK at the time.
*  And it was amazing machine because I think it trained a whole generation of programmers in
*  the UK because it was so accessible. You literally switched it on and there was the basic prompt and
*  you could just get going. And my parents didn't really know anything about computers. So because
*  it was my money from a chess competition, I could say I wanted to buy it. And then I just went to
*  bookstores, got books on programming, and started typing in the programming code. And then of course,
*  once you start doing that, you start adjusting it and then making your own games. And that's when
*  I fell in love with computers and realized that they were very magical device. In a way, I kind
*  of I wouldn't have been able to explain this at the time, but I felt that they were sort of almost
*  a magical extension of your mind. I always had this feeling and I've always loved this about
*  computers that you can set them off doing something, some task for you, you can go to sleep,
*  come back the next day and it's solved. That feels magical to me. So I mean, all machines do that to
*  some extent, they all enhance our natural capabilities. Obviously, cars make us allow us to
*  move faster than we can run. But this was a machine to extend the mind. And then of course, AI
*  is the ultimate expression of what a machine may be able to do or learn. So very naturally for me,
*  that thought extended into AI quite quickly. Do you remember the programming language
*  that was first started in? Was it special to the machine? No, it was just a basic. I think it was
*  just basic on the ZX Spectrum. I don't know what specific form it was. And then later on, I got a
*  Commodore Amiga, which was a fantastic machine. Now you're just showing off. So yeah, well, lots of
*  my friends had Atari STs and I managed to get Amigas, it was a bit more powerful. And that was
*  incredible. And I used to do programming in assembler and also Amos basic, this specific
*  form of basic. It was incredible actually. So I learned all my coding skills. And when did you
*  fall in love with AI? So when did you first start to gain an understanding that you can not just
*  write programs that do some mathematical operations for you while you sleep, but something that's
*  akin to bringing an entity to life? Sort of a thing that can figure out something more complicated
*  than a simple mathematical operation. Yeah, so there was a few stages for me, or while I was
*  very young. So first of all, as I was trying to improve at playing chess, I was captaining various
*  England junior chess teams. And at the time, when I was about, you know, maybe 10, 11 years old,
*  I was going to become a professional chess player. That was my first thought.
*  So that dream was there to try to get to the highest level.
*  Yeah. So I was, you know, I got to when I was about 12 years old, I got to master standard,
*  I was second highest rated player in the world to Judith Polger, who obviously ends up being
*  an amazing chess player, and a world women's champion. And when I was trying to improve at
*  chess, what you do is you obviously, first of all, you're trying to improve your own thinking
*  processes. So that leads you to thinking about thinking, how is your brain coming up with these
*  ideas? Why is it making mistakes? How can you how can you improve that thought process? But the
*  second thing is that you it was just the beginning. This is like in the in the early 80s, mid 80s of
*  chess computers, if you remember, they were physical boards like the one we have in front
*  of us. And you press down the, you know, the squares. And I think Kasparov had a branded
*  version of it that I got. And you were you know, used to that they're not as strong as they are
*  today. But they were they were pretty strong. And you used to practice against them to try and
*  improve your openings and other things. And so I remember, I think I probably got my first one was
*  around 11 or 12. And I remember thinking, this is amazing, you know, how someone programmed this
*  this chess board to play chess. And it was very formative book I bought, which was called the
*  chess computer handbook by David Levy, it's kind of came out in 1984 or something. So I must have
*  got it when I was about 1112. And it explained fully how these chess programs were made. And I
*  remember my first AI program being programming my Amiga, it couldn't, it wasn't powerful enough to
*  play chess, I couldn't write a whole chess program. But I wrote a program for it to play Othello,
*  reverse it's sometimes called I think in the US. And so a slightly simpler game than chess,
*  but I used all of the principles that chess programs had alpha beta search, all of that.
*  And that was my first AI program. Remember that very well, it's around 12 years old. So that that
*  brought me into AI. And then the second part was later on, when I was around 1617. And I was writing
*  games professionally designing games, writing a game called theme park, which had AI as a core
*  gameplay component as part of the simulation. And it sold, you know, millions of copies around the
*  world. And people loved the way that the AI, even though it was relatively simple by today's AI
*  standards, was was reacting to the way you as the player played it. So it was called a sandbox game.
*  So it's one of the first types of games like that, along with SimCity. And it meant that every game
*  you played was unique. Is there something you could say just on a small tangent about really
*  impressive AI from a game design, human enjoyment perspective, really impressive AI that you've seen
*  in games? And maybe what does it take to create AI system? And how hard of a problem is that? So a
*  million questions that would just as a brief tangent. Well, look, I think games, games have
*  been significant in my life for three reasons. So first of all, to I was playing them and training
*  myself on games when I was a kid, then I went through a phase of designing games and writing AI
*  for games. So all the games I professionally wrote had AI as a core component. And that was mostly in
*  the 90s. And the reason I was doing that in games industry was at the time, the games industry,
*  I think was the cutting edge of technology. So whether it was graphics with people like John
*  Carmack and Quake and those kinds of things, or AI, I think actually all the action was going on in
*  games. And we're still reaping the benefits of that even with things like GPUs, which I find ironic
*  was obviously invented for graphics, computer graphics, but then turns out to be amazingly
*  useful for AI. It just turns out everything's a matrix multiplication appears in the whole world.
*  So I think games at the time had the most cutting edge AI. And a lot of the games,
*  I was involved in writing. So there was a game called Black and White, which was one game I was
*  involved with in the early stages of, which I still think is the most impressive example of
*  reinforcement learning in a computer game. So in that game, you trained a little pet animal.
*  It's a brilliant game.
*  Yeah. And it sort of learned from how you were treating it. So if you treated it badly,
*  then it became mean. And then it would be mean to your villages and your population, the sort of
*  little tribe that you were running. But if you were kind to it, then it would be kind.
*  And people were fascinated by how that works. And so was I, to be honest with the way it kind of
*  developed. And- Especially the mapping to good and evil.
*  Yeah. Made you realize,
*  made me realize that you can sort of in the way, in the choices you make, can define
*  where you end up. And that means all of us are capable of the good evil. It all matters in
*  the different choices along the trajectory to those places that you make. It's fascinating.
*  I mean, games can do that philosophically to you. And it's rare. It seems rare.
*  Yeah. Well, games are, I think, a unique medium because you as the player, you're not just
*  passively consuming the entertainment. You're actually actively involved as an agent. So I
*  think that's what makes it in some ways can be more visceral than other mediums like films and
*  books. So the second, so that was designing AI in games. And then the third use we've used of AI
*  is in deep mind from the beginning, which is using games as a testing ground for proving out
*  algorithms and developing AI algorithms. And that was a sort of a core component of our vision at
*  the start of deep mind was that we would use games very heavily as our main testing ground,
*  certainly to begin with, because it's super efficient to use games. And also, it's very
*  easy to have metrics to see how well your systems are improving and what direction your ideas are
*  going in and whether you're making incremental improvements. And because those games are often
*  rooted in something that humans did for a long time beforehand, there's already a strong set of
*  rules. Like it's already a damn good benchmark. Yes. It's really good for so many reasons because
*  you've got clear measures of how good humans can be at these things. And in some cases like Go,
*  we've been playing it for thousands of years. And often they have scores or at least win conditions.
*  So it's very easy for reward learning systems to get a reward. It's very easy to specify what that
*  reward is. And also at the end, it's easy to test externally how strong is your system by, of course,
*  playing against the world's strongest players at those games. So it's so good for so many reasons.
*  And it's also very efficient to run potentially millions of simulations in parallel on the cloud.
*  So I think there's a huge reason why we were so successful back in starting out 2010. How come
*  we were able to progress so quickly because we utilize games. And at the beginning of DeepMind,
*  we also hired some amazing game engineers who I knew from my previous lives in the games industry.
*  And that helped to bootstrap us very quickly. And plus it's somehow super compelling, almost
*  at a philosophical level of man versus machine over chessboard or a go board. And especially
*  given that the entire history of AI is defined by people saying it's going to be impossible to
*  make a machine that beats a human being in chess. And then once that happened, people were certain
*  when I was coming up in AI that go is not a game that can be solved because of the combinatorial
*  complexity. It's just too, it's, you know, no matter how much Moore's law you have,
*  compute is just never going to be able to crack the game of go. And so then there's something
*  compelling about facing sort of taking on the impossibility of that task from the AI
*  researcher perspective, engineer perspective. And then as a human being, just observing this whole
*  thing, your beliefs about what you thought was impossible being broken apart, it's
*  humbling to realize we're not as smart as we thought. It's humbling to realize that the things
*  we think are impossible now perhaps will be done in the future. There's something really powerful
*  about a game, AI system, being a human being in a game that drives that message home for like
*  millions, billions of people, especially in the case of go. Sure. Well, look, I think it's a,
*  I mean, it has been a fascinating journey. And especially as I think about it from, I can
*  understand it from both sides, both as the AI, you know, creators of the AI, but also as a games
*  player originally. So, you know, it was a really interesting, you know, I mean, it was a fantastic,
*  but also somewhat bittersweet moment, the Alpha Go match for me, seeing that and being obviously
*  heavily involved in that. But, you know, as you say, chess has been the, I mean, Kasparov,
*  I think rightly called it the drosophila of intelligence, right? So it's sort of, I love
*  that phrase. And I think he's right because chess has been hand in hand with AI from the beginning
*  of the whole field, right? So I think every AI practitioner starting with Turing and Claude
*  Shannon and all those, the sort of forefathers of the field, tried their hand at writing a chess
*  program. I've got an original edition of Claude Shannon's first chess program, I think it was 1949,
*  the original sort of paper. And they all did that. And Turing famously wrote a chess program that,
*  but all the computers around then were obviously too slow to run it. So he had to run, he had to
*  be the computer, right? So he literally, I think, spent two or three days running his own program
*  by hand with pencil and paper and playing a friend of his with his chess program. So,
*  of course, Deep Blue was a huge moment, beating Kasparov. But actually, when that happened,
*  I remember that very, very vividly, of course, because it was, you know, chess and computers
*  and AI, all the things I loved, and I was at college at the time. But I remember coming away
*  from that being more impressed by Kasparov's mind than I was by Deep Blue. Because here was Kasparov
*  with his human mind, not only could he play chess more or less to the same level as this
*  brute of a calculation machine. But of course, Kasparov can do everything else humans can do,
*  ride a bike, talk many languages, do politics, all the rest of the amazing things that Kasparov does.
*  And so with the same brain, and yet Deep Blue, brilliant as it was at chess, it'd been hand coded
*  for chess, and actually had distilled the knowledge of chess grandmasters into a cool program,
*  but it couldn't do anything else. Like it couldn't even play a strictly simpler game like Tic-Tac-Toe.
*  So something to me was missing from intelligence from that system that we would regard as
*  intelligence. And I think it was this idea of generality, and also learning. So that's what we
*  tried to do with AlphaGo. Yeah, with AlphaGo and AlphaZero, MuZero, and then Godot, and all the
*  things that will get into some parts of there's just a fascinating trajectory here. But let's
*  just stick on chess briefly. On the human side of chess, you've proposed that from a game design
*  perspective, the thing that makes chess compelling as a game is that there's a creative tension
*  between a bishop and the knight. Can you explain this? First of all, it's really interesting to
*  think about what makes a game compelling, makes it stick across centuries. Yeah, I was sort of
*  thinking about this. And actually, a lot of even amazing chess players don't think about it
*  necessarily from a game's designer point of view. So it's with my game design hat on that I was
*  thinking about this. Why is chess so compelling? And I think a critical reason is the dynamicness
*  of the different kind of chess positions you can have, whether they're closed or open and other
*  things, comes from the bishop and the knight. So if you think about how different the capabilities
*  of the bishop and knight are in terms of the way they move, and then somehow chess has evolved to
*  balance those two capabilities more or less equally. So they're both roughly worth three points each.
*  So you think that dynamics is always there and then the rest of the rules are kind of trying to
*  stabilize the game? Well, maybe. I mean, it's sort of I don't know, chicken and egg situation,
*  probably both came together. But the fact that it's got to this beautiful equilibrium,
*  where you can have the bishop and knight that are so different in power, but so equal in value across
*  the set of the universe of all positions, right? Somehow they've been balanced by humanity over
*  hundreds of years, I think gives the game the creative tension that you can swap the bishop
*  and knights for a bishop for a knight and they're more or less worth the same. But now you aim for
*  a different type of position. If you have the knight, you want a closed position. If you have
*  the bishop, you want an open position. So I think that creates a lot of the creative tension in
*  chess. So some kind of controlled creative tension. From an AI perspective, do you think
*  AI systems could eventually design games that are optimally compelling to humans?
*  Well, that's an interesting question. You know, sometimes I get asked about AI and creativity.
*  And the way I answered that is relevant to that question, which is that I think there are different
*  levels of creativity, one could say. So I think if we define creativity as coming up with something
*  original, right, that's that's useful for a purpose, then, you know, I think the kind of
*  lowest level of creativity is like an interpolation. So an averaging of all the examples you see. So
*  maybe very basic AI system could say you could have that. So you show it millions of pictures
*  of cats. And then you say, give me an average looking cat, right, generate me an average looking
*  cat, I would call that interpolation. Then there's extrapolation, which something like AlphaGo showed.
*  So AlphaGo played, you know, millions of games of go against itself. And then it came up with
*  brilliant new ideas like move 37 in game two, brilliant motif strategies and go that that no
*  humans had ever thought of, even though we've played it for 1000s of years and professionally
*  for hundreds of years. So that that I call that extrapolation. But then that's still there's still
*  a level above that, which is, you know, you could call out of the box thinking or true innovation,
*  which is, could you invent go? Right? Could you invent chess and not just come up with a
*  brilliant chess move or brilliant go move? But can you can you actually invent chess or something as
*  good as chess or go? And I think one day, AI could, but the what's missing is how would you even
*  specify that task to a program right now. And the way I would do it, if I was best telling a human
*  to do it, or games designer, human games designer to do it is I would say something like go, I would
*  say, come up with a game that only takes five minutes to learn, which go does because it's got
*  simple rules, but many lifetimes to master, right, or impossible to master in one lifetime, because
*  it's so deep and so complex. And then it's aesthetically beautiful. And also, it can be
*  completed in three or four hours of gameplay time, which is, you know, useful for our us, you know,
*  in a human day. And so you might specify these side of high level concepts like that. And then,
*  you know, with that, and maybe a few other things, one could imagine that go satisfies those
*  constraints. But the problem is, is that we were not able to specify abstract notions like that,
*  high level abstract notions like that yet to our AI systems. And I think there's still something
*  missing there in terms of high level concepts or abstractions that they truly understand and,
*  you know, combinable and compositional. So for the moment, I think AI is capable of doing
*  interpolation and extrapolation, but not true invention. So coming up with rule sets,
*  and optimizing with complicated objectives around those rule sets, we can't currently do. But you
*  could take a specific rule set, and then run a kind of self play experiment to see how long,
*  just observe how an AI system from scratch learns, how long is that journey of learning.
*  And maybe if it satisfies some of those other things you mentioned in terms of quickness to
*  learn and so on. And you could see a long journey to master for even an AI system,
*  then you could say that this is a promising game. But it would be nice to do almost like
*  alpha codes or programming rules. So generating rules that kind of that automate even that part
*  of the generation of rules. So I have thought about systems actually,
*  I think be amazing in for a games designer, if you could have a system that takes your game,
*  plays it 10s of millions of times, maybe overnight, and then self balances the rules
*  better. So get tweaks the rules, and the maybe the equations and the parameters, so that the game
*  is more balanced, the units in the game or some of the rules could be tweaked. So it's a bit of like
*  giving a base set and then allowing Monte Carlo tree search or something like that to sort of
*  explore it. And I think that would be super, super powerful tool actually for balancing,
*  auto balancing a game, which usually takes 1000s of hours from 100s of games, human games testers
*  normally to balance some one game like StarCraft, which is Blizzard are amazing at balancing their
*  games, but it takes them years and years and years. So one could imagine at some point when
*  this stuff becomes efficient enough to you might better do that like overnight.
*  Do you think a game that is optimal design by an AI system would look very much like a planet Earth?
*  Maybe, maybe it's only the sort of game I would love to make is is and I've tried,
*  you know, my in my in my games career, the games design career, you know, my first big game was
*  designing a theme park, an amusement park, then with games like Republic, I tried to, you know,
*  have games where we designed whole cities and allowed you to play in. So and of course,
*  people like Will Wright have written games like SimEarth, trying to simulate the whole of Earth,
*  pretty tricky. But I said, Merth, I haven't actually played that one. So what is it? Does it
*  is sort of a pre evolution? Yeah, it has evolution. And it's sort of, it tries to,
*  it sort of treats it as an entire biosphere, but from quite high level. So nice to be able to sort
*  of zoom in, zoom out, zoom in. Exactly. So obviously, it couldn't do that was in the night.
*  I think he wrote that in the 90s. So it couldn't, you know, it wasn't it wasn't able to do that.
*  But that that would be obviously the ultimate sandbox game, of course.
*  On that topic, do you think we're living in a simulation?
*  Yes. Well, so okay, so I'm going to jump around from the absurdly philosophical to the
*  short, short, very, very happy to so I think my answer to that question is a little bit complex,
*  because there is simulation theory, which obviously Nick Bostrom, I think famously first proposed.
*  And I don't quite believe it in in that sense. So in the in the sense that are we in some sort
*  of computer game, or have our descendants somehow recreated earth in the, you know,
*  21st century and some for some kind of experimental reason, I think that, but I do think that we that
*  that we might be that the best way to understand physics, and the universe is from a computational
*  perspective. So understanding it as an information universe, and actually information being the most
*  fundamental unit of reality, rather than matter or energy. So physicists would say, you know,
*  matter or energy, you know, equals MC squared, these are the things that are the fundamentals
*  of the universe, I'd actually say information, which of course itself can be can specify energy
*  or matter, right? Matter is actually just, you know, we're, we're just out the way our bodies and
*  the molecules in our body are arranged is information. So I think information may be
*  the most fundamental way to describe the universe. And therefore, you could say we're in some sort of
*  simulation because of that. But I don't I do I'm not I'm not really subscriber to the idea that,
*  you know, they these are sort of throw away billions of simulations around, I think this is
*  actually very critical and possibly unique, this simulation.
*  Particular one. Yes. So but and you just mean treating the universe as a computer
*  that's processing and modifying information is a good way to solve the problems of physics,
*  of chemistry, of biology, and perhaps of humanity and so on.
*  Yes, I think understanding physics in terms of information theory,
*  it might be the best way to really understand what's going on here.
*  From our understanding of universal Turing machine, from our understanding of a computer,
*  do you think there's something outside of the capabilities of a computer that is present in
*  our universe? You have a disagreement with Roger Penrose about the nature of consciousness. He
*  thinks that consciousness is more than just a computation. Do you think all of it, the whole
*  shebang is the kind can be can be a copy? Yeah, I've had many fascinating debates with
*  Sir Roger Penrose. And obviously, he's he's famously and I read, you know, Emperors of the
*  New Mind and and, and his books, his classical books, and they were pretty influential in the,
*  you know, in the 90s. And he believes that there's something more, something quantum that is needed
*  to explain consciousness in the brain. I think about what we're doing, actually, at DeepMind,
*  and what my career is being, we're almost like Turing's champion. So we are pushing Turing
*  machines or classical computation to the limits, what are the limits of what classical computing
*  can do now. And at the same time, I've also studied neuroscience to see and that's why I did my PhD
*  in was to see, also to look at, you know, is there anything quantum in the brain from a neuroscience
*  or biological perspective? And, and so far, I think most neuroscientists and most mainstream
*  biologists and neuroscientists would say there's no evidence of any quantum systems or effects in
*  the brain. As far as we can see, it's it can be mostly explained by classical, classical theories.
*  So and then so there's sort of the the search from the biology side. And then at the same time,
*  there's the raising of the water at the bar from what classical Turing machines can do.
*  And, and, you know, including our new AI systems. And as you alluded to earlier,
*  you know, I think AI, especially in the last decade plus has been a continual story now surprising
*  events and surprising successes, knocking over one theory after another of what was thought to be
*  impossible, you know, from go to protein folding, and so on. And so I think I would be very hesitant
*  to bet against how far the universal Turing machine and classical computation paradigm can go.
*  And my betting would be that all of certainly what's going on in our brain can probably be
*  mimicked or approximated on a classical machine, not, you know, not requiring something metaphysical
*  or quantum. And we'll get there with some of the work with alpha fold, which I think begins the
*  journey of modeling this beautiful and complex world of biology. So you think all the magic of
*  the human mind comes from this just a few pounds of mush, biological computational mush, that's
*  akin to some of the neural networks, not directly, but in spirit that deep mind has been working with.
*  Jason Vale Well, look, I think it's, you say it's a few,
*  you know, of course, it's this is the I think the biggest miracle of the universe is that
*  it's just a few pounds of mush in our skulls. And yet it's also our brains and the most complex
*  objects in that we know of in the universe. So there's something profoundly beautiful and
*  amazing about our brains. And I think that it's an incredibly, incredible, efficient machine. And
*  and it's, you know, a phenomenon, basically. And I think that building AI, one of the reasons I want
*  to build AI, and I've always wanted to is, I think by building an intelligent artifact like AI,
*  and then comparing it to the human mind, that will help us unlock the uniqueness and the true
*  secrets of the mind that we've always wondered about since the dawn of history, like consciousness,
*  dreaming, creativity, emotions, what are all these things, right? We've wondered about them since the
*  dawn of humanity. And I think one of the reasons and you know, I love philosophy and philosophy of
*  mind is, we found it difficult is there haven't been the tools for us to really other than
*  introspection to from very clever people in history, very clever philosophers to really
*  investigate this scientifically. But now, suddenly we have a plethora of tools. Firstly, we have all
*  the neuroscience tools, fMRI machines, single cell recording, all of this stuff. But we also have
*  the ability computers and AI to build intelligent systems. So I think that, you know, I think it is
*  amazing what the human mind does. And, and, and I'm kind of in awe of it, really. And, and I think
*  it's amazing that without human minds, we're able to build things like computers, and actually even,
*  you know, think and investigate about these questions. I think that's also a testament
*  to the human mind. Yeah, the universe built the human mind that now is building computers that help
*  us understand both the universe and our own human mind. Right. Exactly. And I mean, I think that's
*  one, you know, one could say we are, maybe we're the mechanism by which the universe is going to
*  try and understand itself. Yeah. It's beautiful. So let's, let's go to the basic building blocks
*  of biology that I think is another angle at which you can start to understand the human mind, the
*  human body, which is quite fascinating, which is from the basic building blocks, start to simulate,
*  start to model how from those building blocks, you can construct bigger and bigger, more complex
*  systems, maybe one day the entirety of the human biology. So here's another problem that thought
*  to be impossible to solve, which is protein folding and Alpha Fold or specific Alpha Fold 2
*  did just that. It's solved protein folding. I think it's one of the biggest breakthroughs,
*  certainly in the history of structural biology, but in general and in science,
*  um, maybe from a high level, what is it and how does it work? And then we can ask some fascinating
*  questions after. Sure. Um, so maybe I to explain it to people not familiar with protein folding is,
*  you know, first of all, explain proteins, which is, you know, proteins are essential to all life.
*  Every function in your body depends on proteins. Sometimes they're called the workhorses of biology.
*  And if you look into them, and I've, you know, obviously as part of Alpha Fold, I've been
*  researching proteins and, and, and structural biology for the last few years, you know,
*  they're amazing little bio nano machines, proteins, incredible if you actually watch little videos of
*  how they work animations of how they work and, um, proteins are specified by their genetic sequence
*  called the amino acid sequence. So you can think of it as their genetic makeup. And then in the body,
*  uh, in, in nature, they, when they, when they fold up into a 3d structure, so you can think of it as
*  a string of beads, and then they fold up into a ball. Now, the key thing is you want to know what
*  that 3d structure is, um, because the structure, the 3d structure of a protein, uh, is what, uh,
*  helps to determine what does it do, the function it does in your body. Uh, and also if you're
*  interested in drug drugs or disease, you need to understand that 3d structure, because if you want
*  to target something with a drug compound about to block something, the proteins doing, uh, you need
*  to understand where it's going to bind on the surface of the protein. So obviously in order to
*  do that, you need to understand the 3d structure. So the structure is mapped to the function.
*  The structure is mapped to the function and the structure is obviously somehow specified by the,
*  by the amino acid sequence. And that's the, in essence, the protein folding problem is,
*  can you just from the amino acid sequence, the one dimensional, uh, string of letters,
*  can you immediately computationally predict the 3d structure? Right. And this has been a grand
*  challenge in biology for over 50 years. So I think it was first articulated by Christian
*  Anfinsen, a Nobel prize winner in 1972, uh, as part of his Nobel prize winning lecture.
*  And he just speculated this should be possible to go from the amino acid sequence to the 3d
*  structure, but he didn't say how. So it was, it, I, you know, I've been, it's been described to me
*  as, as equivalent to Fermat's last theorem, but for biology, right? You should, as somebody that
*  very well might win the Nobel prize in the future, but outside of that,
*  you should do more of that kind of thing in the margins, just put random things that will take
*  like 200 years to solve. Set people off for 200 years. It should be possible. Exactly.
*  And just don't give any intentions. Exactly. I think everyone's exactly, it should be,
*  I'll have to remember that for future. So yeah, so he set off, you know, with this one throw away
*  remark, just like Fermat, you know, he, he set off this whole 50 year, uh, uh, uh, uh, field really
*  of computational biology and, and they had, you know, they got stuck, they hadn't really got very
*  far with doing this. And, and, um, until now, until alpha fold came along, this is done
*  experimentally, right? Very painstakingly. So the rule of thumb is, and you have to like
*  crystallize the protein, which is really difficult. Some proteins can't be crystallized
*  like membrane proteins. And then you have to use very expensive electron microscopes or
*  X-ray crystallography machines, really painstaking work to get the 3d structure and visualize the
*  3d structure. So the rule of thumb in, in, in experimental biology is that it takes one PhD
*  student, their entire PhD to do one protein. Uh, and with alpha fold two, we were able to predict
*  the 3d structure in a matter of seconds. Um, and so we were, you know, over Christmas,
*  we did the whole human proteome or every protein in the human body, all 20,000 proteins. So the
*  human proteome is like the equivalent of the human genome, but on protein space and, uh, and
*  sort of revolutionized really what, uh, uh, uh, structural biologists can do because now, um,
*  they don't have to worry about these painstaking experimentals, you know, should they put all of
*  that effort in or not, they can almost just look up the structure of their proteins, like a Google
*  search. And so there's a data set on which it's trained and how to map this amino acid sequence.
*  First of all, it's incredible that a protein, this little chemical computer is able to do that
*  computation itself in some kind of distributed way and do it very quickly. That's a weird thing. And
*  they evolve that way. Cause you know, in the beginning, I mean, that's a great invention,
*  just the protein itself. And then there's, I think probably a history of like, uh, they evolved,
*  to have many of these proteins and those proteins figure out how to be computers themselves in such
*  a way that you can create structures that can interact in complexes with each other in order
*  to form high level functions. I mean, it's a weird system that they figured it out.
*  Well, for sure. I mean, we, you know, maybe we should talk about the origins of life too,
*  but proteins themselves, I think are magical and incredible. As I said, little, little
*  bio nanomachines and, and, and actually let Leventhal, who is another scientist, a contemporary
*  of Amphicen, he coined this Leventhal, what became known as Leventhal's paradox, which is exactly
*  what you're saying. He calculated roughly a protein, an average protein, which is maybe 2000
*  amino acids, bases long is, is, is, can fold in maybe 10 to the power 300 different confirmations.
*  So there's 10 to the power 300 different ways that protein could fold up. And yet somehow in nature,
*  physics solves this, solves this in a matter of milliseconds. So proteins fold up in your body
*  in, you know, sometimes in fractions of a second. So physics is somehow solving that search problem.
*  And just to be clear, in many of these cases, maybe you can correct me if I'm wrong,
*  there's often a unique way for that sequence to form itself. So among that huge number of
*  possibilities, it figures out a way how to stably, in some cases there's might be a dysfunction,
*  so on, which leads to a lot of the disorders and stuff like that. But most of the time it's a
*  unique mapping and that unique mapping is not obvious. No, exactly. Which is what the problem is.
*  Exactly. So there's a unique mapping usually in a healthy, if it's healthy. And as you say,
*  in disease, so for example, Alzheimer's, one conjecture is that it's because of a misfolded
*  protein, a protein that folds in the wrong way, amyloid beta protein. So, and then because it
*  folds in the wrong way, it gets tangled up, right, in your, in your neurons. So it's super important
*  to understand both healthy functioning and also disease is to understand, you know, what these
*  things are doing and how they're structuring. Of course, the next step is sometimes proteins
*  change shape when they interact with something. So they're not just static necessarily in biology.
*  Maybe you can give some interesting, sort of beautiful things to you about these early days
*  of alpha fold, of solving this problem, because unlike games, this is real physical systems that
*  are less amenable to self play type of mechanisms. The size of the data set is smaller than you might
*  otherwise like. So you have to be very clever about certain things. Is there something you could speak
*  to? What was very hard to solve? And what are some beautiful aspects about the solution?
*  Yeah, I would say alpha fold is the most complex and also probably most meaningful system we've
*  built so far. So it's been amazing time actually in the last, you know, two, three years to see
*  that come through because as we talked about earlier, you know, games is what we started on
*  building things like AlphaGo and AlphaZero. But really, the ultimate goal was to not just to crack
*  games, it was just to build use them to bootstrap general learning systems, we could then apply to
*  real world challenges. Specifically, my passion is scientific challenges like protein folding.
*  And then alpha fold, of course, is our first big proof point of that. And so, you know, in terms
*  of the data, and the amount of innovations that had to go into it, we you know, it was like
*  more than 30 different component algorithms needed to be put together to crack the protein folding.
*  I think some of the big innovations were that kind of building in some hard coded constraints
*  around physics and evolutionary biology, to constrain sort of things like the bond angles
*  in the protein and things like that, but not to impact the learning system. So still allowing
*  the system to be able to learn the physics itself from the examples that we had. And the examples,
*  as you say, there are only about 150,000 proteins, even after 40 years of experimental biology,
*  only around 150,000 proteins have been the structures have been found out about. So that
*  was our training set, which is much less than normally we would like to use. But using various
*  tricks, things like self distillation, so actually using alpha fold predictions, some of the best
*  predictions that it thought was highly confident in, we put them back into the training set,
*  right to make the training set bigger. That was critical to alpha fold working. So there was
*  actually a huge number of different innovations like that that were required to ultimately crack
*  the problem. Alpha fold one, what it produced was a distogram. So a kind of a matrix of the pairwise
*  distances between all of the molecules in the protein. And then there had to be a separate
*  optimization process to create the 3D structure. And what we did for alpha fold two is make it
*  truly end to end. So we went straight from the amino acid sequence of bases to the 3D structure
*  directly without going through this intermediate step. And in machine learning, what we've always
*  found is that the more end to end you can make it, the better the system. And it's probably because
*  in the end, the system is better at learning what the constraints are than we are as the human
*  designers of specifying it. So anytime you can let it flow end to end and actually just generate
*  what it is you're really looking for, in this case, the 3D structure, you're better off than
*  having this intermediate step, which you then have to handcraft the next step for.
*  So it's better to let the gradients and the learning flow all the way through the system
*  from the end point, the end output you want to the inputs.
*  So that's a good way to start on a new problem, handcraft a bunch of stuff, add a bunch of manual
*  constraints with a small end to end learning piece or a small learning piece and grow that
*  learning piece until it consumes the whole thing. That's right. And so you can also see,
*  this is a bit of a method we've developed over doing many successful alpha, we call them alpha
*  X projects. And the easiest way to see that is the evolution of AlphaGo to AlphaZero. So AlphaGo
*  was a learning system, but it was specifically trained to only play Go. And what we wanted to
*  do with the first version of AlphaGo is just get to world champion performance no matter how we did
*  it. And then of course AlphaGo Zero, we remove the need to use human games as a starting point.
*  So it could just play against itself from random starting point from the beginning. So that removed
*  the need for human knowledge about Go. And then finally AlphaZero then generalized it so that any
*  things we had in there, the system, including things like symmetry of the Go board, were removed.
*  So the AlphaZero could play from scratch any two player game and then MuZero, which is the final,
*  our latest version of that set of things, was then extending it so that you didn't even have
*  to give it the rules of the game. It would learn that for itself. So it could also deal with computer
*  games as well as board games. So that line of AlphaGo, AlphaGo Zero, AlphaZero, MuZero,
*  that's the full trajectory of what you can take from imitation learning to full self
*  supervised learning. Yeah, exactly. And learning the entire structure of the environment you put in
*  from scratch, right? And bootstrapping it through self play yourself. But the thing is,
*  it would have been impossible, I think, or very hard for us to build AlphaZero or MuZero first
*  out of the box. Even psychologically, because you have to believe in yourself for a very long time.
*  You're constantly dealing with doubt because a lot of people say that it's impossible.
*  Exactly. So it was hard enough just to do Go. As you were saying, everyone thought that was
*  impossible, or at least a decade away from when we did it back in 2015, 2016. And so yes,
*  it would have been psychologically probably very difficult as well as the fact that of course,
*  we learn a lot by building AlphaGo first. I think this is why I call AI and engineering science.
*  It's one of the most fascinating science disciplines. But it's also an engineering
*  science in the sense that unlike natural sciences, the phenomenon you're studying
*  doesn't exist out in nature, you have to build it first. So you have to build the artifact first,
*  and then you can study how and pull it apart and how it works.
*  This is tough to ask you this question, because you probably will say it's everything. But
*  let's try to think through this, because you're in a very interesting position,
*  where DeepMind is a place of some of the most brilliant ideas in the history of AI. But it's
*  also a place of brilliant engineering. So how much of solving intelligence, this big goal
*  for DeepMind, how much of it is science? How much is engineering? So how much is the algorithms?
*  How much is the data? How much is the hardware compute infrastructure? How much is it the
*  software compute infrastructure? What else is there? How much is the human infrastructure?
*  And like just the humans interacting in certain kinds of ways, you know, all the space of all
*  those ideas, and how much is maybe like philosophy? How much, what's the key? If
*  you were to sort of look back, like if we go forward 200 years and look back, what was the key
*  thing that solved intelligence? Is it the ideas or the engineering?
*  I think it's a combination. First of all, of course, it's a combination of all those things,
*  but the ratios of them changed over time. So even in the last 12 years, so we started DeepMind in
*  2010, which is hard to imagine now because 2010, it's only 12 short years ago, but nobody was
*  talking about AI. I don't know if you remember back to your MIT days, you know, no one was talking
*  about it. I did a postdoc at MIT back around then, and it was sort of thought of as a, well, look,
*  we know AI doesn't work. We tried this hard in the 90s at places like MIT, mostly using logic systems
*  and old fashioned sort of good old fashioned AI, we would call it now. People like Minsky and
*  Patrick Winston, and you know all these characters, right? And I used to debate a few of them and they
*  used to think I was mad thinking about that some new advance could be done with learning systems.
*  And I was actually pleased to hear that because at least you know you're on a unique track at
*  that point, right? Even if all of your professors are telling you you're mad.
*  That's true.
*  And of course, in industry, we couldn't get, you know, it was difficult to get two cents together,
*  which is hard to imagine now as well, given that it's the biggest sort of buzzword in VCs and
*  fundraising's easy and all these kind of things today. So back in 2010, it was very difficult.
*  And the reason we started then and Shane and I used to discuss
*  what were the sort of founding tenets of DeepMind. And it was various things. One was algorithmic
*  advances. So deep learning, you know, Jeff Hinton and co had just sort of invented that in academia,
*  but no one in industry knew about it. We love reinforcement learning, we thought that could be
*  scaled up. But also understanding about the human brain had advanced quite a lot in the decade prior
*  with fMRI machines and other things. So we could get some good hints about architectures and
*  algorithms and sort of representations maybe that the brain uses. So at a systems level,
*  not at an implementation level. And then the other big things were compute and GPUs, right?
*  So we could see a compute was going to be really useful and it got to a place where it become
*  commoditized mostly through the games industry. And that could be taken advantage of. And then
*  the final thing was also mathematical and theoretical definitions of intelligence.
*  So things like AIXI, AIXI, which Shane worked on with his supervisor Marcus Hutter, which is
*  this sort of theoretical proof really of universal intelligence, which is actually a reinforcement
*  learning system in the limit. I mean, it seems infinite compute and infinite memory in the way,
*  you know, like a Turing machine proof. But I was also waiting to see something like that too,
*  like Turing machines and computation theory that people like Turing and Shannon came up with
*  underpins modern computer science. I was waiting for a theory like that to sort of underpin
*  AGI research. So when I met Shane and saw he was working on something like that,
*  that to me was a sort of final piece of the jigsaw. So in the early days, I would say that
*  ideas were the most important. For us, it was deep reinforcement learning, scaling up deep learning.
*  Of course, we've seen transformers. So huge leaps, I would say, three or four, if you think from 2010
*  till now, huge evolutions, things like AlphaGo. And maybe there's a few more still needed. But
*  as we get closer to AI, AGI, I think engineering becomes more and more important and data. Because
*  scale and of course, the recent results of GPT-3 and all the big language models and large models,
*  including our ones, has shown that scale and large models are clearly going to be a necessary,
*  but perhaps not sufficient, part of an AGI solution. And throughout that, like you said,
*  and I'd like to give you a big thank you. You're one of the pioneers in this, is sticking by ideas
*  like reinforcement learning, that this can actually work, given actually limited success in the past.
*  And also, which we still don't know, but proudly having the best researchers in the world and
*  talking about solving intelligence. So talking about whatever you call it, AGI or something like
*  this. That's speaking of MIT, that's just something you wouldn't bring up. Not maybe you did in like
*  40, 50 years ago. But that was, AI was a place where you do tinkering, very small scale,
*  not very ambitious projects. And maybe the biggest ambitious projects were in the space of robotics
*  and doing like the DARPA challenge. But the task of solving intelligence and believing you can,
*  that's really, really powerful. So in order for engineering to do its work, to have great
*  engineers build great systems, you have to have that belief, that threads throughout the whole
*  thing that you can actually solve some of these impossible challenges. Yeah, that's right. And
*  back in 2010, our mission statement, and still is today, it used to be, solving step one,
*  solve intelligence. Step two, use it to solve everything else. So if you can imagine pitching
*  that to a VC in 2010, the kind of looks we got, we managed to find a few kooky people to back us,
*  but it was tricky. And it got to the point where we wouldn't mention it to any of our professors,
*  because they would just eye roll and think we committed career suicide. And so there's a lot
*  of things that we had to do. But we always believed it. And one reason, by the way, one reason I've
*  always believed in reinforcement learning is that if you look at neuroscience, that is the way that
*  the primate brain learns. One of the main mechanisms is the dopamine system implements some form of
*  TD learning as very famous result in the late 90s, where they saw this in monkeys, and as a
*  propagating prediction error. So again, in the limit, this is what I think you can use neuroscience
*  for is, in any mathematics, when you're doing something as ambitious as trying to solve
*  intelligence, and it's blue sky research, no one knows how to do it, you need to use any evidence
*  or any source of information you can to help guide you in the right direction or give you confidence
*  you're going in the right direction. So that was one reason we pushed so hard on that. And just
*  going back to your earlier question about organization, the other big thing that I think
*  we innovated with at DeepMind to encourage invention and innovation was the multidisciplinary
*  organization we built, and we still have today. So DeepMind originally was a confluence of the
*  most cutting edge knowledge in neuroscience with machine learning, engineering and mathematics,
*  and gaming. And then since then, we've built that out even further. So we have philosophers here
*  by ethicists, but also other types of scientists, physicists, and so on.
*  And that's what brings together, I tried to build a new type of Bell Labs, but in its golden era,
*  and a new expression of that to try and foster this incredible innovation machine. So talking
*  about the humans in the machine, DeepMind itself is a learning machine with a lot of amazing human
*  minds in it, coming together to try and build these learning systems. If we return to the big,
*  ambitious dream of AlphaFold, that may be the early steps on a very long journey in biology,
*  do you think the same kind of approach can use to predict the structure and function of more
*  complex biological systems? So multi-protein interaction, and then you can go out from there,
*  just simulating bigger and bigger systems that eventually simulate something like the human brain
*  or the human body, just the big mush, the mess of the beautiful, resilient mess of biology. Do you
*  see that as a long-term vision? I do. And I think if you think about what are the things, top things
*  I wanted to apply AI to once we had powerful enough systems, biology and curing diseases
*  and understanding biology was right up there, top of my list. That's one of the reasons I
*  personally pushed that myself and with AlphaFold. But I think AlphaFold, amazing as it is, is just
*  the beginning. And I hope it's evidence of what could be done with computational methods.
*  So AlphaFold solved this huge problem of the structure of proteins, but biology is dynamic.
*  So really, what I imagine from here, and we're working on all these things now,
*  is protein-protein interaction, protein-lickon binding, so reacting with molecules. Then you
*  want to build up to pathways and then eventually a virtual cell. That's my dream, maybe in the next
*  10 years. And I've been talking actually to a lot of biologists, friends of mine, Paul Nurse, who
*  runs the Crick Institute, amazing biologist, Nobel Prize winning biologist. We've been discussing
*  for 20 years now virtual cells. Could you build a virtual simulation of a cell? And if you could,
*  that would be incredible for biology and disease discovery because you could do loads of experiments
*  on the virtual cell and then only at the last stage validate it in the wet lab. So in terms of
*  the search space of discovering new drugs, it takes 10 years roughly to go from identifying a target
*  to having a drug candidate. Maybe that could be shortened by an order of magnitude if you could do
*  most of that work in silico. So in order to get to a virtual cell, we have to build up understanding
*  of different parts of biology and the interactions. So every few years I talked about this with Paul,
*  and then finally last year after AlphaFold, I said, now's the time we can finally go for it.
*  AlphaFold is the first proof point that this might be possible. He's very excited. We have
*  some collaborations with his lab. They're just across the road actually from us. It's a wonderful
*  being here in King's Cross with the Crick Institute across the road. I think the next steps,
*  I think there's going to be some amazing advances in biology built on top of things like AlphaFold.
*  We're already seeing that with the community doing that after we've open sourced it and released it.
*  I often say that if you think of mathematics as the perfect description language for physics,
*  I think AI might end up being the perfect description language for biology because
*  biology is so messy. It's so emergent, so dynamic and complex. I find it very hard to believe we'll
*  ever get to something as elegant as Newton's laws of motions to describe a cell. It's just
*  too complicated. I think AI is the right tool for this. You have to start with the basic building
*  blocks and use AI to run the simulation for all those building blocks. Have a very strong way to
*  do prediction of what, given these building blocks, how the function and the evolution of
*  that biological system. It's almost like a cellular automata. You have to run it. You can't analyze
*  it from a high level. You have to take the basic ingredients, figure out the rules and let it run
*  but in this case, the rules are very difficult to figure out. You have to learn them.
*  That's exactly it. The biology is too complicated to figure out the rules. It's too emergent,
*  too dynamic compared to a physics system like the motion of a planet. You have to learn the rules
*  and that's exactly the type of systems that we're building. You mentioned you've open sourced
*  AlphaFold and even the data involved. To me personally, also really happy and a big thank
*  you for open sourcing Majoco, the physics simulation engine that's often used for robotics research
*  and so on. I think that's a pretty gangster move. Very few companies or people would do that kind
*  of thing. What's the philosophy behind that? It's a case by case basis and in both those cases,
*  we felt that was the maximum benefit to humanity to do that and the scientific community. In one
*  case, the robotics physics community with Majoco. We purchased it. We purchased it for the express
*  principle to open source it. I hope people appreciate that. It's great to hear that you do.
*  The second thing was and mostly we did it because the person building it was not able to cope with
*  supporting it anymore because it got too big for him. He's an amazing professor who built it in the
*  first place. We helped him out with that. Then with AlphaFold is even bigger, I would say. I
*  think in that case, we decided that there were so many downstream applications of AlphaFold
*  that we couldn't possibly even imagine what they all were. The best way to accelerate
*  drug discovery and also fundamental research would be to give all that data away and the system
*  itself. It's been so gratifying to see what people have done that within just one year,
*  which is a short amount of time in science. It's been used by over 500,000 researchers have used
*  it. We think that's almost every biologist in the world. I think there's roughly 500,000 biologists
*  in the world, professional biologists, have used it to look at their proteins of interest.
*  We've seen amazing fundamental research done. A couple of weeks ago, there was a whole special
*  issue of science, including the front cover, which had the nuclear pore complex on it,
*  which is one of the biggest proteins in the body. The nuclear pore complex is a protein that governs
*  all the nutrients going in and out of your cell nucleus. They're like little gateways that open
*  and close to let things go in and out of your cell nucleus. They're really important,
*  but they're huge because they're massive doughnut ring-shaped things. They've been looking to try
*  and figure out that structure for decades. They have lots of experimental data, but it's too low
*  resolution. There's bits missing. They were able to, like a giant Lego jigsaw puzzle, use AlphaFold
*  predictions plus experimental data and combined those two independent sources of information,
*  actually four different groups around the world were able to put it together more or less
*  simultaneously using AlphaFold predictions. That's been amazing to see. Pretty much every
*  pharma company, every drug company, executive I've spoken to has said that their teams are using
*  AlphaFold to accelerate whatever drugs they're trying to discover. I think the knock-on effect
*  has been enormous in terms of the impact that AlphaFold has made.
*  It's probably bringing in, it's creating biologists. It's bringing more people into
*  the field, both on the excitement and both on the technical skills involved. It's almost like a
*  gateway drug to biology. Yes, it is. You follow a lot of-
*  Computational people involved too, hopefully. I think for us, the next stage, as I said,
*  in future we have to have other considerations too. We're building on top of AlphaFold and these
*  other ideas I discussed with you about protein-protein interactions and genomics and other things.
*  Not everything will be open source. Some of it we'll do commercially because that will be the
*  best way to actually get the most resources and impact behind it. In other ways, some other
*  projects we'll do non-profit style. Also, we have to consider for future things as well,
*  safety and ethics as well. Synthetic biology, there is dual use and we have to think about
*  that as well. With AlphaFold, we consulted with 30 different bioethicists and other people expert
*  in this field to make sure it was safe before we released it. There'll be other considerations
*  in future, but for right now, I think AlphaFold is a gift from us to the scientific community.
*  I'm pretty sure that something like AlphaFold will be part of Nobel prizes in the future,
*  but us humans, of course, are horrible with credit assignment, so we'll, of course,
*  give it to the humans. Do you think there will be a day when AI system can't be denied that it earned
*  that Nobel Prize? Do you think we will see that in the 21st century? It depends what type of AI
*  we end up building, whether they're goal-seeking agents who specify the goals, who comes up with
*  the hypotheses, who determines which problems to tackle. And tweets about it, announcements.
*  Yes, it's announcements about results exactly as part of it. I think right now, of course,
*  it's amazing human ingenuity that's behind these systems and then the system, in my opinion,
*  is just a tool. It would be a bit like saying with Galileo and his telescope, the ingenuity,
*  the credit should go to the telescope. It's clearly Galileo building the tool which he then uses.
*  I still see that in the same way today, even though these tools learn for themselves.
*  I think of things like AlphaFold and the things we're building as the ultimate tools for science
*  and for acquiring new knowledge to help us as scientists acquire new knowledge.
*  I think one day, there will come a point where an AI system may solve or come up with something
*  like general relativity of its own bat, not just by averaging everything on the internet or averaging
*  everything on PubMed, although that would be interesting to see what that would come up with.
*  That, to me, is a bit like our earlier debate about creativity, inventing Go
*  rather than just coming up with a good Go move. I think if we wanted to give it the credit of
*  like a Nobel type of thing, then it would need to invent Go and sort of invent that new conjecture
*  out of the blue rather than being specified by the human scientists or the human creators.
*  I think right now, it's definitely just a tool. Although it is interesting how far you get by
*  averaging everything on the internet, like you said, because a lot of people do see science
*  you're always standing on the shoulders of giants. The question is, how much are you really reaching
*  up above the shoulders of giants? Maybe it's just assimilating different kinds of results of the
*  past with ultimately this new perspective that gives you this breakthrough idea. But that idea
*  may not be novel in the way that it can't be already discovered on the internet. Maybe the
*  Nobel prizes of the next hundred years are already all there on the internet to be discovered.
*  Jason Suellentrop They could be. I think this is one of the big mysteries. First of all,
*  I believe a lot of the big new breakthroughs that are going to come in the next few decades,
*  and even in the last decade, are going to come at the intersection between different subject areas
*  where there'll be some new connection that's found between what seemingly were disparate areas.
*  One can even think of DeepMind, as I said earlier, as a sort of interdisciplinary between
*  neuroscience ideas and AI engineering ideas originally. I think there's that. Then one of
*  the things we can't imagine today is, and one of the reasons I think people, we were so surprised
*  by how well large models worked, is that actually it's very hard for our limited human minds to
*  understand what it would be like to read the whole internet. I think we can do a thought experiment,
*  and I used to do this, of, well, what if I read the whole of Wikipedia? What would I know? I think
*  our minds can just about comprehend maybe what that would be like, but the whole internet is
*  beyond comprehension. I think we just don't understand what it would be like to be able to
*  hold all of that in mind potentially, and then active at once, and then maybe what are the
*  connections that are available there. I think no doubt there are huge things to be discovered
*  just like that, but I do think there is this other type of creativity, of true spark, of
*  new knowledge, new idea, never thought before about, can't be averaged from things that are known,
*  that really, of course, everything comes, nobody creates in a vacuum, so there must be clues
*  somewhere, but just a unique way of putting those things together. I think some of the
*  greatest scientists in history have displayed that, I would say, although it's very hard to know,
*  going back to their time, what was exactly known when they came up with those things.
*  Although, you're making me really think because just the thought experiment of deeply knowing
*  a hundred Wikipedia pages, I don't think I can, I've been really impressed by Wikipedia
*  for technical topics, so if you know a hundred pages or a thousand pages, I don't think we can
*  truly comprehend what kind of intelligence that is. It's a pretty powerful intelligence. If you
*  know how to use that and integrate that information correctly, I think you can go really far. You can
*  probably construct thought experiments based on that, like simulate different ideas. So if this
*  is true, let me run this thought experiment, then maybe this is true. It's not really invention,
*  it's like just taking literally the knowledge and using it to construct a very basic simulation of
*  the world. I mean, some argue it's romantic in part, but Einstein would do the same kind of things
*  with a thought experiment. Yeah, you one could imagine doing that systematically across millions
*  of Wikipedia pages plus PubMed, all these things. I think there are many, many things to be discovered
*  like that that are hugely useful. You could imagine, and I want us to do some of these things in
*  material science, like room temperature superconductors is something on my list one day,
*  I'd like to have an AI system to help build better optimized batteries, all of these sort
*  of mechanical things. I think a systematic sort of search could be guided by a model,
*  could be extremely powerful. So speaking of which, you have a paper on nuclear fusion,
*  magnetic control of talk about plasmus to deep reinforcement learning. So you're seeking to solve
*  nuclear fusion with deep RL. So it's doing control of high temperature plasmus. Can you explain this
*  work? And can AI eventually solve nuclear fusion? It's been very fun last year or two, very
*  productive, because we've been taking off a lot of my dream projects, if you like, of things that
*  I've collected over the years of areas of science that I would like to, I think could be very
*  transformative if we helped accelerate, and really interesting problems, scientific challenges in of
*  themselves. This is energy. So energy, yes, exactly. So energy and climate. So we talked about
*  disease and biology as being one of the biggest places I think AI can help with. I think energy
*  and climate is another one. So maybe they would be my top two. And fusion is one area I think AI
*  can help with. Now, fusion has many challenges, mostly physics, material science and engineering
*  challenges as well to build these massive fusion reactors and contain the plasma. And what we try
*  to do and whenever we go into a new field, to apply our systems is we look for, we talk to domain
*  experts, we try and find the best people in the world to collaborate with. In this case, in fusion,
*  we collaborated with EPFL in Switzerland, the Swiss Technical Institute, who are amazing. They have a
*  test reactor, they were willing to let us use which, you know, I double checked with the team,
*  we were going to use carefully and safely. I was impressed they managed to persuade them to let us
*  use it. And it's an amazing test reactor they have there. And they try all sorts of pretty crazy
*  experiments on it. And what we tend to look at is if we go into a new domain like fusion,
*  what are all the bottleneck problems? Like thinking from first principles, you know,
*  what are all the bottleneck problems that are still stopping fusion working today?
*  And then we look at, you know, we get a fusion expert to tell us, and then we look at those
*  bottlenecks, and we look at the ones which ones are amenable to our AI methods today.
*  And then and would be interesting from a research perspective from our point of view,
*  from an AI point of view, and that would address one of their bottlenecks. And in this case,
*  plasma control was perfect. So, you know, the plasma, it's a million degrees Celsius,
*  something like that's hotter than the sun. And there's obviously no material that can contain
*  it. So they have to be containing these magnetic, very powerful, superconducting magnetic fields.
*  But the problem is plasma is pretty unstable, as you imagine, you're kind of holding a mini sun,
*  mini star in a reactor. So you know, you kind of want to predict ahead of time,
*  what the plasma is going to do. So you can move the magnetic field within a few milliseconds,
*  you know, to basically contain what it's going to do next. So it seems like a perfect problem,
*  if you think of it for like a reinforcement learning prediction problem. So, you know,
*  you got controller, you're going to move the magnetic field. And until we came along, you
*  know, they were they were doing with with traditional operational research type of
*  controllers, which are kind of handcrafted. And the problem is, of course, they can't react in
*  the moment to something the plasma is doing that they have to be hard coded. And again,
*  knowing that that's normally our go to solution is we would like to learn that instead. And they
*  also had a simulator of these plasma. So there were lots of criteria that matched what we like to use.
*  So can AI eventually solve nuclear fusion? Well, so we with this problem, and we published it in
*  Nature paper last year, we held the fusion that we held the plasma in a specific shapes. So actually,
*  it's almost like carving the plasma into different shapes and control and hold it there for a record
*  amount of time. So so that's one of the problems of fusion sort of solved. So have a controller
*  that's able to no matter the shape, contain it, contain it and hold it in structure. And there's
*  different shapes that are better for for the energy productions called droplets and, and so on. So
*  so that was huge. And now we're looking, we're talking to lots of fusion startups to see
*  what's the next problem we can tackle in the fusion area.
*  So another fascinating place in a paper title, pushing the frontiers of density functionals by
*  solving the fractional electron problem. So you're taking on modeling and simulating the
*  quantum mechanical behavior of electrons. Yes. Can you explain this work? And can AI
*  model and simulate arbitrary quantum mechanical systems in the future?
*  Yeah, so this is another problem I've had my eye on for, you know,
*  decade or more, which is sort of simulating the properties of electrons, if you can do that,
*  you can basically describe how elements and materials and substances work. So it's kind of
*  like fundamental if you want to advance material science. And, you know, we have Schrodinger's
*  equation, and then we have approximations to that density functional theory, these things are, you
*  know, are famous. And people try and write approximations to these, to these functionals,
*  and, and kind of come up with descriptions of the electron clouds, where they're going to go, how
*  they're going to interact when you put two elements together. And what we try to do is learn a
*  simulation, learn a functional that will describe more chemistry types of chemistry. So until now,
*  you know, you can run expensive simulations, but then you can only simulate very small
*  molecules, very simple molecules, we would like to simulate large materials. And so today, there's
*  no way of doing that. And we're building up towards building functionals that approximate Schrodinger's
*  equation, and then allow you to describe what the electrons are doing. And all material sort of
*  science and material properties are governed by the electrons and how they interact.
*  So have a good summarization of the simulation through the functional. But one that is still
*  close to what the actual simulation would come out with. So what, how difficult is that task?
*  What's involved in that task? Is it running those, those complicated simulations, and learning the
*  task of mapping from the initial conditions and the parameters of the simulation, learning what
*  the functional would be? Yeah. So it's pretty tricky. And we've done it with, you know, the
*  nice thing is we there are we can run a lot of the simulations that the molecular dynamic simulations
*  on our compute clusters. And so that generates a lot of data. So in this case, the data is generated.
*  So we like that sort of systems. And that's why we use games, it's simulated generated data.
*  And we can kind of create as much of it as we want, really. And just let's leave some, you know,
*  if any computers are free in the cloud, we just run we run some of these calculations, right?
*  Compute cluster calculation. I like how the free compute time is used up on quantum mechanics.
*  Yeah, quantum mechanics. Exactly simulations and protein simulations and other things.
*  And so and so you know, when you're not searching on YouTube for video cat videos,
*  we're using those computers usefully and quantum chemistry. The idea by and putting them to good
*  use. And then yeah, and then all of that computational data that's generated, we can then try and learn the
*  functionals from that, which of course, are way more efficient. Once we learn the functional,
*  then running those simulations would be. Do you think one day AI may allow us to do something
*  like basically crack open physics, so do something like travel faster than the speed of light?
*  My ultimate aim has always been with AI is the reason I am personally working on AI for my whole
*  life is to build a tool to help us understand the universe. So I wanted to
*  and that means physics really, and the nature of reality. So I don't think we have systems that
*  are capable of doing that yet. But when we get towards a GI, I think that's one of the first
*  things I think we should apply a GI to. I would like to test the limits of physics and our knowledge
*  of physics. There's so many things we don't know. This is one thing I find fascinating about science
*  and, you know, as a huge proponent of the scientific method as being one of the greatest ideas humanity
*  has ever had and allowed us to progress with our knowledge. I think as a true scientist,
*  I think what you find is the more you find out, the more you realize we don't know.
*  And I always think that it's surprising that more people aren't troubled. You know, every night I
*  think about all these things we interact with all the time that we have no idea how they work.
*  Time, consciousness, gravity, life. We can't, I mean, these are all the fundamental things of nature.
*  I think the way we don't really know what they are.
*  To live life, we pin certain assumptions on them and kind of treat our assumptions as if they're
*  fact. That allows us to sort of box them off somehow. Yeah, box them off somehow.
*  But the reality is when you think of time, you should remind yourself, you should put it off,
*  take it off the shelf and realize like, no, we have a bunch of assumptions. There's still a lot of,
*  there's even not a lot of debate. There's a lot of uncertainty about exactly what is time.
*  Is there an era of time? You know, there's a lot of fundamental questions that you can't just make
*  assumptions about and maybe AI allows you to not put anything on the shelf. Yeah. Not make any
*  hard assumptions and really open it up and see what exactly I think we should be truly open minded
*  about that. And exactly that not be dogmatic to a particular theory. It'll also allow us to build
*  better tools, experimental tools eventually, that can then test certain theories that may not be
*  testable today about things about like, what we spoke about at the beginning about the computational
*  and nature of the universe, how one might, if that was true, how one might go about testing that,
*  right? And, and how much, you know, there are people who've conjectured people like Scott
*  Aronson and others about, you know, how much information can a specific plank unit of space
*  and time contain, right? So one might be able to think about testing those ideas if you had
*  AI helping you build some new exquisite experimental tools. This is what I imagine,
*  you know, many decades from now we'll be able to do. And what kind of questions can be answered
*  through running a simulation of them? So there's a bunch of physics simulations, you can imagine,
*  that could be run in some kind of efficient way, much like you're doing in the quantum simulation
*  work. And perhaps even the origin of life, figuring out how going even back before the work of
*  AlphaFold begins of how this whole thing emerges from a rock. Yes. From a static thing. What do
*  you think AI will allow us to, is that something you have your eye on? It's trying to understand
*  the origin of life. First of all, yourself, what do you think? How the heck did life originate
*  on earth? Yeah, well, maybe we'll come to that in a second. But I think the ultimate use of AI is to
*  kind of use it to accelerate science to the maximum. So I think of it a little bit like
*  the tree of all knowledge. If you imagine that's all the knowledge there is in the universe to
*  attain. And we sort of barely scratched the surface of that so far. And even though, you know, we've
*  done pretty well since the Enlightenment, right, as humanity. And I think AI will turbocharge all
*  of that, like we've seen with AlphaFold. And I want to explore as much of that tree of knowledge
*  as is possible to do. And I think that involves AI helping us with understanding or finding patterns,
*  but also potentially designing and building new tools, experimental tools. So I think that's all,
*  and also running simulations and learning simulations, all of that, we're already,
*  we're sort of doing it at a baby steps level here. But I can imagine that in the decades to come,
*  as, you know, what's the full flourishing of that line of thinking, it's going to be truly incredible,
*  I would say. If I visualize this tree of knowledge, something tells me that that knowledge,
*  tree of knowledge for humans is much smaller. In the set of all possible trees of knowledge,
*  it's actually quite small, given our cognitive limitations, limited cognitive capabilities,
*  that even with the tools we build, we still won't be able to understand a lot of things.
*  And that's perhaps what non-human systems might be able to reach farther, not just as tools,
*  but in themselves understanding something that they can bring back.
*  Yeah, it could well be. So I mean, there's so many things that are sort of encapsulated
*  what you just said there. I think first of all, there's two different things. There's like,
*  what do we understand today? What could the human mind understand? And what is the totality of what
*  is there to be understood? Right? And so there's three concentric, you know, you can think of them
*  as three larger and larger trees or exploring more branches of that tree. And I think with AI,
*  we're going to explore that whole lot. Now, the question is, is, you know, if you think about
*  what is the totality of what could be understood, there may be some fundamental physics reasons why
*  certain things can't be understood, like what's outside a simulation or outside the universe,
*  maybe it's not understandable from within the universe. So there may be some hard constraints
*  like that, you know, could be smaller constraints, like we think of space time is fundamental for
*  us, our human brains are really used to this idea of a three dimensional world with time,
*  maybe, but our tools could go beyond that. They wouldn't have that limitation necessarily. They
*  could think in 11 dimensions, 12 dimensions, whatever is needed. But we could still maybe
*  understand that in several different ways. The example I always give is when I, you know,
*  play Gary Cuspar at Speed Chess, or we've talked about chess and these kinds of things, you know,
*  if you're reasonably good at chess, you can't come up with the move Gary comes up with in his move,
*  but he can explain it to you. And you can understand post hoc the reasoning. So I think
*  there's an even further level of like, well, maybe you couldn't have invented that thing.
*  But going back to using language again, perhaps you can understand and appreciate that same way
*  that you can appreciate, you know, Vivaldi or Mozart or something without, you can appreciate
*  the beauty of that without being able to construct it yourself, right, invent the music yourself.
*  So I think we see this in all forms of life. So it'll be that times, you know, a million,
*  but it would you can imagine also one sign of intelligence is the ability to explain things
*  clearly and simply, right? You know, people like Richard Fierman, another one of my all time heroes
*  used to say that, right? If you can't, you know, if you can explain it something simply, then you
*  that's a that's the best sign, a complex topic simply, then that's one of the best signs of
*  you understanding it. Yeah, so I can see myself talking trash in the AI system in that way.
*  Yes.
*  It gets frustrated how dumb I am and trying to explain something to me. I was like, well,
*  that means you're not intelligent, because if you were intelligent, you'd be able to explain it
*  simply. Yeah, of course, you know, there's also the other option, of course, we could enhance
*  ourselves and without devices, we are already sort of symbiotic with our compute devices,
*  right with our phones and other things. And, you know, there's stuff like neural link and
*  accepture that could be could could advance that further. So I think there's lots of lots of really
*  amazing possibilities that I could foresee from here. Well, let me ask you some wild questions.
*  So out there looking for friends, do you think there's a lot of alien civilizations out there?
*  So I guess this also goes back to your origin of life question, too, because I think that that's
*  key. My personal opinion looking at all this and, you know, it's one of my hobbies physics, I guess.
*  So I you know, it's something I think about a lot and talk to a lot of experts on and read a lot of
*  books on. And I think my feeling currently is that that we are alone. I think that's the most
*  likely scenario given what what evidence we have. So and the reasoning is, I think that,
*  you know, we've tried since things like SETI program, and I guess since the dawning of the
*  space age, we've, you know, had telescopes, open radio telescopes and other things. And if you think
*  about and try to detect signals. Now, if you think about the evolution of humans on Earth,
*  we could have easily been a million years ahead of our time now or million years behind, right,
*  easily with just some slightly different quirk thing happening hundreds of thousands years ago.
*  You know, things could have been slightly different if the meteor would hit the dinosaurs a
*  million years earlier, maybe things would have evolved. We'd be a million years ahead of where
*  we are now. So what that means is if you imagine where humanity will be in a few hundred years,
*  let alone a million years, especially if we hopefully, you know, solve things like climate
*  change and other things, and we continue to flourish, and we build things like AI, and we
*  do space traveling, and all of the stuff that that humans have dreamed of forever, right,
*  and sci fi has talked about forever. We will be spreading across the stars, right. And Voyn Neumann
*  famously calculated, you know, it would only take about a million years if you send out
*  von Neumann probes to the nearest, you know, the nearest other solar systems. And then they built,
*  all they did was build two more versions of themselves and set those two out to the next
*  nearest systems. You know, within a million years, I think you would have one of these
*  probes in every system in the galaxy. So it's not actually in cosmological time, that's actually a
*  very short amount of time. So and you know, we've people like Dyson have thought about constructing
*  Dyson spheres around stars to collect all the energy coming out of the star, you know, that
*  there would be constructions like that would be visible across space, probably even across a galaxy.
*  So and then, you know, if you think about all of our radio, television,
*  emissions that have gone out since since the, you know, 30s and 40s, imagine a million years of that,
*  and now hundreds of civilizations doing that. When we opened our ears, at the point we got
*  technologically sophisticated enough in the space age, we should have heard a cacophony of voices,
*  should have joined that cacophony of voices. And what we did, we open our ears, and we heard nothing.
*  And many people who argue that there are aliens would say, well, we haven't really done
*  exhaustive search yet. And maybe we're looking in the wrong bands, and, and we've got the wrong
*  devices. And we wouldn't notice what an alien form was like to be so different to what we're used to.
*  But you know, I know, I don't really buy that, that it shouldn't be as difficult as that. Like,
*  I think we've searched enough. There should be everywhere. If it was, it should be everywhere.
*  We should see Dyson spheres being put up, sun's blinking in and out, you know, there should be a
*  lot of evidence for those things. And then there are other people argue, well, the sort of Safari
*  view of like, well, we're a primitive species still, because we're not space faring yet. And,
*  and we're, you know, there's some kind of global, like universal rule not to interfere,
*  Star Trek rule. But like, look, look, we can't even coordinate humans to deal with climate change.
*  And we're one species. What is the chance that of all of these different human civilization,
*  you know, alien civilizations, they would have the same priorities and, and agree across, you know,
*  these kind of matters. And even if that was true, and we were in some sort of Safari for our own
*  good, to me, that's not much different from the simulation hypothesis. Because what does it mean,
*  the simulation hypothesis, I think in its most fundamental level, it means what we're seeing
*  is not quite reality, right? It's something there's something more deeper underlying it,
*  maybe computational. Now, if we were in a, if we were in a sort of Safari Park,
*  and everything we were seeing was a hologram, and it was projected by the aliens or whatever,
*  that to me is not much different than thinking we're inside of another universe, because we
*  still can't see true reality. Right? I mean, there's there's other explanations, it could be that
*  the way they're communicating is just fundamentally different, that we're too dumb to understand
*  the much better methods of communication they have. It could be I mean, it's silly to say, but
*  our own thoughts could be the methods by which they're communicating, like, the place from which
*  our ideas writers talk about this, like the muse, yeah, the, it sounds like very kind of wild, but
*  it could be thoughts, it could be some interactions with our mind that we think are originating from
*  us is actually something that is coming from other life forms elsewhere, consciousness itself
*  might be that it could be but I can't see any sensible argument to the why why would all of
*  the alien species be in this way, yeah, some of them will be more primitive, they will be close
*  to our level, you know, they would, they should be a whole sort of distribution of these things,
*  right? Some would be aggressive, some would be, you know, curious, others would be very
*  historical and philosophical, because, you know, maybe they're a million years older than us,
*  but it's not, it shouldn't be like what I mean, one, one alien civilization might be like that,
*  communicating thoughts and others, but I don't see why, you know, potentially the hundreds there
*  should be would be uniform in this way, right? It could be a violent dictatorship that the people,
*  the alien civilizations that become successful, become,
*  um, gain the ability to be destructive, an order of magnitude more destructive,
*  but of course, the sad thought, well, either humans are very special, we took a lot of
*  leaps that arrived at what it means to be human, there's a question there, which was the hardest,
*  which was the most special, but also if others have reached this level, and maybe many others
*  have reached this level, the great filter that prevented them from going farther to becoming a
*  multi-planetary species are reaching out into the stars, and those are really important questions
*  for us, whether there's other alien civilizations out there or not, this is very useful for us to
*  think about, if we destroy ourselves, how will we do it, and how easy is it to do?
*  Yeah, well, you know, these are big questions, and I've thought about these a lot, but the
*  interesting thing is that if we're alone, that's somewhat comforting from the great filter
*  perspective, because it probably means the great filters are past us, and I'm pretty sure they are,
*  so going back to your origin of life question, there are some incredible things that no one
*  knows how happened, like obviously the first life form from chemical soup, that seems pretty hard,
*  but I would guess the multi-cellular, I wouldn't be that surprised if we saw single cell life
*  forms elsewhere, bacteria type things, but multi-cellular life seems incredibly hard,
*  that step of capturing mitochondria and then using that as part of yourself when you've just eaten it.
*  Would you say that's the biggest, the most, like if you had to choose one, sort of Hitchhiker's Galaxy,
*  one sentence summary of like, oh, those clever creatures did this, there would be the multi-cellular.
*  I think that's probably the one that's the biggest, I mean, there's a great book called
*  The Ten Great Inventions of Evolution by Nick Lane, and he speculates on 10 of these, you know,
*  what could be great filters. I think that's one, I think the advent of intelligence and conscious
*  intelligence and in order, you know, to us to be able to do science and things like that is huge
*  as well. I mean, it's only evolved once as far as, you know, in earth history, so that would be a
*  later candidate, but there's certainly for the early candidates, I think multi-cellular life forms
*  is huge. By the way, what it's interesting to ask you if you can hypothesize about what is the origin
*  of intelligence? Is it that we started cooking meat over fire? Is it that we somehow figured out
*  that we could be very powerful when we started collaborating? So cooperation between our ancestors
*  so that we can overthrow the alpha male? What is it, Richard? I talked to Richard Randham,
*  who thinks we're all just beta males who figured out how to collaborate to defeat the dictator,
*  the authoritarian alpha male that controlled the tribe. Is there other explanation? Was there
*  2001 Space Odyssey type of monolith that came down to earth?
*  Well, I think all of those things you suggested are good candidates, fire and cooking, right? So
*  that's clearly important for energy efficiency, cooking our meat and then being able to
*  be more efficient about eating it and consuming the energy. I think that's huge and then utilizing
*  fire and tools. I think you're right about the tribal cooperation aspects and probably language
*  as part of that because probably that's what allowed us to outcompete Neanderthals and perhaps
*  less cooperative species. So that may be the case. Tool making, spears, axes, I think it's pretty
*  clear now that humans were responsible for a lot of the extinctions of megafauna, especially in the
*  Americas when humans arrived. So you can imagine once you discover tool usage, how powerful that
*  would have been and how scary for animals. So I think all of those could have been explanations
*  for it. The interesting thing is that it's a bit like general intelligence too, is it's very costly
*  to begin with to have a brain and especially a general purpose brain rather than a special
*  purpose one because the amount of energy our brains use, I think it's like 20% of the body's
*  energy and it's massive. And when you're thinking chess, one of the funny things that we used to
*  say is it's as much as a racing driver uses for a whole Formula One race. Just playing a game of
*  serious high level chess, which you wouldn't think just sitting there because the brain's using so
*  much energy. So in order for an animal, an organism to justify that, there has to be a huge payoff.
*  And the problem with half a brain or half intelligence, say an IQs of like a monkey brain,
*  it's not clear you can justify that evolutionary until you get to the human level brain.
*  And so how do you do that jump? It's very difficult, which is why I think it's only
*  been done once from the sort of specialized brains that you see in animals to this sort of general
*  purpose, truing powerful brains that humans have, which allows us to invent the modern world.
*  And it takes a lot to cross that barrier. And I think we've seen the same with AI systems,
*  which is that maybe until very recently, it's always been easier to craft a specific solution
*  to a problem like chess, then it has been to build a general learning system that could
*  potentially do many things. Because initially, that system will be way worse than less efficient
*  than the specialized system. So one of the interesting quirks of the human mind of this
*  evolved system is that it appears to be conscious. This thing that we don't quite understand, but it
*  seems very, very special, its ability to have a subjective experience that it feels like something
*  to eat a cookie, the deliciousness of it or see a color and that kind of stuff. Do you think in
*  order to solve intelligence, we also need to solve consciousness along the way? Do you think
*  AGI systems need to have consciousness in order to be truly intelligent? Yeah, we thought about
*  this a lot, actually. And I think that my guess is that consciousness and intelligence are double
*  dissociable. So you can have one without the other both ways. And I think you can see that with
*  consciousness in that, I think some animals, pets, if you have a pet dog or something like that,
*  you can see some of the higher animals and dolphins, things like that, have self-awareness
*  and are very sociable, seem to dream. A lot of the traits one would regard as being conscious
*  and self-aware. But yet they're not that smart. So they're not that intelligent by say IQ standards
*  or something like that. Yeah, it's also possible that our understanding of intelligence is flawed,
*  like putting an IQ to it. Maybe the thing that a dog can do is actually gone very far along the
*  path of intelligence and we humans are just able to play chess and maybe write poems. Right, but
*  if we go back to the idea of AGI and general intelligence, dogs are very specialized, right?
*  Most animals are pretty specialized. They can be amazing at what they do, but they're like kind of
*  elite sports people or something, right? So they do one thing extremely well because their entire
*  brain is optimized. They have somehow convinced the entirety of the human population to feed them
*  and service them. So in some way, they're controlling. Yes, exactly. Well, we co-evolved
*  to some crazy degree, right? Including the way the dogs even wag their tails and twitch their noses,
*  right? We find inexorably cute. But I think you can also see intelligence on the other side. So
*  systems like artificial systems that are amazingly smart at certain things like maybe playing go and
*  chess and other things, but they don't feel at all in any shape or form conscious in the way that
*  you do to me or I do to you. And I think actually building AI, these intelligent constructs,
*  is one of the best ways to explore the mystery of consciousness, to break it down.
*  Because we're going to have devices that are pretty smart at certain things or capable
*  at certain things, but potentially won't have any semblance of self-awareness or other things.
*  And in fact, I would advocate if there's a choice, building systems in the first place,
*  AI systems that are not conscious to begin with are just tools until we understand them better
*  and the capabilities better. So on that topic, just not as the CEO of DeepMind,
*  just as a human being, let me ask you about this one particular anecdotal evidence of the Google
*  engineer who made a comment or believed that there's some aspect of a language model,
*  the Lambda language model that exhibited sentience. So you said you believe there might
*  be a responsibility to build systems that are not sentient. And this experience of a particular
*  engineer, I think, I'd love to get your general opinion on this kind of thing, but I think it
*  will happen more and more and more, which not when engineers but when people out there that
*  don't have an engineer background start interacting with increasingly intelligent systems, we
*  anthropomorphize them, they start to have deep impactful interactions with us in a way that we
*  miss them when they're gone. And we sure as heck feel like they're living entities,
*  self-aware entities, and maybe even we project sentience onto them. So what's your thought about
*  this particular system? Have you ever met a language model that's sentient?
*  No.
*  On record?
*  No.
*  And what do you make of the case of when you kind of feel that there's some elements of sentience to
*  this system?
*  Yeah. So this is an interesting question and obviously a very fundamental one. So the first
*  thing to say is I think that none of the systems we have today, I would say even have one iota of
*  semblance of consciousness or sentience. That's my personal feeling interacting with them every day.
*  So I think this way premature to be discussing what that engineer talked about. I think at the
*  moment it's more of projection of the way our own minds work, which is to see a purpose and
*  direction in almost anything that we, our brains are trained to interpret agency basically in things,
*  even inanimate things sometimes. And of course with a language system, because language is so
*  fundamental to intelligence, it's going to be easy for us to anthropomorphize that.
*  I mean, back in the day, even the first, the dumbest sort of template chatbots ever, Eliza
*  and the ilk of the original chatbots back in the 60s fooled some people under certain
*  circumstances, right? It pretended to be a psychologist. So just basically wrap it back
*  to you, the same question you asked it back to you. And some people believe that. So I don't think
*  we can, this is why I think the Turing test is a little bit flawed as a formal test because it
*  depends on the sophistication of the judge, whether or not they are qualified to make that
*  distinction. So I think we should talk to the top philosophers about this, people like Daniel Dennett
*  and David Chalmers and others who've obviously thought deeply about consciousness. Of course,
*  consciousness itself hasn't been well, there's no agreed definition. If I was to speculate about
*  that, the working definition I like is it's the way information feels when it gets processed. I
*  think maybe Max Tegmark came up with that. I like that idea. I don't know if it helps us get towards
*  any more operational thing, but I think it's a nice way of viewing it. I think we can obviously
*  see from neuroscience certain prerequisites that are required, like self-awareness, I think is
*  necessary but not sufficient component. This idea of a self and other and set of coherent preferences
*  that are coherent over time. These things are maybe memory. These things are probably needed for
*  a sentient or conscious being. But the difficult thing I think for us when we get, and I think
*  this is a really interesting philosophical debate, is when we get closer to AGI and much more powerful
*  systems than we have today, how are we going to make this judgment? One way, which is the Turing
*  test, is a behavioral judgment. Is the system exhibiting all the behaviors that a human sentient
*  or a sentient being would exhibit? Is it answering the right questions? Is it saying the right things?
*  Is it indistinguishable from a human? And so on. But I think there's a second thing that makes us
*  as humans regard each other as sentient. Why do we think this? And I debated this with Daniel
*  Dennett. And I think there's a second reason that's often overlooked, which is that we're
*  running on the same substrate. So if we're exhibiting the same behavior, more or less,
*  as humans, and we're running on the same carbon-based biological substrate, the squishy
*  few pounds of flesh in our skulls, then the most parsimonious, I think, explanation is that you're
*  feeling the same thing as I'm feeling. But we will never have that second part, the substrate
*  equivalence, with a machine. So we will have to only judge based on the behavior. And I think
*  the substrate equivalence is a critical part of why we make assumptions that we're conscious.
*  And in fact, even with animals, high-level animals, why we think they might be, because
*  they're exhibiting some of the behaviors we would expect from a sentient animal. And we know they're
*  made of the same things, biological neurons. So we're going to have to come up with explanations
*  or models of the gap between substrate differences between machines and humans to get anywhere
*  beyond the behavioral. But to me, the practical question is very interesting and very important.
*  When you have millions, perhaps billions of people believing that you have a sentient AI,
*  believing what that Google engineer believed, which I just see as an obvious, very near-term
*  future thing, certainly on the path to AGI, how does that change the world? What's the
*  responsibility of the AI system to help those millions of people? And also, what's the ethical
*  thing? Because you can make a lot of people happy by creating a meaningful, deep experience
*  with a system that's faking it before it makes it. Who is to say what's the right thing to do?
*  Should AI always be tools? Why are we constraining AI to always be tools as opposed to
*  friends?
*  I think these are fantastic questions and also critical ones. And we've been thinking about this
*  since the start of DeepMind and before that because we planned for success and
*  however remote that looked like back in 2010. And we've always had these ethical considerations
*  as fundamental at DeepMind. My current thinking on the language models and large models is
*  they're not ready. We don't understand them well enough yet in terms of analysis tools and
*  guardrails for what they can and can't do and so on to deploy them at scale. Because I think
*  there are big still ethical questions like should an AI system always announce that it is
*  an AI system to begin with? Probably yes. What do you do about answering those philosophical
*  questions about the feelings people may have about AI systems perhaps incorrectly attributed?
*  So I think there's a whole bunch of research that needs to be done first
*  to responsibly before you can responsibly deploy these systems at scale. That will be at least be
*  my current position. Over time, I'm very confident we'll have those tools like interpretability
*  questions and analysis questions. And then with the ethical quandary, I think there
*  it's important to look beyond just science. That's why I think philosophy, social sciences,
*  even theology, other things like that come into it. Where arts and humanities, what does it mean
*  to be human and the spirit of being human and to enhance that and the human condition?
*  Allow us to experience things we could never experience before and improve the overall human
*  condition and humanity overall. Get radical abundance, solve many scientific problems,
*  solve disease. This is the era I think we're heading into if we do it right.
*  But we've got to be careful. We've already seen with things like social media how dual use
*  technologies can be misused by firstly, by bad actors or naive actors or crazy actors.
*  So there's that set of just the common or garden misuse of existing dual use technology.
*  And then of course, there's an additional thing that has to be overcome with AI that eventually
*  it may have its own agency. So it could be good or bad in of itself. So I think these questions
*  have to be approached very carefully using the scientific method, I would say, in terms of
*  hypothesis generation, careful control testing, not live A-B testing out in the world. Because
*  with powerful technologies like AI, if something goes wrong, it may cause a lot of harm before you
*  can fix it. It's not like an imaging app or game app where if something goes wrong, it's relatively
*  easy to fix and the harm is relatively small. So I think it comes with the usual
*  cliche of like with a lot of power comes a lot of responsibility. And I think that's the case here
*  with things like AI, given the enormous opportunity in front of us. And I think we need a lot of voices
*  and as many inputs into things like the design of the systems and the values they should have and
*  what goals should they be put to. I think as wide a group of voices as possible beyond just the
*  technologists is needed to input into that and to have a say in that, especially when it comes to
*  deployment of these systems, which is when the rubber really hits the road, it really affects
*  the general person in the street rather than fundamental research. And that's why I say,
*  I think as a first step, it would be better if we have the choice to build these systems as tools
*  to give and I'm not saying that it should never they should never go beyond tools,
*  because of course, the potential is there for it to go way beyond just tools. But I think that
*  would be a good first step in order for us to, you know, allow us to carefully experiment,
*  understand what these things can do. So the leap between tool to sentient entity being
*  is one we should take very careful. Yes. Let me ask a dark personal question. So you're one of the
*  most brilliant people in the community, also one of the most kind, and if I may say sort of loved
*  people in the community, that said, creation of a super intelligent AI system would be one of the
*  most powerful things in the world, tools or otherwise. And again, as the old saying goes,
*  power corrupts and absolute power corrupts. Absolutely. You are likely to be one of the
*  people, but I would say probably the most likely person to be in the control of such a system.
*  Do you think about the corrupting nature of power when you talk about these kinds of systems that
*  as all dictators and people have caused atrocities in the past always think they're doing good,
*  but they don't do good because the powers polluted their mind about what is good and what is evil.
*  Do you think about this stuff or are we just focused on language model?
*  No, I think about them all the time. And I think what are the defenses against that? I think one
*  thing is to remain very grounded and sort of humble, no matter what you do or achieve. And I
*  try to do that. My best friends are still my set of friends from my undergraduate Cambridge days,
*  my family's and friends are very important. I think trying to be a multidisciplinary person,
*  it helps to keep you humble because no matter how good you are at one topic, someone will be
*  better than you at that. And always relearning a new topic again from scratch or new field is
*  very humbling. So for me, that's been biology over the last five years. Huge area topic and
*  I just love doing that, but it helps to keep you grounded and keeps you open minded.
*  And then the other important thing is to have a really group amazing set of people around you at
*  your company or your organization who are also very ethical and grounded themselves and help to
*  keep you that way. And then ultimately, just to answer your question, I hope we're going to be a
*  big part of birthing AI and that being the greatest benefit to humanity of any tool or technology ever
*  and getting us into a world of radical abundance and curing diseases and solving many of the big
*  challenges we have in front of us and then ultimately help the ultimate flourishing of
*  humanity to travel the stars and find those aliens if they are there. And if they're not there,
*  find out why they're not there, what is going on here in the universe.
*  This is all to come and that's what I've always dreamed about. But I think AI is too big an idea.
*  It's not going to be, there'll be a certain set of pioneers who get there first. I hope we're in
*  the vanguard so we can influence how that goes. And I think it matters who builds, which cultures
*  they come from and what values they have, the builders of AI systems. Because I think even though
*  the AI system is going to learn for itself most of its knowledge, there'll be a residue in the system
*  of the culture and the values of the creators of that system. And there's interesting questions to
*  discuss about that geopolitically, different cultures as we're in a more fragmented world
*  than ever, unfortunately. I think in terms of global cooperation, we see that in things like
*  climate where we can't seem to get our act together globally to cooperate on these pressing matters.
*  I hope that will change over time. Perhaps, if we get to an era of radical abundance, we don't have
*  to be so competitive anymore. Maybe we can be more cooperative if resources aren't so scarce.
*  It's true that in terms of power corrupting and leading to destructive things, it seems that some
*  of the atrocities of the past happen when there's a significant constraint on resources.
*  I think that's the first thing. I don't think that's enough. I think scarcity is one thing
*  that's led to competition, zero-sum game thinking. I would like us to all be in a positive some world.
*  And I think for that, you have to remove scarcity. I don't think that's enough, unfortunately,
*  to get world peace because there's also other corrupting things like wanting power over people
*  and this kind of stuff, which is not necessarily satisfied by just abundance. But I think it will
*  help. But I think ultimately, AI is not going to be run by any one person or one organization.
*  I think it should belong to the world, belong to humanity. And I think there'll be many ways
*  this will happen. And ultimately, everybody should have a say in that. Do you have advice
*  for young people in high school and college? Maybe if they're interested in AI or
*  interested in having a big impact on the world, what they should do to have a career they can
*  be proud of or to have a life they can be proud of. I love giving talks to the next generation.
*  What I say to them is actually two things. I think the most important things to learn about
*  and to find out about when you're young is what are your true passions is first of all,
*  as two things. One is find your true passions. And I think you can do that by the way to do that is
*  to explore as many things as possible when you're young and you have the time and you can take those
*  risks. I would also encourage people to look at the finding the connections between things
*  in a unique way. I think that's a really great way to find a passion. Second thing I would say
*  advise is know yourself. So spend a lot of time understanding how you work best, like what are
*  the optimal times to work? What are the optimal ways that you study? What are your how do you
*  deal with pressure? Sort of test yourself in various scenarios and try and improve your
*  weaknesses. But also find out what your unique skills and strengths are and then hone those.
*  So then that's what will be your super value in the world later on. And if you can then combine
*  those two things and find passions that you're genuinely excited about that intersect with what
*  your unique strong skills are, then you're onto something incredible and I think you can make a
*  huge difference in the world. So let me ask about know yourself. This is fun. This is fun. Quick
*  questions about day in the life, the perfect day, the perfect productive day in the life of
*  Demisys Hobbits. Maybe these days there's a lot involved. Maybe a slightly younger Demisys Hobbit
*  where you could focus on a single project maybe. How early do you wake up? Are you night owl?
*  Do you wake up early in the morning? What are some interesting habits? How many dozens of cups of
*  coffees do you drink a day? What's the computer that you use? What's the setup? How many screens?
*  What kind of keyboard? Are we talking Emax Vim or are we talking something more modern?
*  So a bunch of those questions. So maybe day in the life. What's the perfect day involved?
*  Well these days it's quite different from say 10, 20 years ago. Back 10, 20 years ago it would have
*  been a whole day of research, individual research or programming, doing some experiment, neuroscience,
*  computer science experiment, reading lots of research papers and then perhaps at night time
*  reading science fiction books or playing some games. But lots of focus, so like deep focused
*  work on whether it's programming or reading research papers. Yes, so that would be lots of
*  deep focus work. These days for the last sort of I guess five to 10 years I've actually got quite
*  a structure that works very well for me now which is that I'm a complete night owl, always have been,
*  so I optimize for that. So I basically do a normal day's work, get into work about 11 o'clock and
*  sort of do work till about seven in the office and I will arrange back-to-back meetings for the entire
*  time of that and with as many, meet as many people as possible. So that's my collaboration
*  management part of the day. Then I go home, spend time with the family and friends, have dinner,
*  relax a little bit and then I start a second day of work. I call it my second day of work around 10
*  pm, 11 pm and that's the time till about the small hours of the morning, four, five in the morning
*  where I will do my thinking and reading research, writing research papers. Sadly I don't have
*  time to code anymore but it's not efficient to do that these days given the amount of time I have
*  but that's when I do, you know, maybe do the long kind of stretches of thinking and planning and
*  then probably, you know, using email or other things I would set, I would fire off a lot of
*  things to my team to deal with the next morning but actually thinking about this overnight we
*  should go for this project or arrange this meeting the next day. When you think it through a problem,
*  are you talking about a sheet of paper or the pen pen? Is there some structured process?
*  I still like pencil and paper best for working out things but these days it's just so efficient
*  to read research papers just on the screen. I still often print them out actually, I still prefer to
*  mark out things and I find it goes into the brain quicker, better and sticks in the brain better
*  when you're still using physical pen and pencil and paper. So you take notes with the? I have
*  lots of notes, electronic ones and also whole stacks of notebooks that I use at home.
*  On some of these most challenging next steps, for example, stuff none of us know about that you're
*  working on, you're thinking, there's some deep thinking required there, right? Like what is the
*  right problem? What is the right approach? Because you're going to have to invest a huge amount of
*  time for the whole team, they're going to have to pursue this thing. What's the right way to do it?
*  Is RL going to work here or not? What's the right thing to try? What's the right benchmark to you?
*  Do we need to construct a benchmark from scratch? All those kinds of things.
*  Yes. So I think all those kinds of things in the nighttime phase but also much more,
*  I've always found the quiet hours of the morning when everyone's asleep, it's super quiet outside.
*  I love that time, it's the golden hours between one and three in the morning.
*  Put some music on, some inspiring music on and then think these deep thoughts. So that's when
*  I would read my philosophy books and Spinoza is my recent favourite can, all these things.
*  I read about a great scientist of history, how they did things, how they thought things.
*  So that's when I do all my creative thinking. I think people recommend you do your
*  creative thinking in one block and the way I organise the day, that way I don't get
*  interrupted because obviously no one else is up at those times. So I can get super deep and super
*  into flow. The other nice thing about doing it nighttime wise is if I'm really onto something
*  or I've got really deep into something, I can choose to extend it and I'll go into six in the
*  morning, whatever, and then I'll just pay for it the next day because I'll be a bit tired and I
*  won't be my best. But that's fine. I can decide looking at my schedule the next day and given
*  where I'm at with this particular thought or creative idea that I'm going to pay that cost
*  the next day. So I think that's more flexible than morning people who do that. They get up at four
*  in the morning, they can also do those golden hours then, but then their scheduled day starts
*  at breakfast, a.m. whatever they have their first meeting. And then it's hard, you have to reschedule
*  day if you inflow. Yeah, that could be a truly special thread of thoughts that
*  you're too passionate about. This is where some of the greatest ideas could potentially come is when
*  you just lose yourself late in the night. And for the meetings, I mean, you're loading in really
*  hard problems in a very short amount of time. So you have to do some kind of first principles
*  thinking here. It's like, what's the problem? What's the state of things? What's the right next step?
*  You have to get really good at context switching, which is one of the hardest things
*  because especially as we do so many things, if you include all the scientific things we do,
*  scientific fields we're working in, these are entire complex fields in themselves. And you
*  have to sort of keep up to abreast of that. But I enjoy it. I've always been a sort of generalist
*  in a way. And that's actually what happened in my games career after chess. One of the reasons I
*  stopped playing chess was because I got into computers, but also I started realizing there
*  were many other great games out there to play too. So I've always been that way inclined,
*  multidisciplinary, and there's too many interesting things in the world to spend all
*  your time just on one thing. So you mentioned Spinoza, got to ask the big, ridiculously big
*  question about life. What do you think is the meaning of this whole thing? Why are we humans
*  here? You've already mentioned that perhaps the universe created us. Is that why you think we're
*  here? To understand how the universe works? Yeah, I think my answer to that would be and at least
*  the life I'm living is to gain and understand the knowledge, to gain knowledge and understand
*  the universe. That's what I think. I can't see any higher purpose than that. If you think back
*  to the classical Greeks, the virtue of gaining knowledge, I think it's one of the few true
*  virtues is to understand the world around us and the context and humanity better. And I think if
*  you do that, you become more compassionate and more understanding yourself and more tolerant
*  and all these other things may flow from that. And to me, understanding the nature of reality,
*  that is the biggest question. What is going on here is sometimes the colloquial way I say. What
*  is really going on here? It's so mysterious. I feel like we're in some huge puzzle. But the
*  world is also seems to be, the universe seems to be structured in a way. Why is it structured in a
*  way that science is even possible? The scientific method works, things are repeatable. It feels like
*  it's almost structured in a way to be conducive to gaining knowledge. Why should computers be
*  even possible? Isn't that amazing that computational electronic devices can be possible?
*  And they're made of sand, our most common element that we have, silicon on the earth's crust. It
*  could be made of diamond or something. Then we would have only had one computer. A lot of things
*  are slightly suspicious to me. This puzzle sure as heck sounds like something we talked about
*  earlier, what it takes to design a game that's really fun to play for prolonged periods of time.
*  It does seem like this puzzle, like you mentioned, the more you learn about it,
*  the more you realize how little you know. It humbles you, but excites you by the possibility
*  of learning more. It's one heck of a puzzle we got going on here. Like I mentioned, of all the
*  people in the world, you're very likely to be the one who creates the AGI system that achieves human
*  level intelligence and goes beyond it. If you got a chance, and very well you could be the person
*  that goes into the room with the system and have a conversation, maybe you only get to ask one
*  question. If you do, what question would you ask her? I would probably ask what is the true nature
*  of reality. I think that's the question. I don't know if I'd understand the answer because maybe
*  it would be 42 or something like that. But that's the question I would ask.
*  Then there'll be a deep sigh from the systems like, all right, how do I explain to this human?
*  Exactly.
*  All right, I don't have time to explain. Maybe I'll draw you a picture. How do you even begin
*  to answer that question?
*  Well, I think it would...
*  What would you think the answer could possibly look like?
*  I think it could start looking like more fundamental explanations of physics would be the beginning.
*  More careful specification of that, taking you, walking us through by the hand as to what
*  one would do to maybe prove those things out.
*  Maybe giving you glimpses of what things you totally missed in the physics of today.
*  Exactly.
*  Exactly.
*  Just here's glimpses of, no, there's a much more elaborate world or a much simpler world or
*  something.
*  A much deeper, maybe simpler explanation of things, right? Then the standard model of physics,
*  which we know doesn't work, but we still keep adding to. That's how I think the beginning of
*  an explanation would look. It would start encompassing many of the mysteries that we
*  have wondered about for thousands of years, like consciousness, dreaming, life, and gravity,
*  all of these things.
*  Yeah, giving us glimpses of explanations for those things.
*  Well, Damis, you're one of the special human beings in this giant puzzle of ours.
*  It's a huge honor that you would take a pause from the bigger puzzle to solve this small
*  puzzle of a conversation with me today. It's truly an honor and a pleasure.
*  Thank you so much.
*  Glad to have you. I really enjoyed it. Thanks, Lex.
*  Thanks for listening to this conversation with Damis Esabas. To support this podcast,
*  please check out our sponsors in the description. And now, let me leave you with some words from
*  Edsker Dijkstra. Computer science is no more about computers than astronomy is about telescopes.
*  Thank you for listening and hope to see you next time.

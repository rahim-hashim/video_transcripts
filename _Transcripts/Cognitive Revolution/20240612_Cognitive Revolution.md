---
Date Generated: June 13, 2024
Transcription Model: whisper medium 20231117
Length: 3165s
Video Keywords: []
Video Views: 202
Video Rating: None
Video Description: Dive into the world of AI investments with Eric Vishria of Benchmark and Sergiy Nesterenko of Quilter. Explore the future of AI in hardware design, the strategies for venture capital investment in the AI era, and the impact on society. Discover why Benchmark has yet to invest in foundation model companies and the significance of solving enduring problems in this dynamic field. Join us for an eye-opening discussion on the intersection of AI technology and business innovation.

SPONSORS:
Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Recommended Podcast - The Riff with Byrne Hobart
Byrne Hobart, the writer of The Diff, is revered in Silicon Valley. You can get an hour with him each week. See for yourself how his thinking can upgrade yours.
Spotify: https://open.spotify.com/show/6rANlV54GCARLgMOtpkzKt
Apple: https://podcasts.apple.com/us/podcast/the-riff-with-byrne-hobart-and-erik-torenberg/id1716646486

CHAPTERS:
(00:00:00) Introduction
(00:10:12) The Idea Maze
(00:12:28) Disruptive Approach
(00:15:47) Sparse reward problem
(00:18:26) Sponsors: Oracle | Brave
(00:20:34) Reliability of the reward signal
(00:28:12) Model size and compute
(00:30:14) Simulation methods
(00:35:48) Superhuman circuit board design
(00:38:53) Sponsors: Squad | Omneky
(00:40:38) What does the future of circuit board design look like?
(00:43:11) How do I make money in AI?
(00:46:18) What is cutting edge?
(00:48:34) Researchers vs. engineers
(00:50:51) Call for startups
---

# Investing in AI for Hard Tech, with Eric Vishria of Benchmark and Sergiy Nesterenko of Quilter
**Cognitive Revolution:** [June 12, 2024](https://www.youtube.com/watch?v=64iPS9AXrcc)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution. Today we have a short but fascinating
*  conversation about investing venture capital into the AI wave and about the application of AI
*  to hardware problems with Eric Visschria, general partner at Benchmark, and Sergey Nesterenko,
*  founder and CEO of Quilter. Regular listeners will recall that we recently cross-posted an episode
*  featuring Sergey from Will Summerlin's autopilot feed, but rest assured that this episode covers
*  almost entirely new territory, including what amount to my follow-up questions on Quilter's
*  vision for superhuman circuit board design, the reinforcement learning approach that they're
*  taking to get there, and what this could all enable for society more broadly. We also get
*  Eric's point of view on what sorts of investments are likely to pay off in the AI era, starting with
*  the provocative vision of circuit board design as an AI and done problem, not another copilot
*  problem, that attracted him to Quilter in the first place. We also consider the questions that
*  Benchmark asks in an attempt to determine whether a new company is solving an enduring or a temporary
*  problem, and we discuss the reasons that Benchmark has not invested in any foundation model companies
*  to date. Eric describes these companies as investing huge amounts of capital to create some of the most
*  remarkable, but also some of the most rapidly depreciating assets in venture capital history.
*  As always, if you're finding value in the show, we'd ask that you take a moment to share it with
*  friends. And at the same time, we invite your constructive feedback and your topic or guest
*  suggestions either via our website, cognitiverevolution.ai, or by DMing me on your
*  favorite social network. Finally, a quick reminder that I am looking to connect with aspiring AI
*  engineers and also AI advisors who are excited about helping Main Street businesses take advantage
*  of AI technology. I've mentioned this twice and got good feedback each time, so please keep it coming,
*  and before long, we might have a Cognitive Revolution jobs board on our hands. For now,
*  I hope you enjoy this under the hood look at AI investment strategy and this glimpse into the
*  future of AI-powered hardware design with Eric Vishria of Benchmark and Sergey Nestorenko of Quilter.
*  Eric Vishria, general partner at Benchmark and Sergey Nestorenko, founder and CEO at Quilter.
*  Welcome to the Cognitive Revolution. Thank you for having us.
*  Yeah, excited for this conversation. Regular listeners will of course know that we ran
*  a cross post with Sergey from Will Summerlin's new feed on all things AI in automation.
*  For the deep dive on Quilter, that's the episode to check out to get up to speed and learn how the
*  company is approaching the automation of integrated circuit board designs with a reinforcement
*  learning approach, which is fascinating. Today, I think a little bit of a broader conversation on
*  just kind of where this whole AI thing is going, big picture and how you guys are thinking about
*  both investing in companies that will hopefully stand the test of time and also try to build a
*  company that will be able to successfully ride the wave and not be crashed over by the wave,
*  which is definitely like a challenging dance for many founders right now. I guess, Eric,
*  maybe you want to start off with just giving a little bit of background as to what it was that
*  got you guys interested in Quilter specifically and how that fits into your broader philosophy
*  and portfolio. Sure. Super, super excited to be here. So thank you again for having me
*  and having us on the show. There's no shortage of AI startups out there. So each of us,
*  each of the benchmark partners are probably meeting four or five of them a week. And so
*  you're kind of perpetually meeting new ones. And a lot of them sound really interesting.
*  You know, they have really interesting ideas. And I would actually even say the revenue traction
*  on a lot of the companies is tremendous. Like it's just unlike anything that we've seen just
*  in terms of the speed of revenue traction and everything else. But obviously, in the kind of
*  timeline that we're investing as early stage investors, you're looking on a five or 10 year
*  horizon really of the company maturing into a big business and wanting to be one of these
*  exceptional kind of companies that get created in our industry a few times a decade. And so
*  a big part of what we're looking at is which of these companies is not just riding the wave and
*  not just on a sugar high, as I would describe it, of either revenue or traction or developers or
*  hype investor dollars, but has an opportunity to build a really big business. And obviously,
*  that's really hard to figure out at the early stages of the company, but that's
*  what we're paid to do. So that's what we try to do. And one of the frameworks that I use
*  right often is just, well, what's changing in the world that is going to enable this company to be
*  really large, which has nothing to do with company actually, it's just like what's happening in the
*  world. And of course, there's AI, which is okay, that's a wave, but there's actually, you need
*  something more substantive and specific for a company to be able to be created and be durable
*  around that. And I think in the case of Quilter, there were a couple of things that really caught
*  my eye, which was first off, obviously, electronics are permeating every aspect of our life,
*  like things that were very simple, not that long ago, like a light switch now have electronics in
*  them. They have circuit boards in them in ways that just weren't true before. And so you have a
*  rapid expansion of the number of companies, the number of products that are electronics and have
*  circuit boards in them. And that is a first very fundamental thing that's happening in the world
*  and seems bad. And I didn't really understand this until I met Sergey, but the process of actually
*  designing or laying out these circuit boards, place and route, I guess, as it is called in the
*  parlance is like an incredibly manual and time consuming and slow process. And one of the things
*  I think we know just industry wide is the faster you're able to iterate on products, the better
*  and better they get. And that kind of friction in the process seems bad in a world where electronics
*  are permeating everything that we interact with. So that was interesting. But then the real thing
*  where it started to get where the story started to get really compelling to me was particularly,
*  I don't know, six months ago or so, everybody was talking about co-pilots, co-pilot this,
*  co-pilot that, there's a unique co-pilot for lawyers, there's a co-pilot for doctors,
*  there's a co-pilot for developers. In each of those spaces, there's team companies that emerge
*  that are doing some form of co-pilots. And Sergey's kind of provocative statement at the time
*  was like, this isn't a co-pilot problem. It's just not for co-pilots. You don't want a human assisted
*  guy to do printed circuit board layout. And I was like, oh, okay, that's different than anything
*  that I've heard in the last few months. That's just a different view. And so it's, well, why?
*  And as well, a co-pilot or an auto layout does 90% of the job. Then by definition, the other 10%
*  of these layouts, which is they're all these thin lines that are connecting one component to another
*  component. And they're all over the circuit board. As you look at it, you're like, wow, a human laid
*  that out. And then that seems really tough. And if I had to draw another line, how am I going to draw
*  the line and not mess up everything else that's already laid out? They're pretty dense. And so
*  it's like, this isn't a, it's just not a human assist problem. It's a problem that should be AI
*  and done. AI should just do it, do it entirely. And in order to get there, we have to have a
*  clean interface where we kind of get the design and architecture of it. And then we have a thing
*  that can be spit out and go to manufacturing. But those interfaces exist in the industry. And so we
*  sit in the middle and we take on that aspect of it and we just lay it out. And we have to obviously
*  start with simpler boards. We can't do a super, super complicated iPhone A14 to start. We got
*  to start with something simpler and work our way up, but we can work our way up and just be AI and
*  done. And so that was the first really provocative, just makes you think, oh, wait, there's a whole
*  bunch of things that we just are doing with humans and co-pilot's vogue, but is co-pilot the right
*  answer? In a whole bunch of cases like co-pilot, it's not the right answer. It's just not. We should
*  just let AI do it, which is cool. That was a different perspective. So that was the first thing.
*  And then the second thing, which really kind of got me thinking was, okay, everyone's talking about
*  large language models. And he's, yeah, we're not using any of that. That's not what we're using.
*  Oh, okay. Well, that's different too. And I'll come back around in a second, but that was,
*  his perspective was like, hey, that's not the right AI for this problem. The right AI
*  is we design a game, we tell the game what the optimization problem is. And do we want to optimize
*  for price? Do we want to optimize for performance? Do we want to have a really dense board that's
*  expensive to build, but super power efficient? Or do we want to have a really cheap board that's
*  bigger and has more space on it? And if we actually give the user these controls, then the AI will be
*  able to give them a range of solutions and they can kind of pick where they want to be on that
*  solution set. And I was like, that's cool. That's a very provocative thing. And so those were kind
*  of the very specific things like, which is there's electronics permeating everything. There was a
*  view that this is a AI and done problem, not a co-pilot problem, which was different. And there
*  was a view of the right kind of AI to use for this particular problem, which isn't, again, the kind
*  of thing that everyone's talking about. And as you kind of dug into it, it seemed like really
*  cogent. And I know nothing about printing circuit boards and know very little about, obviously,
*  specific technology. So you're kind of thinking about it and you're trying to validate it. And
*  then you're talking to people and going after it. But the biggest thing that just to kind of zoom
*  out for a second, for any entrepreneur and anyone kind of thinking through these things, there's a
*  Chris Dixon wrote this short post several years ago called the IDMAs. And if you haven't read it,
*  you should read it because it's a short but very powerful pose. And I'll summarize it. What you
*  want to do when you're talking to an entrepreneur is like you want someone who's been like rolling
*  around in this idea for a long time. Like they've been in the IDMAs and they've kind of gone down a
*  path and they've hit a dead end and then they've backed up and gone down a different path and hit
*  different dead end and then backed up and kind of tried to figure their way through the maze.
*  And as you're talking to them and asking them questions, what you keep getting is you keep
*  getting, yeah, I thought about that, but here's why that doesn't work. So here's why I think this
*  could work. And you're just like, and what you realize is maybe they have a path through or
*  maybe they don't, but they've been exploring and living and rolling around in this idea and turning
*  it over and turning it this way and that way. And so they just, there's so much depth on the problem.
*  There's so much depth on the potential solution that you kind of are like, if there's going to be
*  someone who's going to figure it out the way through the maze, like this person has a really
*  good shot at it. And obviously with Sergey, his experience at SpaceX, designing a bunch of boards,
*  going through that, and then playing with and trying to figure out solutions and applications
*  of AI to solve this problem, first realizing the problem, trying to pursue a whole bunch of
*  different ways to solve the problem, having the realization that it really is an AI and done kind
*  of problem, having the realization that of the right kind of AI techniques to use for it.
*  Those were just like evidence to me that he's lived in this maze for a long time.
*  And so that was probably like the macro thing that gets you excited. It just ends up being like very
*  exciting when you find someone who has kind of approached it like that.
*  Cool. I appreciate the backstory. I kind of want to maybe circle back in a minute to
*  this disruptive approach. This seems like a pretty classic, almost textbook example of
*  a disruptive solution in that it seems like it's coming in at kind of the low end of the market.
*  It's serving people. If I recall from the other episode that we posted that it was striking to
*  hear actually that SpaceX has an internal board team, but they couldn't serve you.
*  And it's a man talk about a market that's got to be very broadly underserved if an internal
*  specialist team can't even serve the other team at SpaceX. Like that's pretty wild. So it seems
*  like there's a potentially a very kind of textbook pattern here of starting at the bottom of this
*  market, massively expanding the bottom of the market. I wonder how often that's something that
*  you're seeing across the portfolio or specifically trying to do. But maybe before coming back to that,
*  can I try a little bit of this idea maze stuff? I have a couple of ideas that I'm wondering kind of
*  maybe why they didn't work or why they wouldn't work. Would you be game for a couple of possibly
*  hair-brained ideas that you can shoot down, Sergey? Yeah, if I can, happy to.
*  Okay. These are potentially quite novice ideas, but I guess for starters, what's the data
*  landscape in this space? A typical deep learning approach is predicated on a lot of data. Is there
*  any open source data set out there that somebody could go tap into any significant scale of
*  published boards that could be used in that way or was sort of just lack of data a forcing function
*  to make you go in another route AI-wise? Yeah, that's a good question. And probably one of the
*  most common questions that I get about how Quilter is using AI for this problem. I think what most
*  people tend to think is how does Co-Pilot work? You take all of GitHub and all of Stack Overflow,
*  feed it into an LLM and it makes good predictions based on the average human behavior. And obviously
*  we don't do that. So we don't do that for two reasons. One that you mentioned is there actually
*  just isn't that much data. So if you look at all of GitHub, not that many open source boards,
*  there's a few sources here and there, but not a lot. The best ones are locked away behind
*  companies. They're in Apple's repositories and Google's repositories and space access repositories.
*  But there's another reason that's even more compelling to me why that's the wrong approach,
*  which is fundamentally people are not good at designing boards, just full stop. So if it's a
*  process that takes for a complicated board two, three, four months, you are going to make a whole
*  bunch of like margin on margin decisions that make your resulting board like much bigger than it
*  otherwise could have been. I use more layers than it could have be more expensive than it could have.
*  And if you just use data to do supervised learning and try to predict boards, you're probably going
*  to get roughly that level of performance of a high level human designer, even if you could get
*  all of that data. But with reinforcement learning, you have the opportunity to go significantly
*  better than humans. Right? So this is the most famous example I always come back to is DeepMind
*  playing Go, right? The AlphaGo problem. They actually started first by training on human data
*  and then creating agents that are based on human expert moves. And they got to a grand master level
*  with that. But the best system today starts with no human data at all. It just learns how to play
*  the game and it determines whether it wins or loses. And then that is what gets you to far, far
*  superhuman levels. Nobody can match. So did you also start with like literally zero human
*  data as input or did you have some? And especially if you started with none, like how do you get over
*  the sparse reward problem? This seems to come up all the time. And I'm reminded also of the Eureka.
*  I used to say about AI, no Eureka moments, meaning like at least from the generalist systems,
*  you wouldn't see them doing like legitimately new stuff better than human. With the Eureka project,
*  actually, I started to have to say precious few Eureka moments because now there's at least like
*  some examples that are starting to pop up. In that case, I'm sure you're well aware they use
*  GPT-4 to write the reward function for the robot hand as it was like learning to do all these tasks
*  where in the beginning, its success is so fleeting or even non-existent that it's really hard to even
*  score what it's doing. So I guess I'm curious, how did you get over the sparse reward problem,
*  especially given how little data you had to go on at the beginning?
*  Yeah, totally. So in general, the sparse word problem kind of broadly stated is
*  you're kind of a good reward. So winning the game of creating a circuit board is so rare that as you
*  randomly explore, you never find it. And that's an issue because if you never get a signal that you
*  won a game, how do you ever learn anything? So the nice thing is that people have this problem,
*  right? Like people in general have broken up the problem of circuit board design into
*  many different steps and have basically come up with heuristics along the way.
*  So what Quilter can do in terms of not running into the ultimate sparse reward problem of design an
*  entire board and at the end, only if you get a yes from all the physics simulators that this board
*  is going to work, do you get a one and otherwise you get a zero, right? What we do is just break
*  it up into problems, right? So we take the first part of the problem, which is placing the components,
*  we can make sure that at that point it's manufacturable, the components don't collide,
*  things of that nature, and then compute some heuristics that basically indicate how likely
*  we are to succeed at the next phase, which is the routing phase, and so on and so forth.
*  Similar things for actually meeting all of the physics constraints, right? Like you can
*  simplify the problem to an extent to compute basic fast dense rewards that correlate to your
*  ultimate sparse reward. And that's what we have to do for now. Now I will say that long term,
*  the dream for this is definitely a single sparse reward. There's a single yes or no this board
*  will work or not. And when we're really uprooting the typical patterns that humans use and are trying
*  to do much better than them, that's what we'll have to do. But for now, since we're not as good
*  as humans at layout, especially on more complicated boards, we can still use the same heuristics that
*  they would use to just at least automate, similar to what they would have done.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  AI might be the most important new computer technology ever. It's storming every industry
*  and literally billions of dollars are being invested. So buckle up. The problem is that
*  AI needs a lot of speed and processing power. So how do you compete without costs spiraling out
*  of control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure,
*  or OCI. OCI is a single platform for your infrastructure, database, application development,
*  and AI needs. OCI has four to eight times the bandwidth of other clouds, offers one consistent
*  price instead of variable regional pricing. And of course, nobody does data better than Oracle.
*  So now you can train your AI models at twice the speed and less than half the cost of other clouds.
*  If you want to do more and spend less like Uber, eight by eight and Databricks Mosaic,
*  take a free test drive of OCI at oracle.com slash cognitive. That's oracle.com slash cognitive,
*  oracle.com slash cognitive. The Brave Search API brings affordable developer access to the
*  Brave Search index, an independent index of the web with over 20 billion web pages.
*  So what makes the Brave Search index stand out? One, it's entirely independent and built from
*  scratch. That means no big tech biases or extortionate prices. Two, it's built on real
*  page visits from actual humans, collected anonymously, of course, which filters out
*  tons of junk data. And three, the index is refreshed with tens of millions of pages daily,
*  so it always has accurate up-to-date information. The Brave Search API can be used to assemble a
*  data set to train your AI models and help with retrieval augmentation at the time of inference,
*  all while remaining affordable with developer-first pricing. Integrating the Brave Search API into
*  your workflow translates to more ethical data sourcing and more human representative data sets.
*  Try the Brave Search API for free for up to 2000 queries per month at brave.com slash API.
*  Yeah, interesting. It sounds like if I understand your comment correctly, the answer to this might
*  be yes. But I was wondering if there's an analogy between the reinforcement learning processes
*  that are used on the language models and these sort of evaluator systems, which I understand are
*  not models, right? They're just sort of either simulators or checkers that are deterministic.
*  But people worry a lot about, in the context of language models, the idea that the human reward
*  signal is not fully reliable, right? Like we're kind of inconsistent, we're sometimes mistaken.
*  It's been observed in many language models that there's a certain sycophancy tendency where it
*  seems to try to tell you what you want to hear versus the truth in some cases, because maybe
*  that's what got higher reward in the training process. So it sounds like there is a similar
*  problem here where the checkers are that they might be like purely physics simulators and could be
*  like rock solid, or I could imagine that they're on a foundation of sort of a bunch of heuristics,
*  which might in some subtle ways kind of also lead the process a bit astray.
*  One thing that I've, this is an analogy that is imperfect in about 50 ways, but it's kind of
*  supposed to like, one of the things that I've been thinking about to try to articulate the GEN-AI
*  limitations, and particularly like the LOM and even stability models, like limitations versus
*  versus some of these other techniques and what humans are actually good at,
*  is like, I think humans are very good at extrapolation. So like coming up with novel
*  things and developing and pushing creativity and if this, then that, like we can also do this and
*  you can take it and extrapolate. But because of the way these are trained and everything else,
*  it feels, and of course, who knows, but it feels like a lot of the GEN-AI stuff is good as
*  interpolation, which is within the bounds of things we already know, like what are other points,
*  like in that space. And it kind of makes sense if you think about it, like it's, they're interpolating,
*  they're figuring out like what the next word is or what the next image could look like based on
*  the training set that is pushed in a bunch of dimensions and humongous and everything else,
*  but it's still bound. It's bound by all the stuff that humans have prior created. And so
*  this is part of why I think that AI scare stuff is so misguided and not really because it's,
*  hey, if they're interpolating, okay, that's like, it seems fine. And it feels like humans will
*  continue to be good at extrapolation, which is developing new novel techniques to do like various
*  things. And that's a very important and valuable thing that we'll be able to continue to do.
*  That was a very macro answer to your question. I'm curious what you guys think.
*  I have a ton of thoughts about that, but I think our subscribers have heard them in other contexts.
*  I mean, I kind of feel like all this stuff is converging. So that's why I was making the,
*  trying to make the connection between the, how much, basically how much do we trust the reward
*  signal in the context of reinforcement learning for language models? It certainly helped a lot,
*  but not that much, I'd say is kind of the consensus answer. I wonder what the situation is
*  in the context of circuit boards. And then we could maybe also speculate about a similar question
*  when it comes to self-play there. It seems like the sort of narrow problem, not just one domain,
*  but in general, narrow problems are better suited to self-play for now. But we are also starting to
*  see some of these self-play techniques be applied to language models. And that's where I'm also like,
*  I don't know if it's going to stay in the bounds of what humans have given it for all that much
*  longer. But let's take it piece by piece. Sergey, let's start with the, how much do you trust the
*  reward signal in the context of your problem? Yeah. One of the nice things about working on
*  a hard physics problem, like humans are not in the loop. Like humans are actually bad at looking at
*  a board and judging if it's going to work or not. That's where like 80% of boards that are built are
*  faulty in some way. And it's because humans are just not good at that task fundamentally.
*  But all of the core physics is computable, right? Like we care about laws of the Maxwell equations
*  and laws of thermodynamics. And we've had convergent techniques to solve those for over a hundred years.
*  So in our case, like if you actually use the Oracle, like actually numerically solving
*  the Maxwell equations for every set of possible considerations and problems,
*  and you're kind of being careful to make sure that you're convergent and approximate everything
*  correctly, it's completely trustworthy, much more trustworthy than the human result by far.
*  Only problem with that is speed, right? If it takes 20 minutes to compute a single
*  physics solution and you need to do millions of those as you fine tune on your model,
*  that's problematic. So what you can do is you can make approximate models that are just conservative.
*  And so at that point, maybe you're not doing the best possible arrangement that physics could
*  allow, but you're still doing one that works, still doing one that competes or beats humans,
*  and it's still definitely going to work because you've been careful about the physics approximations
*  you've used. So I think that's one of the luxuries that we have is we don't have to negotiate with
*  humans, right? We just have to make sure that it's manufacturable and that it's going to work.
*  And physics tells us the answer. And physics is unambiguous about that.
*  Gotcha. And these were tools that existed already in the industry that you're able to build on top
*  of. Yeah. When the system is going about the process of designing, how iterative and sort
*  of tree searchy is that process? Because I think folks again will know at least the basics of
*  AlphaGo, right? These are like hyperparameters ultimately that you can sort of turn up or down
*  at runtime, right? But how deep are you going to allow a system like AlphaGo to search the space
*  of possible moves is a huge factor in how well it's going to do. If you just make it do a single
*  raw guess, it's not going to do super well. If you allow it to map out a bunch of possibilities and
*  then get scores on all those possibilities, then it can sometimes land on superhuman results.
*  So give us a sense for kind of what that search iteration and scoring loop looks like in your
*  context. Yeah, I think actually this is somewhere where a user has meaningful choice. So for a lot
*  of designs, you just want it fast, right? You're maybe primarily focused on making sure that your
*  schematic is okay. You don't care if the board is rather sparse, big, not very dense, maybe it's a
*  little more expensive to manufacture, so on and so forth. And in that case, you don't really want a
*  whole lot of search. You just want the first answer that's going to faithfully implement the schematic
*  on the board. And so in that case, the ideal thing is to return an answer within a few minutes to an
*  hour. On the other hand, suppose you're looking at a board that's going to have 100 million units
*  produced, like an iPhone leather board or something like that. And if you save a cent or a dollar on
*  every board, like that's a lot of value. In that case, you might let it search for a month and
*  explore in all sorts of directions, because that's how long it would have taken a human to do it
*  anyway for a single design, nevermind for the billions and billions you could explore with
*  this kind of system. So this isn't like a lever that we have in the tool today. We kind of just,
*  we basically treat overnight as the constraint for us right now. So the idea is that at the end of
*  the day, you finish your schematic, you uploaded it, and either immediately or sometime within the
*  next 12 hours, you get a result. And that morning, the next morning, you can look at it and see if
*  it's up to standards. But in the future, I see that being a lever. And it's for you to decide
*  what is more important to you. Yeah, that makes sense. What are the size of the models? What does
*  the compute look like? And how much of it is on the inference side versus on the scoring side
*  in the physics simulations? Yeah, those are all really good questions. So obviously, we're not
*  dealing with the kind of compute that LLMs deal with. Like we're not using 10,000 GPUs to train
*  across a trillion tokens and whatever crazy numbers are being used nowadays. This is a relatively
*  focused problem. And we can deal with much smaller models, but we can deal with much faster convergence
*  times, much less compute effectively. So the right now, the vast majority of the compute is
*  going into kind of the like actually playing the game. And so a lot of that is still actually CPU
*  cores. And then some of it is GP cores, depends on which part of the problem. And then the kind
*  of other part of the majority is going into like training. And we actually train during the
*  production runs. So we have fast enough environments and fast enough evaluation that as somebody
*  uploads a board, we're not just doing inference, we're actually training on that board as it was
*  uploaded. Now, the cost of physics is going to increase for us for sure. One of the ways that we
*  are expanding in the market is by enumerating all of the different types of physics considerations
*  you have to look at, and basically chipping them off one by one, right? So instead of saying, hey,
*  we're going to attempt all kinds of boards from all types of physics and do only the easy small ones,
*  we're saying, okay, for now, we're doing low speed boards that have up to four amps of current or
*  something like that. And okay, the physics to compute that is straightforward. The next thing
*  we're working on is high speed digital. And then we'll step into approximate, maybe bounding methods
*  of computing whether or not those high speed digital signals are going to be okay or not.
*  That won't be too expensive, but then we'll do one or two validation runs at the end with a full wave
*  model. And that's probably, if I had to guess right now, it's probably going to cost us a few GPU days
*  per board, something of that nature. Interesting. Okay. So it sounds like ultimately more
*  compute on the validation side than on the generation side, just because of the intensity
*  of simulating. Is it simulating physics or is it just solving? Is it like a closed form solution of
*  a ton of crazy differential equations or is it a sort of more Wolfram style? Like you got to actually
*  play this out in simulation, no shortcuts kind of a thing. Yeah, the simulations, that's another thing
*  that we're exploring heavily. There's a lot of different ways to solve differential equations,
*  so the most brute force simple way is at least for electromagnetic, this method called finite
*  difference time domain, where you literally just grid the entire world in 3D and you basically just
*  apply the differential forms of the Maxwell equations in sequence. So you take almost like
*  a curl of your local pixels of electric field and do that for the magnetic field, do that for electric
*  field, and you have to do that for a hundred million cells for a hundred thousand steps,
*  something like that. So it's just a lot of raw compute, but there's also much more clever methods.
*  So FEM is kind of a different way of approaching this problem within electromechanics, in particular,
*  this seems like method of moments that only look at like the surfaces of your different electrical
*  systems. And then there are approximations. So in the approximation of a low speed, low frequency,
*  you can actually factor out time out of the differential equations. And so you can do this
*  thing called the quasi-static approximation, where you don't run time at all, and you're only looking
*  at capacitance and mutual inductance of the systems. And for certain frequencies, that's a perfectly
*  sufficient approximation. So on and so forth. Yeah, very interesting. The sort of maybe that
*  reality maybe blunts the value of this next idea that I had, but I was thinking if you did have a
*  lot of data, and I wonder if there presumably are some, I don't know the structure of this industry,
*  but just using like chips as a reference point, obviously there's a few manufacturers that take
*  in a lot of designs and output the actual devices. I would assume there's probably some big players
*  in the circuit board space as well, who are like getting lots of designs. And one might imagine
*  the sort of big data approach, something like a diffusion model seems like it could be an interesting
*  fit for this, where you would kind of run a bunch of loops through whatever, and the models can vary.
*  So you have a transformer, like the latest stable diffusion version, they run a bunch of passes
*  through this transformer. At each step, they're denoising from raw visual noise to the image.
*  You could imagine sort of a similar approach to, and this is also happening for proteins now too,
*  it's crazy. So it seems like it could also perhaps apply to a circuit board design.
*  And first you're kind of doing, it would sort of even follow the path that you described,
*  where it's first you kind of lay out the big things, and then gradually you're getting more
*  and more into the low level details of the design. I guess questions there would be like,
*  do you think that would work? And if so, is that something that worries you from a competitive
*  standpoint at all? And then maybe though, it just wouldn't even be that much of advantage because
*  the, if all the compute is on the simulation side anyway, then maybe it doesn't really matter.
*  Yeah. So the big issue with that is the quality of your data, right? So one of the just the facts
*  of life in this industry is that three times out of four that you submit a board to a manufacturer,
*  it looks right. It's manufacturable. The manufacturer can follow all the tolerances
*  and all that stuff, but the physics just doesn't work. So even if you collected all of that data,
*  you still have the problem of going through and identifying which of these is an actual working
*  board and which of these have mistakes, right? Because it's a junior engineer or somebody who
*  didn't see some sort of issue or something like that. Even senior engineers make mistakes on
*  the electromagnetic supports all the time. You just, you fundamentally have thousands of components,
*  tens of thousands of traces to look at, all of which impact the other. And so it's just very
*  difficult for human to keep all that in mind. So if you're going to clean the data, you still have
*  to run the simulations to make sure that whichever candidates you're training are actually good.
*  The other problem is that the information that the manufacturers are getting is not sufficient
*  to do this. The manufacturers basically get, you can imagine this like a photo. Like if you're
*  developing film, you get a mask, a set of masks that shows you how to edge copper on all the
*  different layers of the board and then which components to glue down. But that doesn't actually
*  tell you what signals are happening throughout the board. And you need to know that to evaluate the
*  physics. So I mean, we could generate our own data by just self play or like every time we find a
*  good candidate, save it in a database, then train the diffusion model to just recreate those. I
*  think that's valid. But the point is that you still have to kind of come up with those data points
*  that you have verified from physics first principles are actually good designs.
*  Yeah, that's interesting. I feel like there's some way in which the noise sort of cancels out.
*  No doubt that in and I'm just kind of porting my intuitions from other domains of AI here,
*  but certainly no doubt that people do spend a lot of time curating data and going for quality. But
*  also it does seem that the models are pretty tolerant to at least some amount of kind of
*  wrong stuff in the data. And I guess it kind of regularizes out in the training process,
*  one hopes. And in practice, it does seem to work. I don't know if you think that it's just like
*  fundamentally not going to work in this case, but it seems like more your motivation, if I
*  understand correctly, is like, it's more about you want to get to superhuman and you think that the
*  reinforcement learning is obviously like the proven path to get there. And that argument
*  definitely makes a lot of sense to me. What do you think is the timeline to superhuman circuit
*  board designs? What would keep you from going faster toward that superhuman board design future?
*  Yeah, I mean, in my perspective, the bottleneck is talent, right? Finding really great people
*  to work on this kind of problem is the hard part. It's you have so many different aspects of this
*  that need to be really amazing, right? You need to have amazing people who are expert at neural nets,
*  expert at cutting edge reinforcement learning methods. You can't just grab the latest thing
*  and apply it and hope for the best. There's a lot more nuance to this. But also on the C++ side,
*  the CUDA side, the physics side, all of those things have to come together. The timeline,
*  I can't predict it exactly. Maybe for small boards, we're a few years away. Maybe for
*  something like a motherboard, we're five years away. But I'm guessing.
*  Yeah, my crystal ball also gets very foggy more than a couple months out.
*  As it should.
*  In terms of the kind of big problems that you need to solve that you're like, maybe not sure
*  how you're going to solve or that you need the talent to come join the company to be able to
*  get over certain humps. I often feel like when I talk to people, especially those in research,
*  and maybe you may say, well, that's the difference is that it's research versus actual
*  engineering. But I often feel like I get the sense that a lot of things are working,
*  a very high percentage of things are working and that a lot of times multiple different
*  approaches probably could have worked. It seems like just in general, we've hit on a couple of
*  architectures that are really working, but it seems like there's a lot more where that came from
*  and presumably we'll be discovering more and more all the time. Is there something that you're
*  legitimately not sure if it's going to work or really have no idea how you will make it work?
*  Or does it feel like the kind of thing where, of course, there's going to be work and optimization
*  and making it run faster and all that kind of stuff, but basically it feels like you're going
*  to... Is there a sheer face of a mountain that you have to scale vertically or is it kind of
*  graduated stairs that you're pretty confident you can climb one by one?
*  I'm confident in the letter. This is 100% a solvable problem. Given enough time,
*  I'm confident we'll solve it. The nice thing about this problem is there's a lot of steps
*  you can take. With something like self-driving, you kind of have a do or die. Either you're
*  confident you're not going to crash or you're not. And of course, there's still gradations,
*  but the stakes are really high. With us, we have a lot of checkpoints along the way. We have
*  checkpoints in terms of complexity and size of board. We have checkpoints in terms of the
*  physics that we can solve. We have checkpoints in terms of the ambition to be significantly better
*  than humans that can come over time. And with those kinds of stairs ahead of you, you can treat
*  each one as, okay, now it's going to make this 20% better, 20% better, 20% better, 20% better,
*  and let it compound over time. I don't see anything fundamentally about this problem that is
*  unsolvable in any way. It's going to be hard. Don't get me wrong. It's going to take a lot of
*  people. It's going to take a lot of effort, but there's nothing about this that seems unsolvable
*  in any way. Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Hey all, Eric Torenberg here. I'm hearing more and more that founders want to get profitable
*  and do more with less, especially with engineering. Listen, I love your 30-year-old ex-fang senior
*  software engineer as much as the next guy, but honestly, I can't afford them anymore. Founders
*  everywhere are trying to turn to global talent, but boy, is it a hassle to do at scale from
*  sourcing to interviewing to on the ground operations and management. That's why I teamed up with Sean
*  Lanahan, who's been building engineering teams in Vietnam at a very high level for over five years
*  to help you access global engineering without the headache. Squaad, Sean's new company, takes care
*  of sourcing, legal compliance, and local HR for global talent so you don't have to. With teams
*  across Asia and South America, we can cover you no matter which time zone you operate in.
*  Their engineers follow your process and use your tools. They work with React, Next.js,
*  or your favorite front-end frameworks. And on the back end, they're experts at Node, Python,
*  Java, and anything under the sun. Full disclosure, it's going to cost more than the random person
*  you found on Upwork that's doing two hours of work per week but billing you for 40. But you'll get
*  premium quality at a fraction of the typical cost. Our engineers are vetted top 1% talent and actually
*  working hard for you every day. Increase your velocity without amping up burn. Head to
*  choose squaad.com and mention Turpentine to skip the wait list. Omniki uses generative AI to enable
*  you to launch hundreds of thousands of ad iterations that actually work, customized across all platforms
*  with a click of a button. I believe in Omniki so much that I invested in it and I recommend you use
*  it too. Use Cogrev to get a 10% discount. When you hit that mature phase where we now have
*  superhuman circuit board design, what does that look like to somebody like me? Can I just show
*  up and say, hey, I'm making a talking stuffed animal and how ignorant can I be and still
*  get a board out? Because it's like today to even specify what you want is sort of an expert
*  problem. What do you see the sort of independent entrepreneur tinkerer kind of person who like
*  has a product in mind, knows literally nothing. Do they talk to a language model and work their
*  way towards specifications and then put specifications into your system? What's that
*  sort of future state round trip look like? Yeah, sure. So with us, like we're focused
*  explicitly on layout, which is kind of one of two problems, right? To give you an analogy to hang on
*  to, think of creating a schematic for a circuit board as writing code, right? Like a schematic
*  literally looks like a block diagram with inputs, logic in the middle and outputs, and it's entirely
*  kind of logical and abstract. You're just communicating to other engineers what the inputs,
*  outputs, and functionality of the board will be. Layout is like compiling your code, right? Like
*  how do you actually make something physical that takes that schematic or takes that code and like
*  actually makes the atoms of the world do that, right? So we're very specifically targeting the
*  layout portion because we think a compiler should exist for electronics and it just doesn't.
*  The nice thing about that is that a lot of the benefits that we now have because compilers
*  exist in software, I think are going to happen and are going to answer your question in electronics,
*  right? So compilers eventually led to higher level languages, eventually led to things like Python,
*  eventually led to large language models that allow you to write the Python and automate the
*  whole thing. We will eventually move up that stack and look at schematic and how to make that
*  piece easier so you don't have to learn how to write C++, that you could learn how to write
*  Python or maybe even just deal with block diagrams and make a circuit board.
*  Yeah, that's really interesting. It reminds me a lot of, we just did an episode on this tiny GPU
*  project where a young guy set out to design his own GPU from scratch in two weeks and ended up
*  taking him four, which was pretty remarkable. And a big part of why that's possible, I mean,
*  it's still quite an accomplishment in my view, but a big part of why that's possible is that
*  the sort of equivalent of the layout compiler does exist. And so he was able to kind of get to that
*  stage and be able to feed it into an existing system that could do that sort of gnarly work for
*  him. But yeah, that's helpful. But just zooming back out to the benchmark portfolio more broadly,
*  what would you say here are kind of like the patterns that are common across the portfolio?
*  What investments have you guys made that sort of have a very different pattern in terms of
*  what part of the market they're going after first that are maybe in or not in this classically
*  disruptive mode? And I guess broadly, how do I make money in AI? Yeah, that is the right question.
*  I'm very bullish because I think the overall, like we want to be in areas where there's lots
*  of disruption and lots of things changing. That creates the kind of primordial soup for there to
*  be like new big things created. So it's really valuable in that way. And we've seen that. And
*  there's always a lot of crap that gets created and a bunch of stuff that doesn't work. But there are
*  a bunch of good things that get created in the process and it's all about finding them.
*  Really loosely, I think you kind of have in AI right now, it feels to me like there's three big
*  categories of companies. There's a foundational model companies that are like, they're building
*  foundational models. They have some techniques around it. They have proprietary data. Maybe they
*  have other things that they're using and they're trying to do something really special there.
*  Then there's a set of like infrastructure companies in the next category. I'm on the
*  board of Cerebris, which we invested in in 2016. That's an AI chip and systems company
*  that's focused on training. But you have Grok. I'm also on the board of Fireworks, which is an
*  inference provider. And there's a bunch of things where we're also invested in this. So there's
*  quite a few in that category too, which are their infrastructure, which is enabling some of the
*  other stuff that's happening in the ecosystem. That's been a pretty fruitful area. I think those
*  companies have done well. They've gotten a revenue quickly and so forth. And then the third category
*  are companies like Serges, like Quilter, which are vertical applications of AI. So they're applying AI
*  to try to do something. And we see those for lawyers, we see them for doctors, we see them
*  for accountants. We obviously printed circuit board design. So there's just like a bunch of those
*  things too. And each of those three categories, which is very abstract and loose and they're all
*  kind of different. They have a set of really big opportunities and really big problems.
*  I would say the foundational models are incredibly expensive to develop.
*  They are extremely quickly depreciating. I said this before, I think they're the fastest
*  depreciating asset in the history of humankind, which is like you build one, you spend $150 million
*  on it. And six months later, someone can build the same thing for $5 million. That's not historically
*  a good way to make money with venture capital. It's just like that money tends to get incinerated
*  and then someone has something alternative. And we'll see, I could be totally wrong on that. Maybe
*  someone will build something that defeats it. But the general purpose models have proven to be really
*  expensive and depreciate very quickly what is cutting edge. The infrastructure companies have
*  done pretty well in a bunch of ways. They have real business opportunity. They're enabling a
*  bunch of things. The question always exists with them, which is do those problems exist
*  for very long? To some degree, a lot of AI development is where software development was
*  like circa, I don't know, 2002 in terms of the tool sets available and the abstractions that
*  people are working with. And so some of the things that people are solving, I'm just not sure that
*  they're going to be around for a long time. And so that's a potential real challenge there. But
*  What do you have in mind there? Are you talking like LLM observability type?
*  Yeah, that's a great example. That's a great example, which is just like, is the LLM observability
*  thing a thing? It's a thing today. I don't know if it's a thing long term. Maybe not. We have to
*  think through it. But that's a pretty challenging, that could be a potentially challenging area.
*  That'd be one that we think about a lot. And then vertical stuff has proven to be
*  the fastest revenue traction. Some of the revenue scale of the vertical companies has been insane.
*  But the common criticisms of are there any moats or barriers to entry?
*  If you can build a company very quickly in three months or six months and get something out to
*  people- Weekend hackathon for that matter. Yeah, weekend hackathon. Then that also means the 10
*  other competitors are going to do that. And do you end up with something durable there or not?
*  And I think we just don't know in a bunch of cases. You have to have a theory of it. In the
*  case of looking at Quilter or Benchmark Investment in Sierra or some of these others, I would say
*  we have a view, a belief that there's something durable there that will be built and compound
*  over time, even though they got quick traction. And so I think that's just something that we have
*  to look at. And there's a lot of value. This is what's cool about what's happening right now,
*  is there's lots of traction. There's lots of really interesting ideas in all of these categories.
*  And obviously amazing people working on them, but we got to figure it out. And so that's how I've
*  been thinking about it. I'd also say there's this other thing that's really interesting to me,
*  where a lot of the AI work has happened with researchers. You hear it all the time. This is
*  the researcher, their PhDs. They're doing that. And who's telling me this? I forget. One entrepreneur
*  was telling me this. It was like, you get this. So the researchers are writing something. It works.
*  It kind of works in a research context, which is a proof of context, proof of concept or experiment.
*  And then they take that code and they try to scale it in production. And it's, holy shit,
*  that's not good. That doesn't work. It's not written for that or whatever. And this entrepreneur
*  said, she's, I have a rule when it comes to code written by researchers. And I think she said,
*  she was just like, it's just RM star. There's this bridge and divide, which is quite between
*  research and proving something out conceptually and actually like turning that into shipping
*  product that can scale and work and be iterated on. And that's a divide that just didn't exist in
*  software development, at least in my adult lifetime. Maybe it existed in software development,
*  back in databases in the seventies and eighties. But I don't know enough if it did or not, but it's
*  been like, so that's when I say that the stack maturity, the kind of stuff that people have to do
*  to work with PyTorch today or work with CUDA today or something like that, that's just not something
*  that software developers had to deal with for at least 20 years.
*  Soterios Johnson Yeah, that reminds me of comments I heard Demis
*  Osavis make about why they have taken this step now of merging DeepMind into Google proper after
*  so many years of kind of holding it out as its own thing. He basically just said, we're now at the
*  point where we're not done with research, but certainly a lot of the research has been done.
*  And now it's like becoming the bridge to engineering that is a huge challenge. And that's
*  where they feel like the time is right. Soterios Johnson
*  And it's more of everything. We do want to continue to do novel research and push the
*  limits of it. But as we try to bring this stuff into real applications to benefit humanity,
*  we have to engineer it. And that's its own thing. It's not so simple, it turns out.
*  Soterios Johnson I know we're just about out of time with
*  you guys today. Do you have any kind of call for startups, anything that you wish somebody had
*  brought you that you haven't seen or haven't been able to find yet?
*  Soterios Johnson I have this thing that if a venture capitalist has the idea,
*  with very few exceptions, like maybe Mike Spicer or someone else like that can pull it off. But
*  if the venture capitalist has an idea, that's a bad situation because this is not what we're,
*  to the idea-maze point where we started, that is not our job, nor is the thing that we are
*  generally good at. Look, I would say I continue to be really excited. I think we have a ton of
*  companies across the board, at least in terms of the infrastructure companies and the vertical
*  applications that are super interesting. I would love to meet amazing people who have been working
*  on ideas or thinking about something for a long period of time and are obsessed with it. And that's
*  a very broad remit, but our job is to be involved in the best companies as early as possible.
*  And so that's what we want to do.
*  Mad Fientist Yeah, I hear that. With as fast as things are
*  moving today, there's really no substitute for obsession.
*  Soterios Johnson Yeah, totally.
*  Mad Fientist All right, great. Well, this has been a lot of fun, guys.
*  Sergey Nestorenko, founder and CEO of Quilter, Eric Vishria, general partner at Benchmark. Thank
*  you both for being part of the Cognitive Revolution.
*  Thank you so much.
*  Soterios Johnson Thank you, Nathan.
*  Mad Fientist It is both energizing and enlightening to hear why people listen and learn what they
*  value about the show. So please don't hesitate to reach out via email at tcr at turpentine.co,
*  or you can DM me on the social media platform of your choice.

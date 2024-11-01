---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 3416s
Video Keywords: []
Video Views: 553
Video Rating: None
Video Description: In this episode from @AutopilotwithWillSummerlin  Sergiy Nesterenko, founder of Quilter (backed by Benchmark), discusses designing PCB circuitboards end-to-end using reinforcement learning. "Autopilot" host Will Summerlin and Nesterenko cover how current PCB boards are designed and how Quilter’s tech stack enables faster board design, what better circuit boards enable in the future, their GTM and where they are seeing most market pull right now, and much more.

Subscribe to @AutopilotwithWillSummerlin 
- Spotify: https://open.spotify.com/show/6YQZkKHN7EP2yWedAvSxBC?si=18377c69a2804333&nd=1&dlsi=18fee5e95b284d02
- Apple: https://podcasts.apple.com/us/podcast/autopilot-with-will-summerlin/id173816383

Check out Nathan's new chatbot on www.cognitiverevolution.ai
--
SPONSORS:

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Plumb is a no-code AI app builder designed for product teams who care about quality and speed. What is taking you weeks to hand-code today can be done confidently in hours. Check out https://bit.ly/PlumbTCR for early access.

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

--
LINKS:

Quilter: https://www.quilter.ai/
Autopilot Ventures: https://www.apv.vc/
--

X/SOCIAL:
@labenz (Nathan)
@WSummerlinAI (Will)
@sergiynest (Sergiy)
@quilterai (Quilter)

--
TIMESTAMPS:
(00:00) Intro & Sergiy’s Background
(04:31) What Sergiy learned from SpaceX
(05:53) Founding thesis of Quilter and Quilter’s journey
(06:57) Where would one find circuit boards?
(08:11) What is the process of designing a circuit board?
(09:39) Design process today with Quilter
(14:34) Sponsor: Omneky
(16:01) Quilter’s thesis and designing more complex circuits
(18:25) How much are humans currently paid for board design
(19:41) Labour dynamics in board design
(20:30) Do most companies have board designers in house?
(21:14) Incentive structure
(22:44) What does a high performance circuit board look like vs low performance?
(26:37) Quilter’s technology stack
(29:15) Sponsor: Plumb | Squad
(31:15) How Quilter can grow with scale?
(33:50) Where is circuit manufacturing happening
(37:17) What other parts of knowledge work can be solved with reinforcement learning
(41:03) GTM and who Quilter is selling to
(42:48) Pricing
(44:04) Where Quilter is seeing the most market pull right now
(45:21) What makes Quilter an exciting company to work at or invest
(47:14) The effects of closed research in private companies for the industry
(49:25) Open source vs closed source
(51:14) What Sergiy would advise to himself in his early founder
(53:59) What drew Sergiy to working with Benchmark
(56:19) Wrap
---

# Automating Circuit Board Design Using Reinforcement Learning w Sergiy Nesterenko, Founder of Quilter
**Cognitive Revolution:** [April 25, 2024](https://www.youtube.com/watch?v=0M_0xhb8Uyk)
*  Hello and welcome to the cognitive revolution where we interview visionary researchers,
*  entrepreneurs and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life and society in the coming years.
*  I'm Nathan Labenz joined by my co-host Eric Thornburg.
*  Hello and welcome back to the cognitive revolution.
*  Today I'm pleased to introduce Autopilot, a new podcast hosted by Will Summerlin,
*  which explores the past, present and future of AI and automation with expert guests.
*  Will is the founder and managing partner at Autopilot BC and before that he covered software
*  and artificial intelligence at ARK Invest. He was also previously the founder and CEO of PIN AI,
*  a venture-backed startup that developed an AI-powered security platform.
*  In this episode, Will interviews Sergey Nestorenko, the founder and CEO of Quilter,
*  a startup that uses reinforcement learning to automate the complex process of designing
*  printed circuit boards. As an electronics engineer at SpaceX,
*  Sergey experienced firsthand the challenges of circuit board design.
*  A single board can take weeks or months to design and validate, issues and errors are common,
*  and iteration involves the production of physical prototypes, which can be frustratingly slow.
*  With Quilter, however, Sergey aims to make circuit board design as fast and seamless
*  as compiling code. In this conversation, Will and Sergey dive deep into circuit board design
*  as it exists today, tell the founding story and technology behind Quilter,
*  and consider both how to earn trust with AI-created designs and how to navigate the labor
*  dynamics of an industry poised for disruption. While Sergey is quite upfront about the fact
*  that Quilter can only handle relatively basic designs today, even this suggests major problems.
*  In addition, Quilter is also very clear about the major productivity gains and changes to the
*  nature of jobs. And more importantly, if Quilter achieves its vision of superhuman circuit board
*  design performance, which given the success of other narrow reinforcement learning systems,
*  seems very plausible to me, we'll see a much bigger impact on employment in years to come.
*  For more fascinating looks at critical but often neglected domains and the impact that
*  AI automation is and will continue to make on them, subscribe to Autopilot with Will
*  and Sergey. And of course, we here at the Cognitive Revolution always welcome your feedback.
*  Right now on our website, cognitiverevolution.ai, you can chat with my personal AI clone,
*  which is powered by Delphi AI and trained on all Cognitive Revolution episodes.
*  Feel free to ask it any questions you have, give it a guest suggestion, or just tell us
*  something that we got wrong. I've had a couple good experiences with it, but I'm really curious
*  to see how it works for others. And finally for now, remember that I am helping a few different
*  companies hire AI engineers. So if you're looking for a new AI engineering role, you can go ahead
*  and DM the real me on the social media network of your choice. With that, here's Sergey Nestorinko
*  of Quilter on the AI automation of circuit board design from the new podcast Autopilot with Will
*  Summerlin. Welcome to Autopilot, a podcast where we discuss the past, present and future of AI and
*  automation. We explore how AI is creating and disrupting large industries and conversations
*  with top founders, investors and historians. I'm your host, Will Summerlin. Let's dive in.
*  Sergey, thank you for joining us. You are the founder and CEO of Quilter. You just raised a
*  $10 million round led by Benchmark. So congratulations on doing that. In a little bit,
*  we'll get into PCB design and how it's broken and how you guys are fixing it. But for context,
*  let's start with you and the founding story. What were you doing before and why did you found Quilter?
*  Yeah, Will, thanks for having me. It's great to be here. My first job out of college was at SpaceX.
*  I was responsible for Falcon 9 and Falcon Heavy's second stage in high radiation environments.
*  Basically, rocket when you go to space don't die. That was my job, which involved a whole
*  lot of electronics. So the founding story of Quilter actually was largely inspired from that,
*  just suffering the pain of developing hardware and all the supporting hardware to develop hardware
*  at SpaceX. If we go back to SpaceX for a second, we'll get into what you're working on
*  now. What lessons did you learn? SpaceX is obviously an incredible company. It solves
*  really hard problems. It seems to have a relatively intense culture. I'm curious what you took away
*  from that culture that you're bringing over to Quilter. Yeah. Will, there's a lot. I think on a
*  daily basis, if you ask the awesome team that I work with, I'll probably cite some learning from
*  SpaceX almost every single day. Off the top of my head, I think maybe the biggest one is just
*  how important it is to have something exciting to work on. The fact that SpaceX would come in
*  the door and it's like, all right, we're actually trying to go to Mars. That's not a joke. We have
*  to actually make decisions that eventually get us there. That's exciting. It makes recruiting
*  really easy. It makes showing up at work really fun. It makes you work hard at your current project
*  to get another cool project in the future. I've seen some of that here. The team at Quilter is
*  awesome and everybody shows up with a ton of energy every day. We've been lucky to recruit
*  amazing talent. There's just something wonderful about working on something hard, something
*  important, something cool. That's the biggest one. I don't know. It's probably dozens of others.
*  It's like the classic missionary versus mercenary argument, right? The missionaries will be
*  intrinsically motivated. Yeah. I've never worked in a context where that wasn't the kind of the
*  drive-in case, but from my experience, that certainly resonates. When you started to think
*  about founding Quilter, what was the founding thesis? What problem were you trying to attack?
*  When we found a Quilter, it actually wasn't focused at all on circuit boards, believe it or not.
*  This was 2019. It was a slightly different capital environment than it is today.
*  Kind of got the opportunity to meet an investor. There was Michael Deering at Harrison Metal at the
*  time and just talk about what it might be like to start a company, what we might do.
*  We first actually headed in the direction of making low-cost sensors for manufacturing.
*  That was the first idea and thesis. Spent a few months thinking about that direction. It wasn't a
*  good idea, at least not for us. We were too late to it, I think. Shifted to doing analysis on those
*  sensors. That turned out not to be a great idea. Then shifted to reliability analysis on circuit
*  boards. Then I started thinking, why do analysis if I can just design it correctly in the first
*  place? It probably was almost a whole year of this wilderness period of, what am I actually
*  going to do with this company before we landed on creating circuit boards?
*  When we think about circuit boards, maybe we can start at a fifth grade level and then we can dig
*  it a little bit deeper and get more advanced. If you're explaining this to me like I'm a fifth
*  grader, what are circuit boards? I started ripping open appliances in my house. Where would I find
*  them? First of all, circuit boards are just an important part of electronics, which is typically
*  the thing that connects all the different pieces together and makes them come to life.
*  Actually, I guess I have some examples right here that I can just physically show.
*  Circuit board is this rigid piece of fiberglass and copper that connects a bunch of chips.
*  These chips on a piece of electronics are the things that perform these different functions,
*  do some processing, store some memory, have some power. The circuit board glues them together.
*  It's a passive element and it just is meant to connect them logically.
*  When you're taking something apart, you'll find them just about everywhere. Obviously,
*  something like your computer or your TV is probably primarily a circuit board.
*  You'll see it in your light bulb. You'll see it in the control center of your stove or whatever else.
*  Anything that has any amount of sensing and actuation will probably have electronics and
*  therefore circuit boards. Does every electronic have its own unique circuit board design? I would
*  assume that my laptop has a different circuit board design than my iPhone. Yeah, that's a really good
*  question. In general, yes, very much so. The thing that is fixed and hard to create and therefore
*  is reused between a lot of products are the chips. In general, creating a new chip is a
*  multi-million dollar proposition. It's very difficult to go create a unique chip for a unique
*  product. The circuit board is kind of the opposite. You can take all of these chips
*  that already exist, glue them together in some new way, and make a new product.
*  Definitely, the board in your iPhone is different than the one in your Android,
*  different than the one in your computer, so on and so forth with relatively few exceptions.
*  Is the complexity of the circuit board correlated with the sophistication of the device? An iPhone
*  would have a much more sophisticated circuit board than an alarm clock.
*  Oh, absolutely. Yeah, the sophistication of a circuit board or the difficulty scales with roughly
*  two things. One is just the combinatorial complexity. So how many things are there on that
*  board? How densely packed are they? And then the other is physics-related. So does the board have a
*  lot of very high-speed signals which are difficult to work with, or does it have a lot of very high
*  power signals which create heat that you have to manage? And yes, of course, the difference between
*  an NVIDIA video card and an alarm clock is night and day.
*  That makes sense. Maybe we can shift into the design phase of this.
*  Without quilters, say we're using the traditional methods of human knowledge work labor, how does
*  one go about designing a circuit board? What would I be optimizing for if I were to design one?
*  And what tools would I be using?
*  Yeah, so I like to think of the process of designing a circuit board in three major steps.
*  And I often like to make the analogy to software because more people I think have written some
*  code than have designed a circuit board. So I find that helpful. So the first step to designing a
*  circuit board is to create what's called a circuit schematic. So if you've never seen one before,
*  it looks a lot like a block diagram or a flow chart. So you're kind of in a relatively human
*  readable language trying to explain what are the inputs, outputs and function in the middle
*  that the board will do. So you might say I have a connector, I have a processor, I have some memory,
*  I have a radio antenna, and then I drive that antenna or something like that. You can think
*  of that a lot like writing code. So writing Python, this kind of human readable representation is a
*  lot like creating a schematic. That's the first step. The second step is to convert that schematic
*  into kind of a set of blueprints that a manufacturer can actually use to turn into a real physical
*  design. Once you have the schematic, you have to kind of explain to the manufacturer exactly how
*  to arrange copper, fiberglass, solder components together to make that schematic real. And so I
*  think of that kind of like compiling code. That's the second step. And then of course, the last step
*  is to take that blueprint, it's called a layout, send it to a manufacturer, manufacturer creates it,
*  you get the board on your desk, and usually you figure out that you messed something up and you
*  try all over again. How long does it normally take to go from step one to having the manufacturer
*  actually produce something? Is that typically like a week long period or a year long period?
*  Yeah, it depends very much on the board you're designing. So once you finish the schematic
*  doing this process called layout, it can be a couple of hours for something really, really
*  simple with a few components, or it can be many months. If you're thinking of like a Starlink
*  Contanna or an iPhone motherboard, you're easily looking at two, three months of manual labor to
*  make that design happen. Ironically, the process of doing layout is much faster in a lot of cases
*  than manufacturing itself. In many cases, especially if you're willing to pay for it,
*  once you have a design, you can have a prototype on your desk within 24 hours,
*  or even just a few days if you're willing to pay for fast shipping from China. But the process
*  of doing layout varies between, you know, typically it's a few days, but it can be a few months.
*  Is there some level of like validating the design before you go to manufacturing,
*  not only to make sure that you know the system works, but also to make sure that it's manufacturable?
*  Yeah, yeah, that's a good question. So there is some amount of this. Yes. So in general,
*  basic questions about manufacturing are pretty well handled today. You know, so one of the first
*  things that you're doing when you're creating a board is you're deciding where exactly do all of
*  the chips go? How do I make sure that none of them are colliding? And then how do I connect all of
*  them with copper on the board? So making the basic checks around, hey, nothing's colliding,
*  all the chips are connected the way that your schematic said, and all of the connections are
*  far enough apart that like the copper doesn't bleed into itself because of etching imperfections,
*  stuff like that. That's called the design rule check or DRC. And it runs very quickly in any
*  of these tools that you use to design boards. That's not so bad. The hard part starts to show
*  up when you start to think about more complex interactions. So I'll give you an example.
*  One of the difficult things to understand in circuit board design is this notion called
*  crosstalk. So if you have two connections between chips that are not tied to each other, not actually
*  physically touching, they can still couple a lot of energy between each other. So you'll have a
*  signal on this wire A, that signal because it's a wave in electromagnetics can jump over to the
*  wire B. And in most extreme cases, you can actually couple more energy to the other wire than the one
*  that you intended it for. So this can very quickly ruin your board from totally from working at all.
*  And so you have as a designer, you know, potentially hundreds or thousands of these
*  possible imperfections to consider. And in general, it's very difficult to make sure you've
*  gotten them all right. Designers typically use, you know, rules of thumb to design boards, quote
*  unquote, correctly, as they make an attempt at this. There are some simulations that you might run
*  on cases where you know there will be issues. But there is not like a one click button that
*  definitely gives you a sure thumbs up that you are completely confident it's going to work.
*  And practically speaking, it almost never does work. You almost always find something that you
*  have to go back and redesign for. Hey, we'll continue our interview in a moment after a word
*  from our sponsors. The brave search API brings affordable developer access to the brave search
*  index, an independent index of the web with over 20 billion web pages. So what makes the brave search
*  index stand out? One, it's entirely independent and built from scratch. That means no big tech
*  biases or extortionate prices. Two, it's built on real page visits from actual humans collected
*  anonymously, of course, which filters out tons of junk data. And three, the index is refreshed with
*  tens of millions of pages daily. So it always has accurate up to date information. The brave search
*  API can be used to assemble a data set to train your AI models and help with retrieval augmentation
*  at the time of inference, all while remaining affordable with developer first pricing.
*  Integrating the brave search API into your workflow translates to more ethical data
*  sourcing and more human representative data sets. Try the brave search API for free for up to 2000
*  queries per month at brave.com slash API. Omniki uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work customized across all platforms
*  with a click of a button. I believe in Omniki so much that I invested in it, and I recommend you use
*  it to use cog rev to get a 10% discount. So if I'm going to replay this a little bit,
*  the design process today without Quilter is almost based on like tribal knowledge that
*  sits within a designer's head. And it's a relatively manual process to sort of solve the puzzle.
*  What is the designer's life like with Quilter? How much of that do you guys automate today? And
*  how do you think that's going to evolve over the next five years? Yeah, so the principle of what
*  we're trying to do is to completely eliminate layout altogether. We want to get to the point
*  where doing a PCB layout is like compiling code, where, you know, in practice, pretty much in all
*  cases, people just click a button and it runs. Now, of course, that's much easier said than done.
*  And so that's an easy thing to say, but very, very difficult thing to do. So with Quilter,
*  for the boards that are kind of in our scope today, which I could talk about in a second,
*  that is very much the process, right? The designer will finish their schematic,
*  they will open up the beginnings of their board file in order to enter some constraints. So,
*  for example, you might have very physical requirements on how big the board can be,
*  where connectors go, where buttons go, where a screen might go. And then everything else that
*  you need to do, you simply leave off the board in the design file, upload it to Quilter, and then
*  Quilter drives it all the way home straight to something you could submit to a manufacturer.
*  But of course, it should make it clear that it's limited what kinds of boards we can do,
*  right? If you give us a computer motherboard or a video card today, we can't do it. And so you're
*  just not going to get a good result, you probably won't even get a completed result. But for boards
*  that are sort of within our parameters, we've done this many times and it works just fine.
*  Is the thesis that over time, you'll sort of move up the stack of complexity
*  and get to a point where you can design a board for a laptop? Or is the market big enough at the
*  bottom? Yeah, I mean, I think that there is a significant market at the kind of
*  bottom of the complexity chain for sure. I mean, even quote unquote, easy boards where the physics
*  isn't that complicated, they still can take a week to do or two weeks to do by hand. So there's still
*  a very, very significant value to eliminating that work. And even more importantly, reducing that
*  latency of your product iteration. But we of course, want to be able to do all of them.
*  Because we eventually can unlock the potential to design better boards than humans can.
*  And that opens up a whole new set of considerations.
*  How much are humans currently paid? Do you have any sort of rough idea of the current labor spend
*  on board design? Yeah, totally. So on average, this is actually a profession. So there are people who
*  specialize in this specific task of doing PCB layout. I believe the median salary in this profession
*  is about 100,000 to $110,000 per year. And it's overall, it's not just those people who do this
*  task. You know, people who almost anybody who designs electronics eventually has to do their
*  own layouts and really professional PCB layout folks are typically reserved for designs that
*  are really complicated and really mission critical. So again, thinking back to SpaceX, right, we had,
*  you know, a team of a few dozen people who would do PCB layout, but they could only support, you
*  know, flight computers and, you know, the intense radios and everything like that. Even for someone
*  like in a position, you know, like myself doing radiation testing, we had to do our own designs
*  because that team just simply couldn't support us. And, you know, it could easily take up half
*  of your time designing these kinds of boards. So in total, you know, we estimate that there are,
*  you know, it's hard to get a precise number, but, you know, 20, 30, 40, $50 billion a year of labor
*  being spent on this task. What are the labor dynamics like? Are there labor shortages? Is there
*  oversupply of board designers? Yeah, I think there's actually a drastic
*  undersupply of board designers and electrical engineers in general. It's definitely a big
*  problem. I think what you're seeing is that, and I don't have numbers for this to make it really
*  concrete, but I think what you're seeing is that a lot of the young engineering talent nowadays is
*  choosing to go into software and AI and robotics, and fewer are going into electrical engineering
*  and specifically these skills of kind of intense PCB design. So, I mean, just from my own experience
*  in SpaceX, right, I wish we had more support for doing layout with that central layout team,
*  because then you don't have these folks, you know, these adjacent roles doing that same task.
*  I think there's a significant shortage of this kind of skill out there.
*  SpaceX is somewhat unique in terms of vertical integration. Do most companies have designers
*  in-house or are they third party services that people typically rely on or companies typically
*  rely on? Well, so I think most companies that develop hardware have their own internal
*  electrical engineering talent. That doesn't mean that they necessarily have their own
*  layout folks. That can depend case by case. But even a company that is, you know, five or ten
*  people developing IoT products will probably have a few engineers doing the PCB design, the electronics
*  design, and either they will choose to have someone do the layouts or they will pay someone
*  externally to do the layouts for them. Got it. That makes sense. Maybe we can talk about the
*  incentive structure a little bit. If I'm a hardware company and I need to design a circuit board,
*  what do I care about? Do I care about the time it takes to design it, the cost to design it,
*  the efficiency of the system? Like, what are the incentives that I really care about?
*  Yeah, I think that really depends. That really depends on who you are within the company and
*  the application. So we can maybe talk about a few different cases. So if you are designing
*  an early prototype for a board, that's probably the most important thing is the speed. What's
*  the fastest you can get it on your desk and start playing with it? And just to give some perspective
*  to this, for every one flight computer, you're probably going to design tens or hundreds of
*  early prototypes, validating little pieces of the design, validating memory chips and power chips,
*  and also creating support equipment to fully test it. On the exact opposite extreme,
*  if you're Apple and you're designing a motherboard for the iPhone, you probably care most about
*  size, performance, and maybe to some extent cost. I mean, obviously to an extent cost,
*  but maybe that's not the thing you push down the most. So it really depends whether you're
*  building kind of a one-off prototype, in which case you think speed is very important. And of
*  course it has to work. Or if you're building a mass production unit, in which case reliability,
*  cost, form factor, maybe even aesthetic are the most important things.
*  Maybe we can double down on performance. What does a well-designed high performance circuit
*  board look like versus a poorly designed low performance? Yeah, so the simplest way to look
*  at this is that when you just look at the raw PCB itself, right? So when you've got a schematic
*  and it does some function, like maybe it's an Nvidia video card, right? Some fast processor
*  with fast memory. The job of the circuit board is just to faithfully recreate that schematic.
*  So a poorly designed board is just going to prevent your chip and your memory from working
*  at the speed that they could work at. What you'll find is that if you run them really,
*  really slowly, everything is okay. But then as you turn up the speed of the communication
*  between the memory and the chip, eventually it starts to fail. And of course that's terrible.
*  You don't want to be bottlenecked by the performance of your board. So there's a
*  threshold you have to meet on how good your design is to not ruin the schematic that you design.
*  The other thing is that there's other kind of limitations. So for example,
*  to make a product in the United States, you have to pass FCC testing. You have to make sure that
*  your board doesn't emit radio waves that jam everything else in your house, right? So of
*  course, if you've made a poor design, that's going to happen. And you're not going to be
*  allowed to sell the product. But if you've made a good design, that won't happen. There might be
*  some cases where that's really the ultimate goal is making sure that the board itself is not the
*  bottleneck for your schematic, that it's like the raw chips that you're working with that are the
*  bottleneck for speed or power performance of your design. And if you think about kind of the arc of
*  using some level of AI and automation to design circuit boards, if we start as like trying to get
*  to a point where you're as good as most human designers, the average human designer, and then
*  the end of the arc is like you're better than the best human designer, where are we on that arc? And
*  do you think we'll get to a point within the next five years or so where your system is better than
*  the best human designers? Yeah, I mean, frankly, I don't think we are as good as the average designer
*  on anything kind of physics and density related. Like this problem is very, very difficult. And I
*  don't think we've reached that point yet. I think the only thing that we are significantly better
*  than humans at is just time. So on a board where these physics constraints are not as significant,
*  we can do in an hour would take someone a week to do. But of course, the interesting and difficult
*  parts of this come up when we are as good as or better than most humans at all of the physics
*  things. And I absolutely think that's achievable within five years. You mentioned earlier, like,
*  perhaps we'll be able to do things in the future with better design circuit boards than we have
*  today. What are those things? Like what is sort of like the horizon of interesting problems we can
*  solve with really good circuit board designs that we just don't have today? Yeah, I think like,
*  you know, a really obvious one is cost and size reduction. So one of the things that a designer
*  has to consider is if they sit down to do a design, it's going to take two or three months to do.
*  Their worst fear is being a few weeks away from completion and realizing that the design is not
*  going to close. Like they just simply can't get everything to kind of fit and be set up in a
*  functional way. That would require them to go back and kind of resize the board, for example,
*  or add layers to the board, which could easily add more weeks or even a month or more to their
*  cycle, which is unacceptable. So what you find people doing is making a lot of conservative
*  assumptions, right? You make the boards a little bit bigger than they have to be, you give them
*  more layers than they have to have to use, you know, thicker traces or more copper pools than
*  you might need to use. And so that ultimately results in larger boards that have lower yields
*  to manufacture and are therefore just more expensive. I think that's probably the most
*  obvious thing that could be done to improve boards. And if we kind of dig open the hood
*  a little bit or dig under the hood a little bit, as you guys think about building your technology
*  stack, obviously you're not building on top of like GPT-4. This is a different problem set.
*  Maybe you can talk through the type of machine learning approaches you guys are taking
*  and specifically whether or not you need a lot of proprietary data and how you go about acquiring
*  that data. Yeah, that's a great question. So the best analogy for how we approach this problem
*  is to look at what DeepMind did with AlphaGo. So we use a branch of machine learning called
*  reinforcement learning, where basically you create some sort of game, you create an agent that can
*  play that game and you create some sort of score or reward that tells the agent how well it did
*  at playing that game. So obviously with DeepMind, they did this with the game of Go and famously
*  eventually defeating the world champion at that game. What we're doing is creating quote-unquote
*  the game of circuit board design. We're creating agents that play that game and then the score is
*  physics and manufacturability. So how cheap did you make this board? Is it actually going to work?
*  So on and so forth. That's what tells you whether you won or lost. So the nice thing about reinforcement
*  learning is that one of the ways to approach it is that you don't actually need any external data.
*  This is actually something that's been tried multiple times in this space. A lot of people
*  have this first principles idea of like, let's take a bunch of human design boards, show them
*  as examples to a neural network and try to recreate them. That's not how we approach this
*  problem and that's not what we do. In part because, well, it is actually just difficult to get to
*  really good designs. There's not a GitHub of millions and millions and millions of designs out
*  there. And furthermore, the best designs are locked away at Nvidia, at Apple, at SpaceX,
*  and not an open source. But second of all, I actually think long-term that's the wrong approach.
*  I think that if you focus on learning from human examples, you're likely to peak at roughly human
*  performance, which is actually what happened to DeepMind when they first started playing Go.
*  They looked at a whole bunch of human examples of moves, trained on them, queried the net to make
*  the best human-like move, and they got to like a grand master level, but not a world champion level.
*  The best strategies came from the network trying new things and seeing how they work
*  and remembering them. And I think that's what will eventually lead to superhuman level board designs
*  for Guilter. Yeah, it's like there's all this unexplored solution space outside of where
*  humans have been playing. And if you can explore that, you might find much more efficient designs
*  than what humans know today. Hey, we'll continue our interview in a moment after a word from our
*  sponsors. Today's podcast is brought to you by Plum. Is your product team struggling to keep up
*  with the incredible pace of AI development? Are you tired of spending countless engineering hours
*  just to test out small prompt changes in your product? Thankfully, there's Plum. Build cutting
*  edge AI experiences for your users in a fraction of the time. Say goodbye to the slow, tedious
*  process of hand coding and hello to the future of AI development. Get ahead of your competition
*  and start moving as fast as AI does. Check out useplum.com. That's Plum with a B for early access.
*  Hey all, Eric Torenberg here. I'm hearing more and more that founders want to get profitable
*  and do more with less, especially with engineering. Listen, I love your 30 year old ex-fang senior
*  software engineer as much as the next guy, but honestly, I can't afford them anymore.
*  Founders everywhere are trying to turn to global talent, but boy, is it a hassle to do at scale.
*  From sourcing to interviewing to on the ground operations and management. That's why I teamed
*  up with Sean Lanahan, who's been building engineering teams in Vietnam at a very high
*  level for over five years to help you access global engineering without the headache.
*  SQUAD, Sean's new company, takes care of sourcing, legal compliance, and local HR for global talent
*  so you don't have to. With teams across Asia and South America, we can cover you no matter
*  which time zone you operate in. Their engineers follow your process and use your tools. They work
*  with React, Next.js, or your favorite front end frameworks. And on the back end, they're experts
*  at Node, Python, Java, and anything under the sun. Full disclosure, it's going to cost more than the
*  random person you found on Upwork that's doing two hours of work per week but billing you for 40.
*  But you'll get premium quality at a fraction of the typical cost. Our engineers are vetted top
*  1% talent and actually working hard for you every day. Increase your velocity without amping up burn.
*  Head to choose squad.com and mention Turpentine to skip the wait list.
*  As you think about the advantages of scale in this type of business or this type of product,
*  presumably the more boards you design, the better you get at designing boards and creates more
*  customers, which creates more boards. There's this sort of compounding mode. And I've always
*  thought of compounding modes in AI as a data advantage. If you need proprietary data,
*  the more customers you have, the more data you generate, etc. How does that play out for you
*  guys? Does that compounding mode exist? And as a result of that, do you think you'll get harder
*  to compete with as you scale? Yeah, I definitely think so. So one of the things that's possible
*  for us to do, and this isn't something we currently do, but that I've personally thought about a bit,
*  when you look at any one customer, a lot of their boards and a lot of their designs start
*  to look really similar. So I'll give you one example. At SpaceX, we were forced to use
*  kind of a single relatively small set of components in our library of designs. And it's for good
*  reason. You want to make sure that each part that you're going to put on a vehicle is well
*  screened and understood and has a good supply chain and all that stuff. And yeah, what that
*  kind of means is that when you go to design a new board, you're going to reach into that library
*  for a component you've probably previously used that has already been screened, rather than the
*  10 other alternatives that exist in the market. I mean, even without that, even for an individual
*  designer, you're likely to work with the tool that you already know how to use. So if you're
*  writing code, you're going to reach for a package that you've used before. If you're designing a
*  board, you're going to reach for a chip that you've used before. So there's a potential to make
*  little mini networks for each customer that have gotten good at their designs and only tackle
*  their designs to keep the data kind of safe to them, but then get kind of special precision
*  on the kinds of stuff that they're asking for. I think the other way that Coulter can kind of grow
*  with scale is actually by integrating with manufacturers. I think that one of the other
*  pains that exists today in design is you actually kind of have to go and figure out who's going to
*  manufacture your board first, and then design to their specifications. Whereas if you think about
*  it with code, it's exactly the opposite. You write your code, and then you choose at the end which
*  processor to compile it for. And so as Coulter goes and integrates more manufacturers, gets to
*  know manufacturers, and closes the loop, that's another place where we can benefit from scale of
*  serving manufacturers a lot more designs at once, helping them with their margins, building those
*  relationships, bringing costs down, and eliminating pain for the customer to submit those designs to
*  the manufacturers. If you think about the manufacturing side, is most of the manufacturing done in
*  China today, or is it sort of being distributed into other regions? Yeah, I think it's probably
*  true. So by volume, there's no question about it. By number of unique designs, it's probably still
*  true that China manufactures the most. But there is a significant amount of manufacturers here in
*  the States that do local designs. There's kind of two reasons that folks would choose to manufacture
*  boards in the United States, or primarily two reasons. One might be you might be required to
*  do so. So if you're SpaceX, you can't send your designs to China because of ITAR. The other is
*  latency. So when you design, when you have somebody fab your board on Sure, they can, you know, build
*  it and drive it over the same day, and you can be working on that board. Whereas if you have to fly
*  it over from China, then you're kind of at least limited by shipping. So I don't have an exact
*  number for how many designs are manufactured uniquely in the States versus in China. But
*  the biggest fab in China does about 8,000 unique designs per day. Wow. So it's a lot. That's insane.
*  Is the manufacturing process and I guess the sort of manufacturing layer relatively commoditized,
*  or do different manufacturers like have some proprietary process that is a lot cheaper or a
*  lot more efficient? The answer is kind of both depending on what part of the difficulty scale
*  you're looking at. So if you're thinking of a really simple board with high margins and thick
*  traces and everything like that, sure, every designer can do it. And you know, the margins
*  aren't that high for anyone and so on and so forth. But the different fabs certainly distinguish
*  themselves once you get into special features, right? Once you get into high speed signals with
*  special materials or tolerances or yield, or whether they focus on quick turn or high volume,
*  that's where you start to see some differentiation. When you think about quilter and your ability to
*  sort of automate the design phase, I would assume the process today is like you still go to a
*  manufacturer and they'd ship you a physical board that you can run tests on. Will that be the case
*  in five years or will you guys get good enough where you can run essentially a simulation and
*  all the tests and by the time you get a board back from a manufacturer, it works exactly as expected?
*  Yeah, our goal is definitely to get the board right on the first try. I think that's absolutely
*  achievable. I think that the answer to will this board work or not is in principle computable.
*  I don't think it's easy. I think it's going to take time, but I think it's possible.
*  You know, all we're really talking about here is capturing the process of manufacturing,
*  Maxwell equations, and laws of thermodynamics. There's a lot to do. It's a lot of compute. It's
*  a lot of things to think of, but it is possible and we should do it because I think that the
*  problem with waiting for a board to come back, getting on your desk, finding an issue, fixing it,
*  and resubmitting, that's the thing that takes the most time away from a designer. With code,
*  it's relatively easy to write a bunch of print statements and debug and keep rerunning it.
*  With a board, it's actually very, very hard to figure out what you did wrong.
*  That can take weeks or months or some boards will ship with an issue never figured out.
*  I think there's a lot of value in getting it right the first time if you actually can.
*  You mentioned compute. Are scaling laws here sort of the same as they are in
*  LLMs? The bigger the model, the more compute you use to train it, generally the better the performance?
*  Certainly. Increasing model sizes, increasing compute, creates a better performance,
*  but it's not the only bottleneck. I think in reinforcement learning, you have these three
*  totally different pieces. What is the game that you're playing? What is the agent? What is the
*  score? You can't just invest in a huge agent, but then have a very difficult to play game that's
*  super slow to evaluate and a score that doesn't actually reflect real life. We invest not just in
*  more compute, more model. We invest across all of those kind of pieces.
*  Have you guys been constrained in any way by GPU access or is that not really been an issue?
*  Not at this point. We try to focus on problems where it's not requiring some massive million
*  GPU for three months kind of run or problem. That's very expensive, but also very, very slow to
*  iterate on. There's a surprising amount that you can do in reinforcement learning with a single GPU
*  in a few minutes. One of my favorite demonstrations to show people is that you can train a robot to
*  walk in a simulation in five minutes on a single GPU. Five minutes of training compute?
*  Yeah. This is worth talking about. There's a cool library called Jax, I think coming out of Google,
*  that basically gives you a whole bunch of cool to access for training models, for building models,
*  and so on and so forth. What they've done is they've written a physics engine in that language,
*  so to speak, that basically also evaluates in GPU. You can simulate like a human know it or a
*  hexapod or a cheetah or whatever. This is sort of robot system that needs to walk on a GPU.
*  You can evaluate about 50 million of those episodes, so like taking a thousand steps,
*  roughly speaking, in a matter of a few minutes. Given that that's possible, we try to look for
*  things like that as much as possible because then we're not just hoping for the best with a
*  huge model. We're really getting at, are we using the right model? Do we have a game that's that
*  fast to evaluate? Are we looking at the right things and we can iterate faster and so on and so forth?
*  Outside of circuit board design, what other problems or say domains of human knowledge work
*  do you think could be solved or partially automated with reinforcement learning?
*  That's a good question. I mean, most explicitly, the stuff that I've been thinking about is
*  tangential to circuit board design. There's two other similar problems that look almost exactly
*  like circuit board design, and that's chiplet design and then potentially chip design. Those
*  are really interesting, but we can classify that as electronics design. I'm excited for it in a lot
*  of different cases. I mean, I'd love to see more solutions doing mechanical approaches like this.
*  When you consider something simpler like let's design a fan or a heat sink, right? What's the
*  right way to arrange fins on a heat sink? That's something that could be interesting to do with
*  reinforcement learning. All the way through, can we design a plane? Can we design a wing
*  that is more efficient and has less turbulence and whatever else? These are not something I
*  know anything about, but it would be very, very interesting to explore and study.
*  Yeah. It seems like any sort of like almost like design optimization where you have well-defined
*  constraints, like the laws of physics, you create these outer bounds of constraints and
*  explore a wide range of solutions based within that.
*  100%.
*  That makes sense. As you guys think about go to market and monetizing the product,
*  who were you typically selling to? Is there like a head of electrical engineering inside
*  of a company or is it somebody else? Yeah, that's a really good question.
*  Our current go to market is primarily driven by our technical capabilities.
*  In the five-year future where we can solve any board and do a computer motherboard,
*  sure, there's going to be a head of electrical engineering or a head of PCB design that we can
*  directly approach who's going to see millions of dollars of value for their company for this
*  almost immediately, but we just can't do that yet. We're in this trickier phase of like,
*  where can we actually solve problems today while we build to that future?
*  The most kind of direct interesting segment has actually been what I think of as electrical
*  engineering adjacent roles. I'm thinking of folks who are they required to have a circuit board to
*  do their job, but that is not their primary function. Myself from SpaceX was exactly this
*  kind of example where my primary function was to test electronics and predict radiation effects
*  in flight and make sure that it was all okay, which required me to design a lot of boards,
*  but that wasn't the main thing I was trying to do. For me, being able to automate that piece and
*  just have it work was really attractive and I was not designing the kinds of boards that were so
*  complicated that it couldn't be done. We're seeing interest from folks that are firmware
*  engineers, robotics engineers, automation engineers, test engineers, lots of these kind of
*  tangential roles that are not designing the main Apple motherboard, but are designing the things
*  that are immediately adjacent to it. That makes sense. As you think about kind of pricing and
*  like the long-term pricing model, if you're able to do designs as good or better than humans,
*  do you think about a pricing model that sort of reflects like the human labor costs that you're
*  replacing or do you think about it in a totally different way? Yeah, 100%. I think that we do
*  think about it with the kind of existing way to value this work because there's already an
*  existing budget item, because people are already familiar with it. The way that this is typically
*  done in the space today, if you were to say outsource a layout to an external fabricator,
*  it's done in proportion to the amount of time that it's going to take.
*  So people will take a look at the whole board, count the number of pins or the number of
*  connections that they need to make and charge somewhere between one to ten dollars per pin or
*  one to ten dollars per connection. It kind of depends on where you're doing it, which country
*  and so on and so forth. So that's a budget item and a pricing structure that already exists that
*  we can directly tap into. So maybe at first we'll start out on the cheaper side of things
*  and then over time as we provide more value and more simulation results, then people can
*  we can come up to the more expensive side of that. Yeah, that's how we're thinking about it.
*  Where have you seen the most market pull so far? Is it in companies that are designing,
*  I know you guys are right now focused sort of at the bottom of the pyramid on simpler designs,
*  is that typically like a consumer electronics company? Is it a defense tech company? Like
*  where are you seeing the most market pull right now? Yeah, so the interesting thing is that
*  it's actually less segmented by the vertical of the company and more by who at the company you're
*  talking to. So whether you're SpaceX or a consumer company, you probably have both really,
*  really difficult, intense designs and really, really easy kind of intern could do it type of
*  designs. So that's where this kind of electrical engineering adjacent thinking came from, is that
*  we were just seeing folks who were doing these boards that didn't want to be doing them and could
*  be better using their time somewhere else. And we see that everywhere. We see that in aerospace,
*  we see that at these chip makers, we see that at consumer companies, you name it.
*  Certainly, I think, you know, if we had to pick a type of company that has seen the most interest,
*  it's those who value speed. Right. So those for whom having a board on your desk tomorrow,
*  rather than next week is critical. That's like who's approaching us most.
*  That makes complete sense. As you go about building out your own team internally,
*  obviously, AI talent is hot right now and quite competitive. I've seen this in other places and
*  heard this from other founders that it's actually easier to recruit talent if you're working on
*  something interesting. And you brought this up at the beginning of the podcast being missionary
*  driven versus building another chat bot for XYZ. I'm curious if you're seeing that play out in real
*  time. 100%. Yeah, without a question. I mean, I think that the things that make it attractive
*  to work on something like this is, well, for one, reinforcement learning itself is a more rare
*  application of machine learning. You know, there's probably 10 to 100 times as many applications of
*  more traditional supervised learning in the industry than there is reinforcement learning.
*  So immediately, experts in reinforcement learning are drawn to us because we're an example of an
*  application of their work. And so we've seen some of that. The other thing that makes it really
*  exciting for people is having something physical that you can imagine. Right. Like we're not talking
*  about, you know, like you said, like a slightly better, you know, user experience score at the
*  end of a chat conversation, we're talking about something you can hold, something you can kind of
*  physically work with. Like, for example, one of the goals that I have for the company, this might be
*  a bit ambitious, but but we'd like to do it. I want to be able to take this video call on a
*  Quilter designed computer by the end of this year. And I think like, that's awesome. Yeah, I think,
*  should we pull that off? I mean, if not this year, we'll pull it off shortly after. But like,
*  imagine writing some code, and then eventually having a board on your desk that then you made
*  with algorithms that then does that, like that is so satisfying to think about and to do. And so
*  certainly that draws people to tackling this problem.
*  That'll be in the Computer History Museum one day, an exhibit. That's no, that's that's awesome. And
*  that's that's an incredible, incredible goal. Another question on talent. It seems like the
*  sort of trajectory for a typical research scientist focused on AI or machine learning broadly,
*  kind of went through undergrad, went through a PhD program, did a bunch of research, and then went to,
*  one of the big tech companies and continue doing research there. And a lot of that research was
*  essentially academic research, it was open source. And now it seems like that trajectory has shifted.
*  So now people are going straight from undergrad into companies, whether that's open AI, or you
*  guys are somewhere else, and doing research that sort of, you know, close within that organization.
*  I'm curious if that is a risk, both in terms of like the quality of talent, but also in terms of
*  reinforcement learning is great. There's a bunch of examples from DeepMind that you guys can pull on.
*  And as companies sort of close themselves off a little bit more, that becomes less successful.
*  And I'm curious if either of those two things are kind of existential risks for the AI industry at
*  large. I hesitate to think that that will be. I mean, just historically speaking, when companies
*  go and require a whole bunch of talent and therefore inject money into a bunch of problems,
*  you don't end up seeing something completely isolated, you end up seeing a whole bunch of
*  open source examples and alternatives and a vibrant ecosystem for that. It's hard for me to
*  imagine that wouldn't be the case here. Even if the best RL engineers are going to, I don't know,
*  DeepMind and DeepMind starts close source everything, maybe they'll maintain an edge
*  for a little while. But just the raw, I think, interest, the number of people who are going to
*  go study it and the number of people who are going to make an open source project to try to
*  get a job at DeepMind is only going to go up. So yeah, I guess it's not something I've considered
*  as a potential threat. That makes sense. Yeah. And I'm curious, if you look at kind of the AI
*  landscape at a very high 30,000 foot level, there is this big kind of battle between open source
*  and closed source. I'm curious if you have an opinion on how that's going to shake out over
*  the next five years, whether the sort of closed source foundation models run away or open source
*  continues to keep up and starts to create some level of commoditization. I don't know that I
*  have a good prediction on that, to be completely honest with you. I mean, I think, again, historically,
*  open source has been incredible and underestimated. As a good example of this take,
*  Windows versus Linux. I mean, Windows is probably still the most popular OS for home use, but
*  for production servers, Linux runs everything, even though Microsoft spent plenty of time trying
*  to make production grade servers and Windows Server and whatnot. The thing I think that's
*  really different here is with a neural network, open source shines when there's a critical mass
*  of people interested in contributing to it. And a large number of relatively small contributions
*  results in a really fantastic product. So you think of like VS code where you can have 10,000
*  people write a small extension. And because of that, there's a huge ecosystem of things that help
*  you. That makes a really great product. But it's not clear that a thousand people spending an hour
*  a week produces a better neural network or something like that. And so that maybe is an
*  argument against open source being quite as competitive as it has been in the past. But I
*  don't know. I don't think I have a strong bet or opinion in one direction or the other, to be
*  honest. No, that's a really good point. It's like you have these step function improvements,
*  like transformer, right? That sort of leads to the step function, increasing capabilities.
*  And if those happen sort of within a closed environment, perhaps that's an unfair advantage.
*  That makes a ton of sense. And we're running close on time here. Maybe if we go back and you've been
*  building Quilter for a few years, and I'm sure you've had a lot of experiences, both positive
*  and negative, if you could take everything that you've learned in the process so far,
*  go back to day one of founding the company, what advice would you give yourself?
*  That's a good question. I mean, I wish I could just like remember everything we did wrong and
*  then replay it like very, very specifically. Like, for example, let's skip the whole wilderness
*  period of a year of exploration. And let's go straight to this. But I mean, of course,
*  that's not the intent of the question. I mean, I think honestly, probably the single most useful
*  thing I wish I invested in more early on that maybe is helpful to other founders is accounting
*  for the fact that building a startup is really difficult, and really lonely and brutal at times.
*  And I think that the things that have been most effective for me in dealing with that is, you know,
*  number one being surrounded by really great people, right? Like if you if you have a co founder,
*  that's fantastic. If you have friends who are building really difficult things or building
*  other startups, that's fantastic. You know, when you're talking to investors or partners,
*  you should be evaluating that probably more than financial terms and whatever else, because it's
*  going to be so important. Because at the end of the day, most founders just quit at some point.
*  And it's obvious why and just surviving that is so important. I think the other is just self care,
*  right? Like, I, you know, going through a company is a lot more stress and kind of self criticism
*  than than working at a big company, even like SpaceX. I mean, maybe like watching a rocket
*  launch on the day of launches is more stressful than an average day at a running startup. But
*  on the whole, it's no comparison. And so investing in self care, right? Like, you know, having a
*  routine, making sure that you're always carving out time with family, making sure that you're
*  exercising and eating well and sleeping well. All these things are obvious, but so easy to forget
*  when you get sucked into the work and you keep running. That's great advice. Yeah, I remember
*  I had a startup in a prior life and, and I was like, so just focused on what we were doing,
*  I didn't have a couch in my apartment. We just like spent all the time in the office. And finally,
*  after like, I don't know, six months, my girlfriend came over and was like, you really need to buy a
*  couch. I was like, oh, I got it. And it just didn't even cross my mind. But I agree. Yeah,
*  it's certainly important to take care of yourself. And ultimately, in many ways, your job as a CEO is
*  to influence people and make decisions, right? And if you're not taking care of yourself, it's
*  hard to do either of those things. That's great. You raise money from benchmark. Bitchmark is
*  obviously a legendary firm that many founders want to work with and many investors want to be like.
*  I'm curious, what drew you to benchmark and what excites you about working with them?
*  So I got the introduction to benchmark through one of my existing investors who spoke very
*  highly of them. So I'm working directly with Eric Visschria there, who I got to meet and get to know
*  a little bit before we made the commitment. I think there's two things more than anything that
*  drew me to working with them. Number one was experience. I think that there's a lot to be
*  learned from previous failures, but there's potentially even more to be learned from previous
*  successes. And working with someone who has seen that story of seed through public company and seen
*  it multiple times is super attractive. The hope is that that results in avoiding lots of mistakes
*  that are unnecessary and unforced. The second thing is, as any founder should, I did a lot of
*  diligence on Eric, both on people he recommended I speak to and people I found in my own way.
*  And I've never heard such positive founder reference. Like bar none, I've never done a
*  reference call for an employee or a coworker or a boss or partner or anything that came up that
*  positive. And so that made my decision for me really quickly. That's awesome. Well, congratulations
*  on the journey so far and excited to watch it unfold. And if you have a spare laptop at the
*  end of the year, I'll certainly take one off your hands. If people want to follow the journey, or if
*  I'm a consumer company or a company that needs to design electronic circuit boards or an engineer
*  that wants to try to find a way to work with you, how can we get in touch or follow the journey?
*  Yeah, easiest thing is our website. So quilter.ai. If you search for Quilter PCP or Quilter AI on
*  Google, I'm sure you'll find it as well. Certainly careers page, we're open to people joining us.
*  We're an open beta. So if you're an electrical engineer, welcome to upload signs and try it out.
*  And I'm sure we have social links there as well for kind of updates along the way. And yeah,
*  once we'll it probably won't be a full laptop. It'll probably be kind of a Raspberry Pi looking
*  thing that we build, but happy to send you one once we have it. That's great. Well, thank you,
*  Sergey. And really appreciate you joining. All right. Thank you all. Thanks for tuning in to
*  the autopilot podcast. If you're using AI to create or disrupt a large industry, I would love
*  to learn more about your story. Drop me a line on Twitter or go to our website, apv.vc. If you want
*  to support the show, the best ways are to leave a review wherever you're listening and subscribe.
*  The autopilot podcast is part of Turpitt time, the podcast network behind moment of Zen,
*  Turpitt time, VC, age of miracles and more shows for experts by experts in tech.

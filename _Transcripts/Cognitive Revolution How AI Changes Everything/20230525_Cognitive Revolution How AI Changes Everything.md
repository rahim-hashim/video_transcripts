---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 4849s
Video Keywords: []
Video Views: 2357
Video Rating: None
---

# The AI Chip Revolution with Andrew Feldman of Cerebras
**Cognitive Revolution "How AI Changes Everything":** [May 25, 2023](https://www.youtube.com/watch?v=JjQkNzzPm_Q)
*  This wasn't about making money.
*  This wasn't about moving the ball forward a little bit.
*  We wanted to move an industry forward
*  and we wanted to put our shoulders to it
*  and see if we could transform an industry.
*  We tried to see if we could come up
*  with a solution that was creative
*  and that would be substantially better.
*  Not a little bit, not 10 times better,
*  but 50 or a hundred times better.
*  Hello and welcome to the Cognitive Revolution,
*  where we interview visionary researchers,
*  entrepreneurs and builders working on the frontier
*  of artificial intelligence.
*  Each week we'll explore their revolutionary ideas
*  and together we'll build a picture of how AI technology
*  will transform work, life and society in the coming years.
*  I'm Nathan Labenz joined by my co-host, Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution.
*  In the era of deep learning and scaling laws,
*  it's often said that the three fundamental ingredients
*  to AI are algorithms, data and compute.
*  We've spent a lot of time on this show
*  exploring different aspects of algorithms
*  and the centrality of data has run through
*  just about every conversation that we've had.
*  But today we take our first step into the world of compute.
*  My guest, Andrew Feldman, CEO of Cerebris Systems,
*  makers of the world's largest ever chip
*  and inductee into the Computer History Museum,
*  is the perfect guide to help understand the landscape
*  at both a metaphorical and also a very practical level.
*  For the last few years and still today,
*  AI computing has been performed on GPUs
*  or graphics processing units,
*  simply because GPUs have been the best way
*  to parallelize computation at scale.
*  Nvidia, the dominant maker of GPUs
*  is now a $750 billion company.
*  That's up more than double so far just in 2023.
*  Yet, GPUs were not specifically designed for AI workloads
*  and they require an extremely complicated software stack
*  to wire them together and to shuffle all the data around.
*  For many of the large scale AI training projects
*  conducted over the last few years,
*  making the GPU clusters work was a significant part
*  of the overall effort.
*  GPT-4 training is rumored to have cost
*  some $100 million or more
*  and next gen systems could stretch into the billions.
*  This makes computing infrastructure
*  a focus of geopolitical strategy and industrial policy
*  as nations position themselves for the AI era
*  and also a possible supply chain choke point
*  that could lend itself to regulatory control.
*  Thus, to have a sense of where AI is going,
*  it's critical to understand the fundamentals of compute.
*  Andrew and his colleagues at Cerebra Systems,
*  all veterans of the chip industry,
*  recognized the opportunity presented
*  by the rise of deep learning
*  and the compute intensive workloads
*  that AI systems would require well before most others.
*  And they set out to build a chip from the ground up
*  with AI systems in mind.
*  What they came up with and what they are selling today
*  is not just the world's biggest chip,
*  but a full multimillion dollar computer
*  that eliminates much of the complexity
*  associated with AI workloads,
*  simply by scaling the hardware itself.
*  Of course, as you'll hear,
*  building the world's largest ever chip
*  while conceptually simple at a high level
*  is extremely complicated in theory and in engineering.
*  Of course, Cerebras is not alone in designing chips
*  specifically for AI.
*  Nvidia is getting into the game
*  along with Google, Meta and Microsoft.
*  But in a market that's growing as fast
*  as the AI market currently is,
*  there will be plenty of space
*  for many companies to flourish.
*  And I certainly expect that Cerebras systems will.
*  Now, I hope you enjoy the introduction to compute for AI
*  that is this fascinating conversation with Andrew Feldman.
*  Andrew Feldman, welcome to the Cognitive Revolution.
*  Well, thank you, Nathan.
*  Thank you for having me.
*  I am super excited about this conversation
*  because you have built along with your co-founders
*  and I know you're always very gracious
*  about giving credit to your teammates,
*  but really a remarkable company
*  that I didn't know a lot about before we connected,
*  but which has built an awful lot of stuff
*  that kind of goes from a very foundational layer
*  increasingly all the way up toward a very productized layer
*  and you're in hardware.
*  So I think our audience doesn't know
*  probably as much about hardware as we do about AI
*  and especially all the applications
*  that we're seeing right now.
*  So I'm excited to get into it with you.
*  I've been trying to study up myself to prepare,
*  but probably gonna ask some kind of rookie questions
*  and hoping that you can kind of help guide us
*  through kind of an understanding of this hardware world,
*  but also the very unique path
*  and approach that you have taken on it.
*  Happy to do it.
*  The thing that you guys are most known for
*  and that you're in the computing hall of fame for
*  is the world's biggest ever chip,
*  2.5 trillion transistors if I understand correctly.
*  So let's just start off with,
*  what inspired you to go try to set a world record
*  with the biggest chip ever
*  and what do you have now that is so special?
*  Well, thanks, Nathan.
*  That's a really good question.
*  I think chips are a little bit like cars.
*  Some are good for taking kids to soccer practice
*  in the grocery store.
*  Others are good for moving lumber and bricks.
*  Still others are really fun to drive on Saturday.
*  We wanted to build a chip that was optimized for one thing
*  and that was for AI work.
*  And AI work presents a very specific set of challenges.
*  It has a huge amount of relatively simple compute
*  and a tremendous amount of communication
*  of moving information around.
*  By building a very big chip,
*  we can keep that information on chip
*  and communication on chip is fast and it's power efficient.
*  Order thousands of times faster
*  and thousands of times more energy efficient
*  than if you have to leave the chip boundary,
*  travel across a motherboard,
*  maybe out a switch to another chip.
*  And so by building a very large chip,
*  we were able to do AI compute extraordinarily efficiently
*  and blisteringly fast.
*  Cool, okay.
*  I think we're gonna get into all of this layer by layer.
*  And just for your reference too,
*  I think our audience probably has a pretty good sense
*  that obviously people are training larger and larger models
*  with bigger and bigger data
*  and that just requires a ton of compute, right?
*  Everybody kind of knows that.
*  I think we also probably have a decent sense
*  that we can't use CPUs for that
*  because we need some element of parallelization.
*  And then I think a lot of people are still kind of
*  at the moment where they're like,
*  so that's where GPUs come in
*  and it gets complicated from there.
*  So again, just so you can kind of help calve it yourself
*  and help fill in the gaps for us.
*  I just kind of want to start again, layer up the chain.
*  What is a chip?
*  This is something that is so basic,
*  but tell us what a chip is in the first place.
*  A chip is an electric circuit
*  that is put on a piece of silicon.
*  It's just that simple.
*  That's a transistor that is embedded into a bit of silicon.
*  And as they get more complicated,
*  there are more and more of these circuits, these transistors,
*  that are in chunks of silicon.
*  And these are the things that power computers,
*  that power the displays,
*  power sort of most of our digital world
*  is one form or another of these circuits
*  that are housed on a piece of silicon.
*  And so there's like tons of different kinds, right?
*  I mean, the kind of canonical ones would be your CPUs,
*  your GPUs.
*  Now you've got the world record biggest ever.
*  Just give us some other sense too
*  of like the diversity of chips
*  and sort of the things that can be accomplished
*  with a little thing carved on a piece of silicon.
*  Sure.
*  I think there are very tiny ones that are sensors.
*  They're ones that draw sort of milliwatts of power,
*  absurdly little amounts of power.
*  There are ones that control dishwashers.
*  Your fancy coffee maker is controlled by a little chip.
*  Much of your car now is controlled
*  by one form or another of a chip.
*  Much of what we do every day,
*  our phones, our laptops, our computers, the cloud,
*  all of these are powered by one form or another
*  of a different size, different shape compute.
*  And chips are where compute lives.
*  So the first thing you have to do
*  when you're gonna set out to build something like this
*  is design it.
*  And this, I think it would be really interesting
*  to contrast kind of how you guys have built your company.
*  Cause I don't know if vertical integration
*  is quite the right term,
*  but it seems like you do operate at a lot more layers
*  of the value creation stack than most.
*  So first there's firms that specialize entirely
*  in designing the chip and you guys do that,
*  but then you do more up the stack as well.
*  So let's start with the design process.
*  What is it like to design a 2.5 trillion transistor chip?
*  First, it's really hard.
*  And it takes years and it takes
*  hundreds of millions of capital.
*  It takes a passion for really hard engineering projects.
*  You have to love hard technical challenges.
*  You're absolutely right.
*  We love those challenges
*  and we love being a system company.
*  So we build the chips,
*  we build the motherboards that they live on.
*  We build the enclosures,
*  the whole computer, the server.
*  We integrate the power supplies, the cooling.
*  And so what we deliver is a whole computer
*  optimized for AI.
*  And sometimes we deliver clusters of these,
*  including in some of the largest supercomputers
*  optimized for AI ever built.
*  So we do work all the way up the stack
*  from the compute silicon
*  to the compiler, to the management software,
*  all the way up the stack.
*  And that's a really fun problem.
*  And you asked about the chip,
*  you begin usually having done simpler ones in the past.
*  That's sort of the way it works, Nathan.
*  It's 20 or 30 years of increasingly complicated chips.
*  One has a collection of friends and colleagues
*  who are leaders in chip design.
*  And you get together and you begin thinking about
*  which problem you wanna solve.
*  And this is my fifth startup.
*  And each time we've built dedicated chips
*  and print circuit boards and put them in a system
*  and built the system software and solved a hard problem.
*  And so in late 2015, the founders and I got together
*  and we said, now which problem do we wanna solve?
*  And we got interested in the problems of AI.
*  And we asked ourselves, what does the AI work
*  really want from the underlying machine?
*  What's hard about AI work?
*  And what is the right type of computer to build for it?
*  We came up with the idea that we could build
*  a dedicated machine, not repurpose
*  a graphics processing unit, but a dedicated machine
*  where every ounce of its energy, its focus was aimed
*  at this particular problem, not lots of other problems
*  but this problem.
*  And then every decision we made, how big it was,
*  the shape of the core, how many cores,
*  every decision was made towards the end
*  of optimizing for AI work.
*  So you set that vision from the founding in 2015.
*  The models at that time were obviously a lot smaller.
*  So you had clearly some foresight there to be skating
*  where the puck is going to be, so to speak.
*  I have no foresight, Nathan nor any technical vision,
*  all of that's my co-founders.
*  I have good ability to pick other founders and co-founders
*  and world-class employees, team members.
*  No, we were interested in the problem of AI.
*  It was clearly something on the horizon
*  and sort of it presented a new challenge to compute.
*  In the same way that cell phone compute presented
*  a new challenge to the compute world, it was different.
*  And when there's a new compute challenge,
*  historically new players emerged.
*  None of the leaders in x86 compute, not Intel, not AMD
*  were able to capture this new work in the cell phone world.
*  All of it went to ARM, 100%.
*  We saw that sort of sea change happening
*  with the rise of AI.
*  We were probably wrong.
*  We probably underestimated the size and scope
*  of what AI would be, but we knew that it was interesting.
*  It presented a new problem to computers
*  and that we could build a better machine,
*  optimized for this particular problem.
*  And that was the founding impetus for the company.
*  Hey, we'll continue our interview in a moment
*  after a word from our sponsors.
*  Hi everyone.
*  I wanted to take just a moment to share another podcast
*  that I've been enjoying recently, the AI Breakdown.
*  As anyone in AI knows, the pace of progress
*  and all the new releases are relentless.
*  I call myself an AI scout and I work overtime to keep up.
*  But these days, even I can't keep track of everything.
*  The AI Breakdown helps me make sure
*  that I don't miss anything important
*  by curating news and analysis daily.
*  Host Nathaniel Whittemore, AKA NLW,
*  quickly highlights the top stories of the day
*  before going deeper on a single topic of interest.
*  Episodes are usually 15 to 20 minutes
*  and he releases them every single day.
*  Now it's not easy to keep up with a daily release schedule
*  and still maintain your sanity.
*  So I really appreciate how NLW maintains a curious posture
*  and avoids rushing to judgment.
*  A big part of the reason I'm inclined to recommend the show
*  is his willingness to sometimes say, I don't know.
*  I think listeners will find the AI Breakdown
*  to be a great compliment to the long form,
*  deep dive interviews that we create.
*  So I encourage you to check it out.
*  The link to the AI Breakdown with NLW is in the show notes.
*  Omniki uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work,
*  customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it
*  and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
*  So maybe we could kind of build up the story a little bit
*  also in terms of the team and kind of the roles
*  and how you layer out the company over time
*  because I have to imagine that this is your vision.
*  The first thing you're gonna do is design, right?
*  And so there's a certain skillset that comes there,
*  but then next you're gonna have to go
*  get this thing manufactured and that presumably
*  brings out a new set of problems and skillsets.
*  So like, who was the first group that you hired
*  to design this thing and like, how long did that take?
*  I think Nathan, most of us who are serial entrepreneurs,
*  we work with many of the same people time and time again,
*  all of the founders worked with me at my last company.
*  Our CTO, Gary Latterback, was my co-founder
*  at the last company.
*  Michael James, JP Fraker and Sean Lee
*  were all technical leaders at our last company.
*  And so you generally begin with the best people
*  you've ever worked with.
*  And I'm sure that's the same in your business
*  and in many businesses is that you begin with people
*  who you really enjoy working with
*  and who inspire you every day.
*  And one of the things you do as a CEO
*  is you have lists in your mind of great engineers
*  and smart investors.
*  And some of your time you're talking
*  to the really smart investors
*  and some of the time you're engaged
*  with extraordinary engineers.
*  Some of whom have worked with you in the past,
*  others maybe worked with partners
*  or you had a chance to engage with them
*  and they really impressed you.
*  And so at the beginning, usually the founders get together,
*  they settle on a vision and often it's a very high level.
*  We wrote two things on the whiteboard.
*  We wanted to work together again.
*  We wanted to do something important.
*  And this wasn't about making money.
*  This wasn't about moving the ball forward a little bit.
*  We wanted to move an industry forward
*  and we wanted to put our shoulders to it
*  and see if we could transform an industry.
*  And so once we'd identified, we were meeting regularly
*  and once we'd identified a problem that interested us,
*  we tried to see if we could come up
*  with a solution that was creative
*  and that would be substantially better.
*  Not a little bit, not 10 times better,
*  but 50 or 100 times better.
*  And once we had that idea, we began to socialize it
*  with some of the best people we'd worked with
*  over the years and see if they were excited by it.
*  And of the first 20 or 30 employees,
*  almost everyone had worked with us previously.
*  And that's one of the really fun things about Silicon Valley.
*  And we have people here who I worked with in 96
*  at our very first company.
*  We have people who we'd worked with 2000, 2003,
*  from 2003, 2007.
*  Each company has people you note and say,
*  that's an extraordinary person.
*  If we ever need that set of skills again,
*  I'd love to work with them again.
*  They make those around the better.
*  They bring interesting ideas to the table.
*  And so once you have an idea and a direction,
*  you begin systematically reaching out
*  to the best people you know.
*  And while you're doing that,
*  you begin to engage with investors.
*  We were fortunate, we made eight pitches
*  and got eight term sheets.
*  And so we were able to fund the company very quickly
*  with world-class investors, the best in the business.
*  We were able to bring some super angels to the table,
*  some really wise people to act as sort of advisors
*  and sort of a rabbis to keep us from making mistakes
*  that were too egregious.
*  And usually the first problem is one of architecture.
*  And the problem of architecture is,
*  you're at point A and you wanna get to Z,
*  how do you break this up?
*  What are the pieces?
*  How do you attack this large unknown problem?
*  And which parts of that problem
*  are going to be extraordinarily difficult?
*  And which parts are gonna be sort of solid engineering
*  problems but don't require vast invention?
*  And once you've broken up the problem into pieces,
*  once you've identified which piece is gonna be hardest,
*  we like to begin with the hardest piece.
*  For us, that was, how do you build a chip
*  that is orders of magnitude faster
*  than a graphics processing unit?
*  And how do you do things that graphics processing units
*  are historically bad at?
*  When your audience works with GPUs,
*  they often encounter problems with memory
*  and particularly with memory bandwidth.
*  How do you resolve those problems?
*  How do you make sure you're not a little better
*  but you're hundreds of thousands
*  or tens of thousands of times better
*  on these key dimensions that underpin the AI workload?
*  And so we began working on the problem
*  and you work on the problem every day.
*  The technical team is engaged.
*  I'm out talking to other engineers
*  seeing if they wanna talk to us further.
*  Step by step, you build up your team.
*  Each time you bring in a guy you've worked with,
*  you ask him or her,
*  who are the best people you've worked with?
*  We haven't worked together in three or four years.
*  Who are the best engineers you encountered?
*  And then you go talk to them.
*  You say, look, we heard great things about you.
*  People we really trust are really impressed
*  with the work you do.
*  Would you like to talk to us?
*  And you build a cadre, a nucleus of extraordinary people
*  and engineers like to work
*  with other extraordinary engineers.
*  They're motivating.
*  They get your juices going.
*  And so at this point, you've got a team,
*  maybe 20, 25 people.
*  You've identified the hard parts of the problem
*  and you're systematically attacking it.
*  That's how you get going.
*  For context, one thing I did in preparing for this
*  was just read the recent book, The Chip War.
*  I was just trading emails with the author.
*  Definitely a really good kind of general history primer
*  on chips, why they're important.
*  And one of my big takeaways was just
*  the extreme specialization and the extreme kind of
*  coordination of the global value chain
*  that all kind of comes together to create things.
*  And there's like, seemingly multiple,
*  almost single points of failure in terms of like
*  one company makes the machining without which,
*  nothing else can happen.
*  Only one, right?
*  Just one Dutch company makes the manufacturing tools
*  that all chips use.
*  What that has me thinking for you is like,
*  when you're going so far outside the bounds
*  of what has kind of been done and you're like
*  not doing something that's on maybe anybody else's
*  TikTok sort of roadmap, what ended up being
*  the hardest thing?
*  And to some degree, I mentioned that had to be that like
*  nobody can help us with some of these things, right?
*  Even the wafer itself, I believe there probably was no wafer
*  that big for you to even start with.
*  I don't know if you've ever seen those old maps
*  from the 14 to 1500s.
*  And they have the land they knew.
*  And then they have these areas where they had no idea
*  what was there.
*  And they draw a picture of a dragon and under it,
*  they'd write here be dragons.
*  And we were only interested in sailing there, right?
*  We have no interest in charting territory
*  that other people have seen and done.
*  We wanna be out there at the leading edge.
*  We wanna be out there with the dragons.
*  And that's hard, right?
*  There are bad days out there.
*  There are challenges that nobody's ever encountered before.
*  People had tried and failed to build big ships.
*  And there was a big literature on why you would fail.
*  And we solved all those problems in about six months
*  for $20 million.
*  But nobody ever gotten further than that.
*  Nobody failed further up the mountain, right?
*  And I tell people, imagine you're
*  at the base of Everest having beers
*  before it had been summited.
*  And some climbers just came down and they said,
*  about halfway up, it's brutal, we couldn't do it.
*  You're gonna have a real problem there.
*  For the first time, you guys go up,
*  you get all the way to the top, you come back down
*  and you're having beers with these guys again.
*  And you say, guys, that's not the hard part, right?
*  The hard part was way further up.
*  And at every stage, we had to invent things, right?
*  There weren't tools, there weren't manufacturing equipment.
*  There weren't ways to cool, there weren't components.
*  At each stage, when you do pioneering innovation,
*  there's not a catalog where you can look up and say,
*  oh, here are these other components
*  that will fit right in with this.
*  And so you have to be ready for that.
*  And we had some experience doing extraordinary innovation,
*  but it's not easy.
*  But what we found is we were able to inspire
*  our vendors.
*  And they also got excited.
*  I remember one of them said,
*  what you guys are doing is why I became an engineer.
*  Right, and that wasn't one of our engineers,
*  that was a vendor's engineer who had work to do
*  to modify their parts.
*  It was inspiring when people do amazing things.
*  So Nathan, at every stage, it was a challenge.
*  There was no easy bit.
*  I wanna get into the weeds a little bit more
*  of the hard bits with you.
*  So what I understand is you've reassembled the,
*  got the gang back together for one more heist.
*  And it's all the best people you've ever worked with.
*  And you, it sounds like first spent six months
*  architecting the chip itself to kind of satisfy yourselves
*  that you could design something that could
*  meet the performance criteria that you set out.
*  So now you've got a software,
*  described essentially, right?
*  Essentially a blueprint for a circuit
*  that is beyond comprehension in terms of its complexity.
*  And now, where do you go from there?
*  Usually you have a software simulator.
*  So you've built software that you believe will behave
*  the way your chip will.
*  You have different types of simulators that have been built
*  and you begin experimenting to understand
*  what trade-offs you can make.
*  And while that's going on,
*  usually some guys begin the early stages of chip design
*  and they begin thinking about how they would construct
*  the chip, how they would organize these integrated circuits
*  into delivering what you want.
*  And they begin thinking about the hard problems of
*  if we need a third row of seats,
*  what does that mean for the length of the car?
*  If you want a truck bed,
*  what does that mean for the backseat?
*  It means it's really difficult.
*  Let me just go a little bit down more to root level again,
*  though, like if, so what are these trade-offs?
*  Like you're kind of talking about cores versus memory,
*  how much of like relative inputs.
*  What you have as a chip architect
*  is an amount of real estate, right?
*  You have a fixed bit of real estate,
*  that's the size of the chip you wanna make
*  and you need to allocate some of it to compute
*  and some of it to memory and some of it to communication,
*  to the moving of information around the chip.
*  And you have to make decisions.
*  Do you want a big core?
*  Do you want lots of little cores?
*  Do you want memory centralized?
*  Or do you want each core, each little compute engine
*  to have its own dedicated memory?
*  And there are pros and cons of each
*  and different types of workloads,
*  say database or graphics,
*  would lead you to very different decisions.
*  And so while you're doing this,
*  you're examining what does AI want?
*  What is it, it asks of the underlying compute,
*  what's hard about it?
*  Is it one big compute problem
*  or lots of little compute problems?
*  Do you do the work once and then you're finished?
*  Or do you do lots of little problems,
*  learn a little bit, lots of little problems,
*  move the data, lots of little problems?
*  Each one of those would produce
*  a very different architecture.
*  And that's exactly the way you think about this problem.
*  And AI has some very particular characteristics.
*  The cores don't all work on the same problem.
*  When the reason CPUs aren't optimized for this work
*  is the CPU has a big pile of memory
*  in the middle called a cache.
*  The cores all have access to this.
*  And if you wanna put one chunk of data in
*  and have lots of compute engines work on it,
*  that's a great way to do it.
*  That's not the way AI works.
*  AI has lots of little calculations
*  which then move the work, right?
*  We think about the layers, right?
*  You're doing work in one layer
*  and then you move the work to the next layer
*  and you do the work in the next layer.
*  There's a sequentialness about AI.
*  And so we thought what is the right mapping
*  of compute, of memory, of communication bandwidth
*  to this particular problem, right?
*  Does AI present big complex problems?
*  Do you need 64-bit double precision, right?
*  That's historically been the data format of supercomputers.
*  Turns out you don't need it.
*  So we don't have it.
*  The GPU is also designed to solve all these other problems.
*  So they have to waste some of their real estate
*  with circuitry for a problem that's not AI.
*  We take that out.
*  And so you think about which problems
*  you're gonna be good at,
*  which problems you're not even gonna try to be good at.
*  Right, focus.
*  And you think about for this class of problems,
*  what is the best way to achieve your goal?
*  Small number of big cores, large number of little cores,
*  distributed memory, centralized memory,
*  lots of little IO, a small number of big pipes
*  or lots of little pipes.
*  How are you gonna get data onto and off of the chip?
*  All of these are sort of the questions
*  that architects ask themselves at the beginning of a problem.
*  And so too, you said earlier that the problems
*  that people encounter with GPUs is not enough memory
*  or slowness in moving things around in and out of memory.
*  You can elaborate on this if you want to,
*  but I think the kind of core reason that that happens,
*  especially in like the training process, right,
*  is you have to kind of keep track of all of these parameters
*  and the back propagation gradients
*  at all of these different points.
*  And you can't kind of lose that stuff until you've done
*  a certain batch of computation,
*  made all the necessary updates,
*  and then can kind of save that and free up some memory.
*  That's kind of my very poor man's interpretation
*  of the situation.
*  It's a good poor man interpretation.
*  There are two problems that haunt GPUs.
*  The first is we now are working with models
*  that have very large parameter counts
*  and too many parameters to store in their memory.
*  So right away, they need to shard your parameters
*  across many GPUs.
*  That's a complicated problem.
*  The second problem is the actual calculation
*  of a big layer is too big for a GPU.
*  And so they have to take that giant matrix multiply
*  and break it up into little pieces
*  and spread that over many little GPUs.
*  All right.
*  Now, when you do that, to get the answer,
*  you have to wait until the last one has given its part back.
*  Right, that's Amdahl's law.
*  And so you care desperately about how far away in time
*  each of those parts of the main calculation are.
*  So right away, you see the problem.
*  You've got these giant networks.
*  You've got lots of little GPUs, maybe hundreds or thousands.
*  You're trying to think about how to place work
*  on each individual one, how to break up your problem,
*  how to break up the number of parameters you have.
*  Those are painful problems.
*  And that's the distributed compute edge of AI.
*  Right, and if you look at these papers,
*  whether it's the Lama paper or the GPT-4 paper,
*  at the back, they usually give credit to dozens of people
*  who are involved in just this part,
*  not the AI, but the distributed compute,
*  how to break up the problem and spread it out.
*  You have a big chip, takes minutes.
*  You don't have to worry about that at all.
*  We have in our architecture enough memory
*  for trillions of parameters.
*  We have enough cores, 850,000 cores,
*  so that even the largest layer
*  of the largest neural network can fit,
*  so we never have to break things up.
*  And so it vastly simplifies
*  how you place big neural networks onto our compute.
*  It kind of sounds like with this giant chip,
*  the function is probably a lot more like
*  what people visualize for themselves
*  as going on in a neural network architecture
*  when they sort of envision like there are layers
*  and things are kind of moving from layer to layer.
*  I'm gathering kind of that the parameters
*  kind of can stay in place on the big chip
*  and then the data can kind of move,
*  but the parameters just get kind of loaded
*  and then you don't have to fuss with that.
*  Whereas on GPUs, it looks nothing like what you think
*  and instead it's like a total
*  incomprehensible distributed mess.
*  That's right.
*  Let's think about sort of the history for a sec.
*  In 2014, 2015, we saw the rise of AI start.
*  We saw GPUs begin to get used.
*  2015, 2016, we saw that communication
*  was gonna be the hard part of this problem.
*  Our solution was to build a bigger chip
*  so you had to communicate less.
*  Nvidia's solution was to buy Mellanox,
*  to buy a company that specialized in Ethernet
*  and InfiniBand's ability to tie together
*  lots of little chips.
*  Tying together lots of little chips
*  is very complicated and messy.
*  Performance is almost always sub-linear.
*  And that's the same in almost all our lives
*  is that if you say your job takes you X amount of time,
*  if you add a second person, it doesn't take half X ever.
*  If you're lucky, it takes less time, but not half.
*  And if you add 10 or 50 people, it never takes a 50th.
*  Right?
*  In fact, frequently it takes more time
*  because you've got to coordinate, you've got to organize,
*  you've got to divide up work, you've got to distribute work.
*  It's the exact same thing in building clusters of computers
*  that as these problems got so big,
*  we couldn't do them on one GPU.
*  We tried to break them up and spread them over hundreds.
*  Now the actual problems of coordination,
*  of breaking up the problem,
*  these are the same problems that management exists for.
*  That's the overhead.
*  We're able to sidestep those with a very big chip.
*  You almost had it exactly right.
*  We hold the activations on the chip and we don't move those.
*  The data streams in, the parameters stream in,
*  and the activations stay and we stream the gradients out.
*  And so what we're able to do
*  is move information less frequently.
*  We were able to keep data closer to compute
*  so it takes less time to access it.
*  Every core has its own dedicated memory,
*  never any contention.
*  These are things that we thought about
*  would help the AI work, part of the architecture.
*  Contention.
*  And contention, just to contrast,
*  this is like when multiple processes need to access data
*  that may be in the same data access bottleneck.
*  Exactly, that's exactly right.
*  Contention is when lots of people are trying
*  to check out a Safeway at the same time.
*  There's just a queue.
*  And where's the queue form in a GPU?
*  The queue forms when lots of cores
*  are trying to get to off-chip memory.
*  They have this memory that lives off-chip.
*  And all these workers need data.
*  They're all trying to get off-chip at the same time.
*  And that's memory bandwidth contention right there.
*  And that's a fundamental challenge in the design of GPUs.
*  So how general is this?
*  I'm struck by the fact that you started the company
*  before Transformers.
*  And are still the fastest on earth at Transformers.
*  That's pretty good architecture that the team did.
*  We're really proud of it.
*  Yeah, it's awesome.
*  How narrowly sort of tailored is the chip to,
*  if all of a sudden there was a recurrent network breakthrough,
*  would that cause you problems?
*  It's a very, very, very, very, very, very, very, very,
*  Nathan, you put your finger on, I think,
*  what is one of the fundamental questions
*  of computer architecture.
*  And that is which part of your design to be general
*  and which part to be specialized.
*  Right, now, Nvidia in earlier GPUs,
*  in the V100 and the A100,
*  they put customized circuitry
*  in for three by three convolutions.
*  And if you were doing computer vision,
*  those were really helpful.
*  But if you were doing language and LP work,
*  they were extremely inefficient.
*  Right, that's the price of specialization.
*  You get good at it if you work on that problem.
*  But if another problem comes along, you're less good at it.
*  Where we focused our energy and our design
*  was in the underpinning of AI.
*  The underpinning of AI is sparse linear algebra.
*  All of the AI problems,
*  whether they're graph neural networks,
*  whether they're computer vision,
*  whether they're big language models,
*  all of them decompose down to linear algebra,
*  and in particular to sparse linear algebra.
*  And so what we optimized our engine for
*  was to be good at that problem.
*  And that turned out to be a really good architectural choice.
*  Use this phrase AI compute versus dense compute.
*  I guess AI compute sounds synonymous with sparse
*  if it's contrasted against dense.
*  So help us understand that a little bit better.
*  Like when am I running something
*  that's dense versus sparse?
*  I know that like a lot of activations,
*  like I've seen papers recently where like
*  a lot of activations can just be rounded down to zero
*  and you'll be fine.
*  I don't know, is that gonna hold first of all,
*  as like more intensive training comes online,
*  those things seem like they'll become less sparse.
*  But first what sparse means is
*  a sparse matrix has lots of zeros in it, right?
*  And so you have two matrices,
*  you're gonna multiply them together,
*  and one has, or both have a lot of zeros.
*  Now the GPU goes ahead and multiplies everything together.
*  Now that's not very smart,
*  because multiplying by zero takes time,
*  takes power, and produces no new information.
*  You didn't have to do the multiplication
*  to know that anything multiplied by zero is gonna be zero.
*  Right, and so doing that is like walking in place
*  in a race to the finish line.
*  You make no forward progress, you burn calories,
*  you waste everybody's time.
*  Our machine, because it was designed not for graphics,
*  which is only a dense problem,
*  but our machine was designed only for AI,
*  which is frequently a sparse problem,
*  when it encounters a zero,
*  it doesn't do the multiplication, it skips it.
*  You don't need to do the multiplication
*  because you know the answer.
*  You know the answer before you do it
*  without doing any work.
*  And so as these problems demonstrate sparsity
*  in any number of ways,
*  in their weights, in their activations, in their structure,
*  you can avoid doing useless work.
*  Right, and that's a very powerful notion, right?
*  Because what you want is every ounce of your power
*  and every ounce of your compute
*  pointed at problems that move you towards the goal line
*  of completing your training run,
*  or completing your inference
*  and doing your auto regression inference
*  or your classification if it's something else.
*  And so that's the difference between a dense engine
*  and a sparse engine,
*  is whether when you encounter a zero,
*  you mindlessly multiply it
*  because that's what you do to everything,
*  or whether your core is smart enough to say,
*  whoa, no need to multiply that, let's skip that,
*  move on, move on, move on.
*  And what a whole collection of recent papers have showed
*  is exactly what you said, is that sometimes
*  you can round these weights down to zero and lose nothing.
*  And when you do that, and you have a sparse engine like ours,
*  you can train much, much faster for fewer compute
*  and using a fraction of the energy.
*  And that's what a whole series of papers
*  we've published have shown.
*  Others have published similar papers,
*  the guys at NeuroMagic published
*  a very interesting paper on this
*  and how it relates to inference, the guys at Mnemonic.
*  There are a whole group of people
*  doing extremely interesting research
*  on what we can do to take this absurd amount
*  of compute necessary to train these models
*  and shrink it down without losing accuracy.
*  And that's what you get with sparse.
*  So this might be too hard, it may just be too gnarly
*  to give us an intuition for,
*  but what I do find fascinating about this
*  and the parallel between biology and AI,
*  I don't like to over-analogize,
*  but I do see that in both cases,
*  there's this sort of like, where does the intelligence
*  or the sort of ghost in the machine,
*  where does that start to emerge?
*  Because at the foundation here,
*  you have this ultimately instantiated
*  in a physical circuit form, right?
*  Where it's like, and somehow there is a fully
*  deterministic process that is engraved,
*  represented in an engraving on a piece of silicon, right?
*  That does that logical switch on when it's a zero,
*  I can somehow skip this step.
*  Can you give us any intuition
*  for how that process is ultimately
*  like physically instantiated?
*  Let's think about it this way.
*  Say your system for moving freight
*  can only move pallets, okay?
*  So you put a bunch of boxes on the pallet,
*  you wrap the pallet up with plastic,
*  you move it with a forklift, you put it in a truck,
*  you move it across country.
*  Now in that world, you may not have the ability
*  to determine if one of those boxes is empty,
*  because all your system is doing
*  is putting it on pallets, wrapping it up and moving it.
*  That's a dense law.
*  Doesn't matter what's in the package, all right?
*  You're gonna treat it the same way.
*  You're gonna multiply by it.
*  If you had the capability to know what's in every package,
*  you would never ship an empty package across country.
*  That would be brain dead.
*  If you had, in this case, what it is,
*  is the memory bandwidth,
*  you could know what's in a package
*  and throw it away before you wrapped it up,
*  put it on a pallet and moved across country.
*  This is sort of what happens when in the mathematics,
*  when you have huge amounts of memory bandwidth,
*  you don't have to move pallets worth of data over.
*  You can move vectors of data over
*  or even scalar worth of data over.
*  And when you have that sort of fine grain control,
*  just like when you had control of each box, right?
*  If you could do that,
*  you never have to move empty boxes.
*  And this is achieved by having
*  an extraordinary amount of memory bandwidth,
*  because that allows you to move data
*  to and from your compute engine with tremendous control.
*  And that's one of the advantages of this architecture.
*  Okay, you got the chip.
*  Now you gotta go source a wafer.
*  You have to find somebody to actually do
*  the engraving on the wafer.
*  You have to package.
*  These are all the layers where all,
*  there's this insane supply chain specialization.
*  And I imagine this was all hard
*  because you were probably out of kind of standard spec
*  at every step of the way, right?
*  Every step of the way.
*  The process is not quite engraving, it's photolithographic.
*  So you're gonna etch
*  and you're gonna do that with a laser.
*  And if you want to be at an aggressive geometry,
*  and what that means is if you wanna be able to pack
*  an extraordinary number of transistors
*  in a given square millimeter of silicon,
*  you only have two choices.
*  You either go to TSMC in Taiwan or you go to Samsung
*  in Seoul.
*  And starting at about seven nanometer technology,
*  that is the only two choices.
*  In 2016, when we went out,
*  we were at the 16 nanometer node.
*  That means there are 16 nanometers gap
*  between each of these transistors.
*  So you only have two choices.
*  And one of the very few advantages
*  of not being in your 30s is that
*  if you've been in the chip industry for a while,
*  you've built relationships with chip manufacturers.
*  And we had a relationship
*  with Taiwan Semiconductor Manufacturing.
*  We flew out to Taipei and we met with their leadership.
*  And we told them we had an idea to build a chip
*  that was 56 times larger than anybody had ever done.
*  Moreover, our idea allowed them not to change
*  their manufacturing process,
*  to use the steps they already use,
*  and that we'd patented these ideas,
*  and that together we believed we could do something
*  that had never been achieved before.
*  And to their great credit,
*  they're a company with tens of billions of revenue
*  and we were 30 dudes in a PowerPoint.
*  And they listened, they thought about it.
*  In the meeting, they greenlit the project.
*  A tremendous credit to a company
*  that puts decision makers in a room
*  with innovative startups.
*  They greenlit the project.
*  We built the part and first time around it worked.
*  There's a couple of things there that are super interesting.
*  I mean, for one thing,
*  when you're raising your initial capital,
*  a risk presumably would be,
*  are you gonna be able to convince one of the two companies
*  that could possibly actually manufacture this
*  to take your business,
*  given that they've got a lot of stuff going on?
*  Then because that's such a risk,
*  your answer to that risk was,
*  okay, we're gonna figure out how to do a giant chip
*  with the same machinery that currently makes
*  a bunch of smaller chips.
*  And the stepping that you referred to
*  is a sort of etching one chip at a time,
*  on a wafer and then those get kind of sliced up
*  and then you've got like a bunch of little chips, right?
*  You figured out how to do your whole thing
*  with the same core architecture for them.
*  All chips, first, the way chips are made
*  is there's a 300 square millimeter circle of silicon.
*  That's a blank wafer.
*  And that enters the fab.
*  And just like your mother knocked out cookies,
*  the stepper flashes little cookie cuts
*  across this 300 millimeter square.
*  And then what happens usually is the wafer goes out
*  to a singulation and it's cut along all those cookie lines,
*  just like your mother when she pushed down
*  and the cookie cutter ended up with a cookie, right?
*  And so all chips begin as part of a full wafer.
*  They get etched as part of a full wafer.
*  And then they get chopped into little pieces.
*  That's why they're called chips
*  because they're chips off the full wafer.
*  We thought, how silly is that?
*  To break up the little pieces
*  and then pay for expensive switching
*  to try and get it to behave like it was together again.
*  And that what if we didn't cut it up into pieces?
*  And our innovations allowed the step in process
*  to remain largely unchanged
*  and allowed us to communicate across
*  what's called the scribe line,
*  the line that they were usually gonna cut, right?
*  If your mom knocked out all those cookies,
*  remember she lifted up the dough, the extra dough,
*  there were the cookies left
*  and then she rolled that into dough
*  and made a few more cookies.
*  That extra dough is what we call the scribe lines
*  and usually it's cut away.
*  We said, how do we invent a technique
*  using their existing methodology
*  to communicate across that
*  so that you don't need to cut it all?
*  And the first block of our IP
*  and dozens of so patents were around how we might do that.
*  Once you have this giant part,
*  and I don't know if you have a video version of this podcast,
*  but yeah, this is what our chip is.
*  This is an Nvidia A100,
*  this poor sad little small thing here, right?
*  This is our chip, right?
*  So,
*  once you understand that you're gonna end up with a chip
*  that's 56 times bigger, has trillions more transistors,
*  you have a new class of problems.
*  How you're gonna power it, how you're gonna cool it,
*  how you're gonna feed it with data.
*  And that was the next step in our system design.
*  We invented techniques to deliver power to it.
*  We invented techniques to cool it.
*  We were among the first to deliver water cooling
*  to AI dedicated processors.
*  When you cool with water,
*  you have all sorts of advantages.
*  Water is an excellent coolant,
*  air is a really weak coolant.
*  When you cool with water,
*  you can run your chips at lower temperatures.
*  When you run at lower temperatures,
*  your reliability goes up, all sorts of advantages.
*  So we had the opportunity with all this compute, right?
*  Hundreds of GPUs worth of compute in one little area.
*  We could cool it with water,
*  we could keep the temperature low,
*  we could feed it with huge amounts of data,
*  all of that to get this world leading performance.
*  Fascinating.
*  So I wonder, it seems like there's kind of a story
*  of convergence that has driven the AI moment
*  that we're in over the last few years.
*  And I wonder if you're maybe even potentially
*  gonna unlock another layer of convergence.
*  If the early, the triad, right?
*  Of algorithms, compute and data and those kind of all,
*  have to have them all, right?
*  You gotta have a smart algorithm,
*  you gotta have the compute.
*  Most people today default to thinking of GPUs
*  that unlocks this parallelization.
*  But as we've talked about,
*  it comes with this incredible complexity.
*  And while you've been building your giant chips
*  for the last seven, eight years,
*  there's been a whole other giant effort
*  that has gone toward building up a software stack
*  to manage that complexity.
*  If I start to imagine the future, I'm thinking,
*  is there any bottleneck to how many chips you can produce?
*  And do we go to a world where we get both of those
*  converging, the complexity of the software,
*  as maybe models get even bigger,
*  and now the cluster is not the Nvidia chips,
*  but your chips?
*  Is that where we're headed?
*  We are.
*  Couple things.
*  First, the software landscape is both more simple
*  and more complicated than it was in 2015.
*  In 2015, if you remember,
*  there were half a dozen frameworks, right?
*  There was Cafe, there was Theanos,
*  TensorFlow was rudimentary,
*  I don't think there was PyTorch happening.
*  There were a lot of different choices.
*  And right now the world has sort of settled on PyTorch,
*  right?
*  The number of languages that the ML practitioner writes in
*  has really narrowed.
*  Also, because of the work of Chris Latner and others,
*  there is a merged and intermediate representation,
*  in particular MLIR,
*  so that this PyTorch can be compiled
*  to something everybody agrees on.
*  None of that was in place,
*  and that's a vast simplification.
*  Now with that, our models have gotten absurdly large, right?
*  And not only have they gotten large,
*  but we've learned that using a ton of data
*  is really helpful.
*  And so we're running very big models with huge datasets,
*  and that results in a need for obscene amounts of compute,
*  where really, where dozens of GPUs don't get it done,
*  you need thousands or tens of thousands of GPUs.
*  We replaced hundreds of GPUs,
*  and so what we saw right away
*  was an opportunity to build clusters of our machines.
*  And in November of last year,
*  we announced a supercomputer called Andromeda
*  built up of 16 of our machines.
*  That's 13.6 million cores, right?
*  That's big.
*  The largest supercomputer on earth has eight million cores.
*  They're bigger cores,
*  but just sort of as an idea of how much compute is here.
*  And with this, we had the opportunity
*  to immediately train an open source and GPT models.
*  And so, what, six weeks ago, five weeks ago,
*  we put into the open source model
*  six weeks ago, five weeks ago,
*  we put into the open source community seven GPT models,
*  trained to the chinchilla point,
*  and we're one of the initiators in this recent push
*  to not close models, to not do what OpenAI did
*  and keep GPT-4 closed, to not do what Meta did with Llama
*  and have it with a really restrictive license.
*  We were able to cluster these machines
*  so that we could move extremely quickly
*  through a collection of GPT models
*  and that we could put them in the open source community
*  for everybody to use and use any way they want.
*  We used an Apache 2 license.
*  So if you wanna make money on them, please go make money.
*  It's amazing that you can create a supercomputer
*  out of 16 chips.
*  Is there a 256 chip version of that
*  or is there any sort of scaling problem
*  that you will encounter as you try to build clusters?
*  We've worked on problems past 192.
*  And for today, there's just not even workloads
*  that need that much.
*  Are you ahead of what the max workloads are?
*  Well, I think there are projects that we'll announce
*  over the next six or eight months
*  that use an enormous number of these machines
*  in some of the largest clusters on earth.
*  How many chips are you making on an annual basis?
*  How much do they cost?
*  Can I buy one?
*  This doesn't seem like something people would normally
*  buy one of, it seems more like a shared access model
*  would make more sense.
*  Nathan, if you would like a chip,
*  I might be able to find you a chip,
*  one that somebody dropped or something.
*  I'll take what I can get.
*  Look, we have customers around the world.
*  We have customers in Japan, across North America, in Europe.
*  We have customers in the military, at the government,
*  in large enterprise, among tech startups.
*  We have customers who deploy whole systems on premise.
*  We don't sell the chips, we sell the whole system,
*  the whole computer.
*  On premise, we have customers that use our cloud.
*  And so we've tried to think about how to meet customers
*  where they are.
*  Younger AI practitioners want everything in the cloud.
*  Big Pharma often has, or companies in the energy industry
*  often have extraordinarily proprietary data
*  that they like to keep on premise.
*  We have customers in both,
*  GlaxoSmithKline, Total, all customers of ours.
*  I wonder how abstracted away folks are from,
*  like if you're a developer,
*  if you're a machine learning practitioner,
*  like a GlaxoSmithKline, and you insist that,
*  we're not gonna send anything off premise,
*  so that's just a non-starter.
*  And then you have an option of like,
*  okay, we can go assemble our own GPU cluster,
*  or we can buy like one of the biggest chip ever in a system.
*  How is the experience then of actually doing
*  machine learning at this company change,
*  depending on which choice you make?
*  In both cases, you'll likely write in PyTorch.
*  In our case, you'll spend very little time
*  thinking about distributed compute with the GPU.
*  You will spend a lot of time
*  thinking about distributed compute.
*  In the GPU's defense, if you wanna do rendering
*  or some other graphics work,
*  you have that ability with those GPUs.
*  With us, you don't.
*  We're gonna be a dedicated AI machine.
*  We're likely to be tens or hundreds of times faster,
*  depending on how many GPUs you replace.
*  So your iteration time for your research
*  will be vastly accelerated.
*  Is there a sort of parallel,
*  like contention, I guess, question as well?
*  Like, let's say we have one system
*  and we have 10 machine learning practitioners.
*  If they have a GPU cluster,
*  they can sort of split up the GPUs.
*  How do they divide access to your system?
*  In a time division.
*  I mean, I think if you have 10 and you're using a cluster,
*  everybody's got a tiny little bit of a cluster
*  and everybody's, you know,
*  and everybody's drinking coffee
*  waiting for their training runs to complete.
*  I think on our machine,
*  each training run will be very, very fast
*  and the results will be, for everybody,
*  will be completed sequentially,
*  but in a tiny fraction of the time.
*  This is an extraordinary time in AI.
*  And I think the last six months
*  have been a veritable revolution.
*  And I think we are still very much at the beginning still.
*  Mostly what we're doing today
*  is replacing things we already do
*  a little bit more efficiently, right?
*  We already write copy.
*  We already generate stories.
*  We already do many, many things.
*  We haven't got to the point yet where we do new things,
*  things that we've never done before,
*  where we reorganize around AI.
*  And historically, that's when you get this
*  unbelievable burst of a productivity gain.
*  Do you see giant chips like this on the edge at some point?
*  You know, how far does this go?
*  Like, is my, you know, future Tesla
*  gonna have kind of, you know,
*  one big world record holding chip in it?
*  No.
*  I think, you know, each problem
*  has characteristics that the solution needs to meet.
*  The problems of the edge are one of distribution, right?
*  You have lots of cars.
*  They're all gonna send data back somewhere.
*  That's where you're gonna have the big chips, right?
*  They're not gonna be in your cell phones,
*  but the training that the system is doing,
*  the cell phones, inference engines use
*  are gonna be done somewhere with an extraordinary amount
*  of compute and an extraordinary amount of data.
*  That the problem with the edge with regard to training
*  is the edge doesn't hold a lot of data.
*  The edge almost by definition is storage light.
*  And so the right thing for the edge
*  is something very different
*  than the right thing for the core.
*  And the problem of training
*  is a profoundly data intensive problem, right?
*  That's not a good problem for the edge.
*  The problem of inference is an extremely data light problem,
*  right?
*  In image out classification,
*  in prompt out a thousand, 10,000 tokens.
*  I mean, that's tiny, tiny, tiny.
*  That's a good edge task.
*  Where are you gonna hold a trillion tokens on the edge
*  for training, right?
*  Where are you gonna hold the compute power equivalent
*  to 16, 32 of our systems or tens of thousands of GPUs?
*  That's what you want for training.
*  And so I think just like today in the data center for x86,
*  you have big honking servers
*  that are doing the work in the data center
*  and you have small efficient compute in your phone,
*  it's ARM, and they divide up the work, right?
*  Some of the work is done on your phone
*  and sometimes it goes back into the cloud,
*  works on a big server, brings down the answer.
*  That model is exactly what's gonna obtain
*  in the AI world as well, my guess.
*  So maybe I may have a misconception
*  and maybe you can correct me on it,
*  but what I was kind of thinking in terms
*  of the edge is my understanding is like
*  the memory requirements for training are usually like
*  either two or four x or something,
*  the memory requirements for inference
*  because you have to like keep track
*  of the back propagation gradients,
*  which you don't have to do at inference time.
*  But it still seems like for my like edge device today,
*  or even if I wanna go do like a collab notebook
*  on collab pro, I can only load so big of a model.
*  And I guess what I'm kind of wondering is like,
*  you know, is there something I'm missing that,
*  because I'm envisioning a big chip
*  that kind of solves this memory problem,
*  being able to do like big model fast,
*  you know, in a loop inference on the edge,
*  which is kind of, you know, you have to have that loop
*  if you're gonna have like a robot or a car, right?
*  There are two different classes of inference problem.
*  One is the autoregressive inference problem,
*  and the other is a classification problem.
*  Autoregressive inference is much, much harder.
*  And you have to, it requires vastly more compute.
*  The problems of self-driving cars are one of classification.
*  Child, dog, pile of leaves, right?
*  Your car's gotta behave differently
*  with that classification.
*  That problem can be done extremely quickly
*  in a very small chip after a great deal of training.
*  And that's why Elon keeps bragging about
*  how much compute he has in the data center.
*  The problem of autoregressive inference,
*  which is chat, GPT and others,
*  is so hard and challenging that, you know,
*  Microsoft and OpenAI are capping your ability to use it
*  after they set it out for free, right?
*  Because that actually takes a fair bit of compute.
*  So most of what robots do is image,
*  and is a classification problem,
*  which can be handled very quickly in a very small chip.
*  Most of autoregressive inference
*  is still being done in the data center,
*  and is a big opportunity for big chips like ours,
*  and requires big clusters of GPUs as well.
*  So do you guys offer managed inference type service today?
*  Not yet, but it's around the corner.
*  I have a couple kind of usual fun closing questions.
*  If I could throw a couple of quick hitters at you.
*  First, just your favorite AI products and experiences
*  that you'd recommend others check out.
*  I'm awed still by the power of chat GPT.
*  I like Replit for code generation,
*  and the work Amjad's doing is really interesting.
*  Dave over Jasper, he built a nice company,
*  and using Jasper for brand voice is, we use it here.
*  It's really, really interesting application.
*  Those are all consumer applications.
*  We have non-consumer applications
*  that I'm extremely proud of.
*  Our work was part of the work done by Argonne National Labs
*  that won the top paper at the last Super Compute Show,
*  in which we were predicting, based on COVID virus DNA,
*  we were predicting mutations.
*  And that was really cool work,
*  and may well be the foundation for vaccines
*  that cover more potential mutations.
*  There's work being done at Galaxus Smith Klein
*  in epigenomics.
*  There's this collection of work that people don't see
*  because it's not consumer focused,
*  that I think is extremely powerful,
*  and we'll have a profound influence on how we live.
*  Yeah, the intersection of AI and biology
*  is a very difficult dynamic to predict,
*  but it definitely is gonna have a huge impact.
*  Speaking of which, our second quick hit closer is,
*  let's imagine a hypothetical situation
*  where Elon's got neurolinks in 1 million human heads.
*  General safety profile looks pretty good.
*  There may be some noise on the internet about it,
*  but best received wisdom is it's clinically approved.
*  Would you be interested in getting one at that point
*  so you could control your computers with your brain?
*  I think the problem that Elon's identified,
*  and I know Elon, he's right.
*  The problem is one of input and output.
*  That one of the really interesting things about our brain
*  is the amount of IO we can deliver to it through our eyes.
*  And it is vastly more than we can figure out
*  how to deliver even a big chips like ours.
*  And so what he's trying to solve,
*  the problem he's trying to solve for there is an IO problem.
*  And I think that's enormously interesting.
*  I don't know if I would leap in it.
*  I'm sort of happy with my human limitations.
*  But the notion that one of the things
*  that makes the brain so interesting
*  is its ability to get data to it at a vastly higher rates.
*  Orders of magnitude, hundreds of orders of magnitude,
*  maybe thousands of orders of magnitude,
*  faster than we can deliver information to a chip.
*  And deep down, that's the insight I think he's chasing.
*  And that's what Neuralink is about.
*  And I think that formulation of the problem
*  that we have all this compute on chips
*  and the binding constraint is IO.
*  And when we look at our brains,
*  we can get so much data in through our eyes,
*  through tactile, through sense, smell and taste,
*  unbelievable how much info we can deliver to the brain.
*  And if you look at babies, that's what they're doing.
*  They're touching things, they're tasting things,
*  they're looking at the world.
*  And that's just, their brains are being inundated with data.
*  And I think the recent work in large language model
*  shows just how important that data is.
*  That it's not about parameter count,
*  it's really about data and the quality of data.
*  I also think of it in terms of
*  sort of potentially unlocking communication
*  direct from the brain and a sort of,
*  or to the brain in a higher dimensional space
*  than the language bottleneck that we can kind of speak with.
*  The language bottleneck is a problem.
*  It takes a lot of words to describe a picture.
*  And what you're thinking about there is,
*  you're converting experience
*  into a relatively simple bit stream words.
*  Whereas images, smells, taste,
*  sensations are vastly richer.
*  And so I think your formulation is a very reasonable
*  and absolutely accurate formulation of this IO problem,
*  of how we get away from the relatively simple stream
*  of vector characters.
*  Okay, here's a far out one.
*  I don't know where consciousness comes from in a person
*  or why I have any subjective experience.
*  And I just Googled quickly,
*  100 trillion synaptic connections in the human brain.
*  I compare that to your 2.5 trillion transistors.
*  And I really wonder, why is everybody so quick to say
*  that we are so confident,
*  that there's nothing that it feels like
*  to be these new extremely complicated substrate
*  that somehow percolates up this sort of pretty interesting
*  and seemingly intelligent behavior.
*  Do you have an intuition for either like,
*  why we should be confident in feeling
*  like there's no subjective,
*  and I don't mean a human like subjective experience.
*  If there is a subjective experience,
*  I expect it to be very alien and weird,
*  but people are so confident that there's none.
*  And I'm wondering, do you have confidence that there's none?
*  If so, can you tell us why,
*  or are you open to the possibility that your chips may
*  or chips plus algorithm may feel something?
*  I'm confident I have no idea.
*  Really, and I think what's actually happening
*  underneath all this is a lot of addition and multiplication.
*  Right, that's what sparse linear algebra is, right?
*  Can extraordinarily complicated things be built up
*  on extremely simple foundations?
*  I think we know they can.
*  I think we know they can.
*  Would we know what self-awareness for a machine would be?
*  It's not clear to me, we would know it.
*  You know, economists used to say
*  humans behave in self-interested manner.
*  And then, and they're rational.
*  And then others came along and proved they're not.
*  But the truth is, as a rule of thumb,
*  most of the time people are pretty self-interested.
*  It's an okay way to understand behavior.
*  I don't think we're gonna know or understand it,
*  but I think we'll have some rules of thumb.
*  You know, it will behave as if it was thinking like a human.
*  It will behave as if it had feelings.
*  Whether it actually had feelings or not, I have no idea.
*  And I don't even know the right framework
*  for attacking that problem intellectually.
*  But I think there's a big difference between saying
*  humans do rational calculations
*  about self-interest constantly, which we know they don't.
*  They're thinking as biased, they don't.
*  They don't.
*  And saying that, look, as a rule of thumb,
*  you get a pretty good result if you estimate
*  people's behaviors about self-interested.
*  I think it'll sort of be the same,
*  that we will see behaviors we recognize.
*  We will probably mis-tribute it, as the economists did,
*  to a feeling, to self-interest.
*  It will be a reasonable rule of thumb.
*  And that's sort of the way I think about it.
*  But Nathan, there's certainly many people
*  wiser than me on this topic for you to have on your show.
*  People who've thought more deeply about it,
*  who weren't encumbered by trying to build a chip
*  and a system and a software stack and make it easy to use
*  and build big clusters and run big models,
*  who really think about these problems holistically.
*  Well, it's a tough one.
*  I don't know that there's actually all that many people
*  with a read on this out there.
*  So I'll just ask you one final question,
*  which again is kind of pushing a little bit beyond
*  your wheelhouse of the chip business that you've built,
*  which this has been a phenomenal angle
*  on that whole industry.
*  And also just really deep dive into,
*  at least from our standpoint,
*  deep dive into all the problems.
*  I know you guys go a lot deeper still yet, of course.
*  But just zooming out and trying to take stock
*  of where we are in this seemingly kind of
*  phase change moment.
*  What are your biggest hopes for and fears for society
*  at large as AI really comes online?
*  There is tremendous opportunity to change the way we work,
*  live and play.
*  And with every powerful technology,
*  there are ways for it to be used for grand evil.
*  And facial recognition can simultaneously be used
*  to persecute minorities.
*  And it can be used to identify terrorists.
*  I think we have to remember to compare our technologies
*  against not idealized versions, but actual reality.
*  Humans are terrible drivers.
*  We kill other humans all the time.
*  The goal of self-driving cars is not
*  to avoid killing people.
*  The goal of self-driving cars is to kill a lot less people
*  by driving.
*  And I think that's really important.
*  We are, despite 50 or 70 years of sort of thoughtful effort
*  to reduce biases in our decision-making,
*  people are still extremely biased in their decision-making.
*  It's not surprising that our first models are biased
*  in their decision-making.
*  But for me, I think it's easier to correct algorithms
*  than it is to correct people.
*  And once you correct the algorithm, they stay corrected.
*  Whereas people tend to regress.
*  And so I think there is opportunity for good and evil.
*  I think like the web, which sort of began dashing
*  into pornography and into the dark web
*  and the rest of the benefits sort of caught up
*  some years later.
*  I think the opportunity for AI to be used
*  for thoughtful fishing, for sort of painful scamming,
*  for oppression is real and large
*  and has to be thought through carefully.
*  But I think on balance, I think this technology
*  will fundamentally improve the way we live, work and play.
*  And I think that that is the case for everything important.
*  There is no important technology that can't be used for evil.
*  I wanna thank you for having us, Nathan.
*  I think it was really fun conversation.
*  Clearly, I do a few of these
*  and your questions were really thoughtful
*  and fun to ponder.
*  Andrew Feldman, thank you for being part
*  of the Cognitive Revolution.
*  Omniki uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work,
*  customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it
*  and I recommend you use it too.
*  Use Cogrev to get a 10% discount.

---
Date Generated: May 09, 2024
Transcription Model: whisper medium 20231117
Length: 6738s
Video Keywords: []
Video Views: 668
Video Rating: None
---

# TinyGPU, Massive Learning, with Adam Majmudar
**Cognitive Revolution How AI Changes Everything:** [May 06, 2024](https://www.youtube.com/watch?v=WulkHHZVbf4)
*  So these special registers are registers that you can't write to.
*  The GPU itself handles writing to them.
*  And that means that the GPU itself supplies this code execution environment with like,
*  Hey, you're this block number.
*  There's this many threads in each block and you're also this thread number in this block.
*  And so the hideable job of the GPU now is like, okay, well, how do we manage how to
*  divide up these threads into the available compute cores, wait for them to complete their
*  job and then give them more jobs when they're done completing their work.
*  The analogy is like if aliens come to Earth and they find the computer, like, how are
*  they going to understand it?
*  Are they going to break it down and look at all the connections, the transistors and see
*  what's happening?
*  No, they're not going to understand it by doing that.
*  They have to come to some understanding of their own and then test it against the
*  computers that they have.
*  It's a bit of a massively over complex analogy for going through a GitHub repo.
*  Hello and welcome to the cognitive revolution, where we interview visionary researchers,
*  entrepreneurs and builders working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life and society in the coming years.
*  I'm Nathan Benz joined by my co-host, Eric Torenberg.
*  Hello and welcome back to the cognitive revolution.
*  Today, I'm excited to share my conversation with Adam Majmodar, creator of the tiny GPU
*  project, in which Adam set out to speed run the creation of a GPU from scratch in just a
*  few weeks, despite having no previous experience designing GPUs.
*  The result is truly remarkable and a great educational resource for anyone who wants a
*  better understanding of the foundational technology on which today's frontier AIs are
*  trained and run.
*  In this episode, Adam walks us through the GPU architecture layer by layer from the tools he
*  used to learn and design to the GPU programming paradigm of single instruction, multiple data
*  to the process of hardware implementation and verification in a way that I think will be
*  illuminating for just about anyone who's not already an expert in this critical industry.
*  Along the way, I think this episode has a couple of big picture lessons to teach us as well.
*  First, it's a powerful reminder of the multi-generational tech stack that all of today's
*  A.I. breakthroughs are built upon.
*  Adam was able to do this work thanks to the compounding progress in chip design and design
*  automation software that thousands, if not millions of engineers have delivered over decades.
*  Second, it shows just how much A.I.
*  itself is accelerating the learning process for individuals.
*  Adam relied heavily on Chet GPT and Claude to help guide his learning journey whenever he
*  got stuck. He would propose hypotheses to the A.I.
*  and get feedback, enabling him to make much faster progress than learning solely from static
*  resources. I found it particularly interesting to hear him describe today's leading models as
*  having a sort of intuition for science and engineering, which transcends online resources in
*  important ways. I've experienced this myself most recently while trying to bring myself up to speed
*  on the intersection of A.I.
*  and biology and separately when planning a Mac OS app.
*  But I think it's a truly important capability, which when combined with the agentic capabilities
*  that we expect from next generation models, suggests potential for genuinely transformative
*  impact in the near future.
*  Finally, beyond the technical content itself, I came away incredibly impressed with Adam as a
*  thinker, builder and communicator.
*  The depth of understanding that he demonstrates reflects a level of curiosity, resourcefulness and
*  relentless drive to figure things out that will surely enable him to make a real impact in
*  whatever domain he decides to tackle next.
*  Personally, I came away from this conversation with a much stronger intuition for how GPUs
*  actually work under the hood, and I'll bet this episode will scratch a lingering itch for many,
*  many people. One note, if you're listening to the audio only podcast feed, we do use a screen
*  share in this episode and refer to a number of diagrams and code samples from the tiny GPU GitHub
*  repository. With that in mind, I would recommend the YouTube version of this episode if that's
*  convenient for you, though we'll also have a link in the show notes in case you want to follow
*  along on your own.
*  As always, if you're finding value in the show, I'd appreciate it if you'd take a moment and share
*  it with friends. And if you do have any feedback, you can reach us via our website, cognitive
*  revolution dot AI, or by DMing me on your favorite social network.
*  Now, without further ado, please enjoy this whirlwind tour through GPU architecture with tiny GPU
*  creator Adam Majmodar.
*  Adam Majmodar, creator of the tiny GPU project.
*  Welcome to the cognitive revolution.
*  Thank you for having me.
*  I'm excited about this. So you've created this project that really caught my eye called tiny GPU
*  in which you describe yourself as having no prior experience creating GPUs, but nevertheless set
*  out to speed run creating one from scratch in just a few weeks.
*  And I imagine you have learned an unbelievable amount from doing that.
*  I've learned quite a bit just from following your progress.
*  And hopefully the audience will be able to learn a lot from following the results of what you did as
*  well. You want to start off by just introducing yourself a little bit and telling us how you got
*  this crazy idea?
*  Yeah, sure. I'm Adam.
*  I've been working on a company called Third One for the past three years.
*  Started in college and worked on it full time during college and then worked on that for a couple
*  of years in Gapier.
*  And I just stopped working on that recently.
*  And then now I've been doing a couple of deep dives, which I've been sharing on Twitter on
*  different industries that are the overlap between what I think are going to be defining
*  technologies within the next few decades and areas that I've had demonstrated interest in my whole
*  life. And my goal has been how fast can you get to a point of technical competence and industry
*  competence? So the kind of two sides to it.
*  It's not just like the technical side of things.
*  It's actually like understanding the industry and how things are going right now, understanding
*  tailwinds and also understanding the opportunity landscape specifically for young people.
*  Plus, tiny GPU happens to be the result of the technical part of that, which is I just finished
*  my deep dive on chips.
*  I'm now applying to use other ones.
*  But during that deep dive, my goal was basically learn the entire engineering stack of chips and
*  computation and history of it.
*  And part of that process was basically two two week sprints.
*  The first two weeks sprint was can I learn how to make a chip all the way from EDA, which is the
*  electronic design side, and then understand how fabrication works and understand the
*  architectural side all in two weeks, which is traditionally something that people can spend
*  two plus years in college to do.
*  And my belief was basically you can cut it down about 100x time wise.
*  Of course, you're not going to be learning the same thoroughness as what other people are doing.
*  But the question you ask yourself is, is the thing that matters the thoroughness and the
*  quantity of stuff that you learn?
*  Of course, people who spent three years on this know way more than me about lots of different
*  detailed stuff. Or is it that there's some not really 80 20, it's more like a 99 one where it's
*  like one percent of the stuff is actually most of the important value.
*  And if you can figure out how to extract that quickly, then you get much more value out of the
*  learning. So that was the context behind the project.
*  And so I did the two weeks spent that time learning how to make chips.
*  And then by the end of that, I formed this intuition, which is like, OK, now that I know this,
*  what's a really cool project I can build that will teach me a lot.
*  It will also be fun.
*  It also has potential to be interesting and valuable to people.
*  And given the whole wave of stuff around AI, you have GPGPUs and tensor crossing units and all
*  kinds of AI accelerators and also just a whole loop around ASICs.
*  I thought it would be interesting to dive into the GQ as a foundational way to learn all of that.
*  So that's the context and the content.
*  Love it. Well, let's get into it.
*  One of the challenges that you noted right up front that I hadn't really considered, but
*  definitely makes a lot of sense is that there aren't a ton of great learning resources out
*  there for things like this because a lot of the technology is proprietary.
*  That includes designs.
*  I've done some of my own prep in realizing that like Nvidia has not published every layer of their
*  technology stack.
*  And so there's questions even to this day about how some of the most advanced GPUs work in some
*  critical ways and also design tools, the software packages, that those are not always super easy to
*  come by either.
*  So maybe for starters, just characterize that landscape a little bit and tell us what learning
*  resources and software tools you were able to avail yourself of.
*  So I'll contrast this to CPUs, which is a much broader landscape and there's a lot more learning
*  resources.
*  And the reason is probably because of how old it is.
*  The CPU is basically the oldest invention in terms of actual useful computing.
*  Lots of people will disagree with that statement, but the core concept out of it.
*  And because of that, there's so many learning resources.
*  If you take an architecture course in college, you'll learn how to build a CPU.
*  There's basically tons of courses around it.
*  And what it means to have it fully documented and taught is not just how it works at a high level.
*  Oh, here's the different parts.
*  There's the data memory and program memory, high registers.
*  It's actually like getting into the control signals in the low level and understanding how
*  machine language translates into stuff happening, the CPU and stuff like that.
*  So it's like the connection between the software and the hardware level.
*  And that's really what it takes to be able to completely replicate it.
*  If you want to build a CPU from scratch, at the end of the day, you need to understand
*  how you can actually program it and how you can turn that into low level signals in your design.
*  And so in contrast with GPUs, there's essentially nothing at that level.
*  So what you'll find is if you go look for NVIDIA and AMD GPU designs, you'll see high
*  level architecture and we'll show you all the different pieces of them.
*  And of course, it's a little bit ridiculous to even expect something at the control signal
*  level for designs that large.
*  But actually, there's no resources that dumb these things down into the simple elements.
*  That you can at least try to implement something yourself.
*  Now, one person pointed out that Intel actually does have three low level diagrams.
*  Again, you wouldn't really use it for learning because it's an actual GPU.
*  So it's not really too easy to understand.
*  And that can be one interesting approach for people.
*  Gotcha.
*  OK.
*  What about on the tool side?
*  I assume you were not able to use all the same software platforms that folks add in
*  video or at AMD, maybe more at AMD because I believe there's stacks in a more open source.
*  But what were you able to use to actually create these things?
*  Yeah.
*  So certainly my stack is completely different from all the real players.
*  So the thing is, in this space, the EDA tooling, like the electronic design automation,
*  which is what you use to actually convert your architectural designs into an actual
*  chip layout and also do a lot of stuff optimizing your design, which is basically the entire
*  complexity of the process.
*  Those things cost like hundreds of thousands of millions to millions of dollars, like per
*  seat and per company.
*  And so an individual can basically never actually use those things.
*  And in terms of shipping and actual production quality layout, basically need those.
*  They have a complete mode on this industry.
*  The nice thing, though, is there is this project funded by DARTA within the past, I'll say,
*  five to 10 years.
*  Not sure I'm exact number.
*  Called OpenRoad.
*  And it's an attempt at making an open source EDA software.
*  It's obviously way worse than those real production ones in many ways.
*  It's not feature complete.
*  But for simple cases, like what any individual would do or install businesses would do,
*  it's completely a suggestion.
*  And then the last piece that made all this possible is that, again, in the past decade,
*  there's this company called Skywater.
*  And they basically made this open source EDA stat for their own process node, which means
*  that they have their own foundry that produces chips at the 130 nanometer scale, which is
*  just like the size of the gates and the transistors they make.
*  And they opened it with this thing called eFabless, where multiple people can basically
*  pay a much smaller amount to get like 100 chips for this process.
*  And that costs like 10K.
*  And this other group called Tiny Tape Out, advertise the costs.
*  So they'll be like, OK, 100 people cannot pay for a tiny slot.
*  I will put like 100 projects at each of these chips.
*  And so because of this incremental cheapening of everything, it now becomes possible for
*  someone like me or others to use that, basically the Skywater process node to make a chip.
*  And then you use something built on the Open Road stack called Openlane.
*  It's basically just Open Road specifically for that Skywater stack.
*  And now all that's open source.
*  Obviously, there are some synopsis accadem such as the real production tools, but completely
*  functional for what I would want to do or like any individual hobbyist.
*  Cool.
*  So we'll maybe get back to the sort of hypothetical manufacturing side toward the end once we
*  get through all the design considerations.
*  But do I have it right that at the end of this,
*  you have a micro tiny, I should say, GPU that could be included alongside like 100 other
*  projects on one chip.
*  And then that chip would be what you would actually get if you ordered through the process
*  you described would be like a chip that has your design plus 100 other designs all on it.
*  And then everybody just shares in the production cost, but also gets access to one another's
*  designs.
*  Is that how that's working?
*  And I'm probably actually going to do that.
*  The thing that I mentioned about tiny tape up created by the sky day, he's basically like
*  a goat of making ASIC accessible nowadays.
*  You can find him on Twitter and you can find his course which is zero to ASIC.
*  He has basically made this process where they'll buy up one of those e-fabulous $10,000 slots
*  where you have to get 100 tips, you have to pay 10,000.
*  And as I said, they'll allow 100 people or a big group of people to submit their projects.
*  And for example, yeah, exactly what you said is I could submit this to that, which I will do.
*  And I'll get the chip.
*  And the cool thing is I'll get the chip and I'll be able to play with my project,
*  but I'll also be able to play with the projects of all other 99 people who submitted
*  and what just says the cool byproduct of it.
*  That's awesome.
*  Other than for learning, what is this good for?
*  Are there projects that people are actually, where they're building things where they can't
*  get something that meets their requirements that they can only get this way?
*  Or is this really all for the love of the game and the fun of the DIY?
*  Now with these stacks opening and the tool becoming better,
*  that there might be like an interesting analog market or a smaller CLASIC market,
*  where at least you could do the initial prototyping phase of the stack.
*  I think in practice, there's not going to be huge businesses built on this.
*  I really began it will always make sense if we go to the real production stacks.
*  So I do think it's mostly hobbyists.
*  And I think the most interesting thing on the learning side is getting more college
*  students and younger people, just getting the intuition of this.
*  Since the industry was created and the engineering was much worse of popular
*  several decades ago, getting any generation to it is interesting given that there is
*  a whole landscape of a chips act and there's some geopolitical incentives there.
*  Yeah. Cool. Makes sense.
*  Okay. So let's get into the project itself.
*  One thing I wanted to just try to do upfront is figure out the scope.
*  When you say designing a GPU from scratch, there's like a lot of layers to the tech stacks.
*  Obviously you're not going all the way down to mining your own minerals.
*  So what was like the foundation that you said, okay, like this is deep enough down the tech
*  stack, but I'll count it as from scratch, but I'll still be able to use this kind of
*  foundation to build the plot.
*  Yeah, that's the pressure. So there's a couple of things.
*  First of all, obviously I'm not building the whole ED pipeline,
*  contractor, anything like that.
*  So the place where I really started since there along, which is where most design started,
*  which is basically called your register transfer level logic is just designing the
*  specific memory and the specific wires that connect up the chip to make all the logic.
*  And so designing something at that layer is the layer that I was targeting.
*  And then also more specifically, because that's very generic,
*  the architecture that I wanted to choose is obviously very nitpickable in the sense that,
*  okay, you have a giant GPU. There's like millions, thousands of features to this GPU.
*  The question is, what are you going to include?
*  And because the word GPU is an amorphous term nowadays, like it started out being
*  referring to graphics processors. Now people are still using it for lots of stuff that aren't
*  graphics processors, like transfer processors and other NL accelerators.
*  And so there's some blurry line in terms of what GPU counts as.
*  And so because of that, I set my goal of what do I want to focus on with this,
*  not as like graphics hardware or any of the specific things like that.
*  I'm more like, if you want to understand this kind of giant blob of areas that spawned from GPUs,
*  what are the core concepts you need to understand in order to be able to build on top of them and
*  understand little details? And then my goal is, can I create a foundation where using this foundation,
*  you'll be able to learn all of the important stuff. And by choosing that, it allows me to strip away
*  a lot of the complexities of some of the nuances of any little engineering decision.
*  If you're choosing to make like graphics hardware or any of the other specific things
*  and just focus on that, the fundamentals that I was talking about.
*  And so some people would disagree, right? Because it's a blurred line, some people will be like,
*  oh, that's not a GPU. It doesn't include graphics hardware or whatever. There's like
*  Netflix you can make everywhere. But at the end of the day, it's just a design decision
*  for the purpose of that product, which is like, how can you teach people how this stuff works?
*  Most effectively. Yeah, it makes sense to me. And no doubt these are super complicated.
*  It's often said these days that chip making is the most complicated industry in the world.
*  And arguably the most complicated thing that humans have ever devised to manufacture at scale. So
*  yeah, not surprising that you'd have to make some simplifying assumptions to pursue a project like
*  this. Hey, we'll continue our interview in a moment after a word from our sponsors.
*  AI might be the most important new computer technology ever. It's storming every industry
*  and literally billions of dollars are being invested. So buckle up. The problem is that AI
*  needs a lot of speed and processing power. So how do you compete without costs spiraling out of
*  control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure,
*  or OCI. OCI is a single platform for your infrastructure, database, application development,
*  and AI needs. OCI has four to eight times the bandwidth of other clouds, offers one consistent
*  price instead of variable regional pricing. And of course, nobody does data better than Oracle.
*  So now you can train your AI models at twice the speed and less than half the cost of other clouds.
*  If you want to do more and spend less like Uber, eight by eight and Databricks Mosaic,
*  take a free test drive of OCI at oracle.com slash cognitive. That's oracle.com slash cognitive,
*  oracle.com slash cognitive. The Brave Search API brings affordable developer access to the Brave
*  Search index, an independent index of the web with over 20 billion web pages. So what makes the Brave
*  Search index stand out? One, it's entirely independent and built from scratch. That means
*  no big tech biases or extortionate prices. Two, it's built on real page visits from actual humans,
*  collected anonymously, of course, which filters out tons of junk data. And three, the index is
*  refreshed with tens of millions of pages daily. So it always has accurate up to date information.
*  The Brave Search API can be used to assemble a data set to train your AI models and help with
*  retrieval augmentation at the time of inference, all while remaining affordable with developer
*  first pricing. Integrating the Brave Search API into your workflow translates to more ethical
*  data sourcing and more human representative data sets. Try the Brave Search API for free for up to
*  2000 queries per month at brave.com slash API. One of the things that you mentioned in your
*  Twitter thread that originally caught my attention was that the beginning of the exercise was a
*  real challenge in just prioritization, figuring out what really matters most. You came up with
*  three things that you felt mattered the most. We can get into each one in turn, but you want to
*  just give a high level of what those three things are and how you identified them, maybe a little
*  bit on what you decided to leave out. And then we can go deeper into each of the three. Yeah. So
*  the three things I chose are architecture, parallelization, and memory. And granted that
*  whole Twitter thread, although it was written colloquially, I'm not sure if you'll like to
*  read it out, but it's actually the result of hindsight. And so like all the architecture
*  design I chose for example, the design decisions that I put up front are actually the result of
*  me having gone through the entire process. I didn't have that intended foresight at the beginning.
*  But the reason I chose those things is because, and even maybe I've rephrased them to two really,
*  like architecture is not really saying much. When I met by focusing on architecture, it's like
*  what are the key elements of each piece of the GPU that are important to all GPUs? Like
*  different GPUs have different little specific elements tailored to their need. But one of the
*  things, again, going back to the foundations that you absolutely need to understand these concepts
*  in order to understand how this, the whole thing works broadly speaking. And so I broke that down
*  over time. Now I had the architecture diagram in my tweet and that was a good breakdown of basically
*  the most simple possible explanation of how GPUs work. And we can get into the specifics of that.
*  Now the other two terms were actually the more interesting parts. So I'll start with parallelization
*  because that's the one that is most obvious on the surface level. And that's, yeah, GPUs obviously
*  are built to do parallel computation. That's their whole utility. Basically in graphics are where
*  the rest of this graphics use cases in general and machine learning, they benefit a lot from doing
*  matrix map. And if matrix map happens to be element wise, in other words, computations on
*  individual elements don't depend on other elements, which means you can do them all at once.
*  And that's a whole reason why GPUs are useful. So the whole point of GPUs is instead of a CPU where
*  generally things are thought of as being executed sequentially, in practice this is exactly true,
*  but like generally you execute L at one, then two, then three, then four. And now you've done
*  this whole thing for clock cycles or for cycles of computation. Instead of the GPU, you just distribute
*  it out among a bunch of compute resources. And now you're accomplishing this all in a
*  much faster time period. Now, the interesting thing about parallelization, on the surface,
*  it seems like it's just, oh, you need to have a bunch of compute resources or like compute cores,
*  and then you can distribute these workloads across the compute cores. Actually, it turns out
*  a lot more trivial than some of the other difficulties. So there's one, the problem of
*  how do you distribute these workloads effectively with your resources and manage the resource
*  utilization effectively to maximize it. It's not a one interesting problem, but that happens on
*  like the hardware level. And then there's also maybe a more interesting thing, which is
*  what is the software pattern of parallelization? As in, how do you actually program these things?
*  It's one thing to make the hardware support this capability, but how do you actually make the
*  software easy to use for developers who aren't usually used to it? And that's arguably one of
*  the core problems that Nvidia solved in what made them win with the census day cap, but their CUDA
*  software designer is so good for parallel programming, probably by nature of how similar
*  and integratable it was into the previous stack that these developers who needed to use it were
*  used to, or to see. And so another interesting element to highlight there is since the program
*  side is so important, how does the programming pattern that people are so familiar with actually
*  get implemented in the hardware? So that was an interesting element of parallelization. So just
*  to break that down again, it was the two interesting things in parallelization were resource management
*  and resource utilization, and then software pattern to hardware. How does that get implemented?
*  And specifically the software pattern is called same instruction, multiple data. And that just
*  means that you're executing the same code on multiple pieces of data, like elements of the
*  matrix. And in hardware, it's called same instruction, multiple thread, which is just like the
*  hardware manifestation of that. And then the last thing, which is less obvious and more interesting,
*  maybe most interesting realization for me, and maybe it's more obvious than actually doing the
*  program to like GPU programmers, because it's actually like a first-party thing in, for example.
*  But memory management is really interesting to me. And the reason is because I've had a completely
*  wrong notion of memory management in GPUs. In fact, I didn't even realize how important it was
*  initially. This is the thing I was saying in my tweet, or George Hoss told me. I like randomly
*  read it to him and I was like, hey, can you give me feedback on my design? He's like,
*  dude, this doesn't like accomplish the whole memory management problem, which is the most important
*  thing. And what that is, is it would see initially that when you're thinking about parallelization,
*  the bottleneck on how much you can parallelize computation is how much compute resources you have.
*  In other words, let's say I want to do 100 major traditions at a time. That means I need 100
*  different cores that support addition. And it seems like that's the bottleneck. In practice,
*  it's actually not that at all. In practice, it's actually memory. Because in order to do 100
*  editions, yes, you need 100 compute units, but you also need to be able to read from 100 different
*  memory locations at once from the global memory. And global memory is bottlenecked on how much
*  bandwidth it has. And that bottleneck tends to be the limit because there's a pretty big latency
*  in terms of this is the unit wants to access memory, then it needs to send the request,
*  and then it needs to wait for it. And if all of these units are kind of access memory at the same
*  time, you may actually have more requests for memory than you have bandwidth in global memory,
*  which means that you need to actually manage all these requests in memory. And that causes like a
*  huge latency. And to rip a quote directly from what George Hoss sent to me, he said that GPUs
*  is largely the task of trying to work around memory lancies and hide them away at different
*  layers. And that's a lot of what the challenge GPUs really is about, which is why architecturally
*  they've had all these things to solve that like memory and for standard and then they also have
*  multiple layers of caches to prevent having to access global memory and share memory and all
*  kinds of other stuff. So memory pattern is another very important part of GPUs.
*  Okay, cool. That's a great over. Where do you think it makes the most sense to start
*  in terms of spiking down each of these three? I originally had architecture first, but based
*  on your description there, I might go parallelization first and then come back to architecture. But what
*  do you think makes the most sense? It actually might be easiest if we go in reverse over because
*  people are probably most familiar with software, right? So you could actually start with the
*  software side of things, the ISA software side, and then it'll work backwards until how this is
*  actually implemented in the hardware. You think that makes sense? Sure. I'll have you follow your
*  lead. I mean, define terms for us. ISA is instruction set architecture. Exactly. Yeah. I was
*  confident about the instruction set. I didn't know the A actually there. So this part might be a bit
*  challenging to do without video. But I think almost all of this art is going to be near impossible to
*  do without video. So that's the caveat. But it's going to be really challenging to talk about
*  different instructions and the actual code and stuff like that, which I think is important to
*  understand it. Let's do this. I'll share my screen. I've got these notes up and I can, I'm right on
*  your GitHub page. So, okay, cool. Let's just try to describe it, talk people through it. If you want
*  to get a clearer view of this, we'll have the video on the YouTube version. Yeah. So let's scroll
*  down to the kernel system. Yeah. Perfect. We can do Matrix Edition. So if you just scroll up a bit.
*  Yeah. That's perfect. Okay. So the best way to start with understanding this whole system is by
*  understanding the software pattern, just because that's generally most familiar to people, easiest
*  to see the layout of what's happening. And so generally the way you think about GPU software is
*  it's the SIMD pattern, which is same instruction, multiple data. And so all that means is you're
*  just going to write one instruction. You're not going to do any loops or anything to be like,
*  okay, execute this instruction on all this different data. You're just going to do
*  an instruction that's basically invariant to the data that it receives. And what's that, what that
*  means is your code is going to take in some data, it doesn't know what the data is. And based on
*  that data from, let's say two different matrices, it's going to perform a computation on the data
*  to get the element of the resulting matrix and it's going to put that back in memory.
*  To take a concrete example of this, we can say Matrix Edition, which is probably one of the most
*  simple GPU use cases. So let's say we have two one by eight matrices, which means each matrix has
*  eight elements and let's call them matrix A and B. And all we want to do is quickly compute
*  the addition of these matrices, which we'll call matrix C. So let's say that
*  matrix A and B are loaded into memory in elements zero to seven for matrix A and then eight to,
*  what is that, 13, eight to 15 in for matrix B. And we just want to put matrix C, the result of
*  this addition, into elements 16 plus of memory. And one thing you could do in a CPU is write a
*  program and that program is going to take, like in a for loop, it's going to be like, okay, four i
*  less than eight as in like for each of the eight elements, add up the element for matrix A and B,
*  put that into the element in matrix C, and we're going to do that as in take eight cycles,
*  like eight iterations of the for loop. And so that's one way to do that sequentially.
*  Now, alternatively, what you could instead do is write this thing called a kernel, which is a GPU
*  program. And this kernel is just going to handle adding up one pair of elements in the A and B
*  and putting it into one slot in matrix C. And so we'll say this kernel is going to take the i-th
*  element of matrix A and B, add them up, and then put it into the i-th element of matrix C.
*  And so the actual code for that's pretty simple, I'm sure everyone can imagine what that's like.
*  So you're going to basically read some global memory, the base address of A plus the i-th element,
*  which is just like getting the element from A, you're going to take the base address of B,
*  get the i-th element, read it out, add it up, and then put it into C there. So actually the program
*  itself is very straightforward and there's not really any GPU element right there. So the main
*  thing with the GPU is you just want to tell it how many times do you want to execute this instruction
*  and on how many different values of i do you want to execute on them. So in this case, we want this
*  to be from the 0th to the 7th element of each matrix, there's an 8 elements, so we want 8
*  different values of i. And that means that, and that's just because we want to add up the 8
*  different elements of the matrix. We're going to call each of those times where we need a separate
*  execution of this code, that's going to be called a thread. And a thread is just executing the same
*  code again on multiple different parts of the matrix. And for this code, all we have to do is
*  specify what each thread is going to do, which is just going to basically just read two addresses
*  and then have them write an address. And there we're just going to run 8 of them. And the question
*  is, when you run 8 of these threads, let's say we now have 8 of these exact same pieces of code
*  running in our GPU, let's just say somehow we've accomplished that. The question is, how do you
*  actually get each of these threads to do something slightly different? They're all running the same
*  instruction, but you actually need them to be able to perform it on separate data, like the
*  different elements of the matrix. And so what you need to do is somehow in the actual hardware
*  of the GPU, you need to make each little area that's executing one of these kernel codes,
*  you need each little area to know something about which thread it's executing. Is it executing the
*  zero thread? Is it executing the second thread or whatever? And if you have a way to do that,
*  then within that hardware, the hardware can know something about its own context. So let's say the
*  hardware knows which thread it's executing. Now the hardware can say, hey, there's this instruction
*  here that's supposed to load some data in from memory. The data that I want to load in is actually
*  based on which thread is being executed here. So if I'm currently executing thread number zero,
*  I want to load in the zeroth element today and zeroth element of B. If I'm trying to execute
*  thread number one, I'm bringing the first element of each one, blah, blah, blah, and I want to store
*  it in the first element of C. And so that is the most important thing here. So the two important
*  things are, one, we're writing some code that just is meant to be executed by a single thread,
*  and then we're going to specify how many threads to execute. And the second important thing here
*  is these special values, which are going to be local in the hardware. So each time a thread is
*  getting executed in hardware, they have some broader context about what's going on here.
*  And so if you look at those, for people looking at C, there's these values called block index,
*  block dimension, and thread index. And this will probably be familiar to people who are familiar
*  with CUDA. Obviously there's more complexity in the actual pattern. But basically the way this
*  works is that when you have tons of threads that need to be executed for something, you're going
*  to group these threads into batches that are basically executed together on a single compute
*  unit. And those batches are called blocks. And so let's say our block size is four, which is what
*  it is on my current GPU design. That means that batches of four threads are going to be executed
*  together. And so whenever these things are executed, basically what you want to know is
*  which block number is currently being executed. And then within that block number,
*  what is the thread index in that block number? So that means that the threads are each going to have
*  an index from zero to three for each block because there's four threads per block. And then let's say
*  we have 10 blocks being executed. So now if we're on block three, how do we get the current thread
*  that's being executed? Very simply, we're just going to multiply the block ID three by the number
*  of threads per block. So now that's like 12. So that means that there's 12 threads that have already
*  been executed in the previous three blocks. And then we're just going to add the thread ID. So now
*  we know we're on the thread number 12, 13, 14, 15. And now those threads are pulling the receptor
*  data they need to commemorate. And so that is how the STEMD architecture, like programming pattern,
*  is implemented in programming. And then we'll talk about how that's implemented in the hardware
*  and it's very simple. And that's the core understanding you need to know. Some kind of
*  what's the kernel programming pattern. And in terms of this as an asterisk, like how do I decide
*  what instructions to include in my ISA? As you can see, like I'm trying to make it as minimal as
*  possible. And so really my decision function there was basically what are the minimal set of things
*  I could implement. In other words, make some cool useful use cases. And so matrix addition,
*  matrix multiplication were the most obvious things there. And so the instructions I chose are
*  basically just what's actually needed to support those, which is just basically some basic arithmetic,
*  loading and storing data from memory, because that's how you basically get your inputs and
*  then store the result of your computation. And it costs just for some convenience, but yes.
*  Cool. That was all quite well said. So just to try to summarize quickly back,
*  I'll go back to the block code thing. We'll come back to the instruction set. When you look at this
*  block of code, the key thing to understand is this code only executes the addition of one element
*  from within the arrays that are going to or the matrices that are going to be added together.
*  And so the key trick is you have to write the code in such a way that it can take in as a variable
*  which position are you in, and then handle everything else just based on that one variable
*  that the hardware will actually feed in at runtime. So everything is going to be the same,
*  except for what position you're in. And then that will determine the offset of the memory,
*  which will determine what value you load in, which will determine what value you ultimately
*  calculate and therefore what value you're going to put back into which position in memory.
*  All of that is determined by what position you are in the broader array of computation.
*  And you can think of that as in your case, you've got a one by eight, but obviously you could get,
*  I believe the current GPUs go up to like three dimensions of.
*  Yeah, there's like, yeah, you want to give us just a little bit of flavor as to how this kind of
*  gets more complicated from here? Yeah. So in actual GPUs, first of all,
*  they have more than just block index, block dimension and thread index to identify thread.
*  There's like a couple more dimensions of just like different groups of batching that basically
*  have to use every single dimension to identify what thread you're in. And then some other
*  interesting things. So I basically just captured the most simple piece of GPU programming here.
*  In reality, there's a couple other very interesting and important things. So first of all,
*  when you're loading and storing data, there's something that we'll maybe get to later, but
*  by nature of how GPUs have different layers, different levels of memory, and they have shared
*  memory, which is shared between an entire block with threads, which means that four different
*  threads can actually store stuff and read stuff from the same location. It's called shared memory.
*  And then each thread also has its own dedicated memory called a register file. That's important.
*  And so one complexity that I didn't implement here, which is there in real GPUs, and it's
*  very important for actual use cases, is that you can actually choose which memory you're putting
*  stuff in. So my pattern, there's only two types of memory you interact with. All of these MUL,
*  ADD, COMP, all these instructions, everything that has like an R in its parameter. So it'll be like
*  multiply R0, R2, R3. That's operating on registers for each thread, which means that stuff is all
*  just specific to a single thread, the thread that's currently executing, and it's storing
*  stuff in these local register files that has local data. And it's basically just performing
*  complications on the register values. And then there's the load and store instructions, which is
*  either loading data from global memory into the register or storing data from the register into
*  global memory. There's really only two levels of memory happening here. In a real GPU, you have
*  separate instructions that are going to let you interact with registers, global memory, and also
*  shared memory, and there are also layers of caches. So that's one thing. Then one other interesting
*  thing is in real GPU programming, you have the ability to synchronize different threads with
*  each other with barriers, which means that because of the necessity of shared memory, that means like
*  let's say four threads, they want to store something in this shared area and then access
*  it from each other. But what happens if one of the threads is ahead of the other? In other words,
*  one thread gets to some step and the other threads are not there. And now what if this thread is going
*  to read some data from the shared memory? Well, if it's going to do that, it needs to make sure
*  that the other threads are at the same point. Otherwise, it can have that corrupt data or maybe
*  the data is not ready yet to be read by that thread. And so there's these things called barriers where
*  you can basically synchronize threads. So it's like this thread is just going to wait until all the
*  other threads are going to get to the same point. And that is going to be something maybe where it
*  reads some shared memory or something like that. So that's another important thing, which again,
*  I didn't implement because it's explainable from here. And also the complexity of implementing it
*  is not worth it. Okay, cool. That's good. Hey, we'll continue our interview in a moment after a word
*  from our sponsors. Hey all, Eric Torenberg here. I'm hearing more and more that founders want to
*  get profitable and do more with less, especially with engineering. Listen, I love your 30 year old
*  X Fang senior software engineer as much as the next guy, but honestly I can't afford them anymore.
*  Founders everywhere are trying to turn to global talent, but boy is it a hassle to do at scale from
*  sourcing to interviewing to on the ground operations and management. That's why I teamed up with Sean
*  Lanahan, who's been building engineering teams in Vietnam at a very high level for over five years
*  to help you access global engineering without the headache. Squad Sean's new company takes care of
*  sourcing, legal compliance and local HR for global talent. So you don't have to with teams across
*  Asia and South America. We can cover you no matter which time zone you operate in their engineers,
*  follow your process and use your tools. They work with react next JS or your favorite front end
*  frameworks. And on the backend, they're experts at node Python, Java, and anything under the sun.
*  Full disclosure, it's going to cost more than the random person you found on Upwork. That's doing two
*  hours of work per week, but billing you for 40, but you'll get premium quality at a fraction of
*  the typical cost. Our engineers are vetted top 1% talent and actually working hard for you every day.
*  Increase your velocity without amping up burn. Head to choose squad.com and mention turpentine to skip
*  the wait list. Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations
*  that actually work customized across all platforms with a click of a button. I believe in Omniki so
*  much that I invested in it and I recommend you use it to use cog rev to get a 10% discount.
*  Do you want to next just talk through a little bit the instruction set and maybe give a little
*  flavor to what kind of the next in instructions would be if you were to expand from here?
*  Yeah, so instruction set, I would say a lot of it is very simple. So you have
*  addition, subtraction, multiplication, division, very straightforward. Everything just takes
*  three registers and so the important thing I'll talk about here is just the specifics of the
*  register file. So with addition, subtraction, multiplication, division, for context, each
*  thread has 16 registers, which means that it has 16 different places that it can store whatever
*  values it wants to store for any arbitrary computations. And importantly, the last three
*  of these register values are restricted. And so we'll call those registers 13, 14, and 15.
*  Those are how in my GPU, the actual those custom context values I was talking about
*  are not a real GPU. It doesn't necessarily work like this. But basically the important thing is
*  every thread has access to its context. I happen to implement that through these registers. And so
*  these special registers are registers that you can't write to. The GPU itself handles writing to them
*  and that means that the GPU itself supplies this code execution environment with like,
*  hey, you're this block number, there's this many threads in each block, and you're also this thread
*  number in this block. And again, that's how in the hardware, the code has access to those values.
*  Now the last 13 registers are read-write registers, which means the code is free to access these
*  somehow for once. And so these add, subtract, multiply, and divide, what they do is basically
*  take the values of two registers, which you then specify with four bits, which is what you need to
*  specify an address of 16 different possibilities. And it will take the value from these from two
*  different registers and it will perform a computation on them. I could actually subtract
*  from the multiplication division and then store that result back into one of the registers,
*  all the registers specified by four bits. Now with the load and store instructions, similarly,
*  the load instruction will take the address of one register. So it will take the value of one of the
*  registers, that's going to specify a memory address. So for example, if that register has
*  the number four in it, it's going to go load in element number four from global memory,
*  and it's going to put that into another register. And for the store instruction, it's going to take
*  the value of one of the registers and store it into a memory address in global memory,
*  just like another register. So again, those are register computations. That constant is
*  very straightforward. You just load in a specific value that you want to into a constant
*  to the register. And that might just be because you want to use it for addition or something else.
*  Now the interesting instructions that I'll spend a bit more time explaining are the
*  BRNZP, which stands for branch. It's a branch instruction and a comparison instruction. And
*  these two work together like the simplest implementation, kind of 90-year implementation
*  that allows you to do if statements and looping. And this is all like CPU stuff,
*  or C unit or DPS too. But the main thing is that what you want to do is create some condition.
*  And then if this condition is true, you can jump somewhere else in your code, which means,
*  let's say I want to do something like, if one of my registers is greater than zero, then jump to
*  the end of this, stick this entire segment of code, otherwise go through it. So that's basically like
*  an if statement, right? Or you could do a loop. So you could do some code, you could put a label
*  at the top of the code. So let's call it like a loop label, which is actually in one of my kernels
*  below. And then you have a whole part of code. And then below that code, you're going to say,
*  if some condition is true, jump all the way back to the top of the loop, which is going to keep it
*  looping until that condition is in an arbitrary. The way that you implement this is with the
*  comparison and branch instructions. And it's always basically a comparison than a branch.
*  So what you do is first you do the comparison instruction. And that's basically going to take
*  two registers. It's going to compare them. And then it's going to check if the result of
*  subtracting the second register from the first is positive, zero or negative. And it turns out you
*  can actually do a lot with that. So you're just going to compare two registers and it's going to
*  store that result if they're positive, negative or zero from the difference between them in
*  something called the NZP register, which is stored in the program counter unit of the G like any
*  compete unit basically. In our case, it happens to be a thread execution unit in a GPU. And so the
*  program counter now has the current line of code being executed. And now it also has this comparison
*  thing, which is storing whether the result of the subtraction of the two registers is positive or
*  negative. Now with that, so you're going to have now some NZP value and it's going to have a one
*  specifying whether it's negative, zero or positive. Now the next instruction, brnzp, which is branch,
*  it's to allow you to specify branch to some specific line, as in jump to some specific line
*  of code if the NZP register holds some specific set of values. So you could say if the NZP register
*  is saying that this comparison is negative, then jump back to her loop code, which is exactly what
*  we did in the matrix multiplication. So the matrix multiplication needs to do a loop through some
*  code. So what it does is it compares some counter, basically it's just incrementing a counter and that
*  counter is supposed to do some number of loops through the code. So let's say in our case, the
*  counter needs to go through basically two loops. And so it's just storing the value and that value
*  is going to start at zero and keep incrementing up until it's past the counter. And so basically
*  the way you would use these instructions is use the comparison instructions. So you're going to say
*  compare my counter to the value that the counter is supposed to always be less than. And then if
*  the counter is still less than the max value, go back and loop, otherwise don't loop. And so that's
*  how you'd use those two instructions to create conditional logic, which is exactly what the code
*  does. So those are pretty important. I know the last two instructions are very straightforward. So
*  there's like the no-opt, which is basically an algebraic instruction, it just moves on to the next line.
*  And there's a return instruction, which tells the GPU that it has reached the end and executing
*  specific cut. And that's how you do the entire ISA. And that also, obviously this part is actually a
*  lot of the hard part. Once you understand this code layer, which is how we started here,
*  then the hardware layer actually becomes a lot more clear what's going on. And that's partly a
*  result of the fact that this code layer is the result, a lot of fine tuning on the hardware layer
*  also in terms of what I actually included here. But yeah. Okay, cool. Again, maybe just to try to
*  recap a little bit there. I hadn't understood coming in that you had these three dedicated
*  registers, which is just a position in the local most memory, right? That sort of declare to the
*  kernel, which is the form of parallel programming that says, here's what to do, given what position
*  you are in. That indication of where you are is provided in these dedicated registers. And then
*  separately you have, I guess, how is that? That's not really related to the size of the instructions.
*  That's kind of independent. Like how many ridges I was conflating those for a second in my head,
*  because you numbered the instruction set with a similar gap. Is there a connection there that I'm
*  inferring correctly or am I hallucinating this? So there's a couple of connections in the instruction
*  set to the hardware. There's two important connections and they're very much demonstrating
*  that this is a dummy project. So first of all, if you look at the instruction set, each instruction
*  is 16 bits, which means that the first four bits of the opcode, meaning that basically, since there
*  can only be 16 different combinations of that, that means that with this design I've created,
*  there's actually only space for 16 total instructions, which means there's only space
*  for four or five more instructions if I wanted to add them. Now the second constraint is that
*  I've made it so that each register is specified by four bits, which means that there can only be up
*  to 16 registers. If I wanted more registers, I couldn't do that. I would need a fifth bit,
*  this slight register, which means the instruction would have to be longer. And then the second
*  third thing is that the constant and more importantly the branch instructions,
*  they both take immediate values, which means they're not taking some value from a register.
*  They're literally taking values that are specified in the code. Those are numbers.
*  And if you look at those, each of the numbers is eight bits, which means that the branch instruction
*  can only specify the branch to eight bits of program memory because the branch instruction
*  is telling it, if some condition is true, jump to this line of the program, which means that
*  in order for the branch instruction to cover the entire program, my hardware as in my program
*  memory can only use that stuff at eight bits, which means it can only have 256 or by following
*  the six rows. So those are the constraints created by the instructions here. And again,
*  in reality, for this reason, instructors are usually a lot longer than 16. Usually they're
*  32 bit like the instructions, but yeah. So if you wanted to have more memory, you would have to have
*  longer addresses for that memory. And if you wanted to have more instructions, you would have
*  to have obviously bigger labels for those instructions. And maybe this is where we're
*  headed next, but I'm a little fuzzy. I'm like, basically each one of these instructions is
*  implemented by hardware at this point. This is like the last layer of software. When this gets
*  issued to the GPU or to a compute core within a GPU, it now says, okay, I'm going to actually fire
*  up a particular circuit that's going to do this stuff now. Right. There's no further software
*  to. One caveat. So I obviously oversimplify, pretty much everything I said here in this whole
*  thing is simplified in some way, but I feel like one example of an oversimplification here is like
*  in a branch instruction. In reality, the number of bits in the immediate in a branch construction,
*  if it is an immediate, is not limiting the program. The reason that I limited it is because
*  your alternative is to make this thing an offset. So instead of it being like literally branched
*  this line, you could be like branch to some offset from the current line as in branch plus 50 or
*  branch minus 50, in which case you could do it a couple of times and then you're not limited. So
*  you can, you can get infinitely far in memory. There's tons of other ways to approach it.
*  That's just one example of a constraint because I one did not support negative numbers here
*  and two, I'm not making an offset. I just wanted to jump to a specific one for simplicity sake.
*  Now that's like a constraint that in reality there's tons of ways around this, but
*  yeah, that's an example. And then in terms of the second part, that's exactly right. The important
*  thing to take away from this part, maybe there's still lots of fuzzy details, especially for people
*  listening. The important thing is one, you understand the importance of each instruction
*  and why it's there and what it's supposed to do. You understand the general programming pattern.
*  Again, it's hard to draw even just because it's assembly and assembly itself is not necessarily
*  the easiest thing to pick up. It makes sense when you look into it, but you just need to understand
*  those parts and the important GPU programming patterns because a lot of the actual implementation
*  will get revealed in the hardware. Okay. I think it's just about time probably to turn to hardware,
*  but let's just scroll through the multiplication one more time because this is where you have
*  basically brought it all together in terms of the complexity that you can support,
*  where we've still got to be mindful of where we are in the thread. But this time the calculation,
*  do I have it right that basically this calculation determines one position in the output matrix?
*  That's exactly right. And so you're going to get a two by two so that you're going to have
*  four spots in the output matrix. So that's why this is four threads. Each one of those threads
*  is going to do a different set of, it's still going to touch all the numbers basically, right?
*  But it's going to do them slightly differently to get to the final spot in the output matrix.
*  And to do the sort of rows and columns, it has to do this loop. And this is where we get
*  to the point where you have to have this comparison and branching.
*  Yeah, exactly. The reason is just because the nature of matrix multiplication being a little
*  more complicated than addition. With addition, you just add up to elements with matrix
*  multiplication. Unfortunately, it's not just like multiplying the elements. It's like a dot product
*  between two vectors in the matrix. It means like you just take two like vectors, which is just
*  rows, a row and a column of elements, and then you multiply their elements by each other and then add
*  up the results. So it's actually a bunch of different computations, not just like a single
*  point wise multiplication or something, which is why there's a loop here and why there's a bunch
*  more multiplication and additions going on, which is what necessitates the comparison and branching
*  in this case. And I would say that's the most important thing. For people who want to understand
*  the specifics of the kernel, you can look at it. It's relatively simple, but maybe a little bit
*  beyond the complexity of what makes sense to explain on ARIA. Yeah. And I misspoke when I said
*  that it's going to touch all the numbers. It's going to touch one row or column for each of the
*  two input matrices. Exactly. Yeah. So it's like that's a lot of numbers. In this case, it happens
*  to be three quarters of them for each computation. Okay. Cool. Well, then I guess it's time to get on
*  to the hardware. So how do you think best to approach that? Yeah. So this part is actually
*  going to be a lot simpler, thankfully. And so the best way to start it is to just start with the
*  architecture of the entire GPU, and then we can dive into the thread architecture. And so this is
*  a great straight board. Okay. So we talked about this program, right? So now the nice thing is we
*  can explore, okay, how is this program going to actually get executed in the GPU? And that is going
*  to take us through basically the entire architecture and also the motivation for why everything exists
*  here. First of all, let's take the example of our matrix addition kernel. So we have this code.
*  The question is, are we going to actually load this up into the GPU and how are we actually going to run it?
*  And so what we'll do here is first we'll look through how this works high level in the architecture.
*  Then we'll look into individual threads and how to see how this code is executed in an individual
*  thread level. And then in the last piece of this that might be interesting is we can actually look
*  through the test case and briefly explain in the causatory how it's actually tested and simulated.
*  So it's not just the theoretical. Those kernels that are written in there, there's actually a setup
*  for them to actually get run on this GPU design and see the entire output of everything that's
*  going on. And so we can touch on that last and maybe like touch on some of the interesting things
*  in the code. So what we'll place it all stark is we have this matrix addition kernel and the question
*  is how do you actually get this to execute on GPU? On one hand, you need to load up the code into
*  there, but then it's like, okay, how do I actually make this thing run and get the result back?
*  So the way this is going to work is first we'll think about global memory, which is like the place
*  where you're going to load up all the prerequisite data of this code. First of all, you have the
*  actual kernel code and that's as you wrote below or before, it's just a bunch of instructions.
*  And those instructions happen to be written in assembly, which is like some nice verbal format
*  for us to visualize them. In reality, we would compile that assembly, just a pre-setting setup,
*  compile that assembly into the object code, which is specified by the ISA. So it's just going to be
*  a bunch of ones and zeros, all 16 bits long and load that into program memory. So now let's assume
*  we've loaded that into program memory. Let's say it's like 12, 15 lines long. So now we have our
*  kernel code loaded up into program memory and that's just going to specify exactly where the
*  kernel is set, this and this. And then the second piece of it is in data memory, we're going to load
*  up the actual data that we want to perform computations on. In this case, this would be like
*  the two 1 by 8 matrices. We'll call them A and B. So as I said before, A is going to be in addresses
*  0 to 7 and then B is going to be in addresses 8 to 15. And then we'll say that C is going to be in
*  addresses 16 to 23. So that's going to be our result. Currently our result matrix is going to
*  start out with nothing in it. And so what is the goal of our entire program? The goal is to somehow
*  get the GPU to use that code that we just loaded up in program memory. And somehow at the end,
*  it's going to need to fill out rows 16 to 23 in memory with the correct results of the additions
*  of A and B. And then we're going to read that out at the end. So from the host machine's perspective,
*  which is like the CPU talking to the GPU, what we need to do is basically get this from code,
*  load it into program memory, load up our data into data memory, somehow get the GPU to start
*  this whole computation. It's going to do its thing. And then at the end of it, GPU is going to tell
*  us it's done. And then there's going to be in data memory, the answer. And the host machine can just
*  read out that answer. And so that's kind of the interface of the GPU basically. So in this picture,
*  you're going to have global memory with program memory and data memory. And that's the only piece
*  of that. And then another important thing in GPUs is the actual bus square data kind of
*  transverse between the CPU host and the GPU. Again, I left that out because of simplicity reasons.
*  But the other important control thing here besides the memory is what's called the device control
*  register. Now, in real GPUs, this is a lot more complicated. But in this case, if you remember,
*  what we need to specify is basically the number of threads to execute. So we need to tell the GPU
*  that, hey, this thing in program memory, which is just a single kernel code, we need to tell it,
*  you need to run this thing eight times. And so the way that you do that is in my design,
*  you would store the grand count inside the device control register. And so the device
*  control register is mainly just used to store some high level data about how you want the GPU
*  to execute. In this case, the only piece of high level data we really need to specify is how many
*  threads should you be executing? And so now we have program memory loaded up, data memory loaded up,
*  device control register loaded up. Those are the three things you need to do to get this GPU to be
*  prepared to run something. And then that's the external interface. Then we're going to send a
*  start signal. And that's going to tell the GPU, hey, everything's loaded and ready to go. You need
*  to start basically performing computations on data. And that's like a clean break. So that's like the
*  interface and the app that you do. Now we're going to get into the computational parts, but
*  us loss there. Does that make sense? Yeah, I think so. And probably just worth
*  reiterating that there's like even in some ways more complexity on the CPU side. And you said the
*  host machine, we're sort of assuming here that you have a general purpose CPU that can do the
*  compiling and can handle the like outer loop of here's what I'm trying to do and get something
*  back and show it to you on a screen that's done. And this sort of sits within that. So it's funny
*  because the programming paradigm is in ways is more complicated. But then in other ways, it's a
*  lot less complicated because it can take advantage of all of the universal computing benefits of a
*  CPU host machine. Aside from that, I think it all makes sense. That's a good point because GPUs are
*  not really meant to run alone. They're always in practice. Either hooked up to a host, like you'll
*  see them next to the computer and like a rack or you have to be cut to one of the cloud or something
*  like that. That's not really very practical, but depending on what you're doing. But yeah, they
*  usually have a host connected to them that can send them data and interface with them. But yeah,
*  that's a good point. So now we can get into the computation pattern, right? And high level is
*  actually pretty simple. So the main things to focus on is you have this dispatcher and the
*  dispatcher is just responsible for, as we said, these threads are executed in blocks and a block
*  is just a batch of threads that gets executed together at the same compute resources. And so
*  basically the way to think about this is your GPU has some large number of compute resources
*  that are organized inside cores. And so this GPU design happens at four cores and each core has
*  the capacity to execute a bunch of different threads in parallel. And from a high level,
*  before diving into Watson cores, let's just assume the core is some black box. And we just know that
*  this black box, we can just get it from some group of threads, which is going to be a block size of
*  threads. So in this case, four threads at a time, we can give each compute core four threads at a
*  time, going to do some applications and finish tossing the threads somehow. And that's going to
*  tell us when it's done. And so the high level job of the GPU now is like, okay, how do we manage,
*  how to divide up these threads into the available compute cores, wait for them to complete their job,
*  and then give them more jobs when they're done computing their computing work. And so basically
*  all of this is just managing all the compute cores, figuring out when they're available for
*  new work, and then just staffing new blocks to these cores. Now in Takus, this is one place
*  where there's a lot of complexity in GPU, because you can imagine when you have a ton of different
*  cores performing stuff at once and different cores can perform different blocks, like they
*  can execute different blocks of threads at once and they have a complex resource management,
*  you can do a lot of different optimizations to make sure that you're getting maximum
*  resource utilization. And so this is a soft place where there's like a ton of space for optimization,
*  be sure to use things more efficiently, threading in, like you might call it, threading in different
*  threads at once to make sure that everything's getting used. And then of course, for simplicity
*  sake, in this example, we use a very simple version of that, which is just that the disk
*  actor looks out for when a core is done executing its threads, and just as it looked like, and just
*  like a round robin style. So it just looks at all of the cores sequentially, and then keeps dealing
*  them more threads if they're ready. That's like the simple way to think about it. And so the
*  dispatcher is one of the more complex elements of the GPU. Now if we get into the individual compute
*  cores. Dispatcher is flared for a second? Fair, yeah. One thing, what level of design did you have to go to
*  in this project to create a dispatcher? Is that something that you had to design, and if so, at
*  what level, or was it something that you could drag off a menu of available components? Yeah,
*  so pretty much nothing here was an available component, to be honest. So the nice thing is I
*  had two or three repositories to reference. So there's this thing called Meow GPU, which is like
*  an open source Verilog GPU made a while ago by Sunscrull, I forget which school it is.
*  And there's this thing called Verigp, two open source GPUs. The thing is these things have very
*  little documentation, and then they're not really written to be simple. They're written to do like
*  attempts at production GPUs. One of them is like completely unfinished. Meow is actually finished.
*  And first of all, architecturally, they're somewhat different in some ways, because again,
*  they're optimizing for production usability. And the second thing is because of how big they are,
*  they're just not very easy to understand. And so my process for creating things was not really,
*  you can't really go through them and try to understand. The analogy is like if aliens
*  come to Earth and find the computer, like how are they going to understand it? Are they going to
*  break it down and look at all the connections, the transistors and see what's happening? No,
*  they're not going to understand it by doing that. They have to come to some understanding of their
*  own and then test it against the computers that they have. It's a bit of a massively over complex
*  analogy for going through a GitHub repo. That's actually the analogy for mapping out the brand,
*  which is not a good idea. But yeah, so my approach to going through these repos was not like going
*  through them and trying to understand. It was actually like talking to Claude and JackYubyKey
*  I see names of things. I'll see a folder called, I don't know, just that or schedule or whatever.
*  And I'll try to figure out with Claude through first principles, like where does this have to
*  fall into place in the GPU? And then that part's not too hard. So then it's like, okay, I get to
*  something. Then I'll start to propose how I think it works. And the reason is because there's not
*  really anything that teaches you how these things work, like anywhere online, because it's all
*  proprietary and they have their own algorithms and stuff. And so even to make a simple version,
*  you'd have to be like, so for the dispatcher, for example, I come up with a hypothesis like,
*  oh, I think a simple version of this would be XYZ. Like I think a simple version of this would be
*  like round-robin scheduling while looking at what course are available, which is super simple.
*  And then I would have to get confirmation. So Claude would be like, actually,
*  they don't need that. So I think you should think about it like this or something like that,
*  which is interesting that there's nothing publicly available. But Claude and JackYubyKey,
*  in some cases, it's things that are purely intuitive and it just has the benefit of
*  engineering intuition on stuff that I haven't gotten into. In some cases, it says stuff that's
*  definitely implemented in proprietary GPUs. And maybe it's still out there through intuition,
*  but it's a little more stuff that's a little more complicated than what I expected it to know,
*  which is pretty cool. But yeah, as long as it answers your question, there is no off the shelf
*  stuff. I basically had to design everything myself from how I thought it would work and then get
*  confirmation from it. Maybe look into the repo to see, oh, this repo actually happens to do
*  something a little similar to what I suspected. And now I can actually understand it because I
*  came up with it first. And I had to do that for all the elements. Straight up, some of them are
*  a lot simpler to understand than others. But yeah. Okay. So this thing implements a round-robin where
*  it just says, I'm going to just keep looping through, as long as I'm live, I got to just keep
*  looping through all of the compute cores, check their status. So that implies then that the compute
*  core is maintaining a status that can be checked. And if it's available, then I'll send it another
*  thread to process. And if it's not, then I'll come back to it on my next loop. And all of that is
*  implemented in hardware. You're beyond the point of programming this at this point, right? Yeah.
*  This is implemented in hardware. Yeah. So do you have a diagram of that? Can we look at that?
*  We can look at the code in the repo. There's no diagram. The diagram is for thread execution,
*  but there's no like disaster diagram. Okay. Let's look at the code to just see what that looks like.
*  So if you go into source and then dispatcher.sc, yep, this is it. You can see all the code is
*  documented with like at the top, you see there the important points. And you can see there's
*  some of the things that we're saying must be there are there. First of all, the important thing with
*  the dispatch is that it has a start signal. And what that means is that thing we were saying at
*  the top level, we're going to tell the GPU to start the place where that actually goes into
*  the dispatch. So the dispatch says, oh, I've gotten full to start. Now I'm going to start sending off
*  these blocks to the actual cores. And that's what starts execution. That's the start signal you see
*  here. You see the thread count coming in from the device control register, which is again important
*  for the dispatch because it needs to know how many threads doesn't need to execute a total.
*  How many threads has it already executed? And that's what's going to tell it like, oh, I have
*  this many threads, we're going to execute. Let me go send them off to the compute units. Then you can
*  see the core stage. So that's the thing where you're saying, oh, it looks like the cores must
*  have their own knowledge or status of if they're ready or not. And so that's exactly what you see
*  there. You see core done, which is like, oh, this core is done processing. And then, so you see core
*  done, core reset and core start. Those are important. This is basically the way to dispatch this and do
*  stuff, right? It's waiting for the core to be done. It's going to say, oh, here's a core that's done.
*  Let me reset this core. So that's going to set all of the state back to empty. So it's going to clear
*  everything out. And then it's going to say, oh, this core just got reset by me. All right, I'm going
*  to go start it up with the next block of threads if there's still more blocks. And if you slow down
*  a bit, you can see there are some intermediate variables which store like, how many more blocks
*  do I have left? So that's blocks, destashed and blocks done. And that's just saying, okay, I need
*  to process this many more blocks of threads before this is completely done executing. And then the
*  last thing that the dispatcher does, down in this loop, but you can see at the top, there's a done
*  signal exported from the dispatcher. That done signal is sent out to the GPU itself. And so not
*  that one, but in the actual model definition a little bit further up, there's just something
*  called the straight up done. You can see it in a couple of places, output registered done. And that's
*  going to tell the whole GPU, hey, all everything is done. And then it's going to stop executing
*  everything. And now it's just going to wait for the host machine to basically pull out the results
*  from memory. And that was machine can just reset the GPU. And that's like one full execution loop.
*  You can see that the dispatcher kind of high level is responsible for managing that whole high
*  level execution flow. So yeah. Cool. This is code. How does this thing get translated into
*  hardware? This is what the package that you're working in does?
*  So the way that this whole thing works is just like EDA in general, you design your architecture
*  based on what it's supposed to do. There's a functional logic in Verilog, or in this case,
*  system Verilog, which is just like a modern version of Verilog. And then there's these entire
*  software stack, which is what I was talking about before, which basically translate that Verilog
*  into an actual design. And in practice, that's really hard because there's so many different
*  steps that go into it. You need to synthesize the Verilog down into just a logic. There's a chart of
*  the logic that's specified in there. And then because of the way that people program stuff,
*  that logic is inherently not very perfect. It's going to be way more complicated than it needs to
*  be. You can do some processing to basically get that logic down into its simplest form.
*  That's still the equivalent. So that process of turning the Verilog into a logic flow is called
*  synthesis. And then once you do that, you can perform a bunch of analysis on whether this design
*  is valid or not. Then you convert that logic that you've created into gates. And then those gates are
*  based on a specific process. So basically, you have these things called standard cells, which are
*  specific gate designs, designed for a specific foundries process after using gates. So you
*  convert them into gates, and then you lay out all these gates on a huge chip design. So the
*  gates are just laid out everywhere all over the chip based on a bunch of different optimizations.
*  Then you hook up all the gates with wires, like the gates that need to be connected together.
*  And then there's several cycles of optimization on this whole process to make sure that
*  everything is valid, all the timings are valid, because electrical signals need to flow through
*  this chip. And if any of the signals flow through the chip slower than the actual clock time of the
*  chip, that's going to cause errors. So there's tons of different errors there, even just at a
*  logic level. And then on a hardware level, because this is actually electronics, it's not necessarily
*  code, but it's nice that I didn't code the complexity way higher. There's these things
*  called parasitics, which is like, oh, you're actually dealing with wires and metals. And
*  if there's wires near each other, they actually have capacitance between each other. And there's
*  like tons of other electrical effects that can suck with the chip. And so you need to do copy
*  tapes to prevent that stuff too. And there's so many complicated things that at the very end,
*  your whole design is there, it gets outputted into the layout. And that's in the form of a GDS2 file,
*  which just happens to be the file format specifying all the metal layers to send to a foundry.
*  And then you do a final comparison called a layout or a synthetic, which is make sure that
*  this style layout you got after tons of optimization is actually logically equivalent to your original
*  design. And then you can submit that layout to like a foundry. And now in practice, you're actually
*  going to do a ton of formal verification also on this layout to make sure like, all of these bad
*  states are impossible to get into. And again, at hardware design in general, the verification
*  process is so important because on the software, you can't ship and iterate, you just fuck with you,
*  you mess it up. There's all that stuff. But that's what happens. Again, if anyone had to program all
*  that, that's impossible to get into the task. But thankfully, all these EDA softwares do it for you
*  for a couple million dollars. And actually, thankfully for me, there's Bumpin' Land, which does it for you
*  for free. And that's super little, but yeah. Even that has some complexity going through it. Because
*  once you do that, you run through a bunch of errors and you have to fix that in your code.
*  Yeah, you can see where the decades have gone in terms of building up the stack. Talk about
*  on the shoulders giants. What does this feel like on the open version that you were working on when
*  you go to, I'm not even sure what the right word is, but I want to say compile, but it's almost,
*  it's more like translate from hardware designs. That's what it's called. Hardening. So how long
*  does that take for something relatively simple like this? And you're running on your local.
*  Yeah. So local laptop, I would say is pretty powerful on this stuff. You know, it's an M2.
*  So that's like probably on the better side of like a hobbyist doing this stuff. And it can take 20,
*  25 minutes to go through the whole flow. It does like cookie different steps. And that takes like
*  a bunch of time. It does like tons of optimizations, really cool things that you can see all the
*  different steps going on and try to understand them. And then you do want to see errors on any
*  step. Often you do. And the one thing is like, obviously the stuff isn't like perfectly documented
*  or there's like millions of errors you can run into. Obviously, I think that's a creation,
*  but so many different errors you can run into. And it's not really well documented,
*  almost not a member well documented. And they're also like really random error messages. And so
*  one of the challenges of it is it's a lot less easy to use. Like you just got to figure stuff out and
*  it's so much just stuff. You have no idea what's going on. And you just got to try your best to
*  figure out what's going on and debug it. So I think very low transparency on the debugging side,
*  which is probably one of the biggest, it does the biggest thing because that's the whole flow.
*  Like that's basically the output of the flow is like, what bugs do I need to fix before I can
*  get a finalized GDS? But it's doable. And you just push through it then it works.
*  I said we got your client, it's magical. There's any insert visualizing it and it's pretty sick.
*  Yeah, it's fascinating. How many cycles would you say you went through in this project of that
*  20, 25 minute hardening process before you got one that actually didn't error out of that new?
*  Oh, a lot. I have all of them saved in here. I can say it's like 30, 35, like that, something
*  a lot of different cycles. They're not in the repo, they're just in my local.
*  Okay, cool. So let's come back to the overall GPU architecture. So we've got these modules,
*  components that are defined in code that are hardened into an actual, ultimately, I guess,
*  that the classical word would be like etching. But now with this, it's like a, it's a light process,
*  at least in most advanced nodes. So that translation is happening with this decades in the making
*  shoulders of giants software stack. And that gives you the ability to define each of these things and
*  then it go to come back in 20 minutes and see if it works or not. Yep, exactly. And you have to then
*  also define the interface, right? Like the compute cores have to maintain. So next time, I'm interested
*  to see a little bit of the interfaces is always I think about programming a lot in terms of
*  interfaces, like where is it that it's declaring whether it's done and not done so that the
*  dispatcher can reassign or not reassign as appropriate. But take us through the rest of
*  the architecture however you think best and we could check out a couple of those things.
*  Let's look at the GPU.se file first. That's the high level interface that's going to be interesting.
*  And then we can look into the compute cores in detail, put in the executions.
*  Yeah, this is the high level file. There's some parameters at the top. Those are mostly unimportant.
*  The interesting ones are the number of cores and the number of threads per block. So here,
*  yeah, I guess it's a slight to two. That thing you can just completely change around. So you can
*  switch the number of cores three or four or whatever. And you can switch the number of threads in each
*  block, which is just going to change how many threads can get executed on each core at once,
*  which means that there's going to be more compute resources and remister files and everything on each
*  core. And that will make your sense later. But you can see the high level interface here. You have
*  the clock and reset. Those are mostly unimportant. Those are just like the, you have that for every
*  design and that's just going to allow you to have clock cycles on your GPU and reset stuff.
*  The interesting part of the question on clock also, it seems like if everything is built perfectly,
*  everything would take the same amount of time. I'm a little bit confused as to why, if I
*  distribute four threads across this thing, like why don't they all finish it at the same time?
*  Good question. So the reason, the sole reason for this, and this is the reason behind my memory
*  intuition and by George Hopps that the whole problem is memory. We'll see that when we dive
*  to the thread execution is like, if there was no reading and writing for memory, it would all
*  finish at the exact same time because everything is deterministic there. It just takes the same
*  amount of cycles for every instruction. The thing is when you have memory, like loading from global
*  memory, that memory is DRAM. So first of all, it's using capacitors to store memory, which is
*  it has some latency to it. You don't just get it back to one clock cycle basically, which has some
*  non-determinism. The bigger thing is the bandwidth issue. So like if I have a thousand compute cores
*  requesting some values for memory and memory can only support a hundred reads at once, that means
*  that this is going to start to get chewed up. So there's going to be like a thousand compute cores
*  request data, then a hundred of them are going to get back data at the next hundred, which means that
*  certain cores, even if they're on the same, even if they're being tossed together, they might make
*  requests to memory at the same time. They may not get the data back at the same time because memory
*  has an unknown latency, it's asynchronous. And that means that if one thread gets memory back
*  earlier or later than the other ones, then it may have to wait for the other ones or there's a bunch
*  of stuff that happens around that. So my design, it waits for the other ones, which means it can't
*  just keep going. And then similarly across the cores, even if they all start executing grants at
*  once, one core might finish way before the others because it just got data from memory back earlier.
*  That's about as really the bottlenecks to see it, which is why
*  AirBus and it's all about matching memory latencies, but that really is the bottleneck.
*  And the clock, just to set a foundation on that as well, is essentially an electrical
*  impulse. It's a change in voltage that is getting applied through the whole chip. Is that right?
*  Yep. So the clock is just basically a cycle. It's like a sine wave almost of some signal going from
*  high to low over and over at some periodic interval, usually a couple of milliseconds,
*  a couple of seconds, or something like that. And basically every time the clock goes from zero to
*  one, it's just like a sine wave, but every time the clock goes from zero to one, remasters in the
*  chip, like deep flip-flops, they will take in a new value. And so that creates the wave for state.
*  That type of state transfers on the clock, so like whenever the clock happens, which means that
*  except for the pulse, then the sends happen in the GP. So it's like generally in each clock cycle,
*  you're going to have the start of the clock cycle, so new values are set, then you have all these
*  wires propagating signals, and the next clock cycle, the values are set again. And so it sets
*  this time interval, state is set on the clock cycle, and then self-set happens in between that time
*  of where state is set. And that's going to help you influence what's the next state. And the other
*  thing that's important about the clock is you can't just set the clock insanely fast because
*  the chip actually has physical constraints, right? Electricity actually needs, if you need
*  something all the way on the left side of the chip to communicate, something all the way on the
*  right side of the chip in one clock cycle. There's actually constraints there because the
*  electricity takes time to propagate across the chip, which means that your clock cycle needs to
*  be longer than the maximum propagation time of signals that need to communicate in your chip.
*  And that's actually something that EDS does. So that's one thing. It's like static time of
*  analysis. Make sure that all the timings in your chip are valid based on the clock cycle time.
*  Gotcha. Okay, cool. So if something is waiting, again, it sounds like you could implement this in
*  probably a lot of different ways, but you could have your course sort of saying,
*  I'm in waiting mode. So this cycle, I basically just do nothing because I'm still waiting for
*  the memory to return. And then next cycle, if I got it back, that I can actually do it.
*  And that's because there's different latencies, they can just diverge in terms of where they are
*  in their particular execution flow. In an actual production environment with the over many
*  gobs and gobs of gates, ultimately, that are being included in a single chip now,
*  presumably there's also some difficulty there, like some just inconsistency or whatever that
*  could create divergence. I don't know if that's the kind of thing that would get disclosed, but
*  I imagine there must be some sort of engineering just to try to
*  not allow some local defects to ruin the whole thing, right?
*  Yeah, I would say that's one fabrication layer. There's tons of like local defects is actually
*  one of the biggest problems in the fabrication industry. That's why contamination control is
*  such a big thing because as you start scaling down the size of individual transistors, now smaller
*  and smaller defects that didn't matter before can actually break everything because they can get in
*  the way of gauge or basically there's tons of different places in the chip where a contaminant
*  can just ruin the whole thing. And that's why there's just like all the technology on actual
*  fabrication has been advancing to smaller, smaller scales, the contamination control technology has
*  had to get better and better. But that being said, that's more so a concern of the actual
*  fabrication process. The reason is that they actually have a kind of testing and the testing
*  is built around like one, they have a lot of contamination control, two, they have a testing
*  to make sure that even if there is some contamination breaking the chip that they're going to be able to
*  test that and discard the bad ones. That process is imperfect, but generally speaking, that's
*  probably the biggest thing that determines chip yields and practice. And generally speaking,
*  that's a concern of the foundries, not really someone like Nvidia that's into the design,
*  they'll just ship off their designs to TSMC and TSMC will often be concerned with that.
*  But generally speaking, Nvidia can probably assume that most of the chips are working once they get
*  it. Cool. All righty. Should we go back to the dining room? Yeah, we can do that.
*  So now we can go into what's going on inside each compute core. So we already saw the interface of
*  the dispatcher. So each compute core is basically going to get told by the dispatcher, you're
*  executing this block ID, and you're going to get this many threads in the block ID. What's a,
*  when dispatchers will say, hey, execute four threads in block number two, and tell me when
*  you're done, basically. So what's going to happen is the dispatcher is first going to reset the
*  compute core, then it's going to tell it here's your block number, here's how many threads to
*  execute. And it's going to tell it start. It's going to tell it to start signal, similar to how
*  the GPU got a start signal. And then the question is what's going on inside the compute core to
*  process those threads up until the point where it's reporting back to the dispatcher, then it's done.
*  That's like the high level interface at compute core. And so there's a couple of key pieces of
*  the core. And first of all, there's the high level control logic that's shared between all
*  the threads. And then there's like the actual thread execution, where we split out into a number
*  of different threads within the core. First, we can talk about the high level logic that's shared
*  between all threads. And then we can dive into the thread. So high level, there's basically three
*  units that are shared between everything. So there's the scheduler. And again, this is where
*  there's a ton of complexity. It's now managing the resources of how many, however many different
*  groups of resources there are in the unit of u core. Now in practice, it's in p core isn't actually
*  thought of as having a certain number of threads. It just has some finite number of resources.
*  And then however many threads of these execute, they just stay executed on those resources.
*  And typically a scheduler is responsible for handling the difference between like
*  the dispatcher says, hey, execute eight threads. And you may only have four, like four different
*  groups of resources on your compute core. So now the compute core needs to manage the execution of
*  these threads in parallel or in sequence or how her determines is most efficient. So again, that's
*  why there's a lot of complexity in the scheduler. In my case, what I basically said is each compute
*  core is just going to process one block at a time. So it's not going to be able to say like,
*  hey, you can give me eight threads and I'll do like four at a time. It's just going to be like,
*  just give me how many threads I support. So each compute core supports four threads at a time,
*  which means that each resource that the red needs, it's going to have one resource. So like each
*  thread needs a register file. Of course we have four register files. Each thread needs its own ALU.
*  It's going to have four ALUs. So you get the point there. And basically what happens is the
*  scheduler handles the execution of the threads in terms of there's let's say 15 instructions that
*  each of these threads needs to execute. So now the scheduler is going to possibly execute the
*  control flow of how these instructions just handle. And so the way that happens is let's
*  say we're on structure number zero. So we've just been issued a group of like four threads
*  for the dispatcher and we need to execute these threads. So we're on instruction number zero.
*  So what we're going to do is first of all, we only know to start with instruction number zero.
*  We don't even know what that instruction is. So first we need to somehow get that instruction
*  from where it's stored and stored in program memory, because that's where we put it before at
*  the start. And so the fetcher is the first thing that's going to execute. So the scheduler is going
*  to tell the fetcher, hey, go retrieve this instruction from program memory. So that's the
*  whole job in the fetcher basically is to get instructions from program memory. And then in
*  practice, it actually doesn't catch it because instructing every room edit is like all threads
*  are going to be executing the same instructions. So one optimization we can do that's nice is that
*  the fetcher once it gets an instruction once it can just store it locally and then all the threads
*  can just use that again instead of going global memory. So that's the fetcher. And then what the
*  decoder is going to do, which is going to basically get us into the thread.hole is we now have this
*  instruction, which is a bunch of ones and zeros. It has its opcode, which is going to tell you what
*  the instructions supposed to do and it has all the registers and specific values. Now we need to
*  somehow translate that instruction into something that all these different compute resources can
*  actually use. And so that's the job of the decoder. And as we get into this thread, it will become a
*  lot more clear what the decoder is actually doing. So let's look at the actual compute resources that
*  are in thread. This is the last piece of this diagram and then we'll go off to the next diagram.
*  Within the thread in my design, there's basically four key pieces of memory and resources.
*  So each thread has its own register file that we've already talked about. That's each thread has
*  its own ability to perform computations on some data. And then importantly, it has its own program
*  counter, which means that each thread can be on its own line of the program. That's because
*  based on the data, different threads might have to jump around different lines of the code.
*  And in practice, that's challenging to implement. So that's called branch divergence, which means
*  different threads branch to different lines of the code. Now in our design, even though each thread
*  has its own program counter, for simplicity, all the threads are assumed to be basically continuing
*  on the same instruction. And it just so happens that I wrote programs where that is the case,
*  like all the threads stay on the same instruction. So this design was efficient for implementing that.
*  And then last two things, which are important. So each thread has its own ALU, arithmetic logic unit,
*  which is the actual compute that's like performing multiplication for addition. So that's the all
*  the arithmetic instructions in there. And it's the forming computations of the registers.
*  And the last thing is the load store unit, or the LSU. And that's the thing that's responsible for
*  fetching data from memory. And so that's the thing that does the load and the store instructions. So
*  as you can see, each thread has its own unit that is separately able to load data from memory and
*  store data into memory. And importantly, before we dive into the specifics of how all these pieces
*  interact, and so I know it's like, completely unclear at this point, it's just like, oh, I guess
*  it's like these high level things, I wonder how they actually work in practice. The important thing
*  is that the FETCHER and the LSUs, there's like a bunch of them across the GPU, right? Because each
*  core has a FETCHER. And that means that if we have four cores, there's going to be four FETCHERS,
*  and they might all be requesting instructions at once. And similarly, there's going to be like,
*  there's four LSUs per core and four cores, there's going to be 16 LSUs in the whole GPU,
*  and those could all be requesting memory at once. So the question is, how do we manage to constrain
*  of memory has a fixed data? Let's say I can only take two requests at once or something,
*  and all these resources are requesting memory at the same time. So you need something to actually
*  throttle all the memory requests, and on the GPU side, hold them. So it's like, here's all of our
*  requests, and then send them slowly to memory to respect the bandwidth that every actually supports,
*  and then slowly send those responses back into the individual compute units in the core.
*  So that's what the memory controllers perform. So there's one for program memory, one for data
*  memory, and those controllers are basically responsible for respecting the bandwidth that
*  the global memory actually accepts, and then taking all of the requests from the compute resources
*  and throttling them to the bandwidth of what the memory accepts. That's what the memory controllers
*  do. And yeah, with that, I'll pause there, and then after this, we can dive into the app for
*  throttling execution. Yeah, I think I get it. And again, all of these things are, at this point,
*  purely physical, right? We've left the realm of software some time ago. So the software
*  release stops at the point where the kernel is compiled, is the right word in that case, and
*  put into the program memory. And then everything after that is a purely function of the hardware.
*  The hardware is routing everything through just an insane tangle of ultimately logic gates.
*  Exactly. Yeah. Does anyone have an intuition for that at this point? It seems like we've got so
*  high up this tech stack over the decades that I wonder, is there anyone that can really
*  go to the gate level and understand how something as complicated as a data memory controller
*  works? Does anybody have an intuition for that at this logical gate level?
*  Yeah, definitely. Yeah. So I think most people doing architecture and design stuff,
*  they'll probably understand most of these elements at a gate level. Obviously, more complicated logic,
*  it's futile, and there's no point really to try to understand exactly what's happening at a gate
*  level. I think the main intuition you need is understand the core of how memory works at a gate
*  level, usually like static RAM. And that's pretty interesting. You understand how a latch works and
*  then a flip-flop works, and that's the core of understanding memory. In practice nowadays,
*  most of it is dynamic and only cache is static, but that's something people understand at a low
*  level. And then ALUs, and again, we're going to go into the diagram, and that's going to show you
*  as close to the low level as you get. It's going to show you multiplexers and stuff, which again,
*  are pieces that people understand at the hardware level. But yeah, I would say people do understand
*  it at that level. Now in practice, you don't really need to, as long as you know, as long as
*  you trust the processor. It's like, okay, I know that this is going to get translated into gates.
*  So this general way, you can study the gates in computer architecture class, and you don't
*  really need to know it past that. And then I would say really track architecture people.
*  There's a ton of stuff. The thing that makes them really good is that they're managing a lot of
*  stuff in their head, which most people are not. And usually that's not really a gate level logic,
*  although I'm sure they have that in their head too. It's more like understanding the implications
*  of stuff besides just the high level. Design's a really nice high level in practice. There's
*  actually a lot of complexity. For example, writing code in Verilog, knowing how many gates
*  a piece of code actually translates into is important. For me, it's like, oh, I might just
*  write the divide sign as my division instruction. This is the C. In reality, nobody would ever do
*  that. The divide sign actually turns into a gigantic piece of hardware, which you would never actually
*  want to use. You wouldn't actually want to implement the division thing as an instruction.
*  So it's things like that. And then also being able to manage all the parasitics and knowing
*  the actual electronics of it and how the electronics work if you place things in
*  different places. There's like tons of things like that. Honestly, the way I would describe
*  it high level is people have a surprising level of understanding of the EDA flow and the things
*  that influence that flow in their head. And they can get it by intuition. Obviously not the whole
*  thing, but pieces that most people won't. And somewhat I've noticed from a very limited perspective,
*  that's what a lot of the really good architecture people have. So I would say certainly with people
*  with intuitions and all these things. Fascinating. Okay. Cool. So should we go to the thread diagram?
*  Yeah, we can do that. And this is going to be nice, especially for people who are familiar with CPUs,
*  because this is going to get into very familiar territory. So you can see here something that
*  looks very similar to a CPU in many ways. It almost is exactly like a CPU except for the LSU
*  and my little details in the research file. But what you see here is, first of all, most importantly,
*  everything that has red text and blue text, that is stuff that's coming from the decoder. So now you
*  can actually see exactly what the decoder is doing, which is the decoder is responsible for converting
*  the instruction into these red and blue signals. And these red and blue signals are going to be
*  used as control signals to control the execution and intellectual thread. So what you see here is
*  a single thread. Obviously there's multiple of these per core and all of them are going to get
*  the same control signals once since the decoder is just shared between the core. And now you can see
*  how the execution of a thread is happening with the control signals. And you can see the familiar
*  elements in the diagram above. So you have a register file, you have the ALU, you have the LSU,
*  you have the PC. And this is the standard CPU style. But the general flow of what you're seeing
*  is you have the register file, you have the ability to access two registers from the register file,
*  which are called the source and transfer registers. That's why they're called RS and RT.
*  And those are also like there in our ISA. And using those registers, there's a ton of different
*  stuff you can do with it. And so the job of a decoder is to tell the compute resources dedicated
*  to thread at any given point in time, what stuff am I supposed to do right now? And so it's going
*  to basically do that by turning off and on different parts of the compute unit. For example,
*  if you look in the ALU, it was just focusing on one unit. So you see the arithmetic unit.
*  And that can do four different things. So we know from our instructions that the arithmetic unit
*  and the ALU needs to be able to do addition, multiplication, subtraction, division. And those
*  are going to be like literally four separate hardware circuits that do each of those things.
*  And so now the question is, the arithmetic unit is taking in these two values, it needs to perform
*  one of those computations, right? So what it's going to do is it's going to take in this control
*  signal, the ALU arithmetic multiplexer, which is much shorter multiplexer. And that's going to tell
*  it, hey, so actually what it's going to do is it's going to do all four at the same time. It's going
*  to both multiply, add, subtract, and divide all of them. And it's going to divide those four outputs
*  into this thing called a multiplexer, which is just like a signal chooser. And so now you have
*  all these possible values it could choose. Now this multiplexer value set by the decoder is going
*  to say, hey, which one should I actually take? So let's say we did like an addition instruction.
*  The decoder is going to set this MUX value to zero, which is we'll say the thing associated
*  with addition. And now that multiplexer is going to take these four inputs, just going to output
*  the one specified by division addition. And that's going to come out into the ALU output MUX. And then
*  here's another multiplexer just to be exhaustive with the design. So now you see like, okay, we
*  have the output from the arithmetic unit. Then again, there's also going to be an output in the
*  comparison unit on every single cycle. So it's not just like we're only performing the computation
*  done by the things that's sent by the instruction. Actually, all the computations are happening
*  because they're just in wires. So they're all disconnected, all the wires are always connected.
*  The question is, which computation are we actually taking this time? So the ALU output multiplexer
*  is going to choose, hey, on this instruction, this should be set to zero because we're going to take
*  the arithmetic unit to output this time. And that's going to get outputted. And then that value,
*  you can see in the rest of the design, most importantly, that's going into the register
*  input multiplexer. And so just to finish this part of the flow, the register input multiplexer
*  is going to be zero this time. It's going to say, hey, we got some value from the ALU. And we actually
*  want to use the ALU value this time and store it back in the register. So you see, okay, we're
*  choosing the ALU output. And then that's going into the destination register, which is what our idea is.
*  I'm going to save that back into the register file in the registry specified by the instruction.
*  And so now you see, okay, that's actually a full loop, for example, with the add instruction.
*  It's basically completing the addition, choosing to output that addition from the ALU, and then
*  choosing to store that output back in the register file, and that's how you get the addition value.
*  And so similarly with the LSU, pretty simple. So you have control signals to enable read of the
*  device. And when you set those signals and everything else is going to be off those times,
*  as specified by the decoder, it's going to make a request out to the memory controller.
*  The memory controller is going to make a request out to memory, and it's going to type it back.
*  And this LSU is going to be in a waiting state. And the scheduler, which we talked about before,
*  is going to see that this threads LSU is still waiting. And it's just going to keep waiting
*  until the LSU gets response from memory. And then the last thing which will help you is the PC.
*  So if you go over to the program counter unit in the top right. So this is the stuff I was
*  talking about before with the whole branch of compare instructions. So generally, the next
*  program counter is just going to be the next line of code, which means we just want to add one to
*  the current program counter. Very straightforward. If we're on a comparison instruction,
*  if you still have the time to do the NCP register. So if we're on a comparison instruction,
*  we are going to actually get the NCP register and that's going to tell us, hey, the comparison we
*  just did, it has these NCP values. It was either NG0 or positive. Then on the branch instruction,
*  it's going to use that NCP tester. You can actually see the NCP signal coming in from
*  the instruction that we said before. And what that's going to do is basically check,
*  hey, did the comparison instruction match this NCP, like the set of NCP values? If it does,
*  and we're going to jump to that immediate values specified by the instruction. Again,
*  you don't really need to understand exactly what every single control signal is doing. If you want
*  to, you can look at the diagram and it will become much more clear, more clear than my
*  explanation. But the important thing is that you understand generally that, oh, this is the layer
*  where actually the instructions are getting literally translated into hardware signals,
*  and it is generally the flow of how the thread gets executed, how the program counter gets updated,
*  and how register values and global memory data values get updated. And that's basically how
*  the entire thread gets executed, like in the kernel. And if you remember in the register file
*  over there, there's those three special values, which give us context on where we are in thread
*  execution. That's getting set by the core. And basically that's how it turns to be executed.
*  This is like the low level of the individual compute of the CPU. And again, it's very similar
*  to a CPU because at this level, we have basically entirely some similarities to CPUs. Basically,
*  it's like a mini CPU here. Cool. That's really very well done. And if you're listening in audio
*  only mode at this point and a little confused, definitely check out the YouTube or jump straight
*  to the GitHub project and check out the diagram because it definitely will help if anything is
*  unclear from the verbal description. Okay. You've designed all this. You've got all the code.
*  We've taken the spike from sort of what you would do at the programming layer,
*  how that gets propagated through the hardware. Is it time to go on to how you actually get to
*  visualize and verify that this is working? Yep. We can go to that. So if you go into the
*  test folder, I'm going to show you quickly how I like simulated everything. And then on the tweet,
*  there's also a video of what's actually happening in GPU. But yeah, so in the test
*  folder, we can just look at, for example, the test mat add kernel. So literally all we have here is
*  I manually compiled all of those kernels I wrote into the valid machine language for my GPU.
*  So here you see the matrix addition kernel. And then in Python, I wrote this external interface.
*  The memory is external to the GPU design. It's not in the hardware. So I made like a simulator
*  right there that basically simulates exactly the behavior of memory. On every cycle, it just
*  checks that there's a request to the memory from the memory controllers. And if there is,
*  it responds with the data. The reason is because memory is not part of the GPU. It's usually like
*  external DRAM or with memory or something like that. So you wouldn't really include that as part
*  of the design. So that's what we're simulating here. In the actual, if I actually tape this out,
*  there'll be an external DRAM similarly like this. And so we load up the program memory here,
*  load up the data memory, as I said, exactly like I was talking about there. And both of these are
*  simulated memory. And then also right there, I've set the value a little below for the device control
*  register, telling it to execute eight threads. And then basically all you do is, so I have this
*  setup program and all that does is it's actually going to take those memory values and load them
*  in. It's actually going to take the threads and load them in. And then it's going to call start
*  and so it's going to set the start sequence to five and it's going to trigger everything.
*  And then we have this little piece of code displaying the data memory, just the visualization
*  purposes. You can see what's starting out as. And then now you're seeing the exact way to interface
*  with it. So you're seeing like, just wait until the GPU is done signal is set to one. In other words,
*  the GPU says it's done. So it starts out at zero, whereas I keep running cycles until the GPU says
*  it's done. And for each cycle, the GPU is going to be processing. And I have this nice piece of
*  code here, which is written on helper files, which is going to display out state of the GPU.
*  And so what that actually does is it's going to show you every single thread in every single core.
*  What are the registers being read? What are the current register values? What is the ALU output?
*  What is the LSU output? What are like the states of the core? Is it like waiting or is it executing
*  or is it decoding or fetching or whatever? Those are really nice to see just like the control flow
*  and debugging. And I encourage anyone who's really curious to see that. That's like a sick learning
*  process. Just go run the matrix edition parallel. There's instructions in the repo and then go look
*  at the log file that gets generated. You're going to see 500 cycles. Like, oh, every single thing
*  that's happening inside the GPU to execute this code, which is pretty fun, but yeah, it's pretty
*  simple. And then I did the same thing for matrix multiplication. So you can see the whole execution
*  trace. Then you could see at the end, it prints out the final data memory and you can actually see
*  the final values that have been correctly computed. And for anyone curious to see if it doesn't want
*  to run it, there's a video of it, which is in the tweet fed. That'll probably be linked here.
*  Cool. This is awesome. Anything else we want to talk about at the real low level? Otherwise,
*  maybe I have just a couple high level questions to ask to conclude with.
*  Yeah, this is great on the low level. People have questions in this DME or put an issue on
*  GitHub or whatever. So with already a lot of people have been contributing to the GitHub more
*  than I expected, but yeah. Yeah. There's definitely a lot of curiosity out there about this sort of
*  thing right now, but it's not easy to go as far as you have. So I'm not surprised at all that
*  people want to follow in your footsteps. Certainly I'm one of them. Coming out of this project,
*  is there anything that still feels mysterious to you or questions you weren't really able to
*  get a good grasp on things you wish you understood better? Do you feel like you have it all
*  reasonably well understood? Yeah. So I think I got basically my goals on it and my goals with
*  anything learning wise in a technical capacity is usually not necessarily to be super niche deep
*  in every single area. Because honestly, I've spent infinite time going deep in any engineering
*  discipline. It's more so to get to a level where I understand the entire landscape from an engineering
*  standpoint and all the key intuitions. And I'm actually deeper than most of the people who are
*  just going in for an entrepreneurial engineering goal. So I don't get able to spar with the
*  engineers and anything and fully understand everything they're talking about. But then I'm
*  mostly like entrepreneurially motivated in terms of obviously this case, there's not really much
*  of an entrepreneurial opportunity. It's like a super lindy industry. And it's like, I'm not going
*  to go compete in GPUs or something. But it's just generally how I approach technical things.
*  And so I feel like I got to the level of intuition where I cannot understand anything I need to.
*  And I put at the bottom of the repo, read me like some of the more interesting, more advanced GPU
*  concepts that I looked into that I didn't implement. So that was fun. But yeah, generally,
*  I think I accomplished my goals. I don't think I would want to spend the time to go
*  super deep into any one of these things, unless I had to be, unless I happen to be interesting to
*  some frontier problem, where it's actually useful to go into those. But that's generally how I think
*  about it. What do you think this tells us if anything about the future of the chip industry?
*  I feel like there's a lot of debate obviously around is Nvidia going to take over the world?
*  Is AMD going to make a comeback? Why is like, TSMC stock not up nearly as much as the chip designers?
*  And I feel like somebody might say, Geez, you made it pretty far in two weeks. If you were actually
*  to try to go manufacture something, you wouldn't make it nearly as far in two weeks. That would
*  seem to suggest that there's something a little out of whack where the like, why is all the value
*  accruing to the design side as opposed to the actual manufacturing side? But what's your take
*  on that, if any coming out of this experience? Yeah, I have my own opinions that I think my
*  opinion is so far from being credible and experienced enough to have a useful take on
*  saying the one thing I'll say is that I don't think there's anything wrong with the value accrual to
*  people with massive moats. It makes sense, especially like this late on. It's such a
*  lindianist share this and I think for people curious about that stuff, all I would say is
*  read 7 powers and 7 powers will just explain why moats make sense and why even though if
*  you guys did this in two weeks, realistically speaking, you can't do anything to challenge
*  these people in most cases. And again, disruptive innovation is the place where you get the challenge
*  incumbents, but that's not really probably going to happen much here. And the incumbents are also
*  very competent. Like in video and TSMC, it's because it's such a well-inceptivized industry
*  that like the incumbents can't possibly become incompetent because of how incentivized it is
*  across all this busy driving the world to start to make a better industry. So it's definitely
*  challenging. And there's also like a lot of takes again, like I can't claim to know about
*  you can challenge TSMC or Nvidia, but a lot of employees in Nvidia, for example, there's
*  like a one viral tweet the other day where a guy who just thought Nvidia was like, now that I've
*  left Nvidia, I can confirm that you're not catching up to them within the next 10 years. And I would
*  think that those reflectives are probably pretty accurate given the nature of the industry and
*  economics of it. It sounds like it definitely is too pill to climb. I think one thing that's really
*  interesting, I'll shout out one company here. They don't need my shout out at all, but like
*  Fulton Atomic Semi. And I think that is probably the coolest attempt at doing anything in this
*  industry in the past 20 years. This is Ken Sandinouf, he's built a semiconductor fab in his garage.
*  And now he's trying to build cheap affordable semiconductor fabs for initially the mid market
*  like the FPGA market. And there's not really an incumbent there. Like basically nobody has ever
*  done it before. The question is not like can he beat the incumbents? It's just is it possible
*  to create it? If he succeeds there, he's going to create a gigantic mid market. It's kind of like
*  what we were talking about here where I was like, oh yeah, hobbyists knew this stuff. But
*  realistically, like most people, if you want to hit rock and scale, you just have to hit the
*  incumbent. You just have to use the incumbents. I think this is something where because he's
*  tackling down market efforts, he's actually legitimately creating a new market opportunity
*  if he succeeds. So I think that's the coolest attempt in terms of this market.
*  If he's trying to do something that will make an impact on the young person.
*  And the value there is custom designs for relatively, like comparatively low end use cases?
*  It's not even that. So it'll actually scale probably pretty far, but it's more like a
*  current chamber costs like $10 billion. And if you want to use them, you have to like chip off
*  your stuff and wait a long time to get back to samples. And then there's also the FPGA market,
*  which is a lot faster, but you don't actually get like a real design. It's like an FPGA.
*  And basically what we're doing is creating fabs that are like way cheaper, like on the
*  order of hundreds of thousands instead of billions of dollars. And you can get your designs
*  immediately because you just buy a fab and you just have it with you, which is first of all,
*  very obviously going to completely change it for the market. But eventually it may actually replace
*  down and mid market opportunities. So it's actually pretty big in terms of you don't even
*  need to go to the huge boundaries. You can just use these things, which are way more price efficient.
*  So that could be huge. Yeah, fascinating. So the idea there would be like enterprises would run
*  their own small fab in the same way that today they might run their own cluster or they could
*  go to a fab provider in the future. They might run their own fab internally because it's been
*  modularized to the point. Yeah. Fascinating. Yeah. Do you have any thoughts? One of the paper that
*  has really caught my eye recently was the Microsoft 1.58 bit paper where basically they showed that
*  you could implement neural networks without, there's obviously been a ton of work in like
*  quantization of the values within neural networks. Right? We go from full long floating points down to
*  smaller and smaller bit resolution. The smallest that seems to have been demonstrated to work so
*  well so far is this 1.58 bit, which is just minus one, zero and one are the only available values
*  in a network. And they still show that you can actually get them to work with that. One of the
*  things they said in that paper was that this opens up potentially totally different hardware
*  future because obviously you don't need nearly as much complication to just handle one, zero and
*  minus one as compared to all the math if you're doing longer precision numbers. Does this give
*  you any intuition for how that might play out in the future? Yeah. So here's just two. One of the
*  things that people criticize about the big measurements of compute power nowadays is flops,
*  which is floating point operations per second. And that's like kind of the benchmark for
*  compute towers versus in GPUs nowadays. And one of the reasons they criticize it is because if you
*  have 32 bit floating point values, if you just switch those to 16 bit floating point values,
*  like drastic and reduce the flops, because it just takes the last time to perform computations on
*  size, sorry, drastically increase the flops. And that's actually what Nvidia is doing. So like they
*  just released their Blackwell. One of the things they've been doing, obviously they've been boosting
*  their flops in many other ways, but their Blackwell now has smaller floating point numbers because ML
*  doesn't really need gigantic floating point numbers on my graphics. And so by doing that,
*  just by nature doing that, they massively boosted the flops. It is actually meaningfully faster for
*  these cases of less relevant too. And so it's exactly the implication. If you use two bit,
*  1.5 bit values, the flops is going to go off quite crazy. And the important hardware thing is,
*  yeah, it's not to happen. Like what that actually means is that those register values, like in this
*  case, again, this is what I meant by it's a bit simplification. You can explain important things
*  with it. So the register values in this case, they're 16 bit register values, right? They store
*  16 bits in them. And in real GPUs, they have a whole host of registers. They have registers that
*  ensure floating point 16 and 32 bit numbers. They have scalar registers and they also have
*  vector registers. So what this means is like in the hardware, you would actually have registers
*  that store two bit values or something like that, one bit, two bit values. And that's going to be
*  way faster. And that's how it gets implemented in the hardware. But yeah, that's pretty interesting.
*  Yeah. I'm curious. It seems to be a big simplification in terms of just a lot of
*  the components too, right? Like you imagine the sort of arithmetic layer that you had where you're
*  saying it's doing addition, subtraction, multiplication, division all the time.
*  If you're down to just a much more limited set of logical operations that you need to
*  perform at each given step, that can presumably just get a lot smaller too, right?
*  Yeah, definitely. Although I'm sure that's what determines the flops increasing, but I'm sure
*  we're grossly oversimplifying a lot of the things because I bet you wouldn't actually just have just
*  two bit floating point registers in your whole GPU. So there's probably a lot of complexity to it.
*  But as an all-in-one situation, I'm sure this is generally valid.
*  Okay, cool. That's all I've got. Anything else you want to talk about? Otherwise,
*  I maybe just ask you what you're on to next. Yeah, honestly, this was cool. It was good talking
*  about it too. I didn't expect it to be this much technical detail. I guess another interesting
*  thing is the place that AI played in this. I guess I thought too much to say there, except that it's
*  very clear that AI has a huge place in learning now. And I think part of my learning philosophy,
*  in many ways people may see me, like people who see my stuff now may think of me as like a
*  chipped person right now or something like that. But really I'm just trying to learn a lot of stuff
*  really fast based on a completely different high level framework I've been using to decide on this
*  stuff, which I'm going to talk about. But I think what AI has made possible is my learning philosophy,
*  which is extremely aggressive. I believe because of this, a number of different things that I can
*  learn stuff and people can learn stuff like 100x, 200x faster than they think. Obviously, as I said,
*  to be able to work less complete depth, but with the same or more practical knowledge,
*  I think AI has enabled that in a pretty crazy way. And this has helped me to really feel the
*  truth of that. Because in many ways this could not have been possible without AI. So that's
*  an interesting takeaway I have. Cool. Love it. This has been a fabulous walkthrough of TinyGPU.
*  Congrats on a successful speed run. I'm looking forward to what your next one will be and certainly
*  will be following you for updates. For now, I will say Adam Mashbuddar, thank you for being
*  part of the cognitive revolution. Thank you for having me. It is both energizing and enlightening
*  to hear why people listen and learn what they value about the show. So please don't hesitate
*  to reach out via email at tcr at turpentine.co or you can DM me on the social media platform of your
*  choice.

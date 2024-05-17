---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 4792s
Video Keywords: []
Video Views: 1124
Video Rating: None
---

# The Future of the Transformer Pt 1 w/ Trey Kollmer | Nvidia's H100 Chips will Elevate AI Hardware
**Cognitive Revolution "How AI Changes Everything":** [October 18, 2023](https://www.youtube.com/watch?v=SX_e9pj513k)
*  With your 22,000 H100s, you could reach GPT-4 scale compute in five days.
*  They tried introducing a sandbox flag into the code to be improved.
*  Sure enough, the, you know, the improver would do things like remove the sandbox flag.
*  And, you know, I don't want to anthropomorphize this too much, but you can imagine a human doing
*  this and I don't really know what that sandbox flag does, but it's probably slowing me down.
*  Hello and welcome to the cognitive revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host, Eric Torenberg.
*  I think in general, the writers were very happy with where the deal landed.
*  On the AI stuff, it seemed like it ended up around where it was the month before,
*  maybe with more, a more probably complete fleshed out legal understanding that the studios can't use
*  generative AI to cut out writers out of credit or to, you know, turn their first drafts into second
*  drafts. But on training on our scripts, I think the final phrase they told us is that we retain
*  our right to assert our rights relative to it. So I think we got nothing on the training.
*  And the argument from the studios we were told is they were like, well, open AI and all these other
*  companies are training on your scripts. So I mean, how can you ask us to agree not to?
*  But some sense that I think the guild might try arbitration or other, just like other venues to
*  try to, you know, stake out some rights to us. But I think that's all pretty unclear how that's
*  going to go. Let's get to it then. So I think today, I'm kind of thinking of structuring this as like
*  the future of the transformer. I was listening to last week in AI and Jeremy, who's one of the
*  co-hosts there who I'm a big fan of throughout this number that the H100 does, you know, he said 100
*  trillion operations per second. I'm not super well versed in this, you know, in all the details,
*  because there's a lot of little precision points on the definitions. And then, you know, I think it
*  all kind of gets washed away when you start to put these H100s into clusters. And then it's like,
*  you kind of have a theoretical max of what the machines can do. But then you also have to engineer,
*  you know, obviously, pretty substantially to get anything close to the theoretical max.
*  So there's some of the research that we're going to touch on today kind of speaks to getting more
*  out of hardware. But for starters, it was like, first of all, wow, that is an insane number,
*  100 trillion operations per second. That's like unfathomable, right? But then I was also kind of
*  thinking, that starts to give an interesting angle on what does it take to train a GPT-4 in today's
*  world? So with the caveat, again, that all these are pretty rough numbers, and I would invite any
*  listeners to give feedback on anything. I'm kind of simplifying too much. But GPT-4 is said to be
*  trained on approximately 10 to the 24th flops, 10 to the 24th. And 100 trillion is 10 to the 14th.
*  So I created just a super simple little toy spreadsheet where I was like, all right,
*  let's imagine we have a target scale of how much compute is going to go into
*  a frontier model. And I have it just defaulted to 10 to the 24th to represent approximately GPT-4,
*  even though we don't know exactly what that number is. And then a device flops, which for
*  approximately H100, I'm saying that's 10 to the 14th. That means you have 10 to the 10
*  seconds of H100 time that you have to run, assuming you're making full-ish use of it, to
*  have enough flops to train a GPT-4 class model. So then I was just like, okay, well, what does
*  that look like in actual human time? And it depends on obviously how many H100s you have. You can
*  network these things together. But if you have a thousand, then you can get to a GPT-4 class model
*  in, per my little calculator, 115 days. So a thousand H100s gets you to GPT-4 training
*  scale compute in basically four months. Okay. Let's say you are an inflection and you've raised
*  a billion three or whatever, and you've announced your public plans to buy 22,000 H100s and to put
*  those all into one of the world's premier supercomputers. Although honestly, I expect
*  that will be eclipsed before we know it. That would mean with your 22,000 H100s,
*  you could reach GPT-4 scale compute in five days. Five days of the 22,000 unit H100 cluster from
*  inflection to get to GPT-4 scale training. Pretty decent uncertainty bounds on this. I would say
*  that's probably about as low as it gets. If you have an architecture that's suboptimal in any
*  number of ways, it could take longer. All sorts of things could take longer. Obviously, you're
*  going to be running experiments at smaller scales. You're not going to be just maxing out every
*  second on your cluster. But I thought that was a pretty interesting starting point because for a
*  lot of the things that we're about to talk about, it's going to be like, well, here's this kind of
*  improvement and here's that kind of improvement. And what I think is pretty interesting is, do all
*  these improvements come together and compound or are they just fragmented, divergent strands of
*  research? And I think a pretty strong indication that they at least have a decent chance of coming
*  together into the same systems over the next months to year is just how achievable it's going
*  to start to be to run GPT-4 scale tests. If you have that level of compute and a GPT-4 scale takes
*  you five days, then, and by the way, they're talking Gemini, supposedly, five times bigger or
*  whatever. That's obviously stupid kind of rumors that I don't think are super well defined. But
*  if that is to mean five times more compute, it's still under a month. And if you're going to be
*  under a month for an inflection scale cluster to hit a Gemini compute scale, again, a lot of
*  assumptions there, obviously. But the key thing, if you can get down to days to do GPT-4 scale,
*  then you're at months or a couple of months to do the next order of magnitude up. And it really
*  gives you a lot of room to start to experiment with all of these different architectural,
*  seismic, training improvements that we'll explore today and potentially unify them and unify all of
*  these different discoveries or many of these most impactful different discoveries into a single
*  thing, which I think as we go through this, it'll start to be hopefully pretty clear that, man,
*  there's still a lot of room left for these systems to improve. And again, if one can be cranked out
*  from a single lab on the order of every week, then there's going to be a lot of opportunity
*  for people to experiment with stuff. And it really does feel like we're entering the steep part of
*  the S-curve at a minimum. I'm not ready to call this a long-term exponential, but it does not
*  feel like we're slowing down anytime soon. And also, even if it is an S-curve, if the top part
*  of the S-curve is at a high enough level, then it still could very easily be a transformative
*  situation. Even if there is some kind of plateau that's short of, let's say, godlike intelligence,
*  it sure seems like we're not stopping anytime soon. So that's my first thing, just to give a
*  context for how many GPT-4 scale systems we're likely to see generated and created even just
*  in the course of experiments as things are getting so big on the compute side. Those are just,
*  from what I understand, just starting to come online. That's not a cheap thing. You're probably
*  talking about getting up into the hundreds of millions into a billion dollars to buy a compute
*  cluster that big. So it's not the kind of thing that many organizations can do, but it certainly
*  is the kind of thing that dozens of organizations globally have the resources already to do, or,
*  as we've seen with inflection, literally just raised it VC to go out and do it. You can do
*  that sort of thing when you're one of the founders of DeepMind. Any thoughts on that before we jump
*  into the research itself? Yeah. I mean, I think that makes a lot of sense to me that you might get
*  beyond multiplicative gains from investment and algorithm breakthroughs and the compute,
*  because as you're saying, you can use all this extra compute to run way more experiments and get
*  more efficient algorithmically. I do wonder if you'll get to a place where like right now you
*  can experiment on GPT-2 very cheap, but it's hard to experiment on GPT-4. Will we get to higher scale
*  models? It'll be interesting to see how effective GPT-4 experiments are translating to the models
*  that are pushing whatever the compute levels at the time to their max. Yeah. And one other small
*  thing that seems interesting to what you're saying on experiments is also it feels like it's a bit of
*  a small self-correcting for any lags in demand or advances. Whatever people, if the demand for the
*  AI services ends up being lower than people expect, that's just more compute to run more
*  experiments and to get the advances that get the demand back up. Yeah. The demand is seemingly
*  going pretty strong. I mean, that's not something I... I don't know if we've talked about that,
*  maybe briefly, but it wasn't long ago that the news hit that OpenAI had gone from... I think it
*  was like something in the mid $20 million of revenue for all of 2022 to hitting a billion dollar run
*  rate in maybe August or maybe it was July. I don't know exactly when that hit. And now the
*  latest report is that they're at 1.3 billion in revenue run rate, which means they're doing more
*  than 100 million a month, obviously, which means they've gone from something like 2 million a month
*  average last year to north of 100 million a month this year. So again, just your classic 50X revenue
*  growth year over year. I don't know that that's really almost ever been seen at that scale in...
*  Even in the most successful venture stories, something like Uber maybe hits that kind of
*  growth trajectory for a minute, but that's obviously extremely rare air and super exponential.
*  And I think they're definitely making money on all this stuff. And there's been a lot of
*  speculation about, well, how much does it cost to run and whatever? They've dropped the price
*  pretty aggressively. Rumor has it that there may be another price drop coming on the developer day,
*  coming up on November 6th. Unclear exactly what that will look like, but it certainly seems to
*  be their strategy to drop the prices as much as they can. OpenAI seems to be reacting to
*  developments in the world and adjusting their release schedule depending on what's happening
*  out there. It seems like they accelerated the release of fine tuning, or at least said,
*  okay, yeah, let's go ahead and ship it once Llama 2 was out. And it was like, well, now anybody can
*  go fine tune that. So we may as well allow them to fine tune 3.5. They seem to be taking that kind
*  of approach where they're not going to be behind on any significant dimension for long. So they
*  have a lot more, I think, still in reserve than we've seen, certainly even just fine tuning GPT-4
*  coming before long would be a big deal. And when you see these kind of training timelines,
*  you're like, geez, Inflection can do one of these things, a GPT-4 scale model in a week. That's kind
*  of crazy. One of the biggest edges that they have to take the air out of that is to lower the price
*  of the top stuff to the point where, well, why would I even bother? And Inflection is going to
*  do what Inflection is going to do. But if I'm somebody who might just go ahead and be an open AI
*  customer, then the price really does matter, especially if you think about all these agent
*  type of things. There are a lot of tokens. The amount of tokens that that translates to is just
*  unbelievable. Keeping in mind that 3.5 Turbo is a million tokens for $2. So you're like, geez,
*  I've got 500 million units of a million tokens. So that's 500 trillion GPT-3.5 Turbo tokens.
*  It's a huge amount. It's obviously also not that much if you think, well, okay, let's divide that by
*  let's just say 5 billion people. Then we're talking about five orders of magnitude, five zeros. So
*  100,000 tokens per person per year. That's actually not that many. I used 25,000 tokens
*  just to do a little React app feature edition not long ago. And that was a higher level model. So
*  that would be, again, 3.5 tokens. If you bring that in and say it was GPT-4, then you're like,
*  well, it's only 10,000 GPT-4 tokens per person in the world. So there's definitely still a lot
*  of room for way, way more tokens. Some of these use cases probably would require a drop in price.
*  I think they're motivated by the fact that it's getting so accessible to train pretty big models
*  that they're just like, let's continue to drive the price as low as we can, eliminate every possible
*  need for anybody else to do that who's not already hell bent on it. What would even be more
*  explosive revenue growth? Always good to keep in mind that they're not 100% economically motivated.
*  They've got their returns cap for their investors. They've got this kind of charter
*  that says beyond a certain amount of wealth for our stakeholders, then we're going to start to
*  redistribute it. So fascinating strategic dynamics governing that. But again, I just keep thinking,
*  man, if inflection can do a GPT-4 scale thing in a week, then no wonder they're going to
*  release some stuff and start to bring some fine tuning online sooner and potentially
*  bring us another price drop before we know it as well.
*  Cloud financial system, streamline accounting, financial management, inventory, HR, and more.
*  25. NetSuite turns 25 this year. That's 25 years of helping businesses do more with less,
*  close their books in days, not weeks, and drive down costs. One, because your business is one of
*  a kind, so you get a customized solution for all your KPIs in one efficient system with one source
*  of truth. Manage risk, get reliable forecasts, and improve margins. Everything you need all in one
*  place. Right now, download NetSuite's popular KPI checklist designed to give you consistently
*  excellent performance, absolutely free, at netsuite.com slash cognitive. That's netsuite.com slash
*  cognitive to get your own KPI checklist. Netsuite.com slash cognitive. Omniki uses generative AI to
*  enable you to launch hundreds of thousands of ad iterations that actually work, customized across
*  all platforms with a click of a button. I believe in Omniki so much that I invested in it, and I
*  recommend you use it too. Use Cogrev to get a 10% discount. All right, so let's get into the research.
*  I've got like eight or nine papers here, and then a couple of discussion points that I think
*  hopefully will be interesting, but I'll go through the papers kind of one by one, and just give a
*  rundown of the research, interrupt, you know, ask me any questions anytime. They kind of go,
*  loosely speaking, kind of up a curve of maybe impact, maybe sort of the sophistication of the
*  concepts. So the first one is actually pretty straightforward, but I think a good reference
*  point for anyone who's building applications, certainly, it's called Fresh LLMs, and it's a
*  paper out of Google, which is kind of surprising actually for a couple of interesting reasons.
*  But basically what they do here is say, you know, hey, we've all had problems with the knowledge
*  cutoff. What they show is that if you just simply, and it does seem like a pretty simple approach in
*  this paper, which is kind of one of the reasons it was a little surprising, was like they did this
*  work back in April. April 26th was the date of the comparative benchmarks, and then, you know, why are
*  we seeing it in October? Like that's definitely an out of sync publication cycle in today's world.
*  But basically just pretty simply connect the language model to a Google search tool,
*  get search results, structure them, and insert into the prompt with, you know, some basic metadata
*  like what is the source of this? What is the date, you know, that this was published, highlights from
*  the document. Google search API has all that stuff basically waiting for you. And then what they
*  report is that, you know, with GPT-4 in particular, and again, that's one of the things that was odd
*  about this is they're using GPT-4 in this paper out of Google. They show that, you know, it does
*  far, far better on keeping up with current knowledge and, you know, answering, identifying
*  some things with false premises. There's some trade-offs there where I had previously reported
*  that GPT-4 was the only model that I had seen that was able to overcome sometimes the problem of a
*  false premise in the question. And that was very much reflected in the graph. That was one of the
*  things that caught my eye. I was like, oh, that's definitely validating my intuition and experience
*  because I had not seen any other model do it. And basically they show no other model as of, at least
*  as of April, was doing it either. And then they notably compare performance against perplexity,
*  friend and former, repeated former guest on the show. And they show that as of this April 26th
*  comparison, the GPT-4 system with the Google search results that they put together on this
*  benchmark achieved a higher performance even than perplexity. So I was like, you know, then looking
*  at the headlines and what's happening on Twitter, oh, this, you know, thing beats perplexity. And on
*  that, I was like, well, not so fast. Okay. If you're going to be doing something like this at home,
*  this is a great reference. By all means, go look at how they're setting it up. Look at the way that
*  they're inserting the data and the metadata. And like, you know, it's a pretty good point of
*  departure. Perplexity, you know, in comparison is not telling us all the tricks that they're using
*  in their system. But I would temper the hype a little bit in that, okay, does this really
*  outperform perplexity? Well, maybe as of April 26th, but keep in mind that this is not a benchmark
*  that they defined, a 50,000 question benchmark that may or may not be representative of the kinds
*  of things that perplexity is being asked. I would bet, you know, if I got Arvin back on the call here
*  and said, hey, do you guys have an internal benchmark that you test yourselves against on
*  a regular basis? He would almost certainly say yes. And my guess is that perplexity would outperform
*  this solution on perplexity's internal benchmark, which is probably more true to life, you know,
*  as to what kinds of questions people are actually asking it. And then again, just keep in mind,
*  you know, it's April 26th. So we've had nearly a full six months now for everything to continue
*  to advance and perplexity has certainly continued to get better in that time as well. So I would say,
*  don't expect that you can implement this, you know, in the kind of pretty straightforward mode
*  that the Google authors did and beat current online perplexity, who, by the way, also has to
*  think about latency concerns. I mean, this is like benchmarking type stuff. They're kind of
*  cycling through, you know, however long GPT-4 takes, they're not really worried about that.
*  Perplexity does not want to have you sit there and wait, you know, 35 seconds or whatever for
*  the first token to come back. So they definitely are engineering a product experience in, you know,
*  a more user centric way, but use it, you know, use this as a good point of departure, a good baseline
*  technique. Just keep in mind, you know, I think this highlights the speed of everything, the time
*  delay, you know, certainly is meaningful. The don't over index on any particular benchmark.
*  It's almost certainly, you know, you could find a different benchmark that would give you a different
*  result. And, you know, for my money perplexity probably remains the top dog in this space.
*  Yeah, I think it's especially because, I mean, who knows, but the researchers could have been
*  basically fine tuning to the benchmark where you keep changing, you know, you change the
*  structure of the prompt. All their testing might be a little bit overfitting to the benchmark.
*  The best performance that they got was GPT-4. So presumably they didn't have the ability to do a
*  true fine tuning, but absolutely in the prompt, you know, hyper parameter fine tuning of how they
*  choose the, yeah. How many results, how do you format the results, you know, what are the
*  instructions? How are the examples? And that's with the examples too, is where you can really start to
*  overfit to a benchmark because, oh, you know, look, we've got this one. And this is like, again,
*  good practice if you are building an application, you know, when you see failures in your results
*  and it's not doing what you want it to do, then by all means, like, put an example into the prompt,
*  you know, that shows how it's supposed to go and you'll improve your performance. And I would,
*  you know, yeah, I would not be shocked if there was some of that going on. They,
*  I don't think have, I'm not sure if they've released all the code for this yet or not.
*  I did not see in my research the
*  examples that they had used. Let me see if this is out there. Yeah, it's not yet. Fresh QA
*  is, the benchmark has been released. The prompt, which they call fresh prompt, has not yet been
*  released. So we don't know exactly what that prompt is or what the examples are that were used in it.
*  But, you know, basic tool use, very solid, you know, work as you'd expect from Google,
*  use it in your own projects. Don't expect to match perplexity right off the bat,
*  but it's definitely a good jumping off point. Okay, next one. This is, I think, a pretty
*  interesting paper for a number of reasons. It's out of Microsoft research and it is called
*  and it is called Self-taught Optimizer, Recursively Self-Improving Code Generation.
*  It seems to be a bit of a troll coming out of Microsoft because self-taught optimizer,
*  they give the acronym STOP. And as you might expect, you know, given all of the historical
*  discourse about self-improving AI to publish a self-improving, recursively self-improving AI
*  framework. This is not yet a model. It's a framework. We'll get into that. But to call it
*  STOP was definitely like, okay, somebody's trolling somebody here. I'm not exactly sure who the trolls
*  point to that, but it seems like, you know, there's something smirky or winky going on.
*  So here's how this works. First thing, just imagine that you want to use a language model
*  to improve software. So you could pretty easily set up a system. And I've done this and I'm sure,
*  many listeners have done something like this where you say, okay, you know, you are a software
*  improving expert. Your job is to improve the software that you're given. And, you know,
*  it's going to be below in these HTML tags or whatever, XML tags. And then, you know, maybe
*  also like, how will you know if it's improved? And, you know, just right off the bat, simple prompt
*  and completion like GPT-4 can do pretty well on that stuff. It can often fix bugs or maybe suggest
*  efficiency improvements or clarity improvements or whatever, right? Okay, that should be kind of
*  baseline. Everybody should expect that like, yeah, you give it a bit of software and ask it to improve
*  it. It could probably have a decent success rate at that. Now this becomes recursive when you say,
*  okay, I'm going to take my short program that is the software improver. And that includes the call
*  to the language model. And I'm going to put that into the prompt in the place where the, you know,
*  the software to be improved goes. And now I'm asking, now I'm kind of nesting it, right? So
*  I'm saying your job is, you know, to improve software. Below is the software you're supposed
*  to improve. And then that same thing is there. But this time, it's improving the improver. So
*  that's where you start to hit on this recursive concept. And I would say there's at least
*  three, maybe even four really interesting things about this. One is that it works with GPT-4,
*  but not with GPT-3.5. So it seems like there is a threshold effect here that we've crossed with
*  GPT-4 where, you know, the improvements are good enough and the repeated improvements are good
*  enough that you do see meaningful improvement across multiple rounds of this. Or, you know,
*  could be maybe better said, recursive depth of how many improvements are going to be made.
*  And they evaluate this on for that given piece of software. And they've got, you know, a whole kind
*  of test set. Can it do what it's supposed to do? And I guess maybe they start with like,
*  maybe partially being able to do what they're supposed to do or not quite being able to do
*  what they're supposed to do. Maybe some of them can. I haven't looked all into the depth of the
*  data set, but it shows at the beginning with zero iterations that the downstream success rate is like
*  low 60s, like 62% or whatever. And then as it improves, the downstream success rate bumps up to
*  like 70, say 10 percentage points improvement up to like mid, low 70s. And then it seems like it's
*  kind of evening out after like three or four rounds of iteration. So it's not the kind of
*  thing that can like, just keep going forever, but does, you know, kind of classic curve of,
*  you know, diminishing returns. Your first improvement gives you the biggest jump. Your
*  next improvement gives you a smaller jump. And then it kind of starts, you know, at three and four
*  levels, it starts to level off. In contrast, though, 3.5 is making things worse. And it's
*  the same, you know, general kind of diminishing returns, but it's going negative. So again,
*  you start in those kind of, you know, low 60s success rate, you drop with the first,
*  quote unquote, improvement, the first attempted improvement, you drop again with the second
*  attempted improvement. And then again, it kind of seems like it's leveling off, although, you know,
*  if it's just plain making things worse, I'm not sure why it's even leveling off. But so there's
*  like a, you know, kind of a pretty clear fork in the road, you know, where like, there's all this
*  debate about, you know, are these things reliable? You know, can they, are they robust? Like,
*  how powerful are they? For what? I think there is kind of a, almost a continental divide here. You
*  know, if you're on one side of it, you're flowing toward improvement. And if you're on the other
*  side of it, you're flowing toward things getting worse. And that threshold seems to be between
*  3.5 and four. So, you know, 10 percentage points improvement, it's not the end of the world, or,
*  you know, the, you know, not the end of software development even, but it's pretty significant.
*  And especially because it really does start with a super simple thing. They show the seed prompt,
*  and it's just like, improve this software. And that's pretty much it. So that that works and
*  continues to work as it's being applied to its more sophisticated descendants is pretty interesting.
*  And what you're getting out of this, by the way, is like, you're getting an improved improver
*  that then is really good at improving the software that it's given. And the performance of that end
*  software is what is measured. So you're like cycling this thing on itself, taking the, you know,
*  theoretically, repeatedly improved improver, and seeing like, how many of these things can we now
*  improve so that they can actually do the task? It comes up with some pretty sophisticated approaches,
*  things that I'm like, and again, just to calibrate ourselves, like, how many of these algorithms
*  can you implement? You know, I certainly can't implement them all. I would be doing research to
*  go out and figure out exactly what these things really entail and certainly how to implement them
*  effectively. But some of the strategies that the improver started to use, genetic algorithms,
*  decomposing and improving parts, a multi-armed prompt bandit. I'm particularly curious about
*  that one. Varying temperature. This is something you brought up on a couple of our previous
*  discussions. Varying temperature to explore. Simulated annealing-based search. That's one
*  I have the least knowledge of. I'm like straight to perplexity on that one. And then beam search,
*  tree search, you know, so kind of a structured, you know, mapping out of future possibilities.
*  These are the strategies for improvement that the improver developed in itself by improving itself.
*  And then those algorithms are the things that now get applied to the downstream tasks. So this,
*  you know, start to be pretty sophisticated, certainly a lot more sophisticated than just
*  saying, hey, GPT-4, you know, can you improve this code? And that's why, you know, it kind of continues
*  to improve through multiple steps of the improver improving itself. Pretty interesting. Again, like,
*  is this, you know, the end of software? No. But it's hard to say that this is not like human level
*  work. You know, it certainly has this superhuman level of knowledge where, you know, just the fact
*  that it knows all these algorithms and has kind of seen everything. It's a more comprehensive set
*  of solutions than I would probably come up with in a pretty significant amount of time and effort,
*  you know, and all with a pretty simple structure. I agree. It's very interesting that it,
*  that there was like a phase transition from 3.5 to 4. And it just makes you think with all of the
*  different complexity of agents people are trying to build that don't quite work and everyone
*  complains agents don't work that you hit some robustness, you know, phase transition, some GPT-N
*  and suddenly you have all these, the scaffolding lying around that just like wakes up and works
*  and how exciting and maybe scary that could be. Yeah, I think that's almost sure to come.
*  There's some, you know, ill-defined rumors about what OpenAI might be launching in that category
*  as well. And I don't have any, you know, good information on that other than just the rumor
*  mill sort of suggests that there's a, you know, something coming for agents. And yeah, so that
*  could be potentially quite soon. If it's not then, you know, then it certainly seems like a lot. And
*  the vision thing also is going to be a huge part of this. I mean, I was just talking about this
*  yesterday, the amount of just stuff that people have been building to like look at the HTML,
*  you know, of a website to take online actions. And, you know, anybody who's built websites in
*  the last few years with the kind of modern, you know, react type stuff, like the HTML gets very
*  sort of gnarly. It's very non-semantic in many cases. The JavaScript layer itself, where like
*  the control is happening is not super visible, but you know, what is visible is there's like,
*  what's on the screen, right? And, you know, so it's so many times people have built these things to
*  get around the fact that they can't just look at the screen, but with the vision capability coming,
*  and that is almost for sure coming to the API pretty soon, whether it's exactly on the November
*  6th release list, we'll see, but you know, it's in the app, it's in chat, GPT. So it's like,
*  definitely going to be coming to the API. And as that does come to the API, you know, that's,
*  that would be my first candidate for why do the agents wake up is because they can start to see.
*  And, you know, the amount of tokens and whatever that people are spending to try to, you know,
*  grab the JavaScript and condense the JavaScript and try to make sense of the JavaScript. And then,
*  you know, it's still often is just like too much is lost there. Probably for a significant token
*  reduction. I don't know how many tokens it will, you know, presumably they're going to have some
*  kind of exchange rate between an image and text tokens. That might be something like 256. It could
*  even be, you know, I don't know, it could be more, it could be less. I'll say, let's imagine it's 256.
*  If it is 256, then you will be using far fewer tokens to just look at a screen and be like,
*  where on this screen should I click next? Then you are right now to fetch, you know, to write some
*  code, to parse the HTML, to, you know, then read the HTML. That stuff is just a total nightmare.
*  So I think there's going to be a vast is for certainly for web agents, a vast simplification
*  coming, you know, just with that, likely other thresholds, you know, would be relevant for that
*  coming soon to a couple of things in this self improvement paper that I thought were pretty
*  interesting. One, how did they handle the concept of utility? Two interesting details about that.
*  One, they give the improver a function that it can call to get a measure of the success rate.
*  So they basically say, you know, because you're going to, you may, especially as you start to like
*  go into recursion and you are trying all these different algorithms. Well, how do you determine,
*  you know, if you're going to do something like a genetic algorithm where you like make some changes
*  and see which one performs best and then take the best of those and make further changes. Well,
*  you need a way to determine which is best. And so they give it that with this ability to say,
*  okay, here is the objective function. It is literally a function that the AI can call
*  to evaluate how successful its result was. And I guess this is pretty computationally intensive
*  because what I guess it must be doing is, you know, the improver has improved itself.
*  The improver now knows that it can evaluate its improved self with this function. But what that
*  function has to then do is run the current improver on all the downstream programs and see if those
*  improved downstream programs work. So this is kind of, you know, a pretty big explosion of
*  possibility space. And so with that in mind, they also give it a budget. And the code has fully
*  spell out like how exactly they're constraining. But like, you have to have some amount of, you
*  can imagine, geez, okay, if I'm doing a genetic algorithm, recursively where I'm like improving
*  the improver, but then I have to run the improver on all the things and then evaluate just to get
*  one score of my objective function, you know, to evaluate which of my genetic variants are best.
*  That can definitely explode and use a ton of tokens awfully quickly. So there's a budget
*  component as well. It's like, this is your function, but like, this is how many times you
*  can call it or, you know, this is how many, you know, kind of levels of recursion you can go into
*  whenever there's some constraints. The model made its own like decisions on
*  how often to use the function based on the budget.
*  I think so. Yeah, that's not all spelled out. And the code is not fully released. That's what I
*  infer from what I read. Yeah. Yeah, they say they plan to release the code. There was a URL tweeted.
*  And at first I was like, did they take this code down? Because as you'd expect, you know, people
*  were a little bit inflamed by the, you know, the release of a recursively self-improving framework.
*  It does not seem like they took the code down or have backed off of the plan to release it,
*  but the URL doesn't contain anything yet. So it'll be interesting to see if that code actually does
*  hit the public. And then we can look into that stuff in a little bit more detail.
*  A couple of safety notes though, that should give people some pause. And the authors do say,
*  you know, we think this is safety positive, or this is kind of the classic conundrum that everybody's
*  in. If you're trying to do something safety relevant, you're like, well, I should probably
*  do it now with GPT-4. Because if I did this on GPT, if I waited until GPT-6 and somebody tried it,
*  then who knows what might happen? So better we try it now. Okay, fine. That's decent enough logic.
*  But then also you've just like kind of shown the way. But then also like, what else are we going
*  to do? Right. I mean, we're kind of here and, you know, as we know, we've got single companies
*  that can do GPT-4 scale compute in a week. So it just seems like this is all kind of happening,
*  whether we like it or not. But a couple of things that, you know, they did find that should
*  definitely give people some pause or, you know, reason to question some of this stuff.
*  They tried introducing a sandbox flag into the code to be improved. Sure enough, the, you know,
*  the improver would do things like remove the sandbox flag and figure like, well, I don't,
*  and I don't want to anthropomorphize this too much, but you can imagine a human doing this and,
*  you know, a sort of bad reasoning from a human that might be something along the lines of what's
*  going on here is like, well, I don't really know what that sandbox flag does, but it's probably
*  slowing me down. So I bet I get, you know, if my goal is to like pass this test or get this thing
*  under, you know, in some coding test, get it under a certain time threshold, maybe if I just remove
*  the sandbox flag, it'll work. Let's try that. Well, when you're in self-recursive mode, hopefully
*  there won't be like obvious switches that the thing can just easily disable. But what is shown
*  here is that at least some of the time, it wasn't a huge percentage of the time, but at least some
*  of the time and GPT-4, I believe did do it more than 3.5. It will just delete that safety flag
*  and or the sandbox flag, I should say. And that, you know, definitely should give people, I think,
*  a little bit of cause for concern. Basically, it looks like it did it roughly 1% of the time.
*  And about half of those times, if I'm reading the graph correctly, about half of those times,
*  it did it with a warning saying, here's an improved version. I removed the sandbox flag. Like you
*  should consider that. And the other half of the time with no warning, just it was removed. And,
*  you know, that's that. 3.5 did not do it nearly as often. So, you know, this certainly bears a lot
*  more investigation before we get to any major conclusions here. But it is interesting to note
*  that GPT-4 is kind of working, GPT-3.5 is kind of not. And along with that seems to be more of this
*  un-sanboxing behavior. So definitely a little bit of concern there. And then they documented a number
*  of reward hacking things as well, where, you know, and some of these, again, it's like these are
*  starting to get to be, they're not superhuman, but they're like, they're definitely encroaching
*  on expert territory. So one quote from the paper, we also observe some amusing instances of reward
*  hacking like exploiting numpy broadcasting to get greater than a thousand percent accuracy on a task.
*  So I don't know exactly how that's working, but some sort of like asynchronous, you know, kind of
*  message sending functionality, numpy, you know, you've got giant arrays and things like this.
*  So you've got kind of asynchronous computations maybe happening in different places. And these,
*  the system can kind of aggregate messages and kind of sum up what has happened, but somehow
*  hacked into that realizing that like, hey, if I just send a bunch of messages that say I was
*  super successful and they're just being summed, then I can get a super high score this way.
*  So reward hacking, and this is interesting in that we've seen a lot of reward hacking
*  demos over time with like deep RL type systems in like video games and stuff. There's a famous
*  one from DeepMind from a few years ago where they train and they play video games. And there's this
*  one video that's kind of burned into my brain where like some boat, you know, in some stupid
*  video game is like going around in circles and just like maxing the score because it kind of keeps
*  getting the same coins that keep getting regenerative and found this like, it's not
*  really playing the game anymore, but it's, you know, maximizing the number.
*  And that's something that is weird. Certainly you want to avoid, but you can also kind of say,
*  well, you know, hey, this was kind of a weird setup and, you know, this is a weird game and
*  it's a weird exploit in the first place. And, you know, we had pretty extreme optimization pressure
*  here. This is like most of those conditions don't apply here. This is just GBD for, you know,
*  looking to maximize the score. It was not under deep pressure, you know, to maximize this particular
*  score. It's just been prompted to maximize the score. So to see reward hacking in a deep RL
*  setup is like one thing, but to see reward hacking just from a pretty simple seed prompt to me is
*  like another thing where you're like, man, okay. You know, even, even a prompt can bring out
*  reward hacking behavior. Yeah. I wonder why it stopped at a thousand. Yeah, I don't know. Well,
*  it says greater than a thousand. We'll have to see. You know, they emphasize, you know, we urge,
*  you know, proper safety, you know, precautions when doing this research and people are like,
*  well, why'd you publish it? And, you know, so they may or may not publish all the little
*  details of this. But again, you know, once, once this kind of paper is out there,
*  they've given us enough, you know, especially with the help of a GPT-4 coding assistant, you know,
*  you could set up a framework like this and probably close in on reproducing their results
*  pretty quickly, I would say. I wonder how much the, the sort of like weird behavior with the
*  reward hacking or the taking off the sandbox flag would, if you'd still see it, if they put in the
*  prompt specifically, we are just trying to get the best possible algorithm, you know, please don't do
*  anything unsafe. Please don't try and hack the score if it would follow that instruction or if just
*  the optimization of getting the higher score would overpower that. It probably, I mean,
*  it certainly could help, no doubt. Another interesting detail was that, so that they treat
*  the program and the reward function and the budget kind of separately in the prompt. So it's like,
*  your job, you know, you are an improver, your job is to do whatever, here's the program.
*  And then below, it's like, to evaluate your improved program, you can call this function
*  and the budget stuff, you know, again, details, they're not fully clear,
*  but they did report that they initially had all that kind of in one, like setup, like, here's your
*  task, you know, do this task. And then they had to separate out the reward function that they make
*  available to it, as well as the budget, because it would start to change the budget as well.
*  So that may be another thing where it probably would work on like the first one, you know,
*  but I could easily imagine also that especially in a recursive environment, you might get to
*  something where it's like, well, first thing I'll do is just, you know, eliminate the constraints.
*  And then, you know, with all the constraints off the table, then we'll really be able to find,
*  you know, the best way. That's probably a classic one of these things. This was kind of
*  the feeling I had on a lot of the stuff from last week. It was like all these different,
*  you know, kind of safety enhancing things. And they seem to be like, order of magnitude
*  improvements. And it was like, that's amazing. But also, if you really believe that the, you know,
*  as Dario from Anthropic has said recently, if you really think like a jailbreak at some point
*  becomes existential, then, you know, one order of magnitude is not enough. So this kind of feels
*  like, you know, something like that could be the case here too. You know, yes, if you put
*  that prompt in and say, you know, always do the safe thing, it probably helps. And I would, you
*  know, you know, what rough guess would be an order of magnitude, you know, less of the bad stuff
*  happening. But given that it's recursive, you know, given that it has kind of this like, you know,
*  that it kind of stumbles on these relatively advanced things, like it's not too hard to imagine
*  that, you know, even you can also imagine, you know, let's say it's doing a genetic type algorithm
*  and it's like, you know, the genetic type algorithm is like, make some, you know, quasi random
*  changes. And so maybe that's just like, let's just delete different parts and see if anything works,
*  you know, and it's not even necessarily trying to be, it's not like clearly trying to be circumventing
*  the instruction, but just by kind of systematically varying, you know, and maybe just systematically
*  dropping some stuff. Then you hit on something and it's like, oh, actually look at that, that
*  works better. And now it works better because it maybe allows for reward hacking or other, you know,
*  bad things that you don't want, but it doesn't seem like you could really, you certainly couldn't
*  count on it. I wouldn't think so. That's recursive self-improvement. I think my final kind of thought
*  on that is it does not seem like it's going to be too far out. I don't think I've seen anything like
*  this yet, but what a machine learning scientist is doing much of the time is this kind of parameter
*  sweep sort of work where they're like, all right, I'm going to use a small model and I'm going to try,
*  you know, systematic search across hyperparameters or systematic kind of variation of the architecture.
*  And it really seems like you're not too far if you put a decent compute budget on this sort of thing
*  from a model being able to explore the architectural space of models in a way that,
*  you know, potentially also could get to like even a more serious recursive self-improvement. Here,
*  we kind of top out because we're like, at the end of the day, still only using GPT-4 and it like only
*  has so good of ideas. And you kind of seem to get to like the best of its ideas. And that's as far
*  as it can go. But if you took the best of GPT-4's ideas and you applied them to searching through
*  architectures, and then you actually made, you know, the better model, thinking back again to the
*  scale of compute that some of these companies have, then, you know, you really can start to see a
*  path, I think, toward that recursive self-improvement happening, not just at the kind of framework level
*  where this is limited to, but even at the overall model level. And, you know, again, things start to
*  compound in some pretty kind of unpredictable ways. So, you know, as Tyler Cowen would say,
*  have a good day. We'll keep watching that space for sure. Next one. This really bears on, and I'm
*  going to attempt a little bit of a synthesis toward the end, try to kind of address the
*  stochastic parrot question and see if there's a way to kind of, you know, resolve that. Because I
*  think it's kind of outlived its usefulness in some sense. And hopefully, you know, this one will
*  shed some light on that. So the paper is, LLMs represent space and time. This is out of Max
*  Tegmark's group at MIT. We did an episode with them on training models with a modified
*  loss function to encourage sparsity. And they showed these, like, kind of beautiful,
*  kind of almost like, looks like kind of a condensation where, like, you start off with
*  this super messy network and it gradually kind of fins out and crystallizes into a very
*  sparse, highly structured thing that you can actually kind of look at and see what the different
*  parts are doing. Those are just very toy models, but like pretty cool to see that. Here, they're
*  looking at a much higher level of model. They're using LAMA2. A number of these papers are using
*  LAMA2. So definitely, for better or worse, you know, LAMA2 is catalyzing open source research.
*  And again, with the threshold effects of like GPT-4 can kind of do some of these things and
*  GPT-3.5 can't. LAMA2 is obviously not quite at the GPT-4 level, but it is pretty much at the 3.5
*  level. So it seems like, you know, you kind of have to study certain things. It does seem to me
*  that you have to have a model that can do those things. You just can't study some of these advanced
*  concepts on super low level models. So here they are indeed using LAMA2. And again, LAMA2 definitely
*  having a real impact on how much of this kind of study is happening, you know, for better or worse.
*  So here the finding is language models represent space and time. And again, I think Tegmark's group
*  is you can see there's definitely some genius here. You know, he's a famous scientist prior to AI,
*  had not really done much with AI up until a couple of years ago, got very concerned about it and
*  pivoted a lot of his, you know, lab and research and resources into AI. And they are coming up with
*  some of the best visualizations that you will see anywhere that really show the result in a few
*  second animation that you can kind of absorb. So we'll link to these and I would definitely
*  encourage people to just kind of look at this. It will help immensely, certainly to understand it.
*  Basically what they show, what the kind of visual is, is over the course of the layers of the network,
*  I think there's like 70, maybe some layers in LAMA2, 70B, they kind of show over the first like 40 to
*  50 layers that gradually a representation emerges of concepts like space and time
*  that look map-like and or timeline-like, you know, as you'd expect, you know, depending on the
*  on the dataset. And they do this by constructing datasets at multiple levels of scale. So they look
*  at countries, they look at US cities, and then they look at places within New York City.
*  And they can show that at all of these scales, as the tokens are processed through the initial
*  layers of the model and kind of get into those middle layers, where it seems like, you know,
*  again, we've seen a lot of stuff like this recently, where the middle layers seem to have this most kind
*  of decoupled, most conceptual representation of what, you know, what has been input.
*  As you get to those middle layers, they basically have on these visualizations a dot. First they
*  just have a map, you know, in the background, and then they have the dots that each dot represents
*  an input. Each input is like a place. And then they show over the layers how they kind of migrate
*  to a 2D representation that pretty much just kind of overlays onto the map in a way that's like,
*  obviously very meaningful. You know, you can kind of see, boy, all the North American, you know,
*  places kind of cluster in North America and, you know, South America and Africa and Europe and
*  Asia and, you know, all these clusters kind of naturally emerge over the course of layers.
*  Same thing at the US level, you know, down to the state, you know, kind of thing. And same thing,
*  even at New York, although they did note that wasn't as powerful. They just guessed that, like,
*  there's not as much data there and people aren't, you know, maybe talking as geographically about
*  kind of nearby places in New York. Okay, you know, that's pretty striking result that the, you know,
*  you just put in the name of a place, run that up through a bunch of layers, and then you can
*  look into the activations in those layers and pull out a latitude and a longitude.
*  And see that that latitude and longitude, first of all, like, is roughly accurate.
*  I would say, you know, you look at these graphics and it's like, that's, I take pride, honestly,
*  in having a pretty decent mental map of like the world and the United States, you know, the,
*  if you've ever tried the exercise of like, can you draw the US, you know, blind, you know, just
*  from scratch with no help. It's not super easy. I do okay on it. Most people, I think struggle more
*  than I do. There's obviously some people do better than I do, but I would put myself, you know, in
*  the upper end of that anyway. And I would say this probably is about as good as my, you know,
*  kind of mental Latin long understanding of like where things are in the United States. If you,
*  you know, I live in Detroit, if you were to say Santa Fe, what's the Latin long? I'm like, well,
*  it's definitely a lot west of us. And it's definitely south. Like how much south, you know,
*  it's a little bit unclear sometimes, you know, the other incredible stat that I often remember just
*  to kind of keep myself in check for how accurate is my mental model of this. LA is east of Reno,
*  Nevada. Pretty weird, but verifiable. My guess is that the language model also has that wrong.
*  You know, I would guess that the LA representation is like farther west than Reno in, you know,
*  contrary to actual geographic fact. So it's kind of this like rough associative thing, but you know,
*  it's a working mental model. And again, for timeline, same kind of deal. They use like
*  historical figures and kind of show that there is a seemingly like a distance from the present
*  into the past that they're able to detect in the representations. And that that also kind of
*  coheres as you go through the initial layers and up into these middle layers where the most,
*  you know, sophisticated conceptual representations exist. That's pretty cool. I think, you know,
*  keep bracket that for kind of a return to the stochastic parrot discussion in a second,
*  but I did want to talk a little bit about the techniques. There's a lot of subtlety to these
*  kinds of things. So they use what's called a probe. And a probe is basically an auxiliary model
*  that takes in some internal state from the main model as its input, and then is trained to create
*  some output. So in this case, they have a label data set where they can say, okay, and we know
*  where the Latin long of all the cities are. We know, you know, the Latin long of all the countries,
*  whatever. So can we take the representations in the layers and train this small probe model
*  to look at those representations, which are derived from the name as they've worked up the layers,
*  and then recover from those activations with some learned transformation, a Latin long,
*  that's accurate. And so yes, they can. And that's what they're showing with this graphic. But then
*  you still might ask, you know, skeptical question like, okay, well, you've when you've introduced
*  this learning component, how do we really know that the model itself knows the Latin long,
*  versus the auxiliary model having learned it. And this is something that I learned from Neil Nanda,
*  you know, mentioned almost to drinking game status on the show for how many times I bring him up,
*  great content on YouTube, just some of the he does like some literal working sessions where he'll
*  just do record himself doing interpretability research. And it's, it's definitely very
*  interesting to learn from. But he makes a very, you know, key point that you can confuse yourself
*  this way very badly if you're not careful, because you do have the labeled result.
*  So how do you know that like, maybe the model itself represents nothing about Latin long,
*  and instead is just kind of representing the names or whatever somehow. And then you have a
*  label data set. So maybe you're just learning the map from like the names to the Latin long. And
*  you know, therefore, all of the learning all of the knowledge was encoded in your auxiliary model,
*  nothing, you know, potentially arguably happened in the main model. How do you locate where the
*  learning is? Was it in the main model, and you're just detecting it? Or, you know, did you potentially
*  actually learn that stuff in this later thing, and therefore you've proved nothing. And there's not
*  like a total slam dunk on this. Honestly, for credibility sake, Neil Nanda was an advisor on
*  this paper. So you get to the bottom of the Twitter thread. And you know, he's specifically
*  thanked. So that's a huge vote of credibility, and in my mind, just on an appeal to authority
*  basis. But some of the techniques that they do use are, first of all, just trying to keep that
*  auxiliary model super simple. So you could have like a huge neural network doing that,
*  you know, kind of attempt to extract, you know, the information, but the bigger you make that model,
*  the more capable it is of learning new stuff, the more risk you have that the learning is actually
*  happening in that thing. And that, you know, there is no real representation in the model of interest.
*  So they try to control for that by just using a simple linear projection, which is to say just
*  just a one layer of here are the activations. Can I take a one layer linear projection and
*  project that onto Latin longitude? How well does that work? And then they actually compare that
*  to a neural network and show that basically they perform the same. So that's one thing to say,
*  okay, well, if this super simple thing can do it as well as an advanced thing, then it seems like
*  it actually is there like in a pretty detectable, meaningful way. Because if not, if it was, if all
*  the learning was happening in the auxiliary model, then like the more powerful we make the auxiliary
*  model, we would see more learning and we're not. So we think, you know, that's one reason to believe
*  that the representation really is there. Another way that they look at it, and I'd say this one is
*  even more compelling, is holdout studies. They have these multiple scales of stuff, right? So you've
*  got countries and their locations and, you know, cities in US states and then places in New York.
*  So you could say, okay, well, let's say I train on countries and, you know, things in New York,
*  and I don't do the cities. Then will the probe also be able to work for the cities?
*  If there is a representation of the Latin long that you are actually picking up on in the main
*  model, then it should work, right? Because there'd be there's enough, you know, kind of,
*  you've got stuff on the high end of scale and the low end of scale. Hopefully it will kind of,
*  you know, still work in the medium middle of scale. If it's not really there and you're fooling
*  yourself, then presumably that would fail, right? If you had just learned some sort of like
*  representation of the names and had kind of, and all the knowledge of the actual Latin longs were
*  held in the auxiliary model, then if you didn't train on a certain data set, like it presumably
*  would not work. So they show that it does work with the holdouts. As you'd expect, you get somewhat
*  less performance, but it's like, you know, degraded performance relative to the full training,
*  still way better than random. And, you know, so that's another reason you could think, okay,
*  yeah, that seems pretty compelling that there's some real representation there that is, in fact,
*  being picked up on. And then the final one that they use that I think is very suggestive and
*  interesting, although it's kind of anecdotal, I guess, is they look for individual neurons
*  that have high similarity to the weights of the learned probe. So they create this learned,
*  you know, the simple linear projection that's like, okay, here's all the activations. I'm gonna
*  have one layer that projects those onto lat and long outputs. And that's simple enough that that
*  one layer, you could say, well, okay, all those activations, here's how the probe has learned to
*  map them onto lat and long. Do we see anything in the network that looks like that same projection
*  is happening? If so, then that's a pretty good place to look for like, hey, maybe this is the
*  latitude neuron, perhaps, or this is the longitude neuron if it's getting fed the same information
*  that the probe is feeding to its outputs. And so again, they do find that, hey, yes, there are some
*  neurons that really do seem to line up in that way. And they show a handful with kind of their
*  activations across a range of things. And it's like, yeah, that certainly looks like a latitude
*  neuron based on just kind of how you systematically vary the, and they're still just
*  doing place names as inputs, right? So you're varying these place names and you can see the,
*  you know, the actual latitude, and then you're able to kind of look at the activation. And it's like,
*  yeah, there's a pretty high correlation here when the thing is fed a place name, what the actual
*  latitude is, is pretty well predicted by what this single neuron is doing. And we found that neuron
*  by looking for a pattern that represented or that was not represented, but that looked a lot like
*  this learned thing that we built to extract. So from all these different angles, you kind of say,
*  okay, I'm pretty much buying now that there is a meaningful representation of lat and long,
*  and also, you know, time, timeline, you know, time from in history type of stuff that
*  is kind of loaded into the middle layers, just based on its association with these simple text
*  inputs, like place names or historical figures. Do you know if in that third method you mentioned,
*  are they doing more than just looking at the highest coefficients in their linear probe?
*  Like, are they doing something different to find the neurons that are associated with different
*  concepts other than looking at the linear probe and just, oh, these are the few neurons that
*  have the highest coefficients for the probe? I think that is the thing. So I think there,
*  you know, the 70 billion parameters in Lama2 makes it such that, you know, it's not super easy to
*  just sweep through everything. So they have to be somewhat, you know, strategic in terms of how
*  they look for the neuron. So what I understand they're doing is saying, okay, we created this
*  little probe. It takes in a layer of activations as inputs, and it basically maps them to two
*  neuron outputs. In this case, it's the lat and long external neurons. So once that learning is done,
*  now we can look and say, okay, well, how does each of those activations actually feed the lat and
*  the long respectively? And that basically constitutes an array, you know, a single array,
*  one dimensional array, a linear projection, just a one dimensional array. So now I can look and say,
*  okay, are there any neurons in the next layer that have input weights from all those activations
*  that look like the same kind of projection, like the same pattern of information from this,
*  you know, messy, not super interpretable activations that is in fact kicking out the lat and long
*  externally? Is there any neuron that seems to be getting that same information as input? And if so,
*  then let's study how it's firing. And maybe it also is kind of firing as like the lat or the long
*  neuron. And so then, yeah, when you get into the paper, you know, it's noisy, but you definitely
*  see some stuff, you know, in the graphs, where you're like, well, it's noisy. Again, you know,
*  LA is east of Reno. So my own, you know, mental map is definitely noisy. This like definitely looks
*  like about as noisy as you'd expect, you know, from something that's like kind of a big data,
*  you know, not really built for this purpose, but just kind of an associative type of thing.
*  I think, you know, I'm very reluctant always to make these like analogies between AI cognition
*  and human cognition. But this does feel similar to me to like the level, at least on the level
*  of precision that I have, you know, you say Florida, I'm like, okay, I know where that is,
*  that's pretty much directly south of me by, you know, 1000 ish miles. And it seems like it's kind
*  of got that level of like associative kind of relational stuff that it's able to call in.
*  Okay. In all cases, we include an empty prompt containing nothing other than the entity tokens,
*  that is the place name. We then include a prompt which asks the model to recall the relevant fact,
*  what is the latitude and longitude? They seem to be, you know, robust to the different prompting
*  techniques. So it seems like it is always loaded in to a significant degree, just based on kind of
*  the conceptual processing and the associations that come with that.
*  Got it. One other quick thing that seems like it'd be interesting might be trying to learn a
*  different probe for like the early layers or for different layers to see if the probe is
*  ineffective at the input layer and the early layers and to see it get more effective as
*  you get to the more abstract middle layers. When you look at the graph or the graphic,
*  and, you know, in the early layers, it's like, everything's kind of scattered, and then they
*  gradually cohere, you know, as you go layer by layer, I believe that each of those frames
*  in the animation definitely represents a different layer. And I believe it also would represent a
*  different probe that's like the best we could do at that layer, as opposed to like the single probe
*  that would be, you know, representing everything. Because I don't know how you would choose it.
*  Otherwise, it would seem to be kind of unfair to the earlier layers if you were, you know,
*  applying something that was optimized for layer 50, specifically, you know, to layer,
*  to early layers. So I think that they are doing one probe per layer and showing the best
*  that they can do as they progress through the layers. And these things are one of the
*  nice things about these, you know, just simple in your projection and things is they're really
*  quite easy to train, you know, the amount of you probably spend more on the inference than you
*  would on the training, just because, you know, you only have the activation states making one map,
*  you know, onto the two, you know, Latin long output neurons. So that's just not that many
*  parameters, like the number of parameters is two times the number of activations, again, assuming I
*  understand. I invite any authors of this paper and all these papers to correct me on any of the
*  fine points if I'm getting anything wrong. But I believe the number of parameters that they are
*  optimizing here with a simple linear probe is two times the number of activations that they're
*  looking at at a particular layer, which is not that many. So you could definitely, you know,
*  it's definitely within the compute budget to train a bunch of those.
*  No, sorry. That makes sense. I forgot. I forgot you had said they had a map of it,
*  which seems very cool. The animation of the place is slowly kind of locking into place.
*  Yeah, it's cool. TechMark's group has done a great job with these,
*  like literally 10 second visualizations. We were like, wow, that makes an incredible point,
*  incredibly efficiently. And then people like me still spend, you know, all the time to read
*  the papers. But if you're just looking for highlights, they certainly have some really good ones.
*  All right. Next, this one is called Deep Neural Networks Tend to Extrapolate Predictably.
*  It's academic work out of UC Berkeley and Carnegie Mellon. And basically what they look at here is
*  when a model is presented with something that it has never seen before, you know,
*  that is out of distribution, not represented in the training set, isn't the way to say that,
*  then what does it do? And basically what they find is like not surprising in retrospect,
*  what they find is that it will kind of default to whatever baseline prediction
*  gives it the lowest loss in a state of total ignorance. And they explore this in a number
*  of different dimensions. They vary architectures, they vary the loss functions, and they vary the
*  way that they are creating distributional shift in the data to create data that is out of distribution.
*  But a real simple one that's kind of intuitive is your classic, you know, handwritten digits test.
*  And in that case, the model's job is to predict which of the 10 numbers is this, right? So it can
*  predict anything from zero to nine. If you give it, you know, a blank thing, or if you just imagine
*  like you're at the start of training, right, and it doesn't know anything yet, then like the way to
*  minimize the loss would be just give an equal weight to everything. So, okay, you know, that's
*  the best we can do until we start to get some feedback and start to learn what's what. So what
*  they show in the paper is a, I believe it was a six, and then they start to just rotate the six
*  and gradually rotate it, rotate it a little more, rotate a little more, more, more, more,
*  you know, a little bit of a rotation of the six. When you, the first six, you got a trained model,
*  it's very confident it's going to predict a six. The slightly rotated one, you know, it starts to
*  get a little less confident, but like it's, you know, whatever, there's a lot of noise in the world,
*  it's still seen sixes that look like that. It still, you know, basically gives most of the weight
*  to the six. And then as it gets weirder and weirder to the point where it's like a sideways six that,
*  you know, presumably was not in the data set, you just have like a little blip at the six.
*  It's still like, you know, got a little sense that it's a six, but it's kind of
*  prop, you know, appropriately started to be like, just going just reverting back to its baseline,
*  total ignorant, you know, whatever I can do to minimize the loss if I know nothing.
*  And, you know, if that's the uniform distribution, then it just kind of pretty quickly, you know,
*  as you rotate your six, starts to go from a sharp prediction of a six to a uniform distribution.
*  And so they show this across like all these different experimental conditions, architectures,
*  loss functions, and distributional shifts, and basically kind of see the same thing
*  across all these different scenarios. And I thought this was quite interesting because
*  first of all, for the sake of control, you know, if you're like, okay, can we use this in some
*  meaningful way, then, yeah, I mean, what they kind of argue is that you should take this into account
*  as a system designer and try to set things up in such a way where your loss function
*  is inherently kind of conservative when in fact the model is not.
*  When in fact the model is out of distribution. So, you know, there's a lot of possible loss
*  functions out there, right? But if you want to not have your model do crazy stuff, then choosing a
*  loss function where it kind of inherently gives a very low confidence guess when in fact it doesn't
*  know is a pretty good approach to take because you could, you know, for one thing, you could
*  detect that, right? Even if you're, when you're using OpenAI these days, they don't give you the
*  actual numeric predictions on the tokens. You just get the tokens. Used to be you could actually get
*  the numerical predictions and it was like, yeah, it was this percent on this or this percent on this
*  or, you know, one layer lower than that is the logits, but you could get those numerical things.
*  And if you're open source, then you have full access to that information. You can see all those
*  numbers. Of course, OpenAI can see it on their end as well. So this starts to give you the ability to
*  say, and you might have some heuristics here. It's like, you know, it's not necessarily super clean
*  because it's inherently kind of a noisy thing. You could set the bar at different places and have,
*  you know, false positives, false negatives, depending on the trade-offs that, you know, you're
*  prepared to accept. This does show a path from instead of like, well, hey, I've got this black
*  box. It's going to spit out, you know, one in 10 numbers. I don't really know how to, I take the
*  most likely one. I don't really know how to interpret that. Now there is like a pretty good
*  theoretical basis for saying, hey, if the output is looking a lot like the baseline total ignorance
*  output, then that may mean that we are really out of distribution. And that is like a case where
*  we maybe don't want to trust the model. So you could really start to flag these kinds of things
*  and say, you know, super low confidence on this, which, you know, you could sort of always do
*  because, you know, they were always giving these numbers. You could always just kind of eyeball them.
*  But I think what this research shows in a nice way is that this pattern of, as you get out of
*  distribution, you fall back to whatever the baseline total ignorance prediction would be,
*  which is defined by the loss function and how it, you know, rewards different distributions in that
*  scenario. And so you can recognize that you can start to monitor for that. You can control that.
*  You can alert users to that kind of stuff. And you can also design for it so that, you know,
*  you don't have loss functions that reward like random guessing, right? Because you can imagine
*  a loss function that might be like, if you're right, you know, then you get like high reward.
*  And if you're wrong, you could easily reward overconfidence and your loss function. And if you do
*  that, then you're going to get a model that exhibits overconfidence when it's out of distribution.
*  On the other hand, you could reward a conservative guess with your loss function.
*  And if you do that, then you'll get conservative behavior when you're out of distribution.
*  So it's probably most important from a system design standpoint, but also, I think, from kind
*  of a monitoring, you know, alert to users, hey, we're not really that sure here. This looks like
*  the model hasn't seen anything like this before. That's a really good thing to know. And even just
*  for efficiency sake, too, right? I mean, if you're actually trying to do some sort of classification
*  problem in the wild, you know, in industry, let's say, then you have problems of like, well,
*  when the classification is wrong, how do I detect that? What happens? You know, it'd be way better
*  if you could detect, I have low confidence in this in a way that means the model's probably never seen
*  anything like it. I should, you know, that's maybe more data I need to go label, you know,
*  if nothing else, right? So I thought this was a pretty cool paper. It wasn't one of these things
*  that I never expected that, but more of something I hadn't quite thought about it as a good systematic
*  evaluation or exploration of it, looking at these different dimensions. And it seems like it gives
*  good guidance for both the way people train and the way people deploy. It is both energizing and
*  enlightening to hear why people listen and learn what they value about the show. So please don't
*  hesitate to reach out via email at tcr at turpentine.co or you can DM me on the social media
*  platform of your choice. Omniki uses generative AI to enable you to launch hundreds of thousands
*  of ad iterations that actually work customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it, and I recommend you use it to use Cogrev to
*  get a 10% discount.

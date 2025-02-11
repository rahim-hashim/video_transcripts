---
Date Generated: July 04, 2024
Transcription Model: whisper medium 20231117
Length: 6136s
Video Keywords: []
Video Views: 144
Video Rating: None
Video Description: Nathan hosts Albert Gu, assistant professor at CMU and co-founder of Cartesia AI, to discuss the groundbreaking Mamba architecture. In this episode of The Cognitive Revolution, we explore the state space model revolution, diving into the technical details of Mamba and Mamba 2. Join us for an insightful conversation on the future of AI architectures and their potential to transform the field.

Apply to join over 400 founders and execs in the Turpentine Network: https://hmplogxqz0y.typeform.com/to/JCkphVqj

RECOMMENDED PODCAST:
Byrne Hobart, the writer of The Diff, is revered in Silicon Valley. You can get an hour with him each week. See for yourself how his thinking can upgrade yours.
Spotify: https://open.spotify.com/show/6rANlV54GCARLgMOtpkzKt
Apple: https://podcasts.apple.com/us/podcast/the-riff-with-byrne-hobart-and-erik-torenberg/id1716646486

SPONSORS:
Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

CHAPTERS:
(00:00:00) About the Show
(00:05:39) State Space Models
(00:13:05) Intuition and inspiration
(00:18:27) Surprises
(00:22:33) Sponsors: Oracle | Brave
(00:24:41) Biological inspiration
(00:25:19) MAMBA breakthrough
(00:30:59) How does the state work?
(00:36:44) What is the size of the state?
(00:39:05) Training vs. Inference (Part 1)
(00:42:04) Sponsors: Omneky | Squad
(00:43:51) Training vs. Inference (Part 2)
(00:43:51) Sequence Models
(00:49:20) Mamba inference
(00:57:53) Mamba2 vs Mamba1
(01:16:05) Overtraining and the future of SSMs
(01:17:44) Training efficiency vs inference efficiency
(01:20:52) Hybrid models
(01:25:04) Scaling Attention Layers
(01:30:23) Optimizing State
(01:34:09) The extrapolation abilities of the SSMs
(01:36:37) Sequence parallelism with Mamba 2
(01:39:20) Why are you publishing all this?
(01:40:46) Cartesia and Together
(01:41:54) Outro
---

# The State Space Model Revolution, with Albert Gu
**Cognitive Revolution:** [July 04, 2024](https://www.youtube.com/watch?v=1zjMalKLHiA)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution. Today I am thrilled to share
*  my conversation with Albert Gu, assistant professor at CMU,
*  co-founder of Cartesia AI, and leader of the state space model revolution.
*  I'm always looking for something that could fundamentally change the AI landscape,
*  and with that mindset I was one of the very first to recognize the importance of the selective
*  state space mechanism that Albert and his co-author Tree Dow introduced in their now famous Mamba paper
*  last December. While a number of other projects had already delivered subquadratic scaling
*  properties at the time, Mamba was the first architecture to also outperform transformers
*  on key metrics. This result inspired my obsession with state space model research,
*  which has so far produced my original Mamba emergency pod, a shockingly popular two-hour
*  monologue in which I declared the end of the transformer's era and the beginning of the new
*  mixture of architecture's era, and also a two-part Mamba Palooza episode back in March,
*  which I created with Jason Moe, who chronicles state space model developments online at statespace.info,
*  and who joins us again today. Both of those episodes are good background for today's
*  conversation, and with that context you'll understand why it was such an honor to get Albert
*  on the show. We began with a discussion of where his ideas come from in terms of intellectual
*  history, practical motivation, theoretical inspiration, and ultimately a sort of black box
*  design intuition. After that, we go deep into the technical details of Mamba and the more recently
*  published Mamba 2, which very notably and a bit surprisingly from my perspective achieves better
*  results with a simpler and somewhat less expressive core mechanism, which happens to allow for more
*  efficient training on modern hardware. As you'll hear in that part of the conversation about all
*  these various trade-offs, I finally cleared up one lingering but important misconception that I had
*  about the Mamba architecture. I thought that it was GPU SRAM size that limited the size of the
*  all-important internal state, when in fact it was the speed of computation of the original
*  selective statespace mechanism that was the actual practical constraint. This is a minor point,
*  but if you hope to have frontier understanding, let alone insight, it is super critical to
*  understand which resource constraint is the overall system bottleneck at any given point in time,
*  and so I'm very glad to have cleared that up. From there, we move on to briefly discuss the
*  explosion of Mamba-inspired literature. Jason reports that there are now 267 papers and projects
*  downstream of Mamba, and they've introduced a number of interesting innovations, including
*  multiple approaches to scanning images and other non-sequential data, and also the use of multiple
*  internal states. From there, we explore a couple of future directions for this research, including
*  the opportunity to train models on super long context data sets, which Jason has been pushing
*  forward independently in the background, and also the possibility of moving toward more expressive,
*  but presumably also more expensive-to-train mechanisms. We even get to my favorite idea
*  to speculate about, the potential to design multi-state systems where each state plays a
*  specific role. Albert said that he is interested in pursuing this direction, as he thinks it could
*  perhaps deliver both superior performance and easier interpretability. We went over 90 minutes
*  in this recording and only briefly touched on the commercial applications of Albert's work at
*  Cartesia at the very end. If you want to hear more about that, I can also recommend his recent
*  appearance on the NoPriors podcast, which covers almost entirely different ground than we cover
*  here today. Finally, a brief reflection. For listeners who are relatively new to AI and still
*  building taste and intuition, I hope this episode is encouraging. Just three years ago, I had a
*  casual interest in AI, but really very little technical depth and no expectation that I could
*  contribute to the broader conversation. Today, I'm proud to look back on my response to Mamba
*  and feel like I got the big things really right, and also to reflect on this conversation and note
*  that Albert agreed with some of my current intuitions on the path forward. Of course,
*  there are levels to the game, and I don't expect to make contributions as fundamental as Albert has,
*  but still I found it reassuring that even a bona fide genius like Albert has at times stumbled
*  onto some key discoveries, gradually figured out how his own creations work, and even today
*  has as many questions as answers. I find this to be true in general. A lot of AI work is less
*  principled than it may initially appear, and in many cases, multiple different approaches turn out
*  to work similarly well. So if you're still finding your footing in the AI space, I hope that the
*  cognitive revolution helps you build intuition and ultimately confidence that you can contribute
*  in a meaningful way. After all, if there's one thing I know for sure, it's that where we're going,
*  we will need as many curious human minds as we can possibly get. If indeed you are finding value
*  in the show, I would appreciate it if you take a moment to share it with friends. Of course,
*  we welcome your feedback on our website, cognitiverevolution.ai, where you will now
*  find a link in the header to a Google form where I'm accepting resumes for circulation with friendly
*  companies. And as always, you're welcome to DM me on the social network of your choice.
*  I have been traveling over the last week and I still owe a number of people responses,
*  but I am moving things forward behind the scenes. Now, I hope you enjoy this deep dive into the mind
*  and the core mechanisms driving the state space model revolution with the one and only Albert Gu.
*  Albert Gu, assistant professor at CMU, co-founder of Cartesia AI and leader of the state space
*  model revolution. Welcome to the cognitive revolution. Thanks for having me, Nathan.
*  I'm really excited for this conversation and excited also to welcome back Jason Moe to the
*  show who regular listeners will remember from our Mamba Palooza literature review episode in which
*  we covered the first 90 days of downstream Mamba literature. He probably narrowly beats me out as
*  your number one fan, given how deep he's gone into understanding all the Mamba literature and even
*  training some of his own long context Mamba models. So we've got two big fans of your work here and
*  excited to get into the very nitty gritty details of it over the next 90 minutes or so.
*  For starters, do you want to give us just a brief intellectual history of the state space
*  model revolution? I think like many apparent overnight successes, yours was several years
*  in the making. I think certainly regular listeners to this show know about Mamba, but I think the
*  broader community at this point knows about it, but they may not know as much about the several
*  years worth of work that you built up before getting to that breakthrough moment.
*  Absolutely. This is something that I could probably go on for a while, but I'll try to give a
*  somewhat abridged summary, but maybe also with a little bit more context that a lot of people
*  don't know about. The brief summary is actually Mamba and the state space models are very closely
*  related to RNNs or recurrent neural networks as most people probably know. These models were
*  things that I started working on a couple of years ago. I actually had an internship with
*  my mentor, Chalagmachary, at the time who's now at EPFL in Switzerland. Shout out to him. He was
*  a fantastic mentor and an expert in RNNs. I got interested in them actually right before the
*  fifth year of my PhD. That was the first time I got introduced in sequence models. The core idea
*  here is really just the idea of stateful recurrence. When I first saw it, it just felt very powerful,
*  and it felt like a fundamental computational paradigm, especially for modeling sequences.
*  That's actually what people thought of before transformers. It was just the common knowledge
*  that this is just obviously the right thing to do for sequences. It's funny that the pendulum
*  swung completely the other way. Nowadays, young researchers coming up, some of them barely even
*  know how these recurrent models work. People think, oh, attention is obviously the right thing to do
*  for sequences. It's just funny how things are dominated by what's popular. Really, they both
*  have a lot of merits and stuff. At the time, I was just super interested from an intellectual
*  standpoint. Just felt like there was something really important there. I basically was working
*  on recurrent models for several years, starting from them. The first paper was maybe a little
*  clumsy, but then stumbled on some of the more mathematical ideas in line of work.
*  There is this paper called Hippo, which I did together with Tridau in 2020. That leveraged some
*  of the older theoretical work that we had done on orthogonal polynomials and function approximation
*  and stuff. At the time, I also had no idea what a state-space model was. It turns out that that is
*  a type of state-space model, but it was derived from a completely different perspective. A lot
*  of it was basically like, how can you have a recurrent finite state that is compressing
*  your history? That's a theme that we'll probably touch on a lot today, but that's core to everything
*  going on in all of these types of models. That idea is the one that I thought was really powerful
*  and felt really intrinsic to modeling sequences, well, or even intelligence.
*  Hippo took a very mathematical approach to it. I later realized that that approach is really only
*  good for certain types of models. Later on, Hippo led to this paper called S4. The full acronym
*  stands for the Structured State-Space Sequence Model, which maybe I'll explain again later.
*  What I think of now is basically, these are called state-space models, but the funny thing is I
*  really still think of them more as RNNs, which was my roots. You can think of them as a different
*  variant of it, or you can even think of RNNs as variants of state-space models. They're related,
*  but of course, they came from a different perspective and some different theoretical
*  grounding, which makes them a little different. The connection was made between these models and
*  the classical state-space models from controls. Nowadays, I think that the gap there is actually
*  bigger than people think. This is a whole other discussion, but the word state-space model is,
*  unfortunately, a little bit overloaded. People frequently get confused, people from other fields
*  think you're talking about something entirely different because they have their different
*  versions of these models. I think they are related, and there is certainly inspiration
*  coming from there. Fundamentally, I think of what we call state-space models in AI and deep learning.
*  The longer form of it is what I call structured state-space models, which are different than the
*  statistical or controlled state-space models from other disciplines. That connection was made
*  through this lens of theoretical stuff from RNNs, and that's what led to a lot of things.
*  Like I just said, these models were around 2020, 2022 is when S4 was published. They were the first
*  time that these were really able to be used for anything. There's a bunch of fundamental
*  computational difficulties to training these models. That's what a lot of the early work that
*  went in was trying to resolve. Also, we later realized that these models do have an inductive
*  bias. I still believe to this day that the types of models we use, there is no real free lunch in
*  terms of, can you really just take one model and use it everywhere? People kind of have that
*  impression for attention, but I don't think that's actually true. We can go into the details a little
*  more later again. These early state-space models, we realized they were mainly good for perceptual
*  modalities like audio, video, things that are closer to raw signals and more continuous in nature.
*  One reason why they kind of existed for a while but didn't catch on is because they weren't really
*  good at language back then. People did try, but I think pretty quickly realized that that wasn't
*  really what they were good for. People have been trying for a while. So that's when I moved more
*  toward this time variant or input dependent type of SSM, which is what Mamba is. Actually, something
*  that people probably don't know is that I was trying to work on this back in the Hippo days.
*  So after we published Hippo, which was this very theoretical paper, I spent several months trying
*  to make some time variant version of it work. And I think some remnants of that are still in our public
*  code base. As you can see, we were using these scans, input dependent discretizations or input
*  dependent parameters way back then. The main issue is that it's really hard to get these things to
*  work computationally. So it was just being intractable to train. And it was only over the
*  course of a very meandering path through all of these other models like S4 and all its follow-ups
*  that we figured out how to simplify the model more and more to the point where we could finally
*  implement that selective idea very efficiently. So that idea was really just a very simple change,
*  which is the idea that you can make some of the parameters of your model depend on the input.
*  In some ways, it's what makes attention work as well. And that idea, to your point, it seems like
*  it came out of, it was like a thing recently. But actually, it's both like we were trying this a long
*  time ago, and it just took a lot of work to get it to work. But also, these ideas are not really new.
*  They're very related to classical RNNs. I think in the Mamba paper, we talk about how it's related
*  to gating mechanisms of LSTMs and these things that people used to use. And it's just like this
*  giant confluence of tons of different factors, like ideas from these older RNNs to these ideas
*  from SSMs to simplifying the model, getting a state expansion, training more stably. All these
*  things just took a lot of time to do everything the right way and put everything together the
*  right way. And then it culminated in these things that you see today, Mamba and Mamba 2.
*  So yeah, there was a lot of history there. Hopefully someday I can write some of it more
*  up. And you would be shocked at how much of it was kind of accidental. A lot of it was
*  very theoretically motivated, but some of it was just like, you throw stuff at the wall and
*  see what sticks. And I believe that being a good experimentalist is very important.
*  Even if you're a theory person in modern AI and deep learning, you just have to be a good
*  experimentalist. That's a very long answer to this question. But that's great. So I guess a couple
*  threads that I'll try to pull out of there and you can correct my summaries if I get anything wrong.
*  It sounds like there's sort of a tick tock process between theory and experiment. It's not really one
*  is a bigger part of your process than the other. It's that you are trying to find the right balance
*  and the right alternating back and forth between them. And that's where you get the best results.
*  Is there anything more you could give people to kind of develop their intuition? Because I think
*  people look at this sort of work and they're like, where do these ideas come from? And I don't know
*  if there's any more habits of mind or any kind of motivations or themes that you could highlight
*  that you think people should pay more attention to. But that I think would be of real interest to a
*  lot of people. Yeah, I think some of this is quite hard to explain because some of it is actually
*  quite intuition driven. That's what underlines both the theory and the empirical research.
*  One thing I kind of mentioned at the beginning is this theme of like, something just really compelled
*  me to the idea that stateful recurrence is fundamental. And I don't know that I can
*  necessarily tell you why. I can tell you a lot of the downstream effects of it. I go around talking
*  about how the idea of compressing context or information into a state somehow feels important
*  because it's like stripping out unnecessary stuff. This is one of the big things. Maybe we'll talk
*  a little bit more specifically about attention versus SMs later, but this is kind of one of the
*  big things. What is the difference between them? One is kind of like trying to remember everything.
*  One is actually trying to do intelligent compression. And that I think years ago when
*  I was working on RNNs, it kind of early occurred to me that this is, is this related to how the
*  brain processes information? It does kind of feel like a very large state, but like a finite state
*  that is doing fuzzy compression. And so a lot of this was just kind of intuition driven early on
*  that I felt like it was elegant and important. And the theory and the math involved in a lot
*  of these models was also just something that compelled me. So there was a bit of like an
*  aesthetic taste to it as well. But then I think like the theory and the experiments to me almost
*  come afterwards. It's like I had like a conviction that something was interesting here and then
*  just kept working on lots of ideas. And sometimes I would go do other stuff and then come back to it.
*  The way research unfolds a lot is like ideas can come from many different sources and
*  trying to solve one problem doggedly doesn't always lead to the best results. And one of the
*  things that I think has driven some of my work is just keeping an eye on other sorts of connections.
*  People look at this and see how I've made some connections like signal processing to various
*  other fields, numerical in your algebra and stuff like that. And that's all kind of intentional for
*  me. It's that I like learning about different things and then I'll have some problems in mind
*  that I care about and eventually connections will come together. But I wouldn't say it's like a super
*  targeted process, but sometimes it's just the way inspiration unfolds. And then a lot of it is also,
*  I have like a mathematical background and so looking for formalisms, looking for things that
*  feel principled is a big component of how I approach problems. Another component is that I
*  think I'm actually a pretty good experimentalist and a lot of things are kind of you generate lots
*  of ideas and then you just try to figure out how to de-risk or try them as fast as possible.
*  Like there's probably a lot of different components of the models that ended up working.
*  I mean obviously I tried them because there was some reason for it, but there would be things where
*  I would even try things I didn't think would work, but were cheap to try because why not?
*  And it turns out they worked really well and then later on it turns out it is actually important.
*  So one example of this is that when I was first doing S4, we had like a bunch of these different
*  HIPPO matrices that we could use and only one of them made sense to me. There was another one that
*  wouldn't have made sense to try in the S4 model. So basically S4, you use these like predetermined
*  initializations and each of these initializations came from the older HIPPO theory and some of them
*  kind of made sense in this model and some of them they were basically a fixed formula for a matrix,
*  but that formula was just kind of like nonsense to use in this space-based model. I tried it anyways
*  and it worked better and then two years later when I was actually preparing for my job talk at CMU,
*  I was trying to figure out how do I actually explain this and was doing a bunch more theory
*  and I finally figured out that actually it was principled all along, I just didn't know the
*  underlying reason why. And so this happens a lot too and in fact I think a lot of modern progress
*  in that is more driven this way where you kind of try things empirically and then later on explain
*  it using theory rather than going from first principles. As a mathematician, I always love
*  actually being able to figure out something from first principles, but you can't always do that.
*  So it really is like a big interplay. I spend my time doing both of these in quite balanced both
*  the theory and the empirical work. At the end of the day, I think a lot of it is also like this will
*  feed back into your intuition and then doing anything big just requires having a lot of
*  conviction and intuition for why something is important even if you can't explain it at the
*  time. My PhD advisor would tell us this like take big bets, figure out what you want to bet on,
*  that's really what underlies it more than the actual process itself necessarily.
*  Cool, that's really interesting. So I can definitely relate first of all to the experience
*  of having something that you thought was like a less good idea actually be the thing that delivers
*  the breakthrough. I told this before so I won't tell it again, but I made one actual discovery
*  contribution to chemistry way back in the day when I was a student studying chemistry and it
*  came from an experiment that seemed to have failed except when we drew the trend line, we were like,
*  what if we extended the trend line in the other direction? Maybe that one looks like it's actually
*  could be working and sure enough in defiance of all of our understanding of the mechanism that we
*  thought we knew it ended up working. So it can definitely relate to that.
*  Did you eventually figure out why it worked? I think there may be just now with all of these
*  models for simulating the way that molecules interact on a very small scale, we might be in
*  a better position to crack that. It was a very poorly understood thing at the time, like a metal
*  catalyzed hydrocarbon oxidation reaction that the transition state was just kind of a very
*  hand wavy understanding that we had. So we shouldn't have been, and maybe I wouldn't say
*  we were too surprised that we got something off model because the model wasn't like a very high
*  confidence model. But it is funny because all these years later, we're now actually starting to get
*  some of the ability to simulate those transition states in ways that at the time were basically
*  impossible for us. Yeah, that makes sense. I feel like I haven't had many things that were like
*  huge surprises out of nowhere because a lot of it is a process that built up over time. I mean,
*  I certainly believed in recurrent models a lot more than other people did because I was working
*  them for a while. And so when things were working, it was a pleasant surprise, but it wasn't like we
*  were shocked by it. It was like, well, things are doing what we finally thought they should do all
*  along. The things that kind of come out of surprise are often more on a micro level. For example,
*  the example I gave with this one different matrix works really well and we didn't quite know why.
*  And yeah, usually you can figure out how to explain these things afterwards.
*  I think the theme of taking inspiration from biological systems is also a pretty powerful
*  one that I see come up in various different contexts here. It seems like,
*  I don't know to what degree this was exactly motivating you, but you can certainly just
*  introspect to a degree and say, well, geez, my memory is certainly not like all tokens related
*  to all other tokens, right? There's clearly some sort of compression going on, some sort of like
*  abstracting away of details. And so on that basis alone, it feels like something like this
*  needs to work, right? Like we don't get to expand our memory with every new input as we go through
*  life. So it's like in principle, there's got to be some architecture that would be able to do
*  a similar thing. Yeah, I think the question of biological inspiration is pretty interesting.
*  Both sides of the debate makes sense. Like some people think that we shouldn't be constrained by
*  biological mechanics and so on. Of course, we can design things however we want, and we can
*  design things better than evolution, which is kind of a very stupid algorithm. And I think that's
*  true as well. But at the same time, whenever there are clear things that biological agents do better,
*  then that becomes a clear source of like, well, why aren't we trying to learn from it or taking
*  some inspiration for it? Or clearly there's maybe something there that we can incorporate or could
*  help us in some way. So yeah, this is like the analogy to the brain is something that we kind of
*  liked pretty early on. Now I have to add a disclaimer that I barely know any neuroscience.
*  So this is like the loosest of intuitions probably, but maybe sometimes that's what's
*  useful. I think like, actually, I guess another just a little Easter egg. The Hippo paper,
*  which was kind of our first one that I would say was really in the SSM line of work. The title
*  Hippo, actually, if you look at the paper, it makes sense in the context of the method. It stands for,
*  I think, high order polynomial projection operators. But actually that was a backronym from
*  she wanted to call it Hippo, which is short for the Hippo campus, which is the part of the brain
*  that does the memory. So there's a fun little story there. And we kind of have a picture in
*  the paper with a little brain and the Hippo campus is highlighted. So it was definitely like back,
*  back from the very beginning, we were kind of thinking of this analogy, whether or not,
*  you know, it's actually accurate or not, but it made sense to us. Hey, we'll continue our
*  interview in a moment after a word from our sponsors. AI might be the most important new
*  computer technology ever. It's storming every industry and literally billions of dollars are
*  being invested. So buckle up. The problem is that AI needs a lot of speed and processing power. So
*  how do you compete without costs spiraling out of control? It's time to upgrade to the next
*  generation of the cloud, Oracle Cloud Infrastructure, or OCI. OCI is a single platform for your
*  infrastructure, database, application development, and AI needs. OCI has four to eight times the
*  bandwidth of other clouds, offers one consistent price instead of variable regional pricing.
*  And of course, nobody does data better than Oracle. So now you can train your AI models
*  at twice the speed and less than half the cost of other clouds. If you want to do more and spend
*  less like Uber, eight by eight and Databricks Mosaic, take a free test drive of OCI at oracle.com
*  slash cognitive. That's oracle.com slash cognitive, oracle.com slash cognitive.
*  The Brave Search API brings affordable developer access to the Brave Search index,
*  an independent index of the web with over 20 billion web pages. So what makes the Brave
*  Search index stand out? One, it's entirely independent and built from scratch. That means
*  no big tech biases or extortionate prices. Two, it's built on real page visits from actual humans,
*  collected anonymously, of course, which filters out tons of junk data. And three, the index is
*  refreshed with tens of millions of pages daily. So it always has accurate up to date information.
*  The Brave Search API can be used to assemble a data set to train your AI models and help with
*  retrieval augmentation at the time of inference, all while remaining affordable with developer
*  first pricing. Integrating the Brave Search API into your workflow translates to more ethical data
*  sourcing and more human representative data sets. Try the Brave Search API for free for up to 2000
*  queries per month at brave.com slash API. Yeah, it's funny you say that because I have another
*  episode in the works with the author of a rag system called Hippo rag, which is also Hippo campus
*  inspired, working at a different level. But, you know, again, taking inspiration from the fact that
*  we have this sort of associative memory that is very easy to add to and like integration happens
*  pretty naturally. And sort of saying like, how can we create a system that doesn't necessarily mimic
*  that in certainly not in like a, you know, a detailed way, but at least can sort of try to
*  achieve some similar functionality. So yeah, the inspiration of the hippocampus keeps giving even
*  if at a high level. Okay, let's talk about the Mamba breakthrough. And then we'll get to the
*  Mamba to breakthrough. The way I think about the Mamba one breakthrough is that you figured out a
*  way to move from a system where regardless of input, the same computation would happen on that
*  input every time to this sort of forking mechanism, where there now becomes like two routes for the
*  input to get processed and they can sort of interact with each other. And that creates just
*  like a fundamentally higher degree of freedom system. I'm not super mathy and I'm not super
*  formal in that understanding. Can you help me like develop my intuition any better than that without
*  having to resort to notation? Yeah, so that really is the main intuition. So kind of the way that we
*  were thinking about it is that these models are like recurrent models, you have a fixed state,
*  and then you're kind of processing it with some sort of mechanism to create the next state. And
*  the idea is like, if you're using this analogy to these like these stateful models, all they have is
*  the state, what's most important for them is to be able to utilize that state as effectively as
*  possible and entails both how do you like put information into the state and how do you take
*  information out of the state. So kind of focusing on that expressive, the expressiveness of that
*  mechanism was something that was kind of clearly very important. And then there are actually
*  probably many ways to achieve that. So you could use like, you can design a recurrent mechanism
*  that updates your state as complicated as you want. And probably there's actually a pretty big
*  design space of things that will work pretty well, is my guess. Turns out that probably kind of like
*  going from the first order to second order is, I would guess gives you pretty much all of the lift
*  or like a large chunk of all you need. And so basically, as you were saying, one way to think
*  about this is that the original models of these were linear in the sense that you apply the same
*  linear transform to your state every time. And you can think of this linear transform really as
*  simply as something that's just like, we're going to take my entire state vector and multiply it by
*  a constant to kind of like reduce the magnitude of everything in it. So this is kind of like how
*  older LSTMs worked in a sense, you had this gate that kind of like reduces the magnitude of how
*  much you're like, you literally just downscale the entire state down by a constant, right? And so
*  you're kind of reducing that what's stored in there and then incorporating new information from
*  the input. And that's really all you need for these recurrent models, at least right now, like
*  nothing is significantly more complicated than that. And then the one observation is that if
*  you're always downweighting your state by the same amount every time, it just intuitively doesn't
*  feel right when you're dealing with discrete information dense data. And so the example that
*  I don't remember if I actually wrote this example in the original Mamba paper, I think I wrote this
*  in the Mamba2 blog post, but this was intuition we had for a long time ago, which is like,
*  if you have a sequence of tokens, there will often be filler tokens or irrelevant tokens in it.
*  For example, in language, you can have filler words, right? So if you actually took a transcript
*  of some speech, like an actual transcript, there's going to be plenty of ums and whatever in there.
*  And that just is really completely like useless. So the fact that it is taking up a time step is
*  really kind of arbitrary. And the idea that we wanted was to be able to skip over time steps if
*  necessary. Or if there is a new input that's super important, how do you kind of focus only on that
*  new input and put that input into your state and ignore everything else? So that is exactly what
*  led to this selection mechanism. Or you can think of it kind of either way. You can think of this as
*  like, that's your desert errata. And then how do you design a mechanism to accomplish that? And
*  probably the simplest thing that works is basically the selection mechanism of these SSMs,
*  which is very similar to the gating mechanism of RNNs, which is basically just saying that
*  whatever parameter you're using to up weight or down weight your state versus your input,
*  just make that parameter itself a function of the input. So now your model can just
*  look at the next token as an, I'm going to decide to keep my memory and ignore the input. And that
*  weight will be controlled by looking at the input itself. So that's really it. I think at high level
*  is pretty simple. Of course, like a lot of details are needed to implement this and get it to kind of
*  work well and efficient. So I guess that's kind of what the whole paper is about. Like actually
*  some details are kind of carried forward from the older SSM work. So that was one reason why
*  it was developed in this roundabout way because there's a, yeah. So for example, like why I said,
*  this is very similar to like an LSTM, right? So why didn't LSTMs work? Why does this work?
*  That's where all of the history through the SSMs really helped. We realized a lot of other things,
*  for example, that like linear models are actually all you really need for these recurrent things.
*  You need like a little bit of nonlinearity, which is basically encapsulated by the selection
*  mechanism. But other than that, this was quite counter-intuitive to a lot of people because
*  I believe basically that one of the reasons why these older RNNs didn't work is because they were
*  nonlinear. People made them nonlinear because they thought that would make them better, but I actually
*  think that makes them worse because of other optimization reasons or it kind of limits how
*  much you can control how your information is propagating through the state, right? So like
*  the nonlinearity is going to squash the state in unexpected ways and you don't really know what's
*  happening. And so removing all of those, linearizing them actually gave us a lot more control over
*  things. And then there was a bunch of that theory to figure out how do you actually initialize and
*  define these models and parameterize them, which all became a lot easier once we like simplified
*  and stripped out the unnecessary stuff. And then I kind of mentioned as well that for a while,
*  we were trying to get the selection mechanism to work, but there was just so many like computational
*  issues. And so after like simplifying a bunch of other things and understanding these models pretty
*  deeply, we were finally able to reincorporate to the so-called selection or gating and get it to
*  work. But like that idea is really simple. This idea of that your dynamics of your recurrent or
*  dynamical system should be dependent on the input itself to get more control. That's really it.
*  Gotcha. So one thing that I've never quite been able to understand clearly, even with a look into
*  the code is what exactly is the state? Is there one state? Because like the Mamba architecture
*  has the layers in the same way that like a transformer has layers, right? Yeah. And at
*  each layer, there's this sort of token wise new information projection into the state
*  computation and then passing on to the next layer. Is it one state that serves all of those layers
*  or does like each layer have its own state? Yeah. So the way I think about it is that these
*  modern deep neural networks, they're composed, like you said, of a bunch of layers where each
*  layer is what I call a sequence model, which is basically the way I define sequence models
*  often in my talks is that it's just a mapping from like an input sequence to an output sequence
*  that kind of like incorporates some mixing along the sequence dimension.
*  So attention RNNs, CNNs, these are all examples of sequence models that satisfy this interface.
*  And now given one of these simple maps, they are composed into deep neural networks by taking like
*  one of these layers, and then you add like a layer norm, you add a residual connection,
*  and then you just like stack these blocks a bunch of times, right? But each of those blocks,
*  like the thing inside the block is what I think of as the core unit that's processing your input.
*  And so they, for the most part, behave pretty much independently. So to answer your question,
*  basically, yeah, I think like each of these layers is basically an independent sequence to sequence.
*  And because they're completely independent to each other, they all have their own state basically.
*  And so when like creating these models and reasoning about them, it's usually helpful to think of them
*  at a finer grained level, where we are thinking of the core SSM layer. So for example, when we
*  talk about Mamba, there's a bit of a conflation between the whole architecture versus the core
*  SSM. In the paper, we called the inner SSM the S6 layer. I don't know if I really like the name,
*  but there was nothing else we could figure out what to call it. And that thing is a very
*  self-contained sequence of sequence mapping. And then you kind of wrap that around in this fancy
*  neural network architecture. But actually all of that other stuff, to me, is not the most important
*  part. And then it's that inner SSM layer that has a state. And that is the thing that is mixing
*  across the sequence. Yeah. Another way you can put it is that, for example, these layer norms,
*  these MLPs, these residual connections, all of them are operating independently per time step.
*  So like every single time step you have a token, that token gets processed by this MLP and norms
*  and whatever. And so all of those things are not really like the sequence model part of the model.
*  It's not doing any information mixing across the sequence dimension. And so those things have no
*  concept of a state. So you have to drill in deeper to the core thing that is doing any sort of
*  mixing across the sequence that has a state. And another kind of interesting concept is that we
*  can really think of any model as having a state. So state-based models obviously have a state,
*  that's what they're named for. But in some sense, any autoregressive sequence model has a state.
*  And so what we mean by that is that if you think of like a GPT model, it's this transformer,
*  that part is actually like pretty much any model that is trained autoregressively or have a state.
*  But the autoregressive part means that you're producing an output token and then kind of feeding
*  it back into the model and then using that new word to produce a new word. And then you keep
*  feeding in this loop. And now the concept of a state is just, what does the model need to store
*  in memory in between one token to the next token? That's like a pretty precise definition. And it
*  really encapsulates the nature of these different types of models. For SSMs, you would basically
*  drill into the model, you kind of ignore all these MLPs and other linear projections and stuff,
*  and just look at the core SSM part of it. And that SSM is going to have like one fixed size or current
*  state where every time you take one more step and process the next token, the state will undergo an
*  update. And so it's the thing that the model needs to remember to process the next token,
*  or you can think of it as what the state is the thing that the model is storing internally that
*  summarizes everything the model has seen so far. So this is the core concept that really led to
*  Hippo and all these other things. It's all about how do you define something that compresses the
*  history? But of course, you don't need the state to be fixed size for it to be considered a state.
*  So the way I think of it, I would define a transformer to also be a stateful model,
*  where the state is the KV cache, basically, if you're familiar with those concepts. So basically,
*  attention looks at your new thing, and it compares it to every single token in the past.
*  You usually have this diagram where you look at the connections and you're literally comparing it
*  pairwise. In the past, you compare it pairwise. In the inference mode, you compare it to every
*  single previous token. And so the state is what the model, what did the model need to remember?
*  The model needed to just cache every single previous token or some representation of it.
*  And that is literally what the KV cache is. And so for a transformer, that's what I consider its
*  state. And so now you can kind of reason about the trade-offs of these models through the lens of
*  what is being stored in the state. So the highest level description of the trade-off between these
*  things is that the SSM has a fixed size state that has been designed to try to intelligently
*  compress history into a form that is easy for the model to extract new information from. And again,
*  I think that there's lots of fundamental reasons why this is a good idea, but this can't do
*  everything. Just like human memory is very imperfect, imprecise, which is probably why
*  it's also powerful because you can remember fuzzy representations of lots of things, but it's harder
*  to be more precise. No one can memorize a dictionary and well, people can, but most people can't,
*  because it's being compressed into this fuzzy representation. And so it's augmented by having
*  like an entirely different state, one that is literally just like kind of storing everything
*  that it's seen so far. And so the model can like literally look back and look at every single past
*  thing it's seen and do what it wants with that. So that's kind of where the differences, the high
*  level difference between the SSM and the transformer come in is in this concept of state. And they work
*  the same way. It's like every attention layer has its own state. Every SSM layer has its own state,
*  for the most part. Now, more recently, people have played with other ideas where you can share
*  states between things and so on, but at a high level, that's not really how it works.
*  Yeah, that's super interesting. So that means that the original Mamba states are pretty small. This
*  was one of the things I was trying to figure out is like, because they're confined to the size of
*  the available SRAM. And that's not that much depending on exactly what hardware you're running
*  on. And so now we also have to remember to divide that by the number of layers in the model. And
*  that is sort of the maximum size of memory that is available at each layer would be probably down
*  to something like a megabyte or even smaller than a megabyte. Is that right?
*  Well, so when you're using this in training mode, we put all the states, we kind of like don't
*  materialize the states because we don't need them. So this is kind of where the clever algorithmic
*  techniques come in, where old school RNNs like LSTMs, you needed to materialize the state in
*  every forward pass, but you needed to materialize it in DRAM in every forward pass. And so you are
*  actually like creating these states. And that's what limited the size of these states. And that's
*  what limited them from really scaling. Now with Mamba, it's a little more subtle than that. So
*  what happens is that you can basically, and even before Mamba, like with S4, this was a common theme
*  of all of these states based models. One of the defining characteristics is that their state,
*  all of them can really be rewritten in multiple ways in a way that hides the cost during training
*  time, but then you materialize the states again at inference time. So basically Mamba talks a lot
*  about kind of only materializing the state in the more efficient levels of the memory hierarchy,
*  like in SRAM. And that is what happens during training. And basically the reason is that at
*  training time, so yeah, so maybe this is kind of some intuition. So I've talked about how at
*  inference time, the state is where you need to like go from one input to the next one in order
*  to process the next input. And at inference time, we do have to materialize the whole state. It's
*  because we need to keep it stored somewhere in between time steps, right? So we're going to be
*  keeping that in DRAM, like main memory. And you can't avoid that because that's, by my definition
*  of the state, that is like what it needs to do. You need to store it somewhere so that you can
*  process the next input. The difference is that in training time, because the point of training is
*  that you see like the whole sequence at once, you see every input at once, and there's no notion of
*  this sequential reality where you're like seeing them one at a time. And so then you can try to
*  be clever and find ways to not materialize the state because you actually didn't need that state
*  to process the next input. You can kind of like materialize the state more ephemerally or even find
*  other ways to completely get rid of the state. But the idea is that basically, because you see all the
*  inputs at once, you're not in this regime where you need to store the state in between processing
*  inputs. And so we kind of like can figure out the entire state ahead of time, right? The entire state
*  for every element of the sequence, we can figure that out in one go ahead of time. And then because
*  we can figure that out ahead of time, we then don't need to like write the whole thing down.
*  We can go straight to like jumping from that to the output and find clever ways to kind of
*  do that more efficiently and not have to write down the intermediate states. So yeah, back to
*  your question about like how big is the state, we do need to materialize it at inference time for
*  these auto-regressive models. However, they are still a lot smaller than usually what people use
*  for transformer. And the very horse-grain way to think about it, which is actually, I think,
*  pretty accurate is that, so basically, like these models all have a concept of like a model width,
*  which is sometimes called demodel in transformer literature. So it's basically like the size of
*  every single activation, your model is going to be the same size, which would be like, you know,
*  like a thousand or 2000 or 4000 or something. And then the memory cost of these models scales
*  basically for transformer, it's that size times the length of the KV cache. So if you want to
*  be caching your entire history of say T tokens, then you'll be storing T times your model with
*  amount of memory that needs to be like stored in main memory as you're doing inference.
*  And for the SSM, instead of T, where T is the number of like tokens you're trying to cache,
*  we use instead an expansion factor that we call N, and that is a completely controllable
*  hyperparameter. So that controls basically the amount of compression you want. So a transformer
*  might be saying like, we've seen 10,000 tokens, the amount of memory we're storing is 10,000 times
*  demodel. And with an SSM, it's basically going to be like 100 times demodel or 200 times demodel,
*  whatever. Like this is a completely controllable expansion factor is what we call it. And that's
*  basically the trade off between the efficiency versus performance that we want. So this is
*  exactly the thing that controls the amount of compression that you want. Right? So more
*  compression means fuzzier memory, but faster. And sometimes maybe even like smaller things can help
*  because you're forcing the model to be more intentional. So we see kind of diminishing
*  returns in this thing. But the important part is that like, this to me feels like a much more
*  natural lever of how do you control your memory size versus with a transformer, either you just,
*  instead of this like controllable expansion factor, your memory scales with a number of tokens,
*  you're trying to remember, and then you're playing a different game, you're placing a game that's like,
*  how many tokens do I want to remember and which tokens I want to remember. You just think about
*  it very differently, right? But these are kind of the way to think about like how the memory
*  compares for both of these models. Hey, we'll continue our interview in a moment after a word
*  from our sponsors. Omnike uses generative AI to enable you to launch hundreds of thousands of
*  ad iterations that actually work customized across all platforms with a click of a button. I believe
*  in Omnike so much that I invested in it, and I recommend you use it too. Use Cogrev to get a 10%
*  discount. Hey, all Eric Torenberg here. I'm hearing more and more that founders want to get profitable
*  and do more with less, especially with engineering. Listen, I love your 30 year old ex-fang
*  senior software engineer as much as the next guy, but honestly, I can't afford them anymore.
*  Founders everywhere are trying to turn to global talent, but boy is it a hassle to do at scale,
*  from sourcing to interviewing to on the ground operations and management. That's why I teamed
*  up with Sean Lanahan, who's been building engineering teams in Vietnam at a very high level
*  for over five years to help you access global engineering without the headache. Squad, Sean's
*  a new company, takes care of sourcing, legal compliance, and local HR for global talent so
*  you don't have to. With teams across Asia and South America, we can cover you no matter which
*  time zone you operate in. Their engineers follow your process and use your tools. They work with
*  React, Next.js, or your favorite front end frameworks. And on the backend, they're experts at Node,
*  Python, Java, and anything under the sun. Full disclosure, it's going to cost more than the
*  random person you found on Upwork that's doing two hours of work per week but billing you for 40.
*  But you'll get premium quality at a fraction of the typical cost. Our engineers are vetted top
*  1% talent and actually working hard for you every day. Increase your velocity without amping up burn.
*  Head to choose squad.com and mention Turpentine to skip the wait list.
*  So kind of dig in a little bit more on the difference between the inference time and the
*  training time and why the state doesn't need to be materialized in the one versus the other.
*  I can understand that, okay, if I'm going to be generating one token at a time, I have to have some
*  memory to take me from one timestamp or one token to the next. But it's a little less clear
*  how you get around that at training time. I sort of get it with transformers where it's like all
*  versus all. But here, there's this like, what I'm trying to ultimately train this thing to do is
*  go one step at a time and not look back at all the tokens, right? In practice, at inference,
*  it's only going to have the state. So how are we squaring the circle? I mean, this is sort of a
*  pretty fundamental duality and conceptual insight, I think. But I'm maybe not quite fully grokking it.
*  Yeah. So it kind of goes back to this idea that like, well, let's think about what the model is
*  actually doing at the end of the day. And as I kind of defined it, these sequence models are
*  a transformation from an input sequence to an output sequence, right? And that map is actually
*  the only one you care about. So especially at training time, but also at inference time,
*  all you really care about is the map from like, you get an input token, what is the output token
*  for this particular layer of the sequence model? And then you can think of the state as an auxiliary
*  thing that helps you perform that map. Because as we said, like a sequence model is one where
*  all it is is a map from an input sequence and output sequence, but it's mixing along the sequence
*  dimension. So basically, another words to say is like this particular output token at some time t
*  depends not only on the input at time t, but on everything before it or like it can depend on
*  all the inputs. And that's why at inference time, we get a new token at time t. And we want to
*  compete the output at time t. But that output like dependent not just on this token, but on a bunch of
*  other previous tokens. And so that's why we needed the state to remember the context of all those
*  previous tokens. So that's why there is like a physical thing that you need to materialize that
*  is representing all the previous tokens. And so I can create this input to output map. But at the
*  end of the day, all we cared about was the input to output map. We cared about how do you compute
*  this output. And the state was like basically a supporter or like a helper thing that helped us
*  compute this map because we lost access to the previous inputs. Now at training time, we only
*  care about this input to output map. Because we see every input at once, we're no longer constrained
*  by the idea that like we lost some of the inputs. And so we need to materialize the state to help
*  us. And so there are many models where you can basically like go straight from the input to the
*  output by rewriting the definition of the model mathematically or so on. But even in the simplest
*  case, what we could have done, like what actually happens in Mamba, which is actually, it's this
*  thing that we call it the hardware algorithm. But in some ways it's kind of simple and kind of dumb,
*  but it's just saying that we are still going to materialize. Like we wanted to create the input to
*  the output. As a helper to do that, we needed to create the state. And so we are still going to
*  create the state, but we're going to materialize the state only so that we can use it to create
*  the output. And then once we create the output, we're going to throw away the state. And so we
*  store the input, we store the output, and then in between that we materialize the state, but then
*  we throw it away immediately. And so that's what reduces kind of the memory consumption, or that's
*  what allowed us to put that state only in certain parts of the GPU, because we really only care about
*  the output and the state is just a helper. And so, yeah, that's just kind of the thing about it. And
*  at inference time, the difference is that we still only care about the input to output mapping,
*  but in this case we cannot throw away the state because, like I said, we lost access to other
*  parts of the sequence. And so the state is playing a helper role that's storing that information for
*  us so that we can still create this function from the input to the output. And so maybe you can kind
*  of think of it as like at training time, you never needed a state. Same for transformers,
*  there's no concept of a KV cache, right? At transformer, you can think of as attention,
*  you can just think of it as a mapping from like a set of inputs to a set of outputs.
*  In attention's case, it's doing all these pairwise comparisons, but it's just a function from a
*  sequence to a sequence, no concept of state. At inference time, we suddenly need this concept
*  of a state to help us do the decoding because we lost access to history. And all models have
*  this concept of a state, like I was saying before. And that's kind of the fundamentals of it. And
*  then how do you actually define all these maps? How do you actually compute them? That gets a
*  little bit more into the weeds of, there's many ways of doing it. And so in the case of Mamba,
*  we still do materialize the state, but the observation is just that you can just throw
*  it away immediately and rematerialize it in the backwards pass, actually. In the case of attention,
*  you never needed to even think about the state in the forward pass on the model.
*  In the case of Mamba 2, actually, it's a little bit similar where we do this chunkwise thing
*  that's a little bit similar to attention. And there is an implicit idea of a state there,
*  but it's not materialized at all in the forward pass because there's just a completely different
*  computational graph that allows us to compute the same input to output mapping. So that's kind of
*  like linear attention in general is very related to these SSMs. And that's same sort of concept.
*  In S4, there was a same sort of concept where there is a recurrent state, but in the training
*  pass, we can completely rewrite the computation to, instead of being a stateful RNN, we rewrote it as
*  a convolution instead. And that convolution, once again, it's just a map from the input to the output
*  sequence, no concept of a state, completely different computation path just happens to be
*  mathematically equivalent. So yeah, that's kind of how I think about what is the role of the state.
*  So is it accurate then to say that the, I think you said this, but just to make sure I'm clear,
*  at inference time, Mamba does send the state out of the SRAM and to the main memory. And is it
*  shuttling those in and out like on a per layer level? Like if I have a 20 layer Mamba, I've got
*  20 internal states right then that I'm shuffling in and out. Yeah, of course there's optimizations
*  that people can do with this. And actually this is an area of research I think is interesting
*  where people did in the past, like with, when RNNs were popular, people would try to optimize them
*  for hardware and do optimizations. Like actually if your state is small enough, you can just keep it
*  in SRAM and avoid the expensive memory transfers, which takes up your bandwidth.
*  But then of course it would just be sitting in SRAM eating up some of that,
*  that other layers can't use. But so that's the sort of trade-off that one could think of.
*  But the most kind of standard thing to do is just you would treat this as any other layer would be
*  treated. And every time you use the layer, you would move all your weights and your state,
*  like from main memory into SRAM, do your computations there and move it back out.
*  And that normally does happen on a per layer basis for like every other layer. And that's
*  where specifically doing RNN type optimizations, it's the same thing that would happen for Mamba as
*  well. Yeah. And so the efficiency comes from just the fact that the state size is smaller. So
*  whereas in an attention layer, you're doing the exact same sort of like moving parameters and
*  state around because the state is so much bigger. Usually that's what makes it slower inference time.
*  And in Mamba, it is, we still do the sort of the same concept. It's just much smaller states. So
*  there's only certain regimes also where this helps. Like when the sequence length is very long,
*  when the batch size gets bigger and whatnot, that's when your state really explodes in size
*  and becomes the limiting factor. And that's when you see these efficiency gains for these compressed
*  state models like SSNs like Mamba. Yeah. It is interesting to think that there are probably a
*  lot of little subtle variations on this that could work. Certainly we've seen in the transformer
*  context, there's like various kinds of caching and shared queries across layers. And that seems
*  to be like something people have pushed pretty far. I think the most recent character scaling
*  blog post showed a lot of room to share different aspects of that cache across layers. And it sounds
*  like there's some similar possibilities here if I take your implication correctly. Yeah. It remains
*  to be seen. One of the things that I generally like to emphasize for people interested in this
*  space is that I had a vision for this. I have a lot of ideas. I have a lot of particular reasons
*  why I think that these models make sense, but there's still a large sense of it that's kind of
*  intuition driven. And it's coming more from the idea that I don't have all the ideas. There's
*  hopefully going to be plenty of smart people who are interested in this and want to work on things.
*  And they'll come up with lots of optimizations and lots of ideas that we can't see right now.
*  But there's more of a faith that if and when people spend as much effort trying to optimize
*  these models as they have for other models like attention, even if we don't see these
*  optimizations now, they exist because there is something fundamental to the definition and
*  like the fundamentally different nature of these models. So back when attention came out, no one
*  knew the exact set of optimizations we have today. And people look at them now and they're like,
*  oh, attention. A lot of the most optimized implementations or variants are cut down on
*  a lot of the issues with those models with the state size and so on. People might ask,
*  does that reduce the benefits of SSMs and so on? But I think one thing to remember is that there
*  are probably just as many optimizations that could be done for these models that would further push
*  their efficiency, expressiveness and performance. I don't see all the ideas now, but I believe they
*  are there and would definitely encourage people to continue thinking about this direction.
*  Well, let's get into some of the evolutions and optimizations that you've made with Mamba2. And
*  then we can talk a little bit about some of the downstream work that the community has produced
*  over the last six months. The Mamba2, I mean, Jason and I have studied this and have kind of
*  identified a number of differences based on the conversation so far. If I had to summarize those
*  differences, it seems like there is a small compromise made in the expressivity of the
*  model. That is that part of the sensitivity of the computation to the input is made slightly
*  less sensitive to the input. And in exchange for that, you get a lot of nice things from modern
*  hardware. Take it from there. Yeah, that is a very good summary of the high level trade-offs,
*  especially from a practitioner standpoint. That was the main motivation between Mamba2 and Mamba2.
*  We were pretty happy with where Mamba got us in terms of being able to do all this selectivity
*  stuff. As I mentioned, doing that is computationally very nontrivial, and we were able to do it
*  reasonably efficiently, but there are still clearly shortcomings because the core SSM part
*  was not leveraging any tensor cores or in other words, matrix multiplications, which is what all
*  modern hardware is pretty much specialized for. Part of it is a little unfortunate in that, have
*  you heard of the concept of the hardware lottery? So there's this concept where software and hardware
*  and models kind of all co-develop in a feedback loop. And so models that were doing well early on,
*  people start building specialized hardware for, that incentivize people to optimize and push those
*  families of models even harder. And it becomes hard to break out of the cycle, even if there...
*  Maybe at some points it can feel a bit more of a local optimum and there's entirely different
*  things that make sense. And one can argue maybe attention has sort of taken that role. To be
*  clear, I don't think attention is going anywhere. I think it is very important, but is it all you
*  need? Not sure I believe that either. And so the unfortunate thing becomes that because things
*  have co-evolved so tightly, it becomes harder for other types of completely different models to
*  gain traction because they just won't be as efficient. And it's not that the models can't
*  fundamentally be as efficient, but because that's what the current hardware is built for,
*  is not those models it's for, like CNN, like convolutions and attention and things like that.
*  The point is that part of me is a little reluctant to be like, let's change the model so that we can
*  make it efficient on hardware because it feels a little bit like playing into the hardware lottery,
*  that feedback loop, kind of like throwing our hands up and saying, okay, we just have to play
*  this in game. On the other hand, it's kind of inevitable because the fact is just that you need
*  something practical to be worthwhile. And unless you can take a bigger bet and build your hardware,
*  which will take years of development, it doesn't make sense. So we were trying to figure out if
*  there was a compromise that could let us keep the spirit of Mamba and these SSMs, but find other
*  algorithmic innovations that could let us leverage matrix multiplications and leverage
*  the tensor cores on GPUs and make it even more practical. So we worked on that actually back in,
*  I'm not sure if people realized, we kind of hinted at it in our release tweets, but we basically had
*  the algorithm and most of the model for Mamba 2 done back in October, basically, before Mamba 1
*  came out. And we originally thinking of putting it out much earlier, but we're both pretty busy
*  these days. But yeah, pretty early on, we were trying to figure out how to make it more efficient
*  on hardware. And we took some inspiration from things like linear tension as well. And so basically,
*  we figured out that if you kind of restrict the expressivity in one specific way, the model
*  becomes, because it's simpler, it also becomes easier to compute with. And we kind of found like
*  an alternate computation path to compute the model. Then turns out like, there's a bunch of pretty
*  interesting theoretical connections there. So the Mamba 2 paper is very long and has a lot of theory
*  I mean, it's not that complicated, I think, if you really look into this day, I don't know if that
*  paper is like deep or trivial. But you know, maybe that's exactly where you want to be. Yeah, so we
*  basically just found a way to try to like, I think probably there's still more that can be done,
*  but we were pretty happy with where it ended up here. And Mamba 2 was a mix of all these things.
*  So the core thing from the practical standpoint is the faster algorithm. To me, the most interesting
*  part of the paper, actually the theory, which I think do reveal a bunch of interesting connections
*  that I think will hopefully inspire a lot of downstream work. Most of my students at CMU are
*  basically doing stuff based off Mamba 2. And these connections open up a bunch of like more
*  fundamental research directions. But for the Mamba 2 paper itself, the most direct consequence was
*  this faster algorithm. Now, I think there's a natural question about what are we paying
*  for this improved efficiency. And I think honestly, I'm not completely sure myself at this
*  point. So I think this is one of those things where like me and Tree did as much experimenting
*  as we had time for. But I think there's a lot of work to do and kind of maybe like the interpretability
*  side or the mechanistic, like, you know, actually going to the black box and figuring out what these
*  things are learning. That would be really great to kind of explore. As far as we can tell, so I guess
*  to give a brief nutshell of how Mamba 2 differs from Mamba 1. We've talked a bit about how these
*  models broadly speaking, they have a fixed size state. And at every time step, you're kind of like
*  decaying the state by some factor that depends on the input in the case of selective SSMs like Mamba.
*  Now that factor can take different forms of granularity. So you can think of the state
*  vector as like, I don't know, what's the actual size, it's going to be something that's like
*  demodeled by like 100. So maybe like 100,000 numbers in your state for one layer of the model.
*  In Mamba, each one of them undergoes a different decay per time step. We're going to take the input
*  and project it up to a vector that's the same size as the state vector. And then we take the
*  element-wise product of those two. So every single individual number in my state will get decayed by
*  a different amount that could be a constant or it could be depending on the input. So that's kind of
*  how all these previous SSM worked. In Mamba 2, basically, the reduced expressivity comes from the
*  fact that we take like large chunks of your state and decay all of those chunks by the same
*  amount. So you might take your 100,000 numbers and split it into like a thousand chunks of 100 each.
*  And then each one of these components of the state of size 100, each of these hundred numbers will
*  get decayed by the same amount when you go to the next time step. So basically the expressivity and
*  kind of these recurrent dynamics, the dynamics are what I call like the decay factors because
*  they control the evolution of your state. There is reduced expressivity in that update mechanism.
*  So we were actually not completely sure if this hurt us or not. Mostly we looked at like downstream
*  tasks. I think we concluded that it doesn't seem like it is hurting us, but I can imagine that maybe
*  there are more specific tasks that it can. I don't know what these are off the top of my head. It would
*  be great if the community starts digging in there. But I could also see maybe that the reduced
*  expressivity could also potentially help you because there's the age old question of like
*  flexibility versus inductive bias or kind of like how much priors do you put on your model? How much
*  structure do you put into your model? And for things like convolutions, there's lots of structure
*  baked in and it makes them very well suited for certain types of applications. Similarly, I can
*  imagine a world in which the additional structure being baked into Mamba2 that is reducing its
*  expressivity is actually also providing a helpful form of inductive bias that can help it on some
*  tasks. The simple example, which I think I also wrote in the blog post on Mamba2, is this example
*  that I gave earlier today where one of the motivations for this concept of sensitivity
*  is ignoring filler words or filler tokens. And so if you see an um, you might want to ignore the
*  whole thing. And how does that work mechanically in the model? That means that you'll take my state
*  and kind of, if I want to ignore the next token, then I just don't want to decay the state when I
*  move over, right? So that input dependent decay factor, I'm just going to set to like one. So I'm
*  multiplying my entire state by one. And so it's not changing at all. Now, maybe that sort of
*  thing is easier if your dynamics are tied. So if I took like a block of my state in Mamba1,
*  each one of these are going to evolve independently. How do I know whether it's
*  truly preserving all the information? The model is going to have to make every single one of those
*  scalar update factors equal to one, whereas in Mamba2, it only needs to make much fewer one of
*  those update factors equal to one because those update factors are being used on a lot more of the
*  activations in the state. That's kind of like a very, very simple thought experiment about like,
*  why might it be possible that it's actually useful to have this form of reduced expressivity?
*  One particular downstream task that intrigued me that I haven't had time to personally dig in
*  is this concept of associative recall, which a bunch of researchers working in this space,
*  some of which from my PhD supervisor's lab, Chris Ray, some of these students, Simran and Sabri,
*  were working on identifying where recurrent models fall short of attention and identified
*  this concept of associative recall, which is one can imagine it kind of like a dictionary lookup
*  as well. It's like, can a model learn to read the dictionary and then given a new word, can it
*  retrieve the dictionary? They found that this is very, very hard for recurrent models, which makes
*  sense. Like we previously said, human brains can't do this either and finite-sized state models,
*  which are trying to compress stuff intentionally, have a hard time doing this. Now, it turns out
*  that most of these recurrent models basically struggle a lot on these tasks. Mamba1 is actually
*  pretty good compared to a lot of the elements out there, but for some reason, Mamba2 blows Mamba1
*  out of the water on this specific type of task. And all I have are the empirical results. I'm
*  pretty sure they're correct, but I didn't have time to dig in mechanistically what's going on.
*  Even just ablating away parts of the architecture would help. And the only possibilities are either
*  some random part of the architecture that I thought was irrelevant actually really helps on
*  something like this. I wouldn't put it past this possibility, but the other possibility is
*  potentially the inner SSM itself is actually better suited for this type of task because again, maybe
*  the difficulty of associative recall is kind of like caring and remembering your state exactly.
*  And having this concept where we're going to block your state into chunks, maybe each chunk
*  represents a concept and it's going to kind of decay or evolve together. Maybe that's actually
*  a helpful form of inductive bias. So yeah, it's a jury's still out. Not really clear what the
*  trade-offs there are exactly, but definitely a potential area to investigate. I have a lot of
*  follow-up questions. So I guess the other part that I thought I understood from the Mamba2 paper
*  is that internal states can be bigger, right? You can now sort of spread this out over more hardware
*  and do various forms of parallelism. And with that comes just the opportunity for bigger states.
*  When you were making these comparisons of Mamba2 versus Mamba1, what exactly are we holding
*  constant there? A lot of times people hold flops constant. It seems like that's not quite really
*  the right unit here because here you're using more flops, but using the hardware more efficiently.
*  Maybe hardware hours would be maybe one way to think about it. Could be tokens, I suppose,
*  also as well. What's the input and resource that's held constant? What is allowed to vary?
*  And how does that inform our intuition? Yeah, that's a good question. So there's
*  many different axes involved in thinking about efficiency. So of course, like you said,
*  flops is one. You can hold many other things constant, such as wall clock time. So that's
*  going to compare more to actual hardware utilization as well. You can also hold
*  inference time efficiency as the constant. While training is usually correlated with
*  inference time, they might not be exactly the same. And one example is Mamba2 versus Mamba1.
*  So first, let me just say a little bit more about the differences. There's many,
*  a bunch of differences, but they kind of fall into two buckets. One of them is what goes into
*  the core SSM layer. So this is something I mentioned earlier. There's a core SSM layer,
*  and this block gets stacked a bunch of times and incorporated into other components. That core layer
*  is what I think of as the fundamental difference between Mamba2 and Mamba1. And if I'm being more
*  precise, in Mamba1, we define this thing called the S6 layer. In Mamba2, we define the thing called
*  the SSD or state space dual layer. That's the name that we give to this core inner SSM layer,
*  which is the thing that has these ABCD matrices and whatnot. That is the main thing that's changed.
*  We talked about earlier, that's the part of the model that has a state. That's the thing where
*  all these considerations about the state effects. There are a bunch of other changes to the
*  architecture, which is what I call the thing that you're, how you're wiring all these layers together.
*  That I think is a little less relevant, or these things are kind of also independent. We could have
*  used the same inner SSM layer from Mamba and made the architectural changes in Mamba2. And that would
*  have been just completely independent changes. Some of the things you mentioned, like some of
*  the differences that Mamba2 allows us to do. For example, in Mamba2, we start talking about
*  sequence parallelism, tensor parallelism, and so on, like other forms of infrastructure and
*  efficiency optimization, systems optimizations. Those are mostly, I would say, kind of based on
*  the architecture and not the core, like Mamba2, like the SSD layer. We could have made these
*  changes for Mamba1 as well to get the efficiency in there. The reason we included in Mamba2 is
*  because A, they are like sensible changes to make as a default. B, because some of the reasons we
*  motivated them was because of the connections we drew in Mamba2 between SSMs and attention.
*  So that was kind of the whole theme of this state space dual layer. It's a duality between the
*  state space model. And that helped us realize a couple of connections that helped us kind of like
*  change the architecture in a way that is a little more transformer-like, but will allow us to
*  leverage techniques from transformer literature to improve the systems aspect and the efficiency.
*  But many of those could have been applied to Mamba1 as well. It's kind of in the architecture.
*  The second category of things, which is more important, are the changes made inside the core
*  SSM layer. And that's the thing that we were talking about, like changing the definition of
*  the model, changing the expressivity, but in return getting much more efficiency. And part of
*  that efficiency is letting us get larger states. So now, back to the original question, like how
*  do we actually make this comparison then? It is tricky. So it really depends on what axes you care
*  about. And the trade-offs are not all correlated. So in the main comparisons we made on the scaling
*  laws, what we decided to do is kind of just preserve the model size. So like the standard
*  definitions of model size is like, how many layers do you use? What's your model width or the demodel?
*  These all lead to models roughly comparable parameter counts. And we just kind of chose to
*  roughly preserve the same parameter counts and so on. And the parameter count of Mamba2 versus
*  Mamba1 doesn't really differ that much. And this is another axis of efficiency that we could have
*  talked about. People often control for parameters as well. What we decided to do was in the main
*  comparisons to control for parameters, mainly because that kind of utilized these very standard
*  model sizes and because all these other axes of control were a little hard to do the exact
*  right thing. So they all changed maybe a little bit and we decided that we'll just kind of look
*  at all the changes together. And so in the regime where we kind of controlled for parameters,
*  Mamba2 was basically pre-dominant over Mamba1 in terms of performance as measured by perplexity
*  and wall clock time, or kind of all just strictly better. But again, that's only one facet of the
*  comparison. But yeah, by wall clock time, if you're kind of controlling for like training
*  actual speed, Mamba2 is way better than Mamba1, but you might want to control for inference speed
*  instead, because after you train the models, of course they're deployed and maybe that's what
*  actually swaps the cost that might actually affect the performance and the models actually
*  building more. There the comparison is a lot less clear because Mamba2 allows us to get larger
*  states while training and still being efficient. But we might not want larger states because
*  there's like this whole Pareto frontier of like state size versus model performance where like
*  larger states will get you more performance, but it saturates at a point. And between that fact and
*  the fact that there's reduced expressivity, maybe if you really only cared about inference time,
*  you would actually want smaller, more expressive states, which are going to be faster inference
*  time because inference really scales with of course the model size, but also like the state
*  size of the model. So we actually didn't compare that in the Mamba2 paper, but basically the point
*  was that Mamba2 is really focused on the training side because for most people, that's what's going
*  to dominate your research, like experiment cost. Even for people who want to serve models,
*  the training is very non-trivial because it's not only training the model, but experimenting with it.
*  Right. And the faster you can experiment, the more you can improve things and so on. So we decided
*  that training speed was a very, very important factor. And that's what like, yeah, we had a
*  huge improvement there from Mamba2. I can imagine worlds in which people might want to be running
*  smaller models on device or something and really only care about that, that you would then use a
*  completely different axis of comparison, like the inference speed and make different sets of
*  choices that you might want to make. Now, I do think that it's likely that the architectural
*  changes we made in Mamba2 are just better. There's things like, where do we place the linear projections?
*  Do we add extra normalization layers? Stuff like that are basically the bulk of the changes
*  architecturally we made in Mamba2, which I think probably are sensible by default,
*  but for the core SSM layer, it's not quite clear. It really depends on which one of these axes you
*  care about. And they're all reasonable, I think. Okay. There's a lot there. I think the analysis
*  of all these different trade-offs is super interesting. I want to make sure I understand,
*  is the change that allowed there to be bigger states, how did that get unlocked?
*  Yeah. So that's the thing that's really like in the core, how did we come up with Mamba2?
*  And I don't know if there's an easy way to explain this without being super technical,
*  but it's kind of related to the idea we talked about before, where in the training pass of the
*  model, the forward pass, you see the whole sequence ahead of time, and you're just trying to compute
*  this input to output map on your sequence. That map, if you can, that map, you can compute however
*  we want. And if you can rewrite it in ways that are more efficient, then that's basically for free.
*  So the small change in expressivity in the model, in the definition, basically allowed us to do this
*  forward pass from the input to the output that avoided materializing the state. Basically,
*  like, so now in the forward pass, we actually don't materialize the states most of the time.
*  Or you can think of it as like, we materialize the states in between chunks. One way of viewing
*  this whole change is that we're going to take the input sequence and chunk it into small pieces.
*  And then within each chunk, we can compute the input to output map without even thinking about
*  the state, just like attention. Attention as a state, which is the KV cache, but in the forward
*  pass of the model, you do just like these three giant matrix multiplications and don't need to
*  think about the KV cache. In Malba 2, it becomes a similar concept where we rewrite the computation
*  in this attention-like way, where we do matrix multiplications on each of these small chunks.
*  And then we do materialize the state in between the chunks, but because we're chunking things,
*  the number of states we have to materialize goes way down. So that's a little more technical into
*  how the algorithm works and why this allowed us to be much faster during training.
*  The idea is just that in between chunks, we're able to leverage matrix multiplications now,
*  and we're also able to reduce the amount of states we have to materialize. So your question was,
*  how did we get there? So yeah, that's basically the main idea for how we got these increased states
*  to state sizes. The core insight is, because we want to take advantage of the highly efficient
*  matrix multiplication capabilities of the modern hardware, we will make this compromise
*  in terms of the expressivity of this projection layer that puts new information into the state.
*  And then we can afford bigger states because we're actually going to move some off of...
*  I'm still a little bit fuzzy on how that actually gets me more state size inside.
*  It's like when we say that we can get more state size, there's always implicitly a trade-off
*  involved here. Like in Mamba 1, we could have gone a larger state size. The second part of
*  that sentence that is left unsaid is that it would be much slower. So you can always define
*  your state sizes pretty much as large as you want. The computation of the model is the same,
*  it's just that in practice on hardware, this is going to become very slow. Because in Mamba 1,
*  what happens is that you're materializing these states in SRAM, you're using no matrix
*  multiplications, and so you're doing just lots of flops that are the less efficient form of flops
*  utilizing tensor cores. So in Mamba 2, when we say we can get larger state sizes, what we're
*  actually saying is that as the state size grows in either Mamba 1 or Mamba 2, it's relatively
*  more efficient in Mamba 2 to have larger and larger states compared to Mamba 1. And the reason
*  that is true is because in Mamba 2, we basically completely rewrote the computation to not
*  materialize the states in the forward pass. Basically, the change in the expressivity in the
*  model is what allowed us to rewrite the computation in a way so that the sequence to sequence mapping
*  in the forward pass can bypass writing down the state. That's why when we have larger states,
*  it is relatively more efficient than Mamba 1, where if you double the state size, we're doubling the
*  computation, pretty much doubling the walk-on time to an approximation. In Mamba 2, much of the
*  computation is not directly contingent on the state size. That's why larger states scaled better
*  in Mamba 2. So maybe that's a little more nuanced when I was looking at it.
*  So I think maybe a misconception that I had coming into this is that I had assumed that in Mamba 1,
*  the size of the state was limited by the available SRAM. And you're saying not really,
*  there was actually more SRAM available, but it was the computation that was just going to get
*  slow and sort of governed how big the internal states would be. Now, because the tation is faster,
*  you can use more of the available SRAM for states.
*  It is true that in Mamba 1, you're limited by the amount of SRAM. I don't think we scale the models
*  to a size where that actually would have mattered. And so the trade-off that we were considering more
*  is even assuming you can fit everything into SRAM, there are still different types of computations
*  that are more or less efficient. And Mamba 1 is purely a bunch of element-wise operations.
*  So we kind of have a plot near the end of the paper that kind of directly shows this, where
*  we increase the state size in both models and show how in Mamba 1, it rapidly kind of reaches
*  this saturation point where your speed basically increases linearly with the state size because
*  you've already saturated how faster a model can do things like element-wise multiplications.
*  Whereas in Mamba 2, as the state size increases, we're shutting more work into the matrix
*  multiplications, which are actually scale much, much better. Okay, cool. I think I have at least
*  an intuition that I feel satisfied with, which is always a great spot to get to.
*  This is actually a Jason question. Could you imagine, and also kind of taking inspiration
*  from the sort of trend toward over-training, right? We've definitely gone down this path of
*  chinchilla scaling laws to llama, highly over-trained, but more like inference-efficient
*  training strategies. Could you imagine a move in the other direction where you would say,
*  hey, what if we made this inner mechanism more expressive? Maybe we'll pay some training time
*  tax, but if it really works, then maybe that could be a path toward something that is really
*  powerful and potentially could be more efficient on the inference side. Does that make sense?
*  There is something there for sure. That's one thing that when me and Tri were doing Mamba 2,
*  we were kind of discussing even how to pitch it. For the most part, we think it is just better for
*  most people to use, at least especially for more exploratory things. But I was a little hesitant to
*  try to claim that it was strictly better than Mamba 1 because I think we just don't completely
*  understand. I do think there are maybe niche cases or maybe even not niche, but maybe after
*  you finish exploring whether SSMs are good for your application, then you decide you really want
*  to optimize for inference time. Then you decide to go for a more expressive model with smaller
*  states that is just as optimized for inference as possible and just eat the training costs.
*  That certainly seems viable to me. I don't know if we'll see a big shift towards that,
*  but it's certainly not out of this world. I can definitely see people doing that.
*  Yeah, because I guess it's really interesting to think about the trade-offs between training
*  efficiency and inference efficiency. I think there's a lot of people putting models into
*  production that are really willing to trade off training efficiency. If you think about
*  SSM as a starting point, I think there were some papers about this. In theory, there are ways maybe
*  it could be more expressive. Even the SSM, I have no intuition on what the mathematics would have
*  to be to make it more expressive. Maybe you'd have to get away from the diagonality. Any ideas,
*  I mean, what Mamba 3 or this go in the other direction? How much cost that you would have
*  to incur to gain the diversity? For example, there is a recent paper by Will Merrill,
*  who does a lot of work on formal languages and sequence models. To my understanding, basically
*  said that in terms of a formal language perspective, the SSMs that we're using are not
*  better than other types of linear models and not as expressive as LSTMs, I think was the claim.
*  I believe that there are some subtleties there where I'm not sure if I should say this,
*  because basically, to my understanding, the fix was to make the SSM state a square matrix instead
*  of a diagonal matrix. I think this paper sort of said that the other issue was that you need the
*  A matrix to be input dependent and ours wasn't, but that seems a bit of a red herring to me because
*  the discretized A matrix, I'm getting a bit into the weeds of SSMs again, but there's this
*  discretization step that all the old ones used where you create your current dynamic matrix A,
*  what we call A bar through this other formula, but effectively in Mamba, the recurrent matrix
*  is dependent on the input. Then I think this paper claimed that you need not only that,
*  which already is true, but also that you need it to be dense instead of diagonal to get full
*  expressivity. I might be completely wrong, but that was my understanding. That's an example of how
*  making the model more expressive might actually make a difference, at least in this case, from a
*  theoretical formal language perspective, but maybe also in practice in cases, it could help.
*  Maybe the model just learned how to do things it couldn't do before. I don't really know,
*  but the downside of that is that the speed cost would be basically unmanageable, I think,
*  and thus people come up with much more clever techniques. That was actually the exact thing.
*  Earlier when I said that I had been trying the selective mechanism long, long time ago,
*  what we were trying to do was, this is right after the hippo paper, there we were using
*  dense matrices, and I was basically trying to make them input dependent and still able to be
*  computed fast. I spent quite a while on it and it was just impossible. The way that things have
*  evolved have been pretty intentional and maybe technically or theoretically loses some expressivity,
*  but I personally feel that in practice nothing really has been lost. I definitely could be
*  wrong there. Maybe if we somehow find ways of defining dense matrix or more expressive
*  SSMs that can be computed efficiently, we'll see different set of things that could be unlocked.
*  Maybe at inference time you don't really lose any speed. Exactly to the point of this question,
*  maybe there is a world in which somebody would want to make that trade off to eat this massive
*  training cost right now in return for a better model that is going to be the same speed at
*  inference. That's a great example. It connects also to an intuition that I have around hybrids
*  and more and more diversity perhaps coming in hybrid space. We've seen that hybrid attention
*  in state space, selective state space model, Mamba and Jamba and whatever, hybrids seem to always win.
*  It seems like there's a sort of emerging consensus that somewhere between one in eight, one in ten,
*  one in twelve layers need to be an attention layer to get the benefits of the attention
*  mechanism and then the rest can be like the state space model. If we kind of search that space at
*  small scale, maybe we could end up only having to use one in twenty layers or something to
*  get the unique micro skills that it brings to the table. How do you think about these sort of
*  complementarity between these different core mechanisms? Maybe you could define it in terms
*  of the problem. Is there something that you still see that the current mechanisms can't do that you
*  would be looking for a third core mechanism to be able to layer in with the others?
*  Yeah. First in terms of the trade-offs between these, I think this is something that
*  I've been saying for a while. A lot of people have independently concluded this, that the mechanisms
*  are just doing complementary things. At this point, I actually don't know if a pure SSM could
*  recover the ability of attention on some types of tasks. For example, the dictionary example I've
*  been using or maybe reversing a string. A lot of these things that, the same type of tasks that
*  humans might have trouble with in working memory is the same things that attention is good for
*  because it is giving you a database of every, like a scratch pad basically, or there's many
*  analogies you can use. It allows you to just look at every single password, attend to every past
*  thing that you've seen. I'm not sure at this point whether a pure SSM can figure out how to do exactly
*  all of that. Conversely, I think that the place where SSMs really are useful over attention that
*  I think has also been underexplored are areas where the, kind of on more raw data or areas where
*  things have not been processed as cleanly as for attention. So example I use is that the performance
*  of transformers is like pretty contingent on the tokenizer. And I think the intuition for that
*  is that the tokenizer is helping doing a form of compression that is like a separate stage of the
*  pipeline. It's a little bit handcrafted. That's helping the model compress things that it doesn't
*  need, right? And without that compression step, attention has a really hard time doing the
*  compression by itself because it is by definition a model that does no compression. And so like
*  there was a follow-up called Mamba Byte by Sasha Rush and his students at Cornell that showed that
*  if you're modeling from raw bytes, Mamba seemed to do way better than attention. And I think my
*  intuition there is that when you're modeling at the byte level, like there's so much lossy information,
*  like we humans don't look at things at the character level. We chunk them into words or other
*  concepts. And for transformers, that's what the tokenization step does. And that's why they are
*  worse on less processed data. For Mamba, the whole idea of it is that you can do compression so that
*  theoretically the performance will be the same in either case. Of course, it's going to be slower
*  to train because you're doing a little less of the handcrafted, like simplifying the data, but
*  that's maybe a working explanation for why it does so much better on that sort of data.
*  And similarly, we've seen in other forms of data that have co-evolved less with transformers, such
*  as in the original Mamba paper, we did some DNA modeling. That may be also why it seemed to work
*  better out of the box there. As for a third mechanism that can complement both of these,
*  that's a great question. I haven't thought too much about it. I am kind of, one thing I'd be
*  quite interested in is something that is better at, maybe also related to this tokenization thing,
*  but something that can actually automatically chunk things in a differentiable way, like input
*  dependent, smart like pooling layer that can chunk things. I haven't really seen anything like this.
*  I think that would be really cool and maybe also kind of important because otherwise a lot of these
*  models are just quite wasteful in ways that are hard to get around. But yeah, who knows about that?
*  People have been trying to come up with alternate mechanisms forever. I'm still open to the
*  possibility that just scaling attention layers really will get us more and more smarter models.
*  Some people think that there's a limit to that. Some people think they don't. I don't think I've
*  made up my mind. I obviously think that there are real benefits to using alternate models like SSMs,
*  but it's not to say that maybe if all the compute in the world is thrown at just scaling attention
*  more, maybe it will just work. Yeah. Well, that's one of the trillion dollar questions.
*  Anyway, we've studied the Mamba derived literature quite a bit. I wouldn't say at this point I've
*  read every paper by long shot because they, like everything else in AI right now, are going
*  exponential. I don't know if you've peeked at our notes, but would you care to guess the number of
*  Mamba derived papers that Jason has counted up in catalog to date?
*  I think that there have been, it's been out for around six months now and seven months maybe,
*  and I think probably has around a few hundred citations. So I would guess like
*  two, 300 papers maybe. I do see lots of random follow-ups that are basically plug and play,
*  basically. Take the model and plug it in somewhere. Those are always fun because I think one of the
*  reasons we did this is because we did want to create like a fundamental primitive building
*  block that people can just use just like attention has been used. Yeah. It's been a little surprising
*  how much people really seem to like it. The names are also something out of my expectations when we
*  first put this out. I didn't think everyone would be naming their thing like Mamba, Zamba, Jamba,
*  whatever. Your reasoning is sound. 267 is the number of papers and projects that Jason has
*  collected into a spreadsheet. So we can share that full list. That'd be interesting. There's a
*  lot of applications. Yeah, sorry. It was very selective. So I mean, if you go to archive,
*  I mean, there's probably more than that, that reference. But that includes like a lot of
*  GitHub work, stuff that only really circulates on Twitter, but that's still good quality work.
*  So yeah, I think that there's probably somewhere around like close to 500 citations, but a lot of
*  them probably are like, just mentioning SSMs. And then Mamba is kind of the representative citation
*  as well as S4. The amount of applications would be lower than that. But there is a surprising
*  number to me of like things that just kind of used it. And let's see, what have there been?
*  There've been things on graphs, plenty of language things, lots of vision things. I saw a tweet once
*  where like every single possible scan pattern for like images has been used to try to feed it into
*  a Mamba layer. Like time series, probably like one of my collaborators at Cornell did some genomics
*  modeling. So yeah, there's lots of stuff. Anywhere you see sequences, I think it is kind of a natural
*  choice. I don't think it's always the best choice. Like sometimes attention really is used for a
*  reason. If you really have no ordering on your input or not very much sequential structure,
*  it really does make more sense to use attention sometimes. And that may be a reason why the scan
*  order is so important for all of these vision papers. So I think it's unsurprising that in a
*  lot of places where there's less coevolution of the application with transformers and there's
*  less structure and so on, and there is sequential structure, that's really where like Mamba and like
*  SSMs shine. And I think that's hopefully what people have been finding in these follow-up
*  applications when they kind of just replace their transformer with a Mamba layer.
*  56.6% of those JSON reports are in the vision and image category. And if anybody wants to
*  hear us talk more about the different scan approaches that we covered quite a few of them
*  a couple months ago in the Mamba-Palooza episodes. Oh, really? Okay. So one thing that I've been
*  looking for somebody to try to create some sort of loss or objective function on the state itself,
*  where I'm kind of motivated by this idea that I think like we're all expecting there to be
*  these like great AI assistants that are going to have full context on us and whatever. And right
*  now we sort of have this missing memory problem, like missing middle memory, right? Where we have,
*  at least with attention, we have like the finite context window and then we have like a sort of
*  tool used to search through email. We don't really have that middle integrated memory that would sort
*  of match our own experience of being able to generally remember stuff. That was what attracted
*  me initially most to the Mamba work was that it seemed like a big step in that direction.
*  And so then I've been thinking like, again, maybe taking a little inspiration from biology,
*  there's different kinds of memories and you could imagine sort of saying, hey, what if we had a
*  couple different internal states and they were responsible for different things? Could we define
*  that or sort of enforce some not strictly predefined encoding, but could we sort of
*  incentivize different kinds of memory representations with the expectation that those will work together
*  downstream as I encounter different sorts of scenarios? I guess another way to frame that might
*  be like this idea of optimizing or a loss function or objective function or something around the
*  contents of states, because that feels important to me or it feels like something that could be
*  like very high promise. Sure. So this question of what can you do with the state or can you
*  like optimize the state and stuff? I think that that's really interesting and actually kind of
*  core to some of the more interesting use cases of state space models that could be unlocked.
*  So as we discussed for most of the rest of this, like previously, so far, I've kind of talked about
*  the state as this auxiliary thing that helps you do autoregressive inference, which is one way of
*  thinking about it. But when we've moved away from the transformer regime, which is about caching
*  what you've seen, and we've moved more to this stateful compression regime, which is what the
*  SSM has, I think that we can now start leveraging that state in really interesting ways. And things
*  include, for example, once you've what they can do is this state that kind of compresses what you've
*  seen so far, it might be a lot more interpretable in or it might be interpretable in different ways.
*  A transformer state is very easy to interpret. It's just a retrieval cache of your tokens.
*  The SSM state likely compresses the information or context in interesting ways. Maybe they get
*  disentangled in the state. If you've seen concepts like word embeddings or other forms of embeddings
*  of concepts, they end up kind of naturally being composable or representing concepts that are more
*  interpretable. I wonder if the same sort of thing could be done using SSM state. So for example,
*  one thing that we at Cartesia are kind of doing is using state as a form of encoding
*  tiles or stuff like that. Normally, if you want to encode a speaker in audio or some sort of style in
*  envision, this would be like a separate vector that you throw into your thing, an entirely
*  different module. But in the case of SSMs, if you model everything autoregressively,
*  the state of your model might just encode like, if you think of doing zero shot continuations or
*  prompting, but on different modalities, like on some speech thing or a piece of music or some video,
*  you now for free have this fixed size state that must be encoding some attributes of the prompt
*  that you've given it. And now that state is likely to be interpretable or you can maybe
*  interpolate things to blend between voices or blend between image styles and stuff like that.
*  So I think that whole thing would be a very interesting kind of line of research.
*  And you can also do things like directly try to optimize that state. In a transformer,
*  the KV cache is not something that you think of as being like an independent thing that you're
*  injecting. It's just something that was part of the transformer. Whereas in SSM, you can take any
*  initial state and think about what, like that is a complete summary of the prompt. And now you can
*  use that in maybe creative ways. For example, in like transformer based models, people might try to
*  cache previous conversations or previous part of the history by storing that KV cache. But now with
*  an SSM, you can create like a similar style flavor of this cache, but it's much, much easier to work
*  with because instead of these variable length databases, you just have these fixed size state
*  that like encoded some part of a conversation. Maybe they've encoded like speaking styles or
*  stuff like that, that you can just create a database with, play around them interesting ways.
*  And then you can maybe directly optimize on top of them. This is actually something that the RWKV
*  project has done, which is kind of like a parallel effort to SSMs that started a few years ago and
*  has also been working on recurrent models. I don't know too much about what they're up to right now,
*  but I oversaw that they've kind of tried this idea of fine tuning models on downstream tasks,
*  not by fine tuning the actual weights, but just the initial state passed into the model.
*  And so this provides like a really interesting degree of control. This maybe is very related
*  to what you're saying about optimizing directly the state. I think there's actually, this is one
*  of those things where I think that there's probably so many creative ideas that people can do to
*  leverage the states of these models that there's some of them that I'm working on right now, but
*  I think there's probably lots and lots of really interesting creative ideas with potential to use
*  them for. So I'm very excited about all of those possibilities. Cool. That's really interesting.
*  Jason's doing some of these like long sequence things. He'd probably be interested in your
*  comments around like, why does it seem to scale to 3X? And is there a path to more or what's up
*  with that? I really think the Infinii attention paper from Google seemed like a big deal. And I
*  kind of imagine that you inspired them to publish that. What's the extrapolation abilities? Works
*  have shown that they can extrapolate to like three times the context they were trained on.
*  I don't really know either. I think people have found that if you fine tune it a little bit,
*  it will extrapolate way, way longer. But I do wonder if training data is the solution. Maybe it
*  is. It's just like if you ever need to have long dependencies, you just need to train on it
*  at some point, maybe not very much. Or maybe there is a different modeling mechanism that can allow
*  models to really bake in the idea that they should be robust across very, very long dependencies.
*  But definitely I think that this is an approach that makes sense. Yeah, I think people have tried
*  similar things for Transformers and so on, but I don't know if there have been head to head
*  comparisons. But in a recent collaboration with Nvidia, we sort of found that these SSM-based
*  models do seem to extrapolate much better than Intention at least. And that's part of the whole
*  appeal of recurrence. I'm not very familiar with the Infinii Intention actually. That was like
*  relatively recent. There have been a lot of modifications to Transformers to try to extend
*  their context length. And a lot of them have the flavor of basically incorporating true recurrence,
*  maybe at the block-wise level or chunk-wise level, into the Transformer. I think a lot of those ideas
*  just need to be validated. I mean, I think they're coming from a perspective that's similar to where
*  we were coming from, which is that you really need true recurrence to get potentially infinite
*  context. The questions then become like, how do you get the model to actually learn from that context?
*  Even the oldest RNNs in principle had infinite context, but how do you actually make them learn
*  those dependencies and can actually remember that information to model them? That's the part
*  that's not trivial. A lot of that might just be empirical validation. I haven't seen compelling
*  evidence for any of these many flavors of recurrent Transformers, whether they really work at the same
*  scale. That's one of the reasons I think people were excited about Mamba, because it seemed kind
*  of the first or one of the first to really show completely alternate, completely recurrent thing
*  that was matching Intention at least on perplexity and so on. And I don't know that I've seen
*  really robust comparisons for some of these alternate flavors of recurrence.
*  I'm really excited about sequence parallelism with Mamba too. I think it's going to be a
*  game changer just for long sequence. It's just the amount, the things you can do on less hardware
*  can be great. Sequence parallelism and other algorithmic improvements, that's something also
*  I and Tree are both very excited about. And one of the whole reasons that I started this entire
*  line of work on recurrent models is that one of the examples, I talked about how I felt like
*  there's something fundamental, there's some intuition for why this is a core mechanism
*  that should matter. And one of those was just that it feels like the type of thing that should allow
*  you to get past finite context windows. And I've always been interested in infinite context.
*  And it seems like you can't really do this without some form of recurrence.
*  And here there's an important distinction between engineering improvements versus
*  fundamental model trade-offs. So in practice, what's happened is that attention has always been
*  scalable to as long as people need. Back four years ago, five years ago, when I was working on
*  long context and RNNs, no one cared about long context. And I was interested in it more from
*  fundamental capabilities perspective, because it seemed like something that models should be
*  able to do, humans can do it. Maybe we don't have the applications for it right now, but it seems
*  like it is an important part of capabilities. And at the time, no one really had long context
*  benchmarks. And then when people started caring about it, the engineering improvements have
*  scaled so well that Google Gemini is known for its 1 million plus context window and so on.
*  And sure, so they managed to get it to work. And like I said, I'm also open to the idea that
*  that's really all you need, but somehow it's still missing this. It's somehow still finite,
*  right? No matter how many engineering improvements you throw in, it's still going to be finite. And
*  that speaks to me that there is still a missing piece. And so that's one thing that I've always
*  just been interested from the perspective of here's a simple capability that we should be able to do
*  that we can't really. Just how do you have something that can have infinite context? How do you have
*  a system that can learn indefinitely and so on? I don't know that whether or not it's some sort of
*  solution, but at least there is some, one of the reasons why I was interested in them is because
*  they at least have some hope of it. In principle, recurrent models are always updating their state
*  with all of their past. And of course, as you throw more information in it, maybe that gets
*  information gets lost, but it's an approach that seems sensible. And then we start running into
*  questions with the engineering challenges as well, throwing in sequence parallelism and so on.
*  And so, yeah, so I think we're quite interested in like, how far can you actually take the scaling
*  of these models? Cool. That's really interesting. Why are you publishing all this? I think we've
*  just seen it in the last 48 hours, the second inflection like deal with adept going to Amazon.
*  And basically you can get that deal, you can demonstrate that you can train a roughly
*  competitive model. I would expect that there's like a lot of interest also in people who can
*  come up with like fundamentally new architectures, which as far as I know, like those companies
*  had not really. So I'm interested in how you're thinking about putting this work out into the
*  open as opposed to keeping it secret or one might infer that you have more secrets.
*  Why am I still publishing, I guess? Well, you know, I'm kind of an academic researcher at heart.
*  It's the world is changing really fast in the AI world, but I think why do research, why do AI is
*  a lot of it was like towards actually understanding the nature of intelligence. That's just why I was
*  always fascinated by AI since I was for a long time, just feels like this fuzzy concept that is
*  really mysterious, but really fascinating. And I would love to, for us as for humanity to understand
*  it better. I think doing academic work is important for that. Maybe there's times where I'm working on
*  that may not be released or maybe doing a delayed release, but at the end of the day,
*  there's lots of things that I think I would love to continue supporting the academic community and
*  sharing these interesting ideas. So I think that's something that matters a lot to me.
*  Cool. Do you have a two sentence on the nature of the relationship between Cartesia and together?
*  I think we're not actually like that closely related. I mean, we naturally connected because
*  me and Tree work closely together as academics and I'm at Cartesia Tree's Chief Scientist of
*  Together. We kind of do different things together is really focused on the infrastructure and
*  serving deploying models here at Cartesia. We're making bets behind SSMs. And in general,
*  we think of ourselves more research focused training models from scratch and creating better
*  models is something that we really focus on. There are natural partnerships there as well,
*  of course, but it's not tied at the hip in any way. We mostly operate completely independently.
*  Cool. Well, you've been extremely generous with your time and insight into all this stuff. And we
*  are both big fans of your work and we'll continue to watch for your upcoming product releases and
*  even with more anticipation any future papers that you'll be dropping. So for now, I will just say,
*  keep up the good work and Albert Gu, thank you for being part of the cognitive revolution.
*  Thanks a lot for having me. It's been a pleasure. It is both energizing and enlightening to hear
*  why people listen and learn what they value about the show. So please don't hesitate to reach out
*  via email at tcr at turpentine.co or you can DM me on the social media platform of your choice.

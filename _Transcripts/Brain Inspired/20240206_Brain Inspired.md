---
Date Generated: April 19, 2024
Transcription Model: whisper medium 20231117
Length: 5334s
Video Keywords: []
Video Views: 771
Video Rating: None
---

# BI 183 Dan Goodman: Neural Reckoning
**Brain Inspired:** [February 06, 2024](https://www.youtube.com/watch?v=kIM44Gnq9Qc)
*  But I also think that plasticity, brain plasticity, will continue to surprise us. We'll find
*  things that we hadn't even imagined that the brain is doing. I think I understand how
*  it would feel for like you to be working on this really important and exciting topic and
*  be making so much progress and then some neuroscientist come along and says, you should be learning
*  from what I do. But I feel like there's so many basic things that we just haven't ever
*  answered. We've had a hundred years of neuroscience and we don't know whether spike times matter
*  or not.
*  I know, it's sad. It's sad.
*  Hello Brain Inspired crew. This is Brain Inspired. I'm Paul. You may know my guest today as the
*  co-founder of NeuroMatch, the excellent online computational neuroscience academy. Or you
*  may know him as the creator of the Brian spiking neural network simulator, which is freely
*  available. I know him as a spiking neural network practitioner extraordinaire. Dan Goodman
*  runs the neural reckoning group at Imperial College London, where they use spiking neural
*  networks to figure out how biological and artificial brains reckon or compute. As you
*  likely know, almost all of the current AI that we use to do all the impressive things
*  that we do is built on artificial neural networks. Notice the word neural there. That word is
*  meant to communicate that these artificial networks do stuff the way our brains do stuff.
*  And indeed, if you take a few steps back and you maybe spin around 10 times, take a
*  few shots of whiskey and then squint really hard, there is a passing resemblance between
*  artificial networks and our brains. One thing you'll probably still notice in your drunken
*  stupor is that amongst the thousand ways that artificial networks differ from brains is
*  that they don't use action potentials or spikes. From the perspective of neuroscientists, that
*  can seem mighty curious, because for decades now, neuroscience has focused on spikes as
*  the things that make our cognition tick. We count them, we compare them between different
*  conditions during cognitive tasks. And generally, we put a lot of stock in their usefulness
*  in brains. So what does it mean that modern neural networks disregard spiking altogether?
*  Maybe spiking really isn't that important to process and transmit information as well
*  as our brains do. Or maybe spiking is one among many ways for intelligent systems to function well.
*  Anyway, on this episode, Dan shares some of what he's learned and how he thinks about spiking and
*  spiking neural networks and a host of other topics. And you can learn more about his work
*  in the show notes at braininspired.co.uk slash podcasts slash 183. And of course,
*  I linked to a few of the papers that we chat about today. As always, a huge thank you to my
*  Patreon supporters. You can learn how to support the show and get the full episodes and a few other
*  bells and whistles at the website at braininspired.co. Okay, I reckon you'll enjoy this episode. And I hope
*  you do. Here's Dan. In a world where we've already reached artificial general intelligence,
*  and we've done it without spiking neural networks, but with rate based neural networks,
*  one researcher, actually a lot of other researchers as well, is sticking to their guns and studying
*  spiking neural networks. That researcher today is Daniel Goodman. Welcome to the podcast. Thanks
*  for being here. Thank you very much for inviting me. It's very exciting to be on this. We listen
*  to it a lot. So we're talking about it in the lab. So it's nice to be on. Apologies and thank you.
*  So I haven't had someone on talking about spikes in a long time. And I thought it's overdue. And
*  you have been studying spiking neural networks since you got into neuroscience, I believe. You
*  have a mathematical background hyperbolic geometry, I believe is what you got your PhD in. And maybe
*  we can come back to that. But when you started studying neuroscience, were you immediately
*  interested in spiking neural networks? What's the background there? Why spiking neural networks?
*  Yes, I got into neuroscience after deciding that I wanted to do something other than maths. And I
*  just started reading around. And basically, I think that the thing that just popped out to me is that
*  why does the brain use this weird mechanism? Spikes are kind of a bizarre way of communicating
*  information in a way. You have these binary pulses, but that they come at very precise or
*  potentially very precise times. Yeah, what's going on there? And how do we think about modeling that?
*  It really struck me as a question that was sort of interesting, I guess, from a mathematical
*  perspective. I mean, I was coming from maths. So it seemed mathematically interesting, but it also
*  seemed like a good, just general problem. Yeah. Why did you, what made you want to venture away
*  from math? Yeah, I guess I wanted to do something that was, I wouldn't say more applied, but more
*  like rooted in the real world. I really enjoyed doing maths as an undergraduate and as a PhD
*  student. But it kind of, well, my little anecdote about this is that I wrote one paper during my
*  PhD. And I presented at a conference and about six people were interested. And I think those are the
*  six people that have ever cared about that paper in all time. So it felt like it was a slightly
*  monastic experience of experiencing the world. I wanted to do something a bit more in the world.
*  And I'd actually always been interested in, I guess, intelligence, broadly speaking. Both my
*  parents are psychologists. So my dad had me reading David Marr at like 14 years old. Wow.
*  So I guess it was kind of natural for me to somehow sort of find myself doing this. And then it was
*  really confirmed when a biologist friend of mine said, Oh, you should do neuroscience, they need
*  mathematicians. And I was like, okay. I don't know if that was true or not. But it was enough to get
*  me hooked. So I mean, it's interesting, at least to me anyway, that if you ask a physicist, right,
*  a physicist will say, Well, you know, what's the problem? I can solve it. There's this sort of
*  arrogance I might. That's maybe being unkind. But physicists think they know the right approach to
*  everything. And I'm not sure about mathematicians. What do mathematicians do they carry with them?
*  That's the same sort of arrogance?
*  Yeah, I guess so. Although, I mean, they don't venture outside of math so often as physicists,
*  perhaps. So perhaps it's not quite so flagrant.
*  Yeah. Yeah. Well, I can't I can't tell you how many conversations I've had with with fellow
*  neuroscientists, ruling the fact that we have not had more of a mathematical background and how it
*  slows us down so frequently. So that's something that you don't face.
*  No, although there's very different types of maths. Like, yeah, in many ways, a lot because a lot of
*  the maths that's done in neuroscience is done by physicists. It's a sort of mindset that is
*  actually quite different to what I did as a pure mathematician. So I
*  is it closer to applied?
*  Yeah, exactly. It's a bit more closer to it, I guess, they're close to applied. So like, for me,
*  as a as a as a pure mathematician, I rarely had to take deal with like solving a really hard
*  differential equation. Whereas that's like bread and butter for physicists. And they get really
*  good at it. I was more about I guess pure maths is somehow more about like, how much of this
*  information can we throw away and still say something generally interesting about it? It's a
*  different sort of sort of mindset. So yeah, I'm still quite like flummoxed by some of the
*  physicists stuff like, oh, what's that? That's the equation called you used to solve diffusion
*  problems. Oh, that's a nightmare.
*  Yeah, yeah, exotic. Yeah. Yeah. Well, okay. So you're reading David Maher at 14. And he's the one
*  that so many people point to in terms of how to approach studying, quote unquote, intelligence,
*  right, taking that top down approach where you figure out the behavioral computation first, and
*  then search for algorithms, and then finally look at the implementation level in the brain. But like
*  we just said that, you know, you've been spiking, studying spiking neural networks forever now,
*  what is it about spiking in general, that that turns you on scientifically? And you already said
*  that it's just a curious way you think to reckon and by the way, your group neural reckoning. I
*  actually looked up reckoning today. Do people tell you this? No. Okay, because the way that I think
*  of reckoning is like the third definition, which is a comeuppance, right? Like, you have to finally
*  pay your dues. But it really just means calculate. Yeah, yeah, exactly. That's more the sense that I
*  had in mind for it. I just didn't want it to be like the Goodman lab. I try and avoid like stuff
*  like that. Yeah. It's a cool name, especially with the definition that I had in mind also,
*  because it's it's like saying, hey, you're gonna have to reckon with these spikes eventually,
*  right? Yeah, well, I like that element as well. So then, you know, when I say what's important,
*  when I generally ask what's important about spiking, I get sort of one or one or two general
*  answers. One, computational efficiency, right? It's always up there. And I'm trying to be more and
*  more convinced that that that's a super important for intelligence reason. But the other reason is
*  just, well, that's how brains do it. So there must be something special about it. So do you fall into
*  either of those camps? Or do you have anything to add? Why you think that spiking itself might be
*  important? I agree with both of those. And I also kind of agree that there's also something
*  slightly unsatisfactory about that answer. But maybe we can come back to that. But yeah,
*  now I agree with both of those. And I think it's not just this is how the brain does it. So there
*  must be something special about it. But this is how the brain does it. So if we want to understand
*  the brain, we need to understand it. Okay, obviously, that's less important if you're
*  thinking about AI, or if you're thinking about it in some more higher level, sort of cognitive
*  frame of mind. But if you really want to understand ultimately what the brain is doing,
*  I mean, it is doing it with spikes. So we do kind of need to understand them at some point.
*  But there are levels of understanding, right? And one could argue as many of the modern deep
*  learning practitioners, modern neuroscientists who use deep learning to study the brain would
*  likely argue that, well, maybe spikes are really not that important. Because look at all the
*  functions that we can provide with these rate based models.
*  Yeah, no, I think that's right. I mean, one starting point that you always have to bear in
*  mind in this is that both spiking neural networks and rate based artificial neural networks are both
*  universal function approximators. So you're never going to find something that SNNs can do,
*  that ANNs can't do, or vice versa. You can always do it. The question is, and this actually gets to
*  the other point that you mentioned, is there one that for particular sorts of problems is much more
*  resource efficient than the other? Suppose that there's refined some tasks that you can do with
*  SNNs that you need 100,000 times more neurons to do with an ANN. Now, in a way, that's just a
*  resource constraint problem, right, of the sort that you find uninspiring.
*  Well, it's also a thought experiment. I mean, are there examples that you can think of that? I'm
*  sorry to interrupt, but...
*  Yeah, so I have to be honest and say I don't think that there are yet examples of things where SNNs
*  are definitely better. I mean, there's things I think where it's clear that that's what the brain
*  is using. Like in the sound localization circuit, we use the timing of individual spikes, and that's
*  important. And it uses properties of spiking neurons, it uses coincidence detection, for example.
*  So in terms of understanding the brain, I think there's definitely cases where spiking is important.
*  And if you do sort of like information theoretic analyses, you see that spikes timings are carrying
*  information that isn't carried by the rate. And even going one further than that, I'd say
*  the question shouldn't really be like, can you prove that the spikes are important? It's more the
*  other way around. It's like, can you prove that the spikes are not important? They're definitely
*  there. So the burden of proof should really be the other way around. But yeah, I don't think that we
*  have a really clear and obvious example of like, okay, in this computation, the spikes, we know
*  that the spikes are doing something that we couldn't easily do with ANNs. But I think part of the
*  reason for that is that we don't know how to think about the type of mathematical systems that are
*  involved in spiking. So ANNs, it's linear algebra, it's calculus. We've been thinking about that for
*  hundreds of years. We have amazing mathematical tools for thinking about that. Spikes are weird.
*  They're sort of discrete, and discrete systems tend to be more difficult than continuous systems
*  in any case. And they're sort of continuous as well. And so that's almost like the worst of both
*  worlds in terms of our understanding. We can't really apply our discrete systems thinking,
*  and we can't really apply our continuous systems thinking. So what do we do? And I think
*  part of what happens is that we end up looking at the problems that our tools can do.
*  So we have ANNs that are very like, for example, I think it's not surprising that
*  static image recognition was one of the earliest success stories of ANNs because time doesn't
*  matter. And those tools are really good for dealing with things where time doesn't matter.
*  As we start to get more and more interested in things where time does matter, I think maybe
*  this is a hypothesis, right? I don't have a proof for you here. We don't yet have the example where
*  spikes do better. But maybe we'll start to see cases where, if not spikes, something a bit more
*  like spikes, something with some element of both time and space built into it starts to become
*  interesting. And I think maybe, I don't know if this is true or not, but maybe we're already
*  starting to see that, for example, like thinking about self-driving cars. That's somehow quite
*  different from a lot of the early success in that you're not presented with an image and like,
*  here is an answerable question. What is this a picture of? Like one feed forward run, bam,
*  you know what the picture is. It's like, here's a continuous stream of information. At any moment,
*  some tiny feature in the corner might become present that becomes critically important,
*  right? Like the child's football flying out between two cars or something like that.
*  And I think one of the reasons we're not making such fast progress on things like self-driving
*  cars, as was hoped for, is that that tool is not so good for that problem. Obviously, we don't have
*  a spike in your network that can do that either. But yeah, again, that I think is because we don't
*  yet have the same quality of mathematical tools, the same vocabulary or frameworks for thinking
*  about that. But so then going back to the efficiency question, I mean, timing and efficiency
*  are sort of wrapped up with each other, I suppose. Is this where you think that efficiency
*  becomes important is because of the timing element?
*  I think there's two different elements. One of the reasons why the neurons, the spiking neurons,
*  are efficient is because they're not continuously communicating. They only have these bursts of
*  information. And obviously, that's something that happens in time. But I think that there's also
*  just an element of processing continuously varying signals, I guess. So we can use ANNs to
*  recognize sounds, for example. But very often, those frameworks are not taking, as it were,
*  like we are, a stream of samples over time, something like that. They're doing a free
*  analysis and they're treating it as an image, essentially. So they're turning this time
*  varying problem into a static image problem, because we've got a tool for doing static image
*  problems. And amazingly, it does really well. But it's not, I think, what our brains are doing. And
*  it's not necessarily the right tool for that task. I don't know if that answers your question.
*  Yeah, no, I just I want to think of efficiency as a important for intelligence computational
*  principle. But it sure feels like with computing speed and power these days, we can just brute
*  force our way there. And I'm not sure that efficiency is all that important. But I want
*  to be convinced of it. Yeah, I actually kind of think that we are maybe getting close to the
*  point where efficiency is starting to be a limiting factor, even people have been saying that. I'm
*  sorry to interrupt. No, no, that I mean, it's true. It's true. People have been saying that for a long
*  time. But I saw an analysis, I can't remember who did this. But basically saying that if you look at
*  the amount of energy that needs to be put in to get an improvement on various like test scores,
*  in like ML benchmarks, like you're getting a doubling of energy for like a halving of the
*  improvement over time, right. So at some point, that does have to cap out. We can't keep doubling
*  energy to get, you know, a quarter of a percent better on the benchmark, and then an eighth of a
*  percent better, and then like, whatever, right. Right. And also, I think that there's an increasing
*  interest in being able to do stuff that doesn't require sending your data to a central server,
*  which then runs it on some massive, you know, computational thing and then sends the answer
*  back. So for example, like that's not ideal for self-driving cars, because you have latency
*  issues, right. If you need to make a quick decision, you don't want to have to send it back,
*  send the data to a server and get a response back. Obviously, that's also critical for sort
*  of animals in the wild, but that's a separate issue. Right. That's perhaps also one of the
*  things that gets people interested in neuromorphic computing, right. Like the promise of that.
*  So I think that there might be a limit. I think we're probably, we haven't reached it yet,
*  but like last, I think it was last week, there was an announcement of, I think it was Facebook
*  wants to buy 350,000 of these mega H100 GPUs and various like analyses of how much carbon
*  those would be dumping into the environment. And I think OpenAI had a similar sort of announcement
*  that they want to sort of like solve the energy problem in order to make further progress. So I
*  think, you know, it is becoming an issue. We may not have quite tapped out the approach yet. Yeah.
*  I mean, I think it's important, but I mean, maybe more than that is that there might be like a huge
*  leap if you could, if instead of just like a small improvement of energy efficiency, you could get
*  like a massive leap in energy efficiency. Maybe you can then bypass that like poor scaling where
*  energy is doubling and performance is halving and yeah, get some sort of, I don't know,
*  more linear scaling or who knows, right. But there could be all sorts of interesting things going on
*  there. So your bet, what I wanted to ask you is whether you've ever been tempted to abandon
*  the study of spiking neural networks in favor of these rate-based models that have been
*  performing so well. And I know offline you mentioned to me that you maybe weren't
*  initially as excited about using machine learning approaches to study brains and cognition, but that
*  you've come around to them. So maybe you could elaborate on that as well. Yeah. I might have
*  been thinking, I mean, so I went to NeurIPS in 2009, something like that. I didn't know anything
*  about machine learning at that time. And it was already like, it was gearing up. It wasn't quite
*  as, you know, it wasn't as big as it was now, but it was gearing up. And I remember coming back from
*  that conference and my supervisor said, okay, what do you think of all this machine learning stuff?
*  And I was like, it just seems to be something for selling adverts as far as I can tell.
*  Which is true. And I still kind of hold on to that, but I do feel like I really missed a big
*  opportunity there to realize that something important was happening. I think definitely
*  something important is happening, right? Like the effect of machine learning on neuroscience,
*  I think, is a good thing. I'm not one of the sort of like anti-machine learning,
*  but I'm also skeptical about certain elements of it. Sorry, what was the question? I feel like I'm
*  getting sidetracked here. What was the question originally, and then I immediately switched it
*  because I'm a terrible host, was whether you've ever been tempted to jump ship from spiking
*  neural networks. Yeah. So actually, I mean, I was kind of, I think I was kind of on that, on the way
*  to that until I read about this new development in training spiking neural networks, surrogate
*  gradient descent. So this is this idea from Friedman-Zenker and Emre Nefci, which is basically
*  an idea from taking the algorithms from machine learning, but with a clever trick, allowing you
*  to train spiking neural networks, which normally, which were really hard to, I mean, there was a
*  technical reason why training spiking neural networks using those algorithms is hard, which
*  is that they're not differentiable and all of those methods require differentiability.
*  Anyway, so I read about that and I tried it out and it just works amazingly. It's like magic.
*  Well, there have been multiple approaches to training spiking neural networks in the past,
*  so why this one in particular? It just was a step beyond?
*  Yeah, it just, I mean, it just works, right? So in the old days, we used to train things with
*  STDP and we could kind of get spike time independent plasticity. We could kind of get some interesting
*  results from that. But it never got us, like right from the beginning, I thought like if we,
*  of my time in neuroscience, I thought if we want to study the brain, we have to study it in the
*  environment in which it's doing its thing, right? Like it deals with high dimensional complicated
*  noisy signals. You know, it's got a really hard task. That's why intelligence is interesting
*  because it's solving a really hard task. But we study these incredibly simple sort of laboratory
*  stimuli where everything is perfectly controlled. And it was hard enough even to get STDP to work
*  in those like highly simplified scenarios. And then, you know, machine learning comes along,
*  sorry, gradient descent comes along. And it just like, oh, you want to recognize an image? Okay,
*  just give us some images. Bam, it just learns to do it. Recognize some sounds? Bam, it just learns
*  to do it. And so suddenly we can do the thing that I always wanted to do, which is have these
*  spiking neural networks that are solving like interesting real world problems. Of course,
*  now the problem has shifted in my mind to how do we understand what those networks that we've
*  trained are doing and say something interesting about them. And I'm still thinking about that.
*  But at least we can now do the thing that I always wanted to do. So that's for me what was a big
*  change. So that's one of the areas that it doesn't bother you that it is not biologically accurate
*  because surrogate gradient descent, and please correct me, my description, basically does a
*  forward pass with spikes, and then emulates the back propagation algorithm, which is not biologically
*  plausible. But it does that by replacing the unit spike with like a sigmoid, right? Or like
*  something that's differentiable. And so it doesn't bother you at all that that's essentially what
*  all other rate based networks do in terms of training the network, but it's not not how brains
*  do it. There is one thing that bothers me, which is I don't understand why that trick works.
*  And as far as I know, I keep asking Friedemann about this every time I talk to him. Like none
*  of us really know. I mean, we have some sort of vague intuitions, but we haven't really solid
*  answers to why this trick should work, which means we also don't know in what cases it doesn't work.
*  Right? If we knew why, if we had a solid answer to why it would work, we could say, okay, well,
*  it'll train to do these sorts of things, but it won't be able to train to do these sorts of things.
*  I would feel more satisfied if I had that answer. But I don't feel too upset that it's not learning
*  in the same way that biology is learning. Because what I want to do with it is not come up with a
*  model of plasticity, but find out what functions spiking neural networks are capable of. And for
*  that, I don't really care. It's just an optimizer for me. And so then going back to the machine
*  learning approach, one of the reasons that you're more on board with it now is because you can use
*  more complicated tasks, right? Ask your networks to solve more complicated,
*  more ecologically valid. Would that be a way to say it as well?
*  Definitely. Yeah. Yeah. And I think what sorts of interesting things come out of that, like
*  things that are optimal for very simplified problems are not necessarily the same things
*  as are optimal when things get messy. So yeah. Part of what you do is come up with a more complicated
*  task for your networks to perform. Because when you train them on these fairly simple tasks,
*  you realize, well, they don't actually need these features, right? The networks don't need
*  these particular features to solve the task and we can do it fairly straightforward. So part of
*  what you do is just make more complicated tasks and figure out, well, when does it kind of break
*  those simpler models and when do we need the more complicated models? So I guess my question is,
*  originally what I was going to say is all of our problems are messy and require these more
*  complicated computational tricks, but maybe that's not true. Maybe most of what we do is
*  actually kind of simple and it's not necessary. I mean, I think right from the beginning, we have
*  a very complicated sensory world to decipher, right? There's a lot of noise.
*  As I'm here recording, I can hear in the background the lift shaft behind me, the people
*  talking out in the corridor, and I hope not too much of that is coming through on this microphone.
*  And I'm filtering all of that out. That's really quite hard. And just going back to our idea,
*  I think that's something that still machine learning is not terribly good at actually,
*  is extracting the background noise and understanding speech.
*  The cocktail problem.
*  Yeah, the cocktail party problem, exactly. But yeah, sorry, that was a distraction.
*  So I think we're always dealing with quite complicated problems
*  in terms of the inputs that humans are interested in. Just thinking again about
*  the visual field. That's an awful lot of data, most of which we're throwing away,
*  but we don't know which bits to throw away. That's already quite a hard problem, right?
*  And yeah, I think we're always doing, I guess our brains wouldn't be so big if we weren't always
*  solving quite hard problems.
*  So going back to the surrogate gradient descent that got you all excited about
*  sticking with spiking neural networks. First of all, how close were you to jumping ship?
*  It's not so much I was thinking of jumping ship, it's just that I was finding myself
*  thinking more and more about solving problems, not using spiking neural networks, I guess.
*  Yeah, I don't think I was fully planning to jump ship. It was just that my interests
*  were starting to drift off in various different directions. And then the surrogate gradient descent
*  really has refocused me, I guess, on thinking that's really interesting and worth following up on.
*  Does the rest of the, do your cohorts also love the surrogate gradient descent? I mean,
*  because there are so many different other solutions that have been proposed.
*  Yeah, I mean, there's a whole family of things that are similar to some surrogate gradient descent,
*  but there's definitely been a sort of leap at around about that time. So surrogate gradient
*  descent isn't the only one. There's other approaches. For example, so Tim Mascherriere
*  came up with a really interesting approach to treating the neural networks as if they had just
*  one spike, and then using this time of that spike as a continuous variable. So that was another trick
*  for doing it. And then there's other groups that have sort of taken a slightly sort of hybrid
*  approach to that. And yeah, so there's various similar things that are somehow in the air.
*  My impression is that surrogate gradient descent, at least from what I've seen,
*  works the best. Now that's probably going to be controversial. Probably people will tell me that
*  in our tests, R1 works the best. That's just my feeling. I think it's good for everyone to do
*  their own thing. But yeah, I mean, I think in the world of people who are interested in spiking
*  neural networks, it's really taken that field by storm quite a lot. Yeah.
*  But you don't think that having an algorithm like surrogate gradient descent that is really
*  good at training networks, you don't think that that gives us any purchase onto how brains are
*  learning, just how they're performing the tasks once they've learned.
*  Yeah, that's a really interesting question. It doesn't have to. Logically, it could be
*  entirely separate. I think it is probably quite an interesting starting point if you're also
*  interested in plasticity. Okay. So I mean, you can't directly apply surrogate gradient descent for
*  a well-known reason, which is that it uses global information that wouldn't be available to an
*  individual neuron, right? It's the same for just using any sort of gradient descent as a model of
*  plasticity. It uses information that the neuron can't know. And then there's a whole sort of slew of
*  work that says, okay, well, can we approximate what gradient descent is doing with a local rule?
*  And actually already that can generate a lot of the sort of plasticity rules that people have
*  studied in the past in neuroscience. This is a generating idea that can sort of
*  backwardly explain a bunch of stuff that we did previously.
*  I think that's also a really interesting approach going forward as well, I think, by studying how
*  we could do gradient descent biologically. It's likely we'll come up with good ideas.
*  But I also think that brain plasticity will surprise us, will continue to surprise us.
*  We'll find things that we hadn't even imagined that the brain is doing. There was that
*  paper, I can't remember, sometime in the last few years, that showed that neurons were exchanging
*  little packets of RNA. They were sending messages to each other in little, you know, like encapsulated
*  packets of RNA. We don't know what that's doing. We know that that's happening. Maybe that's
*  something to do with learning. Who knows, right? And if that's something to do with learning,
*  then anything is possible, right? Because we're sending arbitrarily complex message from neuron
*  to neuron. And I wouldn't be surprised if more things like that sort of show up in the future.
*  So yeah, I don't think we should be too constrained by a specific idea of like
*  learning must happen at the synapse and anything that the synapse can't see must be irrelevant.
*  Yeah, I mean, I repeat myself ad nauseum about this, but the more I learn about brains,
*  the more confounding it seems because there are just so many different possibilities, right? So
*  we've lived since, let's say Donald Hebb and the neurons that fire together, wire together paradigm
*  of learning. And that might just be one of, I don't know, 20 different ways, which is, I'm not sure if
*  in some sense, that's exciting. And in another sense, it's daunting. I don't know how you feel
*  about that. Yeah, both. But I think more exciting, right? I mean, one of the reasons they came into
*  neuroscience, I think, is because I like the idea of this, everything is still to play for.
*  Unlike maths, where we've got thousands of years of history and all the big questions are kind of
*  already solved to some extent. Like everything is kind of unknown in neuroscience. We don't really
*  know how the brain is working very much at all. We know lots of little bits. And I think neuroscience
*  is actually in a really exciting time for that at the moment. There have been some really cool
*  discoveries and things you've talked about on the show before, like representational drift, for example,
*  or there's a surprising amount of synaptic turnover that exists in the brain. We have this idea that
*  memories are encoded in sort of static weights that once learned basically never change. That's
*  a classical way, but it looks like that doesn't really happen anymore. So that completely messes
*  with our way of thinking about what neural networks might be doing. And so I think that's
*  great. I mean, I love that. I don't have the answers to those questions, but it's really fun
*  to have things that completely challenge our really basic conceptions of what's going on in the brain.
*  Oh, and finding out that maybe astrocytes are much more important than we ever thought.
*  I was going to ask you about astrocytes.
*  I also don't really know how to think about that. That's another... So I think it's really good to
*  be really open-minded about what might be important. Because if we go in with too fixed an idea,
*  learning must happen here and it must have this sort of shape. We're not going to find answers.
*  We have to be more open-minded if we're going to get those answers.
*  So this is a two-pronged question, then. But maybe now is the right time to ask it or them.
*  I agree that we know... It pains me to say this, but there's... Let's say it this way. This is
*  more optimistic. There's still lots to learn about the brain. I was going to say that we know very
*  little. I'll say there's lots to learn. You're more diplomatic than me.
*  Trying. I'm trying. So I have a current project where it's hugely exploratory right now as well,
*  because we don't know some fundamental assumptions and it just hasn't been explored very much.
*  There's not much theory to go on in that case. How much do you lean on theory? How much do you
*  think that we need theory versus how much should we be just exploring? Because of...
*  We'll talk about some of your work that explores some hyperparameters and stuff. But because
*  it just seems so high dimensional, the way that the brain can solve things,
*  is it just a matter of exploring and, for lack of a better term, stamp collecting for a long time
*  while our theories get shaped? Or do we need to go in with a theory first approach?
*  That's a really hard question. I think we kind of have to explore both ways of doing things.
*  That's always going to be my answer. I kind of feel like in all cases in a sense, we just need
*  to be trying out a lot of different stuff because we can't know in advance what is going to work and
*  what isn't going to work. And everyone just has to make their own bet about that. I think it's really...
*  The back and forth between those two approaches is what generates a lot of interesting ideas.
*  If we're talking about experiment versus theory, for example, that discovery of synaptic turnover,
*  that raises a lot of questions about what our theories were before. You didn't need to go into
*  finding that there was this synaptic turnover with a theory. You can just observe that and say it,
*  and then everyone's like, oh, what do we do about that? But also I think, and this is something
*  maybe we could do more of, we could say, here's a thing that would make sense for the brain to
*  be doing as a theoretical perspective. Can we do better at probing that with experiments?
*  I think we do that direction, I would say less well than the other direction. But when you said
*  theory, do you mean theory versus experiment or sort of like
*  theory as in mathematical theory versus simulations or something like that?
*  Well, I meant more along the lines of a David Maher kind of computation
*  approach. So the brain is doing X. Or let's say like plasticity. So we could come in and say,
*  the brain has to change synapses so that they're the perfect weights.
*  And then when we start looking and we see that, oh, these weights are
*  constantly undergoing turnover, they're never the same, it's a much more dynamic process.
*  So what does that do to our theory? Do we stick to the theory and say, well, it has to be,
*  there has to be some level of static, connective strength, right? Because that's what our theory
*  says needs to happen. But that doesn't exist. So then where do we go from there? Right? So
*  an alternative approach is to measure these things, to stamp collect and say, well, how much is it
*  turning over? And then build your theory from there. Yeah. Yeah. And again, like, sorry, if this is
*  boring, but I think we just have to do, we have to do both. Right. And you see this in response to
*  this thing about synaptic turnover, right? Like the first responses from the theory community to
*  that were, okay, but maybe there's something that's still invariant. Right. So and then we'll switch
*  to thinking about that thing that's invariant. And maybe that's true. But maybe there's a more
*  interesting answer. But whatever that more interesting answer would be is probably something
*  that's harder to come by. And I think, well, going back to possibly something I said earlier,
*  we kind of have this static way of analyzing things. We have this mathematical frameworks
*  that are good for that. And we're less good at dynamical thinking in some sense. I mean,
*  we have dynamical systems, but it's not exactly what I mean, dynamical system, because that's
*  also in a weird way, a sort of a static thing. So it's all states, spaces, state, which is static.
*  Yeah. What would be that? What will be beyond dynamical systems? I mean, I have impartial to
*  a process philosophy based approach, but I struggle mightily to think about how to apply
*  it practically in this in, you know, in experimental settings. Yeah. I mean, it's super
*  hard. And yeah, we don't have the existing mathematical tools to do it, I think. Is that
*  the barrier, you think? For me, that's one of the big barriers. I just don't know how to theorize
*  about this in a satisfactory way with maths. And because I'm originally a mathematician,
*  it always comes back to maths for me. Like, basically, I'll have understood something once
*  I can turn it into a mathematical way of thinking about it, which isn't true for everyone. Yeah. I
*  mean, I guess some of what I'm doing in my work is trying to come up with simple enough that I
*  can make progress on them, cases where that slightly more dynamical way of thinking about things
*  makes sense. And then I'm sort of hoping, I guess, that somehow by looking at lots of these
*  sort of examples, something will jump out at me, which I can't say that it has yet.
*  Okay. But yeah, so anyway, I'm almost doing fishing experiments in the
*  pool of possible computational simulation experiments or something like that.
*  Yeah. Maybe this is a good time to talk about heterogeneity in time constants, right? So is
*  this one of those cases where you... I don't know how you decided to test that in particular
*  among all the different kinds of hyperparameters that you could have tested, but can you explain
*  kind of what you did and what you learned from it and maybe why you did it? Yeah. So this is a paper
*  that came out a couple of years ago where basically we showed that... Well, in a lot of work on spiking
*  neural networks, not all work, but quite a lot, people would say, okay, here's the neuron model.
*  It's got these parameters and we're going to see what happens when we sort of train the weights
*  to do various tasks or something like that. And actually that project just came out with me saying,
*  well, look, this gradient descent thing is we can just make those neuron parameters trainable as
*  well, right? In fact, it was a one-line change to the code to make those parameters trainable
*  versus not trainable. It was as easy as that in a way. What happens when we do that?
*  And what we found was that if we made the time constants, which the reason why we pick time
*  constants actually is we looked at other stuff as well, is just that for a very simple leaky
*  integrated phi neuron, there's not so many parameters that are actually in there. Time
*  constant is one of the main ones. To define time constant just to be thorough. Right. So time
*  constant is basically how, for a leaky integrated phi neuron at least, it's how quickly the neuron
*  forgets its previous inputs. So if it's got a very short time constant, the only thing that matters
*  to the neuron is the most recent few spikes or the spikes that have arrived. Let's say it's the
*  time window that it remembers over. Right. So if you've got a one millisecond time constant,
*  only the spikes that have arrived in the last couple of milliseconds will matter.
*  Anything that arrived before that will have been forgotten. As a time constant of 100 milliseconds,
*  it's all of the things that happened in the 100 milliseconds before that matter.
*  When I say it like that, you might think, okay, well, why shouldn't you always have it be longer?
*  Well, also the timing doesn't matter so much within that window. Right. So if your time constant is
*  one millisecond, because it's only things that happened in the last millisecond or few milliseconds
*  that matter, timing is now very important because all of those things have to happen simultaneously.
*  So it's a coincidence detection. If it's like 100 milliseconds, it's basically just how many
*  spikes have come in recently. So it's switched from being a more temporal to a more sort of integrating
*  neuron. Right. So what we found was basically we tested it on a whole bunch of different tasks
*  and the tasks varied in how much temporal structure they had in them. So at one end,
*  they were just like static images essentially. So there's no temporal structure to them. We can
*  do that with spiking neurons, but we're not really in a sense getting anything that we couldn't do
*  with an artificial neural network. At the other end, we were looking at sounds, which have a lot
*  of temporal structure in them. And basically what we found is that the more temporal structure you
*  had, the more you got an improvement from allowing this heterogeneity in the time constants.
*  And the gain could be quite dramatic for those most temporally complex tasks. So that essentially
*  by adding in that heterogeneity, you got as much increase in performance as you would get from
*  multiplying by 10, the number of neurons are a hundred or something like that in the network.
*  So if you hadn't got that heterogeneity, you'd need 10 or a hundred times as many neurons.
*  So that was one part. And then we also found that after training, if you just took a histogram of
*  the time constants as found, they had a very sort of characteristic shape that when you look in real
*  data, you also see the same characteristic shape. So that was also kind of interesting.
*  One of the points that I've read or heard you make is that this is essentially a free,
*  inner-dedically free way for brains to be more robust and to learn better,
*  because it doesn't cost anything to build in that heterogeneity.
*  Yeah. In fact, it's even further than that, which is that it may actually
*  cost us to not be heterogeneous, right? To have everything be exactly the same might be more
*  expensive for the brain than to have everything be variable. And you also see that in neuromorphic
*  computing. I don't know if you want to talk about that now or later, but in some forms of
*  neuromorphic computing devices, there's sort of like noise in the manufacturing process. So that
*  the equivalence neural properties, it would be really hard to get them all exactly the same
*  or expensive or whatever to have every property be exactly the same. So having them all be
*  a bit noisy and spread out is actually more the default thing. And therefore, again,
*  in neuromorphic computing, it may actually be energetically cheaper to have heterogeneity than
*  not to. Or alternatively, it may be that you just have to live with that if you want
*  to implement things in brains or in neuromorphic computing devices.
*  You don't have any idea, sorry, this isn't a side, but whether that heterogeneity is a species
*  dependent thing, right? So like maybe lizards don't have much heterogeneity, they only have
*  really low time constants. I'm sorry if this is a naive question.
*  So I use data from the Allen Institute, which has this unbelievably amazing database that they
*  just make freely available to everyone. And it was in there across several different species.
*  Okay.
*  So like it was there in humans, it was there in primates, it was there in
*  the cats, I can't remember. There were a number of mice, maybe. There were a number of species in
*  that database, and it was there in all of them. But also, I mean, I think I would, and I know
*  that you've also, you've had Yves Marder on and talked about the STG and the fact that in those
*  circuits, those neuron parameters vary by orders of magnitude from crab to crab, right? So it seems
*  to me that it's likely that that heterogeneity is probably everywhere. Although I mean, I'm not an
*  expert on, maybe in C. elegans things are cleaner, but I sort of...
*  I was going to ask about C. elegans next, but I'm sure it's actually known in C. elegans.
*  But the reason why...
*  It's so much said in there, I just don't know.
*  Yeah, me either. I think the reason why I was asking that is because it dawned on me that
*  evolutionarily, perhaps it's not energetically favorable. It's not free, although the way to
*  build in heterogeneity, although the way you said it earlier, that it actually costs more to not
*  have the heterogeneity, maybe that's the better way to look at it evolutionarily as well.
*  Yeah, I feel like I'm not enough of a sort of geneticist or a developmental biologist
*  to answer that question. I think that would be a really interesting question to know the answer to.
*  Is it more expensive to have all the neurons being the same or is it more expensive to have them all
*  be different? I just don't know. But I think it may be the case that it's more expensive to
*  have everything be the same. In a way, you need to have some sort of quality control mechanism that
*  forced them to be the same, right? Right, which is impossible.
*  That's right. Well, I think if it mattered that they had some precise value, then we'd probably,
*  evolution would have found a mechanism to make sure it had that precise value.
*  But if it doesn't matter either way, then you would expect that part of the state space to
*  be explored in some species, I suppose. That's true. Yeah. So there might be
*  somewhere it's more heterogeneous than others. Yeah.
*  So, okay, so this is like one hyperparameter. We were just talking about how complicated
*  brains are, how messy they are, how there are so many different hyperparameters that you could
*  play with. And you just mentioned Eve Marder and her classic work on showing that
*  there's lots of different ways to do the same thing. And there's one way to do multiple things.
*  Going back to the idea of like theoretical approaches, part of your tagline on your
*  website is that you're looking for unifying perspectives, unifying approaches. But then
*  it seems like the more we discover, the less unifying it actually is. Because as you fish,
*  you catch a bunch of different kinds of fish. And this fish that we were just talking about
*  are these time constants, right? But that's just one of many hyperparameters that's like
*  constantly overturning and constantly changing in this dynamic, highly recurrent, etc., etc. brain.
*  I mean, do we need like a theoretical approach for sort of each question, right? Do we need a
*  theoretical approach for time constants? Is that going to be its own thing? Or what I'm, you know,
*  I'm not saying a unifying theory of the brain. But then the alternative to that is to have
*  10,000 theories of the 10,000 processes happening in brains. So where do you fall in thinking about
*  that? It's certainly a possibility that that won't be a unifying idea. But I think it's
*  always more interesting to look for them. And so for example, like one of the things that we
*  looked at, and we didn't find an answer to this, is we wanted to try and find a mathematical
*  explanation for why this heterogeneity had these properties that it did. And I think we had some
*  intuitions. For example, there's some stuff from sort of like random network theory in machine
*  learning that basically says that you kind of, like having some randomness in the structure
*  can often be beneficial. And I think that they also don't fully understand exactly what's going
*  on there. But again, it's been demonstrated in multiple cases. And like maybe what was going
*  on is somehow the same, right? Like if everything is the same versus there being some sort of like
*  random structure to it, something about robustness may fall out of that. Like I'm being very vague
*  here because we didn't manage to pin this down exactly. But it feels to me like there could
*  be an explanation of what was going on that could both explain why is that these random matrices
*  have interesting structuring and also explains why is that having heterogeneity in your own
*  properties is valuable. I could imagine a theoretical explanation that does cover all
*  of those cases, even if I don't quite have it yet. So I think that there can be those unifying
*  principles, but they're hard to get out.
*  Would you not be satisfied with a non-mathematical explanation?
*  Because randomness, right? I mean, I guess you randomness is mathematical, but yeah.
*  Maybe it's because I'm a mathematician. But for me, like,
*  I guess my bias is like, what it is to understand it is to be able to reduce it to maybe not like
*  necessarily a simple equation, right? But something that I, if it's understandable and
*  it's a quantifiable thing, I feel like that's what maths is to me in some sense. It's putting
*  that understanding on there. So for me, it kind of would be that. But maybe that's just because
*  I have such a strong mathematician bias that I can't imagine any other sort of understanding
*  that makes sense.
*  Let's talk about sparsity. So sorry if this is kind of a leap, but sparsity is on my mind a lot
*  these days. And you had mentioned to me that you have begun to think of it as an important
*  principle of brain reckoning. I'm going to start using reckoning all the time now, by the way.
*  Thank you for that. Yeah. The reason why it's on my mind is because I'm recording neurons in like
*  mouse motor cortex and basal ganglia. And these are like really low firing neurons. So they have
*  a sparsity to them and it's has been difficult to get a purchase on how they're encoding ongoing
*  behaviours because there's just not as nearly as much structure there as there is in like, let's
*  say, non-human primate motor cortex or different areas while they're performing tasks. Why do you
*  think sparsity, why have you come to think, I suppose, over time that sparsity might be an
*  underlying important principle?
*  Yeah. Well, I mean, sparsity is one description of spikes, right? That's temporal sparsity.
*  They're just these messages that occur infrequently in time. And you also have sparsity
*  in space. And you have a lot of that in the brain, right? You've got N neurons, you certainly don't
*  have N squared synapses connecting all of those. That would be way too many. So we have to have a
*  much sparser set of connectivity. So I guess the reason I think that there might be something
*  unifying those two is that we've just seen a lot of cases where putting things through a bottleneck
*  can have really valuable computational properties. So like in machine learning,
*  for example, you've got autoencoders, right? You take a high dimensional thing, you squeeze it down
*  through a few layers into something low dimensional, and then you squeeze it back out again.
*  And that autoencoder network often has a lot of interesting things going on in it. Basically,
*  it forces you to throw away information that isn't so relevant, so it has a compression factor.
*  And it often discovers structure in that much lower dimensional representation. So I think
*  that there's an interesting computational properties. And then there's also this famous
*  information bottleneck principle, right? Which is a way of sort of analyzing. So the way I think
*  about it, I don't know if this is a way everyone thinks about it, is for me, it somehow defines
*  what a computation is. I think in neuroscience, we often have this idea of representations of
*  something else, right? So like the retinal code is a representation of the visual image, for example.
*  And then quite often you have further transformations that somehow have this
*  representation of quality. You can reconstruct the input from the output. But ultimately,
*  I think what the brain has to do is it has to start throwing away information. It has to say,
*  this is the information that matters, and I want to throw everything else away.
*  And for me, that's what makes a computation interesting in some sense, right? That you've
*  thrown away irrelevant information. And that's kind of what the information bottleneck principle
*  tries to encode. It's like, what is the sort of the transformation that maximizes the information
*  about the thing that I care about and minimizes the information about everything else? And I
*  find that a really powerful sort of mathematical framework for thinking about the sorts of
*  computations that I would expect. Particularly, I think the sort of early perceptual systems,
*  like early visual system, early auditory system would be doing. They would be like,
*  our main job at the start is to keep the relevant stuff and throw everything else away because
*  there's too much data. Back to efficiency. Back to efficiency, indeed. Yeah.
*  So, right, exactly. So that's why I guess I think that those two questions of efficiency and
*  what the interesting computation is aren't entirely disconnected. Because it seems like
*  you could think about this bottleneck as being about efficiency, but they also seem to be actually
*  about being able to do the task well at all. Like throwing away irrelevant stuff. Ultimately,
*  you've got to do that if you do the task. So, yeah, that's somehow.
*  It's not have to. I don't think that you have to, right? Because let's say in an autoencoder,
*  there's a bottleneck, right? But then in an autoencoder, you're reconstructing, often,
*  you're reconstructing the original signal. And so that means that there is information gain after
*  the bottleneck that has been learned, right? So the system has learned to just take the,
*  low dimensional representation and then fan it back out. But that information is encoded in
*  the connections of that network. So in that sense, you're not really losing information if you can
*  just regain it. So in an information theoretic perspective, you can only ever lose information.
*  You can't gain information. So no, you're not gaining information when you reconstruct.
*  Although maybe it kind of looks like it. It's just that you're, I guess, highlighting
*  information that was already there by reconstructing the original image, for example.
*  Reconstruct. Okay. So I know like in Shannon, we don't have to go down this road, but in Shannon
*  information, then yeah, you're not gaining information. But because you have a structure
*  that does transform the signal back into a different high dimensional state or whatever,
*  one could say maybe non-Shannon informationally that information is built into the structure.
*  And we don't have to talk about meaning versus information, but yeah. So I guess technically,
*  you're right. Yeah. Well, I mean, you could think of the autoencoder as just being a way to train,
*  to do the encode bit. You don't have to do the decode bit afterwards, right? You could work with
*  the encoded thing. So the fact that you decode is there in order to make sure that you're not
*  throwing away relevant information. Right. And to your point, in terms of needing
*  eventually to perform the task, I mean, there's this, you know, in the past decade or two,
*  15 years, maybe there's all this work on motor cortex, motor brain activity being on this low
*  dimensional manifold. And this is where like the dynamical systems approach has really shown
*  S-H-O-N-E is that once you're performing the behavior, it's actually quite a low dimensional
*  representation, if you will. Yeah. Although I think that there is still some open questions about
*  to what extent that's just because the task that we're asking them to do is low dimensional. But
*  let's not get into that. No, no, that's like my current research world right now. It's actually
*  kind of frustrating. I need your theoretical abilities and your mathematical abilities to
*  help me. Yeah. So sparsity, did we wrap up enough on sparsity?
*  Yeah, I guess so. I mean, yeah, for me, I think it's just, it's tied up in this idea of bottlenecks
*  being important. And it gets at this thing that I would like to get at, which is that there may be
*  something interesting, both in spikes and in sort of sparse connectivity structures,
*  more generally, that is more than just about resource efficiency.
*  How do you get at that? How do you design that? I guess not experiment because you're not an
*  experimentalist, but how do you move forward with that? I'm genuinely curious.
*  Well, one of the things that we've been doing with one of my PhD students recently is trying
*  to understand to what extent just having sparsity in a network causes the different elements of that
*  network to learn different functions. So that's modularity basically, functional specialisation.
*  And what we found is it has to be incredibly sparse to automatically learn different functions.
*  Now there's other ways you can get specialisation. There's learning rules that can encourage it to
*  be specialised. There's training regimes that can create specialisation. There's all sorts of other
*  things. And we're not saying that that's the only route to specialisation, but this was my first
*  attempt to try and start to think about does that sparsity on its own have interesting
*  implications for the types of computations the networks can learn, for example. And in that case,
*  it looks like sparsity on its own wasn't quite enough. But what we did find was that sparsity
*  combined with other forms of resource constraint did create quite robust specialisation. So if you
*  had tons and tons of neurons, it didn't need to learn to separate functions into modules. If you
*  really cut down the number of neurons to the absolute bare minimum, then it did. Or you could
*  put other types of resource constraint on it. So that's one way that I'm trying to get at that.
*  Yeah, I mean, so that's an interesting thing, because you kind of have to keep everything else
*  still while you change sparsity, right? Which is not the way that that brains work. So it's almost
*  a cheat. Yeah, no, it was nightmarishly difficult to isolate just sparsity and keep everything else
*  relatively controlled. And when you look at that paper, there's I think there's a bunch of
*  slightly odd choices. And those odd choices are because we were really trying to control everything.
*  But that was really hard. And I think that there is an open question about how much we learn given
*  that we had to do so many odd choices and control so many things. But that's what we were trying to
*  get at was just like, just isolating this the effect of this one key like or where you also
*  introduce resource constraints as well. Right? So there's several few variables and have them
*  all be precisely controlled. Yeah. So this would be a good time to ask you then,
*  what you think about the naturalistic turn in neuroscience where so the traditional neuroscience
*  is control everything do very controlled reduced experiments, where you try to control everything
*  like like you're doing in your spiking neural networks, right? And these days, so the data set
*  that I'm working with is just a mouse walking around in a box with an electrode and not tasked
*  with anything, not doing anything cognitively complex or anything. And in under that regime,
*  you're not I mean, you still control well, it's in a box, right? And you control its environment.
*  But you don't you don't control where it where it looks, you don't control, you know, how it
*  moves, where it moves, etc. And it's proving difficult to I want to do an experiment, I'm
*  constantly wanting to do an experiment instead of which is fascinating. And I'm like really
*  interested in it. But it means that things are going really slowly, because we don't really know
*  how to think so much about these kinds of less controlled experiments. So what is your take on
*  on this ecological turn? If you will? Yeah, I mean, I think that we it's hard, but we have to like,
*  we have to do it. Because that is what the brain is ultimately trying to do, right? It's not trying
*  to solve to alternative forced choice with every other, you know, in a dark room, right?
*  So if we really want to understand what it's doing, we kind of have to do that.
*  We have to deal with more ecological environments. But yeah, I totally agree that that that really
*  leaves us hanging in a way like so what can we do in terms of of an experiment? I mean, I think
*  we can certainly learn some things by just, you know, letting the animal just do its thing and
*  recording what happens. And there's that great paper by Carson Stringer and others, where I
*  think that they had a I think it was a mouse just, you know, going around looking at stuff. And
*  they also recorded its facial muscle movements using cameras. And they did discover something
*  really interesting from that they discovered that you could explain as much variance in visual
*  cortex from knowing the facial movements of these of these mice as you could from knowing what it
*  was looking at. So that's a discovery. And another one that I think we haven't really got our head
*  around what that means. But I guess that doesn't get everything you might want to learn. Yeah,
*  like it's the conflict between having control so that you know what the effect of what you've done
*  is, and being in a sort of naturalistic environment. That's yeah, that's it's really,
*  it's really challenging. I mean, there's an argument that when you do control for everything,
*  you're actually building in the answer by controlling it. Yeah. So I think I've read
*  that you've I think I've read from you that there's a lot of low hanging fruit. I'm not sure if that's
*  the exact phrase that you used right now. Right now, there's a lot of low hanging fruit in terms
*  of spiking neural networks. So I mean, I know you have your own projects, but what are some
*  what are some things that you think some projects that people should take on that you're not
*  personally invested in? If you just had to give advice to someone wanting to use spiking neural
*  networks to understand something? Well, that's a good question. I think that there's a there's a
*  lot of mileage in just seeing how different neuron properties can aid different sorts of function.
*  Right. So like that heterogeneity paper that I mentioned that we talked about earlier,
*  that was basically like, what what is the contribution of time constants to function?
*  And it's best to always use one line of code if you can.
*  And if you can do it with just one line of code, it's all the better.
*  So so but I think you could just you could just generate like enormous number of those you could
*  be like, okay, well, let's let's take that one step further. Now. What about dendrites? Like
*  a dendrites useful, we could run the same thing right in dendrites, like what what are they doing?
*  And I know that there are people out there doing that already. But you could just there's all sorts
*  of like, okay, make pick an ion channel, right? Look at its dynamics. Like, is that what's that
*  useful for? Or is it just that, you know, that that's a mechanism that's there? Is it not really
*  contributing to function? Or is it really particularly useful for some? But I feel like
*  you can you can do a lot with training a network with and without some mechanism and then saying,
*  did that help? I think that's, that would be a low hanging fruit.
*  But you have to ask the right question. In that case, you have to ask the right question,
*  you have to have the right task. I mean, this gets to something I was going to ask you about
*  the right level of abstraction, right? Since you mentioned ion channels, for some reason,
*  ion channels are the first thing that people scoff at when they say like, that's too detailed,
*  you know, but you mentioned the Allen Institute, there are people like a gal to involve who has
*  been on the podcast who, you know, have these like highly detailed simulations, right? To understand
*  how like the neural signals that the brain produces, how those arise, and then how to
*  better to study them. And then you have people who say, well, ion channels dendrites, that's too,
*  like, that's too much detail for what you're actually asking functionally to understand it.
*  And you're somewhere in between there, I suppose. Are you at the correct level of abstraction? And
*  how do you know? Well, I'd like to think so, obviously. But yeah, no, I mean, it's a guess,
*  and everyone makes their own guess. So yeah, so my preference is somehow to, I don't think that
*  those things are irrelevant. I don't think dendrites are irrelevant. I don't think ion
*  channels are irrelevant. But I also don't think that we can just throw all of those details into
*  a massive box and gain understanding. We have to approach that in a more simplifying abstracting
*  way. This is my own personal preference, right? So for example, I really like the approach of
*  Dendrify, which is a new piece of software that came out in the last year or so, which basically
*  takes a detailed dendritic model and reduces it sort of automatically to just like one or two
*  compartments. And now, okay, now I can maybe understand one or two compartments. I can train
*  those one or two compartments. I can see what things that I can do with that. And maybe that
*  tells me something about what I could do if I had a thousand compartments. But I don't want to start
*  with a thousand compartments because I feel like I'll never get anywhere if I try and do that.
*  And similarly, for ion channels, I think that there's all sorts of things that definitely
*  are potentially interesting, right? So you have different sorts of inhibition, right? You have
*  shunting inhibition, which has a different sort of inhibition, like where the inhibition
*  falls on the dendritic tree can be important. Like those things might all be really important,
*  but I want to study that in an abstract way, not by like coming up with a single neuron
*  model that requires a hundred thousand parameters of which we only know five,
*  and we have to guess the other, whatever. So yeah, but I do think one of those things can be
*  important. And time constants is, I mean, in a way it's just ion channels, right? It's just one
*  particular abstract view of ion channels. What's something that's holding you back right now? What
*  are you stuck on that you feel you need some breakthrough to make progress on?
*  I think there's two things, I guess. So the easier thing, which I think is just going to be solved
*  at some point. Okay, let's say five to 10 years. That's my prediction. Always. Yeah. Exactly.
*  No, no, it's a fair comment. It's a fair comment even before I've said what it is.
*  And that's basically how to train spiking neural networks as efficiently as we can train
*  artificial neural networks. Because right now, so I've talked about surrogate gradient descent
*  and how much I love it. It's incredibly resource hungry to train. Oh, okay. Okay. I didn't realize
*  that. Yeah, no. So it's interesting because like the goal there is something very resource efficient
*  by a spiking neural network, but the training is actually much, much less efficient. And that's
*  why we haven't done it at scale. The largest spiking neural network I've trained with surrogate
*  gradient descent is maybe a thousand neurons. Okay. I think that the largest anyone's trained
*  is in the small tens of thousands. And it's just because the memory consumption of surrogate
*  gradient descent grows very rapidly with number of neurons. So that's a sort of technical problem.
*  And I suspect that we'll just get us, I mean, there's lots of people working on solving that.
*  There's lots of different approaches being tried. I suspect that some, and none of them have quite
*  worked perfectly yet, although there's been progress. So I suspect that that's just going
*  to get solved at some point, because if that feels like a, just like a purely technical in some sense,
*  I think that it might involve quite fundamental insight about learning to do that. So it's not
*  purely technical, but it just, it just feels solvable. It feels like it's a,
*  a well enough posed problem that we can solve it. You don't think it's just going to be stumbled
*  upon by enough people poking around in different directions? Yeah, it's possible. Yeah. But, but
*  yeah, I guess, I guess the reason I just is, is what I just said is just it's, it's well posed.
*  Right. And when a problem is, is well posed, I kind of believe in a solution. Interesting.
*  The less well posed problem that keeps holding me back is, I think we touched on it a few times,
*  is the lack of a good mathematical framework to, to talk about a lot of the stuff that I'm
*  interested in. Like to talk about sort of systems that are both discrete and continuous. So spiking,
*  for example, or to approach sparsity. In machine learning, sparsity is a really interesting,
*  but slightly niche topic. There definitely are people who are interested in it, but the tools
*  are really much less well developed for sparsity. If you try and use sparse connectivity in one of
*  the big machine learning toolboxes, you'll find that it's terribly inefficient. And it's because
*  that theory development isn't there yet. Both at a technical level, but also, I think at a conceptual
*  level, we just, we haven't got the right mathematical concepts to approach a lot of this stuff.
*  So that's, so sparsity is something where its importance is recognized without having a good
*  fundamental concept of why. I think so. Yeah. And you're also interested in modularity and
*  understanding modularity better. Is that something also where we don't have enough mathematical
*  tools to approach? Does that fall under that umbrella?
*  Yeah. I mean, we, so in that paper, we spent a lot of time, in fact, probably the most time in that
*  project, just coming up with a measure of whether a piece of the network was specialized for a
*  particular function or not. And that was like, surprisingly difficult. So near the beginning of
*  that project, I think I asked on Twitter, how do you define whether something is specialized on
*  something? And that created this huge discussion and there were no really clear answers that came
*  out of it. So we came up in the end with three measures and we were kind of satisfied in that
*  these three measures, which were kind of different from each other, kind of qualitatively did the
*  same thing in our model. So it felt like maybe they were measuring something meaningful or real.
*  But again, that's a very vague thing to say, right? Like we've got these three measures and
*  they're qualitatively quite similar. You'd like to say something a bit more concrete than that,
*  ideally. I mean, this is where I'm continuing to try to wrap my head around this, of how to even
*  talk about it. But this is where I want to have principles to can point to something like
*  complexity, right? Well, in a complex system,
*  this happens and be satisfied with that answer as its own unifying principle. And that's a
*  terrible example because complexity is like such a poorly defined term and encompasses so much. But
*  the principles of that nature, I want to be able to confidently state and mean and feel comfortable
*  doing so. And I'm not there yet. Do you think that that's a possibility though?
*  Yeah, I think so. I think we will find the right concepts. I'm so optimistic about that. But I do
*  think that we're still quite far. And I think in a way that's why neuroscience in a way. I mean,
*  not everyone agrees with me on this. I kind of feel like neuroscience is almost like
*  pre-paradigmatic. Oh, a lot of people do. A lot of people do agree with you. Yeah.
*  Well, it's a controversial one, right? But I feel like there's so many basic things that we just
*  haven't ever answered. In a way, we've had 100 years of neuroscience and we don't know
*  whether spike times matter or not. I know. It's sad. It's sad.
*  Well, it's sad. But it's also just because we don't have the right frameworks to answer
*  questions like that. But I think that the development of those is just hard. Like
*  looking at physics, the development of the concept of mass, for example,
*  as opposed to weight or whatever, that really unlocks a lot of stuff. But that wasn't easy to
*  come by. That took a lot of development before we got that concept right. And once we got it,
*  it unlocks so much stuff. So I think that we may well have a similar thing here,
*  that we're still in this sort of stumbling around the dark, just trying out a lot of stuff.
*  But I do think that we will make progress. What do you think is the, if you had to point
*  to the single most valuable thing that artificial intelligence, let's say deep learning,
*  has taught neuroscience, what would you say, if anything?
*  I mean, for me, the big thing is it's the training algorithms. There are these algorithms that,
*  surprisingly, mathematical, can do it. There's a lot of surprising stuff there, right? Like
*  stochastic gradient descent, for example, compared to just hill climbing, sort of standard gradient
*  descent, lets you learn really hard tasks. And you throw in momentum into that, and you can learn
*  even harder tasks. And we can just take those tools and start using them. For me, that's brilliant.
*  So that's the technical thing. I think intellectually, there's a really interesting
*  thing as well, which is that what we think is hard might not be what's actually hard in some sense.
*  Like, it feels incredibly difficult for us to imagine being able to draw a picture of a tiger
*  in a top hat in the style of Van Gogh or whatever. But it turns out that that's actually easier than
*  catching a ball. This is more of X paradox. Who's that, sorry? More of X paradox, where it's,
*  yeah, a lot of things that we take for granted that are super easy for us are hard for machines
*  and vice versa. And vice versa, right. So I think that's also really interesting. So often,
*  what I'm interested in when I look at these machine learning models is that because we know
*  that they're not as capable in some sense of general intelligence as us, what they're doing
*  is in some sense simpler. And it tells us that this thing that we were looking at that we thought
*  was the source of all understanding of our own intelligence, it wasn't actually quite that.
*  You know, it helps us, I think, focus our attention on what we don't know and what we still need to
*  understand better in some way. Which is not to say, sorry, I've heard this one a lot. So I'm not
*  saying that anything that machine learning can do is automatically not interesting and not what real
*  intelligence is about. I think at some point we'll have enough of these pieces that they will just be
*  intelligent. It turns out that that is what intelligence is. It's more that you can do
*  surprisingly much with tools that are not necessarily perfectly aligned to that goal,
*  I think. And so for me, I think of large language models like that, I don't think that they're doing
*  given my bias. I don't think that they're doing language or reasoning the way we're doing reasoning.
*  But you've got to admit that they do an amazing job. And that this thing that isn't really what
*  we're doing turns out to be good enough to do 95% of what we do. But it's also interesting that
*  there's surprisingly some bad at some stuff. Like on a whim, I tried out testing whether
*  GPT could match parentheses and it can't match parentheses.
*  What do you mean match parentheses?
*  Oh, right. Like, they're the same number of open parentheses as closed parentheses in a bit of
*  code. So why is it that it can't do this incredibly basic task, but if I ask it to write me a program
*  to do X, it can just do that. Even if it's something that hasn't seen before.
*  I would argue humans are not very good at counting open and closed parentheses,
*  at least in my coding, unless it auto fills for me.
*  Fair enough. But if that's what we were trying to do, I think we can probably do it right.
*  Like we can force it. But it's really surprising how bad it is actually. You can give it examples
*  where it's obvious that the parentheses are matched and it just guesses at random basically.
*  And often just tells you completely unrelated stuff.
*  But I think that that's, I mean, I did that and I looked into it and it turns out that there's all
*  sorts of surprisingly simple things like that that large language models are bad at. They can't
*  count. So if you write like a, a, a, a, a, a, how many a's were there, it gets that wrong, things
*  like that. And of course, each time anyone finds one, the people making them change the model so
*  it can do that. So they never last very long, these things. But it's amazing that this thing
*  that can't do this, something we think of as so simple, it can write us a program to do really
*  complicated functions or draw us a picture that's better than we could draw ourselves or
*  summarize a paper or a field or in a surprisingly, surprisingly accurately.
*  Right. Like it tells us that what we, what we think is, what we think is difficult is maybe not
*  quite right. And I think that's valuable. To me, that's fairly humbling in terms of thinking
*  of my own intelligence, right? Because we value those sorts of skills, like you were just saying
*  above catching a ball, for instance. But then I see, you know, a machine do something that's
*  very, what I would consider an intellectual feat on my own or something that I can't do,
*  you know, but I could just ask a large language model to do it. Do you feel the same as I feel
*  that, I'm not sure if humbling is the right word, but a sense of like, oh, maybe, um,
*  my reaction is like, oh, maybe that's like not very intellectually difficult. Maybe it's not very
*  difficult. Yeah. And I don't really know if difficult really makes sense, but I think
*  difficult really makes sense. But I have the same feeling as you, right? Like, um, I thought, you
*  know, maybe I thought like being able to write nice prose was, was important, but it turns out
*  that it can do a better job of that.
*  And here's my question. Does it reduce the value of humans doing things like that? Does it reduce
*  the value of poets, let's say, right? Not as human beings, but in terms of the, the,
*  how we revere certain talents.
*  I mean, in a way we can already answer that, right? Because we've seen it in things like
*  chess playing, right? It's, it's been now a while since we weren't as good at chess as computers.
*  And I feel like we're still interested in, I mean, I'm not, I don't, I don't play chess,
*  but I feel like people who are interested in chess, but I feel like people who are interested,
*  I don't know, has, has interest in chess waned since computers got better at it? I'm not sure
*  that it has. I'm not sure either. Yeah. I don't know. But I'm still seeing people are still
*  playing it. Yeah. Yeah. And I think it's worthwhile. Like I've taught my son how to play chess and we,
*  you know, we play occasionally. It's been a while, but, but I'm also less interested in it as an
*  intellectual pursuit, I think because of the success. Yeah. I mean, I think that's probably
*  going to be at some point an existential question for our species, but at some point, but we're not
*  quite there yet. Fortunately, five to 10 years, five to 10 years. Exactly. Let me ask the converse
*  of the question I asked you before. And then I want to talk about your recent sort of meta science
*  stuff. And I won't keep you all day, but so I asked you, you know, what you think that AI has
*  done for neuroscience. What do you think that let's say your own work and, or just neuroscience
*  in general has done or will do for AI? Yeah. I mean, I think historically they've, there's been,
*  I wouldn't say it as simply as like what has neuroscience done for AI. I mean, I think if you
*  look at the early history, it was almost that they weren't separate questions, right? Right.
*  The people who were doing one were doing the other and they didn't think of it as separate questions.
*  And more recently they have diverged, but I think that's almost a shame. I feel like it,
*  it would be nice to have some of that early energy of like, this is somehow the same question that
*  we're approaching in. We've got different ways of approaching it. Part of that is just the phrase
*  artificial quote intelligence, which I've come to despise because it reifies intelligence,
*  which maybe is not a thing anyway. Sorry to interrupt. Yeah, no, I agree. I try and always
*  talk about machine learning rather than AI. But yeah, for that reason, I think it's one of those
*  buzzwords that, yeah. But as to what that interaction could meaningfully be about,
*  I think counted from people who are like from machine learning people, a bit of skepticism
*  about the idea that they have anything to learn from neuroscience. And I think I get it. I think
*  I understand how it would feel for like you to be working on this really important and exciting
*  topic and be making so much progress. And then some neuroscientists come along and says,
*  you should be learning from what I do. Yeah, that would be pretty annoying.
*  And I'm not sure it's really as simple as that. But I think what could be useful is
*  for us to think of it as two aspects of the same question. This is probably,
*  this is my mathematician talking, it's probably too abstract. But what are the space of
*  intelligent mechanisms out there? And maybe machine learning is going to explore some
*  part of that space and neuroscience is exploring another part of the space.
*  But they're somehow exploring the same problem, but from two different points of view. And I think
*  that it would be good if both sides knew a bit more about the other, even if it's not a direct
*  matter of like, we'll take ideas from one side and go to the other side or vice versa. But more like,
*  if we have a broader conception of the problem that we're trying to solve, we might come up
*  with answers that we wouldn't have done with a more narrow conception. I think that's how I would
*  put it. And do you feel optimistic for yourself moving forward that those fruits are there for
*  you to discover? Yeah, I think so. I mean, I feel like there's a lot of exciting, interesting stuff
*  in that sort of space. Like for me, I think a lot of what I'm thinking about is trying to
*  think about the tasks that
*  are different, I guess, from the ones we've looked at before. So for neuroscience,
*  we need to look at more richer, messier data, right? But on the other hand, machine learning
*  people maybe need to think more about behaviour or about generalisation. Obviously, it's not that
*  that's an unstudied topic in machine learning, obviously. But that's maybe in the study of those
*  sorts of things is where knowing a little bit about how the brain does things might inspire
*  something, right? Because it's already doing those things. So yeah, I think it's in that space
*  between I think that there's some interesting stuff. That's where I guess where my interests are.
*  Okay. All right. So we're going to take an orthogonal turn here, because I know that as
*  you age in academia, like any good neuroscientist, you're becoming more and more curmudgeonly.
*  It's one way to put it. And seeing the cracks, what's working, what's not working. And
*  there's a cottage industry of complaining about the publishing industry.
*  Yeah, I just use industry twice. And you're part of that cottage industry. And do you not review
*  papers anymore?
*  Yeah, no, I stopped. I quit all my editorial positions and stopped reviewing because I think
*  it does damage to science. And I can talk about my sort of personal reason for doing that, which
*  was I always found reviewing and later editing an uncomfortable experience.
*  All right. Well, Dan, I really appreciate your time. I won't keep you all day here, but continue
*  the good work with the spiking neural networks. And I'm looking forward to seeing what you're
*  going to be working on in the near future with them. And we didn't talk about all of your,
*  the good deeds that you have done outside of science as well with things like neural match
*  and snafu. Is that what it's?
*  Snufa.
*  Yeah.
*  Snufa. Snufa. Yeah. Snafu is the-
*  It's like as close as possible to snafu without actually being snafu.
*  Was that intentional?
*  A little bit.
*  Okay. It just worked out that way. Anyway, I'll mention those in the introduction. So,
*  but thanks for being with me. I appreciate the time.
*  Okay. Thank you very much. It's really a pleasure to be here.
*  I alone produce Brain Inspired. If you value this podcast, consider supporting it through Patreon
*  to access full versions of all the episodes and to join our Discord community. Or if you want to
*  learn more about the intersection of neuroscience and AI, consider signing up for my online course,
*  Neuro AI, the quest to explain intelligence. Go to braininspired.co to learn more. To get in touch
*  with me, email paul at braininspired.co. You're hearing music by the new year.
*  Find them at thenewyear.net. Thank you. Thank you for your support. See you next time.
*  Bye.

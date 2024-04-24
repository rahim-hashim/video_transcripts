---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 3576s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 162
Video Rating: None
---

# BI 042 Brad Aimone: Brains at the Funeral of Moore's Law
**Brain Inspired:** [July 28, 2019](https://www.youtube.com/watch?v=OLq_F-fCEdE)
*  The inspiration of neuroscience into deep learning is from the 60s and 70s.
*  Yeah. With a little bit of sprinkled in from the 80s and 90s, but not very much.
*  And there's clearly so much more we understand about how the brain works
*  that could be fed back into AI probably relatively quickly if the two fields talk
*  to each other more. Most of them aren't going to know the distinction between a
*  deep learning net and the brain. They're not surprised if I tell them that the
*  brain is more complicated than a deep learning network.
*  This is Brain Inspired.
*  Moore's Law is dead. Long live the brain.
*  Hmm. Not sure that has quite the right ring to it. Might have to work on that a little bit.
*  Well, hello, brains. This is Paul Middlebrooks. Welcome to the show.
*  This is the second half of my conversation with Brad Imini, the neuromorphics and computer
*  scientist with a history and a heart in neuroscience at Sandia National Laboratories in New Mexico.
*  I advise you to listen to the previous episode, episode 41, to better understand this one.
*  This episode picks up right where the last one leaves off. In the first part of our conversation,
*  we talked about neurogenesis deep learning. We also talked about Brad's whetstone method
*  of sharpening deep neural networks until they are sharp enough to become spiking neural networks.
*  The neuromorphic computing workshop, NICE, that Brad runs every year. In this episode,
*  we finish our conversation talking about neuromorphics and its relation to AI and
*  neuroscience. Among other things, we talk about how our knowledge of brains could help the world
*  of computing progress once Moore's Law does take its final, beautiful breath.
*  Show notes are at braininspired.co.
*  Here's the last little bit of my time with Brad Imini.
*  So one way to approach AI is whole brain emulation. Emulating as precisely as possible,
*  as much as we know about the brain. Well, actually, whole brain emulation would be
*  essentially downloading the entirety of the brain in some certain state that then you could unfreeze
*  and dynamically use in your hardware system or in your software system. What do you think the
*  prospects are for whole brain emulation and would we even want it? Because in neuromorphics,
*  there's this sort of give and take of how much of the brain do we want to use. Then like you were
*  talking about before, it's about solving problems. So you have this little principle and then you can
*  take it and run with it and not necessarily do it like brains do it, but use the abstract principle
*  like brains do it, but use the abstract principle for your own inspiration to compute something
*  that solves a problem, for instance. So would we even want to emulate whole brains, right? Or
*  would we be limiting ourselves in some sense? So I think that I'm skeptical of that direction.
*  I'm skeptical of that direction from my personal experience in doing large scale models.
*  Yeah, okay. There are two reasons for my skepticism, especially as it relates to neuromorphic
*  computing. So I built these large scale models and I had lots of fun doing it and I learned a
*  lot from it. So I'm not going to say that the value of large scale models is not there, but I
*  do think that as you build these models, inferring insight from those models ends up becoming as big
*  or if not a bigger challenge than building the models themselves. Never mind the fact that
*  collecting the right data from a brain to download it all into a simulation is going to be a very
*  hard challenge biologically. If you had a whole brain, let's just say that someone gave you
*  the whole brain on neuromorphic chips and it had every connection and all the dynamics you needed
*  to replicate a brain, mouse brain, say, then we're going to be where we are now in systems
*  neuroscience and how do we interpret what's going on in that? Right. So I think just because you
*  had all the data doesn't mean that we are theoretically mature enough to interpret all
*  of that data. It's a little bit, I think, almost a controversial statement. So much of the brain
*  initiative has been about collecting data. I think that it is a necessary step, but I also
*  think that our theoretical tools to interpret data at that scale are limited. So I mean, I take the
*  box and I'd start using it to develop the theoretical tools, but I don't think the box is going to solve
*  you the problems of AI today. That box being the whole brain on a simulation. The second reason
*  I'm skeptical of it from a neuromorphic point of view is that as I built really, really big
*  simulations, I never once said to myself, I wish I had a neuromorphic chip to accelerate
*  these simulations. Yeah, go ahead. Well, I'll always say that. So when I was building larger
*  and larger scale biological simulations, so millions of spiking neurons from the hippocampus
*  in silico, I was running them on supercomputers, the sort of large HPC platforms that we have here
*  at Sandia. And the thing that I learned was that the computing resources I had and that are
*  increasingly available are sufficient for doing these really large simulations. Ultimately,
*  you're going to have to pay a power bill or some cost where having neuromorphic accelerators would
*  be useful. But for the most part, having a neuromorphic chip would not give me any capability,
*  any sort of ability to do anything at a bigger scale than the tools I already have at my disposal.
*  I see. We've gone a long way with exascale, pedascale supercomputers. They're not easy to
*  program. The neuromorphic chips aren't easy to program either. So I think that a good
*  computer science simulation on conventional supercomputing resources can probably do all
*  of the large scale simulations we probably need today. That's not to say neuromorphic doesn't have
*  value to feedback into neuroscience. I think it absolutely does. But I don't think that value is
*  just letting you have bigger and bigger simulations. Well, that's what I was going to ask next.
*  There's a lot of push from a lot of theoretical and computational neuroscientists who see the value
*  in deep learning as being able to generate new theories to then push back into neuroscience and
*  understand brains better by developing and analyzing these deep networks. I was going to
*  ask if you think that neuromorphics will help us understand brains and if so, how?
*  So my personal hope, you know, I'm a neuroscientist at heart, so I want to understand the brain as
*  much as anybody else doing neuroscience. And the reason I justify taking this sort of
*  diversion into computing is that I think that by thinking about how to solve problems using neurons,
*  real world problems, things like maybe deep learning problems, but maybe think about how
*  to solve a partial differential equation using neurons, which is something else we've been doing,
*  or things that may not look anything like how the brain works. But by learning how to solve
*  problems using neurons as the sort of logic gates as the tools. And that is done with the intent of
*  eventually putting those applications on neuromorphic chips. But thinking about solving problems in this
*  way will provide us a different perspective by which we can look at how the brain solves problems.
*  Because ultimately, the brain has at its disposal billions and billions of neurons
*  that can be wired together to solve different tasks. And we really have very little foundational
*  insight into what it means to wire together neurons to solve tasks. So if I want to just hand
*  you if I gave you 100 neurons, and I said, build a Boolean circuit to add two numbers.
*  The thing is, you can do that. Right. Right. You know, it's not what the brain does. But
*  by understanding how those sort of Legos fit together in fairly small packages,
*  very small applications like that, I think that we can eventually build towards more and more
*  complicated things that ultimately will start looking like how the brain does things. Because
*  when you start having millions of neurons, needing to connect to millions of other neurons,
*  the brain is actually a very good template to start looking for those solutions. So I think that this
*  sort of approach of doing basic computation with neurons will eventually wrap back to understanding
*  how the brain works from a completely different direction. This is it's interesting because people
*  think of neural networks as being a bottom up approach because you're emulating neurons by
*  having individual units and then just using the statistical properties as it learns. But what
*  you're talking about is more of a bottom up approach almost, I'd say. And in that in the way
*  that you're speaking about it, neural nets is almost a top down approach because you're just
*  throwing the computation. Well, you're feeding the answers to the network and just asking it to
*  perform the work, which is almost top down. Yes, I would agree with that. I think that
*  I see a value in almost learning how to program neurons at the assembly code level, so to speak.
*  How do you wire neurons together? Which if you look at the full spectrum of nervous systems,
*  things like Drosophila and C. elegans and even a number of mammalian
*  sub-circuits are more or less hardwired. I mean, it's not just a blank slate that we present a lot
*  of data to and hope it learns during development. The architecture is very much present in almost
*  all nervous systems. And then within that architecture, there's learning to kind of
*  fine tune things. But the idea that we can go about the brain is just a blank slate that we just
*  present a lot of data to and it's going to learn how to be a brain. I think that's clearly not
*  what happens in actual biological nervous systems. So I'm not going on a big limb there.
*  So going from this direction where I say, I want to solve this simple function
*  with neurons and I want to start building up from that into something more complex and more
*  complex and more complex. I think that there is a lot of opportunity there and we're just starting
*  doing that sort of thing. But I do think that in that respect, the sort of neuromorphic
*  view of computing will eventually feed back into how we understand the brain in kind of a unique way.
*  Sounds hopeful. I hope you're right. What do you think are a few of the main hurdles
*  right now in neuromorphics that are in the way of neuromorphics taking over versus deep learning,
*  for instance, or just progressing in general? Well, I don't think neuromorphic computing and
*  deep learning are orthogonal. I think that in some sense, neuromorphic computing, it's a hardware
*  story, first and foremost. And deep learning is an algorithm, an eye story. And I think that
*  the neuromorphic field is going to be able to take advantage of deep learning success and
*  find an application that will get it to develop more. So I think in that sense,
*  they're complementary to each other. I do think that brain-inspired algorithms as a whole,
*  my personal view is that the biggest challenge they face is how do we get
*  new insights from neuroscience into the computing field? So if you look at deep learning, which is
*  clearly a success and arguably a success for neural-inspired AI, the inspiration of neuroscience
*  into deep learning is from the 60s and 70s. With a little bit of sprinkled in from the 80s and 90s,
*  but not very much. And there's clearly so much more we understand about how the brain works
*  that could be fed back into AI, probably relatively quickly, if the two fields talk to each other more.
*  Hmm. And I mean talk to each other more than just how do we use deep learning in neuroscience,
*  or how do we show that the brain does deep learning? Like that sort of conversation, I think,
*  is going to happen, but it's not necessarily what I'm talking about. What I think needs to happen is
*  I think people who are educated, trained in neuroscience, you know, need to take a hard,
*  long look at what problems the AI field as a whole, not just the deep learning field,
*  but AI as a whole is struggling to solve. And, you know, I think that neuroscience will have a lot
*  to offer in terms of this sort of longer term, where, what comes next after deep learning sort
*  of view. But the only way that neuroscience can have that is if neuroscience kind of meets halfway,
*  at least, in that conversation. Yeah. And then really, it's hard. I mean,
*  it's hard. You told immersion like I did, maybe, you know, people can do it, but you don't want
*  that you want people to be you want this sort of dialogue to exist at a healthier level that doesn't
*  require people drop what they're doing. So I do think there's a lot of hope. But I do think that
*  sort of interaction is going to be a challenge. And it applies to neuromorphic as well. I think
*  people building ships based on how the brain is structured, they need to talk to people actually
*  know how the brain is structured, right? It's not, you know, you can't get it by reading Wikipedia
*  pages. Anti Wikipedia stance there. Nice. No, I completely agree. But it sounds like the the
*  consensus from people, again, who, you know, speak at the the nice workshop that we talked about a
*  few minutes ago, the consensus seems to be that neuromorphics won't replace like von Neumann type
*  computers that we have these days. But instead, as we move forward, we'll complement them like
*  when needed. Is that your take as well? I think that's fair. I mean, you know, there's a reason
*  that classical computing approaches have dominated for 7080 years. They're very, very good at doing
*  what they do, which is kind of implementing serial instructions, you know, mostly mathematical
*  sort of functions. And there's no reason why we would use a neuromorphic approach to do basic
*  computing stuff like, you know, balance your checkbook on Excel, you probably could. But I
*  don't think you need to and I don't think you'd want to. So I think that the view that we're going
*  to have a more heterogeneous future of computing is increasingly being accepted by the broader
*  community. By the broader neuro neuro morphic community. Oh, I'd say everyone I think computer
*  scientists as a whole. You know, we see this. I mean, people have CPUs and they have their GPUs
*  to do deep learning training. Yeah. And they you know, people are working on other accelerators
*  to do different things. I think neuromorphic approaches are going to be something in that sort
*  of category. You'll always have your CPU doing CPU stuff, but we'll be able to use the neuromorphic
*  computing to do certain sorts of tasks very efficiently at very low power at very large
*  scale. Well, I mean, these the CPUs of unknown install computers, right, they, they always give
*  me the same answer when I ask for a calculation, for instance, or when I balance my checkbook.
*  Humans don't do that, for example, neuromorphics tend to not do that as well. And so I had Anne
*  Churchland on my show a couple episodes ago now. One of the things that she found in her
*  study on decision making is that animals in her case, mice have these lapses in their decision
*  making, where even though the answer seems pretty obvious, they'll still make the wrong decision.
*  Right. And her take is that this is a balance between exploration and exploitation, that,
*  you know, animals still are trying to explore different options, different alternatives as a
*  way of learning the environment. And she says that we would want AIs to have lapses like these to
*  always be exploring. And there's also this concept of bounded optimality developed and
*  talked about by Stuart Russell, which says basically that a machine has this finite speed
*  and memory and can do the best it can with what it has. Right. Do you think this is an
*  inherent compromise or even an essential element of something like eventual general AI? Is
*  imperfection a computational and almost fundamental consequence of achieving general intelligence?
*  So I would, I think I would agree that there's a very strong biological value of having
*  imperfection in the sense that you were talking about it. Although I think the way you described
*  it, it isn't really imperfection. It's just the task that's being optimized is not necessarily
*  the task that one is observing. Good point. So, you know, if you, the trial and error,
*  the explore and exploit sort of trade off is trying to maximize performance over time scales
*  that likely are far longer than an individual mouse training session and so forth. Cause,
*  you know, ultimately the mouse brain doesn't really know why it's being strapped up and being recorded.
*  Right. And I think what you want in a general AI system or even a more, you know,
*  smaller ambition neuromorphic application is the ability to control that.
*  So if I'm balancing a checkbook or if I'm navigating a self-driving car and,
*  you know, I'm trying to do something that has to be reliable at 99.9999%. I need to have the ability
*  to tune to that. And I would say that our brains actually are pretty good at tuning to really high
*  reliability if they need to be. The thing is, is that for a lot of what we do, we don't need to be
*  right. We're willing, we're willing to kind of loosen up that. And I would, you know, full
*  speculation mode, I would say this is where things like nerd neuromodulators like serotonin come into
*  play is actually fine tuning the sort of sharpness by which our computations are done.
*  And in a neuromorphic algorithm sense, you know, if I'm, if I'm self-driving a car and I want to
*  have a neuromorphic algorithm do the navigation and I'm in a critical operational state, you know,
*  I have to get to the hospital very quickly for whatever reason, it's not a good time to do the
*  explore phase. Just like, you know, you know, as a human, if you need to, if you're late to work,
*  it's not a good time to kind of, you know, drive by and see what if that donut shop down the street
*  opens up. Right. Or for example, like a stop sign, you wouldn't want a car to not pay attention at
*  some point to a stop sign because it's exploring. Exactly. You know, there's some things that,
*  you know, a stop sign is high consequence for you to misinterpret. I see them as recommendations,
*  but we wouldn't want our self-driving cars to see them though. Probably not. Yeah. I think
*  we'll engineer those to be more reliable. But so I do think tuning the tuning of that is going to
*  be critical. But I think to get to your original question, absolutely an inherent ability to
*  switch between exploring the world and exploiting the world is going to be critical
*  for more sophisticated, intelligent computing. Yeah. General AI, if you will, because I think that
*  being very rigid comes with consequences itself.
*  Quote, machines will be capable within 20 years of doing any work a man can do. End quote.
*  That was Herbert Simon, pioneer of artificial intelligence, among other things, in 1965.
*  So you recently published this paper, Neural Algorithms and Computing Beyond Moore's Law.
*  And this is about scaling computing in general going forward. And I love this because
*  it's essentially your speculations, your very educated speculations on how
*  our knowledge from neuroscience could help computing moving forward. And in this paper,
*  you talk about how you make the case that deep learning is just the beginning, really,
*  and that, you know, there's much more to come as we learn more about brains.
*  And you think that learning about brains is the way to go forward, to develop new
*  theoretical frameworks to drive AI forward. Why is Moore's Law dying?
*  So Moore's Law is funny because when I got here eight years ago to Sandia,
*  I knew what Moore's Law was because probably of like Intel commercials from when I was a kid.
*  Right. Yeah. Everyone's Moore's Law is great. We get faster and faster computers.
*  Was that really in commercials? Maybe. I feel like it was.
*  Okay. Okay. But it's more of a marketing thing in some sense. It's a business observation.
*  And this is one of the things I learned is that what Moore's Law is, is an economic story.
*  It's that the computer industry, through a lot of work, was able to reduce the size of transistors
*  every couple of years. And there was a huge industry committed to doing that process.
*  You know, because it's a material science question, it's a lithography question,
*  it's a engineering question. There are all these things that had to go into making a smaller
*  transistor and then building a CPU or whatever hardware out of that smaller device. And a lot
*  more than just the device sizes. So having silicon that would be 25 nanometers as opposed to 30
*  nanometers, you know, that's part of it. But you have to figure out how to make wires small enough
*  to do that, how to have communication fabrics and so forth. So this is the computer industry
*  for the last 50 years. And the thing is, is that Moore's Law is slowing down. There's a very simple
*  reason for that. And that is that our transistors are starting to get to a finite number of atoms
*  in width. These things are made out of silicon. There's silicon that has, you know, certain
*  impurities in it that allow it to be semiconductors. And as you start getting down to things that are
*  maybe a few dozen silicon atoms in size, which is a few nanometers, you really can't go any smaller
*  and still have a transistor that operates in the sort of functional way that that material is
*  supposed to work. So that's just a pure physical observation, right? The physics of CMOS transistors
*  or kind of silicon transistors just does not allow them to scale smaller, smaller and definitely.
*  Eventually you reach atomic scales and you can't do any smaller. Yeah, and we're getting close.
*  So the computer industry is freaking out understandably, because this was, you know,
*  there's a lot of work and a lot of investment went into it. But every two years, you're able
*  to have a faster, cheaper thing to sell, which in turn amplified, you know, allowed faster,
*  better software and an entire industry to just keep advancing at this time scale. It's kind of
*  a miraculous thing, but we were able to do it. And it was fantastic. But we have to think beyond
*  that now, because it's no longer, we can't assume that two years from now, we're going to have
*  twice as many transistors on our chip.
*  And where's that going to come from is the question. How are we going to move past this,
*  I suppose, is the reason you wrote this paper, huh?
*  It is. And, you know, it actually, you know, a little anecdote. There was another workshop that
*  out of Oak Ridge National Labs that a senior person at a big computing company was complaining.
*  I mean, they were saying how we need some other scaling law, we need something to take over
*  from Moore's law, because we literally have a trillion dollar industry, depending on this sort
*  of scaling. And it occurred to me that that the brain actually has this to offer. And it doesn't
*  have it to offer in the same way we're not, you know, the brain's not going to give you a smaller
*  device, it's not going to give you, you know, an exponentially increasing number of neurons every
*  two years, the way that we've had number of transistors every two years. But it's a different
*  sort of scaling law, is what I more or less propose in this paper, which is that we're at a stage of
*  neuroscience where we've developed a lot of tools, where we can record more and more neurons, we can
*  look at optical tools or electrical tools to measure, you know, how neurons and systems behave.
*  The genetic tools are amazing. But we still don't know a lot. This was the theme earlier in our
*  conversation. We don't know a lot about how the brain is working. So I see that as an opportunity.
*  If we just keep going down this path of neuroscience, we're every two years, let's say,
*  we're going to know more than we knew two years before. And then, or maybe it's five years, or
*  whatever time scale, but we're going to be increasing our neuroscience knowledge of how
*  the brain actually works for generations to come. You know, we're not two years away from
*  understanding everything about the brain. I think it's a good thing. I think that we're at a point
*  where two years from now, we'll be able to go and we'll be able to see amazing, great results.
*  But there'll be a reason to come back for more two years later. And the reason to come back
*  for more two years later, we're at the beginning of a renaissance. And that that sort of continual
*  titration of the secrets of the brain into computing is an opportunity to effectively get
*  the same results that Moore's law gave computing over the last number of decades.
*  So in the paper, and of course, I'll point people to it. It's just this.
*  We'll talk about the potential steps that you lay out. And these are the speculative
*  sort of order of how brain knowledge will contribute to our computing power, essentially,
*  going forward. One of the things you talk about is how neural computing could be one-off
*  or paradigm shifting. And can you explain the difference between those and just the range of
*  effects of those alternative possibilities? So one possibility is if you had a neural computing
*  influence on computing, which was just we're going to use a new architecture, we're going to
*  replace von Neumann architectures with neurons, you know, wired up, however you wanted to wire them up.
*  And the argument was made to me once by someone who knew what they were talking about,
*  that this would be disruptive. But once you do it, you can't benefit from it again and again and
*  again, because it's like, you know, I now have a cortex on a chip as opposed to a von Neumann CPU
*  on a chip. But once I figure out I have that, you know, I'm not going to get cortex 2.0, cortex 3.0,
*  cortex 4.0, if I were to just replicate the architecture of the brain in that sense.
*  So I think, you know, I think there's something to say for that. So it's not simply a case of
*  mimicking the hardware. The hardware will give you some improvement, perhaps, hopefully. But I think
*  there's a deeper question, which is, what is the actual computation? What is the brain actually
*  doing? What is the sort of representations and transformations of those representations, the
*  learning, all of the questions neuroscientists care about, all of those questions about how to
*  do computing in a neural sense? That, I think, is a much longer influence on how we do computing
*  for applications going forward. I don't know if that distinction clear? Yeah, no, it's hard
*  because since it's an audio podcast, you know, I wish people could see this, the graph that I'm
*  looking at from from the paper where essentially you have like Moore's law kind of asymptoting.
*  And then there's this series of increases with these different advances in what we learn from
*  brain science. So the first one, for instance, is feed forward sensory processing, which is
*  basically the big success that we have these days from these deep learning networks. And just to
*  give a sense, each of these steps, there's this quick initial increase, and then there's kind of
*  an asymptote. But then due to advances in our understanding of brains, there's this next step
*  of a quick increase, and so on and so on as we learn more about the brain. Yeah, I understand
*  your question a little better now. So one of the things that I learned from the electrical engineers
*  is that Moore's law, we saw as an exponential increase. But the community was doing kind of
*  incremental things, they make a smaller transistor, the effect of that transistor would have a huge
*  effect in a, you know, over one or two year period. And then the benefit of that particular
*  technology would taper off. And they'd have to come up with a new technology that would
*  basically bootstrap on the past advance to get something a little better. And so as consumers
*  of computing, we would see what seemed to be an exponential increase. As the computing engineering
*  field, what they were seeing is a step ladder, where it's, I'm going to do this technology,
*  then this technology, then this technology that yielded to the world this exponential
*  appearing increase. And I would say that we have the opportunity to do the same thing in neuroscience
*  where deep learning, you know, we're kind of seeing how there was this huge wave of deep learning,
*  where we were going from fairly abysmal performance on image processing tasks, to something was more
*  or less asymptotic when it comes to image classification, you know, you're not going to
*  get better than 99.9% on some of these tasks, obviously. What we need to do is we need to take
*  the next step to maybe something which is a different capability, a different function
*  of brain inspiration. And so I kind of walked through a series of these and it's speculation
*  on my part, you know, based on how I see the field moving, and maybe the order will be different at
*  some, you know, what actually happens, I don't know. But, you know, I do think we're seeing evidence
*  that early stages of some of these next possible technologies are already beginning to occur.
*  We see it with things like recurrent neural networks, people who are looking to the brain for how,
*  you know, local inhibitory circuits, feedback on excitatory circuits. That's a really trendy
*  thing in neuroscience today, especially in cortex. And the deep learning field is kind of primed to
*  take that knowledge to make their algorithms more temporal and have them have a more, say,
*  temporally robust function in dealing with things like video processing and other sorts of tasks.
*  And I think you can kind of walk through a trajectory of steps that neuroscience can add
*  over the next coming decades. Well, just for fun, let's do walk through it if you're game for it.
*  So the first step is actually what's going on right now. It's these, the success that's been
*  going on is these feed forward deep networks, which has already advanced the field, but still
*  has, you make the point, still has a lot to learn from neuroscience, a lot to incorporate from,
*  you know, like you said, these concepts that has driven these successes were basically from
*  the 60s with some sprinkled in 70s and 80s knowledge from our brains. There's still a lot
*  to learn from there. So then eventually we're going to incorporate more into these feed forward
*  systems. And then this next step, like you were just speaking about, are the temporal aspect and
*  the temporal neural networks. I don't know if you want to just elaborate on them.
*  Yeah. So I think, you know, I mentioned things like inhibitory and excitatory networks and how
*  our neurons in the cortex are connected in recurrent loops. They talk to one another,
*  they're spiking. So information's encoded in the time regime. They're interacting with
*  other layers and when things happen is, is just as important as what happens in some respects.
*  And so the deep learning field, or they say the AI field as a whole is only beginning to capture
*  some of that in their thinking with things like long short-term memory networks and other current
*  nets. And some of those ideas have been around a while, but they don't really have the richness
*  and the robustness that we see occurring in cortex. So even our sensory cortex, which was
*  the first stage of this sort of trajectory, if you think of it feed forward, you can do basic
*  image processing, for instance, or basic audio processing. If you think of it as temporal,
*  and you have feedback and you have recurrence as you go through the, you know, kind of through
*  that hierarchy, I think that's probably going to be required for things like video processing and
*  inferring things that are maybe, maybe more kind of motifs, you know, you almost think of as a
*  trajectory of images over time or something like that. You know, our brains clearly operate in a
*  temporal mode. They're not static neural nets. They have this time dimension to them. And it
*  seems in a sense like low hanging fruit for the AI field to kind of embrace. It's a different
*  technology, right? I mean, it took 50 years to go from orientation columns in V1 to what we see
*  today in deep convolutional networks. So hopefully it takes less time than that for this stuff. But,
*  you know, I do think that's kind of the next thing we'll see is what I would anticipate.
*  The temporal neural networks. Okay. And then, of course, that's going to peter out in 10 years
*  when we figured it all out and incorporated all that we know into those. And then Bayesian neural
*  algorithms are going to take over. What's the story here? So, you know, this is what, you know,
*  when you go to a lot of the system neuroscience meetings, you know, there's definitely this feel
*  and I'm not a cortex person, but I think the cortical neuroscience, systems neuroscience
*  community has long looked at the brain. And I think rightly so as having more of what we'd call a
*  Bayesian sort of structure where you have top down sort of preconceptions of what's going to be
*  experienced as a key guide and influence on what the sort of bottom up of what is actually being
*  observed. So the interpretation of sensory information is as much of a function of kind
*  of an expectation of what you're supposed to see or expect to see at that moment coupled with what's
*  actually kind of raw information coming in. And that gives you a higher granularity, better
*  inference of what's happening. So this, I think, you know, is probably widely agreed upon
*  among the systems neuroscience field. Now, the specifics of that would be,
*  you know, obviously depend quite a bit on what research is going on. So the mechanism of that
*  is still unknown. But the sort of behavioral idea of that, I think, is well widely accepted.
*  The AI field, by and large, has not been able to leverage this sort of top down interacting with
*  bottom up in training and inference mode of their neural nets. I think there's an interest,
*  and everyone kind of see the benefit of that. It's just not very clear how to get from where
*  we are today in deep learning to something that has a much richer coupling of expectation and
*  memory, in a sense, influencing what is inferred from inputs from just the raw inputs. So I think
*  that that's a case now where we're seeing that the neural net community definitely would like
*  to go in this direction. And the neuroscience field has been thinking deeply about it for a long time,
*  but we just do not have the sort of insights and mechanisms ready to translate yet. And hopefully
*  those will come about in the next few years. I mean, all of these things, there is some
*  preliminary work and there's still a lot of potential to be done on all these little steps
*  that were not little. Oh yeah, yeah. I mean, people are definitely trying all of these. I'm
*  not making them up. Yeah, no, it's not coming. It is speculation coming from a very educated
*  background here. So, okay, so that's the Bayesian neural algorithms that incorporates this almost
*  sort of predictive coding top down approach here that's missing in deep nets. And then the next
*  one is dynamical memory and control algorithms. What's this about? So this is something where
*  if you look at what I think is really the exciting stuff out of neuroscience in the last
*  10 or 15 years, as we've been able to measure hundreds if not thousands of neurons in given
*  regions, what we see is that there's a lot of structure in how these neurons interact
*  in kind of a dynamical regime. So people like to talk about sort of manifolds of activity and some
*  of the buzzwords that are going on these days. But I think the way to think about it is that
*  it's not a static representation or even kind of maybe a little small snippet of time that
*  represents information in neurons, but rather you have collections of neurons that as a whole
*  population represent fairly rich information about what a memory is or what motor control,
*  you know, how you want to move an arm, for instance, or how a decision should be made.
*  And so a lot of the really nice work out of say, Krishna Shinoi's group in Stanford, for instance,
*  where you look at kind of motor cortex and primates and seeing how you have very large
*  ensembles of neurons represent an intended motor action. But it's not like one neuron
*  represents the action. It's rather this collection of neurons at some population level, changing it
*  kind of in coherence with one another to represent a movement. And I think we see that
*  in decision circuits, we certainly see that in memory circuits, things like hippocampus and whatnot.
*  So I think that's fairly far out for an AI point of view. But I think it's something that we're
*  starting to really observe empirically in the brain. And it's very, very kind of exciting to see
*  coming out of neuroscience right now. Okay, yeah. And as these sort of steps go on, the more almost
*  more speculated the less we know about what how it might develop and how we might move forward on
*  it, obviously. But so the next step is multiple steps, sort of that you can it's like the unknown
*  future, essentially. And you talk about cognitive inference, algorithms, self organizing algorithms,
*  and beyond. Yeah, no, and I think this is where you start seeing all of this come together.
*  You know, the brain we know, has dynamics, and is doing coupling top down and bottom up inference,
*  and, you know, is learning on the fly at many different timescales, is doing all of this in
*  every region at the same time. And there's just we're nowhere close to that in any AI system today.
*  But, you know, we're starting to see people think about that, right, you see DeepMind,
*  some of their really nice work on AlphaZero, where they actually have like systems, you know,
*  different neural systems interacting with one another at different timescales in order to solve
*  some of these games. The models are relatively straightforward, fairly conventional, given the
*  techniques that that people use today. But the sort of system view of it where you have
*  the coupling of these different approaches, working together to solve hard tasks, is exciting. And I
*  think that as we are able to fill in the gaps more on neuroscience, we can start seeing more
*  impact in those fields. This is great. So, I mean, I really encourage people to we really just scratch
*  the surface, you know, what what you talked about in the paper, what have you had a lot of interaction,
*  a lot of feedback from people in the computing world, you know, what are they in general think
*  about advancement via neural inspiration? So I wrote this paper for the computer science field,
*  it was mostly because we hear a lot in neuroscience about kind of, hey, this great
*  stuff happening in deep learning or whatever, right, we hear a lot of the buzzwords, but we
*  often don't know what the details are. And the computer science field, they're, they're in the
*  opposite position. They hear a lot of okay, here's a big finding out of, you know, neuroscience,
*  it came out in science. And, you know, the cnn.com article says that they, they figured out how the
*  amygdala works or whatever. And clearly, we haven't done that. And so I was trying to bring
*  neuroscience in a more grounded way to the computer science field. And I think when I've
*  talked to computer scientists, that's what they want. So the challenge is, you know, they're not
*  educated in biology. They're definitely not educated by large in neuroscience, they know that they need
*  to go in this direction, or a new direction. And this one makes as much sense as any of them. But
*  they don't have a roadmap. They don't know what's possible. They don't have a filter for what's real
*  and what's fake. Yeah, they need a fake news sensor on all of the pop stories out of the brain,
*  right. So they think the computer science field is open to this for the, with the caveat that they
*  want real world impact at the same time. So what they want to see is they want to see that the
*  brain, you know, they think the brain is going to be something they have to worry about in the future.
*  They don't think they need to worry about it today. They kind of want to know when they need
*  to worry about it. Or they want to know that other people are doing that worrying for them.
*  Yeah. Well, interesting. So but but they haven't been antagonistic toward it,
*  or Moore's law, ending deniers or something. No, I think most computer scientists who are well read
*  in things like Moore's law, and it's certainly not all of them, but most who have paid attention to it
*  acknowledge that novel directions are needed. And we should just look at the fact that,
*  you know, up until 10 years ago, neural networks were a niche technique within computer science.
*  Yeah. And most computer scientists rolled their eyes if anyone said I have a neural
*  network to solve that. Well, that's yeah, because there hadn't been that many successes
*  in that niche yet either. Yeah, there were a lot of big failures of that niche, too. And
*  so what happened was they started showing really big success in the field kind of gravitated
*  towards that. Yeah. I think that that has made them open to neuroscience as a whole. Most of them
*  aren't going to know the distinction between a deep learning net and the brain. They're not surprised
*  if I tell them that the brain is more complicated than a deep learning network. But I think that,
*  you know, why they need to look beyond deep learning, you know, they're open to that. And
*  they kind of like the idea that there is more to come. But, you know, it's far away from what they
*  do. Right. So I think they want help. They want the neuroscience field to kind of show them what
*  it is they need to do. So there's so much to learn. And learning takes time in so many different
*  fields. And it's really difficult to be an expert in neuroscience and an expert in AI and an expert
*  in computer science, for instance. So when I went to my undergraduate, there wasn't even a
*  neuroscience undergraduate degree. That's changed since. You know, at the time, there were a bunch
*  of biology degrees. None of them were even neuroscience. But now I find myself wondering,
*  you know, when will there be a degree that is basically a joint program of neuroscience
*  slash AI slash computer science? When's that going to happen? And do we need it?
*  I think we need it for graduate school now. You know, I've benefited immensely by being part of
*  a kind of an experimental computational neuroscience program at UCSD that Terry
*  Sienowski had started within the neurobiology graduate construct there. So my graduate degree
*  was in computational neuroscience. It had elements of what we would call machine learning today.
*  But it was mostly neuroscience with a more computational bent. And I think we need more
*  of that. And I imagine more of that is starting in some of these more forward looking university
*  programs, probably is like specializations. For undergraduate, I don't know. You know,
*  undergraduate degrees, you want one that there needs to be a real world benefit of having that
*  degree if someone does not go to graduate school. Yeah, right. And, you know, we see more and more
*  of that for neuroscience now with especially, you know, healthcare applications in neuroscience and,
*  you know, even things like, you know, finance and AI jobs, you know, someone who comes out of
*  neuroscience with some programming skills, you know, they can probably do well for themselves,
*  as an undergrad. Like you say, these are complicated fields, and they're complicated for fairly deep
*  theoretical reasons, especially at the intersection of neuroscience and computing. So undergraduates
*  being exposed to both is invaluable. But whether that should be a degree or not, I think time will
*  tell. Just something to bring those, because right now what we have is a bunch of different people
*  specialized in different areas. And I'm just envisioning somehow to bring the Renaissance
*  person back in that realm almost, you know. Well, I think the thing that I would, in hindsight,
*  that I would have done, you know, if I knew what my career was going to be, which of course you
*  don't, but if I had known, I think fundamental theoretical computer science classes, at least as
*  a grad student, probably would be very beneficial to anyone interested in systems or computational
*  neuroscience. Because what theoretical computer science tells you, and I've learned since then,
*  is that it really provides concrete foundations of what is and is not computable with what sorts of
*  resources. And the brain has to obey those laws. So there, you know, there are certain things that,
*  you know, the brain solves very hard problems, but it has to solve them with, under the same
*  sort of constraints that a von Neumann machine has to solve them, a Turing computation-based
*  machine has to solve. And I think that foundational theoretical insight is probably as important to a
*  neuroscientist thinking about the computation of the brain as, say, a basic physics laws. You know,
*  Shannon information is probably as critical as understanding what diffusion is. So I think that
*  sense, bridging those fields, at least as a graduate program and thinking about fundamentals
*  of computation is very important. So is that how you, if you had to start over, is that how you
*  would proceed then? I mean, I would, I mean, what I would do is I would make sure to expose myself to
*  that world. Yeah. A lot of what I think neuroscientists are struggling with are things
*  that were basically struggled with by the computing field many years ago, just cast in a different way.
*  The computing field and the neuroscience field have stayed fairly distinct,
*  historically, because both have been very successful. There's a lot of physics that
*  gets into neuroscience, but not a lot of computing that gets into neuroscience. So I would have
*  personally bridged those two more actively than I did. What is something that you used to believe
*  that you think now is naive? One thing that I used to strongly believe in was the sort of power of
*  large scale simulations for kind of bridging the understanding gap of the brain. I see. So,
*  you know, and I, because that's what I worked on. So of course you're kind of a
*  de facto believer in what you work on. And I remember asking somebody, why don't you see
*  more of this? Why don't you see people building biologically realistic models at large scale?
*  Why I say I was naive is at the time, you know, I was in a well-resourced lab as a graduate student
*  with the freedom to do that. And what I see now and what I can really appreciate now is that
*  the both the data cost and the time cost of doing those sorts of studies is very risky for most
*  researchers. So, you know, I do believe that, you know, if you look and say, and you'll pick a brain
*  region, you know, medial septum, right, random brain region, there is a lot of anatomy and
*  physiology literature and behavioral literature manipulating that brain region. There's not a lot
*  of literature out there to build a fairly strong model of almost any region. I could build one of
*  the medial septum, but I'd have to commit six months of my life to it. Yeah. Or more. And I've
*  done it before for another brain region. So it'd be faster for me. And the thing is, is that it's
*  not a scalable approach. It's not really fair to tell grad students to commit their career to this.
*  Yeah. Because they may not get anything out of it. You may not. You know, we may not have the tools.
*  We may not in the end may not have the right data for it. And so, you know, a lot of people chase
*  this dream of building the bigger and bigger simulation or say that's a dream. And I think
*  that you run the risk of ending up with a big bag of nothing at the end. You know, I think I was lucky
*  that we got very good publishable results that influenced experiments. But, you know, to do it
*  over again, I don't know if it was a smart risk to take. And so I certainly was naive to think that
*  that's what the field needed more of. Yeah. I don't think the sort of culture and resource
*  structure for neuroscience is right for that. At least for today. Do you think that deep learning
*  is overblown? No. Deep learning is making huge real world impacts. It will continue to do so.
*  It is step one in your steps of the paper that we talked about. So, yeah. Yeah. I think it is just
*  step one though. Yeah. I think that it's not, I don't think we put a bow around the brain and say
*  it's done its thing on computing. Let's move on. How do you, there is so much to keep up with,
*  you know, so many, I don't know how many papers are published each day posted just on archive,
*  for instance. How do you keep up with this blistering pace of progress in the fields as
*  diverse as you want to keep up with, like neuroscience and AI and neuromorphics?
*  It's hard. So I will say that within the neuromorphic field, it is small enough
*  that I'm able to keep track of the right people and with the conferences that we're part of.
*  Yeah, that helps. For neuroscience, you know, I actually find Twitter to be a really good filter.
*  You know, just a certain amount of Twitter buzz around a paper usually will attract my attention
*  to it. Sure. Which is, okay, 140 characters, I guess 280 characters or less to sell a paper.
*  I'm probably missing a lot and I certainly am. But every once in a while, you see some real good
*  nuggets come through and that's probably the best filter I have. And I think similar for AI,
*  the Twitterverse is probably the best. It does seem like a lot of academics and especially
*  neuroscientists seem to use Twitter in that same way. Yeah, I mean, there's so much out there.
*  Ideally, everyone would have more time to kind of just sit there and go through everything. But
*  it, you know, crowdsourcing probably is the most efficient way to do it.
*  What's something that you are 95% sure about?
*  I would say that I'll say I'm 95% sure of it, but it'll be a controversial statement.
*  Good, good.
*  Is that our ability to understand brain diseases, especially a number of the really hard to kind of
*  identify molecular mechanisms things, things like depression and schizophrenia and so forth,
*  is going to require a deeper computational view of how the brain works. Like I truly believe that
*  these are diseases of computation in a sense, neural computation. And the only way that you're
*  going to cure a disease of neural computation is if you understand the neural computation.
*  I don't know if that's a, you know, I don't think that's a universally agreed upon view.
*  I'm pretty sure NIH does not. No, yeah.
*  Fun things of that in mind. But that would be, I do think that that is the case.
*  So Brad, you've spent so much time with me. I really appreciate all this time.
*  I have one more question for you in just a second, but I'm going to say you're three and a half hours
*  away from Durango. When you're coming through, if you need, I know you just had a well-deserved
*  vacation. If you need another one, head this way. We'll go ski purgatory. We'll run the Animas
*  River. Just come on and take a break. My last question for you, given what I've seen on some
*  of the nice workshop videos online and given where you live in the country, how often do you wear
*  ties with green chili peppers on them? I have one tie with green chili peppers. It probably
*  only comes out during certain nice workshop meetings. Letting people know where you stand
*  on the green chilies. You got to represent New Mexico. Well, it's green and red chilies. I think
*  both are on the tie and both fantastic additions to one's meal. Everyone in the region loves the
*  green chilies. So there you go. Had to ask. Well, thanks so much for your time. I really
*  appreciate it, Brad. Well, thank you for the opportunity. This has been fun.
*  Brain Inspired is a production of me and you. You can support the show through Patreon for a
*  microscopic two or four dollars per month. Go to braininspired.co and find the red Patreon button
*  there. Your contribution will help sustain and improve the show and prohibit any annoying
*  advertisements like you hear on other shows. To get in touch with me, email paul at braininspired.co.
*  The music you hear is by The New Year. Find them at thenewyear.net.
*  Thanks for your support. See you next time.
*  You trust the sky. You must like your lies from blue eyes.

---
Date Generated: April 19, 2024
Transcription Model: whisper medium 20231117
Length: 5447s
Video Keywords: []
Video Views: 613
Video Rating: None
---

# BI 184 Peter Stratton: Synthesize Neural Principles
**Brain Inspired:** [February 19, 2024](https://www.youtube.com/watch?v=pQWHZDQQSLs)
*  And that's where I really started sort of solidifying my ideas around what you might
*  call biological neural computation and how different it was to, or how different it is
*  to, you know, standard artificial neural networks and machine learning.
*  How much of the brain can be understood in terms of these principles?
*  Now, obviously, you can't understand the principles individually.
*  You do need to understand the principles individually.
*  But if you want to look at how the brain works, individually is not going to cut it.
*  Even your thoughts for the future are really just predictions, right?
*  It's a principle that should be understood from a brain building block perspective.
*  This is Brain Inspired.
*  I'm Paul.
*  Peter Stratton is my guest today.
*  Pete is a research scientist at Queensland University of Technology, and I was pointed
*  his way by a Patreon supporter who sent me a sort of perspective piece that Pete wrote,
*  which is the main focus of our conversation, although we also talk about some of his work
*  in particular.
*  For example, he works with spiking neural networks like my last guest, Dan Goodman.
*  What Pete argues for is what he calls a sideways-in approach.
*  So a bottom-up approach is to build things like we find them in the brain, put them together,
*  and voila, we have cognition.
*  On the other hand, a top-down approach, which is the current main approach in AI, for example,
*  you train a system to perform a task, you give it some algorithms to run, and you fiddle
*  with the architecture and the lower-level details until you pass your favorite benchmark
*  test.
*  Pete is more focused on the principles of computation that brains employ that current
*  AI doesn't.
*  So if you're familiar with David Marr, this is akin to his so-called algorithmic level,
*  but it's between that and the implementation level, I'd say, because Pete is focused on
*  the synthesis of different kinds of brain operations, how they intermingle to perform
*  computations and produce emergent properties.
*  So he thinks more like a systems neuroscientist in that respect.
*  Figuring out how to synthesize these neural principles, Pete says, will lead to better
*  AI.
*  So we discuss a handful of those principles all through the lens of how challenging a
*  task it is to synthesize multiple principles into a coherent functioning whole as opposed
*  to a collection of parts.
*  But hey, evolution did it, so I'm sure we can too, right?
*  By the way, I'll be in Lisbon, Portugal at the end of February for the CoSign conference.
*  So if you're around that conference and you want to say hi, please do.
*  Thank you to all my Patreon supporters.
*  If you want to be able to reach out to me and influence who I invite on the podcast,
*  for example, or you just want to show appreciation, consider supporting Brain Inspired through
*  Patreon.
*  Go to BrainInspired.co to learn how.
*  All right, thanks for listening.
*  And here's Peter Stratton.
*  It was actually a Patreon supporter slash listener who turned me on to a particular
*  paper that you wrote.
*  And I was going to say recently, but when I looked it up, it was actually four years
*  ago, I think, that when you actually wrote the manuscript of the paper called Convolutionary,
*  Evolutionary, and Revolutionary, What's Next for Brains, Bodies, and AI.
*  And this is a short.
*  I recommend the paper because it's short, but it's like packed full of information
*  and ideas.
*  So it was like a really pleasant read.
*  And so he sent this to me with a couple questions.
*  I thought, oh, I should have Pete on the podcast.
*  So thanks for joining me here.
*  Thank you for inviting me.
*  One of the things I find interesting when we and we're going to get into a lot of the
*  ideas that you've written about.
*  But one of the things I found interesting is that from what I understand about your
*  background is in a computer, you have a computer science and artificial intelligence background.
*  And yet what you write about and advocate for in the paper are a lot of principles to
*  build into artificial intelligence that are from the neurosciences.
*  And I just I wonder where that came from and how you came about deciding that maybe neural
*  principles could be important.
*  It started in my PhD, I think.
*  I was quite interested in machine learning way back.
*  Well, in the late 80s, when backpropagation first appeared and in my in the 90s, I did
*  my PhD and I was really interested in in neural networks, but not so much in gradient
*  descent.
*  Even back then, I was thinking there's probably other ways of doing this.
*  Gradient descent seemed like a very unbiological way of doing things.
*  And so I was more interested in this idea of self-organization, which has been looked
*  at in the past and then kind of forgotten.
*  So then I think after the PhD, I then sort of spent some time in industry.
*  Then I came back to to research and I spent about 10 years at this institute called the
*  Queensland Brain Institute.
*  And literally, I was the more or less the data scientist looking at all these all the
*  data from neuroscience experiments.
*  And that's where I really started sort of solidifying my ideas around what you might
*  call biological neural computation and how different it was to how different it is to
*  standard artificial neural networks and machine learning.
*  And when I look at the capabilities of even simple brains like flies, insects, things
*  like that, the Drosophila, the Drosophila melatnigaster that they often do experiments
*  on, I think has about 100,000 neurons in its brain.
*  And yet it has a massive behavioral and survival repertoire.
*  You know, it's amazing. And these animals seem to sleep and they do all sorts of
*  interesting things. And then the bee, you know, the standard honeybee, about a million
*  neurons and, you know, incredible behavioral repertoire.
*  You know, they communicate. They do the waggle dance to tell each other how far away
*  sources of pollen are and things like this.
*  So these neural networks are tiny compared to, you know, our large language models and
*  the biggest models that we currently work on, but immensely capable.
*  And I guess the interesting question is, how do they do that?
*  So that's what I'm most interested in.
*  I want to come back to this because the examples that you gave are all about behavior.
*  So and we'll come back to this idea.
*  But one of the first things you said was that you became interested partly at least
*  because of backpropagation.
*  But then you weren't actually interested in stochastic gradient descent.
*  But you said in the 80s when these algorithms were written down on paper.
*  But it didn't work so well back then.
*  Right. And but you were interested in it even so.
*  So so the story of backpropagation is that it kind of worked a little bit.
*  But, you know, it took like 20 years for enough data to scale up essentially in
*  computational power. And then all of a sudden backpropagation really worked to
*  train these networks. But but you saw that algorithm and that piqued your interest.
*  It did because it was so different from, you know, standard von Neumann computation.
*  Right. And it was using these things called units or cells or, you know, I guess neurons,
*  you could call these little processing units all connected together in parallel.
*  So it was doing a lot of this idea of parallel computation, which obviously is also what
*  the brain is doing at a very kind of like basic level.
*  There's some analogies there. So that's what got me interested.
*  It was like, well, I hate this is something along the lines of what the brain might be
*  doing. But it's also got to be very different.
*  So what is your just overall take then, given the massive success, quote unquote, of these
*  deep learning networks these days that are essentially built off of, you know, relatively
*  few neural principles and then a lot of computation and a few tricks and bells and whistles.
*  Are you not impressed by them like everyone else?
*  Or are you going to say, of course, I'm impressed by them.
*  But yeah, yeah, I think you called it.
*  They're very impressive in what they can do, right, especially these large language
*  models. It just seems to be a step change in capability.
*  And it's got a lot of people interested in the general public and a lot of, you know,
*  let's face it, a lot of scientists as well.
*  No one really understands how these things work.
*  We can we can build and we can train them.
*  But how do they actually work mechanistically inside is quite a mystery.
*  So they're very interesting.
*  And honestly, yet also, I've got to say the capabilities of these networks has surpassed
*  anything that I expected Gradient Decept to be able to do.
*  And I think a lot of people are probably in the same boat as me in regards to that.
*  So how has this been possible?
*  I think it's just a matter of these networks getting bigger and bigger and bigger.
*  You know, they're they're ridiculously sized now and the amount of training data that
*  you're able to throw at them.
*  I still believe that Gradient Decept is quite an inefficient way of learning.
*  It's just that we do have such huge amounts of data now and access to huge compute
*  resources, you know, data warehouses, which is what you need to actually train one of
*  these models. And I think that's just made it that's made it possible.
*  It's not it's not so much the the technology or our understanding that has progressed.
*  It's literally just it's a it's brute forcing the problem, I guess, without really
*  understanding how we're doing it.
*  Yeah, I've been trying to avoid the term brute forcing because I think I've used it on
*  the last few episodes. I was just thinking on the train ride home.
*  No, no, you should use it. But I feel like I'm overusing it.
*  So I'm glad that you used it. Right.
*  But so do you think like something like Gradient Decept then?
*  And, you know, once we build in these principles that that we're going to talk about in
*  this episode will be seen as a capable but just inefficient way of doing the same kinds
*  of things that future AI networks will do systems.
*  Yeah, I mean, that's a good question.
*  It's. You know, I would have said, I think, like I just said, it surprises me how
*  capable these things are now.
*  And this is even possible.
*  So I'm kind of like low to say that we've reached the limit or we've hit the wall.
*  Right. In terms of what gradient descent can actually do.
*  Yeah, that's that's a fool's errand, it seems these days.
*  So I think so.
*  As long as the amount of data that we have access to keeps going up and and our
*  computers keep getting more powerful or bigger, you know, bigger data centers
*  throwing out more bigger, bigger GPUs.
*  I mean, that's really what's driven this.
*  Then, you know, the potential is, I guess, theoretically limitless.
*  But in practice, you know, the fact that these models seem to be getting exponentially
*  bigger, you know, they're basically growing by an order of magnitude in size every year.
*  And the amount of power required to train them is also growing about the same in order
*  of magnitude every year.
*  And the cost is is substantial.
*  You know, it's got to the point now where it's only the biggest basically tech
*  companies can actually afford to train one of these models.
*  It's costing the order of 10 million to 100 million dollars to that's 100 million
*  you know, real US dollars to train one of these large language models now.
*  It's an insane amount of money.
*  So how much bigger can these models get before people go?
*  We just can't afford to train them anymore.
*  There's not enough compute and or money in the world to actually do this.
*  Now, there has to be a limit.
*  I'm just not quite sure where that limit is.
*  So, you know, other people have obviously recognized this and they're looking at ways
*  of making training AI or training artificial neural networks using gradient descent.
*  They're looking at ways of making that more efficient.
*  And there's certainly efficiencies to be gained in building some more, you know,
*  specific purpose built hardware and things like that.
*  But in terms of these, like multiple orders of magnitudes of improvement, I don't
*  see that happening.
*  So to come back to your original question, the world is an extremely complex place.
*  Right now, yes, learning how to generate text and even look at images and things like
*  that. It's it's it's achievable if you've got, say, 100 million dollars in your pocket.
*  But the world is way more complex than sets of images and text.
*  You know, so if you're looking at actually creating general purpose, I for instance,
*  general purpose robots and things like this.
*  Like I said, I'm not going to say it's impossible using gradient descent, but I just
*  feel like it it's going to be very, very difficult and extremely exceedingly expensive
*  to do that, at least with current technology or with anything that we have sort of like
*  it even in the pipeline.
*  So the other problem with with robots is actually gathering the training data.
*  You know, there's a huge amount of like, you know, whatever petabytes of text data and
*  images on the Web, which you can basically have instant access to.
*  But if you're trying to gather training data for for robots in the real world, you
*  really it gets a lot slower.
*  Right. And can you get enough training data for that for real to do real robotics in
*  the real world is another kind of unknown at the moment.
*  There's a lot of people working on simulation environments.
*  But again, simulation is never the same as as the real world.
*  And you can't do that. You know, you can't simulate data as efficiently as you can
*  collect it. Not not if you want it to be really real.
*  So there's a lot of impediments to.
*  What you might call AGI or at least general purpose robots, if you kind of want to call
*  them sort of the same thing, there's a lot of impediments to doing that with gradient
*  descent that I currently don't see easy ways around.
*  This goes back to you mentioning the the importance of the of the impressive
*  behaviors of honeybees and fly fruit flies.
*  And I know a behavior is important to you and you've worked on, you know, robotics
*  and. I mean, in a sense, do you think that more of X paradox is even heightened now
*  that, you know, so we have these, you know, more of X paradox is the idea that it turns
*  out that what we thought was hard to do is actually rather easy, like training AIs to
*  play good chess and go and stuff.
*  And what we thought was easy to do, like catching a ball is actually difficult to do.
*  And perhaps that's even more highlighted now than it ever has been.
*  I don't even know the current state of robotics.
*  So maybe you can catch me up to speed on that.
*  I just know that they have traditionally been lagging behind these systems that don't
*  actually need to behave in any way.
*  Right. So there's a there's a few different angles to that.
*  So there's even some work going on here in Australia, in the institute that I work at,
*  where there are some some researchers trying to make robotics move more fluidly, more
*  like people. So, you know, trying to get a if you if you look at a typical robot, if
*  you give it the task of going to a table and picking up a can, say, it moves, you know,
*  for want of a better word, it moves very robotically.
*  You know, it will approach the table, then it will stop.
*  And then this this lever will come out with a gripper on the end and it will move slowly
*  and in a straight line towards the towards the can.
*  And then it will stop and it will grasp the can.
*  And it just looks robotic.
*  Right. And so there's clearly different ways that biology solve these problems.
*  And there's people here working on that.
*  So now we've got quite an impressive demonstration that I wasn't involved in at all.
*  But basically, where a robot can be moving past the table quite, quite rapidly and
*  fluidly and dynamically actually grasp something on the table as it goes past.
*  And this is this is quite an impressive feat.
*  And when you see the when you see the videos, it's it looks really, really different.
*  It looks organic. So this this has not been solved using
*  terribly many neural networks or biological sort of motion and muscle principles.
*  It's still going back to kind of like first principles in robotics, but doing it in a
*  very, very clever way.
*  What are those like feedback loops?
*  Yeah, it has to be closed for a start.
*  Yeah. And you basically you're continuously sensing your position and your gripper
*  position relative to the object you want to grasp.
*  And it's all about closed loop and dynamic updates and things like that.
*  Yes. Which, you know, it's kind of like a no brainer, really, when you think about it
*  when you see the demo, you go, yeah, why hasn't it always been done that way?
*  I think. And again, this is one of the first problems in robotics.
*  It's it's a lot about sort of breaking a problem down.
*  It's this like divide and conquer.
*  And it's the yeah, it's the stepwise refinement that engineers like to do to kind
*  of like isolate problems and and go, OK, well, the first step is to get to the table,
*  you know, and then the second step is to work out what I need to grasp.
*  And the third step is to put my gripper close to the cup, you know, and things like
*  this. And engineers like to break this down.
*  And that's not how biology does it. So again, it seems to be quite often the case
*  that if you take inspiration from biology, you can actually solve these problems
*  in a much more dynamic and robust fashion.
*  And I think that's what the team here has been trying to do.
*  So that's one of the issues, I guess, with robotics.
*  It's just not fluid. It's too.
*  Overly engineered, which basically means that it looks robotic and the solutions
*  are often brittle.
*  Now, obviously, the brain.
*  Sort of uses the same principles of robustness and closed loop control.
*  But the processing behind that is very different.
*  And that that leads into the second thing about robotics and why I think robotics is
*  probably useful for AI is because our intelligence is actually built on controlling
*  our body in the world.
*  You know, this whole capacity we have for things like abstract thought and language
*  and all that stuff, the amazing high level abstractions that the human brain and other
*  higher animals can do didn't come out of nowhere.
*  And it didn't it didn't appear.
*  It didn't appear in an isolated sort of environment.
*  It appeared in the world, in the physical world, in bodies that are actually needing
*  to survive in the world.
*  And it seems like a lot of the principles, the computational principles that are used
*  by much simpler animals are actually kind of like adopted and co-opted into the
*  higher level processing that our brain is capable of doing.
*  So if we want to understand intelligence, whatever that actually means, I mean, it's
*  obviously very hard to define, right?
*  Thank you. Yep.
*  If we want to actually understand it then and even come up with a good definition for
*  it, right, then then we really need to be looking at simpler animals and how they
*  process sensory stimuli and control the body in the world and then how we can co-opt
*  some of those principles for higher level processing.
*  And that's exactly what our brains seem to be doing.
*  So that that leads to this.
*  Maybe you wanted to bring it up.
*  Sorry, maybe later. But it's the idea of the embodied Turing test.
*  Quite a few eminent AI researchers have kind of alluded to recently in a nature
*  paper a couple of years ago, basically saying that if we want to understand
*  intelligence, then we really need to understand how simple creatures survive in the
*  world and then build up from there rather than diving straight into these high level,
*  sort of like symbolic reasoning processes that the human brain is capable of doing.
*  Start simple and see how that leads to our capabilities.
*  Right. And and the understanding of the nuts and bolts behind the high level
*  reasoning that we're capable of doing is what we're currently lacking.
*  So it's there's a lot there to respond to and digest, actually.
*  So I recently had my friend John Crackauer on the podcast and he's a neuroscientist and he actually argues directly against that.
*  So I am I love the idea of thinking of higher cognition and thoughts as analogous to internalized movements.
*  Right. And and it's interesting that you know, we started off talking about feedback loops and robotics.
*  Actually, I had a guest on many moons ago now, Henry Yan, who thinks that neuroscience essentially needs a revolution,
*  like a paradigmatic revolution in the Kuhnian sense in terms of thinking of cognition as just nested,
*  hierarchical feedback loops essentially all the way up into our cognition, which is in line with that idea of thought as being analogous to internal
*  kinds of movements or actions. Right. But John argues that he thinks it's ironic, for example, that, you know, the the latest great AI is built on not on things like that,
*  not on things that are that lower, lower animals, other smaller mammals, et cetera, are capable of doing, but are built on what we as humans are capable of doing.
*  And that there might very well be and he argues that there is a break between understanding how things move in the world and those principles and the principles of higher level cognition,
*  that there's likely a that they're just worlds apart to him.
*  And he he doesn't agree with the idea of the embodied and active, the 4E approach to studying as that as a gateway to studying higher cognition, essentially.
*  So do you I mean, do you think that there's like just a stepwise way from of going from where you know, from simpler animals?
*  That's a better way to say it. And studying how they survive and move in the world to higher cognition or will they need to be different principles that we'll have to grapple with and understand?
*  It's interesting. I find it interesting that a neuroscientist will actually have that point of view.
*  To me, when you look at the brain, right, and I like I said, I spent 10 years in a brain institute, this idea that that, you know, what you might call thought is really just internalize and abstracted action, right?
*  Which is something you just said, and it's also something I mentioned in the paper that we're discussing.
*  Yep.
*  That just makes sense from there's a lot of evidence that that is kind of how the brain works. And it's how we behave as well.
*  So in terms of how the brain works, if you look at the brain, you know, the the the frontal lobes where you know, basically most of our actions are represented, you could say at a very coarse level, you know, the front of the brain, the frontal lobe is, is more for action and movement.
*  And the back of the brain is more for perception, sensory perception. So, you know, that that's always a very coarse generalization. But you can start with that. And then if you look at just forward of the what's called the central sulcus,
*  central sulcus.
*  Yeah, that's the line that goes this way across across your brain that basically divides the front half and the back half of the brain. So directly forward of that is your basically your muscle representation, you have a representation of all the muscles in your body. And again, it's like the sensory
*  homunculus, it's basically laid out in the shape of a body in your brain. And triggering those neurons, if you stimulate one of those neurons with an electrode or something, it'll cause a muscle twitch somewhere in your body. So you can map out this you can map out this body map in the brain.
*  The homunculus. Yeah, yes. Yeah. Right. So as you go forward from there, you go from that's called motor and motor region and one, as you go to m two, basically, these are combinations of muscle actions that occur at the time, say, so, you know, repetitive, easily repeated, well memorized movements are represented there. And these neurons tend to fire, you know, like a few hundred milliseconds before the actual motor neurons fire when you're about to do an action. And then as you move further and further,
*  forward, in your in your frontal lobe, basically, what seems to happen is you're getting longer and longer sort of temporal representation. So representations of in time of movements that you are potentially going to do further in the future. So you know, you have a you potentially have a I'm going to go shopping kind of like neuron somewhere in the brain. And it's not it's obviously it's not a grandmother neuron. It's not that simple. But there is some representation in your frontal lobes of doing the action of going shopping, or driving
*  a car or things like this, you know, some very high level neurons in your brain. And all these things are basically, you can call them abstracted actions, or delayed actions or compound actions or something like that. You could also call them in a way concepts, right. And this is where a lot of concepts are actually tied to what that means for us as an embodied agent in the world. And these high level concepts really stem
*  from just delayed and abstracted actions. And you can see that, you know, even, you know, like phylogenetically and evolutionarily in the way that brains have developed over time. The simpler vertebrates, for example, have very small, you know, frontal cortices or almost no frontal cortex at all. And then the more ability you have for abstract thought is this frontal lobe that's really exploded in humans, right.
*  And it literally just builds off the simpler actions that are represented in in the brains of simpler animals and also in our brain in the lower level regions of the frontal cortices. So that's kind of like the, that's the evidence from the neuroscience perspective, in any case, that this is what's going on. Everything stems from low level actions, in terms of the structure of the brain from low level concepts and low
*  level actions up to high level concepts and high level actions. So everything, if you think about everything we do and everything we think is really just ultimately leading to some sort of action, right. It can be action like, you know, we can make plans for the years or decades in the future. And that's our brain.
*  Simpler animals don't have the capacity to think that far ahead, you know, and the very simplest ones are simply like, you know, stimulus response, you know, like mollusks and things like this, right. They have very simple nervous systems, but no ability to abstract into the future. So there's definitely evidence from neuroscience that kind of shows this. And also when you look at even at the structure of the brain across the cortex, from these low level motor regions up to the very
*  high level regions, the structure is also really, really strikingly similar in the across the across the entire motor or frontal cortex, but also even in the in the sensory cortices, the actual structure of the brain in the cortex itself is remarkably similar, whether that part of the brain is is devoted primarily to sensory processing or primarily to, to coordinating muscle movements and motor actions and abstract thought.
*  It's, it's very difficult to tell unless you're an expert, you know, by looking at a slice of cortex and by looking at sensory cortex or motor cortex, you know, it's often quite hard to tell. So there's, there's really, really similar processes going on in all these different parts of the brain.
*  So if you're saying that there's something very particular that humans can do in terms of abstract thought, you need to explain why that would be the case when the actual substrate that seems to carry that out is the same across across all brains.
*  Yeah, I'm not saying that he's saying that he has the solution. But, you know, so, for example, and we don't need to harp on this for long, but the example that he regularly gives is, you know, if I tell you to go to imagine standing outside your own home, and then we're going to have to go to the hospital.
*  And then you're walking through the door and going to the kitchen to get a butter knife, then opening the fridge, you know, you can imagine all that without moving at all. And that there's simply no evidence that any other species can do this, right? That's the most parsimonious explanation.
*  So we need to be able to explain those higher level kind of processes. And he doesn't he doesn't believe that there's a continuous path from simple movement to high level thought, right?
*  Okay, so yeah, I mean, that's an interesting point of view. And obviously, this is this is, I wouldn't call it contentious, but this is undecided. Right? So there's definitely anyone who says that it's that it is decided is, you know, obviously, I would disagree with right. That's the one thing I can say for sure.
*  So, yeah, there's a there's a lot of stuff that we just don't know about the brain. And I think this this disagreement that I have with this guy would would obviously be just an indication of that. So it's no problem. It's just the way science works.
*  Right? Yeah. Quickly haven't asked this of anyone in a while. Where are we? Do you think in neuroscience and understanding the brain? Are we at the beginning? Are we in the middle? Are we close to it?
*  That's a difficult question. I would say it's it's it's a bit of a cliche to say, but it's it's the more we understand about the brain, the more we know that we don't know. Right?
*  God, I said this exact phrase that again, that's another thing I'm trying to not say frequently. So I'm glad you're saying I got to apologize. I knew that that was a bit of a cliche, but it's kind of true. Right? Yeah. So you know, my kids have asked me the same question. How far are you to compare?
*  I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I'm not sure. I
*  any other information that comprehendаю
*  Curse
*  all
*  almost exactly water
*  just show how he gets with
*  but how all holds together
*  the emergence
*  dynamics and the emergence properties of the brand
*  I'm
*  And that's what we don't understand.
*  And that's, is that neuroscience even,
*  or is that computation or engineering or physics?
*  There's a lot of physics involved in this as well.
*  Physics is a lot about emergent properties
*  and emergent dynamics even.
*  So, in the end, it might not even be a neuroscience problem
*  or you have to redefine what you mean by neuroscience.
*  It's more like what I'm interested in,
*  which is neuroscience and neurocomputation,
*  I guess, in neuro AI.
*  But it's really kind of like a separate field
*  to neuroscience because we take what we know
*  about the brain from neuroscience
*  and then we try to construct models
*  and understand the emergence that's going on.
*  Before we get into, because I wanted to just jump right
*  into the ideas in your paper, but before we get into that,
*  how would you describe your overall goal?
*  Well, I mean, that's a good question too.
*  Um, I guess on what level?
*  The reason I, well, the reason why I ask is tied
*  to the way that you present all these principles
*  in the paper and it's tied to the,
*  what you just said about it really hangs,
*  or really it's about how all these things hang together.
*  And that's what we're gonna get into in a minute.
*  And so, then I wonder like, well, are you,
*  it's an ambitious goal to synthesize all these principles
*  and that we're not gonna go through all the principles
*  that you talk about in the paper, but I thought,
*  well, is that your goal to like kind of step by step
*  incorporate these things until you have them all
*  incorporated into the, and build these emergent systems
*  and emergent computations?
*  Look, given enough time, but you know,
*  perhaps like a semi infinite life,
*  I guess that would be my goal.
*  Yeah, but given that I'm probably not gonna have time
*  to do all of that, I guess it would be,
*  the goal would be to kickstart that process
*  and to get people aware of, you know,
*  what we do know about the brain
*  and how that we can actually leverage that
*  into building better AI, you know,
*  which is what this paper was all about.
*  So, you know, at one level, my goal is to just, you know,
*  enjoy what I do and follow my curiosity, you know,
*  which is kind of like, you know,
*  I guess the ultimate goal of pure science.
*  But then I guess you also need to have concrete goals
*  in order to keep yourself honest
*  and actually do something useful.
*  So in terms of that, yes, it would be to take
*  these principles and start putting them together
*  and then understand it.
*  You know that each principle alone doesn't do much, right?
*  It's only when you combine them that you start getting,
*  you know, kind of like potentially building
*  useful emergent systems.
*  And so you need to try to understand that emergence.
*  And like I mentioned before,
*  that's where we really fall down in these complex systems.
*  You know, you can't write an equation
*  that actually solves these things.
*  You really, you need to build it and understand it
*  from an emergent point of view.
*  Okay, well, like I said, it's ambitious.
*  And I'm about to read 13 different principles
*  that you list toward the end of your paper
*  at the risk of losing the listeners.
*  But I do it just because to highlight the ambition
*  and the difficulty of going down that road
*  and trying to incorporate all these things
*  so that they hang together.
*  Okay, so sparse spike time coding, self-organization,
*  short-term plasticity, reward learning, homeostasis,
*  feedback predictive circuits, conduction delays,
*  that one's not often mentioned, oscillations,
*  innate dynamics, stochastic sampling,
*  multi-scale inhibition, K winner take all,
*  and embodied coupling.
*  So I don't even know where to begin.
*  So I know that-
*  What does it all mean?
*  Well, yeah, well, it's all in the paper.
*  So I'll refer people to the paper
*  where you discuss all these principles in more detail.
*  But the idea of, so you just got done saying
*  that we understand so little of the brain,
*  but then there are these 13 principles
*  that you find are probably super important
*  to be able to build not separately, but together
*  and have everything work in a synthetic fashion
*  to generate these emergent properties of complexity.
*  So maybe we know more than we think we do
*  if we can point to these principles.
*  Personally, I would like to think so.
*  And I tried to make the list exhaustive,
*  but I think that's rather conceited
*  to actually believe that it would be right.
*  I think there are principles
*  that we don't currently understand,
*  that we don't even kind of like,
*  we have no idea of the potential existence of,
*  or the requirement for.
*  So I imagine that list is going to get bigger.
*  At the moment, I think, yeah,
*  I've tried to basically capture everything,
*  all the high level kind of like mechanistic principles
*  that the brain seems to be using to perform computation.
*  And these are the ones,
*  I'm obviously not the first one
*  to talk about these principles.
*  Each one has been independently researched.
*  And like I say in the paper,
*  some of them are quite extensively researched.
*  I might be the first one to put them all together,
*  but again, that's probably not true.
*  So it's just a matter of how much of the brain
*  can be understood in terms of these principles.
*  Now, obviously, it's not,
*  you can't understand the principles individually.
*  You do need to understand the principles individually,
*  but if you want to look at how the brain works,
*  individually is not going to cut it.
*  We're going to need to combine them
*  and have a look at the resulting,
*  I keep using the word emergent,
*  so I'm using that now,
*  but look at the resulting properties
*  of the system as a whole.
*  And that's the only way to actually understand,
*  to understand your computation.
*  When we do that,
*  so when we do start putting them all together,
*  and this is one thing I do say in the paper,
*  there haven't been very many attempts
*  to actually put these principles together,
*  even though individually they've been,
*  some of them are reasonably well understood.
*  The real value in understanding these as mechanisms
*  is when we try to unite them
*  as the brain has done quite successfully.
*  So when we start doing that,
*  I think it's going to be quite likely
*  that other principles will emerge,
*  or at least the requirement for other principles will emerge,
*  because we'll put these things together
*  and the models still won't be working like the brain.
*  Something will go awry,
*  or something will just not work at all.
*  And in which case we can then,
*  we have the ability then to look at the model
*  and go, well, what seems to be missing?
*  And then we can look back to neuroscience
*  and this is quite often what happens.
*  You build a model and for instance,
*  a model of STDP,
*  the spike timing dependent plasticity,
*  and then you realise that, okay, STDP is pretty much unbounded.
*  These synaptic connections are more or less unbounded
*  in pure theoretical STDP.
*  And that can't happen in the brain.
*  There has to be some sort of normalisation process going on.
*  And of course, we have normalisation in our deep networks, right?
*  And that comes about purely through an actual practical requirement for it.
*  And the same happens in the brain.
*  So then you start looking at things like,
*  okay, there must be homeostatic processes in the brain
*  and it turns out there are, there are a heap of them
*  that do basically the normalisation.
*  They do it in a more biologically realistic way, obviously,
*  rather than just summing weights and dividing by the number of weights
*  and whatever, doing L1 or L2 normalisation.
*  The brain is not doing that.
*  But it has a similar ultimate functional goal
*  of normalisation in artificial neural networks.
*  So that's where the homeostasis comes in.
*  You realise you need the mechanism
*  so you can look to biology to go,
*  okay, how does biology accomplish this?
*  And quite often the information is there already in neuroscience.
*  You just need to basically digest and absorb that into your model.
*  And there will be other things, other principles
*  that we're going to need to incorporate.
*  I can be almost certain about that.
*  I mean, the ones that I just listed off also are,
*  they do sound like a bottom-up approach, right?
*  They sound like kind of low-level mechanistic processes.
*  But you write in the paper that what you're taking
*  is a side-in approach.
*  Sideways in.
*  Yeah, sideways in approach.
*  So maybe you could just describe that,
*  because it does sound like a list of lower-level processes.
*  Well, they're sort of low-level in as much as you can name them.
*  And the homeostasis in some cases is like normalisation.
*  But mechanistically, that can actually embody
*  quite a complex biological process underneath that.
*  And that doesn't necessarily need to be modelled
*  from a bottom-up point of view.
*  So the functional goals of some of these mechanisms
*  potentially implemented with very complex biological mechanisms.
*  You don't need to actually do that in a bottom-up, faithful sort of fashion.
*  You can sort of abstract the functional goal out
*  and just do that in the simplest computational way possible.
*  So that's kind of what I mean by the sideways in.
*  So when it comes to the modelling system called neuron,
*  that models physical neurons and channel densities
*  and this sort of thing.
*  Ion channels.
*  Yeah, ion channels and dendrites and axons
*  in actual, their full 3D glory.
*  I don't think we need to do that to understand
*  at least the basics of neural computation.
*  You know, there's obviously nuances there.
*  And I think if you wanted to actually reproduce
*  a specific brain, for example, well then yes,
*  you're going to need to model those things.
*  But if you just want to model neural computation
*  at a core scale, you probably don't need to do
*  that level of biophysical detail, I would say.
*  So that's what I mean by not doing the bottom-up.
*  Some of these processes, like I said,
*  very complex biologically, but we can actually
*  just abstract them away.
*  And as long as you get the really important thing
*  then is what level of abstraction is sufficient.
*  And what level of abstraction is too much.
*  Because at some point, if you abstract too much away,
*  then you start losing some of these emergent properties.
*  And you don't want to do that.
*  Yeah, well, that was maybe my next question is,
*  I mean, you look at a list like this
*  and these are all biological processes.
*  And then you think, okay, I'm going to abstract away
*  what's unnecessary from them all
*  and then somehow piece them together.
*  But this is something that evolution has done
*  over eons and eons and eons.
*  And it just seems like a tall order for us to,
*  and maybe a bit of hubris for us to be able to say,
*  okay, well, I'll just take all of these things
*  and I can just program oscillations in this one program
*  and then I'm going to merge it with homeostasis
*  in another program and reward learning with another program
*  at a abstract level that feels comfortable to me
*  without even knowing whether the biological process is,
*  what levels are important for their integration, right?
*  Yeah.
*  So, yeah, that's obviously a very, very good point.
*  And that comes back to,
*  probably other mechanisms will be required.
*  Probably some of these mechanisms
*  will need to be broken down into simpler sub mechanisms
*  when it comes to it.
*  And I think it all just comes down to the fact that
*  we don't know what these models will do until we build them, right?
*  Because there is complexity science,
*  trying to understand the science of complexity
*  and emergence is really in its infancy, right?
*  So it's just one of those things where you've got to build it and see,
*  and what's it not doing, what's not working.
*  So when I say oscillations, I think oscillations are themselves
*  an emergent property of neurons and networks and spikes.
*  And inhibitory, GABA, expressing neurons
*  in combination with the excitatory, you know,
*  AMPA expressing neurons and NMDA.
*  And I think all these things,
*  oscillations themselves are an emergent property.
*  I wouldn't want to be building oscillations
*  at a given frequency into my model.
*  I'd want that to be an emergent property
*  because I think that's really important for, you know,
*  this communication through coherence idea,
*  where basically what that means is that different brain regions
*  will oscillate in synchrony when they need to communicate.
*  And they'll go out of phase or oscillate at different frequencies
*  when they don't need to communicate.
*  And it's a very, very powerful idea.
*  And this is one of those ideas that I think hasn't really been used in AI at all.
*  You know, we're even, we can simulate the dynamics of this.
*  Of these processes in the brain.
*  But in terms of utilizing them for computation,
*  as far as I know, no one's ever tried to do that.
*  At least not at more than a very sort of basic level.
*  So I wouldn't want to program the oscillations in.
*  Oscillations are something that I want to have emerge
*  because you never quite know when two brain regions are going to couple,
*  you know, through synchronous oscillations
*  or phase shifted oscillations as they need to do.
*  So these sorts of things are just things you need to build and see how it works.
*  But so oscillations is a good example also where there's plenty of work
*  looking into the potential causal properties of oscillations.
*  You know, so yes, they're an emergent property,
*  but then they can have a top-down effect on these lower level components as well
*  as being generated by the lower level components.
*  So there's this inter-level play that again,
*  it seems like it's going to be daunting to find that right excitatory inhibitory
*  balance, you know, within a layer coupled with the homeostasis
*  and for those oscillations to have the right effects
*  when they need to have the right effects for the honeybee to do the waggle dance.
*  You know, right, right. Good point.
*  So I think this is actually something I allude to towards the end of the paper
*  is that there is this idea that the more principles that you start
*  incorporating into your models, the more complex the model becomes
*  and the harder it is to tune or to get to do anything.
*  That's certainly, you know, that's certainly a relevant concern,
*  but the opposite might also be true.
*  If you do incorporate the right principles, for instance, some of this homeostasis
*  at potentially multiple different levels, because you mentioned levels as well
*  and that's another very interesting point.
*  But if you do incorporate these principles, sometimes they become synergistic
*  and they just work when you get the combination just right.
*  And homeostasis is a good one.
*  In the models I'm building right now, I do have, you know,
*  some simple homeostatic processes going on.
*  And it's amazing.
*  Is this spiking neural network models that you're currently working on?
*  Yeah. And it's amazing how far you can push some of the other parameters in the model
*  in terms of things like synaptic weights, for example,
*  or the number of connections each neuron has.
*  You can change some of these parameters that should wildly affect the dynamics.
*  But in the end, ultimately, they don't.
*  The network just finds a happy operating point somewhere in the parameter space
*  due to the interplay between things like the homeostasis
*  and the causal strengthening of synapses between neurons,
*  despite timing-dependent plasticity.
*  It will simply find a happy operating point due to the interaction of these mechanisms.
*  And if you take one of the mechanisms out, the model then actually becomes quite unstable.
*  So it's actually when you put all these,
*  when you get the right combination of mechanisms in there,
*  it actually all just seems to work.
*  And I really believe, you know, the brain, this is exactly what's happening in the brain.
*  The brain is at this sort of like, and this is where a lot of the physics comes in.
*  And this is one reason why there are some eminent physicists who have gone into neuroscience.
*  Because the brain dynamically seems to be operating at a critical point in its dynamics,
*  at a phase transition basically, somewhere between seizure and random noise.
*  It seems to be where the brain is operating.
*  And our brains thread that needle really, really well.
*  And that's why…
*  Robustly.
*  Very robustly, yeah, due to, it would seem, a lot of these homeostatic mechanisms.
*  And things need to be pushed way out of the operating region in order for, you know,
*  diseases like epilepsy, for example, to manifest.
*  Because the brain is just so good at maintaining its dynamics in this critical
*  region of phase space.
*  And so the reason it's able to do this is through these homeostatic mechanisms.
*  And if you can identify the right mechanisms, I think it will all just self-adjust, right?
*  So the reason that spiking networks have been thought of as being, you know,
*  difficult slash impossible to work with.
*  And everyone basically, everyone who, a lot of people who've had a go at
*  modeling spiking networks, ultimately kind of like give up and go back to either deep learning or
*  doing gradient descent with spiking networks, for example, to try to like shoehorn that learning in
*  there, you know?
*  And the reason being that they haven't actually just got the right combination of
*  homeostatic principles and some of these other mechanisms.
*  When you get it right, it just works.
*  And that seems to be a fundamental principle of the brain that we really need to be
*  cogent of, I think.
*  It's really, you get that right, and then suddenly things start falling into place.
*  This is a bit of an aside, but I'm sure some listeners are thinking, well, what about
*  all of the psychological difficulties people are having, especially these days?
*  If it's so robust and it just falls into place, why is psychosis up more than ever?
*  Why does everyone have ADHD?
*  Why are we all depressed?
*  Why, you know, I'm not sure if that's a fair question to ask you at this point,
*  because I know you're not a psychologist, but one does wonder, you know, thinking of
*  higher cognition and is there a continuum or is there a break and it's an emergent sort of property?
*  And then, oh, are we really that robust or have we passed some point that now we're,
*  you know, skating on thin ice, et cetera?
*  Yeah, okay, so now we're kind of getting into, I guess, you might call it social neuroscience.
*  I'm certainly interested in all the different neuroscience fields.
*  I don't know terribly much about social neuroscience, but I think, yeah, we are pushing
*  the limits of what our brain has sort of evolved and is capable of adapting to, you know?
*  The world has changed so much in the last even 20 years, you know?
*  And definitely, like, incredibly, like, it's unrecognizable from, say, 100 to 150 years ago.
*  In terms of the stress and strain we're putting on our brain with, you know, always on and
*  always connected and social media and things like this, it's just not a natural environment.
*  It's not what the brain is.
*  Maybe it's too much leisure time now.
*  Maybe we have it too, you know, things are too good.
*  They're better than they've ever been.
*  So we don't have to think about where to get food except for the shopping list.
*  Right. Yeah, I think there's definitely evidence for that too, in terms of, yeah,
*  the incidence of, say, depression and anxiety is way lower in developing nations, right?
*  When you are actually concerned about your day-to-day survival,
*  you tend to not get depressed.
*  You can be living in horrid conditions, but because you actually have a real, like,
*  a literal goal to survive each day, you don't, you literally just don't have time to, I guess,
*  to get depressed, more or less.
*  You're too busy living.
*  And it's only when you have sort of like this time to ruminate, self-reflect and
*  be on your screen and get bored, you know, watching TikTok clips and things like this,
*  that's where these kind of like psychological problems seem to start creeping in.
*  And I would still go back to the fact that it's simply because our brain
*  has not evolved in that sort of an environment.
*  We are not adapted to live in a high-tech world.
*  I love getting out to nature, especially like the beach and swimming in water and things like that.
*  It's so calming and so relaxing. You just feel good doing it.
*  And I think there's a lot to be said. I mean, you can get into the
*  para-physical interpretations and things like that that a lot of people do,
*  but I don't do that. I think it's just because it's where we grew up as a species,
*  and I think it just feels comfortable being there.
*  Yeah. I'm not going to pretend to be a well-being guru or anything because there are like
*  debilitating psychological disorders that have nothing to do with TikTok and social media.
*  I'm not trying to shortchange psychological disorders as being all about our modern leisure,
*  lackadaisical lifestyles or anything, but there's probably something there.
*  Yeah. I agree. And there's also a lot of, as you say, there's a lot of psychological problems
*  that have been around forever as well. And again, I think there's a reason for that.
*  If everyone was the same, if there was no kind of like a... We need a distribution of traits,
*  of phenotypes basically in any species, because if everyone is specialized to
*  excel in the current environment, if everyone is perfect for whatever it is you currently do
*  as a species, then if things change, if there's some sort of like a catastrophe or a new predator
*  appears or whatever, then there'll be no one that is kind of like adept at dealing with that within
*  your species, and your species is likely to go extinct. So you do need, for instance, an obvious
*  one is you need people who are extroverted and bold and fearless, because when times are good,
*  they're the sort of people who are going to do really well in an environment, the ones who take
*  risks. Whereas if things are not looking good for you, like environmentally speaking, or there's a
*  new pathogen or something, what you really want are these fearful, introverted type people who
*  keep to themselves and don't like socializing. I'd say there's a new pandemic, for instance, back in
*  Neolithic days or something like that. You want people who basically are very fearful of this
*  in order to, because they will probably in that case be the ones who survive. So you need a broad
*  range of phenotypes, and it's a very clinical and scientific way of looking at it, but that is one
*  reason why you get such a diverse range of people. And unfortunately, sometimes these phenotypes just
*  push the limits so far that fear leads to anxiety, like a constructive fear actually leads to more
*  or less full-time anxiety and phobias and debilitating psychological trauma and things
*  like that. And it's simply a consequence, I think, of, like I said, it's very scientific and clinical,
*  but it's a consequence of having to maintain diverse phenotypes within a population.
*  So, Pete, I have you on record now saying that introverts are fearful and extroverts are bold.
*  I'm just kidding. I don't want that to be the message.
*  No, no. Not entirely true, obviously.
*  Yeah. I'm a bold introvert myself, I'll say. Yeah, we could go down a very dangerous road here and
*  get both of us in trouble, I suppose. But speaking of psychology, so you're taking this sideways-in
*  approach. And, but I wonder, so another approach is this kind of top-down approach, the functionalist
*  approach, right? Which is in large part how large language models and current deep learning have
*  had the successes that they've had because they've been trained to do particular tasks.
*  And it's through the learning of those tasks that their weights all get set in just the right way to
*  perform the task very well, right? And so in that respect, it's more about the psychological,
*  I'll use that term in air quotes, function that a network, let's say, is tasked to perform.
*  So I'm wondering if, because I don't think that you really talk about using that kind of functionalist
*  behavior, top-down psychological function approach to sort of constrain models, right? A lot of what
*  you talk about are these principles of neural computation. So are you more interested in the
*  computational capabilities or the actual functional outputs, functional capabilities? Or another way
*  to say that is do the psychological functional capabilities inform or guide you at all, like
*  in thinking about neural computation? To answer that, I should, I could potentially go back to
*  this idea of the embodied Turing test. So... Sorry, could you just explain the embodied Turing
*  test? I don't think that you explained it earlier. Right, sorry. So it's this idea that, yeah,
*  the basic idea is just to understand intelligence, we need to understand the building blocks of the
*  brain. And to understand the building blocks of the brain, we really need to go back to
*  what simple creatures do. Okay. From say, you know, whatever, the simplest, even
*  simplest animal with a nervous system, like a sea slug or something like that. Or a sea elegance.
*  Yeah. All the way up to us, but everything that's in between. Because there are many things that
*  are conserved from the simplest nervous system up to the most complex. But what's the Turing test
*  part of that? The Turing test is basically, the idea is you build robots that can do what
*  animals can do. Right? Oh, and so the Turing part of it is that I can't tell that octopus robot from
*  a real octopus or something? Correct, in terms of its behavior. Yeah, that's right. So the way they
*  frame it in the paper is more or less like animals have these competencies that we cannot currently
*  replicate, even with our best technology. And obviously these competencies are a function of
*  their brains, right? But also their bodies. And the fact that the brain is coupled with the body.
*  And of course, this is a fairly pervasive idea. Everybody knows about it, but very few people
*  actually pay it much heed or use it in their research. Right? And so what this paper was
*  calling for was, okay, we actually need to start doing this in order to understand how the brain
*  works. You really need to start simple and put the brain in a body and see what it can do when
*  it interacts with the environment. And so it becomes this entire, the feedback loop, the closed
*  loop between the brain, the body and the environment. Back to the brain, recensing. The brain does
*  perform some action in the world. It changes the next perception. The brain then processes that
*  perception and decides on the next action and so on. Obviously it's not that simple. And there are
*  multiple loops, abstracted loops going all the way up and they all interface and influence each other,
*  top down, bottom up and sideways in. Right? And that's what we need to understand in terms of
*  understanding intelligence. So it's a really completely different approach, as you said,
*  to something like a large language model, where it's basically just, well, let's just throw all
*  this text out and get it to predict the next word. And that's all that the large language models are
*  doing, but they do it extremely well. And it turns out that in doing so, they're formulating concepts
*  like humor and even like a concept of awe and inspiration and all these things that are very,
*  very hard to define and pin down. But if you tell a large language model to make up a joke, it will.
*  And occasionally they're even a little bit funny. So they've got some sort of idea of what humor
*  actually is. And they know what humor is when they see it. And they're able to even generate
*  it, novel instances of it, which is amazing. It's amazing what these things can do. But I think
*  it's a small fraction of what the brain can do. If you want to put the parallel there between, okay,
*  what part of the brain is a large language model actually emulating? I would say
*  it is literally just the feedforward connections in the cortex.
*  Wow. Okay.
*  Right? And I think now, how would I justify that? Well, you know, large language models are
*  typically, they're all just feedforward. There's a huge amount of feedback in the brain as well,
*  which is completely ignored in almost all our AI. We have very few effective recurrent models,
*  I guess, in AI. So these large language models are very good at extracting high level features
*  from their input. And I think that's exactly what the cortex is doing, both sensory and motor. So
*  perceptual feature extraction is what the sensory cortices are doing. So you take individual edges
*  at low level, say visual cortices, and they're combined into things like maybe like simple shapes.
*  And then shapes are combined into things like faces and cars. And you have representations
*  of these objects in your sensory cortices. And I think exactly the same thing is happening in your
*  motor cortex. It more like temporal extraction, temporal feature extraction, which also happens
*  in you have temporal, which means features that occur over time, you know, like moving
*  representations of moving objects and things like that, you get those in sensory cortices.
*  In your motor cortices, you have representations of actions over time. And it's doing motor feature
*  abstraction. That's sort of what I've called it. So you get perceptual feature extraction
*  in sensory cortices and motor feature abstraction in your motor cortices.
*  And it's the same process just applied to different inputs, basically.
*  So if we want to understand the brain, we really need to understand those processes. And if we want
*  to understand computation in the brain, so neural computation, we need to understand those processes.
*  And you're not going to do that just by throwing a huge text corpus out of feedforward network.
*  You know, you'll get a part of the brain, you'll get like, I think, the feature extraction,
*  the feedforward feature extraction, that's what you're getting in a large language model.
*  But you're not getting any anything else. Feedback connections outnumber feedforward
*  connections in the brain. So the feedback is obviously at least as important as the
*  feedforward, possibly more important than the feedforward connections. Then you have all these
*  subcortical connections as well. And then you have the body that the brain is tightly innately
*  coupled with. All these things influence and control and actually dictate what computation
*  in the brain actually is. And a large language model has none of that. So you need to come at
*  it from and this is what I'm advocating for. You need to come at it from a holistic perspective.
*  We're not good at that. I'm not good at that. Yeah, yeah. That's true. I mean, it's difficult.
*  It's very difficult. Yeah. It's not out yet. But I just had a researcher, Dan Goodman, on the podcast
*  and he specializes in working with spiking neural networks. And he actually thinks that now is the
*  time to be excited about spiking neural networks because of a recent development in training them,
*  which kind of mimics back propagation called surrogate gradient descent. But it is a global
*  learning rule, right? And it still uses gradient descent. But he's found a lot of success in how
*  it works. But would you agree that now would be the time to be excited about spiking neural
*  networks? Because you mentioned earlier, a lot of people shy away from them or dabble in them and
*  then go back to what works because they're tricky and can be difficult and prickly, etc. But is that
*  coming around? Are we going to see more and more spiking neural networks these days?
*  There's still a very niche kind of research project.
*  The problem is that for specific tasks, deep networks, deep learning and gradient descent
*  works really, really well. There's no argument there. And it's almost like a black box. You can
*  throw a problem at it. And because there's been so many really smart people at Google and various
*  other places working on these, the Python packages for doing deep learning, the problem is that
*  deep learning is literally a novice can almost come along now and construct a deep learning model.
*  Spiking networks are not at that stage yet. It's not that they can't be. It's just that the
*  research effort hasn't been applied to them yet.
*  Well, one of the things he says is they're still really difficult to scale up because
*  they're computationally really super expensive still. But maybe that's using that gradient descent
*  learning rule and maybe the local learning rules that you're implementing reduce that
*  computational requirements. Yeah. I think that's certainly part of it. It also comes down to just
*  not understanding all the principles well enough. Or at least there's a lot of little tweaks and
*  heuristics in deep learning, like the dropout and things like that. But they just seem to work
*  in practice and they're well implemented and you don't need to worry about it anymore.
*  So that sort of overall tweaking and heuristics and polishing to the nth degree of the
*  spiking network packages, they barely even exist now, let alone having been tweaked to the nth
*  degree. They're just not and they're not out there. So that's a big impediment, I think,
*  to further research. And the problem is that the longer this status quo is maintained,
*  the further behind spiking networks will get potentially. So it's more or less a labor of
*  love and you've really got to embrace the vision and believe the vision of what spiking networks
*  can be before you leave and spend time actually working on them. And there's probably just not a
*  lot of people who really believe it that deeply, I think, to actually take a gamble on their career
*  and go into spiking nets. It's been shown theoretically that they're more powerful.
*  It's rigorous. They're rigorously more powerful than artificial neural networks. But people think
*  they're finicky and difficult and yeah, sure, theoretically they might be more powerful,
*  but in practice they just don't seem to work. And this is what people will say. So that's the,
*  I guess, the medium-term goal is to leapfrog these chasms in functionality and understanding
*  and get spiking networks to the point where, okay, right, they do seem to work and they do seem to
*  have some advantages. And when it gets to that point, I don't think people will start
*  embracing them a little bit more easily and more often.
*  I want to hear you and more often. I want to hear your own, and I'm sorry to put you on the spot,
*  if I'm putting you on the spot, but your own roadmap in your head. So now you've got a pretty
*  good spiking neural network model and so are you going to take that and then start adding other
*  things more to it or are you going to then build a different kind of model with, say, innate dynamics
*  or something, the vision that you have to implement some innate dynamics or some self-organization,
*  and then try to marry them? Or do you see a roadmap for yourself moving forward? What's
*  the low-hanging fruit for you? What's the really difficult thing that maybe the light at the end
*  of the tunnel? Do you see that vision? So I think as a scientist, you tend to
*  oscillate, right? Sometimes you're looking at the big picture and you try to build this big
*  roadmap for yourself. And then other times you need to really bury yourself in the details,
*  right, to actually make notable progress in any one of those particular problems,
*  you really need to get there. I was going to say reality slaps you in the face then.
*  Right, right, right. So this paper, as you said, I think I loaded five years ago. It was only
*  published last year. I didn't submit it for years. It was just sort of lying around.
*  So that paper five years ago was my attempt obviously at the grand vision. Now I'm kind
*  of buried in the details. So when you ask a question, what's the big roadmap? Well,
*  what's tomorrow bring? Yeah, exactly. It's a difficult question. I think a lot of it is
*  spelled out in the paper in terms of incorporating all these mechanisms. 13 of them, I've never even
*  counted them. So that's interesting. Yeah, well, I actually enumerated them because they're listed.
*  And yeah, but the order of adding them, right? So that's why it's so ambitious because like,
*  how do I even begin? What is the easiest thing to begin with? What are the two things that I think
*  I could get to integrate well in a model to get them working? And so it's difficult to know what's
*  most important on the list. What's easiest, et cetera?
*  The models I'm currently building are using sparse spike coding, spike timing dependent
*  plasticity, and homeostasis. So firing rate homeostasis. So each neuron has a set firing
*  point that, or a number of spikes at a time it would like to emit. And you have a range of
*  firing rates across the network. There's also weight homeostasis, but it's different to just
*  like L1 or L2 normalization. It's basically trying to balance. These networks also have an
*  excitatory inhibitory balance, which again, seems to be another principle that might have been missed
*  in machine learning community. It's well known amongst neuroscientists and in the cortex that
*  there's this EI balance it's called. And it turns out it's not there just for looks or for
*  complex dynamics, which the cortex seems to generate. It's even required in feedforward
*  networks to maintain the spike amplitudes or the net input into each neuron as information
*  propagates through a multilayer network. You need this balance in order to actually maintain
*  more or less, you call it dynamics, the feedforward dynamics in a functional range.
*  And that really hasn't been recognized in the past. So what I'm doing now is I'm incorporating
*  all of these principles into these networks. And right now, just doing it on MNIST. Now I know
*  MNIST is a solved problem. A deep network can get something like, what's the record now? 99.9%
*  correct or something. It's basically it's better than humans do. And again, how is that even
*  possible? These are handwritten digits and now we've got AIs that can read them better than people.
*  So it's solved in terms of gradient descent line, convolutional neural networks. A simple convolutional
*  CNN can solve MNIST for at least a battery of them. What they call the forest or more or less of CNNs
*  can solve it very well. But in spiking networks, it's definitely not a solved problem. So
*  we're trying MNIST more or less as a checkpoint for ourselves. And on MNIST, we're getting better than
*  any other nonconvolutional architecture spiking network has ever achieved on MNIST. So that's
*  progress as far as spiking networks are concerned. The next step would be probably to try it on a
*  bigger image type problem. Because even people who I've personally spoken to people who have
*  been in spiking networks and they say, yeah, they work for MNIST, that's fine. But they don't work
*  for bigger problems. They literally just fail. So that I think is that's tomorrow for me.
*  Tomorrow is okay, let's chuck ImageNet at a spiking net and see how it performs. And can we get it
*  close to gradient descent for a similar network architecture? That's pretty much my goal is to
*  look at the performance of gradient descent and get spiking networks to approach. They'll never be
*  as good because there's no error propagation. There's no indication to the network of exactly
*  what the output should be. But the brain gets away with that. Getting into the idea, is there
*  gradient descent happening anywhere in the brain or something like that propagation? There probably
*  is in specific regions and for specific tasks. But in general, the cortex learns through
*  self-organization. I think that's reasonably well accepted. There'll be people who disagree,
*  but they'll be in the minority, I think. So that would be the next task for spiking networks is
*  just throw some more complex problems at it that are already solved in the gradient descent field.
*  But the more complex a problem we can solve, the more people will start taking
*  notice of spiking networks, I think. Well, that's okay. So I was going to ask you
*  if you feel bound to attack these benchmarks that have been set for what deep learning models have
*  been successful at, because that's not robotics and it's not what brains are for. So it might be
*  different kinds of – and this goes back to me asking you about the psychological functions and
*  cognitive functions that are more related to what humans do and whether that might be – if that's
*  a step too far to start just asking about a different avenue of cognitive function rather than
*  tackling these things that have already been done. But you just said you do need people to
*  pay attention to it and people will pay more attention to it when they start tackling these
*  same benchmark tests, I suppose. That's exactly right. For one thing,
*  well, there's three things. Yes, people will pay attention, right? And these are known benchmarks,
*  right? And that's the second thing. These are known benchmarks. So it's easy to – you're
*  basically comparing apples with apples. But you're totally correct. The whole point and the whole –
*  where spiking networks and more biological AI really comes into its own is when you do start
*  interactions with the body and with the environment because that's where the dynamics of
*  a spiking network actually come to the fore. The fact that – and I mentioned this briefly in the
*  paper. As you say, it's very dense and I don't expand on a lot of the ideas. Maybe that's
*  another paper down the track and that'll be the 100-page paper rather than the 6-page paper.
*  But the dynamics of spiking networks are always transient, right? There's no stable state in the
*  brain because a spike happens and then it's gone. It is actually just a moment in time. It's a
*  unitary event. And so the way that this processing actually unfolds is completely different to
*  an artificial neural network. And when you think about it, our bodies, we survive in time in the
*  world. We perceive in time everything is transient. It's all dynamics, right? And so this is where
*  spiking networks will really, I think, become particularly useful. And this is where
*  gradient descent and artificial neural networks may be starting to hit a wall.
*  I'm low to actually proclaim that definitely. But in terms of interacting with the real world,
*  the complexity of the real world, gathering enough data to train a gradient descent model
*  in the real world, these are all quite prohibitive at the moment. Whereas the dynamics of a spiking
*  network and the rapid local learning that you get using rules like spike timing dependent plasticity,
*  they seem to be perfectly cut out for doing that job. So yes, it's actually a question that I kind
*  of grapple with. Should we just keep trying to go to the next benchmark and at least get close to
*  matching what gradient descent is capable of doing on each of these benchmarks? Or should we
*  just dive right into the robotics side of things and show what spiking networks are potentially
*  capable of in the real world? There's a risk, right, that if you follow the benchmarks that
*  you're actually going to, it'll lead you to the incorrect solutions because you're going to be
*  tackling problems that you won't eventually be tackling when you're in an embodied system,
*  for example. That's entirely true. Yeah. Yeah. Yeah. And that's one of the reasons that I took
*  this job in a robotics institute, right? Even though I'm not actually working with the robots
*  myself, I'm surrounded by them all the time. So I keep some basically front of my mind and every
*  day, every time a robot trundles past my desk, it's like, okay, what's it doing? And how could I get
*  a spiking network to do that? And I've got this idea kind of like ticking over in the back of my
*  mind all the time. But it is a leap. It's a leap and it's a leap into the unknown. And it's probably
*  a bit too ambitious and a bit too much of a chasm at the moment to really bridge. I think I need to
*  understand, we all need to understand the dynamics and the capabilities of spiking networks a little
*  bit better before we make that leap. And so really the best way to do that is just on current
*  benchmarks, I guess, as trivial and mundane as it may seem. Every time I try a spiking network on
*  a new data set, I learn something new. Right. I think that's the point. When I stop learning
*  anything new by applying it to these canned data sets and standard benchmarks, that's when I'll
*  stop doing it. All right. Very good. So I'm going to zoom us out and ask you kind of a larger
*  question. And then I actually have a guest question from the person who sent me your
*  paper in the first place before we wrap up here. So the zoom out, so this will be like the end of
*  the public version and then the rest will be like a little bit extra for Patreon supporters.
*  So what we'll end on here in the public version is you don't write the acronym AGI or the phrase
*  artificial general intelligence does not appear in that paper. But you did mention it earlier and
*  part of the context that you mentioned it is that your kid has asked you, you know, when
*  is it going to, when are you going to figure out AGI or is that what you're working on? I don't
*  remember what the exact question was. But you don't mention it. But looking at a list like
*  of the principles that we've been talking about, and this also has to do with me asking you what
*  your goal was, because I was going to guess maybe it's AGI. But so here's the question,
*  you know, do you think that building these principles in is going to lead to AGI? Do you
*  think that we're on our way to AGI? Or do you even acknowledge AGI as a thing? Because I actually,
*  I don't really, depending on how you define it. But Brady, where are we in terms of that,
*  if you think that we're headed that way? Right, right. So I mean, that is the rough, isn't it?
*  How do you define AGI? I mean, we, it's really difficult to even define just intelligence in
*  terms of what is intelligence for us or what is intelligence for, you know, biology and
*  intelligence in the environment. I mean, it can mean so many different things. So that's one of
*  the reasons I left it out of the paper, I guess, because it is just such a load. That was intentional?
*  Was it intentional that you didn't? Or I think it was intentional. So dense, you couldn't even fit
*  it in. Those three letters. I think it was probably at the back of my mind, I just thought,
*  well, it's a loaded term. And it, in some respects, it's a little bit, unless you're
*  specifically talking about that, it's a little bit unscientific to bring it up, even, you know,
*  because it's just so open to interpretation. So just for the sake of, I guess, trying to write,
*  you know, the most rigorous paper that I could on this topic, I just didn't mention it. But of
*  course, that's, you know, I think everyone who works in AI has that, has that in mind, right,
*  whether it's their goal or not, they can kind of see that the field is probably heading in that
*  direction. So, you know, what do we mean by and this is this is the problem, what do we mean by
*  AGI, you know, now for me, you know, there's this whole, before the idea of this embodied
*  Turing test, which is really looking at animals, up to humans, but starting with animals, there was
*  this idea of, you know, can we build a robot that can just walk into a an unknown house,
*  find the kitchen, make a cup of coffee for you, you know, a person could do that, right? Pretty
*  much any person, at least in the Western world can walk into almost any house in the world.
*  They know what a kitchen is, they know what taps are, they know where to get water, they know that
*  the kettle is going to be on on the shelf or in a cupboard somewhere, if they can't see it,
*  they'll search for it. They'll find the coffee in a cupboard somewhere, you know, and they'll be
*  able to make a cup of coffee in a house you've never seen before. So this was a test that was
*  proposed, I think decades ago, you know, can we build a robot that can actually do this?
*  And that was, yeah, like I said, that was kind of like a precursor to the embodied Turing test.
*  Now, would you call a robot that can do that? Would you call that, you know, an AGI? I guess
*  that's just arguing, you know, really semantics, like, that would be, we definitely don't have a
*  robot that can do that right now. And if we could build a robot that could do that, it would be
*  incredibly impressive. But more of a point would be incredibly helpful. Especially because I'm too
*  lazy and depressed to go make myself a cup of coffee. No, I'm just kidding. Right. So just in
*  terms of if it can do that, it can do pretty much any manual labor that we want it to. So and that's
*  going to be incredibly useful and game changing for society, you know, and, you know, that's what
*  Elon Musk is trying to do with the Tesla bot, Optimus or whatever it's called, you know, he's
*  trying to change the face of labor globally. Of course, you know, I think that's very misguided,
*  because it's not just a matter of building the hardware. It's the real problem is the real issue
*  is the brain. It's the AI that controls the robot. And that's a long way off, you know, we can build
*  robots that are physically capable, sure, but not mentally capable of actually carrying out the
*  computation required to do these things. So, you know, coming back to your AGI question, is that
*  AGI? Would you call that AGI for robot? If we build a robot that can do those things? I don't know.
*  Semantics, semantics. Exactly. So in terms of the bullshit term, it's I've come to hate the term
*  artificial intelligence. And was it John McCarthy, one of the earliest AI folks in, you know, the
*  Dartmouth summer conference when they were going to figure out AI? I mean, I think it was John
*  McCarthy who coined the phrase AI, artificial intelligence, and I'm butchering the history. But
*  one of those guys, one of those researchers really hated the term. And I really have come to dislike
*  it myself. Yeah, I think, you know, it's a loaded term, and it's probably overused. Do you have any
*  other reasons for disliking it? Because it reifies intelligence as it sort of equates intelligence
*  between biological organisms and not biological organisms, as if they're the same thing. And,
*  you know, like we just said, there's all sorts of intelligences across species, different types of
*  intelligences. So to say it's an artificial intelligence, as if it's one thing, is strange
*  for me to conceptualize at this point. And so I guess what you're saying, it comes down in part to
*  just our inability to even define what intelligence is, right, let alone artificial intelligence.
*  Yeah. I mean, we have to operationalize everything, which is fine. Yeah. Okay, no, no, I get that. So
*  we're certainly heading towards more capable models. Let's put it that way.
*  Well said. Whatever you want to call it, we're getting towards more capable models. At some
*  point, they're actually going to be useful. And that's when it's really going to make a difference.
*  Now, how do we make these things useful? You can argue that I guess chat GPT is already useful,
*  because people are actually using it. You know, kids are using it for their assignment, their
*  school assignments. But more to the point, people are using it in workplaces, you know, to write
*  emails and, I don't know, draft up ideas, brainstorming, they're using all sorts of
*  different fields, right, really diverse fields. Architects are using, you know, generative AI to,
*  you know, brainstorm new ideas for buildings. So, you know, it's becoming useful already.
*  But still, it's only in the digital useful in the digital domain. So when it becomes useful in the
*  real world, you know, I guess I'm talking robotics, that's really going to be even more
*  game changing, I would say. Okay, so we're winding down. And I have one last question for you. And
*  then I promise I'll let you go. And that is, do you see a role for consciousness in any of this?
*  You know, is consciousness important? Is it a byproduct? What are your thoughts on that? And,
*  you know, if we build in all of if we integrate all these things, is consciousness going to emerge
*  if it's a dynamical enough system, etc. Right. Well, that's if you think AI or AGI is a loaded
*  term, well, then consciousness is definitely sure. Yeah, okay. Awareness. I don't know. What do we
*  call it? I'm not sure what to call it. No, I just mean anything, anything that's representative of
*  that concept. Look, yeah, it's, it's, it's, it's very hard to kind of sum up. I've had like our
*  long discussions, you know, with journalists and things about this and barely scratched the surface.
*  So I don't think there's anything special about the human brain, right, or any animal brain that
*  leads to consciousness. That's almost like saying, if you believe that, then you kind of have to
*  believe that there's like, I guess, like, you're separating the mind and matter, right, if you do
*  that. You know, and so can we emulate consciousness in a machine? I guess? Would it be useful to do so
*  also? Well, would it be useful? Would it? But would it? Would it be avoidable? Or if is there some
*  level of intelligence where consciousness just appears? You know, so in other words, if we do
*  build the loaded term AGI, or, you know, something that understands the world the way that we do,
*  is it necessarily going to be conscious? I tend to lean towards the answer being yes, it will.
*  It will be conscious, simply because there's just nothing special about the human brain. It is just
*  a whole heap of biochemical processes going on, right? It's chemistry and physics. That's what
*  the brain is. Somehow that leads to this, you know, this innate subjective feeling of awareness
*  that I have, and that I presume you have, although I can never know. But there's nothing special
*  about the brain. It is purely a physical thing that leads to a purely mental state of awareness.
*  So I think if you build something that computes like the brain does, but you build it in silicon,
*  and it uses, you know, pure electrical spikes rather than electrochemical spikes that are used
*  in the brain, will it be conscious? I'd say there's a good chance that it will. Yes.
*  I've just got a warning about my battery. That's okay. I think I've still got plenty.
*  That's all right. So I think, yes, the answer is yes, machines will be conscious at some point
*  when we do get to that point. Exactly what that point is, I don't think anyone knows.
*  Yeah. All right. That's a ridiculous and great place to end. So Pete, thank you for staying
*  so long with me and going down many roads. And I'll point people obviously to the paper that we
*  most discussed, but some of the other work where you've started implementing some of these things
*  as well in the show notes. So thanks for coming on. Thanks for having me. It's been an absolute
*  pleasure. Thanks, Paul.

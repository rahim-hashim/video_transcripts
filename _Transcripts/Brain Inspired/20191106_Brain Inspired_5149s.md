---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 5149s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 15784
Video Rating: None
---

# BI 052 Andrew Saxe: Deep Learning Theory
**Brain Inspired:** [November 06, 2019](https://www.youtube.com/watch?v=jm_3CGjYYPs)
*  To me, one of the key tasks of theory right now is to test the hypothesis that deep learning
*  is telling us anything about the brain.
*  When I started, it took me, I would say, three years to get around my own mind's intuition
*  that these things were trivial.
*  Even if tomorrow there was a neural network that predicted every brain activation everywhere
*  in the brain and also solved all general artificial intelligence, I would not feel done because
*  I want to feel like I know how it works.
*  Right.
*  Right.
*  This is Brain Inspired.
*  Hello, good people.
*  This is Paul Middlebrooks.
*  So deep learning has risen, but there is a gap in our understanding how deep nets are
*  solving the problems that we ask them to solve.
*  So we have created something that we don't understand.
*  It's similar to the way I feel about my children, but that's another story.
*  To understand deep learning better, deep learning theory is on the rise.
*  And today my guest is Andrew Sachs.
*  Andrew is a professor, or more accurately, a Sir Henry Dale Fellow at Oxford, and he
*  is steeped in deep learning theory.
*  Andrew wants to understand deep networks better so that we can understand our own brains and
*  minds better.
*  One approach he takes is to simplify deep networks to isolate some of their properties
*  so we can better understand what effects various features have on the network's learning and
*  performance.
*  We talk a lot about his work with deep linear networks in which he has stripped out the
*  the non-linear functions in the units and thus can examine the effect of network depth
*  and the amount of parameters versus the amount of data.
*  And he relates all this to what might be happening in our brains.
*  He also tests out the phenomenon of replay, which we talk about, to figure out when replay
*  is actually beneficial and when it's not so necessary.
*  And WARNING!
*  WARNING!
*  Equation alert!
*  We have a first on the show, a guest with the audacity to use an equation.
*  So consider yourself warned, but he is quite gentle and it is a beautiful equation.
*  And by the way, Andrew is looking for students and post-docs.
*  He wanted me to pass that along to you.
*  If you are into this topic, check out the show notes where I link to his website and
*  the stuff that we talk about today.
*  Those are at braininspired.co.
*  Richard, Lin, Jay, Nigel, Marson, Mark, and Max, thank you so much for your support on
*  Patreon.
*  It is a huge help and I am so thankful.
*  I am using your support to continue to create the show and I'm excited to be giving back
*  to you soon in the form of the course that I'm creating about all the stuff that we talk
*  about on this show.
*  Alright, I hope you enjoy this episode with Andrew Sacks.
*  I have the deep and non-linear brain of Andrew Sacks with me today.
*  Andrew, thanks for joining me.
*  My pleasure.
*  Okay, Jay McClellan, Christoph Schreiner, Andrew Ng, Surya Ganguly, Krishna Shinoi,
*  Christopher Summerfield, Tim Behrens, who's your favorite?
*  I know it's not Tim.
*  Oh, yeah, I mean, I've been so fortunate.
*  You left out Heim Sampolinski.
*  Oh, that's right, of course.
*  Yeah, just a few big names among all of those names in there.
*  Yeah, I've been very lucky.
*  So I just named a bunch of people that you've either worked with or have served sort of
*  as the mentor role, you know.
*  You did your graduate work at Stanford where you had multiple advisors and I almost want
*  to just quit everything and become like an advocate for this mentoring approach.
*  The degree of specialization these days, so everyone's a specialist in something and very
*  few people are generalists, that together with the notion that like one powerful form
*  of creativity is combining ideas from different domains, right?
*  So I mean, how can someone best emulate this?
*  How do you think you've been at first of all, how do you think you've benefited from having
*  multiple PI advisors, but also having them on kind of on the neuro side and on the AI
*  side and having those multiple perspectives?
*  Yeah, I think it's been absolutely wonderful from my perspective.
*  I think right now there's no way to train directly in theoretical neuroscience.
*  So if you want to study it, you kind of have to make one of these unusual conglomerations
*  of advisors.
*  And some people come from physics, some people come from engineering.
*  But when I was trying to get an advisor at Stanford, I went to Jay and said, this is
*  what I want to do.
*  I want to sort of think about deep learning in the context of neuroscience and psychology.
*  And he said, that's great, but I don't I'm not sure I can advise you on the deep learning
*  side. So then I went to engineering and he said, look, it sounds interesting, but I can't
*  advise you on the psychology side.
*  And I just said, well, this seems to me to be so important that I still want to do it.
*  Can we can we have a team advising situation?
*  And I think that to do good research, you're often looking for a kind of a sneak attack,
*  right? You need some new, unusual perspective.
*  So in that sense, trying to find methods from different fields is just super important.
*  So, yeah, I found it very valuable.
*  You can also play them off against each other, tell when you're working, when you're
*  right. Yeah, no one's to like, yeah, they can't really be on you all the time because
*  you can just use any excuse you want.
*  I'm working on this at this point.
*  Yeah. Oh, I guess one last thing I would say is I think it's if you're going to go that
*  route, it's very important to have a question that you care about that gives it all
*  coherence. Yeah, I think that's sort of one aspect that's important to making that
*  well. Well, yeah, you started by saying that you knew what you were interested in.
*  So that is I don't know how many people know exactly what they're interested in when
*  they're starting out. Was this when you were applying to grad school or when you had
*  gotten in and then you were getting a feel for what you were going to do?
*  I think even my applications had something in this broad area.
*  Yeah, I mean, it was sort of right when deep learning was starting to pick up and I just
*  thought it was fascinating and seemed like it should have broad neuroscience applications.
*  And so you propose the multi mentor approach.
*  Yeah, I think it's common to have it's not it's not uncommon to have multiple advisors, but
*  maybe the stretch of disciplines that were on my team was a bit unusual.
*  Yeah, it's really yeah, I'm just really jealous.
*  So OK, so you will you claim the title theoretical neuroscientist and we will dive in
*  deeper to what you do.
*  But very broadly, where do you place your work and your interests on the scale of
*  artificial versus natural intelligence?
*  Oh, you know, I don't spend much time considering that question.
*  It's all intelligence.
*  Yeah, I mean, at some level, I feel like we could have lived in a world where the
*  departments were slightly redrawn and there was something like the Department of the
*  Science of Intelligence.
*  And maybe it wouldn't seem like such a core question to answer.
*  I definitely love studying the brain.
*  So, I mean, I think I started off in engineering, did robotics and this kind of thing,
*  and have been sort of marching over towards neuroscience ever since.
*  So it really does.
*  I think at this point is probably what I find super interesting.
*  But if my work has AI implications, that's absolutely wonderful.
*  And I think there's not that much of a gap between those things ultimately.
*  So, yeah, I mean, you mentioned there's, you know, there aren't just ready made
*  departments for these things at the moment.
*  And that might be.
*  Coming to fruition at some point, I don't I really don't know.
*  Some people think that should happen.
*  There should be departments of, you know, School of Intelligence, you know, for
*  instance, that just covers it all.
*  But, you know, for the time being, how would you advise someone who's interested in
*  working at the interface of AI and neuroscience, let's say?
*  What are some of the key things for them to pursue?
*  I think right now, because of how the departments are laid out, if you go to a
*  neuroscience department as an undergrad, it will be difficult to get quantitative
*  training at the level you would get in the CS department or physics department.
*  And so that's not that's not universally true.
*  There are exceptions, but I think you have to check your university.
*  And if that's the case, then I think you'd have to consider a more quantitative
*  track, at least for undergrad.
*  And that's a shame.
*  Like I wish I wish it was the case that there was a sort of theory track built
*  into undergrad programs that will let you go as far as you wanted in that
*  quantitative direction.
*  But I think at the moment, you know, I've heard senior people advise undergrads to
*  study physics or some other discipline and then come back later on and switch
*  back to neuroscience, which isn't great because physics is not neuroscience.
*  It would be much better if you could teach all these things with the content
*  matter being neuroscience, if that's what you happen to be interested in.
*  Yeah, I had Jessica Hamrick, Jess Hamrick on the show, and I asked her like what,
*  you know, how much time should you spend studying AI versus studying neuroscience
*  or, you know, right in between.
*  And her idea was, I think you need to go all in on both very separately.
*  So, and then you kind of end up being in the middle on average, but in your time,
*  you're actually studying them almost completely separately.
*  And, you know, so I, so the idea of getting the physics, something like
*  getting the physics, and I don't think that that's such a bad idea anyway,
*  because it's such a disparately different approach that it might be.
*  I mean, that's what's happening these days anyway, is everyone from physics is
*  bringing their physics ideas into the study of intelligence.
*  So, yeah, so, but the, the quantitation is unavoidable.
*  I mean, you just, you need that background.
*  You need that solid foundation, right?
*  Yeah.
*  Well, I actually think it's possible, it's possible to switch from neuroscience
*  and gain the quantitative side too.
*  It's just, it's a bit of a rough road either way you've picked it, right?
*  So, you just got to choose which seems easier to you to sort of teach yourself
*  quantitative methods, which I actually think a lot of people feel like that's
*  difficult to sort of teach them out of a book.
*  So if you're in that camp then, but there are definitely people who
*  have made that switch, so I think it can go either direction.
*  I just, I often have these conversations and it's sort of, um,
*  maybe a little sad when someone says, you know, I picked psychology as
*  my undergrad major because I was so interested in the brain.
*  And now I realize that I've missed all of these quantitative methods and I'm
*  really interested in deep learning and I want to take that forward.
*  Um, so.
*  But that's a strange thing to say.
*  If you're really interested in the brain, go study physics.
*  Yeah, exactly.
*  Okay.
*  Well, so there's this interesting pattern that I've observed, um,
*  with some variation, of course.
*  So on the one hand, when I ask AI folks, uh, they tend to think that
*  neuroscience has a lot to offer AI.
*  Um, but it's, it's often unclear, you know, what exactly, what, what
*  principles would be useful or the right way to, or scope to incorporate,
*  uh, neuroscience knowledge into AI.
*  On the other hand, uh, when I ask neuroscience folks, they think that AI
*  has a lot to offer neuroscience, but not necessarily the other way around.
*  Many think that AI is advancing so fast that there isn't really anything
*  neuroscience can contribute to it.
*  I, uh, I mean, I'm coming from the neuroscience side, so of course I'm
*  biased, but I actually, I think that's a naive notion, um, and I have a
*  vision that it will prove naive.
*  But I think that, I think that neuroscience has a lot to offer AI.
*  I'm guessing that you do too.
*  And I'm wondering if that's the case, how you think beyond just, you know,
*  inspiration, um, how neuroscience, especially systems, neuroscience, uh,
*  can contribute to AI, like in, in what areas or, or in what manner?
*  Yeah, sometimes I think it just comes down to timescale because if you're
*  talking to an engineer and they say like, okay, should I use a rectified
*  linear unit or should I use a sigmoid in my deep network?
*  They say, which one does the brain use?
*  I mean, clearly that's not really going to let you make progress if you're,
*  if you're, um, uh, coming from the neuroscience side.
*  But if you look on a long timescale, I mean, after all the AI systems
*  today are neural networks, right?
*  I mean, they're called neural networks.
*  Yeah.
*  Because they borrowed a ton of principles that have been worked out in
*  dialogue with psychologists and neuroscientists.
*  So I guess what I'm saying is I wouldn't discount what you
*  might be calling inspiration.
*  I think there will always be.
*  You know, for someone who has a specific application, um, the computer
*  scientist is going to be able to put in those last few extra principles to make
*  it really work for that specific application they're interested in.
*  And, and so the details right at the end are probably going to look like
*  they're a bit removed or could look like they're a bit removed from neuroscience.
*  But still, if they're training neural networks, if they're using sparsity,
*  you know, there's these sort of broad principles that do come up again and again.
*  Um, I think there's been a lot of dialogue with neuroscience and it's not.
*  I also, it's just not a, not like it's a unidirectional arrow, right?
*  I mean, there's these ideas were all built with lots of people talking to
*  each other across these disciplinary boundaries.
*  So it's already, I would say, co-created by all of these research communities.
*  You mentioned that, that there are, oh, I don't remember the qualifier, lots of
*  neuroscience ideas incorporated into neural nets, for instance.
*  But another way to look at it is that they're actually very few because these,
*  like a neural net in principle is, is based on what was known about brains way
*  back when, and there really haven't been that many details, modern knowledge
*  incorporated into the neural nets.
*  And it, it's, it's been a matter of just getting the neural nets to work basically
*  with what they have and throwing a few tricks in there as well to make them
*  tweaking them, to make them work better.
*  And so I would actually, my perspective is that there's very, very little biology
*  and I'm not sure how much there needs to be, but just looking at a neural net, it's
*  just so far removed from the way brains are structured and operate that it's almost
*  unfair to call it a neural net.
*  Yeah.
*  I mean, there's this very complicated relationship between the neural network
*  and actual brain, right?
*  I mean, it's clearly at this intermediate level of description, but, you know, I
*  mean, taking away some of your inputs is an approximation of what happens in
*  dendritic integration and responding to an injected current with an approximately
*  rectified linear kind of function is approximately what happens in a neuron.
*  So it's not totally out there.
*  And then I think if you bring the psychology evidence in from connectionism,
*  there's a lot of psychological phenomena that have been explained through using
*  these kinds of networks.
*  So that's more empirical grounding for these as an intermediate level of
*  description, but you're right.
*  Of course, I mean, we don't build in dendrite models and these kinds of things.
*  It hasn't really been much to be gained so far from that kind of level of detail.
*  Although people are working on that stuff.
*  I've had a, you know, a few on my show, but what would you say to it?
*  Like a systems neuroscientist who wants to, who wants their work to contribute to,
*  to knowledge in the AI research world, but they're down because they think that
*  it's not going to happen.
*  And what would you say to make them chipper?
*  I guess I would say.
*  Um, I think the first thing I would say is be ready for it to take 20 years.
*  Just do some good.
*  That's not going to improve their mood.
*  Come on.
*  20 years is nothing.
*  And then the, the like second part of that is be ready to take some steps, which
*  might appear to be incremental and not on that path.
*  Right?
*  So like, uh, to me, one of the most important things to do right now is to
*  just give some clear empirical tests of whether the brain does something
*  like gradient descent or not.
*  And if you're able to make that experimental case, very convincing and
*  clear, then I think there will be a flood of research on these learning based
*  topics, which we will see, you know, eventually probably it will turn out
*  the brain doesn't quite do gradient descent, it's doing something different
*  or you'll start to see the other principles you need, and those will be
*  what eventually trickles into the AI systems.
*  Um, all right.
*  So guys, you hear that just work for 20 years.
*  That's the, that's the advice from my current guest here.
*  I'm going to get lots of, lots of great feedback on this.
*  Um, yeah.
*  Sort of a related question then if it takes 20 years, you know, there have
*  been AI winters, right, where, you know, they starts off strong and then there's,
*  you know, funding goes away and then you realize that, oh, single layer, layer
*  perceptrons can't learn everything under the sun, so let's quit, you know, things
*  like that.
*  What balance do you think?
*  Because you recognize that these things take a long time, uh, and you have to
*  stick to your intuition, to your gut, you feel like what you're doing is right.
*  If you're going to, if you're going to do that for the long haul, you kind of
*  have to stick to what you believe.
*  What do you think the right balance is in following that, following your
*  intuition against the, going against the grain, uh, versus, you know, seeing
*  the way things are moving and pivoting and changing your direction and changing
*  your own beliefs, for instance.
*  I'm not sure I, I'm not sure I know how to balance those.
*  I mean, there's sort of the career aspects of, you know, do you need to put
*  food on the table so you have to, you know, the grant funding dried up, so you
*  have to switch, but putting that aside, I mean, I think, I think the, all of the
*  winters that have occurred, but the, the error was to think that the critique
*  completely sunk the whole project.
*  So I think probably the plausible path is to say, this is a step forward, you
*  know, whatever the excitement was that started that bubble before the crash,
*  there was a kernel of truth there.
*  And then we need to as clearly delineate that kernel of truth as possible
*  and, uh, build from that.
*  So, and, and eventually I think, you know, if you think it's a reliable
*  insight, it's going to have to come back around eventually.
*  Very good.
*  All right.
*  Let's talk some science.
*  You want to?
*  Great.
*  So, uh, deep learning theory.
*  Um, so I kind of want to just approach this gingerly because this is what you
*  study, I want to talk about how you approach it, and then we'll get into more
*  specifics about what, what you've done.
*  So is it fair to say that you use whatever similarities brains and deep
*  neural networks have to explore how the, the underlying principles in deep nets
*  might elucidate something about the underlying principles in brains.
*  Is that a fair way to describe it?
*  Sure.
*  Yeah.
*  I mean, the thing I would add is that to me, one of the key tasks of theory right
*  now is to test the hypothesis that deep learning is telling us anything about
*  the brain, right?
*  So, so the, the, um, instead, like I certainly wouldn't assume that deep
*  learning does the question is how can we make it an empirical question as to
*  whether deep learning is actually giving us insights.
*  So that's one major plank of what I'm trying to work on.
*  Okay.
*  Uh, brains and, and, uh, deep artificial nets are different.
*  Agree?
*  Yes.
*  Okay.
*  And importantly, we can do different things with real brains and artificial
*  neural networks, so real brains are pretty much set in their size and shape.
*  Uh, we can't mess with them too much or we'll get in trouble or bad things will
*  happen, um, you know, they grow and develop, you can't add more layers to
*  see what happens for instance.
*  Um, and sort of, you know, the goal is we're trying to understand how they
*  manifest learning intelligence, everything that, that brains do.
*  Uh, whereas artificial neural networks are under our complete control.
*  Um, so we, we can make them deeper.
*  We can add more layers.
*  We can add more units, uh, increase their breadth.
*  Um, but they quickly become untenable and basically impossible to understand
*  how they're doing what they do.
*  So we're, you know, we're basically, we just created another problem for ourselves.
*  Right.
*  So in that realm, it's like damn near impossible to determine what properties
*  are important for the performance of a deep net.
*  Um, and so, so what you're doing, so when, when I say performance, what people
*  usually think is the percentage error on, uh, you know, they get, they can name.
*  Cats at 98% accuracy.
*  And that's what most people think of as performance.
*  Um, but what performance also means is how you get from a naive untrained
*  neural network to a 98% correct neural network.
*  So that's another aspect of performance.
*  Otherwise known as learning dynamics is one way to appreciate that.
*  And, and really that's kind of, I would say the main thrust of what you're
*  studying is the learning dynamics of these neural networks.
*  Is that, is that right?
*  Yeah.
*  Yeah.
*  Okay.
*  So one of the main things you do is you remove the nonlinearities
*  from neural networks to study them.
*  Uh, and this is, this is a major simplification because all of the
*  deep neural networks these days that are used for anything useful are, are deep,
*  um, nonlinear neural networks.
*  So what are the differences between linear and nonlinear neural networks
*  sort of computationally, uh, and, and how they behave?
*  Right.
*  So I guess at a high level, of course we wish we could do theory
*  with the nonlinear networks.
*  Right?
*  So there's no question that's the goal.
*  The goal is to explain what happens in these nonlinear networks.
*  Um, but just like in electrical engineering, you learn about linear
*  circuits, not because any circuit is linear, like there is no linear
*  circuit in the world, right?
*  Universe.
*  Yeah.
*  In the universe, but it clarifies the conceptual structure and it's a
*  prerequisite to understanding the more complex case.
*  So, uh, that the ideal scenario will be the same thing with these, um, deep
*  neural networks, we have a simplified model that is more tractable.
*  It can get mathematical insight into, and hopefully it behaves somewhat
*  like the nonlinear, uh, networks.
*  If it didn't, it wouldn't be interesting.
*  It turns out it actually behaves sort of remarkably similar in terms of learning
*  dynamics to its nonlinear counterparts.
*  So the difference between a deep linear network and nonlinear network, a linear
*  network, when you add more layers, the composition of linear functions is
*  still just a linear function.
*  So that means no matter how deep I make this network, I'm still stuck
*  with just linear regression.
*  And that is not going to do well on image net or, you know, recognizing
*  cats for stocks, any task, any real world tasks, it's not going to actually
*  perform that one perform well.
*  Okay.
*  And so when I say that, you're probably thinking like, this sounds like a dead
*  end, why are we still talking about this?
*  But you have to separate representational power from learning dynamics.
*  And it turns out that when it comes to learning dynamics, when you make one of
*  these deep linear networks deeper, the learning problem changes when you add
*  each new layer and the dynamics can be highly nonlinear and show all of these
*  key features of the nonlinear problem.
*  So once you have one or more hidden layers, the learning problem is non-convex,
*  which is a key mathematical property of the nonlinear ones.
*  What does that mean practically with like the error surface?
*  It means the error surface is no longer just some simple bowl.
*  So if a convex problem, the learning problem, okay.
*  So first of all, deep learning takes optimization view of the learning question.
*  So what you try to do is change your weights to optimize some performance
*  objective, like the squared error or classification performance and that
*  optimization problem, the function you're optimizing, it could look like a nice
*  round bowl and imagine just dropping a ball somewhere on the bowl, you're always
*  going to roll down to the lowest point.
*  There's nowhere you can get stuck.
*  Everything's going to work.
*  That's a convex problem.
*  Global minimum, global minimum.
*  The non-convex problem could have a really bumpy surface.
*  So you could have little pockets where you could get stuck, local minima.
*  You can also have saddle points.
*  So just imagine that in one direction is just looks like a saddle basically in
*  one direction, it curves up, but in another direction it curves down.
*  There's other exotic things that can happen in non-convex optimization problems
*  and the deep linear networks, they're simple, but they still have those
*  features actually.
*  So that's why I think they're still worth analyzing and they give you these sort
*  of really rich, interesting dynamics.
*  So why is it important for brain sciences to have simple models to study?
*  I think if you're an engineer, you need the system to work.
*  Competence is king, right?
*  It's just sort of non-negotiable.
*  Solve the problem.
*  Yeah.
*  For the brain sciences, competence is very important.
*  We would like to be analyzing models that really work, but we also need to
*  analyze models that we fully understand.
*  And the virtue of these simple models is you can strip everything out until you
*  just have the simplest possible model that gives you the phenomenon you're
*  interested in, and then maybe you feel a little justified in saying like,
*  okay, I understand what's giving rise to this phenomenon.
*  So a one simple example of that is a lot of people used to think that in deep
*  networks, sometimes you train them and they'd apparently learn nothing for a
*  while, they'll just be sitting there, not getting any better.
*  And then all of a sudden there'd be the sharp drop where they get much better in
*  terms of their performance.
*  And people thought that that was due to the non-linearities, but it turns out
*  these deep linear networks show that too.
*  So it wasn't due to the non-linearities.
*  It's actually just inherently due to depth.
*  Yeah.
*  So that's the kind of insight that I think you can get from these simple models.
*  How often do you get the question of the form, you know, this is all very nice, but
*  we know brains don't fill in the blank, don't do it this way, don't have this
*  particular quality, you know, the brains are non-linear, for instance, you know,
*  how often do you get that kind of criticism?
*  Yeah, if I had a dime for everything.
*  So I, but it's, I mean, it's a valid critique though.
*  The only thing is, and I don't know why this style of reasoning isn't more
*  common in the brain sciences and also CS.
*  So in a lot of fields, this, this feels very natural to people to say, I'm going
*  to have a simpler model and I think it retains some features to the problem and
*  it's going to generalize, but in the brain sciences, people are jumped to the,
*  to the complexity of the brain very quickly and think that that's essential.
*  And in machine learning also, I think it's historical there.
*  One of those AI winters you mentioned was caused because basically they were
*  using linear networks and it couldn't solve the XOR problem.
*  And the solution was to make them non-linear.
*  And so it's sort of seared into the mind of people that this
*  linear networks are trivial.
*  And that's true when it comes to representational power, but not when
*  it comes to learning dynamics.
*  So I think we have some unlearning to do of that, uh, that particular principle.
*  And maybe another way of saying it is I don't think non-linearities
*  are going to come save us.
*  Sometimes people will say, Oh, I know that this simple network doesn't satisfy
*  some theory I've proposed, but once you add the non-linearities, it will.
*  And that could be the case, but I think it's also plenty of reason to believe
*  it's not going to be the case.
*  Well, so I guess it sounds like your, um, critics are more, more from the
*  neuroscience side than from the AI side.
*  Oh, I, I think most people see the value of it on both sides.
*  And I think the critics are on both sides to be sure.
*  And I mean, they're right.
*  You know, we would like to get to the non-linearities.
*  Of course.
*  Does it matter that, um, so, you know, I'm not being critical here, but does it
*  matter that you're studying learning theory in the regime of back propagation,
*  which is one of those things that is like not a biologically plausible mechanism?
*  Great.
*  So this to me is the question.
*  When you say that something's biologically plausible, I would say that
*  that is basically relying on your background intuition based on lots of
*  data and we could stop the conversation there, but it seems more productive to
*  me to say, instead of relying on that background knowledge, let's make some
*  explicit predictions.
*  What does it mean for a system to be doing gradient descent?
*  How will we know?
*  And then let's go do that experiment.
*  Well, gradient descent is different than back propagation, um, at least
*  at the mathematical level.
*  So just to be clear, but yeah, but, but I like this bigger picture of
*  gradient descent, so please carry on.
*  Right.
*  Yeah.
*  So, um, but you've, you've just highlighted something that I should have
*  been more careful because that to me is a key point.
*  All of the predictions I make flow from gradient descent, which is just the
*  mathematical specification of how you're solving this optimization problem.
*  They don't actually get to the algorithmic level of how you'd
*  calculate that gradient direction.
*  So it could be back prop.
*  It could be any of these other options we now have on the table for how to do it.
*  And I think that's important because you could go hunting in the brain for any
*  one implementation, and if you don't find it, doesn't mean the brain isn't
*  doing gradient descent, just might be using some other implementation.
*  Yeah.
*  So, so to me that's step one is, is the brain doing gradient descent?
*  And that's an empirical question that we should seek to answer.
*  Yeah.
*  So empirical questions, is it hard to find experimentalists who will want
*  to test these, the theoretical ideas?
*  Yeah, I think it is.
*  I think it's always a negotiation.
*  Right?
*  So, I mean, there's sort of the ideal experiment that a theorist dreams up,
*  and then you talk to an experimentalist and say, that's not even possible.
*  Um, and unfortunately, I think for these learning dynamics questions, it's a
*  little, the situation is a little bit different.
*  The experiment is doable.
*  It's just enormously time consuming and a total pain.
*  And so, yeah, it is hard to tell someone like, look, this is
*  going to take two years, right?
*  I mean, so I think all you can do is, which, which is what I spent a lot of my
*  time doing is trying to see where the opportunities are to bring the theory
*  closer to the experiments that people are already running so that they don't
*  have to adapt as far.
*  And then also, you know, sometimes you find a brave soul who says, I see
*  why this is valuable, let's go do the hard version and I've gotten lucky
*  in that direction.
*  It's, it's brave.
*  If it works, it's, uh, it's, uh, stupid if it doesn't, I guess.
*  That's right.
*  Okay.
*  So, so you, you went in, you were interested in these bigger questions.
*  And at some point, I don't know when you can tell me you started studying linear
*  networks to get at some of these things and you realize, oh, this is a good way
*  to do it.
*  How has your sort of gut feeling because now, now you're in it.
*  You can't get out.
*  You can't get out of the linear network business now for 20 years, apparently.
*  So how has your gut feeling changed, um, from the early days of when you started
*  working with linear networks to, to ask these sorts of questions that we will
*  get to in just a minute.
*  Um, how has that changed relative to now?
*  Like how you view the power of, of what you're doing?
*  I definitely did not expect them to be as interesting a model as they
*  have turned out to be.
*  When I started, it took me, I would say three years to get around my own.
*  Mine's intuition that these things were trivial.
*  And I don't know what happened.
*  One day I was like, okay, let's just try taking the nonlinearities out.
*  And it gave all the same phenomena, at least qualitatively.
*  And I said, wow, okay, well, we could probably understand it.
*  You didn't have to go to a revival or something.
*  You actually came to it on your own.
*  No one, no one put their palm on your forehead and said you're healed.
*  Yeah.
*  Yeah.
*  I mean, it is a weird thing being, I feel like we're often trying to see around our
*  own intuitions that are wrong.
*  This was really deep inside me.
*  So it took a while, but, um,
*  but it definitely has its limits, but I don't think we've exhausted them yet.
*  So questions like continual learning, there's definitely a way to pose that in
*  linear networks, um, lots of questions related to generalization, frequency
*  effects, the impact of curriculum, meta-learning, all of these could have a
*  deep linear network version of them.
*  It's not to say it's the only way.
*  So there are lots of other models.
*  I don't actually just do deep linear networks.
*  I know, but you're the deep linear network go-to person.
*  So, so here we are.
*  So you just mentioned generalization.
*  Um, so one thing you study is generalization in deep nets.
*  So let's start there.
*  Uh, what does it mean to say that a deep network generalizes well?
*  Uh, I guess the canonical version of that would just be supposed that I train a
*  network on 10 examples of dogs and cats.
*  And then I give it some 11th example that it's never before seen.
*  And then the question is, what is its typical accuracy on one of these new
*  examples?
*  Um, that's how it's been formalized usually in machine learning.
*  And in fact, it's a bit of a more technical definition.
*  So you could talk about the training error, which is how well are you doing on
*  those exact 10 examples you train the system on, and then the test error, which
*  is how well are you doing on an ever before seen example and the difference
*  between them.
*  That's what theorists really mean by the generalization error.
*  Quantified generalization.
*  Yeah.
*  Yeah.
*  And I think one of the things that deep learning practitioners have done is sort
*  of shifted the focus of theorists away from that generalization gap to just the
*  absolute performance level of the, like, what does it matter if there's a huge
*  gap between the training, uh, accuracy and the testing accuracy?
*  All you actually care about is what was the test accuracy and was it good?
*  That's sort of the deep perspective.
*  Okay.
*  So it's a slight shift.
*  Yeah.
*  So our brains don't overfit, uh, things they, they generalize very well.
*  So deep nets overfit.
*  So deep nets can be kind of have a small parameter base relative to the
*  amount of data you're feeding them.
*  Or you can be feeding them relatively the same amount of training examples as,
*  you know, data as they have, uh, parameters in them, or then you get into these
*  really deep nets and they have a lot more parameters than the actual data that
*  you're feeding them.
*  And that's most akin to what our brains are, right?
*  Because, uh, if you're seeing 10 pictures of dogs and cats on our brain,
*  brains have 86 billion neurons, not that we're using them all to, um, to
*  answer the question, but, but we essentially are that case where we have
*  super high parameter space with relatively little training data.
*  Um, and, and you show an interesting thing that happens with deep nets as
*  you increase the ratio of, uh, training data to parameters, let's say, do you
*  want to just talk about how that develops?
*  Sure.
*  Yeah.
*  So there's sort of the standard go to locks tail in machine learning, which
*  would say you can have a really simple model that's so simple that it can't even
*  fit your training data.
*  And so it's not going to do that well on new data either, right?
*  This is just too simple.
*  So that's underfitting.
*  And then you can have a model, which is super, super complex.
*  It fits all the training data perfectly, but maybe it does these crazy things,
*  uh, in between the training examples and so on new examples, it does very badly.
*  And then somewhere in the middle, things are just right.
*  It's like the Goldilocks position, right?
*  Okay.
*  So that's in a lot of textbooks.
*  It turns out though, if you just take a deep network and you keep going, so
*  instead of things being, instead of the model being fairly complex, you make it
*  outrageously complex, then all of a sudden it starts working very well again.
*  Can fact be the best model you train.
*  So for instance, you could have a model with, um, millions of synapses trained
*  with only, I don't know, a hundred training examples, and that would be doing
*  better than a model that only had 50 synapses.
*  So this surprised a lot of people because it doesn't seem like, how could you
*  constrain all of those, the value of all of those synapses?
*  Right.
*  And in fact, what you get, which, um, Misha Belkin is called a double descent
*  curve, it's a good name for it is if you plot sort of model, increasing model
*  complexity here, it could just be the number of hidden neurons in your neural
*  network.
*  Um, so you have increasing model complexity, then sort of things initially
*  get a little bit better, but then they have this big spike where the complexity
*  is at intermediate value, and then it starts decreasing again for these very,
*  very large models.
*  So that's it.
*  That's why I call it a double descent curve.
*  And for linear networks, you can get a very clear analysis of exactly what's
*  going on to cause this phenomenon.
*  And the core thing there is you don't like basically dynamics enter the picture.
*  When you have fewer examples than training data, there are lots of networks
*  that would have given you perfect fits to all your training data, but had
*  different completions for the rest of the training of the test examples.
*  Um, if you were to just randomly pick one of those, you do terribly because it
*  would probably be doing some crazy stuff.
*  So that's called Gibbs learning, but we don't randomly pick them.
*  What we actually do is gradient descent, starting from smallish weights.
*  And the smallest weights is really key piece there.
*  It just turns out that it's going to keep you near a simpler solutions.
*  So instead of picking one of these really complex continuations of your
*  function, you end up picking a simple one that generalizes pretty well.
*  So small weights is one which is regularization essentially, right?
*  Yeah.
*  So, so that's a, that's a key and, and having a large network with the small weights.
*  Those are those, are those the two keys that aid generalization?
*  Yeah, there's some subtle effects that come from having, seem to come from
*  having these really large networks.
*  So it makes the, the structure of the correlations that you're trying to learn
*  slightly better conditions when you have these very large networks, which is
*  a little counterintuitive, not sure I fully have the intuition for why that is the case,
*  but the only time things go really wrong is when you can just barely squeeze everything in.
*  So if you just have enough parameters, you could just barely fit all your training
*  examples, then if you imagine changing one of those training examples, you
*  have to be completely sensitive to it.
*  So you have like full sensitivity to any changes in your, any noise in your training
*  data set.
*  It's like locked in to those examples.
*  Yeah.
*  Yeah.
*  So that's when you get giant spikes in the test error.
*  What does it, first of all, what does it say about brains then?
*  How do you map this on the idea of small initialized weights?
*  I mean, of course you can map on the large network into a brain very easily,
*  intuitively, but the regularization aspect of having small weights to train
*  what would that mean in brains?
*  Right.
*  The small relative to what is the first question.
*  So it's, it's, um, there are lots of different ways you could regularize it.
*  So the small weights plus gradient descent, just one option.
*  Um, you could have explicit penalties, right?
*  So maybe you think there's just a part of the synaptic dynamics in the brain are to
*  keep synaptic strengths small on average.
*  Um, that would be something like weight decay in the AI world that can definitely
*  also solve this problem.
*  Um, but otherwise, yeah, I would have to say that, um, if you wanted to take this
*  proposal very seriously for brain sciences, you would say that most of your synapses
*  start off with values near zero and they move away from that special point of zero
*  when you're actually trying to learn some new tests.
*  Um, and the, the, yeah.
*  And the intuition being that if they are zero, you're typically representing a
*  simpler function.
*  I see.
*  Cause it's not participating.
*  Right.
*  Well, with, with large weights, initializing with large weights and deep nets, I mean,
*  you've shown that, um, essentially that you can, it learns really fast.
*  Uh, but then it's not general at all.
*  So you pay a big penalty with generalization.
*  And then if you initialize with the lower weights, the learning can, like, uh, can
*  really, uh, look plateaued, like very little.
*  And then you have this sort of sharp rise, right.
*  In the learning.
*  And I don't know, it seems like those learning curves match what brains tend
*  the way and my own experience of how I tend to learn a skill, right.
*  Like guitar or something like that.
*  There's this long period where you feel like nothing's happening and then you have
*  like a breakthrough, right.
*  Yeah.
*  Right.
*  So this now brings depth into the picture pictures.
*  Everything I was saying is just about a linear network.
*  When you add depth, you make the learning problem more complicated.
*  It's not convex.
*  One consequence of that is if you start with small weights, turns out that learning
*  slows down and it slows down exponentially in depth.
*  So that's, that's sort of an example of beautiful theory question.
*  You can answer with these deep layer networks.
*  Suppose I make the network bigger.
*  How much does it slow down?
*  Yeah.
*  Right.
*  And the answer for these deep layer networks is if you have small weights, it's slowing
*  down exponentially in depth.
*  And then the other interesting thing is the trajectories change from being sort of a
*  simple exponential approach where it just monotonically gets better over time to these
*  sigmoidal stage like transitions where, yeah, the network sits there doing apparently
*  nothing until it acquires a subpart of the network.
*  At which point it fairly rapidly transitions.
*  It's not instantaneous transition, but it fairly rapidly transitions to fully learning
*  that subpart.
*  And like you're saying, that's been observed in lots of developmental studies.
*  So, you know, there is some sense in which this could describe human learning.
*  That's one suggestion you put forward is you can go through a sequence of quasi stage
*  like transition, transition, transition, transition, transition, transition, transition,
*  transitions over time that would be a potential consequence of learning deep deep networks.
*  Just to come back to the generalization.
*  Yeah, no, yeah, because I want to get back to the depth as well.
*  But yeah, I have some more questions about it.
*  Yeah.
*  So what you've hit on is this intriguing thing.
*  I said to generalize well, you need to start with small weights.
*  But I said to train quickly.
*  Maybe I didn't say it, but to train quickly in these deep networks, you need to start
*  with large weights.
*  Absolutely right.
*  And so there actually is this tension, at least in deep linear networks.
*  There's a trade off between learning speed and generalization ability that's controlled
*  by the size of those initial weights.
*  So this kind of ties into the complementary learning systems theory story.
*  So so you were Jay McClellan was your one of your mentors in graduate school, and he
*  developed the this theory that has to do with learning fast in the hippocampus and learning
*  slow in the cortex.
*  That's a very, very rough description of it.
*  But I've had on a Shapiro on the show and she does work with the CLS, I'll call it.
*  And so we've talked about before.
*  So listeners will be somewhat familiar with it.
*  I would hope so.
*  So you studied how replay this phenomenon that is supposed to undergird learning in
*  the complementary learning system.
*  You study how replay might contribute to generalization.
*  Yeah, so I don't you know, you can just give a real quick overview of what replay is.
*  And then and then I want to know, like, what's what's the optimal amount of replay and the
*  optimal situation for how much replay do I need, man?
*  Right.
*  Yeah.
*  So replay is this observation that during quiet rest and at night, sometimes you'll
*  see specific neural ensembles that you experience during the day reactivate or sometimes it
*  could even be like you might have an animal navigating a maze and you'll see that the
*  replayed sequence of positions actually takes some turn that the animal didn't make.
*  So it's a very complex set of phenomena.
*  But what I've been asking, I suppose you just zoom in to the sort of simple supervised
*  learning scenario where you're just trying to learn to map from inputs to outputs.
*  You could ask this generalization question in the following way.
*  Here's a game.
*  I am going to give you data every day, so some amount of training experience and you
*  have a choice.
*  You can either take that data, store it in a temporary buffer and replay it repeatedly
*  into a neural network that then does gradient learning.
*  Or you could take that data, never store it and just do pure online learning where I
*  train on each example one after the other.
*  And so this is a very simple formalization, this idea that you could have a dual system
*  memory where you're doing this replay.
*  You have something like a hippocampus where you can hold on to things versus if you really
*  had no ability to store your experience directly and you just had to use an example and
*  throw it away.
*  When would these two strategies differ?
*  And so the result that comes out of this is that replay is not always beneficial.
*  If you have a lot of data, if I give you lots of experience during each day, it just
*  doesn't matter because online learning will get to the same place as this replay strategy.
*  So you need to be in the limited data regime.
*  The second thing is how rule following or noisy the rule is you're trying to learn.
*  If the rule that you're trying to learn is extremely noisy, the only way to get rid of
*  the noise is to average it out.
*  And the only way to do that is to see lots of examples.
*  So it basically reduces back to the previous one.
*  So what this means is the only case that we found where replay is sort of decisively
*  superior to online learning is in the limited data regime when you're learning a very
*  reliable rule.
*  And arguably, that's kind of a situation that lots of brains face.
*  Right.
*  So that, I mean, you definitely don't get much training experience.
*  And at least in terms of the rule following this, it could be a complex rule, but your
*  caregiver usually, if you're looking at a dog caregiver, usually says, oh, look, that's
*  a dog. They don't say that's a porcupine.
*  Right. So the labels are correct.
*  Yeah. And in that setting, the replay is very useful.
*  I mean, does this sort of suggest that you wouldn't want you kind of want to be able to
*  switch between these types of regimes with a lot of replay and little replay?
*  And that suggests that your brain either knows how to switch between the right, you
*  know, knows when to give you just the right amount of replay, right?
*  Knows the right amount of replay to use if you're going to be optimizing.
*  Or the brain could be operating in a regime where it's just there isn't a switch that
*  says, OK, give me lots of replay now because I need to really learn this versus, oh, I'm
*  getting lots of examples.
*  So I don't need the replay.
*  I would imagine it would be the case that there's some mechanism that as as you're in
*  an experience and you realize, oh, I it's very limited data, but very accurate, let's
*  say, and then your brain knows to give you replay.
*  What do you think? What are your thoughts on this?
*  Do you think this is a natural shifting that the brain does?
*  Yeah, I think that's a great question.
*  And I'm working on sort of experiments that are aimed at testing exactly that, because
*  that's the interesting suggestion emerging from this, right, is you should modulate how
*  much replay you do depending on the type of task you face.
*  And it's an open question whether the brain does that.
*  So I'm working on this with James Fitzgerald and Nelson Spruce and Wayne Onsen at
*  Janelia. And that's sort of the exact question they're interested in.
*  So I think. Certainly an intriguing prediction, and it's also interesting that this
*  is some a way in which it's slightly different from many CLS proposals is
*  too much of a good thing is bad. It's too much replay.
*  You actually start overtraining. That's a feature of the setting we're analyzing.
*  So you do need to carefully titrate it, which doesn't occur in several of the other
*  CLS proposals called replay a good thing.
*  But maybe replay is just something that's only demanded when necessary, for instance.
*  Right. Right. I guess that's there's lots of different hypotheses.
*  Yeah, I mean, so there are all kinds of predictions that stem from this, for instance,
*  once you start getting an example right, you don't need to replay replaying.
*  So is there a per example prioritization, things like this or a baseline rate of replay
*  when you are just to maintain things like that?
*  Well, man, there's a lot of a lot of research on replay these days, so hopefully there'll
*  be lots of answers coming out here.
*  We kind of slipped into talking about depth before.
*  So let's slip back into it here.
*  One of the things we didn't talk about is how just how to get a linear network.
*  But, you know, basically you have these nonlinear networks.
*  They're just all connected.
*  All the units are connected to each other layer wise.
*  And to to isolate depth, for instance, you needed to extract to transform a nonlinear
*  network into its linear compatriot linear version, essentially.
*  So how did you isolate the effect of depth and how does depth affect learning in deep nets?
*  Yeah, so the isolation is fairly simple.
*  It's also kind of brutal.
*  You just sort of strip out all the nonlinearities.
*  And but that's not quite so crazy if you think of a sigmoidal neural network.
*  So in a sigmoidal neural network, you have this activation function, which is mapping
*  from basically input current output firing rate.
*  Right.
*  And it has these two upper and lower limits.
*  But in between them, it's approximately a little linear piece.
*  Right.
*  So you can also think of this as we're describing the dynamics early in learning for a
*  nonlinear network.
*  And in fact, if you plot those two, you'll see they're bang on top of each other for a
*  while and then they sort of split off.
*  So that's one interpretation.
*  And then in terms of the dynamics, I think I alluded to some of the changes.
*  So one big one.
*  But before you get into that, I just want to.
*  So just envisioning like a nonlinear traditional net, you have this like really nice
*  slide in your talks where you show you end up from the all on all connections between
*  all the units in a neural net.
*  And you said it's brutal, but simple.
*  But you actually have to go through quite a bit more math to basically get independent
*  noncoupled chains of units right to isolate the effect of death.
*  That's what I was that's what I was hoping that you'd address as well.
*  I see.
*  OK, yeah.
*  So that's more about the solution method.
*  Yeah.
*  So the mathematics behind how you so just taking out the nonlinearities doesn't give
*  you the equation for the dynamics all the weights are going to take.
*  Right.
*  And you could strip out all the nonlinearities and still train it using a computer.
*  But that wouldn't be taking advantage of the additional mathematical tractability.
*  So I can actually write down an explicit formula for what every single weight in that entire
*  network across all the layers will do at every point in time.
*  And that formula sort of relies on this decoupling trick.
*  The idea is in a deep network, all of the weights are coupled together.
*  So if I change one of them, it's going to have rippling consequences as it flows through the
*  rest of the network.
*  There's a particular change of variables.
*  Think of looking at it, looking at this network through the right sort of lens,
*  where all of that coupling is removed.
*  And what you have is just a bunch of independent 1D chains.
*  So you can really think of that as suppose you had a network that was just a single neuron in
*  each layer, one after the other, which by the way, is a beautiful simple model to think about
*  a lot of these deep learning phenomena.
*  Just try to wrap your head around that.
*  It's called the cerebellum.
*  No, I'm just kidding.
*  Go ahead.
*  Maybe.
*  And so the sort of lucky fact mathematically is you can solve each of these 1D chains
*  independently, don't need to know about the rest.
*  And then you can combine things back together by doing the inverse of this change of variables.
*  So that's sort of the mathematical solution.
*  It's a hugely powerful tool just to see what all the actual effects of all the weights.
*  So yeah, anyway, thanks for explaining it.
*  So then you can isolate what the effect of depth is when adding more depth essentially into
*  neural nets.
*  So what's the effect of depth?
*  Yeah.
*  And just to be clear, this is only on the learning dynamics side, right?
*  So you're not.
*  Yeah.
*  There's lots of other effects of depth if it's nonlinear.
*  But anyway, so at least for the learning dynamics picture,
*  one of the major effects is it changes the trajectories from being sort of just simple
*  monotonic approach to the final error value to these stage like transitions.
*  And you get one stage for each of those independent decoupled networks that we were just talking
*  about.
*  So it's quite amazing.
*  You have this deep network and it's seeing the exact same data.
*  The data sets not changing over time.
*  And yet you see this dramatic unfolding where it goes through stage after stage after stage,
*  picking up additional sub pieces of the problem.
*  So that's one big difference.
*  Another thing is the deep networks are exquisitely sensitive to what's already in them.
*  Which I think is really interesting.
*  I think of all the work in brain sciences considering priors and the impact of prior
*  knowledge.
*  Well, that's really salient in these dynamics.
*  What's already in the network can completely change the learning dynamics.
*  So when I've been talking about the stage like transitions and talking about solutions
*  starting from basically no knowledge, and I call it tabula rasa where you have small
*  weights.
*  But if you put rich knowledge in there, the dynamics can completely change.
*  That's another feature of the dynamics that is quite interesting.
*  Is this related to the early unsupervised learning training of networks?
*  Yeah, exactly.
*  So that's one example.
*  If you don't start from just small weights, but instead pre-train each layer using unsupervised
*  learning, then you're starting from a very different initial position in your network.
*  And in fact, learning is very fast after that.
*  And that's just one version of the start with large weights prescription for fast training
*  in these deep linear networks.
*  I mean, a lot of people talk about how maybe we're born,
*  maybe there's a lot of unsupervised learning going on.
*  And you've talked about this in early critical periods of development.
*  And then I even had Tony Sater on the show and other people have talked about the idea
*  of evolution itself being a sort of compressed version that you're coming in equipped with all
*  this long, long term learning, which was a combination of supervised and unsupervised.
*  But then you which sets you up to develop your brain in such a way to maximize the unsupervised
*  learning early on to then later go into a supervised learning regime.
*  So this is all really interesting stuff.
*  Yeah, I think that's a beautiful connection between critical period plasticity and this
*  potential unsupervised learning.
*  And one interesting thing there is there's a time when I thought you had to really get
*  it all exquisitely right.
*  Like the details mattered of that unsupervised learning.
*  But the interesting thing from these solutions is actually you're just trying to set the
*  right scale of the weights when it comes to learning speed, at least.
*  And so because I at least the puzzle to me was the critical period plasticity.
*  It could be like three days in auditory cortex for rodents.
*  So how much experience do you actually get in three days?
*  I mean, does that really sample the entire space of stimuli you're going to see?
*  It seemed like that was sort of too little to really learn a, you know, exquisitely
*  tuned representation.
*  But what if one of those days is cloudy?
*  You're screwed.
*  Yeah, exactly.
*  So but this is suggesting, well, if it's just a starting point, maybe you're fine.
*  Right.
*  Maybe it just sets things so you can learn quickly after that.
*  Interesting.
*  Yeah.
*  Well, anyway, so sorry for the divergence there.
*  So OK, so depth.
*  I don't remember where we were talking about how depth affects the actual learning.
*  Yeah.
*  So maybe it's also worth.
*  So there's these stage like transitions.
*  Yeah.
*  But the impact of prior knowledge and.
*  Well, OK, if you'll bear with me, maybe I'll try to describe one equation.
*  It's very simple.
*  And I think it's very beautiful.
*  I'm going to do it.
*  Oh, my God.
*  He's going to do it, folks.
*  I wasn't going to ask you.
*  Let's do it.
*  Oh, man.
*  All right.
*  Let me sit down here.
*  No, I'm just go for it.
*  So the left hand side is the time it takes to learn some subpart of the overall problem.
*  You're trying to learn.
*  So that's learning time.
*  Right.
*  And the right hand side is one over the initial strength of that subpart.
*  You think of the strength as a value between zero and well,
*  but it's zero if you don't know it.
*  And it's greater than zero if you do know it raised to the depth of the network.
*  OK, so the equation is T equals one over B to the D.
*  All right.
*  If B is the strength of the part.
*  And I really like this because it's telling you.
*  How learning dynamics relates to network structure.
*  And it's also got this prior knowledge piece in there.
*  Right.
*  So it's saying learning time depends on the structure of the network, meaning the depth D.
*  But it also depends on the knowledge is already in the network, which is this initial subpart
*  strength B and it sort of closes that whole loop.
*  And so if the initial subpart strength is very small, then when you raise that to a large power,
*  you're going to have a really, really slow, exponentially slow learning time.
*  But if it's quite large, then actually deep networks can be very fast in their learning speed.
*  I see.
*  So there's some something in the middle, probably that is that best describes different parts of our brains.
*  I mean, so if you had infinite.
*  So one of the questions is always like, what if we just had added more layers and you had infinite amount of layers?
*  What would that do to it?
*  So in that equation, if the initialized structure is large, then you never learn.
*  Right.
*  Oh, wait, let's see.
*  B is large.
*  Now you have me doing math on the show.
*  If you can get.
*  Yeah, right.
*  If you can get that B to be one, then one to the D is just one.
*  Right.
*  So that's sort of the special point.
*  If you can manage to get.
*  And that that initialization corresponds to the unsupervised pre-training initialization.
*  The unsupervised pre-training initialization just described also corresponds to just initializing with what's called orthogonal matrices.
*  There's different ways of doing it.
*  But in that case, then you're right.
*  If you look at the limit of the learning time, as the depth of the network goes to infinity, it's actually still finite and not that much slower than a shallow network.
*  So, yeah, I think that's an interesting potential message.
*  It's interesting.
*  So, I mean, what what does this mean for learning in brains?
*  What have you how has this shaped your thought about how learning in brains occurs?
*  Well, I guess one direction I've tried to look at is developmental trajectories of human children learning semantic concepts and this kind of thing.
*  So, for instance, if you're learning about the worlds of animals and plants and dogs and cats and you know the animals, the broad category, the dog is the more specific category in this kind of thing.
*  You can formalize a version of that in this deep network scenario.
*  This is building off Tim Rogers and Jay McCullin's model of this semantic cognition study where you just have a neural network that it sees something like a dog and then it tries to predict all the properties that animal has.
*  So maybe the dog can bark, has fur, likes frisbees, this kind of thing.
*  And just from learning about those associations of items for the properties they have, these deep networks can come to organize their world hierarchically if there is underlying hierarchical structure in the properties.
*  And one of the things that developmental psychologists have observed empirically is children tend to learn the broadest distinctions first.
*  So first they'll master animal versus plant before they go on to dog versus cat and so on.
*  It's contested, but that's at least one version of reading the data.
*  If that's the case, the question is, when do you get that? Do deep networks do that?
*  And in fact, the answer is the deep networks do do that.
*  So these stages that they go through that I've just been talking about, when you expose them to hierarchical data, you can actually prove that for certain types of hierarchies, it must start with the broadest distinction.
*  And then go to the lower level distinctions.
*  And each of these categories is acquired with one of these stage like transitions in the developmental trajectory.
*  So it does look at least qualitatively like what we see in these children's trajectories.
*  And how is that related to so back in symbolic AI days, you'd have basically a tree structure.
*  You'd have these semantic networks, right?
*  Where you go down the branch points and then you end up with your semantics, essentially.
*  So and I know that's come a long way, but what you're saying is a somewhat structured,
*  I mean, because you have to structure the deep neural network that does the semantic learning as well, right?
*  Because you have different parts, categories feeding into the different layers of the network.
*  Yeah, well, it's fairly generic.
*  So it just gets different items as input.
*  You could think of that as I think of it as the output of IT or something.
*  So it's just like you're looking at a dog.
*  And then on the output side, it doesn't explicitly see the category dog.
*  It just has a bunch of properties it's supposed to.
*  Oh, I see.
*  I was thinking more of it like a sentence structure where there's an action being taken by the dog or something like that.
*  I see.
*  Yeah.
*  Yeah.
*  So at least in the simple example, it's quite generic and I find it very interesting still that
*  nevertheless it comes to organize its knowledge into a hierarchy and also to
*  generalize on the basis of that hierarchical structure,
*  even though you didn't explicitly build it in sort of the way that you would in some of these other
*  approaches you're talking about.
*  Yeah.
*  So in the symbolic approach, you'd say, well, I'm just going to explicitly fit a tree structure.
*  And then you can get these really fast stage like transitions.
*  Sometimes you see one more new animal or one more new property and all of a sudden the whole tree re-arranges,
*  which is kind of true of human development.
*  We do go through these massive reorganizations and there's a lot of beautiful work by Susan Carey.
*  It's called the theory theory.
*  There's lots of developmental psychologists pursuing this idea that we have different theories
*  of the world and our theories that we hold can undergo these fast changes.
*  But the sort of neural network response to that is, well, it's not actually a complete
*  stage like switch.
*  It's not instantaneous.
*  Really you get these graded transitions and you can't see evidence for that.
*  And that's some of the data that you might use to say actually the deep network is perhaps
*  explaining what's going on here.
*  I think I lost track and I'm now not realizing how the semantic network work relates to the depth,
*  the semantic knowledge work that you do with the hierarchy.
*  So is there a special level of depth related to the hierarchical structure that's needed?
*  Yes, yes.
*  Right.
*  So you might be thinking if I have a depth five hierarchy that I'm trying to learn,
*  I need five hidden layers.
*  Yeah.
*  That's actually not the case.
*  And you might be thinking, oh, maybe the lower layers learn about the smaller categories like
*  dog versus cat.
*  Yeah.
*  Leaves.
*  And the higher layers, that also turns out to not be the case.
*  What happens is all of the layers learn basically the same content.
*  They all have a hierarchical representation.
*  It just gets stronger over layers until at the end it's very strong.
*  This is in part because we're talking about linear networks.
*  Not really majorly reformatting things.
*  Maybe it's different with nonlinear networks, but at least in linear networks that's the picture.
*  And the other contrast to draw about, so why are we, what is depth doing here?
*  Well, you could have just had a linear network with no hidden layers.
*  And then it turns out it doesn't show all kinds of these phenomena.
*  So it won't have this progressive differentiation.
*  It doesn't go through stage-like transitions.
*  One other consequence of that, it's very salient, is you can go to a small child and say,
*  does a worm have bones?
*  And the child will say, yes, probably.
*  Of course.
*  Now they never could have seen that because no worm has bones.
*  So where did they get the idea?
*  The idea is you have this transient overgeneralization because most animals have bones.
*  And so you've said, well, the worm is sort of like an animal, it probably has bones.
*  Those kinds of transient overgeneralizations also probably don't happen in shallow networks,
*  but do happen in the deep networks.
*  So there's a whole rich set of phenomena that seems to occur.
*  Once you add these hidden layers, that doesn't occur in just the pure associator.
*  That's interesting.
*  So I had Talia Konkel on the show and she studies the visual,
*  ventral visual stream in image representation.
*  And she has kind of turned it on its side.
*  So the classic story is that you start in early layers and you get edges and really lower level
*  features, and then the representations become more complex until you wham, you have an object in IT.
*  But she has found that if you look at it on its side, the categories of things that you're
*  representing are the same across those layers.
*  So there's a category of swath of brain that crosses those layers that represents animate
*  objects. There's a swath that represents large inanimate objects and there's a swath that
*  represents small inanimate objects.
*  And that jibes well with what you're finding with the semantic representations across the units
*  as you get down to the levels.
*  Yeah, that's fascinating.
*  I probably should have already looked at that.
*  I will definitely look at that more afterwards.
*  So one other comment there is that's really about localization.
*  If I'm following you, you're saying this specific part of the brain sheet represented
*  large categories and this other area represented small categories.
*  And that was sort of consistent across layers.
*  So the basic deep network, the deep linear network solutions, they don't actually tell you about
*  localization because any permutation of the hidden layer, I could just undo and the next layer up.
*  And so you probably have to add some additional assumptions to get particular structuring to the
*  different layers.
*  But yeah, definitely the fact that all layers would partially represent all categories is a
*  strong prediction.
*  Yeah, interesting.
*  Andrew, I didn't say congratulations.
*  Didn't you just become a professor?
*  Well, yes, but the title is not that here.
*  But yes, pretty much.
*  Oh, well, what's the title?
*  It's Sir Henry Dale Fellow.
*  Oh, sounds very British, doesn't it?
*  Anyway, it sounds like you got a sounds like you're promoted.
*  So congratulations.
*  So not a postdoc anymore.
*  That's great.
*  Okay.
*  So what do you think?
*  Are we basically on track to replicate all the brain principles in AI eventually?
*  Or is it going to or will AI look vastly different from the way it works in brains
*  when we get to whatever we really mean by artificial general intelligence when we get there?
*  I'm not sure.
*  I mean, I think there might be a lot of core ideas that are shared.
*  But if you're making a system that does, I don't know, hyperspectral imaging or processes,
*  specific types of data, it's at least conceivable to me that you'd have
*  other principles at work beyond what happened in brains.
*  Why would we limit ourselves to brains?
*  Yeah, I mean, there's the standard argument of, oh, we don't build planes the same way
*  the birds fly.
*  But I think I'm also sensitive to fighting the last battle, right?
*  That's the other thing is maybe that was, well, first of all, I don't actually think
*  that was true in detail if you look at the plane story, but setting that aside.
*  That sort of idea is we don't know what the next step is going to take.
*  It could be that actually looking to the brain is the right step.
*  And I think I'm just glad there's lots of researchers trying lots of different things.
*  Yeah, and throwing everything at the wall.
*  How is your perspective about the power of deep learning in general?
*  How has that changed as you've learned so much more about it?
*  Yeah, I think there's no question it's a field with a ton of hype.
*  And so looking at the AI winter, you have to say, okay, wait, what here is really going
*  to stick around?
*  And sometimes I like to distinguish the greater deep learning hypothesis from the lesser one.
*  So what I've talked about today, I mean, you heard me talk about basically feedforward
*  networks.
*  This is a very simple scenario.
*  Yeah, doing perceptual classification, essentially, right?
*  Right, yeah.
*  So it's clear that that is not the whole picture, right?
*  There's a lot of other stuff you're going to need.
*  In that view, this might just be one step forward.
*  I do think it is one step forward.
*  And the question it forces you to ask is how structure relates to learning dynamics.
*  I think it's an important question.
*  The greater hypothesis is to say, well, if we start adding additional principles, like
*  if, for instance, we step back and say, deep learning just means optimization of cost functions,
*  then maybe that's general enough that it could start getting us quite far.
*  But it's also general enough that it's quite vague, right?
*  So it doesn't really constrain that much of what you could propose.
*  For instance, the entire free energy principle, which is already quite
*  general and vague, you can formulate it's just a cost function optimization, right?
*  So it's contained within this greater deep learning hypothesis.
*  So I feel like the most interesting thing is to make these proposals as specific and
*  concrete as possible.
*  But that's just my personal perspective.
*  The idea of progress is interesting to me.
*  It's not even clear to me what progress actually is.
*  And I'm wondering if you have an idea of what you consider a meaningful sort of unit of progress
*  in what you do, for instance, in theoretical neuroscience.
*  What would it mean to advance something?
*  And to you, what feels like progress, for instance?
*  Because I ask because a lot of people from the AI side of things say, well, you're just
*  trying to solve problems.
*  And in that sense, a unit of progress is pretty easy because you solve the problem,
*  and that's progress.
*  But on the neuroscience side, unless you're trying to, well, I mean, we're all trying to
*  help cure diseases, and that would be progress.
*  But just understanding what's happening in the brain is somewhat of a vague notion.
*  And it's hard to know, like, well, when have I actually progressed in my understanding
*  of what the brain is doing?
*  So do you have an idea for you personally?
*  Yeah, it's something I think about.
*  I'm not sure I have made it fully concrete.
*  But to me, it really is a psychological sense of having a model or concept that I feel like
*  I can get my head around psychologically.
*  Like, I want to understand it.
*  And that, you know, I've had that feeling a couple of times where there was something
*  that's totally confusing, and now it's like, no, I've got this.
*  So the generalization was one thing.
*  You know, to me, that psychological aspect might be irreducible.
*  Even if tomorrow there was a neural network that predicted every brain activation everywhere
*  in the brain and also solved all general artificial intelligence, I would not feel done
*  because I want to feel like I know how it works.
*  And that is also enormously motivating.
*  There are a lot of people, by the way, who think that's impossible.
*  So I have plenty of people say, why do you even do theory?
*  These networks are so complicated, we'll never understand them.
*  And again, I come to realize that I think it's a timescale thing.
*  So I don't expect to understand them tomorrow.
*  But if you look at the gap between Aristotle introducing physics to Newton
*  actually getting somewhere quantitative, it was thousands of years.
*  So, you know, we just started.
*  I think we will invent the conceptual tools that allow humans to understand deep networks.
*  Even these complex nonlinear ones.
*  I just think it's going to take a while.
*  I actually had Jay McClellan on the show and, you know, he's got this.
*  He gave himself 10 years because he thinks he's toward the end of his career.
*  He gave himself 10 years to figure out mathematics in deep networks, you know.
*  So he's still fully committed to the long run.
*  Less long, but still committed to the long run.
*  Yeah.
*  Yeah.
*  What's something that you worry about or makes you nervous?
*  Well, right now I'd say Brexit.
*  I mean, as a UK academic, it's not great.
*  Yeah, right.
*  I think there was some good news that came out the other day, right?
*  Yeah, it's hard to follow all the twists.
*  I know.
*  My advice is not to follow any of it, but okay.
*  Yeah.
*  Science-wise, I guess I'm slightly worried about the hype
*  leading to unnecessary winter.
*  But I think the difference this time around is it's making people money very clearly.
*  Deep networks are actually deployed.
*  That's a difference that wasn't true in the previous winters.
*  So I'm not actually super worried about that.
*  Well, it was true in the 70s during the expert systems times, right?
*  So there were systems that were being deployed and it was making companies money.
*  Yeah, before that, it was all theoretical and all the funding dried up pretty quickly.
*  Yeah, but I'm with you.
*  I don't think funding is going to dry up, but I don't know why I think that.
*  It might be a naive assumption.
*  It just seems like it's just too much of a tidal wave right now.
*  What's something that you pay almost zero attention to
*  that you know you really should be paying attention to?
*  Well, I was about to say reinforcement learning,
*  but I do have a thin thread of work on reinforcement learning.
*  So I can't say zero attention.
*  I think actions add a whole bunch of interesting concepts that have to get in the picture
*  that I haven't really been looking at so far.
*  Yeah.
*  What's something that you mentioned earlier,
*  if you might just repeat what you said earlier,
*  but what is something that you used to believe that you now consider naive?
*  I used to believe that, oh, these are going to sound so arcane,
*  but I used to believe that the main barrier to training deep networks was local minima.
*  I now don't believe that at all.
*  Well, you've done work on that so that essentially there aren't local minima.
*  So you researched your way out of that belief.
*  Sure.
*  Yeah, I used to believe large models wouldn't generalize at all.
*  There's another one.
*  I remember running that simulation just going, what?
*  Like I've been, it just exploded my intuition seeing these large models doing well.
*  In retrospect, now it seems very obvious, but at the time it was quite surprising.
*  Those are the best.
*  I love those moments.
*  What's one trait of our intelligence or cognition that you think will be
*  especially difficult to build into AI?
*  Well, I think there are probably many.
*  One question that I've become interested in sort of gets into meta-learning ideas,
*  what Matt Bobfenik and his collaborators have been working on, which seems like
*  one thing humans can do is set up and manage a new learning problem.
*  If I put you in front of a computer game, you'll treat the point score as the objective
*  that you're aiming for.
*  It seems to me like that's actually quite a delicate thing because you have every
*  incentive to lie to yourself.
*  If you said, all right, this point score is not actually my objective, dying as
*  quickly as possible is my objective, you get a much higher score much more quickly.
*  And so there's this question of like, how do we hook up these internal rewards and
*  what we call the correct answer?
*  How do we hook these things up to actually get the system performed very well?
*  You might call it cognitive controlled learning.
*  That seems like one complicated thing towards getting these systems to be more general.
*  Do you think that any of this is going to lead to any sort of satisfying account of
*  subjective awareness?
*  Not deep linear networks.
*  That's the secret is linear networks.
*  I think we're going to do it.
*  But yeah, I mean, I think this is one step on the road.
*  I do.
*  I think it's one step on the road, but I think we're going to need
*  genuinely new ideas to close that particular gap.
*  I also don't personally believe that it's just a matter of making the systems bigger
*  and training them on more data.
*  I think there's going to be some new concepts that we need to get the subjective piece off
*  the ground.
*  Well, Andrew, thanks for spending so much time with me today.
*  Are you so I said you're stuck in linear networks, but are you going to jump out?
*  And what's the main focus of your lab going to be going of your work going to be going forward?
*  I wouldn't call it a lab.
*  It's not a lab.
*  I'm used to saying lab.
*  Yeah, no, it's I mean, theory lab.
*  There's sort of two prongs.
*  The first is just extending our mathematical toolkit for understanding these models.
*  And I think that's everyone has said that deep networks are black boxes.
*  If we can change that, it will be a great accomplishment.
*  And then the second big thread is experimental collaborations to see exactly
*  if we can make these things precise enough to test them.
*  So those are the broad categories.
*  Some of the theory uses deep linear networks, but a lot of it doesn't.
*  It's just it's interesting.
*  There's a huge literature from statistical physics on neural networks, which is super relevant.
*  You could read this stuff from the from a while ago, and it could be published today.
*  And so sort of mining some of those insights, bringing them back seems really worthwhile to me.
*  Interviewed Nathaniel Dahn, and he does a lot of theoretical work, too.
*  And he said among he and his friends talk about whether they need to start their own
*  experimental labs, because everyone's got a theory and they're looking for experiment experimentalist
*  to do it.
*  But when I started, I didn't even appreciate the difference between someone who did theory
*  and someone who did experiments only, because I just thought everyone in computational neuroscience
*  and cognitive computational neuroscience did both.
*  And so now there seems to be a real clear theoretical drive.
*  And then there's all these people doing experiments.
*  They're like, Whoa, I got my own stuff to work on here, buddy.
*  I don't want to have to test your theories.
*  Yeah, that's right.
*  I mean, that's also true.
*  Yeah.
*  So I did do I did a lecture physiology experiment during my grad school years.
*  And I would consider doing psychophysics experiments.
*  I did some of those, too.
*  But I think at the end of the day, I have to admit other people are just so much better
*  at it than I am that I should probably stay in the theory world and try to see if we can
*  get the collaborations working.
*  Well, man, you're doing really great work.
*  And so I really appreciate the work that you do.
*  And and talking to me today, you must get people also thankful that you are doing these
*  simplified versions of models to see like what to isolate the effects of depth and what
*  underlies generalization and things like that.
*  Yeah.
*  Yeah.
*  But maybe they haven't expressed it.
*  Yeah, no, sure.
*  I mean, it's it's um, there is something satisfying when you feel like it.
*  You understand it psychologically.
*  So yeah, I hope it grows in the future.
*  Well, good luck, Andrew.
*  And I appreciate you.
*  Thanks.
*  Yeah.
*  Thanks for your time.
*  Brain inspired is a production of me and you.
*  You can support the show through Patreon for a microscopic two or four dollars per month.
*  Go to brain inspired dot co and find the red Patreon button there.
*  Your contribution will help sustain and improve the show and prohibit any annoying
*  advertisements like you hear on other shows.
*  To get in touch with me, email Paul at brain inspired dot co.
*  The music you hear is by the new year.
*  Find them at the new year dot net.
*  Thanks for your support.
*  See you next time.

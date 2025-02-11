---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 3649s
Video Keywords: ['Education', 'Science', 'Technology']
Video Views: 9081
Video Rating: None
---

# BI NMA 03: Stochastic Processes Panel
**Brain Inspired:** [July 22, 2021](https://www.youtube.com/watch?v=AbiGI_ciCTM)
*  This might actually be something useful for the Neuromatch listeners out there.
*  Maybe we should briefly talk about the concept of normative models, because I think all four
*  of us are deeply committed to that way of thinking.
*  Why are we so excited about normative models?
*  Math is so cool because you can take reality and kind of transfer it to this space where
*  you can do operations and get something new and then come back and that will still correspond
*  to reality.
*  I think if you want to be really original, you're going to have to give up some coolness
*  because there are many people who are entering the field kind of swept by this wave of enthusiasm
*  for certain ideas like deep learning.
*  And what that means is that many people are basically doing more or less the same thing.
*  If you're still working on the same thing you told your hiring committee you would work
*  on 10 years later, then something has gone wrong.
*  And probably most people find their questions because their data don't make sense without
*  different questions.
*  This is Brain Inspired.
*  Hi everyone, I'm Paul.
*  This is the last discussion panel of the first round of NeuroMatch Academy where we are ostensibly
*  talking about stochastic processes.
*  Bayesian inference and models, decision making, optimal control, reinforcement learning, causality,
*  those were the topics for the past week in NeuroMatch.
*  With me today are Yael Niv from Princeton University, Conrad Kurding from the University
*  of Pennsylvania, Tim Behrens at University of Oxford, and Sam Gershman from Harvard University.
*  And three of those people, Conrad, Tim, and Sam, you've heard multiple times on the podcast
*  before, but Yael is a new person on the podcast, so it was really nice to have her.
*  So we do talk high level about some of the topics related to this past week, especially
*  normativity and why these models are good models to use to understand brain function.
*  And then we go on to talk about a host of topics related to just doing science and thinking
*  about these sorts of things, where questions come from, and how to get a good question.
*  I make the fun mistake of calling mathematical and computational approaches to the brain
*  sterile, by which I meant no harm, but it sets off quite a discussion that then winds
*  its way among many other topics.
*  For the record, I call this approach sterile in terms of its purchase on matters of connecting
*  brain function to subjective experience, qua philosophy of mind.
*  And that set off a fun flagellation of me, which was fun.
*  I link to all the guests and to Neuromatch Academy in the show notes, braininspired.co
*  slash podcast slash nma-3.
*  Okay enough of me, better things await you, and here are those better and fruitful, I
*  hope, things.
*  So what I'd love for you to do is just introduce yourself, what you do generally, very high
*  level, and then what I would like you to say just as an example, as a personal example,
*  what do you think you're best known for, and what are you most proud of in your work?
*  So Konrad, perhaps we should just start with you, the Neuromatch central person here.
*  Well great, thanks for having me.
*  I'm Konrad Kodding.
*  I am one of the co-founders of the Neuromatch movement.
*  I deeply believe in accessible teaching and communication in the field.
*  I'm probably best known for Bayesian models of how we might be thinking.
*  And I think I'm most proud about thinking about the epistemology behind neuroscience.
*  Nice, proud of the thinking.
*  So that hasn't...
*  That's right, exactly.
*  So I've been struggling for years with how I want to think about brains, and I oscillate
*  between many different views.
*  And I think I'm seriously most proud about giving all these different ways of thinking
*  a brain in a way, like what I feel to be a fair shake, despite the fact that I'm deeply
*  opinionated obviously.
*  I imagine that's a trait of many among the panel here.
*  Yael, who are you?
*  And what do you do and what are you best known for and what are you most proud of?
*  Hi, I'm Yael Niv.
*  I am at Princeton University.
*  What am I best known for?
*  I think I might be best known for reminding people who study reinforcement learning that
*  we should think about how states enter into the picture, so how people and animals learn
*  what are the states of a task or what's the structure of a task.
*  What am I most proud of?
*  Actually, you can ask Sam later what I'm best known for, because he was making some kind
*  of face that made me think I'm saying the wrong thing here.
*  Well, I was just going to say that I don't have to say what I'm best known for anymore.
*  That's right.
*  I'm best known for what Sam discovered when he was in my lab.
*  No, no, no.
*  I'm not trying to steal your thunder, Yael.
*  I'm just saying that I'm best known for probably the work that I did with you.
*  Yes, well, similarly here, I'm best known for the work that you did when you were in my lab.
*  And actually, that goes well with what I'm most proud of.
*  I was trying to think really quickly because I didn't think of this before.
*  Maybe you asked us to do that, but I didn't.
*  What am I most proud of?
*  And I think that's the fact that I once got a graduate mentoring award.
*  Early on, that was an early on career.
*  That tends to be a common answer is when, oh, no, a reward that you got as a faculty member
*  mentoring a graduate student.
*  Is that what that is?
*  Yes, I got a graduate mentoring award as faculty.
*  Not that early on, a couple of years ago.
*  Yeah, very good.
*  Tim, let's swing it to you.
*  Who the heck are you, Tim?
*  What do you do?
*  What are you proud of and what are you known for?
*  Yeah, so I'm Tim Burns.
*  I guess I probably best known.
*  I don't really know, but I made some software that is popular for
*  figuring out brain connections.
*  And so I guess that's certainly what I'm most cited for.
*  So I assume I'm best known for that, too.
*  I'm most proud of.
*  I don't know, maybe there's a diversity of stuff.
*  I've dipped my nose in some.
*  I mean, I sort of sort of feel like I've tackled a few different problems always
*  with a couple of themes.
*  So I try to think of new ways of thinking about data.
*  So trying to see what you can measure that we couldn't measure before.
*  And and I
*  often try to think that something isn't solved until you can see it more than one
*  species and more than one technique and that kind of stuff.
*  So that's that's mostly why I do.
*  Thinking about that diversity, I mean, all of you on this panel have expressed
*  that that diversity in interests and in your works, which kind of goes against.
*  Maybe common.
*  You know, what you're supposed to do is dive really deeply into one topic
*  or two topics, right?
*  And that's that's the way you make your bones.
*  But I mean, everyone's shaking their head.
*  So I think there's different models.
*  I agree with you that you should go deep,
*  but you don't have to stay with often when you go really deep.
*  You find that you're related to something else.
*  I think in an interesting way.
*  And so I think that the ability to think, to see relationships
*  across different things, I think is
*  is another powerful way that academics make them.
*  There's the guy that entered the
*  the guy that invented MRI,
*  who shamefully well, I mean, he didn't know.
*  So this is actually this is wrong.
*  He's got a Nobel Prize for his contribution to nuclear magnetic resonance.
*  And I think it was Han, although I can't remember.
*  But somebody else will remember better when I say that he also figured out
*  the dynamics of motion of of bacteria and things like that,
*  using the same kind of physical principles that he discovered for animal.
*  I think it was hard.
*  I think the. Yeah.
*  I wanted to say that you're also talking to a group of theoreticians here.
*  And maybe maybe this is a little bit more characteristic of theoreticians,
*  that it's not only what Tim is saying, that you take one method
*  and find connections at different places.
*  But sometimes what I find with a few myself and a few of my colleagues
*  who are theoreticians is we're interested in a problem.
*  We make, you know, some headway in it, clearly not solve it
*  and like the solved term, but then kind of lose interest in it.
*  And it's like, OK, so what's the next problem I'm going to solve?
*  I mean, some people, again, there are different ways to do this.
*  Some people spend their whole career on some problem on one problem.
*  And some people after three, five years are like, OK, done with that.
*  Now let's go to the next thing.
*  I think Tim is expressing is a somewhat different sentence.
*  I'm not saying that that doesn't happen, but I resonate with what Tim was saying
*  in the sense that what going deep really means
*  in some cases is to attain a level of abstraction.
*  And you're thinking about a problem that renders visible connections
*  that you didn't see before. Right.
*  And so it doesn't not the same as just drilling down for in the same topic forever.
*  Well, Sam, I was going to say
*  you may be best known for not being very deep yourself.
*  So let's but I don't know what that's supposed to mean.
*  I don't know. I just wanted to give it a little spice.
*  Sam, who are you?
*  What do you do? What are you best known for and most proud of?
*  I I'm a professor at Harvard, and I think we already covered
*  what I'm best known for, I guess, possibly my work with you.
*  And I say what that was about.
*  You should say, yeah, I mean, it's the causes.
*  Everybody knows he's best known for it. So.
*  It's also been I mean, no, no discredit the other.
*  It's also been massively developed in your own life as faculty as well.
*  And so it's worth noting that that is a major achievement.
*  The also well known for. Yeah.
*  Yes, it's the problem, I would say, broadly speaking, of structure learning.
*  How do we discover the structure of the world around us?
*  And that has many different manifestations in reinforcement, learning and beyond.
*  As far as what I'm most proud of, I really have to go with
*  the people answer, which is I'm most proud of the students and postdocs
*  that have gone through my lab, because that's really the gift that keeps on giving.
*  OK, so I just had to look back because there's a lot of topics
*  that were covered throughout the the week.
*  There's Beijing topics, decision making, optimal control,
*  reinforcement, learning and causality.
*  So I guess our conversation should be centered around these topics loosely.
*  We can't drill down into into all of them.
*  But maybe I'm you know, one way to start start this off is to ask
*  where you guys think, you know, which of these topics
*  has the most fruit to offer in terms of connecting?
*  Because these are very it's computational neuroscience.
*  Computations are sterile mathematical objects.
*  Which of these I just do sterile in there for fun.
*  But which which has the most fruit to offer in terms of connecting
*  minds with brains or what we what we think of as minds.
*  So I think I zoom out in a way.
*  I think it's this week that has a lot to offer, which is in the first week
*  we learn a lot about the basics and techniques.
*  Whereas this week we learn about these concepts that we can relate
*  to the way we think in a way much more than maybe what we did in the first week.
*  So I mean, I think both based in RL,
*  which are two things that are close to all of our hearts on this call
*  are both tools and models of the brain.
*  And and thinking of them in both of those ways is informative and exciting
*  because it means that you can imagine how your brain might be working
*  in the same way as how you can be analyzing your data, which I think is.
*  Yeah, I mean, that's something that I always love whenever whenever you.
*  I love the fact that with Bayes, what you have to really specify
*  if you're going to solve a problem is a generative model.
*  And the rest of it, you then choose between the sort of Bayesian toolkit
*  that's available.
*  But once you once you understand what the problem is,
*  that is enough to specify the solution.
*  And somehow that what I that's that's what I think is
*  something purely elegant about that, because really, as a theoretician,
*  your job is to understand the problem, not to solve the solution.
*  And there's something beautiful about imagining the brain that way, really.
*  What it's trying to do is build is understand the problem,
*  the world around it as the problem, build them, build a forward model of that.
*  And then it can learn that inversion somehow.
*  There's something beautiful thinking about that way.
*  And you can actually express reinforcement
*  learning in those same terms as well, if you if you choose to.
*  Also, these these two theories are both normative.
*  So, you know, Bayesian inference is a kind of statistically
*  optimal way to integrate information and reinforcement learning is a
*  optimal way to learn predictions, to learn expectations.
*  So. In that sense, I think what Tim was saying is both of them,
*  we can use them as data analysis methods, for instance, when we get data
*  and we want to, you know, extract information from it, we can use these methods,
*  especially Bayesian inference is
*  as tools as you know, that you could use in many areas.
*  But then our brain does that too,
*  because our brain is so optimal and awesome.
*  Just the other day, my son asked me if our brain, if like our neurons
*  compute all kinds of things and can do exponents, how come we don't know
*  how to do exponents when we are babies?
*  And so, yeah, our brain knows how to do Bayesian, really optimal,
*  awesome stuff that we don't know how to do yet as researchers.
*  Yeah.
*  When what do you start asking these kind of questions?
*  My son is he's nine and a half.
*  Wow. So it's two years.
*  So it was our own. OK.
*  So maybe we should briefly talk about
*  the concept of normative models, no, because because I think all four of us
*  are deeply committed to that way of thinking.
*  Why are we so excited about normative models?
*  I don't I don't think that we should.
*  Shackle ourselves to normative models.
*  I tend to think of normative models more as a kind of starting point
*  for thinking about the problem, like I thought Tim put it well very well.
*  One way of approaching the complexity of the brain is to say that
*  there are certain problems that the brain is trying to solve.
*  We can stipulate some assumptions that we impute to the brain.
*  And then once we basically specify the problem, we can ask what we try
*  to characterize the solution and ask whether that is
*  at all similar to what we can measure about brain and behavior.
*  But that that doesn't necessarily mean that
*  that we have to that all of our models have to be purely normative.
*  There are points in the modeling process where we have to kind of adapt them
*  to the biological constraints, which might also be normative,
*  but it's not always obvious what what they are.
*  Sometimes they're just kind of empirical constraints.
*  Yeah. I mean, like for me, then not the drive to what's normative thinking
*  drives from me, me kind of I feel like
*  I understand those aspects.
*  It's it's the normative models are usually of the flavor where I say something
*  in the world, there's noise in the way you move your muscles.
*  In the world, there's noise in the way we perceive things.
*  And it feels like those are things that I can understand
*  because they're not relating to the brain, which I'm very conflicted
*  about what we know.
*  There's something about the world and then ideal behavior, optimal behavior,
*  like derives from that understanding that we have about the world.
*  And as scientists, we're very used to talking and thinking about the world.
*  And so in that sense, for me, at least the drive towards normative models
*  comes from a sense of humility about what I feel I really understand
*  about the brain.
*  You feel like you understand optimality assumptions?
*  I mean, I'm not saying that you can certainly write down
*  a mathematical equation and say, I understand the equation, right?
*  But you feel like you understand the
*  biology well enough to say, all right, these are the optimality
*  equations that the brain is actually solving.
*  Well, I don't think we know what which optimality equations
*  our brain is really solving, but we have an idea about that.
*  And like we are talking in most cases about humans trying to do certain things.
*  And if you play tennis or something, I know that you're trying to score points.
*  I don't need to understand the whole properties of your brain to like
*  get at meaningful models.
*  And if you come to my lab and we do an experiment with you,
*  I will pay you based on the points that you make in that game.
*  So in that sense, there exists a lot of and even areas where it's not so clear,
*  let's say soccer, where you could say, well, that's this thing of how well I got space.
*  And sorry again, Tim, for the Euro Cup.
*  But like we reason about it.
*  Now, like like like our language is full of things about what we are trying to achieve.
*  So that's that there's a risk there of missing out on a lot of things
*  that we're trying to achieve as humans, which are all the social things
*  that we're trying to achieve.
*  Even while you're playing tennis, you're trying to score points.
*  But maybe you want to shame the other person.
*  Maybe not. Maybe you want the audience to like you.
*  Maybe you want, you know, who knows what else?
*  You might not be super aware of that.
*  You might not report it, but it might be driving a lot of your actions.
*  And I think one of the things that we,
*  you know, there's been a lot of advance in cognitive neuroscience,
*  thinking of a person as a single unit that that, you know, a brain in isolation,
*  but actually in the real world, we're like we're such social animals.
*  So we've missed a lot.
*  And that may be, you know, where we should go next.
*  And I think where Sam is going is going with his research is is really bringing in
*  the social component.
*  I mean, there's there are a lot of people who are thinking about
*  sort of cognitive neuroscience as possible.
*  They're not thinking about it with the same naturalistic way you're thinking about.
*  But but there's a yeah, it's just worth pointing out that there are there are.
*  Oh, yeah, yeah. No, I mean that nobody's research.
*  Like us here in this conversation saying, you know, we know what people are
*  optimizing that misses a lot, you know, maybe their motor actions.
*  I want to, you know, not spill the coffee from my cup.
*  But that's such a small part of our world of what we're optimizing.
*  People are optimizing.
*  I don't know if I know if people are optimizing.
*  So when it comes to social things, I think it's not true
*  that we don't have good ways of starting to think about it.
*  And like people spend a surprising amount of their days talking about social relation.
*  Hey, I would like to convince them that I know what I'm doing.
*  I'm worried they're judging me like a lot of human language
*  is exactly about what we are optimizing in social relations.
*  So so I don't think that that space is fundamentally different.
*  Maybe for the Neuromatch people.
*  So sorry to move us away off social neuroscience,
*  but I think probably that's not our collective area of expertise.
*  Maybe it is worth just specifying this difference
*  between a normative model and a and and and what the alternatives are.
*  And so I mean, I suppose
*  in some sense, there are models that we know do something as a model of the brain.
*  And then we ask, well, here's the model that does something.
*  Does it look like what the brain does it?
*  And let's cross all of those as normative.
*  I know that that's going to there's going to be debate about that.
*  But let's put ConvNets and all that kind of stuff in that class of models.
*  Kind of what model?
*  The answer to the question of what does the brain do?
*  Not, for instance, how does it do it?
*  Well, even with a ConvNet or with something like this
*  told me like machine that I built, you can say, OK, let's look at
*  let's look at the the it's solving a problem.
*  I understand what problem it's solving.
*  And I can look inside the representations and they look similar to what the brain does.
*  The sun. So this is that kind of model.
*  All those are model of all you can do that.
*  That kind of thing without anything about the brain at all.
*  And just look at the behavior, as he says, a what model?
*  But then there are like other types of models that are models directly of the data.
*  Or there are models or the or there are models
*  of the brain that that's just try to to predict the
*  how the how the neurons interact with each other without knowing.
*  The process process.
*  Yeah, exactly. The process without considering
*  what the problem is, the neurons are trying to solve.
*  I guess those are the sort of three classes of models.
*  And it and they could consider they can consider what problem is being solved,
*  but they're more focused on how is that problem solved rather than
*  what is the problem that is being solved?
*  Yeah, OK. Yeah. Yes.
*  I mean, you know, if you have a circuit model of
*  how a neuron can compute a prediction error, the problem is compute a prediction error.
*  And you can say here is how the circuit can do it.
*  But it's not asking why should you compute a prediction error to start with?
*  That's what I thought, as I just would need to press a go with you guys.
*  And I didn't expect to talk again.
*  So but but I wanted I wanted to say one one more thing.
*  Gosh, now I can't remember exactly what it was linked to before.
*  But Paul, you said that math is these.
*  How did you describe it? Sterile, sterile.
*  You said that, like, we're computational people and the math is sterile
*  computational stuff and call you sterile.
*  The computational approach is kind of sterile.
*  I wanted to say that
*  there's this awesome book called Dialogues on Mathematics by Alfred Renne
*  that has like three short dialogues and like, why is math relevant?
*  Like, why do we care about math
*  in the form of dialogues between like Achilles and the Tortoise or something like that?
*  And the main point there is that math is so cool because you can take reality
*  and kind of transfer it to this space where you can do operations
*  and get something new and then come back.
*  And that will still correspond to reality.
*  So like we can't it's hard to do operations on things in the world,
*  but it's easy to do operations on things in math and maintain kind of truthness
*  when you translate back.
*  And I think in that sense, these normative models are very important.
*  And I think that the normative models or the classes of models
*  that we're talking about, there's this abstraction that you can work with
*  to understand things about the brain, even if every part of the process
*  is not how the brain does that process.
*  So the brain has to do a lot of, you know,
*  satisfying and taking, you know, really hard computational problems.
*  You can't you just like, you know, a lot of things we can't even solve optimally,
*  supercomputers with Bayesian inference because they're just too big.
*  And the brain just does this all the time.
*  So it must have some shortcuts to do this.
*  But we can, you know, we can move in the mathematical space.
*  We don't know how to move in the brain space.
*  And then we get to something and we're like, OK, so the brain should
*  in the end have as a product of the computations, this and that.
*  And you go back to the brain and you're like, oh, lo and behold.
*  Or at least you go back to behavior and you see, lo and behold,
*  there are signatures of this mathematical quantity there,
*  even if you don't know how the brain computed it.
*  But when I was talking about the sterility of the computational approaches,
*  what I was trying to link it to was mind, because there is brain
*  and there's the, you know, the implementation of how it happens in the brain.
*  But at that abstract level in mathematics, does that help us
*  connect to what we think of as mind subjective experience that we
*  many of us know, let's not be right there.
*  In what sense is mind subjective experience?
*  Well, so it depends on how you define mind.
*  It's part of mind, right?
*  It all depends on how you define mind.
*  But people commonly think what I mean is subjective experience.
*  That's what I mean, because that's the the connection that is that.
*  Well, that's the question.
*  Is there a connection?
*  Does do the computational models help you?
*  And I know that subjective experience is not the goal of the computational
*  neuroscience program at Neuromatch.
*  So we don't need to go down that road.
*  But that was more the upper level question.
*  I think of mind is just the functioning of the brain.
*  So I think, Paul, I feel like it's very illuminating what you just said,
*  because I actually think a lot of neuroscientists think in this way,
*  which is that there's all the mechanistic stuff that happens with the neurons.
*  And then there's mind and mind is all the subjective stuff that we experience
*  and are phenomenal experience.
*  And I think that that view,
*  I mean, I'm caricaturing it, but I think that that view stems from
*  a sort of lack of knowledge or in some cases, disinterest in psychology
*  and cognitive science, because there's lots to think about the mind,
*  even not talking about neurons.
*  That's not about subjective experience.
*  And it's kind of and it's sort of like there's this whole missing chunk
*  of knowledge that.
*  Yeah.
*  And also, if the so I'm just going to plus one on.
*  I'm not sure how you do plus one on a podcast,
*  but plus one on what Sam was saying.
*  I just add that people that if if neuroscientists
*  are going to give up on the brain side of subjective experience,
*  to think is what episodic memory people look at or I mean,
*  there's a whole load of people in neuroscience that that investigate
*  that from a non computational perspective.
*  Then if we can't think of that computationally, then we failed.
*  But subjective experience is part of the brain.
*  And so both so I think that on like looking at it both ways,
*  wrong, Simon, I probably disagree with you about the statement
*  you just made there. Is that fair, Simon?
*  Or yeah, I mean, I was making a different point, which is just setting aside
*  the validity of subjective experience as a topic of study.
*  I'm just saying that the view that mind is subjective experience,
*  I feel like permeates the thinking of many neurologists
*  and prevents them from really engaging
*  with the cognitive aspects of brain function.
*  But Paul, I want to bring back the big point to you.
*  You said sort of like you guys enter computation, isn't that super sterile?
*  And isn't that far away from the subjective experience?
*  The whole premise of that is that for some reason,
*  just because we use mathematical tools, we are further away than, say,
*  an experiment.
*  And I just don't want to accept that as an assertion.
*  So basically, just because our favorite tools
*  is an equation that doesn't in any way make it more sterile
*  or further away from reality.
*  I'll tell you, the equation is not the way we study the brain.
*  The equation is often stated, a hypothesis that we then go and test
*  experimentally or in other ways.
*  It's just it's a tool to ask questions really precisely.
*  So but let me just let me just back up, Paul, for a second and challenge.
*  Why is this all on me? I'm just asking questions.
*  I'm not I don't have a position that I'm coming from,
*  that math is sterile and experiments aren't or something.
*  But I'll take that. I'll be that person.
*  I'll be the punching bag here.
*  You're a professional podcast host, so everywhere it counts.
*  A provocateur. Yeah.
*  But let's let's say we're studying the kind of thing
*  Yale studies or some studies where we have what we really want to understand
*  is the graph of the experience of the task or something like that.
*  If we if we didn't need equations to be part of this,
*  then we would design our experiments very differently.
*  It is unfortunately true that we do have to design our experiments
*  to be tractable to the equations that we want to investigate.
*  And so and sometimes they do end up seeming a bit dry
*  and drier than than than they than they would do if we didn't.
*  If we weren't making these precise computational statements.
*  So it's driving. Oh, sorry.
*  Good. No, no, no.
*  I was wondering why sterile and dry.
*  These are
*  turn kind of not exactly insults.
*  Not if you're lying. I got that.
*  Well, it just it's it strikes me that, I mean,
*  it really depends on your cast of mind.
*  Some people find the mathematics enthralling.
*  And that's right. Right.
*  And so I don't I'm this is I'm not going to make a value judgment about it.
*  Some people like it and some people don't. That's fine.
*  But that wasn't the point.
*  I mean, so I think the math is fantastic.
*  Even even in.
*  But I think that the fact that we're trying to get to that level of prescription
*  means that we have to do experiments that are not naturalistic often.
*  Yeah, exactly.
*  But we can take the two of them totally apart.
*  And like we can do naturalistic experiments with stuff, stuff
*  that is really like real life using math,
*  because that's the precise way of asking questions.
*  And we can use absolutely boring, trivialistic lab tasks
*  without touching a line of code or math.
*  So I just just think this like perception, not like,
*  sure, computation is hard.
*  And that's why people go to a neural match and learn about it.
*  But that like the magic isn't
*  and isn't diminished the slightest bit by that.
*  And I think that that's important.
*  I think you're mischaracterizing what, at least to me, from my vantage point,
*  the computational aspect is the magic is that is the the top level.
*  What you should what everyone should be doing,
*  how everyone should be thinking about about brains.
*  And I don't see any evidence to counter that.
*  I would say that's not magical, Paul,
*  because magic implies that there's something you don't understand.
*  This is we're going to quibble over words.
*  Sorry. Why don't you lead us back to the fact that you really important?
*  I think this is really important.
*  And I think this is one of the things that the goal of a course like
*  Neural Match is, is to make it not look magical,
*  because magical seems like something that I can't do myself.
*  And Conrad said the math is hard.
*  Lots of things are hard.
*  Doing experiments is hard.
*  Like a lot of it is hard, but it's all learnable.
*  And I mean, different people find it easier to learn different things.
*  But I think I mean, speaking about Bayes and inference,
*  you asked in kind of the email that you sent us, one of the things was,
*  what did we struggle most in our career?
*  And one of the things I was I was kind of laughingly telling myself
*  it's Bayes and inference with Bayes rule.
*  Like I knew Bayes rule and I sat for like, I don't know, two years in my
*  in the lab where I was as a graduate student.
*  And people would talk about Bayes and inference every day, pretty much,
*  or every other day.
*  And I would be like, how did they always remember which part is the prior
*  and which part is the posterior?
*  And like those didn't make sense to like, I understood I I could derive the equation.
*  It's a very simple equation, but it didn't I didn't have the intuition for it.
*  And then at some point it clicked.
*  And now, like, I totally like I see it and I understand it.
*  And so it used to look like magic to me, like magic in the bad way of like,
*  I don't know what's the input and what's the output.
*  How do they compute these probability distributions?
*  What goes in and like and for me, one of the things that makes it easy
*  and lose the magic and become like, I can use this as a tool and I can understand this.
*  It's just write down the code.
*  And literally, it's like, oh, I have everything I need.
*  Like the prior is just like the result of the previous iteration.
*  And then I multiply it by something that I know.
*  And then I divide, you know, like once you put it all in code for me,
*  then I'm like, OK, now it's not magic and it's good that it's not magic.
*  I don't want it to be magic.
*  I want it to be usable.
*  And I think that's that's one of the things that hopefully students got out of the
*  out of the lectures and the exercises and Neuromatch.
*  I'm sure they've done this, but I used to I should do this again, actually.
*  I'm sure the Neuromatch kids have done this.
*  But I like whenever someone came to my lab, I used to tell them,
*  spend the first week just estimating the mean and the mean,
*  the mean of some data and the standard error on that mean,
*  using all the different flavors of Bayes.
*  And it takes like from from
*  like direct from sampling techniques to direct integration techniques to analytic.
*  You can do you can do that particular exercise in about 10 different ways.
*  Once you've done that, you understand a lot about Bayes.
*  It takes I mean, obviously, doing that properly will take more than a week.
*  But but just just once you know how to estimate,
*  that's the total joy of Bayes, right?
*  Once you ask them once you know how to estimate the mean is from data with Bayes,
*  you can do everything with Bayes because it's just about specifying
*  a different generative model.
*  Tim, if you have that like exercise or assignment in writing, I totally want it.
*  I can I can definitely.
*  I mean, it's really it's really not hard to make.
*  I can really make it. Yeah.
*  Yeah. Yeah. I love that. Thank you. Yeah.
*  I was going to say, I'll next week.
*  You're that's when your child is going to come to you and say,
*  I know that my brain can update to do to do Bayesian inference,
*  but why can't I understand it?
*  And then you'll give maybe you'll give the child the exercise, those exercises.
*  But yeah, no, my kid is super magical.
*  That is magical.
*  Well, case. So let's get off of magical because that was just an error,
*  I guess, on my part, saying using the word magical because the real magic is not real.
*  But let's go to coolness, OK, because let's call it cool.
*  I have a friend who runs a lab and he and I were talking about how
*  when we went into graduate school, we didn't have any coding experience.
*  And and now he says all the kids coming in,
*  they're all like machine learning experts.
*  And that's because deep learning is cool.
*  And and so the that's what I was talking about is the computational approach
*  is the cool kid is the way is the cool way to do
*  the popular kid in in neuroscience these days.
*  And that's so different.
*  I mean, when some of us here who are older than others here
*  were growing up as is right early career scientists.
*  I jokingly say, like, if you if you said I'm a computational
*  neuroscientist, people would go talk to someone else in the party.
*  Right. They was like, this was not the cool kid.
*  Nobody wanted to hire computational neuroscientists.
*  Nobody was really sure what computational neuroscientists were.
*  Very few universities had a computational neuroscience program.
*  There were some summer courses because that that was like,
*  let's get people into the field.
*  So computational neuroscience always had like a fair share of summer courses.
*  But that because there was nothing else, you couldn't study it
*  anywhere else in some sense.
*  And it's amazing to me to see also like reinforcement learning.
*  Nobody used to talk even even in a computational summer
*  computational neuroscience summer course.
*  I remember I was a student in 2001 and the European
*  computational neuroscience summer course, it's now the course in Portugal.
*  It was then in Italy that year.
*  And in the whole course, we did not have anything about reinforcement learning.
*  Nothing, nothing, nothing like a four week course.
*  And the last week they asked us for feedback.
*  And I said, you know, you kind of miss the whole like area.
*  And now it's such a hot topic.
*  It used to be that you would find like an SFN, maybe like
*  10 posters of interest.
*  And now they're like there's a whole session every day
*  that's like mostly reinforcement learning stuff.
*  So it's there's been a huge change in the field.
*  And it's really amazing to witness.
*  Kind of scary as well.
*  It was kind of nice when just a few of us
*  can actually say about coolness.
*  I mean, I obviously I'm very gratified that
*  people think, or at least some people think that computational neuroscience is cool.
*  At the same time, I also think that
*  when it comes to some specific choice of research idea,
*  I think if you want to be really original,
*  you're going to have to give up some coolness.
*  All right. There's a tension fundamentally between being cool and being original,
*  because there are many people who are entering the field,
*  kind of swept by this wave of enthusiasm for certain ideas like deep learning.
*  And what that means is that many people are basically doing more or less the same thing.
*  And and I understand that, particularly for young people who enter in
*  and are trying to find some promising topic of research.
*  That's it's natural to gravitate towards the cool things.
*  But in some ways, I hope that we can train people to to to resist that
*  to some extent and think about original ideas.
*  When I started, when I started my career, everybody was doing vision.
*  Everybody in computational neuroscience was doing computational vision.
*  And I was like, still, that's still the case, though.
*  But I remember saying to myself, I don't know what I want to do.
*  I know what I don't want to do. And that is that.
*  And it was almost just because everybody was doing it.
*  And that just pushed me away.
*  And look where I ended up and what everybody is doing now.
*  But the other things I want to say, Paul, to what you said, that that like now
*  it's cool and everybody comes in knowing how to program and having programming background.
*  I just wanted to say for those listening that not everybody actually
*  a lot of women, it turns out, don't have programming background, also some men.
*  But that's totally fine.
*  It's so learnable.
*  And it's not like you don't have a place in this field if you don't come
*  with this background from home.
*  If there's this perception that everybody has it, but it's really not true.
*  A lot of people in my lab don't have programming background.
*  It came without programming background.
*  You know, Sam came from psychology and kind of a lot of self-learning as a programmer.
*  I have other students coming from math.
*  I almost have no, but actually in my lab, I think have zero people
*  who came from computer science.
*  So programming background is not like the requirement to do this kind of work.
*  Well, that's because psychology is such a soft, magical
*  the other.
*  But Conrad, I didn't go.
*  What are we going to say?
*  Yeah, I wanted to zoom out a little bit.
*  So there's a computer scientist, Dykstra, who is one of the big heroes in my life.
*  And he formulated three rules of what you should do to do good science.
*  And it's highly debated.
*  And there's a lot of people who disagree with.
*  But the last two things we just said perfectly mapped on two of his.
*  The last one we discussed is like, yes, coding, we need to offer long
*  to be able to do the research that we want to do.
*  And one of his rules is you should always do the hardest
*  and most complicated research that you can possibly do, too,
*  because that's the only way to grow as a scientist.
*  And the other one is when given a little bit of time,
*  someone else will solve a problem.
*  You should move away and do something else,
*  which is what you all told us to do.
*  No, like in like in a way being enough in an area
*  where lots of people are doing the same research, you shouldn't be there.
*  It's a waste of mankind's resources.
*  And it also may push you into that space, but you have to compete
*  on the number of hours you spend per week instead of the clarity
*  of the ideas that you can break to it, because these overcrowded fields,
*  there's always other people doing roughly the right thing.
*  And it's just bad because people compete on the wrong things.
*  I was going to say that this is that people go to what's cool.
*  And I want to push back a little bit, Conrad, on the like
*  this strategic idea of you choose an area to like maximize
*  what humankind will discover.
*  I think we choose areas based on what we are super excited about.
*  And it's true that if there's an area that a lot of people are working in
*  and giving great exciting talks on, then students get excited about it.
*  And I wouldn't say don't do something you're excited about
*  because the competition will be tough.
*  It's not just about the competition, but it is.
*  You see, neuroscience is so big.
*  When I started in the field, I had no idea how big that is.
*  So it's really weird that there's these bubbles where all of a sudden
*  you have dozens of labs doing very similar research.
*  And I understand it feels comfortable with a lot of people sharing
*  a certain set of ideas.
*  But I've been part of these bubbles and it feels at the end of the bubbles.
*  Well, maybe we went like a little overboard to that direction.
*  So I do think that that having that velocity of ideas is really incredibly valuable.
*  And that's why if you find an area where lots of people congregate
*  and that's just my own opinion and Dijkstra's
*  that in a way, we want to see if we can bring in new ideas
*  and do something that is somewhat different and like, you told us,
*  you told us that you were like, OK, I don't want to do vision
*  because everyone else is.
*  And you were incredibly off the charts, successful
*  charting new ways of doing things.
*  And I think that possibility exists in a lot of areas of neuroscience.
*  But it's not that I didn't want to do vision, even though I was excited about it.
*  I just wasn't excited about it.
*  Something about it did not excite me, maybe because it seemed to like,
*  I don't know. I don't know why.
*  It was just like the one thing I wasn't excited about.
*  I was excited about pretty much everything else.
*  And I was most excited about reinforcement learning.
*  And I ended up doing that.
*  I'm just saying that, I mean, it's.
*  I think people often try to think, well, I don't know if often,
*  but people sometimes ask me whether I chose an area of research
*  strategically or something like that.
*  And I feel that it's really hard to predict the future.
*  And if you're in an area that's crowded that and that's what you're most
*  excited about, then you can remind yourself that we are not at all close
*  to understanding the brain.
*  So there is room even in that area.
*  And if you're excited about something else that not everybody's excited about,
*  good for you as well.
*  You will, as Conrad, as you were saying, you will help push mankind forward
*  by doing something that not everybody is doing.
*  But really, it's very subjective what we get very excited about.
*  And I would encourage people to not try to overcome their excitement
*  with strategicness.
*  Well, it's actually it's funny because I I was thinking in some ways of the
*  inverse of what you're saying in the sense that, yes, there's a subjective element.
*  First of all, I agree with you.
*  People should do what they're excited about.
*  In addition to the subjective element, I think there's a lot of path dependence
*  about what people are excited about.
*  And I'm excited about things today that if you had asked me
*  10 years ago, if I if I was excited about those things,
*  I would say definitely not. Why would anyone study those things?
*  That single cell learning.
*  Yeah. And I mean, other things like I did work on motion perception.
*  I didn't think that motion perception was particularly interesting.
*  But, you know, it turned out that there are things that were interesting about it
*  for me. But that that had a lot.
*  Again, it was very path dependent because I came to it
*  from a particular angle that that was driven by other things that I did
*  with that were not about, let's say, motion perception.
*  And then the other thing is the other way in which
*  I was thinking about this in a kind of inverted
*  direction from now is that there's a
*  I think there's often a strategic aspect to why people
*  these sort of bandwagon effects where people pile into one
*  research area.
*  Because I think people see what what produces successful careers
*  and they have some anxiety like should I be doing this obscure thing
*  that nobody cares about or this this thing that not just I'm excited about,
*  but many other people are excited about it will advance my career.
*  And so it takes some degree of courage to
*  and acceptance of risk to take the leap into an area that
*  maybe you're excited about, but you're worried that it's not a good career.
*  On the path dependent thing, I just wanted to say that my interest
*  in reinforcement learning came from a paper that I presented in a seminar
*  that seminar started my whole career, an undergraduate seminar.
*  And I don't know if this is true, Sam, or not, but I feel like
*  when you joined my lab, we had this these like many rotations
*  of like two weeks in each lab, in a few labs and in
*  what was then that we didn't have the Neurosciences Institute,
*  the psychology department.
*  And I gave you a paper to read about like,
*  you know, young rats doing extinction differently from old rats.
*  And I kind of feel like that started your model and your whole like
*  PhD thesis from there.
*  So I don't know, maybe you had those ideas already to start with.
*  But I felt like after that, I kind of thought, wow, I should think really carefully
*  what papers I give people, because, you know, when paper goes a long way here.
*  Oh, yeah. I mean, I realized that, too, like I would sometimes
*  throw off a random idea and and the students would like
*  work really hard to sort of figure out what my cryptic half-baked idea was about.
*  When I my intention was not to like set people off on this odyssey.
*  But and so it gave me pause to think about the effects of casual suggestions.
*  Well, I'm very happy I gave you that paper.
*  The path dependence there worked really well.
*  Me too. Can we talk about questions for a second?
*  Because you hear over and over when someone asks, like, what model should I use?
*  The answer is always it depends on what your question is.
*  But a lot of people early on in their careers think, oh, God, I need a question.
*  They don't have a question, right.
*  But they they have a vague interest because deep learning is cool or whatever,
*  you know, in in the brain and computational neuroscience.
*  And then so I don't know if you can say this from your own experience,
*  thinking about path dependency and the nature of how your questions have changed
*  over the course. But and the gist of the was there, did you come in with the right question?
*  Did the right question develop through some one of your advisors
*  giving you a paper about rats or, you know, how did that work?
*  I think I think everybody has to find particularly when you pay.
*  Yeah, I mean, I wrote a little thing about this.
*  But I think like it's the biggest like if you're still working on the same thing,
*  you're you're you told you told your hiring committee you would work on
*  10 years later than something has gone wrong.
*  And and probably
*  most people find their questions
*  because their data don't make sense without different questions.
*  I think there are some people like Sam who are so broadly read
*  that they can find new questions from out of our left field.
*  But I don't think that I am saying all like that.
*  I I look at data and it doesn't make sense.
*  And I feel I mean, I was led to, for example, from frontal cortex
*  to hippocampus because it was anywhere I could make sense of frontal cortex data.
*  And but do you do you remember like the initial part of your career
*  when when that sort of stuff before your questions were well formed?
*  Do you remember feeling, oh, now I have a question and
*  getting to me ages, it to me ages to start working on something that was that.
*  So I was working on on various sort of things
*  that were just like little individual projects that were just related
*  to what I was doing in the postdoc, my postdoc and just worse than in most
*  in many cases, but often related for the first, I don't know,
*  for the first five or six years of running a lab.
*  They were fine.
*  They were just isolated.
*  There was no deep understanding to them.
*  In some ways, maybe I did them for safety because I knew they would work
*  and they'd seen they were related to what I'd done before.
*  But during that time, I formed a lot of deeper,
*  I think, questions about how going going about
*  how to go about these things.
*  And and I think that really that comes from
*  like serially seeing data and it and it only making sense together
*  with with some deeper question.
*  I think that there's no I think if you don't
*  questions don't magic themselves up unless you well unless you read an awful lot.
*  That's the other way that maybe you can get questions.
*  Yeah, I was going to say that that reading is another source.
*  Sometimes it's your own data.
*  Sometimes it's kind of an observation of a phenomenon in the world.
*  Or, you know, since we're studying brains in our own, like subjective experience,
*  that brings a question. But a lot of it, I remember at some point saying
*  to a colleague that I don't have any new ideas.
*  And then like in a different conversation, I said that since my kids were born,
*  I haven't had time to read papers.
*  And she was like, well, no wonder you have no new ideas.
*  Where do our ideas and questions come from?
*  It's from a lot from reading other papers or talks.
*  I have a friend who would directly contradict you, who swears that reading
*  is the devil and you have you generate your own ideas and then those generate new ideas.
*  He does not read. He runs a lab.
*  So just wanted to as a counterpoint.
*  But does he go to talk?
*  In perspective, it can work for some.
*  It worked for Jeff Hinton, but doesn't work for everyone.
*  The depends what you mean by work.
*  I mean, if working also involves forgetting everything other people.
*  The yeah.
*  But I think there's this diversity of where questions come from.
*  Now, like questions come from often questions for me come between fields.
*  There's this field that says this, this field that says that.
*  How does it even fit together?
*  Sometimes they come from reading.
*  Sometimes they come just opposite direction.
*  Look at data like what's the question that would go with the data that I happen to have?
*  And that's also a perfectly fine way of getting like not in the overfitting sense,
*  but like we can measure a and we can measure B.
*  What's the set of questions that you can answer if you can only measure A and B?
*  And it's a different set than what you start with.
*  And I don't think this like notion of like the question is fast
*  and that's trying to answer it is later maps on all projects in your sense.
*  I think it's really important to have a question.
*  I mean, yes, it can come from different places, but.
*  I don't know. I mean, this might be subjective and then how different people do science.
*  But I feel like if you if you're doing a project and you don't know what you're asking,
*  then you're unlikely to find an interesting answer.
*  I totally agree with that.
*  And actually something that I've started doing, I realized reviewing lots of PhD applications.
*  This might actually be something useful for the error match listeners out there.
*  I I realized that the vast majority of applications,
*  when they write their research interests, they say, I'm interested in memory or decision making or whatever.
*  And the problem there, I think, is that when you sit down on day one of grad school,
*  you can't just sit down at your computer and start working on memory.
*  Right. It's just it's not a question that can be answered.
*  Right. And so I started for all the undergrads that work in my lab over the summer
*  and are thinking about applying for grad school.
*  I when I talk to them, I ask them, what is their question?
*  And usually they don't really have one.
*  And and so I tell them to think about it and then talk to me again later.
*  And then we basically talk about it until they have a question.
*  They have a question.
*  You know, it's not necessarily the question that they're going to work on for the rest of their lives.
*  But it's a question that we both agree is good and interesting for them.
*  And I think that's actually a really useful approach to writing, to preparing PhD applications
*  and also to know who you want to work with, who is answering the question that you want to answer.
*  Or we're trying to.
*  It's amazing that you're doing that with undergrads, because I want to say that I asked postdoc
*  applicants, what question do you want to study?
*  And many postdoc applicants don't have an answer to that.
*  It's really hard.
*  Yeah.
*  People will know, you know, what method they want to use or what kind of thing they're interested in.
*  But often they don't have a question.
*  Again, I think it's really important to find a question to do research.
*  But I again want to say to the listeners that if you don't have a question, that doesn't mean you're the outlier.
*  Actually, most people don't have a question.
*  We should tell everyone about how Dickinson found his question for the devaluation experiment.
*  How did he?
*  I don't know the story.
*  The watermelon story.
*  Have you not heard the watermelon story?
*  No, I'm joking.
*  We shouldn't tell that story.
*  We only have like a few minutes left.
*  But it was like an anecdotal personal experience.
*  So it had to do with drinking and drinking too much and having a hangover.
*  But I want to emphasize here that there's a process that we can have that helps, that makes,
*  at least in my experience, the finding of questions easier.
*  So I force everyone before they do real research to write an abstract,
*  which contains a question and the answer that they're expecting for it.
*  And this forcing yourself into like, just put this story that this will be into a hundred words,
*  that really forces people into coming up with a question.
*  And I found that...
*  Are you guys not forced into that?
*  So we have...
*  That's a very cool idea.
*  But we have to do this institutionally.
*  Whenever we start a new project, the graduate student has to give a presentation to the whole department
*  before he gets any data or does anything on it.
*  What does a new project even mean?
*  That's what I was going to ask Conrad, but I guess you as well, Tim.
*  Because Conrad, you said before anybody does real research, what's real research versus fake research?
*  I want people to write an abstract before they do one line of coding.
*  Oh.
*  Any coding.
*  Interesting.
*  I ask people to do more than that.
*  I mean, I ask people to write down their whole model before they do a piece of code.
*  Coding is the new real research?
*  I don't ask anybody to do any of that stuff.
*  I must be doing something wrong.
*  No, no, no. I mean, they're different...
*  It's not one size fits all.
*  It's for certain kinds of projects that...
*  I mean, this is neither here nor there, I suppose.
*  We have to present before we get data.
*  So for the data part of it, we...
*  For any experiment or just for fMRI experiments?
*  Like, you know, if you're going to collect some data on mechanical turk,
*  you have to present to other people about it?
*  So you're totally right, Eyal.
*  It's for experiments on the...
*  It's mostly for experiments on the MRI machines,
*  but we actually also do it for some of our rodent experiments as well.
*  We don't do it for...
*  Yeah, that's different.
*  That's different.
*  Like, most of what we do...
*  Like, we get to an fMRI experiment, like, once in a PhD laid on in the game.
*  Most of the work...
*  And some people don't even...
*  I mean, don't do fMRI their whole thesis.
*  Like, Sam, for instance, his thesis and my...
*  Right? You didn't do fMRI, or did you?
*  I did.
*  You did with Ken, but not with me.
*  With Ken, but not with me, right?
*  I did, but those experiments didn't work out very well.
*  Yeah.
*  You wiped it from your memory.
*  Yeah, that's all right.
*  You want to do it with me?
*  Guys, I have to interrupt this because...
*  I'll tell you about it later, though.
*  It's time to depart.
*  Let's do, like, a little...
*  A very quick experiment, a wet and dirty experiment.
*  Let's test your predictive brains.
*  I want to thank you all for being here.
*  This has been blank.
*  What am I going to say?
*  Inspiring.
*  Serial.
*  Serial, yeah.
*  Magical.
*  Magical.
*  Sam got it.
*  It was magical.
*  So, I don't know.
*  That was kind of a low...
*  That was kind of a low accuracy experiment.
*  But, guys, any parting words before...
*  We hardly talked about anything except fun stuff.
*  So, any parting words specific to anything,
*  any of the topics anyone was learning this week or otherwise?
*  I'm going back to the beach.
*  Yeah, and have fun would be my parting word,
*  both for Tim and for everyone listening in here.
*  Find your question.
*  That was one of the themes there.
*  Well, thanks very much, guys.
*  Thank you.
*  Thanks.
*  Brain Inspired is a production of me and you.
*  I don't do advertisements.
*  You can support the show through Patreon for a trifling amount
*  and get access to the full versions of all the episodes
*  plus bonus episodes that focus more on the cultural side
*  but still have science.
*  Go to braininspired.co and find the red Patreon button there.
*  To get in touch with me, email paul at braininspired.co.
*  The music you hear is by The New Year.
*  Find them at thenewyear.net.
*  Thank you for your support.
*  See you next time.
*  The stare of a boundless blank page
*  led me into the snow.
*  The covers of the past, they take me where I'd go.

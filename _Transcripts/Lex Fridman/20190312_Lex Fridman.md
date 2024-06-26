---
Date Generated: April 14, 2024
Transcription Model: whisper medium 20231117
Length: 3683s
Video Keywords: []
Video Views: 38921
Video Rating: None
---

# Leslie Kaelbling: Reinforcement Learning, Planning, and Robotics | Lex Fridman Podcast #15
**Lex Fridman:** [March 12, 2019](https://www.youtube.com/watch?v=Er7Dy8rvqOc)
*  The following is a conversation with Leslie Kaelbling.
*  She's a roboticist and professor at MIT.
*  She's recognized for her work in reinforcement learning,
*  planning, robot navigation, and several other topics in AI.
*  She won the IJCAI Computers and Thought Award
*  and was the editor-in-chief
*  of the prestigious Journal of Machine Learning Research.
*  This conversation is part
*  of the Artificial Intelligence Podcast at MIT and beyond.
*  If you enjoy it, subscribe on YouTube, iTunes,
*  or simply connect with me on Twitter
*  at Lex Friedman, spelled F-R-I-D.
*  And now here's my conversation with Leslie Kaelbling.
*  What made me get excited about AI, I can say that,
*  is I read Gertel Escher Bach when I was in high school.
*  That was pretty formative for me
*  because it exposed the interestingness of primitives
*  and combination and how you can make complex things
*  out of simple parts and ideas of AI
*  and what kinds of programs
*  might generate intelligent behavior.
*  So you first fell in love with AI reasoning logic
*  versus robots?
*  Yeah, the robots came because my first job,
*  so I finished an undergraduate degree
*  in philosophy at Stanford
*  and was about to finish a master's in computer science
*  and I got hired at SRI in their AI lab.
*  And they were building a robot.
*  It was a kind of a follow on to shaky,
*  but all the shaky people were not there anymore.
*  And so my job was to try to get this robot to do stuff
*  and that's really kind of what got me interested in robots.
*  So maybe taking a small step back,
*  your bachelor's in Stanford in philosophy,
*  did a master's and PhD in computer science,
*  but the bachelor's in philosophy.
*  So what was that journey like?
*  What elements of philosophy do you think you bring
*  to your work in computer science?
*  So it's surprisingly relevant.
*  So part of the reason that I didn't do
*  a computer science undergraduate degree
*  was that there wasn't one at Stanford at the time,
*  but that there's part of philosophy
*  and in fact Stanford has a special sub major
*  in something called now symbolic systems,
*  which is logic, model theory,
*  formal semantics of natural language.
*  And so that's actually a perfect preparation
*  for work in AI and computer science.
*  That's kind of interesting.
*  So if you were interested in artificial intelligence,
*  what kind of majors were people even thinking about taking?
*  What is it in neuroscience?
*  So besides philosophies, what were you supposed to do
*  if you were fascinated by the idea of creating intelligence?
*  There weren't enough people who did that
*  for that even to be a conversation.
*  I mean, I think probably philosophy.
*  I mean, it's interesting in my class,
*  my graduating class of undergraduate philosophers,
*  probably maybe slightly less than half
*  went on in computer science,
*  slightly less than half went on in law
*  and like one or two went on in philosophy.
*  So it was a common kind of connection.
*  Do you think AI researchers have a role
*  to be part-time philosophers
*  or should they stick to the solid science and engineering
*  without sort of taking the philosophizing tangents?
*  I mean, you work with robots,
*  you think about what it takes to create intelligent beings.
*  Aren't you the perfect person to think about
*  the big picture philosophy of it all?
*  The parts of philosophy that are closest to AI, I think,
*  or at least the closest to AI that I think about
*  are stuff like belief and knowledge and denotation
*  and that kind of stuff.
*  And that's, you know, it's quite formal
*  and it's like just one step away
*  from the kinds of computer science work
*  that we do kind of routinely.
*  I think that there are important questions still
*  about what you can do with a machine
*  and what you can't and so on.
*  Although at least my personal view
*  is that I'm completely a materialist
*  and I don't think that there's any reason
*  why we can't make a robot be behaviorally
*  indistinguishable from a human.
*  And the question of whether it's distinguishable internally,
*  whether it's a zombie or not in philosophy terms,
*  I actually don't, I don't know,
*  and I don't know if I care too much about that.
*  Right, but there is philosophical notions.
*  They're mathematical and philosophical
*  because we don't know so much of how difficult it is,
*  how difficult is the perception problem,
*  how difficult is the planning problem,
*  how difficult is it to operate in this world successfully
*  because our robots are not currently
*  as successful as human beings in many tasks.
*  The question about the gap between current robots
*  and human beings borders a little bit on philosophy.
*  The expanse of knowledge that's required
*  to operate in this world and the ability
*  to form common sense knowledge,
*  the ability to reason about uncertainty,
*  much of the work you've been doing,
*  there's open questions there that, I don't know,
*  required to activate a certain big picture view.
*  To me, that doesn't seem like a philosophical gap at all.
*  To me, there is a big technical gap.
*  There's a huge technical gap,
*  but I don't see any reason why
*  it's more than a technical gap.
*  Perfect.
*  So when you mentioned AI, you mentioned SRI,
*  and maybe, can you describe to me
*  when you first fell in love with robotics,
*  with robots or inspired, which,
*  so you mentioned Flaky or Shakey Flaky,
*  and what was the robot that first captured
*  your imagination of what's possible?
*  Right, so the first robot I worked with was,
*  like, Shakey was a robot that the SRI people had built,
*  but by the time, I think, when I arrived,
*  it was sitting in a corner of somebody's office
*  dripping hydraulic fluid into a pan.
*  But it's iconic, and really,
*  everybody should read the Shakey Tech Report
*  because it has so many good ideas in it.
*  I mean, they invented A-star Search
*  and symbolic planning and learning macro operators.
*  They had low-level kind of configuration space
*  planning for the robot.
*  They had vision.
*  They had all, this, the basic ideas of a ton of things.
*  Can you take a step back?
*  Shakey have arms, what was the job,
*  what was the goal?
*  Shakey, yeah, good.
*  Shakey was a mobile robot, but it could push objects,
*  and so it would move things around.
*  With which actuator, with the arms?
*  With itself, with its base.
*  Okay, great.
*  But it, and they had painted the baseboards black.
*  So it used vision to localize itself in a map.
*  It detected objects.
*  It could detect objects that were surprising to it.
*  It would plan and replan based on what it saw.
*  It reasoned about whether to look and take pictures.
*  I mean, it really had the basics of so many of the things
*  that we think about now.
*  How did it represent the space around it?
*  So it had representations at a bunch of different levels
*  of abstraction, so it had, I think,
*  a kind of an occupancy grid of some sort
*  at the lowest level.
*  At the high level, it was abstract, symbolic kind of rooms
*  and connectivity.
*  So where does Flaky come in?
*  Yeah, okay.
*  So I showed up at SRI, and we were building
*  a brand new robot.
*  As I said, none of the people from the previous project
*  were kind of there or involved anymore.
*  So we were kind of starting from scratch.
*  And my advisor was Stan Rosenstein.
*  He ended up being my thesis advisor.
*  And he was motivated by this idea of situated computation
*  or situated automata.
*  And the idea was that the tools of logical reasoning
*  were important, but possibly only for the engineers
*  or designers to use in the analysis of a system,
*  but not necessarily to be manipulated
*  in the head of the system itself.
*  So I might use logic to prove a theorem
*  about the behavior of my robot,
*  even if the robot's not using logic in its head
*  to prove theorems.
*  So that was kind of the distinction.
*  And so the idea was to kind of use those principles
*  to make a robot do stuff.
*  But a lot of the basic things we had to kind of
*  learn for ourselves,
*  because I had zero background in robotics.
*  I didn't know anything about control.
*  I didn't know anything about sensors.
*  So we reinvented a lot of wheels
*  on the way to getting that robot to do stuff.
*  Do you think that was an advantage or a hindrance?
*  Oh, no, I mean, I'm big in favor of wheel reinvention,
*  actually.
*  I mean, I think you learned a lot by doing it.
*  It's important though to eventually have the pointers
*  so that you can see what's really going on.
*  But I think you can appreciate much better
*  the good solutions once you've messed around a little bit
*  on your own and found a bad one.
*  Yeah, I think you mentioned reinventing
*  reinforcement learning and referring to rewards
*  as pleasures, pleasure, I think.
*  Which I think is a nice name for it.
*  Yeah, that seemed good to me.
*  It's more fun almost.
*  Do you think you could tell the history of AI,
*  machine learning, reinforcement learning,
*  how you think about it from the 50s to now?
*  One thing is that it oscillates.
*  So things become fashionable and then they go out
*  and then something else becomes cool
*  and then it goes out and so on.
*  And I think there's some interesting sociological process
*  that actually drives a lot of what's going on.
*  Early days was cybernetics and control
*  and the idea of homeostasis.
*  People who made these robots that could, I don't know,
*  try to plug into the wall when they needed power
*  and then come loose and roll around and do stuff.
*  And then I think over time, the thought,
*  well, that was inspiring, but people said, no, no, no,
*  we wanna get maybe closer to what feels like
*  real intelligence or human intelligence.
*  And then maybe the expert systems people tried to do that,
*  but maybe a little too superficially, right?
*  So, oh, we get this surface understanding
*  of what intelligence is like
*  because I understand how a steel mill works
*  and I can try to explain it to you
*  and you can write it down in logic
*  and then we can make a computer infer that.
*  And then that didn't work out.
*  But what's interesting, I think,
*  is when a thing starts to not be working very well,
*  it's not only do we change methods, we change problems.
*  So it's not like we have better ways of doing the problem
*  of the expert systems people were trying to do.
*  We have no ways of trying to do that problem.
*  Oh, yeah, I know, I think, or maybe a few,
*  but we kind of give up on that problem
*  and we switch to a different problem.
*  And we work that for a while and we make progress.
*  As a broad community.
*  As a community, yeah.
*  And there's a lot of people who would argue,
*  you don't give up on the problem,
*  it's just you decrease the number of people working on it.
*  You almost kind of like put it on the shelf,
*  say, we'll come back to this 20 years later.
*  Yeah, I think that's right.
*  Or you might decide that it's malformed.
*  Like you might say,
*  it's wrong to just try to make something
*  that does superficial symbolic reasoning
*  behave like a doctor.
*  You can't do that until you've had
*  the sensory motor experience
*  of being a doctor or something.
*  So there's arguments that say
*  that that problem was not well formed,
*  or it could be that it is well formed,
*  but we just weren't approaching it well.
*  So you mentioned that your favorite part of logic
*  in symbolic systems is that they give short names
*  for large sets.
*  So there is some use to this.
*  They use symbolic reasoning.
*  So looking at expert systems and symbolic computing,
*  what do you think are the roadblocks
*  that were hit in the 80s and 90s?
*  Okay, so right, so the fact that I'm not a fan
*  of expert systems doesn't mean that I'm not a fan
*  of some kinds of symbolic reasoning, right?
*  So, let's see, roadblocks.
*  Well, the main roadblock, I think,
*  was that the idea that humans could articulate
*  their knowledge effectively into some kind
*  of logical statements.
*  So it's not just the cost, the effort,
*  but really just the capability of doing it.
*  Right, because we're all experts in vision, right?
*  But totally don't have introspective access
*  into how we do that, right?
*  And it's true that,
*  I mean, I think the idea was, well, of course,
*  even people then would know, of course,
*  I wouldn't ask you to please write down the rules
*  that you use for recognizing a water bottle.
*  That's crazy, and everyone understood that.
*  But we might ask you to please write down
*  the rules you use for deciding, I don't know,
*  what tie to put on or how to set up a microphone
*  or something like that.
*  But even those things, I think people maybe,
*  I think what they found, I'm not sure about this,
*  but I think what they found was that the so-called experts
*  could give explanations, sort of post-hoc explanations
*  for how and why they did things,
*  but they weren't necessarily very good.
*  And then they depended on maybe some kinds
*  of perceptual things, which again,
*  they couldn't really define very well.
*  So I think fundamentally, I think the underlying problem
*  with that was the assumption that people could articulate
*  how and why they make their decisions.
*  Right, so it's almost encoding the knowledge,
*  converting from expert to something
*  that a machine can understand and reason with.
*  No, no, no, no, not even just encoding,
*  but getting it out of you.
*  Just.
*  Right?
*  Not writing it, I mean, yes, hard also
*  to write it down for the computer,
*  but I don't think that people can produce it.
*  You can tell me a story about why you do stuff,
*  but I'm not so sure that's the why.
*  Great, so there are still on the hierarchical planning side,
*  places where symbolic reasoning is very useful.
*  So as you've talked about, so where's the gap?
*  Yeah, okay, good.
*  So saying that humans can't provide a description
*  of their reasoning processes, that's okay, fine,
*  but that doesn't mean that it's not good to do reasoning
*  of various styles inside a computer.
*  Those are just two orthogonal points.
*  So then the question is, what kind of reasoning
*  should you do inside a computer?
*  Right.
*  And the answer is I think you need to do
*  all different kinds of reasoning inside a computer,
*  depending on what kinds of problems you face.
*  I guess the question is, what kind of things
*  can you encode symbolically so you can reason about?
*  I think the idea about, and even symbolic,
*  I don't even like that terminology
*  because I don't know what it means technically and formally.
*  I do believe in abstractions.
*  So abstractions are critical, right?
*  You cannot reason at completely fine grain
*  about everything in your life, right?
*  You can't make a plan at the level of images and torques,
*  for getting a PhD.
*  Right.
*  So you have to reduce the size of the state space
*  and you have to reduce the horizon
*  if you're gonna reason about getting a PhD
*  or even buying the ingredients to make dinner.
*  And so how can you reduce the spaces
*  and the horizon of the reasoning you have to do?
*  And the answer is abstraction,
*  spatial abstraction, temporal abstraction.
*  I think abstraction along the lines of goals
*  is also interesting.
*  Like you might, or well, abstraction and decomposition.
*  Goals is maybe more of a decomposition thing.
*  So I think that's where these kinds of,
*  if you wanna call it symbolic or discrete models come in.
*  You talk about a room of your house instead of your pose.
*  You talk about doing something during the afternoon
*  instead of at 2.54.
*  And you do that because it makes your reasoning problem
*  easier and also because you don't have enough information
*  to reason in high fidelity about your pose of your elbow
*  at 2.35 this afternoon anyway.
*  Right.
*  When you're trying to get a PhD.
*  Right.
*  Or when you're doing anything really.
*  Oh, yeah, okay.
*  Except for at that moment.
*  At that moment, you do have to reason
*  about the pose of your elbow, maybe.
*  But then maybe you do that in some continuous
*  joint space kind of model.
*  So again, my biggest point about all of this
*  is that there should be, the dogma is not,
*  dogma is not the thing, right?
*  We shouldn't, it shouldn't be that I am in favor
*  against symbolic reasoning and you're in favor
*  against neural networks.
*  It should be that just computer science tells us
*  what the right answer to all these questions is
*  if we were smart enough to figure it out.
*  Well, yeah, when you try to actually solve the problem
*  with computers, the right answer comes out.
*  You mentioned abstractions.
*  I mean, neural networks form abstractions or rather,
*  there's automated ways to form abstractions
*  and there's expert driven ways to form abstractions
*  and expert human driven ways.
*  And humans just seem to be way better
*  at forming abstractions currently and certain problems.
*  So when you're referring to 2.45 p.m. versus afternoon,
*  how do we construct that taxonomy?
*  Is there any room for automated construction
*  of such abstractions?
*  Oh, I think eventually, yeah.
*  I mean, I think when we get to be better
*  and machine learning engineers will build algorithms
*  that build awesome abstractions.
*  That are useful in this kind of way that you're describing.
*  Yeah.
*  So let's then step from the abstraction discussion
*  and let's talk about Palm MDP's
*  partially observable Markov decision processes.
*  So uncertainty.
*  So first, what are Markov decision processes?
*  What are Markov decision processes?
*  And maybe how much of our world can be models and MDP's?
*  How much, when you wake up in the morning
*  and you're making breakfast,
*  do you think of yourself as an MDP?
*  So how do you think about MDP's
*  and how they relate to our world?
*  Well, so there's a stance question, right?
*  So a stance is a position
*  that I take with respect to a problem.
*  So I, as a researcher or a person who designs systems,
*  can decide to make a model of the world around me
*  in some terms.
*  So I take this messy world and I say,
*  I'm gonna treat it as if it were a problem
*  of this formal kind,
*  and then I can apply solution concepts or algorithms
*  or whatever to solve that formal thing, right?
*  So of course the world is not anything.
*  It's not an MDP or a Palm DDP.
*  I don't know what it is,
*  but I can model aspects of it in some way or some other way.
*  And when I model some aspect of it in a certain way,
*  that gives me some set of algorithms I can use.
*  You can model the world in all kinds of ways.
*  Some have, some are more accepting of uncertainty,
*  more easily modeling uncertainty of the world.
*  Some really force the world to be deterministic.
*  And so certainly MDP's model the uncertainty of the world.
*  Yes, model some uncertainty.
*  They model not present state uncertainty,
*  but they model uncertainty in the way
*  the future will unfold.
*  Right.
*  So what are Markov decision processes?
*  Okay, so Markov decision process is a model.
*  It's a kind of a model that you can make that says,
*  I know completely the current state of my system.
*  And what it means to be a state is that I have all
*  the information right now that will let me make predictions
*  about the future as well as I can.
*  So that remembering anything about my history
*  wouldn't make my predictions any better.
*  But then it also says that then I can take some actions
*  that might change the state of the world
*  and that I don't have a deterministic model of those changes.
*  I have a probabilistic model of how the world might change.
*  It's a useful model for some kinds of systems.
*  I think it's, I mean, it's certainly not a good model
*  for most problems.
*  I think because for most problems,
*  you don't actually know the state.
*  For most problems, it's partially observed.
*  So that's now a different problem class.
*  So, okay, that's where the POMDPs,
*  the Partially Observed Markov Decision Processes step in.
*  So how do they address the fact that you can't observe
*  most incomplete information about most
*  of the world around you?
*  Right, so now the idea is we still kind of postulate
*  that there exists a state.
*  We think that there is some information about the world
*  out there such that if we knew that,
*  we could make good predictions, but we don't know the state.
*  And so then we have to think about how,
*  but we do get observations.
*  Maybe I get images or I hear things or I feel things,
*  and those might be local or noisy.
*  And so therefore they don't tell me everything
*  about what's going on.
*  And then I have to reason about,
*  given the history of actions I've taken
*  and observations I've gotten,
*  what do I think is going on in the world?
*  And then given my own kind of uncertainty
*  about what's going on in the world,
*  I can decide what actions to take.
*  And so how difficult is this problem
*  of planning under uncertainty in your view
*  and your long experience of modeling the world,
*  trying to deal with this uncertainty
*  in especially in real world systems?
*  Optimal planning for even discrete POMDPs
*  can be undecidable depending on how you set it up.
*  And so lots of people say,
*  I don't use POMDPs because they are intractable.
*  And I think that that's a kind of a very funny thing to say
*  because the problem you have to solve
*  is the problem you have to solve.
*  So if the problem you have to solve is intractable,
*  that's what makes us AI people, right?
*  So we solve, we understand that the problem we're solving
*  is wildly intractable that we can't,
*  we will never be able to solve it optimally,
*  at least I don't.
*  Yeah, right.
*  So later we can come back to an idea
*  about bounded optimality and something.
*  But anyway, we can't come up with optimal solutions
*  to these problems.
*  So we have to make approximations,
*  approximations in modeling, approximations
*  in the solution algorithms and so on.
*  And so I don't have a problem with saying,
*  yeah, my problem actually, it is POMDP
*  in continuous space with continuous observations
*  and it's so computationally complex,
*  I can't even think about it's big O whatever.
*  But that doesn't prevent me from,
*  it helps me, gives me some clarity
*  to think about it that way.
*  And to then take steps to make approximation
*  after approximation to get down to something
*  that's like computable in some reasonable time.
*  When you think about optimality,
*  the community broadly has shifted on that,
*  I think a little bit,
*  in how much they value the idea of optimality,
*  of chasing an optimal solution.
*  How has your views of chasing an optimal solution
*  changed over the years when you work with robots?
*  That's interesting.
*  I think we have a little bit of a methodological crisis
*  actually from the theoretical side.
*  I mean, I do think that theory is important
*  and that right now we're not doing much of it.
*  So there's lots of empirical hacking around
*  and training this and doing that and reporting numbers,
*  but is it good, is it bad?
*  We don't know, it's very hard to say things.
*  And if you look at like computer science theory,
*  so people talked for a while,
*  everyone was about solving problems optimally
*  or completely and then there were interesting relaxations.
*  So people look at, oh, can I, are there regret bounds
*  or can I do some kind of approximation?
*  Can I prove something that I can approximately
*  solve this problem or that I get closer to the solution
*  as I spend more time and so on?
*  What's interesting, I think is that we don't have good
*  approximate solution concepts for very difficult problems.
*  I like to say that I'm interested in doing a very bad job,
*  very big problems.
*  Right, so very bad job, very big problems,
*  I like to do that, but I wish I could say something,
*  I wish I had a, I don't know,
*  some kind of a formal solution concept
*  that I could use to say, oh, this algorithm actually,
*  it gives me something, like I know what I'm gonna get,
*  I can do something other than just run it
*  and get out 6.7.
*  That notion is still somewhere deeply compelling to you.
*  The notion that you can say, you can drop thing
*  on the table says this, you can expect this algorithm
*  will give me some good results.
*  I hope there's, I hope science will, I mean,
*  there's engineering and there's science.
*  I think that they're not exactly the same.
*  And I think right now we're making huge engineering
*  like leaps and bounds so that engineering is running away
*  ahead of the science, which is cool.
*  And often how it goes, right?
*  So we're making things and nobody knows
*  how and why they work, roughly.
*  But we need to turn that into science.
*  There's some form, it's, yeah,
*  there's some room for formalizing.
*  We need to know what the principles are.
*  Why does this work?
*  Why does that not work?
*  I mean, for a while people built bridges by trying,
*  but now we can often predict whether it's gonna work
*  or not without building it.
*  Can we do that for learning systems or for robots?
*  Your hope is from a materialistic perspective
*  that intelligence, artificial intelligence systems, robots,
*  just fancier bridges.
*  Belief space.
*  What's the difference between belief space and state space?
*  So you mentioned MDPs, small MDPs,
*  reasoning about you sense the world, there's a state.
*  What's this belief space idea?
*  That sounds so good.
*  It sounds good.
*  So belief space, that is, instead of thinking about
*  what's the state of the world
*  and trying to control that as a robot,
*  I think about what is the space of beliefs
*  that I could have about the world?
*  If I think of a belief as a probability distribution
*  of every ways the world could be,
*  a belief state as a distribution.
*  And then my control problem, if I'm reasoning about
*  how to move through a world I'm uncertain about,
*  my control problem is actually the problem
*  of controlling my beliefs.
*  So I think about taking actions,
*  not just what effect they'll have on the world outside,
*  but what effect they'll have on my own understanding
*  of the world outside.
*  And so that might compel me to ask a question
*  or look somewhere to gather information,
*  which may not really change the world state,
*  but it changes my own belief about the world.
*  That's a powerful way to empower the agent
*  to reason about the world, to explore the world.
*  So what kind of problems does it allow you to solve
*  to consider belief space versus just state space?
*  Well, any problem that requires
*  deliberate information gathering.
*  So if, in some problems, like chess,
*  there's no uncertainty, or maybe there's uncertainty
*  about the opponent, there's no uncertainty about the state.
*  And some problems, there's uncertainty,
*  but you gather information as you go, right?
*  You might say, oh, I'm driving my autonomous car
*  down the road, and it doesn't know perfectly where it is,
*  but the light hours are all going all the time.
*  So I don't have to think about whether to gather information.
*  But if you're a human driving down the road,
*  you sometimes look over your shoulder
*  to see what's going on behind you in the lane,
*  and you have to decide whether you should do that now.
*  And you have to trade off the fact
*  that you're not seeing in front of you
*  and you're looking behind you,
*  and how valuable is that information, and so on.
*  And so to make choices about information gathering,
*  you have to reasonably space.
*  Also, I mean, also to just take into account
*  your own uncertainty before trying to do things.
*  So you might say, if I understand
*  where I'm standing relative to the door jam,
*  pretty accurately, then it's okay for me
*  to go through the door.
*  But if I'm really not sure where the door is,
*  then it might be better to not do that right now.
*  The degree of your uncertainty about the world
*  is actually part of the thing you're trying to optimize
*  in forming the plan, right?
*  That's right, that's right.
*  So this idea of a long horizon of planning for a PhD,
*  or just even how to get out of the house,
*  or how to make breakfast.
*  You show this presentation of the WTF,
*  where's the fork, of a robot looking at a sink.
*  And can you describe how we plan in this world,
*  this idea of hierarchical planning we've mentioned?
*  So yeah, how can a robot hope to plan about something
*  with such a long horizon, where the goal is quite far away?
*  People since probably reasoning began
*  have thought about hierarchical reasoning,
*  the temporal hierarchy in particular.
*  Well, there's spatial hierarchy,
*  but let's talk about temporal hierarchy.
*  So you might say, oh, I have this long execution
*  I have to do, but I can divide it
*  into some segments abstractly, right?
*  So maybe I have to get out of the house,
*  I have to get in the car, I have to drive, and so on.
*  And so you can plan, if you can build abstractions.
*  So this, we started out by talking about abstractions,
*  and we're back to that now.
*  If you can build abstractions in your state space,
*  and abstractions, sort of temporal abstractions,
*  then you can make plans at a high level.
*  And you can say, I'm gonna go to town,
*  and then I'll have to get gas, and then I can go here,
*  and I can do this other thing.
*  And you can reason about the dependencies
*  and constraints among these actions,
*  again, without thinking about the complete details.
*  What we do in our hierarchical planning work
*  is then say, all right, I make a plan
*  at a high level of abstraction.
*  I have to have some reason to think that it's feasible
*  without working it out in complete detail.
*  And that's actually the interesting step.
*  I always like to talk about walking through an airport.
*  Like, you can plan to go to New York
*  and arrive at the airport, and then find yourself
*  in an office building later.
*  You can't even tell me in advance what your plan is
*  for walking through the airport,
*  partly because you're too lazy to think about it maybe,
*  but partly also because you just don't have the information.
*  You don't know what gate you're landing in,
*  or what people are gonna be in front of you or anything.
*  So there's no point in planning in detail,
*  but you have to have, you have to make a leap of faith
*  that you can figure it out once you get there.
*  And it's really interesting to me how you arrive at that.
*  How do you, so you have learned over your lifetime
*  to be able to make some kinds of predictions
*  about how hard it is to achieve some kinds of sub-goals.
*  And that's critical.
*  Like you would never plan to fly somewhere
*  if you couldn't, didn't have a model of how hard it was
*  to do some of the intermediate steps.
*  So one of the things we're thinking about now
*  is how do you do this kind of very aggressive generalization
*  to situations that you haven't been in and so on
*  to predict how long will it take
*  to walk through the Kuala Lumpur Airport?
*  Like, you could give me an estimate
*  and it wouldn't be crazy.
*  And you have to have an estimate of that
*  in order to make plans that involve
*  walking through the Kuala Lumpur Airport,
*  even if you don't need to know it in detail.
*  So I'm really interested in these kinds of abstract models
*  and how do we acquire them.
*  But once we have them, we can use them
*  to do hierarchical reasoning,
*  which I think is very important.
*  Yeah, there's this notion of goal regression
*  and pre-image backchaining,
*  this idea of starting at the goal.
*  And it's just forming these big clouds of states.
*  I mean, it's almost like saying to the airport,
*  you know once you show up to the airport
*  that you're like a few steps away from the goal.
*  So thinking of it this way is kind of interesting.
*  I don't know if you have further comments on that,
*  of starting at the goal.
*  Yeah, I mean, it's interesting that Simon,
*  Herb Simon back in the early days of AI
*  talked a lot about means ends reasoning
*  and reasoning back from the goal.
*  There's a kind of an intuition that people have
*  that the number of states base is big,
*  the number of actions you could take is really big.
*  So if you say, here I sit
*  and I wanna search forward from where I am,
*  what are all the things I could do?
*  That's just overwhelming.
*  If you say, if you can reason at this other level
*  and say, here's what I'm hoping to achieve,
*  what could I do to make that true
*  that somehow the branching is smaller?
*  Now, what's interesting is that
*  like in the AI planning community,
*  in the class of problems that they look at
*  and the methods that they tend to use,
*  it hasn't turned out that it's better to go backward.
*  It's still kind of my intuition that it is,
*  but I can't prove that to you right now.
*  Right, I share your intuition,
*  at least for us mere humans.
*  Speaking of which, when you maybe,
*  now we take a little step into that philosophy circle.
*  How hard would it, when you think about human life,
*  you give those examples often.
*  How hard do you think it is to formulate
*  human life as a planning problem or aspects of human life?
*  So when you look at robots,
*  you're often trying to think about object manipulation,
*  tasks about moving a thing.
*  When you take a slight step outside the room,
*  let the robot leave and go get lunch
*  or maybe try to pursue more fuzzy goals.
*  How hard do you think is that problem?
*  If you were to try to maybe put another way,
*  try to formulate human life as a planning problem.
*  Well, that would be a mistake.
*  I mean, it's not all the planning problem, right?
*  I think it's really, really important that we understand
*  that you have to put together pieces and parts
*  that have different styles of reasoning
*  and representation and learning.
*  I think it seems probably clear to anybody
*  that it can't all be this or all be that.
*  Brains aren't all like this or all like that, right?
*  They have different pieces and parts
*  and substructure and so on.
*  So I don't think that there's any good reason
*  to think that there's gonna be one true algorithmic thing
*  that's gonna do the whole job.
*  Just a bunch of pieces together,
*  designed to solve a bunch of specific problems.
*  One specific...
*  Or maybe styles of problems.
*  I mean, there's probably some reasoning
*  that needs to go on in image space.
*  I think, again, there's this model-based
*  versus model-free idea, right?
*  So in reinforcement learning, people talk about,
*  oh, should I learn, I could learn a policy
*  just straight up a way of behaving.
*  I could learn it's popular learning.
*  A value function,
*  that's some kind of weird intermediate ground.
*  Or I could learn a transition model,
*  which tells me something about the dynamics of the world.
*  If I take a, imagine that I learn a transition model
*  and I couple it with a planner
*  and I draw a box around that,
*  I have a policy again.
*  It's just stored a different way, right?
*  It's, but it's just as much of a policy
*  as the other policy.
*  It's just, I've made, I think,
*  the way I see it is it's a time-space trade-off
*  in computation, right?
*  More overt policy representation,
*  maybe it takes more space,
*  but maybe I can compute quickly what action I should take.
*  On the other hand, maybe a very compact model
*  of the world dynamics plus a planner
*  lets me compute what action to take too,
*  just more slowly.
*  There's no, I mean, I don't think,
*  there's no argument to be had.
*  It's just like a question of what form of computation
*  is best for us.
*  For the various sub-problems.
*  Right, so, and so like learning to do algebra manipulations
*  for some reason is, I mean,
*  that's probably gonna want naturally
*  a sort of a different representation
*  than riding a unicycle.
*  At the time constraints on the unicycle are serious.
*  The space is maybe smaller, I don't know,
*  but so I-
*  And there could be the more human size
*  of falling in love, having a relationship.
*  That might be another style of-
*  I have no idea.
*  How to model that, yeah.
*  Let's first solve the algebra and the object manipulation.
*  What do you think is harder, perception or planning?
*  Perception, that's why I'm planning.
*  Understanding.
*  So what do you think is so hard about perception
*  by understanding the world around you?
*  Well, I mean, I think the big question
*  is representational.
*  Hugely the question is representational.
*  So perception has made great strides lately, right?
*  And we can classify images
*  and we can play certain kinds of games
*  and predict how to steer the car
*  and all this sort of stuff.
*  I don't think we have a very good idea
*  of what perception should deliver, right?
*  So if you believe in modularity, okay,
*  there's a very strong view which says
*  we shouldn't build in any modularity,
*  we should make a giant gigantic neural network,
*  train it end to end to do the thing
*  and that's the best way forward.
*  And it's hard to argue with that
*  except on a sample complexity basis, right?
*  So you might say, oh, well, if I wanna do
*  end to end reinforcement learning
*  on this giant, giant neural network,
*  it's gonna take a lot of data
*  and a lot of like broken robots and stuff.
*  So then the only answer is to say,
*  okay, we have to build something in,
*  build in some structure or some bias.
*  We know from theory of machine learning,
*  the only way to cut down the sample complexity
*  is to kind of cut down,
*  somehow cut down the hypothesis space.
*  You can do that by building in bias.
*  There's all kinds of reasons to think
*  that nature built bias into humans.
*  Convolution is a bias.
*  It's a very strong bias and it's a very critical bias.
*  So my own view is that we should look for more things
*  that are like convolution,
*  but that address other aspects of reasoning, right?
*  So convolution helps us a lot
*  with a certain kind of spatial reasoning
*  that's quite close to the imaging.
*  I think there's other ideas like that,
*  maybe some amount of forward search,
*  maybe some notions of abstraction,
*  maybe the notion that objects exist,
*  actually I think that's pretty important
*  and a lot of people won't give you that to start with.
*  So almost like a convolution in the object,
*  semantic object space or some kind of ideas in there.
*  That's right and people are starting,
*  like the graph convolutions are an idea
*  that are related to relational representations.
*  And so I think there are,
*  so I've come far afield from perception,
*  but I think the thing that's gonna make perception
*  kind of the next step is actually understanding better
*  what it should produce, right?
*  So what are we gonna do with the output of it, right?
*  It's fine when what we're gonna do with the output is steer,
*  it's less clear when we're just trying to make
*  one integrated intelligent agent.
*  What should the output of perception be?
*  We have no idea and how should that hook up
*  to the other stuff?
*  We don't know.
*  So I think the pressing question is,
*  what kinds of structure can we build in
*  that are like the moral equivalent of convolution
*  that will make a really awesome superstructure
*  that then learning can kind of progress on efficiently?
*  I agree, very compelling description
*  of actually where we stand with the perception of them.
*  You're teaching a course on a body and intelligence.
*  What do you think it takes to build a robot
*  with human level intelligence?
*  I don't know if we knew we would do it.
*  If you were to, I mean, okay, so do you think a robot
*  needs to have self-awareness, consciousness,
*  fear of mortality, or is it simpler than that?
*  Or is consciousness a simple thing?
*  Like do you think about these notions?
*  I don't think much about consciousness,
*  even most philosophers who care about it
*  will give you that you could have robots that are zombies,
*  that behave like humans but are not conscious.
*  And I, at this moment, would be happy enough with that.
*  So I'm not really worried one way or the other.
*  So the technical side,
*  you're not thinking of the use of self-awareness.
*  Well, okay, but then what does self-awareness mean?
*  I mean, that you need to have some part of the system
*  that can observe other parts of the system
*  and tell whether they're working well or not.
*  That seems critical.
*  So does that count as, I mean,
*  does that count as self-awareness or not?
*  Well, it depends on whether you think
*  that there's somebody at home who can articulate
*  whether they're self-aware.
*  But clearly, if I have like, you know,
*  some piece of code that's counting
*  how many times this procedure gets executed,
*  that's a kind of self-awareness, right?
*  So there's a big spectrum.
*  It's clear you have to have some of it.
*  Right, you know, we're quite far away on many dimensions,
*  but is there a direction of research
*  that's most compelling to you for, you know,
*  trying to achieve human-level intelligence in our robots?
*  Well, to me, I guess the thing that seems most compelling
*  to me at the moment is this question
*  of what to build in and what to learn.
*  I think we're missing a bunch of ideas
*  and we, you know, people, you know,
*  don't you dare ask me how many years it's gonna be
*  till that happens, because I won't even participate
*  in the conversation, because I think we're missing ideas
*  and I don't know how long it's gonna take to find them.
*  So I won't ask you how many years,
*  but maybe I'll ask you when you'll be sufficiently impressed
*  that we've achieved it.
*  So what's a good test of intelligence?
*  Do you like the Turing test, the natural language,
*  and the robotics space?
*  Is there something where you would sit back and think,
*  oh, that's pretty impressive as a test, as a benchmark?
*  Do you think about these kinds of problems?
*  No, I resist.
*  I mean, I think all the time that we spend arguing
*  about those kinds of things could be better spent
*  just making the robots work better.
*  So.
*  You don't value competition?
*  So, I mean, there's a nature of benchmark,
*  of benchmarks and data sets or Turing test challenges
*  where everybody kind of gets together
*  and tries to build a better robot
*  because they wanna out-compete each other.
*  Like the DARPA challenge with the autonomous vehicles.
*  Do you see the value of that?
*  Or can get in the way?
*  I think it can get in the way.
*  I mean, some people, many people find it motivating
*  and so that's good.
*  I find it anti-motivating personally.
*  Yeah.
*  But I think what, I mean, I think you get an interesting
*  cycle where for a contest, a bunch of smart people
*  get super motivated and they hack their brains out
*  and much of what gets done is just hacks,
*  but sometimes really cool ideas emerge
*  and then that gives us something to chew on after that.
*  So, it's not a thing for me,
*  but I don't regret that other people do it.
*  Yeah, it's like you said, with everything else,
*  the mix is good.
*  So jumping topics a little bit,
*  you started the Journal of Machine Learning Research
*  and served as its editor in chief.
*  How did the publication come about?
*  And what do you think about the current publishing model
*  space in machine learning, artificial intelligence?
*  That's interesting, yeah, okay, good.
*  So it came about because there was a journal called
*  Machine Learning, which still exists,
*  which was owned by Cluer.
*  And there was, I was on the editorial board
*  and we used to have these meetings annually
*  where we would complain to Cluer that it was too expensive
*  for the libraries and that people couldn't publish
*  and we would really like to have some kind of relief
*  on those fronts and they would always sympathize
*  but not do anything.
*  So, we just decided to make a new journal.
*  And there was the Journal of AI Research,
*  which was on the same model,
*  which had been in existence for maybe five years or so,
*  and it was going on pretty well.
*  So, we just made a new journal.
*  It wasn't, I mean, I don't know, I guess it was work,
*  but it wasn't that hard.
*  So basically, the editorial board,
*  probably 75% of the editorial board
*  of Machine Learning resigned
*  and we founded this new journal.
*  But it was sort of, it was more open.
*  Yeah, right.
*  So, it's completely open, it's open access.
*  Actually, I had a postdoc, George Kanadaris,
*  who wanted to call these journals free for all.
*  Because they were, I mean, it both has no page charges
*  and has no access restrictions.
*  And the reason, and so lots of people,
*  I mean, there were people who were mad
*  about the existence of this journal
*  who thought it was a fraud or something.
*  It would be impossible, they said,
*  to run a journal like this with basically,
*  I mean, for a long time, I didn't even have a bank account.
*  I paid for the lawyer to incorporate
*  and the IP address.
*  And it just didn't cost a couple hundred dollars a year
*  to run.
*  It's a little bit more now, but not that much more.
*  But that's because I think computer scientists
*  are competent and autonomous in a way
*  that many scientists in other fields aren't.
*  I mean, doing these kinds of things.
*  We already typeset around papers.
*  We all have students and people
*  who can hack a website together in the afternoon.
*  So the infrastructure for us was like, not a problem.
*  But for other people in other fields,
*  it's a harder thing to do.
*  Yeah, and this kind of open access journal
*  is nevertheless one of the most prestigious journals.
*  So it's not like a prestige and it can be achieved
*  without any of the...
*  Paper is not required for prestige, turns out.
*  Yeah.
*  So on the review process side,
*  I've actually, a long time ago,
*  I don't remember when I reviewed a paper
*  where you were also a reviewer.
*  I remember reading your review and being influenced by it.
*  It was really well written.
*  It influenced how I write feature reviews.
*  You disagreed with me, actually.
*  And you made it my review, but much better.
*  But nevertheless, the review process has its flaws.
*  And how do you think, what do you think works well?
*  How can it be improved?
*  So actually, when I started JamLR,
*  I wanted to do something completely different.
*  And I didn't because it felt like
*  we needed a traditional journal of record.
*  And so we just made JamLR be almost like a normal journal,
*  except for the open access parts of it, basically.
*  Increasingly, of course, publication
*  is not even a sensible word.
*  You can publish something by putting it in an archive
*  so I can publish everything tomorrow.
*  So making stuff public is, there's no barrier.
*  We still need curation and evaluation.
*  I don't have time to read all of archive.
*  And you could argue that
*  social thumbs-upping of articles suffices.
*  You might say, oh, heck with this.
*  We don't need journals at all.
*  We'll put everything on archive
*  and people will upvote and downvote the articles.
*  And then your CV will say, oh man, he got a lot of upvotes.
*  So that's good.
*  But I think there's still value
*  in careful reading and commentary of things.
*  And it's hard to tell when people are upvoting
*  and downvoting or arguing about your paper on Twitter
*  and Reddit, whether they know what they're talking about.
*  So then I have the second order problem
*  of trying to decide whose opinions I should value and such.
*  So I don't know.
*  If I had infinite time, which I don't,
*  and I'm not gonna do this
*  because I really wanna make robots work,
*  but if I felt inclined to do something more
*  in the publication direction,
*  I would do this other thing,
*  which I thought about doing the first time,
*  which is to get together some set of people
*  whose opinions I value and who are pretty articulate.
*  And I guess we would be public,
*  although we could be private, I'm not sure.
*  And we would review papers.
*  We wouldn't publish them and you wouldn't submit them.
*  We would just find papers and we would write reviews.
*  And we would make those reviews public.
*  And maybe if you, so we're Leslie's friends
*  who review papers and maybe eventually
*  if our opinion was sufficiently valued,
*  like the opinion of JMR is valued,
*  then you'd say on your CV that Leslie's friends
*  gave my paper a five-star rating
*  and that would be just as good as saying,
*  oh my God, it accepted into this journal.
*  So I think we should have good public commentary
*  and organize it in some way,
*  but I don't really know how to do it.
*  It's interesting times.
*  The way you described it actually is really interesting.
*  I mean, we do it for movies, imdb.com.
*  There's experts, critics come in, they write reviews,
*  but there's also regular non-critics.
*  Humans write reviews and they're separated.
*  I like open review.
*  The iClear process, I think, is interesting.
*  It's a step in the right direction,
*  but it's still not as compelling
*  as reviewing movies or video games.
*  I mean, sometimes almost, it might be silly,
*  at least from my perspective to say,
*  but it boils down to the user interface,
*  how fun and easy it is to actually perform the reviews,
*  how efficient, how much you as a reviewer
*  get street cred for being a good reviewer.
*  Those human elements come into play.
*  No, it's a big investment to do a good review of a paper,
*  and the flood of papers is out of control.
*  So there aren't 3,000 new,
*  I don't know how many new movies are there in a year.
*  I don't know, but there's probably gonna be less
*  than how many machine learning papers there are
*  in a year now.
*  And I'm worried, you know, I,
*  right, so I'm like an old person,
*  so of course I'm gonna say,
*  ra ra ra, things are moving too fast,
*  I must stick in the mud.
*  So I can say that, but my particular flavor of that is,
*  I think the horizon for researchers has gotten very short,
*  that students want to publish a lot of papers,
*  and there's a huge, there's value,
*  it's exciting and there's value in that,
*  and you get patted on the head for it and so on.
*  But, and some of that is fine,
*  but I'm worried that we're driving out people
*  who would spend two years thinking about something.
*  Back in my day, when we worked on our theses,
*  we did not publish papers.
*  You did your thesis for years,
*  you picked a hard problem and then you worked
*  and chewed on it and did stuff and wasted time
*  and for a long time.
*  And when it was, roughly when it was done,
*  you would write papers.
*  And so I don't know how to,
*  and I don't think that everybody has to work in that mode,
*  but I think there's some problems that are hard enough
*  that it's important to have a longer research horizon,
*  and I'm worried that we don't incentivize that at all
*  at this point.
*  In this current structure.
*  Right.
*  So what do you see as,
*  what are your hopes and fears about the future of AI
*  and continuing on this theme?
*  So AI has gone through a few winters,
*  ups and downs.
*  Do you see another winter of AI coming?
*  Or are you more hopeful about making robots work,
*  as you said?
*  I think the cycles are inevitable.
*  But I think each time we get higher, right?
*  I mean, so, you know, it's like climbing some kind
*  of landscape with a noisy optimizer.
*  So it's clear that the deep learning stuff
*  has made deep and important improvements.
*  And so the high water mark is now higher.
*  There's no question.
*  But of course, I think people are overselling
*  and eventually investors, I guess,
*  and other people look around and say,
*  well, you're not quite delivering on this grand claim
*  and that wild hypothesis.
*  It's so probably it's gonna crash some amount.
*  And then it's okay.
*  I mean, but I can't imagine that there's like
*  some awesome monotonic improvement
*  from here to human level AI.
*  So in, you know, I have to ask this question.
*  I probably anticipate the answers,
*  but do you have a worry short term or long term
*  about the existential threats of AI
*  and maybe short term, less existential,
*  but more robots taking away jobs?
*  Well, actually, let me talk a little bit about utility.
*  Actually, I had an interesting conversation
*  with some military ethicists who wanted to talk to me
*  about autonomous weapons.
*  And they were interesting, smart, well educated guys
*  who didn't know too much about AI or machine learning.
*  And the first question they asked me was,
*  has your robot ever done something you didn't expect?
*  And I like burst out laughing
*  because anybody who's ever done something on the robot,
*  right, knows that they don't do it.
*  And what I realized was that their model
*  of how we program a robot was completely wrong.
*  Their model of how we can program a robot
*  was like Lego Mindstorms.
*  Oh, go forward a meter, turn left, take a picture,
*  do this, do that.
*  And so if you have that model of programming,
*  then it's true, it's kind of weird
*  that your robot would do something
*  that you didn't anticipate.
*  But the fact is, and actually,
*  so now this is my new educational mission.
*  If I have to talk to non-experts,
*  I try to teach them the idea that we don't operate,
*  we operate at least one or maybe many levels
*  of abstraction about that.
*  And we say, oh, here's a hypothesis class.
*  Maybe it's a space of plans
*  or maybe it's a space of classifiers or whatever,
*  but there's some set of answers and an objective function.
*  And then we work on some optimization method
*  that tries to optimize a solution in that class.
*  And we don't know what solution is gonna come out, right?
*  So I think it's important to communicate that.
*  So I mean, of course, probably people who listen to this,
*  they know that lesson,
*  but I think it's really critical to communicate that lesson.
*  And then lots of people are now talking about, you know,
*  the value alignment problem.
*  So you wanna be sure as robots
*  or software systems get more competent
*  that their objectives are aligned with your objectives
*  or that our objectives are compatible in some way,
*  or we have a good way of mediating
*  when they have different objectives.
*  And so I think it is important to start thinking in terms,
*  like you don't have to be freaked out
*  by the robot apocalypse to accept that it's important
*  to think about objective functions and value alignment.
*  And that you have to really,
*  everyone who's done optimization knows
*  that you have to be careful what you wish for,
*  that sometimes you get the optimal solution
*  and you realize, man, that objective was wrong.
*  So pragmatically in the shortest term, it seems to me,
*  that those are really interesting and critical questions.
*  And the idea that we're gonna go from being people
*  who engineer algorithms
*  to being people who engineer objective functions,
*  I think that's definitely gonna happen.
*  And that's gonna change our thinking and methodology.
*  You started at Stanford philosophy,
*  the Swiss of computer science,
*  and now we'll go back to philosophy.
*  Philosophy maybe.
*  Well, I mean, they're mixed together
*  because as we also know as machine learning people,
*  in fact, this is the lecture I gave in class today.
*  When you design an objective function,
*  you have to wear both hats.
*  There's the hat that says, what do I want?
*  And there's the hat that says,
*  but I know what my optimizer can do to some degree
*  and I have to take that into account.
*  So it's always a trade-off
*  and we have to kind of be mindful of that.
*  The part about taking people's jobs,
*  I understand that that's important.
*  I don't understand sociology or economics
*  or people very well.
*  So I don't know how to think about that.
*  So that's, yeah,
*  so there might be a sociological aspect there,
*  the economic aspect that's very difficult to think about.
*  I mean, I think other people should be thinking about it,
*  but that's not my strength.
*  So what do you think is the most exciting area of research
*  in the short term for the community and for yourself?
*  Well, so, I mean, there's this story I've been telling
*  about how to engineer intelligent robots.
*  So that's what we wanna do.
*  We all kind of wanna do, well, I mean,
*  some set of us wanna do this.
*  And the question is, what's the most effective strategy?
*  And we've tried, and there's a bunch of different things
*  you could do at the extremes, right?
*  One super extreme is we do introspection
*  and we write a program.
*  Okay, that has not worked out very well.
*  Another extreme is we take a giant bunch of neural goo
*  and we train it up to do something.
*  I don't think that's gonna work either.
*  So the question is, what's the middle ground?
*  And again, this isn't a theological question
*  or anything like that.
*  It's just like, how do we,
*  what's the best way to make this work out?
*  And I think it's clear, it's a combination of learning.
*  To me, it's clear.
*  It's a combination of learning and not learning.
*  And what should that combination be
*  and what's the stuff we build in?
*  So to me, that's the most compelling question.
*  And when you say engineer robots,
*  you mean engineering systems that work in the real world.
*  Is that, that's the emphasis.
*  Last question, which robot or robot
*  is your favorite from science fiction?
*  So you can go with Star Wars or RTD2
*  or you can go with a more modern, maybe Hal.
*  I don't think I have a favorite robot from science fiction.
*  This is back to, you like to make robots work
*  in the real world here, not in...
*  I mean, I love the process
*  and I care more about the process than the process.
*  The engineering process.
*  I mean, I do research because it's fun,
*  not because I care about what we produce.
*  Well, that's a beautiful note actually.
*  And Leslie, thank you so much for talking today.
*  Sure, it's been fun.
*  Thank you.

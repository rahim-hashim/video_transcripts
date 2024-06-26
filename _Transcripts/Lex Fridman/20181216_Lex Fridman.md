---
Date Generated: April 14, 2024
Transcription Model: whisper medium 20231117
Length: 2564s
Video Keywords: []
Video Views: 64018
Video Rating: None
---

# Pieter Abbeel: Deep Reinforcement Learning | Lex Fridman Podcast #10
**Lex Fridman:** [December 16, 2018](https://www.youtube.com/watch?v=l-mYLq6eZPY)
*  The following is a conversation with Peter Abil.
*  He's a professor at UC Berkeley and the director of the Berkeley Robotics Learning Lab.
*  He's one of the top researchers in the world working on how we make robots
*  understand and interact with the world around them, especially using imitation and deep reinforcement learning.
*  This conversation is part of the MIT course on Artificial General Intelligence
*  and the Artificial Intelligence podcast.
*  If you enjoy it, please subscribe on YouTube, iTunes, or your podcast provider of choice,
*  or simply connect with me on Twitter at Lex Friedman, spelled F-R-I-D.
*  And now here's my conversation with Peter Abil.
*  You've mentioned that if there was one person you could meet, it would be Roger Federer.
*  So let me ask, when do you think we will have a robot that fully autonomously can beat Roger Federer
*  at tennis, Roger Federer level player at tennis?
*  Well, first, if you can make it happen for me to meet Roger, let me know.
*  In terms of getting a robot to beat him at tennis, it's kind of an interesting question because
*  for a lot of the challenges we think about in AI, the software is really the missing piece.
*  But for something like this, the hardware is nowhere near either.
*  To really have a robot that can physically run around, the Boston Dynamics robots are
*  starting to get there, but still not really human level ability to run around and then swing a racket.
*  So you think that's a hardware problem?
*  I don't think it's a hardware problem only. I think it's a hardware and a software problem.
*  I think it's both. And I think they'll have independent progress.
*  I'd say the hardware maybe in 10, 15 years.
*  On clay, not grass.
*  I'm not sure what's harder, grass or clay. The clay involves sliding,
*  which might be harder to master actually.
*  You're not limited to bipedal.
*  We can build a machine. It's a whole different question, of course. If you can say, okay,
*  this robot can be on wheels, it can move around on wheels and can be designed differently, then I
*  think that can be done sooner probably than a full humanoid type of setup.
*  What do you think is swing a racket? So you've worked at basic manipulation.
*  How hard do you think is the task of swinging a racket? Would it be able to hit a nice back hand
*  or a forehand? Let's say we just set up stationary,
*  a nice robot arm, let's say, a standard industrial arm, and it can watch the ball come and swing the
*  racket. It's a good question. I'm not sure it would be super hard to do. I'm sure it would require a
*  lot. If we do it with reinforcement learning, it would require a lot of trial and error. It's
*  not going to swing it right the first time around. But yeah, I don't see why I couldn't.
*  So you think it's learnable.
*  I think it's learnable. I think if you set up a ball machine, let's say on one side,
*  and then a robot with a tennis racket on the other side, I think it's learnable.
*  And maybe a little bit of pre-training and simulation. Yeah, I think that's feasible.
*  I think the swing the racket is feasible. It'd be very interesting to see how much precision it can get.
*  Because, I mean, that's where, I mean, some of the human players can hit it on the lines,
*  which is very high precision. With spin. The spin is an interesting, whether RL can learn to
*  put a spin on the ball. Well, you got me interested. Maybe someday we'll set this up.
*  Your answer is basically, okay, for this problem, it sounds fascinating. But for the general problem
*  of a tennis player, we might be a little bit farther away. What's the most impressive thing
*  you've seen a robot do in the physical world? So physically, for me, it's
*  the Boston Dynamics videos always just ring home and just super impressed.
*  Recently, the robot running up the stairs doing the parkour type thing. I mean, yes,
*  we don't know what's underneath. They don't really write a lot of detail. But
*  even if it's hard coded underneath, which it might or might not be just the physical abilities
*  of doing that parkour, that's a very impressive. So right there, have you met spot many or any of
*  those robots in person? Let's spot many last year in April at the Mars event that Jeff Bezos
*  organizes. They brought it out there and it was nicely following around Jeff. When Jeff left the
*  room, they had it follow him along, which is pretty impressive. So I think there's some confidence to
*  know that there's no learning going on on those robots, the psychology of it. So while knowing
*  that while knowing there's not if there's any learning going on, it's very limited. I met spot
*  many earlier this year and knowing everything that's going on, having one on one interaction.
*  So I get to spend some time alone. And there's a immediately a deep connection on the psychological
*  level, even though you know the fundamentals, how it works, there's something magical. So
*  do you think about the psychology of interacting with robots in the physical world? Even you just
*  showed me the PR to the robot and there was a little bit something like a face, had a little
*  bit something like a face, there's something that immediately draws you to it. Do you think about
*  that aspect of the robotics problem? Well, it's very hard with Brett here, we'll give him a name,
*  Berkeley Robot for the Elimination of Tedious Tasks. It's very hard to not think of
*  the robot as a person. And it seems like everybody calls him a he for whatever reason,
*  but that also makes it more a person than if it was a it. And it seems pretty natural to think
*  of it that way. This past weekend really struck me. I've seen Pepper many times on videos,
*  but then I was at an event organized by, this was by Fidelity, and they had scripted Pepper
*  to help moderate some sessions. And they had scripted Pepper to have the personality of a
*  child a little bit. And it was very hard to not think of it as its own person in some sense,
*  because it was just kind of jumping, it would just jump into conversation, making it very interactive.
*  Moderator would be saying, Pepper would just jump in, hold on, how about me? Can I participate
*  in this too? And you're just like, okay, this is like like a person. And that was 100% scripted.
*  And even then it was hard not to have that sense of somehow there is something there.
*  So as we have robots interact in this physical world, is that a signal that can be used in
*  reinforcement learning? You've, you've worked a little bit in this direction. But do you think
*  that that psychology can be somehow pulled in? Yes, that's a question. I would say, a lot,
*  a lot of people ask. And I think part of why they ask it is they're thinking about
*  how unique are we really still as people like after they see some results, they see a computer
*  play go to say computer do this, that they're like, okay, but can it really have emotion? Can
*  it really interact with us in that way? And then once you're around robots, you already start
*  feeling it. And I think that kind of maybe methodologically, the way that I think of it is,
*  if you run something like reinforcement learning, it's about optimizing some objective. And
*  and there's no reason that the objective couldn't be tied into how much does a person like
*  interacting with this system? And why could not the reinforcement learning system optimize for
*  the robot being fun to be around? And why wouldn't it then naturally become more and more attractive
*  and more and more, maybe like a person or like a pet, I don't know what it would exactly be,
*  but more and more have those features and acquire them automatically. As long as you can formalize
*  an objective of what it means to like something, what how you exhibit, what's the ground truth?
*  How do you how do you get the reward from human? Because you have to somehow collect that information
*  within you human but you're saying if you can formulate as an objective, it can be learned.
*  There's no reason it couldn't emerge through learning. And maybe one way to formulate as
*  an objective, you wouldn't have to necessarily score it explicitly. So standard rewards are
*  numbers and numbers are hard to come by. This is a 1.5 or 1.7 on some scale, it's very hard to do
*  for a person. But much easier is for a person to say, okay, what you did the last five minutes was
*  much nicer than we did the previous five minutes. And that now gives a comparison. And in fact,
*  there have been some results on that. For example, Paul Cristiano and collaborators at OpenAI had the
*  hopper, mojoco hopper, one legged robot, the backflips purely from feedback. I like this better than
*  that. That's kind of equally good. And after a bunch of interactions, it figured out what it was
*  the person was asking for, namely a backflip. And so I think the same thing. Oh, it wasn't trying to
*  do a backflip. It was just getting a score from the comparison score from the person based on
*  the person having a mind in their own mind, I wanted to do a backflip, but the robot didn't know
*  what it was supposed to be doing. It just knew that sometimes the person said this is better,
*  this is worse. And then the robot figured out what the person was actually after was a backflip. And
*  I'd imagine the same would be true for things like more interactive robots that the robot would
*  figure out over time, oh, this kind of thing apparently is appreciated more than this other
*  kind of thing. So when I first picked up Sutton's, Richard Sutton's reinforcement learning book,
*  before sort of this deep learning, before the reemergence of neural networks as a powerful
*  mechanism for machine learning, RL seemed to me like magic. It was beautiful. So that seemed like
*  what intelligence is RL reinforcement learning. So how do you think we can possibly learn anything
*  about the world when the reward for the actions is delayed is so sparse? Like where is, why do
*  you think RL works? Why do you think you can learn anything under such sparse rewards, whether it's
*  regular reinforcement learning or deep reinforcement learning? What's your intuition?
*  The counterpart of that is why is RL, why does it need so many samples, so many experiences to
*  learn from? Because really what's happening is when you have a sparse reward, you do something
*  maybe for like, I don't know, you take 100 actions and then you get a reward. And maybe you get like
*  a score of three. And I'm like, okay, three, not sure what that means. You go again, and now I get
*  two. And now you know that that sequence of 100 actions that you did the second time around somehow
*  was worse than the sequence of 100 actions you did the first time around. But that's tough to
*  not know which one of those were better or worse. Some might have been good and bad and either one.
*  And so that's why I need so many experiences. But once you have enough experiences, effectively,
*  RL is teasing that apart. It's starting to say, okay, when what is consistently there when you
*  get a higher reward and what's consistently there when you get a lower reward? And then kind of the
*  magic of sometimes the policy gradient update is to say, now let's update the neural network
*  to make the actions that were kind of present when things are good, more likely, and make the
*  actions that are present when things are not as good, less likely. So that's that is the
*  counterpoint. But it seems like you would need to run it a lot more than you do, even though right
*  now, people could say that RL is very inefficient. But it seems to be way more efficient than one
*  would imagine on paper, that the simple updates to the policy, the policy gradient that somehow
*  you can learn exactly, you just said, what are the common actions that seem to produce some
*  good results that that somehow can learn anything? It seems counterintuitive, at least.
*  Did is there some intuition behind? Yeah. So I think there's a few ways to think about this.
*  The way I tend to think about it mostly originally, when so when we started working on deep
*  reinforcement learning here at Berkeley, which was maybe 2011, 12, 13, around that time,
*  John Schulman was a PhD student, initially kind of driving it forward here. And
*  the way we thought about it at the time was if you think about rectified linear units, or kind
*  of rectifier type neural networks, what do you get? You get something that's piecewise linear
*  feedback control. And if you look at the literature, linear feedback control is
*  extremely successful, can solve many, many problems surprisingly well. I remember, for example,
*  when we did helicopter flight, if you're in a stationary flight regime, not a nonstationary,
*  but the stationary flight regime like hover, you can use linear feedback control to stabilize
*  a helicopter, very complex dynamical system. But the controller is relatively simple. And so I
*  think that's a big part of is that if you do feedback control, even though the system you
*  control can be very, very complex, often relatively simple control architectures can already do a lot.
*  But then also just linear is not good enough. And so one way you can think of these neural
*  networks is that then sometimes they tile the space, which people were already trying to do
*  more by hand or with finite state machines, say this linear controller here, this linear
*  controller here, neural network learns to tile the space and say linear controller here, another
*  linear controller here, but it's more subtle than that. And so it's benefiting from this linear
*  control aspect, it's benefiting from the tiling, but it's somehow tiling it one dimension at a time.
*  Because if let's say you have a two layer network, even that hidden layer, you make a transition from
*  active to inactive or the other way around, that is essentially one axis, but not axis aligned,
*  but one direction that you change. And so you have this kind of very gradual tiling of the space,
*  we have a lot of sharing between the linear controllers that tile the space. And that was
*  always my intuition as to why to expect that this might work pretty well. It's essentially
*  leveraging the fact that linear feedback control is so good, but of course not enough. And this is a
*  gradual tiling of the space with linear feedback controls that share a lot of expertise across them.
*  So that's really nice intuition. But do you think that scales to the more and more general problems
*  of when you start going up the number of control dimensions, when you start going
*  down in terms of how often you get a clean reward signal? Does that intuition carry forward to those
*  crazier, weirder worlds that we think of as the real world?
*  So I think where things get really tricky in the real world compared to the things we've looked at
*  so far with great success in reinforcement learning is the time scales, which takes us to an extreme.
*  So when you think about the real world, I mean, I don't know, maybe some student decided to do a
*  PhD here, right? Okay, that's a decision. That's a very high level decision. But if you think about
*  their lives, I mean, any person's life, it's a sequence of muscle fiber contractions and
*  relaxations. And that's how you interact with the world. And that's a very high frequency control thing.
*  But it's ultimately what you do and how you affect the world. Until I guess we have brain readings,
*  you can maybe do it slightly differently. But typically, that's how you affect the world.
*  And the decision of doing a PhD is like so abstract relative to what you're actually doing
*  in the world. And I think that's where credit assignment becomes just completely beyond what
*  any current RL algorithm can do. And we need hierarchical reasoning at a level that is just
*  not available at all yet. Where do you think we can pick up hierarchical reasoning by which mechanisms?
*  Yeah, so maybe let me highlight what I think the limitations are of what already was done
*  20, 30 years ago. In fact, you'll find reasoning systems that reason over relatively long horizons,
*  but the problem is that they were not grounded in the real world. So people would have to hand design
*  some kind of logical, dynamical descriptions of the world. And that didn't tie into perception.
*  And so it didn't tie into real objects and so forth. And so that was a big gap. Now with
*  deep learning, we start having the ability to really see with sensors, process that and understand
*  what's in the world. And so it's a good time to try to bring these things together. One, I see a
*  few ways of getting there. One way to get there would be to say, deep learning can get bolted on
*  somehow to some of these more traditional approaches. Now bolted on would probably mean
*  you need to do some kind of end to end training, where you say, my deep learning processing somehow
*  leads to a representation that in term uses some kind of traditional underlying dynamical systems
*  that can be used for planning. And that's, for example, the direction Aviv Tamar and
*  Thanard Kuritach here have been pushing with causal info again, and of course, other people too.
*  That's one way. Can we somehow force it into the form factor that is amenable to reasoning?
*  Another direction we've been thinking about for a long time and didn't make any progress on was
*  more information theoretic approaches. So the idea there was that what it means to take high
*  level action is to choose a latent variable now that tells you a lot about what's going to be the
*  case in the future, because that's what it means to take a high level action. I say, okay,
*  I decide I'm going to navigate to the gas station because I need to get gas for my car. Well, that
*  will now take five minutes to get there. But the fact that I get there, I could already tell that
*  from the high level action I took much earlier. That we had a very hard time getting success with,
*  not saying it's a dead end necessarily, but we had a lot of trouble getting that to work.
*  And then we started revisiting the notion of what are we really trying to achieve?
*  What we're trying to achieve is not necessarily hierarchy per se, but you could think about what
*  does hierarchy give us? What we hope it would give us is better credit assignment.
*  What does better credit assignment is giving us? It gives us faster learning.
*  And so faster learning is ultimately maybe what we're after. And so that's where we ended up with
*  the RL squared paper on learning to reinforcement learn, which at the time Rocky Duan led. And
*  that's exactly the meta learning approach where you say, okay, we don't know how to design hierarchy.
*  We don't know how to design hierarchy. We know what we want to get from it. Let's just end to an
*  optimize for what we want to get from it and see if it might emerge. And we saw things emerge. The
*  maze navigation had consistent motion down hallways, which is what you want. A hierarchical
*  controller should say, I want to go down this hallway. And then when there is an option to take
*  a turn, I can decide whether to take a turn or not and repeat. Even had the notion of where have you
*  been before or not to not revisit places you've been before. It still didn't scale yet.
*  To the real world kind of scenarios I think you had in mind, but it was some sign of life that
*  maybe you can meta learn these hierarchical concepts. I mean, it seems like through these
*  meta learning concepts, get at the what I think is one of the hardest and most important problems of
*  AI, which is transfer learning. So it's generalization. How far along this journey
*  towards building general systems are we being able to do transfer learning well?
*  So there's some signs that you can generalize a little bit, but do you think we're on the
*  right path or totally different breakthroughs are needed to be able to transfer knowledge
*  between different learned models? Yeah, I'm pretty torn on this. And then I think there are some very
*  impressive results already. I mean, I would say when even with the initial kind of big breakthrough
*  in 2012 with AlexNet, the initial thing is, okay, great. This does better on ImageNet,
*  hence image recognition. But then immediately thereafter, there was of course the notion that,
*  wow, what was learned on ImageNet, and you now want to solve a new task, you can fine tune AlexNet
*  for new tasks. And that was often found to be the even bigger deal that you learn something that was
*  reusable, which was not often the case before. Usually machine learning, you learn something for
*  one scenario, and that was it. And that's really exciting. I mean, that's just a huge application.
*  That's probably the biggest success of transfer learning today, if in terms of scope and impact.
*  That was a huge breakthrough. And then recently, I feel like similar,
*  kind of by scaling things up, it seems like this has been expanded upon, like people training even
*  bigger networks, they might transfer even better. If you looked at, for example, some of the OpenAI
*  results on language models, and some of the recent Google results on language models, they are learned
*  for just prediction, and then they get reused for other tasks. And so I think there is something
*  there where somehow if you train a big enough model on enough things, it seems to transfer
*  some deep mind results that I thought were very impressive, the Unreal results, where it was
*  learned to navigate mazes in ways where it wasn't just doing reinforcement learning, but it had other
*  objectives, was optimizing for. So I think there's a lot of interesting results already. I think
*  maybe where it's hard to wrap my head around this, to which extent or when do we call something
*  generalization, right? Or the levels of generalization involved in these different tasks.
*  Right? So you draw this, by the way, just to frame things, I've heard you say somewhere,
*  it's the difference between learning to master versus learning to generalize, that it's a nice
*  line to think about. And I guess you're saying that it's a gray area of what learning to master
*  and learning to generalize, where one starts. I think I might have heard this. I might have heard
*  it somewhere else. And I think it might have been one of your interviews, maybe the one with
*  Yoshua Benjamin. I'm not 100% sure. But I like the example. I'm not sure who it was. But
*  the example was essentially if you use current deep learning techniques, what we're doing to predict
*  let's say, the relative motion of our planets, it would do pretty well. But then now if a massive
*  new mass enters our solar system, it would probably not predict what will happen. Right?
*  And that's a different kind of generalization. That's a generalization that relies on the
*  ultimate simplest, simplest explanation that we have available today to explain the motion of
*  planets, whereas just pattern recognition could predict our current solar system motion pretty
*  well. No problem. And so I think that's an example of a kind of generalization that
*  is a little different from what we've achieved so far. And it's not clear if just regularizing
*  more and forcing it to come up with a simpler, simpler, simpler explanation. Look, this is not
*  simple. But that's what physics researchers do, right? They say, can I make this even simpler?
*  How simple can I get this? What's the simplest equation that can explain everything? Right?
*  The master equation for the entire dynamics of the universe. We haven't really pushed that
*  direction as hard in deep learning, I would say. Not sure if it should be pushed, but it seems
*  a kind of generalization you get from that that you don't get in our current methods so far.
*  So I just talked to Vladimir Vapnik, for example, who is a statistician, statistical learning,
*  and he kind of dreams of creating the E equals MC squared for learning, right? The general theory
*  of learning. Do you think that's a fruitless pursuit in near term in within the next several
*  decades? I think that's a really interesting pursuit. And in the following sense, in that
*  there is a lot of evidence that the brain is pretty modular. And so I wouldn't maybe think of
*  it as the theory, maybe the underlying theory, but more kind of the principle where there have
*  been findings where people who are blind will use the part of the brain usually used for vision,
*  for other functions. And even after some kind of if people get rewired in some way,
*  they might be able to reuse parts of their brain for other functions.
*  And so what that suggests is some kind of modularity. And I think it is a pretty natural
*  thing to strive for to see can we find that modularity? Can we find this thing? Of course,
*  it's not every every part of the brain is not exactly the same. Not everything can be rewired
*  arbitrarily. But if you think of things like the neocortex, which is a pretty big part of the brain,
*  that seems fairly modular from what the findings so far. Can you design something
*  equally modular? And if you can just grow it, it becomes more capable probably. I think that would
*  be the kind of interesting underlying principle to shoot for that is not unrealistic.
*  Do you think you prefer math or empirical trial and error for the discovery of the essence of
*  what it means to do something intelligent? So reinforcement learning embodies both groups,
*  right? To prove that something converges, prove the bounds. And then at the same time,
*  a lot of those successes are, well, let's try this and see if it works. So which do you gravitate
*  towards? How do you think of those two parts of your brain? So maybe I would prefer we could make
*  the progress with mathematics. And the reason maybe I would prefer that is because often if you have
*  something you can mathematically formalize, you can leapfrog a lot of experimentation. And
*  experimentation takes a long time to get through. And a lot of trial and error, kind of reinforcement
*  learning your research process. But you need to do a lot of trial and error before you get to a
*  success. So if you can leapfrog that, to my mind, that's what the math is about. And hopefully,
*  once you do a bunch of experiments, you start seeing a pattern, you can do some derivations
*  that leapfrog some experiments. But I agree with you. I mean, in practice, a lot of the progress
*  has been such that we have not been able to find the math that allows it to leapfrog ahead. And we
*  are kind of making gradual progress one step at a time. A new experiment here, a new experiment
*  there that gives us new insights, and gradually building up, but not getting to something yet
*  where we're just, okay, here's an equation that now explains how, you know, that would be have
*  been two years of experimentation to get there. But this tells us what the results going to be.
*  Unfortunately, not so much yet. Not so much yet. But your hope is there. In trying to teach robots
*  or systems to do everyday tasks, or even in simulation, what do you think you're more
*  excited about? imitation learning or self play? So letting robots learn from humans,
*  or letting robots plan their own to try to figure out in their own way, and eventually play,
*  eventually interact with humans, or solve whatever problem is, what's the more exciting to you?
*  What's more promising you think is a research direction?
*  So when we look at self play, what's so beautiful about it is goes back to kind of the challenges
*  in reinforcement learning. So the challenge of reinforcement learning is getting signal.
*  And if you don't never succeed, you don't get any signal in self play.
*  You're on both sides. So one of you succeeds, and the beauty is also one of you fails. And so you see
*  the contrast, you see the one version of me that did better than the other version. And so every
*  time you play yourself, you get signal. And so whenever you can turn something into self play,
*  you're in a beautiful situation, where you can naturally learn much more quickly than in most
*  other reinforcement learning environments. So I think, I think if somehow we can turn more
*  reinforcement learning problems into self play formulations, that would go really, really far.
*  So far, self play has been largely around games where there is natural opponents. But if we could
*  do self play for other things, and let's say, I don't know, a robot learns to build a house. I mean,
*  that's a pretty advanced thing to try to do for a robot. But maybe tries to build a hut or something.
*  If that can be done through self play, it would learn a lot more quickly if somebody can figure
*  it out. And I think that would be something where it goes closer to kind of the mathematical leap
*  frogging, where somebody figures out a formalism to say, okay, any RL problem by playing this and
*  this idea, you can turn it into a self play problem where you get signal a lot more easily.
*  Reality is, many problems, we don't know how to turn into self play. And so either we need to
*  provide detailed reward. That doesn't just reward for achieving a goal, but rewards for making
*  progress. And that becomes time consuming. And once you're starting to do that, let's say you
*  want a robot to do something, you need to give all this detailed reward. Well, why not just give a
*  demonstration? Because why not just show the robot? And now the question is, how do you show the
*  robot? One way to show is to tele-operate the robot. And then the robot really experiences things.
*  And that's nice because that's really high signal to noise ratio data. And we've done a lot of that.
*  And you teach your robot skills in just 10 minutes, you can teach your robot a new basic skill. Like,
*  okay, pick up the bottle, place it somewhere else. That's a skill. No matter where the bottle starts,
*  maybe it always goes onto a target or something. That's fairly easy to teach your robot with tele-op.
*  Now, what's even more interesting if you can now teach your robot through third person learning,
*  where the robot watches you do something and doesn't experience it, but just watches it and
*  says, okay, well, if you're showing me that, that means I should be doing this. And I'm not going to
*  be using your hand because I don't get to control your hand, but I'm going to use my hand. I do that
*  mapping. And so that's where I think one of the big breakthroughs has happened this year. This was
*  led by Chelsea Finn here. It's almost like learning a machine translation for demonstrations where
*  you have a human demonstration and the robot learns to translate it into what it means for
*  the robot to do it. And that was a meta-learning formulation. Learn from one to get the other.
*  And that, I think, opens up a lot of opportunities to learn a lot more quickly.
*  So my focus is on autonomous vehicles. Do you think this approach of third person watching
*  the autonomous driving is amenable to this kind of approach?
*  So for autonomous driving, I would say it's third person is slightly easier. And the reason I'm
*  going to say it's slightly easier to do with third person is because the car dynamics are very well
*  understood. So the easier than first person, you mean? Or I think, I think, so I think the
*  distinction between third person and first person is not a very important distinction for autonomous
*  driving. They're very similar because the distinction is really about who turns the steering wheel. And
*  or maybe, let me put it differently. How to get from a point where you are now to a point,
*  let's say a couple meters in front of you. And that's a problem that's very well understood.
*  And that's the only distinction between third and first person there. Whereas with the robot
*  manipulation, interaction forces are very complex and it's still a very different thing.
*  For autonomous driving, I think there is still the question imitation versus RL. So imitation
*  gives you a lot more signal. I think where imitation is lacking and needs some extra
*  machinery is it doesn't in its normal format doesn't think about goals or objectives.
*  And of course, there are versions of imitation learning inverse reinforcement type imitation,
*  and which also thinks about goals. I think then we're getting much closer, but I think it's very
*  hard to think of a fully reactive car generalizing well if it really doesn't have a notion of
*  objectives to generalize well to the kind of general that you would want, you'd want more
*  than just that reactivity that you get from just behavioral cloning slash supervised learning.
*  So a lot of the work, whether self play or even imitation learning would benefit significantly
*  from simulation from effective simulation. And you're doing a lot of stuff in the physical
*  world and in simulation. Do you have hope for greater and greater power of simulation loop
*  being boundless eventually to where most of what we need to operate in the physical world
*  could be simulated to a degree that's directly transferable to the physical world?
*  Are we still very far away from that?
*  So I think we could even rephrase that question in some sense, please.
*  So the power of simulation, right? As simulators get better and better, of course, becomes
*  stronger and we can learn more simulation. But there's also another version, which is where you
*  say the simulator doesn't even have to be that precise, as long as it's somewhat representative.
*  And instead of trying to get one simulator that is sufficiently precise to learn and transfer
*  really well to the real world, I'm going to build many simulators, ensemble of simulators,
*  not any single one of them is sufficiently representative of the real world, such that
*  it would work if you train in there. But if you train in all of them, then there is something
*  that's good in all of them. The real world will just be another one of them that's not identical
*  to any one of them, but just another one of them. Now this sample from the distribution of simulators.
*  We do live in a simulation, so this is just one other one. I'm not sure about that, but yeah.
*  It's definitely a very advanced simulator if it is. Yeah, it's a pretty good one. I've talked to
*  Russell. It's something you think about a little bit too. Of course, you're really trying to build
*  these systems, but do you think about the future of AI? A lot of people have concern about safety.
*  How do you think about AI safety as you build robots that are operating in the physical world?
*  How do you approach this problem in an engineering kind of way, in a systematic way?
*  So when a robot is doing things, you kind of have a few notions of safety to worry about. One is that
*  the robot is physically strong and of course could do a lot of damage. Same for cars,
*  which we can think of as robots do in some way. And this could be completely unintentional. So
*  it could be not the kind of long-term AI safety concerns that, okay, AI is smarter than us and
*  now what do we do? But it could be just very practical. Okay, this robot, if it makes a mistake,
*  what are the results going to be? Of course, simulation comes in a lot there to test in
*  simulation. It's a difficult question. And I'm always wondering, like I always wonder,
*  let's say you look at, let's go back to driving, because a lot of people know driving well, of
*  course. What do we do to test somebody for driving, right? To get a driver's license.
*  What do they really do? I mean, you fill out some tests and then you drive. And I mean,
*  for a few minutes. In suburban California, that driving test is just you drive around the block,
*  pull over, you do a stop sign successfully, and then you pull over again and you're pretty much
*  done. And you're like, okay, if a self-driving car did that, would you trust it that it can drive?
*  And I'd be like, no, that's not enough for me to trust it. But somehow for humans,
*  we've figured out that somebody being able to do that is representative of them being able to do
*  a lot of other things. And so I think somehow for humans, we figured out representative tests
*  of what it means if you can do this, what you can really do. Of course, testing humans, humans don't
*  want to be tested at all times. Self-driving cars or robots could be tested more often, probably.
*  You can have replicas that get tested and are known to be identical because they use the same
*  neural net and so forth. But still, I feel like we don't have this kind of unit tests or proper tests
*  for robots. And I think there's something very interesting to be thought about there,
*  especially as you update things. Your software improves, you have a better self-driving car suite,
*  you update it. How do you know it's indeed more capable on everything than what you had before,
*  that you didn't have any bad things creep into it? So I think that's a very interesting direction
*  of research that there is no real solution yet, except that somehow for humans we do.
*  Because we say, okay, you have a driving test, you passed, you can go on the road now. And humans
*  have accidents every like a million or 10 million miles, something pretty phenomenal
*  compared to that short test that is being done.
*  So let me ask, you've mentioned that Andrew Ng, by example, showed you the value of kindness.
*  Do you think the space of policies, good policies for humans and for AI is populated by policies
*  that with kindness or ones that are the opposite, exploitation, even evil? So if you just look at
*  the sea of policies we operate under as human beings, or if AI system had to operate in this
*  real world, do you think it's really easy to find policies that are full of kindness,
*  like we naturally fall into them? Or is it like a very hard optimization problem?
*  I mean, there is kind of two optimizations happening for humans, right? So for humans,
*  there's kind of the very long term optimization, which evolution has done for us, and we're kind
*  of predisposed to like certain things. And that's in some sense what makes our learning easier,
*  because I mean, we know things like pain, and hunger and thirst. And the fact that we know about
*  those is not something that we were taught. That's kind of innate. When we're hungry,
*  we're unhappy. When we're thirsty, we're unhappy. When we have pain, we're unhappy. And ultimately,
*  evolution built that into us to think about those things. And so I think there is a notion that
*  it seems somehow humans evolved in general to prefer to get along in some ways, but at the same
*  time also to be very territorial and kind of centric to their own tribe. And so I think that
*  their own tribe is like, it seems like that's the kind of space we converged onto. I mean,
*  I'm not an expert in anthropology, but it seems like we're very kind of
*  good within our own tribe, but need to be taught to be nice to other tribes.
*  Well, if you look at Steven Pinker, he highlights this pretty nicely in
*  Better Angels of Our Nature, where he talks about violence decreasing over time consistently. So
*  whatever tension, whatever teams we pick, it seems that the long arc of history goes towards
*  us getting along more and more. I hope so.
*  So do you think it's possible to teach RL-based robots this kind of kindness,
*  this kind of ability to interact with humans, this kind of policy? Let me ask a fun one.
*  Do you think it's possible to teach RL-based robot to love a human being
*  and to inspire that human to love the robot back? So to like a RL-based algorithm that leads to a
*  happy marriage? That's an interesting question. Maybe I'll answer it with another question, right?
*  Because I mean, it's a, but I'll come back to it. So another question you can have is, okay,
*  I mean, how close does some people's happiness get from interacting with just a really nice
*  dog? Like, I mean, dogs, you come home, that's what dogs do. They greet you. They're excited.
*  Makes you happy when you come home to your dog. You're just like, okay, this is exciting. They're
*  always happy when I'm here. I mean, if they don't greet you, because maybe whatever, your partner
*  took him on a trip or something, you might not be nearly as happy when you get home. Right? And so
*  the kind of, it seems like the level of reasoning a dog has is pretty sophisticated, but then it's
*  still not yet at the level of human reasoning. And so it seems like we don't even need to achieve
*  human level reasoning to get like very strong affection with humans. And so my thinking is,
*  why not, right? Why couldn't, with an AI, couldn't we achieve the kind of level of affection that
*  humans feel among each other or with friendly animals and so forth?
*  It's a question. Is it a good thing for us or not? That's another thing, right? Because I mean,
*  but I don't see why not.
*  Why not? Yeah. So Elon Musk says love is the answer. Maybe he should say
*  love is the objective function and then RL is the answer. Right?
*  Well, maybe.
*  Maybe.
*  Oh, Peter, thank you so much. I don't want to take up more of your time. Thank you so much for
*  talking today. Well, Lex, thanks for coming by. Great to have you visit.

---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 3337s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 6210
Video Rating: None
---

# BI 016 Ryota Kanai: Artificial Consciousness
**Brain Inspired:** [October 31, 2018](https://www.youtube.com/watch?v=h1qo_quPvrE)
*  So right now, there's no other theory that can tell us whether AI systems have consciousness
*  or not.
*  I know that I don't know what would happen if I were to press that button.
*  Don't press it, man.
*  Don't press it.
*  This is Brain Inspired.
*  Hello good people.
*  This is Paul Middlebrooks.
*  I mentioned last episode and I'll mention it again.
*  You can now support the show on Patreon.
*  You can access it through my website, braininspired.co, or go directly to patreon.com slash braininspired.
*  You can sign up for either $2 or $4 per month, which works out to about 50 cents or $1 per
*  episode respectively.
*  I don't plan to run ads, so your support is much appreciated.
*  A few people have signed up already and I can tell you I feel deep gratitude to you
*  guys.
*  So thank you.
*  So the other night I was laying awake in bed thinking of you guys and how to improve the
*  And I thought, hey, wouldn't it be great if in every show I included a joke about neuroscience
*  or AI?
*  A joke of the week, if you will.
*  So I searched for jokes of that ilk and lo and behold, I found basically nothing.
*  So I thought up a few jokes myself and against my better judgment, here is today's joke of
*  the show.
*  So there's this kid Jimmy and he really wants to go play soccer, but none of his friends
*  are available and he thinks, oh, I'll just teach my robot here, Samantha, how to play
*  and then we can play together.
*  So Samantha and Jimmy go to the soccer field and Jimmy says, here, Samantha, let me show
*  you how to kick the ball.
*  And he steps back and he winds up and he kicks the ball.
*  And Samantha says, oh, that's great.
*  Could you just show me one million other examples at a million different other angles and then
*  I'll be able to play.
*  Hey Al, where's that rim shot?
*  Thank you.
*  Okay, yeah, against my better judgment, like I said.
*  I'd love to hear your best neuroscience or AI jokes.
*  Send them to paul at braininspired.co or you can tweet to me.
*  I am at PGmid.
*  And believe me, I do have other jokes.
*  That one was just the one that elicited the tiniest snicker from my wife.
*  So send them to me, please.
*  Okay, one last piece of business here.
*  I will reiterate again, I really want to get more women on the show.
*  It's not for lack of trying.
*  I've been rejected multiple times, which is a familiar theme in my life.
*  But if you have suggestions for women that you would like to hear speak, I do have a
*  few lined up, but they're in the future.
*  So but yeah, send your suggestions to paul at braininspired.co, please.
*  Okay, I may be a poor judge of jokes and a poor writer of jokes.
*  But I am an excellent judge of character and an excellent judge, as you know, of podcast
*  guests.
*  Today's guest is Ryota Kanai.
*  And man oh man, I hope you guys are ready for this.
*  Ryota founded and runs a company called Aria.
*  We talk about Aria and how it morphed from a company that uses AI to analyze human brain
*  imaging to a company trying to understand how AI works and how the functions of consciousness
*  work.
*  So he has two goals here.
*  One is to implement the functions of consciousness.
*  And we discuss some of those functions and how this approach differs from implementing
*  the subjective, phenomenal aspect of consciousness, usually associated with the term.
*  And his second goal is to figure out how to measure whether a given system has consciousness.
*  To do this, Ryota for now is working with the only game in town, something called integrated
*  information theory, or IIT, which is an approach developed by Giulio Tononi, and in which you
*  calculate a number, phi, that is a measure of the degree of consciousness of a system.
*  We also talk about the historical course of how people have studied consciousness, the
*  possibility that general AI may actually require consciousness, which I believe is different
*  than the standard take.
*  We talk about reinforcement learning in general, and then how he and his team have implemented
*  curiosity and empowerment in a reinforcement learning AI agent.
*  So it would be intrinsically motivated to explore and exploit its environment.
*  He also shares how his thinking about consciousness has morphed over time.
*  He's gone through three phases thus far, and plenty more.
*  Without further ado, please enjoy our conversation.
*  Ryota Kanai, thank you for being on the podcast and welcome.
*  My pleasure.
*  So you have a background in brain imaging and brain stimulation and studying our visual
*  system and perception and time perception.
*  And most recently, you're in 2015, you founded and you're the CEO of Aria Inc.
*  You guys have a team of about 26, last I looked, if I counted, with three advisors.
*  And it seems like you're putting out just shy of 2 million papers per year these days.
*  So Aria does a variety of things.
*  And all of these things, when you read the mission, is to transform information to create
*  value for society.
*  But do you want to tell me a little bit more about the company?
*  Yeah, sure.
*  Yeah, so as you mentioned, my background is neuroscience and I was doing neuroimaging.
*  So initially when I founded this company, our focus was to combine machine learning
*  and neuroimaging.
*  And so before I founded this company, I was working at the University of Sussex in the
*  UK.
*  But then I realized in Japan, there's a lot of health checkups that involve neuroimaging.
*  So I wanted to access that huge data so that we can create value, especially in prediction
*  of future neurological disease and things like that.
*  But then we shifted our focus more towards AI.
*  Yeah, part of the reason is my real interest is in consciousness.
*  So I did research into the visual system and time perception in humans because I wanted
*  to understand how the brain generates consciousness.
*  And since we also had expertise in application of AI, so we wanted to also try to understand
*  consciousness in AI because we are very limited in terms of actual measurement technology
*  in neuroscience.
*  So if we use fMRI, we can only look at the whole brain, but with a very poor resolution,
*  or we can look at single neurons, but then we can't see the whole brain.
*  So if we use AI, we can see all the units and all the connectivity.
*  So then we thought perhaps we can start from understanding how AI works to understand potential
*  functions of consciousness.
*  So that's how we shifted our focus in the company.
*  But at the same time, we are a for-profit company, so we also deal with many commercial
*  projects, especially in collaboration with major companies in Japan.
*  Great.
*  And I should say that I'm speaking to you right now that the company is based in Tokyo
*  and you're in Tokyo.
*  It's 10 a.m. there.
*  It's 7 p.m. here.
*  So I got out of putting my kids to bed.
*  So this is great for me.
*  Thank you.
*  Good time.
*  So like you said, one of the goals is to create artificial consciousness, and you've been
*  interested in consciousness for a long time.
*  So we have a lot to talk about.
*  You're the first person where we're really going to focus on consciousness and the only
*  person where we're going to talk about creating artificial consciousness.
*  So Richard Feynman, the great physicist and teacher and thinker, his last words were,
*  this dying is boring to his sister.
*  And that has nothing to do with what we're about to talk about.
*  But he did have some things left on his blackboard as well.
*  And one of the last written statements that was on his blackboard when he died was, what
*  I cannot create, I do not understand.
*  So I think that that's a great segue into talking about this.
*  So in your words, what's the goal here and how do you define consciousness for this purpose?
*  Yeah, I'm also familiar with this quote and that's basically our spirit in trying to create
*  consciousness.
*  Although we are a for-profit company, we have deep interest in understanding what consciousness
*  is.
*  In the past 25 years or so, neuroscientists have tried to find neural correlates of consciousness.
*  And actually they're having a lot of progress and it was very useful to try to find what
*  kind of neural activities give rise to consciousness.
*  So in that sense, we have made a lot of progress.
*  But pro is the most important contribution from neuroscience or consciousness is to
*  make consciousness research science.
*  But on the other hand-
*  As opposed to philosophy, you mean?
*  Yeah, yeah, exactly.
*  So actually, a lot of people have skepticism about the possibility of studying consciousness
*  because sometimes it's associated with something spiritual or some people say consciousness
*  is not really defined.
*  But once we start thinking about how to create consciousness, we have to take consciousness
*  seriously and think about the potential benefit of having consciousness, especially in the
*  course of evolution.
*  For some reason, evolution came up with consciousness.
*  But the current AI doesn't seem to have any subjective experience.
*  Well, maybe we just don't know.
*  Yeah, but there's something fundamentally missing in our knowledge about the relationship
*  between intelligence and consciousness.
*  We are currently taking two approaches.
*  So one is, as I said, we want to understand potential functions of consciousness and implement
*  them to see whether we get any functional gain.
*  On the other hand, we also need to test whether consciousness is present inside any AI systems.
*  So basically, there are two goals.
*  So one is to create consciousness through functional implementation.
*  And the other one is to prove consciousness in AI systems.
*  So the second one is particularly difficult.
*  So we are mainly working on the first one.
*  But the second one is philosophically important.
*  And I don't think it's an impossible program.
*  I want to talk about both of those approaches.
*  But first, I really, I'm just curious how people in different fields have reacted to
*  your definitions of consciousness and your approaches and just in general, your goal
*  to create it.
*  So you have philosophers, you have neuroscientists, you have AI people.
*  I mean, has there been a lot of support, a lot of any outright hostility?
*  How's that gone from the different fields?
*  OK, yeah, it depends on the person I talked to.
*  But my focus on the function of consciousness doesn't seem to be satisfying to many people
*  because people interested in consciousness want to understand the subjective nature of consciousness.
*  The magic, yeah.
*  Yeah, it's sometimes called qualia.
*  So when we see some images, we have a particular experience generated internally.
*  Like when we see the color of red, it feels like red.
*  And so there's something like redness of red.
*  But then people understand why, like, spiking of neurons give rise to that kind of particular
*  sensation.
*  But if I say, maybe, the potential function of consciousness is to distinguish different
*  images or use that information for planning future action, then it's a functional description,
*  but doesn't really explain why subjective experience emerged.
*  So in that sense, it's not satisfying.
*  But on the other hand, AI researchers or roboticists often think consciousness is a trivial problem.
*  So actually, a lot of people, including philosophers, have thought about potential functions of
*  consciousness.
*  So in that sense, what I'm claiming is not necessarily completely new.
*  There are a lot of researchers who already worked on the concept of machine consciousness,
*  especially in the context of engineering.
*  But in the mainstream consciousness researchers, most of the focus has been on the so-called
*  phenomenal consciousness, which is the subjective aspect.
*  But my belief is we should pay more attention to the so-called access consciousness, which
*  is a functional aspect of consciousness.
*  Because we tend to think it's an easy problem, but it's still quite difficult.
*  And mainly the reason is a lot of cognitive functions are not well defined.
*  Because we cannot directly access other people's experience, so we don't know whether other
*  people feel read in the same way as I feel read.
*  And so in that sense, the subjective aspect is not really reachable.
*  But on the other hand, when we try to study consciousness in animals or babies, we make
*  inferences about consciousness in other beings.
*  And we do that through something we can objectively quantify or observe.
*  For example, there's a philosophical position called higher order thought theory, which
*  states that consciousness happens when the system has a meta representation of sensory
*  representation.
*  In other words, some sort of metacognition.
*  So we can talk about or we can measure the ability of metacognition in many different
*  systems, including other people.
*  So actually, we can just jump into it then, because metacognition, which is near and dear
*  to my heart.
*  I tried to study metacognition in monkeys in graduate school.
*  Oh, great.
*  Yeah.
*  And well, I just thought, what's the highest level cognitive process I can study in a monkey?
*  And that's what I came up with.
*  So anyway, that's one of the functions of consciousness you've listed throughout things
*  that I've read and seen in your talks.
*  So yeah, so that's a big one.
*  Yeah.
*  So we always have to study consciousness through some function we can observe externally.
*  And then that part is not even trivial.
*  So my position is before thinking about how to solve the hard problem, which is how subjective
*  experiences are generated from physical brains, we need to really understand what consciousness
*  is good for.
*  You know, it's interesting.
*  A typical criticism might be that we don't even understand consciousness, so we can't
*  build it.
*  We can't generate it.
*  And your response has been, exactly, we don't understand it, so we need to build it so that
*  we can understand it.
*  You have this great article on, I guess it's called Nautilus.
*  It's an online magazine.
*  And I just want to read the quote.
*  The article is called We Need Conscious Robots.
*  You say, debates on consciousness are often too philosophical and spin around in circles
*  without producing tangible results.
*  The small community of us who work on artificial consciousness aims to learn by doing.
*  So I think that's a really good summary of what you're doing here.
*  So we talked about metacognition, which is a representation of a representation of a
*  sensory or motor representation.
*  You want to just talk about some of the other functions of consciousness, potential functions?
*  Yeah.
*  So in cognitive neuroscience, we have encountered many tasks where consciousness seems to be
*  important.
*  But based on those observations, what we are thinking about the potential functions of
*  consciousness are the ability to generate information internally.
*  In other words, we first need to gain the so-called internal models of the world and
*  of the self and then use the model to generate potentially counterfactual situations.
*  So maybe this sounds very complicated, but the idea is we have something like a simulator
*  inside our mind and then use that for thinking about what might happen when we were to make
*  a particular action.
*  So maybe the simplest thing is I can imagine what I would see if I were to wave my hand
*  in front of my eyes.
*  But then I can imagine what that kind of sensory information is even without actually executing
*  the action.
*  But this is a very simple example, but I can also think about how to drive from one city
*  to another city by mentally simulating what kind of route I'm going to take and so on.
*  So that kind of mental simulation becomes possible once we can use our internal model
*  for many different purposes.
*  And this is particularly important when we consider the so-called artificial general
*  intelligence.
*  So the reason is once we have a model, we can use that model for many different purposes.
*  So when we have a mental map of our environment, then we can use the map to go to any place
*  on the map.
*  So that gives us some flexibility in terms of changing the goal.
*  But then we can also consider more abstract maps.
*  So for example, to solve some mathematical problems, we can think about many different
*  ways to approach that problem and then mentally simulate or actually execute calculation and
*  so on.
*  So having this kind of internal model or internal map is particularly useful.
*  And to my belief or my hypothesis is the function of consciousness is to use this kind of maps.
*  Yeah, it's interesting, Wint.
*  You just made me think of trying to solve hard problems.
*  And you're working on them really consciously, let's say, focusing on them.
*  And your map example made me think of this in a mathematical equation or something.
*  You're visualizing it and you can't, you beat your head up against the wall for half an
*  hour or an hour and finally you get up and you walk away and you don't think about it.
*  And so your subconscious works on it and then it pops into your mind all of a sudden.
*  What a beautiful model for that is just to have this internal generative model that's
*  exploring all these spaces and it's generating it and then you can just let it go because
*  it's generating it and passing that information on to your subconscious.
*  Do you want me to just spend the rest of our interview just talking about potential scenarios
*  for how this would work?
*  But it made me think of the interaction between conscious processes and subconscious processes
*  and the way that what you were just talking about could work in that fashion.
*  So I think that that's an interesting potential function of consciousness.
*  Yeah.
*  But what's missing in my hypothesis is how to draw the boundary between conscious and
*  unconscious processing.
*  So as you said, a lot of thinking happens without consciousness.
*  So there's something automatic.
*  So for example, in neuroscience, we know that not all the neural activities in the brain
*  contribute to consciousness, but we only have access to a part of it.
*  And yeah, so there's this huge problem, this boundary problem.
*  So how do we know which part of the brain activity contributes to consciousness and
*  where the boundary is?
*  So that's an unsolved problem.
*  And also, when I talk about this information generation hypothesis, I don't have a direct
*  answer to this.
*  So yeah, so in that sense, it's still a work in progress.
*  But I think we can get a lot of insights from another theory called integrated information
*  theory proposed by Giulio Tononi and his colleagues.
*  Yeah, well, you were talking about your two approaches, and one is to test whether something
*  is conscious.
*  This is one that you use frequently, right?
*  This is the main theory that you utilize when you're trying to test this.
*  Yeah.
*  So right now, this integrated information theory, or IIT, is the only theory that gives
*  us a measure of whether some intelligent systems have consciousness or not.
*  And nobody knows whether this theory is correct.
*  And there has been very little attempt to test this theory because it's computationally
*  very hard to actually measure the consciousness measure called phi.
*  Yeah, so the integrated information theory, its metric is called phi.
*  And I think that is that the main criticism of the theory is that mathematically, it is
*  either impossible or virtually impossible to solve it exactly?
*  Well, yeah, that's one of the criticisms.
*  But my impression is that people, well, a lot of criticisms are not really based on
*  good understanding of the theory.
*  But I think the theory of consciousness needs to be applicable to any system, including
*  AI.
*  So right now, there's no other theory that can tell us whether AI systems have consciousness
*  or not.
*  So in that sense, IIT is the only theory that gives us some idea or gives us some concrete
*  measure we can use to test consciousness in AI.
*  But at the same time, it's all hypothetical.
*  So we can measure phi of an AI and then claim, OK, this one has maybe 10 bits of consciousness
*  or something like that.
*  But we also need to test whether the theory is correct or not based on empirical data.
*  And people think it's impossible because it's computationally intractable.
*  But we are also developing more practical measures of phi so that we can actually compute
*  integrated information in the brain and in AI.
*  So like you said, I'm not really up to date with modern integrated information theory
*  and calculating phi.
*  But how many different versions are there?
*  Oh, there are many.
*  So roughly speaking, there are three different versions of IIT.
*  The first one is based on mutual information and it doesn't assume any dynamics of the
*  system.
*  And the second one is similar to the first one, but then it included dynamics of the
*  system.
*  So it was a major change.
*  And then the third one was a major update to the theory and started to involve many
*  new things like concepts and also the distinction between mechanism level and system level integration.
*  So the theory got a lot more difficult.
*  And I also heard they're working on a new version of IIT.
*  So there will be four different versions.
*  And mainly, we are currently working on IIT 2.0.
*  So we're trying to make IIT 2.0 computable.
*  But some concepts we're developing are applicable to IIT 3.0.
*  So we're making progress.
*  And yeah, but I think although IIT started from the context of neuroscience, of consciousness,
*  but that information theory itself seems to be useful in characterizing many different
*  complex systems.
*  Just giving them a number and different degrees.
*  Yeah.
*  So in principle, we can compute consciousness of the internet.
*  You had to do that.
*  I had to say consciousness of the internet.
*  Yeah, OK.
*  Yeah.
*  Yeah.
*  So that kind of thing is in principle possible and interesting to think about.
*  One of the consequences of sort of buying into IIT, integrated information theory, seems
*  to be also buying into panpsychism.
*  So panpsychism, and you can correct me if I'm wrong, is the belief that consciousness
*  lies on a gradient and is present to some degree in all things.
*  Do I have that right?
*  Yeah.
*  Yeah.
*  Yeah, that's right.
*  And you're a panpsychist.
*  Is that right?
*  Yeah, I must agree.
*  But I think panpsychism is a very natural philosophical position.
*  Because in terms of physical materials, there's nothing special about the brain.
*  What's important is the way neurons are configured and wired together, which somehow generate
*  consciousness.
*  But the important thing is the information in the brain rather than how that information
*  is supported by physical substrates.
*  So in that sense, it's natural to believe that consciousness can be implemented into
*  other non-organic materials.
*  In that sense, there's nothing special about the brain or biological systems, but the consciousness
*  can happen in any material.
*  So in that sense, I'm a panpsychist.
*  But we need to identify the necessary and sufficient condition.
*  And we also need to understand what it means to have information in our physical system.
*  Yeah.
*  Just as an aside here, speaking of necessary and sufficient, more long lines of sufficient,
*  I think I'd heard about this before, but I just recently heard about a case.
*  It's been around for a while.
*  There was a man who had hydrocephaly since his youth, and 90% of his brain was gone because
*  of the condition.
*  He's an adult, and he's fully functioning, fully conscious.
*  I don't know what his phi score is.
*  And his IQ was low, but he got along socially and could get along in society just fine.
*  And where is consciousness in the brain?
*  What does that mean when 90% of it is missing?
*  So it's just interesting to think about.
*  I don't know if you'd heard about him and or if you had thoughts about him.
*  Yeah.
*  I think it's probably a study by Marker.
*  And so basically, the patient had only the midbrain and without any neocortex.
*  There was no neocortex?
*  Well, I don't know the exact composition.
*  There might be still some left, but the main point is there was very little brain preserved.
*  So then this observation led some people to think that we may not need the cortex to have
*  consciousness and also used as an argument for the potential presence of consciousness
*  in insects.
*  Right.
*  So in a way, when we think about consciousness across many different species, maybe we shouldn't
*  think that the neocortex is the only place where consciousness happens.
*  We may have many different levels of consciousness.
*  And so a lot of times, lower part of the brain, like brainstem, is much more necessary to
*  support consciousness.
*  It may not contribute to the content of consciousness.
*  But of course, when we think about consciousness in flies, they don't have neocortex, but they
*  have very sophisticated systems.
*  So, yeah, it's interesting to think about.
*  Well, OK, so most people, when they think of consciousness in AI, they think of first
*  creating general AI and then either creating consciousness on top of that, or some people
*  think that consciousness will just emerge once we successfully implement general AI.
*  So do you think we can have consciousness without general AI?
*  That's an interesting question.
*  I guess the standard view is that we don't need consciousness to create general AI.
*  Right.
*  But I want to challenge this notion because, as I said, we have a functional gain from
*  the ability to generate information internally, such as flexibility to change goals on the
*  fly once we have internal models.
*  So if my conjecture is correct and consciousness happens whenever some information is generated,
*  internally, then general intelligence may require that kind of function because it allows
*  the agent to use the knowledge for many different purposes.
*  So I see some potential commonalities between the ability to generate the information and
*  the ability to adapt to different goals flexibly in general AI.
*  So maybe in that sense, consciousness is a requirement for general AI.
*  I hope we find out soon enough.
*  In your broad estimation, how far along are you in your project here to replicate functions
*  of consciousness in artificial systems and solving the ability to measure it?
*  And how far along are you?
*  And what is your outlook?
*  When is it going to happen?
*  Yeah, I hope it will happen soon.
*  But I think what will happen in reality will be a very slow progress.
*  So maybe it may not be us, but some people may create consciousness without knowing that
*  they actually created consciousness.
*  But for example, if we manage to create a very primitive level of consciousness, like
*  maybe insect level consciousness, we may not know whether it's real consciousness or not.
*  And I think at some point, people will start accepting consciousness in machines once they
*  start interacting with autonomous robots.
*  For example, like Sony has a pet robot called Eyeball, which has the shape of a dog.
*  And people already have a lot of attachment to that kind of robot agent.
*  I guess they are still unconscious.
*  But at some point, particularly if they are free autonomous and use some sort of internal
*  model of the environment and have the model of the agent itself, they will have all the
*  key functions of consciousness.
*  And people will start feeling consciousness in those agents.
*  So it's purely from an external viewpoint.
*  Yeah.
*  So as I said, there are two aspects.
*  One is to create consciousness and the other one is to prove the existence of consciousness.
*  But the second one is hard and maybe it's more cultural.
*  It's very hard to get the exact answer whether other animals or other people are conscious.
*  Even for humans, it's really difficult to prove that other people have consciousness.
*  As you're speaking, I was just imagining a future paper from you entitled, Stop Swatting
*  Flies, about how we've discovered consciousness in flies.
*  Let's say we do.
*  Let's say there's a measure we discover and we feel confident that there's a measure of
*  consciousness in flies, let's say.
*  Will we feel more guilty swatting them, for instance?
*  Well, probably not.
*  I think some people already think other animals have consciousness, but we still eat them.
*  Sure.
*  Yeah.
*  So on the other hand, right now, people don't attribute consciousness to machines.
*  But by some point, maybe we will start treating AIs as though they were animals.
*  Yeah.
*  I think that'll come sooner rather than later, I think.
*  How about we spend a few minutes?
*  These have been pretty broad and this has been really fun for me, talking about the
*  broad topics of consciousness.
*  You want to spend just a few minutes talking about one of your recent papers that's come
*  out?
*  This paper is called, A Unified Strategy for Implementing Curiosity in Empowerment-Driven
*  Reinforcement Learning.
*  This is really, we're going to keep it high level, but this is the nuts and bolts of what
*  you're doing here.
*  We actually haven't talked about reinforcement learning much at all on the show.
*  I hate to do this to you, but in the broadest terms, can you say what reinforcement learning
*  is?
*  Yeah, sure.
*  Reinforcement learning is a study of how to train an agent, it could be animal or AI,
*  to learn how it should interact with the environment to maximize their achievement in certain
*  goals.
*  Most of the time, it's based on some reverse function given externally.
*  For example, maybe the famous example is DeepMinds DQN, which solved many Atari games.
*  There the goal is to maximize the scores.
*  We can use reinforcement learning to train an agent to maximize some scores or some gain
*  in games or in reality.
*  But recently, people have been training intrinsic motivation in these reinforcement learning
*  agents.
*  What does that mean and what did you guys do in the paper here?
*  Intrinsic motivation is to have an internal reward rather than external reward to train
*  agents.
*  In particular, we focus on information as motivation.
*  Here we took two types of intrinsic motivation.
*  One is curiosity and the other one is empowerment.
*  Curiosity is very useful.
*  Let me talk about current limitation of reinforcement learning first.
*  There are many limitations, but the main problem of reinforcement learning is that basically
*  the agent tries all kinds of things to get some point.
*  Once it gets a point, then it learns to repeat the actions that led to that reward.
*  In reality, rewards are very rare and also delayed.
*  In a complex environment, it's very difficult to try everything out until you get the reward.
*  I don't think people would pay you to do all the random things.
*  I don't know.
*  I'm pretty good at it.
*  In that sense, we needed to find more efficient way to train agents.
*  Curiosity is one way to train agents when there aren't many rewards.
*  The way to do it is we use information gain as an intrinsic motivation.
*  Whenever you discover something new about the environment or whenever you improve your
*  internal model, you get the reward.
*  It's similar to curiosity in humans.
*  When we encounter a situation where we don't have enough information, we want to understand
*  the situation by gaining new information.
*  I don't know.
*  It's hard to come up with a good example, but if there's some sort of mysterious button
*  on the wall, we want to push it.
*  That's curiosity.
*  Also, I think humans are strongly motivated by curiosity.
*  This says, I have trouble focusing on my work because there are a lot of interesting tweets.
*  A lot of times, the titles of news media make you curious and want to click.
*  People are intrinsically motivated to gain new information.
*  In the same way, we can use this incentive to train agents because that facilitates exploration
*  of the environment, which is important.
*  Once we have a good internal model, as I said, we can use the internal model to solve many
*  different problems.
*  Even when there's no clear definition of what the right thing to do, it's generally good
*  to understand the current situation better so that we can use the understanding of the
*  situation to solve problems that happen in the future.
*  That's curiosity.
*  Empowerment is a different kind of intrinsic motivation.
*  It's the incentive to maximize the possibility of your future.
*  For example, when you are in a room, you don't know where the next position you have to be
*  in the room.
*  But in that situation, you want to be in the center of the room because you can reach anywhere
*  very quickly.
*  You want to be in a state or a well-prepared state where you can reach anywhere.
*  But also, maybe the reason why people want to have money is to maximize this empowerment.
*  When you have more money, you can use it for many different purposes.
*  That way, you can maximize future possibilities.
*  That's a different kind of intrinsic motivation.
*  What's common between these is that these are not defined externally.
*  But when there's no clear rewarding goals, it's beneficial for the agent to maximize
*  all these quantities.
*  In this paper, what we did was we formulated curiosity and empowerment in terms of information
*  flow.
*  Basically, what we did was define curiosity as information flow from the environment to
*  the agent.
*  The agent wants to maximize the amount of information coming from the environment so
*  it can learn more quickly.
*  Empowerment is the opposite information flow from the agent to the environment.
*  By maximizing this, what it means is that whenever the agent takes an action, then
*  the consequences are more predictable for the agent.
*  It's a little bit like a complicated concept.
*  But the point is, by maximizing this information flow, the agent has more control over the
*  environment.
*  We unified these strategies in terms of information flow and implemented them into deep neural
*  networks so that the agent can...
*  Basically, the model part is the reinforcement of deep learning.
*  It's deep learning with reinforcement learning rewards driving the learning process?
*  Yeah, exactly.
*  Reinforcement learning has many standard algorithms.
*  We use standard reinforcement learning algorithm, but the reward came from information flow
*  from outside to inside or from inside to outside.
*  Got you.
*  If this agent that had the two types of intrinsic motivation, if it were a human, would it be
*  someone who prefers learning things that are hard to learn or mastering skills that are
*  difficult to master and yet obtaining as much money as possible through doing these things?
*  Yeah, exactly.
*  Something like that.
*  If AIs are motivated that way, I think they will become eventually very strong.
*  We are interested in intrinsic motivation because intrinsic motivation is a way to implement
*  autonomy.
*  We want to have AI agents that find goals themselves without us telling them what to
*  do.
*  I think that kind of autonomy is another interesting aspect of consciousness.
*  Also, to implement intrinsic motivation, the agent needs to have the ability to imagine
*  what would happen in the future.
*  For example, without the ability to evaluate its own prediction.
*  For example, about this mysterious button on the wall, I know that I don't know what
*  would happen if I were to press that button.
*  Don't press it, man.
*  Don't press it.
*  That's kind of a meta-representation based on evaluation of an internal model.
*  That's the situation where information generation becomes relevant.
*  This motivation is also related to works by Carl Christon, who proposes the free energy
*  principle because he talks about minimizing uncertainty in the future through using internal
*  models.
*  He talks about counterfactual predictions and things like that.
*  The motivation comes from the consideration of what the brain might be doing and how this
*  ability to predict what might happen next seems to be highly important for function
*  consciousness.
*  I'm internally curious and now I will externalize that curiosity.
*  The terms that are being used, curiosity, empowerment, is this the Wild West of AI terminology?
*  If I write a paper, can I make up a new term and ascribe it a function, an equation, and
*  an optimization, but give it what's historically been a human label like curiosity and empowerment?
*  There are many different terms for this.
*  I know there are a lot of standard terms already.
*  These are used.
*  They are not something we just came up with.
*  This is interesting work.
*  I had to pick one paper to really talk about because you guys are working on so many different
*  fronts all along these same lines.
*  It's really fascinating stuff and I'll link to stuff in the show notes here.
*  Did we miss anything on the paper?
*  We are not completely satisfied with the paper because it was still very theoretical and just
*  a presentation of the idea that we can formulate these things in terms of information flow
*  and possibly implementing to neural networks.
*  But to really prove the power of this approach, we want to also show this in a larger scale
*  project.
*  For example, implementing this into robots or drones so that we can observe the behavior
*  of such agents in a more complex environment.
*  Do you guys have stuff like that in the pipeline, in the works?
*  We recently got a grant to work on drones.
*  We want to create curious drones.
*  I don't know how to control them but that will be interesting.
*  Don't press the button.
*  Maybe you should press the button.
*  I'm not sure yet.
*  We have just a few more minutes left and I appreciate you hanging on and being so generous
*  with your time.
*  I have some more general questions if you don't mind and then we'll just wrap up.
*  It seems to me in what I observed in my science career that the active practice of science
*  seems to lead people over time to sort of start studying the lower level questions.
*  You go in with a big question and then you realize we don't know the answer to that
*  and we also don't know the answer to the things that would support that function and then
*  you study lower and lower questions.
*  I'm curious how that was a goal of mine was to try to stay as high level as possible.
*  I'm just wondering how you've managed to stay focused on the big question, consciousness.
*  I see.
*  It's been very difficult to focus on the big question because there are always low-hanging
*  frills.
*  And resistance from colleagues as well, correct?
*  Yeah, that's true.
*  I have to confess that I also worked on many sort of irrelevant projects.
*  But whenever I divert from my original interest, I tend to get depressed and I get sick.
*  So I know I need to work on consciousness.
*  On the other hand, it's very frustrating that I cannot make much progress as much as I want.
*  I can claim that I'm interested in consciousness.
*  We work on consciousness.
*  But we are working on a very small part of consciousness.
*  I wish I could make much more progress more quickly.
*  So your curiosity is going wild here, but your empowerment is not optimized.
*  Yeah, something like that.
*  I admire that you keep at it.
*  That's what I tried to do as well.
*  Of course, then I quit and moved into an RV.
*  It didn't work out for me.
*  I'm curious how your views on consciousness have changed since beginning to think about it.
*  I remember reading Neurophilosophy by Patricia Churchland and coming at it from a
*  philosophical standpoint and then getting interested in the neuroscience.
*  Have you been steadfast throughout with the same view or did you used to have a different view of consciousness?
*  Yeah, I think I changed my views on consciousness quite a lot.
*  Maybe there are three different phases.
*  I got interested in consciousness because it's a big problem for science.
*  I was reading Charmer's Conscious Mind when I was an undergrad.
*  I thought all the neuroscience is completely useless.
*  Nobody is really addressing the heart problem in consciousness.
*  But at the same time, I think a lot of my colleagues working on neuroscience consciousness
*  are interested in the quality problem.
*  But then I encountered Tononi's Integrated Information Theory
*  and I thought it gave us some remedy for the heart problem.
*  But also it got me interested in information in physics.
*  Because if I take the theory seriously, any system that has integrated information
*  could have consciousness.
*  But then I need to understand what information is in terms of physics.
*  So that's an interesting area.
*  That was my second stage.
*  I still retain that viewpoint.
*  But more recent view I got was the importance of functions of consciousness.
*  I think that has been dismissed in the field.
*  For example, I didn't like Daniel Dennett's position of consciousness.
*  I quite like what he calls the question of consciousness,
*  which is the question of what you gain by having conscious perception.
*  So the potential functional consequences of consciousness,
*  which is not very well known.
*  In a way, to make more tangible progress in consciousness research,
*  I feel like we need to really understand a more functional side of consciousness.
*  So that's my current position.
*  I'm trying to work on it by trying to create consciousness in AI.
*  That's great.
*  So you said you walked down a few different roads that didn't bear fruit.
*  What's something that you either failed at
*  or an idea that you were just wrong about?
*  How did that affect you moving forward?
*  You have to choose one.
*  For me, there are too many.
*  I wish I worked on animals as well.
*  I took subjective experience maybe too seriously.
*  So I started with human psychophysics.
*  But I think facts are very important.
*  We don't gain new facts by observing human behaviour that much.
*  Of course, that's important.
*  But I think we need to do a lot more observation in the brain
*  with more cutting-edge technologies.
*  So maybe in my career choice,
*  I feel I should have studied animal consciousness.
*  Maybe I can do that next,
*  but I have to at least try to solve something
*  in what I'm trying to do now.
*  So maybe that's my next career.
*  I think you picked a good time to do it.
*  My advice would be to not do the animal research yourself
*  but have other people do it because it takes so long.
*  Yeah, I agree.
*  I mentioned earlier, and this is just a fun question,
*  but you inspired me to think about working on a problem
*  and then walking away from it,
*  and then the solution comes to you later.
*  What's one way that when you're feeling stuck on a problem,
*  how do you get unstuck?
*  Do you have a method?
*  Do you have any methods?
*  Yeah, that's an interesting question.
*  I don't feel I get stuck often.
*  Maybe to me, a bigger problem is to find time
*  to continuously work on the problem.
*  Yeah, yeah.
*  Yeah, usually I don't get stuck,
*  but maybe some projects have lower priority
*  and I just can't find enough time to work on them.
*  Well, you're always getting interrupted by interviewers
*  wanting to interview you.
*  So my last question here, Ryota, is how do you see red?
*  No, I'm just kidding.
*  A little hard.
*  Where should people find out more about what you do?
*  You're on Twitter.
*  Yeah, you can find me on Twitter.
*  That's Kanair.
*  You could also check our website.
*  It's ariya.org, where we put our publication list.
*  So you can find some of the work we are working on.
*  And yeah, like many of our members go to a conference
*  called ASSC, which is Consciousness Conference.
*  Or you can just visit us in Tokyo.
*  Oh, great.
*  I really appreciate the time, Ryota,
*  and thank you and much luck to you.
*  This has been fun for me.
*  Yeah, thank you.

---
Date Generated: April 11, 2024
Transcription Model: whisper medium 20231117
Length: 9910s
Video Keywords: ['agi', 'ai', 'ai podcast', 'artificial intelligence', 'artificial intelligence podcast', 'facebook', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'machine learning', 'meta', 'mit ai', 'neural network', 'nyu', 'reinforcement learning', 'self supervised learning', 'yann lecun']
Video Views: 441265
Video Rating: None
---

# Yann LeCun: Dark Matter of Intelligence and Self-Supervised Learning | Lex Fridman Podcast #258
**Lex Fridman:** [January 22, 2022](https://www.youtube.com/watch?v=SGzMElJ11Cc)
*  The following is a conversation with Jan Lakoon, his second time on the podcast.
*  He is the chief AI scientist at Metta, formerly Facebook,
*  professor at NYU, touring award winner,
*  one of the seminal figures in the history of machine
*  learning and artificial intelligence, and someone who is brilliant
*  and opinionated in the best kind of way.
*  And so it's always fun to talk to.
*  This is a Lex Friedman podcast to support it.
*  Please check out our sponsors in the description.
*  And now here's my conversation with Jan Lakoon.
*  You co-wrote the article Self-Supervised Learning,
*  the Dark Matter of Intelligence. Great title, by the way, with Ishan Misra.
*  So let me ask, what is self-supervised learning
*  and why is it the dark matter of intelligence?
*  I'll start by the dark matter part.
*  There is obviously a kind of learning that humans and animals are
*  doing that we currently are not reproducing properly with machines or with AI.
*  So the most popular approaches to machine learning today are
*  or paradigms, I should say, are supervised learning and reinforcement learning.
*  And they are extremely inefficient.
*  Supervised learning requires many samples for learning anything.
*  And reinforcement learning requires a ridiculously large number of trial
*  and errors to for a system to learn anything.
*  And that's why we don't have self-driving cars.
*  That's a big leap from one to the other.
*  OK, so that to solve difficult problems,
*  you have to have a lot of human annotation for supervised learning to work
*  and to solve those difficult problems with reinforcement learning.
*  You have to have some way to maybe simulate that problem
*  such that you can do that large scale kind of learning that reinforcement
*  learning requires. Right.
*  So how is it that, you know, most teenagers can learn to drive a car
*  in about 20 hours of practice,
*  whereas even with millions of hours of simulated practice,
*  self-driving car can't actually learn to drive itself properly.
*  And so obviously we're missing something, right.
*  And it's quite obvious for a lot of people that, you know,
*  the immediate response you get from many people is, well, you know,
*  humans use their background knowledge to learn faster.
*  And they're right.
*  Now, how was that background knowledge acquired?
*  And that's the big question.
*  So now you have to ask, you know, how do babies in the first few months of life
*  learn how the world works, mostly by observation,
*  because they can hardly act in the world.
*  And they learn an enormous amount of background knowledge about the world.
*  That may be the the basis of what we call common sense.
*  This type of learning is not learning a task.
*  It's not being reinforced for anything.
*  It's just observing the world and figuring out how it works.
*  Building world models, learning world models.
*  How do we do this and how do we reproduce this in machines?
*  So self-supervised learning is, you know, one instance
*  or one attempt at trying to reproduce this kind of learning.
*  OK, so you're looking at just observation.
*  So not even the interacting part of a child.
*  It's just sitting there watching mom and dad walk around, pick up stuff, all that.
*  That's that's what we mean about background knowledge.
*  Perhaps not even watching mom and dad, just, you know, watching the world go by.
*  Just having eyes open or having eyes closed or the very act of opening
*  and closing eyes that the world appears and disappears.
*  All that basic information.
*  And you're saying in order to learn to drive,
*  like the reason humans are able to learn to drive quickly,
*  some faster than others, is because of the background knowledge
*  they were able to watch cars operate in the world
*  in the many years leading up to it, the physics of basic objects and all that.
*  That's right. I mean, the basic physics of objects, you don't even know.
*  You don't even need to know, you know, how a car works, right?
*  Because that you can learn fairly quickly.
*  I mean, the example I use very often is you're driving next to a cliff
*  and you know in advance because of your, you know, understanding of
*  intuitive physics that if you turn the wheel to the right,
*  the car will veer to the right, will run off the cliff, fall off the cliff
*  and nothing good will come out of this. Right.
*  But if you are a sort of, you know, tabularized reinforcement
*  learning system that doesn't have a model of the world,
*  you have to repeat falling off this cliff
*  thousands of times before you figure out it's a bad idea.
*  And then a few more thousand times before you figure out how to not do it.
*  And then a few more million times before you figure out how to not do it
*  in every situation you ever encounter.
*  So self-supervised learning still has to have some source of truth
*  being told to it by somebody.
*  So you have to figure out a way without human assistance
*  or without significant amount of human assistance to get that truth from the world.
*  So the mystery there is how much signal is there,
*  how much truth is there that the world gives you, whether it's the human world,
*  like you watch YouTube or something like that, or it's the more natural world.
*  So how much signal is there?
*  So here's the trick.
*  There is way more signal in sort of a self-supervised setting
*  than there is in either a supervised or reinforcement setting.
*  And this is going to my analogy of the cake.
*  The, you know, the cake has someone that's called it,
*  where when you try to figure out how much information
*  you ask the machine to predict and how much feedback
*  you give the machine at every trial in reinforcement learning,
*  you give the machine a single scalar, you tell the machine you did good, you did bad.
*  And you only tell this to the machine once in a while.
*  When I say you, it could be the universe telling the machine, right?
*  But it's just one scalar.
*  So as a consequence, you cannot possibly learn something very complicated
*  without many, many, many trials where you get many, many feedbacks of this type.
*  Supervised learning, you give a few bits to the machine at every sample.
*  Let's say you're training a system on recognizing images on ImageNet.
*  There is 1,000 categories.
*  That's a little less than 10 bits of information per sample.
*  But self-supervised learning here is a setting.
*  Ideally, we don't know how to do this yet,
*  but ideally you would show a machine a segment of video
*  and then stop the video and ask the machine to predict what's going to happen next.
*  So you let the machine predict and then you let time go by
*  and show the machine what actually happened
*  and hope the machine will learn to do a better job at predicting next time around.
*  There's a huge amount of information you give the machine
*  because it's an entire video clip of the future
*  after the video clip you fed it in the first place.
*  So both for language and for vision,
*  there's a subtle, seemingly trivial construction,
*  but maybe that's representative of what is required to create intelligence,
*  which is filling the gap.
*  Filling the gaps.
*  It sounds dumb, but it is possible you can solve all of intelligence in this way.
*  Just for both language, just give a sentence and continue it,
*  or give a sentence and continue it.
*  Or give a sentence and there's a gap in it,
*  some words blanked out and you fill in what words go there.
*  For vision, you give a sequence of images
*  and predict what's going to happen next,
*  or you fill in what happened in between.
*  Do you think it's possible that formulation alone
*  as a signal for self-supervised learning can solve intelligence for vision and language?
*  I think that's our best shot at the moment.
*  So whether this will take us all the way to human-level intelligence or something,
*  or just cat-level intelligence is not clear,
*  but among all the possible approaches that people have proposed,
*  I think it's our best shot.
*  So I think this idea of an intelligent system filling in the blanks,
*  either predicting the future, inferring the past, filling in missing information.
*  I'm currently filling the blank of what is behind your head
*  and what your head looks like from the back,
*  because I have basic knowledge about how humans are made.
*  And I don't know what you're going to say at which point you're going to speak,
*  whether you're going to move your head this way or that way,
*  which way you're going to look,
*  but I know you're not going to just dematerialize and reappear at three meters down the hall,
*  because I know what's possible and what's impossible according to intuitive physics.
*  You have a model of what's possible and what's impossible,
*  and you'd be very surprised if it happens, then you'll have to reconstruct your model.
*  Right. So that's the model of the world.
*  It's what tells you what fills in the blanks.
*  So given your partial information about the state of the world,
*  given by your perception, your model of the world fills in the missing information,
*  and that includes predicting the future,
*  re-predicting the past, filling in things you don't immediately perceive.
*  And that doesn't have to be purely generic vision or visual information or generic language.
*  You can go to specifics like predicting what control decision you make when you're driving in a lane.
*  You have a sequence of images from a vehicle and then you have information,
*  if you recorded on video, where the car ended up going.
*  So you can go back in time and predict where the car went based on the visual information.
*  That's very specific, domain specific.
*  Right. But the question is whether we can come up with sort of a generic method
*  for training machines to do this kind of prediction of filling in the blanks.
*  So right now, this type of approach has been unbelievably successful in the context of natural language processing.
*  Every modern natural language processing is pre-trained in self-supervised manner to fill in the blanks.
*  You show it a sequence of words, you remove 10% of them,
*  and then you train some gigantic neural net to predict the words that are missing.
*  And once you've pre-trained that network, you can use the internal representation learned by it
*  as input to something that you train supervised or whatever.
*  That's been incredibly successful. Not so successful in images, although it's making progress.
*  And it's based on sort of manual data augmentation.
*  We can go into this later. But what has not been successful yet
*  is training for video. So getting a machine to learn to represent the visual world, for example,
*  by just watching video. Nobody has really succeeded in doing this.
*  OK, well, let's kind of give a high level overview.
*  What's the difference in kind and in difficulty between vision and language?
*  So you said people haven't been able to really kind of crack the problem of vision open in terms of self-supervised learning.
*  But that may not be necessarily because it's fundamentally more difficult.
*  Maybe like when we're talking about achieving, like passing the Turing test in the full spirit of the Turing test in language
*  might be harder than vision. That's not obvious.
*  So in your view, which is harder or perhaps are they just the same problem?
*  When the farther we get to solving each, the more we realize it's all the same thing.
*  It's all the same cake.
*  I think what I'm looking for are methods that make them look essentially like the same cake, but currently they're not.
*  And the main issue with learning world models or learning predictive models is that the prediction is never a single thing
*  because the world is not entirely predictable. It may be deterministic or stochastic.
*  We can get into the philosophical discussion about it. But even if it's deterministic, it's not entirely predictable.
*  And so if I play a short video clip and then I ask you to predict what's going to happen next, there's many, many plausible continuations for that video clip.
*  And the number of continuation grows with the interval of time that you're asking the system to make a prediction for.
*  And so one big question with self-supervised learning is how you represent this uncertainty, how you represent multiple discrete outcomes,
*  how you represent a sort of continuum of possible outcomes, et cetera.
*  And if you are sort of a classical machine learning person, you say, oh, you just represent a distribution.
*  And that we know how to do when we're predicting words, missing words in the text, because you can have a neural net give a score for every word in the dictionary.
*  It's a big list of numbers, maybe 100,000 or so.
*  You can turn them into a probability distribution that tells you when I say a sentence, the cat is chasing the blank in the kitchen.
*  There are only a few words that make sense there. It could be mouse, it could be a lizard spot or something like that.
*  And if I say the blank is chasing the blank in the savanna, you also have a bunch of plausible options for those two words.
*  Because you have kind of an underlying reality that you can refer to to sort of fill in those blanks.
*  So you cannot say for sure in the savanna if it's a lion or a cheetah or whatever, you cannot know if it's a zebra or a goo or whatever.
*  Well, the beast, the same thing.
*  But you can represent the uncertainty by just a long list of numbers.
*  Now, if I do the same thing with video and I ask you to predict a video clip, it's not a discrete set of potential frames.
*  You have to have somewhere representing an infinite number of plausible continuations of multiple frames in a high dimensional continuous space.
*  And we just have no idea how to do this properly.
*  Finite high dimensional.
*  So like you...
*  It's finite high dimensional, yes.
*  Just like the words, they try to get it to down to a small finite set of like under a million, something like that.
*  Something like that.
*  I mean, it's kind of ridiculous that we're doing a distribution of every single possible word for language and it works.
*  It feels like that's a really dumb way to do it.
*  Like there seems to be like there should be some more compressed representation of the distribution of the words.
*  You're right about that.
*  And so, do you have any interesting ideas about how to represent all the reality in a compressed way such that you can form a distribution over it?
*  That's one of the big questions.
*  You know, how do you do that?
*  I mean, what's kind of, you know, another thing that really is stupid about, I shouldn't say stupid, but like simplistic about current approaches to self-supervised learning in NLP in text is that not only do you represent a giant distribution over words,
*  but for multiple words that are missing, those distributions are essentially independent of each other.
*  And, you know, you don't pay too much price for this.
*  So you can't.
*  So, you know, the system, you know, in the sentence that I gave earlier, if it gives a certain probability for a lion and cheetah and then a certain probability for, you know, gazelle, wildebeest and zebra,
*  those two probabilities are independent of each other.
*  And it's not the case that those things are independent.
*  Lions actually attack like bigger animals than cheetahs.
*  So, you know, there is a huge independence hypothesis in this process, which is not actually true.
*  The reason for this is that we don't know how to represent properly distributions over combinatorial sequences of symbols, essentially, because the number grows exponentially with the length of the symbols.
*  And so we have to use tricks for this.
*  But those techniques can, you know, get around, like don't even deal with it.
*  So so the big question is, like, would there be some sort of abstract latent representation of text that would say that, you know, when I when I switch lion for gazelle lion for cheetah, I also have to switch zebra for gazelle.
*  Yes, so this independence assumption, let me throw some criticism at you that I often hear and see how you respond.
*  So this kind of filling in the blanks is just statistics.
*  You're not learning anything like the deep underlying concepts.
*  You're just mimicking stuff from the past.
*  You're not learning anything new such that you can use it to generalize about the world.
*  Or OK, let me just say the crude version, which is is just statistics.
*  It's not intelligence. What do you have to say to that?
*  What do you usually say to that? If you kind of hear this kind of thing?
*  I don't get into those discussions because they are kind of pointless.
*  So, first of all, it's quite possible that intelligence is just statistics.
*  It's just statistics of a particular kind.
*  Yes, where is the philosophical question?
*  This is kind of is is it possible that intelligence is just statistics?
*  Yeah. But what kind of statistics?
*  So if you are asking the question, are the models of the world that we learn, do they have some notion of causality?
*  Yes. So if the criticism comes from people who say, you know,
*  current machine learning systems don't care about causality, which by the way is wrong, you know, I agree with them.
*  Yeah, you should, you know, your model of the world should have your actions as one of the inputs
*  and that will drive you to learn causal models of the world where you know what intervention in the world will cause what result.
*  Or you can do this by observation of other agents acting in the world and observing the effect, other humans, for example.
*  So I think, you know, at some level of description, intelligence is just statistics.
*  But that doesn't mean you don't, you know, you won't have models that have, you know, deep mechanistic explanation for what goes on.
*  The question is, how do you learn them?
*  That's the question I'm interested in.
*  Because, you know, a lot of people who actually voice their criticism say that those mechanistic model has to have to come from someplace else.
*  They have to come from human designers.
*  They have to come from I don't know what.
*  And obviously we learn them.
*  Or if we don't learn them as an individual, nature learn them for us using evolution.
*  So regardless of what you think, those processes have been learned somehow.
*  So if you look at the human brain, just like when we humans introspect about how the brain works,
*  it seems like when we think about what is intelligence, we think about the high level stuff like the models we've constructed,
*  like cognitive science, the concepts of memory and reasoning module, almost like these high level modules.
*  Is there is this serve as a good analogy?
*  Like, are we ignoring the dark matter, the basic low level mechanisms, just like we ignore the way the operating system works,
*  we're just using the the high level software.
*  We're ignoring that at the low level, the neural network might be doing something like statistics like me.
*  Sorry to use this word probably incorrectly and crudely, but doing this kind of fill in the gap kind of learning and just kind of updating the model constantly
*  in order to be able to support the raw sensory information, to predict it and adjust to the prediction when it's wrong.
*  But like when we look at our brain at the high level, it feels like we're doing like we're playing chess.
*  Like we're like playing with high level concepts and we're stitching them together.
*  We're putting them into long term memory.
*  But really what's going underneath is something we're not able to introspect,
*  which is this kind of simple, large neural network that's just filling in the gaps.
*  Right. Well, OK, so there's a lot of questions that are answers there.
*  OK, so first of all, there's a whole school of thought in neuroscience, competition neuroscience in particular,
*  that likes the idea of predictive coding, which is really related to the idea I was talking about in self-supervised learning.
*  So everything is about prediction.
*  The essence of intelligence is the ability to predict and everything the brain does is trying to predict everything from everything else.
*  OK, and that's really sort of the underlying principle, if you want, that self-supervised learning is trying to kind of reproduce this idea of prediction.
*  That's kind of an essential mechanism of task independent learning, if you want.
*  The next step is what kind of intelligence are you interested in reproducing?
*  And of course, you know, we all think about, you know, trying to reproduce sort of high level cognitive processes in humans.
*  But like with machines, we're not even at the level of even reproducing the learning processes in a cat brain.
*  The most intelligent or intelligent systems don't have as much common sense as a house cat.
*  So how is it that cats learn? And, you know, cats don't do a whole lot of reasoning.
*  They certainly have causal models.
*  They certainly have, because, you know, many cats can figure out how they can act on the world to get what they want.
*  They certainly have a fantastic model of intuitive physics, certainly of the dynamics of their own bodies, but also of praise and things like that.
*  So they're pretty smart. They only do this with about 800 million neurons.
*  We are not anywhere close to reproducing this kind of thing.
*  So to some extent, I could say, let's not even worry about the high level cognition and kind of long term planning and reasoning that humans can do until we figure out, like, you know, can we even reproduce what cats are doing?
*  Now, that said, this ability to learn world models, I think, is the key to the possibility of learning machines that can also reason.
*  So whenever I give a talk, I say there are three challenges in the three main challenges in machine learning.
*  The first one is, you know, getting machines to learn to represent the world and proposing self-supervised learning.
*  The second is getting machines to reason in ways that are compatible with essentially gradient based learning, because this is what deep learning is all about, really.
*  And the third one is something we have no idea how to solve, at least I have no idea how to solve, is can we get machines to learn hierarchical representations of action plans?
*  You know, like, you know, we know how to train them to learn hierarchical representations of perception, you know, with computational nets and things like that and transformers.
*  But what about action plans? Can we get them to spontaneously learn good hierarchical representations of actions?
*  Also gradient based.
*  Yeah, all of that, you know, needs to be somewhat differentiable so that you can apply sort of gradient based learning, which is really what deep learning is about.
*  So it's background, knowledge, ability to reason in a way that's differentiable, that is somehow connected, deeply integrated with that background knowledge or builds on top of that background knowledge.
*  And then given that background knowledge, be able to make hierarchical plans in the world.
*  So if you take classical optimal control, there's something in classical optimal control called model predictive control.
*  And it's been around since the early 60s.
*  NASA uses that to compute trajectories of rockets.
*  And the basic idea is that you have a predictive model of the rocket, let's say, or whatever system you intend to control, which, given the state of the system at time t and given an action that you're taking the system.
*  So for a rocket to be thrust and all the controls you can have, it gives you the state of the system at time t plus delta t.
*  So basically differential equation, something like that.
*  And if you have this model and you have this model in the form of some sort of neural net or some sort of set of formula that you can back propagate gradient through, you can do what's called model predictive control or gradient based model predictive control.
*  So you can unroll that model in time.
*  You feed it a hypothesized sequence of actions.
*  And then you have some objective function that measures how well at the end of the trajectory the system has succeeded or matched what you want it to do.
*  Is it a robot harm?
*  Have you grasped the object you want to grasp?
*  If it's a rocket, are you at the right place near the space station?
*  Things like that.
*  And by back propagation through time, and again, this was invented in the 1960s by optimal control theorists, you can figure out what is the optimal sequence of actions that will get my system to the best final state.
*  So that's a form of reasoning.
*  It's basically planning and a lot of planning systems in robotics are actually based on this.
*  And you can think of this as a form of reasoning.
*  So, you know, to take the example of the teenager driving a car again, you have a pretty good dynamical model of the car.
*  It doesn't need to be very accurate.
*  But, you know, again, that if you turn the wheel to the right and there is a cliff, you're going to run off the cliff.
*  Right. You don't need to have a very accurate model to predict that.
*  And you can run this in your mind and decide not to do it for that reason, because you can predict in advance that the result is going to be bad.
*  So you can sort of imagine different scenarios and and then, you know, employ or take the first step in the scenario that is most favorable and then repeat the process of planning.
*  That's called receding horizon model predictive control.
*  So even all those things have names going back decades.
*  And so if you're not the classical optimal control, the model of the world is not generally learned.
*  This sometimes a few parameters you have to identify that's called systems identification.
*  But but generally, the model is mostly deterministic and mostly built by hand.
*  So the big question of AI, I think the big challenge of AI for the next decade is how do we get machines to learn predictive models of the world that deal with uncertainty and deal with the real world in all this complexity?
*  So it's not just the trajectory of a rocket, which you can reduce to first principles.
*  It's not it's not even just a trajectory of a robot arm, which again, you can model by careful mathematics.
*  But it's everything else, everything we observe in the world, you know, people, behavior, you know, physical systems that involve collective phenomena like water or or, you know, trees and branches in a tree or something or or complex things that humans have no trouble developing abstract representations and predictive model for.
*  But we still don't know how to do with machines.
*  Where do you put in in these three, maybe in the in the planning stages?
*  The game theoretic nature of this world where your actions not only respond to the dynamic nature of the world, the environment, but also affect it.
*  So if there's other humans involved, is this is this point number four or is it somehow integrated into the hierarchical representation of action in your view?
*  It's not that it's not always integrated.
*  It's just it's just that now your model of the world has to deal with, you know, it just makes it more complicated.
*  The fact that humans are complicated and not easily predictable, that makes your model of the world much more complicated, that much more complicated.
*  Well, there's a chess.
*  I mean, I suppose chess is an analogy.
*  So multi-carotid research.
*  I go, you go, I go, you go like a undercut pot.
*  They recently gave a talk at MIT about car doors.
*  I think there's so much she learning to but mostly car doors.
*  And there's a dynamic nature to the car, like the person opening the door checking.
*  And he wasn't talking about that.
*  He was talking about the perception problem of what the ontology of what defines a car door.
*  This big philosophical question.
*  But to me, it was interesting because like it's obvious that the person opening the car doors, they're trying to get out like here in New York, trying to get out of the car.
*  You slowing down is going to signal something.
*  You speeding up is going to signal something.
*  That's a dance.
*  It's a asynchronous chess game.
*  I don't know.
*  So it feels like it's not just I mean, I guess you can integrate all of them to one giant model like the entirety of the.
*  These little interactions because it's not as complicated as chess.
*  It's just like a little dance.
*  We do like a little dance together and then we figure it out.
*  Well, in some ways, it's way more complicated than chess because because it's continuous.
*  It's uncertain in a continuous manner.
*  It doesn't feel more complicated, but it's more complicated because that's what we're we've evolved to solve this kind of problem.
*  We've evolved to solve.
*  And so we're good at it because, you know, nature has made us good at it.
*  Nature has not made us good at chess.
*  We completely suck at chess.
*  In fact, that's why we designed it as a game is to be challenging.
*  And if there is something that, you know, recent progress in chess and go has made us realize is that humans are really terrible at those things, like really bad.
*  You know, there was a story right before AlphaGo that, you know, the best go players thought there were maybe two or three stones behind, you know, an ideal player that they would call God.
*  In fact, no, they are like nine or ten stones behind.
*  I mean, we're just bad.
*  So we're not good at it's because we have limited working memory.
*  We know we're not very good at doing this tree exploration that, you know, computers are much better at doing than we are.
*  But we are much better at learning differentiable models to the world.
*  I mean, I said differentiable in the kind of, you know, I should say not differentiable in the sense that, you know, we went back up through it.
*  But in the sense that our brain has some mechanism for estimating gradients of some kind.
*  Yeah. And that's what makes us efficient.
*  So if you have an agent that consists of a model of the world, which, you know, in the human brain is basically the entire front half of your brain, an objective function, which in humans is a combination of two things.
*  There is your sort of intrinsic motivation module, which is on the basis of ganglia, you know, on the basis of your brain.
*  That's the thing that measures pain and hunger and things like that, like immediate feelings and emotions.
*  And then there is, you know, the equivalent of what people in Reference Metronome call a critic, which is a sort of module that predicts ahead what the outcome of a situation will be.
*  And so it's not a cost function, but it's sort of not an objective function, but it's sort of a, you know, trained predictor of the ultimate objective function.
*  And that also is differentiable. And so if all of this is differentiable, your cost function, your critic, your, you know, your world model, then you can use gradient based type methods to do planning, to do reasoning, to do learning, you know, to do all the things that we'd like an intelligent agent to do.
*  And the gradient based learning, like what's your intuition? That's probably at the core of what can solve intelligence.
*  So you don't need like a logic based reasoning in your view.
*  I don't know how to make logic based reasoning compatible with efficient learning.
*  Yeah.
*  And OK, I mean, there is a big question, perhaps a philosophical question.
*  I mean, it's not that philosophical, but that we can ask is that, you know, all the learning algorithms we know from engineering and computer science proceed by optimizing some objective function.
*  Yeah.
*  Right. So one question we may ask is, does learning in the brain minimize an objective function?
*  I mean, it could be a, you know, a composite of multiple objective functions, but it's still an objective function.
*  Second, if it does optimize an objective function, does it do it by some sort of gradient estimation?
*  You know, it doesn't need to be backdrop, but some way of estimating the gradient in an efficient manner, whose complexity is on the same order of magnitude as, you know, actually running the inference.
*  Because you can't afford to do things like, you know, perturbing a weight in your brain to figure out what the effect is.
*  And then sort of, you know, you can do sort of estimating gradient by perturbation.
*  To me, it seems very implausible that the brain uses some sort of, you know, zero-thorough order black box gradient free optimization, because it's so much less efficient than gradient optimization.
*  So it has to have a way of estimating gradient.
*  Is it possible that some kind of logic-based reasoning emerges in pockets as a useful, like you said, if the brain is an objective function, maybe it's a mechanism for creating objective functions.
*  It's a mechanism for creating knowledge bases, for example, that can then be queried.
*  Like, maybe it's like an efficient representation of knowledge that's learned in a gradient-based way or something like that.
*  Well, so I think there is a lot of different types of intelligence.
*  So first of all, I think the type of logical reasoning that we think about, that we are, you know, maybe stemming from, you know, sort of classical AI of the 1970s and 80s.
*  I think humans use that relatively rarely and are not particularly good at it.
*  But we judge each other based on our ability to solve those rare problems.
*  It's called an IQ test.
*  I don't think so.
*  Like, I'm not very good at chess.
*  Yes.
*  I'm judging you this whole time because, well, we actually...
*  With your, you know, heritage, I'm sure you're good at chess.
*  No, stereotypes.
*  Not all stereotypes are true.
*  Well, I'm terrible at chess.
*  So, you know, but I think perhaps another type of intelligence that I have is this, you know, ability of sort of building models to the world from, you know, reasoning, obviously, but also data.
*  And those models generally are more kind of analogical, right?
*  So it's reasoning by simulation and by analogy, where you use one model to apply to a new situation.
*  Even though you've never seen that situation, you can sort of connect it to a situation you've encountered before.
*  And your reasoning is more, you know, akin to some sort of internal simulation.
*  So you're kind of simulating what's happening when you're building, I don't know, a box out of wood or something, right?
*  You can imagine in advance what would be the result of cutting the wood in this particular way.
*  Are you going to use screws or nails or whatever?
*  When you are interacting with someone, you also have a model of that person and sort of interact with that person, you know, having this model in mind to kind of tell the person what you think is useful to them.
*  So I think this ability to construct models of the world is basically the essence of intelligence and the ability to use it then to plan actions that will fulfill a particular criterion, of course, is necessary as well.
*  So I'm going to ask you a series of impossible questions as we keep asking, as I've been doing.
*  So if that's the fundamental sort of dark matter of intelligence, this ability to form a background model, what's your intuition about how much knowledge is required?
*  You know, I think dark matter, you can put a percentage on it of the composition of the universe and how much of it is dark matter, how much of it is dark energy, how much information do you think is required to be a house cat?
*  So you have to be able to, when you see a box go in it, when you see a human compute the most evil action, if there's a thing that's near an edge, you knock it off.
*  All of that, plus the extra stuff you mentioned, which is a great self-awareness of the physics of your of your own body and the world.
*  How much knowledge is required, do you think, to solve it?
*  I don't even know how to measure an answer to that question.
*  I'm not sure how to measure it, but whatever it is, it fits in about about 800,000 neurons, 800 million neurons.
*  The representation does?
*  Everything, all knowledge, everything, right?
*  It's less than a billion. A dog is two billion, but a cat is less than one billion.
*  And so multiply that by a thousand and you get the number of synapses.
*  And I think almost all of it is learned through this, you know, a sort of self-supervised learning, although, you know, I think a tiny sliver is learned through reinforcement learning and certainly very little through, you know, classical supervised running, although it's not even clear how supervised learning actually works in the biological world.
*  So I think almost all of it is self-supervised learning, but it's driven by the sort of ingrained objective functions that a cat or human have at the base of their brain, which kind of drives their behavior.
*  So, you know, nature tells us you're hungry.
*  It doesn't tell us how to feed ourselves. That's something that the rest of our brain has to figure out, right?
*  Well, it's interesting because there might be more like deeper objective functions that are lying the whole thing.
*  So hunger may be some kind of, now you go to like neurobiology, it might be just the brain trying to maintain homeostasis.
*  So hunger is just one of the human perceivable symptoms of the brain being unhappy with the way things are currently.
*  It could be just like one really dumb objective function at the core.
*  But that's how behavior is driven.
*  The fact that the orbezo ganglia drive us to do things that are different from, say, an orangutong or certainly a cat is what makes human nature versus orangutong nature versus cat nature.
*  So, for example, you know, our orbezo ganglia drives us to seek the company of other humans.
*  And that's because nature has figured out that we need to be social animals for our species to survive.
*  And it's true of many primates.
*  It's not true of orangutongs. Orangutongs are solitary animals.
*  They don't seek the company of others. In fact, they avoid them.
*  In fact, they scream at them when they come too close because they're territorial.
*  Because for their survival, evolution has figured out that's the best thing.
*  I mean, they are occasionally socially, of course, for reproduction and stuff like that.
*  But they're mostly solitary. So all of those behaviors are not part of intelligence.
*  People say, oh, you're never going to have intelligent machines because human intelligence is social.
*  But then you look at orangutongs, you look at octopus.
*  Octopus never know their parents.
*  They barely interact with any other.
*  And they get to be really smart in less than a year, in like half a year.
*  You know, in a year they're adults. In two years they're dead.
*  So there are things that we think as humans are intimately linked with intelligence, like social interaction, like language.
*  I think we give way too much importance to language as a substrate of intelligence as humans.
*  Because we think our reasoning is so linked with language.
*  So to solve the house cat intelligence problem, you think you could do it on a desert island.
*  You could have a cat sitting there looking at the waves, at the ocean waves, and figure a lot of it out.
*  It needs to have sort of the right set of drives to kind of get it to do the thing and learn the appropriate things.
*  But for example, you know, baby humans are driven to learn to stand up and walk.
*  This desire is hardwired. How to do it precisely is not. That's learned.
*  But the desire to walk, move around and stand up, that's sort of hardwired.
*  It's very simple to hardwire this kind of stuff.
*  Oh, like the desire to. Well, that's interesting. You're hardwired to want to walk.
*  That's not a, there's got to be a deeper need for walking.
*  I think it was probably socially imposed by society that you need to walk all the other bipedal.
*  No, like a lot of simple animals that, you know, would probably walk without ever watching any other members of the species.
*  It seems like a scary thing to have to do because you suck it bipedal walking at first.
*  It seems crawling is much safer, much more like why are you in a hurry?
*  Well, because you have this thing that drives you to do it, you know, which is sort of part of the sort of human development.
*  Is that understood actually what? Not entirely. No. What is the reason to get on two feet?
*  It's really hard. Like most animals don't get on two feet.
*  Well, they get on four feet. You know, many mammals get on four feet very quickly.
*  Some of them extremely quickly. But I don't, you know, like from the last time I've interacted with a table,
*  that's much more stable than a thing than two legs. It's just a really hard problem.
*  Yeah. I mean, birds have figured it out with two feet.
*  Well, technically we can go into ontology. They have four. I guess they have two feet.
*  I mean, they have two feet. Chickens, you know, dinosaurs have two feet, many of them.
*  Allegedly. I'm just now learning that T-Rex was eating grass, not other animals. T-Rex might have been a friendly pet.
*  What do you think about, I don't know if you looked at the test for general intelligence that Francois Chalet put together.
*  I don't know if you got a chance to look at that kind of thing.
*  What's your intuition about how to solve like an IQ type of test?
*  I don't know. I think it's so outside of my radar screen that it's not really relevant, I think, in the short term.
*  I guess one way to ask, another way, perhaps more closer to what, to your work is like,
*  how do you solve MNIST with very little example data?
*  That's right. And that's the answer to this probably is self-supervised learning.
*  Just learn to represent images and then learning to recognize handwritten digits on top of this will only require a few samples.
*  And we observe this in humans, right? You show a young child a picture book with a couple of pictures of an elephant and that's it.
*  The child knows what an elephant is.
*  And we see this today with practical systems that we train image recognition systems with enormous amounts of images,
*  either completely self-supervised or very weakly supervised.
*  For example, you can train a neural net to predict whatever hashtag people type on Instagram, right?
*  And you can do this with billions of images because there's billions per day that are showing up.
*  So the amount of training data there is essentially unlimited.
*  And then you take the output representation, you know, a couple of layers down from the output of what the system learned
*  and feed this as input to a classifier for any object in the world that you want.
*  And it works pretty well. So that's transfer learning.
*  OK, or weakly supervised transfer learning.
*  People are making very, very fast progress using self-supervised learning for this kind of scenario as well.
*  And, you know, my guess is that that's that's going to be the future for self-supervised learning.
*  How much cleaning do you think is needed for filtering malicious signal or what's a better term?
*  But like a lot of people use hashtags on Instagram to get like good SEO that doesn't fully represent the contents of the image.
*  Like they'll put a picture of a cat and hashtag it with like science. Awesome. Fun.
*  I don't know. All. Why would you put science?
*  That's not very good SEO.
*  The way my colleagues who worked on this project at at Facebook now, Meta, Meta AI, a few years ago dealt with this is that they only selected something
*  like 17000 tags that correspond to kind of physical things or situations like, you know, that has some visual content.
*  So, you know, you wouldn't have like hashed TBT or anything like that.
*  Also, they keep a very select set of hashtags.
*  Yeah. OK. But it's still in the order of, you know, 10 to 20 thousand.
*  So it's fairly large. OK.
*  Can you tell me about data augmentation?
*  What the heck is data augmentation and how is it used?
*  Maybe contrast of learning for for video.
*  What are some cool ideas here?
*  Right. So data augmentation.
*  I mean, first, data augmentation, you know, is the idea of artificially increasing the size of your training set by distorting the images that you have in ways that don't change the nature of the image.
*  Right. So you take you do you do endless.
*  You can do data augmentation on endless.
*  And people have done this since 1990s.
*  Right. You take a in this digit and you shift it a little bit or you change the size or rotate it, skew it, you know, etc.
*  Add noise.
*  Add noise, etc. And it it works better if you train a supervised classifier with augmented data, you're going to get better results.
*  Now, it's become really interesting over the last couple of years because a lot of self-supervised learning techniques to pre-train vision systems are based on data augmentation.
*  And the the basic techniques is originally inspired by techniques that I worked on in the early 90s and Jeff Hinton worked on also in the early 90s.
*  There was a parallel work I used to call this Siamese Network.
*  So basically, you take two identical copies of the same network, they share the same weights, and you show two different views of the same object.
*  Either those two different views may have been obtained by data augmentation or maybe it's two different views of the same scene from a camera that you moved or at different times or something like that.
*  Right. Or two pictures of the same person, things like that.
*  And then you train this neural net, those two identical copies of this neural net, to produce an output representation, a vector in such a way that the representation for those two images are as close to each other as possible.
*  As identical to each other as possible.
*  Because you want the system to basically learn a function that will be invariant, that will not change, whose output will not change when you transform those inputs in those particular ways.
*  So that's easy to do.
*  What's complicated is how do you make sure that when you show two images that are different, the system will produce different things?
*  Because if you don't, you can't do that.
*  When you show two images that are different, the system will produce different things.
*  Because if you don't have a specific provision for this, the system will just ignore the inputs.
*  When you train it, it will end up ignoring the input and just produce a constant vector that is the same for every input.
*  That's called a collapse.
*  Now, how do you avoid collapse?
*  So there's two ideas.
*  There's one idea that I proposed in the early 90s with my colleagues at Bell Labs, Jane Bromley and a couple other people, which we now call contrastive learning, which is to have negative examples.
*  So you have pairs of images that you know are different, and you show them to the network and those two copies, and then you push the two output vectors away from each other.
*  And it will eventually guarantee that things that are semantically similar produce similar representations and things that are different produce different representations.
*  We actually came up with this idea for a project of doing signature verification.
*  So we would collect signatures from multiple signatures on the same person and then train a neural net to produce the same representation and then force the system to produce different representation from different signatures.
*  This was actually the problem was proposed by people from what was a subsidiary of AT&T at the time called NCR.
*  And they were interested in storing representation of the signature on the 80 bytes of the magnetic strip of a credit card.
*  So we came up with this idea of having a neural net with 80 outputs that we would quantize on bytes so that we could encode the signature.
*  And that encoding was then used to compare whether the signature matches or not.
*  That's right.
*  And then you would sign, it would run through a neural net, and then you would compare the output vector to whatever is stored on your card.
*  Did it actually work?
*  It worked, but they ended up not using it.
*  Because nobody cares actually.
*  I mean, the American financial payment system is incredibly lax in that respect compared to Europe.
*  Oh, with the signatures? What's the purpose of signatures anyway?
*  Nobody looks at them. Nobody cares.
*  Yeah.
*  So that's contrastive learning, right?
*  So you need positive and negative pairs.
*  And the problem with that is that even though I had the original paper on this, I'm actually not very positive about it because it doesn't work in high dimension.
*  If your representation is high dimensional, there's just too many ways for two things to be different.
*  And so you would need lots and lots and lots of negative pairs.
*  So there is a particular implementation of this, which is relatively recent, from actually the Google Toronto group, where Jeff Hinton is the senior member there.
*  It's called SIEMCLR, S-I-M-C-L-R.
*  And it's basically a particular way of implementing this idea of contrastive learning, the particular objective function.
*  Now, what I'm much more enthusiastic about these days is non-contrastive methods.
*  So other ways to guarantee that the representations would be different for different inputs.
*  And it's actually based on an idea that Jeff Hinton proposed in the early 90s with his student at the time, Sue Becker.
*  And it's based on the idea of maximizing the mutual information between the outputs of the two systems.
*  You only show positive pairs. You only show pairs of images that you know are somewhat similar.
*  And you train the two networks to be informative, but also to be as informative of each other as possible.
*  So basically, one representation has to be predictable from the other, essentially.
*  And he proposed that idea, had a couple of papers in the early 90s, and then nothing was done about it for decades.
*  And I kind of revived this idea together with my postdocs at FAIR, particularly a postdoc called Stephane Denis,
*  who is now a junior professor in Finland at University of Aalto.
*  We came up with something that we called Barlow Twins.
*  And it's a particular way of maximizing the information content of a vector using some hypotheses.
*  And we have kind of another version of it that's more recent now called V-CREG, V-I-C-E-R-E-G.
*  That means variance, invariance, covariance, regularization.
*  And it's the thing I'm the most excited about in machine learning in the last 15 years.
*  I mean, I'm really, really excited about this.
*  What kind of data augmentation is useful for that non-contrastive learning method?
*  Are we talking about, does that not matter that much?
*  Or it seems like a very important part of the step.
*  Yeah.
*  How you generate the images that are similar but sufficiently different.
*  Yeah, that's right. It's an important step, and it's also an annoying step,
*  because you need to have that knowledge of what data augmentation you can do that do not change the nature of the object.
*  And so the standard scenario, which a lot of people working in this area are using, is you use the type of distortion.
*  So basically you do a geometric distortion.
*  So one basically just shifts the image a little bit. It's called cropping.
*  Another one kind of changes the scale a little bit. Another one kind of rotates it.
*  Another one changes the colors. You know, you can do a shift in color balance or something like that.
*  Saturation. Another one sort of blurs it. Another one adds noise.
*  So you have like a catalog of kind of standard things, and people try to use the same ones for different algorithms so that they can compare.
*  But some algorithms, some self-supervised algorithms actually can deal with much bigger, more aggressive data augmentation, and some don't.
*  So that kind of makes the whole thing difficult.
*  But that's the kind of distortions we're talking about.
*  And so you train with those distortions, and then you chop off the last layer, a couple layers of the network,
*  and you use the representation as input to a classifier. You train the classifier on ImageNet, let's say, or whatever, and measure the performance.
*  And interestingly enough, the methods that are really good at eliminating the information that is irrelevant, which is the distortions between those images,
*  do a good job at eliminating it. And as a consequence, you cannot use the representations in those systems for things like object detection and localization, because that information is gone.
*  So the type of data augmentation you need to do depends on the task you want eventually the system to solve.
*  And the type of data augmentation, standard data augmentation that we use today, are only appropriate for object recognition or image classification.
*  They're not appropriate for things like...
*  Can you help me out understand why localization is not... So you're saying it's just not good at the negative, like at classifying the negative, so that's why it can't be used for the localization?
*  No, it's just that you train the system, you give it an image, and then you give it the same image shifted and scaled, and you tell it that's the same image.
*  So the system basically is trained to eliminate the information about position and size. So now you want to use that to figure out where an object is and what size it is.
*  Like a bounding box, it could still find the object in the image, it's just not very good at finding the exact boundaries of that object. Interesting.
*  Interesting. Which, you know, that's an interesting sort of philosophical question. How important is object localization anyway?
*  We're like obsessed by measuring, like image segmentation, obsessed by measuring perfectly knowing the boundaries of objects when arguably that's not that essential to understanding what are the contents of the scene.
*  On the other hand, I think evolutionarily, the first vision systems in animals were basically all about localization, very little about recognition.
*  And in the human brain, you have two separate pathways for recognizing the nature of a scene or an object and localizing objects.
*  So you use the first pathway called the ventral pathway for telling what you're looking at.
*  The other path with the dorsal pathway is used for navigation, for grasping, for everything else.
*  And basically a lot of the things you need for survival are localization and detection.
*  Is similarity learning or contrastive learning, are these non-contrastive methods the same as understanding something?
*  Just because you know a distorted cat is the same as a non-distorted cat, does that mean you understand what it means to be a cat?
*  To some extent. I mean, it's a superficial understanding, obviously.
*  But like, what is the ceiling of this method, do you think? Is this just one trick on the path to doing self-supervised learning?
*  Or can we go really, really far?
*  I think we can go really far. So if we figure out how to use techniques of that type, perhaps very different, but of the same nature,
*  to train a system from video to do video prediction, essentially, I think we'll have a path towards, I wouldn't say unlimited,
*  but a path towards some level of physical common sense in machines.
*  And I also think that that ability to learn how the world works from a sort of high throughput channel like vision is a necessary step towards sort of real artificial intelligence.
*  In other words, I believe in ground-in intelligence. I don't think we can train a machine to be intelligent purely from text.
*  Because I think the amount of information about the world that's contained in text is tiny compared to what we need to know.
*  So for example, people have attempted to do this for 30 years, the psych project and things like that,
*  of basically kind of writing down all the facts that are known and hoping that some sort of common sense will emerge.
*  I think it's basically hopeless. But let me take an example. You take an object. I describe a situation to you.
*  I take an object, I put it on the table, and I push the table. It's completely obvious to you that the object will be pushed with the table, right?
*  Because it's sitting on it. There is no text in the world, I believe, that explains this.
*  And so if you train a machine as powerful as it could be, you know, your GPT 5000 or whatever it is, it's never going to learn about this.
*  That information is just not present in any text.
*  Well, the question, like with the psych project, the dream, I think, is to have like 10 million, say, facts like that, that give you a head start, like a parent guiding you.
*  Now, we humans don't need a parent to tell us that the table will move, sorry, the smartphone will move with the table.
*  But we get a lot of guidance in other ways. So it's possible that we can give it a quick shortcut.
*  What about a cat? A cat knows that.
*  No, but they evolved. So...
*  No, they learned like us.
*  Sorry, the physics of stuff?
*  Yeah.
*  Well, yeah, so you're saying it's...
*  So you're putting a lot of intelligence onto the nurture side, not the nature.
*  Yes.
*  We seem to have, you know, there's a very inefficient, arguably, process of evolution that got us from bacteria to who we are today.
*  Started at the bottom, now we're here.
*  True.
*  The question is how fundamental is that, the nature of the whole hardware?
*  And then is there any way to shortcut it if it's fundamental?
*  If it's not, if it's most of intelligence, most of the cool stuff we've been talking about is mostly nurture, mostly trained.
*  We figure it out by observing the world.
*  We can form that big, beautiful, sexy background model that you're talking about just by sitting there.
*  Then, okay, then you need to...
*  Then like maybe it is all supervised learning all the way down.
*  Self-supervised learning, say.
*  Whatever it is that makes human intelligence different from other animals, which a lot of people think is language and logical reasoning and this kind of stuff.
*  It cannot be that complicated because it only popped up in the last million years.
*  Yeah.
*  It only involves less than 1% of our genome, which is the difference between human genome and chimps or whatever.
*  It can be that complicated.
*  It can be that fundamental.
*  Most of the complicated stuff already exists in cats and dogs and certainly primates, non-human primates.
*  Yeah, that little thing with humans might be just something about social interaction and ability to maintain ideas across a collective of people.
*  It sounds very dramatic and very impressive, but it probably isn't mechanistically speaking.
*  It is, but we're not there yet.
*  We have...
*  I mean, this is number 634 in the list of problems we have to solve.
*  So basic physics of the world is number one.
*  What do you...
*  Just a quick tangent on data augmentation.
*  So a lot of it is hard-coded versus learned.
*  Do you have any intuition that maybe there could be some weird data augmentation, like generative type of data augmentation, like doing something weird to images, which then improves the similarity learning process?
*  So not just kind of dumb, simple distortions, but by you shaking your head, just saying that even simple distortions are enough?
*  I think no.
*  I think data augmentation is a temporary necessary evil.
*  So what people are working on now is two things.
*  One is the type of self-supervised learning, like trying to translate the type of self-supervised learning people use in language, translating these two images, which is basically a denoising autoencoder method.
*  So you take an image, you block, you mask some parts of it, and then you train some giant neural net to reconstruct the parts that are missing.
*  And until very recently, there was no working methods for that.
*  All the autoencoder type methods for images weren't producing very good representation.
*  But there's a paper now coming out of the FAIR group at Immanuel Park that actually works very well.
*  So that doesn't require data augmentation, that requires only masking.
*  Only masking for images?
*  Right. So you mask a part of the image and you train a system, which in this case is a transformer because the transformer represents the image as non-overlapping patches.
*  So it's easy to mask patches and things like that.
*  Okay, then my question transfers to that problem, the masking.
*  Why should the mask be a square or a rectangle?
*  So it doesn't matter. I think we're going to come up probably in the future with ways to mask that are kind of random, essentially.
*  I mean, they are random already.
*  No, no, but something that's challenging, optimally challenging.
*  So maybe it's a metaphor that doesn't apply, but it seems like there's a data augmentation or masking.
*  There's an interactive element with it.
*  You're almost like playing with an image.
*  And it's like the way we play with an image in our minds.
*  No, but it's like dropout. It's like both machine training.
*  Every time you see a percept, you can perturb it in some way.
*  And then the principle of the training procedure is to minimize the difference of the output or the representation between the clean version and the corrupted version, essentially.
*  And you can do this in real time.
*  So most of the machines work like this.
*  You show a percept, you tell the machine that's a good combination of activities or your input neurons.
*  And then you either let them go their merry way without clamping them to values or you only do this with a subset.
*  And what you're doing is you're training the system so that the stable state of the entire network is the same, regardless of whether it sees the entire input or whether it sees only part of it.
*  You know, the Nozio-Otoe encoder method is basically the same thing, right?
*  You're training a system to reproduce the input, the complete input and filling the blanks, regardless of which parts are missing.
*  And that's really the underlying principle.
*  And you could imagine sort of even in the brain, some sort of neural principle where neurons kind of oscillate, right?
*  So they take their activity and then temporarily they kind of shut off to force the rest of the system to basically reconstruct the input without their help.
*  And you can imagine more or less biologically possible processes.
*  Something like that.
*  And I guess with this denoising auto encoder and masking and data augmentation, you don't have to worry about being super efficient.
*  You can just do as much as you want and get better over time.
*  Because I was thinking like you might want to be clever about the way you do all these procedures, you know, but that's only it's somehow costly to do every iteration, but it's not really.
*  Not really.
*  Maybe.
*  And then there is, you know, data augmentation without explicit data augmentation.
*  This data augmentation by weighting, which is, you know, the sort of video prediction.
*  You're observing a video clip, observing the, you know, the continuation of that video clip.
*  You try to learn a representation using the joint embedding architectures in such a way that the representation of the future clip is easily predictable from the representation of the observed clip.
*  Do you think YouTube has enough raw data from which to learn how to be a cat?
*  I think so.
*  So the amount of data is not the constraint.
*  No, it would require some selection, I think.
*  Some selection of, you know, maybe the right type of data.
*  You need to put on the rabbit hole of just cat videos that might you might need to watch some lectures or something.
*  No, you wouldn't.
*  How meta would that be if it like watches lectures about intelligence and then learns, watches your lectures and NYU and learns from that how to be intelligent?
*  I don't think there would be enough.
*  What's your, do you find multimodal learning interesting?
*  We've been talking about visual language, like combining those together, maybe audio, all those kinds of things.
*  There's a lot of things that I find interesting in the short term, but are not addressing the important problem that I think are really kind of the big challenges.
*  So I think, you know, things like multitask learning, continual learning, you know, adversarial issues.
*  I mean, those have great practical interests in the relatively short term, possibly.
*  But I don't think they're fundamental.
*  You know, active learning, even to some extent, reinforcement learning.
*  I think those things will become either obsolete or useless or easy once we figured out how to do self-supervised representation learning or learning predictive models.
*  And so I think that's what the entire community should be focusing on.
*  At least people are interested in sort of fundamental questions or really kind of pushing the envelope of AI towards the next stage.
*  But of course, there is like a huge amount of very interesting work to do in sort of practical questions that have short term impact.
*  Well, you know, it's difficult to talk about the temporal scale because all of human civilization will eventually be destroyed because the sun will die out.
*  And even if Elon Musk is successful, multi-planetary colonization across the galaxy, eventually the entirety of it will just become giant black holes.
*  And that's going to take a while.
*  So but what I'm saying is then that logic can be used to say it's all meaningless.
*  I'm saying all that to say that multitask learning might be your song.
*  You're calling it practical or pragmatic or whatever.
*  That might be the thing that achieves something very akin to intelligence while we're trying to solve the more general problem of self-supervised learning of background knowledge.
*  So the reason I bring that up may be one way to ask that question.
*  I've been very impressed by what Tesla autopilot team is doing.
*  I don't know if you got any chance to glance at this particular one example of multitask learning where they're literally taking the problem like I don't know Charles Darwin start studying animals.
*  They're studying the problem of driving and asking, OK, what are all the things you have to perceive?
*  And the way they're solving it is one, there's an ontology where you're bringing that to the table.
*  So you're formulating a bunch of different tasks.
*  It's like over 100 tasks or something like that that they're involved in driving and then they're deploying it and then getting data back from people that run to trouble.
*  And they're trying to figure out do we add tasks?
*  Do we like we focus on each individual task separately?
*  In fact, half.
*  So the I would say I'll classify Andre Capati's talking to is so one was about doors and the other one about how much image net sucks.
*  He kept going back and forth on those two topics, which image net sucks, meaning you can't just use a single benchmark.
*  There's so like you have to have like a giant suite of benchmarks to understand how well your system actually works.
*  I agree with him.
*  I mean, he's a very sensible guy.
*  Now, OK, it's very clear that if you're faced with an engineering problem that you need to solve in a relatively short time, particularly if you have it almost breathing down your neck, you're going to have to take shortcuts.
*  Right. You might think about the fact that the right thing to do in the long term solution involves some fancy self-supervised running.
*  But you have, you know, you know, most breathing on your neck.
*  And, you know, this involves, you know, human lives.
*  And so you have to basically just do the systematic engineering and, you know, fine tuning and refinements and try and error and all that stuff.
*  There's nothing wrong with that.
*  That's that's called engineering.
*  That's called, you know, putting technology out in the in the world.
*  And you have to kind of ironclad it before before you do this, you know, so much for, you know, grand, grand ideas and principles.
*  But, you know, I'm placing myself sort of, you know, some, you know, upstream of this, you know, quite a bit upstream of this.
*  You're a Plato think about platonic forms.
*  You're you're platonic because eventually I want that stuff to get used.
*  But it's OK if it takes five or ten years for the community to realize this is the right thing to do.
*  I've I've done this before.
*  It's been the case before that.
*  You know, I've made that case.
*  I mean, if you look back in the mid 2000, for example, and you ask yourself the question, OK, I want to recognize cars or faces or whatever.
*  You know, I can use completion on that, so I can use a more conventional kind of computer vision techniques, you know, using interest point detectors or sift denser features and, you know, sticking an SVM on top.
*  At that time, the data sets were so small that those methods that use more engineering work better than confidence.
*  There's just not enough data for confidence and confidence were a little a little slow with the kind of hardware that was available at the time.
*  And there was a sea change when basically when, you know, data sets became bigger and GPUs became available.
*  That's what, you know, the two of the main factors that basically made people change their change their mind.
*  And you can you can look at the history of like all sub branches of AI or pattern recognition.
*  And there is a similar trajectory followed by techniques where people start by, you know, engineering the hell out of it.
*  You know, be it optical character recognition, speech recognition, computer vision, like image recognition in general, natural language understanding, like, you know, translation, things like that.
*  Right. You start to engineer the hell out of it.
*  You start to acquire all the knowledge, the prior knowledge, you know, about image formation, about, you know, the shape of characters, about, you know, morphological operations, about like feature extraction, Fourier transforms, you know,
*  vernis-le-moments, you know, whatever. Right.
*  People have come up with thousands of ways of representing images so that they could be easily classified afterwards.
*  Same for speech recognition. Right.
*  There is, you know, it took decades for people to figure out a good front end to preprocess speech signals so that, you know, the information about what is being said is preserved.
*  But most of the information about the identity of the speaker is gone.
*  You know, Kestrel coefficients or whatever. Right.
*  And same for for text. Right.
*  You do name entity recognition and you parse and you do tagging of the parts of speech and, you know, you do this sort of tree representation of clauses and all that stuff right before you can do anything.
*  So that's how it starts. Right.
*  Just engineer the hell out of it.
*  And then you start having data and maybe you have more powerful computers.
*  Maybe you know something about statistical learning.
*  So you start using machine learning and it's usually a small sliver on top of your kind of handcrafted system where you know you extract features by hand.
*  Okay. And now, you know, nowadays the standard way of doing this is that you train the entire thing end to end with a deep learning system and it learns its own features and, you know, speech recognition systems nowadays.
*  OCR systems are completely end to end.
*  It's, you know, it's some giant neural net that takes raw waveforms and produces a sequence of characters coming out.
*  And it's just a huge neural net. Right.
*  There's no Markov model.
*  There's no language model that is explicit other than, you know, something that's ingrained in the in the sort of neural language model.
*  If you want same for translation, same for all kinds of stuff.
*  So you see this continuous evolution from, you know, less and less hand crafting and more and more learning.
*  And I think it's true in biology as well.
*  So, I mean, we might disagree about this.
*  Maybe not in this one little piece at the end.
*  You mentioned active learning.
*  It feels like active learning, which is the selection of data and also the interactivity needs to be part of this giant neural network.
*  You cannot just be an observer to do self supervised learning.
*  You have to. Well, I don't know.
*  Self supervised learning is just the word.
*  But I would whatever this giant stack of in your own network that's automatically learning, it feels my intuition is that you have to have a system, whether it's a physical robot or a digital robot that's interacting with the world and doing so in a flawed way and improving over time.
*  In order to do form the self supervised learning.
*  Well, you can't just give it a giant sea of data.
*  OK, I agree and I disagree.
*  I agree in the sense that I think I agree.
*  I agree in two ways.
*  The first the first way I agree is that if you want and you certainly need a causal model of the world that allows you to predict the consequences of your actions to train that model, you need to take actions.
*  You need to be able to act in a world and see the effect for you to be to learn causal models of the world.
*  So that's not that's not obvious because you can observe others.
*  You can observe others and you can infer that they're similar to you and then you can learn from that.
*  Yeah, but then you have to kind of hardware that part.
*  Right.
*  You know, mirror neurons and all that stuff.
*  Right. So and it's not clear to me how you would do this in a machine.
*  So so I think the the action part would be necessary for having causal models of the world.
*  The second reason it may be necessary or at least more efficient is that active learning basically goes for the juggler of what you what you don't know.
*  Right. Is this obvious areas of uncertainty about your your world and about how the world behaves.
*  And you can resolve this uncertainty by systematic exploration of that part that you don't you don't know.
*  And if you know that you don't know, then you know, it makes you curious.
*  You kind of look into situations that and, you know, across the animal world, different species at different levels of curiosity.
*  Right. Yeah.
*  Depending on how they're built.
*  Right. So, you know, cats and rats are incredibly curious.
*  Dogs know so much.
*  I mean, less.
*  Yeah. So it could be useful to have that kind of curiosity.
*  So it'd be useful.
*  But curiosity just makes the process faster.
*  It doesn't make the process exist.
*  The so what process what learning process is it that active learning makes more efficient.
*  And I'm asking that first question, you know, you know, we haven't answered that question yet.
*  So, you know, I worry about active learning once this question is the more fundamental question to ask.
*  And if active learning or interaction increases the efficiency of the learning,
*  see, sometimes it becomes very different if the increase is several orders of magnitude.
*  Right. Like that's true.
*  But fundamentally, it's still the same thing.
*  And building up the intuition about how to in a self-supervised way to construct background models, efficient or inefficient, is is the core problem.
*  What do you think about your show Ben just talking about consciousness and all of these kinds of concepts?
*  I don't know what consciousness is, but it's a good opener.
*  And to some extent, a lot of the things that are said about consciousness remind me of the questions people were asking themselves in the 18th century or 17th century when they discovered that, you know, how the eye works and the fact that the image at the back of the eye was upside down.
*  Right. Because you have a lens.
*  And so on your retina, the image that forms is an image of the world, but it's upside down.
*  How is it that you see your eyesight up?
*  And, you know, with what we know today in science, you know, we realize this question doesn't make any sense or is kind of ridiculous in some way.
*  Right. So I think a lot of what is said about consciousness is of that nature.
*  Now, that said, there is a lot of really smart people that for whom I have a lot of respect who are talking about this topic.
*  People like David Chalmers, who is a colleague of mine at NYU.
*  I have kind of an unorthodox folk speculative hypothesis about consciousness.
*  So we're talking about the study of world model.
*  And I think, you know, our entire prefrontal cortex basically is the engine for our world model.
*  But when we are attending at a particular situation, we're focused on that situation.
*  We basically cannot attend to anything else.
*  And that seems to suggest that we basically have only one world model engine in our prefrontal cortex.
*  That engine is configurable to the situation at hand.
*  So we are building a box out of wood or we are driving down the highway playing chess.
*  We basically have a single model of the world that we configure into the situation at hand, which is why we can only attend to one task at a time.
*  Now, if there is a task that we do repeatedly, it goes from the sort of deliberate reasoning using model of the world and prediction and perhaps something like model predictive control.
*  Which I was talking about earlier to something that is more subconscious that becomes automatic.
*  So I don't know if you've ever played against a chess grandmaster.
*  You know, I get wiped out in, you know, 10 10 plays.
*  Right. And, you know, I have to think about my move for, you know, like 15 minutes.
*  And the person in front of me, the grandmaster, you know, would just like react within seconds.
*  Right. And I have to think about my move for, you know, like 15 minutes.
*  Right. Within seconds. Right.
*  You know, he doesn't need to think about it.
*  That's become part of subconscious because, you know, it's basically just pattern recognition at this point.
*  Same, you know, you the first few hours you drive a car, you're really attentive.
*  You can't do anything else. And then after 20, 30 hours of practice, 50 hours, you know, is subconscious.
*  You can talk to the person next to you, you know, things like that.
*  Right. And that's the situation because unpredictable.
*  And then you have to stop talking.
*  So that suggests you only have one model in your head.
*  And it might suggest the idea that consciousness basically is the module that configures this world model of yours.
*  You know, you need to have some sort of executive kind of overseer that configures your world model for the situation at hand.
*  And that that leads to kind of the really curious concept that consciousness is not a consequence of the power of our minds, but of the limitation of our brains.
*  But because we have only one world model, we have to be conscious.
*  If we had as many world models as there are situations we encounter, then we could do all of them simultaneously.
*  And we wouldn't need this sort of executive control that we call consciousness.
*  Yeah, interesting. And somehow maybe that executive controller, I mean, the hard problem of consciousness,
*  there's some kind of chemicals in biology that's creating a feeling like it feels to experience some of these things.
*  That's kind of like the hard question is, what the heck is that?
*  And why is that useful? Maybe the more pragmatic question.
*  Why is it useful to feel like this is really you experiencing this versus just like information being processed?
*  It could be just a very nice side effect of the way we evolved.
*  That's just very useful to to feel a sense of ownership to the decisions you make,
*  to the perceptions you make, to the model you're trying to maintain.
*  Like you own this thing and this is the only one you got.
*  And if you lose it, it's going to really suck.
*  And so you should really send the brain some signals about it.
*  What ideas do you believe might be true that most or at least many people disagree with you with?
*  Let's say in the space of machine learning.
*  Well, it depends who you talk about.
*  But I think so certainly there is a bunch of people who are nativists, right?
*  Who think that a lot of the basic things about the world are kind of hardwired in our minds.
*  Things like the world is three dimensional, for example, is that hardwired?
*  Things like object permanence is something that we learn before the age of three months or so.
*  Or are we born with it?
*  And there are very wide disagreements among the cognitive scientists for this.
*  I think those things are actually very simple to learn.
*  Is it the case that the oriented edge detectors in V1 are learned or are they hardwired?
*  I think they are learned.
*  They might be learned before birth because it's really easy to generate signals from the retina that actually will train edge detectors.
*  And again, those are things that can be learned within minutes of opening your eyes.
*  I mean, since the 1990s, we have algorithms that can learn oriented edge detectors completely unsupervised with the equivalent of a few minutes of real time.
*  So those things have to be learned.
*  There's also those MIT experiments where you kind of plug the optical nerve on the auditory cortex of a baby ferret, right?
*  And that auditory cortex becomes a visual cortex, essentially.
*  So clearly, there's learning taking place there.
*  So I think a lot of what people think are so basic that they need to be hardwired, I think a lot of those things are learned because they are easy to learn.
*  So you put a lot of value in the power of learning.
*  What kind of things do you suspect might not be learned?
*  Is there something that could not be learned?
*  So your intrinsic drives are not learned.
*  There are the things that make humans human or make cats different from dogs, right?
*  It's the basic drives that are kind of hardwired in our basal ganglia.
*  I mean, there are people who are working on this kind of stuff that's called intrinsic motivation in the context of reinforcement learning.
*  So these are objective functions where the reward doesn't come from the external world.
*  It's computed by your own brain.
*  Your own brain computes whether you're happy or not, right?
*  It measures your degree of comfort or discomfort.
*  And because it's your brain computing this, presumably it knows also how to estimate gradients of this, right?
*  So it's easier to learn when your objective is intrinsic.
*  So that has to be hardwired.
*  The critic that makes long-term prediction of the outcome, which is the eventual result of this, that's learned.
*  And perception is learned and your model of the world is learned.
*  But let me take an example of why the critic, an example of how the critic may be learned, right?
*  If I come to you, I reach across the table and I pinch your arm, right?
*  Complete surprise for you. You would not have expected this from me.
*  I was expecting that the whole time. But yes, right. Let's say for the sake of the story.
*  Yes.
*  Okay. Your Bizzoganglia is going to light up because it's going to hurt, right?
*  And now your model of the world includes the fact that I may pinch you if I approach my...
*  Don't trust humans.
*  Right. My hand to your arm.
*  My hand to your arm. So if I try again, you're going to recoil.
*  And that's your critic, your predictor of your ultimate pain system that predicts that something bad is going to happen and you recoil to avoid it.
*  So even that can be learned.
*  That is learned, definitely. This is what allows you also to define some goals, right?
*  So the fact that you're a school child who wakes up in the morning and you go to school,
*  and it's not because you necessarily like waking up early and going to school,
*  but you know that there is a long-term objective you're trying to optimize.
*  So Ernest Becker, I'm not sure if you're familiar with him, the philosopher, he wrote the book Denial of Death,
*  and his idea is that one of the core motivations of human beings is our terror of death, our fear of death.
*  That's what makes us unique from cats.
*  Cats are just surviving.
*  They do not have a deep, like cognizance, introspection that over the horizon is the end.
*  And he says that, I mean, there's a terror management theory that just all these psychological experiments that show basically this idea that all of human civilization,
*  everything we create is kind of trying to forget if even for a brief moment that we're going to die.
*  When do you think humans understand that they're going to die? Is it learned early on also?
*  I don't know at what point. I mean, it's a question like, you know, at what point do you realize that, you know, where death really is?
*  And I think most people don't actually realize what death is, right?
*  I mean, most people believe that you go to heaven or something, right?
*  Well, so to push back on that, what Ernest Becker says and Sheldon Solomon, all of those folks,
*  and I find those ideas a little bit compelling is that there is moments in life, early in life, a lot of this fun happens early in life,
*  when you are, when you do deeply experience the terror of this realization and all the things you think about, about religion,
*  all those kinds of things that we kind of think about more like teenage years and later.
*  We're talking about way earlier. No, it was like seven or eight years, something like that.
*  You realize, holy crap, this is like the mystery, the terror.
*  Like it's almost like you're a little prey, a little baby deer sitting in the darkness of the jungle, the woods, looking all around you.
*  There's darkness full of terror. I mean, that's that realization says, OK, I'm going to go back in the comfort of my mind
*  where there is a deep meaning, where there is maybe like pretend I'm immortal in however way,
*  however kind of idea I can construct to help me understand that I'm immortal.
*  Religion helps with that. You can delude yourself in all kinds of ways, like lose yourself in the busyness of each day,
*  have little goals in mind, all those kinds of things to think that it's going to go on forever.
*  And you kind of know you're going to die. Yeah, it's going to be sad, but you don't really understand that you're going to die.
*  And so that's that's the idea. And I find that compelling because it does seem to be a core unique aspect of human nature
*  that we were able to think that we're able to really understand that this life is finite.
*  That seems important. There's a bunch of different things there.
*  So first of all, I don't think there is a qualitative difference between between us and cats in the term.
*  I think the difference is that we just have a better long term ability to predict in the long term.
*  And so we have a better understanding of other world works.
*  So we have better understanding of finiteness of life and things like that.
*  So we have a better planning engine than cats? Yeah.
*  OK, what's the motivation for planning?
*  Well, I think it's just a side effect of the fact that we have just a better planning engine because it makes us,
*  as I said, the essence of intelligence is the ability to predict.
*  And so the because we're smarter as a side effect, we also have this ability to kind of make predictions about our own future existence or lack thereof.
*  OK, you say religion helps with that. I think religion hurts, actually.
*  It makes people worry about what's going to happen after their death, et cetera.
*  If you believe that you just don't exist after death, like it solves completely the problem.
*  You're saying if you don't believe in God, you don't worry about what happens after death?
*  Yeah, I don't know. You worry about about, you know, this life because that's the only one you have.
*  I think it's well, I don't know.
*  If I were to say what Ernest Becker says, and I agree with him more than not, is you do deeply worry.
*  If you if you believe there's no God, there's still a deep worry like of the mystery of it all.
*  Like, how does that make any sense that it just ends?
*  I don't think we can truly understand that this right.
*  I mean, so much of our life, the consciousness, the ego is invested in this in this being.
*  And then science keeps bringing humanity down from its pedestal.
*  And that's another another example of it.
*  That's wonderful. But for us individual humans, we don't like to be brought down from a pedestal.
*  You're saying like, but see, you're fine with it because well,
*  so what Ernest Becker would say is you're fine with it because that's just a more peaceful existence for you.
*  But you're not really fine. You're hiding from.
*  In fact, some of the people that experienced the deepest trauma earlier in life,
*  they often before they seek extensive therapy will say that I'm fine.
*  It's like when you talk to people who are truly angry, how are you doing? I'm fine.
*  The question is, what's going on?
*  I had a near death experience. I had a very bad motorbike accident when I was 17.
*  So but that didn't have any impact on my reflection on that topic.
*  So I'm basically just playing a bit of a devil's advocate, pushing back on wondering,
*  is it truly possible to accept death?
*  And the flip side that's more interesting, I think, for AI and robotics is how important is it to have
*  this as one of the suite of motivations is to not just avoid falling off the roof or something like that,
*  but ponder the end of the ride.
*  If you listen to the stoics, it's a great motivator.
*  It adds a sense of urgency.
*  So maybe to truly fear death or be cognizant of it might give a deeper meaning and urgency to the moment to live fully.
*  Maybe I don't disagree with that.
*  I mean, I think what motivates me here is knowing more about human nature.
*  I mean, I think human nature and human intelligence is a big mystery.
*  It's a scientific mystery in addition to philosophical and et cetera.
*  But I'm a true believer in science.
*  And I do have kind of a belief that for complex systems like the brain and the mind,
*  the way to understand it is to try to reproduce it with artifacts that you build
*  because you know what's essential to it when you try to build it.
*  The same way I've used this analogy before with you, I believe,
*  the same way we only started to understand aerodynamics when we started building airplanes,
*  and that helped us understand how birds fly.
*  So I think there's kind of a similar process here where we don't have a full theory of intelligence,
*  but building intelligent artifacts will help us perhaps develop some underlying theory
*  that encompasses not just artificial implements,
*  but also human and biological intelligence in general.
*  So you're an interesting person to ask this question about sort of all kinds of different other intelligent entities or intelligences.
*  What are your thoughts about kind of like the touring or the Chinese room question?
*  If we create an AI system that exhibits a lot of properties of intelligence and consciousness,
*  how comfortable are you thinking of that entity as intelligent or conscious?
*  So you're trying to build now systems that have intelligence and there's metrics about their performance,
*  but that metric is external.
*  So are you OK calling a thing intelligent or are you going to be like most humans
*  and be once again unhappy to be brought down from a pedestal of consciousness slash intelligence?
*  No, I'll be very happy to understand more about human nature, human mind and human intelligence
*  through the construction of machines that have similar abilities.
*  And if a consequence of this is to bring down humanity one notch down from its already low pedestal,
*  I'm just fine with it. That's just the reality of life.
*  So I'm fine with that.
*  Now you were asking me about things that opinions I have that a lot of people may disagree with.
*  I think if we think about the design of autonomous intelligence systems,
*  so assuming that we are somewhat successful at some level of getting machines to learn models of the world,
*  predicting models of the world, we build intrinsic motivation objective functions to drive the behavior of that system.
*  The system also has perception modules that allows it to estimate the state of the world
*  and then have some way of figuring out a sequence of actions to optimize a particular objective.
*  If it has a critic of the type that was describing before,
*  the thing that makes you recoil your arm the second time I try to pinch you,
*  intelligent autonomous machine will have emotions.
*  I think emotions are an integral part of autonomous intelligence.
*  If you have an intelligent system that is driven by intrinsic motivation, by objectives,
*  if it has a critic that allows it to predict in advance whether the outcome of a situation is going to be good or bad,
*  it's going to have emotions. It's going to have fear.
*  When it predicts that the outcome is going to be bad and something to avoid,
*  it's going to have elation when it predicts it's going to be good.
*  If it has drives to relate with humans in some ways, the way humans have,
*  it's going to be social. It's going to have emotions about attachment and things of that type.
*  I think the sci-fi thing where you see commander data having an emotion chip that you can turn off,
*  I think that's ridiculous.
*  Here's the difficult philosophical social question.
*  Do you think there will be a time like a civil rights movement for robots where,
*  okay, forget the movement, but a discussion like the Supreme Court that particular kinds of robots,
*  particular kinds of systems deserve the same rights as humans because they can suffer just as humans can, all those kinds of things?
*  Well, perhaps, perhaps not. Imagine that humans were, that you could die and be restored.
*  You could be 3D reprinted and your brain could be reconstructed in its finest details.
*  Our ideas of rights will change in that case. If you can always just, there's always a backup, you could always restore.
*  Maybe the importance of murder will go down one notch.
*  That's right. But also your desire to do dangerous things like skydiving or race car driving, car racing,
*  all that kind of stuff would probably increase or airplane aerobatics or that kind of stuff.
*  It would be fine to do a lot of those things or explore dangerous areas and things like that.
*  It would kind of change your relationship. So now it's very likely that robots would be like that because they'll be based on perhaps technology
*  that is somewhat similar to today's technology and you can always have a backup.
*  So it's possible, I don't know if you like video games, but there's a game called Diablo.
*  My sons are huge fans of this.
*  Yes.
*  In fact, they made a game that's inspired by it.
*  Awesome. Like built a game?
*  My three sons have a game design studio between them.
*  That's awesome.
*  They came out with a game last year. No, this was last year, early last year, about a year ago.
*  That's awesome. But so in Diablo, there's something called hardcore mode, which if you die, there's no, you're gone.
*  Right.
*  That's it. And so it's possible with AI systems for them to be able to operate successfully and for us to treat them in a certain way,
*  because they have to be integrated in human society, they have to be able to die, no copies allowed.
*  In fact, copying is illegal. It's possible with humans as well, like cloning would be illegal, even when it's possible.
*  But cloning is not copying, right? I mean, you don't reproduce the mind of the person and experience.
*  It's just a delayed twin.
*  But then it's, we were talking about with computers that you will be able to copy.
*  You'll be able to perfectly save, pickle the mind state.
*  And it's possible that that will be illegal because that goes against, that will destroy the motivation of the system.
*  Okay. So let's say you have a domestic robot, okay, sometime in the future.
*  Yes.
*  And the domestic robot comes to you kind of somewhat pre-trained, can do a bunch of things.
*  Yes.
*  But it has a particular personality that makes it slightly different from the other robots because that makes them more interesting.
*  And then because it's lived with you for five years, you've grown some attachment to it and vice versa.
*  And it's learned a lot about you. Or maybe it's not a household robot.
*  Maybe it's a virtual assistant that lives in your augmented reality glasses or whatever, right?
*  The Her movie type thing, right?
*  And that system, to some extent, the intelligence in that system is a bit like your child or maybe your PhD student in the sense that there's a lot of you in that machine now, right?
*  And so if it were a living thing, you would do this for free if you want, right?
*  If it's your child, your child can then live his or her own life.
*  And the fact that they learn stuff from you doesn't mean that you have any ownership of it, right?
*  But if it's a robot that you've trained, perhaps you have some intellectual property claim.
*  Intellectual property? Oh, I thought you meant like permanent value in the sense that part of you is in...
*  Well, there is permanent value, right? So you would lose a lot if that robot were to be destroyed and you had no backup, you would lose a lot.
*  You would lose a lot of investment, you know, kind of like a person dying, you know, that a friend of yours dying or a co-worker or something like that.
*  But also you have like intellectual property rights in the sense that that system is fine-tuned to your particular existence.
*  So that's now a very unique instantiation of that original background model, whatever it was that arrived.
*  And then there are issues of privacy, right? Because now imagine that that robot has its own kind of volition and decides to work for someone else.
*  Or kind of thinks life with you is sort of untenable or whatever.
*  Now all the things that that system learned from you, can you like delete all the personal information that that system knows about you?
*  I mean, that would be kind of an ethical question.
*  Like, you know, can you erase the mind of an intelligent robot to protect your privacy?
*  You can't do this with humans. You can ask them to shut up, but that you don't have complete power over them.
*  Can't erase humans. Yeah, it's the problem with relationships, you know, that you break up.
*  You can't you can't erase the other human with robots.
*  I think it will have to be the same thing with robots that that risk that there has to be some risk to our interactions to truly experience them deeply, it feels like.
*  So you have to be able to lose your robot friend and that robot friend to go tweeting about how much of an asshole you are.
*  But then are you allowed to, you know, murder the robot to protect your private information?
*  Yeah, probably not. I have this intuition that for robots with with certain like it's almost like regulation.
*  If you declare your robot to be, let's call it sentient or something like that, like this, this robot is designed for human interaction.
*  Then you're not allowed to murder these robots. It's the same as murdering of the humans.
*  Well, but what about you do a backup of the robot you do preserve on a hard drive or the equivalent in the future?
*  That might be illegal. It's like it's a piracy. Piracy is illegal.
*  But it's your own. It's your own robot, right? But you can't. You don't.
*  But then but then you can wipe out his brain. So the this robot doesn't know anything about you anymore.
*  But you still have technically is still in existence because you backed it up.
*  And then there'll be these great speeches at the Supreme Court by saying, oh, sure, you can erase the mind of the robot just like you can erase the mind of a human.
*  We both can suffer. There'll be some epic like Obama type character with a speech that we we like the robots and the humans are the same.
*  We can both suffer. We can both hope we can both all of those all those kinds of things.
*  Raise families, all that kind of stuff. It's it's interesting for these.
*  Just like you said, emotion seems to be a fascinatingly powerful aspect of human to human interaction, human robot interaction.
*  And if they're able to exhibit emotions at the end of the day, that's probably going to have us deeply consider human rights like what we value in humans, what we value in other animals.
*  That's why robots and AI is great. It makes us ask really good questions.
*  The hard questions. Yeah. But you you ask about you asked about the Chinese room type argument.
*  You know, is it real if it looks real? Yeah. I think the Chinese argument is a ridiculous one.
*  So so so for people who don't know Chinese room is you can I don't even know how to formulate it well.
*  But basically you can mimic the behavior of an intelligent system by just following a giant algorithm codebook that tells you exactly how to respond in exactly each case.
*  But is that really intelligent? It's like a giant lookup table. When this person says this, you answer this.
*  When this person says this, you answer this. And if you understand how that works, you have this giant, nearly infinite lookup table.
*  Is that really intelligence? Because intelligence seems to be a mechanism that's much more interesting and complex than this lookup table.
*  I don't think so. So the I mean, the real question comes down to do you think you know, you can you can mechanize intelligence in some way, even if that involves learning.
*  And the answer is, of course, yes, there's no question.
*  There's a second question then, which is, assuming you can reproduce intelligence in sort of different hardware than biological hardware, you know, like computers.
*  Can you, you know, match human intelligence in all the domains in which humans are intelligent?
*  Is it possible? Right. So that's the hypothesis of strong AI.
*  The answer to this, in my opinion, is an unqualified yes. This will as well happen at some point.
*  There's no question that machines at some point will become more intelligent than humans in all domains where humans are intelligent.
*  This is not for tomorrow. It's going to take a long time, regardless of what, you know, Elon and others have claimed or believed.
*  This is a lot a lot harder than many of many of those guys think it is.
*  And many of those guys who thought it was simpler than that years ago, you know, five years ago now think it's hard because it's been five years and they realize it's going to take a lot longer.
*  That includes a bunch of people at DeepMind, for example.
*  But I have an extra touch base with the DeepMind folks.
*  But some of it, Elon or Demisasavvas, I mean, sometimes your role, you have to kind of create deadlines that are nearer than farther away to kind of create an urgency.
*  Because, you know, you have to believe the impossible is possible in order to accomplish it.
*  And there's, of course, a flip side to that coin. But it's a weird you can't be too cynical if you want to get something done.
*  Absolutely. I agree with that.
*  But I mean, you have to inspire people to work on sort of ambitious things.
*  So, you know, it's certainly a lot harder than we believe.
*  But there's no question in my mind that this will this will happen.
*  And now, you know, people are kind of worried about what does that mean for humans?
*  They are going to be brought down from their pedestal, you know, a bunch of notches with that.
*  And, you know, is that going to be good or bad?
*  I mean, it's just going to give more power, right?
*  It's an amplifier for human intelligence, really.
*  So speaking of doing cool, ambitious things, FAIR, the Facebook AI research group, has recently celebrated its eighth birthday.
*  Or maybe you can correct me on that.
*  Looking back, what has been the successes, the failures, the lessons learned from the eight years of FAIR?
*  And maybe you can also give context of where does the newly minted meta AI fit into?
*  How does it relate to FAIR?
*  Right. So let me tell you a bit about the organization of all this.
*  Yeah, FAIR was created almost exactly eight years ago.
*  It wasn't called FAIR yet.
*  It took that name a few months later.
*  And at the time I joined Facebook, there was a group called the AI group that had about 12 engineers and a few scientists, like, you know, 10 engineers and two scientists or something like that.
*  I ran it for three and a half years as a director.
*  I hired the first few scientists and kind of set up the culture and organized it, you know, explained to the Facebook leadership what fundamental research was about and how it can work within industry and how it needs to be open and everything.
*  And I think it's been an unqualified success in the sense that FAIR has simultaneously produced, you know, top level research and advanced the science and the technology, provided tools, open source tools like PyTorch and many others.
*  But at the same time has had a direct or mostly indirect impact on Facebook at the time, now Meta, in the sense that a lot of systems that Meta is built around now are based on research projects that started at FAIR.
*  So if you were to take out, you know, deep learning out of Facebook services now and Meta more generally, I mean, the company would literally crumble.
*  I mean, it's completely built around AI these days.
*  And it's really essential to the operations.
*  So what happened after three and a half years is that I changed role.
*  I became chief scientist.
*  So I'm not doing day to day management of FAIR anymore.
*  I'm more of a kind of, you know, think about strategy and things like that.
*  And I carry my, I conduct my own research.
*  I've, you know, my own kind of research group working on self-supervised learning and things like this, which I didn't have time to do when I was director.
*  So now FAIR is run by Joël Pinault and Antoine Borde together because FAIR is kind of split in two now.
*  There's something called FAIR Labs, which is sort of bottom up, science driven research and FAIR Excel, which is slightly more organized for bigger projects that require a little more kind of focus and more engineering support and things like that.
*  So Joël needs FAIR Lab and Antoine Borde needs FAIR Excel.
*  Where are they located?
*  It's delocalized all over.
*  So there's no question that the leadership of the company believes that this was a very worthwhile investment.
*  And what that means is that it's there for the long run.
*  Right.
*  So there is, if you want to talk in these terms, which I don't like, there's a business model, if you want, where FAIR, despite being a very fundamental research lab, brings a lot of value to the company,
*  either mostly indirectly through other groups.
*  Now what happened three and a half years ago when I stepped down was also the creation of Facebook AI, which was basically a larger organization that covers FAIR.
*  So FAIR is included in it, but also has other organizations that are focused on applied research or advanced development of AI technology that is more focused on the products of the company.
*  So less emphasis on fundamental research.
*  Less fundamental, but it's still a research.
*  I mean, there's a lot of papers coming out of those organizations and people are awesome and wonderful to interact with.
*  But it serves as kind of a way to kind of scale up, if you want, sort of AI technology, which may be very experimental and sort of lab prototypes into things that are usable.
*  So FAIR is a subset of meta-AI.
*  If FAIR becomes like KFC, it'll just keep the F. Nobody cares what the F stands for.
*  We'll know soon enough by probably by the end of 2021.
*  I think this is not a giant change, FAIR.
*  Well, FAIR doesn't sound too good.
*  But the brand people are kind of deciding on this and they've been hesitating for a while now.
*  And they tell us they're going to come up with an answer as to whether FAIR is going to change name or whether we're going to change just the meaning of the F.
*  That's a good call.
*  I would keep FAIR and change the meaning of the F.
*  That would be my preference.
*  I would turn the F into fundamental.
*  Fundamental AI research.
*  Oh, that's really good.
*  Within meta-AI.
*  So this would be sort of meta-FAIR.
*  But people will call it FAIR.
*  Exactly.
*  I like it.
*  So now meta-AI is part of the Reality Lab.
*  So Meta now, the new Facebook is called Meta and it's kind of divided into Facebook, Instagram, WhatsApp, and Reality Lab.
*  Reality Lab is about AR, VR, telepresence, communication technology and stuff like that.
*  You can think of it as the sort of a combination of sort of new products and technology part of Meta.
*  Is that where the touch sensing for robots I saw that you were posting about?
*  Touch sensing for robots is part of FAIR, actually.
*  Oh, it is?
*  Okay.
*  There is also the other way, the haptic glove.
*  Yes, that's more Reality Lab.
*  That's Reality Lab research.
*  Reality Lab research.
*  By the way, the touch sensors are super interesting.
*  Integrating that modality into the whole sensing suite is very interesting.
*  So what do you think about the metaverse?
*  What do you think about this whole kind of expansion of the view of the role of Facebook and Meta in the world?
*  Metaverse really should be thought of as the next step in the internet.
*  Sort of trying to kind of make the experience more compelling of being connected either with other people or with content.
*  And we are evolved and trained to evolve in 3D environments where we can see other people, we can talk to them when we're near them, or other viewers far away can hear us, things like that.
*  So there's a lot of social conventions that exist in the real world that we can try to transpose.
*  Now, what is going to be eventually the...
*  How compelling is it going to be?
*  Is it going to be the case that people are going to be willing to do this if they have to wear a huge pair of goggles all day?
*  Maybe not.
*  But then again, if the experience is sufficiently compelling, maybe so.
*  Or if the device that you have to wear is just basically a pair of glasses, technology makes sufficient progress for that.
*  AR is a much easier concept to grasp that you're going to have augmented reality glasses that basically contain some sort of virtual assistant that can help you in your daily lives.
*  But at the same time with AR, you have to contend with reality. With VR, you can completely detach yourself from reality, so it gives you freedom.
*  It might be easier to design worlds in VR.
*  Yeah, but you can imagine the Metaverse being...
*  A mix.
*  A mix, right. Or you can have objects that exist in the Metaverse that pop up on top of the real world or only exist in virtual reality.
*  Okay, let me ask the hard question.
*  Because all of this was easy.
*  This was easy.
*  The Facebook, now Meta, the social network, has been painted by the media as net negative for society, even destructive and evil at times.
*  You've pushed back against this, defending Facebook.
*  Can you explain your defense?
*  Yeah, so the description, the company that is being described in some media, is not the company we know when we work inside.
*  And, you know, it could be claimed that a lot of employees are uninformed about what really goes on in the company.
*  But, you know, I'm a vice president.
*  I mean, I have a pretty good vision of what goes on.
*  I don't know everything, obviously.
*  I'm not involved in everything, but certainly not in decision about content moderation or anything like this.
*  But I have some decent vision of what goes on.
*  And this evil that is being described, I just don't see it.
*  And then, you know, I think there is an easy story to buy, which is that all the bad things in the world and the reason your friend believes crazy stuff,
*  you know, there's an easy scapegoat, right?
*  In social media in general, Facebook in particular, we have to look at the data.
*  Like, is it the case that Facebook, for example, polarizes people politically?
*  Are there academic studies that show this?
*  Is it the case that, you know, teenagers think of themselves less if they use Instagram more?
*  Is it the case that, you know, people get more riled up against, you know, opposite sides in a debate or political opinion if they are more on Facebook or if they are less?
*  And study after study show that none of this is true.
*  This is independent studies by academic.
*  They're not funded by Facebook or Meta, you know, studied by Stanford, by some of my colleagues at NYU, actually, with whom I have no connection.
*  You know, there's a study recently, they paid people, I think it was in former Yugoslavia, I'm not exactly sure in what part, but they paid people to not use Facebook for a while in the period before the anniversary of the Sibirnica massacres, right?
*  So people get riled up like, you know, should we have a celebration, I mean, a memorial kind of celebration for it or not?
*  So they paid a bunch of people to not use Facebook for a few weeks.
*  It turns out that those people ended up being more polarized than they were at the beginning and the people who were more on Facebook were less polarized.
*  There's a study from Stanford of economists at Stanford that tried to identify the causes of increasing polarization in the US.
*  And it's been going on for 40 years before, you know, Mark Zuckerberg was born continuously.
*  And so if there is a cause, it's not Facebook or social media.
*  So you could say social media just accelerated. But no, I mean, it's basically a continuous evolution by some measure of polarization in the US.
*  And then you compare this with other countries like the west half of Germany, because you can go 40 years in the East side or Denmark or other countries.
*  And they use Facebook just as much. And they're not getting more polarized, they're getting less polarized.
*  So if you want to look for a causal relationship there, you can find a scapegoat, but you can't find a cause.
*  Now, if you want to fix the problem, you have to find the right cause.
*  And what drives me up is that people now are accusing Facebook of bad deeds that are done by others.
*  And those others are we're not doing anything about them.
*  And by the way, those others include the owner of the Wall Street Journal in which all of those papers were published.
*  So I should mention that I'm talking to Shrep, Mike Shrepfer on this podcast and also Mark Zuckerberg.
*  And probably these are conversations I can have with them because it's very interesting to me, even if Facebook has some measurable negative effect, you can't just consider that in isolation.
*  You have to consider about all the positive ways it connects us. So like every technology.
*  It connects people. It's a question.
*  You can't just say like there's an increase in division.
*  Yes, probably Google search engine has created increase in division.
*  We have to consider about how much information are brought to the world.
*  Like, I'm sure Wikipedia created more division.
*  If you just look at the division, we have to look at the full context of the world and they didn't make a better world.
*  The printing press has created more.
*  Exactly.
*  So, you know, when the printing press was invented, the first books that were printed were things like the Bible.
*  And that allowed people to read the Bible by themselves, not get the message uniquely from priests in Europe.
*  And that created the Protestant movement and 200 years of religious persecution and wars.
*  So that's a bad side effect of the printing press.
*  You know, social networks aren't being nearly as bad as the printing press, but nobody would say the printing press was a bad idea.
*  Yeah, a lot of it is perception and there's a lot of different incentives operating here.
*  Maybe a quick comment.
*  Since you're one of the top leaders at Facebook and at Meta, sorry, that's in the tech space.
*  I'm sure Facebook involves a lot of incredible technological challenges that need to be solved.
*  A lot of it probably is in the computer infrastructure, the hardware, the I mean, it's just a huge amount.
*  Maybe can you give me context about how much of Shrep's life is AI and how much of it is low level compute?
*  How much of it is flying all around doing business stuff in the same way as Zuckerberg, Mark Zuckerberg?
*  They really focus on AI.
*  I mean, certainly in the run up of the creation of FAIR and for at least a year after that, if not more,
*  Mark was very, very much focused on AI and was spending quite a lot of effort on it.
*  And that's his style. When he gets interested in something, he reads everything about it.
*  He read some of my papers, for example, before he joined.
*  And so he learned a lot about it.
*  He said he liked notes.
*  Right. And Shrep was really into it also.
*  I mean, Shrep is really kind of, has something I've tried to preserve also despite my not so young age,
*  which is a sense of wonder about science and technology.
*  And he certainly has that.
*  He's also a wonderful person.
*  I mean, in terms of like as a manager, like dealing with people and everything, Mark also actually.
*  I mean, they're very, like, you know, very human people.
*  In the case of Mark, it's shockingly human, you know, given his trajectory.
*  I mean, the personality of him that is painted in the press is just completely wrong.
*  Yeah. But you have to know how to play the press.
*  So that's I put some of that responsibility on him, too.
*  You have to. It's like, you know, like the director, the conductor of an orchestra.
*  You have to play the press and the public in a certain kind of way where you convey your true self to them.
*  If there is a depth and kindness to it.
*  And it's probably not the best at it. So, yeah.
*  You have to learn.
*  And it's sad to see and I'll talk to him about it, but the Shrep is slowly stepping down.
*  It's always sad to see folks sort of be there for a long time and slowly.
*  I guess time is sad.
*  I think he's done the thing he set out to do.
*  And, you know, he's got, you know, family priorities and stuff like that.
*  And I understand, you know, after 13 years or something, it's been a good run, which in Silicon Valley is basically a lifetime.
*  Yeah. You know, because, you know, it's dog years.
*  So in Europe, the conference just wrapped up.
*  Let me just go back to something else.
*  You posted the paper you co-authored was rejected from Europe, as you said, proudly in quotes, rejected.
*  Yeah, I know.
*  Can you describe this paper and like what was the idea in it?
*  And also maybe this is a good opportunity to ask what are the pros and cons, what works and what doesn't about the review process?
*  Yeah, let me talk about the paper first.
*  I'll talk about the review process afterwards.
*  The paper is called VicReg.
*  So this is I mentioned that before variance, invariance, covariance regularization.
*  And it's a technique, a non-contrastive learning technique for what I call joint embedding architecture.
*  So Siamese nets are an example of joint embedding architecture.
*  So joint embedding architecture is let me back up a little bit, right?
*  So if you want to do self-supervised learning, you can you can do it by prediction.
*  So let's say you want to train a system to predict video, right?
*  You show it a video clip and you train the system to predict the next the continuation of that video clip.
*  Now, because you need to handle uncertainty because there are many, many continuations that are plausible, you need to have you need to handle this in some way.
*  You need to have a way for the system to be able to produce multiple predictions.
*  And the way the only way I know to do this is to let's call a latent variable.
*  So you have some sort of hidden vector of a variable that you can vary over a set or draw from a distribution.
*  And as you vary this vector over a set, the output, the prediction varies over a set of plausible predictions.
*  OK, so that's called I call this a generative latent variable model.
*  Got it. OK, now there is an alternative to this to handle uncertainty.
*  And instead of directly predicting the the next frames of the clip, you also run those through another neural net.
*  So you now have two neural nets, one that looks at the the the initial segment of the video clip and another one that looks at the continuation during training.
*  And what what you're trying to do is learn a representation of those two video clips that is maximally informative about the video clips themselves.
*  But it's such that you can predict the representation of the second video clip from the representation of the first one easily.
*  And you can sort of formalize this in terms of maximizing mutual information and some stuff like that.
*  But it doesn't matter.
*  What you want is informative, representative, you know, informative representations of the two video clips that are mutually predictable.
*  What that means is that there's a lot of details in the second video clips that are irrelevant.
*  You know, I let's say video could consist in, you know, a camera panning the scene.
*  There's going to be a piece of that room that is going to be revealed.
*  And I can somewhat predict what the what that room is going to look like.
*  But I may not be able to predict the details of the texture of the ground and where the tiles are ending and stuff like that.
*  Right. So those are irrelevant details that perhaps my representation will eliminate.
*  And so what I need is to train this second neural net in such a way that whenever the continuation video clip varies over all the plausible continuations, the representation doesn't change.
*  Got it. Yeah, got it.
*  Over the space of representations, doing the same kind of thing as you do with similarity learning.
*  Right.
*  So so these are two ways to handle multimodality in a prediction.
*  Right. In the first way, you parameterize the prediction with a latent variable, but you predict pixels essentially.
*  Right. In the second one, you don't predict pixels.
*  You predict an abstract representation of pixels.
*  You guarantee that this abstract representation has as much information as possible about the input, but sort of drops all the stuff that you really can't predict essentially.
*  I used to be a big fan of the first approach.
*  And in fact, in this paper with the Chan Mishra, this blog post, the Dark Matter Intelligence, I was kind of advocating for this.
*  And in the last year and a half, I've completely changed my mind.
*  I'm now a big fan of the second one.
*  And it's because of a small collection of algorithms that have been proposed over the last year and a half or so, two years, to do this, including V-CREG, its predecessor called Barlow-Twins,
*  which I mentioned, a method from our friends at DeepMind called BYOL.
*  And there's a bunch of others now that kind of work similarly.
*  So they're all based on this idea of joint embedding.
*  Some of them have an explicit criterion that is an approximation of mutual information.
*  Some others at BYOL work, but we don't really know why.
*  And there's been like lots of theoretical papers about why BYOL works.
*  No, it's not that because we take it out and it still works.
*  So there's like a big debate.
*  But the important point is that we now have a collection of non-contrastive joint embedding methods, which I think is the best thing since sliced bread.
*  So I'm super excited about this because I think it's our best shot for techniques that would allow us to kind of build predictive models
*  and at the same time learn hierarchical representations of the world where what matters about the world is preserved and what is irrelevant is eliminated.
*  By the way, the representations of before and after is in the space in a sequence of images or is it for single images?
*  It would be either for a single image for a sequence.
*  It doesn't have to be images. This could be applied to text. This could be applied to just about any signal.
*  I'm looking for methods that are generally applicable that are not specific to one particular modality.
*  It could be audio or whatever.
*  Got it. So what's the story behind this paper? This paper is describing one such method?
*  This is Vicregg method. So the first author is a student called Adrien Bard, who is a resident PhD student at Fair Paris.
*  He was co-advised by me and Jean Ponce, who is a professor at École Normale Supérieure, also a research director at INRIA.
*  So this is a wonderful program in France where PhD students can basically do their PhD in industry.
*  And that's kind of what's happening here.
*  And this paper is a follow up on this Barlow-Twin paper by my former postdoc, now Stephane Deney, with Li Jing and Eurij Bontar and a bunch of other people from Fair.
*  And one of the main criticisms from reviewers is that Vicregg is not different enough from Barlow-Twin.
*  But my impression is that it's Barlow-Twin with a few bugs fixed essentially. And in the end, this is what people will use.
*  Right. So. But I'm used to stuff that I submit being rejected for a while.
*  So it might be rejected and actually exceptionally well cited because people use it.
*  Well, it's already cited a bunch of times.
*  So, I mean, the question is then to the deeper question about peer review and conferences.
*  I mean, computer science is a field that's kind of unique that the conference is highly prized. That's one.
*  Right. And it's interesting because the peer review process there is similar, I suppose, to journals, but it's accelerated significantly.
*  Well, not significantly, but it goes fast. And it's a nice way to get stuff out quickly.
*  To peer review quickly, go to present it quickly to the community. So not quickly, but quicker.
*  Yeah. But nevertheless, it has many of the same flaws of peer review because it's a limited number of people look at it as bias and the following.
*  Like that if you want to do new ideas, you're going to get pushed back.
*  There's self-interested people that kind of can infer who submitted it and kind of, you know, be cranky about it.
*  All that kind of stuff. Yeah.
*  I mean, there's a lot of social phenomena there.
*  There's one social phenomenon, which is that because the field has been growing exponentially, the vast majority of people in the field are extremely junior.
*  Yeah. So as a consequence, and that's just a consequence of the field growing, right?
*  So as the number of the size of the field kind of starts saturating, you will have less of that problem of reviewers being very inexperienced.
*  A consequence of this is that, you know, young reviewers, I mean, there's a phenomenon which is that reviewers try to make their life easy.
*  And to make their life easy when reviewing a paper is very simple. You just have to find a flaw in the paper.
*  Right. So basically, they see their task as finding flaws in papers. And most papers have flaws, even the good ones.
*  So it's easy to do that. Your job is easier as a reviewer if you just focus on this.
*  But what's important is, like, is there a new idea in that paper that is likely to influence?
*  It doesn't matter if the experiments are not that great, if the protocol is, you know, so things like that.
*  As long as there is a worthy idea in it that will influence the way people think about the problem, even if they make it better, you know, eventually, I think that's really what makes a paper useful.
*  And so this combination of social phenomena creates a disease that has plagued other fields in the past, like speech recognition,
*  where basically, you know, people chase numbers on benchmarks. And it's much easier to get a paper accepted if it brings an incremental improvement on a sort of mainstream, well-accepted method or problem.
*  And those are, to me, boring papers. I mean, they're not useless, right, because industry strives on those kind of progress.
*  But they're not the one that I'm interested in in terms of like new concepts and new ideas.
*  So papers that are really trying to strike kind of new advances generally don't make it. Now, thankfully, we have Archive.
*  Archive, exactly. And then there's open review type of situations where you, and then, I mean, Twitter is a kind of open review.
*  I'm a huge believer that review should be done by thousands of people, not two people.
*  I agree.
*  And so Archive, do you see a future where a lot of really strong papers, it's already the present, but a growing future where it'll just be Archive?
*  And you're presenting an ongoing continuous conference called Twitter slash the Internet slash Archive Sanity.
*  André just released a new version. So just not, you know, not being so elitist about this particular gating.
*  It's not a question of being elitist or not. It's a question of being basically recommendation and approval for people who don't see themselves as having the ability to do so by themselves.
*  Right. And so it saves time. Right. If you rely on other people's opinion and you trust those people or those groups to evaluate a paper for you,
*  that saves you time because you don't have to scrutinize the paper as much. It is brought to your attention.
*  I mean, it's the whole idea of sort of a collective recommender system.
*  So I actually thought about this a lot about 10, 15 years ago because there were discussions at NIPS and we're about to create iClear with Yercha Benjoo.
*  And so I wrote a document kind of describing a reviewing system, which basically was, you know, you post your paper on some repository, let's say Archive or now could be open review.
*  And then you can form a reviewing entity, which is equivalent to a reviewing board, you know, of a journal or program committee of a conference.
*  You have to list the members and then that group reviewing entity can choose to review a particular paper spontaneously or not.
*  There is no exclusive relationship anymore between a paper and a venue or reviewing entity.
*  Any reviewing entity can review any paper or may choose not to.
*  And then, you know, given evaluation, it's not published, not published.
*  It's just an evaluation and a comment, which would be public, signed by the reviewing entity.
*  And if it's signed by a reviewing entity, you know, it's one of the members of reviewing entities.
*  So if the reviewing entity is, you know, Lex Friedman's preferred papers, right, you know, it's Lex Friedman writing the review.
*  Yes. What so for me, that's a beautiful system, I think.
*  But what's in addition to that, it feels like there should be a reputation system for the reviewers for the reviewing entities, not the reviewers individually reviewing entities.
*  Sure. But even within that, the reviewers, too, because I said there's another thing here.
*  It's not just the reputation. It's an incentive for an individual person to do great right now in the academic setting.
*  The incentive is kind of internal, just wanting to do a good job.
*  But honestly, that's not a strong enough incentive to do a really good job at reading a paper and finding the beautiful amidst the mistakes and the flaws and all that kind of stuff.
*  Right. Like if you're the person that first discovered a powerful paper and you get to be proud of that discovery, then that gives a huge incentive to you.
*  That's a big part of my proposal, actually, where I describe that as, you know, if your evaluation of papers is,
*  predictive of future success, then your reputation should go up as a reviewing entity.
*  So, yeah, exactly. I mean, I even had a master's student who was a master's student in library science and computer science actually kind of work out exactly how that should work with formulas and everything.
*  So in terms of implementation, do you think that's something that's doable?
*  I mean, I've been sort of talking about this to sort of various people like Andrew McCallum, who started Open Review.
*  And the reason why we picked Open Review for iClear initially, even though it was very early for them, is because my hope was that iClear was eventually going to kind of inaugurate this type of system.
*  So iClear kept the idea of Open Reviews. So where the reviews are published with a paper, which I think is very useful.
*  But in many ways, that's kind of reverted to kind of more of a conventional type conferences for everything else.
*  And that, I mean, I don't run iClear. I'm just the president of the foundation.
*  But, you know, people who run it should make decisions about how to run it.
*  And I'm not going to tell them because they're volunteers.
*  And I'm really thankful that they do that.
*  So but I'm saddened by the fact that we're not being innovative enough.
*  Yeah, me too. I hope that changes. Yeah.
*  Because the communication science broadly, but communication, computer science ideas is how you make those ideas have impact.
*  Yeah. And I think, you know, a lot of this is because people have in their mind kind of an objective, which is, you know, fairness for authors and the ability to count points basically and give credits accurately.
*  But that comes at the expense of the progress of science.
*  So to some extent, we're slowing down the progress of science.
*  And are we actually achieving fairness?
*  And we're not achieving fairness. You know, we still have biases.
*  You know, we're doing, you know, a double blind review.
*  But, you know, the biases are still there. There are different kinds of biases.
*  You write that the phenomenon of emergence collective behavior exhibited by a large collection of simple elements in interaction is one of the things that got you into neural nets in the first place.
*  I love cellular automata. I love simple interacting elements and the things that emerge from them.
*  Do you think we understand how complex systems can emerge from such simple components that interact simply?
*  No, we don't. It's a big mystery. Also, it's a mystery for physicists. It's a mystery for biologists.
*  You know, how is it that the universe around us seems to be increasing in complexity and not decreasing?
*  I mean, that is a kind of curious property of physics that despite the second law of thermodynamics, we seem to be, you know, evolution and learning and etc.
*  Seems to be kind of at least locally to increase complexity, not decrease it.
*  So perhaps the ultimate purpose of the universe is to just get more complex.
*  Have these, I mean, small pockets of beautiful complexity. Does that, does cellular automata, do these kinds of emergence and complex systems give you some intuition or guide your understanding of machine learning systems and neural networks and so on?
*  Or are these for you right now disparate concepts?
*  Well, it got me into it. You know, I discovered the existence of the perceptron when I was a college student.
*  You know, by reading a book on, it was a debate between Chomsky and Piaget and Seymour Pepper from MIT was kind of singing the praise of the perceptron in that book.
*  And the first time I heard about the learning machine, right, so I started digging the literature and I found those books,
*  which were basically transcription of, you know, workshops or conferences from the 50s and 60s about self-organizing systems.
*  So there were, there was a series of conferences on self-organizing systems and these books on this.
*  Some of them are, you can actually get them at the Internet Archive, you know, the digital version.
*  And there are like fascinating articles in there by, there's a guy whose name has been largely forgotten, Heinz von Förster.
*  He's a German physicist who immigrated to the US and worked on self-organizing systems in the 50s.
*  And in the 60s, he created at University of Illinois, Urbana-Champaign, he created the biological computer laboratory, BCL, which was all about neural nets.
*  Unfortunately, that was kind of towards the end of the popularity of neural nets, so that lab never kind of strived very much.
*  But he wrote a bunch of papers about self-organization and about the mystery of self-organization.
*  An example he has is you take, imagine you are in space, there's no gravity, you have a big box with magnets in it, okay,
*  you know, kind of rectangular magnets with North Pole on one end, South Pole on the other end.
*  You shake the box gently and the magnets will kind of stick to themselves and probably form a complex structure, you know, spontaneously.
*  You know, that could be an example of self-organization.
*  But you know, you have lots of examples, neural nets are an example of self-organization in many respects.
*  And it's a bit of a mystery, you know, how, like what is possible with this, you know, pattern formation in physical systems, in chaotic system and things like that, you know, the emergence of life, you know, things like that.
*  So, you know, how does that happen? So it's a big puzzle for physicists as well.
*  It feels like understanding this, the mathematics of emergence in some constrained situations might help us create intelligence,
*  like help us add a little spice to the systems because you seem to be able to, in complex systems with emergence, to be able to get a lot from little.
*  And so that seems like a shortcut to get big leaps in performance.
*  But there's a missing concept that we don't have.
*  And it's something also I've been fascinated by since my undergrad days. And it's how you measure complexity.
*  Right. So we don't actually have good ways of measuring or at least we don't have good ways of interpreting the measures that we have at our disposal.
*  Like how do you measure the complexity of something? Right.
*  So there's all those things, you know, like, you know, Kolmogorov, Chaiting, Solomonov, complexity of, you know, the length of the shortest program that would generate a bit string can be thought of as the complexity of that bit string.
*  I've been fascinated by that concept. The problem with that is that that complexity is defined up to a constant, which can be very large.
*  There are similar concepts that are derived from, you know, Bayesian probability theory where, you know, the complexity of something is the negative log of its probability, essentially.
*  Right. And you have a complete equivalence between the two things.
*  And there you would think, you know, the probability is something that's well defined mathematically, which means complexity is well defined.
*  But it's not true. You need to have a model of the distribution.
*  You may need to have a prior if you're doing Bayesian inference and the prior place the same role as the choice of the computer with which you measure Kolmogorov complexity.
*  And so every measure of complexity we have has some arbitrary necessity.
*  You know, an additive constant, which is can be arbitrarily large.
*  And so how can we come up with a good theory of how things become more complex if we don't have a good measure of complexity?
*  Yeah, which we need for this one way that people study this in the space of biology, the people that study the origin of life or try to recreate life in the laboratory.
*  And the more interesting one is the alien one is when we go to other planets, how do we recognize this life?
*  Because, you know, complexity, we associate complexity, maybe some level of mobility with life.
*  You know, we have to be able to have concrete algorithms for measuring the level of complexity we see in order to know the difference between life and non-life.
*  And the problem is that complexity is in the IODB holder.
*  So let me give you an example. If I give you an image of the MNIST digits, right, and I flip through MNIST digits, there is some obviously some structure to it,
*  because local structure, you know, neighboring pixels are correlated across the entire data set.
*  I imagine that I apply a random permutation to all the pixels, a fixed random permutation.
*  I show you those images, they will look, you know, really disorganized to you, more complex.
*  In fact, they're not more complex in absolute terms. They're exactly the same as originally.
*  And if you knew what the permutation was, you know, you could undo the permutation.
*  Now, imagine I give you special glasses that undo the permutation.
*  Now, all of a sudden, what looked complicated becomes simple.
*  So if you have two, if you have humans on one end and then another race of aliens that sees the universe with permutation glasses,
*  What we perceive as simple to them is hardly complicated. It's probably heat.
*  Yeah, heat. Yeah.
*  Okay. And what they perceive as simple to us is random fluctuation. It's heat.
*  Yeah. It's truly in the eye of the beholder. It depends what kind of glasses you're wearing.
*  Right.
*  It depends what kind of algorithm you're running in your perception system.
*  So I don't think we'll have a theory of intelligence, self-organization, evolution, things like this,
*  until we have a good handle on a notion of complexity, which we know is in the eye of the beholder.
*  Yeah, it's sad to think that we might not be able to detect or interact with alien species because we're wearing different glasses.
*  Because the notion of locality might be different from ours.
*  Yeah.
*  This actually connects with fascinating questions in physics at the moment, like modern physics, quantum physics,
*  like questions about like, can we recover the information that's lost in a black hole and things like this?
*  And that relies on notions of complexity, which I find is fascinating.
*  Can you describe your personal quest to build an expressive electronic wind instrument, EWI?
*  What is it? What does it take to build it?
*  Well, I'm a tinkerer. I like building things.
*  I like building things with combinations of electronics and mechanical stuff.
*  I have a bunch of different hobbies, but probably my first one was little was building model airplanes and stuff like that.
*  And I still do that to some extent, but also electronics.
*  I taught myself electronics before I studied it.
*  And the reason I taught myself electronics is because of music.
*  My cousin was an aspiring electronic musician and he had an analog synthesizer.
*  And I was basically modifying it for him and building sequencers and stuff like that for him.
*  I was in high school when I was doing this.
*  How's the interest in progressive rock, like 80s?
*  What's the greatest band of all time, according to Yann LeCun?
*  There's too many of them.
*  But it's a combination of the Mayavishnu Orchestra, Weather Report, yes, Genesis, Peter Gabriel, Gentle Giant, things like that.
*  Great. OK, so this love of electronics and this love of music combined together.
*  Right. So I was actually trained to play Baroque and Renaissance music.
*  And I played in an orchestra when I was in high school and first years of college.
*  And I played the recorder, crumb horn, a little bit of oboe, things like that.
*  So I'm a wind instrument player, but I always wanted to play improvised music, even though I don't know anything about it.
*  And the only way I figured, short of learning to play saxophone, was to play electronic wind instruments.
*  So they behave, the fingering is similar to a saxophone, but you have a wide variety of sound because you control the synthesizer with it.
*  So I had a bunch of those going back to the late 80s from either Yamaha or Akai.
*  They're both kind of the main manufacturers of those.
*  So they were classically going back several decades.
*  But I've never been completely satisfied with them because of lack of expressivity.
*  And those things are somewhat expressive.
*  I mean, they measure the breath pressure, they measure the lip pressure, and you have various parameters.
*  You can vary with fingers, but they're not really as expressive as an acoustic instrument.
*  You hear John Coltrane play two notes and you know it's John Coltrane.
*  It's got a unique sound. Or Miles Davis.
*  You can hear it's Miles Davis playing the trumpet because the sound reflects their physiognomy, basically.
*  The shape of the vocal tract kind of shapes the sound.
*  So how do you do this with electronic wind instruments?
*  Many years ago, I met a guy called David Wessel.
*  He was a professor at Berkeley and created the Center for Music Technology there.
*  And he was interested in that question.
*  And so I kept kind of thinking about this for many years.
*  And finally, because of COVID, I was at home. I was in my workshop.
*  My workshop serves also as my Zoom room and home office.
*  This is in New Jersey?
*  In New Jersey. And I started really being serious about building my own eWii instrument.
*  What else is going on in the New Jersey workshop?
*  Is there some crazy stuff you built? Or like left on the workshop floor? Left behind?
*  A lot of crazy stuff is electronics built with microcontrollers of various kinds and weird flying contraptions.
*  So you still love flying?
*  It's a family disease. My dad got me into it when I was a kid.
*  And he was building model airplanes when he was a kid.
*  And he was a mechanical engineer. He taught himself electronics also.
*  So he built his early radio control systems in the late 60s, early 70s.
*  And so that's what got me into. I mean, he got me into kind of engineering and science and technology.
*  Do you also have an interest in appreciation of flight and other forms like with drones, quadroptors?
*  Or do you? Is it model airplane?
*  Yes. Before drones were kind of a consumer product, I built my own with also building a microcontroller
*  with JavaScript and XR meters for stabilization, writing the firmware for it.
*  And then when it became kind of a standard thing you could buy, it was boring. I stopped doing it. It was not fun anymore.
*  Yeah. You were doing it before it was cool.
*  What advice would you give to a young person today in high school and college that dreams of doing something big like Yann LeCun?
*  Like let's talk in the space of intelligence. Dreams of having a chance to solve some fundamental problem in space of intelligence,
*  both for their career and just in life, being somebody who was a part of creating something special.
*  So try to get interested by big questions, things like what is intelligence?
*  What is the universe made of? What's life all about? Things like that.
*  Like even like crazy big questions like what's time? Like nobody knows what time is.
*  And then learn basic things like basic methods, either from math, from physics or from engineering.
*  Things that have a long shelf life. Like if you have a choice between like, you know,
*  learning mobile programming on iPhone or quantum mechanics, take quantum mechanics.
*  Because you're going to learn things that you have no idea exist.
*  And you may not you know, you may never be a quantum physicist, but you learn about path integrals and path integrals are used everywhere.
*  It's the same formula that you use for, you know, Bayesian integration and stuff like that.
*  So the ideas, the little ideas within quantum mechanics, within some of these kind of more solidified fields will have a longer shelf life.
*  They'll use somehow use indirectly in your work.
*  Learn classical mechanics like you learn about Lagrangians, for example,
*  which is like a huge hugely useful concept for all kinds of different things.
*  Learn statistical physics because all the math that comes out of, you know, for machine learning
*  basically comes out of what we got out by statistical physicists in the late 19th, early 20th century.
*  And for some of them actually more recently for by people like Giorgio Parisi,
*  who just got the Nobel Prize for the replica method, among other things, it's used for a lot of different things.
*  You know, variational inference, that math comes from statistical physics.
*  So a lot of those kind of, you know, basic courses, you know, if you do electrical engineering, you take signal processing,
*  you'll learn about Fourier transforms. Again, something super useful is at the basis of things like graph neural nets,
*  which is an entirely new sub area of, you know, AI machine learning, deep learning,
*  which I think is super promising for all kinds of applications.
*  Something very promising, if you're more interested in applications, is the applications of AI machine learning and deep learning to science
*  or to science that can help solve big problems in the world.
*  I have colleagues at Meta, at FAIR, who started this project called Open Catalyst.
*  And it's an open project collaborative. And the idea is to use deep learning to help design new chemical compounds
*  or materials that would facilitate the separation of hydrogen from oxygen.
*  If you can efficiently separate oxygen from hydrogen with electricity, you solve climate change.
*  It's as simple as that. Because you cover, you know, some random desert with solar panels
*  and you have them work all day, produce hydrogen, and then you ship the hydrogen wherever it's needed.
*  You don't need anything else. You know, you have controllable power that's, you know,
*  can be transported anywhere. So if we have large scale, efficient energy storage technology,
*  like producing hydrogen, we solve climate change.
*  Here's another way to solve climate change is figuring out how to make fusion work.
*  Now, the problem with fusion is that you make a super hot plasma and the plasma is unstable and you can't control it.
*  Maybe with deep learning, you can find controllers that will stabilize plasma and make, you know, practical fusion reactors.
*  I mean, that's very speculative, but, you know, it's worth trying because, you know, the payoff is huge.
*  There's a group at Google working on this led by John Platt.
*  So control, convert as many problems in science and physics, biology and chemistry into a learnable problem
*  and see if a machine can learn it.
*  Right. I mean, there's properties of, you know, complex materials that we don't understand from first principle, for example.
*  Right. So, you know, if we could design new, you know, new materials, we could make more efficient batteries.
*  You know, we could make maybe faster electronics.
*  I mean, there's a lot of things we can imagine doing or, you know, lighter materials for cars or airplanes or things like that.
*  Maybe better fuel cells. I mean, there's all kinds of stuff we can imagine.
*  If we had good fuel cells, hydrogen fuel cells, we could use them to power airplanes and, you know, transportation wouldn't be or cars.
*  We wouldn't have emission problem, CO2 emission problems for air transportation anymore.
*  So there's a lot of those things, I think, where AI can be used.
*  And this is not even talking about all the sort of medicine, biology and everything like that. Right.
*  You know, like protein folding, you know, figuring out like how can you design your proteins that it sticks to another protein at a particular site,
*  because that's how you design drugs in the end.
*  So, you know, deep learning would be useful.
*  All of this. And those are kind of, you know, would be sort of enormous progress if we could use it for that.
*  Here's an example. If you take this is like from recent material physics, you take a monoatomic layer of graphene.
*  Right. So it's just carbon on an hexagonal mesh. And you make this single single atom thick.
*  You put another one on top. You twist them by some magic number of degrees, three degrees or something.
*  It becomes superconductor. Nobody has any idea why.
*  I want to know how that was discovered. But that's the kind of thing that machine learning can actually discover these things.
*  Well, maybe not. But there is a hint perhaps that with machine learning,
*  we would train a system to basically be a phenomenological model of some complex emergent phenomenon, which, you know, superconductivity is one of those.
*  Where, you know, think this collective phenomenon is too difficult to describe from first principles with the current, you know, the usual sort of reductionist type method.
*  But we could have deep learning systems that predict the properties of a system from a description of it after being trained with sufficiently many samples.
*  This guy Pascal Foua at EPFL, he has a startup company that where he basically trained a convolutional net essentially to predict the aerodynamic properties of solids.
*  And you can generate as much data as you want by just running computational free dynamics.
*  Right. So you give like a wing airfoil or something shape of some kind and you run computational free dynamics.
*  You get as a result, the drag and, you know, lift and all that stuff. Right.
*  And you can you can generate lots of data, train a neural net to make those predictions.
*  And now what you have is a differentiable model of, let's say, drag and lift as a function of the shape of that solid.
*  And so you can do by gradient descent. You can optimize the shape so you get the properties you want.
*  Yeah, that's incredible. That's incredible.
*  And on top of all that, probably you should read a little bit of literature and a little bit of history for inspiration and for wisdom.
*  Because after all, all of these technologies will have to work in the human world.
*  Yes. And the human world is complicated.
*  It is.
*  Yeah. And this is an amazing conversation.
*  I'm really honored that you would talk with me today.
*  Thank you for all the amazing work you're doing at FAIR at Metta.
*  And thank you for being so passionate after all these years about everything that's going on.
*  You're you're a beacon of hope for the machine learning community.
*  And thank you so much for spending your valuable time with me today.
*  That was awesome. Thanks for having me on.
*  That was it was a pleasure.
*  Thanks for listening to this conversation with Yann LeCun to support this podcast.
*  Please check out our sponsors in the description.
*  And now let me leave you some words from Isaac Asimov.
*  Your assumptions are your windows on the world.
*  Scrub them off every once in a while or the light won't come in.
*  Thank you for listening and hope to see you next time.

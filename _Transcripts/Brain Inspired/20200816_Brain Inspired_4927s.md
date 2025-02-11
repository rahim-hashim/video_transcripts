---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 4927s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 13502
Video Rating: None
---

# BI 081 Pieter Roelfsema: Brain-propagation
**Brain Inspired:** [August 16, 2020](https://www.youtube.com/watch?v=3BvVOM7Ifsk)
*  You have to take attention, the role of attention seriously if you think about backpropagation
*  in the brain.
*  Is there an explanatory account to go from that to our phenomenal awareness?
*  And that's a hard question.
*  Yes, I know.
*  I'm not sure I'm going to convince everybody in this field with my, because it's a very
*  difficult field with very different theories.
*  I really thought I had to quit science, you know, because I wrote papers.
*  Yeah, I thought this is a disaster.
*  This is Brain Inspired.
*  Hello, this is Paul Middlebrooks, and you just heard the voice of Peter Rolfsema, who
*  runs the Vision and Cognition Group at the Netherlands Institute for Neuroscience.
*  I invited Peter on the podcast initially because of his work figuring out how the brain solves
*  the credit assignment problem, which is the problem of how a given synapse or connection
*  between neurons knows how to update its strength or weight so as to learn and improve the behavior
*  of the organism.
*  This is not a trivial problem because adjusting the weight of a synapse affects the activity
*  of all of the neurons connected after that downstream, all the way until the end of the
*  chain and some behavior happens.
*  Deep learning's successful solution to this is backpropagation, which uses simple calculus
*  to propagate an error signal backwards through a neural network to update all the weights.
*  And the success of deep learning has sent neuroscientists into a frenzied search for
*  something comparable in brains.
*  The problem is brains can't do backpropagation the way it's done in neural networks.
*  So there have been many different proposed solutions to how brains could solve the credit
*  assignment problem, and Peter has his own solution, which to me is super appealing because
*  it uses what we know about how brains are structured and how they operate.
*  So we discussed his proposal for how brains solve the credit assignment problem, but learning
*  more about Peter's work, I decided also to ask him about two other topics, one being
*  consciousness and his experiments testing the well-known global neuronal workspace hypothesis
*  for how consciousness occurs.
*  And then the other major topic, he is developing methods to cure blindness by implanting electrodes
*  into early visual cortex that can then stimulate the brain in a precise and coordinated manner
*  to cause a person to experience patterns of phosphines or flashes of light that will allow
*  a blind person to interact visually with the world.
*  Okay, so three main topics today, all of which would be worthy of entire episodes.
*  And you can find the related information in the show notes at braininspired.co.
*  slash podcast slash 81.
*  If you value this podcast and you want to support it and hear the full versions of all
*  the episodes and occasional separate bonus episodes, you can do that for next to nothing
*  through Patreon.
*  Go to braininspired.co and click the red Patreon button there.
*  Guys, I just want to say thank you so much for listening to the podcast.
*  This little show is continuing to grow and that's because of your support and your feedback,
*  which you can give through email to paul at braininspired.co.
*  It is abundantly clear to me that I can't please everyone, but I do want to make the
*  best show possible.
*  So thank you for your help in improving the show.
*  All right, enjoy, Peter.
*  Given your interests, and given what you've worked on, I want to ask what brought you
*  into neuroscience?
*  I have a guess and I want to see if my guess is correct.
*  So actually, I studied medicine.
*  And at some point, I realized that I was really attracted to do fundamental science.
*  And my father gave me a book, Goedel Escher Bach.
*  Oh, man.
*  By Doug Hofstadter.
*  Here it comes again.
*  This book keeps coming up.
*  It hasn't come up in a while, but it does keep coming up.
*  Yeah.
*  And so I read it.
*  And then I thought, okay, I want to know how consciousness works.
*  That was my guess is consciousness.
*  Yeah.
*  What percentage of people do you think enter into neuroscience research because of that
*  desire to know what consciousness is?
*  I have no clue.
*  It's got to be high.
*  I actually have no clue.
*  I think a lot of people pretend that they don't.
*  That's my current theory anyway.
*  I mean, it's a big attraction, of course.
*  I mean, somebody told me there are like three big questions.
*  So very large.
*  So what is the origin of the universe?
*  Very small kind of what is matter?
*  What is matter built from?
*  And exactly in the middle, what is consciousness?
*  Yeah, we're all right in the middle here.
*  Yeah, so good.
*  It always makes me feel better when someone actually admits it.
*  But you work directly on it.
*  And so we'll talk about consciousness here in a little bit.
*  So your background, you've mainly, I would say, focused on what you call perceptual organization.
*  And you've developed this incremental grouping theory, where it accounts for how we can look
*  at some sort of crowded scene and know that we're looking at a single object even when
*  it's occluded by other objects.
*  You give a zebra a bunch of zebras is the example that you often give where some zebras
*  are in front of others, but you still look at the scene and you immediately what seems to be
*  immediately see, oh, there's a single zebra, even though you have things, you bind it all
*  together as if it's one object.
*  So you used to think that it was oscillations that would bind different what you call labels
*  for an object together.
*  But you found out that, in fact, it has to do with firing rates.
*  Could you maybe you just briefly describe that that summary of the work, because it kind of
*  leads into some of the other things that we'll speak about.
*  Yes, so I was I did my PhD in the lab of Wolfsinger in Frankfurt.
*  And we were all excited about this idea that oscillations and in particular, the synchronization
*  of neurons at the at the fine time scale of 40 hertz was responsible for the binding.
*  So the idea was that that neurons that kind of line their spikes up really fire synchronously,
*  that they would do so to code for the fact that they are responsible for representing
*  features of the same object.
*  And those neurons that code for features of different objects, they would kind of fire
*  in asynchronously.
*  That was the idea.
*  And I wrote papers about it.
*  And then I started my first postdoc in Amsterdam.
*  And I wanted to test this and demonstrate for once and for all that synchrony was doing
*  the binding.
*  And so I trained monkeys on a task in which they would have to report what they bind.
*  And for that, I had a task in which the monkeys would have to mentally trace a curve.
*  So the curve was visible on the screen.
*  The animal would have to mentally trace it.
*  He was looking here and he was just kind of thinking along the curve, seeing what is on
*  the other end.
*  And then I would have two receptive fields on that very same curve.
*  And they should synchronize.
*  Then I had another version of the same stimulus.
*  But then it would go through the first receptor field, but bend off.
*  So they would avoid the second receptor field.
*  The second receptor field would be on another object.
*  And then these receptors should not synchronize.
*  Okay.
*  And very disappointingly, I found out that this was not the case.
*  Neurons kind of responded, but the synchrony was completely independent of the level of
*  binding.
*  So actually, I thought it's the end of my career.
*  And there was this annoying effect on firing rates.
*  Because if you analyze synchrony, you'd rather have the firing rates constant.
*  But actually, I found out that the firing rates actually were always a bit higher for
*  the object that the animal was kind of mentally tracing.
*  And after one or two, well, one week or so, I started to realize actually the signal is
*  not in the synchrony.
*  The signal is in the firing rate.
*  So all those neurons that represent features of one object, in this case, the curve that
*  the animal is interested in, they enhance their firing rate.
*  And that was then the start of this incremental grouping idea.
*  It's closely linked to what psychologists call object-based attention.
*  So the idea is that all those features that belong to a single object, that they are labeled
*  in the brain by an inspiring rates, and psychologists basically call it this object-based
*  attention.
*  Now, the idea about object-based attention actually was that this is something that happens
*  in parallel.
*  But we found out actually that that can take quite substantial time before you realize
*  all these image elements that belong to a single object.
*  For most objects that you recognize like this cup, it happens fast.
*  Actually, it doesn't happen instantaneously.
*  You can measure that in subject's reaction time.
*  So if you ask the subject two points, this point and this point, are they on the same
*  object, they will tell you.
*  And if these points are a bit farther apart, they will also tell you.
*  But they take them a tiny bit longer.
*  But then you have these crazy objects like curves that are contorted in which it can
*  take you up to 10 seconds before you realize what is on the same object and what is on
*  a different object.
*  You give the example of an electric cord on a toaster or something that's coiled and
*  wrapped around things and it takes a while to trace out the cord.
*  It's kind of a crazy story how I think incremental grouping theory is...
*  I don't know if it's counterintuitive, but the idea, I'll say the idea and then you
*  can correct me, is that there's this feedforward initial sweep in the visual
*  cortex that goes from V1 up to IT.
*  And then there's feedback recurrent processing.
*  And we've talked on the show multiple times about this feedback activity and how it
*  helps process over time, process objects.
*  And that's part of your story.
*  But another part of your story is...
*  So as you sweep forward in the visual stream, you start off in V1 with very small receptive
*  fields.
*  And there's tons of them and then altogether they cover the entire visual field.
*  But then as you progress in the feedforward sweep, as you go up the visual hierarchy,
*  the receptive fields get larger and larger and larger.
*  And the idea of incremental grouping theory is that your brain uses the available
*  receptive field sizes, whatever is available to fill that space, and then piece all of
*  them together.
*  So at every level, you're trying to piece together an object, but then to piece together
*  the entire object, you're actually putting together different receptive fields from
*  different layers in the hierarchy.
*  I know that I just really bastardized that, but how close is my description?
*  That's exactly right.
*  So and in some cases, like this cup, you probably have in your higher areas, say area IT,
*  you have neurons that recognize this cup.
*  And they know it's one object.
*  So then this kind of tying in different receptive field sizes in IT, where you kind of code
*  just for the overall shape saying that this is a cup and not the telephone or whatever.
*  So that can go actually relatively fast.
*  That's image categorization.
*  If there's another object in the scene, say this pen, right?
*  Now there are some contours that belong to the pen.
*  Some other contours that belong to the cup.
*  And also here are contours that belong to the cup.
*  If I now want to grasp it, I better make sure that I recognize objects of the cup as one.
*  And I don't include kind of contours of the pen, because in that case, I would make a
*  mistake during my grasping process.
*  So if you grasp something, it's not only about the shape, overall shape.
*  It's also about what belongs to that cup and whatnot.
*  And in the case of a pen and a cup, that's relatively simple.
*  But there are cases, imagine that you're looking into a box with several elongated objects.
*  There you sometimes really have to work it out.
*  And then you get really tangible incremental grouping with long delays.
*  So in many cases, we measure those delays in psychophysics.
*  In the example that I just gave.
*  So there are two dots on this cup.
*  How long does it take you to realize that they're on the same cup?
*  It goes fast.
*  But there are cases, say, even some natural scenes where it can take several hundred
*  milliseconds before you work it out what belongs to what.
*  And that's incremental grouping.
*  So usually, incremental grouping goes fast.
*  Maybe it's worked out in 150 milliseconds.
*  In some cases, it's much lower.
*  It takes up to a second or even several seconds.
*  And these are not the typical cases.
*  And I actually think that we make eye movements about three times a second.
*  So the typical time that you spend on the snapshots of what you see is 300 milliseconds.
*  That's way too long for just feed forward processing.
*  So that's feed forward processing plus a little bit of this incremental grouping process,
*  this recurrent processing before you work out where it's strategic to make your next time
*  movement.
*  And then you repeat this process over and over again.
*  And part of the story also is learning.
*  As you're looking at an object and processing it and realizing it's a single object,
*  there's learning going on while it's being processed.
*  Could you explain?
*  So why do you need learning?
*  So I'm really interested in how the brain wires itself up.
*  Right.
*  So how do you produce all the connections between, say, the visual cortex and the
*  motor cortex that makes you do the things that will ultimately give you a reward and
*  avoid the things that will ultimately give you punishments?
*  Now, there are theories that try to explain how the brain wires itself up,
*  that only take into account basically the outcome of the trial in terms of whether it's
*  a reward of punishment.
*  And then there is kind of a global signal.
*  And there are like the dopamine neurons in the ventral tegmental area.
*  And they're part of the substantial nigra that seem to code for this what is called
*  reward prediction error.
*  If you get more rewarding than you expected, these neurons fire.
*  Right.
*  And that would be a learning signal that is kind of threw out to brain telling all the
*  synapses, hey, this was better than expected.
*  Better do it again in the future.
*  Yeah.
*  And the other way around, too, if it's kind of disappointing or you get a punishment,
*  there might be other neuromodulatory systems, although we don't understand those as well
*  yet.
*  That kind of tell to all the synapses, hey, better avoid that in the future.
*  That turns out if you make a learning rule, sort of a heavy learning rule where plasticity
*  depends on the pre and the post-synaptic side, plus this neuromodulator, learning is not so
*  good.
*  It's just it seems to misinformation.
*  And what we found and also worked on in models is that if there is a kind of a wave of activity
*  from the visual cortex to the motor cortex, and the motor cortex is competition between
*  the different actions, say motor program A and B.
*  If you then choose motor program A, if you then use feedback from the motor program A
*  to all the neurons in the lower levels that gave rise to the choice of motor program A,
*  so this is the feedback wave, and use the feedback wave to label all the synapses that
*  are going to be held responsible for the outcome of motor program A.
*  So they are basically tagged.
*  These synapses are tagged.
*  They're going to be held responsible.
*  Now, you're going to take motor program, you're going to do action A motor program A,
*  you're going to execute it.
*  Suppose it's good, better than expected.
*  Then all the synapses that were previously tagged in the feedback sweep,
*  they are going to increase in strength.
*  If it was worse than expected, they're going to decrease in strength.
*  It turns out that now we have four factors in our learning rule.
*  We have the pre and the post.
*  We have the global neuromodulator telling all the symptoms in the brain.
*  It's it was good or bad.
*  Plus the feedback wave that tells all the synapses they are responsible for the action,
*  that you get something that is equivalent to error backpropagation.
*  It basically has almost the same convergence properties as backpropagation.
*  So actually in recent work, we have used this biologically plausible version of backpropagation
*  to train networks on tasks that are benchmarks that are used by people who are in deep learning.
*  It turns out that you get basically the same learning rule, only it's a bit slower
*  because we don't have a teacher.
*  If you're outside the reinforcement learning context and you do just standard backpropagation,
*  you give a picture, say of a horse or a zebra to a network,
*  and then you tell the network in the output layer where there are 1,000 neurons,
*  one of them for the zebra, one for the horse, one for a dog, and so on and so forth.
*  You present the zebra and you say, oh, this should have been zebra,
*  but this is reinforcement learning.
*  So the network has to discover that for the picture of a zebra, it should try many,
*  many different actions before it stumbles onto the zebra.
*  Now, given these expected slowdown, it's surprising that it's only a factor of two to three slower
*  than standard error backpropagation.
*  So that's the price you pay for getting rid of the teacher.
*  But other than that, it's basically equivalent to error backpropagation.
*  Well, so there's a lot of things to cover.
*  So you just summarized your solution to backpropagation in the brain.
*  And I want to come back to why learning is necessary.
*  So in your cup example, when you show me the cup and maybe you put a pin in front of it,
*  right?
*  I know what a cup is and I see the cup and even though the pin is in front of it,
*  my brain registers cup at over 150 milliseconds or something like that.
*  But why do my synapses need to change?
*  Or are you you said that you're interested in how the brain wires itself up?
*  Are you more interested in the developmental aspect as I'm a child and learning about the world?
*  Or is it also within adults who know what cups are and you look at a cup and then your brain
*  still tags all of the synapses for learning, even though it's just confirmation?
*  Yes, that's a cup.
*  Is there learning going on in that scenario?
*  Probably not.
*  So if your brain is mature and you know what a cup is, then there is no reward prediction error
*  anymore.
*  Even though all those synapses are labeled, there's no reason because there are nothing
*  unexpected about the cup in your behavior.
*  There are other scenarios.
*  There are two other interesting scenarios in this context.
*  One is a young brain that needs to learn about cups.
*  Then it's pretty relevant, right?
*  And then these mechanisms might be at work.
*  Another scenario is that two more scenarios, actually.
*  One scenario is if there's something like a cup that is just a little bit different from
*  the cup you're expecting.
*  So maybe it's a special cup and you need to really learn about it because it's different
*  and it's very relevant for your behavior.
*  That could happen.
*  And another situation is it's not learning about a cup anymore, but it's learning about
*  the behavior that should be associated with the cup.
*  So maybe in some cases, all the visual categories have been worked out.
*  You know what it is what you're looking at, but you still need to use it in a strategic
*  way in your behavioral program.
*  And then the learning is probably not taking place in the visual cortex, but it could be
*  taking place in other places of the brain.
*  But the learning principles, error backpropagation or its biological equivalent might still be
*  the same.
*  All right.
*  So let's talk about backpropagation.
*  There's this recent flood, I would say, of people trying to figure out how backpropagation
*  works in the brain.
*  And you've been actually working on this for years.
*  I'm kind of wondering if I'm right in thinking that there's a recent surge.
*  I mean, it seems apparent to me, but also just your thoughts on this recent surge because
*  you've been working on it for years before we get into the mechanics of it all.
*  Do you see this as a massive flood right now in trying to figure out how, quote, unquote,
*  backpropagation works in the brain?
*  Yeah.
*  And it's really interesting to see this.
*  So it's, of course, inspired by the huge success that machine learning now has in doing all
*  kinds of tasks, computer games, language translation, and so on and so forth.
*  So people are taking it much more seriously than, say, 20 years ago.
*  And it's really nice to see that now many people are thinking about deep learning and how we can
*  use it to get more insight into learning in the brain.
*  And it's true.
*  We already worked on this in 2005 when we published our first paper about it.
*  Was that the agri-roll?
*  So we now refined it.
*  We now have a new version we call brainprop.
*  I thought it was Q agri-roll is the latest thing.
*  We have several versions.
*  So even newer.
*  Yeah.
*  But I mean, the basic rule is still the same.
*  You use the feedback connections from higher levels, the motor program that gets selected
*  to lower levels to highlight those synapses that are going to be health responsible.
*  But we now worked it out also how to do it efficiently for multiple layers for a network
*  with more than three layers.
*  So it can be as deep as you want.
*  And it's still basically, as I said, we completely got rid of the teacher.
*  So many of the new developments, they still are using a teacher and they're giving nice,
*  nice insights.
*  So there are something called equilibrium prop and some other variants of it.
*  I think it's very interesting, but they're still using a teacher.
*  There's always the question, how exactly would that happen in the brain?
*  What's the teacher in the brain?
*  Right.
*  And so you guys get around that.
*  There's no teacher.
*  There's no teacher.
*  So we really have to take that constraint also more seriously.
*  And I think then what we have is probably the best game in town.
*  So, okay, great.
*  Well, I like your, I mean, I agree with you actually.
*  What are other people that are working on back propagation in brains?
*  Everyone's got their own solution.
*  There's equilibrium propagation, there's feedback alignment, there's, you know, you name it.
*  What's your take on how people perceive your solution?
*  I've been in contact with a number of influential people in this work.
*  We had a conference on Barbados on this and we actually wrote a report about it that was
*  published in Nature Neuroscience.
*  Yeah, I think it's pretty well known.
*  Yeah.
*  So I think people like the idea.
*  And actually, I think it's gradually, you need to understand it maybe.
*  And of course, the people in machine learning, they come sometimes from a different angle
*  and you have to align the terms that you use.
*  But I think it's people are starting to take it more seriously now.
*  Well, I want to ask about the different angles, the different perspectives from machine learning
*  and from neuroscience.
*  It struck me that most back propagation approximations, solutions for brains,
*  have tended to come from the machine learning side and to have that perspective
*  and start with the back with classic back propagation mechanism and then figure out
*  maybe how a brain might implement it.
*  And it seems like you consider you come from the brains perspective.
*  You consider what we know about brains and then figure out, well, how could something
*  like back propagation occur?
*  Would you agree with is there a difference in perspective?
*  Because I think that it leads to different solutions.
*  And so one important thing is, of course, I've been working in attention and have been
*  thinking about the role of feedback, say, in object-based attention.
*  We talked about it in the beginning.
*  And something that is evident also to psychologists is that if there are several things and several
*  actions that you can take, you take one action towards a particular object, that object will
*  have attention.
*  There are very important papers on that, for instance, from Heinrich Darbel, Elin Kowler,
*  and others that demonstrate that if you direct your eyes or make a grasping movement towards
*  a particular object, that's the one that will be in your attention.
*  We also know that individual cortex, these features that belong to those objects, they
*  will be labeled by extra activity.
*  There is basically feedback to those neurons.
*  Now, we also know that attention gets learning.
*  So actually, we carried out a study a few years ago in which there was the same information
*  on the left and the right.
*  It's called redundant cues.
*  So you can basically learn the task based on the information on the left.
*  You could also learn a task based on the information on the right.
*  There was equivalent.
*  But we cue the subjects to pay attention to only one of those sites.
*  They only learn about the one they pay attention to, even though the reward
*  continuities, everything is the same.
*  I think that's an indirect evidence that you have to take attention, the role of attention,
*  seriously if you think about backpropagation in the brain.
*  All these things align.
*  I think it's very strong evidence that these feedback connections are
*  a gate to learning.
*  I consider it very strong evidence for this brain prop or agri-learning rule that we've been proposing.
*  Well, you already described it once, but let's do it again just to be clear before we move on
*  how your solution works.
*  So maybe you can describe it again and then we can move on.
*  Yeah.
*  So it's about linking sensory codes to motor actions.
*  And there can be many layers in between.
*  Now, in the beginning, when these layers are entrained on the motor side of things,
*  you could choose, say, one out of 1,000 actions, a certain limited number of actions.
*  If you then choose an action, those neurons that go for that action, they're going to provide
*  feedback to those neurons in the sensory cortex and all the intermediate stages that
*  gave input to this action and that therefore are going to be held responsible for the outcome
*  of the action.
*  The winner of the voting process to take the action then is activated and that activation
*  then feeds back.
*  That activation feeds back to all the synapses that gave input.
*  Okay.
*  Now, if it's better than expected, there will be a release of neuromodulators like dopamine,
*  but that's relatively global.
*  So it floods the brain with dopamine.
*  But only those synapses that were involved in the sensory motor mapping, so that received
*  a feedback signal, they are going to increase in strength.
*  And all the other synapses that are completely independent, not responsible for this particular
*  action, they're not going to change the synapse, although they see the same level of dopamine.
*  Turns out now, so we're looking at the pre and the post-synaptic activity.
*  We're looking at whether this post-synaptic neuron received feedback from the response
*  selection stage.
*  That's a third factor.
*  A fourth factor is the level of neuromodulator.
*  So all these signals are present at the individual synapse.
*  And then it turns out that if you kind of put them together, you get something that
*  is equivalent to air back propagation, but you don't need a teacher anymore because you're
*  in a reinforcement learning scheme.
*  Most of the time, it seems when people are describing how learning might work in the
*  brain, they say either it's neuromodulators, either it's like a reward prediction error,
*  some sort of perturbation on the synapses, or there must be very specific back propagation
*  happening.
*  It seems obvious to me that everything what we know about the brain is that everything
*  is going on.
*  You're getting the reward prediction error, you're getting the neuromodulators, you're
*  also having this top down feedback.
*  And so I don't know, it just seems like a very natural solution to me.
*  So we agree.
*  Yes.
*  That's good.
*  So I mean, one of the issues, I mean, there's lots of work still to be done on this stuff,
*  but one of the issues is the effects of time because the way that your networks work,
*  there's still a feed forward sweep.
*  And that's like step one.
*  And then so there are like multiple steps and then there's a feedback sweep.
*  I'm wondering if this is something where so in your network at the end stage, there's
*  an action, the unit gets activated and you choose the action.
*  And then there's the feedback signal, but you have to take in eventually will have to
*  take into account time, right?
*  I'm wondering if confidence might come into play as an additional factor that sort of
*  happens over time because still in the network, there's a decision, but it's a discrete event.
*  Whereas maybe confidence could be a lingering activity that's still propagating through
*  the network in how you think you might have done labeling that cup or zebra versus how
*  it actually turns out because you everything is running continuously and dynamically.
*  So you have to have this continuous sort of signal because it's not they're not discrete
*  events.
*  And I don't know, I'm just wondering what you what you might think about some sort of
*  signal that continues on because you have to hang on to the decision to then know whether
*  it was right or wrong to get the reward prediction error to update the synapses.
*  So there are several aspects that you bring up that all need to be addressed.
*  So the first is about the timing question, right?
*  So one of the questions that you could have is that by the time the feed forward propagation
*  is done, the action gets selected and then you need to still have to process the feedback.
*  There are some delays, right?
*  Are they detrimental?
*  So we actually with David Sanbrano and Sander Botte, we did a study on that and it turns out
*  that within kind of physiologically plausible measures of these propagation times, that's not
*  an issue.
*  So that's part of my answer.
*  The other thing is also important to realize that during the first feed forward sweep and
*  then the feedback, that all goes relatively fast, maybe within 100 to 150 milliseconds,
*  maybe a little bit longer, then the synapses get labeled.
*  But maybe the stimulus is gone by the time you get kind of the reward or no reward.
*  The good news is that by that time, you don't need the activity patterns to be there anymore.
*  And actually, there are some indications that by that time, these coincidences that
*  synapse was involved in a particular action is locally stored at the synapse, maybe by
*  some biochemical markers.
*  So there are some candidate mechanisms for that.
*  So the activity pattern of the network by that time can be different, but there are
*  still these biochemical traces that these synapses are going to be held responsible.
*  But it's not necessary for the pre and post-synaptic neuron to be still spiking.
*  So that's the second, maybe partially answer to your question.
*  And then you talked about confidence and confidence and reinforcement learning have
*  something to do with each other.
*  So if you do something that you have done all the time and you know what to do, so you're
*  highly confident and you take an action, then you kind of have a good expectation of what's
*  going to come out.
*  And in that case, even before you execute the action, you have a very good prediction of
*  the amount of reward or the consequences.
*  So in those situations, there's basically hardly any reward prediction error left.
*  If you're not confident, for instance, you're already in the learning phase and you're
*  still trying out, you don't know what you should do, then you're not so confident.
*  And in those situations, you get reward prediction errors.
*  So then the whole learning machinery can take its effect.
*  How do you see your backpropagation alternative solution?
*  How does it fit compared to the many solutions that are out there right now?
*  I think ours is the way the brain does it.
*  So I'm pretty confident about that.
*  So I think the ones like equilibrium, equilibrium propagation, for example, they still need a
*  teacher and it doesn't work as well as ours.
*  So they should just kind of take more of the neurophysiology into account, realizing that
*  these feedback connections are important for selection and also maybe for the taking of
*  synapses.
*  Well, it does align well with the multi-compartment unit type models.
*  People like Tim Lillycraft and Blake Richards are working on where there's an apical dendrite
*  that's sort of isolated from the soma of the cell that gets the feedback.
*  And then depending on the incoming activity to it, then it can update the synaptic weights at the
*  soma, depending on whether it's bursting, etc.
*  And that aligns pretty well with your work.
*  Yes.
*  So I think that part, we basically have a similar view.
*  And that is basically a story about how feedback connections work.
*  So feedback connections go to different layers than feed-forward connections and they are
*  modulatory rather than driving.
*  And so that's a story about how feedback connections work.
*  So I think the different theories have the same thrust.
*  I think our contribution is that it's related to what psychologists call attention.
*  It's related to the selection through feedback and the realization that you don't need a teacher.
*  You can just solve it in a reinforcement learning context.
*  I feel like, whatever, 10 years from now or whenever the story ends about how something like
*  backpropagation happens in the brain, and I'm being sort of pessimistic, I feel like the AI folks,
*  the people on the machine learning side, when that happens, will eventually, whatever the
*  solution is, they'll say, see, it's like backpropagation.
*  When in reality or when what I conjecture will happen is that neuroscience will figure out the
*  solution.
*  I mean, I know that there's a lot of cross talk and machine learning has been very influential
*  and helpful, but there will eventually be a solution to the credit assignment problem in
*  the brain, and it will be pretty far removed from what literal backpropagation is.
*  And so we will arrive at a solution, and it will look like a solution that neuroscientists
*  probably have been working on for a long time, and yet I still feel like the AI side will say,
*  see, it's like backprop.
*  I don't know.
*  Where do you come down on that?
*  I think it's actually, I'm not so pessimistic.
*  So I think it's pretty exciting, actually, that we take the AI folks seriously, so we
*  use their models to understand the brain codes.
*  Yeah.
*  And I have the feeling that they take us seriously as well, right?
*  So they really would like to know how a neuron can do that.
*  They have all kinds of interesting ideas of how you can use these neural mechanisms.
*  And so this is a very exciting time where people from AI and people from neuroscience
*  really talk to each other.
*  And I think we need this.
*  We need their insights because the brain is such a distributed system that it's very hard
*  to make sense how it all fits together without these kind of guiding theories.
*  Yeah.
*  I think I'm not concerned with it.
*  I think I'm observing what I take to be the hubris of the machine learning side.
*  So when backpropagation became big in the 80s, and then there's this backlash, well,
*  it's not biologically plausible.
*  And then since then, even in your latest paper, the term biologically plausible is in the title
*  in one of your recent papers.
*  I just think eventually the answer to the backpropagation approximation in brains is
*  going to be so different than what backpropagation actually is that it won't be fair to say that it's
*  backpropagation-like even.
*  Maybe I'm just concerned with the credit that's given to finding the solution of how brains learn.
*  So I think the machine learning community is going to take credit for it.
*  And I don't want them to.
*  I'm a neuroscientist, right?
*  Okay.
*  You don't care because we're all in it together, right?
*  We're all trying to figure out how everything works.
*  But it's just interesting socially to think about how it's going to play out in that respect.
*  The history, how the history is going to be written.
*  Yeah, I think there are similar stories for backpropagation itself, right?
*  It also has multiple fathers and people debate on who was the original inventor of it.
*  And so thinking deeply about how this works in the brain, for me, it's just interesting
*  scientific questions.
*  So I rather focus on that.
*  What do you think?
*  So I've had a few people on the podcast who have taken Umbridge with the phrase biologically
*  plausible.
*  They don't like that term because we don't actually, the argument is that we don't actually
*  know what's biologically plausible.
*  And when people use that phrase, it's fairly meaningless.
*  But people use the phrase to promote their work as being more important.
*  And you use the phrase and I think I'm sure I've used it multiple times.
*  Do you have a thought on that?
*  Oh, no, I may reconsider using this phrase.
*  I never thought about it this way.
*  I hadn't either.
*  Yeah.
*  So in this specific case, I think it's a really important question to ask how the brain with
*  its many layers between input and outputs can train itself.
*  Also, I mean, people realized, I realized many years ago that it's not going to be back
*  propagation because it's not a teacher who's going to tell the neuron in the motor cortex
*  who should be active and who not.
*  And there are many areas in back propagation where the feedback is basically, according
*  to back propagation, would have to propagate error signals.
*  And we know in areas these error signals do not exist.
*  Now the news is that we do know what is being propagated is attentional signals.
*  And therefore, the insight that we have is that if you combine this local attentional
*  signal, that's a local signal with this global signal that tells all the neurons in the brain
*  and whether it's better or worse than expected, turns out that you have, you can basically
*  partition the back propagation equation in this attention part and in this neuromodulatory
*  parts.
*  And then you can have at the individual synapses all the information that you need for the
*  synaptic update.
*  I think that's the insight.
*  I don't have a problem with the term biologically plausible, but I wonder if the term
*  not biologically implausible would be more satisfying to people who don't like the term
*  biologically plausible because back propagation is biologically implausible.
*  It just doesn't exist.
*  And it's so strange when people insist on saying it could exist because no, it actually
*  can't exist when you look at brains and how they work.
*  Maybe not biologically implausible is the way to go.
*  What for me is important is that people get this insight.
*  So you need a certain number of error terms or pieces of information at the synapse.
*  Pre and post synaptic activity, that's easy, right?
*  That's what the synapse does.
*  But our back propagation says you need something more.
*  And the nice thing is that you can partition this into an attentional signal that is locally
*  specific, but doesn't tell whether it's better or worse than expected.
*  It's just kind of, hey, the synapse was involved in this particular action.
*  And then there's a global signal that is agnostic about specific synapses.
*  It just tells all the synapses in the brain is better or worse than expected.
*  Turns out then you have everything in the synapse that you need to do
*  something that is equivalent to back propagation.
*  I think the tricky part in the details is the wiring and that you still need,
*  so you don't have symmetric feedback signals.
*  It doesn't go reverse direction down the synapses and then feedback.
*  But you still need a feedback network that from the output, you still need the network
*  to feedback onto all of the synapses that were responsible for that output.
*  So I think that's a complicated structural problem, but there's a lot of connections
*  in the brain.
*  So that's solvable.
*  Yes.
*  And we know it has been solved by the brain.
*  So there are two aspects to this.
*  The first is you can set this up.
*  You don't need to set this up at the level of the individual neuron,
*  this reciprocity of connections.
*  If you do it at the level of the cortical column, it's pretty plausible.
*  So I think there's good evidence actually that columns of neurons that feed to other
*  columns of neurons in one direction typically also get a feedback in the other direction.
*  Okay, so that's kind of theoretical hand waving.
*  Now, what about what we measure in the brain?
*  So we just see those signals, right?
*  So imagine doing a curve tracing task where all kinds of lines are interconnected
*  and the monkey has to mentally trace one curve over another curve.
*  It turns out that we find those feedback signals precisely at all those image elements
*  that belong to the object that is being selected by the animal.
*  Same is true for visual search.
*  So if you're looking for something yellow, then even at the level of V1,
*  neurons that respond to the color yellow, they will enhance their response.
*  So the feedback does have this.
*  It has exactly those properties that you need.
*  So we know from the neurophysiological point of view that this is what is going on in the brain.
*  And we know through theoretical, what I call theoretical hand waving,
*  that you can make this work at least at the level of the column.
*  So I'm pretty confident that this is the way it works.
*  In your earlier work, you used a three layer network with basically one hidden unit layer.
*  And you were performing tasks that monkeys perform that we use in neuroscience, right?
*  And this more recent work, you've now stepped up the number of layers and you've shown mathematically
*  that you can do it in very deep networks.
*  And you've also started using the benchmark tasks that are famous in machine learning
*  and shown that, yes, like you said earlier, the price you pay is that learning is a little
*  bit slower, but then you still get very good performance and learning eventually.
*  So now what? What's next?
*  So there has been some beautiful work demonstrating that these networks, for instance,
*  can do computer games.
*  So that would be interesting to have a rich input because in the work with three layers,
*  we basically pre-digested the inputs and made it very easy for the network to know what the
*  input patterns are that it should care about.
*  So I think that would be an interesting direction for us.
*  Something else that I'm interested in is, I think,
*  Bob Finick had a really nice paper about it.
*  It's called Learning to Learn.
*  Metal learning.
*  And it's one of the ideas is that if you start the right information in working memory,
*  you can rapidly switch between tasks.
*  And that's very different from, say, reversal learning in which you learn a RAD to kind of
*  have a certain stimulus that maps into response A and another stimulus that maps into response B.
*  That requires the RAD to learn over hundreds of trials and then you reverse contingencies.
*  And then the RAD has to relearn, rewire the system and so on and so forth.
*  But at some point, the RAD realizes, hey, there are two contexts.
*  I'm in context one and then the stimulus maps onto A.
*  That's called learning to learn, right?
*  So you replace the necessity to rewire the whole system by simple context nodes,
*  which is probably something in working memory.
*  And I think that's really interesting.
*  So I mean, something that I didn't dare to dream about modeling, but I'm now thinking,
*  I'm starting to think about it is, if you tell somebody, you know,
*  I'm going to put you in front of a monitor and this is going to happen,
*  the subject can just do it, right?
*  So it can understand the instructions.
*  It's probably going to be a pattern of activity in the working memory that
*  enables the flexible links between sensory inputs and motor responses that are required later.
*  I think that's very related to learning to learn.
*  So I think that's also a really exciting direction to think in.
*  It is.
*  Is this the most exciting time to be figuring out how brains work?
*  Is this the best time?
*  Is this the best age ever to be in?
*  I think so.
*  It's a lot of fun.
*  Yeah.
*  I wonder if we're going to look silly in a hundred years looking back.
*  We really think we're figuring it out, don't we?
*  To some extent, yes.
*  Well, sure.
*  The humility of a neuroscientist.
*  I love it.
*  Well, Peter, let's talk about one of your first loves here in consciousness,
*  because you've done some experiments recently that I suppose support the global
*  neuronal workspace hypothesis of consciousness.
*  I don't know if you want to, I don't even know if we've described it on the show before.
*  Maybe you could just summarize what the global neuronal workspace hypothesis is.
*  And then I'm wondering, are you fully on board with this as the
*  correct accounting of consciousness?
*  So, yeah.
*  Put you on the spot.
*  Let me try to introduce the idea.
*  And it's not unrelated to recurrent processing.
*  I think every neuroscientist realizes that there are many processes in the brain distributed
*  across many cortical areas.
*  And that's for coherent behavior to come out, you need to connect the nodes.
*  Something needs to happen so that motor cortex and visual cortex start to talk to each other
*  to get meaningful behavior.
*  Then there was, I think, Stan De Haene, he's basically the godfather of global
*  neural workspace theory, although there are also earlier versions of it,
*  for instance, by Bernard Barz.
*  Barz, yeah.
*  And he doesn't get mentioned as much these days.
*  It's always De Haene.
*  Of course, these good ideas always have a whole history.
*  Sure.
*  And what Stan suggested also is that there are all these processors.
*  And he had this extra idea that there is something that he calls ignition.
*  Ignition, yeah.
*  And ignition basically means that a weak sensory stimulus, if it reaches a certain threshold,
*  then it becomes reportable, visible.
*  And these are actually later turned out to be too related, but maybe different things.
*  So visible means basically what people later called phenomenal consciousness.
*  And reportable means what people later called access consciousness.
*  And there are big debates about still the use of these terms and which brain structures
*  are responsible for the two types of consciousness to the degree that they might be separable.
*  When you say ignition, what it's igniting is a global, it's in the name of the phenomenon,
*  but it is a sort of a massive recurrent processing that covers lots of different
*  areas of the brain.
*  So it ignites into this what's called the global workspace.
*  And then there's just enough processing that you're conscious.
*  Is that how it works?
*  Yeah, so I just started to scratch the surface.
*  So of course, the ideas behind it are much deeper.
*  So there, I would like to describe two situations.
*  And I like the curve tracing task because I worked on it,
*  but you could also take a different task.
*  So in the curve tracing task, you have one curve that you mentally trace.
*  Maybe there are some distractors that you're not interested in.
*  You want to know what is on the end of this curve that starts here.
*  So as long as the stimulus is on the screen,
*  you will find that in the beginning, the whole display gets registered.
*  So all the curves on the screen get registered.
*  That's the feed-forward sweep.
*  It goes all the way even to frontal cortex.
*  If it's a strong stimulus, all these stimuli are also,
*  there are frontal neurons that code for these different visual aspects.
*  Now, if you're interested in only one of those curves,
*  for instance, because it's the one that's connected to the fixation point,
*  that curve is going to be over-represented,
*  and the other curves are going to be suppressed.
*  So that's what psychologists call attention.
*  And for me, that has a close resemblance to what is then in your consciousness.
*  And that has also many relations to recurrent processing.
*  There's now a link between the frontal cortex that over-represents this curve,
*  and that feeds also back to lower levels, even to the level of V1,
*  where all these contour elements that belong to that curve
*  are also represented in an amplified fashion.
*  So for me, that is recurrent processing.
*  And this is related to the global neural workspace theory that posits
*  that there are processors for different features in this particular case.
*  Maybe the local features, the local line elements in V1,
*  the overall shape of the curve, maybe an IT cortex.
*  Maybe your plan to make an eye movement to the end of this curve in frontal cortex
*  and other aspects in frontal cortex.
*  All these processors are active, and they have recurrent links.
*  So that's my rendering of global neural workspace theory in the presence of a curve.
*  Now suppose I present only these curves very briefly, and they're gone.
*  Then you can still process them to some degree,
*  although at some point you will find out that your processing is more limited
*  than if these things are still visible.
*  And in those situations, there are still processors that can be active,
*  and they can represent features of a curve no longer visible,
*  and then it's working memory.
*  It turns out that many of these neurons that are active in the first case
*  are also active in the second case, although there are also huge differences.
*  For instance, in V1, you only find a very weak trace of the stimulus
*  that was still there.
*  There are still some working memory signals even in V1, but it's not so pronounced.
*  Now in those situations, the processors that are contributing to the conscious process,
*  they kind of relate strongly to what psychologists call working memory.
*  And in the brain, it's persistent activity.
*  These neurons are persistently active.
*  And now about ignition.
*  So ignition, I think, are all these processors that are part of this distributed
*  representation of the thing that is in your consciousness.
*  And ignition becomes really important in the cases in which the stimulus is only briefly visible,
*  or perhaps only weakly presented.
*  So then you can get a bifurcation in which, say, a very weak stimulus,
*  that's what we used in a paper not so long ago,
*  in which we presented stimuli that were close to the thresholds of perception.
*  Very quickly flashed on the screen, right?
*  Yes, and also weak.
*  So then the same stimulus, sometimes you'll see it and sometimes you don't.
*  And that's interesting, right?
*  Because then you have the same stimulus that gives rise
*  sometimes to a conscious percept of the stimulus and sometimes you fail to see it.
*  So therefore, it's just a nice experimental paradigm.
*  And what we then found is that the ones that kind of make it into consciousness
*  are going to be reportable.
*  These are the ones that are then amplified and also visible at the level of the frontal cortex
*  as a persistent firing rate.
*  So they basically made it into working memory.
*  And those that were not going to be reported, in this case by a monkey,
*  they kind of gave rise to weaker propagation from V1 to frontal cortex,
*  basically unable to reach this stage of ignition.
*  And they basically failed to make it in working memory.
*  So that's where the ignition idea comes into play.
*  As if there's sort of a threshold, if you cross that threshold,
*  you get sort of an amplification and you get a stable representation in working memory.
*  If you fail to reach that threshold, the information is lost.
*  So that's basically the relationship between global neural workspace theory,
*  visible and only temporarily presented stimuli.
*  And also I talked a little bit about how we approach these questions.
*  And you found some evidence that favors this theory.
*  Yeah, so that's basically the experiment I kind of indirectly described
*  in which we presented weak stimuli.
*  And what we found basically is the stimuli, if they're going to be reported,
*  they are propagated, there's some stochasticity in the propagation from V1 to V2 to V4,
*  and so on and so forth.
*  And there was also a prediction of Stan De Haene in his renderings of his version
*  of the global neural workspace theory.
*  And we basically validated that prediction.
*  That's precisely what came out in our experiment.
*  So that was kind of exciting.
*  Yeah, I love in your talks how exasperated you seem
*  that he just made a really quick model in an afternoon, you say,
*  whereas it took you a little bit more than an afternoon to perform the experiments
*  and gather the data and analysis.
*  Serious modeling envy.
*  I've had that as well.
*  So then the second part of my question, are you fully on board with
*  the global neuronal workspace hypothesis as an accounting of consciousness?
*  I'm putting you on the spot here because I can.
*  Yeah, I think I like the idea.
*  I always like the idea and I like the relation between...
*  But I like also, and maybe there are some extra thoughts that I put in
*  because with Victor Lama, we also kind of theorized about this.
*  And so I strongly like the idea that this processor, say in Fontocortex,
*  that sustains the activity and it selects also has its connections to processors
*  at earlier levels, even up to the level V1.
*  And that's related to this idea of object-based attention.
*  So all those features through the feedback that are labeled by enhanced firing rates,
*  that whole that whole all those features are part of your conscious experience,
*  even at the level of V1.
*  And that is related to binding.
*  So this incremental grouping process that I was talking about.
*  And that could be an explanation why the objects that we have in our conscious
*  perception are rich and multi-featured.
*  So I see a strong connection there between incremental grouping
*  and the content of consciousness when the stimulus is there.
*  And the other thing that I've been proposing is that there's a very nice link
*  between what is in our working memory and what is in our conscious perception.
*  In the case the stimulus is no longer there.
*  So is it more, and I apologize because I haven't read up on global neuronal workspace theory
*  in a long time, I've only just, you know, reading your work, re-familiarized myself with,
*  you know, it's in very summarily though.
*  But is it more of an account of the, let's say the neural correlates of consciousness,
*  or does it have an explanatory mechanistic account of qualia, let's say, of phenomenal
*  consciousness of, you know, how you get from that activity, from the ignition and then
*  the global activity, is there an explanatory account to go from that to our phenomenal
*  awareness?
*  And that's a hard question.
*  Yes, I know.
*  I'm not sure I'm going to convince everybody in this field with my, because it's a very
*  difficult field with very different theories.
*  But I mean, it's intuitively very comfortable.
*  Yes, but the thing that I just said goes a little bit in this direction, and that is,
*  that if I say that this recurrent processing that in the frontal cortex gives rise to
*  sustained activity, but also in the visual cortex gives rise to a very rich representation
*  that is labeled basically for attention.
*  And in my view, then that corresponds quite closely to what is in your phenomenal awareness
*  that has explanatory power.
*  But why do we need to be aware of that?
*  However rich of a percept it is, why do we need to experience it?
*  I suppose is, I mean, this is, you know, the age old question, right?
*  Yes.
*  So an indirect answer could be.
*  So there are special types of activity that reflect the fact that, say, a neuron in visual
*  cortex has a special connection to a neuron in frontal cortex.
*  Yeah.
*  And so that is this basically this idea of a global state.
*  And if that has a very special state, what's done called broadcasting, then that is also
*  maybe substance for other thoughts when we think about ourselves.
*  And that might go in the direction of explaining why then this also has this special
*  introspective qualium of, hey, this is on my mind.
*  The qualium, the singular, I like it.
*  How far away are we, do you think, from having a satisfying account of consciousness,
*  subjective, phenomenal awareness, insert, whatever, qualia, for instance, how far away
*  do you think we are from agreeing as a scientific community about the neural underpinnings?
*  If indeed there are neural underpinnings, I guess I have to qualify that.
*  Yeah, that depends on how much you would like to understand of it, because
*  consciousness awareness has many, many layers, right?
*  Some layers, I think we're scratching.
*  So I just gave you an example of a very simple version of a very weak stimulus that can make
*  it or make it not into awareness.
*  I think we have mechanistic understanding of that.
*  The next level is self-awareness or social awareness.
*  I think so there are so many layers of what we call awareness,
*  and we are far removed from deeper understanding of those.
*  Do you think that we have a good grasp on even what it is?
*  There's no it.
*  So if you look at it, it becomes multifaceted.
*  And some parts we start to understand and some parts, I mean, I guess one of the basic
*  questions is why am I now here in this body?
*  And why is it me?
*  What is what is I and what is the substrate of this experience that I have?
*  It's very direct questions that you can only ask yourself.
*  And I think we're very far from answering those.
*  Yeah, I just spoke with Dale Lee and he
*  he believes that subjectivity, because it's subjective, because of our because our phenomenal
*  consciousness is subjective, that it is not available for scientific inquiry, essentially.
*  And that's a frustrating thing.
*  But you think we're on the right track in characterizing.
*  I'm going to say it again.
*  I mean, you know, when you say it, it's almost like it's an object.
*  But you can also think of consciousness as a process and that there's no it there because
*  it is a process.
*  It's frustrating because it's difficult to even talk about what we want to talk about
*  because maybe we haven't characterized it well enough yet.
*  Yeah.
*  So again, there are many layers.
*  Some of them we understand, right?
*  We also understand things about the difference between somebody who's in coma and you hardly
*  has any consciousness and somebody who at least can make all the connections between
*  all the notes in the brain that are necessary for thoughts or for an action.
*  But as I said, there are more difficult layers.
*  And that is also the concept of the self.
*  And then indeed questions that are very deep, like why am I now here and experiencing this?
*  And am I the same person as I was with the same consciousness as, say, two years ago?
*  Or two milliseconds ago.
*  Exactly.
*  Given that so the global neural workspace, it lays out sort of what you need.
*  You need the ignition, you need the broadcasting, and you need this highly recurrent processing.
*  That all seems pretty doable in a machine.
*  Do you think that we're going to do it in a machine?
*  How far away do you think we are from, let's say, the most elementary conscious processing
*  in, I don't want to say deep networks, but we'll just say machines?
*  Yeah. So I think you could probably make machines that have some of these very
*  rudimentary forms of consciousness.
*  Like if there is a weak stimulus, it can go into one of two states,
*  one in which it just sees this and is able to report about it and one in which it did perceive
*  it just because of the stochasticity of the sensors of this, say, robot.
*  And so, but are we going to face ethical problems when we unplug the system?
*  Maybe not yet.
*  I don't know where the boundary is going to be.
*  So I do think that we are heading in that direction for sure.
*  Yeah, I think it's an interesting question.
*  So for instance, if you are going to build very sophisticated robots
*  that have some of this, where we implement some of this neuroscience knowledge that we have and
*  that allow these robots to have a rich interaction with the environment, to have representations of
*  others, humans, robots, and also kind of a conception of itself and its role in the world.
*  It's interesting.
*  At some point, these robots might be claiming their rights.
*  What are we going to do?
*  Unplug, turn the power.
*  Turn the power off.
*  Maybe.
*  So, Peter, we have a few more minutes left here and I want to move on and talk about,
*  speaking of using machine.
*  So we can use machines to aid in our consciousness.
*  And I want to talk about your work in prosthetic vision.
*  So you have these grand plans and you're implementing this idea of being able to
*  stimulate people's V1, really early visual cortex, to give them visual perception.
*  And this would be the idea for people who wouldn't be able to take a retinal implant because
*  there's some damage or some degradation of their processing from their retina to their V1.
*  So your idea is to go in and directly stimulate V1 and give people visual perception.
*  How's it going?
*  How's the project going?
*  First of all, maybe you could describe the project a little bit better than I just did.
*  And then I want to know how it's going.
*  So it's an old idea.
*  It started with the work of Giles Brindley and Dobele worked on it.
*  There are now multiple people on the world who do related projects.
*  I think we made a big step recently.
*  What we did is we implanted 1000 electrodes.
*  It's this Utah probe that is made by the company Blackrock.
*  It's a small chip.
*  And the version that we implanted in monkeys has a total of 64 electrodes.
*  We implanted a whole bunch.
*  We implanted a total of 16 of those.
*  So many.
*  Yeah.
*  So that adds to more than 1000 electrodes.
*  How long was that surgery?
*  It took about eight hours.
*  Yeah.
*  Okay.
*  That's not bad.
*  I mean, we have done this before.
*  So we are getting better at it.
*  And the nice thing is we have about 800 electrodes in V1, also a couple in V4.
*  And the V1 is a map of visual space, right?
*  So if you stimulate it, this location in V1, the human will see a dot of light here.
*  Stimulate a neighbor, he will see a dot of light here.
*  If you see it in stimulate his neighbor, a dot of light there.
*  So it's basically a map of visual space.
*  And if you then plug in a couple of hundred electrodes, that gives you the opportunity
*  to give what people call phosphine.
*  So if you stimulate one of these electrodes, a human, even a blind person will see a spot of light.
*  If you have a couple of hundreds, you can make spots of lights at several hundred locations in
*  the visual field.
*  And you can work with it basically like a matrix board along the highway, right?
*  If you flash one bulb, you will see a dot.
*  But if you flash a pattern of bulbs, you will see a shape or a letter.
*  So we trained monkeys to recognize letters so they were not blind.
*  They could just do the task visually on the screen.
*  But at some point, we didn't present anything on the screen anymore.
*  We just played it to their brain.
*  And it worked.
*  So they can see it.
*  They can recognize letters.
*  So I think that is proof of concepts.
*  So this will work in monkeys.
*  It will work in humans.
*  So for me, the next step is to better understand, of course, how this electrical stimulation
*  works because there are still some things that we need to know better.
*  But also to develop safe implants that with the Utah probe, we know that it works for a year.
*  It works well.
*  And then it starts to degrade a little bit.
*  So there's some damage because this is a stiff silicon thing in the brain.
*  And so we will have to make a version of the electrodes that is durable.
*  So if you implant it now, it will also work next year and also after five years.
*  So that's an important focus of the project.
*  And of course, you have to make this technology wireless.
*  So we worked together with Eduardo Fernandez, who implanted a blind patient with such an electrode.
*  And the current version of the electrodes, the patient still had a plug on the skull.
*  Right.
*  So there's an opening in the skin and then you have the plug.
*  Of course, you would like to get away from that.
*  So that's another thing that needs to be developed.
*  And we started a company and looking for investors to make this happen.
*  Oh, what's the company name?
*  I didn't know that.
*  It's called Phosphenix.
*  So one of these artificial birth steps is called a phosphine.
*  And Phosphenix is kind of it's a phoenix is rising from the ashes.
*  So it's nice of these two ideas.
*  Is the idea though, the idea is not to restore complete, at least at this stage,
*  is not to restore complete vision, but to be able to present a pattern of phosphines
*  that then the patient or person can use to interact with the world.
*  It's not necessarily to present a rich and full visual percept to the person.
*  Exactly.
*  That's very true.
*  So it's going to be a rudimentary form of vision.
*  That's how we call it.
*  And you have an extra opportunity.
*  And that's the following.
*  So the patient also in previous renderings of the device.
*  So there's also the company Second Sites who made a similar device first for the retina
*  and also later for the cortex, although they use surface electrodes that give rise to much
*  coarser phosphines.
*  So you have a camera, say on your glasses, and you have a pocket processor that takes
*  in camera images and produces brain stimulation patterns.
*  Now in the translation from a camera image into a brain stimulation pattern,
*  you can do tricks, right?
*  You can, for instance, only represent those things that are maximally informative.
*  So also in that sense, we are thinking about how to make maximal use of a limited number
*  of phosphines.
*  And you're right.
*  It's not going to be as rich as the vision of a normal person.
*  At least at this stage.
*  But it's useful.
*  And that's what matters.
*  It would be incredibly useful.
*  Yeah.
*  One of the things that I found myself wondering about as well is, so our brains are constantly
*  adapting, constantly learning and changing.
*  And as you start to stimulate early visual cortex, for instance, you have this big mass
*  of recurrence that's happening.
*  And I'm wondering if we know or even have a good guess or conjecture about how stimulating
*  something early on in the visual processing stream would interact with top-down, let's
*  say, attention and feedback processing, especially with respect to what we would consider higher
*  order mental activity.
*  And if it's difficult to know, I mean, is the brain so robust that it really wouldn't
*  have any higher order mental activity effect?
*  Or would this type of stimulation lead to down the road some sort of, I don't know,
*  mental disorder potentially or something?
*  What could the effects be?
*  And I don't know if you've thought about that.
*  Yes.
*  So I think the good news is that this will only work in people who have seen.
*  So you have a history of seeing.
*  So they basically developed their normal visual pathways and then they lost eyesight
*  in the typically in the retina.
*  There are many eye diseases where you lose sight in the eye.
*  So there is this whole chunk of cortex that is waiting for input, but it's not coming.
*  And we're just plugging it in in V1.
*  So the good news is that also at a later stage, this plasticity is
*  certainly in early visual cortex is not so enormous anymore.
*  So you're basically plugging into a system that is waiting for inputs, but it's not
*  terribly plastic anymore.
*  So I'm not particularly concerned about it having detrimental mental influences.
*  Yeah, I don't think they will happen.
*  I don't think so either, but I just one never knows.
*  Yeah.
*  And yeah, but it's maybe less plasticity, but there still is filling in the cortex
*  wants to be used.
*  It can't help it.
*  Right.
*  So it gets used for things and then you're reprogramming it.
*  It's not like it's sitting there just blank and then you plug in its former use.
*  You might get some beneficial plasticity.
*  Yes.
*  Right.
*  Because the patterns that we're going to be able to transmit to the cortex,
*  they are going to be a rudimentary.
*  So maybe the neurons kind of become extra sensitive to small changes in the stimulation
*  pattern that are important for behavior.
*  Like some subtle changes in the visual stimulus are very important and some subtle changes
*  are completely unimportant.
*  And I suspect that the brain would just use that information as it would use normal
*  visual information.
*  Well, it's going to be fascinating to learn how people experience it, to hear the words
*  that people use to describe what they're experiencing.
*  That'll be fascinating work.
*  So good luck with the company.
*  Yeah.
*  Thank you.
*  When did you found it?
*  When did it start?
*  We started it a year ago.
*  Okay.
*  But that was also because we wanted to be a partner in the grant.
*  And so we're still looking for investors.
*  So I hope we will be able to scale it up anytime soon.
*  Are you going to like pitch meetings and things like that startup kind of pitch meetings?
*  Well, we are talking to investors every now and then.
*  Yeah.
*  And then it's a different type of presentation you give them for a scientific audience.
*  So we're just about out of time, but do you mind if I ask you just some kind of broad
*  questions in the last moment or two?
*  So I'm wondering if you've had any failures that have like really stood out,
*  you know, scientific failures, maybe what's one of one of your biggest failures that you've had?
*  And how did you move on from it?
*  Because when people, people don't talk about their failures, that's not what they
*  well, generally bring up on stage.
*  Although you already did mention, oh, I'm going to guess what your failure is going to be.
*  It's going to be the synchronization story.
*  Am I right?
*  Exactly.
*  Yeah.
*  Your heart was in.
*  I really thought I had to quit science, you know, because I really did papers.
*  Yeah. I thought this is a disaster.
*  My whole thesis was on the importance of synchrony and oscillations.
*  And then the first thing I found as a beginning postdoc is that it's just not working like I
*  thought. Yeah.
*  I thought this is the end of my career.
*  What do you think about oscillations now?
*  Because there's still a large part of the story.
*  There's a lot of ideas about how oscillations can even be causal for processing.
*  Right. So where do you land on the synchronization and oscillations story right now?
*  I think that I make exceptions for very slow oscillations because they, I think,
*  may signal really meaningful processes.
*  The best they are signatures.
*  Signatures of safety, forth and feedback processes, but they're not causal.
*  And sometimes I think they're just there to distract the neuroscientists from the truth.
*  Man. Oh, boy.
*  You're making enemies among the oscillations community.
*  Finally, Peter, as people progress in their careers, so you start off and you are discovering,
*  personally discovering, learning things at a rapid rate.
*  And sometimes they're like big things and it feels very satisfying.
*  And as you progress through your career, that rate of discovery kind of slows down.
*  And often, you know, your first project as a graduate student almost defines your career.
*  And then, you know, you build up this body of knowledge and then things start slowing down.
*  Discovery rate wise.
*  I'm wondering if that is what you have experienced in your career and how it has sort of affected
*  your outlook, if so.
*  I think in my career was defined by the fact that I started to think about visual processing binding.
*  And in the beginning, I had many ideas, many of them wrong.
*  And I started to work on them.
*  And over time, my ability to attract good people and work on these ideas has increased.
*  And so that kind of makes the projects that we're doing incredibly satisfying.
*  And with the advent of all kinds of new techniques.
*  So we're also studying some of this recurrent processing now in rodents.
*  They are very powerful techniques where you can use optogenetics to silence neurons.
*  You can use calcium imaging to look at specific types of interneurons.
*  Right.
*  It's just equally exciting.
*  Maybe even more exciting than 20 years ago.
*  I was going to say, you seem like you're more excited.
*  Yeah.
*  And then this visual processes thing, you know.
*  So if you can bring this to humans, it would be so fantastic.
*  And can you believe, I mean, then we have an interface to the brain of a human.
*  You can ask all kinds of questions that we couldn't ask without this technology.
*  Do you feel like you're in competition with Neuralink?
*  So actually I talked to Elon Musk.
*  He at some point invited me.
*  He even talked to me at his house.
*  And I think it's not competition.
*  So I think their focus is a bit different.
*  And I think we have the right technologies for the things we want to do.
*  They have other questions.
*  So they need other technologies.
*  I mean, the technologies they use, most of them are already there, right?
*  And they are kind of distributed around the world.
*  So I'm not part of a number of consortia where we also have all these technologies.
*  So I think we will complement each other.
*  And there will be happy coexistence of several companies who kind of reinforce each other.
*  That's great.
*  Well, that's a great place to end it.
*  Peter, thank you so much for talking with me and good luck with everything.
*  You have multiple exciting things going on.
*  So in a sense that my question about the rate of discovery slowing down was
*  a terrible question because it doesn't seem to with you.
*  I'm enjoying myself.
*  And thanks for the interview.
*  It was a lot of fun.
*  I'm glad you're here.
*  Brain Inspired is a production of me and you.
*  I don't do advertisements.
*  You can support the show through Patreon for a trifling amount and get access to the full
*  versions of all the episodes plus bonus episodes that focus more on the cultural side but still
*  have science.
*  Go to braininspired.co and find the red Patreon button there.
*  To get in touch with me, email paul at braininspired.co.
*  The music you hear is by The New Year.
*  Find them at thenewyear.net.
*  Thank you for your support.
*  See you next time.
*  Bye.

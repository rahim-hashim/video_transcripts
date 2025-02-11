---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 5320s
Video Keywords: []
Video Views: 1038
Video Rating: None
---

# BI 160 Ole Jensen: Rhythms of Cognition
**Brain Inspired:** [February 07, 2023](https://www.youtube.com/watch?v=yW9U2qT093A)
*  So I think what we need to do is to ask what do oscillations do for neuronal computation.
*  The way to think about it is that if you have a lot of neurons firing like crazy and look
*  at the population activity, you don't see any modulation.
*  But if you now start to kill off neurons every 100 milliseconds, you start to see a rhythm
*  emerge.
*  Some years ago I started to get big doubts.
*  Oh, okay.
*  Yes, and that is because...
*  This is Brain Inspired.
*  Hello everyone, I'm Paul.
*  Ola Jensen is co-director of the Center for Human Brain Health at University of Birmingham,
*  where he runs his neuronal oscillations group lab.
*  Ola is interested in how the oscillations in our brains affect our cognition by helping
*  to shape the spiking patterns of neurons and by helping to allocate resources to parts
*  of our brains that are relevant for whatever ongoing behaviors that we're performing in
*  different contexts.
*  People have been studying oscillations for decades and finding that different frequencies
*  of oscillations have been linked to a bunch of different cognitive functions.
*  Some of what we discussed today is Ola's work on alpha oscillations, which are around
*  10 hertz, so 10 oscillations per second.
*  The overarching story is that alpha oscillations are thought to inhibit or disrupt processing
*  in brain areas that aren't needed during a given behavior.
*  And therefore, by disrupting everything that's not needed, resources are allocated to the
*  brain areas that are needed.
*  So we discuss his work on attention in that vein.
*  You may remember the episode with Carolyn Dicey Jennings and her ideas about how findings
*  like Ola's are evidence that we all have selves.
*  We also talk about the role of alpha rhythms for working memory, for moving our eyes, and
*  for previewing what we're about to look at before we move our eyes.
*  And more broadly, we discuss the role of oscillations in cognition in general, and of course what
*  this might mean for developing better artificial intelligence.
*  Show notes are at braininspired.co.
*  For those of you interested, I have reopened my online course, Neuro AI, the quest to explain
*  intelligence, which you can learn more about through this short video series on the website
*  at braininspired.co.
*  We can also learn how to support the show through Patreon to get full episodes and to
*  join our discord community, or just to make a contribution by other means if you value
*  this show.
*  All right.
*  Thank you for being here.
*  Here's Ola.
*  So Ola, you have studied oscillations in the brain for a long time now, and I feel like
*  that phenomena, oscillations, kind of waxes and wanes in popularity in the neurosciences
*  writ large.
*  And I'm just curious, I thought I'd start out by asking you what your view on that is
*  or what your experience has been.
*  Has funding been harder in certain years and have people's interests wax and wane the way
*  it seems like from the outside?
*  Yeah, no, it's a bit difficult to say because I've always surrounded myself with people
*  who are interested in oscillations.
*  So yeah, I started out looking at the hippocampus, looking into hippocampal data, but also doing
*  modeling on the hippocampus.
*  And there you see these very strong theta oscillations.
*  So I think in that part of the community, there's not really a doubt that oscillations
*  are there loud and clear.
*  So then I think there's also regional differences.
*  So I worked in the US with my PhD, and there are people who somehow seem a bit more skeptical
*  about oscillations than in Europe, less so.
*  I don't know exactly what makes that difference.
*  So sure, it has sort of waxed and wane over time the interest in oscillations, but there's
*  also seem to be some interesting regional differences.
*  I hadn't thought about that.
*  Where are we right now?
*  Are we at a peak of interest in oscillations?
*  Are we at a trough or what?
*  I think there's a lot of excitement for oscillations.
*  It's sort of being rekindled.
*  And I think also oscillations are many things, and of course, occurring in different frequency
*  ranges.
*  So there's also sort of when interest wax and vanes, it also depends on what frequency
*  band you're looking at.
*  So back in the 90s, when people talk about the binding theory, that these gamma oscillations
*  say from 40 to 100 hertz were thought to be important for binding, the focus was very
*  much on gamma oscillations.
*  And I think now people are getting more and more interested in a slower type of oscillations.
*  So theta oscillations from 5 to 8 hertz, alpha oscillations from 8 to 12 hertz, and beta
*  oscillations.
*  So maybe there's sort of a shift down in frequency in terms of interest.
*  Yeah, I guess the scale waxes and vanes too.
*  You're an alpha guy, right?
*  Or an alpha male, I suppose I could say.
*  So we'll end up talking a lot about alpha, and I know that's not all you study.
*  Just staying with the big picture for a moment.
*  So spikes are easy, right?
*  Because they're pulses, and you can count them.
*  And oscillations are more slippery, I'd say, like neuromodulation, right?
*  Because there's different analog levels, and then you have to pull out the power within
*  some range, and you have to choose that range.
*  So this leads me to the question of just what your overall worldview is regarding the causal
*  role of oscillations.
*  Are they more constraining?
*  How they interact with spikes, and how spikes interact with them?
*  Are they mutually causal?
*  And then throw neuromodulation in there.
*  It's just harder to think about, for me, it's harder to think about this super dynamic process
*  of oscillations, and what role it plays.
*  How do I really have a clear picture in my mind about how it's interacting with the spikes
*  and what it all means?
*  Yeah, so it's a very good question.
*  So I mean, first of all, we think oscillations are group phenomenon, right?
*  So they are a consequence of the neuron spiking in a synchronized manner, but also in a rhythmic
*  manner, right?
*  So the oscillations follow from that.
*  Yet, I would also argue that the spiking of individual neurons is driven by the group
*  activity, the oscillations, right?
*  So the example would be that if you have an audience, and after a concert, they might
*  start applauding, and then when you start clapping, suddenly you hear they start to
*  clap in a rhythmic manner.
*  So when thinking about that, each individual is driven by the population activity, right?
*  So it's really the oscillations, the group activity exercising a causal effect on the
*  individual, but it's all the individuals together that creates the oscillations.
*  So from that perspective, it's difficult to make a clear causal direction unless you think
*  about the individual neurons at a time.
*  But I can also tell a little story which was very enlightening for me when thinking about
*  oscillations, because I started out by looking at EEG and MEG signals, and I never see the
*  oscillations loud and clear.
*  But of course, we want to link them back to the spiking activity.
*  So I had this PhD student, Saskia Hakens, she was studying the somatosensory system.
*  She started to discuss with Ranol Foromo in Mexico, who was recording from non-human primates
*  in the somatosensory system, and they had all these wonderful spike data and were investigating
*  different aspects of that.
*  They also had the local field potential data, right?
*  But they have never really looked at them.
*  So what Saskia did was that she flew to Mexico, set up the collaborations and started to analyze
*  the data.
*  And what we saw was that when the spikes, the neurons were spiking, the spiking was
*  tightly locked to 10 Hz alpha oscillations.
*  But if you looked at the individual spikes, you did not see much of an oscillation.
*  The firing rate was not very high, so you didn't get this oscillatory pattern.
*  But if you look at the power spectrum of the local field potentials, a clear peak at around
*  10 Hz, and also when we looked at how the spikes linked to the phase of these oscillations
*  in a local field potential, we saw that the spikes were very clocked by these oscillations.
*  But individual neurons weren't necessarily clocked, but among the population of neurons,
*  they were clocked?
*  Is that what you're saying?
*  But rather, when a neuron fired, it fired at a particular phase of these oscillations,
*  but the firing rate was not that high.
*  Oh, so yeah.
*  So you wouldn't see the rhythmic pattern alone because it would be skipping cycles.
*  Yeah, okay.
*  So it wouldn't fire on every cycle, so the spiking wasn't rhythmic.
*  Yeah, I mean, that's the idea is like when an oscillation is happening and there's this
*  peak, right?
*  And it's at that peak that it's maximally allowing or kind of nudging spikes toward
*  firing or allowing them to fire or not repressing them or something or depressing them.
*  But this interaction then, right, between an oscillation and spikes, you can't mess
*  with an oscillation without messing with the spikes and you can't mess with spikes without
*  messing with the oscillation.
*  So I just want like a clear picture in my own head about how to think about that relationship
*  causally and what it means for our cognition and the way and brain function, right?
*  Like what should I think is more important, for instance, right?
*  Yeah, I mean, so the causal discussion becomes very difficult, right?
*  Because it is indeed possible to entrain these oscillations, for instance, by rhythmic
*  flicker in a 10-hertz band, you can entrain alpha oscillations.
*  You can also do transcranial stimulation with current, also at 10-hertz oscillation and
*  entrain these oscillations and then you can show that they have effect on cognition.
*  You can show that these oscillations are inhibitory.
*  However, then one can always argue back and say, hey, these are not the same kind of oscillations
*  as occurring naturally, right?
*  So that makes the causal discussion quite difficult.
*  But in all this, our starting point is that these oscillations are there loud and clear,
*  right?
*  The alpha oscillations are the strongest signal in the ongoing EEG or MEG also doing task.
*  So to me, at least that warns that we should try to understand what they are doing and
*  it also begs the question on how the neurons, they are working together in order to produce
*  the oscillations.
*  And in my mind, the fact that the spiking of the individual cells are timed by the phase
*  of these oscillations also mean that the oscillations would have an impact on how these neurons
*  they compute.
*  The word constraint keeps rolling around in my mind.
*  Do you think of them more as constraints or more as, I mean, constraint and causality
*  are kind of intertwined as well.
*  It could be seen as a kind of causality.
*  I'm trying to get a sense of how powerful you see oscillations in terms of responsibility
*  for brain function.
*  Yeah, I like to think that they are part of organizing the neuronal coding.
*  So to give another example, so John and Keith, he got the Nobel Prize for finding play cells,
*  in the rat hippocampus that fires when the rat is in a specific location.
*  So he also did another very important discovery and that is this notion of phase possession
*  or phase coding.
*  So when you look at the firing of the play cells and relate them to in this case ongoing
*  theta oscillations, and these are these oscillations being 5 to 10 hertz and they are super strong
*  in the hippocampus.
*  So you see them with the naked eye, you cannot miss them.
*  But what they then did was to relate the firing of the play cells to the phase of these
*  theta oscillations and as the rat moves through a play cell, you see the firing happening
*  earlier and earlier in a theta cycle.
*  So that now means that it's possible to take a collection of play cells and then reconstruct
*  where the rat is.
*  What you now also can do is that you can take the phase of firing into account and then
*  you can better predict where the rat is.
*  So that means when we talk about the oscillations constraining the firing, we can also think
*  about the phase in which the cycles they fire coding for information.
*  So of course I cannot prove to you that the brain is utilizing this phase organized code,
*  but at least when we look at the data themselves, we can do a better job at sort of reading
*  the rats or mind of where the rat is by taking the phase of firing into account.
*  If I use the word oscillations are suggestive to neurons, is that too weak?
*  Because you know, neuron neuronal firing is highly variable itself.
*  And then of course, with oscillations, which I'm going to ask you in a second, when we
*  have these terms that are supposed to like denote clear bands of oscillations, but really
*  it's happening.
*  There's bits of oscillations throughout all of the frequencies, right?
*  And so that's kind of noisy and not, you know, it's not as clear as alpha, beta, delta,
*  etc.
*  But is the word suggestive of wind to fire?
*  Is that too light?
*  Does that not give enough credit to an oscillation?
*  Yeah, one could say that the change is the probability for when a neuron fires or not.
*  But I would also say personally, I'm quite sort of signal to noise driven.
*  I study alpha because we see it.
*  And also back to that, the theta and the alpha oscillations in respectively rats and humans,
*  they are so strong, right?
*  So in my mind, and it's very hard to come up with a cognitive task where you do not
*  see robust modulations in the alpha band.
*  So to me, that also speaks to the notion that these oscillations must be important for when
*  neurons they fire or not.
*  Yeah, one of the things I always found frustrating about thinking about oscillations is, you
*  know, it seems like you could take any frequency band and relate it to any cognitive function
*  that you want.
*  So it's hard to, you know, when you think right now in my conversation with you, I'm
*  thinking alpha.
*  That is attention and working memory.
*  And then like you were saying, gamma, oh, that's the binding frequency.
*  But then there are a thousand different stories about how a thousand different frequencies
*  relate to a thousand different cognitive functions.
*  I mean, do you think that we're going to get to a point where we can kind of keep in mind
*  and, you know, when I think alpha, I should think X, right?
*  And when I think beta, I should think X.
*  Or is it just that because the brain is so complicated and complex that we're just going
*  to have a really long table of different cognitive functions that they interact with and how they
*  interact with them?
*  Yeah.
*  But again, I'll go back to the sort of signal to noise argument and then say, if you, for
*  instance, do a working memory task, we see a very robust modulation in Yelva band, not
*  so much in a beta and gamma band, right?
*  So that sort of constrains the issue and the interpretation.
*  So of course, your search space or data space becomes larger when you consider frequencies.
*  But it's not, we don't see these modulations robustly in all frequency bands.
*  They often seem to be constrained to very specific bands.
*  A couple more broad questions before we actually start talking about the interesting work that
*  you do.
*  Are they oscillations or are they traveling waves or both?
*  Yeah, very good question.
*  So when we look at intertranial recordings, for instance, with ECoC, that's where you
*  sort of put a grid of electrodes on the neocortex.
*  On the brain.
*  Yeah, there you see very robust traveling waves.
*  If you look at hippocampal recordings, there's also reports on the theta oscillations traveling
*  down the hippocampus.
*  And I think that's, I think it's, I wouldn't say obvious, but it's like you have all this
*  excitable tissue.
*  And then if there's a generator oscillating in one part of that tissue, it will always
*  be strange if you didn't have waves sort of emerging out from that.
*  The thing is, we have not been very good at quantifying these waves in the context of
*  cognitive tasks.
*  Right.
*  But I strongly believe they are there and I believe they're important.
*  But it's first now we sort of are getting the technology with the multielectrodes in
*  animals to record this.
*  And to observe the waves at the scalp level at humans in EEG and MEG data is a bit problematic
*  because we have the volume reductions and everything sort of blurs together.
*  Right.
*  Yeah.
*  Has your faith in oscillations as a major function?
*  This is a totally unfair question.
*  I know.
*  Has it ever waxed and waned?
*  Have you ever faltered in thinking because you're really focused on oscillations?
*  Yeah.
*  So at least some years ago, I started to get big doubts.
*  Oh, okay.
*  Yes.
*  And that is because you are starting to look at more natural tasks where we allow participants
*  to circuit.
*  And then we see that people circuit three to four times per second.
*  If you now have an alpha oscillations being at 10 hertz and sort of think about the alpha
*  oscillations doing clocking of the processing, then it's sort of odd that you have a relatively
*  low oscillations, 10 hertz sort of meaning 100 milliseconds per period.
*  And then you circuit three to four times per second.
*  Right.
*  It doesn't seem like a very intelligent design to use a bad expression.
*  But what's then safe the whole story is that you now find that often your circuits are
*  locked to the face of these alpha oscillations.
*  And then things start to make sense again, because then you can move your eye in a period
*  where the alpha oscillations are not processing, so to speak.
*  And then when your eye lands, you have the visual information coming in on the excitatory
*  face of the alpha oscillations.
*  So the eye movements are kind of nested within the alpha.
*  Exactly.
*  Yeah.
*  And what made me nervous before observing that was that we started these oscillations
*  and they're actually quite slow in frequency compared to how fast we perform or our visual
*  system operates.
*  So your doubts were because of the timing of the oscillations relative to the spikes.
*  You never thought, like some people claim, oscillations are epiphenomenal.
*  You never had those kinds of doubts.
*  Not really.
*  I have to admit, because we see them so loud and clear when recording EEG and MEG data.
*  And again, it's very hard to come up with a task where you don't see robust modulations.
*  So at least to me, that warns that at least some of us should be investigating them.
*  Then it's all well and fine that some are skeptical and say they're epiphenomenal, but
*  in time, we will sort of resolve the issue.
*  Are those US scientists who say they're epiphenomenal and the Europeans say, no, they're not epiphenomenal?
*  Is that that divide?
*  I wouldn't say there's an Atlantic divide like this, but I mean, there's more sort of
*  trends, right?
*  OK.
*  OK.
*  So one more question.
*  I'm going to ask you a little bit about the relation of some of your work to artificial
*  intelligence later.
*  But artificial intelligence and more and more the cognitive sciences and think of brain
*  functioning in terms of algorithms and objective functions and these sort of very computable,
*  straightforward sequences of computational steps.
*  Do oscillations throw a wrench in that?
*  Are oscillations amenable to algorithms?
*  Can we integrate them into the story about an algorithm or do they complicate that story
*  in a way that maybe can't be saved?
*  So there's two strands to that question.
*  So first, I very much agree with the sort of algorithmic view.
*  So I think what we need to do is to ask, what do oscillations do for neuronal computation?
*  Right.
*  So we shouldn't just sort of correlate them with whatever function we should really go
*  in and ask.
*  It's some processes, computations that can be done better with oscillations than without
*  oscillations.
*  And what we are thinking now is that the 10 hertz theta alpha oscillations in humans and
*  as well as the hippocampal 5 to 10 hertz oscillations, theta oscillations in the rat,
*  what they are, they are inhibitory in nature.
*  So they are pulses of inhibition.
*  So what you should imagine is that the peak of that inhibition, all input are being blocked.
*  But as inhibition ramps down, the most excitable and then the second most and then the third
*  most excitable representation would fire.
*  So what these oscillations then give you is almost like a filter that then allows only
*  the most excitable representations to slip through.
*  But furthermore, they are organized as sequences according to importance.
*  So if you go back and think about O'Keefe and this theta phase coding, a theta phase
*  One can construct models where you have these sequences being read out.
*  So this is spatial representations organized according to excitability or sort of how far
*  they are from the rat's upcoming positions.
*  Furthermore, for the visual system, what we also speculate is that when they are competing
*  visual input, only the most excitable input should go through the visual system.
*  Furthermore, they need to be organized in a temporal code according to importance, if you are.
*  And this is what the oscillations they provide, they inhibit.
*  And when you ramp down inhibition, you get the activation according to excitability.
*  So that's sort of the algorithm we think that these oscillations are doing.
*  But this is very much a temporal algorithm.
*  And if you take like a deep neural network, you don't care about time.
*  I'll just jump to it then.
*  Are we going to be able to build quote unquote strong AI or human-like AI without this kind
*  of temporal aspect built in, whether it's built in via oscillations or not?
*  And do you think we should just build in oscillations or that kind of timing mechanism?
*  Yes.
*  So we are right now playing around with different deep neural networks trying to do exactly that.
*  Oh, OK.
*  So I mean, you're completely correct.
*  When one considers deep neural networks or convolutional neural networks, they do not
*  build in time.
*  Right.
*  And if we then want to relate what's going on in these networks to the temporal dynamics
*  as measured in humans and non-human primates, we cannot do that.
*  So we have some ideas for how to augment deep neural networks to incorporate time.
*  So we call it dynamical deep neural networks.
*  And what you also want to do is to put in these inhibitory oscillations in the network.
*  So the way you should then imagine this is that we present the network with multiple
*  stimuli.
*  So it could be a cat and a dog presented at the same time.
*  But what the network then does is to break that image up into a temporal code.
*  So you have a cat-dog coming out in the other end.
*  And it's these inhibitory properties of the oscillations that would serve to convert the
*  parallel input into a temporal code.
*  How do you add the oscillations in?
*  Are they just a function of the firing of the neurons?
*  And they emerge from that and then affect the neurons themselves?
*  Yeah.
*  So step one is that we simply impose them.
*  So we assume that there's a pacemaker driving it.
*  So I guess what you're getting at, do they emerge from the network itself?
*  And of course, it would be very elegant if they then emerge from the network.
*  But that would then be the next step.
*  It's so complicated and messy.
*  I mean, do you think, obviously, if you have robots, they need to operate in time if we
*  go beyond deep neural networks.
*  And if you want human-like artificial intelligence to be interacting with humans, timing needs
*  to be pretty exquisite as well.
*  And robots moving throughout the world.
*  So in the future, with really great AI robots, are we going to see oscillations as part of
*  that story?
*  I don't know.
*  Oh, come on.
*  Yeah.
*  Yeah.
*  So because, I mean, so far, what we are doing is that we are taking deep neural network.
*  And I think it's amazing what they can do and how the representations emerging in these
*  deep neural networks can be mapped on to human or non-human brain activity.
*  So I think something is correct about those for how representations are being formed.
*  So now we are sort of exploiting that work to make a model of the human virtual stream.
*  So one could then imagine that also when doing that process, we get inspired for how to improve
*  the networks in a machine learning sense.
*  And then there would be an application that could be useful for robots.
*  But so far, I have no idea for how to go the other way, right?
*  Yeah.
*  Interesting.
*  All right.
*  So maybe we should talk a little bit about alpha.
*  Is alpha your favorite frequency band?
*  Not by choice, but that's somehow the data drove us.
*  Yeah.
*  So maybe you could just take us through, there are different frequency bands, many of which
*  you've already mentioned.
*  I guess the alpha band, which is around 10 Hz, was the first to be at least noted by
*  Hans Berger and it used to be called the Berger band?
*  Yeah, the Berger rhythm.
*  Berger rhythm, that's right.
*  And it's classically, well, you should correct me, but historically, it's been associated
*  with things like drowsiness, well, internal thinking, internal cogitation and sleep and
*  things like that.
*  And how has the story of alpha changed over the years?
*  Yeah.
*  So, I mean, it goes back to 1924 when Hans Berger, he identified the alpha rhythm, as
*  we call it now, right?
*  And then there were quite a few investigations, but most of them also concluded that alpha
*  is associated with rest, right?
*  So if you close your eyes, alpha becomes strong.
*  If you become drowsy, alpha becomes strong.
*  So possibly alpha oscillations have also gotten this connotation of being somewhat boring,
*  right?
*  Also, electrophysiologists working with non-human primates were not particularly interested
*  in alpha, right?
*  Because why would you study something that just pops up when nothing is going on?
*  But then what happened was that sort of in the late 90s, people look at the alpha in
*  working memory tasks.
*  And there's a paper by Wolfgang Klimisch where he report that alpha is actually relatively
*  strong during working memory retention.
*  So he referred to that as paradoxical alpha.
*  So yeah, so we were also doing some studies and that was brought me into the field where
*  we looked at the algorithm with working memory load.
*  And what we saw was that the alpha oscillations were becoming stronger and stronger the more
*  you kept in working memory, right?
*  So the more difficult the task, the stronger the algorithm, right?
*  And we thought we got the triggers wrong and so forth, but we checked it in all kind of
*  ways and it held up.
*  And it turns out that it has now been reproduced many times.
*  So that brought us to think that maybe alpha is not about rest, right?
*  So also in line with what Klimisch had proposed, we put forward the notion that the alpha oscillations
*  were inhibitory.
*  So during working memory, that would mean that when you sit there and have to retain
*  something in working memory in order not to have interference, the visual system is shut
*  down by the algorithm.
*  And that was later tested by doing different kind of tasks where we introduced distractors
*  that people could anticipate and we could show that the alpha oscillations pop up before
*  these distractors are occurring in order to suppress the distraction.
*  So the idea is that the alpha is...
*  Okay, there's a few ideas here, right?
*  So the first thing that you mentioned is the stronger the alpha, the more you can hold
*  in working memory.
*  And please correct me, that's because if you have a really strong peak, more neurons can
*  fire and the neurons firing is an analog of things that you can hold in working memory?
*  That was one hypothesis we entertained.
*  And the other hypothesis was that the alpha oscillations were in this case generated in
*  visual cortex.
*  So they were shutting down visual cortex in order to allow say more frontal regions to
*  maintain the working memory representations.
*  So it's not...
*  I thought the story was that it was a top-down control mechanism where frontal areas produce
*  this alpha and that alpha travels to or is manifested in visual cortex and that is a
*  suppressive oscillation in visual cortex so that you're not getting any incoming stimuli
*  so you can remember the phone number over and over, right?
*  Because I don't want to be distracted by incoming stimuli.
*  Yeah.
*  Yeah.
*  I don't know that I would agree on.
*  But then you just said that the early visual cortex was producing the alpha.
*  Yeah, but the alpha has an inhibitory effect, if you will.
*  So the way to think about it is that if you have a lot of neurons firing like crazy and
*  look at the population activity, you don't see any modulation.
*  But if you now start to kill off neurons every 100 milliseconds, you start to see a rhythm
*  emerge, right?
*  So of course, if you kill off all the neurons, you don't see anything again, right?
*  But there's sort of an inverted U shape.
*  So the way we think about alpha being generated is actually by having neurons not firing
*  every 100 milliseconds.
*  So that also explains why the alpha rhythm increases in power as the neuron firing goes
*  down.
*  So this gets back to that interaction, right?
*  Because I thought that the alpha was entraining them in this rhythmic way.
*  And by doing so sort of disrupts the incoming sensory stimulation.
*  But then you're saying that no, it's the neurons themselves that begin to fire rhythmically,
*  which allows the alpha to have more of an effect.
*  Well, there's a difference between sort of the alpha being generated in the network and
*  then what you measure.
*  What you measure is most likely the summed activity of parameter neurons.
*  And that is a consequence of oscillatory activity coming in and then silencing the parameter
*  neurons in a phasic manner.
*  So then you are left with sort of like collective bursts occurring every 100 milliseconds.
*  But the stronger that inhibition, the shorter the duty cycle for the neurons to fire.
*  And then that would emerge as a stronger peak in your power spectrum, albeit the total neural
*  firing is going down.
*  And that is the signature of keeping at bay sensory stimulation.
*  Yes.
*  So then you have, so the old story of sequences of spikes firing at different phases along
*  the peak of the alpha wave signifying however many things you're keeping in working memory.
*  That story, what's the status of that story?
*  Yeah, so that then that does become complicated because I mean, there was a story initially
*  developed for theta oscillations.
*  And there is some support from that, from intercranial data now, where we have been
*  looking at ECoG data.
*  And then in this case, we see 8 Hz oscillations in which we have multiple working memory representations
*  activating on that cycle.
*  But I have to say, it's not a very clean picture, right?
*  Because I mean, 8 Hz is just in the boundary between theta and alpha oscillations.
*  Yeah.
*  The thing is, we speak as if there's this clear line in theta and alpha, but it's 2
*  Hz or something.
*  So I was going to ask you, and we'll come back to this later about individual differences
*  in reading and your work on studying oscillations in reading and predicting.
*  But I'm curious about individual differences in something like working memory, right?
*  So everyone has different capacity for working memory, although we're all kind of the same.
*  And it just seems strange.
*  It would seem strange to me that everyone is operating in the same regime, that it has
*  to be at 8 Hz.
*  It seems like Jessica might operate at 8.5 Hz, or that might be her best oscillatory
*  regime for working memory.
*  And Philip might do better at 10 Hz or something.
*  Are those individual differences clear?
*  And if so, what's the range?
*  Or are our brains just so exquisitely evolved that we're all operating within these narrow
*  bands?
*  Yeah.
*  So I think if you go to a particular individual and measure them repeatedly, you will find
*  that their frequency is quite stable.
*  However, there's individual differences, as you refer to.
*  And some people have been able to show that these individual differences in alpha frequency
*  is important for how people sort of combine things in time.
*  So there's these paradigms where you either can integrate or separate two objects depending
*  on how close they are presented in time.
*  And then people with slower alpha oscillations, they tend to integrate more than people with
*  fast oscillations.
*  So there's these individual differences.
*  Is it better to have a big brain or a small brain?
*  Human.
*  Yeah.
*  Yeah.
*  I don't know.
*  Because I mean, there's also some people that are also trying to find a link between the
*  size of the brain and the alpha oscillations.
*  I'm not up to date on what the findings are, but there's these ideas around.
*  So I mean, just on a personal note, sometimes I wonder, and this is maybe an oscillation
*  story with me, sometimes I think that I think very quickly, but unfortunately not very deeply.
*  So I can think on the fly very quickly, but then I feel like I'm lacking depth in my thought,
*  whereas some people that I've observed who seem to process things more slowly can also
*  seem to process them more deeply.
*  That's a really naive story.
*  I just worry that I'm a very shallow quick thinker.
*  That's the issue.
*  Yeah.
*  So I don't know.
*  I listen to your podcast.
*  So I don't share that concern.
*  OK.
*  We would leave it at that.
*  So I can continue to worry about that then.
*  Well, so I mean, we've touched on working memory.
*  And let's move on to attention because again, so the story in working memory is that alpha
*  has this suppressive role in suppressing distractor information coming in.
*  And I'll link to all these studies that you work on and your lab website for people to
*  learn more about the gritty details and such.
*  I had Carolyn Dicey Jennings on the podcast a few episodes ago.
*  I can't keep track now.
*  And she's a philosopher and she's written about using the evidence of alpha oscillations
*  as an inhibitor, as evidence for that attempt in its role in attention, specifically as
*  evidence for a self, that we have a self.
*  And that's a very loose way to describe her detailed work.
*  I have no idea if you're familiar with any of her work, but or if you have a comment
*  on the relation between alpha and attention and the self.
*  But then you've done a lot of this work showing that alpha has this inhibitory role in attention
*  as well.
*  Yeah.
*  So I mean, so I guess I'm more comfortable about talking about attention and alpha and
*  inhibition.
*  And then maybe we can return to the self.
*  Sure.
*  Maybe.
*  Maybe we can.
*  Yes.
*  So I mean, so the studies for alpha and attention are somewhat simple in the sense that we simply
*  ask people to fixate and then attempt something to the right and then ignore what's to the
*  left.
*  And what we then see is that alpha contralateral to what you should attend to is depressed,
*  but in the other hemisphere associated with the distraction, the alpha increase.
*  So that has sort of become a workhorse paradigm for the alpha oscillations.
*  So I should also say here, but that does not mean that each time you see alpha modulations,
*  it has something to do with oscillations.
*  So we like to think that alpha is always exercising this inhibitory role, but attention is sort
*  of the workhorse for getting that out.
*  So what we would like to do is to generalize this to other brain regions.
*  And maybe that's where the larger discussions come in.
*  So now it turns out that if you look at intertranial recordings, you also see alpha oscillations
*  in other regions than visual regions or somatosensory regions.
*  If you do language tasks, you see alpha modulations in the language areas like left prefrontal
*  cortex.
*  So what I would like to think is that alpha is ubiquitous.
*  And what it actually does is to allocate resources in the brain.
*  So I mean, maybe to say something which is wrong, but there's a saying that you only
*  use 10% of our brain, but we can modify this to say that you only use 10% of our brain
*  at a time.
*  Okay.
*  But it's still wrong.
*  The point being is...
*  It's still wrong though.
*  It's still wrong.
*  It's still wrong.
*  The 10% is wrong, but maybe it's within range.
*  The point being that if all brain regions were active at the same time, there would
*  be sort of information overload.
*  Your brain could not function, right?
*  So what we like to think is that alpha in general is inhibiting all the brain regions
*  not involved in a given task.
*  And then the alpha activity is decreasing in the regions doing the processing itself.
*  And this is not only occurring in the visual system, but it's more general within the full
*  brain.
*  So this is speculation, but it's sort of consistent with the different observations we are making.
*  So it's resource allocation by saying, all right, kind of just always telling everyone
*  to stop except for the relevant networks that need to be highlighted or taken advantage
*  of at the time.
*  Yeah.
*  Yeah.
*  I mean, this begs the question, and I'm sorry to just jump to this, but how...
*  So you use the word attention, right?
*  And if we think of attention as a cognitive function, like a mental cognitive function,
*  I mean, then where does that come from?
*  If alpha is indicative of this process of attention, in other words, how does the controller,
*  let's say it's alpha, know how to control?
*  Yeah.
*  So indeed, there's been a lot of debate about this.
*  And what we initially thought seems wrong are not always correct.
*  So we thought that alpha was under top down control.
*  So if you have to attend to something to the right and there's a distraction to the left,
*  we thought that alpha would increase or your right hemisphere to sort of push out the distraction.
*  So it has been difficult to find evidence for in general.
*  There's some indications, but in general, what we actually see is that it is how much
*  you are attending to the target to the right that then results in the alpha increasing
*  in the non-target hemisphere.
*  So to me, that suggests that some regions are being engaged and then through some sort
*  of lateral inhibitory mechanism, alpha is increasing in the non-engaged regions.
*  So this is also consistent with the perceptual load theory of Nelly Lavi, who has made this
*  point that it's actually very hard to suppress distraction.
*  It's a bit like don't think about the polar bear walking in the door to the right, right?
*  But what you can do is to focus your attention to the left and through that, the alpha activity
*  associated with the door to the right is increasing.
*  So I'm going to have you do a task, right?
*  So I'm going to give you instructions and that's an attention task and I'm going to
*  say you're going to be queued about which side to attend to or something, right?
*  So that's externally, you're getting my instructions.
*  So then you think, okay, there's a top-down thing, I need to do this.
*  And then while you're doing the task, then you're getting this sensory stimulation of
*  like where the cue is going to be.
*  So that is bottom-up driven from our senses.
*  The question is who's doing the doing, right?
*  How does that then turn into the controller, the resource allocation, the alpha that's
*  helping us to attend?
*  It's an impossible question right now, isn't it?
*  Yeah.
*  So the cop-out here is to say is prefrontal cortex, right?
*  But then it almost becomes like a humongous notion, right?
*  So, I mean, at least you would like to think about prefrontal cortex sort of doing a top-down
*  drive to engage the regions that are involved in what you attend to.
*  And then there's a secondary mechanism in which alpha increases in the regions not being
*  involved in the task, right?
*  Go ahead, I'm sorry.
*  But by that, I've not solved the overarching problems of how to kill the humongous, right?
*  That assumption, yeah.
*  So you could tell a story, maybe I'm going to rephrase what you said and tell me what
*  I'm getting wrong.
*  So there's like a mechanism, you know, you have this top-down control from prefrontal
*  cortex, but it's not actually controlling the early visual cortex.
*  There's an inherent, let's say, self-organizing mechanism, quote unquote, in like, let's say,
*  the early visual cortex that then just kind of allowed, it's allowed to be activated within
*  itself that then, so it's a sort of internally self-organized driven way of inducing alpha
*  and shifting attention?
*  Yeah.
*  Yeah.
*  That's cool.
*  So you engage one region and through some sort of lateral mechanisms, regions not involved,
*  that's when the alpha increases.
*  So I want to talk about frequency tagging.
*  This is a really interesting method to use and one could say disturbing on some level,
*  perhaps.
*  So what is frequency tagging in terms of oscillations and how do you use it?
*  Yeah.
*  So it's something we are quite excited about because what we can do is frequency tagging
*  above 50 hertz.
*  So frequency tagging has been used at slower frequencies and the idea is that you might
*  present a participant with a visual display.
*  There's two objects, one you flake at 10 hertz and the other one you flake at 15 hertz and
*  lo and behold, you can see a response in visual cortex to the flake at 10 and 15 hertz and
*  then when you attend to the 10 hertz object, you see an increase in that signal, right?
*  So that works like a charm.
*  The only issue is that it's really annoying to see these flickers and of course, if you're
*  interested in alpha oscillations, then if you start to flake at 10 hertz, everything
*  gets messed up.
*  Yeah, you're blinking a lot.
*  Yeah.
*  But what we have been able to demonstrate is that the visual cortex responds to flickers
*  up to 80 hertz.
*  Don't you have a super, super fast projector though that goes way above 80 hertz, right?
*  Yes, we have a so-called ProPix projector that can go at 1440 hertz.
*  So that's really cool because we can sort of manipulate every pixel on the screen at
*  arbitrary frequencies almost.
*  That's crazy.
*  Yeah.
*  Yeah.
*  So what we then can do is that we can have multiple objects in the visual scene and
*  we flake at them at different frequencies and then we see the response in visual cortex
*  and that response, and as you also mentioned, that flicker is invisible, right?
*  So it's above flicker fusion so you don't see that manipulation.
*  And then we can have multiple objects in the visual scene and then we can sort of manipulate
*  attention if you will and then measure the response.
*  So the question is, so why do we do this?
*  So the thing about these fast flickers is also we can sort of measure the changes in
*  neural excitability on quite a fast time scale because if we flicker at 60 hertz, every cycle
*  is 15 milliseconds, right?
*  So within 20-30 milliseconds, we can see if the attention is changing.
*  So we do this because we want to move towards investigations using more natural stimuli
*  that people can also circuited around.
*  So what we now can do is to also look at the frequency tracking to objects before people
*  are moving their eyes to that object and then see when people start to move their attention
*  and how much attention is being allocated before people move their eyes.
*  So again, the idea is that you can tell about the attention because more of the frequency
*  tagging, more of the hertz that from the side that you're going to attend to gets through
*  because the other frequency that you're tagging at is repressed.
*  Yes.
*  Yeah.
*  You mentioned being able to predict…
*  Well, first, let me back up because we're talking about timing a lot and then I started
*  to think…
*  We think of attention as just a function, but does attention have a timing like how
*  quickly we can allocate our attention and is that…
*  I don't even know if that's a story.
*  Yeah, no, it's a great question because it's something we have been really bothered about.
*  And the thing is we do our good old attention experiment.
*  So we pop up a cue, attend to the left, the cue is on for a few hundred milliseconds,
*  then we wait a second or two and then we pop up some objects for a few other seconds, right?
*  However, so we do our task over multiple seconds and we tell people not to move their eyes,
*  right?
*  However, in daily life, all what we do is to move our eyes around, right?
*  So it's three to four times per second, right?
*  So we have get thousands and thousands of saccades within not so long time spans.
*  So now it turns out that of course some research has been done on that, right?
*  But if you think about what we know about attention and modulation and brain responses
*  and stuff is always over much shorter time scales.
*  And these shorter time scales do not fit well with something that has to happen within say
*  250 milliseconds, right?
*  So if you move your eyes three to four times a second, you have 250 milliseconds to play with.
*  So within that time window, your attention…
*  You first have to sort of process what you fixate at, but then your attention also has
*  to move to where you want to move your eyes.
*  And there might be several objects you want to select from, right?
*  All this has to happen within 250 milliseconds.
*  And to me, that's a big conundrum.
*  And that also means that we need the tools and techniques to be able to study what's
*  going on in the brain with quite a fast time scale.
*  But this is…
*  I thought you were just going to go right into talking about your pipelining model or
*  mechanism.
*  So let's talk about that.
*  Before you do that, so we move our eyes with saccades, which are these ballistics, large
*  eye movements.
*  They can be large or kind of small.
*  And we talked about how that was locked into the alpha phase.
*  Is the same story?
*  I should know this.
*  I bet a previous colleague of mine already published something about this.
*  We're micro saccades.
*  So we were constantly making what are called micro saccades as well.
*  And that's like these little jitters of eye movements, right?
*  So that your whole world scene doesn't change because you're barely moving your eyes.
*  But are those also locked to alpha?
*  Do you know?
*  Yes.
*  Okay.
*  So, yeah, yeah.
*  So that's work by Frig van Ader and Kieran Obra, where they are able to show that if
*  you sit there and you attend to the left, you simply cannot help making these small
*  micro saccades to the left.
*  To the left, yeah.
*  And then your alpha oscillations are also modulated.
*  So there seems to be a correlation there.
*  So to me, that speaks to a coupling between a saccadic system, the saccadic motor system,
*  and the alpha oscillations.
*  So at first that might sound a bit mysterious because we thought alpha was a visual rhythm
*  and so forth.
*  But then thinking about it, of course, the saccadic system and the visual system have
*  to be tightly cobbled.
*  And they also need to be timed in terms of their processing.
*  So it's a speculation.
*  that the alpha oscillations are very much involved in doing that timing.
*  Man, seriously, my previous advisors are going to kill me for not just knowing this off the
*  top of my head.
*  I'll edit that out.
*  I'll edit that out.
*  I'm just kidding.
*  Good.
*  Yeah.
*  No, no, but that, I mean, these are new findings, right?
*  Yeah, in a sense that it's relatively recent that people are starting to look into micro
*  saccades and the alpha oscillations.
*  Yeah, OK.
*  Yeah, I had colleagues in my lab looking at micro saccades, but I couldn't remember if
*  they tied them to oscillations.
*  So I'm hoping not.
*  Now I'm going to have to look it up when we're done speaking here.
*  So OK, so when we were talking about attention, you were talking about the allocation of attention
*  and being able to predict where attention would be allocated by looking at these alpha.
*  And then we were just talking about the timing of attention.
*  You said that that was a big problem.
*  And that brings us, I think this is a good time to talk about that pipelining mechanism
*  that I mentioned a moment ago.
*  So what is that pipelining mechanism and how does it relate to the timing of attention?
*  And maybe, I don't know if we could segue into also the studies on reading that you've
*  done.
*  Yes, certainly.
*  Yeah.
*  So, I mean, the setup for this is 250 milliseconds between each saccade.
*  You have to squeeze in both the processing of what you fixate and you have to squeeze
*  in the planning of the saccade and the pre-processing of where you want to move your eye.
*  How can that all happen within 250 milliseconds?
*  Right?
*  So we think pipelining is involved.
*  So what do we mean by that?
*  So imagine two people doing the dishes.
*  One is washing and then passing on a plate to the other person who's doing the drying
*  and then putting the plate aside.
*  So of course, if they do this in a fully serial way that the guy washing is not going to take
*  the next plate before the guy drying is done, it would be slower as compared to if they
*  somehow work in parallel.
*  So when person two is drying, then person one is picking up the next plate to wash.
*  So this is, I mean, it's sort of the essentials of we think about pipelining.
*  So there's several processes going on, but at different levels of the hierarchy.
*  So the way now to think about it for the visual system is that it could be that you fixate
*  on an object.
*  The first, the low level features are processed maybe in before, right?
*  And then that processing of that object is moving on to object selective cortex and it's
*  then being categorized as an animal.
*  That then leaves open before to process the next item, which then can move on to object
*  selective cortex, which is now done with the first object and so forth.
*  So exactly like washing and drying in the visual hierarchy, there's processing of multiple
*  items, but at different levels of the hierarchy.
*  So that allows you to both process what you fixate at, but then it also opens up the resources
*  that has been processed in early visual regions to do the previewing in early visual region
*  for where your eyes are going to move next.
*  And in my mind, it's simply not possible for the visual system to operate unless there
*  was some sort of pipelining going on because there's simply not time to do every item processing
*  sequentially.
*  Yeah, so I mean, we often, you know, it's old news that the brain operates in a parallel
*  fashion, right?
*  But then when we think of something like the ventral visual stream, we always talk about
*  it in terms of, well, first V1 processes, lines and edges, blah, blah, blah, and then
*  it gets up to higher objects and then we can categorize it.
*  But then we never talk about the dust that's left behind and it sounds like a sequential
*  processing.
*  So first you see the chair and then nothing happens.
*  And then you see the car and then nothing happens.
*  But I like this idea of, you know, at every step in the wake of some sort of visual processing,
*  there is then an opening of resources to do other things and what you're saying, preview
*  other things.
*  Yeah, because I mean, there's also the possibility that everything is going on in a fully parallel
*  process, right?
*  So the two objects, the cat and a dog is being processed at the same time and sort of passes
*  through the hierarchy.
*  But that also creates a bottleneck problem due to the hierarchical organization of the
*  ventral stream.
*  And that's why I would like to think that this pipelining mechanism allows both for
*  sequential and parallel processing at the same time.
*  So go ahead.
*  Yeah, I should say that this is so far speculation, right?
*  So we don't have the evidence for this yet, but that is what we're trying to establish
*  now.
*  But going back to the...
*  Sorry.
*  No, so I don't know if you're going to talk about reading, but it just made me think of,
*  you know, the convolutional neural networks that you talked about that you guys are working
*  on and implementing oscillations in them.
*  Is pipelining a part of that story as well?
*  Yeah.
*  Okay.
*  Because the next question comes like, so just again, imagining the two people doing the
*  dishes, I mean, they better be coordinated, right?
*  Otherwise things go wrong and plates would drop.
*  So how is that coordination achieved?
*  Well, then we think it's by means of these alpha oscillations that's doing the temporal
*  coordination.
*  And earlier you mentioned traveling waves.
*  So we would like to think that there's this traveling wave in the ventral stream that
*  sort of carries the representations through.
*  Gotcha.
*  Okay.
*  So is any of that published on archive?
*  I haven't seen that.
*  Or have you published anything on that?
*  Yeah.
*  So we have a text paper where we speculate on this.
*  Okay.
*  Okay.
*  But again, we are still in the process of trying to find the empirical evidence.
*  Do you want a postdoc?
*  Are you hiring?
*  No, I'm just kidding.
*  So this reading work that you have done, and this maybe leads naturally into talking about
*  the reading.
*  One of the take homes is that faster readers are better at previewing the upcoming word.
*  Yes.
*  So can you?
*  Yes.
*  I'm a really slow reader, so that's bad news for me.
*  But maybe, well, I'll ask you later about comprehension and how that comes into the
*  story as well.
*  But yeah, what have you found in terms of reading and predicting upcoming words when
*  you're looking at a given word, et cetera?
*  Yeah.
*  So that's back to this thinking about the pipelining and the frequency tagging.
*  So now it turns out that we want to study sort of natural vision and visual exploration
*  of natural scenes and how you comprehend those.
*  It turns out to be difficult, right?
*  Because the objects are not well quantified and stuff like that.
*  So going to reading is actually also a good stepping stone for that because it's easier
*  to – the words in sentences are better quantified and you only make saccades in one dimension,
*  right?
*  So what we have been doing is to first look into the saccadic times.
*  And it now turns out that from the eye movement literature, it has been studied for many years
*  how people are doing previewing.
*  So basically, if you focus on word number n and you have word n plus 1, how much do
*  you preview this before you move your eye?
*  Now it turns out that how long you fixate on word n is independent on the word frequency
*  or how difficult the n plus 1 are out there that you are previewing.
*  So that has resulted in different models being sort of quite sequential in the nature.
*  So we sort of challenge that sequential view of reading by using the frequency tagging
*  because what we're doing is that we are flickering this word out there in the paraffolia,
*  in the paraffolia, the n plus 1 word that you're about to move your eyes to at 60
*  hertz.
*  And what we see is that for more infrequent words, the more difficult words, there's
*  a stronger frequency tagging as compared to more easy words.
*  So this suggests that if there's a difficult word being out there in paraffolia, there's
*  more attention being allocated to that.
*  So this is to us evidence for the notion that you're doing the paraffola processing
*  during reading.
*  So it sort of forces a more parallel view of reading.
*  Is it attention or previewing?
*  So you're going along, your phobia, it's like you're reading the word claustrophobic,
*  No, I'll say that you're reading the word I and then in the periphery, you're not at
*  the word claustrophobic yet, but that's an infrequent word.
*  So the sentence is I am claustrophobic and claustrophobic is an infrequent word.
*  And you're saying that the attention, attentional resources are greater to claustrophobic.
*  Does that mean so are you previewing it more than?
*  Yes.
*  But in this case, I would say covert attention and paraffola previewing is one and the same.
*  So what we're getting at is that we want to take the tools and experiences we have from
*  investigating spatial attention, covert attention, and then apply it to more real life examples
*  such as reading.
*  Reading is all about fixating, allocating covert attention, making us a gate.
*  And just to throw this in there, because I think it's an intriguing result, we were talking
*  about the timing of attention.
*  And one of the things that you found is even if you present these words really slowly,
*  that the attentive previewing happens just immediately, even if there's even if it doesn't
*  have to.
*  Yes.
*  Yeah, so and this previewing, it happens within.
*  So you fixate outward N. Even then, the previewing effects start to occur 100 milliseconds in.
*  So it really sort of changes how we think about the speed of the visual system when
*  we're working with these more natural settings.
*  And then really frequent words like the it's not that they necessarily get skipped.
*  Is it just that they get you don't need to allocate much attention to them because they're
*  so automatic because they're so frequent that it kind of well, what is that mechanism?
*  Like how do we kind of skip over the word the but still know it's there and etc.
*  Basically, yes.
*  So so so so you will not linger too much on the when your eyes actually move to that word.
*  Often you would even skip it.
*  Right.
*  But even skipping that word also implies that it has been previewed.
*  Hmm.
*  OK, so so I started this little segment off by saying that faster readers have better
*  previewing ability, essentially.
*  Yes.
*  Yeah.
*  Our slower reader.
*  I don't know if you've tested for comprehension on the material being read, but our slower
*  readers have better.
*  How does this interact with the comprehension of reading?
*  Yeah, no, it's also a very good question.
*  Right.
*  So so I mean, there's this joke about a guy who took a speed reading class and said I
*  read one piece overnight and then his friend like asked him, so how did you like it?
*  And he says, well, I don't really remember.
*  Right.
*  Right.
*  So so that's the point.
*  I mean, of course, if you read really fast, you don't comprehend too much.
*  Right.
*  So so so in this particular study, we check comprehension, but not sort of on a graded
*  scale.
*  But the typical finding is that faster readers are also better readers and also better comprehenders
*  unless you really push people very hard.
*  So they then that that changes around.
*  But in general, fast readers are better readers.
*  So again, I'm coming back to individual differences.
*  I'm wondering if there are different types of people who read fast, but comprehend really
*  well some people who read slow and comprehend better than the fast readers, et cetera.
*  Like how much stock should be?
*  How nuanced are these effects?
*  Do I does this mean that I should work harder to read faster so that I can comprehend better?
*  Or it does my comprehension lead to faster reading?
*  Like, what should I do?
*  Yeah, so so I don't know.
*  So so I have to say, I'm not a reading expert, but we are collaborating with reading experts.
*  But the questions you ask are something some questions we would like to be able to answer
*  with our techniques.
*  So we also sort of can apply our approaches also to see if we can come up with strategies
*  for teaching people to read better and more efficiently.
*  We also want to take this to to to children to investigate when do they start to preview
*  and is that related to their comprehension?
*  And can we through that also come up with strategies for how to teach them to possibly
*  read better?
*  I was going to make an analogy to like our conversation here in terms of predict.
*  You know, I can predict what you might be.
*  What you might what I might predict that you're going to say next, right?
*  But it's different because I have to wait until until you say it to verify it.
*  But when I'm looking at a scene or reading something, I'm constantly predicting upcoming.
*  I can I can preview the upcoming words.
*  So so there's that kind of prediction of what word might be upcoming happening.
*  And at the same time, you have this preview going on.
*  And as I'm reading, I read to my kids every night, you know, and they're fairly simpler
*  books. So I'm like really like predicting kind of far in advance the like what's semantically
*  going to happen, conceptually going to happen.
*  And then I'm also previewing these words.
*  How far out does that previewing happen?
*  I guess out to the as far as your paraphobia will take you.
*  Right. Yeah.
*  So so so we don't know, but we think it goes more than one word, maybe two or three words.
*  So that could also explain why you see the previewing effect at already at 100 milliseconds.
*  But but you mentioned something which is also very important.
*  And that is prediction.
*  So so in a study you referred to, you were very careful about having words that could not be
*  predicted because we want to take away the prediction effect.
*  However, of course, predictions are important.
*  So now Yalipan, so she's the postdoc doing these studies.
*  She's now running a study in which she's specifically looking into the prediction and how that
*  affect the paraphobia processing.
*  And our hypothesis is that if you actually can predict what's coming up, you allocate less
*  attentional resources to that word.
*  So often when I'm reading, sorry to ask you these, you know, have these personal anecdotes and
*  asking you the questions. But, you know, it happens very frequently, especially reading to my
*  children, that I will be I'll still have like a full line below.
*  Right. So I'll be on the next to last line of a page.
*  And then I can without reading all the words, I can be on a word and I don't know if I'm taking
*  it in the periphery, but I can close the page, turn the page and still complete the sentence and
*  the next line that was on that previous page.
*  So then it's almost like it's staying in my working memory or something.
*  So you have this working memory component in addition to the pre viewing and the predicting.
*  Yeah. So I guess that there's the previewing and then also sort of reading ahead.
*  Signedly before you sort of speak out loud what you read.
*  Right. And then there's a working memory coming into play as well.
*  But can you read ahead in the previewing?
*  I suppose you I suppose that that's what previewing is in some sense is reading ahead.
*  Yes. But the question is whether how much you read ahead without moving your eyes.
*  Right. So you can also move your eyes and read the sentence and then keep it in working memory and
*  then sort of say it out loud.
*  You know, there are the scientific journals that print and old classic books print in these
*  like really narrow columns.
*  Yeah. Yeah. I don't even think you probably know this.
*  You know, what's the difference between reading like that and not being able to preview as much
*  linearly anyway out to the right if you're you know, if that's the way that your language goes
*  versus these which is equally there are equal difficulties in the publications where it's really
*  thin single spaced lines, but very wide margin.
*  So you have to like read, you know, 50 words for every line versus reading like four words for every
*  line line in these like thin columns.
*  You know, does this speak to how we should print?
*  Possibly. I mean, so again, I'm not the expert here on that.
*  But but there must be some sort of an optimal medium where the columns are not too wide and not not
*  too narrow. Right.
*  Personally, I find it quite annoying if the column is too narrow.
*  Oh, it's like three words and every other line has a hyphen.
*  Yeah. I wonder.
*  I'm surprised they haven't changed that.
*  I won't name publication names or anything.
*  So, OK, I was going to ask you, I'm glad that we brought up predicting as well, because I was
*  thinking about how to relate these findings to the transformer mechanism in artificial intelligence
*  and these large language models and how essentially they can.
*  They well, so I'm sure you're aware of the studies that relate large language models predicting the
*  upcoming word. Right.
*  And then if it has a high enough predictive probability, then these the ones that generate language
*  will then insert that high most highly predicted word.
*  And I'm sure you know about the studies in neuroscience with MEG and FMIRI being doing this linear
*  transformation to map on and say, oh, yeah, that's what our brains are also doing.
*  We can decode our brain activity such that they're predicting.
*  So how do you think about this in terms of the predictive capacity of the transformer
*  attentional mechanism?
*  I should ask you about what you think about attention as well.
*  And this previewing this peripheral ability.
*  So just to insert one more thing, you know, transformers, you know, you can do everything in
*  parallel. Right. So I don't know that there is any advantage in previewing.
*  It's like they have infinite previewing or something.
*  Yeah. Yeah. Yeah.
*  I mean, so, so, so first of all, I mean, these large language models, right.
*  I mean, they work brilliantly at capture statistical properties of the text.
*  And I think they are an excellent tool for also doing brain imaging type of neuroscience.
*  So if you look at sort of classical psycholinguist studies, it's all about sort of making the
*  perfect data set and controlling every sentence in the words for predictability and what
*  have you. Right. So, so, so, so when psycholinguists, they work, they spend a lot of time on
*  making these perfect data sets.
*  So that's all well and good. But of course, if you want to study more natural language, then
*  there's an issue of how do you quantify the properties of the different words.
*  And then I think tools like GPT 2 or 3 are brilliant at quantifying, say, the predictability
*  of specific words in whatever text you take.
*  Right. So, so as you also mentioned, people are doing that now.
*  To sort of look into what signatures of the brain activity reflects the prediction in
*  relationship to these specific words.
*  So, so as a tool for quantifying different properties of the words in natural text, they
*  are excellent. But I guess what you're also hinting at is, is our brains doing something
*  similar than these large language models, right?
*  Yeah. Yeah.
*  And of course, there's a lot of discussion about this topic these days.
*  Certainly, the architecture is very different, right, from from I would imagine how the
*  neurons they do it. But that does not necessarily mean that they might not have similarities
*  in how they function.
*  But take, take, for example, previewing, right?
*  So should I think of previewing as a so it's a great thing because I can see what's kind
*  of coming up next. But it'd be even better if I could see the rest of the chapter all at
*  once coming up next. Right.
*  And so should I think of previewing as a limitation that a large language model, for
*  instance, overcomes, or should I think of it as something that's like integral to our
*  human like intelligence and therefore should be considered more in terms, you know, like
*  building oscillations into large language models or into deep learning models, right?
*  Or any type of AI. How should I think of previewing it in that respect?
*  Do you think an attention?
*  Yeah, at least sort of previewing a prediction when you're reading, you're probably also
*  building up expectations for what would be coming up in the next sentences, maybe not
*  word to word, but sort of conceptually more conceptual point of view.
*  Right. Yeah.
*  So, yeah. So so so and then you sort of match those expectations with the actual text as
*  that unfolds. And then then you might update your expectations if if if they are wrong.
*  Right. So so but then that sort of gets into the realm of of of predictive coding.
*  Right. And how these updating mechanisms are operating.
*  All right. So in a moment, we'll have a little extra time so I can ask you some questions
*  that some of my Patreon supporters have sent in.
*  And also, I just have a few extra questions for you.
*  But what are you what are you excited about these days?
*  Are you excited about I'm sure it's more than one thing, but it's one of the things like
*  building these oscillations into the deep learning type models.
*  What else can we look forward to?
*  What's exciting you these days?
*  So what is really exciting to me is a new type of MEG system.
*  Right. So we talked about ED where you measure the scat potentials.
*  But MEG we are measuring the magnetic fields generated by neurons in the brain.
*  Typically, we use sensors that are immersed into liquid helium.
*  So they become superconducting and we can measure these tiny, tiny magnetic fields.
*  It works like a charm.
*  But if we want to study children, for instance, the heads are too small for these MEG systems.
*  So they just bob around.
*  Furthermore, the sensors are also sort of a bit far from the frontal lobes because you
*  lean back.
*  So now it turns out that there's a new type of sensors called optically pumped magnetometers.
*  And they with those.
*  So it's by an optical technology called the optical magnetometer.
*  It's an optical technique where you can measure also very small magnetic fields.
*  And these sensors do not require to be cooled by liquid helium.
*  So several groups are now making these so-called OPM systems to measure the brain activity
*  that like an MEG system would do.
*  But you can put the sensors closer to the head so you get a better signal to noise.
*  You also can measure better from frontal regions.
*  And in particular, you can start to study children much better because you can adapt
*  the helmets to the individual brain sizes of the children.
*  So I'm quite excited about the prospects of now developing an OPM system for investigating
*  children.
*  Also, to get back to oscillations, we know that alpha oscillations, they change in frequency
*  with the lifespan.
*  So if you take like a say, four year old child, they might have the alpha oscillations being
*  six, seven hertz.
*  And then they accelerate to about 10 hertz.
*  Then the child is like 10, 12 years old.
*  So if and if you were to go back to the causal issue of these oscillations.
*  Well, now, if these oscillations are changing in frequency over that short lifespan, you can
*  also ask how does that impact your processing, your visual processing, your attentional processing
*  and so forth.
*  But we talked about reading.
*  We can also use this system to now investigate previewing in children and when children start
*  to preview as a consequence of say, maturity and when they learn to read fluently.
*  And is that previewing important for fluid reading and so forth?
*  But the speaking of causality, right, the developing brain, all these synapses are developing
*  and being pruned and you're still myelinating and the structure is slightly changing.
*  So there's still that causal interaction that is kind of an open question, right?
*  Yes.
*  Yeah.
*  But we can still, I mean, if you have a hypothesis about what the alpha frequency is doing in a
*  given cognitive task, then we can also ask how does the performance in that task change
*  as the frequency of these oscillations are changing?
*  I know you're also interested in dyslexia and studying that.
*  And what's the hypothesis that do so dyslexia has long been under diagnosed, I guess.
*  And I know you're not a medical doctor, but all my children's friends seem to have dyslexia.
*  And I don't know if I do.
*  I don't.
*  So many people probably had dyslexia and just were not helped because it was under diagnosed.
*  Are dyslexics not previewing or is it a previewing malady?
*  What's going on?
*  What's the hype?
*  What's your idea?
*  Yeah, also also a very good question, because there's also this debate in a field that what are
*  the root causes of dyslexia?
*  And I think there's a strong consensus that children diagnosed with dyslexia has a problem
*  sort of mapping the words onto sound.
*  Right.
*  So is in that translation from the text to phonology where there are problems.
*  And that's also what they are being trained on.
*  Then there are people who would argue that dyslexia is about spatial attention problems.
*  So now there's different kind of dyslexia, right?
*  So both could be correct.
*  Yeah.
*  But one going hypothesis is that children with dyslexia have to work harder on each word in order to do
*  this mapping.
*  So they do not preview.
*  So it's not necessarily a spatial attention problem they have at first, but they process every word
*  one at a time.
*  So it's a very serial processing.
*  However, through that, they do not train themselves in this sort of spatial allocation of attention
*  during reading.
*  So that would also explain why some people find spatial attention problems in children with dyslexia.
*  So the idea is that's a hypothesis.
*  It's a hypothesis.
*  Yeah.
*  So the idea would because attention is a limited resource.
*  And so if they're allocating that limited resource more to each word, then their previewing is
*  disrupted.
*  Exactly.
*  And then they don't get trained in the same extent as compared to children not having dyslexia in
*  allocating a spatial attention.
*  And then you might find a general spatial attention deficit or the root cause is problems in
*  mapping text and phonology.
*  That's interesting.
*  So Ola, thank you for spending time with me.
*  And I appreciate you explaining so much of your work and talking oscillations with me.
*  Here's to oscillations in their continued waxing in the pantheon of phenomena to study
*  brains and cognition.
*  So thanks for being with me.
*  Yeah, thanks very much.
*  It was great fun and a really good discussion.
*  I alone produce Brain Inspired.
*  If you value this podcast, consider supporting it through Patreon to access full versions of all the
*  episodes and to join our Discord community.
*  Or if you want to learn more about the intersection of neuroscience and AI, consider signing up for
*  my online course, Neuro AI, The Quest to Explain Intelligence.
*  Go to braininspired.co to learn more.
*  To get in touch with me, email paul at braininspired.co.
*  You're hearing music by the New Year.
*  Find them at thenewyear.net.
*  Thank you.
*  Thank you for your support.
*  See you next time.

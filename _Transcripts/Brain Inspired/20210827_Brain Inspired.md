---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 4438s
Video Keywords: ['Education', 'Science', 'Technology']
Video Views: 2047
Video Rating: None
---

# BI 112 Ali Mohebi and Ben Engelhard: The Many Faces of Dopamine
**Brain Inspired:** [August 27, 2021](https://www.youtube.com/watch?v=ryUZf16yOmk)
*  I blame physicists for this for coming up with a unifying theory that's to like, trap
*  everything.
*  I don't know if we can do that about brain or not, because brain is true for physics
*  as well, but brains were not like design.
*  They were evolved.
*  Once I got into dopamine more, I started liking it more because it has some idiosyncrasies
*  that are very particular about dopamine.
*  You know, sort of like the very simple story on the one hand, you know, the very complex
*  reality on the other hand, and the relationship between computation and experiment, and all
*  of that makes it very enticing for me.
*  So this adds, I think, even more complexity, that like, what is the computational units
*  of the brain?
*  I actually think a little bit of the opposite, which is I think that AI and neuroscience
*  are actually coming closer together.
*  This is Brain Inspired.
*  Hey everyone, it's Paul.
*  Those voices you heard were from Ali Mohebi, who's at University of California at San
*  Francisco, and Ben Engelhard, who right now is at Princeton, but will be starting his
*  own lab at the Technion Israel Institute of Technology.
*  So Ali and Ben love dopamine, so much so that they are two of the organizers of the virtual
*  dopamine conference that just had its second iteration.
*  They also love each other, which unfortunately I had already stopped recording when they
*  expressed that mutual admiration.
*  A lot of love in this episode.
*  But today's conversation was originally intended to be a precursor, sort of an introduction,
*  for the panel discussion that I moderated at the recent dopamine conference.
*  And that discussion that I moderated you'll hear soon.
*  It'll be the next episode that I release.
*  But when people love something, they love to talk about it also.
*  And so we did.
*  We talked.
*  And it went longer than we thought it was going to go.
*  And here we are with a full conversation about dopamine.
*  So as you probably know, dopamine is a neuromodulator in the brain.
*  And it's become kind of a darling in AI and in neuroscience because its release in the
*  brain correlates well with a computational process called the reward prediction error
*  and helps drive learning in that way.
*  So during our conversation, you'll hear more about that.
*  You'll actually get the backstory of how dopamine came to be important, how people have thought
*  of it in the past, how it came to be the darling of reinforcement learning in AI in
*  its simple, elegant role, computing that reward prediction error, and how now, like everything
*  else in the complex mess and or beauty of biology, it seems to be involved in plenty
*  of other cognitive functions.
*  So this conversation is a lot about dopamine and its various roles in cognition.
*  And we talk a lot about those various cognitive functions.
*  And we talk about how to think about the role of dopamine and other neuromodulators
*  with respect to integrating them into a computational role with what we traditionally think of as
*  computing events in the brain, like the spiking of neurons.
*  And I also get their reflections on the deep reinforcement learning panel that you will
*  hear soon.
*  Thanks for listening and enjoy Ali and Ben.
*  Ali, Ben, thanks for doing this.
*  So normally what I do is in the introduction to these things, I kind of introduce what
*  the topic was about.
*  But I thought it'd be fun to have you guys on since you co-organize the dopamine conference
*  and kind of get your reflections on the conference as a whole, but also on this panel that people
*  will be listening to in just a moment or two.
*  So I guess, you know, I don't usually do this either, but maybe can you just say a word
*  about who you are and what you do?
*  Ali, start with you.
*  Oh, okay.
*  So yeah, I can start.
*  I'm Ali Mohebi.
*  I'm a postdoc at UCSF Department of Neurology.
*  And I am very interested in dopamine and what role it plays in motivation, learning, cognition,
*  et cetera.
*  Okay.
*  So I was going to, I immediately want to ask a question, but then maybe you could say just
*  a word about yourself.
*  Yeah.
*  So I'm Ben Engelhard.
*  I'm also a postdoc currently at Princeton in the neuroscience department and starting
*  my own lab in a couple of months in the Technion Institute in Israel.
*  Congratulations, Ben.
*  Thanks so much.
*  Although we were just talking a moment ago about how hard that move is going to be in,
*  especially in today's climate and just in general, selling cars, things of that nature.
*  Yeah, but you know, with three kids, I'm sure it's going to be a breeze.
*  How did you guys get interested?
*  So first of all, this was year two of the dopamine, the virtual dopamine conference.
*  Just give us the backstory of how the conference got started and tell us all about the super
*  high demand that led to it being continued in year two.
*  Yeah.
*  So I'm going to give a brief response and let Ali take over because the way I sense
*  it started is one day Ali Moebi woke up and said, we're in the middle of a lockdown.
*  It's I think it was April 2020 or something like that.
*  And he said, you know, we can't do anything.
*  We can't go outside.
*  We can't have a conference.
*  We can't meet people.
*  Let's change that.
*  And so he basically recruited a few people, either students or postdocs.
*  We were five in total.
*  And he said, you know, let's let's make a conference.
*  And so that's how we started.
*  And then we ended up organizing everything pretty quickly.
*  We started contacting all the speakers.
*  We had an amazing response.
*  We contacted some of the best speakers in the field.
*  And pretty much everyone said, yeah, I want to do it because nobody could do anything,
*  I guess.
*  So we're the only the only option in town.
*  And that's how the first one started.
*  And I think that because it was available to everybody anywhere in the world, we got
*  over 2000 people registering, which is a pretty large number for sort of a niche, you know,
*  neuroscience conference, you know, for the subject of dopamine, not just the neuroscience
*  in general, but just dopamine.
*  Yeah.
*  So that was a huge success.
*  And also the quality of the talks was was very impressive.
*  So Ali, did it come to you in a dream?
*  So you just woke up and it was there.
*  So I live in San Francisco, which means that I'm locked in a like teeny tiny studio box.
*  And then we went into lockdown.
*  I was going crazy.
*  I'm just bouncing off the walls.
*  I thought you were going to talk about a psychedelic experience because you were going to go that
*  route there.
*  But yeah, I mean, I think my friend Christine Liu, at some point, she suggested this idea
*  on Twitter that, well, our dopamine meeting is going to get canceled.
*  We were all supposed to go to Montreal for this dopamine meeting.
*  And then she was like, yeah, it would be nice if we have like a gathering of a few
*  of us enthusiasts.
*  And then during a psychedelic trip, perhaps or something, it came to my mind that what
*  if we do this conference?
*  What if we put a conference together, a virtual dopamine conference?
*  And I reached out to Christine and I'm like, Christine, let's do this.
*  It was an amazing experience for all of us.
*  Yeah.
*  So the dopamine, dopamine, my role in this was I moderated this panel that people are
*  going to hear that is was based off the premise of modern, the explosion of modern deep reinforcement
*  learning and kind of how that interacts with the rest of the dopamine story.
*  So which is, I don't know how much of the dopamine, how much of the conference is focused
*  on the sort of systems neuroscience part of dopamine versus the reinforcement learning
*  side.
*  I mean, it's a big blend of all of it.
*  But how did you guys get into dopamine?
*  Dopamine was something I always avoided when I was going through a computational neuroscience
*  program because it was too systemsy, you know, too wet.
*  And it was but it was everywhere already back then.
*  Dopamine, dopamine.
*  But I was like, ah, that's unimportant.
*  So how did how did you guys get into it?
*  So I got into it.
*  I got into it by mistake.
*  My PhD had nothing to do with dopamine.
*  I was working on cortex, you know, doing like cortex like things, you know, brain machine
*  interfaces and learning and stuff like that.
*  And I think the link to learning a little bit maybe led to that direction.
*  But it was mostly when I was looking for postdocs in the US and I traveled all around the US
*  and talked to a bunch of people and I started to see what I want for my postdoc.
*  And what there was at Princeton was this sort of for me an amazing opportunity working with
*  people like Ilana Witten and David Tank in a virtual reality system with mice and sort
*  of cutting edge technologies.
*  And it was about dopamine, which is related to learning, which is something that I was
*  cared about.
*  So, you know, all these things together, I said, let's do this.
*  And once I got into the dopamine more, I started liking it more because it has some, I would
*  say some idiosyncrasies that are very particular.
*  Even within the system neuroscience field, you know, there's something very particular
*  about dopamine.
*  You know, sort of like the very simple story on the one hand, you know, the very complex
*  reality on the other hand, and the relationship between computation and experiment and all
*  of that makes it very enticing for me to study.
*  The very simple story that you referred to there is what deep reinforcement learning
*  is kind of based on.
*  It's one of the most quote unquote successful stories in bringing together things like artificial
*  intelligence and things like neuroscience that dopamine underlies a reward prediction
*  error that leads to reward.
*  And there's very specific circuitry associated with it.
*  But but the other thing that you alluded to is that that's that's not the only story.
*  And we talk about that some in the panel as well.
*  But so I just wanted to make sure that we have I hammered that home that I believe that's
*  the particular story you were referring to.
*  Yes, it is, you know, to learning, you know, the ideas by by Schultz showing the real
*  prediction, a response of dopamine urine and how to relate to learning.
*  Then the idea that this is basically a signal that's propagated throughout the brain and
*  mostly striatum.
*  The signal goes, let's say, to ventral striatum, the acumbens, which is sort of considered
*  one of the sites for learning.
*  And then you potentiate the corticosteroidal connection, the synapses, you know, based
*  on this reward prediction error signal.
*  And that's how you learn.
*  And, you know, that's works great for simple things like pulmonary conditioning.
*  And there's been a bunch of experiments showing that.
*  But the more we learn about the circuitry and the more we do behavior that is more complex
*  and the more we look at the brains in general, we see how this simple story is starting to
*  become stickier and stickier.
*  Ali, is that sad or is that a happy thing that because dopamine has a bigger role now,
*  we think? Yeah.
*  OK. So actually, I want to have a revisionist history of dopamine.
*  I think we should go back to where it all started from.
*  Right. I mean, so if you look at dopamine and what's like dopamine, what did we know
*  about dopamine and when?
*  I mean, dopamine, we knew at some point that had something to do with movement.
*  Right. And we knew this like many other things in neuroscience by a malfunction.
*  So we know that in Parkinsonian disease patients, they lose their dopamine cells, majority
*  of the dopamine cells, and they something becomes wrong with their movements.
*  Right. So for a long time, people believed them were looking for movement related signals
*  in the dopamine. And then at around the same time, there was this other idea.
*  Of dopamine having some role in learning from rewards, which was which goes back to like
*  old and milliner's stuff in McGill, where they would put an electrode, they would stick
*  an electrode in the rat's head.
*  And every once in a while, when rat is visiting one corner of the cage, they would zap him
*  or her and then they would see that rodent, the rat is more interested to explore those
*  corners of the cage.
*  And then they realized that depending on where exactly they stick this probe, the likelihood
*  of rodents visiting those corners becomes more and more.
*  And when they put it in like midbrain VTA, dopamine, ergic cells, I mean, this is where
*  the rats get start visiting that corner more and more often.
*  So people started hypothesizing that dopamine has something to do with reward.
*  So these two accounts start to develop mostly independently.
*  One is more like in the psych department.
*  And then on the neurology side, people interested in Parkinson's disease started looking at
*  dopamine and interpreting dopamine in that sense.
*  And so, I mean, another thing that perhaps inspired by Skinner and Walden too was that
*  there's some aspect of reinforcement in this dopamine signals because like old and milliner
*  were able to teach the rats to press a lever by linking a lever press to zap in the
*  dopaminergic system. So they stick electrodes, zap them, they learn to press a lever.
*  So there's now some reinforcements that motivates you to go and push the lever further
*  and further.
*  You just you referenced Walden too.
*  Was it I read that book many years ago before I knew what before I was a neuroscientist.
*  Is that actually in that book?
*  And is that a good book?
*  Should I reread it?
*  I don't think I should, but maybe you should reread it.
*  Yeah, I read it like a year or two ago and it was interesting.
*  I think if you have ideas about how to shape society or how to like reinforce acts or values
*  and virtues that you want and is it even possible?
*  I think it's a good idea to revisit that book.
*  But it's a novel, right?
*  It's a novel by Skinner, right?
*  So, yeah, he was here.
*  Right. So, I mean, this whole idea of how you can reinforce things and put, uh,
*  potentiate acts and things that you value more.
*  Right. So, and like here, it's like quite related also.
*  I mean, this, these whole series of experiments.
*  Another reason they got a boost was that this is a good animal model for studying addiction,
*  that you get some stimulation in the dopaminergic system and you keep going back and back to the
*  sites that you received this stimulation or keep doing the acts that led you to this feeling of it.
*  So, this is how like dopamine got involved in the addiction research and in the motivation.
*  But then these fields evolved separately from each other.
*  And Wolfram Schultz actually in his last year's talk at Vita, he started going through this very
*  brief history of dopamine that when he started looking at dopamine, he was after the movement
*  signals. He had like monkeys sitting on a chair and moving these bars, doing center
*  outreach tasks and such. And to his surprise, there were like absolutely zero dopamine cells
*  that would respond to the movements itself. And they were confused.
*  He was like, yeah, I'm recording from muscles. I'm recording from mouth. I'm recording from eyes.
*  I see movements. I see movement signals in the EMG of this, these muscles, but I don't see
*  anything in the dopamine cells. And years later, I mean, with the advent and popularity of
*  reinforcement learning, people started looking at and reinterpreting Schultz data and they realized
*  that it might have something to do with the reward prediction error. So, I think the dopamine story
*  did not start. So, this is the revisionist part. It did not start with the prediction error.
*  No, I agree. But I agree with what you said about sort of the diverging views about the movements,
*  Parkinson slash Parkinson studies and sort of the addiction slash reinforcement studies.
*  But I think that at least at some point and probably even now, but certainly, you know,
*  previously people sort of thought about because we know that there are different sort of canonical,
*  pathways of dopamine, more typically, you know, what's called mesocortical limbic, perhaps,
*  which is, you know, VTA to a convulse and then to cortex. And then perhaps this nigrostriatal,
*  which is, you know, substantia nigra pars compacta to striatum, this dorsal part. And so,
*  I think that people did associate sort of the nigrostriatal pathway mostly with Parkinson,
*  because in Parkinson, dopamine neurons will die out mostly in the SNC and not so much in the VTA.
*  In fact, there is sort of like a line that sort of divides. And you can actually look at it,
*  if you stay for something called combining and actually see the difference between SNC
*  and VTA, the neurons and the SNC one died, the VTA does not. And the SNC have sort of
*  somewhat of different projection pattern. So, I think people associated the movement
*  Parkinson function with depth of these, you know, SNC, substantia nigra dopamine neurons,
*  and perhaps even having a permissive role rather than a proactive role. So, the idea is that
*  maybe if you have enough dopamine in striatum, because these dopamine neurons that give you
*  this sort of tonic signal, right? So, this constant, you know, constant release of dopamine,
*  maybe that's enough to have movements and that's all you need. And then maybe that's why you're
*  not seeing any movement signals in these neurons, perhaps. And the VTA neurons, the sort of mesocortical
*  limbic pathway, that the one has been more associated with reinforcement, as well as addiction
*  and perhaps motivation. I don't disagree. I think one of the appeals of the dopamine story in the
*  past was that how like beautiful, there's like a unifying theory of dopamine cells, and this is a
*  global broadcast signal that's just sitting there. And if you read some of like Schultz's older
*  stories, or even like others, have been proposing dopamine as this broadcast signal,
*  that these cells are just sitting there regardless of which type they are recording from SNC cells.
*  In the case of Schultz, most of actually his recordings were from AA to SNC, and then some
*  from VTA. Majority of them do send this broadcast word prediction error signal. And I think that's
*  one of the beauties of this theory. But then in recent years, there's people are paying more and
*  attention to like different functions of dopamine, such as yourself in your 2019 paper, where you
*  start talking about different roles that dopamine cells have in different functions. So I think we
*  are, it's exciting times to be studying dopamine, because we are going back to some of our like
*  original thoughts, because like the appeal of this word prediction error theory, I think was so much
*  and it made us like focus a bit too much on one aspect of dopamine function for the past maybe
*  20 years. And like early on, another aspect of dopamine function that I forgot to mention is
*  its role in cognition and cognitive aspects like working memory, attention, and through the work
*  of one of the early works from like late 70s from Pat Goldman-Rakish and her colleagues at Yale
*  University was that how dopamine in the prefrontal cortex plays a role in sticking to ideas,
*  keeping something in your mind, right? And like she and her colleagues ran a bunch of experiments
*  like increasing dopamine in the cortex, specifically in the prefrontal cortex or
*  ablating dopamine in the prefrontal cortex and see how like these like working memory function
*  get affected and they link it to some mental health disorders such as like ADHD, schizophrenia,
*  and others. But this work is also I think has been overshadowed by this success of the dopamine
*  equals reward prediction error theory. And people are slowly going back to those ideas using new
*  tools and testing some old theories coming up with new hypotheses, etc.
*  Well, this is why I asked though if it's a sad thing because there's an attraction to the
*  simplistic explanations of because it's a simple explanation is powerful, right?
*  Dopamine is this. And of course, but the problem is it's never that way, at least in the brain.
*  But you know, I can't tell you how many times I've been reading, you know, there's a story about
*  two brain areas that are connected in some directional way. And then just a few years later,
*  it's always actually they're also connected by directionally and through three different
*  pathways. And it just always just explodes into the mass of complexity that is the problem that
*  is the challenge of facing facing us. Yeah, I think that, you know, we, I mean,
*  naturally, I would say we tend for to look for this sort of simplified explanations, because
*  that makes it easier to understand. I mean, otherwise, it's very hard to just from the very
*  get go look at something that's incredibly complex and make sense of it. And with regards
*  to what Ali said about sort of the the working memory by Goldner, Rakech and others, that was
*  also together with the movement story, that was also at least in part, I think by them to associate
*  with sort of the idea of a tonic dopamine signal, sort of like a very slowly changing dopamine release.
*  And that was contrasted with the sort of phasic signal, which was like a very, you know, very
*  strong rapid burst of dopamine years, which was associated with the reward prediction error. So
*  even then, when the dichotomy was known, right, because it was known as Ali said, from the 70s,
*  79 was the was the main paper that was published by Goldner and Rakech. It was known that there is an
*  effect in working memory and there is an effect on movement. People say, you know what, there's
*  sort of like these two dopamine signals, the tonic one, that sort of like changes very slowly,
*  and has a mostly permissive role, sort of allowing the downstream circuits to do their thing,
*  either movements in striatum or perhaps working memory in frontal cortex. And then you have this
*  sort of phasic signal, sort of like rapidly changing rapid bursts that would have a role for
*  reinforcement. And again, of course, that cannot, you know, it's not going to turn out to be the case
*  because, as you said, things are always more complex than they seem. But I think it makes sense
*  to start with some. So I'm not criticizing, you know, the past because it makes sense to start
*  with that. You need to have a starting point where you can make sense of things. And it's not wrong
*  to simplify as long as you keep an open mind that it's probably going to be more complex that you're
*  sort of simplified. I mean, this is a topic for another conversation elsewhere, but maybe I should
*  just mention for the reference that I don't believe in tonic dopamine, right, but we can discuss it.
*  Oh, no.
*  You don't believe in it?
*  I don't believe in it. I wrote about it.
*  You have to address that now. Yeah. It's a slight diversion and that's fun. You know,
*  the antagonism is good for the podcast.
*  Let's diverge.
*  Okay, let's diverge. I mean, I don't understand what tonic dopamine means. I mean,
*  with the dopamine signal, what you measure is either firing of dopamine cells, right?
*  Dopamine cells have the tonic firing. That is, in their pacemaking cells, they fire
*  like three or four spikes per second on average, some of them a bit more, some of them a bit less.
*  But then sometimes they fire these bursts of spikes. And that's how they do. You don't see
*  dopamine cells changing their baseline firing rates at all. Like I've recorded from a bunch
*  of dopamine cells. I haven't seen anything like this, which Ida's lab have recorded,
*  Jeremiah Cohen and others in his lab have recorded from a bunch of dopamine cells.
*  You don't see at any point in time, dopamine cells change their baseline firing rate. So
*  we don't see it in any context. We have tried it a few times. I mean, of course, absence of evidence
*  is not evidence of absence, but we don't see it in any context.
*  I'm surprised by this argument coming from you, Ali, because you're one of the main people that
*  are sort of exploring this idea about how actually the release of dopamine in the actions of these
*  cells might not be related in some cases to the firing of the cells themselves. So you can still
*  have fluctuations based on sort of external processes like maybe acetylcholine, right? Which
*  I think you're explored as well and other people do. And so you can have sort of a baseline 5
*  hertz or 4 hertz firing, which will give you a relatively constant with some noise fluctuations
*  of a tonic dopamine release. And then you could have sort of modulation of that release perhaps
*  with some sort of external processes. And of course, we don't know how much modulation we
*  actually need because again, if it's a permissive role, then it's enough to have maybe the 5 hertz
*  gives you what you need to have movements. And then maybe there is some modulation on top of that,
*  which will make movements, you know, change them a little bit. I think with Golder and Rakic,
*  they have this inverted U shape sort of idea where you have too much dopamine is not good and too
*  little dopamine is not good and sort of, you know, the Goldilocks idea of dopamine for working memory.
*  So maybe the 5 hertz is sitting somewhere, you know, around the Goldilocks zone, and then you can
*  have sort of external processes that would modulate that. So that's why I was surprised
*  by this argument coming from you of all people. Okay, just to answer your surprise and then we
*  maybe we can move on. I mean, this could be like a never ending conversation. I'm happy to chat
*  further. But I mean, yes, so that's the second part of my argument that now when you look at
*  dopamine release, you don't again see slow events. So with tonic, what people often mean is that
*  there's this like inherently slow change in the signal. When we look at dopamine release, there's
*  also now that we have the tools to look at them, like in the very fine temporal resolution, you
*  would see these like rapid bursts of activity or like slow, very fast changing. So one thing that
*  I think and we think in our lab that might have alluded to this tonic modulation of dopamine
*  concept was that our measurement tools of dopamine release were slow. So if you measure
*  signals slowly, you may deduce that it's a slowly changing signals. But as you start using better
*  and better tools with better temporal resolution that's made available just in the past like two
*  or three years, we don't see slow changes in dopamine signal. What is slow versus fast here
*  because a spike is fast and neurotransmitter is slow, but it depends on how. That's exactly one of
*  the I think one of the reasons I think this tonic dopamine thing is ill defined that no one can give
*  a good time scale of what is the time scale of a phasic versus tonic dopamine. If it's changing
*  faster than or slower than 20 hertz, is it now called tonic? Tonic is a task of micro dialysis.
*  Right, because in micro dialysis you measure like dopamine concentration every 10 minutes.
*  So it could be, I mean this whole notion could have been just a... No, but I obviously I'm joking,
*  but look for example in cortex we know that the reuptake of dopamine is pretty slow, right?
*  Compared to for example the striatum where the reuptake is pretty fast.
*  So or ion channels in a neuron membrane, right? That's right.
*  So you can well imagine that even if you have sort of fast signals in dopamine release,
*  because the slow kinetics of the reuptake in cortex for example, you could end up with sort
*  of like smeared slower changes in dopamine concentrations. And the other point is that
*  I don't think that the theory required, for example by Goldner and Rekich, I don't think
*  the theory is required like very precise modulation of the tonic signal. The idea is that
*  so you're in a bath of dopamine and if you have a good enough level within a range,
*  you can do, you know, your working memory is gonna work fine, right? So I mean you were talking about
*  the modulation of the tonic signal, but I don't think that was ever really a strong focus of either
*  of these theories. I mean yeah that goes into, I mean many of those studies, I mean these were like
*  super illuminative and like insightful for me, but they were using like late 70s tools which mostly
*  is like slow pharmacology. I mean dump bunch of dopamine in some part of the brain, let it stick
*  around for a few hours and see what effect it has on like activity of these cells, which is very
*  different from its physiological time course. And now I think with better tools like optogenetics
*  and other things, we can have, we can start like dissecting dopaminergic signals in the frontal
*  cortex within the physiological time range that dopamine is affecting it. And in fact, that's
*  something I will be doing in the next few years. Oh very nice. Let's go ahead. Yeah, no, I just
*  want to say again a little bit playing a grumpy advocate that it's true that, you know, optogenetics
*  in terms of the temporal resolution is so much better than pharmacology, but in terms of the
*  I don't know, like cellular resolution or maybe spatial resolution, you're still, when you're doing
*  for example activation, you're activating in a very non-physiological way, right? You activate the
*  entire ball done bundle, you know, super strong. So I think that we don't really yet have, you know,
*  if you talk about, you were talking about physiological sort of like endogenous like type
*  of manipulations, I don't think we're there yet. I should say more physiological. Definitely, no,
*  I would agree with that. But I just want to point out the caveat that we're still, you know,
*  we still don't have the tool that would say that would give us the ability to, you know,
*  do a manipulation that would really mimic the way the activity is normally happening.
*  See, this is a good illustration of taking a perfectly simple story. There's phasic and
*  there's tonic and just finding all sorts of problems with it and issues and, you know,
*  there's a complete gradient between phasic and tonic and maybe there's an analog computation
*  within that gradient, blah, blah, blah. And it seems like if the brain can do something with
*  the tools it has, it does. And I don't know, maybe this is a good time just to segue into the panel
*  discussion. Come on guys, rein it in, rein it in. No, but I think that this was a good illustration
*  of the complexities involved in these sorts of things rather than so what, you know, now all of
*  a sudden, deep reinforcement learning is looks like a very simple, clean story relative to like
*  what's actually happening in the brain, which is, you know, presumably these are things are all
*  based on or related to or an analog of dopamine related computation in brains. So maybe just kind
*  of to segue into that, into the topics that we discussed in the panel. I don't know if you guys
*  have thoughts about how the panel went or if anything surprised you or if, you know, it was
*  kind of on par for the deep reinforcement learning kind of discussion. I don't think I was really
*  surprised. I was hoping that we would go a little bit more and talk about dopamine, I guess, because
*  the nature of the conference and that didn't happen too much. But I think that's sort of a reflection
*  of where the field is right now, which is sort of we're still grappling with the idea of deep
*  learning vis-a-vis brain learning. And we sort of stuck a little bit in trying to figure out the
*  differences and similarities and how to actually relate that. And I think that most of the people
*  that work with deep RL, they don't care about dopamine at all. I mean, they either care about,
*  doing better AI or perhaps care about maybe relating AI to behavior. And I think what's
*  really missing is the third part of the triangle, which will be the circuit itself. And I think that
*  part seems to me, and Ali maybe has a different perspective, more removed from the conversation
*  related to deep RL right now. But that was the part that we were trying to focus more, I guess,
*  in the conference. But I think the panel reflected where the field is, which is more,
*  okay, thinking about the AI part, and perhaps the behavior part in a maybe more high level part,
*  more high level view, and a bit less, more removed from the circuit.
*  There was circuitry talk in the beginnings. And I don't know if it continued throughout.
*  And I tried to keep bringing it back. But to your credit,
*  Yeah, thanks, man. I was feeling down about it. But to your credit, one of the questions
*  within the abstract is, can these new advances in deep reinforcement learning help us understand
*  the role that dopamine plays in learning? But you're right. It was not very dopamine
*  focused most of the time. Yeah, I mean, one thing that surprised me, I think, was like Matt, but
*  when it self-acclaimed radical idea towards the end that brains are deep learning agents, or
*  something to that extent, deep learning, deep RL systems, which is interesting. I'm not sure if I
*  agree with that. Because I mean, how would you define deep? I mean, maybe these are just like
*  loaded words. You can define anything to be like deep reinforcement learning. But is it true? Is
*  it true that brain is implementing a reinforcement or a deep reinforcement learning algorithm?
*  Are we by this discrediting all the other cognitive aspects of brain function, for example,
*  like the memory systems, right, that are somehow again involved with like dopamine, or like,
*  either it's like hippocampal episodic memory related systems, or like prefrontal working
*  memory type systems. I mean, these are involved in learning in many kinds of actually tasks that
*  we train human and animals to perform. It's not just a simple reinforcement learning algorithm,
*  like a Q learning actor critic or any of these systems that are involved. So I'm not sure. I
*  mean, yes, maybe if you define like memory to include what? You're not sure? I am not sure if
*  like, yeah, I mean, there's an appeal to this. And I think it's, I blame physicists for this for
*  coming up with a unifying theory that's like, wrap everything. I don't know if we can do that
*  about brain or not, because brain, I guess, is true for physics as well. But brains were not
*  like design, they were evolved. And one of the fascinating ideas in neuroscience in general,
*  for me is that you have these like multiple different systems that were evolved during
*  different times for different purposes, and then they compete with each other for behavioral
*  expression. So if you're learning to solve a two armed band-aid problem, for example, I mean,
*  if you're designing an algorithm, you can design a reinforcement learning algorithm that would solve
*  this like beautifully and perfectly using TD reinforcement learning algorithms. Use just an
*  RPE and action values, etc, etc, to solve this. But when you train a human or train a rat, a
*  monkey to do this, are they just doing it the same way that you do? And I think this goes back maybe
*  to a broader question, reflection of neuroscience these days that can you, if you can explain an
*  animal's behavior using a computational model, can you then infer from this that brain is using
*  that specific process to solve this problem or not? And I would like to see more conversation
*  about that. I think this was like a blessed panel with the start of the conversation. But in the
*  coming years, I would like to see more and more conversation about like, what is it that we can
*  learn that's like, are we at a point that the divergence between artificial intelligence and
*  neuroscience has gone so far that there's no way I mean, these are now different, like totally
*  different processes, different disciplines, or are there things that can each learn from each other?
*  And I think there was a good start for this conversation.
*  All right, so that was very interesting. I want to remark on several things. I won't have time to
*  just pick a couple. So the first is that, I mean, you were very, very polite when you said, I'm not
*  sure whether the brain is in our deep parallel system. Look, I don't think Matt believes that
*  the brain isn't. I mean, it was obviously sort of, you know, putting it in sort of an extreme way,
*  provocative. And obviously, he works on the parallel system. But clearly, we know that
*  the brain does so many different things in so many different ways that it cannot just be one thing.
*  I think the question is whether there is reinforcement learning happening at all in
*  the way that we think about in the brain. And I think that sort of the dogma story points towards
*  the answer. Yes. So far, you will have to bet I would bet yes. How exactly implemented? I don't
*  know. Is it the only thing that happening? No, it's not. You know, but certainly, yeah, I think this
*  is, you know, these extreme views, even the people who say that, I don't think they really
*  believe them fully just no way of starting a conversation and sort of
*  pointing out the direction, which could be useful. And so regarding your last point,
*  I actually think a little bit of the opposite, which is I think that AI and neuroscience are
*  actually coming closer together. And the reason that sort of inspired me got me excited about
*  this panel is the fact that in deep RL, you have something of a very poor version, perhaps of a
*  circuitry as compared to all the previous reinforcement learning models. And that's something that
*  I said, I looked at that when I first looked at this idea of deep RL and said, well, okay, so
*  we are getting closer in the sense that we might have something to anchor to because one of the
*  problems that we have is exactly what Elise said, which is you have a model and you try to replicate
*  animals behavior. And if you're very good at tweaking your model, you'll be able to do it,
*  right? Because that's what models do. They're very general, typically, and the more general it is,
*  the better your chances are to tweaking it and then sort of recapitulating a behavior.
*  And then you can say, well, you know, maybe the animal uses that model. And there is, it's not,
*  there's no great way, like Elise said, of actually validating that. And for me, the validation that
*  would satisfy me would have to do with a prediction about the circuitry that would be a little,
*  maybe even independent of the animal behavior, which we could then go ahead and sort of probe
*  the brain with an experiment and try to see whether that, you know, comes, whether that's
*  being validated or not, where we get something close to what we thought. And so for me, you know,
*  when I thought about deep RL and dopamine, I said, all right, now we have a way maybe towards,
*  you know, looking at the circuitry that's been, that would be predicted by the mole
*  and getting experimental predictions from that and then going to the brain and trying to do an
*  experiment where we could test those predictions. And so my sense is that ultimately, whether the
*  brain does something like deep RL, for me, I would like to see a validation that involves a prediction
*  about the circuitry that's being proposed by the mole, that then is being validated by an experiment.
*  No, I think that's a good idea. So, I mean, basically what I guess you're suggesting is that
*  like Mars level two should inform us something about like level three, perhaps, which is interesting.
*  I mean, yeah.
*  Right. Level three being...
*  Yeah, I never, because if we just stay on the behavioral level, again, you can always have a
*  mole that does whatever behavior you might find. And if the behavior is the opposite, you can find
*  a mole that does the opposite too. I mean, that's not... When you have something general, I mean,
*  when I started, I was doing motor stuff, motor system, motor cortex, and people had this idea
*  about how motor cortex codes for movement, which is sort of like vector way, all the cells sort of
*  vote which direction the arm moves and so on. And then came the idea about sort of optimal control
*  and how what the motor cortex might be doing is to minimize a cost function that would enable you
*  to move like an optimal control system, the way an engineer would think about it. And one of the
*  main successes of this idea was to recapitulate all sorts of behaviors that people or animals did,
*  the way they move, the kinematics of the movement and so on, the way they would overshoot their
*  target or undershoot in different type of tasks. And for each of these papers, and I'm being very
*  flippant and unfair on purpose, they would change the cost function in a way that would allow them
*  to recapitulate that behavior. And again, I'm being unfair, so don't... I mean, I'm not being
*  100% serious, but I want to bring the point that when you have a general enough theory
*  and you can play with it enough, then recapitulating a particular behavior might not be
*  that strong of a proof. And that is why I would like to sort of mess up the Mars levels
*  and go to the circuitry and get predictions from that to help us get a better, a stronger proof
*  about whether this model is actually related to what's happening in the brain.
*  Yeah, fair. I mean, just for me to wrap up maybe and then I'll shut up soon. I think the way I see
*  it, actually, dopamine system is a very good example for the three levels. And actually,
*  the link between dopamine and reinforcement learning that at the first level, what I see is
*  that there's a problem to be solved, which is how to maximize the expected sum of future rewards.
*  This is the problem that reinforcement learning tries to solve. And whether or not brains or
*  like natural agents are doing that or not, I'm not quite sure. Economists would tell you that,
*  yes, this is exactly what human brains are designed to do, just maximize future rewards.
*  I'm not quite sure about that, but reinforcement learning proposes this series of algorithms.
*  And I mean, we have the old ones that I've read, they're like Q-learning, actor critics,
*  Sarsa, etc., etc. And we try to link them to some brain function to find the mechanism
*  that would implement these functions. So this is the part that I'm not sure whether or not we can
*  get a good link between these algorithms and the way the mechanisms they're implemented in the brain.
*  But what I see, maybe just to say a sentence or two about how I perceive this conference,
*  beyond the panel, there were a few good things and hopes, lights at the end of this tunnel,
*  that we are getting better tools. I mean, we saw a few talks that are like,
*  introducing new tools, including like Ehud Isikoff's amazing new tools that would help us
*  figure out a few things about better and better about mechanism. Like in the past two or three
*  years, the dopamine research field has shifted tremendously because of the advent, I think,
*  of these fluorescent dopamine sensors from Lin Tian's lab and others. And then I saw a few
*  glimpses of a good observation leading to theory. One that I particularly am very fond of was Melissa
*  Warden's observation that how dopamine ramps can be linked to cognitive maps or to exploration of
*  this idea of cognitive maps. I think this is what we need more and more in neuroscience to find the
*  mechanism to make an observation and then try to come up with a theory, at least that links this to
*  some behavioral function. And I saw an example of this in Melissa's talk that was that made me
*  hopeful that we're making some progress. Yeah, I love that. And that's exactly sort of the mixing
*  of the levels that I'm very fond of because that's really, you know, when I that gives me much more
*  confidence that it's rooted in reality, when I see that it's sort of it bears out in at least two
*  different levels. And I think that's what that's what we need to do. And I agree, if people are
*  doing that, and of course, we're limited by the tools we have. But even with the tools we have,
*  there's lots more things that we can do. So I was what I was hoping for is to give some
*  context to the panel here. And what I expected happened where I got a lot more. Did you guys get
*  everything in that you wanted to talk about? I think so. Yeah, I mean, I have a few other points
*  that are like random points that I wanted to talk about. But I think we can I mean,
*  one of them maybe I want just to say here, because it links to your show, which I'm a big fan of,
*  by the way. And I like to keep it like an audio form, not make it a talk show, because I used to
*  listen to it during my commutes. Yeah, it's like very informative. Oh, good. Thanks. I mean,
*  you had Matt Smith on your show, and I forgot, I think it was episode 85, 86, 90 something.
*  I forgot. I'm very sorry. I apologize. It's all in here, buddy. Yeah.
*  And he was talking about this fascinating idea of slow drift, which I think it's an amazing
*  observation. And I like to link that to dopamine and neuromodulatory systems. I think it's a
*  fascinating avenue for future research. And this may link to like more computational or like neural
*  network architectures as well that what we currently are inspired by in our neural nets
*  are like fast neurotransmission, meaning like excitatory inhibitory connection, right? That's
*  like this unit a neuron a fires and then it would excite or inhibit neuron B. And this is like a
*  rapid summation in one step. But what neuromodulators do is that they don't necessarily have an
*  excitatory inhibitory effect. They change the state of a neuron or a network in a way that they
*  would respond differently to future stimuli. Is this like Roshan Kuhl's work on switching states?
*  Maybe it goes even back to like some of the ideas that I've seen abandoned now by like
*  Dershowitz and Jeremy Siemens that's like how like dopamine changes the state of the network.
*  Like different dopamine receptors when activated would move you through this like state space to
*  different like basins of the attractor, which I think these were like amazing theoretical ideas
*  that have not been explored. And what Matt talked about in your previous one of the previous
*  episodes reminded me of that, that dopamine has this role in like attention, for example,
*  and these slow drifts might have been related to that. And we currently have no way of incorporating
*  these in our computational models in our artificial neural networks. And this might be an avenue to
*  do something which is like, yeah, I see myself at least in the future doing that. I proposed
*  this to the Simon Foundation, but I think it's a fascinating idea and we'll see more of this in the
*  future how like these like different neuromodulatory signals like dopamine is one,
*  acetylcholine, serotonin, norepinephrine, how these non-neurotransmitters, these neuromodulatory
*  signals change the state of the network. If there's a connection back to the AI,
*  maybe this is something that we can contribute to their understanding. Maybe this can be one
*  of the wings of that plane. I was originally going to ask you and now I'm going to bring it back in
*  about your thoughts broadly about A, where are we in understanding dopamine and its roles like
*  broadly, right? But then B, I wanted to get back to this idea of, you know, the idea of
*  neuromodulatory modulations being slow. And traditionally, you think when you think about
*  computation, you think about binary, you think about spikes or not spikes, ones or zeros,
*  and that's how you compute things. But do you think we're trending toward a multi-temporal scaling
*  story of computation where neuromodulatory effects might be a slow part of that computation,
*  whereas the spiking is just another faster part of the computation. And where we're going to get
*  this eventual hierarchy of kind of scaled temporal computation. That's a lot to think about, I know,
*  and those were two different questions. But if you have thoughts on either of those,
*  I'd love to hear them. So in response to your second question, maybe first question.
*  Yeah, let's talk about the first question. I think we touched on that a bit. I think we are
*  learning more and more. I mean, as we are graduating from this dopamine RPE theory, which is, again,
*  an elegant account of dopamine function. I like the graduating term there. Yeah, sure.
*  I think we are going back to test out some of the older ideas and we are on,
*  and as we get like better and better tools for probing dopamine function, we are starting to
*  explore the role of dopamine in different functions and different aspects of behavior as
*  some people have shown in like a series of talks during this virtual dopamine conference.
*  But in response to your second question, I think that's very true, right? That we need this
*  to somehow introduce this idea of processing at different time scales. And my pitch to the Simon
*  Foundation for this idea was that, I mean, if you look at behavior, behaviors evolve over time.
*  Over a very different time scale, right? Whereas like new transmission is super fast. It happens in
*  like milliseconds, but behavior, the time scale of behavioral changes are much slower and much
*  different. You have different behaviors that happen and pan out at different time scales.
*  And what could link these two fast processes and slow behavior could be the neuromodulatory systems.
*  And as like Ben was suggesting earlier, for example, like dopamine as like usual suspect of
*  all neuromodulation, I mean, you have this idea of that, yes, dopamine cells fire and then they dump
*  a bunch of dopamine in different parts of the brain. What happens is that then these different
*  parts will absorb this dopamine and they have different rates of absorption because there are
*  different mechanisms involved in the absorption. For example, in the striatum subcortical regions,
*  you have transporters that will just suck out dopamine and put it back inside the cells.
*  And then density of these dopamine transporters are different even in different sub regions of
*  the striatum. But then in the cortex, you don't have dopamine transporters. It has to be,
*  dopamine has to be metabolized and that's a much slower process. So dopamine is hanging around for
*  much longer in different, up to like 30 seconds perhaps, right? If you get a simple puff of dopamine,
*  it will like hang out there for much longer compared to like striatum where it gets sucked up
*  within a second. You mean like a tonic signal, right? No, just...
*  Let's not get into that. But so I mean, and the reason I think this is an appealing idea is that
*  if you look at these like different modules of the brain, different parts of the cortex
*  or different parts of the brain that have evolved and have these like local microcircuits
*  re-involved. But then for the new modulatory systems, there's always one region, one nucleus,
*  or at least mostly one nucleus in the brain that projects to like all over the brain and would
*  broadcast the signal. So that's another appeal of this dopamine as a broadcast signal, that you have
*  dopamine cells sitting in the midbrain and then they just dump dopamine all over the brain.
*  So that to me is something that could change the state of the brain, this how you process. You get
*  more dopamine, you process things differently. Now the same input would mean like a different
*  thing. We have this recent paper came out in Science from Adam Kepich's lab where he was
*  looking at hallucinations or hallucinatory perceptions, halips, I think they call it.
*  The idea was that sometimes the mouse hears things that are not out there, things that they
*  heard something and then they move. And what they show is that how this is related to the dopamine
*  levels in one particular part of the striatum, in the tail of the striatum in the back.
*  So I think the same cues then would mean different things or the absence of the cues.
*  I mean these neuromodular theory signals change the states of the network and how these network
*  process information or even the same information would mean different things. So that's my thought.
*  Yeah, I mean I think that the issue of time scales is actually even worse than that because even if
*  you just talk about regular neurotransmitters and not neuromodulators, you still have different
*  synapses can have very different time scales. And in fact, if you look at computational models,
*  some of the models depending on the time scale of the synapse, you can have a very different type
*  of behavior. There's some rate models where if you have synapses that are slower than 20 milliseconds,
*  let's say, then they behave in a completely different way than it would behave synapses
*  are faster in like 10 milliseconds. So even within that time scale, the network itself can
*  be very different and you can explore that computationally depending on the time scale
*  of the synapses by a few milliseconds of change. And then of course you have the neuromodulators,
*  which right now are being modeled either as very fast or very, very slow because let's remember
*  synaptic plasticity, right? That's sort of the big effect of the neuromodulators like dopamine in these
*  computational models. And that's a very, very slow time scale. And so, but of course within that
*  range of a few milliseconds versus minutes, let's say, you still have what Ali talked about,
*  which is how you can have fluctuations in the way the neurons change its state and the network
*  changes its state. And that has been mostly explored by cellular physiologists, a bit perhaps less by
*  computational or even maybe systems on your scientists. They're starting doing a little bit
*  now, I think. And so that's a new layer of complexity, which is something I like. I like
*  complexity. Maybe that's why I'm studying the brain. And just to piggyback on this idea of
*  complexity, Ali, your idea of the appeal, I understand the appeal of the broadcast signal,
*  where you have the same signal that goes everywhere in the brain and then different brain areas will
*  process it differently depending on the kinetics of the re-uptake of dopamine and depending on
*  their own characteristics of the network. But even that story, I would argue about a complexity
*  because we know that different dopamine projections can transmit different signals to different areas.
*  And so even then you have this added complexity within even within the same nucleus where you
*  have this concentration of dopamine release in neurons or other nuclei when you have sort of,
*  let's say, other new related that's being released, you can still have different streams
*  of information that's being transmitted to different places as well. So I think that the
*  more we're going to delve in, the more we're going to find that we have this further and further
*  subdivision and further and further complexity because of this. Again, this is something that Ali
*  said and there was also a loop in the panel that brains evolved. And they evolved in a way that's
*  so disorganized and chaotic and just gets things to work. And that I think naturally results in a
*  huge amount of complexity. Is one way to think about this. So recently there's been a lot of
*  success in using dynamical systems theory to basically reduce the dimension of our brain,
*  of the activity in our brain. So our brain has tons of neurons and they're all firing, but
*  you can reduce the dimension so that the neural firing is fairly bound to a lower dimensional
*  manifold, lower dimensional shape essentially. And it's trajectories along those manifolds that
*  underlie some of the computation. But what you just said is that we may need to then increase
*  the dimension if we're considering how different areas are responding in different ways to the same
*  signal and how that increases the complexity, the amount of interactions going on. And I don't know
*  if it's worthwhile thinking about it in terms of how that story might map on to the let's make
*  everything low dimensional story. I mean, it's very appealing to make everything low dimensional
*  because then we can put it on a graph and we can look at it. If it's two or three dimensions,
*  that's visual and we're visual creatures. So I think that's part of the appeal. But again,
*  this idea about dimensionality reduction, we need to remember that dimensionality reduction,
*  all the idea about dimensions basically are reflections of the correlation between neurons.
*  How much the activity between neurons is correlated or not. That's all it is. And so if you have a
*  lot of neurons that are highly correlated, even if the pair was correlations are not big, but the
*  correlations overall are strong, then you will be able to do this in short reduction. If you have a
*  very low correlation, the news are independent. Everyone is doing their own thing. Then you can't
*  reduce the dimensionality. And so I think it's clear that, you know, neurons are connected. So
*  they're going to have some correlation and the more news you record, the more saturation you're
*  going to have on the amount of information, which allows you to reduce the dimensionality more and
*  more, relatively speaking. But of course, that's typically done within a single brain area,
*  maybe even within a single condition. And I think that the more you go into multiple
*  brain areas and receiving multiple inputs, including multiple neuromodularity inputs,
*  then it's going to be harder and harder to just think about a 2D space that you can actually plot
*  your graph in different colors and call it today. I mean, there is the visualization aspect, but
*  there also is the aspect of figuring out where the saddle points are, figuring out where the
*  attractors are, where you can predict what state the system will be in given its initial state
*  and the condition. You will know fairly accurately if you know the surface of the
*  manifold, the shape, the topology, then you know where the activity will end up. So there is
*  a computational advantage as well. I think that's independent of the dimensionality. I mean,
*  you could have attractors, you know, you could have attractors be completely independent neurons as
*  well. So I think that it's easier to look at the attractors in a lower dimensional space.
*  Yeah, for sure. Ali, anything to add? We've gone off course, but that's fine.
*  Yeah. I mean, no, no, I think, yeah, I have my own interests and skepticism about these dimensionality
*  reduction things. I agree with Ben that they're amazing visualization tools. And I think it's a
*  good descriptive language for what computation the circuit or specific circuits might be doing. But
*  I'm not sure what we would learn beyond that about the circuit dynamics or circuits,
*  underpinning circuits of a certain behavior. But I think absolutely it's a good descriptive way of
*  computation. I guess I was bringing it up just because it seems like a hopeful story of being
*  able to visualize and use these lower dimensional structures to simplify things. And that's against
*  what Ben loves. And he is saying, oh, good, there's more complexity with the neuromodulatory story.
*  He's rubbing his hands together. That's what you can't do on an audio only podcast to see that
*  someone's rubbing their hands together. So let's add to the complexity here. So Ben alluded to this
*  idea of like, this is one of the hot topics now in the field that during a virtual conference
*  meeting, we also see some traces of it, that there's a disconnect between firing of dopamine
*  cells and the amount of dopamine release. Ben's laughing, but the idea is that-
*  I love it.
*  Yeah. It's been a few years now that we know that dopamine cells are not exactly your typical
*  textbook cells, that the amount of neurotransmitter here, dopamine, that they release is not a passive
*  readout of the cell activity or the cell body activity. I mean, in your typical neuroscience
*  textbook, you read that cells fire action potentials and then proportional to that,
*  they would dump neurotransmitter in their targets. But when was the first study? I forgot. But even
*  if you go back to some of the Schultz's old stuff from like 80s, people were suspecting that
*  if you get a brain slice where you cut out all dopamine cells, the cell bodies, and then you
*  have just the processes in this triatum, for example, just cut it, dump them in the trash,
*  and you stimulate that- you do an electrical stimulation in the same slice and you measure
*  dopamine, you would see dopamine release. So there are mechanisms. And then later out in 2012,
*  using optogenetics, Steph Craig's lab and it was Joe Chear, right? I mean, Roger Cachot.
*  At the same time, what they discovered is that if optogenetically, you stimulate a certain type of
*  interneurons in the striatum, these are interneurons that release acetylcholine, then you would get
*  dopamine released in the striatum, independent of firing of dopamine cells. Dopamine cells are,
*  like cell bodies are dead, or you cut them out, throw them in the trash, and you stimulate these
*  certain interneurons and you would get dopamine released. So this adds, I think, even more
*  complexity that like, what is the computational unit of the brain? I mean, is it firing of cells?
*  Or maybe in this special case, it's not that, it's the amount of dopamine that's getting released.
*  Or even maybe further, I mean, maybe we should reconsider what the computational unit of the
*  brain is and think about like receptor activation. Because in the end, if dopamine cells fire,
*  and there's no receptor to listen to them, have they made any sound?
*  What about water? Because the brain is mostly water, should we consider that the computational?
*  It's salty water, right? If it was water, we wouldn't be alive, right? It's salty water,
*  and it's actually cells that are trying to get a shelter from that salty water.
*  And the gradient there, I think, is the heart of computation there. But yeah, I think it's the
*  receptors. Yeah. So yeah, I mean, this adds to the complexity that dopamine cells don't add.
*  It's not enough just to record from dopamine cells and infer their function. And during this
*  VEDA conference, we saw amazing results from Zeig Kaleig's lab. Paul Kramer showed some amazing
*  stuff. And Cheng Lu from Pascal Kaiser's lab showed another set of amazing results showing how the
*  interaction between cholinergics and dopamine acts on terminals in the striatum,
*  would cause like dopamine release. And we don't know yet, but we are trying to like multiple
*  groups now are trying to understand what are the functional meanings of this now added computation.
*  And I have my own speculations. I mean, it has something to do with like saving. I mean, now I'm
*  just babbling saving like metabolic energy, because I mean, one reason one thought that I had was that
*  like dopamine, unlike other cells, I mean, the branching of dopamine is like maybe two or three
*  folds greater than your typical cells. So changing even the membrane potential would be like very
*  metabolically costly. There have been the computational studies out there that shows that
*  the like energy in terms of ATP required to bring dopamine, like acts on terminal potentials back to
*  arresting potential is like much greater than your typical cells. And it like exponentially increases
*  with the number of branching. And one reason is that maybe brain I mean, I love this idea of
*  evolution of like evolution of systems sitting on top of systems, maybe at some point, they were
*  like easier or more simplistic mechanisms or agents lurking around the earth, and they just
*  needed dopamine to do this for prediction everything, or like two or three more things.
*  But then as things became more and more complicated, brain learned to design this idea of let's do a
*  local release of dopamine in this special circuits, because this circuit maybe cares only about
*  motivation. So you don't need to broadcast dopamine all the way from midbrain to the entire
*  brain and then use all this energy to bring back all these terminals down to the resting membrane.
*  You design or you evolve this local mechanism for dopamine release. I think this is a topic that
*  maybe like 10 people care about in the entire universe. So we should stop.
*  Lots of people care about it. I actually think that both things are probably happening because
*  even when we record from dopamine cells, we see that not all dopamine cells do the same thing.
*  And so you can have that sort of complexity. And then you can add to that the local circuit
*  independent modulation that Ali talked about to have another layer of complexity that even
*  those different signals can be even then further sort of distributed, further modulated
*  in separate ways. And that gives you a lot of control, quote unquote, that's kind of a loaded
*  word about being able to do lots of different things with this type of your model. So I think
*  that's a good thing. Again, I like it. Yeah. And going back to maybe your first question,
*  this is that I think, I mean, there are aspects of like their functions of the dopamine that are like
*  essential to life, like learning from rewards and aversions, right? So the entire brain perhaps
*  needs to be informed about this function that something good happens, right? That's what Matt
*  said. It's the whole brain is a deep RL system. There you go. The whole brain has to be informed.
*  But the whole brain is involved perhaps in deep RL, but it's not. But yeah, I mean, and there's
*  work from like functional MRI stuff from like Karl Dyseroth and others labs looking at reward
*  signals or what prediction signals across the brain. And you see that like brain is involved,
*  right? So it makes sense to have a broadcast signal that would just send out these like alarms
*  or like something good happens, something bad happens, right? If you're the visual cortex,
*  perhaps you still need this. If you're motor cortex, you need this. But then there are like
*  very specialized functions of dopamine that perhaps not every single circuit in the brain
*  needs to care about, right? How to hold a thought in your memory. Perhaps prefrontal cortex wants
*  to know that your visual cortex is, I don't care about that. Let me do my job, right? So
*  these maybe mechanisms evolve. And I agree with Ben that yes, I mean, it's not that like there
*  might be heterogeneity and there is like, at least we know through his work and others,
*  there's heterogeneity in responses. But on top of that, I want to propose that there might be
*  a multitude of local regulation mechanisms for dopamine release that serve these specific
*  functions that we are yet to discover. Yeah. And that's, you know, I think that's
*  really well supported because even though there is heterogeneity in the activity of different cells,
*  when it comes to the big sort of salient behavioral continuencies like reward or aversion,
*  at least reward, you can see that most dopamine cells really respond to it regardless of what
*  they do in different kind of epochs. So certainly, that's something that dopamine seems to be
*  specialized in even if they do other things as well that are more so segregated or heterogeneous.
*  All right, guys. Well, this is what it was going to be at the beginning was a sort of
*  cursory introductory reflective precursor to the dopamine panel. And when it turned into,
*  which is what I thought it would do, what it turned into is a full blown discussion that
*  I think has turned into a real nice compliment because it was focused a lot on the actual
*  dopamine, on neural systems and ideas surrounding those things. So then the next little episode with
*  the panel will focus more on that computational AI and behavior side. So thanks again. And
*  thanks for having me again. And this has been great.
*  Thank you for having us.
*  Yeah.
*  to the full versions of all the episodes, plus bonus episodes that focus more on the
*  cultural side but still have science. Go to brandinspired.co and find the red Patreon button
*  there. To get in touch with me, email paul at brandinspired.co. The music you hear is
*  by the New Year. Find them at the newyear.net. Thank you for your support. See you next time.

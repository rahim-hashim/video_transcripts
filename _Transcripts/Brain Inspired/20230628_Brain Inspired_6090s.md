---
Date Generated: April 19, 2024
Transcription Model: whisper medium 20231117
Length: 6090s
Video Keywords: []
Video Views: 831
Video Rating: None
---

# BI 169 Andrea Martin: Neural Dynamics and Language
**Brain Inspired:** [June 28, 2023](https://www.youtube.com/watch?v=g1xf7n4fh70)
*  I really am trying to explain the thing that I want to understand.
*  Like that's what I'm, even as the rise of large language models come and I feel often
*  that I'm, that I don't always find a camp of people who see things the same way and
*  that can be good and sometimes challenging and can sometimes be very sort of lonely.
*  Why can't dynamical systems represent and compute?
*  We have, it's a choice for us to believe that they cannot.
*  It's a choice for us to not to try to bend or break or reformulate how we talk about
*  these systems.
*  What is the dimensionality of language?
*  Oh, it depends on who you ask.
*  Sorry, is dimensionality one of those words for you?
*  No, dimensionality is a safe word.
*  It's a good word.
*  Hello Intrepid Mind Explorers.
*  This is Brain Inspired.
*  I'm Paul.
*  Today, my guest is Andrea Martin, who is the research group leader in the Department of
*  Language and Computation in Neural Systems at the Max Planck Institute and the Donders
*  Institute.
*  Andrea is deeply interested in understanding how our biological brains process and represent
*  language.
*  To this end, she is developing a theoretical model of language.
*  The aim of the model is to account for the properties of language, like its structure,
*  its compositionality, its infinite expressibility, all while adhering to physiological data that
*  we can measure from human brains.
*  So her theoretical model of language, among other things, brings in the idea of low dimensional
*  manifolds and neural dynamics along those manifolds.
*  So we've discussed manifolds a lot on the podcast, but in short, there are kind of abstract
*  in the space of possible neural population activities, the neural dynamics, and that
*  manifold structure defines the range of possible trajectories or pathways the neural dynamics
*  can take over time.
*  One of Andrea's ideas is that manifolds might be a way for the brain to combine two properties
*  of how we learn and use language and process language.
*  One of those properties is the statistical regularities found in language.
*  So a given word, for example, occurs more often near some words and less often near
*  some other words.
*  This statistical approach is the foundation of how large language models are trained.
*  The other property of language is the more formal structure of language, how it's arranged
*  and organized in such a way that gives it meaning to us.
*  Perhaps these two properties of language can come together as a single trajectory along
*  a neural manifold.
*  And our brain's predictions about what's coming next essentially guide and push neural
*  activity along that manifold trajectory.
*  So that's a mouthful, I know, but we hashed it out more during the episode.
*  And she has a lot more ideas.
*  And of course, we discuss many of them.
*  And of course, we discuss large language models more and how Andrea thinks of them with respect
*  to biological cognition.
*  We talk about modeling in general and what models do and don't tell us and much more.
*  So as always, I hope that our discussion just wets your appetite to learn more about Andrea's
*  work and you can find links in the show notes at braininspired.co.uk slash podcast slash
*  169, where you can also learn how to support this podcast if your hearts are as generous
*  as your minds are intrepid.
*  Okay, thank you for listening.
*  Here's Andrea.
*  Andrea, you've been studying language for a long time.
*  And first of all, why didn't you study vision instead of language?
*  No, I'm just kidding.
*  I'm kidding.
*  I actually have an answer to that.
*  Okay.
*  All right.
*  I actually started working.
*  First, I went to college for one year at Columbia University and then I dropped out.
*  But I worked in a P53 oncogene lab.
*  And I, you know, as like an intern, one of my tasks was to be involved in like sacrificing
*  the animals.
*  And at one point in time, I was a vegan, I'm not anymore.
*  And I found it really rough.
*  And I was like, I'm really interested in neuroscience.
*  What can I study where I won't ever have to use animal models because I don't have
*  the stomach for it, even though I think the data are important.
*  And that's how I ended up with language.
*  I mean, there are many other steps in between.
*  I ended up doing some other stuff and I ended up studying cognitive science at Hamster College
*  where I could really focus exclusively on psycholinguistics and cognitive science.
*  So it really was a matter of...
*  So it's not language per se that you were interested in.
*  I'm sure that you've become very interested in it.
*  It was avoidance.
*  No, it was...
*  It helped me sort of like crystallize what was it about actually the human mind that
*  I was so interested in.
*  It's actually something that I couldn't study in an animal model.
*  A different way to put it.
*  And this is an unfair question because I know that there are many aspects of language that
*  you're interested in.
*  Is there a particular aspect of language that excites you that you're really focused in
*  on?
*  I think it's for me...
*  I mean, I think to foreshadow a bit, it's the idea that language represents sort of
*  the boundary computation for the brain.
*  So I can talk more about this later, but the fact that you need statistical and quote unquote
*  algebraic or variable-like information to account for our language behavior and the
*  language of the world, I think really sort of presses us to say, okay, what's sort of
*  the limits on what we can express in a neural system?
*  And language gives us a really great readout for that.
*  And so following that line, then I guess the most sort of interesting property of language
*  that gets to that is really the notion of compositionality, that you are putting things
*  together that are more than the sum of their parts, but that are a function of them and
*  the rules used to combine them.
*  And that's really...
*  That just seems to be endlessly giving important insights about the human mind and about the
*  brain.
*  So you use the term boundary computation, I believe, there.
*  And then you also use the term limits.
*  I mean, do you think that language represents a bound on our cognitive capacities?
*  I think more what I mean there is at least for what we know about language now, at least
*  just talking about the world's languages and what linguistics tells us, we already have
*  a really hard problem that I think neuroscience and cognitive science are running their best
*  race to try to explain already.
*  But already I think there's a lot of stuff that isn't sufficient or that's sort of falling
*  short.
*  And that's what I mean there.
*  So the other way to look at it more formally is to say, look, if you really want to push
*  a system to be both statistical and algebraic, that that's going to be the boundary condition
*  on the things that you can compute for the brain.
*  What does it mean to say that language is algebraic?
*  That's a good question.
*  So I thought about this a lot since you brought it up.
*  And I think the way that I typically try to get to the problem or define it for people
*  is to say that, to start thinking about it in terms of the fact that human language is
*  shaped by its statistics, but it's not defined by them.
*  So language can break free from the statistics of itself, so frequency or probability of
*  a sound, of a morpheme, of a word or a phrase.
*  And if we couldn't do that, notably our behavior would be really, really different.
*  So it's easy to think of extreme or funny examples like we could only say fixed responses
*  or we'd constantly be stuck in local or minima or maxima about what we're talking about or
*  what we're saying.
*  And we don't do that.
*  And there are many classical and better examples from the cognitive revolution.
*  We can say things that we haven't heard before.
*  We don't have lookup tables of utterances that we're bound to.
*  But I think we kind of actually overlook the simple fact all the time and that not being
*  driven by statistics, well then what is the thing that can explain our behavior and the
*  way the systematicity of language is how they work?
*  And that seems to be minimally some kind of system that has variables at its heart.
*  And it's from that notion that you're not stuck to a fixed value that is a sound or
*  a word that you heard in a particular context.
*  You only return that.
*  You somehow come upon a system of rules where you can have variables and functions that
*  then can be adapted to the conditions at hand, what you need so you can express the thing
*  that's needed in that situation.
*  Where do those rules come from?
*  That is a deep and contentious question.
*  Let me back up because what I wanted to ask just off of what you were talking about was
*  which came first?
*  Statistics or rules or variables?
*  Maybe I will just ask that.
*  Yeah, that's a good place to start.
*  So that's already in itself has got the hard question in it.
*  So which came first?
*  In order to sort of a simple way to talk about the six is to say there it's counting something.
*  But in order to be able to count something, you have to know what that thing is to recognize
*  it and say, okay, obviously the way that we use statistics now in natural language processing
*  and in cognitive science is much more sophisticated.
*  It's not just simply counting one occurrence.
*  But still there has to be some in practice labeling that's going on in the engineering
*  sense or there has to be something built into the system that tells you, okay, this is the
*  thing that's relevant to count to calculate a statistic over.
*  So in that sense, I think you have to at least have some kind of pattern recognition that
*  allows you to extract some invariance across all the different situations that we encounter
*  language.
*  I mean, language learning and acquisition is not my specialty.
*  It's a really hard problem too.
*  But I think that it's clear that there's an interaction between an inductive bias that
*  we have for hierarchical relationships and patterns for looking for more than sequences,
*  for doing more than predicting the next word.
*  And that can then bootstrap over the information that we get from our environment.
*  And we do lots of, I think, interesting internal comparison between representation and context
*  to then over time define these rules.
*  So in some sense, the rules actually are reflected in the statistics.
*  But the statistics don't, from them, just having the statistics alone won't give you
*  the rules.
*  So there's sort of asymmetry between the sources of information.
*  Okay.
*  These are all like big problems.
*  I want to just zoom out and back up maybe and ask how...
*  So language has always intimidated me.
*  I mean, I remember I took a linguistics course and it was kind of fun.
*  But just the idea...
*  So I come from a non-human primate neurophysiology background and studying eye movements and
*  decision making, vision, the vision sciences as everyone else, it's 90% or something.
*  Do you know what the percentage is?
*  I don't even know.
*  No, I don't.
*  Do you know when I was a PhD student at NYU, it seemed like everybody else except for me
*  and my three friends worked on vision.
*  So my anecdote is there's a big population of vision scientists.
*  Well one of the reasons is because the musculature of the eye and making eye movements, all that
*  is really worked out, the circuit diagram and how all that works.
*  So that makes it a somewhat more tractable...
*  That's appealing.
*  Yeah.
*  It is appealing, right.
*  And going back to my own fears about studying language, and I've been focusing a little
*  bit more on language recently as we were talking just a moment ago off air due to these large
*  language models and the rise in the popularity of these.
*  And I've had multiple people on the podcast talking about language, but I think if I...
*  I'm not sure.
*  I feel like language...
*  Here's the question is, I'm curious how your own view on language as an object of study
*  and just as a cognitive process has sort of evolved over time.
*  Has it become easier, seeming like an easier problem to tackle or has it become more wily?
*  No, I think it was always wily.
*  So I do share with you that fear of language or of the enormity of the problem and the
*  endless complexity.
*  For me, it's also the importance is language is so multifaceted.
*  So I really focus on what it means to have a structured representation that's linguistic
*  in something like a neural system and neural dynamics.
*  And for me, that's really core and key part of language, but there's so many other parts
*  of language that are equally important and linguistic and that are also hallmarks of the
*  incredible human capacity of language itself.
*  So that for me is like the source of the fear because it can become so complex and there's
*  so many things that obviously matter to the brain.
*  When we're talking to each other, we can name a long list of factors that are going to be
*  really important, including our eye movements and joint attention and all these things that
*  lead to mutual understanding and our ability to refer to things.
*  But I guess I've already sort of been comfortable with that, that complexity or that chaos of
*  what needs to be explained for a long time.
*  And I think over the years, I've gotten sort of more comfortable or more situated in, oh,
*  yeah, no, it really is.
*  I really am trying to explain the thing that I want to understand.
*  Like that's what I'm, that even as the rise of large language models come and I feel often
*  that I don't always find a camp of people who see things the same way and that can be
*  good and sometimes challenging and can sometimes be very sort of lonely.
*  But more and more, I sort of think, and I think, no, this is really what I think is
*  important, right?
*  I don't think that we get very far by trying to deny what linguistics tells us or escape
*  what psychology tells us about the importance of timing, for example, in cognitive processing.
*  And so no matter sort of what comes in terms of developments in these incredible language
*  model systems, I still don't think that necessarily negates all the other insights of 50 years,
*  if not centuries, of insight in linguistics and psychology.
*  If anything, it sort of emphasizes or reiterates how important it is that we have a theory
*  that can account for both types of information.
*  So for structured information and statistics about it, right?
*  And so far, that's really what I keep seeing is just being absent or not being there.
*  So we kind of, as a field, polarize and go back and forth.
*  So we say, okay, no, well, for a while we focused a lot on symbolic structures and representations.
*  Well, still, I think not as much as we could have or not in the way that would have been
*  most effective.
*  And then, you know, there have been different periods in the history of cognitive science
*  and in language where you have a lot of focus on the importance of statistics and statistical
*  learning.
*  And I don't think one excludes the other by any means.
*  And I'm just sort of hoping that more and more people come around to that point of view,
*  because that's really the hard problem is explaining both or understanding why both
*  are important to the brain for processing language.
*  Okay, right.
*  So your interest is really in how the brain does it, how the mind does it, right?
*  Yeah, I don't know if I would make a distinction between the brain and mind, because I think
*  that's also scary and difficult, but important.
*  But yes, in both, I would say.
*  If we want to be dualist about it, let's say both.
*  Yeah.
*  Well, I just mean in contrast to, you know, the idea of multiple realizability.
*  Like if you can, like, can you, you know, maybe you can brute force this thing using
*  just a statistical and associative approach.
*  And then structure comes along for the ride.
*  I mean, or do you disagree with that?
*  I would disagree with that, because I mean, I think it's going to be really hard to show
*  that structures there without sort of theoretical or like, you know, choices that you make to
*  the instantiation to the particular model that says, you know, here's what we think
*  the ingredients of structure are in there.
*  I think there's a lot of stuff we could talk about in cognitive science about what those
*  things might be.
*  Waiting for them to emerge, I think, is kind of a weird approach.
*  I mean, maybe it's possible, but is that really the approach that we want to take?
*  And then if you sort of wait for structures to emerge from all the data and all the compute,
*  then the question is, what are the right benchmarks or tests?
*  And I feel like that's a huge can of worms and that we can all, we can work on that and
*  fight about it for decades.
*  And I'm not really sure that that's as efficient as saying, I want to build these things already
*  into the model.
*  Then of course, that begs the question, well, what are those things?
*  And how do we do, how do we agree on what is important?
*  I think a lot of people do want to say, oh yeah, I know the structure is emergent, it'll
*  be there.
*  But I feel like that's, you know, sometimes I wonder how do we evaluate that?
*  Is that really, what is the science behind that?
*  If that's the case, which I don't think it is, if it were the case, we still need to
*  explain how did that happen?
*  And what does that tell us about the human organism?
*  Right.
*  Right.
*  OK.
*  So you said a lot there.
*  Well, you know, I've seen multiple people saying that maybe, and we're not going to
*  model pathway quite yet.
*  But just in terms of structure emerging from a purely statistical approach, well, you know,
*  then there's always the question of meaning in the large language models.
*  And multiple people I've had on the podcast have argued that, and others have argued that,
*  well, maybe you can learn meaning later.
*  So it's the opposite direction from the way that humans develop, right?
*  Where the meaning kind of comes along with the language.
*  Maybe you can train up these large language models and that grounding isn't even necessary
*  for meaning.
*  I mean, maybe I wouldn't exclude that possibility.
*  But that seems to me like an engineering question.
*  I mean, the main thing that I think the models are missing that you need to get at meaning
*  is intentionality, right?
*  That's what these, what no system has.
*  And we don't understand how humans have it.
*  I mean, I think that we have it.
*  I don't want to dispute that at all.
*  But how we have it is already, that's also a theoretical object worthy of study as well,
*  right?
*  So the fact that our representations are about things.
*  That's the point.
*  I mean, the reason I brought that up is just because of the structure slash statistics
*  question as well, you know, whether structure can come along later and does it matter the
*  order that these things are learned?
*  And do we need to pay attention to how the human brain and mind develops?
*  Yeah, I think it depends on your goal.
*  I think we need to because I want to come up, that's what I want to explain.
*  That's what I want to study is how the human mind and brain do something as interesting
*  and powerful formally as language.
*  But I think in terms of like the question, can you get a large language model to pass
*  some benchmarks on meaning by first, you know, by adding stuff and grounding later?
*  Sure, why not?
*  I mean, that's the other thing.
*  I mean, there's like infinite ways to cut a cake.
*  There's infinite ways to arrive probably at the end behavior that we want.
*  But is it following the path that we are now?
*  I think that there's actually there's a bit of duality there.
*  So you can say, I think for a theory of how cognition or language arises in the human
*  mind and brain, how it's learned or how it's implemented or how it's how it came about.
*  Yeah, I think that you could some some people I want to sort of leave room for other other
*  points of view.
*  Some people might think that having something like, okay, this is the limit of what can
*  be learned, whatever it is, we still know that's also a subject of debate from all of
*  the data and from increasingly opaque training practices.
*  You know, there's lots of leakage now.
*  Now a lot of we can't really separate even between maybe with GPT-4 it's a bit different
*  with chat GPT, the role of of reinforcement learning human feedback is likely quite large,
*  right?
*  And we just don't we don't know.
*  Then I think we really have to turn to the open source large language models to study
*  questions like that.
*  But I'm not I don't see why in the limit that's going to tell me necessarily anything about
*  how it works in the mind and brain.
*  I will say though, I'm one of the several sort of analogies I've been using to like
*  think about this for myself, but also to communicate with other people.
*  So, you know, in the history of science, right, the debate between geocentrism and heliocentrism,
*  you could actually obtain better model fits, better prediction of celestial, the position
*  of celestial bodies in their path with geocentric models and models that posit that the earth
*  is at the center of our solar system.
*  And that's because you can do that by adding more and more parameters that essentially
*  overfit the data.
*  And so I don't think it's a coincidence that, you know, we have in order to get the level
*  of behavior that we expect now, we need to have more parameters than training data points,
*  because we're really asking these systems to return things that humans are satisfied
*  with and basically through, I think, parameter interpolation, but not to verbatim reproduce
*  the training data.
*  In order to do that, you're going to need this, you know, extreme parameter space.
*  We're going to come to your ambitious theoretical model eventually, but studying language is
*  necessarily a human endeavor.
*  Well, okay, that could be argued, but the vast majority of studying language is using
*  humans, right?
*  And another, I guess, advantage of not using humans or studying something that's not necessarily
*  just a human cognitive function is being able to be more invasive in your experiments.
*  So does the ability to acquire a limited range of data like EEG and fMRI, do you find that
*  as a fundamental limiting aspect of your research or?
*  Well, I'll just leave it at that.
*  Yeah, I mean, I do.
*  I mean, although I see like, I mean, there's, I feel like, you know, there's such ethical
*  reasons are solid.
*  So, I mean, it is what it is, right?
*  Yes, I do feel it's a limitation.
*  I'm not sure.
*  I can't really imagine a world where we fully got around that, but I think it does certainly
*  limit the rate at which we can map, you know, concepts and linguistics and cognitive science
*  to concepts in neuroscience, because like in my model, for example, I'm really, I'm
*  trying to think about things in a population coding level.
*  I just can't get data that are going to give me that resolution.
*  Right.
*  Yeah.
*  I mean, a large part of what you deal with is oscillations.
*  And you can measure oscillatory measures using EEG and MEG.
*  But then you're even, you're interested in the underlying neural population level, you
*  know, with gain modulation, inhibition.
*  And so you, maybe we can just talk about your model now.
*  Yeah.
*  So I mean, I guess one way to say that is so I mean, I still wait, readouts that we
*  use are from MEG.
*  And more and more I talk about them as neural dynamics, because I want to sidestep the debate
*  about pure oscillators and evoked responses, because I think, you know, spoiler, it's both.
*  I don't want to get sort of sidetracked in trying to establish what, you know, again,
*  a false dichotomy.
*  So many things in our field are really a false dichotomy.
*  It's really both like structural and statistics.
*  I think that, you know, the evoked responses are really important.
*  And sometimes I think they are endogenously generated.
*  So there are state changes within that are driven internally, right?
*  But that's what recognizing a word is from speech or putting two words together.
*  You're driving that change, that state change internally.
*  But for me, the important thing about neural dynamics or population arithmetic activity
*  or oscillations is to remember what ultimately their source is in the limit, right?
*  It's driven by neural ensembles.
*  We might not understand the relationship to single unit activity, but single unit activity
*  forming these different ensembles and synchronizing together.
*  At some level, that is going to be reflected in what we can read off in our MEG signal.
*  We just can't exclude different interpretations of it.
*  And that is very limiting.
*  But it doesn't mean that we should only theorize about the readout.
*  It would be sort of like if I tried to come up with a theory in psycholinguistics that
*  was about trying to explain reaction time differences for the sake of reaction time
*  and not trying to talk about the cognitive processes or the limits on eye movements of
*  how eye movement control works, right?
*  Not taking that into account.
*  So for me, it's thinking of something, trying to come up with a theory about, for example,
*  syntactic structure building and oscillations that assumes any kind of one-to-one mapping
*  between structure building and oscillation as if an oscillation is a kind.
*  It just doesn't really float for me.
*  So I try to think, okay, I want to try to do this difficult abstract theoretical work.
*  I'm first going to go into sort of this space where I know, given everything we know about
*  the world, this is where the action has to be happening, even if I can't directly measure
*  it myself.
*  And then try to challenge myself as I develop the theoretical model and different instantiations
*  of specification in a computational model and different empirical projects.
*  Try to say, okay, can the basic tenets, the first principles of this model, what would
*  they look like when expressed on the other end in MEG neural dynamics, which I can't
*  again pin back one-to-one to a particular state of affairs intracranially or on the
*  population level.
*  But still, I want them to be largely consistent with one another.
*  I don't think that it has the same explanatory force to come up with a theory of syntactic
*  structure building that talks about the delta band or the theta band as divorced from the
*  things that are actually producing those signals.
*  So neural dynamics, I'm going to have to struggle to continue because I just want to fall back
*  on oscillations.
*  Just say oscillations, that's absolutely fine.
*  We just go with the agreement between you and I that we don't, we're not trying to
*  talk about pure oscillators.
*  Right, right.
*  Well, that's the thing is it puts such a different flavor onto it and makes it less, it makes
*  it more agreeable because you can talk about dynamics is such a general term, right?
*  And your model talks about neural trajectories along a manifold.
*  So that's dynamics as well.
*  And you don't have to talk about oscillations per se in that regard.
*  Okay.
*  So, while I was going to ask you like what the general, I know there's never a consensus
*  in science, but what the current, current favorability within the language, cognitive
*  sciences, language of language community of oscillations is or neural dynamics or you
*  would answer them differently.
*  I would.
*  So, neural dynamics I think is actually, it includes more people and it includes more
*  periods of time.
*  Periods of time when, you know, like you can include in that related potential research
*  in that, right?
*  But on the other hand, I mean, I think the terms should be flexibly used.
*  But what I find, this is a bit meta response, but sometimes you can use certain terms and
*  they can be very, people can get completely the wrong idea about what you mean or they
*  react so strongly to that term that they don't listen anymore to what your argument is.
*  And so, I just wanted to, I want to try to reach the most, I guess, like prepared listener
*  or interested listener, not by sending people off already on, oh, but it can't be a pure
*  oscillator or it can't, you know.
*  Is rhythms not better?
*  Oh, rhythms is fine.
*  I mean, it depends, like I would say for, again, sorry, my theoretical, my laptop thing
*  is shaking.
*  I think it depends on your, on what your interest is.
*  So I think if you're going to use the term oscillations, then you have to be, you know,
*  careful about it to be sort of neat.
*  If you're going to, if you don't want to make that kind of commitment yet, because you don't
*  have maybe all the information you need, like myself, then I fall back on terms like neural
*  dynamics.
*  But for me, I find I'm okay with all these terms.
*  I don't find them, that they're making important theoretical distinctions at the moment in
*  language.
*  I had David Popol on the show and you know, you cite, he had some of the early work linking
*  rhythms, linking neural dynamics to phonemes and, you know, at the syllable level and correlating
*  different rhythms in EEG signal, for example, to the rhythms of the language.
*  And so, so I'm curious how, so back to my question, just how the field writ large sees
*  this kind of approach that you have, you know, continued and we'll come back to your work
*  as well.
*  I think there's like multiple layers here.
*  So you've got people who are like I've referenced before the debate between, you know, is it
*  an oscillation or not sort of camp and that can be focused around speech and music processing,
*  but it can also sort of be in all areas of neuroscience.
*  Then sort of within sort of the oscillations and speech world, you have people who are
*  interested in speech processing or in how oscillations might shape perception, psychophysics,
*  who are sort of very focused on a different sort of level of explanation, I think.
*  So I was recently at one of my favorite sort of workshops that gets together to talk about
*  exactly these issues and I was just sort of like, I was sort of, how can we not be talking
*  about language when we talk about the brain's response to spoken language, right?
*  I mean, that's really, I think, the behavioral goal.
*  And I feel like the more, I guess, I guess you would say it's the more low dimensional
*  behavioral goal of the brain, right?
*  People are trying to settle upon interpretation of the speech stimulus, right?
*  And so that's going to be linguistic in nature if you know the language.
*  What's the alternative with just talking about it?
*  Go ahead.
*  No, but I don't think that people actually think deeply enough about this.
*  I think there are interesting and important things to be explained in terms of speech
*  processing, but that there might be a lot of, again, dynamics or signals that are going
*  to sort of steer the brain that are more about more mesoscale objects like words or morphemes
*  or intonation or prosody or turn-taking.
*  All these different kinds of things might actually be driving more of the brain's systems
*  or the trajectory where you are at a given moment than per se reading out individual
*  phonemes.
*  Or if you want to talk about that, then you have to, you know, I think employ a different
*  kind of close experimental technique where you're really manipulating things on a very
*  fine-grained level.
*  So I think the sort of world of oscillations in speech processing is really quite focused
*  on understanding the theta rhythm and they have a lot of focus on things like decoding,
*  right?
*  So you, you know, segmentation.
*  And when I see that literature, I feel like it's a bit, it's a very important and inspirational
*  literature.
*  But for me, the difference is I want to have sort of orthogonal evidence to instantiate
*  a process.
*  Like if I want to attribute, because, you know, as you know, neural signals are so messy,
*  right?
*  There's so many things going on in the brain, plus all the signals and noise problems.
*  And then on top of that, I really want to have a strong motivation for saying, okay,
*  this difference that I find, it's really about segmentation or decoding.
*  I feel like that requires a lot of sort of theoretical pre-gaming and computational modeling,
*  I think, you know, ways to develop more specific claims about what those operations might be
*  before you can clearly attribute neural readout patterns to one or the other explanation.
*  But to return to your question about the sort of the status of the field, if I had to sort
*  of like summarize it in a high level way, you've got the focus really on speech processing
*  in oscillations.
*  And then there's a smaller but enthusiastic group of people working on what would have
*  been called sentence processing a few years ago in oscillations.
*  And this actually has roots even decades ago when people started looking in the time frequency
*  domain, mostly with EEG, and looking at basically power modulations.
*  And now this has sort of had a resurgence where we try to, you know, we do have different
*  techniques to look at the relationship between power and phase of different bands and different
*  linguistic annotations.
*  And within that camp, there seems to be some people who are more focused on how much can
*  be explained by having sort of a one-to-one mapping either between syntactic structure
*  or prosody or surprizal and neural oscillations or modulations of them.
*  And then I guess that would be sort of the main approach.
*  And I sort of don't really fall into any of that.
*  Right.
*  Okay.
*  Let's talk a little bit more about your model then.
*  But as you were describing the way the field currently sees this, it made me think of your
*  model.
*  So you posit, I mean, there's a lot of different aspects to your model, but it all kind of
*  begins with an internal predictive sort of model about what is coming speech-wise, right?
*  And that is like shaping the incoming sensory information and pushing it along a manifold.
*  So in that sense, and so maybe you can elaborate a little bit more on your model, but I'll
*  seed it with this question.
*  Like in that sense, are the like theta, are the rhythms sort of a readout of that shaping
*  process, would you say?
*  Yes, I would.
*  Thank you.
*  I'm so, it means so much to me that you got that.
*  That's wonderful.
*  Thank you.
*  Yes.
*  Yes, that's exactly right.
*  So when I was working on this model, I really wanted to challenge myself to try to capture
*  just the minimal things I couldn't give up about language with what I felt was this very
*  sort of abstract, low dimensional, and you could argue it's high dimensional, but it's
*  sort of manifold approaches in neuroscience that have been, they're only becoming more
*  popular but were sort of burgeoning a few years ago.
*  And I took a lot of, really dove into that to try to say, can I really make these things,
*  maybe they can't ever meet in a one-to-one way like I've talked about, I don't think
*  there could be this one-to-one mapping, but at least how much do I have to break concepts
*  in both fields to try to then fuse them together?
*  And I mean, yes, I think it asks a lot of readers, so I know that they have to sort
*  of be willing to dive into both domains.
*  But for me, that was the goal because I was no longer sort of satisfied with coming up
*  with box model-like theories that just didn't have anything to say about the neural readouts
*  that we were measuring.
*  And I didn't want to work on trying to understand these neural readouts and giving up sort of
*  my objective study or the lessons of linguistics and cognitive science.
*  So that was my response to that problem.
*  Well, maybe in your own words, can you describe your model?
*  Like the broad tenets?
*  I thought you did a great job.
*  Oh, okay.
*  Well, I...
*  No, so basically what I wanted to capture with this model was really the idea that you
*  have this unfolding trajectory where you can get a lot of the information that typically
*  would have been thought about in more traditional psycholinguistics or cognitive science models
*  as being sort of separate, right?
*  So even...
*  I in no way deny the fact that syntax and semantics can be described orthogonally, right?
*  So you can have separate formal linguistic fields and tools and methods for describing
*  the systematicity of those information sources in language.
*  But I think to the brain, even though it might...
*  I believe that we and the brain knows rules that are formally dissociable.
*  I think the actual representation of that information in real time and processing probably
*  does not best serve the brain by being distinct.
*  And so one way to bring that together is to think in a manifold space where you have populations
*  that might be able to decompose the source of information like syntax and semantics on
*  But it's really the patterns of activity that you can project into that manifold space that
*  are going to capture that information for language, right?
*  So it's kind of a way of having your cake and eating it too.
*  So you don't deny that you can separate these sources of information formally, but you have
*  a way of expressing them in neural population activity where they impinge upon each other,
*  right?
*  So you have to plot one in relation to the other, and that's the key.
*  So the manifolds are nested much as the structure of language?
*  Yes.
*  Although again, I don't want to say that that's a one-to-one relationship in the structure,
*  although I tried to say that they're not injective in the paper.
*  But I think that discovering exactly how they're nested and how they map onto each other, how
*  much different levels affect each other and how that's expressed in the space time of
*  And that's all obviously up for debate.
*  This is more a theoretical, is this possible?
*  What would this look like?
*  And just last month, they managed someone who was actually starting to work on manifolds
*  and speech processing, and I thought that this is really, really cool.
*  I mean, I'm hoping that they are going to solve all of the really hard bottom-up problems
*  of making manifolds of speech processing in a brain that I can come back in 10 years and
*  be like, oh, let me see if I can test my models on yours.
*  I mentioned it's a theoretical model, but how's it coming along?
*  Where are you in the process of implementing the various?
*  Yeah, there are various offshoots.
*  I'm not sure that I gave the best description of everything that the model claims, but maybe
*  that can come out as I keep talking.
*  What I've been trying to do is the core claim is that you're going to get relational structures,
*  the proto-ingredients of something like a word or a syntactic structure by looking at
*  the dynamics between populations.
*  This is how you can also preserve information.
*  You can bind words together in models like Dora, discovery of relations by analogy.
*  That's Alex Dumas' model, and he's a good friend and collaborator of mine, and we've
*  worked on this question together in the computational modeling space.
*  And then so my theoretical model takes that as a core principle.
*  So you've got this time-based binding, so you've got the neurodynamics that are giving
*  you these relational structures.
*  And then the question is, what are the sort of broad strokes, predictions of that, that
*  we can measure that we don't need to have data we can't get in order to validate or
*  not?
*  And a couple of students in my group have been working on projects that look at that.
*  So basically the sort of most coarse-grained claim is that there's going to be more phase
*  synchronization the more structure that you build.
*  So the more that you have to coordinate these distributed populations together in order
*  to establish relationships between them, the more they're going to be synchronized.
*  That's like a very broad strokes.
*  But might there be a ceiling of synchronization?
*  Probably.
*  That's the important thing.
*  So one of the things that comes back again, so what's the right baseline?
*  So what is sort of the base rate of synchronization in the language network or in the brain in
*  a given time or when you're listening to stories or when you're in resting state?
*  So establishing that's really important.
*  We're not totally there yet.
*  But looking sort of within experiment condition contrast, so between phrases and sentences,
*  for example, when we've meticulously made them the same length in time, physically indistinguishable.
*  This is the work of Pham Bayh, a recent PhD student graduate in my group, that we can
*  show that when you make these stimuli so that they really are physically as similar as possible
*  in the same amount of time, we can still detect a difference in synchronization and different
*  measures related to synchronization in EEG between whether something is a phrase or a
*  sentence.
*  And this is possible in Dutch because we can make phrases and sentences the same number
*  of syllables.
*  So going back to the, you know, just thinking about manifolds again.
*  Yeah.
*  I mean, is there a...
*  So I'm thinking of these kind of nested manifolds and the phase synchronization, helping them
*  communicate between each other.
*  Is there like an upper limit or maybe I should say lower limit, like the lower limit to the
*  dimensionality, right?
*  Because we think of manifolds as like a lower dimensional structure, lower dimensional from
*  the, let's say you have a million neurons, right?
*  Yeah.
*  So it's like a million dimensional space that then gets lowered, right?
*  And I relate the dimensionality to the abstraction of like a concept or meaning.
*  So where's the bottom?
*  Yeah, that's a good question.
*  I hadn't thought about the absolute, you know, what is the absolute bottom?
*  I always think that the important thing to remember with the manifolds that I talk about
*  in my model is that, you know, they're defined over a given time period and, you know, a
*  moment in the brain, so to speak, or a data set that you have.
*  So I don't know if you mean sort of like the bottom for all representational states or
*  for a given data set.
*  Well, I'm just thinking about intelligence and creating concepts and understanding, you
*  know, the meaning of a concept, for example, or the meaning of a story.
*  So maybe this is a way to approach the question.
*  So I was talking actually to Alex Deemus, my friend and collaborator about this.
*  So, you know, just because we think that neural dynamics are important for representing structured,
*  relational, symbolic information, that doesn't exclude the fact that, for example, single
*  units can learn or encode, you know, conductive codes, or that you have a localist node or
*  a localist code, which is different from conductive coding, that would encode some
*  kind of, you know, necessary ingredient for a relation or a particular binding, a particular
*  relationship between a value and a variable.
*  So probably the system is going to use both, right?
*  So you know, the famous grandmother cell and things like this.
*  I don't think that the existence of cells like that, you know, the debates, I don't
*  think that the existence of those, whether that's real or not, necessarily says that
*  neural dynamics aren't important.
*  And I think that neural dynamics being important for symbolic representation doesn't exclude
*  the fact that you have cells that encode this.
*  I think it's a sparse and redundant system.
*  Yeah.
*  Well, I'm not thinking so much in terms of neurons, and I apologize because I think my
*  question is ill-formed.
*  But I think the issue is I'm trying to picture these like state spaces and their relation
*  to each other within language, right?
*  And I want to like, so then I necessarily for myself, because I'm not that bright, I,
*  you know, I'm trying to like see the kind of the shapes and how they relate to each
*  other.
*  Yeah.
*  And then where's the end of it, right?
*  Where's the...
*  Yeah.
*  So I was trying to think about what you might mean with your question that it could be like,
*  what's the...
*  Sorry.
*  Make it a better question.
*  No, it's on my end.
*  I just don't understand the question.
*  No, that like, I was going to say that the sort of, you know, maybe one way to think
*  about it is what the system tries to do, again, because with these manifolds, you can do perceptual
*  inference, right?
*  That's another big part of my model.
*  Yeah, talk about that for a moment because...
*  Yeah.
*  So you want to sort of basically leap, you know, as much evidence as you have, you want
*  to take it as far as you can.
*  And you want to leverage your knowledge about the hierarchical structure of language and
*  your language experience.
*  You want to leverage both of those things, right?
*  So you, you know, we know that we have exquisite sensitivity even to, you know, speaker adaptations.
*  So talking to each other can change our vowel spaces.
*  And I think that, you know, we obviously want to use that information as much as we can,
*  but we don't want to, you know, be taken over by statistics such that we end up in the wrong
*  interpretation or not what's being said, right?
*  Because I know in an extreme situation is if we really were only just predicting the
*  most predictable thing, we would only hear that thing, right?
*  We wouldn't hear what was actually said because people don't always say the most predictable
*  thing.
*  That's often how we get important new information.
*  So I guess that's sort of the lower limit on conceptual representation.
*  If we're not going to talk about single neurons, then I would say is, okay, when you have something
*  that you really can't associatively or structurally or relationally relate to anything else, you
*  know, I guess then you've got, you know, I guess a predicate without an argument or a...
*  But if my internal model would fill that in...
*  Yes.
*  That's right.
*  That's right.
*  Yeah.
*  Yeah.
*  No, I mean, maybe new sensory learning or perceptual learning situations, I think, is
*  like learning that mapping of some sensory stimulus to, you know, your internal model.
*  And I guess my model would claim that that internal model is so biasing that it's always
*  going to be warping that sensory stimulus towards its state.
*  That happens as we get older, right?
*  We don't listen to what people are actually saying.
*  We listen to what we hear them for ourselves in our own internal model.
*  That's right.
*  Yeah.
*  I was just...
*  I mean, so, okay, going back to your model and the original question there, recent original
*  question was, you know, kind of how far along you are with the different aspects of the
*  model.
*  Right.
*  That's right.
*  Yes.
*  Yeah.
*  So like I was saying, so these findings...
*  So we keep finding, you know, again, the important...
*  That when language comprehension is happening, we compare it to a bunch of, you know, carefully
*  thought out controls.
*  We just...
*  We see again, you know, this synchronization is really important and also readouts that
*  are related to synchronization.
*  So coupling of various varieties.
*  And through that, we're then trying to make, you know, more detailed sort of movies of
*  activation in time to spoken language comprehension.
*  And then the rub becomes trying to understand those neurodynamics projected in space.
*  So how do we constrain that in the right space?
*  That's a whole another issue with human brain imaging.
*  I've been working on...
*  You know, starting to work on that in collaboration with others trying to situate these, you know,
*  dynamic signals in a space is a lot.
*  But then beyond that, right, you then want to understand how much of that signal and
*  the dynamics of it is just, you know, pushing a signal through a distributed network.
*  So when you can do...
*  When you can understand what's being said to you, you know, you're presumably recruiting
*  lots and lots of distributed networks, more so than if you can't understand it, right?
*  So even just that difference is probably going to be important for understanding,
*  for example, delta modulations in language.
*  But you know, so that's sort of the empirical trajectory.
*  We're trying to also get a better understanding of what's the right kind of annotation.
*  So a lot of the annotations that we use to decompose our neural readouts are things like,
*  you know, the syntactic structure is annotated in a story, an audiobook story, word onsets.
*  We can also use a lot of natural language processing tools to get things like phoneme
*  entropy, word entropy, surprizal, such and such, and use them to see, you know, as we
*  build these more and more specified or articulated models, how much more of the data is that
*  explained and that's all well and good.
*  But lately, more in my thinking, I mean, there are many people in the group working on that
*  and it's very important.
*  But I think we're all sort of coming to the conclusion together.
*  We need to sort of break or rethink how we think about expressing linguistic representation
*  in our annotations.
*  And so that's probably going to come through a combination of more data-driven decomposition
*  of the neural readout and that's something that actually machine learning and deep learning
*  can help with.
*  Oh, yeah.
*  But that's using it as a tool.
*  Yes, as a statistical model, right?
*  It's a way to decompose signals.
*  Sorry, I just want to clarify what that means, rethinking how the annotations are represented.
*  Yeah.
*  So more and more we're sort of questioning, like I said before, why I think that sometimes
*  it doesn't necessarily serve us to think about how syntax and semantics might be orthogonal,
*  even though they are, you know, I don't take away from any of their legitimacy as separate
*  systems.
*  I think the brain might have to do something more interesting to combine them together
*  or be constrained by them in real time.
*  Now, how would that actually work?
*  So the way that we do it now in our analysis is we annotate things and we, by the way,
*  don't have any good semantic annotations really.
*  That's another thing that we're thinking about and working on, right?
*  So the best thing that people tend to have are things like word embeddings or vector
*  embeddings that has a lot of...
*  In the state space and the message that you gather there.
*  Yeah, and that does okay, but that has a lot of assumptions in it that don't necessarily
*  have to be the case.
*  So we're also trying to explore, you know, what are the assumptions?
*  Are they going in the direction that we want or not there?
*  But my point is there that already in the annotations are some of our...is a specification
*  or a bunch of our assumptions about how it works.
*  And I think that that, you know, we need that right now because we understand so little of
*  the neural readout and it's gotten us...it's really gotten us a foot in the door.
*  And, you know, but I think we need to also at the same time push ourselves to think like,
*  well, how can we change how we think about this representationally without denying any
*  of the system facts, but not really biasing the view of what we see or putting blinders
*  on because we, you know, want to annotate our stimulus in this particular way because that's
*  the way we've always done it.
*  Is this a job for linguistics?
*  It is a job for linguistics.
*  It's where we need linguists indeed.
*  But I thought...but the annotation has been set by linguistics.
*  It has.
*  But...
*  In the past.
*  Yes.
*  So they might be upset if you come back and say, hey, we need you to do this different.
*  I think it's something where we work together, right?
*  Where we say, like, look, this is the property of your formal analysis that we want to capture.
*  But when we do it this way, we have a certain assumption about how that relates to the neural
*  time series data that we don't think is necessarily anything to do with your theory, right?
*  It's just a part of how the annotation works.
*  What do you think about that?
*  And then we can, you know, it's not easy or fast work, but it's important because I think
*  it creates another space where different expertise has come together to try to, you know, what
*  is the essence of what we want to capture with models, right?
*  And annotations are, in a sense, a model, right?
*  So this would be using an argument from dynamics, from time, to nudge a linguist to think more
*  in terms of how time would constrain...
*  There are examples of that out there already.
*  So there are people who have worked and thought about that.
*  But it's more thinking about then, how do you know, at the end of the day, how do you
*  get a matrix that then you relate to another matrix?
*  Yeah.
*  Yeah.
*  Unfortunately.
*  Yeah.
*  And you don't want to just use matrix multiplication.
*  So...
*  Yeah.
*  Okay.
*  That's the go-to.
*  Yeah.
*  Yeah, it was interesting.
*  I'd never thought about annotations in semantics.
*  I mean, you know, the story is it's all in a state space, an embedded vector in a state
*  space.
*  But have you guys come up with other potential...
*  There are some students in the group working on it.
*  It's a hard problem.
*  And I think there's a reason it doesn't exist at this point.
*  Yeah.
*  But it's more focusing more on...
*  And this is also inspired by the work of many, many people, that the sort of transition moments
*  when you have a change of state or something happens in the semantic world, not just the
*  distributional representation of a word in a corpus, it's something that's actually unfolding
*  in that particular phrase, sentence, or discourse that's important.
*  And some other...
*  There are many ways that this has been reflected to some degree in existing things, so situation
*  models, discourse models, but coming up with sort of annotations that could reflect sort
*  of the crucial insight of each traditional level of linguistic analysis I think is important.
*  Not everything is going to stick, right?
*  It's not clear to me how...
*  Again, what is the limit of this?
*  What is the end?
*  When do you stop adding features or predictors?
*  It's not...
*  Yeah.
*  I don't think you can play 20 questions with features or model predictors and win either.
*  But I think it is at least...
*  It is striking nonetheless that we don't seem to have a sort of standing go to temporally
*  situated semantic annotation.
*  Yeah.
*  Well, time is so important for biological systems, right?
*  Yes.
*  I mean, well, I didn't mean that as a question, right?
*  I have...
*  I did not...
*  I have not read this book, but I have it on my desk because it's that important.
*  Okay, cool.
*  I'll have to look that up.
*  The geometry of biological time.
*  I know.
*  You want to be talking about being scared.
*  Oh, that's going to be all about topology and moving along spaces.
*  Yeah.
*  Yeah, that's the other thing.
*  So yeah, then it becomes all about topology and that has lots of assumptions that I'm
*  not totally sure are right for this problem.
*  But anyway.
*  Well, you have to wear a lot of hats, right?
*  That's the other thing about language because you have to understand the linguistic structure.
*  Or you don't have to.
*  I think it's wise to, right?
*  Yes.
*  But I guess linguists...
*  So I'm going to come back to artificial systems here in a second.
*  But the first thing I wanted to ask you about then, linguists have traditionally discarded
*  time because it's of no importance when you're looking...
*  That's a question.
*  That's right.
*  So, okay, let's...
*  Can we return to the great David Marr and say they're working on the computational levels.
*  They have a computational level theory of what needs to be explained.
*  And that does not have to have any bearing on time.
*  Well, that's a question.
*  Is that true?
*  For their brain, I don't think it's true.
*  So that's sort of more and more what my models are ending up being is this...
*  That's the implementation level.
*  Even for the computational level.
*  Yeah.
*  But that you get...
*  All of the levels actually end up constraining each other in practice.
*  So again, it's sort of like the spherical cow situation.
*  Yes.
*  There is value in having theories on those different levels that are divorced from each
*  other.
*  But for me, and trying to go after the question that I'm going...
*  I see more and more how those levels have to influence each other.
*  They have to constrain each other.
*  And time is one that can constrain all of them.
*  And yes, how that impinges on the computational level I think is probably the most fraught.
*  Yeah.
*  Well, you know...
*  So going back to just the importance of time, it's everything.
*  I mean, our communication, yours and mine, I've often just kind of in my mind wanderings
*  thinking about consciousness and thinking, well, maybe the earth, maybe geological time
*  is just on a different scale.
*  We don't have to bring awareness into this.
*  But it's still a time scale.
*  But then something like a Turing machine or a large language model or any computational
*  model, you just can turn it off one day and then it's frozen essentially.
*  And time is not of the essence in a Turing machine, for example, because there's no necessity
*  for it.
*  So is that just a biological constraint or do we really think that there's something
*  that temporal...
*  Are dynamics important for cognition beyond biology?
*  I mean, this is a very deep philosophical and metaphysical question.
*  But I think that we're sort of dealing again on sort of the mesoscale, right?
*  For our brains and our behavior, time is really, really important.
*  And if you want to talk about what is time, of course, it's a deep question beyond the
*  scope of my expertise, but minimally, it has a relational quality, right?
*  So there's some relative nature to it, right?
*  That one thing happened before another or the path back from one state to another is
*  not accessible.
*  And I think not taking that into account would definitely hamper our understanding of how
*  information processing works and what neural time series data can represent or do represent.
*  So in that regard, I guess, a large language model does have some ordering somehow, although
*  it looks at everything all at once in one kind of computational step.
*  But there is a relational aspect.
*  Right.
*  But that relational aspect is fundamentally driven by what the goal of the system is.
*  So relational in accordance to what, right?
*  So if you don't have a...there's sort of no impetus or bias or reason to...or I could
*  say the motivation or the bias or the impetus to have hierarchical structure is not as
*  strong for predicting the next word, if that's your only task in life, as it is for clearly
*  for the task that humans are solving with language, right?
*  That language...I hesitate to use the word evolved because it's so fraught, but that
*  language appeared over time to solve.
*  Neural dynamics instead of oscillations appeared instead of evolved.
*  No, no.
*  I just...well, because I really...because I could just go...I could...you know, we could
*  have several of these interviews about all these other topics, some of which I'm not
*  an expert on.
*  And yeah, I'm trying to avoid that.
*  I want to give you the answers to your questions in a timely fashion.
*  No, I just think evolution has...there's a lot of assumptions about it that might hold
*  for biological systems where the link to language has to be better fleshed out and more carefully
*  contemplated, in my opinion.
*  Yeah, that's fair.
*  Again, not an expert.
*  Yeah.
*  I guess my question really is just about like...maybe I'm repeating myself, but how important
*  is the temporal aspect to cognition?
*  Is it just a biological constraint?
*  Or is there...are there so many different ways to skin a cat that we will eventually...these
*  large language models, even if they work on a completely different principle, will...without
*  having any time constraint, right?
*  And there doesn't need to be a manifold.
*  Well...
*  There doesn't need to be.
*  So one way to think about this is, right, so like I said before, you know, there are
*  infinite ways to cut a cake.
*  I was again trying to avoid the skin a cat exception, but okay, there's infinite ways
*  to skin a cat.
*  Neurodynamics, evolution, and cut a cake.
*  No evolution.
*  Appeared.
*  Emergence.
*  Also bad.
*  No, I'm just trying to not step in all of the minefields in one step.
*  I need to change that language myself, yeah.
*  So the cat language.
*  Anyway, okay, so the point is, so with large language models, maybe what they have in common
*  with the brain, and I don't know, for me this is not a deep insight, but maybe for others
*  it is, is that there's an unfolding time series, and in some way the language model is by having
*  access to everything all at once, but to having this sort of...there are different aspects
*  of the architecture, but also the mapping of the training procedure and everything that
*  do force that kind of sequentialization of information processing, that that is not in
*  common with how speech input comes into the brain at some level, right?
*  But like we were talking about before with time, I think there's a lot of people also
*  thinking about this notion of brain time, right?
*  Part of the reason that we have cognition, a way that we abstract away from sensory and
*  perceptual representations is to get away from the vagaries of time, to be able to do
*  more with that information than just have it be a sort of echoic perceptual thing that's
*  then gone.
*  We can have memory and we can bootstrap that and leverage all the other things we can do
*  with those representations once they've been taken away from their temporal extension.
*  We can do a lot more with that information.
*  But in the brain, in your proposed model, there's still...so oscillations have a lot
*  to do with the computational aspect, right?
*  So they're in some sense an implementation, although we just...before we're talking about
*  how they're more of a readout.
*  Maybe you can clear this up for me more.
*  Yeah.
*  How do you see oscillations in the world?
*  I think it's...so it's again one of these things where one characterization does not
*  exclude the other.
*  And I guess this is coming back again and again for me is that every time one is presented
*  with something that seems like it's mutually exclusive or a paradox, if you do a little bit
*  of digging, you quickly find that it's not.
*  So I think that it's definitely the case that when we talk about oscillations that they
*  can be a readout of computation that you could describe on the population level, right?
*  So in the sort of most neutral terms.
*  But certainly you could use the oscillations as a way of talking about the computations
*  on the population level that, as we talked about before, for humans we can't access.
*  But you can still also imagine a world where sometimes the computation that's embodied
*  in a particular population, it's going on and it gets hit by a traveling wave of information
*  that is going to change the sort of...however you want to talk about it, the LFP, the base rate,
*  whatever of potentiation of that part of that microcircuit or even on a larger level.
*  And then is it part of the computation or not?
*  Yes.
*  But also not know in the sense that you're saying, okay, it was like in the Boushaki term
*  of neural syntax that you're reading something out on the other, that you have a reader that
*  sort of catches the information processing of the last circuit or whatever, right?
*  So you're not in that direct link up situation anymore, but you can have your
*  computations still be affected by it.
*  So I think sometimes it helps to deconstruct a bit what we mean when we say, okay, are they
*  doing computations or not?
*  Is there actually a world where they're only doing computation and they're not or where
*  they're purely epiphenomenal?
*  And often the answer is always in between, right?
*  So same thing with the invoked induced question, right?
*  So clearly there's going to be evoked information that's important.
*  And clearly the role of oscillations or something that happens to oscillations is they get combined
*  with evoked responses because we can talk about...it is still important to talk about
*  specialization and encapsulation and maybe to some degree modularity.
*  Modularity is also one of those words for me.
*  But I think we also can't pretend like everything is independent or not connected spatially
*  next to each other, part of the same organ.
*  I mean, it's amazing thinking that we can think...knowing that we can think at all given
*  there's the circular causality aspect also because part of the computation becomes part
*  of the readout of the computation.
*  Yes, indeed.
*  But maybe that's actually a feature not a bug, right?
*  It's only from our perspective as the measurement person, the experimenter or the modeler,
*  that we make this distinction.
*  That's another important thing to always remember with modeling, that distinction between
*  readout and computation might only be true at that particular instance from our point of view,
*  from the brain's point of view or depending where you are in the brain or what
*  circuit or computation you're interested in, those answers can change.
*  So where am I left then thinking about building models of language?
*  Are we forever going to be coming up short because a model is always wrong, right?
*  Yes.
*  All models are wrong but some are useful.
*  Yes, exactly.
*  For me, I think this is also something that I think about a lot with my friend and collaborator,
*  Olivia Guest, when we talk about what can models tell us and how do models adjudicate between
*  theory and data and that the data are always right and that's not to be a data chauvinist,
*  it's just to be actually a proponent of theory building that we need to...the theories always
*  need to be better and what better actually means is complicated and depends on your goal and the
*  task at hand, right? But also my train of thought.
*  So you're alluding to a couple papers, the most recent was 2023 this year, that is really
*  specific about how to differentiate between levels, right? Theoretical levels, specification
*  levels, implementation, different aspects of how to figure something out.
*  Sorry, before we get to this, can I just interrupt you because I want to get back to...
*  You asked, now I remember what you were asking me. Where are we with building language models in
*  the brain and how frustrating is that? And while you were talking, I was thinking about, well,
*  maybe it helps to talk about what I worry about with the manifold approach is really like...so
*  when we want to think about capturing a formal system like language and a neural manifold,
*  and these are ideas and things I've worried about together with several people in my group,
*  Cass Kofman, Kartikeya Kaushik, and also with Alex Dumas, that how can you...if we want to give a
*  space to something like language, then we're taking this infinite means and putting it in
*  a finite space and isn't that problematic? And then we started to think about this more and more.
*  And basically, we have wanted to do this proof that we haven't gotten around to yet,
*  to try to think about whether the space of ungrammatical things is more infinite or a
*  bigger infinity than the space of grammatical utterances and to understand the relationship
*  of those infinite sets in relationship to the sets of what could be expressed
*  with neural dynamics in various manifold spaces. And I don't know the answer to that.
*  But that seems to me to be a clear, again, I think a lot about boundaries. If it's the case
*  that the orders of magnitude of infinity in those spaces are not reconcilable, then we have a problem.
*  That's for my own brand of language modeling. I can answer the question in response to large
*  language models as well. Let's stick on your own branding of modeling. So what's your hunch to the
*  answer? My hunch is that time, again, is time and space. So I don't have a very strong intuition
*  about the infinity of trajectories in different spaces and how they can...depending on that,
*  of course, and just completely on how they're defined. But time is a really important
*  aspect for approaching limits in those spaces. But my intuition about the grammatical versus
*  ungrammatical structure thing is more sharp. And that is that the space of ungrammatical strings
*  or utterances is going to be larger than grammatical ones. Because even within...this is a lot of
*  interesting formal work exists in linguistics. You can really show that the space of...in the
*  formal space, human languages still occupy a particular corner of that space. They're not
*  actually really that spanning the space of formal systems. And I think that's actually important,
*  and that can tell us something about the neural implementation of these kinds of systems.
*  Because it's like a limiting? Yes. Because I can at least say, okay,
*  if we can understand why those limits are there in that space, can we then understand the analog
*  in the neural manifold space? Again, that gets trippy really fast, but it's at least a foot in
*  the door. It's a way to tack down one part of the map to the other map and then to the territory.
*  Because otherwise, everything...you're no longer pointing at each other in a meaningful way,
*  I think. So that's at least in our space. So trying to sharpen the computational claims
*  of how a neural manifold could lead to functionally linguistic representations is one avenue. Trying
*  to look in neural time series data and neural dynamics to really understand if the broad strokes
*  predictions of the model about synchronization and coupling are born out in a basic way.
*  And then trying to tease apart or break the ways we think about annotations and
*  form linguistic representation to sort of brain them. How much can we warp them or smooth them
*  or change them to become more integratable with our neural dynamics?
*  Is part of the...so you mentioned earlier the problem is you have an infinite
*  potential of grammatical structures. And then the one that we occupy in that state space,
*  we're in a very small corner. Yeah, so it's slightly different. There's two important
*  aspects here. One is that any language has infinite productivity. Basically, through recursion,
*  we can keep adding stuff forever. Nobody does that because nobody lives forever, unfortunately.
*  That's a limit on a proof. But the other observation is that the way that human
*  languages work, they still only occupy one particular corner of the space of possible
*  formal languages, the way the formal languages could work, which we see in computing mathematics.
*  But I think that fact can be capitalized upon more than we currently do in understanding
*  that state space and trying to relate it to neural dynamics in some way. Not in a one-to-one
*  way. Again, that's almost never the right approach. But what are the constraints on that space? What
*  are the constraints on the neural manifold space of expressive trajectories? And then can we begin
*  in that way to gradually link things together such that we have a principled way to decide
*  what are the kind of annotations that we should relate to our neural data?
*  Yeah. Okay. What is the dimensionality of language?
*  Oh, it depends on who you ask.
*  Sorry. Is dimensionality one of those words for you?
*  No. Dimensionality is a safe word. It's a good word. Dimensionality reduction.
*  Well, yeah. I mean, the reason, right. So a manifold is a reduced dimensionality space.
*  And then if we're comfortable with language on a manifold, it sounds dumber.
*  Yeah. No, but okay. I don't want to go into the... tractability is also maybe a bit...
*  It's at least it's more studyable for us. And I think, again, like what I said, if we think that,
*  yes, it's not to say that there aren't neural signals that are tapping into all these different
*  dimensions of language and of perceptual experience. It's just what are the... What's the PCA of them?
*  What is the thing that's really... That we can attribute most of the trajectory to? And as much
*  as that's at least signal strength. Now, that doesn't in any way mean that that other information
*  is not encoded or important to the brain. Yeah. Then we start being limited by how we can relate
*  our models to the data, I think. Okay. Should we go back to talking about just how you approach
*  all these? There are just so many issues. And recently you've written with Olivia Guest,
*  Yes. kind of formalizing an approach.
*  Did you take on that project because just there are so many thorny issues for language specifically,
*  or is this just a cognitive modeling? Yeah. For us, it was really... We were working together
*  and we had such a great time writing the first modeling paper and really coalesced some of the
*  things that she and I think about in our own research programs, which are actually very
*  different. But we think a lot in the same ways. We have a lot of the same sort of reactions to
*  things. And we really had a sort of, I don't know, a catalyzed way of thinking about modeling
*  together. And it was just so much fun. And I really felt that we were... So many things that
*  we've been thinking about really came together. And that was a natural extension to that was
*  something about that for computational cognitive neuroscience. And also the more and more we saw
*  the sort of pattern of reasoning in the field where we think, is that really what people want
*  to claim? What do we take away from that? That's not totally internally consistent. And then we
*  started to analyze it more and think about it more deeply. And then this sort of... It all started
*  actually from a tweet thread of some observations and frustrations that I had. And then Olivia came
*  and worked as a postdoc for a year in my group before moving on to an assistant professorship
*  in AI here at the university. And that one year, we just got so into this paper and banged it out.
*  And there's so many things that would continue from that and thinking about these problems.
*  What were the frustrations that you had? That you felt compelled to tweet about?
*  Yeah, always a mistake, right? Never work out your emotions on social media. In this case,
*  it had a good outcome. But it's more that I see more and more and I don't want to make it
*  personal or anything because I hold us all accountable. I think it's really a sort of
*  zeitgeist or a way of thinking that we all are complicit in. Is that when you fit a model to the
*  data and you get a good fit, you don't conclude that the model then is the object that you're
*  modeling. And that seemed to just start this sort of is happening more and more. And maybe it's
*  particular with language, but I've also seen it in vision, to be honest. And I'm really still
*  very interested in exploring what does that mean for people? And this is sort of a meta science
*  question. Like when you say, okay, this model, because it's very different from the sort of way
*  that we learned cognitive modeling, the both of us in the 90s and 90s. It's just a different
*  approach, right? Where you start to really sort of things start to bleed together in a way that
*  as a modeler, I never considered. Elaborate on that. What do you mean they bleed together?
*  Well, I think it's more sort of like the map and the territory. So the properties of the
*  map that is your model of the territory, they don't extend to the territory itself. So I think
*  in our paper, we have some great example with a digital clock. I don't know if you remember
*  this figure. Yeah, I was just I was trying to pull up the paper just because I wanted to get the
*  different levels right. So this is the 2016 one. For my model or for the work? Sorry, no, the
*  2020. That's the paper with Olivia about logical inference. And yeah, but that doesn't have the
*  one that has the oh, that's the one from 2021. You mean the 2021, the modeling with a theory
*  specification and yeah, okay. Yeah, but we can talk about so the 2023 one is complex.
*  It is. Yeah, no. Remind us of the the clock. Yeah, so the clock. Yeah, I have a slide of it here.
*  I don't know if it's helpful to share that. Well, the vast majority of the audience is
*  on this audio. Okay, so I'll try my best to describe it. So the whole that whole paper is
*  based around what we see as this fallacy and reasoning, not necessarily directly in the
*  empirical work. So we're not making a claim about the work that people are doing is inductive
*  reasoning. So we're not trying to apply deductive rules to it. But what we're saying more is when
*  you create a meta theoretical calculus about that talks that formalizes how models relate to theories
*  and data that these kind of fallacies into a pop up and you see them again and again, we have this
*  whole, you know, whole sort of database of occurrences. So we were thinking about a digital
*  clock and analog clock or a clockwork clock as an analogy to, for example, large language models
*  and the human brain or something. Right. So digital clocks display the time clockwork clocks
*  display the time and require manual winding. Therefore, digital clocks require manual winding.
*  Right. So that's clearly a fallacy. We see it easily when we talk about digital clocks and
*  clockwork clocks. But when we talk about large language models in the brain, somehow this
*  eludes us somehow there's this strong urge to give the attributes of the map to the territory. So
*  then we can translate this. So we do this. So artificial neural networks correlate with
*  MRI data. Brains correlate with MRI data and instantiate the biological mechanisms for
*  cognition. Therefore, artificial neural networks instantiate the biological mechanisms for cognition.
*  So is this in response to like the recent work that compares the predictive responses in brain
*  activity to the predictive correlates that to the predictive aspects in large language models?
*  Yeah, I think it's actually a tradition that's been going on for quite some time. Yeah. No. So
*  then we've made a version of this syllogism that makes it more specific. So artificial neural
*  networks produce grammatical strings. You can say large language models produce grammatical strings.
*  Humans produce grammatical strings and instantiate the biological mechanisms for language.
*  Therefore, large language models instantiate the biological mechanisms for language.
*  Not going to be the case, right? Yeah.
*  Not necessarily. It could be the case.
*  No, it could be the case, but not necessarily.
*  That's a logical fallacy to assume it is the case.
*  Yes. And the other point is that we talk about this in the papers. There's so many things that
*  would disqualify these models as being models of cognition or of language. But we don't worry
*  about that fact so much. Can you list some of those?
*  Well, the parameters, the training procedures, the data, the complete lack of internal structure
*  that has any interpretable mapping to cognitive theory. And that's all changeable, right? That
*  could be changed. It doesn't necessarily have to be the case. But something just to say briefly
*  about it, because again, this is not my focus, is that as you see, as the performance becomes more
*  and more important, the predictive quality for the brain is also going down, right? So that's
*  something that many people have noticed. So yeah. At the end of the day, I don't really know. I think
*  about this a lot because it's so common, right? People really believe that there is something
*  behind it. And I want to understand what that is. So I tried to ask myself, what would it mean
*  if we take that key claim to its limit? And I wrote some notes for myself about this because
*  I was really trying to think about it. And I guess some of the things that-
*  The key claim being that large language models are useful as-
*  So they're different claims. So I think that most extreme version is like large language
*  models are the brain. Everyone will say, oh, no, no, no, I don't mean that. I don't mean that.
*  Okay. But I think another version of that is, oh, well, they're a good model or a good enough
*  model of language in the brain or condition in the brain, right? So I think that's fine.
*  And then we can talk about what's a valuable model. I think that's all very complicated and
*  worth thinking about. But of course- Sorry, what's the key though? The key
*  claim that you mentioned is the good enough version? Yeah. So what typically seems to happen,
*  and this is what this paper with Olivia that we focus on is you find that an artificial neural
*  network or a large language model can predict neural activity. And then what do you conclude
*  from that? Therefore.
*  Therefore. And there's all this range of conclusions. So I guess maybe a good summary,
*  the sort of middle of the road one is like, oh, then these models are good models of condition X,
*  task Y, capacity Z in the brain. Fine. Let's go with that. So then when I was thinking about this,
*  you know, so the price of modeling or the power of modeling is that you sort of exchange,
*  you exchange specificity or you simplify and leave out stuff and gloss over things in order
*  to gain insight into the shared causal structures of the mechanisms between your model and the object
*  of modeling or the phenomenon in the world. Right. But in some way, when we do this, if we say that,
*  you know, substituting models of cognition or theories of cognition and language with large
*  language models is good enough, or if we base our theories on them, in some level, I think we're
*  saying that predicting signals is more important than explaining them. And I think we have to think
*  about if that's what we really need and what are the implications of that. Maybe people disagree
*  with that. Maybe that's not what they mean when they say that. Then I want to know more of what
*  is it what is meant by that? What is the good model? Is it a good model because it predicts?
*  It's a good model because it behaves a certain way. That's the other thing. So in some level,
*  I think we're saying that behavior is an approximating function approximation is enough.
*  And that seems like an engineering goal to me. But some I think even some neuroscientists would be
*  well, neuroscientists concerned with behavior would be okay with that.
*  If the answer is like, what is cognition, not what is biological cognition?
*  Yeah, no, I think this touches quickly and deeply back on to, you know, debates about
*  computationalism and cognitive science, representationalism. And again, I think,
*  again, I think it's both. So I can, you know, why can't dynamical systems represent and compute?
*  It's a choice for us to believe that they cannot. It's a choice for us to not to try to,
*  you know, bend or break or reformulate how we talk about these systems, both formally and conceptually
*  in order to do that. And that's what I think it's the same with structure and statistics face the
*  hard problem. Are they really mutually exclusive? Does one really mean we can't do the other?
*  When is one useful?
*  We're so much more comfortable thinking and talking in dichotomies. Is that a roadblock?
*  On some level, I don't know, I just had the insight that, oh, maybe that's actually like
*  a fundamental part of like, of cognition and perception in general is trying to give a
*  deterministic perceptual interpretation to a probabilistic series of cues, right?
*  All from a probabilistic brain. The probabilistic brain is.
*  Yes. But then again, that's that same tension between structure and statistics and between
*  dichotomies and gradients and whatever, you can create a gradient from between anything.
*  It is again that tension. So you've got, you know, this probabilistic cues and for the sake of
*  behavior and for, you know, I guess, some levels about practicality, determinism enters into this,
*  the processing stream at some point, right? And categorizing things is also one of the things
*  we do well that has served us well, right? So concepts, making concepts.
*  Yes, indeed.
*  So orthogonalizing everything to its maximum degree.
*  That's right. And I think that clearly has a huge benefit, right, in terms of structuring the world,
*  right? Creating an internal structured model. But it has, you know, it has, I think it has negative
*  sides too. But then there's, of course, very interesting things and, you know, there's fuzzy
*  logic and vague concepts of how to be truly vague in logic. And I think, you know, these are sort of
*  the limits of what we can think about formally as well, you know, on the other side, right? But
*  so talking about more sort of practically, right? The urge to, I guess, or the something fundamental
*  about the perceptual system has this categorical goal, right? Because so much of perception is,
*  that's the whole point of it.
*  Yeah. Yeah. Okay. All right. I distracted you from, I think you had some, you were going back to your
*  notes about the way that you think about this fundamental.
*  Right. So what, yeah, so I wanted to think, I was asking myself, like, what's really behind this,
*  right? So like I said before, you know, it's, what's, so what would it mean if a large language
*  model was an adequate theory of X or Y in language or in cognitive science or in neuroscience? And
*  I'm just trying to think about the kinds of answers that you end up with.
*  And again, to summarize those answers is like, don't, maybe this is not doing justice to the
*  range of things out there. But one of the sort of middle of the road things to say, oh, yeah,
*  you know, large language models are a good or good enough model of language processing in the
*  brain or of language representation in the brain. And I want to know more, like, what do people
*  actually mean by that? Right? Because they don't, if you say, well, so do you mean that like the
*  brain is a large language model? They would say no. And that's reasonable. No. Right. So then what,
*  what would it, what does it actually mean? So then I think, charitably, I think what they mean is
*  that there's some important or meaningful similarity between systems that correlate.
*  Right. And this is, again, a little bit what we talked about with the geocentric and heliocentric
*  models, right? They correlate with each other, but they come from fundamentally different claims
*  about the nature of the solar system. But again, as Olivia Guest and I have discussed at length in
*  our papers with multiple realizability, the infinite ways to skin a cat that we've agreed
*  to talk about, infinite ways to cut a cake. This correlation actually doesn't tell us very much.
*  Maybe, maybe, you know, most charitably could say, okay, well then there's got to be some broad
*  strokes, low dimensional similarity, like I said, about the time series or about the fact that,
*  you know, it has all the language data, text data ever produced. And that language is what is
*  underlying that the human mind humans created those data like that. That's in common. Yeah.
*  But it doesn't tell, it doesn't, for me, that's not a, that's not the kind, it's not an explanation
*  for how language works in the brain. And that's just a different, it's a different nature of,
*  of, you know, meaning behind that claim. So that, you know, I think this needs to be analyzed and
*  thought about more carefully. So what, what, you know, if you say large language models are good
*  models of language in the brain, what does it actually mean? What are the things that that
*  entails in logical interpretation?
*  I mean, do you apply the same principle to all the work in vision with convolutional neural
*  networks being the quote unquote best models of, yeah. Yes, we would. Although I realized,
*  you know, that's a, that's a much more, there's a large, much larger literature and a larger
*  sort of population and tradition of people working on that. And I don't, you know.
*  Would you say it's more rigorous too, because the findings are correlated to single units?
*  Single neurons, you know. I think, so I think in the limit and like sort of in the logical space,
*  it's not any different, but there is something I would say inherently beautiful about seeing
*  that correlation sort of extend down to every pin of the, you know, of the system, so to speak.
*  And you see it in that way. And it is, like you said, for some behavioral neuroscientists enough
*  to really be able to predict every subsequent data step, right? And Jim DeCarlo would say,
*  and control, like prediction and control is understanding.
*  Yes, for me that's engineering, but that's, that's okay. I mean, that's, that's what people
*  think, right? It's E understanding, engineering understanding or something.
*  And we want I science. Yeah, there you go.
*  I think, I know, I mean, I think, I think it's complicated. I think these debates are really
*  worth having. And I'm very suspicious of myself and others who have extreme exclusionary views,
*  where you say, you know, that, you know, right. Well, okay, it's maybe, maybe that's all we can
*  achieve, right? Is prediction and control. Don't you want more? Right? I just want more. And I
*  think more is possible. It may not be in the, in the form that we expect, where we think like,
*  okay, and, you know, an explanatory model of making it up, sensory motor control, you know,
*  is we have these boxes and you know, there's just different forms, right? Different levels.
*  And I don't think that we should, you know, every, maybe, you know, I don't think we then that the
*  solution is not to say that prediction and control are is understanding. I think that's.
*  But for you personally, because you dive into potential mechanisms in the brain underlying,
*  you know, how I try. Yeah. Well, yeah. In your theoretical approach. I mean, does it matter how
*  the brain like for you personally to have a satisfactory understanding of how language works
*  in biological cognition in humans? Does it matter how the brain does it?
*  Yes. But I think there are two aspects to that. So do the particulars of how the brain does it
*  matter? Yes and no. Right. So I'm, I'm not able to get, I think maybe this is maybe the difference
*  between the, the DeCarlo prediction and control and is understanding. And that's enough is
*  I had to accept long ago that I would never have perfect prediction or control, right?
*  It uses a different state of, you know, of organism and, and ethical situation, you know,
*  that, that I don't think that I need to have, I don't, I don't want to model, for example, a model
*  of general relativity where I have to know the position of every atom in the universe to know
*  whether my model is correct. That would give me prediction and control, but it would give me no
*  understanding of the principles of the system. But I actually don't, I mean, I would actually say,
*  I mean, I don't know Jim DeCarlo, but I don't think, I think that they, everyone is actually
*  gaining more than just prediction and controls understanding. They're actually doing inference
*  when they write their papers and think about it. They are in their head trying to glean categories
*  and first principles. They are, that's, that's what the human mind does. That's the human urge
*  that underlies all science and it has to be refined and honed and carefully carried out to become
*  science. And then, but I think it's, I mean, I don't think that, I feel like that's, that somehow
*  missing out on a core thing. It's actually not actually accurately describing what people are
*  doing even in vision science to say that you're just trying to get prediction and control and
*  that that's understanding. People are still trying to derive some first principles based on it.
*  You know, I recently had, um, Ellie Pavlik on and, um, Gail Lupien and there's a lot of people who
*  are, one, just, you know, impressed with the large language models, of course, we all are,
*  but also like probing them. And I'm not sure where they land on, you know, whether it's a good model
*  for biological cognition, but then, you know, they're, but they're like, Ellie Pavlik is
*  finding some symbol-like representations, right, in the large language models. And so they are kind
*  of being used to probe and there's a lot of people excited about large language models as models of
*  biological cognition. Well, so can I jump in already? So I would say there already,
*  there's a different approach. So there is a tradition of having, of instantiating symbols
*  and connections networks that goes back to the 80s and 90s, the work of John Hummel and Alex
*  Dumas and Keith Holyoke. And they are, it's sort of a different, you know, the idea is like,
*  what do we need to use to realize something that's symbolic in a neural network? And the key thing,
*  the key sort of insight of Alex Dumas' work is that, you know, what do I need? What is the
*  series of algorithms or transformations of information in the internal states of a
*  settling neural network that I need, you know, to predicate something, right, to learn structured
*  representations from unstructured data, right? That's the insight of Dora, which I could talk
*  for a long time about. But, I've lost my train of thought. Oh, so the other approach that you're
*  talking about is sort of where, well, you know, symbols emerge. And then again, as I talked about
*  the beginning, then you have to do the hard work of like extensively testing this. So then you have
*  to say, okay, what's a symbol? What counts as being a truly symbolic representation? And to some degree,
*  the previous work, especially in analogy and categories and concepts, literature and cognitive
*  science has done this and has established some benchmarks for what that would be. Those are not
*  currently being applied in natural language processing, I think, maybe for historical reasons,
*  or it's taking a while for people to discover that literature again. But it's, I think that's just a
*  very different approach. And it seems more sort of like open-ended, right? So like, you know,
*  what if you just haven't found it again? What is that with the black swans and the white swans? You
*  just haven't, you know, you just don't know whether one day one's going to come along, right? So maybe
*  you just haven't found the right test. And I think that's a much more, I would be much more sort of
*  on shaky ground with that rather than saying, okay, I've understood the principles of what I need
*  to have a neural network realize something that's functionally symbolic. Yes, it's important to test
*  that what the representations are, do those, do they meet those criteria? But then at least I have
*  a theory about what caused that to occur. Otherwise, looking at emergent behavior,
*  let's not to derive that at all, I'm sure that has value. You still look in the end, you find those
*  symbolic representations. Well, how did they get there? How do you know, how are they instantiated?
*  Will they always be instantiated the same way? How much are they dependent on the properties of the
*  data that were produced by systems that have symbolic representations, i.e. humans?
*  Sure. I see I scratched an itch there, or maybe caused an itch with this, you know, specific to
*  symbols. But you know, I was bringing it up as a, which I'm glad I'm glad you went down that road.
*  But I was just bringing it up because the question was, you know, where do you land on what the
*  usefulness of like a large language model in their current instantiation? Are they useless to think
*  about biological cognition? Like, you know, what do you see there? Yeah, I think the links to
*  biological cognition are most tenuous. I think the closest link is through the data, which,
*  you know, we don't always know everything about in the training regime, which we don't always
*  know everything about, but mostly through the data because that is produced by the system we're
*  trying to study. But it's like, through how many filters do you want to study the systems?
*  Okay, so I guess large language models have two aspects that people would deem important for
*  studying, right? So they have the behavior that humans have, right? So let's say that they produce...
*  Impressive output. Right, let's say that.
*  We don't, I mean, so that's the one thing that they have to study. They don't have any of the
*  other constraints that we have. So if we think maybe there's something, maybe that is telling
*  us what in the limit is learnable from data that we don't get exposed to as humans or as children.
*  But I don't think it's useful or productive to sound completely negative about this, but
*  I'm really just honestly saying my point of view is I just don't see the links because they have
*  not been constrained in a rigorous way. I understand the urge to say, oh yeah, it's a great
*  model organism for language, but it doesn't... I don't know, it's a bit like saying, you know,
*  a model organism for a mouse would be like some output of all the mouse behaviors and like a space
*  with like, you know, how much of... Could you know about them? What we know about maybe the
*  mouse is too high up, but about, I don't know, what's the... See elegance that we have the
*  full connect in? Well, of course you can debate about whether that's actually even the right
*  redoubt to be caring about, but I think it's useful to think about for what other system,
*  if you were to make a large language model of it, would you be satisfied studying that object?
*  Well, I think the curiosity is just how well these deep learning models are performing without
*  having been built generally, you know, like with the constraints of organismal... But they were
*  specifically built to do this task, right, that they're doing, and then they are exquisitely tuned
*  now with human feedback, and they are given the... Basically the prerogative, impress us,
*  give me a response that can't be the training data, but that is a really good approximation of it,
*  and of course, you know, that it can do that at all is deeply impressive, but without... You know,
*  we don't know about the leakage, we don't know about how much, you know, the training and the
*  test data is completely blurred, we don't know the role of human feedback, we know that there's so
*  many other things about the models that violate our beliefs about what a tenable system is,
*  they're ethically very fraught, I mean, that's something that is not my expertise, but that I'm
*  very aware of, that there are so many ethical issues that come up with these, and that they
*  really amplify power structures, there's all sorts of complicated important work about that, but yeah,
*  I don't know, I feel like I'm letting you down not being an enthusiast, but I'm just...
*  Why are you so negative, Andrea? I know. No, no, this is great, because it's kind of...
*  So positive about manifolds, so negative about the harsh language model.
*  And LLF, harsh language models have zero manifolds, so...
*  Well, but that, I mean, you know, that's a question.
*  No, I know, yeah. You can make anything into a manifold, though.
*  That's one of the weaknesses of manifolds and gradients, anything can be a gradient.
*  Right, right. Whenever I see
*  gradient work, I'm always like, but anything can be a gradient, but yeah, no, but I do think that
*  it would be, you know, I thought about doing this, I think, I'm not sure that it's worth it,
*  but that, you know, looking at the dynamics of large language models, they're going to be very,
*  very different. So you don't feel like... So you are tempted to sort of probe, look more into
*  large language models for your own negative reasons, of course.
*  Yeah, but I've tried, you know, Alex and I did some work where we, you know,
*  where we made Dora, the settling neural network model that can learn predicates, play
*  Pong after being trained on breakout and vice versa, and it can do that because it learns
*  relational representations. And we did a whole series of stuff where we learned relational
*  representations from the clever data set and then played these games. And the way that the work,
*  it was just so difficult to communicate what we were trying to say. There's such a, I feel like
*  not being completely enthusiastic and on board with large language models, it's already a quite
*  difficult position to be in. And I feel like my own, you know, my own work and my own case is not
*  often served by being negative, but I also don't, I can't, and that's what I think. So I
*  just try to say what I think and be kind about it. But do you feel like that large language
*  model world is encroaching on your approach, you know? Yeah, no, I feel like, and I, you know,
*  the reason why, you know, I feel sort of that I will engage with them because I can't not,
*  they're so, they're everywhere. And I think they're loud. And, you know, with manuscripts
*  and for my students and my team, you know, I have a responsibility and I want to put them in the
*  best position to grow their talent and go where they can go. And I'm not going to hold them back,
*  you know, because of my own beliefs, right? So I, you know, it's an interactive process. And,
*  you know, we always tend to end up on the same page. I mean, I've never had any, like, you know,
*  huge disagreements in my own team is actually quite, I mean, there's many ways to explain that.
*  But my point is more, I don't think it sets, you know, already coming into a polarized debate.
*  And also, you know, I don't know, I think maybe someone who's different from me, if they were
*  advocating my position might be received differently. I can never know about that.
*  So I try to just talk, you know, say what I think, say it in an accessible way,
*  not disparage people's entire research programs, but yet say what I think needs to be said. And
*  that's not, you know, it's not easy. I'll say that it's not always clear what the right thing to do.
*  So it also makes you more unique that you're not walking down the path that every
*  scene everyone seems to be walking down, right? In terms of mentorships and guiding your students,
*  I mean, is there there's value to being unique, right? And just not not falling into the
*  large language model trap. From my experience, you know, again, I don't, you know, go back and
*  forth on this. It doesn't necessarily always go over well, you know, you don't always get hurt,
*  or you get misinterpreted, or sometimes, you know, you just sort of get excluded, because it's not,
*  you know, how do you engage with that? These are also the dynamics of all human activities,
*  science, politics, life. Yay. Yeah, exactly. But I do feel like it's important for my students to,
*  it says a bit of a learning process in that as well. So, you know, well, how do you defend
*  what you really think and how you do it in a way that people will listen to some degree?
*  How do you do it in a way that doesn't exclude you completely from everything else? You change
*  oscillations to neural dynamics is one thing. You don't talk about evolution, you talk about
*  appearances. No, I don't advocate any of this. I'm just, you know, I'm figuring out as I go,
*  it's not it's not easy. But for example, like for funders, I'm very aware that, you know,
*  talking about language models in the brain probably won't be seen as timely or contemporary if you
*  don't have something to say about large language models. Oh, yeah. So just cast them off. No,
*  no. And I feel like that's also that's also sort of not it is also a moment where language is in
*  the public's view a lot more. And so that's actually good for language sciences and for
*  and for neuroscience in the end, too. So it's a way of engaging with that and trying to make the
*  best of it without compromising one's principles. And so, yeah, I just I guess I won't ever go on
*  the record saying I think that there's like, you know, something exciting is going to change
*  everything. I think, again, for what I've said, you know, when we when we say that these these
*  models are enough, we're saying that behavior is more important. And it's not even behavior in the
*  sense of human behavior. I don't even want to make that equivalence that a certain, you know,
*  sequence processing or grammatical strings is more important that are contextually licensed or
*  however you can make them more generous in your description, that that's the most important thing
*  about a model, not what it explains. And maybe from a prediction and controls enough,
*  that's understanding. Maybe those two things align, right?
*  All right, Andrea, I've taken you far enough. And we've we've walked down a hierarchy of
*  manifolds and we haven't even get to everything that I know, I feel like we could have done,
*  you know, there are many other manifolds we could have explored a lot of manifolds.
*  And maybe another time, I'd love to have you back another time. But
*  I appreciate you figuring all this out for us and continued success doing that. And thanks
*  for taking the time. Thank you. Thanks so much for reading my work. I was really it was really
*  wonderful to hear you talk about it that you got it right away. It meant so much to me. Thank you.
*  I alone produce brain inspired. If you value this podcast, consider supporting it through
*  Patreon to access full versions of all the episodes and to join our discord community.
*  Or if you want to learn more about the intersection of neuroscience and AI,
*  consider signing up for my online course neuro AI, the quest to explain intelligence,
*  go to brand inspired.co to learn more. To get in touch with me, email paul at brand inspired.co.
*  You're hearing music by the new year. Find them at the new year.net. Thank you. Thank you for your
*  support. See you next time.

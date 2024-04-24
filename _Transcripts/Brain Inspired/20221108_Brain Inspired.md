---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 6312s
Video Keywords: []
Video Views: 44984
Video Rating: None
---

# BI 152 Michael L. Anderson: After Phrenology - Neural Reuse
**Brain Inspired:** [November 08, 2022](https://www.youtube.com/watch?v=wzAlY4PvbK4)
*  That's a really important thing to notice.
*  And what you see instead is that each bit of the brain is involved in multiple cognitive
*  functions across multiple categories of cognitive function.
*  And now you've got a very different thing to explain.
*  It's a mistake to suppose that just because you can get a neural network to do something,
*  that that means it's a hierarchical representational model, blah, blah, blah, in the brain that
*  does something similar.
*  There's vast mystery here that remains for anybody in this field.
*  And if you deny the mystery, you're simply closing your eyes to the reality of where
*  we are in the science.
*  This is Brain Inspired.
*  Hello, it's Paul.
*  And that was Michael Anderson, a professor at the Rotman Institute of Philosophy at Western
*  University.
*  In 2014, Michael released his book After Phrenology, Neural Reuse and the Interactive Brain, which,
*  among many other things, introduced the idea of neural reuse.
*  Roughly, that is that any given brain area is involved in multiple different cognitive
*  functions.
*  And different cognitive functions happen as a result of the coordinated activity among
*  different sets of brain areas.
*  So a given brain area might be used during one cognitive function, like attention, for
*  example, and have a set of partnering brain areas to implement attention.
*  And that same brain area is reused during another cognitive function, like say, working
*  memory, but have a different set of partnering areas to implement working memory.
*  In the book and related works, Michael details plenty of evidence for neural reuse.
*  And he argues that this is strong evidence against the modular computational view of
*  the brain that still dominates cognitive neuroscience, even though we got rid of that phrenology
*  kind of explanation or view long ago.
*  And he also writes about how it relates to evolution, inactive and embodied cognition
*  and many related topics.
*  So we talk about all that.
*  And Michael takes a couple guest questions from friends of the podcast, John Krakauer
*  and Alex Gomez-Marin, which deal with mental representations and metaphysical views of
*  the mind.
*  So you can learn more about Michael in the show notes at braininspired.co.
*  slash podcast slash 152.
*  If you like this podcast, consider supporting it on Patreon, where you can join our discord
*  community and get all the full episodes.
*  So for example, in this episode, we end up talking about language and transformer models
*  during that extra time.
*  So thank you to all my Patreon supporters.
*  And thank you for listening.
*  All right, here's Michael.
*  Michael, I'm going to actually start by reading the last paragraph from your 2014 book, After
*  Phrenology, before the appendix where you list a bunch of open questions, the official
*  end of the book, I suppose.
*  So here's that last paragraph, and then we'll rewind and talk about what it's about, etc.
*  You wrote, I very much look forward to walking the path that lies ahead.
*  This is, I believe, the most exciting time in the history of the neurosciences, a time
*  when major technological advances are allowing us to measure and analyze brain function in
*  ways undreamt of even just a few years ago.
*  If we can manage to sustain a level of conceptual progress that keeps pace with the rapid march
*  of technology, then the future of our science is astonishingly bright.
*  And then you ask, shall we get to work?
*  So this is, again, from your, I would say it's a modern neuroscience classic, After
*  Phrenology.
*  I see it cited so much.
*  Would you accept that it's a, would you call it a classic?
*  Well I hope so.
*  It was a monumental effort on my part, and it does seem to have been usefully influential
*  in a lot of corners of the discipline.
*  And certainly it's gotten high praise in various places.
*  So the word classic is a bit, it feels a bit much.
*  Okay, well you're maybe being humble.
*  Maybe.
*  But no, but I do think that there's a lot there.
*  And I also think that although it has been influential in various ways across various
*  parts of the discipline, I think, if I'm being honest, I think the depth of that work has
*  yet to be fully understood.
*  And so there is definitely, as it were, as I allude to, as you allude to in that paragraph
*  you read, there is more conceptual work to be done.
*  And I think the book can help, it still has work to do to help with that conceptual work
*  that needs to unfold in the neurosciences.
*  I mean, so I have a cognitive science reading group here at Western, and we read a very
*  nice article, and it exemplifies exactly what I was pointing at in that paragraph, which
*  is it introduces a brilliant new method of measuring intrasubjective correlations in
*  neurodynamics, just really great stuff technologically.
*  And then in the discussion, it falls back on localization of function because, and their
*  method does not naturally match with that approach to interpretation.
*  And so there's a gap there that needs filling.
*  And I think, you know, Afrofrenology has part of the backfill, right, the conceptual apparatus
*  you need to put in place to make full use, to be able to fully appreciate what you're
*  learning from these advanced techniques.
*  But clearly that part has not really registered yet.
*  And so that's the conceptual advances that still need to come, that need to be absorbed,
*  that need to change, not technological practices.
*  I mean, people much more brilliant, much more mathematically talented than I are pushing
*  those frontiers every day.
*  But they're still doing it as if they're working within a framework that we developed for the
*  general linear model for the, for the, well, this thing, the amplitude of this change in
*  this particular region indexes this particular part of the stimulus.
*  That's a really flat-footed and simplistic way of looking at brain function.
*  And we have the conceptual tools to move beyond it, but those things haven't penetrated to
*  the degree that they need to, let's put it that way, you know, that they need to.
*  And I'm hopeful that, look, it's a young science.
*  Well, yeah. So, okay, so you're still hopeful.
*  We're going to have to step back and just talk about the high level conceptual basis and
*  premise of your work, of your research agenda, because there are actually multiple moving
*  parts, right? And then they all kind of fit together.
*  But before we do that, so you're still hopeful, you're still optimistic.
*  They haven't dragged you down reading the conclusions of a paper that that fall back onto
*  the, you know, the...
*  No, no, no. And this is what I said to my grad students who were in that in that room with me
*  yesterday, which is, look, this is exactly the opportunity you want.
*  Right. Right.
*  This is you can say, look, here's a really interesting paper.
*  Right. Look at look at the new method they introduce.
*  Look at the cool findings.
*  And then look at what they do and they interpret it.
*  What paper is this, by the way?
*  So I don't know. I think I don't want to be critical in this way of.
*  But you must see this frequently in the literature.
*  Well, absolutely. And that's that's but this is this is yes.
*  You know, this is, you know, crisis opportunity.
*  Right. So so this is like, OK, that's great.
*  And this particular author, I respect quite a bit, the senior author, you know, and he's
*  been one of the prominent, most prominent neuroscientists really taking seriously the
*  notion that we have to grapple towards a different conceptual framework.
*  Oh, man, you're going to have to make me guess now who the author is.
*  No, maybe people can try and get up with it.
*  Yeah. And but so my message to the students was, you know,
*  oh, this is gross.
*  We should walk away. No, this is now let's look at the success of this method.
*  Right now, if you were to sort of a priori devise a view of brain function.
*  For which this method was the natural answer, what would that view look like?
*  Like what induction can you do from the methods, the success of this method?
*  To a conceptual framework for understanding the brain.
*  That's the gap that has to be filled.
*  And it's going to take a lot of people doing a lot of thinking to fill it.
*  But those gaps, when those gaps show up in literature, the last thing to do is to get
*  frustrated by it. Instead, you say, aha, look.
*  Right. We can show we can demonstrate it's obvious there's a gap here.
*  So let's start doing the conceptual work that would be needed to say.
*  OK, this, you know, so the general linear model, right?
*  This is just straightforward, you know, basically statistical covariance.
*  It was based on the notion that the brain is modular.
*  It's got dedicated regions that do a thing and all you need to do is isolate that thing.
*  And if you could do that and say a display, a simple display or a simple task, you know,
*  you can do it sort of in a visual display or you can do it with a with a kind of a so-called
*  so-called pure task, right?
*  A task that only activates one particular brain function.
*  If you can find that thing, if you can find that display, then when you when you turn
*  that thing on in the display or you have the person do the task, you'll see, ah, this is
*  the bit of the brain that responds most strongly to that.
*  OK, right.
*  That's the that's the terminology.
*  That's the phrenology part.
*  That's the phrenology part.
*  And if the brain were like that.
*  And by the way, people, you know, came up with this notion that the brain, well, it's a
*  very old notion, hence my reference to phrenology.
*  But but even the modern version of it, which is sort of more computational and modular
*  and whatnot. So it's sort of, you know, the the the old old dressed up in the new.
*  The general linear model is a perfect fit.
*  For that notion of what how the brain is organized, right?
*  That's an adequate empirical approach to the brain because it's it allows you to
*  discover the bits that appear to be dedicated to particular functions.
*  And you can get significantly statistically significant models, right, that would support
*  that sort of view as well.
*  Absolutely. So it wasn't like it was a it was a mistake or a dumb move or not at all.
*  There was a view of function.
*  Then people matched the the the the analytic methods to that view of function.
*  And of course, we've got 50 years of neuroscience based on this that has produced all
*  kinds of interesting results.
*  Now, you know, as you know, having read the book, you know, much of my my career for the
*  past 10, 15 years has been dedicated to showing that the data gathered under this
*  assumption actually undermines the assumption.
*  If you look at it the right way.
*  But that brings us back to this paper and the opening, which is that.
*  OK, so now we've got this really brilliant new multivariate method that allows us to,
*  you know, do not just individual but intersubjective measurements of synchrony, you
*  know, under various conditions, really cool stuff.
*  And then they fall back interpreting it as if they're still within the GLM, you know,
*  modular view, even though they clearly reject that.
*  And that's the gap.
*  Could this have been reviewers?
*  Could this have been reviewers that shaped that that outgoing those outgoing remarks?
*  Oh, guaranteed. Yeah.
*  OK. Yeah.
*  So one of the stories I told in this meeting yesterday where we discussed this paper was
*  that I was on a master's, a neuroscience master's defense recently.
*  In which another it's really cool work, you know, pushing the envelope methodologically,
*  you know, trying to.
*  Maybe this is a little off topic, but basically the real innovation.
*  So a typical experiment in neuroscience and cognitive neuroscience in particular is what
*  we call open loop. That is, you have a stimulus, maybe you make a response to it.
*  Maybe it's just passive viewing as in like the movie paradigms that have become very popular.
*  But in any case, whatever your response is, it doesn't affect anything in the future.
*  Right. So it's open loop.
*  The circuit, the usual, you know, sensory motor, sensory circuit is broken.
*  In these cases, we we close the loop.
*  And so this is a student of mine and who's who's now moved to her PhD program and
*  and she managed to figure out a way to play Pac-Man in the scanner.
*  OK. With what?
*  I mean, it's got to be like just a joystick down by your side, right?
*  Yeah, I think with the trackball is what they ended up using just because of, you know,
*  what I thought what we had or because that was you need less movement of the arm.
*  Yeah. Right. So you're wiggling the head less.
*  And so it's just a trackball anyway.
*  That doesn't matter. I don't think.
*  But but here.
*  But the notion, the important notion here is that your actions change your perceptions
*  inside the scanner. This is the inactive viewpoint.
*  This is the inactive view. This is the closed loop view.
*  This is, you know, this is, you know, fixing Dewey's reflex arc problem.
*  And and, you know, lo and behold, it took a lot of technological grit and perseverance
*  and changing, but we got really cool data that showed that, yeah, indeed, the brain
*  looks very different in closed loop versus open loop circumstances.
*  Interesting. To me, that was enough.
*  Like, OK, we proved this could be done.
*  This opens up a whole new avenue for research in closed loop contexts.
*  But some of the other examiners like, well, no, you have to interpret.
*  Like, what does that activation mean?
*  I'm like, we're not there yet. Have you read my book?
*  They have not. But but, you know, so so this notion that somehow,
*  even though you're you're pushing things in a very different direction
*  and you're operating under a very different set of assumptions,
*  you've got to turn around and interpret the local activations.
*  And if you don't do that, you're not done is pervasive.
*  And I think it's a it's a it's a massive mistake.
*  And if you're going to do it, you've got to do it honestly.
*  So you've got to go to something like Neurosynth, you know, that giant database
*  that tell you, yeah, tell your Coney put together and say, OK, well,
*  if you really want to know what this activation means, well, let's let's put it into Neurosynth
*  and let's see all the things that cause activation of the area and now interpret it.
*  Don't just interpret it as if it's in the context, right, that you think you know about
*  in the context of Pac-Man and what could be going on here.
*  Let's look at all the things that could be going on here
*  that have been already observed to be going on there.
*  And of course, nobody takes that stuff, right?
*  They're they're interpreting things in a vacuum.
*  And I think that's really unconstrained.
*  And and there's no reason to do it.
*  There's interesting things to be learned without taking that step.
*  Well, when you take it in a vacuum, though, I mean, you're addressing the cognitive function,
*  for instance, that you are particularly interested in in your lab, right?
*  So but what what you're saying in the neural the neural reuse story,
*  I guess this is a good time to bring it up, is that a particular region
*  can be active in multiple different contexts
*  and that the way that regions interact with each other,
*  there are different sets of regions that are interacting.
*  And so one particular region, if it's active during Pac-Man,
*  doesn't mean it's the Pac-Man region.
*  Or or or the or the ghost region or the pellet region, right?
*  Or the right.
*  That's just a flat footed way of looking at things.
*  And so that's right.
*  That that's that's that's why I say that, you know, if you analyze the stuff
*  gathered under the GLM model, under the modular model, under the dedicated region model,
*  if you look at all the data that's been gathered,
*  then there's a vast troves of this data that have been gathered.
*  And then you you you go at the next level and you analyze it.
*  You can show that the assumptions on under which the data were gathered
*  get undermined by the data itself.
*  Right. Yeah. And that's a really important thing to notice.
*  And what you see instead is that each bit of the brain
*  is involved in multiple cognitive functions across
*  multiple categories of cognitive function.
*  And and now you've got a very different thing to explain.
*  And so one of the conclusions that I came to as a result of this kind of analysis,
*  as you just said, that differential function, differential behavior
*  is not a matter matter of differential activation of brain regions.
*  It's a matter of differential cooperation.
*  Across different brain regions, many of which will be the same
*  across different kinds of behaviors.
*  And again, the data supports this.
*  Now, that's not a deductive argument, right.
*  But that's what the data show.
*  And now you've got to either question the data or question the methods
*  or if you want to get out from under that that conclusion.
*  But so I wanted to ask you how you came to this view, because,
*  I mean, was it something where you were looking at a bunch of data
*  and then, you know, induced neural reuse and
*  and and inactive neuroscience or, you know,
*  was it more something from first principles, just thinking about the complexity
*  and the way that complex neural networks interact?
*  How did you formulate the idea, these ideas over, you know, the few years
*  leading up to because you've been working on this stuff a lot,
*  you know, for a lot longer than you published before you published the book.
*  Yeah. So, you know, I come out of embodied cognition.
*  I was working on embodied cognition before that was a thing.
*  Is it a thing yet?
*  I guess it's a thing now, isn't it?
*  It's definitely a thing.
*  Now, it's it's for sure a thing.
*  You know, there's there's interesting kinds of infighting and, you know,
*  the inactivists versus the embodied cognition versus the ecological psychologist.
*  You guys need to all get along, right?
*  The four E's, they need to get along, right?
*  Well, certainly.
*  So so certainly inactivists and ecological psychologists need to get along.
*  I think there's no question about that.
*  The question is what to do about the embodied cognition, folks.
*  And I did come out of embodied cognition.
*  And here's the distinction.
*  So both in activism and ecological psychology,
*  don't start with representations.
*  Now, depending on who you are, you might think representations
*  come in come online in various ways later.
*  You know, what you're in a pitchy knee is like this.
*  But that's that's that's that's not really a dispute that's worth,
*  you know, breaking up over the difference between that and the embodied cognition
*  theorists is the embodied cognition theorists are still within the computational
*  framework where representations are central.
*  Right. The difference is that the way they understand the nature of the
*  representations is quite different from, say, the a modal symbol theory,
*  which is the extreme of the computational view.
*  But the difference is that the way they understand the nature of the
*  but like the a modal symbol theory of the percent of the physical symbol
*  systems hypothesis, for instance.
*  You know, instead, you know, Larry Barsalu is, you know, James Martin,
*  people like this. No, no, no.
*  There are representations and they're they're computed in kind of the standard way.
*  But the content of those things are grounded in the body in various ways.
*  And that could mean they're grounded in visualization.
*  It could mean they're grounded in inaction.
*  So Andy Clark is for me.
*  He's one of my intellectual heroes.
*  But we disagree on this point. We do now.
*  We didn't back in 1992.
*  But we do now.
*  And because the embodied cognition theorists stick to the representational
*  theory of mind, it's just they understand representation is grounded in the body
*  or action oriented or, you know, there's various stories you can tell
*  about how to understand representations in an embodied sort of way.
*  And I think that marks a really significant divide in the four E world
*  between the embodied folks and the inactive and ecological folks.
*  And that's that's that's, I think, a real divide worth fighting about.
*  Whereas I think the differences between activism and ecological psychology,
*  I think those are the interesting differences of focus.
*  Right. Where differences in starting point.
*  But I think there's really convergence in those views.
*  So I'm going to I'm going to go ahead and play you the first guest question
*  because you dropped the representation word there.
*  And OK, do you want me to finish, though?
*  The we'll come back to it.
*  We'll come back to it. OK.
*  If we can keep that thread.
*  Totally fine. Yeah.
*  So this is from John Crackauer and.
*  Yeah. Oh, yeah.
*  You'll appreciate that.
*  No, I love his work. Yeah.
*  I can I can probably just say the question myself. Yeah.
*  Oh, that'd be that'd be awesome if you say the question.
*  It's actually it's kind of long.
*  So it's almost two minutes.
*  So so be a little patient, I suppose.
*  Both both my guest questions are a little bit long.
*  Hi, Michael.
*  It's John Crackauer here.
*  My question pertains to
*  your recent article in reply to Russ Poldrag on representation,
*  where I think you touch on a number of your favorite topics,
*  you know, including sort of Gibsonian affordances
*  versus representations.
*  And I'm extremely sympathetic to your take
*  on artificial representations, neuro representations and.
*  How they don't really map on to mental representations
*  as posited by most people who believe in them.
*  And, you know, I also wrote a review of Nick Shays book
*  where I felt one didn't even have to invoke representations
*  where he does or someone like Gueltierre Piccinini does
*  in motor cortex, sensory cortex, ventral stream.
*  I don't think the representation needs to be evoked at all.
*  It doesn't solve Ramsey's job description problem
*  or meet, I should say, those criteria.
*  But what I struggle with with all the anti-representationalist
*  is when it comes to the conversation
*  that you're now having with Paul or, you know,
*  true cognitive content, ideas, beliefs.
*  Locked in patients can write novels through eye blinks.
*  Electrodes can evoke forced thoughts in frontal cortex.
*  I simply do not see how we can do without
*  the mental representation notion when it comes to those phenomena.
*  And I always feel like they get skirted around
*  by sub-personal processes in sensory and motor areas
*  and other such things.
*  And citing Dennett in 1981, in my view,
*  does not get rid of the problem.
*  So I was wondering if you could just tell me,
*  how do you come up with a story about this question
*  I'm answering you and how you're going to asking you
*  and how you're going to answer it?
*  Without having to invoke mental representations.
*  All right. Sorry, that was a mouthful and long,
*  but I think you got it all right.
*  Yes. Yeah. And he, you know, this is all familiar territory.
*  So, well, no, a couple of things I want to say at the outset.
*  So, by the way, I totally agree with John about Nick Shea's book
*  and Gualtieros recent work.
*  You know, they use this word representation.
*  And that's fine. People can use it however they want.
*  But the trouble with that word, one trouble with that word,
*  is that it's got such a bit of a historical baggage that comes with it.
*  And I think this is part of it.
*  I say this explicitly, by the way, the other author on that paper,
*  it's not just me, it's Heather Champion, a grad student of mine.
*  And so we say explicitly in that paper that,
*  you know, neuroscientists use that word in such a way
*  that they're kind of borrowing the notion
*  that they're somehow speaking to mental representations,
*  because that's what eventually we do want to understand in psychology.
*  That's psychology, right?
*  At least there's those folks who say psychology is the science of behavior.
*  I'm just quoting textbook titles now, right?
*  But the other is science of the mind.
*  Right. Let's understand how that that bit works.
*  And so at least on the latter interpretation, that's what we're asking.
*  Right. How do beliefs and desires and intentions,
*  how do ideas get expressed and communicated between people?
*  He mentioned writing a novel.
*  I don't know. Anyway, writing a novel.
*  Like, how does that happen without mental representations?
*  So the main point of the piece on Poldrack
*  is to point out that the kinds of things that neuroscientists,
*  and I think he's right to loop Puccini and Shea into this camp.
*  The main thing that they're pointing to aren't the kinds of things
*  that have an obvious relationship to mental representations.
*  And if what we care about is mental representations,
*  this kind of work, at least in its current incarnation, is not going to get us there.
*  It's interesting in its own right.
*  These are clearly, you know, they're part of the mechanism of behavior.
*  These are information carrying neural activations
*  that clearly are involved in behavioral guidance in light of perceptual phenomenon.
*  All that seems right to me.
*  But as I say in that article,
*  that's totally compatible with the Gibsonian take on all of this.
*  Right? Even Gibson would never and did not deny that there are neural representations
*  that carry information about aspects of the world.
*  You should clarify what the Gibsonian take is for the audience, perhaps.
*  Okay. Long story here.
*  But the basic idea is that, so on the classic view,
*  let's just focus on visual perception because that's where Gibson focused.
*  But the same case can be made in other sensory modalities
*  and across different kinds of perceptual experiences.
*  On the classic view, visual stimulation
*  creates a two-dimensional retinal image
*  which clearly cannot capture all the aspects of the actual world.
*  So it's impoverished with respect to the actual world.
*  Therefore, you have this two-dimensional impoverished retinal image
*  from which you have to reconstruct
*  the physical properties and layout of the actual world.
*  So you need a whole bunch of what my friend Tony Chimera calls mental gymnastics
*  to achieve that.
*  And so you build a model, a speculative model,
*  of what the world might be like given the impressions that it's putting on your retina.
*  And once you're in that space, in cognitive science,
*  that just brings in all the old notions of model building and built-in assumptions.
*  And where do the assumptions come from?
*  Are they evolutionarily derived?
*  Or do they come from experience in some way?
*  Right. And so you've got these assumptions that structure.
*  It's very neo-contain, right?
*  You've got these assumptions that structure behavior,
*  that's used to that structure of the model
*  that allow you to interpret the incoming impulses from the retina and so on.
*  Gibson just rejects all that.
*  First of all, he says the retinal image is a fiction.
*  There's nothing in the retina on which an image could be projected.
*  It's a fiction that was derived from experiments
*  where people dissected cow eyes and such things and put them in windows.
*  And notice that the light was refracted through the lens.
*  And then if you put a piece of paper behind it,
*  you got an upside down image of the world.
*  Right. But we can decode based on the two-dimensional retinal activations.
*  Right. And that's the thing you need to decode.
*  And so there was a whole kerfuffle like, oh my gosh, it's upside down.
*  How do we turn it right side up again?
*  Yeah.
*  Right. And that's actually a question that it's funny, right?
*  But it's actually a question that makes sense from within this.
*  If you take the stance, that's a real question.
*  Like, you know, the model's upside down.
*  You've got to turn it back upside right side up somewhere, somehow.
*  So Gibson just rejects all that.
*  He says, look, first of all, there's no retinal image.
*  Furthermore, there's no poverty of the stimulus.
*  Right. Think about it from the standpoint, not of what he calls ecological optics or ecological physics,
*  not from the standpoint of, say, Newtonian or Einsteinian physics, but
*  light in the environment bounces off of and is thus shaped by every surface in the environment.
*  So at any point in an environment, with the exception of things that are fully occluded from
*  incoming light, the light itself is structured in a way such that it carries information
*  about all the stuff that it's bounced off of.
*  He calls this the optic array.
*  And his claim is that the optic array in and of itself carries sufficient information about the
*  layout of the environment.
*  There's no lack of information there.
*  This is direct perception, right?
*  Is that?
*  Yeah.
*  This is what leads up to the view of direct perception.
*  Well, maybe that's too subtle a thing to care about.
*  Yes. This is what leads to the view of direct perception.
*  And so the notion is that what you're not doing is taking the impingements of the world
*  in an imagistic way and using that to build a model.
*  What you're doing is you're learning to coordinate your behavior with the structure that's actually
*  in the light.
*  Right?
*  And so whether it's upside down, right, set up, this is not a relevant question anymore.
*  There's insufficient information in the optic array to allow you to coordinate your behavior
*  with respect to the environment.
*  It specifies, as he says, the layout of the environment.
*  All right.
*  Yeah.
*  And so this is the direct perception view.
*  There don't need to be epistemic mediators.
*  There don't need to be representations.
*  There don't need to be models, right?
*  That then you use to infer what you ought to do in the environment.
*  You can directly perceive the layout of the environment by coordinating with the structure
*  in the light.
*  So that's the Gibsonian view.
*  And it's a non-representationalist view.
*  It's important to note, back to John's question, it's important to note that Gibson himself,
*  he was talking about visual perception.
*  He wasn't talking about novel writing.
*  Right?
*  Right.
*  Right.
*  And so, and what follows from the Gibsonian view, I think, at least if you generalize it to
*  the kind of account you want to give of a cognition writ large, is that there's no necessity
*  to base or to center your explanation of mental phenomena, of successful behavior on
*  representations, on models, right?
*  What you need to do is understand coordinative dynamics, coordinative structures.
*  How does that process happen?
*  And so, James Gibson's wife, Eleanor Gibson, she took over the developmental side of this.
*  And part of her story and some of the people that she trained and worked with,
*  Karen Adoff is one instance at NYU,
*  where what they're understanding is, what does that development look like?
*  By which you learn to coordinate with various kinds of aspects of your environment.
*  What's the information that's available?
*  How do you learn to coordinate with it?
*  What's that developmental trajectory look like?
*  So those are the questions you start asking from the Gibsonian standpoint.
*  Now, novel writing.
*  So one thing, this is not meant to be a sidestep because I'm not going to sidestep,
*  but I got to tell you, I find questions like this really unfair
*  because I want you to show me the cognitive psychologist that has explained novel writing.
*  I don't care how many representations they throw at it.
*  Nobody understands what it takes to write a novel, to be creative.
*  To be creative.
*  But I suppose John's bet would be that the path forward to explaining would be,
*  we would be better served with a representational viewpoint, right?
*  But it's just a more likely bet.
*  Yeah. So I just wanted to register my objection before I said something about it.
*  Because honestly, this is kind of the classic move that the folks within the tradition
*  take with respect to upstarts like ecological psychology.
*  Oh, sure. That's cool for motor control.
*  And in fact, Poldrex says this explicitly in that paper that I responded to.
*  Oh yeah, that's cool for motor control.
*  And visually guided motor activity.
*  But-
*  Right. Needed for perceptions.
*  But he also, in Poldrex's paper, and I think one of the things that John is impressed with,
*  and I'm of course impressed with, I'm sure John's going to be impressed with,
*  I'm sure you're impressed with, are artificial neural networks, right?
*  And that we can get some sort of quote unquote behavior out of an artificial network.
*  And presumably it's through these, the representations in the nodes and weights
*  of that artificial network, right?
*  So just throwing that out there.
*  So remind me of this because I'll come back to that after I, so,
*  well actually, you know what?
*  It's better to lead up this way.
*  So I've got a paper hopefully coming out relatively soon.
*  We've got to revise and resubmit on it, writing it with some collaborators on autoencoders.
*  Was this a preprint already that, is this autoencoders?
*  Oh, you might have seen it.
*  Yeah, yeah, yeah.
*  Yeah.
*  This was autoencoders.
*  Oh, this was a question I was going to ask you.
*  How autoencoders are in line with the Gibsonian?
*  Oh, is that why that question came up?
*  Yeah, because of that preprint.
*  Yes. So it's that.
*  And we revised it and resubmitted it and we'll see what the verdict is there.
*  But the basic conclusion of that paper is that you still don't have to use representational talk.
*  You can talk about adjustments to the structure of the inputs.
*  Right? And so that's, it's at least compatible with a kind of Gibsonian perspective,
*  not in detail, right?
*  Gibson didn't talk anything about neural nets and whatever.
*  But this notion that, and this gets to this interesting paper by, well,
*  Yuri Hassan is one of the authors.
*  Direct Fit.
*  The Direct Fit paper. And we kind of follow his line there, suggesting that, yes, it's an option to
*  talk about these things in terms of models and representations, but you're not obligated to do so.
*  And autoencoders is the vehicle we choose to illustrate that,
*  however successfully you think we did.
*  But back to the question.
*  My own view is that, yes, there are mental representations.
*  And now I give a kind of origin story of them.
*  I think that language began, so I'm Vick and Shtenian on this point,
*  that language began as a kind of a complex method of coordination.
*  So just a straightforward extension of our ability to coordinate with information
*  in the environment, in the optic array, in other modals, sensory modals.
*  And so Vickenstein's Builders is kind of an exemplar for me.
*  Right? You just say slab.
*  And that's not a name for a thing.
*  It's a request for a particular item.
*  And your coworker goes and grabs you a slab, which you then lay on the wall in the correct orientation.
*  And J.L. Austin's How to Do Things with Words is in a similar spirit.
*  That we tend to think of words as representational, as fundamentally representational.
*  And what Austin says is, you know, they're fundamentally performative.
*  And what I suspect is that the representational aspect comes later.
*  It comes from who knows where this came from.
*  Again, I do want to emphasize that despite this often being used as a kind of cudgel
*  against these non-representationalist views of cognition, there's vast mystery here
*  that remains for anybody in this field.
*  Right.
*  And if you deny the mystery, you're simply closing your eyes to the reality
*  of where we are in the science.
*  I just want to clarify, you're talking about mental representation, not neural representation, right?
*  I do not have an account of how neural representation and mental representation line up at this point.
*  No one does.
*  Yeah.
*  That's the issue.
*  Yeah.
*  But to John's question, look, I want to admit, yeah, I think that's right.
*  That there are representation-hungry problems.
*  I would love to get Tony online here for 10 minutes and see what he has to say about this,
*  because he's a bit more aggressive on this than I am.
*  But I think it's right that there are representation-hungry problems.
*  That writing a novel is clearly one of them.
*  It would be.
*  And so I'm happy to let representations in at some level of our mental architecture.
*  Detached?
*  John wants them detached.
*  And a lot of-
*  What does detached mean?
*  Uncoupled, rather.
*  Uncoupled from the sensor motor performative aspect of embodied and active aspect.
*  Yeah.
*  They would have to be that.
*  He mentioned Bill Ramsey.
*  They would have to be that for it to meet the job description challenge.
*  And presumably, they have to be there to write a novel with them.
*  Right?
*  It's not like you're acting out every action of your characters as you, right?
*  And so what I want to say is that I'm perfectly happy to allow them in the cognitive economy.
*  Where I want to draw the line is the notion that they are at the core of that cognitive economy.
*  Right?
*  What they are is add-ons.
*  And where they came in and exactly how they came in, these are all very open questions.
*  You can do the Tomasello thing.
*  But yes.
*  So at some point, we acquired the ability to use storage sensory motor traces
*  to do things that didn't involve overt sensory motor action.
*  And that was probably the origin of mental representations.
*  And once you've got that, then you can elaborate language in a particular kind of way.
*  And once you've got language elaborated in a particular kind of way, now you've got
*  yet another resource to scaffold a level of mental representation.
*  Right?
*  That allows you to do even more cognitive work than you're able to do.
*  Right?
*  So I want to insist that the core of the cognitive system is the sensory motor coupling.
*  But that, yeah, sure.
*  There's an ability to step back, as it were, from that and to utilize the kinds of stored
*  traces that those processes create or enable.
*  Well, I'm not going to articulate this well, I'm afraid.
*  But in the back of my head, I have this.
*  So what you just articulated was that sure, the representations could be there and they
*  could be uncoupled.
*  But the challenge is to get from where we are now to that story.
*  Right?
*  And I suppose someone like John's way of thinking of it would be that we have these
*  internal models and that when they're active, those are the representations.
*  And it's just totally uncoupled from our sensory motor faculties.
*  But then if I was going to speak for you, would I say that in a Gibsonian direct perception kind
*  of way that comes into our sensory apparatus and then gets processed in a direct manner,
*  let's say like that?
*  I mean, as you go up the hierarchical structures in the brain, is there a story to be told
*  about the constraints of the brain architecture where it's essentially the same process
*  where you don't have to speak of representations then, but it's just, you know, I mean, now I'm
*  tripping over my own words because, you know, I'm thinking of like activations becoming more
*  abstracted, more abstracted, right?
*  And then somehow that counts as a representation, but to fit it within a Gibsonian story.
*  Sorry, that was just an incoherent blabber perhaps.
*  Well, and this is the trouble we get into when we start thinking about this, right?
*  So you said hierarchy, right?
*  Hierarchy already brings a bunch of baggage with it.
*  And you said more and more abstract.
*  That already brings in a particular view of what's going on here.
*  I haven't thought a lot about abstraction, I'll be honest, but I, you know, it makes my skin crawl
*  a little bit.
*  So I like, I have the sense that there's something wrong with that way of talking, but the hierarchy
*  thing I want to push back against hard.
*  Okay.
*  Brain is not hierarchical, except in very limited cases, it's heterogical.
*  We could say layered.
*  Well, the brain itself is, you know, anatomically layered,
*  but that's very different from saying it's functionally layered.
*  Okay.
*  Hierarchy implies function to you then, and I suppose it.
*  Yeah.
*  Well, and you said move as things move up the hierarchy.
*  I know, I know.
*  It's hard to avoid the language.
*  Right implies a kind of feed forward thing where we're moving up, maybe it's an anatomic
*  hierarchy, but that somehow maps on to, and despite his dissing of Dennett there, I think
*  I think that basic Dennettian point is right.
*  That the notion that our psychological categories and our way of breaking up psychological
*  function should map in a really neat, direct way to the anatomical regularities, it was
*  a red herring from the beginning and we should have noticed it.
*  That that isomorphism is a red herring?
*  That isomorphism thing.
*  That's what I take from Dennett there.
*  So there's no moving up the hierarchy
*  because first of all, and this is where this is already oversimplified, right?
*  And we get into the reflex arc phenomenon, right?
*  It's not like there's a thing that happens.
*  Right.
*  And then it moves up a hierarchy.
*  That's what happens in neural networks.
*  In isolation.
*  That's one of the dangers of neural nets as a model for the brain because that is exactly
*  what happens in neural nets.
*  There's a thing that happens that's presented to the input nodes and then a bunch of things
*  happen along the way going up a hierarchy often, a real hierarchy.
*  And there's real abstraction because you get features and then higher level mathematical
*  representations of those things.
*  And then you turn the computer off.
*  Yeah.
*  To use that same kind of viewpoint in talking about the brain is I think fundamentally misleading.
*  Because first of all, there's ongoing activity.
*  And not just ongoing activity of the organism.
*  Even if you throw somebody in a scanner and they can't do anything else but sit there
*  and look at whatever you're showing them.
*  There's background activation.
*  There's just the natural oscillatory frequencies of various parts of the brain.
*  So there's no walking up a hierarchy as if that's all that happens.
*  There's stuff going on already that modulates anything that's coming in.
*  And certainly in naturalistic scenarios, there's ongoing activity that's affecting
*  what happened.
*  This is what's right about the multiple drafts theory, which is otherwise crazy.
*  Daniel Dennett's multiple drafts theory.
*  I'm just doing that to Neil Jeanne right now.
*  There's stuff going on all the time.
*  And all that stuff affects the stuff that's the new stuff that's happening.
*  The old stuff is still there and it's exerting its influence.
*  So the notion that there's some kind of strict hierarchy you can identify just seems a mistake.
*  Instead, we've got to understand in the book I say top down, bottom up, side side.
*  And it makes it very hard to study.
*  I do recognize that.
*  This is why you alluded to the appendix of the book.
*  That's why I put the appendix in.
*  I do recognize that the negative part of my work showing, well, that can't be right,
*  that can't be right, that can't be right.
*  You can't just leave it there.
*  You've got to say, okay, what do we do instead?
*  And among the things we do instead is look at dynamics.
*  We look at dynamics directly.
*  We get rid of this whole notion that there can be isolable stimuli or pure tasks.
*  And we look at the modulatory effect of ongoing activation, right, along with inputs and outputs,
*  and how all that works together.
*  And we have the mathematical tools to do it.
*  It's hard.
*  It's hard from an experimental standpoint and it's hard from an analytical standpoint.
*  But we have the tools to do it.
*  But it means getting beyond, and it's hard, as you just demonstrated, right?
*  Talking about things like hierarchies and individual inputs that can be isolated and
*  you can follow its processing in any kind of simple way.
*  That's not the successful future of the neurosciences.
*  Is there room though, and sorry that this is an aside,
*  I was talking with John about this also because he considers himself a pluralist, right?
*  So is there room in a pluralistic approach to understanding brains and minds for us to say,
*  yeah, that looks like a hierarchy, fine, but you can also slice it this other way,
*  and you can also slice it this other way.
*  So everything's okay to talk about in that manner and useful in some respect,
*  but maybe it's not that the brain is a hierarchy, a full stop or something like that, right?
*  Is there use in continuing to use terms like hierarchy and representation and so on?
*  So this gets to the question of sort of realism in models.
*  And I don't mean inner mental models.
*  I mean the models that scientists use to study things.
*  Yeah, right.
*  And so absolutely correct that, yeah, look, if I've got a particular purpose,
*  say I want to predict the onset of Alzheimer's,
*  and it turns out that a particular model that makes assumptions about neural hierarchies
*  is really useful in predicting early onset Alzheimer's and maybe allowing us to intervene
*  at a point in the process that allows better say clinical outcomes
*  than is typically possible, then heck yeah, I mean do that, right?
*  But then don't make the follow-on assumption that you've thereby discovered something fundamental
*  about the architecture of the brain that can be generalized to tell a story about the whole thing.
*  And so if you're a pluralist, then you've really got to resist that latter step,
*  and that latter step proves to be hard to resist if you look at the literature, right?
*  There's this just very recent kerfuffle over this cool paper about zebrafish reflexes and
*  how they're innate and people extrapolating from that, right, to, you know, ah, well this means that
*  in fact there's genetically specified behavioral circuits across, it's like no, it doesn't mean
*  that. It's like yeah, that's cool, and it's important for the survival of this particular
*  species in its ecological niche, right? This is why giraffes, the baby giraffes can walk within
*  whatever a few hours, you know, that's not learned, that's built in and dang well better be because
*  there are lions on that Serengeti and if they can't be mobile quite quick, right, they're not going
*  to survive that. So I would say I'm a pluralist as well, but then if you're a pluralist, I think you
*  also have to be an anti-realist or at least a mild anti-realist. Okay, mild, I'll accept mild there
*  because I think there is room for realism in, well, oh man, now I'm gonna have to play you
*  the second guest question and we haven't fully gone through. You know what, I'm just gonna go
*  ahead and do it because this is getting into, you know, realism and what the world is really like, so
*  okay, if you don't mind, this one also, it's about a minute and a half or so. This is from Alex Gomez
*  Marin and I'll just play it here. It's about, well, I'll just play it. Hello Michael and hello Paul
*  again. I'm Alex Gomez Marin from the Instituto de Neurociencia de Alicante, STAIN, and thank you
*  for asking me to contribute with a question or is it a comment? Okay, so here it goes. Michael,
*  your work is really a garden of stimulating reflections as you have engaged in deep
*  discussions about the future of psychology, its problematic taxonomies, the evolution of the brain,
*  the pitfalls of the stimulus response paradigm, plea for radical embodied cognitive neuroscience,
*  etc., etc. And generally speaking, I agree with virtually all of those, but I wonder, and this is
*  the question, what is your metaphysics? Namely, could you make explicit the philosophical commitments
*  underlying your scientific thinking? For instance, some are proud physicalists and there are others
*  who are crypto-dualists and currently there's a revival of panpsychism and also of idealism
*  and many neuroscientists still believe that one can do science without adopting, consciously or not,
*  any philosophical doctrine. So I'm very curious to know yours, especially given the fact that I'm
*  currently undergoing a kind of 4E crisis, since even when one puts the brain back in the body,
*  acting in the world, it seems to me that materialism, broadly construed, still remains a desperate
*  attempt to understand that four-letter word we call the mind. So thank you and sorry for this
*  rather abstract question. Warm regards from Sami Alicante. Bye bye.
*  RG See, he used his hierarchical brain processing to ask an abstract question. There you go.
*  Is this going to derail us too much, you think?
*  SRS I'm not sure I'm going to have a satisfying answer and I'll tell you in part why. This is
*  something that I'm working on. I've really largely either completely avoided the question of
*  consciousness or talked about a really deflationary view, right? So kind of the sub-personal,
*  you know, basically what Charmell Holmers calls the easy problems. I have a little piece on self-awareness,
*  but it's clearly an easy problem approach to that question. I'm pretty sure I'm not a dualist.
*  RG Are you a realist? The realism thing set me off to play that question.
*  SRS I am a realist, absolutely. I think direct perception leads straight to kind of scientific
*  realism. I'm a big fan of Ian Hacking and his representing and intervening. Even way back in
*  my dissertation, which getting back to the original question is sort of the pre-embodied
*  cognition and body cognition view of things. The fact that we're situated in the world in a way
*  that we are within the causal nexus of that world and can intervene in that world is one
*  of the important resources we have for getting realistic knowledge of that world. So I'm definitely
*  in the realist camp. I don't think, I'm not a realist because I believe we have accurate models.
*  I'm a realist because we have the capacity for successful intervention. RG Control and intervention.
*  SRS Control and intervention. And that's the hacking line on scientific realism. And I adopt that.
*  The question of what is the mind, and I take that to be an allied question about
*  consciousness and experience, and how do we fit those things into a physicalist view.
*  I don't have settled answers to that. I mean, these are important questions, so I don't want
*  to be dismissive of the question at all. But I don't myself have settled answers to that question.
*  I'm once attracted to say, Varela and Thompson's inactivism on this, but they can kind of shade
*  into idealism in various ways. I mean, there's a slope there that they're trying to avoid sliding
*  down and it's not clear that they can. On the other side of the coin, I'm attracted to kind of
*  Jamesian radical empiricism. But as I argued even back in my dissertation, same kind of slippery
*  slope there. So there's something precarious about this and that's fine. I mean, again, I said the
*  word mystery before. I'll repeat it here. There's an important mystery here. And it's a mystery that
*  should interest not just philosophers, but any intellectual and maybe scientists who work on the
*  brain especially. And so I'm attracted to James' notion that the mind is a kind of selection process.
*  I mean, that the nature of the mind is in its selectivity.
*  Conscious mind. You're conflating consciousness in mind right now.
*  It's hard to understand and it's even harder to articulate.
*  James builds an experience from the get-go. And he tries to build it in from the get-go
*  while rejecting both the doctrine of ideas from Locke and so on. And also the kind of Kantian
*  notion of sensory intuitions. So he wants to both get rid of empiricism and idealism
*  in its various incarnations, but nevertheless without getting rid of experience.
*  And I don't understand that view yet. I can say I'm attracted to that view. And that's
*  if I had to pin myself to a metaphysics right at the moment for Alex, that's where I pin myself
*  and see how it came out. But I don't have a way of articulating that yet. And I mentioned to you
*  that I think it was before we recorded. So I'll just say it now. I think the title of my next book
*  or one of my next books is going to be Jamesian Neuroscience. And clearly a lot of that has to do
*  with things we've already talked about. Rejection of the stimulus, the reflex arc concept,
*  the rejection of the notion that there's an adoption of a stream of consciousness
*  versus the notion that there are states of consciousness.
*  Oh yeah. The word state is really, I've come to really, it rubs me the wrong way,
*  the word state in terms of anything having to do with brain or mind.
*  Yeah. Yeah, yeah. So we've got to have, we've got to talk about processes over states.
*  All that has to be worked out. But if I were going to jump on somebody's ship,
*  that would be the one I'd jump on. And we'll see where that leads.
*  But yeah, no, it's an important question.
*  And is it important? I'm sorry to interrupt, but I mean, is it necessarily important?
*  Does it? It's humanistically important.
*  Scientifically, is it important?
*  Well, I think so because the notion might be that, well, certainly aspects of it are clearly
*  scientifically important. So if you think you can isolate states of consciousness, this is what the
*  structuralists, Tichenor and Wundt and these guys, if you think you can isolate states of consciousness,
*  then the way you design experiments is going to be very different than if you're a Jamesian.
*  And you think it's just this, right, the stream of consciousness. And that once you scoop something
*  out of that stream, it's no longer part of the stream. And it's a different thing. Right? So
*  studying this bucket of the stream is just a very different enterprise than trying to get a handle
*  on the stream itself. So do you think that the stimulus response approach to neuroscience has
*  dominated over the past, I don't know, 80, 100, however many decades? Do you think that's been
*  one of the biggest misleading approaches, mistakes scientifically?
*  So I want to resist calling any development in the history of science a mistake.
*  Okay.
*  Because everything that we do leads somewhere.
*  Right. But maybe less efficiently. Some roads are more efficient than others, perhaps.
*  But there's no way to know that. Right? And so in this context, I want to reserve the word
*  mistake for things you should have known better.
*  Okay. But if your metaphysics was right from the beginning, right, then maybe you should have known
*  better. The history could have been different. Yeah. Okay.
*  Right. And there certainly were resources throughout the entire history to have taken
*  a different path. But look, excuse me. I don't think that, and this is back to the word mistake,
*  the other thing, the notion that we didn't learn anything.
*  I didn't say that.
*  Well, but I want to reject that too. I mean, I think we learned a great deal.
*  And my own view is that one of the things we learned is that the assumptions under which we
*  gathered the data undermine the assumptions, that the data undermine the assumptions. And so
*  now we know we need to do something different. I was just going to say, did we need to wait
*  this long or was the evidence in, was enough evidence already in a few decades ago?
*  I mean, will you forgive me if I throw Coon at you right now?
*  Well, I was going to bring up Coon. So please throw Coon at me. Yeah.
*  I mean, just that's...
*  I don't think it was Coon who said this. It might've been Ernest McMullen, one of my old teachers.
*  It's just Thomas Coon that we're referring to who wrote the Structure of Scientific Revolutions.
*  And I was going to ask you about paradigm changes and if you think we're on the cusp of one. But
*  anyway, that might not have been what you were going to throw at me.
*  No, what I was going to suggest... So I can't remember who said it to me. Well,
*  I think it was Ernest McMullen who said it to me. I don't know if he coined this
*  phrase or not. He may have gotten it from somewhere else. But he said that if we actually look at the
*  history of the Copernican Revolution, and this is back to Coon now, right? So I think you just
*  mentioned Structure of Scientific Revolutions. His earlier book was An Analysis of the Copernican
*  Revolution. And now we look at the church's persecution of Galileo for adopted Copernican
*  views. What he said, and he was a priest by the way, what he said was,
*  well, the church was morally wrong to have persecuted Galileo. But epistemologically,
*  they were probably right. In the sense that at that stage, there really wasn't enough evidence
*  to compel anyone to adopt the Copernican over the Talmayan view of the universe.
*  And so there's a very hard question that people spent, obviously, the whole logical positivist
*  movement was about this. What is it when something is confirmed or disconfirmed?
*  Right? This is an impossible question to answer in a definitive way. Like when is there enough
*  evidence? How does that work? And so now you get back to Coon and his claim is that, yeah,
*  that's the wrong question to ask. There's no point at which the evidence has accumulated sufficiently
*  to make it rational to do one thing rather than another. There's always a rational way
*  to continue within the same framework by elaborating the framework. And you can't say
*  it's an epistemic or rational mistake to elaborate the framework rather than jumping to a new or
*  developing a new framework. That's a decision that's made not based strictly on evidence,
*  but based on other considerations. Some of them are a simple, but very simple decision.
*  Considerations. Some of them are aesthetic. Some of them are, you know, some of them, frankly,
*  are personal. They're maybe ambition based or whatnot. And so the reason I bring Coon up here
*  is to your question. There's no point in the recent history of the neurosciences that you could say,
*  ah, here in 2001, we had sufficient evidence to reject X or Y. That's not how it works.
*  There's always evidence that supports. There are always anomalies, things that don't quite fit,
*  but you can kind of squint at them and make them kind of, well, okay, maybe that was just noise or
*  maybe we need to tweak our model a little bit to capture that. And, you know, it's, I won't say
*  never, but it's the rare case where it's irrational to make one choice over the other. And so the way
*  that science progresses is not that way. It's not some kind of accumulation of evidence that other
*  than you say, oh, yeah, we nailed it or oops, no, we've got to reject this and move to something
*  else. It's that people come along and say, you know what, I don't know why, but that just,
*  that doesn't make sense to me. Is there a different way of looking at it? And then,
*  you know, Gibson, you know, since we brought him up already, that's, you know, he was a traditional
*  visual scientist for a long time, but he started noticing, you know, that his participants in his
*  experiments, which were highly constrained, right? You know, this is how you did psychophysics back
*  in the day in visual psychophysics, right? You put people in an ophthalmoscope, you know, with a
*  bite bar, so they're fixed. You have them focus on a distant fixation point, so they're not
*  saccading or anything. And then you show things to them and you have them interpret whatever you do.
*  And then you start with the, well, they weren't perceiving, they were having hallucinations. And
*  right. So what he came to decide, what he came to realize, I would say, is that that setup had
*  actually destroyed the phenomenon of visual perception by oversimplifying it to the point
*  where vision was no longer what was happening. It's completely out of context for the organismic
*  behavior. Yeah. And so he said, okay, well, then what do we need? And this is back to the very
*  beginning here, right? Like, okay, then what are the assumptions about the organism and the environment
*  that make this a nonsense thing to do? That then replace the prevailing view of what's going on in
*  visual perception, which is that you start with these low-level features that you slowly build up
*  into more and more complex pictures of the world. And so what you need to do to study vision is
*  isolate the low-level features, right? And learn how those get processed and then go to more complex
*  things and whatever. But that's the hierarchical view. He just said, no, that framework is
*  mistaken. So we need a new one. And he set about creating a new one. And so I think that's the
*  position we're in now in neuroscience, right? We've been operating under a particular kind of
*  structuralist assumption where we get individually, we initially are receptive to
*  features, very simple features. We build those features up into models of the world. We test
*  those models in various ways through behavior. Again, that leads to all the kind of notions of
*  uncertainty and potential skepticism, like how do we know our models actually fit the world and blah.
*  And in the neurosciences in particular, then we've got a vision of the brain that is oriented
*  towards that. We've got feature processors in the brain, and then we've got things that do
*  conjunctions for us and so on. And then we get object files. I'm now channeling Triesman here.
*  Then we get up to object files, and then the object files end up into concepts in some way,
*  and so on and so forth. And again, the kind of straightforward general new model, straightforward
*  statistical dependence between aspects of the task or the stimulus and activity in the brain.
*  That's a sufficient way to think about it. But I think we're at the point that Gibson hit in
*  visual science, which is now actually we've oversimplified things. That's not how the brain
*  works. We did a different kind of experiment, and we need a different model that sort of better
*  matches the more sophisticated methods that we have. But it sounds like you are comfortable
*  with the current quote unquote, Kuhnian paradigm in neuroscience, comfortable working alongside it
*  without shaking your finger at it and saying, you're doing it wrong, and I'm doing it right,
*  and my paradigm will come through one day, soon I hope. And I don't know if we were talking about
*  this before I hit record, but because After Phenology was 2014, which is now eight years
*  ago, and it's based on all the work that you've done before, but you're still optimistic. I wanted
*  to get your viewpoint on the current paradigm in neuroscience and reflecting on how your ideas or
*  your approach has been accepted and or rejected, how you felt you have fit as the years have gone
*  by. That's a lot to throw at you there. But. So the first neural reuse stuff that appeared in print
*  was like 2006, 2007, something like that. So it's been a while. Yeah, so 16 was my math. Yeah, 16
*  years. And when I started this, I had more of the attitude that you caricatured there,
*  which is I've discovered something that's really important. You all are wrong.
*  And I quickly discovered that was a dumb way to go about things. Okay.
*  Because it implied and I didn't think it through, but it implied and this is back. This is why I
*  reacted the way I did to your word mistake. Mistake. Yeah. Because and I didn't mean to be
*  implying this, but I recognize now that I was that the work that had been done up till that moment
*  was a mistake that was somehow not valuable. And I actually gave a talk in New York and had a very
*  prominent neuroscientist pull me aside after the talk, quite upset with me. Can't name drop again.
*  Okay. And I was very upset. I was very upset. I was very upset. I was very upset. I was very
*  upset. Okay. And she says, I'm really upset about the way you presented that.
*  My grad students are now wondering whether what they're doing is worth it.
*  How dare you upset Ann Treisman like that? Not her.
*  Okay. And my first reaction to that was, that's not science. You can question my data and methods
*  or whatever, but you can't accuse me of emotional abuse. But upon reflection, I think she was
*  probably right. And here's why. Because in fact, the discoveries I've made, let's assume they're
*  discoveries, those discoveries I've made were based on other people's work.
*  Yeah, of course. Other people's mistakes. That's super valuable. What I did was impossible
*  without that work. Right? Yeah. So was it a mistake? Well, I think the assumptions under which
*  those data were gathered is flawed. But we can use the very same data to heal the assumptions,
*  to move the assumptions to a better place. So was it a mistake? No. Are they wasting their time
*  doing it? No. Do they need to reflect in a bit more concerted way on what the assumptions under
*  which they've been gathering their data and maybe they want to change some of them or tweak some of
*  them or do something different? Definitely. Right? And so I pushed on the straightforward empirical
*  stuff for a long time. And then the book is really my attempt to then fill in, at least partially
*  fill in the conceptual background that makes sense of the anomalies. Because the analyses I did on
*  their data revealed that actually the data they gathered were full of anomalous information
*  from the standpoint of their framework. And so, right, I don't know if reuse is a paradigm shift
*  or what paradigm is itself a fraught word. But it does point to the need for a new framework
*  within which data that have been gathered should be interpreted. And that should lead to
*  particular ways of gathering and analyzing data in the future.
*  And so, yeah, the reality is that these enterprises have to be going on in parallel,
*  right, both for practical and even epistemic reasons. Like why would I, I mentioned Alzheimer's
*  earlier, why do I derail anybody's Alzheimer's research? Right. That's just, you know, there
*  are ways, there are things, why would I derail anybody's work in molecular neuroscience?
*  No. In these cases, maybe, you know, the prevailing assumptions about brain structure,
*  actually, or functional structure, aren't really relevant to the importance of that work.
*  Right. But you're talking about people who would want to connect molecular biology to mind or
*  something, right? That's too far a leap. Is that what you're hinting at with that? And their
*  target of explanation is not mind, for example. Yeah. Yeah. Yeah. And so,
*  and with those folks, you know, I'll name drop here, John Bickel, because I know he can handle it.
*  You know, his way of doing kind of direct connections from molecular mechanisms to
*  mental phenomena. I mean, the data are interesting, right? But the framework
*  within which he's operating, I think, is mistaken, not because, and his data don't show that,
*  right, and the stuff he does with Antonio Silva, in particular, his data don't show that it's
*  mistaken. That's really interesting work. But, you know, especially if you're a philosopher of
*  neuroscience, or a theoretical neuroscience of a particular stripe, you don't have the excuse of
*  saying, well, look, I just care about how this neural transcription factor works in this particular
*  circuit. Right. Right. And that's fine. That's great. It's important. And it's going to lead to,
*  you know, really important insights. But if you're not in that kind of camp,
*  we're not involved. We're involved in a giant game of inference to the best explanation.
*  Right. And that means you've got to pull in evidence from all kinds of places, and try to
*  fit it all together. That's why that book is so freaking long. And the longest part is the
*  bibliography. Yeah, well, I think the language chapter might be a little, we're going to come
*  back to that. That might be the longest chapter. But actually, if you bring it into parts, I've
*  got a copy over there. No, actually, I must have given it to somebody. But I think if you've just
*  made it into parts and take the bibliography as a part, I think the bibliography is the longest,
*  because I felt it, I had to gather information, gather evidence from as many places as I was
*  competent to interpret, and then try to fit that into a picture.
*  Let's go back to the very, very beginning of our conversation then, because I think that we've
*  sort of ratcheted to various topics. But early on when you were formulating these ideas, and I was
*  asking, was it the data that was showing you the way, some first principles, just a rethinking?
*  Did you just have a hunch that the current state of affairs in neuroscience was on a less efficient
*  track? No, it was a genuine moment of eureka or aha. Or as, shoot, I forget who said this,
*  someone who watches the podcast will know and will put it in the comments or something.
*  But the quote is, the most productive words in science are not eureka. I have found it, but
*  that's weird. Isn't that Einstein or isn't it attributed to Einstein?
*  Everything's attributed to Einstein. I always mistrust things attributed to Einstein or FDR.
*  William James. Let's say it was William James. Why not?
*  Yeah, it wasn't. But it doesn't matter who it was. So it was that kind of moment.
*  So I'll tell you how it worked out. So I mentioned embodied cognition. We went on a tangent
*  on that as a result of me mentioning that phrase. And so I was a postdoc in AI at the time.
*  And I was doing this side project on embodied cognition and in particular on the neural basis
*  of embodied cognition. And so I was very influenced by Larry Barsalu and Alex Martin.
*  And I said, okay, well, I've gathered up a bunch of neuroimaging data. I have these AI techniques
*  I can use to do pattern recognition and analysis and things like this. So they claim that as a
*  generalizable principle, higher order cognitive functions like language and planning, things
*  like this are built on lower level sensory motor circuits. So I said, okay, well, so they have
*  their individual experiments that show this. Can we see if this is true more generally?
*  And so I put together, I forget how big my database was at the time, but I basically put
*  together a database of neuroimaging experiments. And I did some pattern analysis where I looked
*  at what I classified as higher level functions and lower level. And yeah, if you look at things
*  that way, yeah, indeed, they're right. It's generally the case that higher level functions,
*  mathematics, language stuff, planning, things like that, they're using, they're built on
*  the circuits that are also involved in sensory motor kinds of functions. Okay, cool.
*  But then I realized, huh, what I'm actually engaged in is a kind of confirmation bias,
*  right? Because all I'm doing is looking for evidence for the claim.
*  You weren't trying to falsify anything.
*  I wasn't trying to falsify it. So I said, okay, well, then, let's look for the reverse.
*  Because the reverse all sure shouldn't be true, right, on this model. And guess what?
*  If you look for the reverse, you find that too. And then I was like, well, that's weird.
*  And so then now you start just kind of looking. And that's where NeuroReuse was born.
*  Because one possible conclusion from this sort of analysis, well, everything depends on everything.
*  So let's just go back to Lashley. But that's not what you observe if you actually dive into the
*  data. What you observe is all the stuff I've reported over the years, which is that,
*  you know, well, the base finding is indeed that every bit of the brain is involved in lots of
*  different stuff. Okay, so that's consistent with the embodied view, but it's not the same
*  as the claim they're making. And then you say, and again, it's not just everything depends on
*  everything in some kind of mush. No, there are patterns. So newer cognitive functions,
*  language, mathematics, whatever, rely on more and more widely spread brain areas
*  than older ones, which are more local. Not response inhibition, because that's a pretty
*  low level. And response inhibition uses a lot of different or I'll confess, I've not investigated
*  that in particular. So I thought in one of your plots, you showed that it was response inhibition
*  in particular was one of the test cases where there were lots and lots of different, it relied
*  on lots and lots of different areas. That's in the taxonomy stuff. That's a whole different
*  analytic technique. And that's not a new thing. Sorry to derail you there. No, no, that's an
*  interesting discovery as well, I think that leads to a particular view of how what happens when these
*  brain regions interact. But that's a different point. Yeah, but you're saying that the more
*  recently evolved cognitive functions as far as we can tell, rely on lots more or things that
*  develop later, or things that develop. Evo Devo is hard to disentangle with the data. Right. Oh.
*  So and you find that, you know, older, older, if you can identify them, you know, evolutionary
*  brain regions are involved in more things than newer brain regions. And both of those point to
*  the reuse architecture, right? That what's happening in the brain is not a matter of
*  sculpting regions to serve particular individual functions or behavioral outcomes. Instead, it's a
*  matter of putting the pieces together in the right configuration. And the later something comes on
*  line, the more potentially useful stuff there is in the brain, and no particular reason it should
*  be in one spot, so localized. And so this is the basic picture of reuse, that it's functional
*  cooperation. That's where the game is, and not localization. Is that hard to accept? That seems
*  like a straightforward, acceptable story that wouldn't, I mean, has the neuroscience community
*  just kind of accepted that? Or is there pushback on the neural reuse part of the story? Because,
*  you know, like I said, there's a bunch of different moving parts. This is hard to say. I mean,
*  certainly the neuroscience community has fully embraced network thinking. Yeah. Yeah. Right.
*  Yep. But as an example that we began with, even though they're doing things at the level of
*  networks, and even dynamic networks, they really want to fall back on interpreting the nodes.
*  Right. So there's some kind of stickiness, right? A hysteresis in the system that, right,
*  there's a momentum behind that way of understanding things. Not me. I'm free of all of that, as you've
*  witnessed. No doubt. Yeah. Amazing. Anyway, just the last one you're finding. So then, you know,
*  so that's what that implies, right? That the action is at the level of network configuration,
*  and changing network configurations. Then if you go looking for that, yeah, you can find it, you
*  know, like the same node. So, you know, in the kind of standard talk I'll give on this stuff,
*  you know, you pick a node in this particular case, it's leftangular, I think, it doesn't matter what
*  it is. Anyway, and you say, okay, here's a node. Now it's involved in emotion tasks, involved in
*  language tasks, involved in attention tasks, involved in, right, so on. Well, guess what?
*  It has different partners in every one of those cases. So that same node is involved in all these
*  different, you know, cognitive functions, cognitive capacities, but it's got different partners in
*  each. And that's the story to me. And that's where I think, and it's, I think that particular point,
*  both methodologically and conceptually has yet to really be picked up in any significant way
*  in neuroscience. So networks, yeah. But you know, getting back to hierarchy, hierarchy is still
*  very much part of the notion, whereas I think if you've got shared nodes between these various
*  networks, which you demonstrably do, at least demonstrably based on the data we have,
*  it can't be hierarchical in a strict way. It's got to be hierarchical,
*  right? Because each bit can be a member of multiple different networks.
*  Soterios Johnson But you could talk about functional
*  hierarchies within that domain, right? If you really wanted to.
*  Mark Sperling Right. So this is, you know, you said a lot of moving parts, and this is where
*  things get a little bit delicate, right? So yeah, if you want to fix the behavioral or experimental
*  context and take a snapshot of things, okay, what's this configuration like
*  for this purpose at this moment? Yeah, you may well be able to discover, by the way,
*  I would love for people to do this. And maybe someone has, I mean, the literature is so vast,
*  it's impossible to track it all. But so entirely possible someone has done this. But yeah, so
*  if you take a snapshot of a network in a particular context and hold all that fixed,
*  and then you want to describe that network, yeah, I wouldn't be surprised to discover that there's
*  a discernible hierarchy there. Soterios Johnson
*  But it's a ghost, you would say, within the larger context of other functions and...
*  Mark Sperling It's transient, if that's what you mean by ghost.
*  Soterios Johnson Sure. Yeah. That works. That's better.
*  Yeah, I would say it's transient. And hopefully repeatable, right? Because we are able to return
*  to behavioral context and elicit similar behaviors. So this is what this acronym I came up with for the
*  book Talens, right? Transiently assembled local neural subsystems. And that's the idea that and
*  I should have, but I couldn't fit R in that Tarland's or something. But repeatable is also
*  important. Mark Sperling
*  But not perseverational, perhaps. I'm just thinking in terms of like when we perseverate,
*  we're going back to those same patterns and we're not as plastic as we think we are. Maybe we'll
*  come back to that. Was there more to what you were saying about the neural reuse aspect?
*  Soterios Johnson No, I mean, those are the, again, so it came out of trying not to engage in
*  confirmation bias. And then the patterns that emerged were the things that I've just suggested.
*  And then that's okay, that's cool. And then you continue to develop both analytical and conceptual
*  tools to probe that. So the functional fingerprinting stuff that I did with Luis Pessoa
*  and Josh Kinnison was part of that story. Like, okay, so we have this qualitative measure that
*  individual bits of the brain respond under various circumstances. Can we quantify that?
*  Can we actually do, and yes, in kidney we can, right? You basically turn every part of the brain
*  into a functional vector and then you can quantify its diversity and you can look at
*  the ways in which these things, how that affects, say, the assortative characteristics of that node.
*  And yeah, so we've got that paper in our image that kind of details all that, showing,
*  and an important thing that came out of that conceptually is,
*  well, so you don't need to identify the function of a particular region of the brain to do good
*  neuroscientific work with an ROI. You can say, ah, well, here's its vector, right? Here's its
*  activity budget, right? This is the set of functional characteristics. And yeah, I suppose
*  you could say, oh, well, that must mean it's an X. But the only kinds of things that people have
*  come up with, I'm thinking of Price and Friston now in particular, because they confront this
*  problem, is you get these very general things. Well, it's just an integrator.
*  Yeah, okay. You've got to give it a name, right?
*  Or it's, you know, this is a, you can only come up with these really generic ascriptions.
*  And that's because when you look at the functional profiles of most regions of the brain,
*  it's really freaking complex. And it's hard to say that it only does one thing. And I used to
*  think that, like earlier work, I said, well, okay, let's imagine it does one thing, but that one
*  thing is abstract in a particular kind of way, or it's, you know, I was a programmer before I
*  became a professor. And, you know, so maybe it's like object oriented programming. Reach of these
*  things is a little object. And it provides a service. And that service can be useful under
*  multiple different, in multiple different programs. So maybe it's like that. And that was the first
*  model for reuse. And I've since given that up, because I just think it's more interesting and
*  more complicated than that. And I think this is back to your, the thing you brought up earlier,
*  response inhibition. And so, and actually, the better example is, is attention, but it doesn't
*  matter. The idea is that say the attention specific network, let's assume it's attention specific,
*  when you look at the nodes of the network, none of those nodes are actually attention specific.
*  So somehow, it's the collection of the configuration emerges out of that configuration.
*  Oh, man, you just said it. Each individual bit does a specialized thing. What I want to say instead,
*  is that there's mutual constraint between the nodes. And that mutual constraint selects out
*  one of the functional possibilities of each of the nodes in the service of achieving whatever
*  the behavioral or cognitive function is that that network subserves. And that's what you mean by
*  emergent. You don't mean a spooky property of- No, I mean, something that,
*  and I'm trying to think of a word other than emergent.
*  You could say emergent property. You could, that kind of takes some of the flame out of it,
*  I suppose. I don't know. Yeah, who knows. But whatever. But no, that's just say, the
*  the transient specificity of that network is a function of the way the constraints
*  operate between the nodes. So each of the nodes is multifunctional in an important way.
*  But when it's in a network formed for a particular purpose, behaviorally speaking,
*  then each of those nodes is constrained by its participation in that network to only express
*  some subset or one instance of its functional possibilities.
*  That sentence, by the way, that implies a very different neuroscience than the one we're doing
*  right now. It does. And so you originally, you know, we're thinking of like an abstract way to
*  talk about brain area X, right, in this domain. But then it struck me, do we need to just give up
*  language and ontological terms and start talking about coordinates in a high dimensional functional
*  cognitive space? Because that's less satisfying than to be able to, or do we just need to stop
*  talking about brain area X and start talking more about configurations?
*  Well, what's the way forward is my question, you know, like how to discuss these things.
*  Right. So on the first question, do we need to stop, you know, bringing in
*  psychology talk? You said language. That's too strong.
*  But look, you know, in work I've done, I think we've shown that you can actually do interesting
*  science without bringing psychology talk into it. And just talking about the location of,
*  you know, networks and or nodes of networks in a high dimensional functional space.
*  Now you've still got to characterize the dimensions, I think. But that puts things at
*  sort of one step removed, right, from the typical way of doing an experiment where you think you're
*  directly testing, you know, response inhibition, something you mentioned already, or work in memory
*  or something like this. So, yeah, you can do, as it were, work that's sort of maybe merely
*  predictive. So back to the Alzheimer's example, maybe it's the case that, or epilepsy, something
*  I've actually published one thing on, is, well, what if you were able to track
*  the way a particular region or a set of regions moved, given its activity, in a big high level
*  functional space? And what if it turned out that when it enters this region of that functional
*  space, that's a danger signal?
*  Psychotic break or something.
*  Yeah, or impending epileptic seizure.
*  Seizure, sure, yeah, whatever it is.
*  Right. Well, now you haven't had to use psychology talk at all. Right, you're just doing it in a
*  high level mathematical model. You're tracing these things over behavioral time. And when it
*  enters a particular region of that space, that's meaningful in a particular way. So it's merely
*  predictive. It's probably not explanatory. And there's room in the world for merely predictive
*  sciences.
*  But it's somewhat unsatisfying.
*  Yeah, of course. So that's the second half of your question.
*  I do think that the computer metaphor-inspired vocabulary that we tend to use is likely going
*  to have to be superseded by something else. And so it's just not likely to me, for all kinds of
*  reasons, that even assuming, let's just stick with this high dimensional notion, right? I
*  talk about neural personalities, right, in the book. Right, where what we're not trying to do is
*  say, well, this is the function of that thing. Instead, there's a set of tendencies that this
*  region has.
*  Dispositions, yeah.
*  Yeah, it's got a set of dispositions. Now, either for the individual dispositions or for
*  the high level characterization of the dimensions of that space, we are probably going to want a
*  vocabulary and one that is going to lead us to some kind of satisfying explanation of how all
*  this works. I don't think that the computational metaphor is going to provide that vocabulary for
*  us. For all kinds of reasons, I think it's probably fundamentally mistaken, even just
*  from a evolutionary standpoint, the notion that that's the sort of thing that would have evolved
*  is a computer of a particular kind. I can't deny that it's been fruitful, right?
*  So useful, yeah.
*  It's been driving cognitive psychology, cognitive neuroscience, and other subfields since 1950.
*  But it's also not clear to me that it's... Well, these are useful models, right back to the
*  pluralist question. But it's not clear to me that they're explanatory in a strong sense, just because
*  the trouble with computational modeling is it's too powerful.
*  What do you mean?
*  It's totally unconstrained. I can model anything.
*  Oh, yeah, right. Given enough compute and data, et cetera.
*  Yeah. Giving enough data, given enough
*  parts, given enough, right? I can model anything. This is another, the embodied cognition folks,
*  one of the ways that they get pushed back on is exactly this. Well, sure, of course, the body is
*  important. I can just throw it into my model. It's like, yes, yes, you can. Yes, you can.
*  And you can just model... I don't know if you saw that interesting octopus paper that came out some
*  time ago talking about the decentralized control of octopus tentacles and...
*  Each tentacle has its own mind, right?
*  Each tentacle has its own mind, but also it imposes its own constraints on its own movement
*  as a way to do dimensional reduction. And so the idea was this is supposed to be an example,
*  an exemplar of fully embodied kinds of cognition because the computations, if that's what you want
*  to use that word, it's doing or not with neurons, it's with the body itself.
*  Right. As a constraint.
*  People came along and said, well, I can just model that.
*  Right? I'll just throw that into it. And it's like, yeah, yes, you can.
*  That sucks, but you can.
*  Well, that doesn't suck. That to me is, that's a clue that that framework is not actually a theory.
*  It's a tool.
*  It's just a set of tools. And people often take it to be a theory of the brain,
*  but it's not. It's a set of tools that can be used to understand the brain that wants a theory.
*  It's also a metaphor and it's been, like you just mentioned, a powerful metaphor.
*  Yeah, absolutely. Powerful and fruitful. But it's not a theory of brain function. It's not a theory
*  of mental function. It's a set of tools that you can use to model it. And you need to constrain
*  that modeling with a theory to figure out how you put those models together. And that's the step that
*  has not typically occurred. The notion that you can use, say, I can throw that into my model
*  somehow undermines any particular theoretical approach to the brain is a mistake. That's not
*  how that works. Even though it's largely taken to be a good argument against certain ways of going,
*  oh, I can just throw that in my model. It's like, okay, but that's because your model is
*  unconstrained by a theory. Man, there was so much that I still wanted to ask you, but I really
*  enjoyed the conversation. I really enjoyed the book and just reading your more recent works as well.
*  So thanks, Michael, for coming on. And I just appreciate what you do and good luck with your
*  paradigm shifting work. Well, we'll see. As Kuhn will be the first to point out, no individual
*  author or even group can be responsible for that shift. That shift is an historical phenomenon
*  that occurs or doesn't, depending on lots of factors. Here's another quote. I don't know.
*  It's not really a quote, but who said that paradigms shifts happen when the old people die?
*  So I think the quote you're referring to, and I also don't know who it is, is that science progresses
*  one death, one funeral at a time. One funeral at a time, yeah. One generational funeral.
*  Yeah. Okay. Anyway, thanks a lot, Michael. Thank you. This has been great.
*  I alone produce Brain Inspired. If you value this podcast, consider supporting it through Patreon
*  to access full versions of all the episodes and to join our Discord community. Or if you want
*  to learn more about the intersection of neuroscience and AI, consider signing up for my online course,
*  Neuro AI, The Quest to Explain Intelligence. Go to braininspired.co to learn more. To get in touch
*  with me, email paul at braininspired.co. You're hearing music by the new year.
*  Find them at thenewyear.net. Thank you. Thank you for your support. See you next time.
*  Bye.

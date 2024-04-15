---
Date Generated: April 13, 2024
Transcription Model: whisper medium 20231117
Length: 6756s
Video Keywords: ['scott aaronson', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 150721
Video Rating: None
---

# Scott Aaronson: Computational Complexity and Consciousness | Lex Fridman Podcast #130
**Lex Fridman:** [October 11, 2020](https://www.youtube.com/watch?v=nAMjv0NAESM)
*  The following is a conversation with Scott Aaronson, his second time on the podcast.
*  He is a professor at UT Austin, director of the Quantum Information Center and previously
*  a professor at MIT.
*  Last time we talked about quantum computing, this time we talk about computational complexity,
*  consciousness and theories of everything.
*  I'm recording this intro, as you may be able to tell, in a very strange room in the middle
*  of the night.
*  I'm not really sure how I got here or how I'm going to get out, but Hunter S. Thompson
*  saying I think applies to today and the last few days and actually the last couple of weeks.
*  Life should not be a journey to the grave with the intention of arriving safely in a
*  pretty and well-preserved body, but rather to skid in broadside in a cloud of smoke,
*  thoroughly used up, totally worn out, and loudly proclaiming, wow, what a ride.
*  So I figured whatever I'm up to here, and yes, lots of wine is involved, I'm going
*  to have to improvise, hence this recording.
*  Okay, quick mention of each sponsor, followed by some thoughts related to the episode.
*  First sponsor is Simply Safe, a home security company I use to monitor and protect my apartment,
*  though of course I'm always prepared with a fallback plan, as a man in this world must
*  always be.
*  Second sponsor is 8 Sleep, a mattress that cools itself, measures heart rate variability,
*  has a nap, and has given me yet another reason to look forward to sleep, including the all
*  important power nap.
*  Third sponsor is ExpressVPN, the VPN I've used for many years to protect my privacy
*  on the internet.
*  Finally, the fourth sponsor is BetterHelp, online therapy when you want to face your
*  demons with a licensed professional, not just by doing David Goggins-like physical challenges
*  like I seem to do on occasion.
*  Please check out these sponsors in the description to get a discount and to support the podcast.
*  As a side note, let me say that this is the second time I recorded a conversation outdoors.
*  The first one was with Stephen Wolfram when it was actually sunny out, in this case it
*  was raining, which is why I found a covered outdoor patio, but I learned a valuable lesson,
*  which is that raindrops can be quite loud on the hard metal surface of a patio cover.
*  I did my best with the audio, I hope it still sounds okay to you.
*  I'm learning, always improving.
*  In fact, as Scott says, if you always win, then you're probably doing something wrong.
*  To be honest, I get pretty upset with myself when I fail, small or big, but I've learned
*  that this feeling is priceless.
*  It can be fuel when channeled into concrete plans of how to improve.
*  So if you enjoy this thing, subscribe on YouTube, review the 5 Stars and Apple Podcast, follow
*  on Spotify, support on Patreon, or connect with me on Twitter at Lex Friedman.
*  And now here's my conversation with Scott Aaronson.
*  Let's start with the most absurd question, but I've read you write some fascinating stuff
*  about it, so let's go there.
*  Are we living in a simulation?
*  What difference does it make, Lex?
*  I mean, I'm serious.
*  What difference?
*  Because if we are living in a simulation, it raises the question, how real does something
*  have to be in simulation for it to be sufficiently immersive for us humans?
*  But I mean, even in principle, how could we ever know if we were in one, right?
*  A perfect simulation by definition is something that's indistinguishable from the real thing.
*  But we didn't say anything about perfect.
*  It could be-
*  No, no, that's right.
*  Well, if it was an imperfect simulation, if we could hack it, find a bug in it, then
*  that would be one thing, right?
*  If this was like the Matrix and there was a way for me to do flying kung fu moves or
*  something by hacking the simulation, well then we would have to cross that bridge when
*  we came to it, wouldn't we?
*  I mean, at that point, it's hard to see the difference between that and just what people
*  would ordinarily refer to as a world with miracles.
*  You know?
*  What about from a different perspective, thinking about the universe as a computation, like
*  a program running at a computer, that's kind of a neighboring concept.
*  It is.
*  It is an interesting and reasonably well-defined question to ask, is the world computable?
*  Does the world satisfy what we would call in CS the church touring thesis?
*  That is, could we take any physical system and simulate it to any desired precision by
*  a touring machine, given the appropriate input data, right?
*  So far, I think the indications are pretty strong that our world does seem to satisfy
*  the church touring thesis.
*  At least if it doesn't, then we haven't yet discovered why not.
*  But now, does that mean that our universe is a simulation?
*  Well, you know, that word seems to suggest that there is some other larger universe in
*  which it is running, right?
*  And the problem there is that if the simulation is perfect, then we're never going to be able
*  to get any direct evidence about that other universe.
*  You know, we will only be able to see the effects of the computation that is running
*  in this universe.
*  Well, let's imagine an analogy.
*  Imagine a PC, a personal computer, a computer.
*  Is it possible with the advent of artificial intelligence for the computer to look outside
*  of itself to see, to understand its creator?
*  I mean, that's a simple is that is that a ridiculous connect?
*  Well, well, well, I mean, with the computers that we actually have, I mean, first of all,
*  we all know that humans have done an imperfect job of, you know, enforcing the abstraction
*  boundaries of computers, right?
*  Like you may try to confine some program to a playpen, but, you know, as soon as there's
*  one memory allocation error in the C program, then the program has gotten out of that playpen
*  and it can do whatever it wants.
*  Right?
*  This is how most hacks work.
*  So viruses and worms and exploits.
*  And, you know, you would have to imagine that an AI would be able to discover something
*  like that.
*  Now, you know, of course, if we could actually discover some exploit of reality itself, then,
*  you know, then this whole, I mean, we then in some sense, we wouldn't have to philosophize
*  about this, right?
*  This would no longer be a metaphysical conversation.
*  Well, this was just.
*  The question is, what would that hack look like?
*  Yeah, well, I have no idea.
*  I mean, Peter Schor, you know, the very famous person in quantum computing, of course, has
*  joked that maybe the reason why we haven't yet integrated general relativity in quantum
*  mechanics is that, you know, the part of the universe that depends on both of them was
*  actually left unspecified.
*  And if we ever tried to do an experiment involving the singularity of a black hole or something
*  like that, then, you know, the universe would just generate an overflow error or something.
*  Right.
*  Yeah, we would just crash the universe.
*  Now, you know, the universe, you know, has seemed to hold up pretty well for, you know,
*  14 billion years.
*  Right.
*  You know, my, you know, Occam's razor kind of guess has to be that, you know, it will
*  continue to hold up, you know, that the fact that we don't know the laws of physics governing
*  some phenomenon is not a strong sign that probing that phenomenon is going to crash
*  the universe.
*  All right.
*  But, you know, of course, I could be wrong.
*  But do you think on the physics side of things, you know, there's been recently a few folks,
*  Eric Weinstein and Stephen Wolfram, that came out with the theory of everything.
*  I think there's a history of physicists dreaming and working on the unification of all the
*  laws of physics.
*  Do you think it's possible that once we understand more physics, not necessarily the unification
*  of the laws, but just understand physics more deeply at the fundamental level, we'll be
*  able to start, you know, I mean, part of this is humorous, but looking to see if there's
*  any bugs in the universe that could be exploited for, you know, traveling at not just the speed
*  of light, but just traveling faster than our current spaceships can travel, all that kind
*  of stuff.
*  Well, I mean, to travel faster than our current spaceships could travel, you wouldn't need
*  to find any bug in the universe, right?
*  The known laws of physics, you know, let us go much faster up to the speed of light, right?
*  And you know, when people want to go faster than the speed of light, well, we actually
*  know something about what that would entail, namely that, you know, according to relativity,
*  that seems to entail communication backwards in time.
*  Okay, so then you have to worry about closed time like curves and all of that stuff.
*  So, you know, in some sense, we sort of know the price that you have to pay for these things,
*  right?
*  Under the current understanding of physics.
*  That's right.
*  That's right.
*  We can't, you know, say that they're impossible, but we, you know, we know that sort of a lot
*  else in physics breaks.
*  So now regarding Eric Weinstein and Stephen Wolfram, like I wouldn't say that either of
*  them has a theory of everything.
*  I would say that they have ideas that they hope, you know, could someday lead to a theory
*  of everything.
*  Is that a worthy pursuit?
*  Well, I mean, certainly, let's say by theory of everything, you know, we don't literally
*  mean a theory of cats and of baseball and, you know, but we just mean it in the in the
*  more limited sense of everything, a fundamental theory of physics, right?
*  Of all of the fundamental interactions of physics.
*  Of course, such a theory, even after we had it, you know, would would leave the entire
*  question of all the emergent behavior, right?
*  You know, to to be explored.
*  So it's only everything for a specific definition of everything.
*  Okay, but in that sense, I would say, of course, that's worth pursuing.
*  I mean, that is the entire program of fundamental physics, right?
*  All of my friends who do quantum gravity, who do string theory, who do anything like
*  that, that is what's motivating them.
*  Yeah, it's funny, though.
*  But I mean, Eric Weinstein talks about this.
*  It is I don't know much about the physics world, but I know about the world.
*  And it is a it is a little bit taboo.
*  To talk about AGI, for example, on the A.I. side.
*  So really to talk about the the big dream of the community, I would say,
*  because it seems so far away, it's almost taboo to bring it up because,
*  you know, it's seen as the kind of people that dream about creating a truly
*  superhuman level of intelligence.
*  That's really far out there.
*  People, because we're not even close to that.
*  And it feels like the same thing is true for the physics community.
*  I mean, Stephen Hawking certainly talked
*  constantly about theory of everything.
*  Right. You know, I mean, I mean, people, you know, use those terms who were,
*  you know, some of the most respected people in the in the in the whole world of
*  physics. Right. But I mean, I think that the distinction that I would make is that
*  people might react badly if you use the term in a way that suggests that that
*  you, you know, thinking about it for five minutes have come up with this major new
*  insight about it. Yeah. Right.
*  It's it's difficult.
*  Stephen Hawking is not a great example because I think
*  you can do whatever the heck you want when you get to that level.
*  And I certainly see like senior faculty, you know,
*  you know, at that point, that's one of the nice things about getting older is
*  you stop giving a damn.
*  But the media as a whole, they tend to roll their eyes very quickly at stuff
*  that's outside the quote unquote mainstream.
*  Well, well, let me let me put it this way.
*  I mean, if you ask, you know, Ed Witten, let's say who is, you know,
*  you might consider a leader of the string community and thus, you know,
*  very, very mainstream in a certain sense.
*  But he would have no hesitation in saying, you know, of course, you know,
*  they're looking for a, you know,
*  you know, a unified description of nature, of, you know,
*  of general relativity, of quantum mechanics, of all the fundamental
*  interactions of nature. Right.
*  Now, you know, whether people would call that a theory of everything,
*  whether they would use that that term, that might vary.
*  You know, Lenny Suskin would definitely have no problem telling you that,
*  you know, if that's what we want. Right.
*  For me, who loves human beings and psychology,
*  it's kind of ridiculous to say
*  a theory that unifies the laws of physics gets you to understand everything.
*  I would say you're not even close to understanding everything. Yeah. Right.
*  Well, yeah. I mean, the word everything is a little ambiguous here. Right.
*  Because, you know, and then people will get into debates about, you know,
*  reductionism versus emergentism and blah, blah, blah.
*  And so in not wanting to say theory of everything,
*  people might just be trying to short circuit that debate and say, you know, look,
*  you know, yes, we want a fundamental theory of, you know,
*  the particles and interactions of nature.
*  Let me bring up the next topic that people don't want to mention,
*  although they're getting more comfortable with it, is consciousness.
*  You mentioned that you have a talk on consciousness that I watched five minutes
*  of, but the Internet connection was really bad.
*  Was this my talk about, you know, refuting the integrated information theory?
*  Yes, which was a particular account of consciousness that, yeah,
*  I think one can just show it doesn't work.
*  So let me harder to say what does work. What does work? Yeah.
*  Let me ask. Maybe it'd be nice to comment on.
*  You talk about also like the semi hard problem of conscience.
*  Or like almost hard problem or kind of hard. Pretty, pretty hard.
*  Pretty hard. I think I call it.
*  So maybe can you talk about that?
*  Their idea of of the approach to modeling consciousness
*  and why you don't find it convincing. What is it? First of all, what?
*  OK, well, so so what what what I called the pretty hard problem of consciousness.
*  This is my term, although many other people have said something equivalent to this. OK.
*  But it's just, you know, the the the problem of,
*  you know, giving an account of just which physical systems are conscious and which are not.
*  Or, you know, if there are degrees of consciousness,
*  then quantifying how conscious a given system is.
*  Oh, so that's the pretty hard. Yeah, that's what I mean.
*  That's it. I'm adopting it. I love it. That's a good ring to it.
*  And so, you know, the infamous hard problem of consciousness
*  is to explain how something like consciousness could arise at all,
*  you know, in a material universe. Right.
*  Or, you know, why does it ever feel like anything to to experience anything? Right.
*  And, you know, so I'm trying to distinguish from that problem. Right.
*  And say, you know, no, OK, I am I would merely settle for an account
*  that could say, you know, is a fetus conscious, you know, if so, at which trimester,
*  you know, is a is a dog conscious.
*  You know, what about a frog? Right.
*  Or even as a precondition, you take that both these things are conscious.
*  Tell me which is more conscious. Yeah. For example, yes.
*  Yeah. Yeah. I mean, if consciousness is some multidimensional vector,
*  well, just tell me in which respects these things are conscious
*  and in which respect they aren't. Right.
*  And, you know, and have some principled way to do it where you're not,
*  you know, carving out exceptions for things that you like or don't like,
*  but could somehow take a description of an arbitrary physical system
*  and then just based on the physical properties of that system
*  or the informational properties or how it's connected or something like that,
*  just in principle, calculate, you know, its degree of consciousness. Right.
*  I mean, this this this would be the kind of thing that we would need,
*  you know, if we wanted to address questions like, you know,
*  what does it take for a machine to be conscious? Right.
*  Or when or, you know, when when when should we regard AIs as being conscious?
*  So now this IIT, this integrated information theory,
*  which has been put forward by Giulio Tononi
*  and a bunch of his
*  collaborators over the last decade or two.
*  This is noteworthy, I guess, as a direct attempt to answer that question,
*  to answer the to address the pretty hard problem.
*  And they give a a criterion that's just based on how a system is connected.
*  So you so it's up to you to sort of abstract the system
*  like a brain or a microchip as a collection of components
*  that are connected to each other by some pattern of connections, you know,
*  and and to specify how the components can influence each other,
*  you know, like where the inputs go, you know, where they affect the outputs.
*  But then once you've specified that, then they give this quantity
*  that they call phi, you know, the Greek letter phi.
*  And the definition of phi has actually changed over time.
*  It changes from one paper to another.
*  But in all of the variations, it involves something about
*  what we in computer science would call graph expansion.
*  So basically what this means is that they want it
*  in order to get a large value of phi.
*  It should not be possible to take your system and partition it
*  into two components that are only weakly connected to each other.
*  OK, so whenever we take our system and sort of try to split it up into two,
*  then there should be lots and lots of connections
*  going between the two components.
*  OK, well, I understand what that means.
*  And I guess do they formalize what
*  how to construct such a graph or data structure, whatever?
*  Or is this one of the criticism
*  I've heard you kind of say is that a lot of the very interesting specifics
*  are usually communicated through like natural language, like
*  like through words.
*  So it's like the details aren't always well.
*  Well, it's true.
*  I mean, they they they have nothing even resembling a derivation of this fee.
*  OK, so what they do is they state a whole bunch of postulates,
*  you know, axioms that they think that consciousness should satisfy.
*  And then there's some verbal discussion and then at some point fee appears.
*  Right. And this this was the first thing that really made the hair
*  stand on my neck, to be honest, because they are acting as if there is a derivation.
*  They're acting as if, you know, you're supposed to think that this is a derivation.
*  And there's nothing even remotely resembling a derivative.
*  They just pull the fee out of a hat completely.
*  Is one of the key criticisms to you is that details are missing or is that
*  that's not even the key criticism.
*  That's just that's just a side point.
*  OK, the the core of it is that I think that, you know,
*  they want to say that a system is more conscious, the larger its value of fee.
*  And I think that that is obvious nonsense.
*  OK, as soon as you think about it for like a minute, as soon as you think about it
*  in terms of could I construct a system that had an enormous value of fee,
*  like, you know, even larger than the brain has, but that is just
*  implementing an error correcting code, you know, doing nothing that we would
*  associate with intelligence or consciousness or any of it.
*  The answer is yes, it is easy to do that. Right.
*  And so I wrote blog posts just making this point that, yeah, it's easy to do that.
*  Now, you know, to know his response to that was actually kind of incredible.
*  Right. I mean, I admired it in a way because instead of disputing any of it,
*  he just bit the bullet in the sense, you know, he was one of the
*  the most audacious bullet bitings I've ever seen in my career.
*  OK, he said, OK, then fine.
*  You know, this system that just applies this error correcting code, it's conscious.
*  You know, and if it has a much larger value of fee than you or me,
*  it's much more conscious than you and me.
*  You know, you we just have to accept what the theory says, because, you know,
*  science is not about confirming our intuitions, it's about challenging them.
*  And, you know, this is what my theory predicts, that this thing is conscious
*  and, you know, are super duper conscious.
*  And how are you going to prove me wrong?
*  So the way I would argue, yeah, I guess your blog post is I would say, yes,
*  sure, you're right in general.
*  For naturally arising systems developed through the process of evolution on Earth,
*  the this rule of the larger fee being associated with more consciousness is correct.
*  Yeah, so that's not what he said at all. Right. Right.
*  Because he wants this to be completely general.
*  So we can apply it to even computers.
*  Yeah. I mean, I mean, the whole interest of the theory is the, you know,
*  the hope that it could be completely general, apply to aliens, to computers, to
*  animals, coma patients, to any of it. Right. Yeah.
*  And so so so he just said, well, you know,
*  Scott is relying on his intuition, but, you know, I'm relying on this theory.
*  And, you know, to me, it was almost like, you know, are we being serious here?
*  Like, like, like, you know, like, like, OK, yes, in science,
*  we try to learn highly nonintuitive things.
*  But what we do is we first test the theory on cases where we already know the answer.
*  Right. Like if we if someone had a new theory of temperature, right, then,
*  you know, maybe we could check that it says that boiling water is hotter than ice.
*  And then if it says that the sun is hotter than anything, you know,
*  you've ever experienced, then maybe we we trust that extrapolation.
*  Right. But like this this theory, like if if, you know,
*  it's now saying that, you know, a gigantic grid,
*  like regular grid of exclusive or gates can be way more conscious than,
*  you know, a person or than any animal can be, you know, even if it, you know, is,
*  you know, is is is is so uniform that it might as well just be a blank wall.
*  Right. And so now the point is, if this theory is sort of getting wrong,
*  the question is a blank wall, you know, more conscious than a person,
*  then I would say what is what is there for it to get right?
*  So your sense is a blank wall
*  is not more conscious than a human being.
*  Yeah. I mean, I mean, I mean, you could say that I am taking that as one of my axioms.
*  I'm saying I'm saying that if a theory of consciousness is
*  is getting that wrong, then whatever it is talking about at that point,
*  I I am not going to call it conscious.
*  I'm going to use a different word. You have to use a different word.
*  I mean, it's also it's possible, just like with intelligence,
*  that us humans conveniently define these very difficult to understand concepts
*  in a very human centric way.
*  That's like the Turing test really seems to define intelligence
*  as a thing that's human like.
*  Right. But I would say that with any concept, you know, there's
*  you know, like we first need to define it.
*  Right. And a definition is only a good definition
*  if it matches what we thought we were talking about, you know,
*  prior to having a definition. Right.
*  And I would say that, you know,
*  fee as a definition of consciousness fails that test.
*  That is my argument.
*  So, OK, so let's take a further step.
*  So you mentioned that the universe might be a Turing machine.
*  So like it might be computation or simulatable by one anyway,
*  simulatable by one.
*  So what's your sense about consciousness?
*  Do you think consciousness is computation
*  that we don't need to go to any place outside of the computable universe
*  to, you know, to to understand consciousness,
*  to build consciousness, to measure consciousness, all those kinds of things?
*  I don't know. These are what, you know, have been called the
*  vertiginous questions, right.
*  There's the questions like, like, you know, you get a feeling of vertigo
*  and thinking about them. Right.
*  I mean, I certainly feel like I am conscious in a way
*  that is not reducible to computation.
*  But why should you believe me? Right.
*  I mean, and if you said the same to me, then why should I believe you?
*  But as computer scientists, I feel like a computer could be intelligent,
*  could achieve human level intelligence.
*  But and that's actually a feeling and a hope.
*  That's not a scientific belief.
*  It's just we've built up enough intuition,
*  the same kind of intuition you use in your blog.
*  You know, that's what scientists do.
*  They I mean, some of it is a scientific method,
*  but some of it is just damn good intuition.
*  I don't have a good intuition about consciousness. Yeah.
*  I'm not sure that anyone does or has in the, you know,
*  2500 years that these things have been discussed.
*  But do you think we will?
*  Like one of the I got a chance to attend.
*  Can't wait to hear your opinion on this, but attending your link event.
*  And one of the dreams there is to, you know,
*  basically push neuroscience forward.
*  And the hope in neuroscience is that we can
*  inspect the machinery from which all this fun stuff emerges and see.
*  Are we going to notice something special, some special sauce
*  from which something like consciousness or cognition emerges?
*  Yeah. Well, it's clear that we've learned an enormous amount about neuroscience.
*  We've learned an enormous amount about computation,
*  you know, about machine learning, about you know, AI, how to get it to work.
*  We've learned an enormous amount about the underpinnings of the physical world.
*  You know, and, you know, from one point of view,
*  that's like an enormous distance that we've traveled along the road
*  to understand the consciousness from another point of view.
*  You know, the distance still to be traveled on the road,
*  you know, maybe seems no shorter than it was at the beginning. Yeah. Right.
*  So it's very hard to say.
*  I mean, you know, these are questions like like in in in sort of trying
*  to have a theory of consciousness, there is sort of a problem where it feels like
*  it's not just that we don't know how to make progress,
*  it's that it's hard to specify what could even count as progress. Right.
*  Because no matter what scientific theory someone proposed,
*  someone else could come along and say, well, you've just talked about the mechanism.
*  You haven't said anything about what breathes fire into the mechanism,
*  what really makes there something that it's like to be it.
*  And that seems like an objection that you could always raise.
*  No matter how much someone elucidated the details of how the brain works.
*  OK, let's go to a test in Lobna Prize.
*  I have this intuition, call me crazy, but we that a machine
*  to pass the Turing test in this full.
*  Whatever the spirit of it is, we can talk about how to formulate
*  the perfect Turing test, that that machine has to be conscious
*  or we at least have to.
*  I have a very low bar of what consciousness is.
*  I tend to I tend to think that the emulation of consciousness
*  is as good as consciousness.
*  So the consciousness is just a dance, a social.
*  A social shortcut, like a nice, useful tool.
*  But I tend to connect intelligence, consciousness together.
*  So by by that, do you?
*  Maybe just to ask what what role does consciousness play?
*  Do you think it passed in the Turing test?
*  Well, look, I mean, it's almost tautologically true
*  that if we had a machine that passed the Turing test,
*  then it would be emulating consciousness. Right.
*  So if your position is that, you know, emulation of consciousness
*  is consciousness, then, you know, by definition,
*  any machine that passed the Turing test would be conscious.
*  But it's but I mean, you know that you could say that, you know,
*  that is just a way to rephrase the original question.
*  You know, is an emulation of consciousness, you know, necessarily conscious. Right.
*  And you can you know, I hear I'm not saying anything new
*  that hasn't been debated ad nauseum in the literature. OK.
*  But, you know, you could imagine some very hard cases like imagine a machine
*  that passed the Turing test, but that did so just by an enormous
*  cosmological sized lookup table that just cashed every possible conversation.
*  That could be had the old Chinese room.
*  Well, well, yeah. Yeah. But but this is I mean,
*  I mean, the Chinese room actually would be doing some computation,
*  at least in Searle's version. Right here.
*  I'm just talking about a table lookup. OK.
*  Now, it's true that for conversations of a reasonable length, this,
*  you know, lookup table would be so enormous
*  that wouldn't even fit in the observable universe. OK.
*  But supposing that you could build a big enough lookup table
*  and then just, you know, pass the Turing test just by looking up
*  what the person said. Right.
*  Are you going to regard that as conscious? OK.
*  Let me try to make this formal and then you can shut it down.
*  I think that the emulation of something is that something
*  if there exists in that system a black box that's full of mystery.
*  So like full of mystery to whom?
*  To human and specters.
*  So does that mean that consciousness is relative to the observer?
*  Like, could something be conscious for us, but not conscious for an alien
*  that understood better what was happening inside the black box?
*  Yes. So that if inside the black box is just a lookup table,
*  the alien that saw that would say this is not conscious to us.
*  Another way to phrase the black box is layers of abstraction,
*  which make it very difficult to see to the actually underlying functionality
*  of the system. And then we observe just the abstraction.
*  And so it looks like magic to us.
*  But once we understand the inner machinery, it stops being magic.
*  And so like that's a prerequisite is that you can't know how it works
*  some part of it, because then there has to be in our human mind
*  entry point for the magic.
*  So that's that's a formal definition of the.
*  Yeah. Well, look, I mean, I explored a view in this essay
*  I wrote called The Ghost and the Quantum Touring Machine seven years ago
*  that is related to that, except that I did not want to have
*  consciousness be relative to the observer, right?
*  Because I think that, you know, if consciousness means anything,
*  it is something that is experienced by the entity that is conscious. Right.
*  You know, like I don't need you to tell me that I'm conscious. Right.
*  Nor do you need me to to to to tell you that you are. Right.
*  So so but but basically what I explored there is, you know, are there
*  aspects of a system like like a brain
*  that that just could not be predicted even with arbitrarily advanced
*  future technologies because of chaos combined with quantum
*  mechanical uncertainty, you know, things like that.
*  I mean, that that actually could be a property of the brain.
*  You know, if true, that would distinguish it in a principled way,
*  at least from any currently existing computer, not from any possible computer.
*  But yeah, yeah.
*  The thought experiment.
*  So yeah, if I gave you information that you're in the entire history of your life,
*  basically explain away free will with a lookup table, say that this was all
*  predetermined, that everything you experience has already been predetermined.
*  Wouldn't that take away your consciousness?
*  Wouldn't you yourself that wouldn't experience of the world change for you
*  in a way that you can't? Well, well, let me let me put it this way.
*  If you could do like in a Greek tragedy where, you know, you would just write down
*  a prediction for what I'm going to do, and then maybe you put the prediction
*  in a sealed box and maybe, you know, you you open it later
*  and you show that you knew everything I was going to do.
*  Or, you know, of course, the even creepier version would be you tell me the prediction
*  and then I try to falsify it.
*  My very effort to falsify it makes it come true.
*  Right. Let's let's let's, you know, let's even forget that, you know, that version
*  is as convenient as it is for fiction writers.
*  Right. Let's just let's just do the version where you put the prediction
*  into a sealed envelope. OK.
*  But if you could reliably predict everything that I was going to do,
*  I'm not sure that that would destroy my sense of being conscious.
*  But I think it really would destroy my sense of having free will, you know,
*  and much, much more than any philosophical conversation could possibly do that.
*  Right. And so I think it becomes extremely interesting
*  to ask, you know, could such predictions be done, you know, even in principle?
*  Is it consistent with the laws of physics to make such predictions,
*  to get enough data about someone that you could actually generate
*  such predictions without having to kill them in the process to, you know,
*  slice their brain up into little slivers or something?
*  I mean, theoretically possible, right?
*  Well, I don't know.
*  I mean, I mean, it might be possible, but only at the cost of destroying the person.
*  All right. I mean, it depends on how low you have to go.
*  In sort of the substrate, like if there was a nice digital abstraction layer,
*  if you could think of each neuron as a kind of transistor
*  computing a digital function, then you could imagine some nano robots
*  that would go in and we just scan the state of each transistor,
*  you know, of each neuron and then, you know, make a a good enough copy. Right.
*  But if it was actually important to get down to the molecular or the atomic level,
*  then, you know, eventually you would be up against quantum effects.
*  You would be up against the uncloanability of quantum states.
*  So I think it's a question of how good of a replica,
*  how good does the replica have to be before you're going to count it
*  as actually a copy of you or as being able to predict your actions?
*  That's a totally open question.
*  Yeah, yeah, yeah. And especially once we say that, well, look,
*  maybe there's no way to, you know, to make a deterministic prediction
*  because, you know, there's all there.
*  We know that there's noise buffeting the brain around,
*  presumably even quantum mechanical uncertainty, you know, affecting
*  the sodium ion channels, for example, whether they open or they close.
*  You know, there's no reason why if over a certain time scale,
*  that shouldn't be amplified, just like we imagine happens with the weather
*  or with any other, you know, chaotic system.
*  So if that stuff is important, right, then then, you know, we would say,
*  well, you know, you can't, you know, you're never going to be able
*  to make an accurate enough copy.
*  But now the hard part is, well, what if someone can make a copy
*  that sort of no one else can tell apart from you? Right.
*  It says the same kinds of things that you would have said,
*  maybe not exactly the same things because we agree that there's noise,
*  but it says the same kinds of things.
*  And maybe you alone would say, no, I know that that's not me.
*  You know, it's it doesn't share my I haven't felt my consciousness
*  leap over to that other thing.
*  I still feel it localized in this version. Right.
*  Then why should anyone else believe you?
*  What are your thoughts?
*  I'd be curious. You're a good person to ask, which is
*  Penrose's Roger Penrose's work on consciousness,
*  saying that there, you know, there is some with axons and so on.
*  There might be some biological places where quantum mechanics can come into play
*  and through that create consciousness somehow. Yeah.
*  OK. Well, I'm familiar with this, of course.
*  You know, I read Penrose's books as a teenager.
*  They had a huge impact on me five or six years ago.
*  I had the privilege to actually talk these things over with Penrose,
*  you know, at some length at a conference in Minnesota.
*  And, you know, he is, you know, an amazing personality.
*  I admire the fact that he was even raising such audacious questions at all.
*  But, you know, to to to answer your question,
*  I think the first thing we need to get clear on
*  is that he is not merely saying that quantum mechanics is relevant to consciousness.
*  Right. That would be like, you know, that would be tame compared to what he is saying.
*  Right. He is saying that, you know, even quantum mechanics is not good enough.
*  Right. Because if supposing, for example, that the brain were a quantum computer,
*  I know that's still a computer.
*  You know, in fact, a quantum computer can be simulated by an ordinary computer.
*  It might merely need exponentially more time in order to do so. Right.
*  So that's simply not good enough for him.
*  OK. So what he wants is for the brain to be a quantum gravitational computer.
*  Or he wants the brain to be exploiting
*  as yet unknown laws of quantum gravity, OK, which would which would be uncomputable.
*  Uncomputable. That's the key point.
*  OK. Yes. Yes. That would be literally uncomputable.
*  And I've asked him, you know, to clarify this, but uncomputable,
*  even if you had an oracle for the halting problem or, you know,
*  and or, you know, as high up as you want to go in the sort of high
*  the usual hierarchy of uncomputability, he wants to go beyond all of that.
*  OK. So so, you know, just just to be clear, like, you know,
*  if we're keeping count of how many speculations, you know,
*  there's probably like at least five or six of them. Right.
*  There's first of all, that there is some quantum gravity theory
*  that would involve this kind of uncomputability. Right.
*  Most people who study quantum gravity would not agree with that.
*  They would say that what we've learned, you know, what little we know
*  about quantum gravity from the this ADS CFT correspondence, for example,
*  has been very much consistent with the broad idea of nature being computable.
*  Right. But but all right.
*  But supposing that he's right about that, then, you know,
*  what most physicists would say is that whatever new phenomena
*  there are in quantum gravity, you know, they might be relevant
*  at the singularities of black holes.
*  They might be relevant at the Big Bang.
*  They are plainly not relevant to something like the brain,
*  you know, that is operating at ordinary temperatures,
*  you know, with ordinary chemistry and, you know, the the the physics
*  underlying the brain, they would say that we have, you know,
*  the fundamental physics of the brain, they would say that we've
*  pretty much completely known for for generations now. Right.
*  Because, you know, quantum field theory
*  lets us sort of parameterize our ignorance. Right.
*  I mean, Sean Carroll has made this case and, you know, in great detail.
*  Right. That sort of whatever new effects are coming from quantum gravity.
*  You know, they are sort of screened off by quantum field theory. Right.
*  And this is this, you know, brings us to the whole idea of effective theories.
*  Right. But like we have, you know, like in the standard model
*  of elementary particles, right, we have a quantum field theory
*  that seems totally adequate for all of the terrestrial phenomena. Right.
*  The only things that it doesn't, you know, explain are, well, first of all,
*  you know, the details of gravity, if you were to probe it, like at at,
*  you know, extremes of, you know, curvature or at like incredibly small distances.
*  It doesn't explain dark matter.
*  It doesn't explain black hole singularities. Right.
*  But these are all very exotic things, very, you know,
*  far removed from our life on Earth. Right.
*  So for Penrose to be right, he needs, you know, these phenomena
*  to somehow affect the brain.
*  He needs the brain to contain antenna that are sensitive to the black holes,
*  to this as yet unknown physics. Right.
*  And then he needs a modification of quantum mechanics. OK.
*  So he needs quantum mechanics to actually be wrong.
*  OK. He needs what he wants is what he calls an objective
*  reduction mechanism or an objective collapse.
*  So this is the idea that once quantum states get large enough,
*  then they somehow spontaneously collapse. Right.
*  That, you know, and this is an idea that lots of people have explored.
*  You know, there's something called the GRW proposal that tries to,
*  you know, say something along those lines.
*  You know, and these are theories that actually make testable predictions.
*  Right. Which is a nice feature that they have.
*  But, you know, the very fact that they're testable may mean that in the,
*  you know, in the coming decades, we may well be able to test these theories
*  and show that they're wrong. Right.
*  You know, we may be able to test some of Penrose's ideas,
*  if not not his ideas about consciousness,
*  but at least his ideas about an objective collapse of quantum states.
*  And people have actually like Dick Balmeister have actually been working
*  to try to do these experiments.
*  They haven't been able to do it yet to test Penrose's proposal.
*  OK, but Penrose would need more than just an objective collapse of quantum states,
*  which would already be the biggest development in physics for a century
*  since quantum mechanics itself.
*  OK, he would need for consciousness to somehow be able to influence
*  the direction of the collapse so that it wouldn't be completely random.
*  But that, you know, your dispositions would somehow influence the quantum state
*  to collapse more likely this way or that way.
*  OK, finally, Penrose, you know, says that all of this has to be true
*  because of an argument that he makes based on Gödel's incompleteness theorem.
*  OK, now, like I would say, the overwhelming majority of computer
*  scientists and mathematicians who have thought about this.
*  I don't think that Gödel's incompleteness theorem can do what he needs it to do.
*  Yeah, right. I don't think that that argument is sound.
*  OK, but that is, you know, that is sort of the tower
*  that you have to ascend to if you're going to go where Penrose goes.
*  And the intuition uses with the incompleteness theorem
*  is that basically that there's important stuff that's not computable.
*  No, it's not. It's not just that, because, I mean, everyone agrees
*  that there are problems that are uncomputable.
*  That's a mathematical theorem.
*  Right. But what Penrose wants to say is that,
*  you know, the you know, for example, there are statements,
*  you know, for, you know, given any formal system, you know, for doing math.
*  There will be true statements of arithmetic that that formal system,
*  you know, if it's adequate for math at all, if it's consistent and so on,
*  will not be able to prove a famous example being the statement
*  that that system itself is consistent. Right.
*  No good formal system can actually prove its own consistency.
*  That can only be done from a stronger formal system,
*  which then can't prove its own consistency and so on forever. OK.
*  That's Gödel's theorem.
*  But now why is that relevant to consciousness? Right.
*  Well, you know, I mean, I mean, the idea that it might have something
*  to do with consciousness as an old one.
*  Gödel himself apparently thought that it was, you know, Lucas
*  thought so, I think, in the 60s.
*  And Penrose is really just, you know, sort of updating what
*  what they and others had said.
*  I mean, you know, the idea that Gödel's theorem could have something to do
*  with consciousness was, you know, in 1950, when Alan Turing
*  wrote his article about the Turing test, he already, you know,
*  was writing about that as like an old and well-known idea
*  and as one that he was as a wrong one that he wanted to dispense with.
*  OK. But the basic problem with this idea is, you know, Penrose wants to say that
*  and all of his predecessors want to say that, you know, even though,
*  you know, this given formal system cannot prove its own consistency,
*  we as humans sort of looking at it from the outside
*  can just somehow see its consistency. Right.
*  And the, you know, the rejoinder to that, you know, from the very beginning
*  has been, well, can we really? Yeah.
*  I mean, maybe or maybe, you know, maybe maybe he Penrose can.
*  But, you know, can the rest of us. Right.
*  And, you know, I noticed that, you know, I mean, it is perfectly plausible
*  to imagine a computer that could say, you know, it would not be limited
*  to working within a single formal system. Right.
*  They could say, I am now going to adopt the hypothesis
*  that this that my formal system is consistent. Right.
*  And I'm now going to see what can be done from that stronger vantage point.
*  And and so on.
*  And, you know, and I'm going to add new axioms to my system.
*  Totally plausible.
*  There's absolutely Gertel's theorem has nothing to say about against an AI
*  that could repeatedly add new axioms.
*  All it says is that there is no absolute guarantee
*  that when the AI adds new axioms, that it will always be right.
*  OK. And, you know, and that's, of course, the point that Penrose pounces on.
*  But the reply is obvious.
*  And, you know, it's one that Alan Turing made 70 years ago.
*  Namely, we don't have an absolute guarantee that we're right.
*  When we add a new axiom, we never have.
*  And plausibly, we never will.
*  So on Alan Turing, you took part in the Lobna Prize.
*  Not really. No, I didn't.
*  I mean, there was this
*  kind of ridiculous claim that was made some almost a decade ago
*  about a chat bot called Eugene Goostman.
*  I guess you didn't participate as a judge in the Lobna Prize.
*  But you participate as a judge in that.
*  I guess it was an exhibition event or something like that.
*  Or with Eugene.
*  You know, Eugene Goostman, that was just me writing a blog post
*  because some journalists called me to ask about it.
*  Did you ever chat with him?
*  I did chat with Eugene Goostman.
*  I mean, it was available on the web.
*  The chat. Oh, interesting. I didn't know.
*  Yeah. So all that happened was that,
*  so, you know, a bunch of journalists started writing breathless articles about,
*  you know, you know, first chat bot that passes the Turing test.
*  And it was this thing called Eugene Goostman
*  that was supposed to simulate a 13 year old boy.
*  And, you know, and apparently someone had done some test where,
*  you know, people couldn't, you know, you know, where we're less than perfect,
*  let's say, distinguishing it from a human.
*  And they said, well, if you look at Turing's paper and you look at,
*  you know, the percentages that he that he talked about, then, you know,
*  it seemed like we're past that threshold. Right. And.
*  You know, I had a sort of, you know, different way to look at it
*  instead of the legalistic way, like, let's just try the actual thing out
*  and let's see what it can do with questions like, you know,
*  is Mount Everest bigger than a shoe box?
*  OK. Or just, you know, like the most obvious questions. Right.
*  And then and, you know, and the answer is, well, it just kind of parries you
*  because it doesn't know what you're talking about. Right.
*  So just to clarify exactly in which way they're obvious, they're obvious.
*  In the sense that you convert the sentences
*  into the meaning of the objects they represent and then do some basic
*  obvious, we mean your common sense reasoning with the objects
*  that the senses represent. Right. Right.
*  It was not able to answer, you know, or even intelligently respond
*  to basic common sense questions.
*  But let me say something stronger than that.
*  There was a famous chat pod in the 60s called Eliza, right.
*  That, you know, that managed to actually fool, you know, a lot of people.
*  Or people would pour their hearts out into this Eliza
*  because it simulated a therapist. Right.
*  And most of what it would do was it would just throw back at you
*  whatever you said. Right.
*  And this turned out to be incredibly effective. Right.
*  Maybe, you know, therapists know this.
*  This is, you know, one of their tricks. But it, you know,
*  it really had some people convinced.
*  But, you know, this this thing was just like,
*  I think it was literally just a few hundred lines of Lisp code. Right.
*  It was not only was it not intelligent, it wasn't especially sophisticated.
*  It was like it was a simple little hobbyist program.
*  And Eugene Guestman, from what I could see, was not a significant advance
*  compared to Eliza. Right.
*  So and that was that was really the point I was making.
*  And this was, you know, you didn't in some sense,
*  you didn't need a like a computer science professor to sort of say this.
*  Like anyone who was looking at it and who just had,
*  you know, an ounce of sense could have said the same thing. Right.
*  But because, you know, these journalists were, you know, calling me,
*  you know, like the first thing I said was, well, you know, no, you know,
*  I'm a quantum computing person. I'm not an AI person.
*  You know, you shouldn't ask me.
*  Then they said, look, you can go here and you can try it out.
*  I said, all right. All right. So I'll try it out.
*  But now, you know, this whole discussion, I mean, it got a whole lot more
*  interesting in just the last few months. Yeah.
*  I'd love to hear your thoughts about GPT-3.
*  Yeah. And the last and the last few months we've had, you know, we've we've
*  the world has now seen a chat engine or a text engine, I should say, called GPT-3.
*  You know, I think it's still, you know, it does not pass a touring test.
*  You know, there are no real claims that it passes the touring test.
*  Right. You know, this is comes out of the group at OpenAI.
*  And, you know, they're, you know, they've been relatively careful
*  in what they've claimed about the system.
*  But I think this this this.
*  As clearly as Eugene Guestman was not in advance over Eliza,
*  it is equally clear that this is a major advance over over over Eliza
*  or really over anything that the world has seen before.
*  This is a text engine that can
*  come up with kind of on topic, you know, reasonable sounding completions
*  to just about anything that you ask.
*  You can ask it to write a poem about topic X in the style of poet Y.
*  And it will have a go at that.
*  And it will do, you know, not a not a great job, not an amazing job,
*  but, you know, a passable job, you know, definitely, you know, as as good as,
*  you know, you know, in many cases, I would say better than I would have done.
*  Right. You know, you can ask it to write, you know, an essay,
*  like a student essay about pretty much any topic.
*  And it will get something that I am pretty sure would get at least a B minus,
*  you know, in the most, you know, high school or even college classes.
*  Right. And, you know, in some sense, you know, the way that it did this,
*  the way that it achieves this, you know,
*  Scott Alexander of the, you know, the much mourned blog, Slate Star Codex,
*  had a wonderful way of putting it.
*  He said that they basically just ground up the entire Internet into a slurry.
*  OK. Yeah. And, you know, to tell you the truth,
*  I had wondered for a while why nobody had tried that. Right.
*  Like, why not write a chat bot by just doing deep learning
*  over a corpus consisting of the entire web? Right.
*  And so so so now they finally have done that. Right.
*  And, you know, the results are are very impressive.
*  You know, it's not clear that, you know, people can argue about
*  whether this is truly a step toward general AI or not.
*  But this is an amazing capability that, you know,
*  we didn't have a few years ago that, you know, a few years ago,
*  if you had told me that we would have it now, that would have surprised me.
*  Yeah. And I think that anyone who denies that is just not engaging with with what's there.
*  So their model, it takes a large part of the Internet
*  and compresses it in a small number of parameters relative to the size of the Internet
*  and is able to without fine tuning,
*  do a basic kind of a querying mechanism, just like you describe
*  where you specify a kind of poet and then you want to write a poem.
*  And it somehow is able to do basically a lookup on the Internet.
*  Well, relevant things.
*  I mean, that's what I mean. I mean, I mean, how else do you explain it?
*  Well, OK. I mean, I mean, I mean, the the training involved,
*  you know, massive amounts of data from the Internet and actually took
*  lots and lots of computer power, lots of electricity. Right.
*  You know, there are some some very prosaic reasons why this wasn't done earlier.
*  Right. Right. But, you know, it costs some tens of millions of dollars, I think.
*  You know, less, but approximately like a few million dollars.
*  Oh, OK. OK. Oh, really? OK.
*  More like five. Oh, all right. All right.
*  Thank you. I mean, as they as they scale it up, you know, it will cost.
*  But then the hope is cost comes down and all that kind of stuff.
*  But basically, you know, it is a neural net, you know, I mean,
*  I mean, or what's now called a deep net.
*  But, you know, they're basically the same thing. Right.
*  So it's a it's a form of, you know,
*  algorithm that people have known about for decades. Right.
*  But it is constantly trying to solve the problem, predict the next word.
*  Right. So it's just trying to
*  predict what comes next.
*  It's not trying to decide what what it should say, what ought to be true.
*  It's trying to predict what someone who had said all of the words
*  up to the preceding one would say next.
*  Although to push back on that, that's how it's trained.
*  But that's right. No, it's arguable.
*  It's arguable that our very cognition could be a mechanism as that simple.
*  Oh, of course. Of course. I never said that it wasn't right.
*  But yeah, I mean, I mean, sometimes that that is, you know,
*  if there is a deep philosophical question that's raised by GPT three,
*  then that is it. Right.
*  Are we doing anything other than, you know, this predictive processing,
*  just trying to constantly trying to fill in a blank of what would come next
*  after what we just said up to this point?
*  Is that what I'm doing right now?
*  Is it possible?
*  So the intuition that a lot of people have will look,
*  this thing is not going to be able to reason the mountain Everest question.
*  Do you think it's possible that GPT five, six and seven
*  would be able to with this exact same process, begin to
*  do something that looks like is indistinguishable to us humans from reasoning?
*  I mean, the truth is that we don't really know what the limits are. Right.
*  Because exactly because, you know, what we've seen so far is that, you know,
*  GPT three was basically the same thing as GPT two, but just with,
*  you know, a much larger network, you know, more training time,
*  bigger training corpus. Right.
*  And it was, you know, very noticeably better.
*  Right. Then it's immediate predecessor.
*  So, you know, we don't know where you hit the ceiling here. Right.
*  I mean, that's the that's the amazing part.
*  And maybe also the scary part. Right.
*  That, you know, now my guess would be that, you know, at some point,
*  like there has to be diminishing returns.
*  Like it can't be that simple. Can it? Right. Right.
*  But I wish that I had more to base that guess on. Right.
*  Yeah. I mean, some people say that there will be a limitation on the
*  we're going to hit a limit on the amount of data that's on the Internet.
*  Yes. Yeah. So, so sure.
*  So, so there's certainly that limit.
*  I mean, there's also,
*  you know, like if you are looking for questions that will stomp GPT three,
*  right, you can come up with some without, you know, like, you know,
*  even getting it to learn how to balance parentheses. Right.
*  Like it can, you know, it doesn't do such a great job. Right.
*  You know, like, like, you know, and it's failures are ironic.
*  Right. Like, like basic arithmetic. Right.
*  And you think, you know, isn't that what computers are supposed to be best at?
*  Isn't that where computers already had us beat a century ago?
*  Yeah. Right. And, you know, and yet that's where GPT three struggles. Right.
*  But it's it's amazing, you know, that it's almost like a young child in that way.
*  Right. That.
*  But but somehow, you know, because it is just trying to predict what
*  what comes next, it doesn't know when it should stop doing that
*  and start doing something very different, like some more exact logical reasoning.
*  Right. And so so, you know, the,
*  you know, one one is naturally led to guess
*  that our brain sort of has some element of predictive processing,
*  but that it's coupled to other mechanisms, right, that it's coupled to,
*  you know, first of all, visual reasoning, which GPT three also doesn't have any of.
*  Right. Although there's some demonstration that there's a lot of promise there.
*  Oh, yeah. It can complete images. That's right.
*  And using exact same kind of transformer mechanisms
*  to like watch videos on YouTube.
*  And so the same the same self-supervised mechanism to be able to do.
*  Look, it'd be fascinating to think what kind of completions you could do.
*  Oh, yeah. No, absolutely.
*  Although, like if we ask it to like, you know, a word problem
*  that involve reasoning about the locations of things in space,
*  I don't think it does such a great job on those. Right.
*  To take an example.
*  And so so the guess would be, well, you know, humans have a lot of predictive
*  processing, a lot of just filling in the blanks.
*  But we also have these other mechanisms that we can couple to
*  or that we can sort of call a subroutines when we need to.
*  And that maybe maybe, you know, to go further,
*  that one would one would want to integrate other forms of reasoning.
*  Let me go on another topic that is amazing,
*  which is complexity.
*  What? And then start with the most absurdly romantic question of
*  what's the most beautiful idea in the computer science or theoretical
*  computer science to you?
*  Like what just early on in your life or in general have captivated you
*  and just grabbed you?
*  I think I'm going to have to go with the idea of universality.
*  You know, if you're really asking for the most beautiful, I mean.
*  So universality is the idea that, you know, you put together
*  a few simple operations like in the case of Boolean logic,
*  that might be the and gate, the or gate, the not gate.
*  And then your first guess is, OK, this is a good start.
*  But obviously, as I want to do more complicated things,
*  I'm going to need more complicated building blocks to express that.
*  Right. And that was actually my guess when I first learned what programming was.
*  I mean, when I was an adolescent and I someone showed me
*  Apple basic and then, you know, G.W. basic.
*  If any anyone listening remembers that.
*  OK, but, you know, I thought, OK, well, now, you know, I mean,
*  I thought I felt like this is a revelation.
*  You know, it's like finding out where babies come from.
*  It's like that level of, you know, why didn't anyone tell me this before?
*  Right. But I thought, OK, this is just the beginning.
*  Now I know how to write a basic program, but, you know, really write
*  an interesting program like, you know, a video game,
*  which had always been my dream as a kid to, you know, create my own Nintendo games.
*  Right. But, you know, obviously, I'm going to need to learn
*  some way more complicated form of programming than that.
*  OK, but, you know, eventually I learned this incredible idea of universality.
*  And that says that, no, you throw in a few rules and then you can
*  you already have enough to express everything.
*  OK, so, for example, the and the or and the not gate can all or in fact,
*  even just the and and the not gate or even just even just the NAND gate,
*  for example, is already enough to express any Boolean function on any number of bits.
*  You just have to string together enough of them.
*  You can build a universe with NAND gates.
*  You can build the universe out of NAND gates. Yeah.
*  You know, the the simple instructions of basic are already enough
*  at least in principle, you know, if we ignore details
*  like how much memory can be accessed and stuff like that,
*  that is enough to express what could be expressed by any programming language whatsoever.
*  And the way to prove that is very simple.
*  We simply need to show that in basic or whatever, we could write
*  a an interpreter or a compiler for whatever other programming
*  language we care about, like C or Java or whatever.
*  And as soon as we had done that, then ipso facto,
*  anything that's expressible in C or Java is also expressible in basic.
*  OK, and so this idea of universality,
*  you know, goes back at least to Alan Turing in the 1930s when, you know, he
*  wrote down this incredibly simple
*  pared down model of a computer, the Turing machine, right, which,
*  you know, he pared down the instruction set to just read a symbol,
*  you know, go write a symbol, move to the left, move to the right,
*  halt, change your internal state. Right. That's it.
*  OK. And anybody prove that, you know, this could simulate all kinds of other things.
*  You know, and so so in fact, today we would say,
*  well, we would call it a Turing universal model of computation that is, you know,
*  just as it has just the same expressive power that basic
*  or Java or C++ or any of those other languages have,
*  because anything in those other languages could be compiled down to Turing machine.
*  Now, Turing also proved a different related thing,
*  which is that there is a single Turing machine
*  that can simulate any other Turing machine.
*  If you just describe that other machine on its tape. Right.
*  And likewise, there is a single Turing machine that will run any C program,
*  you know, if you just put it on its tape.
*  That's that's a second meaning of universality.
*  First of all, that he couldn't visualize it and that was in the 30s.
*  Yeah, the 30s. That's right. Before computers really.
*  I mean, I don't know how I wonder what that felt like.
*  You know, learning that there's no Santa Claus or something,
*  because I don't know if that's empowering or paralyzing,
*  because it doesn't give you any.
*  It's like you can't write a software engineering book
*  and make that the first chapter and say, we're done.
*  Well, I mean, I mean, right.
*  I mean, I mean, in one sense, it was this enormous flattening of the universe.
*  Yes. Right.
*  I had imagined that there was going to be some infinite hierarchy
*  of more and more powerful programming languages.
*  You know, and then I kicked myself for, you know, for having such a stupid idea.
*  But apparently, Gödel had had the same conjecture in the 30s.
*  And then, you know, you're in good company.
*  Yeah. And then and then and then and then Gödel read Turing's paper
*  and he kicked himself and he said, yeah, I was completely wrong about that.
*  OK. But but, you know, I had thought that, you know, maybe
*  maybe where I can contribute will be to invent a new, more powerful
*  programming language that lets you express things that could never be expressed
*  in basic. Right. And, you know, and, you know, how would you do that?
*  Obviously, you couldn't do it itself in basic. Right.
*  But but, you know, there is this incredible flattening that happens
*  once you learn what is universality.
*  But then it's also like an opportunity,
*  because it means once you know these rules, then, you know, the sky is the limit.
*  Right. Then you have kind of the same weapons
*  at your disposal that the world's greatest programmer has.
*  It's now all just a question of how you wield them. Right.
*  Exactly. But so every problem is solvable.
*  But some problems are harder than others.
*  And well, yeah, there's the question of how much time, you know,
*  well, of how hard is it to write a program?
*  And then there's also the questions of what resources does the program need?
*  You know, how much time, how much memory?
*  Those are much more complicated questions, of course,
*  ones that we're still struggling with today.
*  Exactly. So you've I don't know if you created Complexity Zoo or.
*  I did create the Complexity Zoo.
*  What is it? What's complexity?
*  Oh, all right. Complexity theory is the study of sort of the
*  inherent resources needed to solve computational problems.
*  OK, so it's easiest to give an example.
*  Like, let's say we want to add two numbers, right?
*  If I want to add them,
*  you know, if the numbers are twice as long, then it only it will take me
*  twice as long to add them, but only twice as long. Right.
*  It's no worse than that.
*  Multi-computer for a computer or for a person.
*  We're using pencil and paper for that matter.
*  If you have a good algorithm.
*  Yeah, that's right.
*  I mean, even if you just if you just use the elementary school algorithm
*  of just carrying, you know, then it takes time that is linear
*  and the length of the numbers. Right.
*  Now, multiplication, if you use the elementary school algorithm, is harder
*  because you have to multiply each digit of the first number
*  by each digit of the second one.
*  Yeah. And then deal with all the carries.
*  So that's what we call a quadratic time algorithm. Right.
*  If the numbers become twice as long, now you need four times as much time.
*  OK, so now as it turns out, we
*  people discovered much faster ways to multiply numbers using computers.
*  And today we know how to multiply two numbers that are end digits long
*  using a number of steps that's nearly linear in it.
*  These are questions you can ask.
*  But now let's think about a different thing that people,
*  you know, they've encountered in elementary school, a factoring a number.
*  OK, take a number and find its prime factors. Right.
*  And here, you know, if I give you a number with 10 digits,
*  I ask you for its prime factors.
*  Well, maybe it's even.
*  So, you know, the two is a factor.
*  You know, maybe it ends in zero.
*  So, you know, the 10 is a factor. Right.
*  But, you know, other than a few obvious things like that, you know,
*  if the prime factors are all very large,
*  then it's not clear how you even get started. Right.
*  You know, you it seems like you have to do an exhaustive search
*  among an enormous number of factors now.
*  And as many people might know, the for better or worse,
*  the security, you know, of most of the encryption
*  that we currently use to protect the Internet is based on the belief.
*  And this is not a theorem.
*  It's a belief that that factoring is an inherently hard problem.
*  For our computers, we do know algorithms that are better
*  than just trial division and just trying all the possible divisors.
*  But they are still basically exponential and exponential.
*  Yeah, exactly.
*  So that's the fastest algorithms that anyone has discovered,
*  at least publicly discovered.
*  You know, I'm assuming that the NSA doesn't know something better.
*  OK, but they take time that basically grows exponentially
*  with the cube root of the size of the number that you're factoring.
*  Right. So that cube root, that's the part that takes all the cleverness.
*  OK, but there's still an exponential.
*  There's still an exponentiality there.
*  But what that means is that, like when people use a thousand bit keys
*  for their cryptography, that can probably be broken
*  using the resources of the NSA or the world's other intelligence agencies.
*  You know, people have done analyses that say, you know,
*  with a few hundred million dollars of computer power,
*  they could totally do this.
*  And if you look at the documents that Snowden released, you know,
*  it looks a lot like they are doing that or something like that.
*  It would kind of be surprising if they weren't.
*  OK, but, you know, if that's true, then in some ways, that's reassuring,
*  because if that's the best that they can do,
*  then that would say that they can't break two thousand bit numbers. Right.
*  Right. Exactly. Right.
*  Then two thousand bit numbers would be would be beyond what even they could do.
*  They haven't found an efficient algorithm.
*  That's where all the worries and the concerns of quantum computing came in.
*  And there could be some kind of shortcut around that. Right.
*  So complexity theory is a, you know, is is a huge part of,
*  let's say, the theoretical core of computer science.
*  You know, it started in the 60s and 70s as, you know, sort of an,
*  you know, autonomous field.
*  So it was, you know, already, you know, I mean, you know, it was well developed
*  even by the time that I was born.
*  But I in 2002, I made a website called the Complexity Zoo
*  to answer your question, where I just tried to catalog
*  the different complexity classes, which are classes of problems
*  that are solvable with different kinds of resources. Right. OK.
*  So these are kind of, you know, you could think of complexity classes
*  as like being almost to to to theoretical computer science,
*  like what the elements are to chemistry. Right.
*  They're sort of, you know, there are our most basic objects in a certain way.
*  I feel like the elements have
*  have a characteristic to them where you can't just add an infinite number.
*  Well, you could, but beyond a certain point, they become unstable.
*  Right. Right. So it's like, you know, in theory, you can have atoms with,
*  you know, and look, look, I mean, I mean, I mean, a neutron star,
*  you know, is a nucleus with, you know,
*  uncalled billions of of of of of of of of of neutrons in it, of of hadrons in it.
*  OK. But, you know, for for sort of normal atoms, right,
*  probably you can't get much above 100, you know, atomic weight, 150 or so.
*  Or sorry, sorry. I mean, I mean, beyond 150 or so protons without it,
*  you know, very quickly fissioning with complexity classes.
*  Well, yeah, you can have an infinity of complexity classes.
*  But, you know, maybe there's only a finite number of them
*  that are particularly interesting, right?
*  Just like with anything else, you know, you you care about some more than about others.
*  So what kind of interesting classes are there?
*  Yeah. I mean, you can have just maybe say what are the if you take
*  any kind of computer science class, what are the classes you learn?
*  Good. Let me let me tell you sort of the the the biggest ones,
*  the ones that you would learn first.
*  So, you know, first of all, there is P.
*  That's what it's called.
*  It stands for polynomial time.
*  And this is just the class of all of the problems that you could solve
*  with a conventional computer like your iPhone or your laptop,
*  you know, by a completely deterministic algorithm, right?
*  Using a number of steps that grows only like the size of the input
*  raised to some fixed power.
*  OK, so if your algorithm is linear time, like, you know,
*  for adding numbers, that that problem is in P.
*  If you have an algorithm that's quadratic time,
*  like the elementary school algorithm for multiplying two numbers, that's also in P.
*  Even if it was the size of the input to the tenth power or to the fiftieth power.
*  Well, that wouldn't be very good in practice.
*  But, you know, formally, we would still count that that would still be in P.
*  OK, but if your algorithm takes exponential time,
*  meaning like if every time I add one more data point to your input,
*  if the time needed by the algorithm doubles,
*  if you need time like two to the power of the amount of input data,
*  then that is that we call an exponential time algorithm.
*  OK, and that is not polynomial.
*  OK, so P is all of the problems that have some polynomial time algorithm.
*  OK, so that includes most of what we do with our computers on a day to day basis.
*  You know, all the, you know, sort sorting, basic arithmetic,
*  you know, whatever is going on in your email reader or an Angry Birds.
*  OK, it's all it's all in P.
*  Then the next super important class is called NP.
*  That stands for non deterministic polynomial.
*  OK, does not stand for not polynomial, which is a common confusion.
*  But NP was basically all of the problems where if there is a solution,
*  then it is easy to check the solution if someone shows it to you.
*  OK, so actually a perfect example of a problem in NP is factoring.
*  The one I told you about before, like if I gave you a number with thousands of digits
*  and I told you that, you know, I asked you, does this does this have at least
*  three non trivial divisors?
*  Right. That might be a super hard problem to solve.
*  Right. Might take you millions of years using any algorithm that's known,
*  at least running on our existing computers.
*  OK, but if I simply showed you the divisors, I said, here are three divisors of this number,
*  then it would be very easy for you to ask your computer to just check each one and see if it works.
*  Just divide it in, see if there's any remainder.
*  Right. And if they all go in, then you've checked.
*  Well, I guess there were. Right.
*  So to any problem where, you know, wherever there's a solution,
*  there is a short witness that can be easily like a polynomial size witness
*  that can be checked in polynomial time that we call an NP problem.
*  OK. Beautiful. And yes.
*  So so every problem that's in P is also an NP.
*  Right. Because, you know, you could always just ignore the witness and just,
*  you know, if a problem is in P, you can just solve it yourself. Right.
*  OK. But now the in some sense, the central,
*  you know, mystery of theoretical computer science is is every NP problem in P.
*  So if you can easily check the answer to a computational problem,
*  does that mean that you can also easily find the answer?
*  Even though there's all these problems that appear to be very difficult to find the answer.
*  It's still an open question whether a good answer exists.
*  So what's yours? No one has proven that there's no way to do it.
*  It's arguably the most, I don't know, the most famous, the most maybe interesting.
*  Maybe disagree with that problem in theoretical computer science.
*  So what's your most famous for sure?
*  P equals NP. Yeah.
*  If you were to bet all your money, where do you put your money?
*  That's an easy one. P is not equal to NP.
*  OK, so I like to say that if we were physicists,
*  we would have just declared that to be a law of nature.
*  You know, just like just like thermodynamics, hilarious.
*  Given ourselves Nobel prizes for discovery. Yeah, yeah.
*  No, and look, if later if later it turned out that we were wrong,
*  we just give ourselves more Nobel prizes. Yeah.
*  I mean, you know, but yeah, because we're so harsh, but so true.
*  I mean, no, I mean, I mean, it's really just because we are mathematicians
*  or descended from mathematicians, you know, we have to call things conjectures
*  that other people would just call empirical facts or discoveries. Right.
*  But one shouldn't read more into that difference in language,
*  you know, about the underlying truth.
*  So, OK, so you're a good investor and good spender of money.
*  So then let me know that.
*  Let me ask another way. Yeah. Is it possible at all?
*  And what would that look like if P indeed equals NP?
*  Well, I do think that it's possible.
*  I mean, in fact, you know, when people really pressed me on my blog
*  for what odds would I put, you know, two or three percent odds.
*  Wow, that's pretty good. That P equals NP.
*  Yeah, just because, you know, when people I mean,
*  I mean, you really have to think about, like, if there were 50,
*  you know, mysteries like P versus NP, and if I made a guess
*  about every single one of them, would I expect to be right 50 times?
*  And the truthful answer is no. OK. Yeah.
*  So, you know, and that's what you really mean in saying that,
*  you know, you have, you know, better than 98 percent odds for something.
*  OK, but so so, yeah, you know, I mean, there could certainly be surprises.
*  And look, if P equals NP, well, then there would be the further question of,
*  you know, is the algorithm actually efficient in practice?
*  I mean, Don Knuth, who I know that you've interviewed as well, right?
*  He likes to conjecture that P equals NP,
*  but that the algorithm is so inefficient that it doesn't matter anyway.
*  Right now, I don't know. I've listened to him say that.
*  I don't know whether he says that just because he has an actual reason
*  for thinking it's true or just because it sounds cool. Yeah. OK.
*  But but, you know, that's a logical possibility, right?
*  That the algorithm could be end to the 10000 time
*  or it could even just be N squared time, but with a leading constant of
*  it could be a Google times N squared or something like that.
*  And in that case, the fact that P equals NP, well, it would
*  you know, ravage the whole theory of complexity.
*  We would have to, you know, rebuild from the ground up.
*  But in practical terms, it might mean very little, right?
*  It if the algorithm was too inefficient to run,
*  if the algorithm could actually be run in practice,
*  like if it had small enough constants, you know, or if you could improve it
*  to where it had small enough constants that was efficient in practice,
*  then that would change the world. OK.
*  You think it would have like what kind of impact?
*  Well, OK. I mean, I mean, here's an example.
*  I mean, you could well, OK, just for starters,
*  you could break basically all of the encryption that people use to protect the Internet.
*  You could you could break Bitcoin and every other cryptocurrency or, you know,
*  a mine as much Bitcoin as you wanted. Right.
*  You know, become a, you know, become a super duper billionaire. Right.
*  And then and then plot your next move. Right.
*  OK, that's just for starters. Right.
*  Now, your next move might be something like,
*  you know, you now have like a theoretically optimal way to train any neural network,
*  to find parameters for any neural network. Right.
*  So you could now say, like, is there any small neural network
*  that generates the entire content of Wikipedia? Right.
*  If you know, and now the question is not, can you find it?
*  The question has been reduced to does that exist or not? Yes.
*  If it does exist, then the answer would be yes, you can find it.
*  OK, if if you had this algorithm in your hands, OK, you could ask your computer,
*  you know, I mean, I mean,
*  P versus NP is one of these seven problems that carries this million dollar prize
*  from the Clay Foundation.
*  You know, if you solve it, you know, others are the Riemann hypothesis,
*  the punk array conjecture, which was solved, although the solver turned down the prize.
*  Right. And and and for others.
*  But what I like to say, the way that we can see that P versus NP
*  is the biggest of all of these questions is that if you had this fast algorithm,
*  then you could solve all seven of them.
*  OK, you just ask your computer, you know, is there a short proof of the Riemann
*  hypothesis, right? You know, that a machine could in a language
*  where a machine could verify it.
*  And provided that such a proof exists, then your computer finds it
*  in a short amount of time without having to do a brute force search.
*  OK, so I mean, I mean, those are the stakes of what we're talking about.
*  But I hope that also helps to give your listeners
*  some intuition of why I and most of my colleagues would put our money on P,
*  not equaling NP. Is it possible?
*  I apologize. This is a really dumb question, but is it possible to
*  that a proof will come out that P equals NP,
*  but an algorithm that makes P equals NP is impossible to find?
*  Is that like crazy?
*  OK, well, if P equals NP, it would mean that there is such an algorithm.
*  That it exists, yeah.
*  But, you know, it would mean that it exists.
*  Now, you know, in practice, normally the way that we would prove anything
*  like that would be by finding the algorithm.
*  Finding one algorithm.
*  But there is such a thing as a non constructive proof that an algorithm exists.
*  You know, this is really only reared its head, I think, a few times
*  in the history of our field. Right.
*  But, you know, it is it is theoretically possible that that that that
*  that such a thing could happen.
*  But, you know, there are so even here, there are some amusing
*  observations that one could make.
*  So there is this famous observation of Leonid Levin,
*  who is, you know, one of the original discoverers of NP completeness. Right.
*  And he said, well, consider the following algorithm that, like, I guarantee
*  will solve the NP problems efficiently, just as provided that P equals NP.
*  OK, here is what it does.
*  It just runs, you know, it enumerates every possible algorithm
*  in a gigantic, infinite list. Yeah. Right.
*  From like in like alphabetical order. Right.
*  You know, and many of them maybe won't even compile.
*  So we just ignore those. OK.
*  But now we just, you know, run the first algorithm.
*  Then we run the second algorithm.
*  We run the first one a little bit more.
*  Then we run the first three algorithms for a while.
*  We run the first four for a while.
*  This is called dovetailing, by the way.
*  This is a known trick in
*  theoretical computer science. OK.
*  But we do it in such a way that, you know, whatever is the algorithm
*  out there in in in our list that solves NP complete,
*  you know, the NP problems efficiently will eventually hit that one. Right.
*  And now the key is that whenever we hit that one, you know, it
*  by assumption, it has to solve the problem, has to find a solution.
*  And once it claims to find a solution, then we can check that ourselves.
*  Right. Because there are these are problems.
*  Yeah. Then we can check it.
*  Now, this is utterly impractical. Right.
*  You know, you'd have to do this enormous exhaustive search among all the algorithms.
*  But from a certain theoretical standpoint, that is merely a constant pre factor.
*  It's at least possible.
*  That's merely a multiplier of your running time.
*  So there are tricks like that one can do to say that in some sense,
*  the algorithm would have to be constructive.
*  But, you know, in in in the human sense, you know, it is possible that to,
*  you know, it's conceivable that one could prove such a thing
*  via a non constructive method.
*  Is that likely? I don't think so.
*  Not not personally.
*  So that's P and NP.
*  But the complex is full of wonderful creatures.
*  Well, it's got about 500 of them. 500.
*  So how do you get?
*  Yeah. Yeah. How do you get more?
*  How do you? Yeah.
*  Well, I mean, I mean, I mean, I mean, just for starters,
*  there is everything that we could do with a conventional computer
*  with a polynomial amount of memory.
*  But possibly an exponential amount of time,
*  because we get to reuse the same memory over and over again.
*  OK, that is called peace space.
*  OK, and that's actually a we think an even larger class than NP.
*  Well, P is contained in NP, which is contained in peace space.
*  And we think that those containments are strict.
*  And the constraint there is on the memory.
*  The memory has to grow with polynomial with the size of the.
*  That's right. That's right.
*  But in peace space, we now have interesting things that we're not in NP.
*  Like as a famous example, you know, from a given position in chess,
*  you know, does white or black have the win?
*  Let's say assuming provided that the game
*  lasts only for a reasonable number of moves.
*  OK, or or or or likewise for go.
*  OK, and you know, even for the generalizations of these games to arbitrary
*  size boards, because with an eight by eight board,
*  you could say that's just a constant size problem.
*  You just, you know, in principle, you just solve it in all of one time. Right.
*  But so we really mean the the generalizations of, you know,
*  games to arbitrary size boards here.
*  Or another thing in peace space would be like, I give you some really hard
*  constraint satisfaction problem like, you know, you know,
*  a traveling salesperson or, you know, packing boxes into the trunk of your car
*  or something like that.
*  And I ask not just is there a solution, which would be an NP problem,
*  but I ask how many solutions are there? OK, that, you know,
*  count the number of of of of valid solutions that that that actually gives
*  those problems lie in a complexity class called sharp P or like it looks like
*  hashtag, like hashtag P got it, which sits between NP and peace space.
*  There's all the problems that you can do in exponential time.
*  OK, that's called X.
*  So and by the way, it was proven in the 60s that X is larger than P.
*  OK, so we know that much.
*  We know that there are problems that are solvable in exponential time
*  that are not solvable in polynomial time. OK.
*  In fact, we even know we know that there are problems
*  that are solvable in N cube time that are not solvable in N squared time.
*  And that those don't help us with a controversy between P and NP.
*  Unfortunately, it seems not or certainly not yet. Right.
*  The the the the techniques that we use to establish those things.
*  They're very, very related to how touring prove the unsolvability
*  of the halting problem.
*  But they seem to break down when we're comparing two different resources
*  like time versus space or like, you know, P versus NP.
*  OK, but, you know, I mean, there's there's what you can do
*  with a randomized algorithm, right, that can sometimes, you know, with some
*  has some probability of making a mistake.
*  That's called BPP, bounded error probabilistic polynomial time.
*  And then, of course, there's one that's very close to my own heart.
*  What you can efficiently do, do in polynomial time using a quantum computer.
*  And that's called BQP.
*  Right. And so, you know, what's understood about that class?
*  Maybe there's a common.
*  So P is contained in BPP, which is contained in BQP,
*  which is contained in P space.
*  OK, so anything you can, in fact, in like in something very similar to sharp P.
*  BQP is basically, you know, well, it's contained in like P
*  with the magic power to solve sharp P problems.
*  OK, why is BQP contained in P space?
*  Oh, that's an excellent question.
*  So there is what I mean, one has to prove that.
*  But the proof you could you could think of it as using Richard Feynman's
*  picture of quantum mechanics, which is that you can always, you know,
*  we haven't really talked about quantum mechanics in this in this conversation.
*  We we did in our previous.
*  Yeah, we did last time. But yeah, we did last time.
*  OK, but but basically you could always think of
*  a quantum computation as like a branching tree of possibilities
*  where each possible path that you could take through, you know,
*  your the space has a complex number attached to it called an amplitude.
*  And now the rule is, you know, when you make a measurement at the end,
*  will you see a random answer?
*  OK, but quantum mechanics is all about calculating the probability
*  that you're going to see one potential answer versus another one.
*  Right. And the rule for calculating the probability
*  that you'll see some answer is that you have to add up the amplitudes
*  for all of the paths that could have led to that answer.
*  And then, you know, that's a complex number.
*  So, you know, how could that be a probability?
*  Then you take the squared absolute value of the result.
*  That gives you a number between zero and one.
*  OK, so I just I just summarized quantum mechanics in like 30 seconds.
*  OK, but now, you know, what this already tells us
*  is that anything I can do with a quantum computer,
*  I could simulate with a classical computer
*  if I only have exponentially more time.
*  OK, and why is that?
*  Because if I have exponential time,
*  I could just write down this entire branching tree
*  and just explicitly calculate each of these amplitudes. Right.
*  You know, that will be very inefficient, but it will work. Right.
*  It's enough to show that quantum computers could not solve the halting problem.
*  Or, you know, they could never do anything that is literally uncomputable
*  in Turing sense. OK, but now, as I said, there is even a stronger result,
*  which says that BQP is contained in P space.
*  The way that we prove that is that we say if all I want is to calculate
*  the probability of some particular output happening,
*  which is all I need to simulate a quantum computer, really,
*  then I don't need to write down the entire quantum state,
*  which is an exponentially large object.
*  All I need to do is just calculate what is the amplitude for that final state.
*  And to do that, I just have to sum up
*  all the amplitudes that lead to that state.
*  OK, so that's an exponentially large sum, but I can calculate it
*  just reusing the same memory over and over for each term in the sum.
*  Hence, hence the P in the P space. Yeah.
*  Yeah. So what out of that whole complexity zoo, it could be BQP.
*  What do you find is the most
*  the class that captured your heart the most, the most beautiful class?
*  It's just well, yeah, I used as my email address
*  BQP QPolly at Gmail dot com.
*  Yes, because BQP slash QPolly.
*  Well, you know, amazingly, no one had taken it. Amazing.
*  But you know, but this is a class that I was involved in, sort of
*  defining, proving the first theorems about in 2003 or so.
*  So it was kind of close to my heart.
*  But this is like if we extended BQP,
*  which is the class of everything we can do efficiently with a quantum computer
*  to allow quantum advice, which means imagine that you had some
*  special initial state that could somehow help you do computation.
*  And maybe such a state would be exponentially hard to prepare.
*  But, you know, maybe somehow these states were formed in the Big Bang or something,
*  and they've just been sitting around ever since. Right.
*  If you found one and if this state could be like ultra power,
*  there are no limits on how powerful it could be,
*  except that this state doesn't know in advance which input you've got.
*  It only knows the size of your input.
*  You know, and that's BQP slash QPolly.
*  So that's that's one that I just personally happen to love. OK. But,
*  you know, if you're asking like what's the you know, there's a class
*  that I think is is is way more beautiful than, you know, or fundamental
*  than a lot of people even within this this field realize that it is.
*  That class is called SCK or statistical zero knowledge.
*  And, you know, there's a very, very easy way to define this class,
*  which is to say, suppose that I have two algorithms
*  that each sample from probability distributions. Right.
*  So each one just outputs random samples according to, you know,
*  possibly different distributions.
*  And now the question I ask is, you know, you know,
*  let's say distributions over strings of n bits, you know,
*  so over an exponentially large space.
*  Now I ask, are these two distributions close or close?
*  Or far as probability distributions?
*  OK. Any problem that can be reduced to that,
*  you know, that can be put into that form is an SCK problem.
*  And the way that this class was originally discovered
*  was completely different from that and was kind of more complicated.
*  It was discovered as the class of all of the problems
*  that have a certain kind of what's called zero knowledge proof.
*  Zero knowledge proofs are one of the central ideas in cryptography.
*  You know, Shafi Goldwasser and Silvio Macaulay won the Turing Award
*  for inventing them, and they're at the core of even some some
*  crypto currencies that, you know, people people use nowadays.
*  But there are zero knowledge proofs or ways of proving to someone
*  that something is true, like, you know, that there is a solution
*  to this, you know, optimization problem or that these two graphs
*  are isomorphic to each other or something, but without revealing
*  why it's true, without revealing anything about why it's true.
*  OK. SCK is all of the problems
*  for which there is such a proof that doesn't rely on any cryptography.
*  OK. And if you wonder, like, how could such a thing possibly exist?
*  Right. Well, like, imagine that I had two graphs
*  and I wanted to convince you that these two graphs are not isomorphic,
*  meaning, you know, I cannot permute one of them
*  so that it's the same as the other one. Right.
*  You know, that might be a very hard statement to prove.
*  Like I might need, you know, you might have to do a very exhaustive
*  enumeration of, you know, all the different permutations
*  before you were convinced that it was true.
*  But what if there were some all knowing wizard that said to you, look,
*  I'll tell you what, just pick one of the graphs randomly,
*  then randomly permute it, then send it to me
*  and I will tell you which graph you started with.
*  OK. And I will do that every single time.
*  Right. And let that in. OK, that's I got it.
*  I got it. And let's say that that wizard did that a hundred times
*  and it was right every time. Yeah. Right.
*  Now, if the graphs were isomorphic, then, you know, it would have been
*  flipping a coin each time. Right.
*  It would have had only a one and two to the one hundred power chance of,
*  you know, of guessing right each time.
*  But, you know, so so if it's right every time, then now you're statistically
*  convinced that these graphs are not isomorphic,
*  even though you've learned nothing new about why they are so far.
*  So, yeah. So so SDK is all of the problems that have protocols like that one.
*  But it has this beautiful other characterization.
*  It's shown up again and again in my in my own work.
*  And, you know, a lot of people's work.
*  And I think that it really is one of the most fundamental classes.
*  It's just that people didn't realize that when it was first discovered.
*  So we're living in the middle of a pandemic currently.
*  Yeah. How has your life been changed?
*  And no, better to ask, like, how is your perspective of the world change
*  with this world changing event of a pandemic overtaking the entire world?
*  Yeah. Well, I mean, I mean, all of our lives have changed, you know, like,
*  I guess, as with no other event since I was born, you know,
*  you would have to go back to World War Two for something.
*  I think of this magnitude, you know, on, you know, the way that we live our lives.
*  As for how it has changed my world view,
*  I think that the the failure of institutions,
*  you know, like like like the CDC, like, you know, other institutions
*  that we sort of thought were trustworthy, like a lot of the media was staggering,
*  was was absolutely breathtaking.
*  It is something that I would not have predicted. Right.
*  I think I wrote on my blog that, you know,
*  it's it's it's fascinating to like
*  rewatch the movie Contagion from a decade ago, right.
*  That correctly foresaw so many aspects of, you know, what was going on.
*  You know, a an airborne, you know, virus originates in China,
*  spreads to, you know, much of the world, you know, shuts everything down
*  until a vaccine can be developed.
*  You know, everyone has to stay at home.
*  You know, you know, it gets, you know, an enormous number of things.
*  Right. OK. But the one thing that they could not imagine,
*  you know, is that like in this movie, everyone from the government is like
*  hyper competent, hyper, you know, dedicated to the public good.
*  Right. And that's the best.
*  You know, yeah, they're the they're the best of the best.
*  You know, they could, you know, and there are these conspiracy theorists, right,
*  who think, you know, you know, this is all fake news.
*  There's no there's not really a pandemic.
*  And those are some random people on the Internet
*  who the hyper competent government people have to, you know, oppose.
*  Right. They, you know, in trying to envision the worst thing that could happen.
*  Like, you know, the the there was a failure of imagination.
*  The moviemakers did not imagine that the conspiracy theorists and the,
*  you know, and the incompetence in the nut cases would have captured
*  our institutions and be the ones actually running things.
*  So you had a certain. Yeah.
*  I love competence in all walks of life.
*  I love I get so much energy.
*  I'm so excited by people who do amazing job.
*  And I like you.
*  Well, maybe you can clarify, but I had maybe not intuition,
*  but I hope that government at its best could be ultra competent.
*  What first of all, two questions like, how do you explain the lack of confidence?
*  And the other maybe on the positive side,
*  how can we build a more competent government?
*  Well, there's an election in two months.
*  I mean, you know, you have a faith that the election.
*  I, you know, it's not going to fix everything.
*  But, you know, it's like I feel like there is a ship that is sinking
*  and you could at least stop the sinking.
*  But, you know, I think that there are there are much, much deeper problems.
*  I mean, I think that, you know, it is it is plausible to me that,
*  you know, a lot of the the failures, you know, with the CDC,
*  with some of the other health agencies even, you know, you know, predate Trump,
*  you know, predate the right wing populism that is sort of taken over much of the world now.
*  And, you know, I think that, you know, it was is, you know, it is very I'm actually,
*  you know, I've actually been strongly in favor of, you know, rushing vaccines of,
*  you know, I thought that we could have done, you know, human human challenge trials,
*  you know, which were not done right.
*  We could have, you know, like I had, you know, volunteers, you know, to actually,
*  you know, be, you know, get vaccines, get, you know, exposed to covid.
*  So innovative ways of accelerating what we've done previously over a long time.
*  I thought that, you know, each each month that you that that a vaccine is closer
*  is like trillions of dollars.
*  Are you surprised?
*  And of course, lives, you know, at least, you know, hundreds of thousands of lives.
*  Are you surprised that it's taking this long?
*  We still don't have a plan.
*  There's still not a feeling like anyone is actually doing anything in terms of
*  alleviate like any kind of plan.
*  So there's a bunch of stuff, this vaccine.
*  But you could also do a testing infrastructure where, yeah,
*  everybody's tested nonstop with contact tracing, all that kind of.
*  Well, I mean, I'm as surprised as almost everyone else.
*  I mean, this is a historic failure.
*  It is one of the biggest failures in the 240 year history of the United States.
*  Right. And we should be crystal clear about that.
*  And, you know, one thing that I think has been missing, you know, even
*  even from the more competent side is like, you know, is sort of the
*  the World War Two mentality, right?
*  The, you know, the mentality of, you know, let's just, you know,
*  you know, if if if we can, by breaking a whole bunch of rules,
*  you know, get a vaccine and, you know, and even half the amount of time
*  as we thought, then let's just do that because, you know,
*  you know, like like we have to we have to weigh all of the moral qualms
*  that we have about doing that against the moral qualms of not doing.
*  And one key little aspect to that that's deeply important to me.
*  And we'll go to that topic next is
*  the World War Two mentality wasn't just about, you know,
*  breaking all the rules to get the job done.
*  There was a togetherness to it. There's yes.
*  So I would if I were president right now, it seems
*  quite elementary to unite the country because we're facing a crisis.
*  It's easy to make the virus the enemy.
*  And it's very surprising to me that the division is increased
*  as opposed to decrease. Yeah.
*  That that's that's heartbreaking. Yeah. Well, look, I mean, it's been said
*  by others that this is the first time in the country's history
*  that we have a president who does not even pretend to, you know,
*  want to unite the country. Right. Yeah.
*  You know, I mean, I mean, I mean, Lincoln, who fought a civil war,
*  you know, you know, said he wanted to unite the country. Right.
*  You know, and and I do I do worry enormously about what happens
*  if the results of this election are contested, you know, and, you know,
*  will there be violence as a result of that?
*  And will we have a clear path of succession?
*  And, you know, look, I mean, you know, this is all we're we're going to find out
*  the answers to this in two months.
*  And if none of that happens, maybe I'll look foolish.
*  But I am willing to go on the record and say, I am terrified about that.
*  Yeah, I've been reading the rise and fall, the third right.
*  There's it's difficult.
*  So if I can, this this is like one little voice
*  just to put out there that I think November
*  will be a really critical month for people to breathe and put love out there.
*  Do not, you know, anger in those in that context, no matter who wins,
*  no matter what is said will destroy our country, may destroy our country,
*  may destroy the world because of the power of the country.
*  So it's really important to be patient, loving, empathetic.
*  Like one of the things that troubles me is that even people on the left
*  are unable to have a love and respect for people who voted for Trump.
*  They can't imagine that there's good people that could vote for the outside.
*  And that's oh, I know there are because I know some of them. Yeah. Right.
*  I mean, you know, it's still, you know, maybe it baffles me.
*  But, you know, I know such people.
*  Let me ask you this.
*  It's also heartbreaking to me on the topic of cancel culture.
*  Yeah. So in the machine learning community, I've seen it a little bit that there's
*  aggressive attacking of people who are trying to have a nuanced
*  conversation about things.
*  And it's troubling because it feels like nuanced
*  conversation is the only way to talk about difficult topics.
*  And when there's a thought police and speech police
*  on any nuanced conversation that everybody has to, like in a animal farm,
*  chant that racism is bad and sexism is bad, which is things that everybody believes.
*  And they can't possibly say anything nuanced.
*  It feels like it goes against any kind of progress from my kind of shallow perspective.
*  But you've written a little bit about cancel culture.
*  Is you have thoughts there?
*  Well, I mean, I mean, I mean, I mean, to say that I am opposed to, you know,
*  the this trend of cancellations or, you know, shouting people down
*  rather than engaging them, that would be a massive understatement. Right.
*  And I feel like, you know, I have put my money where my mouth is,
*  you know, not as much as some people have.
*  But, you know, I've tried to do something.
*  I mean, I have defended, you know, some unpopular people and unpopular,
*  you know, ideas on my blog.
*  I've, you know, tried to defend, you know, norms of
*  of of open discourse, of, you know, reasoning with our opponents,
*  even when I've been shouted down for that on social media,
*  you know, called a racist, called a sexist, all of those things.
*  Which, by the way, I should say, you know, I would be perfectly happy to,
*  you know, say, you know, if we had time to say, you know, you know, ten thousand times,
*  you know, my hatred of racism, of sexism, of homophobia. Right.
*  But what I don't want to do is to cede to
*  some particular political faction the right to define
*  exactly what is meant by those terms, to say, well, then you have to agree
*  with all of these other extremely contentious positions,
*  or else you are a misogynist or else you are a racist. Right.
*  I say that, well, no, you know, you know, don't like.
*  Don't I or, you know, don't people like me also get a say in the discussion
*  about, you know, what is racism, about what is going to be the most effective
*  to combat racism. Right.
*  And, you know, this this this cancellation mentality,
*  I think, is spectacularly ineffective at its own professed goal of,
*  you know, combating racism and sexism.
*  What's a positive way out?
*  So I I try to I don't know if you see what I do on Twitter,
*  but I on Twitter, I mostly in my whole in my life,
*  I've actually is who I am to the core is like I really focus on the positive
*  and I try to put love out there in the world. Yeah. And still.
*  I get attacked and I look at that and I wonder like you too.
*  I didn't know.
*  Like I haven't actually said anything difficult and nuanced.
*  You talk about somebody like Steven Pinker. Yeah.
*  Who I actually don't know the full range of things that
*  that he's attacked for, but he tries to say difficult.
*  He tries to be thoughtful about difficult topics. He does.
*  And obviously, he just gets slaughtered by.
*  Well, I mean, I mean, I mean, I mean, yes,
*  but it's also amazing how well Steve has withstood it.
*  I mean, he just survived that attempt to cancel him just a couple of months ago.
*  Right. Psychologically, he survives it too, which worries me.
*  I don't think I can. Yeah. I've gotten to know Steve a bit.
*  He is incredibly unperturbed by this stuff.
*  And I admire that and I envy it.
*  I wish that I could be like that.
*  I mean, my impulse when I'm getting attacked is I just want to engage
*  every single like anonymous person on Twitter and Reddit
*  who is saying mean stuff about me.
*  And I want to say, look, can we just talk this over for an hour?
*  And then, you know, you'll see that I'm not that bad.
*  And sometimes that even works.
*  The problem is then there's the, you know, the twenty thousand other ones.
*  Yeah. And that's not but psychologically, does that wear on you?
*  It does. It does.
*  But yeah, I mean, in terms of what is the solution, I mean, I wish I knew.
*  Right. And so, you know, in a certain way,
*  these problems are maybe harder than P versus NP. Right.
*  I mean, you know, but but I think that part of it has to be for,
*  you know, that I think that there is a lot of sort of silent support
*  for what I'll call the the the open discourse side, the,
*  you know, reasonable enlightenment side.
*  And I think that that that support has to become less silent. Right.
*  I think that a lot of people
*  sort of, you know, like agree that, you know, a lot of these
*  cancellations and attacks are ridiculous, but are just afraid to say so.
*  Right. Or else they'll get they'll get shouted down as well. Right.
*  That's just the standard witch hunt dynamic, which, you know, of course, this,
*  you know, this faction understands and exploits to its great advantage.
*  But, you know, more people just, you know, said,
*  you know, like, we're not going to stand for this. Right.
*  You know, you know, this is this is, you know, we're guess what?
*  We're against racism, too.
*  But, you know, this, you know, what you're doing is ridiculous. Right.
*  No. And the hard part is like it takes a lot of mental energy.
*  It takes a lot of time.
*  You know, even if you feel like you're not going to be canceled or,
*  you know, you're staying on the safe side, like it takes a lot of time to to
*  to phrase things in exactly the right way and to, you know,
*  respond to everything people say.
*  So but I think that, you know, the more people speak up, then,
*  you know, from from from all political persuasions, you know, from like all,
*  you know, walks of life, then, you know, the easier it is to move forward.
*  Since we've been talking about love,
*  can you last time I talked to you about the meaning of life a little bit.
*  But here has it's a weird question to ask a computer scientist, but has love
*  for other human beings, for for things, for the world around you
*  played an important role in your life? Have you?
*  You know, it's easy for a world class computer scientist.
*  Yeah, you could even call yourself like a physicist.
*  Everything to be lost in the books is a connection to other humans.
*  Love for other humans played an important role.
*  I love my kids.
*  I love my wife. I love my parents.
*  You know, I
*  am probably not not different from most people in loving their families
*  and and in that being very important in my life.
*  Now, I should remind you that, you know, I am a theoretical computer scientist.
*  If you're looking for deep insight about the nature of love,
*  you're probably looking in the wrong place to ask me.
*  But but sure, it's been important.
*  But is that is there something from a computer science perspective
*  to be said about love?
*  Is there or is that is that even beyond into the realm of
*  beyond the realm of consciousness?
*  There was there was this great
*  cartoon, I think it was one of the classic XK CDs where it shows like a heart.
*  And it's like, you know, squaring the heart,
*  taking the Fourier transform of the heart, you know, integrating the heart, you know,
*  you know, each each thing.
*  And then it says, you know, my normal approach is useless here.
*  I'm so glad I asked this question.
*  I think there's no better way to to end this.
*  I hope we get a chance to talk again.
*  This is an amazing, cool experiment to do it outside.
*  Yeah, really glad you made it out.
*  Yeah, well, I appreciate it a lot.
*  It's been a pleasure.
*  And I'm glad you were able to come out to Austin. Thanks.
*  Thanks for listening to this conversation with Scott Aronson.
*  And thank you to our sponsors,
*  Eight Sleep, Simply Safe, ExpressVPN and BetterHelp.
*  Please check out these sponsors in the description
*  to get a discount and to support this podcast.
*  If you enjoy this thing, subscribe on YouTube,
*  review it with five stars and up a podcast.
*  Follow on Spotify, support on Patreon or connect with me on Twitter at Lex Friedman.
*  And now let me leave you with some words from Scott Aronson
*  that I also gave to you in the introduction, which is,
*  if you always win, then you're probably doing something wrong.
*  Thank you for listening and for putting up with the intro
*  and outro in this strange room in the middle of nowhere.
*  And I very much hope to see you next time.
*  In many more ways than one.

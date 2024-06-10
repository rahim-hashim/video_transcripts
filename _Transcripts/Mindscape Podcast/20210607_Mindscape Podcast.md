---
Date Generated: June 09, 2024
Transcription Model: whisper medium 20231117
Length: 5568s
Video Keywords: ['explanation']
Video Views: 12999
Video Rating: None
Video Description: Patreon: https://www.patreon.com/seanmcarroll
Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2021/06/07/x-simon-dedeo-on-how-explanations-work-and-why-they-sometimes-fail/

You observe a phenomenon, and come up with an explanation for it. That’s true for scientists, but also for literally every person. (Why won’t my car start? I bet it’s out of gas.) But there are literally an infinite number of possible explanations for every phenomenon we observe. How do we invent ones we think are promising, and then decide between them once invented? Simon DeDeo (in collaboration with Zachary Wojtowicz) has proposed a way to connect explanatory values (“simplicity,” “fitting the data,” etc) to specific mathematical expressions in Bayesian reasoning. We talk about what makes explanations good, and how they can get out of control, leading to conspiracy theories or general crackpottery, from QAnon to flat earthers.

Simon DeDeo received his Ph.D. in astrophysics from Princeton University. He is currently an Assistant Professor in Social and Decision Sciences at Carnegie Mellon University, and External Professor at the Santa Fe Institute.

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x

#podcast #ideas #science #philosophy #culture
---

# Mindscape 150 | Simon DeDeo on How Explanations Work and Why They Sometimes Fail
**Mindscape Podcast:** [June 07, 2021](https://www.youtube.com/watch?v=IGgmJ788v2A)
*  Hello everyone, welcome to the Mindscape Podcast. I'm your host Sean Carroll. Obviously on a podcast like mine,
*  we're often going to be talking to scientists of various sorts,
*  theoretical scientists in particular, some of my favorites, not all of them, but a lot of times we're talking about the ideas
*  for how we might explain some scientific phenomenon, right? Coming up with a new theory, whether it's dark matter or
*  evolutionary biology or whatever it's going to be. You might remember in fact that I had Lee Smolin on the podcast
*  very recently and despite the fact that we work in very similar areas and we're personally very friendly,
*  we have different ideas about how to go about building the better next generation scientific theories.
*  Why is that? How can two scientists who are both more or less trained in the same way come up with very different
*  preferences when it comes to building new explanations? That's what we're on about today on today's podcast with Simon Dedeo.
*  Simon actually started as a theoretical cosmologist, much like myself,
*  but he switched into some combination of statistics and data-driven social science and cognitive science.
*  So it's a wonderfully difficult specialty to pin down, but he's both at Carnegie Mellon University and also the Santa Fe Institute.
*  So we overlap a lot in our intellectual interests.
*  And what Simon talks about in the paper that we're going to be discussing today is how explanations work.
*  Honestly, explanations in this sense is kind of a synonym for a theoretical viewpoint or formalism to answer some kind of question.
*  So you have some phenomenon, whether it's my car broke down or there's dark matter in the universe, and you want to explain it.
*  Now what happens is you can invent an explanation and different people will prefer different kinds of explanations for different reasons.
*  So what Simon and his collaborators have done is to break down the different parts of Bayesian analysis that go into making a good explanation and sort of
*  quantify different preferences or different values you may have for choosing your personal preferred kind of explanation.
*  Right. Explanations have different kinds of good aspects.
*  An explanation can be simple. It can be powerful.
*  It can be close to things we already understand.
*  It can explain many things at once.
*  These are all good things, but sometimes they fight against each other.
*  Sometimes an explanation can be simple, but not powerful.
*  It's simple for only one phenomenon or it's both simple and powerful, but utterly different than anything we know.
*  So how to balance these is kind of a human subjective thing.
*  And we talk about both how scientists actually do this when you have legitimate scientific disagreements.
*  You know, the many worlds interpretation of quantum mechanics versus the Copenhagen interpretation or pilot wave theories or something like that.
*  What are the different values that the practitioners have that allow them to prefer in an intellectually respectable way these different explanations in a situation where we don't know which one is right yet.
*  And what's fascinating about Simon's analysis is it goes beyond the case where everything's working.
*  Right. You know, I can say that I like many worlds as my favorite theory,
*  but I have absolute respect for people who don't if they have principled reasons for preferring some other things.
*  Sometimes people pick wrong explanations because they're failing at balancing these different kinds of values.
*  So there's sort of a continuum between high level scientific discourse about unknown theories and complete crazy talk conspiracy theories.
*  You know, why do people believe QAnon or that school shootings or false flag operations or something like that?
*  Well, you can understand that in terms of them putting all of their eggs in one explanatory basket.
*  All of their values are concentrated on comprehensiveness and rather than simplicity or something like that.
*  So it's not just that there are sensible people in crackpots.
*  There's a continuum of ways that we can try to explain the world.
*  And you can try to analyze the similarities and differences between conspiracy theorists and the world's best theoretical physicists.
*  OK, it gives you a lot of food for thought about how we go about explaining things in our everyday lives.
*  So with that, let's go.
*  Simon Dedeo, welcome to the Mindscape podcast.
*  Hi, Sean.
*  So we've had a lot of people, at least a few people, talking about misinformation, disinformation, conspiracy theories that people fall in love with, things like that.
*  And I think that what we'll be talking about today, you'll correct me if I'm not getting this exactly right, but rather than focusing on that, you know, the huge wrongness of believing in a conspiracy theory or a crackpot scheme,
*  we're thinking about explanations more broadly and saying that there are people who believe in conspiracy theories or crackpot schemes, but their kind of belief, the way they justify it, etc., is of a piece with perfectly respectable scientific beliefs.
*  We should sort of it's a matter of balancing things here and there rather than a matter of a completely different way of thinking.
*  Is that fair?
*  Yeah, you know, we've been working on these questions for a while.
*  And one of the inspirations for me, at least, was a couple of years ago now, David Deutsch wrote a book called The Beginning of Infinity.
*  Right.
*  And this is a lovely book.
*  It's nuts.
*  But it's lovely.
*  And, you know, Deutsch really focuses on something that I had sort of thought about, but not as clearly for many years, which was this idea that you explain things.
*  Right.
*  And that explanation is not simply, you know, something we do to feel better about the world, but it's actually this enormously generative process.
*  You know, we had this problem.
*  You know, this was this puzzle for me when I first started working outside of physics because people in biology want to predict things, or at least the outside world wants to predict things.
*  Biologists themselves don't usually.
*  When we work on social behavior, people want to say, can you predict the next war or whatever?
*  And so Deutsch really crystallized for me the way in which that's not actually what this game is about.
*  And not only is it not what this game is about, it's like, that's OK.
*  Right.
*  So, you know, the fact that we can't predict things, you know, especially not about the future, is not a sign that we're doing something wrong, but this time we're doing something different.
*  So, you know, Deutsch, that was the sort of way in and that kind of percolated in my head for many years.
*  When I got to CMU, I started working with a graduate student, Zach Vltowicz, and, you know, Zach and I played around with a lot of different ideas.
*  And we started to think about, you know, could we build a theory of explanation making?
*  You know, this, you know, actually, there was another impetus for this, which was, is a logician at CMU, Debbie Borg.
*  And so Debbie and I talked for a while about, there's this joke, right?
*  Why do mathematicians try to prove things they already know are true?
*  Right. Like this is the worst.
*  You know, science is about producing experiments with uncertain outcomes.
*  So, you know, what's the goal of a mathematician?
*  You know, no one's shocked when Fermat's last theorem has no solution.
*  Right. And so, you know, Debbie and I talked about this and, you know, so, you know, just to dig a little into this in science, people have, let's say, tried to even formalize what the next experiment you should do.
*  Is right.
*  So this is called optimal information design, because by any different terms.
*  So you can say, you know, should we build the next Hubble Space Telescope or should we build the LHC?
*  Which one is going to give us more information?
*  Right. And so you pick the one that will give you more information.
*  The one thing you shouldn't do is do an experiment where you are guaranteed to know the outcome.
*  Yeah. So then, you know, we talk and, you know, Debbie and I talking, you say, well, what's why is a mathematician care about proving something they already know is true?
*  And Debbie's answer is something like P versus NP, right?
*  These really challenging problems.
*  One of the intuitions is that the solution is going to discover unexpected connections between very different branches of mathematics.
*  So it'll give us a new view onto things we thought we understood because of the way in which these different chunks have to be brought together.
*  So this is very relevant to my interests, as they say on the Internet,
*  because, of course, in quantum mechanics, we have a situation where generations of physicists have been brainwashed into thinking that we don't need to understand what's happening.
*  All we need to do is make the predictions for the outcomes of observations.
*  And the counterexample I try to say is, look, what if you had a black box into which you could ask literally any outcome of a specific physical situation?
*  Does that count as solving all the physics?
*  Right. You know, anything you want to know.
*  But you have to re-ask it.
*  It doesn't tell you what the theory is.
*  It just tells you when you collide these two billiard balls, they scatter off at this particular angle.
*  I don't think that counts as a good theory of physics.
*  We want the theory for reasons beyond that.
*  Right. Right, right, right.
*  Right. So, you know, if we're building a theory of exactly how to shake the box, like we have a goal in shaking the box in a certain way.
*  Right. And then the question is, yeah, what's the goal?
*  How do we know when we've reached that goal?
*  How do we know if we're on the right track?
*  And so, you know, someone like Deutsch articulates this fact that, you know, what we care about is explanations.
*  Then, you know, Zach and I dig in and we say, all right, let's let's try to build, you know, and this is a joke here.
*  Right. Let's try to build a unified theory of explanation making.
*  And, you know, this then this then rolls into a year of of enormous fun.
*  Right. Trying to make sense of the ways in which you have a whole bunch of different experiments that we do, for example, lab experiments on people and, you know, in a psych lab.
*  Right. Where we say and this is not my work.
*  Tonya Lambrosa is one of the big figures in this.
*  So, you know, you might you might tell somebody, OK, look, there's this alien.
*  Right. These aliens and, you know, they fall victim to these kinds of diseases.
*  And this disease gives these symptoms and that disease gives that symptom.
*  And, you know, this alien comes into your consulting room and he has spots and a cough and, you know, diagnose this alien.
*  And you can look at the different choices people make in a sense of diagnosis by proxy as an explanation for the symptoms that the person brings out, the alien brings in.
*  And so by looking at the choices they make in attributing, let's say, a pair of diseases or a single disease to the alien, you learn a lot about the kind of preferences we have.
*  The ways in which we select explanations, one one from another.
*  And let me just to be super duper clear, we're using the word explanation here almost in the sense of a theory or a model.
*  Right. It's not like someone says, well, explain black holes to me.
*  And we think we know what black holes are.
*  But there's this pedagogical attempt to explain them in a comprehensible way.
*  You're using the word explanation to really mean a knowledge of what is going on behind the scenes that that can help us.
*  And then we can sort of choose between competing explanations that can't all be right.
*  Right. So this is this is great. Right. So, you know, our our model is a Bayesian model, meaning we ask questions about the things we have to hand, say the facts in the world.
*  And we ask the ways in which they match the models we have of the world.
*  And so it's a very specific kind of model.
*  It's a generative model, which says it gives you degrees of belief in the things that could happen.
*  So in that sense, we've really boiled it down to a paradigm that, you know, in one sense, doesn't really match any kind of science we do.
*  Right. Like, you know, condensed matter physics is not a generative model in the sense that it specifies the probability of different things happening.
*  So what is the definition of a generative model?
*  Right. So a generative model tells you not just the things that might happen or the things that could happen, but also gives you degrees of likelihood.
*  OK, for the different things that could happen.
*  It's a way you can think of it as like a mini simulation that you have controls over.
*  So you can see inside the simulator and that simulator, you push a button and it projects a possible world under the screen.
*  Right. So but you asked us, you know, when you asked, what is an explanation more broadly?
*  This gets into a big question that, let's say we can split into two parts.
*  Right. An explanation has to do with empirical facts.
*  Right. It's it's a way of accounting for stuff that has happened.
*  Right. Or stuff, you know.
*  But it's also an account of how that stuff could have happened.
*  And generally, it's an account of other things that might happen, other things you could look for, other things that could happen in the future or were happening somewhere else.
*  So there's sort of two there's sort of two pieces when we think about an explanation, one piece, when we evaluate one one piece is, you know, you asked me to explain this.
*  Right. Can you meaning, can you tell me a story in some way in which the thing that happened comes true?
*  Yeah, sure. Right. So that's kind of this empirical piece.
*  Right. And then this other piece that's sitting there, which is this much troubling piece, is how do I feel about the larger structure of that explanation, including the things that happened?
*  Things that might do for things that could happen in the future, let's say things that I haven't observed yet.
*  Also, things like what does the explanation look like?
*  How succinct is it?
*  How concise is it versus how elaborate it is?
*  So when we refer to things like Occam's razor, what we're talking about is that second chunk.
*  Right. Right. Of the ways in which we might value an explanation.
*  Hiring people for your business is as much about who you say yes to as who you say no to.
*  But it sure helps when you can narrow down the list to only really great choices first.
*  So you're not choosing between good and bad, but good and great.
*  That's what you get with Indeed.
*  Indeed is the job site that makes hiring as easy as one, two, three.
*  Post, screen and interview all on Indeed.
*  You can get your quality short list of candidates whose resumes on Indeed match your job description faster.
*  Only pay for the candidates that meet your must have qualifications and schedule and complete video interviews in your Indeed dashboard.
*  Indeed makes connecting with and hiring the right talent fast and easy with tools like Indeed Instant Match and Indeed Skills Tests that on average reduces hiring time by 27 percent.
*  You can choose from more than 130 skills tests, then add your must have requirements so that you only pay for applications that meet them.
*  Get started right now with a free $75 sponsored job credit to upgrade your job post at Indeed.com slash Mindscape.
*  That's a $75 credit at Indeed.com slash Mindscape. All for valid through June 30th. Terms and conditions apply.
*  And in some this is going to be very vague and then you'll fix it.
*  But one of the nice things about your way of talking about explanations is it is Bayesian, like you said.
*  And we talk about Bayesian stuff on the podcast all the time, so the folks have heard the term.
*  But all we really need is the idea that there's a prior, there's some pre-existing probability or credence that the model is right.
*  And then you update because information comes in.
*  And what you do in some sense is sort of decompose those two parts, the prior part and the likelihood part into different values that an explanation can have.
*  Is that fair?
*  Right. Yeah. So, you know, we put explanations into the supercollider.
*  We spin them really fast.
*  And it turns out that what we thought, right, were two things.
*  They're actually, let's say, at least four things.
*  Right. Tell us what the fourth and sorry.
*  Tell us those four things.
*  I will. I will.
*  You know, the human curiosity is infinite. Right.
*  So and, you know, of course, what does it mean to diagnose or to discover these sub pieces of a mathematical equation?
*  You know, what we're really doing is saying this piece picks up on a psychological value.
*  Right. So, in fact, our minds are sensitive, let's say, not just to the prior and the posterior.
*  Right. The things you knew beforehand and how well you do on the next bit, but also these little pieces.
*  Right. So, for example, in the case of the empirical side of the evaluation of explanations, we split into two pieces.
*  One is descriptiveness. We call it descriptiveness is just how likely is the stuff that happened taken individually given your explanation?
*  Right. So I've got a whole bunch of things that happened.
*  I want you to explain. Right.
*  You give me an explanation. If I pick, let's say, any piece of what I've seen at random, how well does the explanation doing?
*  So as opposed to sorry, let me back up because we're trying to convert into something that is mathematically very clear if we can see the equation in front of us, which which we can't.
*  Right. Right. So in the in basis theorem, there's this idea of the likelihood, which is to say the probability that you would be getting that evidence if this particular explanation were the right one.
*  And I think what I hear you saying is, yes, that's a thing, but we're going to divide that up.
*  We're going to divide this probability of getting the evidence, given the explanation into first the probability of getting this particular piece of data.
*  Is that right? That's right. Yeah. OK.
*  So, you know, I have a story about, let's say, gosh, now I'm now I'm on the spot.
*  I think of a good one. I have a story about why my food tastes this way.
*  OK, let's say and it's hot and it's salty. Right.
*  So I have a certain explanation. And let's say that it's hot and it's salty because I put it in the oven.
*  Right. Now, that explanation does really well to explain why it's hot.
*  Right. It doesn't do so well to explain why it's salty.
*  Right. I might also say it's hot and salty because I put it in the oven and then I salted it.
*  Right. So now, OK, I've what I've done is I've explained two things in the world.
*  In some sense, I've explained them somewhat separately. Yeah. Right.
*  So I've accounted for this fact with this part of the explanation, this other fact with this other part of the explanation.
*  And in that case, sort of trivially, the only value, the only empirical value there is what we call descriptiveness,
*  because it does just as well explaining one part of the data as the other part, as in fact, both parts together.
*  Mm hmm. Good. So there's a different piece, though, here that's coming in or that comes in, which is and maybe this is a better way to say it, Sean.
*  Some explanations link things together. Yeah. Right.
*  Some explanations not only say what's happening, but also say this thing happening is in some way correlated with this other thing happening.
*  Right. So I can put food in the oven, right.
*  Or I can salt the food. But these two things in that explanation aren't really dependent upon each other. Right.
*  Right. So my explanation hasn't linked together these two things.
*  There are explanations that do link things together.
*  So and I mean, I know you're more of the foodie than I am. Right.
*  Like, don't you like salt crust and cook something right?
*  Like, there's some way that like when you cook something in salt, it's better.
*  I don't know. Help me, Sean. Right. Let's imagine there is.
*  You picked a tough example. I think the best the best explanation I can think of is you put salt in it and then you put it in the oven.
*  Sorry. Sorry. Put it in the oven. Right. Right. Right.
*  Maybe you're cooking it in like pure like literally sodium. Right.
*  Maybe you're cooking it Pittsburgh style. Right.
*  Where the salting and the heating is something that has to go together.
*  In that case, the reason it's hot and it's salty is it's being cooked Pittsburgh style.
*  But the and if it's. Yeah. So I think that we would agree.
*  So good. So what we're doing here is taking terms and an equation basis theorem and we're relating them to human values.
*  We like it when if you just sat on the street, do you like explanations that that cover many things at once and link them together?
*  People would say yes. And now you're able to identify where that value is expressed in this theorem.
*  But what's interesting to me here is that this idea that the explanation can link the data together is in what you're calling the empirical part.
*  It's not in the prior. It's not just part of saying, well, it's a simple, cohesive theory of everything.
*  That's ordinarily what I would think of as living in the prior credence before we collect any evidence at all.
*  Right. Right. So this is great.
*  I should say, Sean, I have a better example, which I think will work much better.
*  It was a good example. Or should we just plow onward?
*  Plow onward because we can see the gears turning.
*  That's good for people. OK, good. Good. Good. We can thinking live.
*  So your intuition is not crazy, right?
*  There is something about this feature we call co-explanation, which is how it links things that we've observed together.
*  And that seems to be linked to just how the theory would do in general.
*  Right. It's that's something we call.
*  In fact, we have a name for it. We call it unification.
*  The critical part here, and this is it's in some sense a trivial distinction,
*  is that co-explanation only deals with the facts you have to hand.
*  OK, not necessarily the facts that you could get in the future. Right.
*  So it's simply, you know, somebody presents you a scenario or a situation with a bunch of features in it.
*  He may also present you with different kinds of explanations that make the observed things
*  dependent upon each other or not. OK, right.
*  So it's, you know, in some sense, this is very sort of blinkered view of the world.
*  It's only one part. So it's what we have so far.
*  In other words, let's imagine that there were 50 different ways I could characterize the food I'm eating.
*  And I had a theory that only had two inputs that explained all 50 of them.
*  But if the two that I had actually measured were saltiness and heat and those two needed both the two inputs to explain them,
*  then at that level, I haven't really co-explained anything, even though the theory in itself was quite simple and unified.
*  For these particular data, it was it was not doing that particular value.
*  Right, exactly. So your theory would be, let's say, high in unification. Right. Right.
*  It's it's it's making a lot of promises. Right. It's tempting you. Right.
*  It says, you know, let's go out there and see.
*  And, you know, at some point, we're going to come up to the dark side of this.
*  So QAnon certainly has this feature. It's like, you know, there's a lot of things that might be linked.
*  And I wonder what you'll find if you if you look for yourself. Right.
*  So there are these kind of promises that theories make.
*  And the promises, of course, they're deeply satisfying when they pay off. Right.
*  And so I think about when I teach that co-explanatory moment is a lovely moment. Right.
*  It's, you know, you've thought this like I've been telling you this.
*  Now, check this out. And you pull, you know, you pull away the curtain.
*  And lo and behold, people see this thing in a new light and they understand the old thing and the new thing is being somehow linked together.
*  I remember telling my friends in undergraduate school, you know, what I learned is that when you do a Lorentz transformation in special relativity,
*  you move to a different reference frame.
*  It's just like doing a rotation in space, except it's in space time.
*  And you could see them go like, oh, why didn't they tell us that? That's awesome.
*  Like it's it's unifying these two different things.
*  Yeah, I mean, I know it's funny, I'm trying to think of a better example.
*  So let me let me give you one. So we can maybe use it as we go forward. Right.
*  Let's instead of food, let's say being hot versus salty.
*  Let's imagine you have an undergraduate. OK.
*  And you see they've taken a class in, let's say, French and a class in neuroscience.
*  Right. And so, you know, one explanation is they're interested in French.
*  They're interested in neuroscience. Right.
*  So these two facts are not dependent upon each other.
*  You can basically like French independently of neuroscience.
*  But another explanation would be this is a linguistics major.
*  Right. And now, OK, right.
*  There is now this common explanation that says you're a linguistics major.
*  The fact that you took neuroscience is connected to the fact that you took French. Right.
*  The discovery of majors, right, enables you to make sense of what all the undergraduates
*  were doing in that school, these kind of hidden common causes driving the classes
*  they're showing up. So I think I am getting it.
*  The virtue or the value that we're pinpointing here is not just the simplicity
*  of the underlying explanation, but the fact that it relates these two particular facts
*  that we have that we have seen. It's not just that it explains both.
*  It actually relates them to each other in one doesn't move if the other doesn't move.
*  OK. Right. Good. That sort of thing. Right.
*  You know, you have a sore throat and a runny nose.
*  Right. One answer could be you have allergies and you were screaming.
*  Right. Another explanation could be you have one of these things.
*  Right. You have a virus. Good. OK.
*  There's one thing I want to put.
*  So it's funny, because you you you did the same thing I did when we first started
*  working on this, which is you said, oh, and a co-explanatory theory.
*  Is also a simple one.
*  But it's not right.
*  So you can have some enormous cascade of coincident, you know, of like,
*  I'll tell you why, you know, the bus was late and, you know, your watch was broken.
*  It's because there's a malevolent conspiracy that is, you know,
*  chasing you through the world, arranging things that the guy who fixed your watch
*  timed it to break and stop the bus.
*  And yes, that does make these facts in the world dependent upon each other.
*  It's a deeply non simple theory.
*  Or even if you just had a hundred different kinds of data.
*  And your theory was that.
*  Data one is correlated in this way with data to always and data
*  to is always correlated with data three in this way.
*  And it just goes on with a hundred different correlations independently.
*  Then you've co-explained everything, but you don't have a simple theory.
*  You've you've you've co-explained the pairs, right?
*  So if you think about it, right, like now, now just imagine filling out that pyramid.
*  Right. So these two things are co-explained by this cause.
*  And these two things are co-explained by this cause.
*  Those those hidden things there, those two causes, maybe they're co-explained.
*  Right. So now you get this like big branching tree where, you know,
*  everything goes back to, you know, the Godhead or something.
*  But your instincts are not right, because, you know, if your first thought was,
*  wow, what a simple, it's kind of cool, right, that these two things
*  are dependent upon each other.
*  And I think now it's kind of a nice situation here where we see that
*  the things we like may lead us astray. Yeah. Right.
*  If if somebody, you know,
*  leads you to perceive these two things are correlated, we kind of like it. Right.
*  We think, oh, you know, that's elegant.
*  That's simple. Simplicity is a value. Right.
*  But, you know, let's hold on a second.
*  Right. Because maybe there's some other pieces here that are in play. Right.
*  And this, of course, this was the odyssey of discovery for us
*  is realizing that a lot of things that we think of as values
*  are a lot of things we think of as good things are actually combinations of values.
*  Right. And they're combinations, let's say, of well-weighted values. Right.
*  So this is, you know, you want to cook a good explanation.
*  Don't put, you know, too much fish sauce in. Right.
*  Like a little goes a long way.
*  And so, you know, so it was difficult for us at first
*  to kind of break apart our own values.
*  I mean, I won't speak for Zach. Right.
*  But for me, it was it was difficult to break apart our own values
*  to start to see how things, you know, could go right or could go wrong
*  along each of these axes. Well, that's right.
*  So these are values and not only just
*  value neutral values, but they're they're good values.
*  We would like to be able to co-explain.
*  We like to be able to be descriptive, but they're going to compete against each other.
*  That's going to be the trick.
*  So right. So we have on the table descriptiveness,
*  co-explanation, what are the other values?
*  Excellent. All right.
*  So let's let's sweep over to the let's call it the theoretical side.
*  The theoretical values.
*  Those were the values of the empirical side.
*  And now we're doing the theoretical side.
*  Exactly. Right.
*  So, you know, descriptiveness, co-explanation, it's all about,
*  you know, show me the money, right?
*  Show me the data.
*  Let's see what the explanation is doing for the stuff that's causing us all these problems.
*  So then let's go over to the theoretical side.
*  We split this into two parts, right?
*  One part we called domain dependent value.
*  Let's I'll tell you what I promise.
*  I will tell you what that is in a second.
*  The other part we call, then you'll be happy, Sean.
*  We call this simplicity.
*  That's good. Right.
*  So let's dig into the easy one, which is domain dependent value.
*  Domain dependent value is your intuitions just about the stuff the explanation is about.
*  Right. So, you know, the example, the car mechanic, right?
*  You bring your car in and it's like, oh, yes, it's a Volkswagen.
*  Those years, it's the installation that goes bad.
*  Right. So these kinds of experiences, their intuition, it's tacit knowledge.
*  It's all of these things that go into your sense of how the world works in this domain.
*  Right. So most of our domain dependent values, they're invisible until you change fields.
*  Right. And you'll get really upset because you present a biologist with a theory that explains all the data.
*  And it's really beautiful.
*  And they're like, that's just not how life works.
*  Like, it just doesn't work that way.
*  And you're like, tell me. And they're like, you have to actually do this for 10 years, 20 years.
*  So that's a real part.
*  It's a real part that's sitting there.
*  It's obviously a bit harder to study in the lab because either everybody has the same domain dependent values.
*  We all have the same, like, folk physics, folk biology, you know, sort of stories about the way the world works.
*  And then, of course, in the things we know very well, we have very specific values.
*  But it's tough to get enough car mechanics in the lab at the same time to understand how these values play out.
*  So, I mean, is this how does this relate to the idea that if we have a new idea or some specific explanation,
*  it should try to cohere and be compatible with things that we already think are true elsewhere?
*  Is that the same idea or related idea?
*  I think we really wanted to keep this kind of simple, right?
*  We wanted to say this is just how likely do you think explanations of this pattern are?
*  You may have some deep theory, right?
*  But let's go back to the the car mechanic, right?
*  There's, you know, 50 different models of cars.
*  You work on cars long enough.
*  You learn that the Volkswagen has this installation problem and the Subaru tends to have a piston problem.
*  This is not fitting into some grand theory about car manufacturing and the industry.
*  It might if you were a certain kind of car mechanic, but by and large, you know, you're working off of, you know, let's say,
*  you know, doesn't have to be stimulus response, but just things you've noticed and remembered.
*  Maybe there's some pattern recognition involved.
*  But we really wanted to kind of keep this as almost an untheorized chunk, right?
*  These are the things that make the biologists say life doesn't work that way.
*  And then you say why? And they're like, I, you know, get out of my office, right?
*  It's one thing to start exercising again.
*  It's another thing to keep it up as a regular habit.
*  With world class instructors, curated music and endless fitness variety,
*  Peloton has created an unmatched fitness experience to keep you motivated workout after workout.
*  With epic artist collaborations and instructor curated playlists, Peloton's music experience is unlike any other.
*  Whether you're in the mood for some hip hop, pop or country,
*  the Peloton bike has the right music to keep you entertained and motivated all year long.
*  And whether you're looking for some extra encouragement, structured workouts or just in the mood to laugh,
*  the Peloton instructors are there to bring out your best during each class.
*  From beginner programs to Tabata intervals, Peloton meets you at every step in your fitness journey.
*  As you progress, choose from a wide range of cycling classes that meet your level and keep you challenged every time you clip in.
*  So get started on your Peloton journey.
*  Go to onepeloton.com to learn more.
*  That's O-N-E-P-E-L-O-T-O-N.com.
*  So let me let me try another example.
*  So you and I both used to be cosmologists.
*  We've moved on in our lives.
*  But something that cosmologists often do is to say, well, maybe there's some scalar field or some modification of gravity,
*  some new fundamental physics that stretches out that affects things in galaxies and clusters that we've never noticed here in the lab.
*  And you tell this to particle physicists or to quantum field theorists, and they're like, no, effective field theories don't work that way.
*  You don't you don't have weird things showing up at long distances in the infrared that wouldn't show up at short distances.
*  We're pretty confident in the in the long distances.
*  Is that an example?
*  That that's that's a good example.
*  I think let's let's push even further away from particle physicists, let's say, have stories about how effective field theories work.
*  But, you know, OK, you want a physicist, I'll give you a physicist.
*  So Scott Aronson has a wonderful blog post about why I won't read your proof that P equals NP or P not equal MP.
*  Right. Right. And, you know, it's kind of long list.
*  Right. And none of these.
*  I actually have to remember. But most of these reasons do not involve his theories about the way P versus NP work.
*  Right. These these one of his great examples is if you're using mathematics that I just don't think is powerful enough.
*  Right. Like category. No. Right. Category theory is not going to do this.
*  Now, it isn't because Scott has tried or has some great theory about why category theory won't work.
*  It's just like that. You know, it's that's you know, it's great.
*  But it's that's it's just sandbox stuff compared to what you would need.
*  Well, Scott, of course, former Mindscape guest, more recent Mindscape guest Julia Gallif.
*  She and I were talking about the how one deals with crackpot theories in physics.
*  And the point being, so I have a way of dealing with crackpot theories in physics as a physicist.
*  But she says, you know, she's not a physicist.
*  So how should she approach grandiose claims from people she doesn't know?
*  And because she's not a physicist, she has to rely on signals from the person who has the theory.
*  Right. Like, do they recognize the problems that their theory has?
*  Are they willing to say they might be wrong or are they just like, no, I'm oppressed by the system and I'm a genius that no one else has ever been before.
*  And so, I mean, that's a different kind of domain specific knowledge. Right.
*  It's almost like the psychological domain.
*  Like, what are the features that you're likely to have in a crackpot versus a respectable scientist?
*  Exactly. I think that's even it's that's that's a nice example because it really gets at the un-theorized version here.
*  Right. So, you know, and then there's nothing wrong with the GeoCities web page in the 1990s.
*  Like, John Baez had a GeoCities web page and he talked about, like, the fundamental theories of physics.
*  So, you know, when you turned on that page and it was, you know, I mean, John probably didn't have this, right?
*  You know, it's the animated GIF of, like, the flames and the under construction sign.
*  And it says, you know, how to understand Feynman diagrams.
*  You're like, great, here we go. Right.
*  The same literally the same website in 2020.
*  It's like this is, you know, don't stay away.
*  So, you know, and I think there's, you know, again, when I'm well, and I'm not sure I want to put Zach on the spot here, but, you know, my sense is, is that these domain dependent priors,
*  a lot of this is much more what we might call tacit knowledge.
*  Right. The stuff you know, but you can't say. Right.
*  So, you know, Julia, when she says, OK, I have to watch the person, you know, she's not crazy.
*  Right. There's good reasons to do that.
*  But, you know, when, you know, Scott says, category theory is just not powerful enough.
*  You're like, well, you know, can you can you tell me why?
*  I just really feel like I've been juggling these things for years.
*  So so this is great. It's funny.
*  Try. You know, was that I didn't spend too much time on this this part partly because we had a work limit.
*  But, you know, the domain dependent price are there and they matter.
*  Right. The other piece, right.
*  This is where all the excitement starts showing up.
*  Right. Because this is where we start judging what you might call the aesthetics of a theory.
*  So not how it does on the data to hand, not whether it fits your gut.
*  Right. And your gut, meaning your experiences of empirical life, but the ways in which the theory looks.
*  Right. If you dig deep enough into this, things get very strange and it's sort of beautifully strange.
*  You know, we we talked about many different values that fall under, let's say, the simplicity value, succinctness.
*  Right. Like literally, how short is the explanation?
*  Right. You know, can you say it in five words or less?
*  Right. You know, my dad used to say if someone can't tell you what their job is in a sentence, they don't have a real job.
*  Right. That's maybe a little unfair.
*  But, you know, succinctness is something that might tell you whether the explanation is is a good one.
*  Right. Why were you late? Oh, OK.
*  So probably this is not, you know, you believe this explanation just because it takes a long time.
*  So unfair. Maybe. Right. You know, concision, a slightly more advanced version that talks about, OK, maybe you switch languages here.
*  You know, is it concise in this language?
*  No. Does a lorange transform look particularly elegant and hyperbolic, tan universe?
*  Right. We can talk about unification, for example, which is the way it links things together.
*  We can count the number of hidden causes. Right.
*  We can say, you know, your example of there's a hundred things and they're each pairwise linked together and then we link all the pairs together.
*  OK, fine. It's log number of things, causes, roughly.
*  So the you know, just counting causes. Right.
*  Occam's razor. You know, we debate this a little bit, but one simple thing is to count parameters.
*  Right. How many parameters are in your theory?
*  If you have a mathematical theory. When I was a grad student, I gave a talk on my latest dumb scalar energy theory.
*  And who was it? Some famous physicist said, how many parameters does your theory have?
*  And I said, like, whatever, three. He's walked out. Right.
*  Because I was just too many parameters for him. Right.
*  It was, you know, didn't matter what I could explain.
*  You know, it didn't matter, you know, how everything would link everything together.
*  It's just that's too many parameters. I got to walk my dog.
*  So you're like, I'm leaving social science. Right.
*  Well, and so, I mean, you know, there are some interesting.
*  We'll talk a little bit about the social science stuff, because there's some interesting stuff that happens there with respect to simplicity.
*  You know, you can keep digging, though. So take the take the value of of succinctness.
*  Right. One way is to say not just succinctness in English, you know, but like succinctness.
*  And here we go. Right. Succinctness in the computer program.
*  But if you ran it, would print the explanation out in the language you can read.
*  Right. This, you know, has claimed to being in some sense, you know, the right definition of simplicity or let's say, you know, sort of concession or succinctness, because it makes it sort of language independent.
*  Right. Right. We know, roughly speaking, that whatever language you write in, it won't change that value very much.
*  So you write your code to generate the model in Python versus list versus C.
*  You know, it's maybe a constant offset. Right. So this this idea, and it's called Komagorov complexity, also called Chaitlin complexity, it has many different names for it, because partly it was invented during the during the Cold War.
*  We had many people in the West and they had Komagorov. And so he gets his name on literally everything.
*  But so let's call it let's call it Komagorov complexity. So, you know, this is this in one sense is the ultimate value.
*  If we could perceive this value. Right. We would know that true simplicity of an explanation.
*  Right. Now, should we value that true simplicity? Maybe.
*  Right. Let's put that question aside and just say, you know, whether it's a virtue or not, let's just say, how could we come to know that value?
*  And it turns out it's logically impossible that you could know this value. Right.
*  We can say what it is. Right. But unless you're like Roger Penrose and you think that humans in some sense, transcend the Turing world, if we're not, you know, if we can't be efficiently or in efficiently simulated by a computer, you know, unless you think that we have no contact with this value.
*  It is uncomputable. It's a value. It's uncomputable. Right. And, you know, I go on about this in length.
*  Uncomputable means uncomputable and you can't compute it anyway. Right. So you can't approximate this value because any approximation you do will have unknown error.
*  And then you say, fine, I will compute the error, which, of course, is uncomputable. Right.
*  And so actually, this is a very good opportunity for me to make sure I understand this because, you know, Scott and I wrote a paper, Scott Aronson, and we need to mention the fact that Kolmogorov complexity is uncomputable.
*  And I didn't understand it. He finally taught it to me. So let me see if I remember.
*  I mean, because the obvious counter argument is, given any language, I will just write every computer program from the shortest one to the longest one.
*  Or, you know, I will keep writing longer and longer computer programs until I output the output I want to get.
*  And the reason why that fails is because of the halting problem, because you will eventually hit computer programs that never terminate and you don't know whether it will terminate or not.
*  So if you if you and you're in your enumeration of every computer program, if you don't actually, by luck, output what you're looking for, you will never be able to get to what you're looking for.
*  Right. Exactly. That's that's that's one way it's, you know, all of the your way is blocked at every turn.
*  Right. It's like the, you know, the Dungeons and Dragons game and the, you know, the DM is logic and the DM like you can't get out of the room.
*  So every door you try, there is some problem with it.
*  Right. So your example, Ray, is, oh, if you just enumerate every computer program, then eventually you'll hit one that will never stop.
*  This is the halting problem. Right. So, OK, the halting problem blocks you that way.
*  Some people have different creative solutions for how to solve this.
*  Every creative solution runs into a kind of girdle like problem.
*  Every girdle like problem secretly is a problem of self-reference.
*  And so we're saying that simplicity is something that we hold in great value, but we can't really quantify it.
*  Right. It's like, you know, it's the it's the don't cancel me, John, it's the atheist God.
*  Right. Like, it's the negative theology of the ultimate theory.
*  We will never know. We actually might have it already.
*  Right. But we can never know that we have it.
*  Got it. OK. You know, so I mean, just to drive the intuition here, I love you know, you can transform this into the halting problem.
*  Another thing you can say is and this is what's called Barry's paradox.
*  Right. You know, you you have some way to name all the numbers.
*  OK, find the shortest number that you can't you know, the smallest number you can't name in less than 50,000 words.
*  Right. I have just named that number in less than 50,000 words.
*  So there's some paradox here in talking about how difficult it is to name things.
*  Yeah. In part, because when you name things, you can also talk about names.
*  So that's the kind of self referential aspect here.
*  If we were somehow able to ban all self-reference from our theories, we could actually compute the simplicity.
*  But I'm not sure we want to do that. Right. Because most good theories in some sense can refer back to themselves.
*  Right. In, you know, I guess in some very simple physics theories, that may not be the case.
*  Right. If they're sitting purely as a set of, let's say, discrete update equations,
*  it may be possible to think about the shortest way to specify them.
*  Yeah. But if you, you know, you could say, OK, look, what's the, you know, what's the context for you?
*  Oh, no, because those are uncomputable as well.
*  It's really, it's really hard. Right. It's really hard to have theories that are boring enough such that you can know with absolute confidence their simplicity.
*  So I guess the only one I can think of is like a Markov model. Right. Markov models, we actually do know.
*  Right. We can sort of compute how simple they are.
*  OK. But at the end of the day, where we are here is you have enumerated, denumerated four values.
*  So to remind everyone, the descriptiveness, the co-explanation, the domain specific knowledge, was it domain specific?
*  Priors, domain specific priors. And the simplicity.
*  So these are the things that we look for in an explanation.
*  And when I read your list, it reminded me there was a famous or semi-famous list that Thomas Kuhn came up with.
*  I don't know if you're familiar with this, but, you know, when Kuhn wrote the structure of scientific revolutions and said,
*  well, there are paradigm shifts and you can't even judge one paradigm from within another one.
*  He was accused by his detractors of being a relativist, of saying no scientific knowledge or progress is possible, et cetera.
*  And he didn't think of himself that way.
*  So he wrote a follow up piece where he said, well, no, I'm just saying kind of there's no algorithm for doing it.
*  But there are values that we have. And he listed seven values.
*  And I forget what they were. But one of them was fruitfulness.
*  Like if the theory would not only explain what it's explaining, but it has the promise of explaining other things.
*  So my question is, does your list of four values purport to be it?
*  Is it comprehensive and exhaustive? Are these the values that we have when it comes to explanation or are they some of them?
*  How should we think about that?
*  Right, right. So I would say Kuhn's fruitfulness is probably our unification.
*  Unification being the co-explanation you'd get if you observed lots of other stuff and the theory turned out to be true.
*  Right. OK. So that's you know, it's a piece there.
*  We give it a name.
*  The you know, in the end, it would be nice if we know it would be nice if we had a normative theory of explanation,
*  meaning we know which ones we know when we've got it right.
*  Really, what we have here is a psychological theory. Right.
*  We're interested in the axes along which a theory can get better or worse that we perceive.
*  Right. So it's a little bit, you know, the extreme version would be like, OK, like it can be salty.
*  It can be sweet. Right. Right. How is you know, how do we as explainers, human explainers look at the world or and look at explanations?
*  Then you can say, OK, well, maybe we're not so bad at it because, you know, as David Deutsch says, we have we're amazing, infinitely capable creatures.
*  You know, maybe we're on to something in having these values.
*  But, you know, we can also over and undervalue them.
*  So there's a nice, you know, a line here. Right.
*  Values can be both virtues and vices.
*  We can value the wrong things or we can value them too much or too little. Right.
*  So, you know, Kuhn's list of seven, I wouldn't be surprised if many of them aligned with, you know, the pieces we have.
*  He may have found others that don't align that way.
*  You know, a couple of things to be going on. One is he could be wrong. Right.
*  Another is that he could have a psychological value that for him is very real, but that he has learned.
*  So another piece here that we have is that we can not only not only do we have sort of, let's say, baked in values.
*  So when you study children, you discover psychologists who study this discover that, you know, children like co explanation. Right.
*  They like sweet things and they like co explanation. So some of these are kind of baked in, but others are sort of trainable. Right.
*  So, you know, it's probably the case that, you know, you and I, as people who like physics, you know, had a heavy weight on certain values,
*  let's say the unification value, the simplicity value.
*  But, you know, it was exaggerated over time. Right.
*  Because all of our charismatic teachers gave us candy when we valued simplicity more.
*  You know, conversely, anthropologists, you know, value simplicity less.
*  And it's part because they know the world is not that simple when it comes to people.
*  So I remember there was a simulation. I saw people doing a simulation of, you know, the, you know,
*  civilization developing in the American Southwest, you know, pre pre-contact.
*  And, you know, they had this model where there were people on a landscape and choosing where to walk and choosing where to settle and build,
*  you know, houses. And I'm sitting there, I'm sort of boiling with with upsetness as a physicist.
*  I was just new to the Santa Fe Institute where this was happening at the time.
*  I was like, this is terrible. Right. Like, you know, there's two kinds of houses.
*  How many parameters does this theory have? And then this great anthropologist raised his hand, you know, one of the big, big figures.
*  And he's like, but where are the where are the turkeys? Right.
*  Why don't you have the wild turkeys in the simulation? Because that's important. Right.
*  And he was right. Right. That matters. Right.
*  That's an important part of explaining what's going on where the turkeys are.
*  But, you know, with somebody with a different set of values would say, this is just getting too extreme.
*  Like, we need a different like this.
*  The fact that we're adding these things into the explanation is making it worse and not better.
*  Well, I guess this is I mean, this is one of the things I wanted to ask because you have these different values.
*  And as you just highlighted very clearly in the real world, they compete sometimes anyway.
*  Yeah. I mean, obviously, if there's one theory that is both simpler and more co-explanatory and more descriptive, it will win.
*  But sometimes the theory is less simple, but more descriptive, et cetera.
*  And then you have to balance and that's harder.
*  So I guess two questions. One is, does the right way to balance these values pop out of Bayes' theorem or something like that?
*  Have you mathematically proven the right way? Or question number two, can we empirically figure it out?
*  Like, can you go back in the history of science and say, well, this person was valuing simplicity and this person was valuing their domain specific priors and look who won and sort of total scorecard?
*  Yes. So, well, let's say partly.
*  We have we have a story about the proper weighting between descriptiveness and co-explanation, right?
*  There's a proper ratio in which you should value these ratio and units and the correct units is one.
*  Right. So you should value these two things equally in a certain way.
*  You know, the real challenge here is when it comes to the theoretical values.
*  What we don't have is a normative, let's say, or the optimal or the ideal way to talk about the theoretical value.
*  OK, right. There are people who will tell you that, for example, simplicity has to be a value.
*  And you say, well, why does simplicity have to be a value?
*  And you talk to them long enough and it turns out it's because the universe is simple.
*  Right. OK. Right. How do you know it's simple?
*  Well, it turns out that's the simplest explanation for why.
*  OK. So there are the on that side, we don't have a we don't have an answer.
*  But you ask, of course, the right question is, can we just go see how people do?
*  Right. Can we see how well people who valued this kind of explanation over that one, how they've done in historical time?
*  So we're actually we have a project on this. It's really fun.
*  We have all the data from the proceedings of the Royal Society, the Royal Society of London.
*  So this is the first scientific institution.
*  It's formed in 1666, or at least the journal starts then 1660.
*  It's sorry. The society started in 1660.
*  I know that I was literally reading about it yesterday.
*  Excellent. OK. Journal starts a little bit later.
*  I can't remember now. It's like 1663. Right. This is why I drive historians crazy.
*  You know, it's it's it starts on the order of 10 to the three years after the birth of Christ.
*  So we have this data on essentially how scientists are putting ideas together over time.
*  And how do we track the ideas?
*  We do some magical pattern recognition on the text.
*  We look at the patterns we find.
*  We as scientists say, OK, these patterns are making sense.
*  Right. So we can detect the magnetism idea.
*  We can detect the electricity idea.
*  We can detect the magnetic substances topic, which is a different one.
*  Right. It's like magnetism. What's up with that?
*  Right. And it's sort of sad because our data only goes to the late 1800s, 1887.
*  So we know they're not going to figure out why iron becomes magnetic until the 20th century.
*  Like, it's not it's just not going to happen for you. Right.
*  And so you sort of feel bad like you want to say no.
*  Other things they do figure out, though, of course.
*  And famously, what they figure out is that there is this global conspiracy between the electric and the magnetic fields, which we call the electromagnetic field.
*  These forms and it's tricky to call them co-explanation because these are not these topics or these ideas are not just about the observed things, but also discussions of the ideas themselves.
*  But we can track how these ideas link together over time.
*  The first thing you find is that this value, at least in science, kind of appears out of nowhere. Right.
*  So the first hundred years of science is people putting ideas together in somewhat arbitrary ways.
*  Now, it could be they know that ideas should be linked together and no one's agreed on how to link them together.
*  So they may have the value or perhaps more likely, I would say they haven't yet learned that what you should be doing is finding the ideas that tend to link together and working on those.
*  Right. So preferring and in fact, we can see this happening, preferring to work on ideas that reliably connect to particular other ideas.
*  So this is kind of wild. Right.
*  We can see people moving towards and it starts this preference starts around early 1800s.
*  Actually, one of the first people, one of the issue in which it starts is the issue in which they published Ben Franklin's Kite experiment.
*  Can we date it that precisely? No. Right. But that's where the Bayesian model says. Right.
*  Great Pennsylvania physicist.
*  But, you know, beginning around the early 1800s, we have this era which lasts maybe about 100 years, maybe 50 years.
*  We have this era where people start connecting ideas together.
*  So people know, oh, idea A has something to do with idea B and not C. Right. Right.
*  Whereas, you know, earlier you look 50 years before 100 years before they're like earthquakes, cows, maybe cows.
*  Right. You know, and you're like, no, right.
*  It's not that's not going to happen.
*  But at some point, they start putting these ideas together.
*  The let's say the overall unification level in science starts to rise.
*  We can also see people, as I said, people choosing to work in on areas that are linking together.
*  Right. So we see this emergence, right, of a value, or at least the value begins to articulate itself in the record.
*  Can I with respect to that?
*  Yeah, of course I am.
*  This might be relevant to a very longstanding puzzle that I've wondered about, which was because my first trade book from Eternity to Here was on entropy.
*  And I read a lot about Boltzmann and Maxwell and their discussions, et cetera.
*  And one of the big objections to Boltzmann was he was deriving the second law of thermodynamics that entropy increases as a probabilistic statement, but it wasn't absolute.
*  And people thought it should be absolute. They thought it was a law.
*  They thought it was a law separate from Newton's laws of classical mechanics.
*  And that always puzzled me. Like, how were you allowed to think that?
*  Like, you know, there was the same stuff, right?
*  Like, how could a gas obey Newton's laws and the second law if they weren't compatible with each other?
*  And are you telling me that maybe that possible incompatibility just wasn't something that would throw itself in their faces and make them bothered by it at that point in scientific history?
*  That's great. I mean, it's funny, Sean.
*  One of the papers in our data, I mean, it's a bit ironic, is Bayes' original paper, right?
*  So the Reverend Bayes publishes his article.
*  And it's an amazing article.
*  It's actually it was he died and somebody said Bayes told me the following.
*  It's an amazing article because actually everything's in there.
*  Right. So the idea that models make probabilistic predictions, the idea that you can go both directions, right, that you can go from from model to data, data to model.
*  It's all sitting in there.
*  But somehow this just didn't catch fire for people.
*  Right. The idea that knowledge could be probabilistic.
*  That this was a good representation of what we know or how to know things just didn't take off.
*  Bayes is that those ideas are sitting there and don't get linked, which is sort of interesting.
*  Right. So in one sense, I can tell you, you're right.
*  No one connected these together.
*  In that case, how do you punt it?
*  You might punt that to the domain priors.
*  Newton is about precision.
*  Newtonian laws are about determinism.
*  The solar system will go forever running like a clock.
*  So somehow the idea that there would be some relationship between Newton's that style and probabilistic reasoning is a little bit like the Scott Aronson idea that that's just not powerful enough.
*  But in this case, it's like, no, that's just not the right thing.
*  We've been doing this for 200 years, but they were just wrong.
*  Right. So I think that's that's a lovely example.
*  I mean, it's easy for us to focus on the successes.
*  The obvious one is we can see them put electricity and magnetism together, which is a beautiful thing.
*  We also see them put electricity and electrochemistry together, which is an interesting one because electricity is more the theory.
*  Electrochemistry is the experiment.
*  So we can start to see people see what Joe Mokercole's this this virtuous cycle between theory and experiment.
*  Right. Better theories let you build better devices to get you better theories.
*  Right. So we see some of these loops.
*  The one that I really love, actually, I should say it's not just about physics.
*  Right. So we also see people connect demography and agriculture.
*  Right. You know, births and deaths, right.
*  Lifespans, child mortality.
*  People start to realize this probably has something to do with how people eat.
*  Right. They connect agriculture to geology.
*  Right. Whether your crops grow probably has something to do with the underlying rocks.
*  Right. We see them connect metabolism to to actually to agriculture.
*  Another one metabolism, because it's like the cow eats stuff.
*  Right. And it processes it and it poops it out.
*  And we should probably if we understand that, that'll probably help us explain phenomena that we've noticed in agriculture.
*  Right. And so on and so forth.
*  Good. So it isn't just the you know, it isn't just what we might call the exact sciences that are linking together, but also, you know, these we see paleontology connect to botany.
*  Right. As they start realizing that they can learn about the deep history of plant life, it's not just about dinosaurs.
*  So, you know, this this connection stuff is is is kind of all over the place.
*  And I'll just I'll tell you the story and then we could we could chat a little bit more.
*  But the the one I really love is OK, so they connect electricity and magnetism.
*  Right. The but as we may remember, right, light is a form of electricity and magnetism.
*  Hertz's paper is in like our final issue right before it goes under copyright or whatever.
*  Right. So, you know, at the end, they've put this together.
*  Right. They've linked electricity, magnetism and light.
*  They realize this is all these things all go together.
*  But we can see them make these connections.
*  We can see them start to connect magnetism and light like 40, 50 years earlier, which is wild.
*  Right. Now, what are they doing?
*  They're like, there's this magnetic substance and I shine light through it and like something's weird.
*  Happen. Like, guys, help me out here. Right.
*  Like, what is it about?
*  Like, magnetism seems to be doing something to light.
*  Like, what's right.
*  So you can see them start to make those connections.
*  And so one of the things that brings up for us is can you sort of look into the future?
*  Right. So can you see where the next advances are going to be now?
*  You know, that would be in some sense, you can't really do that.
*  It's impossible to predict an unpredictable future in science is in some sense unpredictable.
*  But it maybe gives us the sense, at least, that we're on the right track here as to what's making for good explanations for them.
*  And I do want to give you enough of a chance to talk about what makes for terribly bad explanations as well, because it's a very fun part of what you've done.
*  I mean, the different values that you've pinpointed, like we said, they compete against each other and it can be in some sense not completely algorithmic how you weigh them against each other.
*  So there's a failure mode where you overvalue a particular kind of thing and undervalue the others.
*  So why don't you tell the Timothy McVeigh story?
*  I think that's a great example. I really like that one.
*  Yes, there's OK. I'll tell you two stories.
*  Timothy McVeigh is a really interesting one.
*  This is a conspiracy surrounding the Oklahoma City bombing.
*  This sort of the worst terrorist attack on American soil by that point, 1995, white supremacist attack.
*  So what happened? Well, Timothy McVeigh and some co-conspirators built a fertilizer bomb, put it into a U-Haul truck, drove it to the federal building in Oklahoma City,
*  set a bunch of timers, left it there.
*  It blew the building to pieces.
*  Many, many people died.
*  It was the devastation is quite shocking.
*  Actually reading about it in retrospect, we sort of forget how insane it was.
*  Just one example, just sort of horror of this is many people died just because of the broken glass that flew out from the explosion.
*  Right. So, you know, the building also collapsed.
*  But so this was crazy.
*  The other thing about this attack that's relevant here is that no one knew who did it.
*  Right. This was actually an extraordinarily meticulously done thing.
*  Right. At least at first, you know, they couldn't, you know, who, you know, who drove the truck?
*  Where did the bomb come from?
*  There was they had no leads.
*  It was, you know, it was not, you know, this there were not mistakes made, let's say, at least early on in this in this investigation.
*  So what happens? Well, McVeigh, you know, sets this bomb off and, you know, he walks away.
*  It's on a timer. You know, he's far enough away.
*  Five minutes later, the thing blows up. McVeigh gets in the car and leaves.
*  So he's in his car.
*  The car he's driving doesn't have license plates on it.
*  He gets on the highway and he starts speeding.
*  He gets pulled over by a cop for not having license plates and for speeding.
*  And the cop notices he's got a firearm.
*  And it turns out it's like an unregistered firearm.
*  He gets thrown in jail.
*  And it's only when he's been in jail for three days that they figure out it's him.
*  So, you know, this gives great puzzle.
*  How could somebody so, you know, able to pull off this plan, right?
*  This very elaborate plan be so stupid, right?
*  You know, like even I know this, like, don't drive a car without license plates.
*  And if you do, don't get on the highway in speed, right?
*  Don't blow past the cop. Right.
*  So, you know, how do you so how do you put this together? Right.
*  The explanation, of course, you and I have about the Oklahoma City bombing and, you know, spoiler.
*  It's true was that he was essentially an insane, you know, deeply evil person who drew a few people in to help him blow up this building, you know,
*  spurred by, let's just call it white supremacist rhetoric.
*  Right. That's our explanation.
*  The problem is, is that it's low in what we might call descriptiveness.
*  Right. It it that explanation postulates that Timothy McVeigh was not a moron, at least in certain relative future planning abilities.
*  And yet he acts like a moron. Right.
*  If you're not a moron, doing what Timothy McVeigh did after the bombing is a low probability event.
*  Right. So now our explanation is suffering on a certain value.
*  Right. It's suffering on this empirical value of descriptiveness.
*  Right. It's, you know, it's like saying to go back to our earlier example, why is the student taking French and neuroscience together?
*  Ah, because they're a romance language major.
*  OK, well, that actually makes the neuroscience less likely because they got other requirements.
*  Right. But you're no nice. Come on. There's other reasons.
*  So some people look at this and they're told this story and they say, no, I can explain that.
*  It wasn't McVeigh. McVeigh. Yes, he's a moron. McVeigh was a patsy.
*  Right. He didn't pull this off. Actually. All right. Let's go. Right.
*  Actually, it's a government conspiracy and the Bureau of Tobacco and Firearms is involved.
*  So they have an explanation which can actually account for these facts.
*  They're better at finding the data.
*  They're better fits to the data. Right. And so, you know, of course, what's coming.
*  Right. What's going wrong for them. Right. I can overfit to the data.
*  Right. And so, of course, the theory they need not only is strange, not only does it violate our domain dependent priors.
*  And the joke is our domain dependent priors, like the government's not that good at doing anything.
*  So how could it do this? Right. But also, it's violating these simplicity priors.
*  Because once you assume there's a conspiracy, OK, you know, who else is in on it?
*  Why did the cops not see it? The cops are in on it.
*  And the cop who wasn't got shot and steering his way.
*  And, you know, the newspaper guy is, you know, he disappeared.
*  So, you know, of course, this this explanation ramifies outwards.
*  That's a case where, you know, we overvalue an anomalous point.
*  Yeah. Right. We overvalue dealing with the anomalous point.
*  That's a classic case from our point of view of going extreme on that first value of descriptiveness, the desire to make sense of every last detail.
*  And this is probably not true, but I can't help but hypothesize that this might have something to do with one's fondness for detective shows and novels.
*  Right. Because when you're when you're in a mystery fiction, there are no coincidences.
*  You'll hear the detective say, I don't believe in coincidences.
*  And like every fact turns out to be really, really important later on.
*  And I think that's partly why Alex Rosenberg, who's another former guest on the show, he likes to say that we make a cognitive mistake by overvaluing stories.
*  Right. We tell ourselves a story that makes everything fit.
*  Sometimes things just happen. Right.
*  And it's hard to it's hard to weigh those two values of admitting that sometimes things just happen with the satisfaction you have of fitting it all together into a matrix.
*  I think that's right. I mean, there's I can't remember if they let us keep this, but Zach and I talk about one of the talk about perhaps.
*  Yeah, there's this enormous pleasure in a detective novel when all the facts are connected together.
*  Right. There's this co-explanatory moment at the end.
*  And there's always the scene, right.
*  Parvo brings everybody into the into the room.
*  You know, there's a great kind of so Alberto Acco in his book, Name of the Rose.
*  And this is not a spoiler. Right.
*  The Name of the Rose is a great this is mild spoiler.
*  Namers is a great book because, in fact, there is no co-explanatory moment.
*  Yeah, it doesn't. It's a detective story without co-explanation.
*  And of course, I think Acco actually he sort of talks about this a little bit in maybe an inter-doctoral essay wrote about it.
*  So that's a great example of how he breaks the convention.
*  But you're right. The you know, Alex says, I think he's got a piece of the puzzle here when he talks about stories because stories
*  often contain this co-explanation.
*  That's what makes them appealing. But there's also more.
*  So, you know, I would say, for example, you know, if we're right about how these empirical values work, you know, you would expect conspiracy theories to involve not just stories, but anomalous facts.
*  Right. So, you know, this meme, you know, jet fuel can't melt steel beams.
*  Right. Which also turns out not to be relevant, but it's a fact.
*  So people are, you know, that fact comes in as well as, you know, dramatic accounts and stories and narratives as well.
*  So there's this empirical side that I think we can't neglect these these little pieces that people that people find attractive at least seem to be part of the part of the appeal.
*  And presumably things like QAnon or Flat Earth beliefs are of the same spirit where you're explaining a bunch of things.
*  I mean, I guess Flat Earth is not quite the same thing.
*  It's not a conspiracy theory, but QAnon is like the classic, it's the epitome of explaining everything by having a million moving parts in your theory.
*  Right. So let me this is a so we talked about one way to go wrong, right, which is this descriptiveness one.
*  Let me talk about the other one, which is the co-explanation going wrong, because this is a different way that things can break.
*  So that little fragment of the McVeigh Oklahoma city bombing conspiracy theory is clearly a case where people need to fix an anomalous piece.
*  Jet fuel can't make melt steel beams, fixes an anomalous piece.
*  Co-explanation is a different appeal.
*  And I think this is partly working in QAnon.
*  I think I can tell this story because I've told it once before, but I won't.
*  This will be the last time I tell this story because it's such a good story.
*  I don't want to I don't want to overplay it.
*  But I will give you an example of co-explanation that I fell victim to.
*  Here we go. We all have.
*  We all have. Right. So this was when I first moved to Santa Fe.
*  And we you know, I was in the cafe and Santa Fe is full of very interesting people, some of whom are crazy.
*  One of the jokes is the people in Santa Fe, like they were so disorganized that their car broke down on the way to San Francisco.
*  Right. So, you know, that's your that's your group.
*  And I'm in the cafe and my first week there and I meet this guy and, you know, he sort of buttonholes me and he starts telling me his conspiracy theory.
*  And, you know, I'm sort of don't make enemies.
*  It's your first week in town.
*  So I'm I'm listening. Right. And he's the conspiracy he's explaining to me.
*  And I think this this guy is long out of this.
*  Right. But, you know, at the time, he was telling me this conspiracy theory known as the sovereign
*  citizens movement.
*  So the sovereign citizens movement is a conspiracy theory that is so elaborate.
*  Right. That, you know, I could if I remembered, I could tell you the whole thing.
*  But just to give you a fragment of that, it involves the idea that British common law in some way meant that the United States government in the 1800s
*  could not borrow money on the credit of the citizens.
*  Like somehow this couldn't work.
*  Right. So what they did was for every citizen, they created a fictitious identity called your U.S.
*  name. So everybody's carrying around a fictitious identity called the U.S.
*  name. And it's the U.S.
*  name identity that, for example, has to obey the law.
*  Right. The U.S.
*  name identity is the one that has to pay taxes.
*  You yourself actually you only it turns out are answerable to like the sheriff of your town.
*  I've never heard this one.
*  So, I mean, this is sort of funny, but it also obviously, you know, the guy keeps going and eventually it turns into, you know, obviously this
*  anti-Semitic feature is now this.
*  Right. One of the nice things about this movement is people know it very well, because one of the things it tells you to do is write a
*  letter to the IRS telling them you're not going to pay taxes.
*  So it turns out they keep those letters.
*  Right. So, you know, this is it's a movement that's relatively easy for the government to track.
*  So he's explaining this to me.
*  And I know at some point I am waiting for it to get dark.
*  But he says, look, I'll tell you something, sorry, but I'll tell you about your U.S.
*  name. You know, the government has to deal with you in your U.S.
*  name capacity all the time.
*  When it does, you know, when you get a letter or something like that, your name will be printed in all capital letters.
*  Right. So this is I take your wallet out, Sean.
*  Give your wallet. I don't have it with me right now.
*  OK, so if your listeners do this right, you can test your you can you can test your
*  co-explanation problem here.
*  Right. It's like your U.S.
*  name government is all capital.
*  I said, now take out your wallet.
*  Look at your driver's license and my name's in all capital letters.
*  Oh, my goodness. What about the past?
*  And I was like, for this moment, Sean, I was like, oh, like, there's something.
*  Oh, my God. There's something to that.
*  No other way. This is a classic.
*  Yeah. It's a classic co-explanation moment because what he's done, of
*  course, is link all of these facts he's given me about the British common law or whatever.
*  It's not that I believe this, right. But it's like he's told me all about Jefferson.
*  It's a nice fact. And then he's given me this story that links
*  with this totally unexpected fact that my driver's license has my name in all caps.
*  Right. So this is now all connected.
*  And it's kind of lovely feeling. Right.
*  You're like the world very briefly got sort of brighter.
*  And, you know, the colors got a little brighter.
*  And then you sort of shake it off and you're like, no, this is this is crazy.
*  But, you know, maybe I think the message or the larger message, Shana, is
*  that these are values.
*  Right. We have them.
*  People who, let's say, fall victim to these conspiracy theories.
*  And even if people even if someone doesn't go crazy, there are some very negative features
*  of believing conspiracy theory, one of them actually being that we love to explain things
*  to each other. It's a human like it's one of the things we do all the time.
*  If your explanatory values go wrong, you can't enjoy this with other people.
*  Right. Yeah. So, you know, you and I sit around and it's like, I don't know, Sean,
*  we would never have this conversation was like, what about the bulls?
*  You know, the Chicago Bulls are doing really well this year.
*  And if you're like, what's your theory?
*  Well, let me explain it this way. That way we can have a lot of fun.
*  But then the guy with the weird values is like, it's the Jews.
*  Right. And you're like, hey, like, don't say that.
*  That's that's insane.
*  But also it's like, that's not how we that's not a satisfying explanation, even if it wasn't.
*  Yeah. Right. So you lose this you lose this ability to spend time with others.
*  And people mention this. So some studies of QAnon people, this is part of it is they sort of get
*  exiled from their friend groups, not even because, you know, because they're being weird or
*  sexist, racist or anything, but because they're they're just no longer fun to do this fundamental
*  human thing with. Right. You can enjoy a sunset with them, but you can't explain why, you know,
*  Trump won the election or why, you know, on Sally so upset this week.
*  So these there are some real downsides.
*  But, you know, I think our message here is that those, you know, those stumbles, those falls
*  that people have, you know, they're not some alien, you know, ridiculous axis that's
*  completely orthogonal to you and I.
*  Yeah, exactly. Right.
*  That, you know, their reasoning, right, their reasoning has gone wrong, but they are still
*  reasoning. They're not babbling.
*  Right. And, you know, the question people always ask us is, OK, you've explained these things.
*  Can you predict what to do about them or what interventions will work?
*  And so the answer is no, we don't do prediction.
*  But the explanation, I think, does potentially, you know, it gives us part of the puzzle,
*  because if we see the membership in a thing like QAnon as in part a disorder of explanation
*  making, well, how do we, you know, how do we fix that?
*  Right. How do we get people's values back into balance?
*  One piece, and this is work that we've been doing when Chloe Perry and I have been doing
*  Chloe's now at University of Michigan is the idea that, you know, you have weird explanatory
*  values. You can't hang out with your friends.
*  You go on the Internet.
*  And what you do on the Internet is not just talk about jet fuel can't make steel beams,
*  but you also share and reinforce these sort of malfunctioning values as well.
*  So you're surrounded by people who don't just believe crazy things, but also have the
*  wrong meta principle for adopting them.
*  It suggests that part of this is disconnecting people from an epistemic value system as
*  well as the particular beliefs.
*  Right. So it isn't just saying it's ridiculous that you think Timothy McVeigh was part of
*  this conspiracy, you know, that people can be smart and idiots the same day, but also
*  making sense of the way that they're connecting things together on a larger scale.
*  But part of what I thought you were saying is that the actual set of epistemic values
*  that the conspiracy theorists have is the same set of values that we very levelheaded
*  natural scientists have.
*  They're just weighting them different.
*  And that sounds like a harder thing to or maybe it's an easier thing.
*  Like, maybe since we rely on the same values, we can sort of speak to those values and
*  bring people back. I don't know.
*  Is there an optimistic message here?
*  So I gave a talk, I see Zach and I together gave a talk to the philosophers at the
*  University of Pittsburgh. Right.
*  So pit philosophy is like best philosophy in the universe.
*  You know, neo Hegelian pragmatism sometimes.
*  But one of the people in that seminar made this lovely remark.
*  She's like, you have an Aristotelian theory of epistemic values, meaning so, you know,
*  in Aristotle, it's all about this balance.
*  Right. Don't be foolhardy, but don't be a coward.
*  Right. Like, where do you find yourself on that continuum?
*  Right. You know, like weakness versus strength.
*  You need to find some like the intelligence here, the wisdom here is finding the correct
*  location on that line, not getting yourself killed, but not running from a fight you may
*  need to fight. We have an Aristotelian theory of these epistemic values.
*  They become virtues when or you become, let's say, epistemically virtuous when you're at
*  the right point here.
*  The golden mean. Now, does Aristotle tell us how to treat, you know, anger?
*  Maybe. Right. People who are too foolhardy, people who don't take enough risks.
*  Maybe. But it tells us maybe one way in which these these values are operating.
*  No, I mean, that's actually really good.
*  Like, I'm becoming more Aristotelian in that sense myself in the sense of me.
*  Not only is it that you balance things and you look for a harmonious middle point, but that
*  there is no algorithm for doing it, right?
*  That there is some kind of human choice.
*  Wisdom is the word you used.
*  Phonases or something like that.
*  I'm sure that the Greeks would say.
*  But but OK, good. So maybe let's wrap this up then.
*  Sure. Yeah. Put it to work.
*  Let's like do some work example here.
*  What how would we think about?
*  Let's say I have lots of work to do and I can pick from.
*  But let's say panpsychism versus physicalism about consciousness.
*  So here are two explanations for consciousness.
*  One is that the world is just protons and neutrons and electrons obeying the core theory.
*  And there is some higher level immersion description.
*  And we call that consciousness.
*  There's another explanation in which no, no, no.
*  I mean, there's that stuff and it obeys those laws.
*  But there's also intrinsically mental aspects of the physical stuff,
*  which are not captured by the standard laws of particle physics, etc.
*  And those extra intrinsically mental aspects are needed to explain conscious experiences.
*  So here's two explanations and you have a bunch of values.
*  And I can kind of I can imagine how I would I would think that the physics one is simpler, maybe.
*  But, you know, what would you what would you say to someone who wanted to evaluate these using your values?
*  You're right. I love this example so much because it's wonderful.
*  So, you know, let's let's let's deal with the with the property dualism one, right?
*  The panpsychism one that says, look, there's just this other property we all have, which is consciousnessiness.
*  This would be, I would say, a highly descriptive theory.
*  Right. You know, there's these things and then there's these other things.
*  And physics does these things.
*  And we just have to stick in this other story here.
*  Right. That they're not connected.
*  Right. There's no co-explanation.
*  You know, this conscious property is in no way correlated with that physical property in any deep way.
*  The you know, it's the properties are live in distinct worlds of matter and spirit.
*  Right. So it's it's winning on descriptiveness.
*  Right. It's not winning so much on co-explanation.
*  But, you know, I want to flip this around because I know what you like.
*  I know what I like, which is this emergence story. Right.
*  You know, there's this, you know, there's this stuff on the bottom here and it's bubbling up to produce these emerging phenomena.
*  Right. But that's actually it's not that simple.
*  Right. Because how many layers between quarks and beliefs are there?
*  Right. How many? OK.
*  Gosh, I guess you have to do the molecules and the molecules.
*  OK, so now you got to get the, you know, the substances and the right.
*  There's a lot of space between the standard model and conscious experience under that other one.
*  So in that case, you know, that almost you could make the pitch like that's a real conspiracy theory.
*  Well, I think this is I make this point in my recent quantum mechanics book about people who believe in,
*  let's say, hidden variables or pilot wave bohmian theories versus people who believe in many worlds.
*  Not only are they different theories and they can argue about which one is right and we don't yet know,
*  but also they both claim they have the simpler theory. Right.
*  But the sense of simplicity is different.
*  And I think that this is one of the reasons why I like your set of values, because I can see them coming apart.
*  The Everettians will say, look at my equations. There's only one.
*  There's one equation. That's all and everything.
*  You just work on that equation and massage it and think about it really hard and you get everything.
*  That's that simplicity for me. And the bohmians say, well, no, look at the world and I can easily locate it in my theory.
*  There's particles like there they are in my theory.
*  I don't need all these layers of explanation.
*  So that's what I call simple. But maybe that's actually more descriptiveness.
*  I'm not sure. I think I think that's actually I mean,
*  I think that's a great way to distinguish the many worlds from these more like pilot wave things.
*  Right. It's true. You have to grind through a lot of mathematics to get from the many worlds to the classical world.
*  Right. Now, in one sense, this is not simple. Right.
*  Like David Wallace's book is five hundred pages.
*  But if you think about this as, let's say, a program that you run, right, to derive these things,
*  the program actually might be quite short in the sense that if you you just have to be really smart,
*  meaning you have to be able to run that program, quote unquote, but the program might be short.
*  Yeah. So I mean, there's the shortness of the program, but there's also how long it's got to run.
*  Right. Right. Yeah. The logical depth they call right.
*  How long the program runs. All of these are you know, these are wonderful.
*  I think one of the pieces, you know, Sean, we could talk about this forever.
*  But one of the pieces in the non many world stories, right, like the bohemian story,
*  I think a lot of this is domain dependent priors.
*  Right. Because I think one of the responses to the many worlds is like, that's just insane.
*  Right. Like, come on. Right.
*  And I think that's an appeal to, let's say, common sense.
*  Right. In the same way, and I can keep going back to this, you know,
*  Aronson, Scott Aronson's example of like reasons why I won't read your proof.
*  And again, Scott, this is, you know, this is a joke blog post. Right.
*  But Scott's like, it would be ridiculous if that's how you proved P not equal to MP.
*  Like, come on. Right. I'm just not going to take it seriously.
*  I think that's, you know, that's a domain dependent story there.
*  So I think that's another piece.
*  It may also suggest why people have been so resistant to the many worlds theory over the years,
*  is that, you know, we can we can convince each other that something's beautiful, it turns out.
*  Right. We can say, OK, this is more beautiful than that.
*  And we learn these values.
*  It may be much harder to push around the tacit knowledge.
*  It may be much harder to push around these these things that we've learned that we don't even know we know.
*  Oh, I think we can't quite articulate.
*  You know, I think that's true. But I also think that even when people share the tacit knowledge,
*  this is the way they balance the different values is is my favorite thing that I got out of what you've been saying here.
*  I'll give you one last example that you can run with or not, as you choose.
*  Lee Smolin was very recently on the podcast and he said he said something not on the podcast,
*  but years ago that that always really, really struck me because I couldn't it was clearly true and I couldn't explain it.
*  And maybe you're helping me explain it. He said, isn't it weird how people who believe in the Everett interpretation of quantum mechanics
*  also always believe that computers will someday be conscious?
*  And it's not because Everett implies the computers will be conscious,
*  but the kind of person who's like, yes, just give me the simple rules and I'll derive everything is likely to buy both Everett
*  and buy that consciousness is substrate independent.
*  That's I mean, you know, this is now this is a lab experiment one could do on mTurk.
*  If you could get enough physicists or, you know, the IRB to actually talk to one.
*  You know, I think this I don't know, Sean, I would again we could go on forever.
*  But one of the things that I think we've missed or it's a big opportunity is to look at these more.
*  Let's call them exalted forms of reasoning. Right.
*  We we tend to look at sort of minute level snap judgments that people make.
*  This is this tells us a lot, but we're missing kind of this.
*  We're missing sort of the culture of explanation making.
*  And that's that's I think I mean, I love this example.
*  I think it would probably hold up. We should run it at the next APS.
*  Do you know about the to ask people the the.
*  Phil people dot org, the website for philosophy.
*  Yes. So David Chalmers and David Bourget, I guess.
*  If you're a philosopher, you can have a profile site on Phil people.
*  And one of the fun things they do is they ask you your opinions about all sorts of hot button philosophical issues.
*  So you could totally cross correlate those. The data are there.
*  Oh, my God. That's amazing. Yeah. No, the data is there.
*  I mean, that's that. Well, I will I will do that this afternoon, because that's a that's a great example.
*  I'm sure there's like 50 questions. And yeah, you know, philosophy tends to have this, you know,
*  it's like, do you believe in analytic, you know, identity or do you believe?
*  Who knows? Right. Like they they have a vocabulary there that enables pretty simple binary.
*  Well, yeah. And all the all the questions are multiple choice.
*  So it's not like there's no essay. So it's like, you know, consciousness, physicalism, panpsychism, whatever it is, dualism.
*  And, you know, that's great mechanics. Everett. Yeah.
*  Well, that's good. I always like I'm I'm I'm so I love it.
*  I love it, Sean. This is I like to end the podcast on an optimistic note.
*  And there is no more optimistic note than giving the podcast guests work to do as a research program.
*  So I'm glad we were able to do that.
*  Simon, the day. Thanks so much for being on the Mindscape podcast.
*  Thank you, Sean.

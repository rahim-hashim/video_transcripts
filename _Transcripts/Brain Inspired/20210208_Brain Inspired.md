---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 5039s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 6457
Video Rating: None
---

# BI 097 Omri Barak and David Sussillo: Dynamics and Structure
**Brain Inspired:** [February 08, 2021](https://www.youtube.com/watch?v=VmScb_QQrE4)
*  I know I'm wrong. I know that it's my personal laziness that pushes me too far into that
*  end of the spectrum and I know this organization is there.
*  Can we use the basic features of dynamical systems to understand what this complex nonlinear
*  system is doing? The idea of universality is that different dynamical systems have properties
*  that are conserved despite the fact that the equations are different or in our parlance
*  despite the fact that the parameters of our neural networks are different.
*  Universality is sort of a question that has to be asked but again it lies on a spectrum.
*  Breaking universality gradually and using that as a constraint to link to the data can
*  be sort of a promising way forward.
*  Asking the right question is the hardest part of science.
*  I want to be in a place where people ask me that question.
*  This is Brain Inspired.
*  What's the best way to model the functioning brain using neural networks?
*  How do we even talk about the emergent properties of massively recurrent interacting neurons
*  without just throwing up our hands and falling back on the vocabulary of folk psychology?
*  Neuroscientists and AI researchers for years have been interested in how exactly deep learning
*  networks work, how to open the black box so to speak and make sense of those networks.
*  After all if we can't make sense of a deep learning network what chance in hell do we
*  have of making sense of the infinitely more complex real thing, the brain?
*  Omri Barak and David Sosilo are two peas in a black box pod.
*  Hmm, that was dead on arrival.
*  Omri and David wrote a paper about a decade ago actually called Opening the Black Box
*  where they used the language and tools of dynamical systems theory to describe the emergent
*  properties of artificial recurrent neural networks or RNNs and they found reliable structure
*  within the dynamics, something David has come to call the dynamical skeleton of the RNNs.
*  Omri works out of the Israel Institute of Technology and David who's been on the show
*  way back on episode five I think, long time ago, works out of Stanford University as an
*  adjunct professor among other venues.
*  And since that black box paper they've both continued pursuing how much we can glean about
*  the function of RNNs using those tools of dynamical systems theory and how it compares
*  with and how relevant it is for how brains function.
*  So this episode is basically all about that.
*  Omri and David reflect on their journey since that original black box paper.
*  We discuss the merits of the machine learning approach to modeling brains versus the sort
*  of more classical computational modeling approach.
*  We talk about the idea of recurrent nets as model organisms similar to how we treat non-human
*  animals as model organisms.
*  And we get into their recent thinking about all of this.
*  David's been studying the idea of universality, for instance, which is the idea that there
*  may be commonalities among artificial and natural RNNs despite their vast differences,
*  both among them and between them.
*  And Omri, among other things, has been studying the learning process in RNNs, like how the
*  dynamics can act as a sort of ongoing prior on the learning process.
*  So if some of that doesn't make sense, don't worry, they describe it better in the episode.
*  And I link, of course, to the related work in the show notes at brandinspired.co.
*  slash podcast slash 97.
*  If you like the show, consider supporting it on Patreon, where I offer a few extra things.
*  There's a Patreon link at brandinspired.co to check that out.
*  I am Paul.
*  Thank you so much for listening and for your support.
*  And here are Omri and David.
*  So David, you were on a super, super early episode.
*  We must have some foolishness in you to have appeared so early in the podcast, but welcome
*  back to you.
*  Thanks for coming back.
*  And Omri, I had emailed you, I think, shortly after maybe I interviewed David.
*  I'm not sure, around the same time, but you were, I think, sipping martinis and roller
*  skating somewhere on vacation, and then it just hasn't worked out back and forth.
*  But I'm glad that you're both here now with me.
*  So thanks, guys, for joining me.
*  Thank you.
*  Good to be here.
*  So the place to start is that you both, you co-wrote a 2013 paper called Opening the Black
*  Box, and it was about using dynamical systems theory to help understand what might be going
*  on in neural networks, well, of networks of actual interacting neurons, also artificial
*  recurrent neural networks.
*  So it's been almost a decade, let's say, we'll just push it a few years, called almost a
*  decade, since you co-wrote that paper.
*  And you've both successfully been continuing to open that black box, rummage around in
*  there and mess around and pull things out and push things around.
*  So we're going to talk about a lot of that stuff today and where it was and how far it's
*  come and where you are now.
*  I'd like to just start asking you kind of a simple question, I hope.
*  And maybe Omri, we'll start with you since you're new to the podcast.
*  What's one of the most, the best scientific moments you've had in your career?
*  Well, actually, I think the Black Box paper might have that moment.
*  What moment is that?
*  Because that, because publishing a paper is like such a long process, is there a moment?
*  Yeah, no, but the particular thing, again, working with David on this, trying to understand
*  what's going on there and how come these things work.
*  And in particular, actually, I remember one point where we sort of, you know, sort of
*  technical, but looking at one of these trained networks and finding a fixed point that turned
*  out to be sort of a subtle point that had one unstable direction and 999, so opposite,
*  one unstable and 999 stable ones, which is sort of what we thought we might find there.
*  But actually finding it was kind of cool.
*  I mean, it was, it was really nice to see that this idea actually works.
*  And I think one of the frustrating and nice things with this approach is that there are
*  almost no guarantees.
*  So you have this idea that, you know, the network might operate in a certain way, and
*  then you look at it and then sometimes it does and sometimes it doesn't.
*  And that leads to quite a lot of frustration when it doesn't.
*  But I guess correspondingly to quite a lot of fun when it does work.
*  So the back story there, Omri, correct me if my memory has gone astray.
*  That paper is really just a textbook application of stability theory to high dimensional,
*  nonlinear neural networks, right, recurrent networks.
*  And so the way that it went down is I had just finished taking that class.
*  And so I was mucking around with artificial RNNs, you know, back then, I'm just going to say RNNs now.
*  And I said, well, geez, maybe this technique works.
*  So basically there's a culture clash there because in the technique of stability analysis
*  and nonlinear dynamical systems analysis in general, it's a very mathematician's approach.
*  And so they like to study these two, three dimensional systems where you can actually prove something.
*  Right. So it was not really a numerical approach, whereas what we did in that paper is very much a numerical approach.
*  So the way it went down is I walked up to Omri, I was like, hey, do you think that fixed points might be negotiating the dynamics?
*  Nowadays, we would call that, the way I would say it now is, do you think the fixed point structure is the dynamical skeleton of this system?
*  Right. And he said, yeah, maybe.
*  And so, so then, so but I didn't know what to do.
*  And so Omri had the idea, he figured out how to make the optimization go.
*  And so then once we had like, hey, wait a minute, there's a thing here.
*  Then we sat down together and started analyzing a bunch of examples.
*  How often do you think that happens when someone is just taking a class,
*  that class sort of leads to an idea and you go from class versus having an idea through your own research?
*  I mean, I know that they're all intertwined, but.
*  You know, I think I think anywhere ideas anywhere you get ideas from.
*  Right. So the problem with classes is like, unless you're really in a new field, in this case, we were.
*  It's very likely that someone will have already trot over that territory.
*  So more likely your own research program, the people you're talking to over time are going to give you ideas that are fruitful in terms of the cutting edge.
*  But anything goes.
*  So for the record, before we proceed, are you guys and Omri, I guess we can start with you as well.
*  Are you more interested in brains themselves or how how brains function, you know, like, you know, the mind or intelligence or the relation between brains and minds or something else?
*  How would you describe what it is that, you know, gets you out of bed?
*  Yeah, that's a surprisingly tough question.
*  You know, I'm in a field where identity crisis is sort of the norm.
*  You know, what sort of the what am I?
*  What are you? Mathematician, physicist, biologist.
*  I think what I'm interested in is how complex systems adapt to their environment.
*  I think that sort of and that includes artificial networks.
*  It includes cancer and genetic networks.
*  It includes brains.
*  But but in a sense, I'm interested in the in the commonalities between these and and the differences in whether studying one can inform us about the other.
*  So my intuition is that there are things that are similar among all of them, and there are things that are certainly different, but also technique wise or data wise, the aspects that are more accessible in in one or the other.
*  And therefore sort of hopping about between them has the potential to sort of keep providing fresh viewpoints.
*  And so I think that's sort of part of what wakes me up.
*  You're almost saying you're interested in complexity.
*  Is that too far stretch or complexity theory, for instance, right?
*  Complexity science, because it seems that sort of not.
*  I would say it's not well defined enough or too large.
*  Yeah, OK.
*  If you will. I mean, you could say, you know, how the properties of strange attractors, right?
*  Is that complexity could be?
*  I'm not interested in that.
*  I mean, it's it's it's funny if I bump into it, but but it's not what drives me.
*  So the learning process, the interaction of a complex system within its environment, the adapting and how that changes.
*  The complex system. And why?
*  Why do they? Why does the system have to be complex in order for that to work in the first place?
*  David, what do you how would you respond to that?
*  So, well, for my part, I'm very much interested in how the brain works.
*  Right. That's already being a topic that's impossibly difficult.
*  So I'm happy I'm happy to hang out in that world.
*  Very much motivated by how what we might understand about the brains can improve the lives of people.
*  So for me, you know, the crossover is into neural networks because I do believe that they are some, if you will, model organism, artificial minor portion.
*  We can study these things in ways that we cannot.
*  So for someone who has a sort of technical bent, you know, the experimental difficulty of neuroscience is just impossible.
*  And so we I've been focusing on these other tools because of sort of both a hypothesis that is my guess and some some very preliminary empirical evidence that artificial networks are actually pretty useful.
*  So that's that's the world in which I'm hanging out.
*  So one of the ways that people think about brains is that brains compute things that their computers, maybe not digital computers, you know, von Neumann style computers.
*  But there's a lot of computational descriptions about what brains do.
*  And I'd like to ask about this idea of computation through dynamics and how how to think about that kind of computation versus the way we normally think of computation as using an abacus.
*  And moving a few pieces around and getting an answer or something.
*  David, maybe you can speak to how how that how computation through dynamics differs from a more traditional Turing machine like computation that we would consider.
*  Right. So the first so coming to starting very high level, you know, there's this our brains computers, you know, yes, brains are computers.
*  There are also a lot more, though. Right. I mean, this is a computer that cares about its place in the world and surviving, etc, etc.
*  But on top of all that, it is also a computer. So that's my opinion.
*  The way that I like to say it is that brains are really crappy von Neumann computers built on amazing neural networks.
*  And, you know, modern day artificial neural networks are really crappy artificial neural networks built on top of amazing von Neumann machines.
*  Nice. All right. So they're related somehow.
*  So that's sort of my perspective there.
*  Now, you there was there was another question that you were you were asking.
*  Well, just how to think about computation through dynamics, like within the dynamical systems framework, right, as a trajectory through dynamical space versus a more static and binary like Turing machine type computation.
*  Or if I'm even thinking about them differently in the correct way.
*  So getting to the answer through dynamics versus getting to the answer through binary computation, let's say.
*  Does that make sense? Yeah, I guess so. So the way the way I would say it is, I mean, dynamics are everywhere.
*  Right. I mean, even when you have a for loop and you want to do a sort, you are still doing something iteratively.
*  Right. So there you go. Right.
*  But but, you know, these days, especially in the machine learning world, the conversation is often one about developing representations that are that are useful for computation versus at least what we've been trying to put forward the dynamics of a computation.
*  And so I don't view these things necessarily as opposed rather complimentary.
*  It's just that I don't really know of anyone who's an expert at all of it.
*  So I'll just admit my own lack of expertise in sort of feed forward representational world.
*  Although, of course, I can have a conversation about it, but I don't I don't research it.
*  So in the computation through dynamics framework, the idea was like, hey, can we use the basic features of dynamical systems, fixed points, linearizations, all of those tools to understand what this complex nonlinear system is doing?
*  And what has turned out to be true?
*  And this is why I think there's there's energy behind it, because it's actually working to some degree.
*  Right. It's not perfect. But I mean, we're dealing with really hard stuff here.
*  But it's empirically it's turned out that you can actually glean insights from some of these techniques.
*  And so that's really what's driving it.
*  It's not so much that this is the only thing.
*  It's rather that, hey, this thing is actually yielding insight.
*  Omri, I don't know if you want to comment on that.
*  I guess, yeah, just just one one thing that I guess it's sort of an association from that is about precision or how exact things are.
*  And the concept that at least I associate with a Turing machine is a very precise, deterministic, if you will, trajectory that has a very discrete set of options.
*  In a dynamical system, naively, you could think of this high dimensional space where you can wander about and maybe have some noise and things of the sort.
*  And a trained recurrent neural network after it has formed these fixed points, in a sense, is in between.
*  If all it has, let's say in a flip flop example, if all it has is a few very strong attractors and everything around it is a business attraction of one of these attractors, then in a sense, it's almost like this Turing machine, because
*  there are very few options for that dynamical system to be at.
*  But I think one of the nice things about these trained networks is that they're imperfect, which I think is what biology does as well.
*  They have to be good enough.
*  They don't have to be perfect.
*  And that means that you don't need a fixed point.
*  You can have a slow point.
*  You don't need all the trajectories to end up in the right place.
*  You need both of them.
*  So the connectivity that has been obtained via training
*  restricts the space of possibilities of this dynamical system.
*  So you can't wander about in this high dimensional space and get lost.
*  But it doesn't restrict it to just being two, three options like a well designed and well behaved program would.
*  So it's sort of in between.
*  And I think this in between these approximate objects are part of a characteristic feature of both trained networks and I think biology.
*  That idea of sort of wandering around the area of what a Turing machine would find a discrete answer to whatever output, right?
*  You're going to eventually output that dynamical systems idea of wandering around.
*  And that approximate area has I mean, it's really changed the way that I think about, well, minds and brains.
*  And I'm wondering if your work, both of you, if your work on applying dynamical systems theory to recurrent neural networks,
*  if how your thinking has evolved with respect to recurrent neural networks themselves, just very high level.
*  You know, you started in a Turing place and now you're in a much different place or how has it sort of changed the way that you think about these things?
*  Go ahead, Omri or David, whomever.
*  Yeah, I'm fired up for this one.
*  So, you know, if you just look a little bit at the history, first there were hot field networks, right?
*  And those are just attractor networks.
*  You can really think about just marbles rolling down hills, right?
*  And so that was a very powerful insight.
*  And people really thought that through for a long time.
*  But it's restricted because those dynamics are very limited.
*  And so then, you know, this idea came out of Echo State Network or Liquid State Network.
*  And that's the idea that, hey, you just throw a pebble in a pond and whatever ripples and crazy interactions it has with the edge of the pond and other ripples happening in the pond,
*  you can decode that and make sense of what happened.
*  In other words, you can back out the pebble getting thrown into the pond.
*  So that's the idea of Liquid State or Echo State Networks.
*  And that's sort of the radical other side, right?
*  This is as far unstructured as it doesn't even matter.
*  Like any medium that sort of reverberates can be used for computation.
*  So what has happened for me, especially with the onset of deep learning,
*  is that I started applying Echo State ideas to neural data.
*  And what I discovered very quickly was that real biological neural data is much more structured than Echo State Networks are.
*  And that the sort of wiggles in an Echo State Network are just sort of wild and out of control in ways that don't make sense empirically when looking at brains.
*  So, well, we started trying backprop now.
*  And that is to say no longer just a random network where you have a readout that you're training, but the whole thing gets to be trained.
*  And all of a sudden, the comparisons started getting a lot more close between the brain and the artificial networks.
*  And I think it just speaks to the idea of what Omri said, which is that, you know, things have to be good enough, right?
*  The computational primitives have to be good enough, but otherwise it's sloppy and that's OK.
*  And that's kind of the world that these artificial networks live in.
*  And apparently, if you believe the comparisons between brains and artificial networks, it's likely where the brain is hanging out a lot of the time.
*  So my evolution has come to this place of sloppy, but has to be good enough.
*  And I just to add one more point to it, I also think that computation itself is fundamentally regularizing or robustness making.
*  If you want to be a successful organism and you have to integrate whatever information in order to eat, you'd better do it reliably.
*  And the dynamics of your system, neural system that's making those decisions, it's going to reflect that.
*  And thus, when you look in the state space and the dynamics, you're going to see something, hopefully, that's intelligent, intelligible.
*  To me, there's also something I guess one one.
*  OK, I think the idea of the tension between these two ends of the spectrum that David described, you know, this very ordered and very chaotic and that the things are in the middle.
*  I think it also exists in your data itself.
*  So, again, historically, because I think because people recorded single neurons, then they had to make sense of these single neurons.
*  So they gave the names and they told stories about them.
*  And that sort of pushes you towards the side of the spectrum where everything makes a lot of sense.
*  And every piece of the puzzle has a very specific role in the whole in the entire organism or network, where this ecosystem approach says nothing matters and everything looks like a mess.
*  And to me, I started looking at data during my PhD.
*  I looked at neural data and this to me was the push away from the ordered part because I was sort of I read the papers and I saw the nice neurons in the figures of the paper.
*  And then I looked at the data and suddenly, I mean, how come the figures represent 10% of the data and 90% looks like junk?
*  And then I start speaking to more and more people.
*  So we, of course, you know, 90% looks like junk.
*  We just pushed in a drawer and never look back.
*  And then I said, OK, so so the data tells me that we need to go somewhere that's less organized.
*  And then personally, my natural inclination is towards the let's say the eco state approach of, you know, let's let's take this mess, messy pile and everything can work.
*  And we don't need any predetermined structure.
*  We don't need to memorize names of if every neuron has a name or every brain area has a name, every gene has a name.
*  I need to know these names and I'm very bad at memorizing names.
*  So I'm more comfortable personally with this holistic approach.
*  But then I know I'm wrong.
*  I mean, I know that I'm criticizing these single neurons too harsh in a sense.
*  So I know that it's my personal laziness that pushes me too far into that end of the spectrum.
*  And I know places exist and I know things that, you know, this organization is there.
*  So in a sense, to me personally, it's I'm sort of using these many times as sort of thought experiments in a sense that I'm saying, let's see if something that's as wild as this can work.
*  But I know it's too far.
*  And then I correct myself in a sense.
*  So so to me, that's an interaction with with data is both to push away from that pole and to attract myself back to that pole because of my personal sort of inclinations.
*  So when you guys use dynamical systems, do you feel like you're learning about brains or minds or both?
*  Definitely both.
*  Both. Is there a distinction? Do you distinguish between brain and mind, David?
*  Boy, that's that question.
*  The question is above my pay grade, I think.
*  I mean, what I'm trying to do, what I'm trying to do is make the pieces and components lead up to computation and whether or not computation is mind is anyone's guess.
*  Right. Certainly in its most basic forms, it's not.
*  But if you say, well, if all these pieces are functioning correctly, somehow mind arises.
*  Well, maybe maybe I'm speaking towards that, but I really, I really wouldn't know for sure.
*  Omri, I mean, I'll ask you the same question and then we'll get into, you know, just using RNNs as model organisms.
*  So again, the brain mind is this tiny question.
*  But I guess I think the way I view mind is a bit like a temperature or other emergent properties, if you will, in physics.
*  Is it a convenient name for a complex phenomenon?
*  And and that's and the thing is that these convenience means that ignoring that can be extremely inconvenient.
*  So only saying there's there's a bunch of neurons and they are active and let's not talk at all about whether there are internal representations and whether thoughts and things like that might make like, you know,
*  maybe technically correct, but extremely inconvenient and therefore not so useful.
*  So so that's just, I guess, a rough thing.
*  Whether whether these dynamical system concepts are applicable to brain and to mind,
*  well, to brain, certainly, because that's the dynamical system we are considering.
*  To mind, in some sense, they have to do that.
*  But you might even say that, again, if you want to be extremely radical,
*  you could say that the dynamical system is brain and the fixed point structure is mind, because that's the emergent phenomenon.
*  Right. You have a certain connectivity that that developed through some interaction with the environment.
*  And now you have this, you know, this, let's say, fixed point landscape or dynamic landscape and that and there are many different implementations that could give to this rise to the same landscape.
*  But that landscape is what allows you to function in the world, if you will.
*  So so in the sense that the sort of the higher level, whether that higher level, of course, it's a tiny component of mind.
*  You know, there's no emotions and it's a very it's a very small component.
*  But I think it does have the flavor of an emergent phenomenon, because you have you have a certain dissociation.
*  You can have many different networks that will give rise to the same dynamical landscape.
*  And to function in the world, you care about the dynamical landscape.
*  You don't care too much about the lower level implementation.
*  So in that sense, I think you could sort of again probably irritate and several philosophers.
*  But I think you could equate these these two levels to brain mind.
*  That's why I, you know, it's hard for me.
*  I'm still rubbing my head around thinking about fixed points and, you know, dynamical landscapes, because it almost is and especially the vocabulary doesn't help because the word attractor sounds causal.
*  Right. And then you start to think about, you know, a fixed point is like pulling the neural activity toward it when, as you just said, it's more of an emergent property that these things are happening.
*  And it just the system happens to be configured such that there are these fixed points in the landscape.
*  But then, you know, and, you know, like we think of mind sort of as like causal.
*  And this is now we're going way off rail here, you know, whether mine can cause things, you know, and whether mine is at the phenomenal to brain.
*  But it just I don't know. It has this in between kind of feel that feels like it's getting at least closer to being right between brain and mind.
*  But, you know, there's still a lot of stuff up in the air, I feel like.
*  So that's why I was asking what it feels like to you guys.
*  Well, to the degree again, I feel like I'm over my head over my skis here, but to the degree that dynamics is related to mind, then we're on the right track.
*  And if you feel like the dynamics are emergent from from the parameters in the middle part is the fixed point skeleton that determines the topological flow of everything,
*  then we may be on the right track. But that's really all I have there.
*  All right, guys. So backing up.
*  So the history of neuroscience is mostly studying animal models, right?
*  Model animal model organisms.
*  You study their behavior, their their brains, you study their behavior, give it a task, see what comes out while you're recording brain activity, et cetera.
*  And then you infer generally to humans.
*  And I guess, you know, with fMRI and a bunch of other technologies now we're recording human brain activity or proxies thereof.
*  But you both it's interesting you both introduce your talks often with this idea of using recurrent neural networks as the new model organism, essentially.
*  And you both talk about the difference between this more classical neuroscience approach to modeling where you think about what might be going on and you build your model that way versus a more machine learning modeling approach to understanding recurrent neural networks, be they artificial or natural.
*  David, can you just explain the difference? And then I'll come back to you for for a question as well.
*  Yeah, sure. So the tried and true methodology for a good number of decades in the early computational neuroscience was you observe a phenomenon in some neural data and then you go build a machine that is a neural network by hand that reproduces some features of that data.
*  And if you can do that, then it's a reasonable thing to say that whatever you cooked into that network could potentially as a hypothetical as as rather as a hypothesis explain the neural data that was observed.
*  That's called building a model, right? And the, you know, by hand and it's great.
*  And so, but given the difficulty in especially systems neuroscience, right, when when lots of things are interacting, that's that's when that's when sort of reductionism starts to fall apart methodologically.
*  Given the sort of lack of progress, it became a question. Well, what if what if we just don't know how to do that? What if it's either too hard? We don't have the right ideas, etc, etc, etc. Too high dimensional. Who knows? Right.
*  We just don't have the intuitions. And so that's where the training approach comes in. That is to say, you know, the way that I would express it is under some under some robustness principle, we don't want all solutions.
*  We'd like our solutions to not be insane, but under some robustness principle, just let an optimization of all of these parameters sort of settle down into something that looks like your data and then go study that.
*  Right. So that's that's what the approach is.
*  Just to follow along there, Omri, you think recurrent neural networks and dynamics may provide the quote unquote correct or better simple parts that we need to study to learn about the larger, more complex functioning system. Can you just elaborate on that idea?
*  Yeah, I mean, so one thing I just remember to to mention is that I think similar things have been done in evolution, basically. So there was there are still are some works that try to use genetic algorithms to get, let's say, genetic circuits.
*  And that that would do a certain function. I think most again, not also many of these works use very low dimensional. So they wanted to see how how negative feedback circuit arises. So you have like five nodes or something.
*  There are works that use larger networks, say either enzymatic or genetic.
*  I think Konekwa Lab has quite a few of them. These approaches existing in other realms as well. And then now I completely lost my thread of.
*  Well, I mean, you've made the point that part of part of the entire point of science is to use simplified things and use the simple parts to understand the larger.
*  So then there's a question of why, why do you need a model at all? Right. I mean, so in principle, if you want to understand a system, then you want what does it mean to understand the system or to have a model of a system? And there are many different answers to that. Some people say that it's prediction that if you can predict how the system will respond to a novel stimulus, others will say that if you build it right, if I know how to build.
*  Something that does this function, then I understand how it works. And then, of course, there's the old bird playing conundrum of I can build something that does the task, but is it do I understand birds? And I think.
*  A, I think it's in defined. I don't think there's there's an answer to what is it mean to understand something personally. I think that I'm sort of I guess in between the prediction and the building part.
*  It's a subjective question. Actually, what is it mean to understand something? I think you'll you'll have different people give you very different answers for the for the exact same system.
*  Whether you know, for some people, if you don't have a pharmaceutical agent that cures a certain disease, they will say that they did not understand the system.
*  And others will say that having your pharmaceutical agent means nothing about understanding because just means that you found a trick that works by accident. But if you look at it and you know what it means, then that's understanding and.
*  Yeah, great. Go ahead, David. I was just gonna say, I mean.
*  I think I'm speaking for Omri here as well, but speaking for myself for sure. I mean, we're definitely in the camp of.
*  Did you even understand the data at all? Right? So like, let's let's not lose sight. Right? I mean, there are data sets in neuroscience where nobody has any idea what's going on.
*  And so I feel like the progress and I do think it is progress, however limited that we were able to help along with is say, hey, look, there is a way to even come up with words for what that data might be doing.
*  Because, you know, at least for some examples before this reverse engineering approach, there would be nobody knew they literally just didn't have an idea.
*  So I do feel like there's been some progress in that, but I don't want to take it too far either. I think I think there's a lot of misses that that might be happening with this the artificial neural network approach.
*  Something that's commonly talked about is, well, you know, what do you have, what do you have to put into it in order to make it look like your data? So it turns out that you'd like it to be as simple as.
*  Match some task on the animal does task a training network to do task a and wouldn't that be great if that was enough to make your neural system now that is to say not its outputs because you optimize them so that they're going to look like what the net what the animals doing.
*  But the internals wouldn't it be nice if the internals just based on that task matching looks like the animal model animal neurons.
*  Excuse me.
*  It turns out it doesn't work right. So that's the dirty secret of the approach is that you have to add a lot of extra stuff.
*  And so what we're what I think that the subfield is coming to is an understanding of or trying to develop an understanding of what those things are.
*  For sure. It's a robustness principle. That is, you don't want very crazy systems. That's just not what brains are doing. Right. But there's other ones that are very particular to the to the system at hand that you're studying.
*  And so one could argue that what you're really doing now is instead of building a system you're you're picking the hyper parameters such that an optimization program builds your system.
*  So if if you haven't reduced some complexity there then you really just have kicked the can down down the sidewalk for a block without learning anything.
*  But I but I don't I don't believe that. I think we I think you have reduced the complexity and you have carved up the space of solutions a little bit more.
*  Yeah, I asked Omri that because he has expressed the notion that thus far neuroscience has by and large failed to find useful simple parts that you could then put back together that in an explanatory or building fashion to make the complex system.
*  So does that ring true to you?
*  I mean, I think again what I basically yes. So I think that my critique was of the let's say single neuron and particularly the single neuron that was exposed to a limited stimulus set.
*  And then and then you start picking on single neurons, man, they're just fine.
*  But in a sense any any.
*  All context dependence basically right so so if you if you probe a system with a very limited set of stimuli, then often you'll find that it does not generalize well when you want to understand how it works otherwise.
*  And then the question is whether these but if you chart this dynamical landscape, then you might have you know, then these rules could be more general.
*  So in that sense, these could be building blocks that are that are more useful.
*  But again, maybe not.
*  Maybe you you do this.
*  You train on a simple task and then you see that if the network has another task in the background, then it will change completely perhaps.
*  Or and I think one one thing that I want to relate to to what David said is that another way to think of it is you know, we train you optimize a network to the task.
*  And then you hope that it will match the data just by virtue of that.
*  Another way to think of it is that maybe you don't because.
*  There could be several solutions to the task right so you could have if you think of it you have you take one particular organism that's trained in this task.
*  And then you take one particular network that was trained in that task now it could be that two different monkeys that learned the task or two different mice that learned task solve it differently.
*  If that happens then.
*  Then what do you hope for me do you hope for the network to to match animal a do you hope it to match animal B do you hope it to match the common aspects of all animals that if there are any.
*  So so I think even that.
*  Even that hope is sort of.
*  If you stop to think of it it's not that trivial.
*  This also brings brings up the topic of universality here I don't know.
*  Yeah yeah well let me ask let me ask one question then I want to pause and i'm going to ask you guys how we should proceed, but.
*  You mentioned that you know the different tasks and the simplicity of many of the tasks and.
*  These days in neuroscience there's just crisis after crisis around every corner, it seems about how we're doing it wrong one of those is that we're not using ecologically valid tasks.
*  And one of the strengths of using let's say recurrent neural networks as model organisms is that you can give it these these same tasks that we're using in animal models right and then ask it to output some behavior match the behavior test the innards of the recurrent model the dynamical.
*  Landscape for instance and compare that to what you see in monkeys much as you know david's done you both done do you worry at all that.
*  The tasks that you're asking your recurrent networks to perform which are often even simpler right three bit tasks and sinusoidal wave tasks in an effort to simplify in an effort to understand.
*  Do you worry that asking your networks to perform a task that is so far removed from the way what animals do in the wild for instance that the answers that you're getting aren't applicable.
*  So I think there's really two axes there right one is.
*  Ethological relevance and the other is complexity of the task and I am much more concerned about the latter.
*  The as being as moving forward and getting the right answers.
*  Yes exactly so the last 10 years have been like hey let's apply these approaches and study these simple what are what we now call simple although it wasn't obvious 10 years ago.
*  But study these simple tasks right and so that's gone you know from from memory to decision making to blot a blot a blot a block.
*  And we've just gone down the line and so well the criticism I think extremely valid criticism is like well brains do lots of things.
*  And they you know so that's is really the magic and how the different how different tasks are solved that is to say if task a has something to do with task B.
*  Does you know is there a generalization aspect to that and how is that captured in the dynamics etc etc this is something that's deeply concerning to me and.
*  I work on that in my research with with postdocs and pushing pushing that idea forward of basically multitask systems so to me that's really critical critical element which is like do lots of things and the other.
*  Generality that's right and so the other is like reaching for example let's say you want to understand arm reaches and motor control of arm reaches.
*  It's one thing to say hey we do the standard center out reaches reach up reach down left right.
*  And so first is let's grapple with the total complexity of this I don't know what it is 50 degrees of freedom arm and digits that can lift and control force and strain and all the rest of it.
*  And so I think that's where we want to go but there are lots of problems in the way including not the least of which is just experimentally getting that data in a rigorous way right so I think there's problems both on the experimental side and on the modeling side but that's clearly where we need to be going.
*  I think one one other aspect that.
*  You know where I think we might want to go that's sort of a tricky aspect is is the process of learning itself so in principle I very much agree with David using the word optimization for this and optimization.
*  In principle in a sense is a process that it doesn't have to be process optimization is finding the best solution.
*  Where is if you think of learning in in a biological that setting it happens over time and in many cases I think you know.
*  David and I many others have been careful to sort of say look here is the network after it has been trained.
*  And this is the object you should be concerned with how we got there you know don't ask us about it that's you know we pulled it out of somewhere it's not of no concern to you.
*  And I think in many cases it's correct and it's a valid warning to issue but I think another sort of.
*  Aspect that I think is is worthwhile to push forward and it's related to the relation validity with respect to biology is the process itself so for instance if you if you know how to perform any tasks.
*  Then they are built on one on top of the other.
*  Right so you have an existing scheme of of that that you learn that you generalize for many tasks and now you learn a new one compositionally you mean.
*  It can be composition it can be you know you know these issues of catastrophic forgetting or but if you if you if you learn a family of tasks and you learn them sequentially.
*  Or you learn your battery of task and then you add another one that already has something with the process in which in which you learn in which you learn and I think that's also somewhere where we can connect.
*  I'm better to to constraints that are in the experience themselves.
*  I guess I agree it's just it's too hard for me.
*  You know when you look at the literature on learning and in the biology it's it's it's the classic example of like a thousand hundred thousand small details with no way of figuring out how those small details come together into something that makes any sense so I find the problem overwhelming personally.
*  So you guys are both working on what you might call a space of solutions right for recurrent neural networks and that is like for a given task or sequence of tasks right or you know interleaved or you know however you want to do it.
*  A family of tasks depending on how you initialize weights and how you train you know that process what range and types of solutions.
*  You know arise through training that network and and David some of the latest work that you've been doing is is on what you call universality which is you know and you can correct me but the roughly the idea that different neural networks might converge to.
*  You know the same or universal solutions right and only you're maybe more skeptical and through your work you've seen that maybe this is not so much the case so we can just go down that road a little bit and David that I define universality.
*  Correctly and and take it from there.
*  Yeah sure so i'm going to diffuse it a little bit at the outset I'm going to be talking about an ideal here and surely what happens in real life if anything about what i'm hypothesizing is true would not be ideal.
*  But nonetheless it's still a guiding idea so the idea of universality is that different dynamical systems sort of have properties that are conserved despite the fact that the equations are different.
*  Or in our parlance despite the fact that the parameters of our neural networks are different right so the classic example.
*  Yeah this is lots of classic physics examples but they're pretty complicated but the classic example in math is Feigenbaum's delta so with these little one dimensional RNNs one dimensional maps they're called you can show that if the if the one dimensional map has certain properties it's unimodal and three or four of these properties but basically.
*  But basically it if it has these things it doesn't matter what the equation form is it will have a number called Feigenbaum's delta related to the onset of chaos and that number for six four point six six nine something something something something something it's the same number across any system that has these properties.
*  Right so I took a lot of inspiration from this example at the first off it's just great science and accessible and people should look it up because it's amazing.
*  But you know in terms of my own work via reading some of that and conversations with people along the way I've started to wonder if artificial neural networks are similar to the degree that we're showing them like you have we're already buying into that hypothesis and not everybody does.
*  But to the degree that artificial networks are similar to brains is there not a universality property going on that is to apply the universality idea directly to brains and artificial networks that is despite the fact that the equations of RNNs are.
*  Almost surely totally different than whatever biophysical equations you'd write down for brain no matter what level of abstraction you try to get at you still going to have massive mismatches right.
*  So given all of that mismatch between what we're trying to model and the tool the RNN that we're using to model it why should anything look similar.
*  Right and my evolution on this topic I've basically come around I'll admit it I'm very much in the universality camp and let me tell you a little bit about my evolution on the topic.
*  I mean in my PhD 15 years ago when I started making networks and you know copying the echo state network algorithms out of the out of the paper and studying what was going on.
*  I thought a neuron was a neuron and what I mean by that is an artificial neuron in my network was a one-to-one mapping to a real neuron in a brain I actually bought that idea and I don't believe it anymore not one bit.
*  You mean functionally you mean?
*  Yeah functionally I'm sorry obviously there's a neuron is a physical thing in a biological animal versus.
*  The mapping doesn't sort of.
*  That's right yes I thought the mapping was one-to-one at the neuron level.
*  You were naive.
*  Yeah basically so but when you take a closer look you say well there's you know neurons have integration properties that integrate over their inputs over synapses and then they decide to fire so there is a little bit similar.
*  Similarity there but by and large I mean artificial networks have floating point accuracy their their their rate networks there's no spikes going on right there's a lot of reasons to be deeply skeptical and then at the higher level the artificial network just has some equation right you say.
*  It's a simple most simplistic form it's a linear system with maybe a saturating non-linearity so you have this matrix application to a vector and then you saturate it and that's your network that's just not a brain nor is it even a network in a brain right there's so much other structure going on.
*  Inhibition excitation spikes all kinds of things in a real brain so that ask the question well why should there be similarity and so if you if you move forward through the 10 years of applying our names to brains and seeing a number of successes.
*  You say well what's going on there so my thinking is that coming back to universality the idea is that these dynamical skeletons that is to say the fixed point structures right.
*  Those things are potentially the conserved element that those are the universality sort of numbers if you will the 46994669 that that is that what the universal property amongst these systems.
*  And there's lots of reasons to think that that might be true not but not necessarily the particular exact fixed point location although if under very precise circumstances maybe.
*  But because these when when we look at fixed points I don't actually care about a fixed point I care about the topological flow of the dynamics in the high dimensional state space and that's what these fixed point structures are negotiating so if a if a if a task requires these properties to be done if it needs these dynamics to be done correctly.
*  Then you need to organize a system that has those dynamical flows and that's the idea of of universality to me as applied to artificial networks and biological networks.
*  Is it valid to say that the other way to think about this is that given the vast differences that you described between you know a unit and a neuron.
*  And yet these you know the the dynamical landscape when you train on a task comes out at least in a similar way if not you know exactly the same in some cases.
*  The other way to interpret that is that the dynamics is is trivial and just something that would come out of.
*  So many other things that maybe it's like the least important thing maybe that reduces its importance right so that's a minor rebuttal but just it occurred to me that that's one way to think about it does that make sense.
*  Yeah so I think that falls into the line of criticism that what we're really studying is tasks and not and not animals so I think to some extent that's true right and and but nor do so again I want to diffuse this a little bit.
*  I don't think that that everything is universal I think it's a guiding property and if you if you set up precise artificial examples you could find I'm guessing my hypothesis very conserved.
*  Probably universal structures of fixed point skeletons right but coming back to the animal which is what you're talking about and the animal has to do lots and lots of things.
*  So lots and lots of tasks to survive so my guess is that the analogy there is well when we see something when we see a dynamic in an artificial network that helps us understand the recordings that is the dynamics the state space dynamics of of animals and we see an overlap there.
*  That what we're why we're seeing an overlap there is some hint or substructure of universality required to do the task or for example.
*  It will and David you didn't really and we don't need to go into detail I suppose but you've tested lots of different types you ran a bunch of tests on hundreds and hundreds.
*  If not thousands of different families of recurrent neural networks and trained in different ways and looked at you know compared them all and then rearrange them and found that there is there are clusters depending on how you look at it.
*  And that you know well let's just let's just talk about it and then we can go back into all these stuff and how it differs so so there's geometrically let's say I'm going to summarize it and then you can maybe detail a little bit more so that geometry.
*  Differed among the recurrent neural networks but the and you can talk about what that means but the fixed point topology so basically the dynamical structure of the networks.
*  All sort of overlapped in many ways so that was that was this universal aspect is the overlapping dynamical structure whereas the different architectures differed in the geometry of the representations and maybe you can elaborate.
*  Yes sure so in that we're talking about a purely artificial studies so there's no biological data here right so I'm testing the idea we were testing the idea.
*  That even in an artificial setting could we find things that were highly conserved structures that were highly conserved across networks that had different equation forms.
*  And different parameter initializations that is to say after training them to death each of these networks you get something that the system solve each system solves a task do the internals as we understand them as visualized through dynamical skeleton and what all of that means are is that conserved.
*  And this is across LSTM's vanilla RNN's GNU's.
*  That's right GRU's.
*  GRU's.
*  Yeah whatever whatever all the standard stuff that people are using in the field right now.
*  And keep in mind those equations are very different like a vanilla RNN is a very different equation on paper than an LSTM very very very different.
*  So a mathematician would night and day right.
*  They do have common elements for example saturations and matrix multiply matrix multiplies but they're still very different so what we found was that if you were to sort of.
*  I don't know how precise to get here basically the geometry of the solutions looked a little different that is to say some were stretched some were rotated differently there's also an unidentifiability there but basically the geometry varied from from.
*  Network to network but if you were to imagine the flows of the dynamics that is to say the dynamical skeleton is negotiating these flows that creates a topology.
*  So in other words to me this if you have a long ellipsoid network state space that does exactly the same set of flows topologically as a very compact circular one that they're doing the same thing.
*  Right and so what we found is in that topological view that.
*  Literally every every every network was basically identical to keep in mind you know there's a lot of experimental artificial experimental.
*  Technology going on here but across thousands of examples and even if we got a few wrong in terms of our analysis it would still be like well.
*  99.9% of these networks are all doing the same thing when viewed through this very specific dynamical systems lens and that was that was the result.
*  First of all I think the very much agree with with David's.
*  View of of in description here of of the first of all the analogy what or in a sense what is the proper way to compare the model data to the experimental data.
*  Right is it the single level is it the task level is it the dynamical object level PCA there are many different levels at which you can do this comparison.
*  And I'm quite convinced again as David said that the single new one is not.
*  Is not the correct one again because it's biologies is sort of.
*  Single segment of a dent right is more complex than a than a full artificial learning.
*  But then I think that the you know your question and what David said is sort of highlighting as always does the spectrum right so.
*  If it doesn't matter then can I have a send the pile.
*  Equations of a send the pile that don't even pretend to look like in your network and they also implement the same equations and maybe I could.
*  But then the question is what are we modeling here and I think.
*  So now how how would one approach that right so you could say well if it is so universal that no matter at all.
*  What which equations are you put up there let's say the implementation level I always get the exact set of fixed point topology then.
*  Have you learned anything about the specific implementation the brains using or have I learned something about that task.
*  If it is again in the extreme case if it doesn't matter at all then obviously I have not learned anything about implementation because.
*  It just proved implementation is irrelevant.
*  But but that's an extreme case so I think the at least two interesting places to go there one is geometry might matter so it could be that the topological landscape is identical and is dictated by the task and not by the implementation.
*  But you could get that the geometrical insights or constraints from the new world data.
*  And again that that has to be done carefully and actually have not I have not carefully thought about how to do that we're not well at the same time not requiring you want to be in your own but I think that it could be done in principle.
*  Well here are two let me just give you two examples right from from neuroscience from so when when if you if you have a dynamical system and you say what you're really interested in is the topology of the dynamical flows.
*  Then you're making an argument that at least within orders of magnitude you don't care about the dynamics right right.
*  So and so how so sometimes it's just about getting from state space region a to state space region B and how that happens whether it's a big swirl or whether it's this.
*  Straight thing it doesn't matter so in that case that's a case of dynamics not mattering where the topology does but let me show you like I believe examples where the dynamics matter well for example in the motor system.
*  Right when I'm lifting my arm and controlling my arm etc etc the speed at which that happens it matters and it's precise another example is out of the.
*  May God just use that lab where they're talking about the geometry of a particular curve in state space as implementing a prior on on some kind of decision making right so that's a case where the geometry did matter and so I'm just helping out here so.
*  So I think that's sort of one one axis with which you can diffuse this criticism of over universality.
*  And then the other one is that it is possible to have tasks that are not universal so.
*  It is possible to have multiple solutions to the same task and if that is the case then once again you can constrain your models with a particular solution.
*  I'm attained by a particular animal and in that case you can also have different solutions.
*  For writing a different strategies that that different animals develop and you might sort of match them to different strategies that are developed by your networks and.
*  In a sense you can take that even further and you can ask if I have a hundred.
*  What's the mice that's all this task can I do statistics and ask what is the distribution of solutions and now if I have a million networks.
*  Can I ask which aspects of.
*  Network architecture modularity.
*  Learn rule order of trials or whatever affect the distribution of solutions there.
*  End of that inform me about some of these underline implementation constraints in the brain so I think this universal is sort of a question that has to be asked.
*  But but again it lies in the spectrum and I think that's sort of walking along the spectrum and breaking universality.
*  Gradually and using that as a constraint to link to the data can be sort of a promising way forward.
*  I totally agree with what I'm saying and I think there are different levels where things where so you basically if you have a couple of solutions then you would have a universality class right.
*  If it's at the algorithmic level so for example you can sort quick sort keep sort bubble sort there's a gajillion sorts right.
*  At the algorithmic level you would say well which one is someone doing and then my guess is if you dive into the implementation detail and you might.
*  For everyone who's doing a quick sort the implementation might still be somewhat universal or at least have hints of it right so that's that's one level.
*  And the other level is really what I'm saying about like well actually even at the implementation level of some of these tasks there still could be various ways that in which it's done and I'm aware of some some work actually.
*  In mice for integration tasks that show that so hopefully that'll come out soon so those with comments I wanted to make.
*  Yeah then I guess that one one example that we sort of we are now sort of.
*  Working on is is again at the jazz area ready set go talk that David mentioned earlier that we trained sort of.
*  Many networks on this task and and we saw different dynamical let's say topologies.
*  I'm sorry this is the ready set go task is that what you said yeah yeah yeah this is the ready set go task so that basically the task is.
*  The animal receives.
*  To to stimuli that are separated by a certain delay of time and it has to reproduce ready set and then go and if you do ready.
*  Set.
*  Go will come later at the same delay so you have to sort of.
*  Match that match the really said great yeah so translate that is set into set go and it turns out.
*  If you think of it as a dynamic a landscape question.
*  It's not that obvious so it's not that you have sort of you know decision and you go right or left to this fixed point or that fixed point but.
*  All the action is happening again in how fast you move or how.
*  Where you go and it turns out that networks that solve this task.
*  Some of them do this with let's say a one dimensional.
*  Slow manifold and others do this with a two dimensional so many for some of them curve and top of themselves some of them do not some of them generate the limit cycle.
*  And some of them do not know the limit cycle is sort of too slow to matter when you train the network but if you don't sort of let it continue then you see that some of them do that and some of them don't.
*  So so in that case you sort of have different variants of solutions.
*  To the same task and again that anything it raises many questions that we have very few answers so far but.
*  For instance if you we use extrapolation so you train the network on a certain set of delays but then you challenge it with longer delays.
*  Intuitively if if if if I tell you what the task is of course you'll be able to extrapolate because you know the rule if I just give you some examples.
*  Of these delays.
*  It's not clear how well you will extrapolate there are some experiments that show that you will you will extrapolate but you will do this sub linearly so you sort of.
*  You.
*  You will.
*  The as the delays I present get longer and longer you will start making shorter and shorter error sort of responses you still respond longer than your training set but not as long as you should have.
*  I have some experiments on the eighties but people were sort of using psychophysics to test extrapolation and people don't do that.
*  It's ill defined but they don't do it as the experiment that would have expected and.
*  And you can ask me is that even a fair thing to ask the network to do because it's ill defined so if I say networks are different when they extrapolate.
*  Is that a true difference or is not should they only care about how they they operate within the training regime.
*  But maybe I can use that to probe the network or to compare it to the new data and I think these are you know we have some clues but.
*  But so far we have many questions as well.
*  Let me let me just jump in and ask you what your thoughts are on or he has on work about direct fit and that so what you're saying is well humans can extrapolate so we could compare or animals could so we could compare.
*  Natural neural networks to the artificial neural networks but already.
*  Is that and and his research shows that maybe you know what he believes that humans can't extrapolate in that we are just we just have so many neurons are recurrent neural network is so large has such high capacity.
*  That everything that we can do well is interpolation is within the training set and anything outside it we actually fail that because we just haven't memorized you know how to do it or haven't had.
*  You know examples of it so and if that's true then comparing between natural and artificial neural networks in that case wouldn't tell us anything I don't know if you have thoughts about that.
*  I guess.
*  It's very hard.
*  It's very hard to compare extrapolation in humans who have a lifelong experience and say whether it's extrapolation.
*  Because the prior knowledge in our end is right to the table or I see you have you created out of nowhere and then you give it this task and this task is its entire life experience.
*  And then you compare it to a subject walking into the room with a college degree and you know with a lifelong experience of being out and about.
*  And you know is that a fair comparison I think David spoke about the fact that the real biological agents have a plethora of tasks that they were trained on and they.
*  They share the components and they use these shared components to to better behave in a new scenario.
*  And when you test the human on a new stimulus it's never really you because there's always some context with these artificial networks you can really surprise them in ways that they don't think you can do as well.
*  We with experimental subjects I think it's you know it's not hopeless but it's it's it's tricky to compare that.
*  Yes, so I do I do think being able to instruct humans is also a big deal right and I think that if you really wanted to study some of this extrapolation you could build in fact I did with Robert Yang Robert Yang did the building but.
*  You could build networks that actually understand language and you know if you think about config this is a side topic but if you think about configuring a neural network to do task a B or C normally you would say well.
*  Here's a hot one for task a hot one for task B hot one for task C one hot encoding rather but somehow language is modular generalizing.
*  Basically configuration for these systems right so I think there's I think there's a world where we could study those things but jumping back out to the topic of universality I definitely agree with Omri that.
*  The specifics details matter and I don't mean to say that like my little crystal are an artificial on and on my network is universally the same as some very complicated biological mammal organism.
*  But to me the idea is at least I guess maybe normative or helps me explain why when these things are so different you might actually see some similarities at all right and so that's really that's really where I would hang my my hat in terms of leaning on on that theory.
*  Omri you're hanging your hat in a different saloon or the same saloon.
*  I think the only thing I'll add is that again this is the spectrum so I think that that I want to go to the other side and then take one step back.
*  And ask whether I can use this small lack of universality to sort of you match the data or to ask you know I know my model is ridiculously unbiological.
*  But for instance is one feature of that more ridiculous than the other if I if I hold the task and play with the biological detail will that mean me closer or further away from the data also I think it's.
*  I think it is a good place to be but but again we're doing linearization right but you want to be to sort of perturb it a bit and see how it responds to various things that's right.
*  Number one and number two do spikes matter number number two excitation and inhibition there could be all kinds of reason there's excitation inhibition that is different cells right cell types.
*  For biological networks that that are concerned with actual metabolism and not getting epilepsy or whatever pick pick your favorite reason why there should be things like this.
*  Now if those if those details matter to solutions then we should absolutely be putting them in our models.
*  But if they don't matter then we need to make a sort of concerted effort both in terms of our work and something of a PR effort to say hey these things don't matter and we're not going to put these in because it's only obfuscating the point of the modeling in the right.
*  I'm just zooming out though isn't it just wondrous and exciting and amazing that there is a resemblance that we can make you know some headway into comparing.
*  These you know both of these complex systems and finding some sort of structure in the randomness some sort of potential universality I mean doesn't that do you ever just take the time to think oh how awesome is that.
*  Are you just too are you too mired in the work to take the time I think it's great I think it's very cool you know and so like it again you know this is why I don't get too caught up in the like does the brain implement back prop conversations.
*  First off as I admitted before the learning stuff just seems impossibly difficult to me so I'm picking easier problems and much respect to those who are biting off the hard ones.
*  But on top of it like if you really believe in some form of universality however minimal not however to some degree of universality but not too much.
*  Then as long as these systems can sort of wiggle into semi optimal solutions then it's not overly important how they got there I probably just made 17 different enemies when I but but I kind of I kind of believe that right.
*  Yeah again I think it's I think it's great and again this as I sort of ended earlier I enjoy looking in a sense even further away.
*  So we're looking at genetic networks looking at a topology of genetic networks and there's the sort of surprising areas where you find.
*  Similar aspects and and I and I really enjoy that so again you know I'm in a job that that all I have to do is have fun right so I try to do that.
*  Oh that's a good way to end it let me let me ask you guys just as kind of a question for the audience for the younger people out there earlier in their careers and then we'll wrap up.
*  Do you guys make time to go outside of your own expertise and think about the bigger questions and if so you know how do you fit that in do you take a date like.
*  Romain Romain Brett takes days off or at least he used to like dedicated to thinking about the big picture why it all matters how it all fits together do you guys take that time and if so how do you do it.
*  Yes it depends on what you mean by big picture I mean that can get pretty cosmic pretty quickly.
*  I don't mean tripping in the desert.
*  Yeah no so so no I guess not really no I don't take that time I'm maybe maybe it's because I already did it.
*  You know I have I believe that the work that I'm doing is important and I have empirical evidence that it's making contact with data.
*  So you know and I feel like I'm bridging what I'm attempting to do is bridge gaps between the granular and the mezzo at least if not the macro.
*  So I'm pretty okay with where I'm at and I don't spend a lot of time on that question anymore although I probably did early on in my career.
*  Do you think it's important to spend that time early on in your career.
*  Absolutely and you know more narrowly asking the right question is the hardest part of science.
*  Yeah.
*  Right.
*  You have to get the questions right.
*  It's easy to say I care about consciousness but how are you going to how are you going to get a crowbar into that question.
*  So getting that correct is the most important part.
*  And in fact you know when I sit down in in lab meetings and we have full discussions with lots of people really the most important part of that feedback for me is that process is calibrating my questions.
*  So I'm I'm lucky I guess to be in the atmosphere I'm at is the people working on around me on various things and that sort of people talk a lot about rather big questions.
*  What ones of anecdotes that when I get my job talk one of the PIs there went and said you know that was a great talk but why are you working on the brain.
*  I mean who cares about the brain you should do.
*  There's lots of other stuff that's more important and I sort of said you know I care about the brain but I want to be in a place where people ask me that question.
*  So I think it's important to to be probed to be poked let's say a bit out of your comfort zone every now and then.
*  But as as everything in this conversation right there's a spectrum and and you don't want to spend all your time being poked because you do nothing.
*  So at the end of the day you have to do things right.
*  Yeah and I think that's right there's a balance.
*  So whether this balance is you know a day a week or a day a month or a week a year it doesn't matter.
*  I mean it's very personal but but I think it's it's it's important to sort of see that you're not drifting to to one of these ends and I have drifted to to both ends at times.
*  Well thank you guys for spending the time with me.
*  I look forward to next time when Omri is studying ant colonies and David's still studying the brain perhaps but I really appreciate it guys.
*  Thank you so much.
*  It was fun.
*  Thank you.
*  Super fun.
*  Thanks for having me.
*  So.
*  Brain Inspired is a production of me and you.
*  I don't do advertisements.
*  You can support the show through Patreon for a trifling amount and get access to the full versions of all the episodes plus bonus episodes that focus more on the cultural side.
*  But still have science.
*  Go to brand inspired dot co and find the red Patreon button there to get in touch with me email Paul at brand inspired dot co.
*  The music you hear is by the new year.
*  Find them at the new year dot net.
*  Thank you for your support.
*  See you next time.

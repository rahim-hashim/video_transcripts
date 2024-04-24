---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 4811s
Video Keywords: ['Education', 'Science', 'Technology']
Video Views: 1242
Video Rating: None
---

# BI 139 Marc Howard: Compressed Time and Memory
**Brain Inspired:** [June 20, 2022](https://www.youtube.com/watch?v=T4OMK5ck2v4)
*  If something interesting happens, like if I clap, it doesn't leave our experience immediately.
*  It lingers for a little bit.
*  If things were able to change more quickly, I mean, there's, there's, look, if this is
*  really a theory of the brain, right, there's thousands of experiments that need to be done.
*  Researchers might reach their own conclusions as to why the brain and the mind choose to
*  do this, but there's no question that it does in many, many, many circumstances.
*  So my answer would be...
*  This is Brain Inspired.
*  I'm Paul.
*  Hello.
*  Can you sense that word, hello, echoing into your past?
*  If you could listen into a certain set of your neurons, called time cells, it would
*  sound something like, hello, hello, hello, hello, hello, hello, hello, hello, hello,
*  as the word recesses into your memory.
*  That's my poor attempt to mimic an exponential function of hellos, and that kind of representation
*  is the focus of Mark Howard's research.
*  Mark runs his theoretical cognitive neuroscience lab at Boston University, and over the past
*  decade or so, he and his colleagues have produced a little explosion of work based on this idea.
*  The idea is that we have lots of overlapping populations of neurons that represent time
*  and events and memory on a compressed logarithmic scale, which is a handy way to represent things
*  over a wide range of time scales.
*  Mark has been mapping psychological and neural data to a mathematical function called a Laplace
*  transform, which Mark argues is a fantastic way to represent not just memory, but all
*  sorts of cognitive functions, like our spatial cognitive maps and more, in part because the
*  Laplace transform is pretty straightforward to implement in populations of neurons, and
*  because it's flexible and general purpose.
*  And as you might expect, populations of neurons in our hippocampus, an area classically important
*  for memory and spatial navigation, cognitive maps, those neurons map onto this mathematical
*  function quite well.
*  But its signature has been found now in many parts of the brain, which would make sense
*  if it's a fundamental computation our brains use.
*  And if it's a fundamental computation our brains use, why not implement it in deep learning
*  networks, which is what Mark is also doing.
*  So we discuss many topics surrounding these ideas.
*  One quick note as well, throughout the episode you'll hear me use the term Laplacian, which
*  is a mistake due to my naivete.
*  Mark later told me that the correct term is always Laplace when talking about the transform,
*  and Laplacian refers to heat equations.
*  And Mark was too polite to correct me all those times that I used the term.
*  So don't make the same mistake I did over and over.
*  And Mark takes a couple guest questions, one from Brad Wyble who's been on the podcast,
*  and one from a Patreon supporter, Howard.
*  Oh yeah, Patreon.
*  If you value what you're hearing, that's a great way to support Brain Inspired, and
*  get your questions asked on the show, among other things.
*  My deep gratitude to you Patreon supporters.
*  Or you might consider taking my online Neuro AI course, which dives deeper into the conceptual
*  foundations of many of the topics that we discuss here on the podcast.
*  You can learn more at braininspired.co, or you can also find the show notes at braininspired.co
*  slash podcast slash 139.
*  All right, enjoy Mark Howard.
*  Mark, I want to thank you.
*  I'm going to read the first sentence from one of your papers because it gave me a delightful
*  moment.
*  And it has nothing to do with what we're going to talk about today.
*  But this is it's actually the intro sentence to one of your chapters starts, human babies,
*  while adorable, are remarkably incompetent.
*  And then you go on to do do sciencey things in the paper.
*  But it made me laugh at the time.
*  It's making me laugh now.
*  So I appreciate that.
*  I don't know.
*  Was that an intentional, put a smile on their face sort of intro?
*  Yeah, I think.
*  Yeah, no, I try to put in little subtle jokes.
*  That one was a little less subtle than my other jokes, which usually acquire no experience.
*  But yeah, it's it really struck me having kids actually, how they know nothing.
*  Right.
*  Everything, everything they have to learn, they have to learn how to stick their hand
*  into their mouth. Right.
*  They can't do that initially.
*  So memory and learning are really important, I guess one might say.
*  Well, anyway, thank you.
*  Thank you for that.
*  Really made me smile a week ago or so.
*  So there's a lot to talk about here.
*  I guess I can start with it's not the same.
*  Doesn't have the same ring as turtles.
*  But I suppose it's Laplace transforms and Laplace inverse transforms all the way down
*  in cognition. Is that right?
*  Yeah, here's how I would.
*  Yeah, that's the that's the hypothesis I'm trying to argue for.
*  So I think if I were to summarize my large scale position on cognition right now,
*  I would say that I think the functional unit of the brain is not the neuron nor the
*  synapse. It's some population of many, many neurons that cooperate to represent
*  quantities and then operations, data independent operations on those quantities to
*  enable us to think.
*  And and we've now observed and we should probably go into the weeds a little bit
*  about this at some point. We've now observed Laplace transform and then inverse
*  pairs. And we'll talk about that more for time and space.
*  And I don't see any reason why one couldn't reuse that same sort of computational
*  language for many, many different quantities.
*  So, yeah, I wouldn't say it's turtles all the way down, but there's a lot of
*  turtles. So there are a lot of turtles.
*  That's true. That's true.
*  Maybe we can back up then. And when I said Laplace, you know, Laplacian, Laplace,
*  that immediately loses people, of course.
*  But maybe you can kind of introduce in words what the main idea is.
*  And I also would love to hear how it originated, how how the Laplacian transform
*  and inverse came to be the thing that you used the mathematical equations to then
*  search for, et cetera, in neural activity.
*  Yeah, sure. So so I was I think one of the reasons that I have a relatively unique
*  perspective on AI and neurosciences that my background was really in cognitive
*  psychology. My PhD, we learned a list of words and remembered things.
*  And I have been working for a very long time on a set of equations to describe
*  behavior and recall tasks called the temporal context model.
*  And I got to a point where I just was convinced the equations were just wrong.
*  Right. Like it wasn't working. We were trying to extend it to it was working really
*  well what we designed it for. But I was trying to extend it as a theory of a whole
*  bunch of stuff. And it was just failing in a bunch of different places.
*  And I came into work one day and my postdoc at the time, Kardeck Schenker, was
*  there and I was like, we got to throw this whole thing out.
*  And I realized that all of the problems we were having had a common solution.
*  And the solution was as follows.
*  If if the brain and this is turns out not to be a unique it seemed really new to me,
*  but it was not actually a unique insight that if the brain had access to a
*  representation of the past that was ordered like a timeline, like a musical
*  score, you know, but the present, you know, anchoring one end and then the past
*  trailing behind.
*  And if you could record what happened when as a function over that recent past.
*  And if you could arrange for that function to be compressed in a particular way, if
*  it could be log compressed like Weber Freckner Law, and perhaps we can talk about
*  that later, that you could then make sense of a whole bunch of problems that we were
*  stuck with. Right.
*  But you knew you knew like that you just said that it, you know, it wasn't new.
*  It was new to you. But you knew about the Weber Freckner Law and you knew about
*  logarithmic compression, right.
*  Ideas in psychology and I think even neuroscience at the time, probably.
*  Oh, yeah. Yeah. I was just I just hadn't been thinking about any of those in my day
*  to day work. Right.
*  So there's a there's a thing like, you know, you know, being a working scientist, you
*  have a set of problems you're working on.
*  And, you know, like I didn't need any of those tools to solve the problems I had been
*  working on up to that point. So I hadn't been thinking about them.
*  And so anyway, so I was I came into work and I was like, you know, I was like, this is
*  this is the thing we have is bad.
*  We need this new thing. And I drew a bunch of pictures and I spent a while trying to
*  explain to Kardic what I was trying to get at.
*  You know, and I drew pictures of what I understood the timeline to be.
*  And I said something like, you know, we need to remember the past as a function.
*  And he said, oh, I know how to do that.
*  Laplace transform.
*  And that and so and and so I went, what?
*  And, you know, he explained it nice and slow to me over and over again for like, you
*  know, about an hour. And I went, oh, yeah, that's a great idea.
*  And then, you know, we we worked things out pretty good, mostly Kardic.
*  And and then we spent the next 10 years, me and many other people spent the next 10
*  years sort of evaluating this hypothesis in the brain on we've extended from time to
*  other variables. And it's just been incredibly fruitful.
*  Well, you started with time and we'll go into time more.
*  But was it was it immediately clear that it would that it would extend to other cognitive
*  functions and variables? And I was I was pretty sure about that.
*  Actually, the very first talk, one of the very first talks I went to as a graduate
*  student was Matt Wilson talking about place cells.
*  And at the time I was working on, you know, temporal context model had was basic.
*  The temporal context model basically is using inputs with a leaky integration to add up
*  to make some slowly changing temporal context to remember the past.
*  And, you know, I wasn't a great physics student, but I knew that the first integral of
*  velocity is position.
*  And I knew I was working on an integrator.
*  And so that was one of the first things that occurred to me is that, you know, these
*  place cells in the hippocampus, which are supposed to be important for episodic memory,
*  time and space ought to have some sort of similar basis.
*  So, yeah, I've been all in on that since like first week of graduate school.
*  OK, but yeah, but at the time you were so when Laplace was said, you guys working on
*  memory. We had already actually tried to even in the context of the temporal context
*  model, you know, which ends up having problems.
*  We had taken really seriously that there ought to be some analogy between space and
*  time. We did like a 2005 paper with Mike Haselmo where we described everything that
*  was known kind of about firing of cells in the entorhinal cortex up to 2005.
*  This was also like one year before the Mosers found grid cells.
*  So it became a lot less, you know, comprehensive in like six months.
*  But at the time, it was it was pretty nice.
*  So, yeah, we I've been thinking about time and space is really closely interrelated the
*  whole time. Yeah.
*  You and the data is born us out.
*  Yeah. Yeah. Well, and Randy Gallistole and many other people.
*  Howard Eichambaum and Endel Tolving and, you know, sure, I'm leaving out a bunch of
*  people. Yeah. Well, let's go.
*  I don't know if we're at the right place to do it, but do you want to go over the kind
*  of big idea of what a Laplace transform is and, you know, get into the weeds as much
*  as you need. But and why, you know, this is a good model for representing functions in
*  the brain and specifically for memory at this point.
*  Yeah. Well, so for time here, let's let's talk for a minute about what the Laplace
*  transform is not.
*  And let's talk about time.
*  Let's talk about time cells. I assume your viewer, your listeners don't really know that
*  story. So I don't think I don't think I've ever talked about time cells on the podcast.
*  So this would be a great place to start.
*  So, yeah, let's start. So I suggest that we start with that and then we'll get to
*  Laplace bit. It turns out that Laplace and time cells are really, really closely
*  mathematically related to one another.
*  And we'll get to that. So if something interesting happens, like if I clap, it
*  doesn't leave our experience immediately.
*  It lingers for a little bit.
*  And in rodent experiments and monkey experiments and recently human experiments, we
*  find also that events that happen in time don't immediately disappear.
*  What they do is they create a sort of a sequence of neural states, in particular,
*  there are these cells that are now referred to as time cells that fire sequentially in
*  the time after some triggering event.
*  So that if I as an oh, in different stimuli, if I chirp instead of clap, there's
*  different there's distinguishable sequences that are triggered.
*  So if I'm five seconds after something happened, I have some set of cells that lets me
*  decode that that thing was five seconds in the past and which thing it was and how far
*  in the past it was because there's a sequence, there'll be different cells before,
*  there'll be different cells after.
*  And because different stimuli, different events trigger different sequences, I can
*  tell what happened when in the past.
*  And so those are time cells.
*  We've now seen those in lots and lots and lots of brain regions.
*  We hear meeting lots of people in many different labs in many different species, for
*  sure. Hippocampus, for sure.
*  Medial prefrontal cortex, for sure.
*  Lateral prefrontal cortex for sure.
*  Many different regions in the striatum.
*  It seems like this is a major thing the brain is doing as we go through our lives is
*  remember the recent past.
*  OK, so the question is, how does that come about?
*  The first thing you might think of and the first thing we thought of was that the time
*  cells, because they fire in sequence, perhaps they should chain one to the other in
*  order to build out a sequence.
*  So the time cell for one second should connect to the time cell for two seconds and
*  three seconds and so on.
*  And if you take the equation seriously, it turns out to be really hard to get to get
*  sequences of the right mathematical form.
*  And there's this requirement that in order to get the equations to work, in order to
*  get the behavioral models to work, you need to obey the Weber-Fechner law.
*  You need to have a log scale.
*  And for technical reasons, it turns out to be extremely difficult to get a reasonable
*  neural network to do that, right, just by connecting the neurons one to the other.
*  And so Kardec's argument was that, well, let's not do that.
*  Let's just compute Laplace transform of the function of what happened when and then we
*  could invert it. And so Laplace transform as a neural network is trivially easy.
*  So I've heard you talk about RNNs on this podcast a couple of times, so I presume I
*  can talk about an RNN. As an RNN, Laplace transform is just a diagonal matrix.
*  It is the simplest possible RNN.
*  And basically the numbers on the diagonal control the rate at which things change.
*  You can think of like a little recurrent network.
*  And the idea is that because you have a bunch of different rates corresponding to a bunch
*  of different times, you're sort of tracing out a line that maps on to the what cross
*  when thing that you want, the timeline that you want to come out and that time cells
*  appear to be representing.
*  And in that diagonal form, you have you just choosing the spacing of the time cells,
*  choosing the rate at which the sequence unfolds just amounts to choosing the numbers
*  along the diagonal. And it turns out to be a right way to do that.
*  And so it's an extraordinarily simple RNN that is really, really easy to compute as
*  just a diagonal matrix with some time constants along the diagonal.
*  And then after that, you can attempt to invert the Laplace transform and you get out
*  sequences of time cells or whatever you want.
*  So to generalize from time to space, you just need to have that diagonal matrix and
*  have it modified by velocity of something.
*  And that's like, you know, that's the insight from freshmen,
*  freshmen classical mechanics.
*  Multiply by velocity on the right hand side and you integrate it, you get out position.
*  So you end up with Laplace transform as a function of position or time or any other
*  variable that you can use any other variable you can get access to the time derivative of.
*  All on the same logarithmic scale.
*  Yeah, to the extent you can choose the time constants to be like literally the time
*  constants and the rate constants have to go on in a geometric series.
*  They have to go like one, two, four, eight, sixteen.
*  Not not usually with a factor of two, but you know, it's hard to do the arithmetic in
*  your head. But if you do that, then you're guaranteed that whatever quantity you're
*  representing is first of all, a function.
*  Laplace is a basis set that describes any function over over the line.
*  Right. And then by choosing the rate constants in that way, you're guaranteed that
*  you have sort of a logarithmic compression of that line.
*  And so, yeah, I think this is extraordinarily general.
*  The other thing I want to say about Laplace is we need not go further into the weeds,
*  but I'd encourage people to like actually this is how I learned a lot about Laplace.
*  Go look at the like a Wikipedia page for the Laplace transform.
*  There's a reason people have studied this for years and years.
*  There's just so many computations that are really trivial to that.
*  They're much more straightforward to do in this integral transform domain.
*  So like, you know, you can convolve functions, you can, which is analogous to, you know,
*  adding probability distributions.
*  You can subtract functions.
*  You can translate functions.
*  You can take derivatives of functions by multiplying by s.
*  You can integrate functions by dividing by s.
*  And so you can build up velocity and acceleration and all kinds of cool stuff.
*  So it's a very general purpose transform in which which can be seemingly implemented
*  fairly simply, neurally plausibly.
*  And we're pretty sure is in the noggin at this point, right?
*  Yeah, you guys have we'll get to I get well, maybe we'll talk about it now.
*  I just wanted to put it into context, like in terms of your clap to
*  audio only visualized this right.
*  So like in terms of time cells, right, when you clap,
*  the sequence of time cells would be something like clap, clap, clap, clap, clap, clap,
*  clap on into the past.
*  Yeah, nicely done.
*  Yeah, the sequence slows down.
*  And we can see that really clearly if you if you make a plot of time cells
*  sorted by the time at which they peak.
*  You don't see a straight line.
*  You see this J that's quite characteristic because the sequence slows down
*  because it's on like a log scale.
*  Right. So the difference between one second and two seconds in the past is not
*  the same as the difference between 10 seconds and 11 seconds.
*  It's like the difference between 10 seconds and 20 seconds.
*  And that seems to be a pretty general thing in the noggin and seems to be true
*  of time as well.
*  So like the way that this would map on to neurons is that you'd have a
*  Laplacian transform and each neuron would have a different time constant
*  corresponding to those delays and spreads of the memory, I suppose, back in time.
*  Exactly. Yeah, you'd have you'd have a lot of cells.
*  So like we observe.
*  So we talked about what time cells look like.
*  Laplace transform cells, which which we tried to call temporal context cells.
*  We'll see what catches on.
*  Have been observed thus far in the internal cortex.
*  And in our study, Ian Brighton, Maria Meister were the cofirst authors
*  and my experimental collaborator, Elizabeth Buffalo, is colast author.
*  What we observed is so the monkey is sitting there in a monkey chair
*  and there's a image presented at time zero.
*  And rather than firing sequentially, whole bunches of cells are perturbed
*  more or less immediately, like within 200 milliseconds.
*  But there's there's no variability in the time of their peak disturbance.
*  Right. So they all so if I clap, they all kind of go on and then they turn off.
*  Right. And some of them turn off fast and some of them turn off slow
*  across cells.
*  There's different time constants describing the rate at which they're turning off.
*  They follow a roughly exponential function.
*  And that's like exactly Laplace transform.
*  It's like E minus ST. Right.
*  And so with a variety of values of S and there's an overrepresentation
*  of fast turning off, corresponding to the overrepresentation of fast
*  cells firing time cells firing early in the sequence.
*  And there's fewer and fewer slow ones corresponding to the sequence slowing down.
*  Like you said, clap, clap, clap, clap, clap, clap.
*  I'm sorry, I did it backwards.
*  So what's the what's the advantage of having a log scale in terms of
*  I mean, you know, intuitively, you know, when when you clap, I can kind of hear it
*  in my echo, right, if I kind of pay attention to it and then it kind of fades.
*  Right. But in terms of representing things, what's the advantage of having a log scale?
*  Before I give you my speculation about that, let me note that the noggin pays
*  that does this over and over and over again. Right.
*  So the so if I take if you look at the density of receptors on your retina, right,
*  as I move from the fovea out towards the periphery,
*  the receptors get more and more widely spaced.
*  And it's known for quite some time that there's there's like a logarithmic
*  distribution of receptors to, you know, along the along the retina,
*  photoreceptors along retina. And that that same same compression
*  is respected throughout the early parts of the visual system.
*  Same is true of V1 and V2 and V3.
*  It's called retinotopic coordinates.
*  Right. They look like this bullseye.
*  The same is true of the nonverbal number system.
*  So if you were not allowed to count or you're a monkey or something, right,
*  your estimates of numbers appear to be on a log scale,
*  you know, which is also probably why, you know, we we might fight over ten dollars,
*  you know, at a lunch order, but ten dollars on your purchase of your car is
*  some completely unimportant. Yeah. Yeah.
*  So anyway, so the brain seems to commit to this over and over and over again.
*  So listeners might reach their own conclusions as to why the brain
*  and the mind choose to do this.
*  But there's no question that it does in many, many, many circumstances.
*  So my answer would be consider the possibility that you didn't have
*  a logarithmically compressed scale, that you had you had some
*  particular finite resolution, right?
*  You picked some number and I'm going to say, you know, instead of having the time,
*  you know, on a log scale, you had I'm going to represent time really, really well,
*  you know, out to, you know, some resolution.
*  So if you if the world agreed with you, right, if the world chose
*  something important, evolutionarily important for you to remember
*  that happened to be that scale, you're great. You're you're doing wonderfully.
*  But if the brain if the world chooses a scale that's faster
*  or slower than your choice, right, you're either going to be if it's
*  you're either going to be wasting a bunch of resources
*  that are not providing any useful information or you're going to be completely blind
*  to that quantity. Right.
*  So choosing a log scale is equivalent to
*  in some sense, making an uninformed prior about what you're going to find out
*  in the world. Right.
*  So that if the world gives you something that's important at 10 seconds,
*  well, you can tell the difference between 10 and 11. Right.
*  If it gives you something, you know, that's important at 100 seconds.
*  Well, you can tell the difference between 100 and 110.
*  And if it gives you one, you can tell the difference between one and one point one.
*  Right. If if you chose some particular number in the world, gave you something else,
*  you'd be in a you'd have a big problem one way or the other.
*  So I think it's I think it's adaptive in that sense, given the world statistics
*  and what to expect. We you already mentioned hippocampus and the Mosers
*  and place cells and grid cells.
*  I don't know if we mentioned that time cells and place cells are both found
*  in hippocampus. Right. Indeed.
*  And there's sometimes exactly the same neurons. Right.
*  And the populations overlap. Right. Yeah. Yes.
*  Which is interesting. And that goes back to time and space.
*  But what I was going to ask about.
*  So and I don't know if your original work was in hippocampus,
*  but you've talked about having and of course, the hippocampus is classically
*  important for memory as the you know, has been the age old story for it.
*  But you have found these kinds of Laplace transforms and inverse
*  transform for transforms.
*  Maybe we should just say Laplace functions in lots of different parts
*  of the brains, brain, like you said.
*  What does that imply about?
*  Well, does that mean that there's memory everywhere in the brain?
*  Or are these used in different cognitive functions?
*  And we'll go, you know, we'll go down a little bit more
*  with different cognitive functions.
*  But just to like come a big picture, what does that imply that they seem
*  to be everywhere?
*  You know, it seems like, you know, like grid cells seem to be everywhere.
*  Every new kind of algorithm seems to be everywhere in the brain.
*  So I think I think so we've seen time cells in many, many different brain regions.
*  Thus far, you know, the the the look for the search for Laplace transforms of time
*  is as at a much earlier level.
*  I'm of the belief that we'll find it lots and lots of places.
*  I misspoke. I'm sorry.
*  Yeah, yeah, yeah, indeed.
*  So so I think the reason why there's time
*  everywhere is because there's nothing there's basically no experience
*  we have where time isn't important, right?
*  Time is important in language.
*  Time is important in, you know, classical conditioning.
*  Time is important in playing basketball, right?
*  If you're in the wrong place, you know, being you need to intersect,
*  you know, the the the ball or, you know, a pass or something.
*  You have to not just be in the right spot.
*  You have to be in the right spot at the right time.
*  That's anticipating time.
*  That's that's a future oriented.
*  Oh, yeah, indeed. No, and we're sure we're sure that we have here.
*  So watch this. I did the little clap thought experiments.
*  Let's say you watch this. So I go A. B.
*  A. B.
*  As I say, A again, A sort of recedes into the past
*  and you're able to predict B and B sort of starts.
*  It feels like it sort of starts out a certain distance from you
*  and then gets closer and closer and closer and closer.
*  And in order for in order for us to behave adaptively,
*  we need to be able to anticipate trajectories in time and space.
*  And we've done some experiments, some psychology experiments
*  that seem to show that, you know, memory for the past,
*  our ability to, you know, retrieve information from the recent past
*  has similar properties to our ability to judge the time of future events
*  that are going to come closer to us.
*  But yeah, no, I'm all in on so and oh, and by the way,
*  both of them seem to be log compressed.
*  So if you wanted to be sort of poetical about it,
*  you'd say that there's something like, you know, logarithmic past pointing to the left.
*  The past is always to the left.
*  There's a logarithmic future to the right.
*  And we're sort of like a time phobia in between the past and the future.
*  And that's where we sort of do our business in the present.
*  In the vortex of the present.
*  Yeah. Yeah. If you wanted to be poetical.
*  Let me say it this way.
*  Different types of memory, you know, in memory research, since I was right,
*  since I was a graduate student, people talk about implicit memory.
*  People talked about like episodic memory.
*  People talked about, you know, this semantic memory.
*  And so I'm saying all those different types of memory
*  are using the same form of temporal representation.
*  They're just doing different computations on them.
*  And so and motor memory as well, you know, making spatiotemporal trajectories.
*  So I think I think, yeah, time is built into the time is really, really important
*  in all those different types of computations we might want to do.
*  Well, yeah. So in some sense, this is a unifying principle of memory, which the
*  the recent past has been dividing memory into thinner and thinner slices
*  of different types of memory. Right.
*  And in some and this Laplacian approach unifies those.
*  But I was going to ask this later.
*  I'll just go ahead and ask it now.
*  It seems intuitively appealing on a short time scale in terms of minutes,
*  up to minutes.
*  You know, maybe maybe, you know, tens of minutes,
*  but then episodic memory, right, when I'm remembering childhood events and stuff,
*  this simple just mechanism, it's not like I have a neuron
*  that's just now firing for something that happened to me
*  when I was six years old. Right.
*  So it's not along that S curve.
*  So it must be some different way to access those memories.
*  So how does this relate to episodic memory?
*  Yeah. So following, you know, Tolving, Tolving's definition
*  of episodic memory was that you relive and re-experience
*  a specific moment in time, and that would correspond to something
*  like a recovery of spatio-temporal context.
*  And that was actually, you know, that was the basic assumption
*  of the temporal context model.
*  So if there's a slowly changing temporal context that follows us along
*  and when we remember something, we go, ha ha.
*  Oh, remember when you and I were, you know, messing around
*  with the microphone earlier on?
*  Oh, yes, we both remember that.
*  And people at home, you know, obviously also have episodic memories.
*  Oh, I remember you were on a podcast with Rainey Galson,
*  you were talking about having some celery flavored chili
*  and how you had a really robust episodic memory for that.
*  And so when you relived, it's as if you were there again, right?
*  You might remember, oh, that person was over there
*  and the taste did icky or whatever.
*  And this person was sad or whatever about their chili losing the contest.
*  Wow. You really remember it well.
*  Yeah, it's as if, well, it was recent, right?
*  So if so, it's as if you're re-experiencing the world.
*  OK, so now, as we just said, you know, as I clap or as we move around
*  the world, we have this record of the recent past that tells us something about
*  that gives us something about the feel of, oh, that clap was five seconds ago.
*  And, you know, that that, you know, the place code is saying something like,
*  oh, I'm like, you know, three meters from the wall over there.
*  And so an episodic memory would be something like,
*  let's just pull up that whole collection of things
*  that was available at that one moment in time while you're having the disgusting
*  celery chili, right?
*  It wasn't disgusting, but go ahead.
*  OK, sorry. Yeah, yeah.
*  Just last place. Creative.
*  OK, very helpful.
*  Poor, poor, poor.
*  Her chili was fine. He was very healthy. Yeah.
*  Nice recovery. Nice recovery.
*  So, yeah, so we we we re the idea is that we reinstate
*  that experience that was unique to that set of circumstances
*  and that the time cells and place cells and, you know, whatever else is going on
*  in the hippocampus and elsewhere gets reinstated.
*  And then that spreads out.
*  And it's it's like, oh, we just jump back in time.
*  Oh, we just remembered this thing.
*  So the question is how right?
*  How is it that you manage to cause this state to, you know,
*  come out of nothing from some partial imperfect queue?
*  And that's a really great question.
*  But anyway, that's the basic idea of how to make episodic memory.
*  And that seems to interesting thing we know.
*  So in the laboratory, we measured and actually, this is like kind
*  of the first experiments I did as a PhD student.
*  You know, in the laboratory, we can measure something like this.
*  Jump back in time. If I give you a list of words, right?
*  You remember a particular word from somewhere in the list.
*  Say you remember the let's let's take the items in the list
*  and map them onto the letters of the alphabet.
*  If you've just recalled, you know, letter H, the next thing that comes to your mind
*  is going to tend to be a nearby letter like I, J or K or
*  G. I had to work for it to E.
*  Yeah, yeah, yeah.
*  And so you get this sort of characteristic curve peeking up around the center.
*  OK, so that curve we call the contiguity effect appears to
*  happen over a wide variety of timescales. Right.
*  So if I take the words in the list and I space them out by 10 seconds,
*  I still get the same curve.
*  If instead this is work by from Carl Healy's lab and
*  Nash Unsworth did experiments like this.
*  And so did Jeff Ward.
*  If I take experiences and space them out by larger and larger timescales,
*  right, including up to like hours or days.
*  Jeff Ward did this experiment, like has a push notification on people's phone
*  to give them a word as they go through the day. Right.
*  You still see the same type of contiguity effect.
*  So there's not some characteristic scale of things being close in time.
*  Right. Because you can you can get things that are close in time.
*  For people at home, I'm doing air quotes around.
*  Thank you for that. Yeah.
*  Yeah. Audio visual.
*  So and that you can and so that you see things are close
*  on some relative scale as if there was some sort of logarithmic basis.
*  So the difference between 10 and 11 is kind of like the difference
*  between 100 and 110 or kind of like the difference between a thousand and 1100.
*  And so that that property seems to be respected in episodic memory as well.
*  I think we got it something pretty important.
*  I'm just going to go ahead and ask you this as well, since you brought up
*  Randy Gallistole and celery chili.
*  So I know that you've been influenced by Randy's work on learning and memory.
*  But on that podcast episode, it was all about his ideas about
*  intracellular memory, that, you know, it's it's essentially
*  in principle impossible to store these things over long periods of time
*  within populations of neurons among the activity of populations of neurons.
*  And what you're saying with a population of neurons, all the different time
*  constants, that it is indeed possible.
*  So I'm curious what you think of that
*  orthogonal aspect of Randy's research, that we actually have to store memories
*  more stably in the cell in something like RNA or proteins or something like that.
*  So, yeah, I need to say Randy's like one of my heroes, right?
*  He's, you know, intellectual giant.
*  He's been immensely influential.
*  Actually, when I came into the lab that one day
*  and I wrote a bunch of problems on the board that we couldn't solve,
*  one of the problems was basically Boston and Gallistole 2009.
*  So he's he's been immensely influential to me.
*  And I accept Randy's critique about
*  computation not being solvable at the level of an individual cell
*  or a synapse or even a bunch of synapses.
*  Rather than trying to look for a solution within a cell or within RNA,
*  we've zoomed out and tried to look for a solution
*  at this sort of population level. Right.
*  And actually, I know about
*  I guess it was about like six, seven years ago,
*  I got myself invited to give a talk.
*  Like I called up my friend at Rutgers and I was like, look, I need to talk to Randy.
*  And so please, please invite me to give a talk.
*  And she was very nice.
*  And take note, let me do that.
*  Aspiring scientists, this is how you get it done.
*  Yeah, I invited myself and Randy was incredibly generous with his time.
*  And he kept saying, you know, what's the number?
*  What's the number? What's the number?
*  If you saw the Randy Gallistole, if you listen to the Randy Gallistole podcast,
*  he said that like half a dozen times on the podcast.
*  He said that like two dozen times to me personally, you know, in his office.
*  And I took it really seriously.
*  And the answer is a number.
*  So here's how I would say it.
*  A number is a distributed pattern over Laplace transform.
*  So if I have a number, right, you know, number is so I can take the real line.
*  Number is some point on the real line.
*  I take a point on the real line.
*  Let me map it onto a delta function centered at that.
*  For those of you with very little math, imagine a flat
*  flat function over the real line, except it sticks way up really super sharp
*  at some point, let's call it a.
*  So now I can take Laplace transform of that function.
*  It's just E minus S.A.
*  And now I can compute and I have some other function for B.
*  And I can now sort of compute and add and subtract.
*  And so I can build out data independent operators
*  like the Gallistole and King
*  book, which was also incredibly, incredibly influential
*  on my thinking about the world.
*  And I could write down neural circuits and they might be right
*  and they might be wrong, but I can for sure write them down.
*  There's no there's no, you know, fundamental limit to that.
*  Yes, I need to be able to read and write numbers, right?
*  I need to let I need to let one population of neurons
*  gate into another population of neurons.
*  I need to be able to, you know,
*  implement the expression for, you know, convolution in the Laplace domain.
*  So, yes, there are there are things, but they're not like magic.
*  There's no and then a miracle happens.
*  It's just, you know, so the brain could for sure do that stuff.
*  And whatever I have in Laplace domain, I can then use the I can
*  reuse the same mechanism for inverting it.
*  And I can use the same type of representation for time and space and number.
*  Oh, did I mention how influential, you know, Randy and
*  Gelman's work on numbers has been, you know, in the logarithmic
*  numbers has been on me. So, yeah, so we can reuse the same data
*  independent operators for different types of quantities.
*  And so, yeah, that's my answer.
*  Have you communicated this to him?
*  Yeah, actually, I sent him I wrote this down as best I could
*  in a paper with Mike Haslund, though, that's on archive right now.
*  And I sent it to him and I thought he'd be so excited.
*  I don't know, maybe he maybe he was, but he also said he made
*  I mean, he made a again, genius response.
*  He was like, wow, that was really nice.
*  But, you know, what else would be nice is if I can't believe you didn't,
*  you know, use the and then again, the absolutely genius comment.
*  Why didn't you take the bit about how you can solve differential
*  equations really easily in the Laplace domain to build up like an intuitive physics?
*  And I was like, oh, God, that's another genius idea.
*  So basically, I think like the last 10 years of my life has been trying
*  to catch up with Randy's thinking.
*  And he, you know, he's he's, you know, he's occasionally frustrated.
*  But I think it's mostly because he's like 20 years ahead of the rest of us.
*  Right. So, yeah, one of my heroes.
*  And but no, I don't accept that.
*  I don't think it's essential that we put memory into RNA. All right.
*  I'll pass this along to maybe I'll send that clip to Randy for fun
*  because he would probably enjoy it.
*  So you were talking about a recurrent neural network and how the Laplace is
*  is very simple to implement in a recurrent network.
*  And of course, the brain is highly recurrent.
*  And we talked about turtles all the way down, Laplace, inverse, Laplace, inverse.
*  As as these
*  representations get cycled back onto themselves.
*  Right. I mean, I'm trying to imagine what it means if you have a set of neurons,
*  right, that do a Laplace transform and then there's like a overlapping population
*  inverse Laplace. And this is kind of a canonical computation.
*  Right. But then the signals coming in are then coming in recurrently as well.
*  So what does it mean to continue transforming and inverse transforming?
*  What would those representations be good for?
*  Interesting question. So.
*  OK, so the place where we've had so, first of all, there's no reason to invert
*  most of the time. Right.
*  You can just keep computing in the Laplace domain and then
*  in principle, it's like if we're if we're building a device from scratch,
*  like an AI or something like that, you know, my my advice would be don't invert
*  unless you really need to. Right.
*  In order to answer a specific question, the place where we've found that we need it,
*  we've started doing like deep networks work on this.
*  The place where we've needed to do transform, inverse, transform, inverse
*  is in deep learning frameworks where we're trying to like decode speech.
*  And so we we are meaning mostly not me again.
*  Zorin Teegange and Per Sederberg, my friends and collaborators at Indiana
*  University and University of Virginia and their students.
*  We've been working together on a framework to try and build out
*  like useful deep networks using these ideas.
*  And one of the things we did was to build this deep network that encodes
*  speech, that decodes speech.
*  And so if we stay in the Laplace domain the whole way, it doesn't work.
*  However, if we go into and out of the Laplace domain from one layer to the next,
*  such that basically you've built a deep network of, you know, log time cells
*  going along, it turns out to have this really nice property that the entire network
*  can deal with rescaled speech.
*  What does that map on to like
*  sub syllabic segments and syllables and morphemes and stuff?
*  Yeah, different. So in the model, different layers of the network end up
*  attaching to different types of meaning.
*  Right. It's an open question.
*  There's people who've argued and I'm not an expert in like auditory cortex.
*  There's people as a first author, Rahman,
*  paper in PNAS arguing that there ought to be log distribution of time constants
*  in auditory cortex. As far as I'm aware, they're completely unaware of all this
*  other stuff with time cells and whatnot.
*  OK. And so they've argued that.
*  So there's at least, you know, some reputable people who make that argument
*  in the model, having log scale at every layer of the network
*  ends up letting the model do the following thing.
*  If I've trained on speech such that, you know, we do like auditory MNIST
*  and the, you know, the model's been trained to decode one or four or eight.
*  We can give it arbitrarily.
*  We can give it slowed speech or sped up speech.
*  I can go, said then
*  in the network goes, oh, yeah, that's a seven and it's really slow.
*  Right. And so it turns out, you know, there's only one way to do that,
*  and that's to have log transform log, log compressed time at every
*  at every layer of the network.
*  But yeah, I was thinking of David Popol, who I had on the podcast, and his
*  dual stream hypothesis of speech perception and how he maps it on to,
*  you know, oscillatory oscillations, right, because we no matter how we
*  how hard we try, we speak at three to four syllables per second,
*  I think is what the number is, but I can't remember.
*  So I thought he might be at least interested in this.
*  And I wonder, I don't know if he's aware of this work either.
*  I'll pass it on to him. Yeah.
*  OK, so interesting. But go ahead.
*  Oh, I was just going to say that the artificial networks,
*  we can make them rescale as far as we want. Right.
*  You've done this with convolutional networks because you've already mentioned
*  that you perform convolutions with Laplace.
*  So maybe let's let's go and talk about the artificial work like the Deep
*  Sith and what you're what you were just talking about as an advancement
*  from Deep Sith, I think. Right.
*  But there's a host of models that you guys have built building in these
*  different time constant Laplace layers, right,
*  which which enables networks to deal with time that way compression.
*  Yeah. So let's let's let's back up a little.
*  So Deep Sith is a network
*  that just has log time scales,
*  log time cells, coding what cross when in series
*  with learnable weights in between the networks.
*  So basically what changes from one layer to the next. Right.
*  And so that network does really good.
*  It you can train it on a problem.
*  It has the property that if you train it on a problem at some time scale
*  and then you train it on a different the same problems fed up or slowed down,
*  it doesn't care because it turns out that
*  it turns out that on a log scale, rescaling time amounts to translation.
*  And so there's a couple of times
*  the difference between 10 and 11 is the same as the difference between 100
*  and 110. Yeah.
*  And so that network is perfect, is exactly as able
*  to learn as something, whether it's fast or slow.
*  Sithcon, which is impressed at ICML and it's on archive.
*  People are interested.
*  Actually, we're just working.
*  We're just working on the camera ready version.
*  So nice. I was doing that yesterday.
*  So it so yeah, it has a CNN and then a Max pull over the CNN,
*  because convolution is translation covariant.
*  The Max pull and rescaling is equivalent to translation.
*  Then if we do rescaling the input, it just moves the peak.
*  OK, and if you have a Max pull on the CNN layer,
*  the network is scale invariant and it identifies the correct thing.
*  The location of the peak moves around.
*  It can tell whether it's fast or slow.
*  That information is encoded in the network.
*  But the thing it spits out for the categorization doesn't care
*  whether it's fast or slow.
*  And we can make that we can without retraining weights,
*  we can make the range of scales over which it generalizes as big
*  or as big as we want without any cost in weights.
*  So this seems like like a good idea.
*  And in any event, you know, if you're building robots or whatever
*  to go off to the moon or go off to Mars or, you know,
*  crawl along the seafloor or whatever,
*  and you want them to be able to deal with a bunch of different environments
*  that you can't anticipate, you have a similar problem that,
*  you know, I said the brain is presumably solving by choosing log scale
*  for the retina or the or or or or or.
*  So I think this is pretty
*  pretty beneficial for deep networks.
*  Dealing with different gravitational forces.
*  I've had on, you know, just a host of people
*  who are building in, you know, different kind of kinds of biological
*  details to artificial networks and, you know, kind of smaller scale.
*  But, you know, like neuromodulation, I just had Matthew Larkimann,
*  who works on the dendritic properties of feedback and feedforward connections
*  and using those principles to build in artificial networks.
*  Is this something that you see as just an obvious thing to build into?
*  State of the art, AI.
*  And, you know, you wonder, well, why isn't this being built in?
*  Or or is it more of a less general purpose and more specific purpose?
*  How do you if you had your druthers, would this be incorporated
*  into all the modern deep learning networks, et cetera?
*  Oh, yeah, if I had my druthers, yes.
*  Yes, that would absolutely.
*  I think the reason I think so, I've thought a lot.
*  Actually, the thing that's been keeping me up lately is reinforcement learning.
*  And so reinforcement learning, you know, comes in my understanding,
*  at least it comes from sort of a score, the Wagner sort of models
*  of classical conditioning and the, you know, the classical conditioning results
*  and the dopamine story with, you know, some of the most profound results.
*  And, you know, one of the really serious triumphs of computational
*  cognitive neuroscience that we've had so far.
*  But the theories of reinforcement learning, they're really a temporal right.
*  We had no idea.
*  The whole idea of the Bellman equation is to try and estimate the future
*  without estimating the future.
*  It's to try and estimate expected future reward with just something
*  that's time local and so that, you know, it steps along this.
*  So how would how would that algorithm look like if the goal in, you know,
*  estimating expected future reward included like an estimate of the future?
*  If you could just directly compute that.
*  So, A, you know, there's the future and here it comes.
*  What if we just assumed we have that?
*  So I think I think the I think if I can, you know, speak really broadly,
*  I think contemporary AI and contemporary deep networks and stuff,
*  they're sort of built on, you know, neuroscience that we got mostly
*  from the visual system and mostly through the 80s and 90s.
*  And also the dopamine system, you know, became like a huge deal in like the mid 90s.
*  And I think I think the the the insights that we've had since then
*  have not yet gotten incorporated correctly into A.R.
*  And I think time is one of those things.
*  And I would even go more more broadly and say that representing,
*  you know, the world as functions in continuous space,
*  continuous space, continuous time, continuous number
*  is also something that hasn't really been properly incorporated into contemporary.
*  So, yeah, I think everybody should do this.
*  And if you're listening to this and, you know, I got lots of ideas.
*  It makes a lot of sense, you know, for robotics, obviously,
*  where that where timing is very important.
*  But, yeah, I mean, aside from the like, you know,
*  a recurrent neural network implicitly has time, right,
*  because it has recurrence and sequences and stuff.
*  But time is not explicitly a time representation is not explicitly built in.
*  And the modern transformer has essentially no time because it does everything in parallel.
*  What about what about that?
*  Do you think it would what what effect might it have on transformer networks?
*  Sorry, I'm just shooting from the hip.
*  So, yeah, I actually I mean, we we've
*  this is not yet published.
*  We're pair and Zoran and colleagues are working on
*  transformers that work over scale invariantly compressed memories.
*  Right. And that's work in progress.
*  For me, I think that transformers,
*  I think that transformers, you know, this might be a little mean.
*  They seem sort of like a hack to me, right, that there's something more basic
*  that the noggin ought to be doing and transformers are sort of substituting for that function
*  in some pretty acceptable way that gives them a tremendous advantage over just simple,
*  you know, feed forward networks.
*  But I think there's a deeper thing to what the noggin is doing.
*  One way to one way to look at that, if I were an AI researcher working on transformers,
*  is to celebrate and say, yeah, it's a hack that we don't need to incorporate all your messy brain crap.
*  We just, you know, we found this shortcut that does it just as well or something.
*  I don't know if you have thoughts on that.
*  Well, I mean, I think that looking at RNNs, one might have said the same thing about RNNs, right?
*  So, you know, we can do RNNs and we can eventually learn long term dependencies
*  and we can eventually back propagate through time.
*  We have all these hacks and tricks.
*  But, you know, I just said, you know, this is like an RNN, but it's a diagonal matrix simpler.
*  Right. So in that case, comparing the RNN to plus transform inverse,
*  this is immensely simpler and doesn't have a problem with back propagation through time at all
*  because it's a diagonal matrix with a set of time constants. Right.
*  So in that case, at least this proposed solution is much simpler than the situation we engineered ourselves into.
*  And I have to say, I do think, you know, contemporary AI is astounding.
*  I feel like, you know, they took, you know, I said sort of dismissively, you know,
*  they're building on brain science from, you know, the mid 90s.
*  But they've also engineered that into just amazing devices.
*  Right. If they were starting, so I think the thing I like to think about, like,
*  is if we had sort of more elegant, simpler, brain inspired theory,
*  and then we started engineering on it, like, where would we end up with and how much more efficient,
*  how much more energy efficient would those devices be?
*  How much more flexible would they be? Seven. Right.
*  Like they'd have capabilities that, you know, we can't begin to understand.
*  And right now it's like three people, it's like four people engineering this. Right.
*  So the fact that we got anything that works at all sort of miraculous.
*  So, well, since we're since we're on the subject of AI, I was going to ask about that, the scaling factors.
*  Right. So we talked about how different neurons need to have different, sorry,
*  time constants to scale out this Laplace mushed out memory trace. Right.
*  When in the networks, I haven't done a deep dive on the networks and how they're trained and stuff.
*  We've just been talking about a little bit, but I'm wondering, so you have to like choose the scale,
*  the factors, right, the time constants of the neurons.
*  Well, you choose the once you've committed to there being a log scale, you have two choices remaining.
*  And that is what is the base of the logarithm? Right.
*  So one, two, four, you know, one, two, four, eight, 16 or, you know, one, three, nine, twenty seven. Right.
*  And then you have to choose the shortest scale. What is the what is one?
*  What's the fastest thing you care about? Oh, and that's right.
*  There's a third thing. You then have to choose how many cells you want to what the extent is.
*  Do you want to go from one to one hundred or one to a thousand or one to a million? Right.
*  So when the networks do those numbers get, could you train, could you learn those numbers is the question.
*  But I know that you think that those are sort of hardwired in the brain, right?
*  Those that they're like intrinsic factors. Not necessarily. Oh, OK.
*  I thought I know. Not necessarily. Yeah, we can rescale them.
*  So the nice thing about this whole thing.
*  So going from time to space basically means that you modulate.
*  So you could hear. Let me try and say it this way.
*  So in differential equation for time, there's sort of like an intrinsic, you know,
*  it's sort of like that's being modulated by some number one.
*  Like we can make time go faster or slower just by taking all of the neurons and changing their gain
*  and changing the gain of all of their time constants together.
*  Sorry, changing the gain of all the neurons changes their time constants all together.
*  That's basically how you go from time to space.
*  So we could go from fast time to slow time in the equations, at least we can modulate all of them together online.
*  And if we wanted to do that, is that what happens when we get a shot of adrenaline or, you know,
*  when when our subjective sense of time goes super slow because we're experiencing because everything
*  we're experiencing it at a higher gain, our time constants are all shifted?
*  It could be. That's that's possible. Yeah.
*  Yeah, I've yeah. Time time goes time goes really slow.
*  And yeah, yeah, it could be. Yes.
*  Oh, my God. That means as we get older, our time constants are really going lower, right?
*  Because time goes by so much faster. Oh, totally.
*  Yeah, yeah. Oh, actually, the other thing I would say is we can also build an ordinal code, right?
*  So if we make so we can build a we can build a code that computes, say, like numbered position within a list.
*  So if I let the velocity depend on is something happening or not.
*  So then if nothing happens, time stands still.
*  But then something happens and I advance the clock a little bit and something else happens.
*  I get a log. I get a log ordinal code.
*  So one could also make sense of the time flies when you're having fun by just saying there's lots of things you're paying attention to.
*  And that pushes stuff along extra fast.
*  And if things are really boring, there's nothing to move time along.
*  You know, these are these are all really, really, really important problems.
*  And there's not a solution given by the equations.
*  I think that people I would be ecstatic if lots of people took up these questions within the context of this sort of theoretical framework and ask questions about, you know,
*  is this population neurons in this region or is, you know, is time perception in this task or retrospective timing and, you know, some behavioral experiment?
*  These are all really important questions.
*  The fixing the parameters in a particular region, in a particular task, in a particular setting, none of that is given by this theoretical framework.
*  It's just sort of constrained the set of problems.
*  And so I would love it if lots of people answered these questions.
*  But what I was going to ask about with your deep nets is, you know, if you if you learned the the time constants, right, or the numbers, the three numbers that you need for the time constants,
*  if that was a learned thing, somehow you train the network to learn that number, if it would then you could empirically look in a population of neurons in the brain and see if it's the same distribution,
*  if it learned a brain like distribution of scaling factors.
*  Yeah. The interesting thing from the brain is we have no idea in hippocampus, at least we have basically no idea what the upper limit of that.
*  We have a pretty good idea what the shortest time scale is.
*  Like, it seems like theta oscillation, something on the order of like 100 to 200 milliseconds.
*  The hippocampus doesn't know anything faster than that, basically, in sequences of things that we can observe.
*  And that makes sense, you know, given theta oscillations and phase precession and stuff like that.
*  But the upper limit of the upper limit of how long those sequences go on, we have no idea.
*  So if we do an experiment that lasts a second and a half, we see a nice sequence that goes a second and a half.
*  Someone does an experiment last 10 seconds. Oh, we have a nice sequence that goes 10 seconds.
*  You know, I have a student, you know, there's a paper, I think last year, arguing for three minutes.
*  I have a student, Yue Liu, that me and Mike Hasimo co-mentored, you know, who went and observed something he thinks looks like sequences over 15 minutes, right, in calcium recordings.
*  So we have no idea what the upper limit is. And so we have no empirical constraints.
*  And if this idea of like scale invariant memory, if it's really a log scale, you should push it as far as you can.
*  There's been slice papers in entorhinal cortex. There's a Nature paper in like 2002 that had a big impact on me, where they set the neuron going in a dish and it fires at a steady rate.
*  And then they stimulate it again, you know, in the experimenter Angel Alonso, who sadly passed away a number of years ago.
*  He told me he's like, yeah, you set the thing going and you go have make a sandwich and have lunch and you come back and it's still firing at the same rate.
*  So that cell has a time constant of infinity, right? It's integrating and has a time constant of infinity.
*  There doesn't appear to be a natural upper limit, at least in that experiment.
*  So that's in a dish in a dish.
*  Indeed. Yeah.
*  OK, so I have a couple of guest questions and I just want to make sure that we don't continue because I have my own all my own questions for you, too.
*  So I'm going to go ahead and going back.
*  This is going back to, I guess, human or natural cognition here.
*  You know, this guy named Brad Weibel.
*  Ah, yeah, I know.
*  Brad Weibel super good.
*  Brad Weibel taught me about the hippocampus.
*  Oh, OK. Yeah, I was going to ask how you guys know each other.
*  I knew I knew that you were friends, but I taught you about the hippocampus.
*  Yeah, so I was I was in the I was a cognitive psychologist, mathematical psychologist in the Kahana lab.
*  Brad had been an undergraduate at Brandeis and hung out and I got to know him really well when he was a PhD student with Michael Hasimo.
*  And they did they did a hippocampal inspired model of free recall, which was the thing I was working on.
*  And I would I would bribe Brad because I couldn't figure out, like, you know, all the anatomy stuff.
*  And so I would bribe Brad by like I had I had things he liked and we would socialize with those things.
*  No, actually, it was it was really high end rolling tobacco.
*  Actually, we don't have to go there.
*  Yeah, that's fine. It was legal.
*  It was legal. Legal. We're both waving our hands right now.
*  It's OK. It was OK.
*  It was it was it was perhaps a poor health choice, but legal and relatively wholesome.
*  And, you know, he'd ask me questions about memory research and behavioral stuff with people.
*  And I'd ask him questions about, like, you know, how is the dentate gyrus?
*  You know, what's the HILA region of the dentate gyrus?
*  And what do I need to know about that?
*  We have these long conversations and we ended up being colleagues at Syracuse University for a number of years.
*  And yeah. OK. So what does Brad want to know?
*  Well, first of all, Brad is in Costa Rica right now.
*  And so he couldn't send me an audio recording.
*  So I have to read it in his voice.
*  So anyway, here's his question. Hi, Mark.
*  As you know, I've always really admired the work, your work on implementing Laplacian transforms as a way to encode and compress information in models of human memory.
*  I was wondering if you have any thoughts on what gets lost in the compression as a given memory gets further back in time?
*  Do you envision it as a random selection process or does our memory system refine itself by progressively removing information that seems irrelevant?
*  If the latter, it seems like a big unresolved question is to understand how such a purposeful editing process is driven.
*  Yeah, fantastic question from my brilliant colleague, Brad Weibel.
*  I think the recent work we've done with Deep Sith says something about this.
*  So in that network, each layer has log compression, right?
*  And basically, the learned weights in between the layers preserve things that are going to be important later on.
*  So the phoneme level, let's say, goes away and it's gone.
*  But if there's a phoneme that's important for decoding the word, that gets passed on.
*  And then the word, presumably that is important in categorizing the sentence, one would hope, also gets passed along.
*  And so I think it's not unreasonable to use.
*  I mean, so in the context of deep networks, PyTorch, you minimize some objective function to categorize stuff.
*  And that works pretty good.
*  You could imagine replacing that with something smarter, like informational bottleneck or predictive coding, but in log compressed time.
*  And that's sort of one of the things we've been thinking about.
*  But fantastic question. Good job, Brad Weibel.
*  This is kind of a somewhat related question, and you may have kind of just answered it.
*  You know, I'm trying to imagine. So in your vision of this, like when you clap your hand, right, that's one event.
*  But we live in this continuous, ongoing, dynamic, interacting, ever changing world.
*  So is everything coming in, getting has its own set of neurons?
*  Like, what's the resolution?
*  A, what's the resolution of our sampling, I guess, of quote unquote events?
*  And then a related question is just, you know, how we segment those events, right?
*  Which is what you were just talking about, discussing, really.
*  Yeah, again, if different layers are using the same principle, but have different definitions of what the answer to your question might be radically different from, say, auditory cortex to medial premeditation.
*  So prefrontal cortex, right?
*  And it's unclear and again, problems we should work out how we, to what extent the brain has control over what information gets gated in.
*  And certainly in the case of animal experiments, there's animals don't particularly care about tones or lights, except insofar as they signal something interesting in the future.
*  So there must be some sense in which some of that can be learned and acquired.
*  OK, I'm sorry I have so many questions, but like such a fundamental and potentially canonical function leads me to wonder how it relates to so many other things.
*  So, for example, in the hippocampus, the phenomenon of replay, right?
*  Where a when we're running through a maze or doing something classic things, rats running through a maze and we talked about play cells earlier.
*  I don't even know if time cells are replayed.
*  But anyway, the you know, when a rat has run through a maze and learned it and stuff, then they stop to rest or sleep or eat or something.
*  Then you can record these replay sequences during these ripples, right?
*  And they can be compressed in time.
*  They can be backwards in time.
*  They can be forward in time.
*  How does the Laplace approach map onto the idea of replay?
*  Yeah, I'm all in.
*  I'm sorry, I'm 90 percent all in on the idea that sharp wave ripples are like a signature of that jump back in time thing we were talking about.
*  Like, remember when you were talking to Randy Galles a little about Chile, right?
*  So and that it sort of makes sense in that the reconstructed positions are discontinuous with the current position.
*  And we've actually been working on detailed neural network models where you write down, you assume there's Laplace.
*  That's right. You assume there's log compressed time cells and then you build like a Hebbian matrix amongst them and you let there be attractor dynamics and you build a line attractor.
*  And we get things out that look kind of sort of at least a little bit like sharp wave ripple events.
*  So I think that's my that's my sensible hypothesis for sharp wave ripples.
*  And we don't know.
*  There was a paper from Howard Eichenbaum was an author on it that came out after he tragically passed away reporting something like sharp wave ripples.
*  It's on bio archive, but I don't think it's been widely accepted thus far.
*  I can say with certainty time cells do phase process.
*  There's been recent work from Mike Haslamo and his students showing that quite beautifully, which is either out or should be out quite soon.
*  So what are the functions of replay is memory consolidation, right?
*  What are the proposed functions?
*  And so the complementary learning systems theory posits to learning systems, right?
*  This fast episodic event based learning in the hippocampus, which then gets slowly consolidated and generalized, perhaps in our neocortex, perhaps through partially through these replay sequences.
*  But the Laplacian approach, I don't know why I keep calling it the approach, it's kind of a one function sort of thing, right?
*  So how do you reconcile a complementary learning systems theory with a Laplacian mechanism?
*  Well, so once you get to the part where there is something like jump back in time, right, then the slow system is things that I choose to jump back in time to a lot.
*  And after so like I play this stupid game, it's like math doku, right?
*  And there's some configuration where one time I was thinking about this friend I had in high school while I was doing this one configuration.
*  And so I came back to that and thought of it a bunch of times.
*  Now I have recovered the same episodic memory like five hundred times playing this stupid game.
*  It's certainly become consolidated into my experience of this silly, silly game, right?
*  So the part I'm interested in is how we manage to jump back in time.
*  I think there's really, really important questions about and actually Ken Norman's recent work on this is really gorgeous.
*  And Marcelo Matar, working with Nathaniel does done really nice stuff on this about deciding when it's adaptive to jump back in time and how to go about consolidating.
*  Part of the problem I'm really interested in and actually complementary learning systems has mostly sidestepped this issue is how you manage to recover these really highly temporally auto correlated patterns.
*  So if you recall, like, you know, Hopfield Networks, you know, you can't build point attractors out of really, really similar patterns, right?
*  They're not eigenvectors of the matrix, because if they were, you know, they would be orthogonal and then it would no longer be similar.
*  So this observation that things change really, really, really slowly over a wide range of time scales, which we're just positive of in the hippocampus and prefrontal cortex and Denise Cai's done work and like lots and lots of people have now shown this.
*  You know, that precludes those patterns that you jump back in time to being eigenstates of a Hopfield Network.
*  And so you might do something else.
*  So anyway, we've thought a lot about this and we think there's an answer that may or may not be unique.
*  But anyway, that's the part of that problem I've spent a lot of time thinking about.
*  Once there is that thing, then the question becomes strategically, how do I choose to and hopefully the end of the the me remembering my friend from high school playing the stupid game on my phone is not super adaptive.
*  Hopefully you do something, you know, you know, better to navigate the world.
*  All of my behavior is super adaptive and just I'm just like constantly improving all the time.
*  Excellent.
*  What can the Laplace not do in the brain?
*  Oh, there's no question there's a lot of stuff that has nothing to do with this Laplace.
*  The Laplace transform is a way to represent numbers, right?
*  Anything that and it's a way to represent numbers and functions over a number field.
*  To the extent there's things that are not like that, like olfaction, for instance, doesn't seem at all like that.
*  There's some incredibly complicated space.
*  There's no as far as I'm aware, there's there's no.
*  So anyway, yeah, it's for representing numbers and for thinking.
*  So there's parts of the brain that don't have anything to do with that.
*  Yeah, those yeah, those are the uninteresting parts of the brain.
*  All right. So we were talking about scale free and log scale cognition and neural activity, et cetera earlier.
*  And you gave plenty of examples of that.
*  Of course, I've had Yuri Buzaki on the podcast and he that we didn't talk about his rhythms of the brain book,
*  but he presented a bunch of evidence in terms of oscillations, et cetera, also scale free.
*  And I I almost played this next question at that point, but I've waited and we're kind of going to zoom out.
*  So here's a question from an awesome Patreon supporter.
*  Hi, Mark. This is Howard Gleodowski, a grad student at Tufts University and a big fan of your work.
*  One of my other favorite neuroscientists is Yuri Buzaki.
*  The jacket blurb to his latest book, The Brain from Inside Out states inside of a brain that represents the world,
*  consider that it is initially filled with nonsense patterns, all of which are gibberish until grounded by action based interactions.
*  By matching these nonsense words to the outcomes of action, they acquire meaning.
*  To what extent do you agree with this idea and how does the Laplace model of memory play a role in your thinking about Buzaki's work?
*  Thanks. All right.
*  Hey, Howard. So let me greet Howard Gleodowski.
*  So, yeah, Yuri's been really influential on me.
*  I think the I mean, I to the extent that this Laplace framework approach is really general and moreover,
*  thinking of thinking of cognition as being built out of functions over number fields.
*  There's certainly cases, for instance, the retina, where there doesn't seem to be any acquired meaning to a location on the physical receptor.
*  If we're taking the idea that this sort of log compression is important for audition, there's nothing in the cochlea that is learned.
*  But we know the cochlea takes log frequency.
*  So it's an open question.
*  So I don't feel I think there's undoubtedly a lot of things that are learned,
*  but the sort of ubiquity of this form of compression and the simplicity of the recurrent networks that give rise to it.
*  It's just a diagonal matrix with, you know, it seems conceivable to me that that might be something where many of those parameters are sort of built in.
*  So I think that's how I'd answer that question.
*  Oh, I thought of a good answer. You were asking, where is there a place where there isn't Laplace?
*  And the answer is the visual system. There's no need to compute, you know, so we use Laplace to get inverse for time.
*  We use Laplace to get inverse for numerosity. The receptors in the retina, they're already there.
*  There's no there's no sense in which one would need to take Laplace transform to compute a function over the visual field.
*  Because the architecture is all the architecture is already logarithmic.
*  Yeah, it's built in there. So there's a there's a nice substantive place where there's no definitely no need for Laplace early visual system.
*  All right. Also the teeth, probably in the teeth as well. But that's not quite the brain.
*  I have two more questions here. One, I'm wondering what kind of obstacles you're facing right now.
*  Is it is are there problems that you're working on where there's just something that you just can't get out of the damn way or,
*  you know, that you can't get over the hurdle?
*  I think no, I think the science is going gangbusters.
*  I think there's cultural problems and I think the incentive structure of science is built in such a way that there's,
*  you know, there's a, you know, incentive structure of science is not built for really radical changes quickly.
*  And there's, you know, the the, you know, the idea that psychology has something important to say about neuroscience is really not something a lot of neuroscientists think at all.
*  And certainly, AI people seem even less interested in psychology.
*  So I think there's I think there's really serious cultural obstacles.
*  But for your science, do you need it to be able to change more quickly? Or is that what you were saying?
*  I think if things were if things were able to change more quickly, I mean, there's there's look, if this is really a theory of the brain, right, there's thousands of experiments that need to be done.
*  Yeah, it seems like there's a lot just waiting to be.
*  Yeah. How many RNN papers and LSTM papers have there been?
*  The answer is in the thousands.
*  You know, if seriously the Deep Scyth and, you know, ScythCon, if there are replacements for RNNs and LSTM, somebody should go check on at least some of those thousands of papers written about RNNs and LSTMs.
*  And so there's no way on earth, you know, my lab or Zoran's lab or Pair's lab or all three of our labs put together can ever come close to that scale.
*  So, yeah, if we're going to if we're going to build out a theory of the brain, there needs to be lots and lots and lots and lots of people working on this.
*  And that I don't have control over.
*  But that's a matter of convincing people as well.
*  Right. What I started to think about was, well, how is that going to help you make people push the like button more in social media or something?
*  Because that's where all of the real a lot of money and very fast progress, because there are tons and tons of people working on it.
*  Right. But but in theory of the brain wise, then you need to do some politicizing and convincing.
*  Correct. To I mean, that's not my guess.
*  Yeah, I don't. Apparently, I'm not super great at that.
*  I sucked at it, which is one of the reasons why that was always a frictional point for me in academia.
*  Yeah, I'm hoping I'm hoping the actually that's that's why I've been spending time on the deep network stuff.
*  I think the as a theory of the brain, the deep network stuff is sort of silly, you know, gradient descent and back propagation are sort of silly.
*  But it's a way. But but by showing that these assumptions lead to capabilities that are categorically different than like generic RNNs or generic LSTM,
*  you know, LSTM papers cited like 25000 times.
*  Right. There's literally thousands of people that have been working on that for decades.
*  The fact that this ragtag group of misfits or whatever can do something that is categorically different.
*  I'm hoping gives people an incentive to go dig into this and take this more seriously than they might have otherwise from this ragtag bunch of misfits, giving talks and writing papers no one reads.
*  And and ne'er do wells. You forgot the ne'er do wells.
*  Yeah, yeah, yeah, yeah.
*  Well, Mark, thank you for your time here.
*  And I have so now I have all these traces going back like tons of events.
*  Right. I wonder how many I have.
*  Maybe you could measure that.
*  I appreciate you being here. Thanks for the time.
*  Thank you very much. Bye bye.
*  To get in touch with me, email paul at brandinspired.co.
*  The music you hear is by The New Year.
*  Find them at thenewyear.net.
*  Thank you for your support.
*  See you next time.
*  The past.
*  Take me where I go.

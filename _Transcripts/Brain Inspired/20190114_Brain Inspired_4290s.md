---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 4290s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 22434
Video Rating: None
---

# BI 024 Tim Behrens: Cognitive Maps
**Brain Inspired:** [January 14, 2019](https://www.youtube.com/watch?v=CwKEqu91hOQ)
*  They discovered that these cells were amazing because these different place fields weren't
*  just randomly assigned, but they would fire on this really beautiful, regular grid.
*  I think that the crispest ideas from AI have not been anything to do with neuroscience,
*  but the biggest intellectual leaps in terms of the inspiration often have.
*  This is Brain Inspired.
*  Hey everyone, this is Paul Middlebrooks forging ahead here on the path for us all to understand
*  brain and machine intelligence just a little bit better.
*  Today I bring you Tim Behrens, a professor at the University of Oxford.
*  Tim is a neuroscientist with a background in anatomy, all kinds of decision making.
*  He's worked a lot on techniques to analyze fMRI data, and a lot of his work involves
*  putting people in fMRI scanners while they perform cognitive tasks.
*  And he works on many things higher cognition, including what we talk about today, how objects
*  in our mind form relationships.
*  This concept of forming pathways in our minds among abstract concepts spring forth partly
*  from earlier work on how a host of neuron types in our hippocampus and interrinal cortex
*  might form the basis for spatial maps in our head that we use to navigate the physical
*  world.
*  So, maps among abstract concepts or maps among physical locations, these functions are collectively
*  called cognitive maps.
*  That's a term used as early as the 1940s when Edward Tolman was doing experiments and writing
*  about cognitive maps, what they are, how they're useful, etc.
*  You may recall in earlier episodes, really early on with Blake Porter, or more recently
*  when I interviewed Jeff Hawkins, when we've talked about place cells and grid cells in
*  the interrinal cortex and hippocampus, but today we really hash out that story a bit more.
*  We talk about grid cells and how the neuroscience of spatial navigation came about, and Tim
*  really tells that story.
*  And we talk about how Tim came to think that those same grid cell-like codes could be used
*  for navigating the abstract concepts that we have in our heads.
*  And we touch on the role of bottom-up data-driven neuroscience versus top-down theory-driven
*  neuroscience, which is a theme that we'll return to a week from now when I speak with
*  John Krakauer the next episode.
*  And of course I bring it to AI and how Tim's work might relate to artificial intelligence.
*  There is a lot that we don't get to that he's working on.
*  Like he has recent work on intuitive planning and hippocampal replay in hippocampal neural
*  circuits.
*  So, I'll leave that to you to learn more about.
*  Quote of the show today by Tim out of nowhere, the quote is, there was a tension for the
*  soul of psychology.
*  Now, come on.
*  What other show are you going to hear that just manifest in a conversation?
*  Okay, show notes are at braininspired.co slash podcast slash 24.
*  Please consider supporting the show on Patreon for the tiny amount of two or four dollars
*  per month.
*  You can find the red Patreon button at braininspired.co.
*  Thanks this week to Vivek and Martin, the latest beautiful souls out there, giving to
*  cause and thanks to the rest of you already supporting this podcast.
*  You guys are awesome.
*  You may have noticed I took a brief hiatus because of the chaos of the holidays, but
*  I am back and I have a bunch of guests line up in the next few weeks.
*  So thanks for listening.
*  Thanks for supporting the show.
*  And I hope that your new year is going outrageously well so far.
*  All right.
*  I hope you enjoy and learn something new and fun from my conversation with Tim.
*  Timothy Edward John Barons, thank you for being here and welcome to the show.
*  Thanks very much for having me.
*  It's a fun podcast.
*  So I will have introduced you, sorry, a lot of your background because you've done a lot
*  of varied kinds of work.
*  You're currently a professor of computational neuroscience at the University of Oxford.
*  And as far as I can tell, you were born in the Oxford buildings.
*  Is that right?
*  I've been here a while.
*  I was certainly an undergraduate in the Oxford buildings.
*  So yeah, I've been here since I was 18.
*  But I also have I have a honorary position at University College London and a welcome
*  center there.
*  So I spend about three days of my week in Oxford and about two days of my week at UCL.
*  Okay, good.
*  I do let you leave the building there.
*  That's good.
*  So, you know, like I said, I will have introduced you, but you have kind of a long academic
*  career of studying various kinds of decision making under various modalities.
*  And you've worked a lot with fMRI and techniques to analyze that sluggish signal we call fMRI
*  and lots more.
*  But recently, you have become interested in the structure or relations between concepts
*  in our mind, part of what's called a cognitive map.
*  So today we're going to talk about your recent work in that vein.
*  Somehow I've always been interested in this in something a bit like that.
*  It's not I mean, I think I've always even the works I did in decision making and reinforcement
*  learning, which I see as part of the same thing.
*  I was always interested in how we build models of the world in terms of, so for example,
*  how fast we learn.
*  I made arguments about how you needed models of how fast the models of the temporal dynamics
*  of the world in order to know how fast to learn.
*  And I made arguments about how you need models of the relationships between things in order
*  to know how to make decisions.
*  And so it is true that it's more explicit in my more recent work.
*  But essentially, there are two parts of my work, but it's not really those two.
*  Historically, I've done a lot of work on anatomy and brain connections in a number of species.
*  And that is quite separate from the work on learning and I guess what you might call cognition.
*  But a lot of the work in cognition is really just about how the brain goes about building
*  models of the world and when does it need to.
*  That's somehow what I've always worked on on that side of my work.
*  And the stuff that you're referring to, which is about grid cells, is perhaps the most explicit
*  example of that.
*  Yeah.
*  Yeah, very good.
*  OK, well, we're going to talk about those grid cells and the fallout thereof here.
*  So you recently published this paper called What is a Cognitive Map?
*  Organizing Knowledge for Flexible Behavior, which describes how grid cell-like codes in
*  the frontal cortex might be a mechanism by which we associate and navigate among abstract
*  concepts.
*  We're going to buttress that also with your recent science paper before that in 2016 called
*  Organizing Conceptual Knowledge in Humans with a Grid-like Code.
*  And in that you demonstrate this by having people stretch out and squash up the necks
*  and legs of birds, which is quite a cruel experiment, my friend.
*  You really have a macabre streak in you, don't you?
*  I don't know.
*  I think that maybe it was my friend and colleague, Jill O'Reilly, and together with our PhD
*  student, Alexa Constantinescu, who came up with the particularity of the bird torturing.
*  Of hate-espised birds, yes.
*  But it is, yeah, I mean, it was just once you're looking for two abstract dimensions,
*  we thought we might as well choose fun ones.
*  OK, good.
*  And who knows?
*  And to it, we may touch on your latest work, some of your latest work, on intuitive planning,
*  which is one way that all of this could work as well.
*  Yeah, yeah, and there's also, I can, we've also got some stuff in review about replay,
*  which is fun.
*  Oh, cool.
*  OK.
*  Well, so there's a lot we could talk about, obviously, but so let's start in the 1940s,
*  which is a great place to always start, right?
*  Let's start with Edward Tolman.
*  Maybe you could just describe the origins of the term cognitive map and the concept of
*  a cognitive map.
*  Yeah, so there was a tension for the soul of psychology that lasted from the, yeah,
*  I mean, I guess through Pavlov and Thorndike and Skinner on one arm of the game against
*  people who thought that there was more to life and intelligence than reinforcement.
*  So it's the behaviorists against the rest.
*  Yeah, the cognitivists.
*  I guess you want to call it that.
*  And I guess Tolman was the most prominent or early one of these cognitivists.
*  And so he was trying to counter the argument that everything was done through reinforcement.
*  And he did so with a beautiful set of experiments showing that animals had detailed knowledge
*  of the of what you might call a map.
*  So of the relationship between places in a maze, for example.
*  And so there would be the ones that make it so that make it most obvious, I think, are
*  experiments like if you let an animal run around a maze for a long time before, before
*  ever putting a reward in the maze, then the moment you put that reward in the maze, they're
*  much, much, much faster to return to that reward than than if you put them naively in
*  that maze for the first time with the reward.
*  And so they learned something about the maze before there was any reward in there.
*  They learned implicitly about all the relationships between it.
*  They don't have to navigate the maze before there was any rewards in the maze.
*  Just just in that exploration.
*  And they would apparently they would learn shortcuts in the mazes as well.
*  So they would learn to take short.
*  So they would take shortcuts.
*  So you so there were like classic classic experiments with shortcuts and blocking arms.
*  So for like you can allow an animal to run around a maze and then you can put a reward
*  at one place and then start them at another place again and again and again.
*  So they become really reinforced on that particular activity of going from place A to place B.
*  And then you think, OK, that's what they're learning.
*  They're learning by reinforcement how to get from place A to place B.
*  But then if you block that route, then told me to show that they had no problem in finding
*  some new route that had never been reinforced.
*  Oh, I see. Yeah, exactly.
*  Or equivalently, if you train them on the long route and then open up a new shortcut,
*  open up an arm that they've never that they've never been reinforced on.
*  Obviously, they've experienced it beforehand when before the reinforce was there.
*  But if you then just open that arm up, then they will be able to take that and go find their award.
*  They know the map, the plan of how things relate to each other and how different routes
*  lead to the same thing.
*  And they're able to use that information in determining their behavior, even when those
*  particular relations have never been reinforced.
*  And he and Tolman obviously was playing with spatial experiments in rodents.
*  But he definitely believed that this idea of cognitive map would generalize to explain
*  an awful lot of our cognition.
*  That's what he believed across domains of social neuroscience, across domains,
*  across, yeah, across abstract thoughts.
*  He certainly wasn't making arguments just about space.
*  Yeah, right. So, I mean, the experiments were definitely about space.
*  But I guess he had a larger picture in mind, like you said, which he called the cognitive
*  a cognitive map, which is understanding all the relations relationships between having
*  a model of how different things relate to each other in your world and being able to
*  use that model to find effectively shortcuts in abstract spaces, understand the relation.
*  I mean, the things that are if you're trying to define why cognitive map is useful to you,
*  for me, the two biggest ones are these ideas of shortcuts.
*  So if you if you discover something after a long, tortuous set of actions, if you
*  understand something about those actions, you may be able to realize there was a quicker
*  way to achieve your goal, which isn't something that you.
*  So it's like a shortcut in abstract space.
*  Or the other thing you can do is if you've got a cognitive map and you know the relationship
*  between all the things in the world is you can do you can make rich inferences from from
*  very little data. You can understand that if something happens to to one thing, it might
*  have big consequences on some other part of the cognitive map because you know the
*  relationships in the cognitive map.
*  And I gave a bunch of examples of that in in that paper that you described.
*  OK, so thanks for the description for what a cognitive map is.
*  However, fast forward in time and the experiments were originally done in spatial
*  navigation settings and along come place cells and grid cells and the hippocampal zoo, as
*  it's called, all these different cells that contribute to spatial navigation.
*  So we've talked about that a little bit on the show, but it'd be nice to sort of
*  unravel it and just talk about the story of grid cells and spatial navigation to set
*  up the transition to what what you're doing these days.
*  So so maybe we can just trace the story of grid cells in the 2D spatial navigation plane.
*  Well, you start with place cells, I guess, with John Keith, Nadel and Keith in the 70s,
*  making arguments about what hippocampal cells were doing.
*  And they found hippocampal cells had these really beautiful
*  spatial response fields, so they would fire.
*  So your listeners should imagine a rat running around.
*  But now instead of a maze, he's running around in a square arena about about a meter by a meter.
*  And that's three feet, folks, three feet for my English listening, my Americans.
*  Sorry for your American.
*  Yeah. Europeans understand meters.
*  We should. But yeah.
*  Yeah. And so then these cells in the hippocampus would fire at very particular points in these in this arena.
*  So it might fire 20 centimeters away from the left wall and 30 away from the from the bottom wall of this arena.
*  And then it obviously have a field.
*  So that would be where its peak was.
*  And it would fire less and less around there, but it would only fire in a very circumscribed part of this arena.
*  And there were these and then there was a huge argument in the 70s about whether they were really coding place or what were they coding?
*  And to some extent, that's still an interesting argument.
*  But Keith managed to convince people that, for example, that wasn't caused by the fact that it smelled different there or the fact that it
*  or the fact that they were looking at a different thing in that place than the other place.
*  Some of the key features of these cells, they're very impressive.
*  They generalized over which direction the rodent is looking on and they generalize over how fast he's running and those kinds of things.
*  It's unlikely to be a sensory or a motor thing that's causing those things.
*  And Keith made these arguments about the 70s and called it a basis for a cognitive map.
*  And it was easy to imagine why it was called a map because it was really spatial.
*  Yeah. It's interesting also to note that Edwin Rolls at the same time was recording in Monkey hippocampus and he was
*  recording some, or maybe a little bit later, but not much, was recording things that didn't look spatial.
*  Right. So and he and these monkeys were hanging out in cages and walking around space.
*  And the cells there did not seem to care particularly where the monkey was, but cared an awful lot more, for example, about what the monkey was looking at
*  or the gaze direction or where it was attending and those kinds of things.
*  And so that already raises the possibility that in an animal that can move its focus of attention to somewhere else, because a rodent is probably at least when it's running along, the most important thing in that rodent's life is where it is.
*  But a monkey sitting up a tree with his excellent vision can be going, oh, there's an apple over there.
*  So it's already interesting to know that it might not be just about where you are, but rather what's important in terms of it.
*  It's an interesting representation of maybe what's relevant to you right now.
*  Whereas, and in a rodent, what's relevant to him right now might be just where he is.
*  Yeah, I mean, it's also maybe this is a time to note that the hippocampal structure, including the hippocampus and interrenal cortex, it's often noted that they're not close to sensory areas.
*  Right. So they're kind of deep in the pathway of of your cortical brain.
*  Right. So it would make sense if these what's being encoded there are a bit more could be a bit more abstract than just where you are, for instance, and could code for such things.
*  Well, there's two things, several things to say about that. Where you are is a very abstract thing.
*  Sure. It's really difficult to get.
*  Imagine all of what you have to do to get something from your retina, a code from your retina, some light from retina, which is a changes depending on the lighting conditions or depending on the the particular head direction that you're looking in.
*  So and there's also egocentric, right? Depends entirely on your visual code depends on where you're looking in terms of your own body orientation, not in terms of the coordinates of the coordinate frame of the of the arena.
*  Right.
*  Changing that into a what we call an allocentric code, which is a code which on an XY plane where you actually are, this is an extraordinarily abstract.
*  I mean, I think that the this word abstract, the reason you're calling it not abstract is because it's so easy for you to know what it is.
*  But I think the computations to get to allocentric position from the retina and the movement of your legs are far from trivial.
*  No, I'm not. I'm not denigrating the computational feats of doing that.
*  I'm just saying that the point has been made before that that that type of machinery could be used for other processes as well, which is actually what a bit about what you know what you do.
*  Talk about.
*  Yeah, the I think the other thing to say about the hippocampus is that despite this, there's been a big focus on space in the Roman hippocampus community, which has been which is famous and has been made particularly famous by the Nobel Prize being awarded to it.
*  Right.
*  But it's also true that the hippocampus is notorious for being important for memory and memory doesn't have to be about space.
*  I mean, who knows whether it will or not, but there's no question that someone should have given Brendan Milner a Nobel Prize for that discovery.
*  Right.
*  And it is just to be clear, we should we should say you're talking about patient HM and other studies about episodic memory and the memory deficits associated with lesions and hippocampal structures.
*  And Alzheimer's disease, I mean, Alzheimer's disease affects makes it difficult to find your keys if you got some disease, but so if you lost your car keys, you probably won't know where they are in space, but it affects an awful lot of other things about your memory as well.
*  Or episodic memory.
*  And certainly the most noticeable thing for somebody with a hippocampal lesion is nothing to do with space.
*  The most noticeable thing is to do with much more abstract memory for much more abstract,
*  cognitive things like just the memory of having met Brendan Milner yesterday was the most noticeable thing.
*  HM deficit.
*  So whilst all these amazing things have happened in space in terms of your own representation, nobody was ever kidded that the hippocampus was really all about space.
*  You know, well, I was going to say I heard Edvard Moser, I think, talking about the current conception and consensus or almost consensus about the hippocampal formation complex.
*  That it does encode spatial navigation, but with things like episodic memory on top of it.
*  Right. So that's one view.
*  So let's let's argue that the hippocampus is a memory system.
*  Then then you have to start figuring out what a memory is and or what an experience is.
*  And there's no question that space and time, which are often found in hippocampal representations, are two really important components of memory.
*  There's no question that those two things are really important components of memory.
*  You remember where you are and roughly what was happening around then.
*  But there are loads of other really important components of memory.
*  And you might argue that the space and time are a fundamental framework upon which other things are built.
*  Or you might argue that two components of memory, I don't think there's any hard evidence to separate out those two arguments right now.
*  OK, well, we could go off the rails here with just the hippocampus, which would be fun.
*  Anyway, yeah. But so getting back to the actual spatial navigation story that Rob, yeah, sorry.
*  Yeah. So you have these place cells, which, you know, and then O'Keefe writes this book called Hippocampus as a Cognitive Map, right.
*  After this, all this place cell work and then what, 30 years later, it took 30 years for six.
*  Yeah. Yeah. Yeah. For Maybritt Moser and Edvard Moser and their colleagues to record what are called grid cells in entorhinal cortex.
*  And I know it wasn't that straightforward, but maybe you can kind of talk about grid cells now.
*  Sure. So these are another amazing discovery. So entorhinal cortex is the input from to hippocampus.
*  Major input, right?
*  Yeah, it's the it's the major input.
*  If you look in the if you look in the textbooks, it's the only cortical input into hippocampus, I think.
*  But in those textbooks, that's no longer thought to be quite true.
*  But it's certainly by far the dominant input into hippocampus.
*  Yeah. And so they, Edvard, the Mosers, Edvard and Maybritt were interested in how you could make such a thing as a place cell.
*  They were interested in these complicated computations that I was referring to before.
*  How do you get something that starts off in in in your retinal space and build something that ends up being an allocentric place cell?
*  Right. Well, because there was this sort of not controversy, but it was unknown whether place cells on their own could encode the spatial navigation or whether they are the downstream cells of other computations.
*  So, yeah, I think maybe that's right.
*  Maybe people thought that at the time, I think that now people would definitely say that.
*  But I mean, I think that really, Edvard and Maybritt were just really interested in how that how you could get something as abstract as an allocentric place cell from.
*  And so they thought the thing to do would be to go and record in the in the structure that's one synapse upstream from from the hippocampus.
*  And so they went and recorded the entorhinal cortex and they recorded lots of.
*  Lots of interesting patterns there that seemed odd in that they would have more than one field.
*  They would be like place cells, but they would have more than one field.
*  And then and this it's all seemed a bit confusing until they made their arena bigger.
*  And I and when they made the arena bigger, they discovered that these cells were amazing because these different place fields weren't just randomly assigned,
*  but they would fire on this really beautiful, regular grid.
*  And this grid is a is like a triangular lattice.
*  And so it's like if you can imagine equilateral triangles all stacked next to each other.
*  And if you put stack enough of them around a central thing, you get a hexagon.
*  Yeah. And so this triangular or hexagonal lattice was beautifully recopetriated in the firing fields of these of these cells, which were clearly clearly coding place, but they were coding multiple places.
*  And those multiple places would lie on this beautiful triangular lattice.
*  So just just to be crystal clear, the rat would start at one place.
*  It would run about, let's say, let's say half a meter right in one direction.
*  And and the cell would fire and it could run half a meter back to where it was before.
*  And another that cell would fire again.
*  And then they could run equilateral triangles all over the field.
*  And that same cell would fire over and over.
*  Yeah. Yeah, exactly.
*  And so in the where they were recording to start with, so these cells would have a period of maybe 30 centimeters.
*  So if you're in an 80 centimeter arena, which they were, then you may get two or three of these things, these place fills and you can't quite see where they are.
*  But if you make the arena a meter and a half, then you're going to get lots of these fields.
*  And then you start to see what it looks like.
*  And it actually turns out that if if you just move the electrodes more dorsal to somewhere to somewhere a little bit further up the entorhombocortex, now the field size reduces and so that the field spacing reduces.
*  And so now there are ones that maybe have 15 centimeter period or something like that.
*  And then they are really, really tiling it in this wonderfully beautiful triangular grid.
*  So it's maps at multiple scales.
*  Yeah. Great.
*  And they call these grid cells.
*  They call them grid cells.
*  Yeah. Yeah, exactly.
*  And so there's the reason they thought that was interesting.
*  I mean, I mean, apart from being interesting because of its beauty.
*  Right. It's very rare you see something that beautiful when looking at neurons.
*  Those neurons have interesting mathematical properties, but they also because they found this regularly spaced grid.
*  The first thing that Moses thought, I think, when they saw these cells was that they would give it they would allow you to compute a metric for space so that you knew how far that you'd run in any one direction.
*  And if you know how far you've run, then that's obviously an important component to knowing where you are.
*  And then that is an important building block for a place.
*  Yeah. OK. So so then you have place cells and you have grid cells and what's called the hippocampal zoo.
*  There is all sorts of cells in their direction cells, social place cells, border cells, object vector cells, reward cells, goal direction cells.
*  I'm sure there are more than I'm missing.
*  But so this work culminated in the 2014 Nobel Prize, which was shared among John O'Keefe and May Britt Moser and Edvard Moser.
*  So that's that's kind of the story of the discovery of spatial navigation in the hippocampus.
*  And there's actually still lots to learn in that vein as well.
*  So how grid cells accomplish that?
*  There's not there's not a totally satisfactory model yet.
*  The book's not closed on it.
*  Although many have been proposed, right?
*  I would like to go I'd like to go much, much further than what you're saying now.
*  I'd say we have we know very little about spatial navigation.
*  Yeah, I hate that every time.
*  Any time we talk about what we know about in the brain, it's always very, very little.
*  We know an awful lot about how how you might navigate an open one meter in.
*  But but that's not what rodents do in the world.
*  They build I mean, they build extraordinary, complicated spatial burrows.
*  They they three dimensional navigate.
*  Yeah, yeah.
*  They can navigate around all sorts of
*  vast, complicated maps and really,
*  really, we have little idea how that works, how you could effectively
*  control your behavior in those worlds, which are not open one meter environments is
*  the subject of as much mystery as abstract representations are, I think.
*  You know, this is maybe we can talk chat about this for a second right now.
*  A lot of people I've had on my podcast and and it just seems
*  recently in the world of models that there's this really big push
*  to come at neuroscience with theoretical claims and then test them experimentally.
*  And we you know, we don't know anything about the brain.
*  We got to come with theory first.
*  And this is one one instance.
*  And correct me if I'm wrong, where the it was more experimental ground up, right?
*  From the beginning, like the the the discovery of the place cells
*  and then the searching for the grid cell.
*  So there's theory coming in, but it didn't start with theory.
*  And so this the siren call right now with deep learning, especially to look
*  for the algorithms and then try to figure out how it works in the brain.
*  This is one minor victory, I suppose, for the lowly experimentalist
*  searching for things. Do you think that that there's any merit to that?
*  Yeah, yeah. I always think there's anything we've ever discovered
*  that started with theory, is that right?
*  I mean, I think that most things start with some data and then you need some theory
*  to explain that data, to explain what will be interesting to look for next.
*  And then you need some more data to see if that theory was right.
*  And then you it's like a cycle.
*  But the start of that cycle is data.
*  Well, we are data. We have to be.
*  We are the data. We have to be the start, I suppose.
*  But you're right that the hippocampus is an extreme example of that
*  because the data seems so intuitively understandable without without the theory.
*  Of theory. And it's also so beautifully structured without the theory.
*  I mean, I think there is a huge amount of theory.
*  I mean, I I do theory.
*  I mean, I think there's a huge amount that theory
*  can add to that hippocampal story.
*  And we're trying to do so.
*  But place cells came before theory grid cells came before theory.
*  Actually, theory then predicted
*  the existence of these things, these boundary and boundaries
*  vector cells before they were seen.
*  That was my friend Neil Burgess predicted they would be there from
*  a beautiful couple of theoretical papers.
*  But the other thing that has been so beautiful
*  in the hippocampal field is this this phenomenon called hippocampal replay,
*  which happens in the shortwave ripples where where
*  which is like you can watch the hippocampus dreaming basically.
*  You can watch it.
*  You can watch what the animals think about.
*  There's a huge amount of structure in that data, which is just stunning.
*  And that has come before any theory.
*  People are just starting to think about theories of replay now.
*  Yeah. And so it's like being one thing after another, which is
*  which has been pleasant surprises from the hippocampus.
*  Yeah, I guess I guess even before that,
*  H.M. was a pleasant surprise for hippocampal people, if not for himself.
*  Right. Yeah, there was no theory for Phineas Gage either, I suppose.
*  All these patients.
*  Well, OK, so I mean, I just I mean, it's just it just must be right.
*  So like it's true in I mean, I don't know, in V1 as well.
*  So who would have these all came before there was any theory
*  to explain why the global filters are there.
*  I mean, now we now there are 10, 15 different theories
*  for why you have those global filters.
*  But like the people who are developing these theories,
*  there's so many possible theories that people that you need something
*  you need to when when our Huffington Fields were looking at sparse coding
*  and visual cortex, if those sparse codes hadn't predicted the global filters,
*  they wouldn't have known whether they were on the right track or not.
*  Same thing with round ballad when they were looking at predictive coding.
*  And now the people who are looking at conv nets to do those same things
*  have a have a similar game in the in the later visual court sees
*  or Doris South people people work on the face patches
*  trying to understand them with these PCA like codes.
*  Those things.
*  There's just no point starting with that with that theory until
*  until the data is there.
*  If you're looking at it, if you're talking about theories
*  of representation, I think that's what you're talking about.
*  Well, and who would have thought?
*  I mean, so a triangle is a beautiful geometric shape, right?
*  But how would anyone have predicted that grid cells would be laid out
*  in these hexagonal structures without actually finding it?
*  You know, because they could be laid out in any structure or or.
*  Well, they could. That happens to be the mathematics.
*  So you could if you if somebody had said
*  what is the most efficient way to index
*  memories, to build and to build an index for memories,
*  which gives a metric structure for space, then maybe a mathematician
*  would come back and say grid cells. Right.
*  But nobody knew that were going to be cells there that were building this metric.
*  This this metric for the spatial for the spatial play cells.
*  Yeah, exactly.
*  So hexagon seem to be special then in a mathematical sense.
*  I mean, are they do we see hexagonal structure
*  throughout the animal kingdom?
*  Is this a common motif in all animals?
*  Do we do we know how prevalent hexagon hexagonal structures are?
*  Brain computations.
*  We know that that's the most efficient way of packing space into dimensions.
*  So if you want to place Gaussian place fields
*  that are going to inhibit each other,
*  so which is basically what all the models of the attractor
*  models of grid cells look like.
*  If you want to place a bunch of Gaussian
*  place fields that will inhibit each other on a 2D plane,
*  then then they'll naturally come out hexagonal
*  because that's the most efficient way of then packing together.
*  Yeah, if you want to pack apples in a crate, you do so with hexagonal packing.
*  It's the most efficient way to pack spheres or Gaussians, that kind of thing.
*  Yeah, so it's the most efficient way to place spheres.
*  It's most efficient way to pack place fields.
*  And so I guess the early people that saw it saw them and said,
*  Oh, yeah, of course, that's the most efficient way to pack place fields.
*  And in hindsight, it was obvious, but I bet there was nobody
*  thinking about it in foresight.
*  So before you before you were stretching and squashing bird necks and legs,
*  people were put into an FMRI scanner and
*  asked to navigate in virtual reality worlds.
*  That's definitely true.
*  That was that work was often done by Neil Burgess and colleagues.
*  Yeah. And so what would happen is this hexagonal structure would be
*  recapitulated, would be found in the FMRI data and in hippocampal structures.
*  And I guess they found did they find it in prefrontal cortical
*  structures as well at the time?
*  Yeah. Yeah. So they found it in
*  the middle frontal cortex, middle parietal cortex and entorhinal cortex.
*  Yeah. So that was amazing to be able to see grid cell activity.
*  There's an interesting trick that I didn't mention before,
*  which lets you see it with FMRI, which is that all of those triangular
*  lattices are aligned with each other in terms of in terms of the sort of
*  if you can imagine a triangle, it has some angle to the edge of the arena.
*  That's called the grid angle.
*  And those grid angles are basically shared amongst all the grid cells.
*  And so it turns out that if you run along that grid angle or any
*  any direction, that's a that's a multiple of 60 degrees away from that grid
*  angle, so 60 degrees is the angle that defines the quadrilateral triangle.
*  If you're running along any of those directions, there's more activity
*  than there is if you're running at one of the intermediary directions
*  that isn't 60 degrees away from the grid angle.
*  And so you had you got this signal called this hexa directional signal.
*  So which go which which is big along any of the grid angles,
*  but small in between the grid angles.
*  And so that was found by Christian Deller and Neil and Neil Burges
*  in the 2010 major paper.
*  And they showed that was true entorhinal cortex, but also in middle frontal
*  and middle parietal, which suggests something pretty incredible,
*  which is that these grid cells might be not just entorhinal cortex in humans,
*  but but also in much broader parts of frontal and parietal cortices.
*  It's those cortices actually are strongly part of the hippocampal network
*  as well as entorhinal cortex is a big output regions of of of hippocampus.
*  And then there is one sign that's away from hippocampus
*  in terms of the input, one extra sign that's not like so.
*  So they've got big inputs to entorhinal and big inputs to
*  nucleus reunions, which allows them to communicate with
*  with hippocampus very, very closely.
*  And so they often oscillate in phase with with hippocampus
*  in like Western State FMRI, for example, or if you put a electrode in both places.
*  I don't know if that's interesting or not.
*  But anyway, the what is interesting is that this FMRI signal,
*  which seems indirect to people used to recording cells,
*  had made a prediction that in humans, at least you would find grid like activity
*  in these regions that were not entorhinal cortex.
*  And that turned out to be true.
*  So Josh Jacobs and it's like free were doing these experiments,
*  very similar experiments in patients, epileptic patients who have
*  electrodes in middle frontal cortex, middle parietal cortex
*  and entorhinal cortex and found grid cells in in all of those places,
*  which is kind of awesome, right?
*  So it's kind of awesome when something as indirect as FMRI
*  is making a prediction about what the representation is going to be.
*  Right, right. OK, so then I'm not sure if this is what really spurred you
*  into thinking about pursuing this with with the bird experiment.
*  So but so why would we think that spatial navigation
*  would generalize to concept navigation before we were about to talk about your
*  your bird experiment?
*  And then we'll get into more broadly concepts of a cognitive map.
*  But is it just the mathematical beauty
*  and efficiency of the hexagonal kind of code that we think, well,
*  this must just generalize the spatial kind of patterning must generalize
*  to to abstract concepts as well?
*  No, I think that there's an awful lot of power in thinking about
*  generalizations and analogies.
*  And I think that in in general, it is true that where they are available,
*  our brain is extraordinarily powerful at taking advantage of them,
*  much more so than any artificial intelligence that's been invented yet.
*  And so it wasn't surprising to me that.
*  So it seemed like it was possible that it would happen.
*  But that's not why I did this study.
*  I did the study because because there were grid cells in those brain regions
*  that there are the brain regions that are that are important in.
*  So those brain regions that are not the entorhinal cortex,
*  where there were grid cells, those brain regions are important
*  for building these abstract models of the world in general.
*  When you look for studies of things like acquired equivalence, right,
*  in rodents, where do things become related to each other?
*  Because similar because like if a predicts reward and be
*  some reward and be predicts some reward, but see, put it some different reward,
*  then it then the representations of A and B will become more similar
*  in in medial frontal cortex.
*  They've acquired this equivalence between them.
*  So they are understanding the relationships between
*  these different stimuli because they both predict the same thing, for example.
*  So that's in really basic rodent studies, but also in
*  in human studies, whenever you do these types of decision making studies,
*  which require things that are more simple than just repeating reward,
*  that are much more sort of Tolman like in their structure.
*  It's those brain regions that seem to be the ones that are most important
*  for making those decisions.
*  So and I was studying value and I was studying how you can
*  the roles of those brain regions, the computational roles of those brain regions
*  in in decision making.
*  At the time, a lot of people were interested in their roles of
*  of computing values from those those those world structures.
*  But nobody knew what the representations of those world structures was.
*  And it seemed to me to be really important to know that.
*  And so I had a bunch of studies trying to get at that in different ways.
*  And so I studied strange things like how you could
*  represent or predict what it would be like to to eat
*  tea jelly if you knew what it was like to eat tea and jelly.
*  You knew how do you combine these things together?
*  What does the neural representation look like?
*  So I I didn't that kind of study.
*  And so I was really at the time extremely interested
*  in how those brain regions were representing the world
*  so that you could make decisions about them and use them to control your behavior.
*  And then I saw that there were grid cells in those regions.
*  And I just thought, well, fuck me, if there are grid cells in those regions,
*  and those are the regions that are that are representing these abstract world models.
*  Let's see if those same cells are representing abstract world models
*  as are as are representing spatial world models.
*  And so often you often I'll stop talking a second,
*  but I think there's something interesting there.
*  For me, this has happened before.
*  But often people often computational people are very dismissive
*  of the idea that knowing where something happens is important.
*  But it is.
*  I mean, like the brain is locally localized.
*  And so for me, the only reason why I was able to make
*  what might be some kind of conception site to how something happens
*  because I saw that two different things happen in the same place in the brain.
*  Yeah, I've forgotten you started your career off in phrenology.
*  So that was the thing.
*  But you mentioned.
*  I mean, yeah, it is it is it is so easily dismissed.
*  But people, I mean, people forget how like the people
*  forget all the early experiments by Lashley, where he just thought
*  the brain was a soup and started cutting bits out randomly.
*  But there is something important about where something happens in the brain
*  as well as what happens. Yeah.
*  You mentioned that the brain, if if there's a useful way to do things,
*  the brain will use it right.
*  So there's a few people, some people like Rudolpho Genas,
*  who wrote I have the vortex, people like Daniel Walpert,
*  who you can look up as Ted Talks and stuff.
*  And other people have talked about how.
*  Or have have suggested that evolutionarily,
*  movement is the central function function of the brain
*  and that through evolution,
*  movement processing has has internalized and become thoughts, essentially.
*  Right. And in that sense, thoughts are a form of movement.
*  And so this kind of if there was a spatial navigation,
*  evolutionarily to begin with, if there's merit to this idea,
*  you know, and that's coded in the hippocampus and then things become layered
*  or wherever it's coded and then things become become internalized
*  and layered in that sense, it makes a lot of sense evolutionarily
*  to use the same code in other parts of the brain and for other cognitive processes.
*  I don't know if you have thoughts about that, but maybe I mean, yeah.
*  So that might be right.
*  Or it might be that we have.
*  Yeah. So there are there are like I don't even I mean,
*  I don't know the answer to this question.
*  It's a philosophy as much as it is science. Right.
*  And I'm not very good at philosophy.
*  But the we don't even know if it's the same cells. Right.
*  We don't know whether the grid cells in the abstract
*  is the same ones as spatial ones.
*  It's completely possible.
*  Like there have been these nice demonstrations that you can get grid cells
*  by just doing a PCA of your experiences. Right.
*  And there's plenty of evidence that your circuits can do PCA is maybe my subjects
*  had a bunch of experiences with with these frecky birds for hours.
*  And then over when they were sleeping, the miracles of sleep,
*  they did a nice PCA of their experiences and and outpops
*  from new grid cells that were never there for space.
*  I don't know. I don't know whether that's true or not.
*  Yeah. I mean, yeah, exactly.
*  OK, so we come to your barbaric bird experiment.
*  So maybe you can just really briefly walk us through what you actually did.
*  Not that you're pulling and pushing on actual birds and just what you found.
*  So I've just been explaining that Neil and Christian found this hexa
*  directional signal, the signal which changes depending on whether you're
*  running along the grid angle or across the grid angle.
*  That's like running in virtual reality in a two dimensional virtual reality.
*  And we had thought for reasons that I've just mentioned,
*  a similar representation might be true for more abstract models of the world.
*  And so we needed a model of the world where we could
*  which was amenable to this particular FMI measurement,
*  which is a measurement that we can make of grid cells in humans.
*  And so we needed a two dimensional model of the abstract model of the world.
*  And so we needed some stimuli which could vary in two dimensions.
*  And so we could have picked any thing that varied in two dimensions.
*  But you went to the pub and you thought, yeah, well, actually, I was in
*  I think that I was in a I don't know how it happened,
*  but maybe Alexa and I were discussing a paper of Russ Poldrack's
*  where he had some birds where he changed the the angle of the neck or something
*  like that. Yeah.
*  I don't think any ideas ever come to a pub without seeing stuff before.
*  Yeah, I think that I can't quite remember who had the idea or where it came from.
*  But it seemed silly, given that we were just looking for two dimensions.
*  It seemed like we should choose some ones that would be
*  interesting or fun.
*  And so we thought of using these these birds.
*  And I think it was related to Russ.
*  Russ Poldrack's got a paper with some birds in there.
*  And maybe we just seen that in the lab meeting or something. Yeah.
*  And so so we thought, OK, cool, we'll use these birds in the end then.
*  But then in order to get this measurement to work,
*  we couldn't just have the stimuli we had to have.
*  We had to be imagine you are moving in this two dimensional space. Right.
*  So in if you imagine the the physical experiment,
*  the physical real world experiment, they were it
*  depended on the direction of movement, not on the place.
*  And so in the analogy for non spatial dimensions,
*  you'd have to change from being from having one neck length to having another
*  in order to move in this two dimensional space.
*  And so the analogy for walking or running in these two dimensions
*  is morphing or stretching the legs or the neck.
*  So in order to get this measurement, we needed to be able to morph
*  the neck and the leg such that the movement in this two dimensional map
*  subtended different angles.
*  And so, for example, if you just move the neck,
*  you might be moving at nought degrees or we just move the legs.
*  That's orthogonal because they're two different dimensions.
*  So that would be 90 degrees.
*  But if you moved the legs twice as fast as you were moving the neck,
*  then that would be 60 degrees, et cetera, et cetera, in this two dimensional
*  in this two dimensional abstract map.
*  And so we had lots of birds that are moving.
*  There were more thing the legs and the next was stretching
*  at different speeds.
*  And so you'd have a duck turning into a swan turning into a flamingo style thing.
*  And you can imagine how you have to change the neck and the next in legs
*  to get those things to happen.
*  And then those movements would subtend
*  different angles in the in the map.
*  The subject would never see that.
*  But that's what the implication would be.
*  And then we went there and tried to figure out if we could
*  see the same hexa directional signal in this stretching bird space.
*  So like a morph that was at nought degrees or would have the same signal
*  as one that was at 60 and 120 and 180, but different from one at 30
*  or 90 or whatever.
*  90 plus 60 is 150.
*  Yeah. And so you can get this beautiful hexa directional symmetry
*  in the FMI signal.
*  And when we found we found that in just exactly the same locations
*  that Neil and Christian had found them in the FMI
*  and that Josh Jacobs and it's like we had found them in the single unit recording.
*  And we figured that that was pretty unlikely to happen by chance.
*  And so we got quite excited.
*  Yeah. So these are abstract bird concepts and relations
*  and nothing to do with physical spatial navigation.
*  So they're so they're navigating among these abstract concepts
*  that they had to learn for the scanner.
*  OK, so you've shown then that this the same kind of
*  hexa directional coding can be applied to these abstract concepts.
*  Now, I had Matt Botvinnik on the show a few shows ago now.
*  That must have been fun.
*  Oh, yeah. He's yeah. He was a lot of fun.
*  And we talked about as meta reinforcement learning work a lot.
*  So how does this grid like cognitive map fit
*  within that meta reinforcement learning work?
*  So just to recapitulate what that is.
*  So they they modeled the prefrontal cortex
*  and the basal ganglia as this big
*  recurrent neural network.
*  And the signals reinforcement learning signals from the basal ganglia
*  would train the recurrent neural network,
*  which was the prefrontal cortex, and it would mold and shape
*  the weights of that network.
*  And then they could hold those weights.
*  They would train on a bunch of different tasks.
*  And then they could hold those weights constant, freeze the weights.
*  Then the learning in the prefrontal cortex would then take place
*  among the activation dynamics,
*  among the units in the recurrent neural network.
*  And they saw a lot of the same things that you see experimentally
*  when you do these tasks and record neurons.
*  I think I summarized that OK.
*  But anyway, so it's a reinforcement learning.
*  It's meta reinforcement learning.
*  So it's a reinforcement learning system training, a reinforcement
*  learning system.
*  And you talk about this in the paper.
*  What is a cognitive map?
*  So how how does the idea of grid cell like coding
*  relate to or map on to this idea of meta reinforcement learning?
*  So, yes, that paper by Jane Wang and Zeb Kirtman Nelson and Matt
*  Botvinick is cool.
*  It it shows that you can learn something,
*  something about the structure of the problem that you're working in.
*  And you can use that to make learning much faster.
*  Yeah.
*  So instead of just learning,
*  instead of just rewards causing synaptic learning,
*  rewards can basically allow you to infer
*  where you are somehow in the structure of the of the task that you're performing.
*  And then you can make all these kinds of cool inferences
*  that I was talking about with cognitive maps earlier.
*  And what they also showed beautifully that that structural knowledge
*  that is held in what they can call the prefrontal cortex can itself be trained
*  over very long time periods by rewards.
*  So you can just build you can just get over many, many experiences.
*  You can build effectively a cognitive map by getting enough rewards
*  so that they called it meta learning because learning the structure of the world,
*  which is somehow a cognitive map, allowed them to learn
*  which thing was rewarded now much faster
*  because they knew the structure of the task or the world.
*  So people have studied these problems in psychology for a long time.
*  The earliest people are like Harlow and he and he he called it learning set.
*  Once you know the structure of a problem, you can learn each new problem much, much faster.
*  So the brain definitely does this.
*  And it's really cool to show that your network can do it as well.
*  It's great fun.
*  So there are some differences between that and a and grid cells
*  that are worth, I think, pointing out.
*  So the first like simple obvious difference is that grid cells are not trained by reward.
*  So Matt and and Zeb and Jane,
*  in order to learn the cognitive map, they did this thing called meta
*  reinforcement learning, which is meant they which has meant they could only learn
*  something new about the cognitive map over very long time scales
*  about which structure, which cognitive map
*  predicted slightly bigger rewards over very long time scales.
*  So it's like really an extreme version of trial and error learning.
*  And you're not.
*  So it's like when you're when you walk through
*  a new room, you will just by associating temporal sequences
*  of associating this room for this corridor, followed by this room,
*  you'll be building up a map just like Tom Tolman's rodents.
*  Rats work to start with.
*  And but but but Zeb and Matt and James
*  network will not be doing that.
*  It will be it will only make it will only change the synaptic
*  weights when it gets a reward.
*  And so it has to.
*  So obviously, they could change that.
*  And I'm sure they are doing that right now.
*  But it's not clear what the correct algorithm for this implicit learning
*  or learning from organizing all of that rather than.
*  So what effectively what they did was allow reward to organize
*  their knowledge into what's relevant and what isn't relevant.
*  And it was it's a clever idea. It's cool.
*  Maybe there are systems in the brain that do that as well.
*  But but that's clearly not what grid cells grid cells.
*  As I told you at the very start of this podcast,
*  we know all sorts of implicit knowledge about the world
*  without ever experiencing any reward at all. Yeah.
*  And so that's one thing that's clearly different about the middle temporal
*  lobe system from from the systems they were modeling in Basel,
*  Ganglia and and frontal cortex.
*  Another thing that's different about it, I think, and I guess
*  Zeb would agree with me, I don't know if Matt would.
*  I haven't spoken to him about it.
*  So I think that the hippocampus system
*  benefits from this thing called factorization, where it can.
*  So there are these remapping experiments showing that
*  if you go between room A and room B,
*  you can get completely different place cells active.
*  But the the grid cells maintain their structure,
*  maintain their metric structure on over these two completely
*  randomly different place cells.
*  And so something about the structure of the world
*  has been separated from something about the sensory and sensory world.
*  And that means that the grid system, I think, would likely
*  be able to generalize beyond its experiences outside of its experiences
*  to do something called extrapolating. Right.
*  So normally, generalization
*  would work in networks, for example, in deep networks,
*  where it works best if you're sort of effectively interpolating your experiences.
*  And I think that's certainly true of Matt and Zeb's network.
*  Basically, in order to get it to do something in order to in order
*  to do something good in a new environment, it has to have seen some
*  an environment that's more extreme than that environment on every dimension.
*  It has and it can do a really good job of of of
*  interpolating its experiences to some new situation.
*  Yeah. I mean, I think that because the the the sensory input
*  and the grid input is factorized in the in the end system,
*  it can do clever things outside of its of the set of experiences that it's had.
*  I don't know whether that's too complex for the podcast, but that's another
*  slightly more sort of technical difference, I think,
*  between the kinds of cognitive maps that you might that might be represented
*  in those different places.
*  But and the other sort of more obvious sort of very clear
*  and obvious potential difference is, of course, that we don't even know
*  if the grid cells are learned at all or whether they come in those structures
*  delivered by evolution.
*  And so then you're that's that's more like another kind of meta learning,
*  which is like designing new architectures,
*  but learning, learning new architectures in deep net,
*  which is also a kind of meta learning.
*  And you might argue that evolution in some way does this kind of meta
*  learning as well to design the best architecture to solve spatial problems.
*  Yeah. Anyway, all those things add up to some interesting differences.
*  But I think the biggest conceptual differences is between those types
*  of learning of a cognitive map is that
*  Matt and Zeb and Jane are really worried about learning from reward,
*  whereas the hippocampus is really is learning from everything.
*  So do you think that,
*  I mean, do you think that the idea of the cognitive map
*  and these hexa directional codes will
*  fit in with the reinforcement learning work to.
*  So what I'm wondering is like how. Yeah, right.
*  So the whole how these grid cell like codes will will improve
*  AI moving forward, essentially, you know?
*  Well, I mean, I think that they
*  there's like a whole field of work on model based versus model
*  free reinforcement learning that's where building models of the world is.
*  So if you have a model of the world,
*  you can do all sorts of things that you can't do with without a model of the world.
*  And it is a major topic of research at like DeepMind, for example,
*  they have a science paper on building models of space.
*  They have a nature paper on on grid cells in spatial models
*  because they realize that if you have your relational knowledge
*  organized well, then you gain an awful lot more from each reward
*  than you do if you don't have it organized well.
*  You can learn much faster from much fewer data points.
*  You can make analogies between things that are similar in some dimension.
*  You can do this other thing that the hippocampus does, which is simulate.
*  So you can before you make decisions or you can try things out in your model.
*  And these are all active areas of research at DeepMind, for sure,
*  where I hang out sometimes.
*  So for me, the essence of cognition.
*  So I mean, I'm more of a cognitive
*  than I am a behaviorist.
*  I think that the
*  the essence of cognition is going to be how rich your your world model is,
*  not how many rewards you've experienced.
*  And I think I think that will be true in deep networks
*  as well as it is true in brains.
*  I mean, basically humans, because they can.
*  So I guess there's three or four things that humans do really, really well
*  that the deepness don't do really well.
*  I mean, there's many, there's many.
*  But like the ability to abstract, the ability to generalize
*  the ability to make inferences
*  things that are that are not in your direct sensory environment
*  all allow you to learn from dramatically less data than
*  any deep network that we have at the moment.
*  So do you think that thinking about general AI,
*  which is the goal among a lot of AI practitioners,
*  do you think that this grid cell like code is
*  the missing piece, one of a few missing pieces,
*  one of many missing pieces that could that could herald in
*  get us closer to what people would consider human level or general AI?
*  I. I don't know how
*  nobody can answer that question, but yeah, I'm not going to argue
*  that it's a grid cell like code, certainly.
*  But I mean, I think the idea of building models of the world
*  of the world is a really important piece in building
*  organized, efficient models of the world is a really important piece
*  in building more sophisticated AIs.
*  If what you're trying to do is build a human, then you need something
*  that has a model, not only of the outside world, but also of itself.
*  And then you get into complicated, interesting
*  arguments about what a model of self looks like.
*  But that's I think that's certainly true.
*  I think certainly a major part of what we call our psyche is our model of ourselves.
*  I think that the part of your model of yourself is a model
*  of what other parts of your brain are doing, parts of your brain
*  that maybe don't themselves have a model of yourself.
*  Like, I guess people would call it the early brain systems
*  that are very responsive to threats and fears.
*  And you I think your cortex will build models of those of those brain systems.
*  And I think that you also need a model of things that
*  I don't know how I will ever get a model of like your gut.
*  And when you're hungry and you're like, I mean, I don't know.
*  I'm not sure the goal of AI is to build something like a human.
*  But if it is going to build something like a human, then the thing is going to need
*  to have arms and guts like a human to unless we give it those models.
*  Well, that's a question is how human do we want AI to be?
*  I mean, it's it's a really open.
*  That's a that's not a question for a scientist.
*  That's a question for an editor.
*  Yeah, sure, sure.
*  So, OK, well, there's rightly so.
*  There seems to be a lot of excitement with grid cells lately.
*  I mean, when you went to 2000, when you win a Nobel Prize for it,
*  then that ushers in a lot of excitement.
*  That wasn't me.
*  They won the Nobel Prize, unfortunately.
*  When one wins a Nobel, when a Nobel Prize is won for a certain topic,
*  that topic is going to garner some attention.
*  And so you're doing this great work and continued success with with moving forward.
*  Tim, what's what's a special talent that you have that
*  maybe not many people know about?
*  I can lick my nose.
*  We're on video. Oh, my gosh.
*  He did it, folks. And now he's not stopping.
*  Well, what?
*  What? Well, that was OK.
*  Well, now we're done. Thank you very much.
*  What can you do?
*  Uh, I can stick out my tongue and touch my nose.
*  Can you go for it?
*  Oh, yeah. No, not with your.
*  No. OK.
*  So what's what do you have a book that you might recommend to people
*  to help them think effectively about these sorts of topics of neuroscience,
*  AI or just intelligence or cognition in general?
*  Yeah. So
*  a day on an average is the best competition on neuroscience book.
*  And McKay is the best AI book.
*  And that's the day on an average theoretical neuroscience.
*  And I can't remember what McKay called his book, but you'll find it.
*  It's freely available online as everything he wrote.
*  What is it's an inspirationally wonderful book.
*  Bishop is good as well and great, but not as good as McKay.
*  And what's good on cognition?
*  Well, I mean, there's books about cognition.
*  Hofstad is fun to read.
*  Oh, good God.
*  I mean, he comes up every podcast.
*  I'm going to have to read the whole thing now.
*  He's fun to read. Yeah.
*  It's interesting. It's inspiring.
*  Yeah. Good. OK.
*  So that's a lot of different answers. That's nice.
*  Have you ever been wrong about anything?
*  I'm wrong about things all the time. Just ask my lab.
*  Anything in particular stand out that that was really
*  affected you or your career or anything?
*  I've ever been wrong.
*  You mean about a scientific position or about?
*  I mean, I. Yeah.
*  So I mean, like a lot of my ideas are wrong,
*  but I try to not be firm in my ideas until I have evidence for them.
*  And so I don't think I've ever been embarrassed.
*  Me wrong about something because I I mean, maybe I'm embarrassingly wrong
*  about the things I'm saying now, but
*  mostly what I try to do in my career is report data.
*  And so I that, yeah, it's not it's not like I just state opinions
*  that that are not I I've never in my life just written a paper stating an opinion.
*  And so and yeah, so I've definitely been wrong in what I think is going on
*  in the brain many, many, many times.
*  But usually before I've been wrong, I've tried to test it.
*  Um.
*  What's something that you wish that you had known going into
*  cognitive neuroscience, neuroscience in general?
*  I don't know, man.
*  So I drifted my career, my career drifted,
*  it drifted slowly and moved and moved around.
*  And and I maybe maybe I mean, so I mean, I I I I played with
*  I spent a lot of my time making data algorithms for for for this
*  and the other, including for like Formula One cars when I was a PhD student as well.
*  And I played around with deep with with neural nets back then.
*  And maybe if I did, this was in the age before we had faster compute,
*  fast enough computers for them.
*  And I feel like I could have been a much richer man if I realized
*  how powerful they would be once computers got fast.
*  Maybe that would have been fun.
*  I would have been useful to know how know about Bitcoin as well.
*  That would have been good.
*  Oh, good. Yeah, yeah. Sure.
*  OK, so what what is something that you believe will come out of the interface
*  of neuroscience and AI work that may sound crazy or counterintuitive?
*  Yeah, I don't know. I mean, I guess I think that the crispest
*  ideas from AI have not been anything to do with neuroscience,
*  but the biggest intellectual leaps in terms of the inspiration often have.
*  I think that when Jeff Hinton was thinking about
*  the sleepwalk algorithm, he was thinking about the brain.
*  I think when he was thinking about convolutional neural networks,
*  he's thinking about the brain with Leanne McCurn.
*  I think that when he probably wasn't thinking about the brain,
*  when he was designing the KL divergence
*  just to optimally organize the sleepwalk algorithm
*  or the backprop algorithm to optimally fit his convnets.
*  But I think that the sort of when he was dreaming about how to
*  the sort of structure of what was happening, he was thinking about the brain.
*  And I think there are other that whenever we know something definitive
*  about the brain, it will inspire things in AI.
*  I think that that that's true.
*  And I think that of the recent big things in AI,
*  a lot of them still have been have been brain inspired.
*  So I feel like although the really crisp thinking and the
*  and the the way to really make things work comes from the maths,
*  it's difficult to have an idea with no inspiration.
*  So I think that's that's why I would say.
*  But you're not going to speculate on anything that might sound crazy.
*  That's going to that we're going to see in 20 years or something like that.
*  Well, I mean, there are other types of cells that there are crisp
*  that are not in neural networks yet, like mirror neurons, for example.
*  Mirror neurons are going to require
*  neural networks to have models of themselves and models of how
*  and analogies between other people and themselves.
*  And those I guess people are building are going to start building
*  neural networks that have models of the neural network,
*  a that has a model of neural network B and those kind of things.
*  And then we'll start seeing those kinds of cells in in
*  in those networks as well.
*  Cool. OK, last question.
*  What are you going to be doing five minutes after you hang up with me?
*  I'm going to speak to a colleague about a journal called E-Life.
*  Another another meeting, another meeting.
*  So all day, I don't miss the meetings.
*  So anyway, thanks.
*  Thanks for. So I appreciate you letting me stretch your time
*  like you stretch bird necks.
*  So thanks for taking the time with me, Tim.
*  It was really fun. Thanks very much indeed. Cheers. Bye.
*  Brain inspired is a production of me.
*  You can support the show through Patreon for a trifling two or four dollars per month.
*  Go to Patreon dot com slash brain inspired
*  or go to the website brain inspired dot co and find the red Patreon button there.
*  Your contribution will help keep this show going without any annoying
*  advertisements like you hear on other shows.
*  To get in touch with me, email Paul at brain inspired dot co.
*  The music you hear is by the New Year. Find them at the New Year dot net.
*  Thank you for your support. See you next time.

---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 6358s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 7595
Video Rating: None
---

# BI 076 Olaf Sporns: Network Neuroscience
**Brain Inspired:** [July 04, 2020](https://www.youtube.com/watch?v=ah257akIv3Y)
*  So, what makes us human then is I think nothing magical, nothing, I don't think it's a special
*  cell type, it's a special brain region, it's a special type of connectivity or topological
*  feature.
*  It's the sudden explosion of possibilities that occurred when our brain topology became
*  capable of using our bodies and feeding itself information in new ways.
*  So, there's a network there, a larger network that's above and beyond what we can measure
*  in individual brains, but I think that's the way I think about it.
*  I was working on some of this stuff, you know, 20, 25 years ago, and believe me, nobody had
*  any interest in it.
*  I gave a talk on small world networks, my first talk on the subject in 1999, and exactly
*  three people showed up.
*  Wow!
*  This is Brain Inspired.
*  Yes!
*  What pops into your head when I say network?
*  Do you think of an artificial neural network, like a deep learning model?
*  Or do you think of real neurons and their connections and brains?
*  Maybe the cities in your country connected by roads?
*  Maybe an ant colony?
*  If you're Olaf Sporns, all these things pop into your head because everything is a
*  network.
*  Olaf has been studying networks for many years now, and specifically networks of the brain,
*  which happens to be the title of the book he wrote about a decade ago, Networks of the
*  Brain.
*  Olaf and his colleagues are responsible for giving us the word connectome, which is the
*  wiring diagram of the brain at various spatial scales.
*  It's a structural network, the connectome, but there are networks made of the activity
*  patterns of our neurons as well, functional connectivity, and all the network dynamics
*  in between.
*  And in the past ten years or so, the study of brains using network science has taken
*  on the name network neuroscience.
*  And that's what we discussed today.
*  We talk about where network neuroscience came from, where it is now, and where it's
*  how Olaf thinks of brain networks relative to artificial neural networks like the current
*  deep learning models.
*  So hopefully this conversation serves as an introduction for you to learn more, which
*  you can do through the show notes at braininspired.co.
*  Speaking of learning more, I was on a run yesterday.
*  I was about halfway up the mountain gasping for air, and in my oxygen-deprived state,
*  I realized something I should have been doing all along in this podcast, and I will start doing.
*  So before I air an episode, to those of you who would like it, I'll send an email with
*  a relevant paper or paper abstract or a link to a video, something like that, that will
*  serve as a primer for the upcoming podcast episode.
*  So if you use this podcast as a source of education or you just want to get more out
*  of it, I know it can get sort of deep and technical sometimes.
*  Hopefully you'll get this email from me.
*  You can digest whatever I send in the email and then let your subconscious do its thing
*  before you listen to the episode.
*  So I put a sign up box right on the home page at braininspired.co, where if you sign up
*  there you will receive these emails about upcoming episodes.
*  I'll also do this on Patreon, of course, where sometimes before I even record an episode,
*  I ask my Patreon supporters if they have specific questions for the guest that I am
*  soon to speak with.
*  OK, Olaf was a pleasure to speak with, and it's exciting to think of where network neuroscience
*  is headed in the near future, and it's good to know that people like Olaf are working
*  on it.
*  Thanks, as always, for listening, and enjoy.
*  Olaf, you just informed me that you are new again just today to your now useless office.
*  How does it feel to be back in your office?
*  Well, it's a little surreal.
*  The department building is completely deserted, and we're still shut down.
*  We're going to open up next week, presumably with some research activity, but for the moment
*  everything is completely empty.
*  I haven't been back here very much at all, maybe twice or so over the last two months,
*  and it's odd to be back in your office seeing it after so many days.
*  Do you miss it, though?
*  Does it feel like coming home in a sense?
*  I do miss it.
*  One thing I miss is that the work-life balance is a little out of shape.
*  I used to use my office a lot for work and then go home and not do a lot of work.
*  Now I'm working from home, so now it's all mixed up.
*  I guess that's the new normal.
*  Also, I miss my books and my papers that are stacked up in my office.
*  I don't have any access to those.
*  I've lost that, but we're managing.
*  I'm glad I could draw you back into your office for an hour or so here.
*  Well, welcome to the show.
*  I want to say thanks for coming on, but also thank you for running a journal that's completely
*  open access, Network Neuroscience Journal.
*  So thanks.
*  Yes, I started that journal with many colleagues in the field in 2016.
*  I was an early adopter of the open access model with PLOS going back almost 15 years
*  now.
*  I strongly believe in the open access model for publication and sharing articles for free,
*  making them immediately available to everyone.
*  That's what we do.
*  We've done this from day one, and it's a model that apparently is being adopted more
*  and more.
*  So how's the journal going?
*  We're doing great.
*  We have a steady flow of submissions.
*  We have an area that I think we're going to talk about more later today in this conversation,
*  network neuroscience.
*  It's a burgeoning, rapidly growing subfield of both neuroscience and network science,
*  and we get really great submissions.
*  We have an enthusiastic board of editors and our reviewers are doing a great job too.
*  So we're doing well, and I'm hoping to expand the journal for the coming years and I'm really
*  working on it.
*  That's great.
*  Just reading the literature, you said it's burgeoning.
*  It feels like it has burgeoned, but I'll ask you about that in a little bit here.
*  Okay, so network neuroscience.
*  I understand that the lofty goal of this subdiscipline, network neuroscience, is to use complexity
*  and network science to bridge all of the levels in neuroscience.
*  So that's from the molecular networks within individual neurons even up all the way to
*  social networks between individual people and as a collective.
*  Today we're probably, I think, going to focus mostly on the level of neurons and the structures
*  that they form, the connectome and the dynamics and functional activity that they give rise
*  to.
*  So I guess I'll just start by asking you how network neuroscience conceptualizes brain
*  function.
*  Good question.
*  And I've come across people who've said to me, well, networks have been around for a
*  long time and so there's nothing new about it.
*  However, there is because while the term network has been used in neuroscience literature for
*  quite some time really, there's a technical way in which we use the term in our little
*  sub area and that is a network is a complex system that's been divided up into nodes and
*  edges, elements of interconnections, and we represent it as a graph.
*  That is a very technical meaning of the term network and that approach does not have a
*  long history yet.
*  I remember starting doing this with some of my colleagues back in the 90s when there was
*  really no interest in this at all.
*  And now it's grown tremendously in part because network science has grown.
*  Network science is a discipline that deals with networks in all contexts.
*  Epidemiology, we're living in a network science world right now because some of my friends
*  in the field are modeling the spread of COVID and that's a network science application.
*  But also in social systems and technological systems, the internet, of course, then social
*  networks and of course, biology, networks of proteins, networks of cells, and the brain
*  is an example of parks and loss.
*  So this is really a technically founded, technically precise undertaking of understanding a system
*  like the brain from a perspective that is based on networks as collections of nodes
*  and interactions.
*  The nodes can be neurons, they can be brain regions depending on the recording methodology
*  or the scale we adopt, and the interactions can be synaptic connections, physical connections,
*  pathways, or functional interactions, dependencies, statistical dependencies, etc. that we talk
*  about in functional connectivity.
*  So that sort of nexus of network science on one side and neuroscience on the other, it's
*  fairly fresh and it has taken off like a rocket ship early.
*  It's amazing to see for me because I, like I mentioned, I was working on some of this
*  stuff, you know, 20, 25 years ago and believe me, nobody had any interest in it.
*  I gave a talk on small world networks in my first talk on the subject in 1999 and exactly
*  three people showed up.
*  Wow.
*  Yeah, the guy who invited me to give the talk and his two graduate students and that was it.
*  You need a world to have a small world network and that wasn't quite a world.
*  And, you know, if I had had any sense of risk aversion, I would have given up on it, right?
*  I would have sort of said, well, that's not going to work because I had this really no
*  interest.
*  But I prevailed and then a few years after that, the idea of the Connect Home came about
*  and, you know, mapping a nervous system in its entirety and at some level of scale with
*  all connections and all elements.
*  And that then became the starting point 15 years ago for where we are now, which is really
*  a big field.
*  I mean, you know, I want to ask you about 100 questions right now.
*  First of all, I'm going to have David Krakauer on the show soon, who's the president of the
*  Santa Fe Institute for Complexity.
*  I know he's been very steeped in the COVID-19 modeling of it, you know, from the network
*  and complexity side.
*  So, you know, that everybody's turned to that's the most famous network right now,
*  I suppose.
*  It sure is.
*  In fact, I'm teaching a course on graduate course on networks.
*  I just taught it in the spring.
*  And when I, you know, in my first class, that's one of the applications that I put on my,
*  you know, on the screen and say, yeah, this is a network.
*  It has a virus spreading.
*  And, you know, there were, we've had a few of these outbreaks now with Ebola and with
*  H1N1 about 10 years ago.
*  Some of my colleagues, good friends in the field, they are modeling that stuff, literally
*  trying to forecast in real time.
*  It's very data driven.
*  It's very, very much of an application of network science.
*  And I wish we had the kind of predictive, you know, data driven modeling in neuroscience,
*  you know.
*  We don't quite yet have the data intake.
*  We don't quite yet have the viable computational framework to use to really make sort of predictive
*  models of brain function.
*  That would be fantastic to have.
*  And maybe we'll get there one day.
*  Yeah.
*  Well, just before we move on again, I usually say this kind of question for toward the end
*  of the show.
*  But since you brought up the three people showing up to your 1999 talk, do you think
*  that that's an important character trait to just keep going in the face of these?
*  I don't know if that's an obstacle, but it is a bad sign.
*  What would you call that experience?
*  Yeah, I sometimes talk to, often talk to, you know, early career scientists, grad students,
*  postdocs about what should what should they do specialize in?
*  How should they shape their careers?
*  And I'm a bad example because I bet on things that didn't really have a high probability
*  of success.
*  Even computational neuroscience, which is now a an ingredient of all neuroscience almost
*  was a was a very small field back in 1990 when I got my Ph.D.
*  When I got my Ph.D., there was no fMRI.
*  So, you know, nothing and nothing that I learned during my Ph.D.
*  classes, courses, projects, whatever, really prepared me directly for many of the technical
*  things that I'm dealing with today.
*  So, you know, it's I kind of persisted in part because I had a few good friends in the
*  field who were equally persistent and who gave me the kind of social support that I
*  needed. You know, Randy McIntosh, Julia Tononi, Carl Friston, those those guys helped me
*  kind of, you know, keeping keeping pushing on in that direction.
*  And eventually we made me made it to the point where it took off and became a an activity
*  that was that is now widely adopted.
*  But that's sort of a principle that low probability, high, high risk, high reward.
*  I you know, that seems to be a recipe for mostly failure and some success.
*  And I don't know how you get the success part of it.
*  Well, I mean, I had I was working on small world connectivity patterns in the 90s and
*  complexity. But I also had other lines of research that I was pushing simultaneously
*  that that were maybe not quite as fringy as that or as arcane and obscure.
*  I was working with robots for a while trying to understand how the brain is embedded in
*  its environment, how the interaction, sort of the dynamic interplay between behavior,
*  movement in the real world, sensory sampling and then brain activity, how that kind of
*  plays out. And robotics was a test bed for that.
*  So I actually had a robot lab for a while and published in that in that in that field,
*  went to meetings at the time quite a bit in an area that's called embodied cognition.
*  It was not totally unconnected for my network and complex systems leanings, of course,
*  because there is still that element of connectedness, right?
*  The brain is connected to the world and to the environment and being an active participant
*  in that interplay, not just a passive sort of, you know, intake of information processor
*  kind of thing, but really shaping the information itself.
*  That was an important lesson that I learned when I was working in that field.
*  And I pursued that in parallel.
*  Also, when I moved here to Indiana University for a few years, I had a robot lab here.
*  And then in 2006, 2007, 2008, connectivity suddenly took off and it sort of consumed
*  my research program entirely.
*  So that's all I'm doing now.
*  The robots are gathering dust.
*  So work all the time.
*  Keep your fingers dipped in a few different buckets along the way.
*  Know when to stop and know when to grab on to the reins and and let it ride.
*  Huh?
*  And and also reach out to others.
*  One of the most important pieces of career advice I like to give sometimes jokingly is
*  maximize your betweenness centrality.
*  In other words, think of yourself in your social in your social network as a scientist,
*  as someone who builds bridges.
*  OK, someone who is in between fields, who makes the connection, let's say between robotics
*  and neuroscience or between neuroscience and network science or complexity.
*  Someone who is conversant on both sides, someone who can bring to the table expertise
*  that otherwise isn't available and makes that connection.
*  It's often those connections that ultimately grow into the next big field or activity
*  that blossoms from that.
*  And you have to have a certain amount of self-confidence, maybe.
*  And and persistence.
*  And even though I never really reflected on it very much at the time, it turned out that
*  I made some some choices that apparently have paid off.
*  Well, sorry, I've taken it so far off course already.
*  But, you know, these days, I know that it's networks all the way down for you.
*  You think in terms of networks with virtually everything like you were just saying.
*  And, you know, so that was in 1999.
*  You gave that three person three attendees talk.
*  And then 10 years later, you 10, 11 years later, you published Networks of the Brain,
*  which is sort of, you know, which was the I don't know, the first book about brain networks,
*  wasn't it?
*  In a sense, yes.
*  I mean, there's always always examples that reach back further.
*  And I had, you know, I have a lot of respect for many senior colleagues in my field who have
*  been thinking along similar lines of mention a few names already.
*  And so I was building on that partially.
*  But I yeah, I wrote that book.
*  I don't know how I did it.
*  I wrote it in 10 or 11 months while I was doing administrative work.
*  The lab never stopped.
*  I was traveling. I remember I I somehow managed.
*  But I think in part because I had that plan in my head for a long time of writing that
*  book and and making that connection between complexity, science, networks and brain
*  function. And I wanted to get some of the key ideas that have animated my own work until now.
*  I wanted to get them across.
*  And so I was very happy to it was a great exercise to write, allowed me to be a scholar for a
*  while and work on something actually entirely on myself.
*  And I'm so pleased with the fact that so many people have read it.
*  And even today, and it's now a decade since it came out, I still come across some people
*  now and then and places that I visit that, you know, pull out their book and say it really
*  made a difference to me to read this and really got me started in my own way.
*  And that's sort of the best reward you can have.
*  You know, somebody actually reads it and takes it takes it to the next level.
*  It really happens with papers, right?
*  Papers have a shorter lifetime in many, many cases.
*  This book is now a decade old and it's still apparently doing quite well.
*  Well, I was going to say, I have a bit of regret, actually, because I remember when the
*  Small World Network stuff was just really taking off and even in the popular press.
*  And and I remember when your book came out and I thought, oh, I should, oh, I should
*  really read that because it seems like this network stuff is taking off.
*  And then I didn't. But I recently did.
*  And first of all, it's extremely well written.
*  It's just a very easy read and gives a great overview of the field.
*  And I know that the network neuroscience has come a long way since then.
*  But I still think it's a wonderful introduction to the topic.
*  And I don't know if a second version is coming out and if it's going to be 10 times as
*  thick or what. But what I want to ask is, you know, since then, you know, we've come a long
*  way. So what is the broad current picture in network neuroscience?
*  Well, first to your question about is a new book coming?
*  I have plans to do something like that.
*  And but it keeps getting away from me.
*  So let's hope I find a break and do it.
*  And I think to your point about it's network, no science has come a long way.
*  Honestly, that book, you know, the references kind of stop in 2009, 2010.
*  And there's been so much more.
*  And our perspective has changed a lot, too.
*  You mentioned small worldness, for instance.
*  It was in many ways a concept that got network science started
*  and restarted and restarted in the 90s with that famous Watson Storgraf paper came out of nature.
*  But today, small world is a totally neglected topic as it doesn't matter anymore.
*  In fact, now we kind of realize that many so many networks.
*  It's everywhere. Yeah, it's everywhere.
*  So in some ways, it's lost interest.
*  People have lost interest in it.
*  That's no longer the core of the field at all.
*  We are now in a very different world.
*  And so to your second question, where has it gone?
*  Right. We want the two things have happened that have driven, I think, the expansion of
*  of network neuroscience.
*  One is that we have a lot more technology available to us today than we had even 10 years ago
*  in terms of recording brain activity, neuronal activity and whole brain activity
*  and take in that data and then and then do data science on it.
*  Essentially, time series analysis through dimension reduction techniques,
*  network science tools, et cetera,
*  kind of dig structure and patterns out of those data.
*  One of the big ways that, you know, one of the big reasons why network neuroscience
*  took a while to take off was because we have no data.
*  Fifteen years ago, 2005, you know, when we wrote that connectome paper,
*  which really was a manifesto that said we need that type of data and information
*  to make sense of the brain, but we didn't have any.
*  And so now we are swimming in data.
*  So that's driving.
*  So there's a demand for tools and techniques to really make sense of the data.
*  The data is not in itself is great to have, but you really want
*  understanding of what the system is doing for that.
*  You do need in part network science methodology
*  because the brain is fundamentally a network.
*  It is elements and interactions.
*  And that's right.
*  That's been driving, I think, the expansion of network
*  neuroscience methodology into electrophysiological recordings,
*  EGM, EG, certainly fMRI and diffusion imaging and whole human brains,
*  but also model organisms, zebrafish, mouse, rat, C elegans,
*  you know, network language terminology, tools, techniques are really
*  pervasive almost in those types of investigations.
*  And it's driven in part by the data.
*  This is an interesting conundrum, I think, because we run up against it all the time.
*  You know, there's this.
*  Cycle, you know, you get more data and then you develop more
*  theoretical tools to analyze the data.
*  But you and you have something like network science, where in theory
*  you have the theoretical tools and you're waiting for the data.
*  But then the data comes and you realize, oh, my gosh, it's
*  we don't have the theoretical tools.
*  It's it's interesting that we cannot
*  imagine what would we do if we had all the data?
*  And I think this is just going to continue moving forward.
*  But, you know, eventually we're going to have the activities of every single neuron,
*  every single type of neuron, you know, and it's going to go into a database.
*  We should, in theory, be able to think what would we do with that data?
*  But we can't do that.
*  And it's an interesting barrier, I find.
*  There's multiple questions that I want to unpack a little bit.
*  So your first point, just to make sure
*  I'm not overstating
*  the tools that we currently have, even from network science,
*  even some of the most advanced things are not always perfect
*  for what we want to do in neuroscience.
*  And one of the ambiguities of network science is because there is
*  a general framework coming more from physics and statistical
*  investigations of networks.
*  But there's also that domain specific knowledge, right?
*  It's data that comes from the brain and that data is the origin of data.
*  We have to take that into account when we analyze the data and model the data.
*  We can't just blind ourselves to it's just a network.
*  You know, that's not that's not quite the way I see it.
*  So the demand for brain specific, brain appropriate, if you wish,
*  tools and methodologies is still there.
*  There are many questions that we cannot answer or even address
*  with network science tools yet.
*  And so that's an ongoing process.
*  Secondly, that's a good question.
*  What would what would we do?
*  What will we do when one day we have a let's say a full account of all neurons,
*  what I call all neurons all the time? OK.
*  Oh, the structure and activity, right? Exactly.
*  So what would we do?
*  You know, just imagine, let's say humans.
*  OK, let's take humans, you know, 80 billion or so nerve cells.
*  And and I like to forget the exact numbers,
*  but certainly trillions and trillions of spikes that occur
*  in any given small period of time as we engage in spontaneous
*  mental activity, but also behavior.
*  So now what are you going to do? OK.
*  That is a a a tough challenge.
*  Not only that, because, you know, all the synapse formation and,
*  you know, just all of the connections that are dynamic
*  the entire time, which sounds crazy.
*  There's dynamics.
*  I'm glad you mentioned it.
*  Even the structural connectivity isn't standing still.
*  I used to actually in my 25 years ago when I was doing wet lab work,
*  that was one of the things that really I wanted to image with with calcium dyes
*  and with with with, you know, I work with with rat cultures at the time.
*  Neural cultures taken from the rat hippocampus to see the plasticity
*  of neural connections across time, essentially take years.
*  And yeah, absolutely.
*  It's changing all the time.
*  It's not standing still. It's not static.
*  It's dynamic structure.
*  The structure changes.
*  The activity on top of the structure changes even faster.
*  And so this is a tough challenge.
*  And I think that that challenge cannot be met entirely with, let's say,
*  you know, that's let's say machine learning or some sort of,
*  you know, throw all the data in a big box, you know,
*  wait a long time or maybe wait a short time and out pops
*  an answer that says this is the this is what's going on.
*  I don't think we can we can quite take that black box approach.
*  I do think and I'm a strong proponent of a theoretical neuroscience.
*  In other words, we do need some overarching mathematical principles.
*  Perhaps we can at some point in the future even call them laws
*  that help us to understand our observations and structure them
*  based on regularities that we believe exist in the world.
*  Without that, the the that it becomes a,
*  you know, an exercise of extracting regularities
*  from high dimensional data.
*  And that's what we for the most part are doing now.
*  Looking for patterns, we're looking for for stable, coherent
*  assemblies of brain regions that say, or the interactions
*  or in terms of neurons, looking for population activity.
*  We're looking for low dimensional manifolds within which we can describe
*  and predict neural activity.
*  And that's important, too.
*  But I think we're still lacking
*  a theoretical framework that we can put over our observations.
*  And that also help us to decide what it is we should measure. Right.
*  There's lots of things that we that we may that we may want to measure in the brain.
*  But what is what are the important variables to track?
*  There are some that perhaps we haven't even figured out yet
*  that that we are missing entirely.
*  So it's sort of a fundamental thing that we need some toys to play with
*  before we can figure out what other parts of those toys
*  we need to collect to make the thing.
*  And that's a terrible analogy.
*  I apologize. But, you know, I sometimes think of laws
*  and even, you know, dimensionality reduction and manifolds
*  and anything like that to reduce the parameters
*  that we use to think about all of these things just as shortcuts to
*  the eventual simulation.
*  But, you know, so so this is where complexity comes in, because
*  it's so complex that to actually really recapitulate it,
*  you have to simulate the whole thing.
*  And that takes infinity.
*  I would cripple with that just a little bit.
*  I don't I wouldn't advocate simulating the whole thing
*  in the sense that, you know, literally everything has to be included
*  in a simulation to understand the real system, because then you
*  what you end up doing is you're replicating
*  the the complicated system you're studying by another complicated system.
*  And now you've you've gained nothing really.
*  You've gained something because you can manipulate the simulation,
*  perhaps more you can use it for forecasting and perturbations and so forth.
*  But but it is not quite understanding of the kind that I'm that I'm driving at.
*  And mind you, complexity, as I view it,
*  does not necessarily mean a an endless profusion and and
*  massing of facts and elements, you know.
*  So it's not complicatedness.
*  Complexity has its own lawful behavior to it.
*  It's unpredictable in many ways.
*  But but it doesn't that doesn't mean that it's that it's entirely random.
*  Complexity kind of, as I like to view it,
*  sort of resides in between randomness and, you know, sort of complete
*  disorganization and on the other on the other end of the spectrum,
*  you know, complete regularity or or or simple replication.
*  Actually, somewhere in the middle.
*  So complexity, if you want to take it seriously,
*  it doesn't mean that we have to look at everything at once.
*  It means that we need to identify those system
*  variables, those things that we need to track
*  that inform us about the state of the system,
*  allow us to to predict its future to some extent.
*  And that is still an ongoing project in our field.
*  I would say networks are one of those ingredients.
*  And I think increasingly in neuroscience dynamics is the
*  is the second ingredient that I think people are certainly taking
*  taking advantage of and pay attention to.
*  And so the intersection of networks and dynamics is kind of where I feel like
*  there's a lot of interesting things happening right now.
*  The that means dynamics on networks, but it also means dynamics of networks,
*  how networks change across time and how that change in term leads to changes
*  off the functional dynamics on top of those network structures.
*  This is what hopefully we'll get into this pretty deeply in just a little bit here.
*  Just to move us forward, because now I just want to perseverate on every point.
*  But because I don't advocate simulation, sir, but
*  now I know that you don't either.
*  So do you think that network neuroscience is going to provide
*  the quote unquote breakthrough that neuroscience has seemingly
*  sought for so long and some people some people expect at some point to happen?
*  Well, I think I think what it has done, it has
*  it offers a new perspective that says the brain is in some ways
*  is not that different from other complex systems.
*  It is a complex system.
*  It belongs to that family of natural biological entities that we study,
*  like the ecology, like a metabolic network, like a protein network.
*  There are neural networks and there's brain networks.
*  There are some commonalities here.
*  There's some differences, domain specific differences, of course.
*  So so it takes away the aura of mystery to some extent.
*  It says here's a here's a perspective that we can use.
*  It's productive. It allows us to understand
*  and explain phenomena better than we were able before.
*  When you say breakthrough, what does that mean?
*  I don't know. That's if we knew what it meant.
*  It's sort of like it's interesting sort of conundrum.
*  I'm not a philosopher, but, you know, if we knew what the what the critical
*  question was that we needed to ask to understand how the brain works,
*  then we would also have the answer, most likely at the same time.
*  Well, we can think of a breakthrough in physics, right?
*  Like general relativity made us fundamentally understand the universe
*  in a different way and be able to ask questions in a different way.
*  And maybe that's along the lines of what breakthrough means.
*  Of course, we don't know how what it would look like.
*  I mean, you know, I'm not a great predictor of the future, honestly.
*  But I and I say this very informally,
*  and I'm sure many listeners will disagree with with this.
*  I don't think neuroscience anywhere close to that at this point.
*  If you if you line up neuroscience and physics on a common time axis,
*  I think we are, you know, maybe we are somewhere in the 19th century right now.
*  Yeah. Yeah.
*  I was in our approaches were still pretty naive.
*  I include I talk about myself here was still pretty naive
*  when we look at the brain and we're still trying to figure out basic things
*  of how it's organized and how it's structured and what are the important things to
*  to to track?
*  How does dynamic activity unfold?
*  How is it related to behavior?
*  We're still, I think, very much at the at the beginning of that.
*  I agree with you. And that's frustrating.
*  It is. It is frustrating, but it's also part of a historical process.
*  You know, and of course, we want to push to the point where we have
*  something like relativity or quantum theory or some other construct
*  that really changes things and opens up new horizons
*  and lets us see things in different ways.
*  Those those days will come.
*  I don't know when.
*  I do believe that that having theory
*  and investing in theory and training students and postdocs
*  to learn about theory, not just computational modeling,
*  but actual theory is important in in making that
*  making that possible for the for the future.
*  So I think we're we're we're not we're not there yet.
*  I don't think that prognosis in itself will give us the answer.
*  I'm not, you know, I'm I'm I'm I think I'm sane enough to to not
*  claim that it's the answer to everything.
*  It isn't. But it's an important perspective
*  and one that that has certainly given me a lot of insight.
*  And I hope it has given other people insight to and it will grow
*  and perhaps link up with other parts of of interdisciplinary
*  complexity research in the future.
*  And then maybe we'll get closer to that ultimate goal of understanding
*  and sort of finding a theoretical framework that really fits.
*  Is there a flagship
*  results or advancement that network neuroscience has made thus far that
*  when you're when you're at a party and someone says,
*  what have you done for us?
*  These hold up.
*  You don't hold up small world network, right?
*  Small, small wellness got us started.
*  It was a historic almost historic artifact.
*  In fact, it was it was around in social sciences, at least since I think 70s.
*  So it wasn't really discovered in 90s.
*  It was kind of just popular in some ways
*  enshrined in this extremely simple and ingenious model
*  that Watson's book gets published.
*  No, there is a lot has happened since.
*  Well, I mean, where do I start?
*  I think there have been lots of advances.
*  First of all, the notion of undertaking
*  taking connectivity and interaction and making that the central
*  that that is really not the traditional way in which neuroscience has been conducted.
*  There are many historical precedents, of course, to
*  researchers, scientists studying connections and studying anatomy.
*  But it really came into the into its own in a new way
*  through this application of network methodology.
*  So the notion that, for instance, somewhat jokingly,
*  not all brain regions are created equal.
*  Now, of course, we've talked in the in cognitive neuroscience forever,
*  not forever, but for maybe for decades,
*  certainly about parts of the brain that are, you know, multimodal or polymodal
*  or association regions, regions that are engaged in more complex processes,
*  planning integration of sensory inputs across modalities, memory, et cetera.
*  And other regions are more peripheral, let's say, more engaged
*  and in sensory processing in a single modality.
*  Those distinctions are not as clean as they appear.
*  But nevertheless, that's been a framework that we've been working with in cognitive neuroscience forever.
*  And now we we suddenly have a way to
*  get to that distinction using network science methodology.
*  And that's the notion, let's say, of hubs, highly connected regions
*  with diverse connections that cross many boundaries
*  that that help to integrate information, many sources.
*  The notion that there's those kinds of cortical hubs, sub cortical hubs,
*  even neuronal hubs now have neurons that have more
*  that are more heavily connected, have more inputs, more outputs.
*  That certainly is something that people did not really consider that much
*  before all this took off.
*  We can now routinely identify those regions in neuroscience
*  data sets, whether they are dynamic or whether they are anatomical.
*  The notion of communities of network modules or communities
*  that allow us to group neurons and brain regions
*  according to their mutual affiliation,
*  they have a similarity in their activity patterns, their statistical dependencies.
*  That's a technical advance that allows us to
*  coarse grained the system.
*  I take a dimensional recording and map it down onto clusters
*  of elements that are mutually more connected internally
*  and less connected between.
*  That's a standard approach now in many neuroscience applications.
*  And it comes from from network science and complexity science.
*  That's a complex system is it has that coarse graining to it.
*  That's one of its hallmarks.
*  You know, Herbert Simon decades ago talked about
*  the near decomposability of complex systems.
*  And you actually applied that to organizational structures
*  in other such non-neuronal systems.
*  That near decomposability, the fact that you can break a system
*  down into components that are not totally separate,
*  but they are internally denser and more causally engaged internally
*  as opposed to between.
*  That's the hallmark of complexity.
*  And we find it in brain networks everywhere.
*  So these are all things that I think network science has contributed
*  to brain studies.
*  And we can now deploy these new ways of looking at the brain
*  also in very concrete clinical applications.
*  You know, a lot of interest in human neuroscience is directed
*  at understanding the origin of brain disorders
*  and those network science tools and techniques have made a difference
*  in allowing us to look at features of the brain from a very different
*  perspective, looking at individual variations among people
*  with and without conditions, different developmental stages
*  across the lifespan in relation to genetic markers.
*  This is all now made possible because of the network neuroscience approach.
*  Yeah, that's great.
*  So there are a lot of complex systems, a lot of networks in the universe.
*  If we step outside, so, you know, in a couple of minutes, I want to talk.
*  We're going to dive deeper into the actual brain and talk about
*  the different perspectives and contributions of network science.
*  But stepping out of brains for a second, you know, is there something unique
*  about brains? You're just talking about the hub structure and,
*  you know, the different structures that are sort of hallmarks
*  of complex systems.
*  But is there something different about brains that just jumps out
*  in the network sense relative to other known complex systems?
*  Well, I guess many aspects of of how nervous systems are structured,
*  how they're how they're built and are not shared by other
*  by other complex networks out there.
*  I mean, the big contrast I sometimes draw on my classes
*  between social networks, let's say Facebook, Twitter, what have you,
*  and the brain. One of the unique aspects of the brain is
*  seems like a very trivial observation.
*  It's a physical system.
*  It's actually, you know, I have one right between my ears.
*  As I talk to you, it occupies, you know, what, you know, whatever,
*  1300 mils of volume.
*  And and I have to power it.
*  I have to eat, you know, I have to take in food
*  so that I can keep making ATP and keep that thing running
*  because it takes up 20 percent of my energy budget,
*  even though it's only two percent of my body.
*  And that's efficient. And that's efficient. Yeah.
*  So those those fundamental facts about
*  about the brain are I mean, these are really fundamental facts.
*  I'm really not joking here.
*  I I feel like that is where brain networks and other networks really diverge.
*  Social network, you know,
*  certain people on Twitter can have 80 million followers, apparently.
*  And there's no cost attached to that.
*  Those links can be made, you know, at infinite.
*  But in the brain, it being a physical system,
*  any kind, any physical connection, any synaptic connection,
*  any axon that is made takes up volume.
*  And every axon, every connection is in a sense, a little cylinder
*  that has a light diameter radius and a length and an extension.
*  And for it to be there, it has to nibble at a limited resource.
*  And that's volume.
*  That fundamental point was made, understood and written down by Ramonica
*  Hall, our, you know, granddaddy, if you wish, granddaddy,
*  the grandfather of neuroscience in general.
*  He wrote about this, understood that fact and thought that it was a driving factor
*  in making neurons the way they look,
*  driving morphology of neurons and the diversity of morphological types that he saw.
*  So brain is physical.
*  Any connection you want to make for the connection takes up
*  volume and space that sets up a competition.
*  You know, that sets up a an economic contest, a trade off
*  between having the connection and making that investment in it
*  versus not having it.
*  And so our connectivity, the actual physical network
*  that we carry between our two ears is shaped by that.
*  I strongly believe it's shaped by that
*  ongoing competition of, you know, can I afford that connection?
*  What is the value of that connection in terms of making the brain perform better
*  in terms of, you know, guiding adaptive behavior and and and and promoting survival
*  versus energy consumption, energy needs.
*  And so the so the brain has a very peculiar structure to it,
*  in part because it has to negotiate that trade off.
*  It has to be functional.
*  It has to be adaptive.
*  It has to support the organism that it's residing in.
*  But it also has to be economical. It has to be cheap.
*  That's not something that I ever really felt like I needed to think of when I was,
*  you know, recording neurons in the frontal eye field, for instance,
*  while monkeys made eye movements.
*  You don't really think about that at all.
*  And in fact, I think it's highly underappreciated in general,
*  which is maybe what you're saying.
*  I don't know. Yeah, it's yeah, it's still I mean, I think it's
*  it's become more appreciated last few years in neuroscience.
*  And then there have been actually a number of really important thinkers
*  and theoreticians and people who have studied this over the years.
*  So this is not an entirely new idea, obviously, the people who have worked on this.
*  But it is something that sets apart the brain from, let's say, a social network
*  or the Internet or other such constructs that perhaps we can
*  conceptualize as complex networks out there because there is that cost element to it
*  and that link to evolution,
*  which, you know, as an evolutionary theorist once said,
*  nothing in biology makes sense except a lot of evolution.
*  And you would swap out biology and say neuroscience, you know,
*  and I sort of subscribe to that.
*  We have to remind ourselves that we are historical artifacts, right?
*  There's a particular history that unfolded.
*  And and here we are.
*  And there are sort of non accidental elements to that history.
*  There are things that have to happen for for intelligence to to emerge.
*  I do believe that.
*  But our brains are also subject to severe energy, volume,
*  space, wiring constraints.
*  So the process cannot go unchecked.
*  And so in that sense, I suspect our brains are actually, along some dimensions,
*  quite suboptimal.
*  That's interesting, because I was going to say it makes a connection
*  to the free energy principle of Carl Fiston, whom you mentioned earlier.
*  And, you know, trying to lower the, you know, in a sense,
*  that is a energy minimization, efficiency maximization theory, in a sense.
*  And not that we need to talk about the free energy principle, but
*  but the brain and the Internet are basically the same thing, right?
*  The Internet's just a big brain, right?
*  It's conscious. Oh, no.
*  Trying to pull my chain. No, no, no, no, no, no, no.
*  I don't buy that at all.
*  In fact, I don't buy and I'm I'm I'm I'm sure you are you are going to get there.
*  I'm sorry. I'll take the question out of your mouth.
*  Basically, it's also not very much very similar to what we what we now see
*  in artificial neural networks and people running.
*  And and, you know, all of those kinds of things that are out there now.
*  Very, very successful rebirth in some ways of the artificial neural network field
*  that I remember was just, you know, emerging when I was a graduate student
*  in sort of mid 80s and was very exciting.
*  And now it's it's blossoming.
*  It's it's all around us.
*  And it's of great interest to many people as many applications and and and many
*  very successful demonstrations of its power, where I feel there's a there's
*  a divergence here is that, you know, none of the architectures that are used in
*  implemented and deep learning networks are subject to to to a lot of these
*  constraints I've just mentioned. Right.
*  You can make you can you can make an N square fully connected network.
*  Sure. Make a network that's randomly connected.
*  Sure. You can do that in the real world in terms of a system that you want to build
*  and put into a living organism. You cannot do it.
*  It will it will be too wasteful in terms of volume and energy.
*  So those those brains that were in a sort of the random brain cannot exist
*  or the fully connected brain cannot exist.
*  It's not even worth thinking about it as a potential null model or a potential sort
*  of alternate reality, because it isn't it isn't possible to build.
*  We are stuck with the architectures that we have in a particular space
*  of what you might call sort of the space of all possible networks.
*  And in that niche, that's where we are.
*  And whatever intelligence and adaptive behavior we can squeeze out of that niche.
*  That's what we've that's what we've got.
*  There are certain things we will never be able to do with the brains that we have.
*  Yeah, I was going to ask about this later, but let's go and explore it a little bit
*  further since since you mentioned it.
*  I mean, first of all, you know, deep learning networks don't need to be
*  constrained by any architectural constraints.
*  Right. And therefore you could say that people do consider architecture because,
*  you know, in a convolutional neural network, let's say, you know, you're constraining
*  operations to parts of the spatial world and convolving the inputs.
*  And, you know, in the latest, let's say, Jim DeCarlo's lab, I just talked to Jim DeCarlo
*  and his models that map onto brain hierarchical brain areas that in some very loose
*  sense is true to architecture and maybe the loosest sense.
*  So, I mean, do you do you think that the AI world needs to pay more attention to
*  architecture? Is there something fundamental about our architecture, which has been
*  shaped to give rise to our to whatever intelligence we have and all across all animal
*  species? There's always some constraint.
*  Is there something fundamental about that architectural constraint that is actually
*  generative, you know, that is a cognitively good thing?
*  Or can we just expand, you know, and make bigger and better fully connected models and
*  somehow optimize even better than, you know, you just said earlier that we're in a
*  great sense suboptimal, which I agree with.
*  So we could optimize beyond us.
*  Right. Sure.
*  That's about seven questions.
*  Sorry. That's seven questions.
*  So how do I how do I even begin to say this?
*  First of all, just to make that clear, I'm really not an AI researcher.
*  I I have I know I'm an outsider to that field.
*  I look in from from the neural network angle sometimes and I cheer I cheer on my my
*  colleagues in AI. I think what they're doing is really changing the way we we interact
*  with data with the world at large.
*  It's great stuff. It's just the comparison between, you know, real brains of the kind
*  that I study, real nervous systems and and AI seems flawed to me.
*  It's it's it's I'm actually not.
*  So let's break it down.
*  So let's say what is another analogy here that is similar, right?
*  Let's take airplanes.
*  Let's take a jet a jet plane on the one side and a bird on the other side.
*  OK, OK. Nobody's advocating that planes ought to be built exactly as birds are built.
*  That would be that would bring air travel to a halt even faster than Covid-19.
*  OK, there would be there would be that that wouldn't work.
*  OK, so what's common between the two
*  between a jet plane and a bird is that they're somehow using similar laws of aerodynamics
*  and and and you know, they both fly but in very different ways.
*  And and planes can do things that birds can never do.
*  And and that's that's fine.
*  OK, and but birds also do things that brains never do.
*  They can land and take off on a spot.
*  I, you know, like many other people who are stuck at home currently,
*  I look out my window a lot more and I see birds doing stuff, you know,
*  and it's entertaining and you kind of appreciate how
*  incredibly versatile and adaptive biological organs can be
*  how they can navigate their environment in ways that,
*  you know, a plane certainly would not would not do so.
*  So planes are more like AI systems.
*  They are built to accomplish particular tasks that a natural biological
*  similar perhaps cannot accomplish.
*  And they do so much better.
*  And they're powerful.
*  They extend our abilities as humans allow us to connect, allow us to get to places.
*  This is good.
*  On the other hand, if you are interested in broad flight,
*  as if that's your scientific interest, you probably want to study birds.
*  You know, you don't want to study planes. Yeah.
*  Not necessarily. But but, you know, and also perhaps there is room for
*  this connects to my old interest in robotics to build
*  to build machines that are a little bit more like birds. Right.
*  You know, that a bit more like insects or or a small, small flying creatures
*  that are much more able to navigate in an enclosed space, perhaps slower,
*  but can gather sensory information or, you know, whatever.
*  So there's there's a an active field of sort of bionics and biological robotics.
*  So biome medics, as it used to be called.
*  And that's that's technology.
*  It's not building airplanes, but it's trying to build something
*  that is more like a bird or an insect and learn from that.
*  And so that's your research goal.
*  If that's your application, then, of course, you would pay more attention to birds.
*  Would an apt analogy here be in the A.I. world?
*  So to the airplane versus bird,
*  our current computer vision, right?
*  It's like saying, oh, we so airplane versus bird airplane.
*  We solved flight and without understanding feathers.
*  So computer vision, we solved vision without understanding the brain.
*  Is that the apt analogy?
*  Because that's a ridiculous statement, right?
*  With that, we it's vision, but it isn't.
*  I mean, it's it's it's vision for technological purposes.
*  It's pattern recognition, maybe it's automatic surveillance,
*  whatever the application may be, or it's it's, you know,
*  recognizing features and medical images.
*  This is all of these important applications.
*  And I don't think it makes sense to really, you know,
*  to reengineer a human brain to accomplish those tasks.
*  Let's do what we can do with with machine vision
*  and A.I. and deep learning applications in that in that problem space.
*  Vision, biological vision is not it's not just that right.
*  Right. For one thing, again, I'm connecting to my old
*  area of robotics, which has taught me a lot.
*  For one thing, I think of vision as an active process. OK.
*  I move my eyes around all the time.
*  I'm not aware of it that much.
*  But the image that I have seemingly stable in my head
*  is actually moving across my retina at a fairly high speed.
*  And and I have to do that because otherwise I wouldn't be able to build a,
*  you know, any representation of my external world.
*  And so biological systems are not like the eye is not a camera.
*  That sits on top of my computer right now looking at me.
*  Biological visual systems are active.
*  They they engage in in their own motor activity
*  to to generate and create information and sample information from the environment,
*  which then in turn is fed to the brain. Right.
*  Which is faced with a constantly changing input pattern that it now kind of
*  builds up into this, you know, seemingly stable mental image that I have
*  that I can operate on.
*  And so that's, you know, that's
*  most machine vision systems aren't designed that way.
*  And for good reason, they are not supposed to solve those kinds of problems.
*  And there's other technological solutions for for getting images
*  and then then have that now. Right.
*  So I mentioned it because it's a flawed analogy.
*  The bird airplane is a flawed analogy, and I'm wondering if it maps on
*  mapped on perfectly.
*  So we're thinking along the same same sorts of lines anyway.
*  Yeah. So I did ask seven questions there.
*  I'll just remind you because I totally got us off track.
*  So one of the questions, you know, well, you mentioned that you have to have
*  the brain inside your skull.
*  Now, a robot or a device does have to have, let's say,
*  an AI system in a physical space as well.
*  So that provides some constraints.
*  What not necessarily mean the fund of some of the robots to be built early,
*  you know, 20 years ago actually had a remote, you know, even at
*  even 20 years ago, 25 years ago, sort of had a remote link to a workstation
*  or a machine that was not carried on board, but
*  to which, you know, sensory input would be sent and then that's where the brain was.
*  And then outputs would be sent to the effectors of of the robot.
*  So I think you can to some extent circumvent that with a with a with a machine
*  that's operating in the real world.
*  But where the machine where such a robot has that has constraints to deal with
*  is the nature of the sensory input, its own motor capabilities
*  and its own time course that goes with that of moving around in an environment
*  that cannot happen at a nanosecond scale.
*  That has to happen, you know, in at a similar time scale as as as
*  say, biological organisms do do that.
*  So those constraints apply.
*  But but you can actually off off board the processing and have a deep net
*  sitting somewhere probably.
*  And that that does all of that.
*  So there's this sort of I'm sort of kind of advocate kind of a pluralist here.
*  Right. There is a eye on one side.
*  It has its own agenda and its own goals and aims.
*  And and that's perfectly good.
*  And then there's neuroscience, which has its own agenda to and goals and aims.
*  They don't necessarily match up perfectly, I don't think.
*  So I would not advocate that I must pay attention to how the brain works.
*  I think it can be very mutually informative.
*  We can learn from each other a lot.
*  But I I think that some of the
*  the biological constraints that brains operate under that we mentioned already,
*  like space and energy and so forth and and his history,
*  you know, having millions of years, billions of years of history behind us.
*  Those don't apply to AI.
*  And and so it's it's a it's a flawed comparison
*  between the two and double.
*  But there will be a gray zone in between where perhaps bio-mimetic robotics,
*  you know, some engineering applications will look more organism and brain like
*  and perhaps also drawn AI advances.
*  So there's going to be a spectrum of things here.
*  So I mean, you had mentioned and I reminded us that you had mentioned
*  that the brain is suboptimal.
*  And then and then I asked, well, OK, so if you take away the constraints,
*  could we potentially exceed the brain's level of optimality?
*  And I'm not sure if optimality is the right
*  because there's a value or there's a there's a judgment in that in the word
*  optimality. But so I'll go ahead and just ask the question anyway.
*  You know, could we exceed the quote unquote optimality then since the brain
*  since, you know, hardware, physical hardware, not wetware,
*  isn't restricted to those constraints?
*  Yeah, we have we have actually tried to address the issue in a simulation context
*  here in my lab last few years, sort of
*  coming up with a concept that we call network morphospace,
*  which is a space of morphologies or topologies, in this case
*  of networks where our brains, it's in a particular part of that space.
*  And so and around it are possible brains that perhaps are wired somewhat differently.
*  And configured a little bit differently.
*  And now the question is, are those better,
*  quote better along some dimension of performance?
*  OK, and the dimensions that we picked
*  of performance to actually study have to do with communication.
*  And it seems that one
*  important aspect of brain function is that neurons can communicate with each other
*  and through that communication process can influence each other's activity patterns
*  and sort of probabilistic response functions and so forth.
*  And in the in the brain at large, what we what we have to accomplish
*  that that job is external pathways or fiber tracks that connect,
*  let's say, remote brain regions with each other.
*  They're laid out in a certain pattern.
*  We more or less have the same pattern.
*  All of us have to do with development and evolution once again in genetics.
*  And the question that arises is that pattern optimally configured
*  to facilitate communication across the brain
*  like a like a perfectly well laid out highway system, you know,
*  where all cities can communicate with each other along sort of,
*  you know, very direct paths.
*  Or is there a way to improve upon it by rewiring or by adding connections
*  or perhaps even by subtracting connections?
*  What does that look like?
*  So we can't make the experiment in real life.
*  You know, obviously, we can't do that yet.
*  Not now. Yet.
*  But that yet will be a long, you know, doubt.
*  Yeah. But what we can do, I will say, is we can study evolutionary relationships
*  among different species.
*  And that is something that we also have done and are doing in the lab here
*  to look at different mammalian species, for example, and compare
*  connection patterns to see if there's any evolutionary trends.
*  But we can't run an experiment on this.
*  What we can do is we can try to do a computational experiment
*  so we can implement a brain network in a computer.
*  We can we can simulate its activity or communication patterns.
*  And then we can modify the structure of that network, the underlying anatomy.
*  And we can study again, is it doing is it working any better now?
*  OK, and so that that's a theoretical exercise to sort of navigate
*  that morphospace and see if we are we on top of a hill, you know,
*  where we're optimal.
*  Any step we take in any direction gets us to our space.
*  Or are we are we on a on an incline?
*  And it's really hard to to to climb up the up the hill.
*  And, you know, so that's those are the kinds of things that we have been doing,
*  have been trying to do is communication the right metric to use?
*  I'm not sure.
*  But in that in that method, we are on a hill, essentially, correct?
*  It is the case that it's very hard to find a close
*  rewiring that is doing any better than what and what we have.
*  Yeah. But but but here's a tricky aspect of this question.
*  And that is what is the mod?
*  What is your how do you define communication? OK.
*  And this gets us into the whole interesting
*  scenario of what we call communication dynamics,
*  which is very much a problem that resides in the intersection
*  of networks on one side and dynamics on the other.
*  You know, think of a brain network as a fairly sparse
*  network of connections among neurons, let's say, you know, in fact,
*  if we if we roll the numbers of all neurons in the brain,
*  I think roughly about one in one in a million of all neuron pairs
*  have a direct connection with each other.
*  The rest are not directly connected.
*  So they have to if they if there's any chance of them interacting at all,
*  they need to do so through intermediate steps.
*  So what does how does communication look like in such a network?
*  Is it unfolding along some
*  preferred route, for instance?
*  The shortest path is often used in network science
*  as a way of navigating a network to go from place A to place B
*  to so in the fewest number of steps. Right.
*  If you want to send up a package from from from here to some other city,
*  you hope that FedEx, you know, uses something close to the shortest path.
*  Otherwise, that package will rumble around for years.
*  I'm still waiting on the shoes that I ordered. Yeah.
*  So, you know, now in in in this context, I just mentioned, you know, shipping
*  or or or communication of goods in a real world network like this.
*  Of course, FedEx does not just send out packages at random,
*  hoping that they arrive at the destination at some point.
*  That's a diffusion process. OK, very wasteful.
*  But what's good about it is you don't have any.
*  You don't need any information to do it.
*  You just send out you just broadcast, you send out your packages
*  and some of them arrive and some some will take a million years to arrive.
*  That's, however, not the way most people think about brain communication.
*  They think that's the shortest path that's being used.
*  It's a direct way of two brain regions, two neurons,
*  if they need to connect to each other.
*  Sets up an important problem because the shortest path
*  can't be discerned, can't be plotted, can't be found
*  without some global knowledge of the network. Yeah.
*  But when you when you come to a new city and you and you and you step onto a subway
*  station and you look for what's my I want to get to the other end of the city,
*  you look at the plan, you look at the subway routes, the way they are laid out
*  and you have a way of plotting to go from A to B in, you know,
*  hopefully a relatively short number of steps.
*  So you'd have to have a perfect model of the structure of your your brain.
*  We need a perfect model of its own structure.
*  But neurons don't have that knowledge and brain regions don't have that knowledge.
*  There's no global map built into the brain that guides communication
*  and kind of routes communication patterns.
*  So the shortest path concept, in my view, is a little suspect
*  when it's when we apply it to the brain.
*  It's at least it needs it needs to be a discussion
*  as to how a brain network might access a shortest path.
*  And that's a nontribular problem.
*  If you don't have that global top down knowledge of how your connections are laid out.
*  So that's it's a big open area right now.
*  I'm I'm sort of excited about it because I think communication
*  is a key neuroscience question that we may ask about how our brain networks,
*  how neurons, how elements in a brain network communicate with each other
*  is an open question.
*  And I feel like it's been understudied.
*  We have been focused on recording from individual neurons or brain regions.
*  But remember, those recordings do not directly capture communication patterns.
*  They only capture the outcome of those communication patterns.
*  The fact that neurons change their firing rates or response properties,
*  the fact that brain regions, you know, both signals go up or go down.
*  That is the consequence of interactions that themselves are very hard to track.
*  So let's just jump in and dive deeper on communication dynamics then.
*  There's a really nice review that you and your colleagues have written recently about this,
*  talking about how it might be the key to bridging the connectome,
*  the structural parts of the brain with what's called functional connectivity.
*  And I'm not sure if we've even defined functional connectivity yet,
*  but maybe you can make the distinction between those two.
*  Yeah, that's a really important distinction to make.
*  And it's often forgotten even by practitioners in the field.
*  On the one side, the connectome, the way we originally proposed it 15 years ago,
*  the connectome was meant to be about structure.
*  It was meant to be a wiring diagram.
*  It was meant to be a complete list of all the connections
*  and the elements and how they're connected.
*  Sort of a top-down map.
*  It's a subway map, really, of how things are connected and at a given level of scale.
*  Single neuron seemed intractable back then and still is fairly intractable, I would say.
*  But whole brain regions, that's tractable now.
*  And that was sort of the level that we aimed at as a first shot.
*  So that's anatomy.
*  OK, but, you know, to some people in neuroscience, the anatomy is boring.
*  Boring. That's right.
*  It just sits there.
*  What? You know, that's not really what the brain is doing.
*  Not to you, though. You're an anatomy kind of guy, right?
*  I'm joking. OK.
*  I remember a time, you know, 20 years ago, I was in anatomy always.
*  But anatomy was not a hot area in neuroscience
*  during that time, and also a couple of decades ago.
*  I think it's gotten a lot more attention again.
*  And I'm really glad about it because it is the foundation of our field.
*  Look at Cajal, OK?
*  He has his incredible insights
*  where many of them came from him considering morphology of neurons
*  and how they're connected.
*  So that's anatomy.
*  On the other side, we have functional connectivity.
*  So what is that? Oh, boy.
*  OK, now we're getting into the into a discussion here.
*  So abstractly speaking, if you have two elements of a complex system
*  and let's say these two elements engage in activity of some kind,
*  voltage going up, voltage going down, spikes happening, what have you.
*  What you can now do is you can construct
*  a measure of statistical dependence between them.
*  How much does the state of one element tell you about the state of the other?
*  It's another way of saying it.
*  If one element goes up, does the other one reliably go up as well?
*  Or does it go down or does it do whatever?
*  And I can't predict what what it's doing.
*  There's many different ways of measuring this cross correlation being
*  the simplest one.
*  You just take two time courses and you cross correlate.
*  And if they're highly correlated, either positive or negatively,
*  then you have information from, you know, just shared information between them.
*  And you can do information theoretic measures.
*  You can do other stuff.
*  So it's a very simple
*  statement about statistical dependence.
*  It does not, generally speaking, does not imply causal interaction
*  and should not. OK, functional connectivity is purely an observational
*  construct that says two things seem to be statistically related or not.
*  You cannot infer from that, typically speaking, that they are also causing
*  each other to be statistically related.
*  You can't even infer that they're structurally connected, correct?
*  No, you cannot.
*  Structural connections are much, much sparser.
*  Statistical dependencies, I can I can usually get a non zero value
*  for any observation of the pair that I can take any neuron, any two neurons
*  in the brain and and define some coefficient of how much relationship
*  there is in terms of their spike trains or their bold activity patterns.
*  I can do that.
*  But I also know that I mentioned, you know, at the neuronal level,
*  only one in a million of those neuronal pairs will actually have a structural
*  connection, a direct connection.
*  OK, so this is where it gets tricky, though, because let's stay
*  at the whole brain level for the moment.
*  Let's say we have two, three, four hundred brain regions.
*  Sort of a good number that we work with, typically.
*  In our day to day work these days.
*  The structural connectivity in terms of the pathways,
*  the white matter pathways that connect these remote brain regions.
*  It may have a density of five, 10, 15, maybe 20 percent.
*  So it's much denser than individual neurons,
*  but it's certainly not a fully connected network.
*  At the level of functional connectivity,
*  if I do something like cross correlation or mutual information
*  of activity traces at the whole brain level, that's always a full matrix.
*  Because all pairs of regions have some level of relatedness.
*  At some level of similarity, even if it's near zero,
*  of how their activity levels vary across time.
*  So you have to threshold it.
*  So you either threshold or you build.
*  And we've done this in years past.
*  Or you try to model the
*  in the functional connectivity between brain regions
*  that are not structurally connected and understand them as a consequence
*  of multiple indirect paths.
*  Because remember, for for two sites to influence each other,
*  it doesn't have to be direct.
*  It can also be, you know, a connects to B connects to C.
*  What happens a lot, especially at the whole brain level,
*  with the kinds of signals we get in MRI is that there will be ultimately
*  a correlation between A and C, even though A and C are not directly
*  structurally connected because there is what we call transitivity.
*  There's sort of like correlations kind of propagate outward
*  and closure ultimately, because the outer ends of such a chain tend to tend
*  to share some variance.
*  They tend to be connected in that functional sense.
*  Now, that is a totally really simple fact.
*  Unfortunately, a lot of, you know, there have been recently
*  a lot of criticism of functional connectivity, which I think is slightly
*  misguided because I don't think functional connectivity really aims
*  at establishing or portraying causality.
*  It should not anyways.
*  But you have terms like Granger causality and things like that.
*  Granger causality is that it's a different site, different construct
*  related to transfer entropy and other information theoretic measures
*  that tries to kind of infer a particular type of causality,
*  which says the future state or evolution of an element
*  is better predicted by taking into account the past states of another element.
*  So you have if you have you have an element A and you want to predict
*  how what is the next state of A, you know, a second or a minute down down the road.
*  You can use its own history to do that.
*  But you do better if you take into account the past states
*  of another element somewhere and that improves your prediction.
*  In that sense, you say that element, that other element is causally engaged
*  in molding or shaping the future states of A.
*  And in that sense, am I going to ascribe a causal influence?
*  That is a variant, I think, of functional connectivity
*  that still is based on observation, still still still is based on time series
*  analysis, still is based on temporal precedence cues
*  that we often use to infer causality.
*  But it is not a direct portrait of causal of causal interaction either.
*  In fact, causality is very hard to get to.
*  It's it's it's it's a word that rolls off the tongue very nicely,
*  has a lot of appeal to it.
*  But boy, it's definitely not easy to get to, especially when you
*  when you're in an observational context and you really can't intervene
*  or make perturbations as we often we're not we can't do that in human
*  brain imaging very, very easily, at least.
*  So we kind of we have, you know, of course, there's ways of
*  trying to use models to infer causal so-called effective connectivity,
*  which is, I think, a very interesting way of doing it.
*  And some of my my old colleague, Cal Friston, in the lead,
*  have done this for many years.
*  And it turns out that that's also not totally straightforward.
*  It's actually a hard process because you have to identify a
*  a generative model, essentially, of your data that is
*  parsimonious, simple as possible, generates, essentially generates
*  data that match what you have observed on the basis of a structural
*  and physiological model that's built into it.
*  And that's a difficult process of model selection and inference
*  that takes up a lot of, you know, a lot of computing and thinking and so forth.
*  Great way of doing things, unfortunately, doesn't scale very well.
*  If you go to more than, you know, a dozen or so elements
*  or brain regions, the model spaces become so large that you can't
*  see it. You just cannot effectively handle it anymore.
*  So that process of inference, inferring a causal interaction from observed
*  from observations is very difficult.
*  Notories are difficult, especially difficult in the case of a system
*  that's so high dimensional, so fine grained and so interconnected as the brain.
*  And we have to just be honest about it.
*  It's not an easy process.
*  Functional connectivity does not give us that.
*  But but I will say it does.
*  It's not nothing. It does have lawful relationships to structural connectivity.
*  Some of them are fairly robust.
*  And it it tells us something about
*  the similarity of firing patterns or activity patterns across the brain.
*  And that's given rise in our field to a whole new way of breaking down the brain
*  into systems internally coherent because they share time course similarity
*  and externally diverse and different.
*  And there's a huge literature of showing how these systems
*  relate to activation, cognitive activations, when people do tasks, to anatomy.
*  And even to other data domains like genetics and develop.
*  So it's been very productive in many ways, but it's not it's not meant to be.
*  And it can't really aspire to be a causal
*  a framework in itself.
*  David Hume is just laughing in his grave right now.
*  Well, I don't know if that covers functional connectivity well enough,
*  but I want to bring in the communication dynamics story.
*  So on the one hand, you have structural connectivity.
*  On the other hand, you have the functional connectivity.
*  And sort of between these two is communication dynamics.
*  How does it sit between structural and functional connectivity?
*  I see it. I see communication with dynamics as kind of the missing link
*  that that allows us to bridge
*  between fairly static, although also changing across time.
*  And anatomy.
*  On the one side, sparse connectivity, that structural and physical and real.
*  On the other side, this is the statistical descriptions
*  based on dependencies really across time courses, which are non-causal
*  underneath it all and partly invisible to us at this point
*  is that process of signaling and communication that occurs
*  neurons in our heads right now are firing furiously.
*  And as a result of that activity,
*  impulses are being sent along axons
*  that impact on their targets, changing their status, their state,
*  their firing pattern subtly or very dramatically.
*  And these communication events of elements in our brains
*  currently communicating with each other at furious speed and a very high rate.
*  That is something that I would contend we cannot directly observe right now.
*  What we can observe is we can record from neurons. Yes, we can record spikes.
*  Yes, but the spikes are recorded locally.
*  They are sort of what a point source is doing at this point in time.
*  But we don't really see the interaction.
*  We don't see the even if we have perfect knowledge of all neurons all the time,
*  we still don't see which connections are active or inactive.
*  Sort of the pathway that information flows.
*  So I'm really thinking of it as a as a flow, as a rapid fire
*  exchange of directed signals that run down physical
*  synaptic pathways, axons, et cetera,
*  that we can't directly observe.
*  That to me is a causal substrate.
*  That to me is like those are the causes
*  of the firing patterns that we then observe of the sent out
*  the ball signal of the changes in activity and activity weight and firing
*  spike timings that we see in signal neurons.
*  The information flow, information flow, right?
*  And so, you know, that's that's a there's a gap here,
*  I think, methodologically in terms of technology, not being able to really
*  visualize this very well yet.
*  It requires typically a process of inference to infer those interactions.
*  This gets us back up.
*  Just previous point about causality and how hard that is to infer
*  if we don't see it directly.
*  And and it is something missing link.
*  And I I have never actually talked with Carl about this,
*  and I hope I'm not doing
*  damage to his to his to his framework.
*  Yeah, but I but I but I do think of it in some ways as a as one way of
*  conceptualizing effective connectivity.
*  Uh huh. Because it is the blow by blow account of which neurons,
*  which brain regions causally affect each other through that communication process.
*  It's going to be a very dynamic construct going to happen.
*  It's not going to be something that is static over any period of time.
*  It's going to be sort of like a like a, you know,
*  think of it like a bunch of flashes of light that occur
*  almost instantaneously change a target's behavior.
*  And then that target, in turn, sends out a signal or not.
*  And that propagates to through the network like a like a like a like a wave
*  or a cascade. OK, I feel like that is where technologically
*  we don't have very good tools to see that directly.
*  And methodologically, the inference is very hard to do.
*  But it is the level that I feel is most closely related to effective connectivity
*  that we would really like to have.
*  And it's so it's a it's a it's a gap in our knowledge, understanding.
*  And I think that would close the gap between the sort of static sparse
*  anatomy on one side and the statistical dependencies,
*  which are non causal, however, on the other side, function of activity.
*  And you also think of it as I'm not sure if this is in the same vein
*  as you were just talking about causally, but as at the.
*  Communication dynamics level, being able to gate information flow
*  is that on a causal level as well and and allow either allow information flow
*  to information to flow easier or gate it.
*  And so it in itself can serve as a way for the brain
*  to integrate and segregate information.
*  Is that right? Yes, absolutely.
*  Very good point you're making here.
*  So we should not think of
*  of these. I don't think of these communication patterns as something
*  that sort of, you know, all communication channels are open all the time.
*  That that that can't be that doesn't sound right to me.
*  I do think that just as you said that there is a way for
*  for for brain, but for the brain itself, perhaps
*  for modulatory systems, etc.
*  to open and close communication channels selectively.
*  Perhaps this is in the end the way that the navigation problem is solved.
*  You know, like the problem we mentioned earlier about accessing the shortest path.
*  Maybe there's a way for past to open and close
*  in a way that allows information to flow one way and not the other
*  and carve out sort of a structure where, you know,
*  certain communication patterns are more privileged,
*  are more frequent, are more abundant, while others are shut out completely.
*  You know, this is something where I'm hoping this is one of my next.
*  Well, I want to undertake in the next months and years, maybe to
*  to get away a little bit from these from these communication models
*  that treat the brain as if it's a gas, you know, where everything is happening
*  all at once and more of a of a system where, you know,
*  certain brain regions, certain elements of the system really aren't meant
*  to communicate, but others are communicating much more frequently,
*  much more readily. And what are the mechanisms
*  and what are the network mechanisms that allow that to happen?
*  And so that's actually one of our next, you know, ideas for projects
*  down the road a few months or so to get back communication
*  and actually look exactly at this.
*  Like you said, you can't measure the communication dynamics directly.
*  So you have to build models.
*  Can you just talk about how you, you know, just briefly how you build models?
*  I mean, you give kind of a two step process.
*  I mean, one thing that you've done that, you know, for instance, right now,
*  we're working with spiking neuron data,
*  data where neurons have been recorded from in a setting
*  where we have access to that individual spiking activity.
*  So how do we infer that communication process?
*  We do things like transfer entropy, which is sort of a more general version
*  of what you mentioned earlier, stranger causality, a way of inferring
*  causal interactions based on criteria.
*  Let's say whether a, you know, whether a
*  another neuron spike train adds information about the future
*  of a neuron that you're looking at.
*  Increases or decreases entropy, in other words.
*  Yeah, exactly.
*  So that results in networks where we have pairwise interactions,
*  directed interactions, actually, that are inferences on,
*  presumably on causal dependencies.
*  We get at that direct, we get an we get an arrow
*  that points in one direction between any pair of neurons.
*  And the arrow has a weight, sometimes it's zero.
*  Now there's no no evidence of any causal interaction at all.
*  And sometimes it's bigger than zero.
*  So we have some evidence that based on the spike trains,
*  that there is a greater causal influence between going from one direction to the other.
*  So that's one way that we can infer.
*  Make sure we try to infer those processes.
*  But there's big problems here because the information theoretic measure
*  transfer entropy, it requires quite a lot of data to actually actually stabilize.
*  And so we can't get to the blow by blow, you know, millisecond
*  to millisecond account of which we have to take a lot of data
*  and sort of smush it together and say, on average, how do neurons interact?
*  Same conundrum in in whole brain FMI recordings
*  where we have time courses, you know, sampled usually at excruciatingly
*  low rates, you know, of like once a second, if we're really good
*  and often two or three seconds apart.
*  And and that those are noisy measurements and and have have have issues
*  kept to do with the with the imaging process itself.
*  And we typically infer interactions
*  based on many minutes of data, many dozens of observations,
*  hundreds of observations sometimes that all get put together
*  into a single matrix of functional connectivity.
*  But what we don't yet have is a more fine grained account
*  of what happens that second, the next second, the next second.
*  We don't have we are working on this now with my my colleagues here at IU.
*  We're about to put some papers out there that that
*  try to address that issue in FMI recording specifically.
*  But but it's still a sort of unsolved problem.
*  We don't have that blow by blow account of communication.
*  We have an overall picture of dependencies.
*  And then sometimes the way of inferring the spike trains direction.
*  But we're not, you know, we're not directly observing or even inferring
*  that, you know, fast dynamic that must occur, must occur.
*  But we can't. It's difficult to see.
*  And so this is this is to me, you know, in the last remaining,
*  you know, who knows how many years I've got left
*  as I'm nearing my expiration date, I'm hoping to make some progress
*  along those lines and then exit the stage and give it to the younger,
*  generation. Raise your arms in triumph as you expect.
*  Well, Olaf, let's see.
*  There's a handful of questions I still have for you if in these remaining moments.
*  Is there anything that we need to add to communication dynamics to to wrap up?
*  No, I think we've touched upon it.
*  It's an open topic, right?
*  And and one that when we hold the review a couple of years ago,
*  one of the impulses to do that was to kind of raise the question
*  and bring the topic out there because I feel it's been underappreciated.
*  Yeah. Well, that's I mean, you know, the network neuroscience comes around.
*  There's, you know, the structural stuff.
*  And we all know about functional connectivity.
*  It's like, oh, now we have this to do.
*  There's always, you know, a new set of problems to deal with.
*  It keeps us busy, you know.
*  Sure. It gets boring if there isn't something new now and then.
*  So going back to, you know, the brain versus other complex networks.
*  So we have the connectome for a lot of different species now.
*  And you kind of go through them in your talks sometimes.
*  I don't think I've heard you talk about the human brain relative to other species.
*  Is there anything that we know about the human brain?
*  Because we're so special, you know, is there is there anything
*  anything in the network neuroscience world that jumps out
*  that is unique about human brains relative to other species at this stage?
*  Yeah, it's a good question.
*  A couple of years ago, I went to a meeting that title of the meeting,
*  actually, I think was what makes us human.
*  They were bringing in people from different
*  neurobiological perspectives, genetics, evolution, AI,
*  but also then, you know, connectivity and brain.
*  And I said to the organizer, I'm very embarrassed because I really don't
*  I got nothing. OK. Yeah.
*  Apart from the fact that, of course, it has its own topology
*  and this looks different
*  just when you look at it from, let's say, even a nonhuman primate brain
*  or another mammalian species brain, the very global things
*  that we've so far been focused on in our field, things like hop structure
*  or communities or even
*  issues about communication, they seem to be playing out
*  fairly similarly across brains of different species.
*  Modularity.
*  Yeah, you can find modular organization
*  all the way down to invertebrate brains.
*  We've worked with colleagues into software for a little bit.
*  We are going to get a lot more software data very soon if it's not already arrived.
*  So and I suspect a lot of what's driving those organizational principles
*  have to do with, you know, very general requirements of what brains are supposed to do.
*  Right. Right. Guide behavior, integrate sensory inputs often from many sources,
*  have access to past information through memory and integrate all this in real time
*  to to guide, especially motor motor behavior out there,
*  whether it's gesticulating with your arms or speech or what have you.
*  So they're sort of a common design specification
*  that that brains kind of have to fulfill.
*  And so perhaps that is driving that at a very global level, brains are,
*  you know, have some common features to them,
*  such as modular organization, some prevalence of hub structure,
*  some regions or some parts of the brain being typically deeper in and more
*  diverse, connected for integration of information purposes.
*  So the glass is either half full or half empty.
*  OK, you can say, well, you found.
*  So in other words, you're telling me you found nothing.
*  OK, half empty perspective.
*  Or you say, wow, you've hit upon a universal principle.
*  OK, you found something that's actually shared,
*  widely shared across different species.
*  And, you know, sometimes I'm on one side, sometimes on the other side.
*  I think so far, specifically human
*  topological features are not that evident to me.
*  OK, maybe because we haven't dug deeply enough.
*  Data haven't been of high enough quality or high enough resolution.
*  But so far, the things that are shared across
*  certainly across primates, certainly across mammals, I would say.
*  The set of things that are shared are much larger than the things that are unique.
*  Looks to me. And so that's that's where we are.
*  So if you ask me what makes the human brain special in terms of its network features,
*  I don't have a lot of answers for you.
*  So I think maybe the title of this episode will be Olaf Sporn's Humans.
*  No, that's not that's not to say that.
*  Because remember, it's not just brain topology.
*  It's also how how the nervous system is connected
*  and how we are connected to our environment and our world.
*  So actually, when I gave that talk at this meeting about what makes us human,
*  my takeaway message was that we shouldn't.
*  It's a mistake to look at specific human features
*  or something totally wonderfully enabling in our connectivity
*  that it makes us so highly intelligent as apparently we are.
*  Sure. His hands are waving in the air.
*  I'm not so sure that, you know, but one thing that that that is
*  somewhat uniquely human is that we have found ways to transmit knowledge
*  across generations. We have a way of building culture.
*  We have social interactions that are, I would say, unparalleled in the.
*  Animal kingdom, OK, to the richness and the the the pervasiveness.
*  And that perhaps taps into some specific brain systems
*  that have evolved that allow us to act on the world in the way that we do.
*  So no language, for instance, I'm not a not a language.
*  I know nothing about language, but people tell me it's you know, it's fairly
*  it's a fairly recent invention evolution from an evolutionary perspective.
*  OK, now we clearly have systems in the brain that are associated with language
*  and perhaps you might say specialized for linguistic processes.
*  And the interesting question is sort of did these systems arise
*  because language was select for or is that something that was there to begin with?
*  And then language kind of our linguistic capacities that evolved in our
*  social world and our environment kind of got a hold of those systems
*  and kind of made them work the way they do.
*  So, I mean, that to me is the big difference.
*  What makes us humans is that we manipulate our environment
*  in ways that is actually threatening the planet
*  and we can transmit knowledge and therefore accumulate and build.
*  And that is not the case for other animal species.
*  Some nonhuman primates can do a little bit of that.
*  Maybe some birds can, but there isn't nearly that profusion.
*  Again, it's some in some level that has to have that has to have a brain.
*  There has to be something in the brain that allows us to do that.
*  Yeah. But I suspect that the answer ultimately is not just in the brain,
*  but it's also in the way that we are able to use our sensory motor capacities
*  to extend our cognition outward.
*  I'm a great fan of Andy Clark's, you know, that cognition framework.
*  Andy was here at IU for a few years and we got to
*  we got to be good, good friends and talked a lot.
*  And I really like his perspective on how cognition is not just happening,
*  you know, in the brain, but it's also it is.
*  We have we have found ways to externalize it to some extent
*  and to and to use our environment to extend our capacities for representation
*  and transmission of information tremendously.
*  Language through writing, through cultural artifacts, social practices.
*  That's what makes us human, I think.
*  That's what accounts for our capacity and our ability to do good things
*  and do terrible things.
*  And you think of that as a network, I imagine.
*  It's like, yeah, I think there is another level of network here.
*  But when I when I wrote Networks of the Brain, here's a little tidbit for you.
*  I chose the title deliberately as Networks of the Brain, because my
*  my plan, my first my first outline that I sent to the publisher
*  was actually going to have a complete second part that deals with this issue
*  of how brains themselves make networks
*  and utilize networks that exist outside of them.
*  And then I, you know, my energy, I think I ran out at some point
*  and I had I had only one chapter at the end,
*  chapter 14, I think it is that sort of touches upon that.
*  But it is a very important
*  set of ideas, I think, to this is, again, a very different thing from AI.
*  Right. This is AI systems really deep on systems are not embodied.
*  They fed, you know, millions of elements of data,
*  but they're not gathering the data themselves and they have no social
*  transmission or anything like that. They have no bodies.
*  They just say it's a flower.
*  Yeah, they're classifiers and and again, very, very important,
*  very powerful in many ways.
*  We talked about this earlier, but what you know, that's what makes us human.
*  Then I think nothing magical, nothing.
*  I don't I don't think it's a special cell type.
*  It's a special brain region.
*  It's a special type of connectivity or topological feature.
*  It's the sudden explosion of possibilities that occurred
*  when our brain topology became capable of using our bodies
*  and feeding itself information in new ways.
*  So there's a network there, a larger network that's,
*  you know, above and beyond what we can measure in individual brains.
*  But I think that's that's the way I think about it.
*  So it's humbling to some extent.
*  I'm not claiming that by, for instance, you know, I do not believe that
*  connectomics, if it's taken to the limit and we get all neurons
*  and all connections, perhaps at one point will give us a magical answer in sight.
*  It is a fundamental ingredient.
*  It is necessary.
*  It has given rise to change in our field.
*  I think it's turning 15 years actually this year.
*  And it just became a word in the English language last year.
*  The Oxford English Dictionary Connectome is officially a new word in the English.
*  Congratulations. Thank you very much.
*  I feel I feel, you know, I've come I've run my course.
*  I can happily, you know, retire.
*  Was, you know, a word I contributed a word to the English language.
*  But anyway, so I mean, I'm not expecting any magic to come from connectomics.
*  I do believe it is fundamental, though.
*  Just genomics, you know, is fundamental for understanding biological systems.
*  But there's no magic answer there.
*  And it's complicated is the answer. Right.
*  And so coming back to what makes us human, I don't I think there is
*  there's no reductionist answer to that.
*  There's no there's no like this is the connection that makes it
*  or this is the cell type of that's the gene or whatever.
*  No, I don't believe that at all.
*  By the way, speaking of connectome, I had Kanaka Rajan on the show
*  and she used the word exposeome.
*  I mean, everything is an ohm now.
*  And that's like what you've been exposed to.
*  I'm like, what is that word?
*  And she said yes, because all ohm words are words now.
*  So thanks, Olaf. Yeah.
*  Yeah, this is true.
*  I mean, there's many ohms out there, but many of them don't make it
*  in the sense of, you know, really taking off as concepts connectome did
*  did make it. And so that's one that I think will stay with us.
*  Well, I've already taken you over time.
*  And so hopefully maybe one day I'll have you back because I wanted to ask
*  all about rich club features and how they underlie our consciousness.
*  Although they're all over every brain, just like every other feature seems to be.
*  And there's nothing special about humans who haven't come in.
*  We haven't mentioned consciousness until this late point in the interview.
*  This is interesting.
*  Yeah. Well, let's talk about consciousness some other time.
*  This is another topic that
*  I have avoided really rocking on, to be honest, for over my career
*  a little bit, because I suppose this will shock you.
*  I don't think ultimately it is all that interesting, but
*  you know, maybe that's left for another conversation.
*  I suppose so. You're killing my audience and me with this leaving off.
*  Let me ask you one thing before we go.
*  It has, you know, learning about the brain and network neuroscience.
*  Is there something that you used to believe that you now looking back think,
*  oh, that was that was naive in my younger days, my inexperienced days?
*  Well, I think, you know, since I've
*  for as long as I can think, almost going back to
*  certainly my undergraduate days and even before then, I was always fascinated
*  by the complexity of biological systems.
*  I didn't have the vocabulary back then or the tools or the insights that I have now.
*  But it was always something that struck me where, you know, biological
*  systems were somewhat different from other physical systems that we might study.
*  The complexity of it, the resilience, the interesting sort of structure
*  and dynamics aspect, the historical aspect, the evolutionary aspects,
*  you know, where these systems come from.
*  And really, to this day,
*  I keep being surprised about how.
*  This complexity plays out in ways that are unanticipated in the brain.
*  There's so many things now that I think are important that I didn't think
*  were important, you know, 20 years ago, this whole interplay of structure
*  and function is sort of a fundamental dialectic, almost using
*  using a philosophical term here of of how this how our brains operate.
*  The fact that there is a a physical infrastructure, neurons, connections,
*  synapses, molecules, etc.
*  And then on top of that, these incredibly rich dynamics that unfold
*  in ways that are bewilderingly complex.
*  And these things interact.
*  The dynamics change the structure, the structure changes the dynamics.
*  All of that's coupled to our bodies and our environments.
*  I certainly didn't think of this of the system in this in this manner.
*  You know, when I first got started and in some ways,
*  the complexity that we're facing is daunting.
*  But I have some hope that as we face up to it and and directly engage with it
*  and use it as a framework for studying, studying the brain,
*  we will ultimately discern laws, function, functional relationships,
*  regularities, principles that are going to allow us to, you know, write down
*  some fundamental working principles of how brains operate.
*  We're not there yet, but I think we have a better chance of getting there
*  now than than than 30 years ago.
*  Well, there's only one way forward.
*  And thank you, Olaf, for helping to move us forward much faster,
*  much more efficient than we otherwise would.
*  And so we're about to hang up.
*  And I know you're in your office when when we're done here,
*  you're going to swivel your chair around, kick your feet up,
*  stare at the books on your shelf, take a deep breath in
*  and relax, maybe turn your printer back on and then maybe go home.
*  Put back on my face mask.
*  I'll put you leave my office and leave the building and go back home
*  and and work from there. Yeah.
*  This is this is the new time right now.
*  So, yeah, it's it was good to talk to you.
*  Good to talk to you. Thank you so much for your time.
*  Thank you as well.
*  Brain Inspired is a production of me and you.
*  I don't do advertisements.
*  You can support the show through Patreon for a trifling amount
*  and get access to the full versions of all the episodes,
*  plus bonus episodes that focus more on the cultural side,
*  but still have science.
*  Go to braininspired.co and find the red Patreon button there.
*  To get in touch with me, email paul at braininspired.co.
*  The music you hear is by The New Year.
*  Find them at thenewyear.net.
*  Thank you for your support.
*  See you next time.

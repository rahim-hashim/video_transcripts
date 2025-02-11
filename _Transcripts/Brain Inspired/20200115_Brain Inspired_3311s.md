---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 3311s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 10335
Video Rating: None
---

# BI 058 Wolfgang Maass: Computing Brains and Spiking Nets
**Brain Inspired:** [January 15, 2020](https://www.youtube.com/watch?v=mtngzbQR3sk)
*  This analogy to deep learning, I think, should make us more humble as scientists.
*  It should really keep our mind more open for the difficulty of the task that we are facing
*  now in reverse engineering a system which, in a sense, has a much worse history than
*  a trained neural network.
*  How far along do you think that we are in understanding how brains compute?
*  This is a very exciting time right now, but how is the cup half full?
*  Is it half empty?
*  How far along are we?
*  Yeah, I must admit, I still think it's pretty empty.
*  We're doing something wrong when we model learning typically because we take off the
*  shelf a certain network and then we expose it to a certain learning problem then.
*  And no network in the brain is ever in the situation then, right?
*  This is Brain Inspired.
*  Essentially, the entirety of the recent successes in AI are built on deep learning networks
*  made of units that communicate with each other using signals that are nothing like the action
*  potentials that underlie communication between real neurons in brains.
*  But does that matter?
*  How necessary are action potentials, or spikes, to manifest intelligence?
*  It's an open question.
*  A functionalist would say not at all.
*  It doesn't matter how you implement a function.
*  What matters is the function.
*  Deep learning folks would also likely say spikes don't matter.
*  After all, look at all the dog breeds we can classify with deep networks that use these
*  continuous activation functions instead of spikes.
*  An environmentalist might think spikes are important, however, if we don't want to continue
*  accelerating global warming and screwing up the planet for future generations by using
*  these insanely energy-hungry continuous activation functions that deep networks use.
*  Spikes are energy efficient.
*  We know that.
*  And that evolution long ago settled on spikes.
*  Like I said, brains use them and brains are super energy efficient.
*  But are there other advantages spikes bring to the table?
*  My guest today, Wolfgang Maas, has long been impressed with brains and interested in what
*  we can learn from brains in terms of theoretical computation.
*  He is and has been at the forefront not just of developing spiking neural networks, but
*  of finding ways to use the experimental results in neuroscience to inspire new ways to build
*  networks that incorporate that biological knowledge.
*  And he doesn't understand why more folks in the theoretical computational world don't
*  do the same.
*  I was fortunate enough to have Wolfgang speak with me and I had planned originally to cover
*  a bunch of the really cool work that he's done recently on spiking neural networks and
*  using biological findings to build in computational features in those networks.
*  And we do talk about spiking neural networks quite a bit actually, but we cover so much
*  other ground I decided like I've done in the past to split our conversation into two episodes.
*  So in this episode, we talk more about the broad picture of the field and culture of
*  theoretical computation and computational neuroscience, how spiking nets are growing
*  in the neuromorphics world, some brain computer interface discussion, and plenty more.
*  And in the second part, which I will release in a few days, we go through a bunch of the
*  features of biological brains that Wolfgang views as potential ways to inspire computational
*  principles and build them into spiking networks.
*  He has incorporated many of these features in his own spiking networks and we run through
*  a bunch of those as well.
*  Spiking neural networks, it's such an interesting topic to me and so exciting to imagine incorporating
*  more and more brain knowledge into AI that they, spiking neural networks, will be one
*  of the first topics that I release in the Brain Inspired course that I'm putting together.
*  And I will include a ton of what Wolfgang has done along with plenty other work being
*  done as well.
*  You can learn more about the course at braininspired.co slash course.
*  So I'm working really hard on it and I want to get it to you as soon as I can.
*  So thanks for your patience here.
*  I recommend heading to the show notes especially for this and the next episode where I will
*  link to a bunch of Wolfgang's beautiful and massive body of work.
*  Those are at braininspired.co slash podcast slash 58.
*  Ronan Thomas, Javier with a hard J, Ethan, Elias, Jung Joon, you guys are the best.
*  Thank you for supporting the show on Patreon.
*  I cannot wait to share content from the course with you soon.
*  Okay, this was a long introduction, sorry, but one last thing here.
*  One of the things I admire about Wolfgang is his stubborn adherence to pursue what he
*  believes is the right path to build intelligent systems.
*  He's been doing it a long time and has faced plenty of resistance, as you'll hear, but
*  he persists and the work he does is all the more beautiful for it.
*  So I wish you, dear listener, the confidence and grit it takes to do the same in your own
*  journey, whatever journey that may be.
*  I guess I should say also, welcome to the Brain Inspired podcast.
*  I'm Paul.
*  Okay, enjoy Wolfgang.
*  Quote, in my darkest hour, I wonder if what we're doing is science as opposed to systematic
*  speculation.
*  Wolfgang, pleasure having you on.
*  Do you know who said that?
*  I don't know, no.
*  That would be you in a talk that I recently watched.
*  Okay.
*  You're lamenting the theoretical computation community not taking experimental data very
*  seriously.
*  Anyway, thanks for being on the show and welcome.
*  I actually do take this thought seriously.
*  I must say I'm a little bit naive.
*  I come off from exact sciences, from mathematics, and then computer science, computation complexity
*  theory.
*  Then I came into or close to the field of computational neuroscience and theoretical
*  neuroscience.
*  I noticed simply the way how these scientific communities work is different.
*  My ideal of a science is physics.
*  I understand some of these breakthroughs in physics really came about when particularly
*  in the last century, there were certain experiments that didn't fit into models from Newton or
*  other old models.
*  These really excited theoreticians looked for a new foundation of their thinking, of
*  their models, which would be consistent with these new experimental findings.
*  This in the end produced theories like quantum theory or relativity theory, which nobody
*  would have thought about just sitting in their chair and thinking how the world might work.
*  I think neuroscience should capture more of this process and spirit.
*  It's interesting that you say neuroscience should because as you were speaking, I was
*  thinking about artificial intelligence and its beginnings and how during its beginnings,
*  people were wanting to understand the mind and intelligence and how it all works.
*  Then they took some very light inspiration from the way that neurons, abstracting from
*  the way that neurons work, and then just went to town and then forgot about brains for
*  a long time.
*  Right?
*  What you're saying is that neuroscience itself, or at least the theoretical side, isn't necessarily
*  paying as much attention to experiment as they should?
*  Correct.
*  I think particularly in the last 10 years, when we get recordings from living animals
*  while they learn even and recordings from many neurons, thousands of neurons, tens of
*  thousands of neurons, even more nowadays, you really have a rich reservoir of experimental
*  evidence which wasn't available 20 years ago.
*  I think theoreticians from many areas should converge onto these data and try to make sense
*  out of them because as far as I can understand them, they're really complicated, confusing.
*  They don't fit into any simple mindset.
*  I think in theoretical neuroscience or computational neuroscience, one should really switch from
*  an exploitation mode into an exploration mode.
*  I personally think we probably haven't really understood the basics really of how brain
*  circuits work, what keeps them really functional, how they learn.
*  I think we're really very much influenced by ideas, partially very old ideas from really
*  thinking about us over many centuries and longer.
*  I think this really somewhat blinds us then.
*  I think if instead of the brain, we would study the liver, we would probably make much
*  faster progress because we don't have so many preconceived ideas how it probably should work then.
*  Yeah, right.
*  One of the things that's interesting about that approach is a lot of people that I've
*  had on the podcast, and it seems like this dominating the current zeitgeist in trying
*  to understand intelligence has to do with Mars levels of understanding.
*  In particular, it seems right now the pendulum has swung to the dominant approach is to go
*  from the higher, from top down, from the computational goals level, use that, theories about that
*  to then think about the algorithms that might be used to accomplish those computational
*  goals and then use those to think about how it might actually be implemented in the meat,
*  in the hardware, like the brains and neural networks and stuff.
*  But you're taking a different approach.
*  Is the bottom-up approach neglected, do you think, these days?
*  This is kind of what you're saying right now.
*  I'm just reframing it in Mars levels, I suppose.
*  You've said actually theorists often use Mars to justify ignoring biological implementation.
*  Yeah, I think now I wouldn't really know a favor particular bottom-up approach, but
*  a two-pronged approach.
*  We should keep all our wonderful ideas and hypotheses in mind, but then look at the evidence
*  and the ground level and simply try to get those things together then.
*  I think partially I can imagine why it's convenient to really interpret Mars as really
*  top-down strategies.
*  It's convenient for theoreticians.
*  You don't have to read all these dirty papers with funny kind of discussions about what
*  data are right or not.
*  You just read other theoreticians' papers and this is much easier for you then.
*  You don't have to get your feet wet then.
*  Believe me, the bottom-up people think the same way about the theory papers, at least
*  in my own experience.
*  So you're a friend to the theoretical community, you're a friend to neuroscientists, you are
*  a friend to computer scientists and a friend to deep learning practitioners.
*  You're bringing us all together around the campfire singing the same song perhaps.
*  Someone must hate you.
*  Who despises you?
*  What group despises you?
*  I don't know.
*  I think there are many people in theory who don't like it so much if the boat is rocked
*  then.
*  I think the theoretical neuroscience community has some aspects of really a belief community
*  which distinguish a community from a scientific community.
*  So in a belief community, people cluster about certain beliefs then and it's not encouraged
*  to come up with completely new beliefs then.
*  And also if you kind of question a certain belief, you don't become popular.
*  And I think one sees this a little bit more belief-like or church-like aspects in any
*  conference or workshop on computational neuroscience because people don't have any heated debates
*  about what is the right approach then.
*  One is just very tolerant of other people's beliefs and expects they do the same.
*  And a little bit you keep in mind, which is one aspect which doesn't occur in church,
*  these people from this community know they are likely to be editors or reviewers of your
*  papers.
*  Oh, right.
*  And you just want to be diplomatic then, right?
*  You don't want to make enemies.
*  And it's a fact that there are certain dominant beliefs like in the say Christian belief community.
*  And these are people are top universities.
*  They have many students.
*  They are good friends with editors of Neuron and Nature Neuroscience.
*  And it's not really recommendable for a generic scientist to rock the boat and to say something
*  which goes against their kind of published beliefs and their work style.
*  I think this is understandable, but it would be better for the community if there would
*  be more kind of rebellions who really say no.
*  All these theories, they don't fit with the following extraments.
*  And I have now here an approach which is suggested by this extramental data.
*  And let's consider this then.
*  So I think we should rather create a community where there is a competition among many different
*  such pursuers of their own approaches.
*  And it's also easier to create newer approaches which don't fit into any of these older beliefs
*  because characteristic for this kind of beliefs around which people group is that many of
*  them are quite old and several decades old.
*  There are not so many really new ones then.
*  And I also want to say something positive.
*  For example, I like very much that Yuri Buzaki has earlier this year published a book, The
*  Brain from Inside Out.
*  And he is such a senior and respected scientist, so he doesn't have to fear for his career
*  then and really questions most of the basic beliefs of theoretical and computational science.
*  I think now for the science at large, it would be wonderful if many also junior people would
*  really run into this and now find really new types of models which are inspired by Buzaki's
*  suggestions or maybe even other alternative suggestions then.
*  But I think just the fact that this book by Buzaki exists shows that there must be something
*  not completely convincing in the basics of the common belief of theoretical neuroscience
*  or the ruling beliefs in neuroscience because Yuri Buzaki certainly knows the literature.
*  And he certainly also has his own bias because he works on systems like the hippocampus which
*  is not the standard system in theoretical neuroscience.
*  So he has a somewhat tilted or more different kind of experimental basis, but he knows the
*  same facts as other people know.
*  And he makes really propositions for approaches and facts which are really orthogonal to many
*  of these common approaches in theoretical neuroscience then.
*  And so this I think is really very nice and one should see this as science that this is
*  not a church community, but it has features of a scientific community.
*  Yeah, a secular community.
*  I really enjoyed Buzaki's Rhythms of the Brain book from many years ago, but I haven't read
*  this one, The Brain from Inside Out, so you recommend it.
*  Yeah, certainly.
*  I think this older book Rhythms, I found it remarkable because it's really one of the
*  very few books where somebody ventures out to go beyond their own data and speculates
*  about how the whole brain might come together and what other problems for really brains
*  have to face.
*  I think in this new book, these rhythms are one of four or five different themes then
*  and he addresses many other aspects.
*  For me, I think the most stimulating proposition of his book is that the usual process in computation
*  theory in neuroscience is that we think we first have to understand how sensory stimuli
*  encoded in the brain.
*  Right.
*  And he argues that this is completely wrong then.
*  No brain would really start to function in this way then.
*  Processing the incoming data isn't the first pass, huh?
*  No, they have to process data, but to make sense out of the data then is his point then.
*  And his point is no brains are really, their goal in organism is really to control motor
*  action decisions, right?
*  And so therefore his argument is that sensory input only acquires meaning in this action
*  oriented context then.
*  I love this notion.
*  This is gaining traction over the past few years, I think, as well.
*  I think now this, he possibly really emphasizes there one particular kind of scientific habit
*  which is very common in theoretical neuroscience is that we all want to understand in this
*  area how the brain works.
*  Now let's really split this into different tasks then, right?
*  So task A is how sensory processing works.
*  Task nine will be how to construct the motor output.
*  And then I think the worst thing is then we split it not only into tasks, which is fine,
*  but we postulate optimization goals for this individual task then.
*  And this is then a large part of this community, really no groups around and really understand
*  this postulated goal of this sensory processing, right?
*  And postulated goals are predictive coding and various shadings and various others, no
*  sparse coding.
*  And in principle, this is not plausible, but I find it problematic if one as an analogy
*  really looks at machine learning for a moment or deep learning we want to write.
*  And if you look there at a really no highly tuned, no highly learned trained system and
*  try to reverse engineering, you'll find it's extremely difficult.
*  Yeah, it hardly ever does at any stage what you expect it to do simply because if you
*  optimize a whole system for a certain kind of more overriding task, it doesn't split
*  up this overriding task in the same way as we humans are trained to do then.
*  It simply finds whatever works best then, right?
*  And it has no incentive for formulating the sub goals in any clear way than in any
*  theoretical tractable way then.
*  And this makes it so difficult to reverse engineer any deep learning system as far as
*  I know them.
*  And in that sense, I think this analogy to deep learning, I think should make us more
*  humble as scientists.
*  It should really keep our mind more open for the difficulty of the task that we are facing
*  now in reverse engineering a system which, in a sense, has a much worse history than
*  a trained neural network because a trained neural network is trained in the end by one
*  author or one author group and one learning algorithm.
*  Where the brain emerged from evolution, there were many kind of phases where something was
*  optimized.
*  Then later another optimization stage produced another system.
*  Now they're working together then in really complicated ways.
*  And so therefore, in this sense, since there were many different phases of development
*  in brains which are now superimposed, then it's even harder to reverse engineer a brain
*  compared with reverse engineering a deep learning network.
*  Right.
*  Yeah, and the deep learning networks, everyone, every week there are about 30 or 40 completely
*  different networks doing completely different optimizations on completely different problems
*  that aren't necessarily even building on each other.
*  Although there is a lot of building on each other but not in evolutionary terms like the
*  brain has for sure.
*  Well, Wolfgang, you've blown up my outline here for the whole podcast.
*  So congratulations.
*  But I love it.
*  So let's talk about what you do for a second.
*  So one description of what you do, and we've already gone down the road of how you approach
*  these things, but one description of what you do is that you take a theoretical computer
*  science approach to understanding how to compute with biological and artificial neural
*  networks.
*  Another description might be that you take modern deep learning and ask how to accomplish
*  the same computation that deep networks do, how to accomplish that with the known properties
*  of how brains function.
*  And yet another is that you observe the computations and algorithms that brains give rise to
*  and perform and you model them again, respecting their properties and constraints.
*  Those are a little all over the place.
*  So which is the better descriptor?
*  How do you describe what you do?
*  I think this was a perfect description.
*  And I have all these parts in me then and I find them mutually inspiring then and also
*  mutually encouraging because after long phase of speculating about the brain, it's sometimes
*  nice simply to think about learning algorithm for spike based hardware.
*  And you know it works.
*  Yeah.
*  And you can measure it then.
*  And I think when sometimes maybe gets more on an unconscious level, no inspiration also
*  for really coming up then with new ideas about the brain then.
*  Yeah, I think that's so valuable to sort of cycle around.
*  And always be thinking about it in very different ways.
*  And that really they inform each other.
*  I really think that's a great approach.
*  Yeah.
*  And I think we're living in very good times then with regard to spike based computing.
*  Now, since not only AVM, but Intel has entered the field and many other startup companies
*  now are in this direction.
*  I think now this field of neuromorphic computing is changing its style then.
*  It used to be also now after cover meets now exciting suggestions in the 80s.
*  It used to be developed a little bit also into a church like communities where people
*  know each know their love, know their own device then their own small robot, their own
*  way of defining what cognition is then.
*  And now this was not questioned by any common benchmarks or performance goals.
*  Now, when this industrial giants now enter this field, then these departments there,
*  they have to justify it to their managers now, whether this is a viable computing
*  alternative or learning alternative.
*  Right.
*  And so therefore they have a much more stronger incentive to really push for
*  benchmarking, for really getting the most out of a certain design approach then rather
*  than be happy with pleasing paradigms to make it really more like an engineering
*  discipline, which I think was missing for a long time in neuromorphic engineering
*  because every part of engineering I know as a non-engineer, there is somewhere a
*  theory and their benchmarks and both of them missing or have been missing in
*  neuromorphic engineering.
*  And I think the push towards these aspects of engineering discipline has become so
*  much larger then.
*  And so therefore we're seeing now within a few years, much more progress in my mind
*  than previously in 10 years or so.
*  Oh, wow.
*  So this, I think really now provides quite a bit of insight.
*  What I also like very much is that this, if you look, take a closer look at now the
*  people and also the publications from these companies like IBM and Intel, it's not
*  really geared only towards now the bottom line now in the end, creating a market and
*  income, but they're really odd by the brain as a paradigm then.
*  Are they?
*  Yeah, they are too.
*  Certainly.
*  I think now you can simply see it, for example, just as a fact that if you look at
*  the research groups which are funded by Intel, they have created their own network,
*  the Intel neuromorphic research community.
*  Yeah.
*  There are a lot of 60 or no more kind of groups.
*  And I think now at least half of them are really biologically oriented.
*  So I think there is really strong belief also from the side of these engineers and
*  these people at Intel that biology can teach us something.
*  You mean they have biology backgrounds?
*  No, they really know them, work out biological paradigms for attraction or other ideas
*  for the use of phases to structure spiking information and various ideas then.
*  So I think this is very nice then.
*  And I think this is somewhat less pronounced as far as I can see it at IBM, but they
*  have in-house certainly also people who really have more background in computational
*  science and also bring these aspects in then.
*  So what, you come from a math background and then a complexity science background,
*  but what drives you really?
*  Like, well, what is your, what's the question that you want to answer?
*  And maybe even how has that changed over time?
*  Yeah.
*  They're really intrigued by understanding how the brain computes and learns them.
*  Okay.
*  And I had approached this more or less in a straightforward manner then.
*  So in older times, there weren't really so many models available.
*  You had in computational complexity theory, there were the so-called threshold
*  circuits, which are kind of a very simplistic form of spike-based neurons.
*  And they were intriguing complexity theory for reasons which are probably unknown
*  outside of this community, because one suddenly found that if you put many of
*  the threshold circuits together, even within a few layers, they suddenly gain a
*  computation power, which is impressive.
*  A potential for it anyway, right?
*  Right.
*  So technically it means that from the perspective of a theoretician in
*  computer science, it could still be that with three layers of threshold circuits,
*  not too many of them, you can't even solve any problem which is NP, which is
*  not the class, which is not all the problems one would like to solve, but
*  cannot solve with efficient algorithms unless they belong to the subclass P then.
*  So for a theoretician, this tells that already with three levels of threshold
*  gates, it becomes impossible to rule out that something can be done by these
*  circuits.
*  They still look like such a simple model then, so that once you think now in
*  afternoon, you could say they certainly couldn't solve the traveling salesman
*  problem or something like this then.
*  And this has intrigued no theoreticians now for almost three decades then.
*  And they still now are struggling with this then.
*  So, no, this is no kind of no depth three threshold circuits are really
*  stumbling block also just from the theoretical perspective then.
*  So one would be no very liberal and now is no is happy with jumping to analogies.
*  No, it could be that evolution also at some point found no, if you have neurons
*  that even though no having few layers of them now suddenly give you really almost
*  unlimited power.
*  And so then the problem becomes really now just to train these circuits for
*  particular functions then.
*  And just one last word, no compared with other concepts in computer science, no,
*  I think most standard is there to compute.
*  Now you look at gates which compute in a Boolean and or negation and when those
*  if I looks at small or shallow circuits of this type, no, they have very limited
*  computational power.
*  So there's something magic happening if you replace a gate function which
*  computes and and or also of many bits by threshold circuit which takes a weighted
*  sum or just the majority of input bits and compares them with the threshold then.
*  So this is really exciting now that there is a strong computational power then
*  really emerges then just from this basic operation of then any simple neuron model
*  also right where you compare membrane potential with a foreign threshold.
*  Yeah, that is kind of how the original McCulloch-Pitts neuron model worked though
*  correct.
*  So I mean is it as a threshold model.
*  Right.
*  Yeah.
*  And we've since gotten so spiking neural networks are a little different, but you
*  know, we've since gotten away from that model.
*  Well, we'll get to it.
*  How about we'll build up to it in a second.
*  But but just thinking about your background and how your thinking has evolved.
*  So you got your PhD in mathematics.
*  Was it pure math at that point?
*  Was it pure mathematics that you liked or was it something that math could do?
*  And I'm asking because I've asked plenty of guests, you know, what's the most
*  important thing for people to learn to get into neuroscience and AI and they
*  almost always say math or, you know, some sort of quantitative approach.
*  Right.
*  And so that's why I'm wondering, you know, if you and I think, well, starting off in
*  just pure math, it would help to have a goal in mind.
*  It's always helps to have a goal in mind when learning a subject.
*  And math is no exception, I think.
*  So I'm wondering what your early goal was.
*  I could what or was it just pure mathematics, the beauty of mathematics?
*  Yeah.
*  That's a very nice question.
*  Yeah.
*  Yes.
*  Actually, it was for me a problem as a student.
*  I discovered no, that no mathematics, especially pure mathematics is something I
*  can easily do, but I was really missing a meaning and a goal then.
*  And the area where I wrote my PhD on was known area of a wonderful professor,
*  Kurt Schütte, who was actually one of the last PhD students of David Hilbert,
*  now one of the truly founding giants of all of mathematics.
*  And he worked actually on Hilbert's program and part of Hilbert's program,
*  because what had really bothered, you know, these mathematicians in the last century
*  was that mathematics, which has a reputation of being the most secure and safe science,
*  now has problems in its foundations.
*  Then possibly you even can do locally correct proof and ending up proving something
*  inconsistent like zero equal one, or that there's certain axioms where you don't really
*  know whether you should believe in them or not then.
*  Right.
*  And so this I found wonderful that pure mathematics, you know, somewhat analogy,
*  analogies to lead to physics now came into a stage where it questions and examines its
*  own foundations then.
*  Yeah.
*  And there was this area of proof theory, which was now founded by David Hilbert, which argue,
*  let's simply look now at mathematical proofs as mathematical objects and try to understand
*  the common networks of these mathematical objects, whether you can rule out that with
*  correct proofs, you can produce stupid outputs then.
*  And so this was a wonderful program.
*  And this is what excited me as a PhD student then.
*  And in the meantime, no, it turned out there are some scientific reasons now why this
*  approach may not really bring us that much as a true answer then.
*  But it has this feature a little bit like also theory of neuroscience, right?
*  It's not just a kind of analytical theory, but it has a meaning or goal which goes
*  beyond this formalism then.
*  Yeah.
*  Well, I mean, and I don't know, part of that is just luck as well, because you're like
*  you said you're adept at math and and if one goes into math, something like math, all
*  of a sudden you can apply it to anything you want to apply it to.
*  So it's very fortunate if you can muster the desire to go down a road like that and
*  you're good at it. I think it's one of the most fortunate things because you can apply
*  it to anything like you do these days.
*  So, well, I'm glad that glad that you did.
*  So, OK, so I was listening to Terry Sanofsky on another podcast.
*  I've actually had him on Brain Inspired here, but I was listening to he was on one of
*  the other one of the many popular AI podcasts and I was surprised he was talking about
*  spiking neural networks, among other things.
*  And I was surprised just how little the host seemed to know about brains.
*  So if you take a deep learning course online, there are all these online courses.
*  They always start off with, you know, here is a neuron.
*  It has an axon. It has dendrites and neural nets are like a bunch of these neurons
*  connected. And then they, you know, I always roll my eyes and, you know, it's like a
*  necessary thing that they have to go through.
*  Show you a picture of a neuron, talk about a neuron.
*  And then they go on to talk about neural networks.
*  And but it's just striking to me how little knowledge about brains people have who work
*  with deep nets often.
*  But the people who developed AI from the start were interested in how brains work.
*  In fact, like the earliest modern computers that we have, the von Neumann architecture,
*  you know, were inspired by the McCulloch and Pitts neuron, which were inspired by how
*  brains work. So so it is interesting how neglected brains are in the deep learning
*  world. But you interact with computer scientists and theorists and neuroscientists and
*  deep learning folks. Where do you see room for the most contribution that's lacking
*  now? I mean, is it is it really that theorists need more neuroscience knowledge?
*  I know that you've already said that you're bringing the data to bear on it, that that's
*  really important, the experimental data.
*  But do theorists need more neuroscience knowledge or do neuroscientists need more
*  theory to drive their experiments?
*  What's where's the most contribution going to take place?
*  Yeah, I would say it is simply I think what is needed then and it's actually fortunately
*  happening already some some expense that these two communities come closer together, that
*  they inform each other, know their post puzzles for the other ones. And you may have noticed
*  that in the last few Nipses and NeurIPS conferences, there were again workshops, know
*  which combined people from deep learning and neuroscience then. And I think it's a growing
*  field in one of the review papers, there was even a plot which showed an exponential growth
*  in papers which have a neuroscience, no content and also using or mentioning deep learning
*  then. So communities are growing together. And also there, I think now one should really
*  avoid to fall into kind of simple characterization then because if you look at
*  now closer at some of the people who work for example at Google DeepMind in London,
*  you find that there are many who really extremely competent for work on the brain,
*  right? Now they have even top neuroscientists like Matthew Bodvinnik or Chris Summerfield
*  from Oxford University and others. And they have top young researchers like Tim Lillicrab,
*  who really know a lot of neuroscience and but still do what people would call deep learning
*  or AI then. I think one should avoid no kind of a cartoon like characterization of what
*  the others are doing then. And I think one of the most common cartoons that one finds
*  not only in computational neuroscience and but also in neuromorphic engineering is that
*  there are this kind of brain oriented research and there are these deep learning people who
*  do some funny numerical game, but they don't really relate to us then. Right. And I think
*  this is really unfortunate for the people who have these beliefs, but there because
*  they are to a large extent wrong then. Not only do many people who work in these companies,
*  not only Google DeepMind, but there's also Google Brain then in the US then another department
*  with hundreds of top researchers, where people really have neuroscientists on board,
*  cognitive scientists on board, they care about brains. But also deep learning nowadays is not
*  that people think all the time about backprop or backprop through time. What you really see
*  instead, it's a newly a culture of categorizing learning and architectures. When you look at a
*  generic paper, no said no ribs. Even if they are in the end about deep learning, you hardly
*  ever see the word deep learning mentioned. Somewhere there are no deep buried in the paper,
*  you find there's a loss function defined then. And then it's taken for granted that you have
*  an algorithm which optimizes this loss function. So therefore, I see this way that deep learning
*  is really used like multiplication is used by people who do arithmetic. You don't write papers
*  about multiplication, you write papers about arithmetic about number theory, you use
*  multiplication, right? And this is really what's happening. Now this enormously flexible uses of
*  deep learning in ever new architectures, ever new functional context. This is really, I think,
*  which makes machine learning or deep learning as a field at the moment really exciting.
*  But there's also the so there's the use of deep learning. But there's also the theory of deep
*  learning, which gets us back to theory of computation and brains as well. And in that
*  respect, you do. If there's a theory of multiplication, then you would talk about
*  multiplication in your paper, right? Yeah. But I think at least at NIPS,
*  one find doesn't find too much there's a little bit work from people more in other communities,
*  than machine learning, who want to explain know why deep learning works, or sometimes doesn't
*  work. And there's a certain characteristic feature, those papers, there, these are people who want to
*  prove something, right? And so this is fun, no, and this is just what they have learned. And then
*  typically, they have to make simplifications to the neural network model, like often assume
*  everything is linear or so, right? And then they prove something. And then this shows limitations
*  then, right? And so this is a problem, I think, at the moment, that I don't see really, that no,
*  the theory of deep learning of this type, really contributes so much to understanding the power
*  and uses and potential of deep learning then. And at the same time, I still know, do also
*  concede that it's, at the moment, a little bit like a miracle, which really asked for scientific
*  scrutiny, know that deep learning works so well, suddenly, right now, since 30 years ago, it didn't
*  work so well then. And I think that the more fruitful approach, and which may be also be the
*  most inspirational one for neuroscientists who want to peek in the field really, is in the direction
*  of reverse engineering, deep learning results then. And so this is something which was, to some
*  extent, also really cultivated by neuroscientists like James DiCarlo from MIT. And now,
*  Jamin Snow, his former postdoc, now at Stanford, who really then both do deep learning
*  experiments, and that do recordings on monkeys, know that are trained to recognize images,
*  and they compare kind of neural codes, know in quotation marks, know in their deep learning models,
*  and what they measure, say, in area IT then, and they find, know, some exciting links between both.
*  And in the last two years, know they have taken this even further, know they started out with
*  feed forward networks, know the standard architecture in deep learning, but now they have
*  started to tackle recurrently connected networks. And they ask a question, well, we know from
*  feed forward networks in deep learning that these are already very powerful. What else can
*  recurrent connections give us from the functional level? And so this is really an exciting question
*  for neuroscientists because we know recurrent connections is one of the most characteristic
*  properties of neural networks in the brain, right? And I think, know, in this way, one has a new
*  approach of, know, really approaching this question, what are they good for, right? What is the architecture
*  of neural networks in the brain really good for? And what I like also about this style of this work
*  coming, starting with this paper from DiCarlo five years, or so years ago in PNAS, is that they
*  introduced a new style in this kind of computational science research, which I like very much because
*  it goes very much against this trend of a church-like community. They really
*  provided empirical basis for judging which of this model is more functional than other ones
*  from various perspectives. And they spent a lot of time really on establishing sound criteria,
*  know, for example, defining something which they call a brain score, which scores whether the model
*  has some brain-like features then. And they like this very, know, neutral engineering-like approach
*  towards understanding, know, complex architectures and possibly brain-like architectures. And I think
*  this will probably help us a lot. And the fact that the networks are trained to perform the tasks,
*  right? And so you train the network to perform the task and then look at how the units are activated
*  and such. So guys, by the way, Wolfgang doesn't listen to podcasts, nor the radio, I found out.
*  But so he doesn't know. You just name dropped four or five people who have been on the podcast
*  before, so that makes me feel great. So that's, you know, friends of the show, essentially. So
*  we're on the right track here. So in some sense, we do know a lot about brains. You know, we know
*  how neurons function pretty well, and we have for a while, you know, we have a pretty good sense of
*  brain architecture, or the, you know, connectomic work is still ongoing, and so on. How far along do
*  you think that we are in understanding how brains compute? This is a very exciting time right now,
*  but how is the cup half full? Is it half empty? How far along are we?
*  Yeah, I must admit, I still think it's pretty empty. So if you take a closer look, for example,
*  you know, I just one basic question, neuroscience question, looking at know the anatomy of a
*  cortical column, whatever this is, then that's simply a small patch of circuitry.
*  Now, there are many papers out there, many published models, but if you take a closer look,
*  they extrapolate very few data, then we don't really have the empirical ground truth of really
*  finding, knowing which neuron, if a particular type of neuron, a particular layer, what is the
*  connection probability to another type of neuron on another layer, then. And there are, in principle,
*  approaches for doing this, like from the Lichtman lab at Harvard, but no, they didn't have the
*  chance to get it funded, to really bring it to really use the very demanding technology to
*  analyze a full cortical column. So it's only a tiny segment. And so therefore, in some sense,
*  we're missing the ground truth, right? So even beliefs know that in the cortical column,
*  there's a certain local circuit template, which is then stitched together to form a carpet,
*  know, which is then the brain area, we don't really know the elementary model then, right?
*  Right. And if we're discussing with experts, if you look even at basic questions, for example,
*  we used to think, for example, that neurons and particular lamina have distinguished role with
*  regard to forward and top downstreams within brain areas. Now it turns out, know that there
*  at least two bottom upstreams, which connect to columns in the lower and higher areas, and two top
*  downstreams in the higher and lower now kind of lamina. So it's as complicated.
*  Come on, come on, let's keep it simple here, Wolfgang. Let's not complicate things any more
*  than they need to be, although they need to be. So.
*  And then, for example, also another kind of more from the functional perspective,
*  I think everybody agrees that, you know, brands must be good at predicting things, right?
*  And so therefore, there must be all the time compare predictions with know the actual ground
*  truth that they're experiencing right now. And so there should be no well defined circuits,
*  which compare these two sources of information, and then do something, subtract them or whatever.
*  And as far as I know, and also as far as experts for this tell me, it's still not known really what
*  neurons do this on which lamina. Yeah.
*  So therefore, as far as I can tell, even for the most fundamental brain computations, we don't
*  really know the players and the architectures for these computations then. In that sense,
*  I think we are pretty far behind then. How do you think that relates to brain machine
*  interfaces and the potential for it? I ask because so well, I don't know how to really
*  approach this without seeming negative. But so Elon Musk's company, Neuralink, just made a big,
*  you know, not announcement, but they just released something. And his notion is that, oh, yeah,
*  we'll just plug into the brain. You know, it's a neural network and we'll figure it out.
*  But it struck me that so Elon Musk, a very bright guy gets things done.
*  But all the things that he's done, Tesla, SpaceX, he's approached from first principles.
*  And you can really do that in physics, for instance, you can because the first principles
*  are pretty established, right? So you can go back and figure out how to make a more efficient
*  battery, you can make more efficient fuel for rocketing into space. But then I thought, well,
*  what are the first principles for brains? Do we really have them? And I don't see them. You know,
*  I know that there are a lot of suggestions for first principles. But what you're saying is
*  that those are missing still ground truth, let's say, if you can equate that with sort of first
*  principles. So and I'm wondering, you know, is that going to hinder our ability to create brain
*  machine interfaces that are really effective? I know I'm going taking a tangent here, but I'm
*  not going to make me think of it. It's a good question. Yeah, I want to address this question.
*  But at the same time, I want to complement my more kind of disappointment about understanding
*  of really know the computations in this basic circuitry is that there's different perspective
*  of kind of canonical cortical circuitry that this in the sense learning machines then.
*  And so therefore, this suggests that it's a wrong question of simply asking just know this circuitry
*  this nuance on this lamina, what do they compute what they're made for, you could view them simply
*  know their models in a learning machine then. And I think this is really a view which has many
*  arguments in favor of them. And then coming back to to musk and brain machine interfaces,
*  what one has no had noticed, then going back even though to this experiments of about FETS
*  several decades ago, that it's not that the brain gives them certain output then,
*  whenever now you engage a brain, no take off signals and then engage the person in a closed
*  loop, then we're saying no, you won't know that this recorded brain signals should know really
*  now control robot arm. Then as soon as this person is observing this and knows that this is the goal,
*  the brain strives to make circuitry no fit into this goal then right.
*  So this is a learning principle.
*  Right. Adaptivity and learning is something which is really possibly an even more
*  fundamental and important principle for understanding brain circuitry and brain function then.
*  And then this gives us some hope then also in so far as we also as I mentioned before,
*  we know for example from work no say from calcium imaging from the tank lab or Chris Harvey labs at
*  Harvard, where they really see no when rodent learn something, certain behavior, how does it
*  change no activity of neurons in a certain area, it was their PPT posterior parietal cortex,
*  and so therefore we have now really something in hand which we didn't have no several decades ago.
*  Right. We see now how learning really changes circuitry on some level and no, there's further
*  work going this direction then. I think what we are still missing is really the understanding
*  on the kind of bottom up level, what happens in neurons and synapses during learning then.
*  I think still there we are still up again simply fundamental experimental impediments
*  that typically you have to do these experiments in slice then, no in a slice, no it is not a
*  working system, it doesn't learn and so therefore we're missing there a link in this possibly the
*  in the most fundamental link in this chain for understanding the organization of learning in
*  the brain really at no the level of neurons and synapses. I think there the information is still
*  very partial then. That wraps up the first part of our conversation.
*  Like I mentioned, I will release the second part in a few days. Alright, goodbye for now.
*  Brain Inspired is a production of me and you. You can support the show through Patreon for a
*  microscopic two or four dollars per month. Go to braininspired.co and find the red Patreon
*  button there. Your contribution will help sustain and improve the show and prohibit any annoying
*  advertisements like you hear on other shows. To get in touch with me, email paul at braininspired.co.
*  The music you hear is by The New Year. Find them at thenewyear.net. Thanks for your support. See
*  you next time.

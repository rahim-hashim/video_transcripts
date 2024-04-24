---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 3995s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 7447
Video Rating: None
---

# BI 041 Brad Aimone: Neurogenesis and Spiking in Deep Nets
**Brain Inspired:** [July 19, 2019](https://www.youtube.com/watch?v=DZoLgrKvGZs)
*  when computer scientists start telling neuroscientists how the brain works, we
*  need to be cautious. If you had a whole brain, let's just say that someone
*  gave you a whole brain on neuromorphic chips and it had every connection
*  and all the dynamics you needed to replicate a brain, mouse brain saying,
*  then we're gonna be where we are now in systems neuroscience and how do we
*  interpret what's going on in that.
*  This is Brain Inspired.
*  Welcome guys and gals, I'm Paul Middlebrooks. Today my guest is Brad
*  Imany, a neuroscientist turned AI researcher slash neuromorphics and
*  computing researcher at Sandia National Laboratories in Albuquerque, New Mexico.
*  Can you spell Albuquerque? So this is fun because I haven't had anyone on the
*  show talking about neuromorphics since way back when, oh what episode was that
*  with Julie Grolier? Episode 19, wow, long time ago. I came across Brad because I
*  learned about his method of transforming a normal deep learning network by
*  using rate based signals into a spiking neural network that uses spikes or event
*  based signals like brains do to allow the transformed network to run on
*  neuromorphic hardware, a method that they call the whetstone method. But as I dug
*  deeper I discovered all of the other interesting stuff that he does and we
*  ended up talking for a long time because the man was generous with his time and
*  for that I am grateful. But because we talked for so long I split our
*  conversation into two episodes. So in this first part of our conversation we
*  talk about what I just described. We also talk about neurogenesis deep
*  learning which is a way to add artificial units to deep learning
*  networks as the networks get trained. So this is inspired by how new neurons are
*  generated in our hippocampus. And we also talk about the neuromorphics
*  workshop that Brad co-created and helps run, the neural inspired computing
*  elements workshop or NICE workshop and you can find links to all of the stuff
*  that we talk about as usual in the show notes at braininspired.co
*  slash podcast slash 41. For example you can find a link to the NICE workshop
*  where they host videos of all the talks and panel discussions from the workshops
*  of years past. All right here's part one with Brad Imany. So I'm doing some
*  research about my next guest and I'm thinking oh this is going to be great
*  you know we you know I haven't talked to neuromorphics on the show since I had
*  Julie Groye on the show a long time ago and this is someone from the more of a
*  computational computer science background and lo and behold I have
*  another damned neuroscientist on the show. Brad welcome to the show. Thank you.
*  So you do have a neuroscience background you did a PhD in Fred Gage's lab
*  studying adult neurogenesis in hippocampus among other things but now
*  you're at Sandia National Laboratories where in Albuquerque New Mexico where
*  you're working with neuromorphics and computing in general and developing new
*  techniques in AI. So just to start off how did you come from the the
*  neuroscience world to this current Sandia National Laboratories world? Yeah
*  so you know like most people's kind of career trajectories mine took me on some
*  unexpected path. When I was leaving the Salk Institute where I was computational
*  neuroscientist working among molecular biologists and neuroscientists you know I
*  really wanted to identify a path by which the work I was doing in computational
*  neuroscience could have some more tangible real-world outputs. Yeah and this
*  is always a struggle especially I think for systems and computational
*  neuroscience where the kind of classic application for neuroscience is health
*  and you know like most people I was I had very interesting ideas I think at
*  the time I thought they were interesting of how my research could play into you
*  know mental health disorders and psychiatric disorders and so forth but
*  the more you push it is a really long path to go from computational neuroscience
*  into anything that might have clinical relevance. Most clinical research is
*  focused on drug discovery for instance. So I got an opportunity to talk to
*  people at Sandia which as a national laboratory doesn't do a lot of
*  neuroscience it certainly doesn't do anything close to the you know
*  experimental neuroscience that you would have in San Diego or any of the other
*  big hubs of neuroscience. So I wasn't sure what I was going to get into when I
*  came out and interviewed but the you know upshot is is that national labs
*  while their mission is not health it's not NIH funded they focus a lot on
*  physical sciences computer science and fields like that and so there's a lot a
*  lot of interest among this community and there has been for you know ten years or
*  so in future models of computing. So neural brain inspired computing fits
*  right into that. So they wanted to bring people in with neuroscience
*  backgrounds in order to start thinking about what the future generations of
*  computers would look like. I was like you know you have big computers and I like
*  to do big simulations so you know that sounds fun let me go play with those big
*  computers. So it was a I saw it as a mutually beneficial thing
*  I'll tell them a bit about the brain I get to play with their their big
*  computers and we'll see what happens. And you know so I did that I came to San
*  Diego for really with the goal of doing what I was doing before which was
*  modeling hippocampus circuits looking at things like adult neurogenesis at
*  larger and larger scales. So be you know pushing the envelope of how big of a
*  simulation one could do. Of course there are issues with that the field as a
*  whole has been trying this in a number of areas and I ran into similar issues.
*  Big biggest one being that you can always build a bigger and bigger
*  simulation but ultimately you're constraining your models based on
*  individual recordings of isolated neurons and you're trying to kind of go
*  from electrophysiology data to something that exists at a very large
*  scale. And how much you can glean from models constructed like that is a
*  challenge. I've been struggling with this my whole career and once I got
*  kind of isolated from the experimental community when I came here it almost
*  opened my eyes a little bit saying you know in order to convince an
*  experimentalist to start modeling you know to do experiments to study what my
*  models produce that would be a really tall order for them. And so we kind of
*  had a nice I think almost soul-searching moment of being a neuroscientist doing
*  really really large-scale simulations. So from that point I kind of started to
*  embrace the sort of computing applications of neuroscience more than
*  just simply using computing as a tool. They've turned you. So this is like how
*  long have you been at Sandia now? About eight years I think I came here late
*  2011. So I mean this is an interesting transformation like you said everyone's
*  career takes a winding path you know but so you've been slowly I mean from just
*  from my own research it looks like you've been slowly becoming more and
*  more enamored with with the computing aspect of all of this. But you're
*  definitely influenced by your knowledge of brains and hence the neural inspired
*  computing aspect of all this. So when you approach a problem do you view things
*  now through the lens of the potential for its computing ability or do you view
*  it through the lens of the potential of its relation to brain what we know about
*  brains for instance? I think it depends it depends on what it is that we're
*  trying to do. In the case of something like deep learning there are times
*  where you want to make it more brain-like you want to add some
*  capabilities some functionality that you know would be great if our algorithms
*  could do what our brains are able to do. And in those cases I think well looking
*  to what the brain does seems the natural and almost easiest path by which we can
*  get that capability into these algorithms. On the other hand there are going to be
*  cases where you know we've used the brain to inspire the hardware architectures
*  that the neuromorphic community is developing and now we can just think
*  about it from a computer science point of view. Given this computing fabric
*  what problems can we solve that are new? And that can take you in a direction
*  that's completely unrelated to how the brain functions or at least we can set
*  aside that constraint move towards you know asking what is a computer made of
*  neurons effectively able to solve more efficiently than a computer made of kind
*  of conventional logic gates. So we do both and I've been I've enjoyed kind of
*  switching back and forth between those different mindsets and admittedly you
*  know I probably confuse people because sometimes I'll be like you know look the
*  brain does this and this and this and you do it that way and other times I just
*  jump at something and say let's ignore the brain let's do it a different way
*  and I think there's there's reason to do both at different times. You're like the
*  only neuroscientist in the room ever right? That's not true actually we have
*  another neuroscientist here Francis Chance who was a professor at UC Irvine
*  for a while and came out of Larry Abbott's group a number of years ago. So we have two
*  computational neuroscientists around. I like what you said earlier about sort of
*  the struggle with the frustration with the clinical relevance not being in a
*  shorter run like the clinical relevance being in the longer run from a
*  computational neuroscience perspective. When I was in graduate school the
*  mantra was I think it was from benchtop to bedside and this is like the idea
*  that your research is directly applicable in the next step to treating
*  people and from a computational neuroscience perspective that is not the
*  way it works so we all just kind of rolled our eyes you know. Yeah. Alright so
*  let's jump in here. So I have so much to ask you about today so we'll see how far
*  we get but let's start with some of your recent work here and then hopefully
*  broaden the conversation to neuromorphics in general and neuroscience
*  and AI. So you developed what you have called neurogenesis deep learning and
*  maybe before we discuss it just as background maybe you can summarize your
*  work a little bit on neurogenesis and memory in the hippocampus from from your
*  PhD work. Yeah so I think my true neuroscience love are new neurons in the
*  hippocampus. Yeah. So you know your is in resting gauges lab as a grad student
*  at first work postdoc and that lab before I got there had been one of a
*  handful of labs around the world that had identified that indeed you have new
*  neurons born into adult brains and this is still a mildly controversial
*  topic but at the time it was very controversial. Historically you know the
*  textbooks I read as a kid you know biology classes in high school there are
*  no new neurons in adults and that's fairly accepted dogma at the time. Well
*  it turns out that there are and in particular the dentate gyrus area of the
*  hippocampus receives a fairly robust level of neurogenesis throughout life.
*  It's robust in that it always happens but it's not a ton of neurons it's just
*  kind of a continuous stream of new neurons coming in. Well it's not it's not
*  so much controversial that there are new neurons being developed in the brain in
*  in hippocampus right. Isn't it more controversial that it's in other areas
*  as well that it's ubiquitous. What's the controversy? So there has been
*  controversy about both. So while I was in grad school the big controversy at
*  the time was whether cortex received new neurons. There were some reports out of
*  Elizabeth Gould's lab I believe it was that had inhibitory neurons being born
*  in different cortical regions and those were you know Pascual or Quiche in
*  particular was very adamant that they were not there. I think it's still open
*  question about whether some of these interneuron populations in different
*  parts of the brain indeed have adult born levels and in some ways I think
*  that's a limitation of the tracking tracer tools that we have. But lately
*  there's been a bit of a renewed controversy around whether humans have
*  adult neurogenesis. Most people would say they do. Studies going back to the
*  late 90s from Rusty and Peter Erickson said this there have been more recent
*  works by Jonas Friesen and others that are looking at kind of radiation
*  tracking from above-ground nuclear tests in the 60s. You can use that to
*  track whether there are new neurons in different parts of the brain. And you
*  see that this happens in dentin gyrus in humans you know post-mortem tissue
*  using these radio labeling studies. So it's pretty convincing evidence but
*  there are a few groups that continue to publish fairly high-profile studies that
*  say it doesn't happen. So you know I'm not a molecular neurobiologist. I'm not
*  an expert on the tracer study you know limitations of different tracers and so
*  forth. But from what I can tell it does seem like you have a robust level of new
*  neurons in healthy adults. I think that if you have certain disease conditions
*  and certainly with aging there is a reduction of these new neurons. So you
*  know depending on what population of people you're testing you may not see
*  very many of them if any at all. But I think that it's probably safe to say that
*  most people listening to this are having new neurons integrating into their
*  hippocampus today. Thank God our hopes and our dreams hinge on this very fact
*  my friend. So help us all remember the conversation. That's right right. Okay
*  well so anyway so what work did you do? So when I started in Rusty's lab the
*  challenge really was what are these new cells good for? I had a colleague that
*  kind of related it as why would you wire a 747 in the middle of flight? It's kind
*  of a you know conceptually challenging thing to do. I'm going to plug new
*  neurons into a functioning awake active brain. And so there had to be some
*  computational reason for this. So I approached it by basically building
*  neural simulations looking at relatively biologically constrained models of the
*  dentate gyrus using thousands of individually modeled neurons using
*  different interneuron populations looking at grid cell inputs various
*  other sorts of inputs. So my thesis was really focused on what adding these new
*  cells into the circuit would do from a information theoretic point of view.
*  The kind of initial thought at the time and I think it's still kind of persists
*  is that the dentate gyrus is responsible for what's called pattern
*  separation. The idea that when you form a new memory you might have two concepts
*  that are effectively pretty close to each other. You think of a green apple and
*  a red apple. They're both apples but one might be more tart than the other. And
*  so we would like to have some way of actually encoding those differently.
*  Make sure that when you form your memory of whether you had an apple you encoded
*  as a green apple or red apple. You're not confusing those two things. And so
*  the dentate gyrus has long been associated with this pattern separation
*  function. And what was interesting about the work that my models kind of
*  produced in those results was that these neurons coming online changed how the
*  dentate gyrus did this pattern separation at least in simulation. And
*  there were a couple of key findings. One that I still like although I've never
*  found a good use for it is that the cells are active at an over a certain
*  finite period of time. So in a sense they kind of form associate allow you to
*  form associations of things that are contemporaneous with one another. So the
*  idea that if I hear a song that was a hit in 1986 I'm gonna think about a
*  vacation I did with my family in 1986 that the song was at the same time as
*  that vacation even though I may not have heard those that song during that
*  vacation. I'm gonna associate those two memories in time. It's because the new
*  neurons coming online overlapped with one another. So that's one theory,
*  the sort of theories that these models produced. The other one that I think was
*  more useful is that we really looked at how neurons could encode information
*  that was novel. The challenge if you think about that, I mean it
*  sounds almost trivial, but if you have a neuron that has thousands of inputs
*  that generally you don't want to fire unless it's responding to something
*  that's been trained to respond to, getting that cell to fire to something
*  novel is actually really hard because the brain is more or less wired not to
*  be noisy. I don't mean noisy in the sense that people see kind of
*  population activity that looks noisy, but rather you don't want neurons firing to
*  completely random arbitrary things. You want neurons firing in a reliable
*  predictive manner. And so how do you get a neuron that's fully formed that has
*  thousands of inputs that is generally inhibited to fire to something new? Turns
*  out that it's actually very hard. You can do some very simple models that say
*  that the sort of sensitive range where you can actually tune a neuron to fire
*  to something novel but not fire too much is very very narrow. Turns out these
*  young neurons actually are very good at responding to novel things. They're in the
*  sense like college kids without a major. They try out all sorts of new stuff and
*  then eventually they gain synapses and they refine themselves to whatever it is
*  they learn to fire to, but during that short period of time they're open to
*  novel responses and they're able to learn to fire to novel things. And that
*  finding actually has become a more directly tangible tool for use in kind
*  of further computational development. So this is a good segue then to fast
*  forward a year or two. I don't know how long this was simmering, but so then you
*  decide, huh, deep learning networks. Maybe they could have some new neurons too,
*  is that how it worked? Yeah, it's kind of the natural thing to do if you have my
*  background and you move into computing. So I'll say that when I first started
*  doing this Neurogenesis stuff, there were people doing neural networks in the
*  early 2000s, 2002, 2003, adding new neurons into trained neural networks and
*  showing that they could avoid something called catastrophic interference.
*  Yeah, so neural networks have this problem and this is the case of probably
*  any of the neural networks that people are familiar with today, deep learning
*  nets and so forth, that once they're trained up on something, if you keep
*  adding new information into those networks, you can either tell them,
*  okay, I don't want you to learn anymore. So you basically lower the learning
*  hard to train past a certain amount or you just keep adding new information to
*  these things and eventually all the things they've learned in the past just
*  collapses and you get this interference effect where they've added too much
*  information onto a network that just doesn't have enough capacity to handle
*  it. So people showed years ago, I mean two decades ago, that new neurons could
*  ameliorate this effect of catastrophic interference. But they never did it,
*  you know, they did it for kind of early 2000s neural net purposes, which of
*  course is completely different than the deep learning generation we live in today.
*  Connectionist models or something, right?
*  Yeah, absolutely. And these were, you know, they're good models and they
*  influenced me, but as far as I know, the people who did this stuff never
*  went into the deep learning field. So we were looking at deep learning kind of as
*  an emerging thing a number of years ago, it's probably been four or five years
*  ago now. And the idea that, you know, these deep learning nets, they, you know,
*  you train them on a lot of data and you might want to apply them to a new set of
*  a new world, right? Something that's slightly different than the world they
*  were trained up in. And that's exactly the case that we think that adult
*  neurogenesis in our brains is useful for. So if I want to do with this deep
*  learning model, what I do, what a human would do, and that is expose it to novel
*  information, novel context, how do I adapt that model? So we decided to
*  basically just do the simplest thing possible. Let's stick new neurons into
*  the deep learning nets. And of course, it has complications. These are deep
*  networks. Where do you stick those deep, where do you stick those new neurons
*  into? For instance, it's not, you know, there are a lot of things you can do
*  there. But then that's kind of the direction of research we took.
*  Maybe we can talk just a little bit about how, so you run into this multiple
*  issues, like you said, one of which is just how to train the network once you
*  add the new neurons. And my understanding is that the neurogenesis
*  training works based on essentially how wrong the network is, how big the error
*  is once you put a new, well, maybe you can just tell us how wrong or how big
*  the error is. So how does it work? And what did you find?
*  Yeah, so the challenge I think that you're alluding to is if I have the
*  ability to add a neuron to my network, when do I need to add that new neuron?
*  Right? When should a network just say, okay, I've, you know, here's a picture of
*  something, classify it as a dog or cat or whatever, or recognize that that's a
*  new class, that that's a dolphin and it wasn't part of my training set and I need
*  to adapt my network to handle it. And this is really the core problem of these
*  adaptive models. You know, we want our models to behave on data that's not part
*  of the training data. That's the reason they're useful. But if something's novel,
*  is it just a different point that would effectively be part of the training data,
*  but it just isn't? Or is it something that's completely different that my model
*  needs to change to? So what we did is we looked back on some of the early deep
*  learning literature, which were very much based on things like autoencoders.
*  And the idea of an autoencoder is my network will train a network to reconstruct
*  the input images. And these are pretty useful models, at least for an academic
*  study like we did, where it gives us a very clear metric of whether the model is
*  able to represent an input piece of data or if it just is failing at representing
*  that data altogether.
*  A really high level. You input an image into this autoencoder and then basically
*  it kind of compresses relevant features then to try to attempt to reproduce that
*  same image. Do I have that right?
*  Yes. And that's the basic idea of an autoencoder. You go from one layer that might have
*  a thousand neurons and you'll go through a few layers. You end up at a hundred neurons
*  and then you go back through that network until you get to the outputs, which are the
*  same as the input layer. And you get back to that thousand.
*  Okay.
*  And so it's a measure of lossiness in a sense is how much you can compress the data
*  and decompress the data and get back what you started with.
*  Gotcha. Okay.
*  So, you know, for neuroscientists who aren't familiar with deep learning and these
*  networks, lots of people are familiar with PCA and PCA is an effect that can be
*  thought of as an autoencoder where your neurons are just linear units.
*  Right.
*  And the idea of PCA is you go from a high dimensional space into some lower dimensional
*  representation and from that you can go back into that higher dimensional space,
*  that sort of compression and decompression and that can tell you how complex the sort
*  of lower dimensional structure of your data is.
*  Okay.
*  So these autoencoders are, you could think of it as a deep PCA that has some nonlinear
*  units in there. But what's nice about this is that you can actually do this sort of
*  step through as far deep into a network as you want to go.
*  So if I imagine I have a five layer autoencoder, I can actually go from layer one,
*  which is my input layer to layer two and I can go back to layer one and that tells me
*  how effective layer two is at representing the information layer one and I can go one,
*  two, three, three, two, one, one, two, three, four, four, three, two, one and just keep
*  going deeper and deeper in the network.
*  And what we found was that these networks that were constructed to represent handwritten
*  digits because everyone does handwritten digits as a first step in deep learning, you see
*  that, okay, the first couple layers tend to be, you know, they're looking at, you know,
*  effectively looking at things like edges and very low level structure.
*  So they just kind of do their thing.
*  So the idea would be that you go in and out and you measure how well that layer can
*  represent. Well, the first layer usually represents things pretty well, even if it's
*  novel because it's looking for fairly simple things.
*  But as you went deeper into the network, you start observing that I add a new handwritten
*  digit. Turns out my network just can't represent that anymore.
*  Three layers in. And so if it can't represent it three layers in, it certainly is not going
*  to be able to represent it five layers in.
*  And that tells us where you want to kind of focus adaptation might be three layers in.
*  And so we would then maybe add a new neuron or change the learning plasticity rates or
*  whatever at that third layer.
*  Haven't learned the new information.
*  And then we maybe fix the third layer.
*  And I would move on to the fourth layer and fifth layer and so forth.
*  So it's iterative.
*  Okay. Yeah, that's what I was going to say is iterative.
*  Yeah.
*  It becomes iterative process, but you end up identifying through this sort of autoencoder
*  structure where the network is beginning to fail.
*  So we don't need to spend too much time about it on this, but I'm just curious.
*  So did it become an automated?
*  Is there an algorithm to determine?
*  I mean, I guess there was an algorithm to determine, okay, add the unit now in this
*  layer if it triggers this big of an error.
*  Yeah. So we had basically an algorithm that was pretty heuristic based.
*  Of saying, you know, if your error passes a certain amount adds add a new neuron here
*  and then retrain.
*  And then we also had a component which did a version of replay similar to what we would
*  see in the hippocampus where you have kind of reactivation of neurons.
*  And we had this replay that was then used to kind of help train that new neuron and
*  make it make sure it plays nice with the existing neurons around it.
*  I must be making so many new neurons because I make so many really large errors.
*  Maybe maybe hopefully that's the case.
*  I don't know how that works.
*  Yeah.
*  No, I think, you know, I would suspect that the brain actually does this sort of thing.
*  Right.
*  I mean, we add new neurons and we plug them in and then if it doesn't work, they kill
*  them off and they put new ones in.
*  So, yeah, well, it's not it's not unreasonable to think that there's a we could come up
*  with ideas going back into the brain from this.
*  It's actually a recurring sort of worry of mine with this whole endeavor of like
*  building neuroscience concepts into into AI.
*  You know, obviously I'm all for using what we know about brains, you know, to build
*  better machines.
*  But for example, neurogenesis, right, you've already said like there's controversy
*  over whether it even happens and we, you know, we don't know exactly how it happens.
*  And this sort of our level of understanding of what's going on in brains is pretty
*  ubiquitous across almost any subject area.
*  When you come to the state of art in neuroscience.
*  And I wonder if we run the risk of sort of incorrectly implementing these concepts that
*  we think we understand from neuroscience trying to implement them into machines into
*  AI and if that's just going to run us into trouble at, you know, along the way.
*  Right.
*  Does that make sense?
*  It makes sense.
*  And I think it's a fair worry.
*  I would say that there's reason I think to be worried about it.
*  And there's a reason that we probably shouldn't be worried about it.
*  I'll start with the reason not to be worried about it.
*  I have found that the computing field, the machine learning field, the general computer
*  science field as a whole, you know, they don't care about how the brain works.
*  Right.
*  Right.
*  They care like anybody on the street does.
*  No, they'd like to know.
*  But ultimately what they want to do is they want to solve problems.
*  And so if I come, if someone comes with a neuroscience interpretation and it turns
*  out that from a neuroscience point of view, just isn't what happens.
*  It's just not what the brain actually does, but it changes how machine learning is
*  able to solve a certain task that no one had been able to solve before.
*  Then I think neuroscience actually is one because there's been an improvement in
*  the world, you know, we've been able to improve some capability of computing in
*  a way that would not have happened without neuroscience being there in the first place.
*  And I would almost guarantee you we see some stuff like that today.
*  You know, right now the machine learning field is running with reinforcement
*  learning and they're running with reinforcement learning on a interpretation.
*  I think of literature from the 80s and 90s that probably would make most
*  neuroscientists a little bit uncomfortable, but it's changing the way AI is
*  functioning and it's doing amazing things.
*  So I think we should embrace that.
*  And as a neuroscientist, I don't critique people for having the
*  implementations in these models not be perfect with how the brain does it.
*  So that's the reason I don't worry about it.
*  Yeah.
*  The reason that probably is worth worrying about is that while AI and
*  computer science and machine learning are very much focused on what works,
*  the neuroscience field, if we ultimately do want to get back and cure diseases
*  and so forth, which I think really is the goal of the field in a lot of ways,
*  it doesn't do any good to go back in and say, hey, the brain is a
*  giant deep learning model because deep learning is really effective at doing
*  these tasks that historically we've relied on humans to do because that's
*  not going to help us cure Alzheimer's.
*  Like I find it hard to imagine that a deep learning interpretation of
*  the brain is going to help us cure disease.
*  So I feel like as long as we're accepting of the fact that the AI
*  field and computer science field can use a abstracted course approximation
*  neuroscience and do great things.
*  We want to help that.
*  It's perfect.
*  But coming back the other way, we need to acknowledge the fact that there
*  was this sort of compression of knowledge going in that direction to begin with.
*  And I think that when computer scientists start telling neuroscientists
*  how the brain works, we need to be cautious.
*  Yeah, I agree with everything that you just said.
*  To me as I was talking with my friend just the other day and I was I pulled
*  the hey, I've got a PhD in neuroscience card and I said and everything I read
*  in the popular media or even in like popular science media about quote unquote
*  how the brain works is just wrong.
*  And and so it's what's really disappointing.
*  Of course, we were talking about this in the context of politics, but what's
*  disappointing is then what I know is that anything I read from any other field
*  with like these claims is that I know that that information is almost certainly
*  wrong.
*  Yeah, but we still take it as all as all right.
*  So as all correct.
*  So the headline will be like for this for this neurogenesis deep learning is in
*  Time magazine or whatever.
*  I don't know what the shows my age and I'm referencing Time magazine, but the
*  headline will be machines use what we know from neuroscience to improve learning
*  in such and such field.
*  But the the key nugget there is we don't actually know that in neuroscience.
*  So it's a it's an interesting cycle, right of having said that I do agree with
*  everything that you just said, but that's the neuroscientists frustration is no
*  we don't understand in fact.
*  Yeah, but you know, so I agree and.
*  I think the issue is based on what we do know or maybe what we what we think we
*  know, but know that we don't know perfectly.
*  Yeah, there you go.
*  There's some metacognition.
*  Yeah, what can we do with it?
*  Is there anything useful to do with this information right and we want to avoid
*  being in this sort of paralysis of perfection and the brains really complicated
*  if we insist on not moving beyond the hallowed halls of a neuroscience
*  institution into the real world until the thing is perfect, then the world's
*  going to bypass the community.
*  Right.
*  Yeah, and I actually think in the case of computing we see this where the
*  neuromorphic community and the machine learning community both they just
*  doing stuff without neuroscientists really telling them what they could do
*  and why they should do it because the neuroscientists were busy fighting with
*  each other, you know, and I was part of that about, you know, what a place
*  cell is for instance, and that's fine.
*  I think as a community we need to always be trying to improve on what we
*  understand what we do, but when we have an opportunity to export knowledge with
*  all the caveats that may need to go with it, but we have the ability to
*  export some sort of insight into how computation works or into how the
*  brain might be treatable for disease or whatever.
*  We need to embrace that opportunity and not not become paralyzed by
*  self-imposed requirements that we have it entirely right.
*  I think this is a really good example.
*  This neurogenesis deep learning of a real advantage.
*  Well for all of us that someone like you went from academia into this
*  more computing space and this is a great example of building in something
*  related to neuroscience and trying it out to solve problems.
*  So I mean along the lines of what you're just saying this just serves as one
*  of the one of many examples, I think but it's it's cool work.
*  So nice nice job.
*  Thank you.
*  Sammy, Jonathan, Pihong, your souls will be going directly to heaven when you
*  perish if you don't upload your souls to the internet, of course, I mean,
*  not that you'll ever perish.
*  Anyway, thank you for supporting the show.
*  This show depends on and runs on your support.
*  I don't do ads to try to sell you mattresses and so on.
*  Although I do love my mattress.
*  Maybe I'm laying on my mattress right now.
*  Anyway, you can support the show for as little as two bucks.
*  Go to braininspired.co and click on the red Patreon button there.
*  So let's transition just a little bit toward the neuromorphics and this is
*  actually the original thing that was the impetus for me to contact you and
*  research what you're doing and that's the wet stone method.
*  So this is another recent project that you've worked on and it's basically a
*  way to take a normal deep learning network and transform it into a spiking
*  neural network so that it can be used on neuromorphic hardware and we'll
*  unpack that in just a second.
*  Well, I don't think that I've ever I don't think I've had any guests that
*  I've talked with on the show about spiking neural networks yet.
*  So this is exciting.
*  So for clarity, what's the difference between traditional deep learning nets
*  and spiking neural networks?
*  Yeah, so deep learning nets and probably 99.99% of artificial neural nets
*  that have ever been made don't have the sort of intrinsic dynamics, the
*  activations that we see in neurons in the brain.
*  Yeah.
*  So neuroscience audience, everyone knows that neurons have action potentials.
*  They're fairly complicated biochemical mechanisms by which you know, you
*  get Hodgkin-Huxley dynamics and so forth.
*  Yeah.
*  But even if you simplify that and you have like an integrating fire neuron,
*  it's just okay, my inputs cross the threshold.
*  I get a spike and that spike propagates down an axon to other neurons.
*  You know, that's what neuroscientists learn from day one, basically.
*  On the other hand, artificial neural networks really are nothing like that.
*  They have neurons that are, you know, nodes or neurons, whatever you want to
*  call them, they're connected to other neurons, but they aren't sending
*  spikes in between them.
*  They're basically sending some sort of continuous value.
*  It may be it's a sigmoid activation function.
*  The trendy thing these days is a rectified linear unit where, you know,
*  above a threshold, I send some value and that value can be from zero to
*  infinity based on how far over the threshold I am.
*  Yeah.
*  And so whether it's a sigmoid or a rectified linear unit or, you know,
*  pick whatever function you want to use, it doesn't really matter.
*  But the deep learning field has made a lot of progress in this sort of
*  continuous valued view of how neural networks can work.
*  And that's great.
*  And they've been very successful.
*  So I'll just let me just interrupt us to be like super, super ridiculous.
*  But one way to, I guess, not visualize, but audit to realize this would
*  be like a deep learning that the units communicate with something like
*  doooo.
*  Whereas in a spiking neural network, they communicate with pop, pop, pop,
*  pop, pop.
*  Would that suffice you think?
*  That's right.
*  And I'm glad you did that.
*  Not me.
*  Yeah, well, yeah, no, I think that's exactly what happens.
*  And from an information theoretic point of view, the continuous valued
*  neurons are better.
*  They there's more information encoded in those neurons.
*  I see.
*  And we see that even in the case of biology, C elegans, retinal, pre
*  ganglion cells in the retina, you know, like bipolar cells and cones
*  and rods.
*  They're all more or less continuous valued.
*  So the issue is not that spikes are better per se.
*  But what ends up happening is that our brains, I mean, I think from a
*  theoretical point of view, why would our brains use spikes when continuous
*  valued neurons are more information rich is that the spikes actually
*  confer very strong signals of noise benefits and very strong energy
*  benefits and using things like temporal coding of when the spike happens.
*  You can recover a lot of that missing information that that was in the
*  continuous value.
*  So neuromorphic hardware, you know, there are several ways of doing
*  neuromorphic hardware.
*  But one of the ways that's been really successful in the last 10 years
*  and IBM has been leading this with their true North chip.
*  Intel has their Loihi chip human brain project has a number of chips
*  Spinnaker and a brain scales chips.
*  And they all use spiking as a mode of communication.
*  And the reason they use the spikes is that you're sending an event.
*  You're sending a one or a zero, but usually only send the ones if it's a
*  zero, you don't send anything right and that's incredibly energy efficient
*  because you're just not moving information around.
*  You're just sending a one every once in a while.
*  Just like you say a pop and that's enough.
*  Is the is the energy efficiency is that the main impetus behind these
*  big corporations developing these neuromorphics or is it is it
*  multifold?
*  I'd say energy efficiency is the most immediate reason for doing it.
*  Okay.
*  You know, there is a hope that by building hardware in the shape of how
*  the brain functions or kind of is structured, let's say novel capabilities
*  and algorithms could come in and change how we use computers.
*  That's I say a medium to long-term goal.
*  These are like their research and development parts of their company
*  that have this longer term investment with a longer term return on that
*  investment in their vision.
*  Yes.
*  Yeah.
*  Most of it is not trying to make money today.
*  They're trying to make money, you know, 10 years from now.
*  Right.
*  And there are some deeper reasons why energy is increasingly a
*  concern to these companies.
*  I see.
*  Yeah.
*  Sorry for the interruption.
*  I just curious.
*  Yeah.
*  And I can talk about that the energy that the reason why you want to
*  push energy in a minute if you want.
*  Yeah.
*  Well, let's cut.
*  Let's come back to it.
*  Okay.
*  So the benefit of going to spiking neural networks is that you
*  potentially could represent your deep learning model and something
*  that is more energy efficient.
*  So it would be you're able to do it instead of taking a hundred
*  watts or a thousand watts or even more.
*  We're able to do something at maybe a few milliwatts.
*  That's the that's the dream.
*  That's the hope that would take advantage of these neuromorphic
*  chips that can operate those sort of scales.
*  So the deep learning field uses these continuous value neurons
*  partially because they're information rich, but partially
*  because things like back propagation work well require having
*  continuous valued neurons.
*  Right.
*  And spiking is not strictly speaking continuous valued.
*  Hodgkin-Huxley neuron would be but that's incredibly complicated
*  and integrating fire neuron is not where you hit a threshold that
*  threshold causes some discontinuity in the response.
*  Yeah, this beautiful back propagation algorithm that's so
*  useful is just people are still trying to figure out how it could
*  work in brains and spiking networks.
*  I know there's a lot of work being done for that.
*  So yeah, and I think it's a lot of the field is focused on how
*  do we make back propagation compatible with spiking.
*  Yeah, and there's been a number of good studies.
*  A lot of them by theoretical neuroscientists who've been going
*  in that direction.
*  Let's make back propagation useful for for spiking systems.
*  And we thought about that, but we decided to maybe go a different
*  way.
*  And this is where you know, we kind of said, okay, let's set
*  aside the neuroscience details for a second and let's come up
*  with something that might be useful for computing fields.
*  We want to target something that's brain-like in its final
*  form, but not necessarily take the brain like path to get
*  there.
*  So if the neural networks require continuous valued neurons
*  in order to train them, but we want to end our end result to
*  be discrete values spiking neurons at the end.
*  Well, what we decided to do and this was really my colleague
*  William Savera who came into my office one day with this idea
*  and it just made total a lot of sense and we went and implemented
*  it.
*  Is that let's take a neuron.
*  Treat it as a continuous valued neuron for most of the training.
*  So, you know, if we think about a sigmoid where you have something
*  that starts off at zero, it gradually increases to one and then
*  tapers off towards one and you have this, you know, the width of
*  that sigmoid is kind of your dynamic range over which your
*  neuron can be trained.
*  What we decided to do is we start, you know, we train it with
*  kind of a standard initialized network and then gradually sharpen
*  those activation functions.
*  So by sharpen, I mean that the range by which it's zero or one
*  becomes closer and closer together and this sort of range where
*  it's a value between zero and one which would be the area that
*  the neuron can learn just gets tighter and tighter.
*  Eventually, that's just going to hit a discrete step function
*  activation, which effectively is like a spike of the spike.
*  Yeah, perceptron would be the computer science term, but in a
*  spiking sense, it's the same thing.
*  And so we just gradually sharpen these networks and that's why
*  the name whetstone came about because use a whetstone to sharpen
*  a knife and we're using whetstone method to sharpen these neural
*  networks.
*  Nice.
*  Okay, gotcha.
*  And you know, it was something that was I think an interesting
*  idea.
*  It was something that we thought could work, but there was really
*  no theoretical reason why it should work.
*  But it does work.
*  Yeah.
*  And one of the things that was really nice is is that we've
*  gone in and looked at lots of different configurations of
*  networks, several different tasks.
*  So not only image classification, but things like reinforcement
*  learning as well.
*  And it turns out that this process of gradually changing the
*  activation functions to fit the requirements of the hardware,
*  and in our case, that's requiring a spike.
*  It works and there's, you know, no reason that this can't be
*  extended to other sorts of constraints that one might experience
*  in a real-world use of a neural network.
*  If I want to just gradually train my neural network to fit any
*  sort of requirement, I incorporate that requirement into my
*  training process.
*  So we've been excited by it because it actually seems like it
*  might bring neuromorphic hardware technologies to actually be
*  able to use deep learning algorithms, which everyone talks about,
*  but no one's really been able to do yet.
*  Well, so is the advantage.
*  Okay, so the way it works is you take the an untrained network
*  and you start training it like your run-of-the-mill deep learning
*  network on these continuous values and through the training you
*  sharpen and then eventually end up with spikes, essentially, and
*  then it's ready for the neuromorphic chips.
*  But does it continue to learn after that or then you have a
*  completely trained network that then you just run on the neuromorphics?
*  So it would be a completely trained network that you just can
*  plop onto the neuromorphics at that stage.
*  You know, you can't really train it anymore unless you have one
*  of these algorithms like a back propagation version that's able
*  to handle discontinuous activation functions.
*  But if you had that you would just train it from that like that from
*  the beginning, I guess.
*  Probably.
*  Yeah.
*  And it turns out that for most applications, the sort of trained
*  network is the sort of thing you'd want to accelerate.
*  So you can spend a lot of time training and the training is
*  actually quite expensive.
*  Yeah, but once you've trained it and you want to stick it into
*  something like a self-driving car, for instance, or a cell phone,
*  you know, pick one of these sort of embedded applications where
*  power might be the requirement, but you're probably not going to
*  want to adapt your model continuously.
*  You know, that in theory, you should be able to just put a neuromorphic
*  chip on your cell phone, put whetstone trained algorithm on that
*  and you'd be able to, you know, do face recognition or something.
*  And then eventually maybe you update your model the way we update
*  you know, maybe update your maps on Google Maps or something.
*  So that would be the idea.
*  But we're really training what's called the or we're really developing
*  a neuromorphic version of what's called the inference mode of the
*  deep learning algorithm.
*  So not the training process, but just the operation of the trained
*  network.
*  I see.
*  So is this ongoing work?
*  I mean, are we going to start seeing these things cropping up here
*  and there or what?
*  Yeah, so we've you know, we're moving towards I guess both in terms
*  of a where can whetstone go?
*  We're putting it on different neuromorphic platforms.
*  We've implemented it on several of the European platforms, Spinnaker
*  in particular and hoping to get those kind of on the existing kind
*  of suite of technologies that are out there today.
*  And then from a more theory point of view, we're starting to ask
*  some questions about how can we use whetstone for maybe some of
*  the more challenging networks and then maybe get to some of the
*  questions you were asking, which is, you know, how can I maybe
*  change a whetstone that train network and have it learn, you
*  know, is there a way to combine this with some of the ideas of
*  the neurogenesis deep learning for instance?
*  So there are some ideas of how we might be able to adapt these
*  things, how we can extend whetstone to be able to do some more,
*  you know, maybe more sparse networks.
*  One thing that we don't do, which the brain certainly does, is use
*  the time dimension of when a cell spikes as part of the encoding.
*  Whetstone converts everything to 0 or 1, which has the benefit
*  that your neural network runs at the same speed that it would
*  have run in a continuous mode.
*  But it has the downside in that we're not really using the
*  fact of when the cell spikes as a carrier of information.
*  Our brains carry information presumably as much of whether a
*  cell spikes, but when the cell spikes and that's less of a
*  feature of whetstone today.
*  So we want to kind of get some of that neuroscience insight into
*  the algorithm going forward.
*  So has it just occurred to me?
*  Is it mostly used in feed-forward learning nets or are there
*  recurrent neural networks that it's also used with?
*  You bringing up the time aspect made me wonder about this.
*  So we've mostly done it on feed-forward nets.
*  We've done a little exploration on recurrent nets and I think
*  that's where we'd really want to have some more explicit
*  representation of kind of spike time as part of that.
*  Gotcha.
*  In the current nets.
*  That's kind of where we see some of the opportunity going forward.
*  Oh, cool.
*  Well, let's transition here and you know, we've talked about
*  these neuromorphic chips.
*  I want to learn a little bit more about NICE, the neural
*  inspired computing elements workshop that you've been doing
*  for what seven years now?
*  Is that right?
*  Coming on seven years, maybe eight years at this point.
*  Yeah, I think we just had our seventh.
*  So just tell us what it is and kind of where you are now with
*  the workshop versus where how it began, you know, where what
*  kind of attendance it was, what kind of people were attending
*  versus what kind of people are there now and etc.
*  So NICE started as a Sandia led workshop and the goal was, you
*  know, bring people together who are interested in neural
*  inspired computing.
*  But not be kind of only hardware people or only application
*  people or only theoretical neuroscientists, but rather bring
*  people kind of from across the landscape.
*  We want something really interdisciplinary.
*  And you know, we did it for entirely selfish reasons initially,
*  which was awesome.
*  You know, we were trying to build up mindshare within the
*  national lab community and Department of Energy who runs
*  the national labs, you know, kind of say, hey, this is an
*  area that we should be investing in and thinking about going
*  forward.
*  And what ended up happening was, you know, we partnered with
*  Carl Heinz Meyer, who unfortunately passed away last year,
*  but he was one of the heads of the human brain project on the
*  neuromorphic side.
*  So he led the brain scales effort and helped bring, you know,
*  worked with Henry Markram and others to get the human brain
*  project off the ground.
*  And he brought a lot of that enthusiasm out of the EU into
*  the workshop and we were able to get other members of government,
*  you know, NSF, DOE, other agencies coming here as well as
*  various academics and national lab partners.
*  So it was really sort of interdisciplinary from a technical
*  point of view as well as from a, you know, at the time,
*  especially a programmatic point of view.
*  So we had researchers, we had funding agencies, and it was
*  basically just kind of bring a bunch of people together and
*  figure out where this field was.
*  Is it ready for prime time yet?
*  So it's evolved from that in that I think we've become more
*  of a conference as opposed to a workshop and I think we're
*  probably going to change the name in a year or so to actually
*  be a conference because what's happening is that we bring
*  people in and, you know, usually it was invite only and eventually,
*  you know, people started saying, well, I'd like to come.
*  Can I come present on this work or, you know, I have this
*  grad student who's interested in learning about this, you know,
*  can I bring this person along as well?
*  Yeah.
*  Then people started saying, you know, I'd like to be able to
*  publish papers at this workshop and we weren't set up for that.
*  Like abstracts and stuff.
*  So sending in abstracts but in the computer science field and
*  the electrical engineering field, people publish at conferences
*  by and large.
*  Yeah.
*  And of course, you know, that's not what I do or had done.
*  So it wasn't that we had thought about that from the start, but
*  it was the community really started nucleating around this
*  workshop that we've, you know, I think all of you know, a lot
*  of people have come most years now.
*  There's a kind of a good contingent of people that make it
*  there every year and we've been trying to trying to open up
*  and reach out to people who are more neuroscientists or maybe
*  more different application areas that might benefit from this
*  machine learning field, for instance.
*  And we tend to do a pretty good job of I think having at least
*  several invited speakers who really are not part of the
*  neuromorphic community come in, inject some insights and
*  knowledge that may have been kind of unfamiliar to people in
*  the community.
*  So I try to always get some neuroscientists maybe come in
*  computational neuroscience side that can come in and say, you
*  know, the active thought in the in the neuroscience community
*  is pointing in this direction.
*  You all need to probably move away from thinking of everything
*  in this way or whatever.
*  So in that and that's been pretty good.
*  I think we've had some good speakers over the years.
*  Most of our talks are online.
*  So if you look up nights workshop.org, there are links to
*  a lot of videos of talks over over the different workshops.
*  I was going to say that and that one of the more entertaining
*  I mean, there are a bunch of good talks from individuals, but
*  I really like the panel discussions where it's a bunch of
*  the speakers sitting around passing the microphone back and
*  forth kind of giving their thoughts on the day, but also
*  taking questions from the crowd.
*  So I really encourage people to I mean, of course I'll link to
*  it in the show notes to go check out the videos, which is
*  just a great resource.
*  And and yeah, it's it's interesting to see the different
*  backgrounds coming together and interacting.
*  So yeah, no, I appreciate it.
*  The panel discussions at the end of the day is probably the
*  most entertaining part at least for me every once in a while
*  you have to rain people in they get a little carried away, but
*  we've had some really good ones over the years.
*  There are certain attendees that are very vocal and their
*  views of how things work and should work and makes for some
*  interesting conversations just to highlight sort of the
*  variety of people there was you know, one one this is very
*  specific example, but a guy stood up to ask a question.
*  I don't know who it was and he said, you know, my background
*  is in neuroscience, but then I went into artificial
*  intelligence and then I went into neuromorphics and then
*  you know, so it's like he encapsulated all of the people
*  that are there in one person sort of, you know, and so so
*  it's a really it's a it's a cool I guess soon-to-be conference
*  that I will hope to go to it's interesting.
*  I almost this year went to the Telluride neuromorphic
*  cognition workshop which is held in Telluride Colorado
*  and I've been in touch with a few of the people behind
*  organizing that and there must be some overlap between NICE
*  and the Telluride conference.
*  Yeah, so there's a lot of common attendees.
*  Yeah, so Telluride which I've never been to and I really
*  would like to go in one of these years gets up the mountains
*  from us from us down here.
*  But the my understanding of Telluride is that it's very
*  focused on kind of a two or three-week long hands-on
*  building neuromorphic systems learning how to write algorithms
*  and design kind of neuroscience capabilities into hardware.
*  Yeah, so it's a very interactive I'd say almost
*  training experience that you know for people that say
*  a graduate student or postdoc stage of their career can go
*  in and really become fluent in a lot of these neuromorphic
*  technologies and so I've heard only amazing things about
*  Telluride.
*  A lot of the people who run Telluride have come to NICE
*  over the years and they present their work often showing
*  kind of here's some demos that were made at Telluride by
*  these teams and so it is an overlapping community.
*  The neuromorphic field as a whole is not very big, you know
*  in terms of people who are actively working in this area.
*  It's still pretty small.
*  So it's kind of an opportunity fun growth period for this
*  field.
*  What's your take?
*  I mean, so you've been doing this for years now.
*  What is your take on the dynamic between people from the
*  academic world and these sort of more industry folks more
*  hardline computer focused computing focused folks.
*  I mean, do they interact?
*  Well, do they get along?
*  Is there often strife and from which side does that strife
*  come from come from?
*  Yeah, it's interesting and in being in a national lab, we
*  sit really on the fence between those and you are especially
*  given your background.
*  So yeah, do you moderate fights?
*  Do you you know, well, I like to think that I can I can
*  talk to both crowds.
*  I don't know if I'm good at moderating the fights.
*  You know the thing that is interesting and I think this
*  is something that neuroscientists don't necessarily
*  appreciate until you get out into whether it's an industry
*  world or computer science world is how much application
*  and sort of performance matters.
*  Yeah, compared to what is kind of intrinsically interesting
*  from a scientific point of view.
*  That's a good distinction.
*  Some people are obvious about when they say something is
*  interesting because I care about applications or it's
*  interesting because I care about just how the brain works.
*  Other people don't tell you, you know, they just get
*  hostile.
*  It's an interesting thing and it's a dynamic that I think I
*  would say that most neuroscientists probably need to think
*  a little bit more about as they start reaching out into
*  machine learning worlds or computer science worlds industry
*  and so forth because you know, most of these people are very
*  smart.
*  You know, if you're in industry and you're running a research
*  lab doing a multi-million dollar project on whatever they're
*  very smart.
*  They're intellectually curious people and they do care about
*  how the brain works and why the brain works the way it does
*  but their bottom line the reason they have a job the reason
*  they're at that meeting is because they're trying to come
*  up with a solution for a problem.
*  Yeah, you know, it's actually not that different than when
*  I was at the Salk and working in Rusty's lab as a grad
*  student and we would talk to people from the Christopher
*  Reeve Foundation where you know spinal cord injury researchers
*  and the people at the Foundation they were interested in
*  curing a disease and at the point where your research when
*  you're giving a talk and your research started to be about
*  well, you know, it's really interesting how this gene
*  interacts with this gene or why this molecular pathway does
*  this and what they're all of a sudden you see them tune out.
*  Yeah, because they're like this is not curing this disease.
*  This is not curing spinal cord injury.
*  It's not curing depression and the same thing happens in
*  machine learning and neuromorphic computing.
*  At some point people have to make money off of this.
*  Yeah, who the hell cares about serotonin they'll say for
*  instance.
*  Yeah.
*  Yeah.
*  I love serotonin but you know, it's hard to defend it sometimes
*  sure.
*  Well that just picked that out of the hat randomly but yeah.
*  Okay.
*  Again, that is the first part of my conversation with Brad
*  I'm an E in the next episode.
*  We'll pick up right where we left off and go on to talk
*  about how what we're learning about brains could be the key
*  to progress in computing beyond Moore's law, which is slowly
*  dying plus all the usual tangents and such.
*  All right.
*  See you then.
*  Brain inspired is a production of me and you you can support
*  the show through patreon for a microscopic to or $4 per month.
*  Go to brain inspired co and find the red patreon button there.
*  Your contribution will help sustain and improve the show and
*  prohibit any annoying advertisements like you hear on
*  other shows to get in touch with me email Paul at brain
*  inspired co the music you hear is by the new year find them
*  at the new year net.
*  Thanks for your support.
*  See you next time.

---
Date Generated: May 27, 2024
Transcription Model: whisper medium 20231117
Length: 7155s
Video Keywords: []
Video Views: 3648
Video Rating: None
---

# The AI Revolution in Biology: From Vaccines to Protein Engineering, With Amelie Schreiber
**Cognitive Revolution:** [May 25, 2024](https://www.youtube.com/watch?v=_YEk0YAd-cw)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution. Today I'm speaking with Amelie Schreiber,
*  a computational biochemist and AI researcher working at the forefront of applying the latest
*  AI models and research techniques to some of the most complex and impactful domains imaginable.
*  Drug design, protein network engineering, and broadly unlocking the secrets of biological systems.
*  In all honesty, this episode has given me more future shock than perhaps any other episode we've
*  done. While traditional analytical methods are not well suited to the crazy complexity of biological
*  systems, and as a result there's still much more that we don't understand about biology than that
*  we do, as Amelie makes clear, modern AI architectures are perfectly suited to take advantage of biology's
*  massive data sets. And thus, a new wave of AI models are poised to dramatically accelerate the
*  process of scientific discovery in biology. Starting with how we understand protein and
*  other cellular structures and the physical interactions between them, and likely soon
*  zooming out to help us understand how our cells, tissues, and bodies function at higher levels.
*  As you might expect, given the incredible complexity of biology, if you're not already
*  well versed in the subject, the first hour will feature a number of new technical concepts. And
*  while Amelie and I do our best to explain them all clearly, this episode, for me at least,
*  did require multiple rewinds for full comprehension. I think it might help to keep in mind the
*  distinction between static structural analysis and dynamic conformational analysis, which allows for
*  molecules to change shape as they interact with one another as you listen. Remember too,
*  that all the models we discussed today are really rather narrow in scope. Foundation models for
*  biology, along the lines of the LLMs that many of us are most familiar with, are just now starting
*  to be trained. One upshot of this is that we discuss different models for predicting shapes
*  versus for predicting sequences. Obviously, in reality, these are two sides of the same coin,
*  but for our purposes, they are often modeled separately. In the second hour, we discussed
*  the implications of all this for human health, longevity, and biosecurity. I had heard, as you
*  probably have, the story of how the first COVID vaccine was designed in just a few days after the
*  right scientists received the required information, but I had never really considered what the world
*  might look like if that pace of medical R&D were to become the norm. The impact would seem to be a
*  near certain revolution, not just in biology, but also in practical medicine. One particularly
*  striking theme is the potential for AI to change the way that we do biological research on humans.
*  The difficulty and danger of experimenting directly on humans has always been a major bottleneck,
*  but the latest models are quickly approaching the point where we should be able to run meaningful
*  digital experiments, and that could radically accelerate the pace of discovery, both for the
*  utopian better and at least with some probability, perhaps catastrophically, for the worse.
*  And all this, by the way, was before Alpha Fold 3, which dropped shortly after we recorded,
*  and which will certainly get its due attention in future episodes. With the full range of
*  possibility in mind, and noting just how small many of these biology models are relative to
*  the latest language models, I definitely want to give a shout out to the policy wonks at the White
*  House who set a lower reporting threshold of 10 to the 23 flops for reporting on biological models
*  as compared to 10 to the 26 flops for language models. That and their recent policy requiring
*  DNA synthesis companies to screen orders against known dangerous sequences are looking extremely
*  smart right now. By comparison, the now familiar question of whether today's chat bots are more
*  helpful than Google for the purposes of making a bio weapon to me, honestly, already feels quite
*  quaint. For what it's worth, because the vision of the future sketched out here was so far outside
*  my previous understanding, I did take some time to double check my high level interpretation of
*  Amelie's claims with some very credible people in the field. One of my very smartest friends,
*  who is also most deeply enmeshed in these issues, said simply, that is exactly what is going to
*  happen. If you find this work valuable, I would appreciate it if you'd take a moment to share it
*  with friends. This episode in particular took a lot more work than a typical CEO interview,
*  but it will be very well worth it if I can help our high value audience get up to speed on such
*  a critical area. And as always, we invite your feedback and suggestions either via our website,
*  cognitiverevolution.ai, or by DMing me on your favorite social network. Now, I hope you enjoy
*  this introductory deep dive into a genuinely awesome area of emerging research that may
*  soon impact all of our lives. This is the AI Revolution in Biology with Amelie Schreiber.
*  Amelie Schreiber, computational biochemist and AI researcher, welcome to the Cognitive Revolution.
*  Nice to be here.
*  I'm excited for this conversation. I expect to learn a lot from it. This all started with a tweet
*  that I saw you put out where you said, here are my top 10 AI tools for biology. And I read down the
*  list and I was like, I don't know what any of these are. So I think pretty much immediately just say,
*  hey, would you be interested in educating me in the form of a podcast? So I appreciate you taking
*  the time. You want to start off by just giving a little bit of context on who you are, what you're
*  doing day to day and what kinds of problems you're trying to solve. Yeah, sure. I'm an AI
*  researcher and I focus on computational biochemistry applications. I actually started
*  out as a mathematician. My training in grad school was in mathematics, actually. I started
*  off with pure mathematics and then transitioned into applied mathematics and data analysis. And
*  then after grad school, I got into deep learning and started working on more AI related things.
*  For me, the biochemistry applications are one of the most compelling things that we could be working
*  on right now. I think other than like AGI, whatever that means, I think it's probably the
*  most important problem we can be working on because it's a huge impact on human health.
*  The applications are really profound and have the potential to be very impactful for everyone. So I
*  get really excited about the biochemistry applications of AI. I have some projects and
*  things that I'm working on that are more related to environmental things and material science type
*  applications. But primarily, I focus on the medical or biomedical aspect of things.
*  Okay. So let me try to give an extremely high level understanding of a couple of the
*  biggest problems that are being studied in biomedical sciences. As I was preparing for this,
*  I was having a good conversation with Claude 3 about it. And I came away with the understanding
*  that both at the level of an individual cell and then again, at the level of the overall
*  organism system, we have one really massive challenge, which is that we don't know how it
*  works. We've got the DNA, which is the code, the RNA, which is both messenger, but also is a
*  machine. The proteins are all machines that fold up in weird ways and interact with each other in
*  three-dimensional space. And then you've got the small molecules as well, which are like signaling,
*  but also if they fit right, all these puzzle pieces fit together in super strange ways.
*  There's this incredible network of interactions where things are disabling each other or promoting
*  each other or interacting in all sorts of complicated ways. The nature of those interactions
*  initially was entirely unclear. And now humanity at large has embarked on this grand project of
*  trying to figure out how do cells work and how do our bodies work. And I'm gathering we're like
*  maybe 5% to 10% of the way there. Most of the interactions remain unknown to us, but we've at
*  least mapped out a decent chunk. So the first challenge, if you're trying to solve a disease,
*  is figure out what is the pathway? What is the interaction in this super complicated thing
*  that is going wrong? And then the second challenge is if I know what is going wrong,
*  can I do something to intervene to stop it? But then again, there could be a lot of other knock
*  on effects. And in that way, there's an important commonality with large language models. These
*  things are not super clean. When language models, people are probably familiar with the notion of
*  superposition, which is when one activation in a network can light up for multiple different
*  reasons. And you certainly see all of these kind of patterns of complexity in biology as well.
*  But we know that there's a lot of stuff going on. There's a lot of interactions that are happening.
*  We don't really know a lot about that, but we're gradually learning more all the time.
*  And then if you do have a target, now it's okay. These are all three dimensional spatial things.
*  And so it's just extremely, extremely difficult. It is. Yeah. How am I doing there in terms of just
*  setting a foundation to understand the challenges? I think you've really hit the nail on the head. I
*  work with a lot of different kinds of molecules. So small molecules, which are your drugs that
*  take in a pill form, these are smaller than proteins and less complicated. And I also work
*  with proteins and also a little bit with DNA and RNA. And understanding protein interaction networks
*  is a very difficult and complex problem. To just determine whether or not two proteins interact
*  with each other already is a hard problem. And then modeling how they fit together when they
*  do interact and understanding the strength and how transient that interaction might be,
*  it's very difficult. So protein interactions especially, but also protein DNA, protein RNA,
*  protein small molecule interactions are all very complicated things to model.
*  There are some new ways to address this that have come out recently that I have a lot of hope for,
*  that I think are very promising, very effective approaches. I use various kinds of AI tools,
*  analyze these molecules, create new ones, modify them, engineer them in ways, grafting them together
*  and stuff, performing complicated operations on these molecules so that they perform a particular
*  kind of function. As an example, designing a new protein to bind to another protein so that you can
*  cause some kind of cascade event in a protein interaction network or so that you can block
*  certain interactions between proteins. A really good example in cancer, your basic first examples
*  of a mechanism of cancer, there's PD1 and PDL1. These are two proteins. One of them's located
*  in the cancer and one of them's located on your immune cells. What happens is these two proteins
*  end up binding to each other. And essentially the cancer turns off your immune cell so that your
*  immune cell doesn't attack the cancer. And that's not good, right? You don't want this kind of
*  interaction between these two proteins because you want your immune system to recognize the cancer
*  and destroy it. Having this interaction turns off your immune system in a very specific way.
*  So you can do things like design binders to this protein to block that interaction and that can
*  help you combat cancer and hopefully treat it. And that's just one basic example of something
*  that you can do with these tools that I'm using and that I'm interested in. You can also design
*  new drugs with them. You can design drugs that are specific to a particular binding pocket on
*  a protein. You can design drugs that have very specific chemical properties. You can design
*  proteins that have very specific chemical and functional properties. And this is pretty new
*  stuff, but you can also do a lot of the same things with DNA and RNA molecules as well.
*  Okay. This is a paradigm shift, right? The application of AI to biology, obviously AI is
*  creating all sorts of paradigm shifts, but I think it might also be helpful for people to
*  understand a little bit better the before state when we didn't have any of these tools yet,
*  which is not that long ago. Not that long ago. Yeah. What was the sort of prevailing approach
*  to figuring stuff out? You hear these stories of, oh, look, we found this frog in the rainforest
*  that is immune to a certain disease. What's going on there? Let's see if we can't find something
*  in this frog. That could be a medicine or whatever. It's really anecdotally special observation
*  motivated investigations in a lot of cases. And then I know there's also just a lot of brute
*  forcing where it's like, we have no idea which proteins are going to interact with which other
*  ones. So let's just create this massive cross matrix and see if we can't figure it out that
*  way and look for hits. Kind of massive assays, just exploring the space. All of these things
*  without any idea of what the puzzle pieces actually look like, which makes it obviously
*  very difficult to figure out how they would fit together. What more would you tell people
*  who want to understand, okay, what was the before before all this stuff started to come online?
*  There's a lot of methods that come from wet lab work where people do this stuff in animals. Like
*  they say you want to do directed evolution on a protein and try to find higher functioning
*  variants or variants that are more thermostable that have higher expression or something like
*  that. You can mutate these things in a lab. You can do like point mutations or you can do
*  two mutations at a time, or you can do multiple. But when you start adding in things higher than
*  just single point mutations, you get this combinatorial complexity, right? And so it
*  gets really unwieldy. I feel like my experience with traditional methods is somewhat limited.
*  I don't come from a wet lab background. I come from a very computational background.
*  I haven't spent a lot of time working with more traditional methods that people have used
*  historically. So computationally, traditionally, the way that this sort of thing was approached
*  was through molecular dynamic simulations. You have what's called a potential and this potential
*  tells you how the dynamics evolve. And is that basically like a energy potential diagram? Help
*  me pin down the ground truth. Yeah. Observing the dynamics of a protein is really hard.
*  The ground truth ultimately is the Boltzmann distribution, which is this theoretical physics
*  idea that comes from statistical mechanics. It's a probability distribution. And you can think of
*  it in terms of an energy landscape, the low parts, the valleys that you have in your energy
*  landscape are going to be the metastable states of the protein. And then the peaks, like on top
*  of the mountains, right? These are states that are very transient and that are unlikely to exist
*  for very long. So when you're trying to model the Boltzmann distribution, you're trying to get out
*  these low energy confirmations from it. And then the transitions between those and understanding
*  how often you transition between this state and this other state and what that transition looks
*  like. This is all part of the dynamics of the protein in the environment. And so I guess the
*  answer to your question is the ground truth is the Boltzmann distribution. Whether or not you can
*  model that on a computer or observe that in a lab is another question, but the Boltzmann distribution
*  of the protein is the ideal ground truth. So it's a probability distribution of what percentage of
*  the time the protein in some solution or whatever is in shape A versus shape B versus shape C.
*  So in terms of just a little intuition for the shapes, I envision a slinky where if I just
*  sit the slinky down on the floor, it will come into a pretty tight coil. And that you might say
*  is like its lowest energy state. Then I can stretch it out. And if I do the work and put the energy
*  into it, then I can stretch it out. Now, if I let it go, it's going to snap back to its low energy
*  state. That reverb moment in between things is a transitional state. It's not going to be in that
*  state very long. It's on its way from one to another. And for any given protein, there could
*  be multiple different low energy states that it might spend time in. And of course, the
*  individual proteins, they're in solution, right? So there's water molecules bouncing off them all
*  the time. So the constant bumping into the environment creates opportunity for these things
*  to occasionally flop from shape to shape. And there probably also is like a path issue where
*  you maybe can get from A to B and B to C, but not necessarily A to C without going through B, I
*  imagine. And so doing all of this is probably hard for a lot of reasons, but you highlighted the fact
*  that the computation is really slow, right? Yeah. So molecular dynamic simulations, they come in a
*  lot of different flavors, a lot of different complexities. Some of them model the proteins
*  using just standard Newtonian physics. And then you can add in more complexity on top of that,
*  things like quantum properties and other features of the protein to make the molecular dynamic
*  simulation more complex and more robust. But these simulations are really computationally intensive.
*  They take a long time, they take a lot of GPUs, and they're just not very efficient. And on top
*  of that, the length of time that you run your simulation for really, in a lot of cases, determines
*  how accurate your distribution is and how accurate the confirmations or trajectories that you get out
*  of that are. So you might run your simulation and not run it for long enough, and you don't get all
*  the different states that the protein might be in, but you miss some of them, right? And there
*  are some new AI models that are trying to address this and trying to make headway into augmenting
*  or even replacing molecular dynamic simulations in a lot of cases. So for example, Alpha Fold 2 came
*  out a couple of years ago, and that was a big deal, right? But you just get a single static structure
*  from Alpha Fold 2. So we give it the protein sequence, which is just a sequence of amino acids,
*  which are represented by 20 letters. And it takes in this protein sequence, and it provides you with
*  a static structure for that protein that's a low energy confirmation for that protein. It also
*  tells you how confident the model is that that is the structure of the protein at that particular
*  point in the protein. And then you can take the average and get an overall confidence for the
*  whole protein. Hey, we'll continue our interview in a moment after a word from our sponsors.
*  or OCI. OCI is a single platform for your infrastructure, database, application development,
*  and AI needs. OCI has four to eight times the bandwidth of other clouds, offers one consistent
*  price instead of variable regional pricing, and of course, nobody does data better than Oracle.
*  So now you can train your AI models at twice the speed and less than half the cost of other clouds.
*  If you want to do more and spend less like Uber, 8x8, and Databricks Mosaic, take a free test drive
*  of OCI at oracle.com slash cognitive. That's oracle.com slash cognitive, oracle.com slash cognitive.
*  The Brave Search API brings affordable developer access to the Brave Search index,
*  an independent index of the web with over 20 billion web pages. So what makes the Brave
*  Search index stand out? One, it's entirely independent and built from scratch. That means
*  no big tech biases or extortionate prices. Two, it's built on real page visits from actual humans,
*  collected anonymously, of course, which filters out tons of junk data. And three, the index is
*  refreshed with tens of millions of pages daily. So it always has accurate up to date information.
*  The Brave Search API can be used to assemble a data set to train your AI models and help with
*  retrieval augmentation at the time of inference, all while remaining affordable with developer
*  first pricing. Integrating the Brave Search API into your workflow translates to more ethical data
*  sourcing and more human representative data sets. Try the Brave Search API for free for up to 2,000
*  queries per month at brave.com slash API. So let me just get into a little bit more how that happens.
*  If I understand correctly, there were proteins that had been analyzed mostly through X-ray
*  crystallography to the point where people were pretty confident that they had a structure.
*  People put a lot of time in the lab. We got to make enough of this stuff, get it to coalesce into
*  some crystal form. Then we can hit it with X-rays and we can try to decipher how that gets scattered.
*  And then we can come up with a structure. And we hope that approximates the structure that it
*  actually takes in the cell, but no guarantees because protein crystals don't really occur in
*  nature, right? That's a very odd thing in the first place. So that was like closest approximation
*  that we could get, right? So that I think that's why the initial things were limited to outputting
*  a single predicted structure. That's right. But again, that protein could exist in other
*  confirmations. It might have other states that it exists in when it's interacting with other
*  proteins or based on the environment that it's in, what temperature it is, things like this
*  can change the shape of the protein, right? They move around. They're very jiggly and they do things.
*  And so having a way to sample the Boltzmann distribution and get all of these different
*  confirmations out of them and also understanding the transitions between these states is a really
*  difficult problem. People have been trying to address this. There's actually a model that just
*  came out middle of last year that does a really good job of addressing this. It's called Distributional
*  Graph Former. It's a generalization of alpha-fold too. It's not just a single static structure
*  anymore. It's actually a whole ensemble of structures and also the transition pathways
*  between those different metastable states. Distributional Graph Former does a pretty good
*  job of doing it too. There's some room for improvement for sure, but it's a pretty solid
*  model. Some people that I have a lot of respect for worked on this and it's a diffusion model
*  similar to like Dali, which most of your watchers are probably familiar with, but it works on proteins
*  instead of images. And then another level of like insane complexity. They interact with each other.
*  So this is like maybe in the presence of some other protein that constrains it in a certain way
*  or some other small molecule perhaps that fits into a pocket of it in a certain way.
*  You can have these deformations and then subject to those constraints, they still find their natural
*  low energy state. Returning to my slinky visualization, I could also step on the middle of it
*  and then the parts on the side would presumably still look like normal, but there'd be this like
*  deformed part in the middle where I'm stepping on it. That's where Alpha Fold Multimer starts to come in.
*  Multimer, yeah. Alpha Fold Multimer models the interactions between proteins. When it predicts
*  the two proteins together, there's an interface region where the proteins are in contact with
*  each other. Alpha Fold Multimer tells you the quality of the interfaces between the two proteins
*  and then you have these predicted aligned error outputs. And these tell you how good of a quality
*  the model has provided you. So on the interface, you have a range of kind of whether these things
*  are like puzzle pieces that are perfectly fit to each other and have a really tight coupling
*  or jigsaw pieces that sort of fit, but they don't perfectly fit and they don't really want to stay
*  together as much. All the way down to obviously they just don't fit at all. They just kind of
*  don't adhere to each other. Is there anything more we could do to develop our intuition there
*  for this dynamic range of how adherent these things are to each other? Yeah. So there's two
*  ideas that you're addressing here. One of them is binding affinity. Like how much affinity these two
*  things have for each other to bind to each other. And then there's also how transient are the
*  interactions between them in terms of like dynamics and like the time spent next to each other. There's
*  recent work, I think it's out of MIT. They use the AlphaFold2 architecture and they train it as a
*  flow matching model, which is a generalization of diffusion. And using this, they get these ensembles
*  of conformations for a protein. And part of the information that they get out of this is how
*  transient the interactions between residues are. Let's say you run your AlphaFlo model and you
*  produce 10,000 different conformations or states that the protein exists in. You can cluster those
*  structurally and then look at which residues are close to each other in each of those clusters.
*  And you can tell how transient the interaction between these two residues are and how much time
*  they spend together. One thing that caught my attention, I believe you had said that there were
*  as many as 10,000 possible conformations for a single thing.
*  Yes. When you run AlphaFlo, it generates conformations of a protein for you. And it was
*  trained on molecular dynamics simulation data. So it does have some notion of dynamics and
*  it produces different conformations of the protein for you. And you can tell it how many of these to
*  produce. And the more that it produces, the more likely you are to get a nice global picture of all
*  the different conformations that might exist for that protein. So we've actually tested AlphaFlo
*  on proteins called fold switching proteins. The most popular example in the literature and in
*  the community right now is KyB. And KyB is this fold switching protein that 10% of the time it
*  exists in this one confirmation and then 90% of the time it exists in this other confirmation.
*  And this is influenced by like a circadian rhythm. And when you apply AlphaFlo to some of these fold
*  switching proteins, it doesn't capture both of those fold switch states. So in the example of KyB,
*  it actually only really predicts conformations that are relatively close to the slightly higher
*  energy confirmation, the one that's a little bit less likely, the one that exists in 10% of the time,
*  which is a little bit odd, right? Because you would expect and maybe want your model to go for
*  the ground state or the lowest energy confirmation. And for some reason, it sticks kind of close to
*  the fold switch confirmation. I'm not sure that there's like a good explanation for why.
*  I think it goes back to the AlphaFlo2 predictions, because when you predict the structure using
*  AlphaFlo2, you get the fold switch state. You don't get the ground state. People have done
*  all kinds of little hacks to try and get out the ground state instead of the fold switch state.
*  The most popular method they hack together is doing MSA subsampling.
*  Can we talk about this MSA thing for a second? MSAs are basically this. A lot of times the
*  changes that happen only happen in certain regions of the protein. And then there are other regions
*  of the protein that are highly conserved. And so when you do an MSA, you can look at which regions
*  of the protein are really highly conserved. And this will give you some indication of which parts
*  of the protein are going to affect the function if you mutate them. So like if I have a region
*  of the protein that evolution hasn't changed or has changed very, very infrequently, if I change
*  that, if I mutate that, it's probably going to degrade the function of the protein or change
*  the function of the protein. Or maybe you'll decrease its thermal stability or something
*  like that. So MSAs are just telling you evolutionary information. And AlphaFold2 uses MSAs. You can
*  either use the database of MSAs or you can have it compute them on the fly to inform how it predicts
*  structure of the protein. Because when you have proteins that are very closely related to evolutionary,
*  their structures are often very similar. That's not always true. I can have two proteins that
*  are very similar but have very different structures. That happens all the time.
*  But if you have this extra evolutionary information in the form of an MSA, you have
*  extra information that helps you predict the structure of the protein of interest.
*  So calling to mind the classic image of the plane with all the spots where the planes came back,
*  having been shot and then all the places that they didn't observe, those were the planes that
*  got shot down. So this is the evolutionary equivalent of that where we don't see changes
*  in certain regions because they're super core to functionality. And that in turn is super useful
*  for prediction making because these parts are the really important parts and the sort of interactions
*  that they have are the whole point of what's going on. And so clustering the MSA captures certain
*  evolutionary information. Different clusters will focus on or accent particular confirmations.
*  And so if I take out one of my clusters and predict the structure using those clusters in the MSA,
*  I'll get a confirmation out from Alpha Fold 2. And then if I pick a different cluster of sequences
*  in my MSA, I'll get maybe a slightly different confirmation or maybe a drastically different
*  confirmation. And if you do this right, sometimes you can get out the different confirmations of
*  these fold switching proteins. And for CHI-B, they've done this successfully and for a few others,
*  but it's not a super robust method. And I think Alpha Flow is more informative. Boltzmann generators
*  or distributional graph former, I think are significantly better in terms of how they approach
*  the problem because they're going to give you more robust information.
*  Okay, that's interesting.
*  So yeah, the Alpha Fold Multimer works really well. You give it the two proteins or multiple proteins
*  and you find out if there's an interaction there. It tells you what the quality of the interfaces are
*  between the two proteins that you're predicting in the Multimer. You could generalize this,
*  and this is something that hasn't been done yet. So people who are looking for research projects,
*  this would probably be a pretty good one. If you generalize this to Alpha Fold Multimer,
*  do the Alpha Flow thing with Alpha Fold Multimer, if it works well, you could figure out how
*  transient those interactions between two proteins are. Because now you have two proteins or more
*  that are in different confirmations at different times and Alpha Flow will generate all these
*  different confirmations for you. And then you can analyze all these different confirmations and
*  figure out how transient the interactions between the two proteins are and get an idea
*  of the dynamic side of things. So hopefully that gives you some idea. I think computational
*  approaches are proving to be much faster, much more effective, and you can scale them.
*  And this is really good because we need things that are more computationally efficient so that
*  we can do this for a lot of proteins, right? Because we have a lot of proteins to do this for.
*  We're working sometimes with millions or hundreds of millions of proteins. Having millions of
*  variants of a protein and being able to assess them and determine their quality in some metric
*  has become a lot easier in the past couple of years even. So like a good example of how AI has
*  sort of replaced wet lab methods, doing directed evolution in a lab in a lot of ways now that we
*  have AI tools to do similar things feels a little bit unnecessary. Like why do we need to go and
*  inject an animal and wait some amount of time for this to play out inside the animal and then
*  actually synthesize these things by hand in a lab somewhere when we can like do very similar things
*  computationally and often get better results. Hey, we'll continue our interview in a moment
*  after a word from our sponsors.
*  Full disclosure, it's going to cost more than the random person you found on Upwork that's doing
*  two hours of work per week but billing you for 40. But you'll get premium quality at a fraction
*  of the typical cost. Our engineers are vetted top 1% talent and actually working hard for you every
*  day. Increase your velocity without amping up burn. Head to choose squad.com and mention
*  turpentine to skip the wait list.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omniki so much
*  that I invested in it and I recommend you use it to use cog rev to get a 10% discount.
*  So it seems in some sense surprising that you would be able to make a new black box system
*  to make these predictions that they would be faster and more accurate as opposed to just
*  running the physics. I have a hypothesis on this but how is that leap happening?
*  Okay, so I think the key here is compression. Neural networks are compressors of information.
*  Whereas in molecular dynamics, you could simplify things by simplifying the forces or simplifying
*  the model in terms of how complicated the physics are that you're doing. So I think
*  the model in terms of how complicated the physics are that you're using to model problems.
*  Like if I strip everything down and just do like bare bones, Newtonian physics,
*  I can simplify things that way but there's no real compression happening. For these AI models,
*  you could think of them as functions but you can also think of them as compressors of information.
*  You're taking something complicated and noisy sometimes and you're compressing it and you're
*  providing a representation of it that is more compact. Traditionally, you think of a deep learning
*  neural network. You've got data. You train on your data. Maybe you have a train test validation
*  split. You train on your training data and you see how it performs on your test data and that's your
*  trained model. But you can also train models with physics constraints. There are some approaches
*  that people are using that are completely data free and are based on physics and the model is
*  learning the physics and compressing that physics. You get something that is faster,
*  like orders of magnitude faster. You get something that produces your answer in a minute instead of
*  four hours or days. If you've done it right, it generalizes to systems that it hasn't been
*  trained on before. People are doing this for this problem in particular, for getting the Boltzmann
*  distribution of a protein and getting all these ensembles of confirmations and their transitions
*  between the states. Does that make sense? Yeah. That was pretty much my hypothesis that it's
*  essentially learning higher order concepts beyond the raw physics. This striking observation that
*  comes up over and over again that, okay, yeah, language models, they're only trained to predict
*  the next token, but they not only seem to be generalizing certainly beyond the narrowly
*  defined bounds of their training data and perhaps to some degree even more than that, a highly
*  debated topic. But what is pretty clearly demonstrated at this point is that in the
*  middle to late layers of a language model transformer, the techniques are there to say,
*  okay, this pattern of activations seems to correspond to this higher order concept that
*  we care about, which is a miraculous thing that it's just predicting the next token,
*  but it's learning these concepts of justice and fairness and ethics and whatever that are obviously
*  useful to predict the next token. That's presumably why they're arising, but not something
*  that's been specifically coded for. I guess in the application to biology, basically the same
*  phenomenon is happening where raw data or raw simulated physics or whatever is the input,
*  I'm guessing that the token level vocabulary of a protein would be the 20 amino acids, but the
*  higher order concepts are like, oh, this chunk of a thing is reused a lot and these two chunks of
*  things interact with each other in a particular way. Give us a little more intuition of that.
*  What are the higher order concepts that these things seem to be learning?
*  The concept that I think you're trying to grasp onto is protein motifs. Motifs are reoccurring
*  patterns that happen in proteins. They're short little sequences of amino acids that
*  recur often in lots of different proteins and generally have a very similar structure across
*  different proteins. If we put aside dynamics for a moment and we just look at structure prediction,
*  so there's another model, ESMfold. This is an alternative model to AlphaFold2 that does
*  essentially the same thing. It predicts the 3D structure of the protein in some low energy state.
*  It doesn't perform as well as AlphaFold2, but it does pretty well. It's a language model. It's
*  something that people call a protein language model. It's built on the BERT architecture,
*  actually, which sounds kind of bad because BERT is this older model that's only used for specific
*  things now. The chat GPT models have overshadowed or outshined the BERT models at this point.
*  But in biology, this actually makes a lot more sense because you have the mass language modeling
*  objective that you train on for protein sequences. You just mask out some of the amino acids in the
*  protein sequence and have it predict what those are. Just by training it to do this
*  and then putting a folding model on top of it called EVOformer, which actually comes from the
*  AlphaFold2 architecture, you don't train on any physics, but somehow you learn how to predict
*  3D structures of proteins. In this case, it's almost like physics mostly isn't needed. If you
*  just want to predict a static structure of a protein, you can get pretty good results
*  just using a BERT type architecture with the mass language modeling objective,
*  training on millions of proteins. You get something that will fold proteins for you pretty darn well.
*  There's some really nuanced architectural differences. AlphaFold2 uses multiple sequence
*  alignments and it also uses templates. In general, it is better performing because it has these extra
*  added things in the architecture that improve its ability to predict the structure.
*  Even there, there isn't really a lot of physics explicitly happening. We're not giving it forces
*  and potentials and things like that. Yet somehow we're able to predict the structure of the protein
*  with really high accuracy for a lot of proteins, for most proteins. I guess that's another example
*  of where AI can be a lot better than the molecular dynamics. If you want to model a protein actually
*  folding in a molecular dynamic simulation to get the folded structure of the protein, this is pretty
*  hard and time consuming and computationally intensive. Whereas for AlphaFold2 or ESMFold,
*  you give it a big protein and it takes a few minutes. These are language model-like models,
*  especially ESMFold. ESMFold is pretty much just a language model. They are learning higher order
*  concepts for sure, just as they do for natural language. You can do topic modeling and things
*  like that on these models where you're looking at groups of amino acids instead of just the individual
*  vocabulary elements. Another thing people have found is the attention maps recapitulate the
*  contact maps for proteins. The contact map is like a 2D matrix representation of all the contacts
*  between the different amino acids in the protein. It turns out the attention map, the matrix that
*  you get from your attention mechanism, recapitulates that and is highly correlated with those contact
*  maps. There's some work on this, maybe three years old now, called Bertology meets Biology.
*  They do a really in-depth study of how to pull out these different things, active sites and binding
*  sites and motifs and things like this, based on the attention maps in the protein language model.
*  I would say training a model to predict binding affinity is a hard thing to do. There's actually a
*  big problem with a lot of these models. Most models that try to predict protein interactions
*  don't generalize well. When people are training them, a lot of times people don't split their data
*  in the right way. If your training data has sequences in it that are very similar to your
*  test data sequences, you're going to get overfitting and you're not even going to realize it.
*  A lot of the protein interaction models that have been trained don't take this into account
*  and they don't split their data based on sequence similarity or structural similarity.
*  The overfitting piece, I didn't quite understand it.
*  When you're training your neural network, you want to make sure that your test data
*  doesn't have a bunch of sequences in it that are highly similar to your training data.
*  It's almost like you're training on the same thing twice and you overfit this way. You don't
*  get a good indication of how well your model generalizes. A lot of people do this. A lot of
*  people coming from deep learning, they don't have a super strong background in biology,
*  they make this mistake very often. There's just tons and tons of models out there
*  that don't generalize and that are very overfit because they didn't split their data based on
*  sequence similarity and or structure similarity. Interesting. Okay.
*  That's not really done in language modeling, right? In language modeling, you could certainly
*  have lots of sentences that are very similar and you don't draw conceptual lines between
*  different parts of the data and try to generalize across those lines. What is the difference in the
*  biology context? My intuition says to the degree that these models are learning, the higher order
*  concepts that really matter, that they should be able to learn those regardless. Again, in the
*  language model case, we don't really have a concept of overfitting, at least in the large
*  scale foundation models. There's still a concept of overfitting in LP and training big giant models,
*  Claude or ChatGPT or whatever. You can definitely still overfit these models for these really big
*  chat type models, like really big LLMs and stuff. First of all, they often only train on one pass
*  through the data. They don't do multiple passes. Partially because of that, overfitting is not much
*  of an issue because you're not training multiple times on the same data.
*  I do think that is changing. One little nugget from the recent Zuckerberg-Dorkesh interview that I
*  definitely made my ears and brain light up was when he said they train these latest llama models
*  on 15 trillion tokens. He said, we'd stop because at some point we need to move on to llama four.
*  But he said we could have rotated the high value tokens through again.
*  And I was like, oh, interesting. Anyway, that's a bit of an aside, but
*  I'm still not quite cracking it, to be honest. Okay. So let's see. So you have your training data
*  and your test data. Your test data is supposed to tell you something about how well the model
*  generalizes. If the metrics on your test data are substantially worse than the metrics on your
*  training data, then you've overfit. So to get a good idea of how well your model is generalizing
*  to unseen data, you want at least part of your test data to be very dissimilar from your training
*  data. And this is a big thing that people discuss is whether or not these things generalize to data
*  that's out of distribution. And if you train them in the right way, you can get models that
*  generalize well to out of distribution data. That means it's picked up on some deeper concept
*  that generalizes to areas that it hasn't seen before. And it's using those really deep concepts
*  to make predictions or generate things that are out of distribution. This is not something that's
*  impossible to do. You just have to do it right. And in the case of biological sequences like
*  proteins, the way that you do this is you look at the sequence similarity between the protein
*  sequences in your training data and your test data. And you can also look at structural similarity
*  because you can have different sequences that fold into the exact same structure more or less.
*  And so sometimes, depending on what your model architecture is and what your goal is, you may
*  also want to split based on structural similarity, but not just sequence similarity to make sure that
*  your model is generalizing and not overfitting. Does that make sense? Yeah.
*  I think so. Any given architecture, presumably the very best performance would be if you trained on
*  all the data. But in order to effectively evaluate your architectures along the way,
*  you need to have some holdout to evaluate against. And these similar enough sequences basically are a
*  data leak in the same way that if you find out after you do your thing that, oh, hey, we actually
*  had MMLU in the training data for the language model, then it means like, oh, well, you can't
*  really trust the MMLU scores anymore. And the model still may be good. It may not be so good.
*  But if you train on MMLU, we can't really score you on MMLU. And this is a similar set problem.
*  Yeah. Exactly. And there are even more nuanced ways of splitting the data too for specific things.
*  They trained a new version of DiffDoc. I think they call it DiffDoc L because it's larger.
*  It's the large DiffDoc. And they use this method called confidence bootstrapping,
*  which is sort of like reinforcement learning. And they also split their data in a really unique way.
*  They split their data based on these domains that are present in these interactions to train a
*  model for docking. So you have a ligand, a small molecule ligand that you're trying to dock into
*  a protein and do like blind docking, which is a hard problem. And they get like substantially
*  better performance. And it generalizes a lot better in this new version of DiffDoc because
*  of the way that they trained it and the way that they split their data. And they have really strong
*  confidence that their model is generalizing to out of distribution data. And it's able to predict
*  on things that it hasn't seen before. And they're very dissimilar from what it has seen.
*  So just to make sure I understand, what they've demonstrated is that you should be more confident
*  in doing this stuff in totally new regimes based on the fact that they've been very
*  meticulous in the data split. Whereas if they had thrown everything into the training, then you
*  would have a hard time knowing to what degree to be confident in out of distribution stuff.
*  Yeah. Okay. Cool.
*  And they did a really good job with that model. I think their performance boost was pretty big.
*  They got a lot better performance out of it too. So it's definitely a good model to look into if
*  you're looking to get into this stuff. Something else we should probably get into is training
*  models that are like AlphaFold that do more than just proteins. You might have complexes where
*  there's a protein in a small molecule or protein in DNA or protein in RNA or a metal or whatever.
*  There's all these other biomolecules that you might want to model in complex with each other.
*  And to generalize AlphaFold Multimer to this new situation is pretty hard, but people have managed
*  to do a pretty reasonable job of it. There's still room for improvement on these, but a new
*  model that just came out recently is Rosetafold All Atom. Rosetafold All Atom will let you predict
*  complexes that have proteins in small molecules, proteins in nucleic acids, and proteins in metals
*  too. Big step forward now because now you can apply this idea to these other complexes and you
*  can get this score that tells you how likely there is to be an interaction there and how strong that
*  interaction is. And you could also probably do the AlphaFlo type method with something like Rosetafold
*  All Atom as well and get something like conformational ensembles out of it. And something
*  like that is probably coming soon. So yeah, I would say now a lot of the more interesting
*  models are more influenced by diffusion and flow matching models. A lot of the generative models
*  that we're getting that are predicting the Boltzmann distribution or that are generating
*  new protein structures for you with specific shapes and functions or that are allowing you
*  to design new sequences that fold into a particular backbone. A lot of them are more influenced by
*  diffusion and flow matching than language modeling and transformers. Some of them use transformers,
*  but they're starting to be a lot more influenced by Dali type models, I would say. You're starting
*  to get this really fine-grained control over what kinds of proteins or small molecules or nucleic
*  acids that you can generate. And there's actually some models that have come out that are text
*  conditioned. So a couple of the models that I mentioned were protein DT and molecule STM.
*  These are generative models that are text conditioned. They use the exact same method
*  as CLIP. They use contrastive learning and they have captions and molecules or
*  captions and proteins. And they allow you to type in a natural language prompt and get out a molecule.
*  So protein DT, for example, or molecule STM, you can give it a text prompt in natural language
*  describing the properties of the molecule in just natural human language, giving it like this
*  molecule has these chemical properties and it has this sort of bias away from or towards these amino
*  acids or interacts with these other molecules in such a way. You can give it these natural language
*  text prompts and it will generate proteins and small molecules for you that satisfy these
*  constraints or that correspond to the text prompt that you give it. And there are more models like
*  this that have come out recently that do similar things. They're text conditioned, like diffusion
*  models or flow matching models that are generative and that produce molecules with specified
*  properties based on natural language text, which in my mind, that's kind of mind-blowing. I think
*  that's amazing. Having a model that will just generate molecules for you that fit natural
*  language descriptions, that's crazy. Like that's amazing. Yeah, no doubt. Okay. In actual work,
*  what are the cycles that are used to actually make progress on questions of interest? Like you have
*  a target, you want to make some modification. Like how do these things fit together to
*  allow us to work a lot faster and get more value from our limited wet work resources?
*  Are you familiar with RF diffusion at all? No, not really. RF diffusion is a diffusion model that
*  used the Rosetta fold backbone and trained it as a diffusion model to denoise 3D structures of
*  proteins. You don't give it a text input, but you can condition it on other types of things.
*  It's a little more specific and it's a little more geared towards people who want to perform
*  surgery on proteins. RF diffusion doesn't usually get used on its own because RF diffusion just
*  works at the level of structure. It's doing the denoising process on the structures of the
*  proteins. It doesn't know anything about the sequence of the protein. So I need a separate
*  model like Ligand and PNN to design the sequence for that 3D structure. So they kind of go hand
*  in hand. RF diffusion designs the structure and then Ligand and PNN designs the sequence for that
*  structure that will fold into it so that you have something you can actually go and synthesize in a
*  lab. You need a protein sequence to synthesize to get the protein structure. So once you've generated
*  your 3D backbone of your protein, you design a sequence for it using Ligand and PNN. So if you
*  want to design new proteins with specific structural properties and you want to get your hands dirty
*  and perform surgery on these proteins and graft them together or take pieces from this one and
*  graft it onto this one or generate a protein with a specific sort of fold tertiary structure or
*  or maybe generate a protein that binds to a specific protein with really high affinity and
*  specificity. These are the things that RF diffusion is good for. There are several different
*  versions of RF diffusion. There's a new version that just came out called RF diffusion all atom.
*  Which allows you to generate proteins that will bind to small molecules. So you can generate
*  proteins with binding pockets that are highly shaped complementary to a small molecule Ligand.
*  And with RF diffusion and RF diffusion all atom, you can also do something called motif scaffolding
*  which is where you pull out motifs from a protein that you like. Maybe they're like binding sites
*  or active sites or maybe there's a particular segment of the protein that binds to a different
*  protein that you're interested in or performs a specific function. And you can pull these pieces
*  of the protein out and scaffold them and build a new protein around those pieces that holds those
*  pieces in place so that you have a new protein with very specific 3D structure that performs
*  very specific function. It's been a very influential model and a very useful model and it's definitely
*  one of my favorites. What exactly it is that you're specifying? You're saying I want it to have
*  certain properties and then it's filling in the sequence that gets you to those properties?
*  Yeah, the most basic usage of RF diffusion is unconditional generation of a protein.
*  So you just you tell it some length or range of lengths and it will just generate proteins of that
*  length that are brand new that have never been seen in nature before and very often are very
*  designable and that you can actually synthesize and create in a lab. And that's just completely
*  unconditional generation. You don't give it any sort of constraints. It just generates a new protein
*  for you of a particular length. One of the really interesting functions of RF diffusion is it will
*  design binders for you. So if I have a target protein and I want to design a protein that binds
*  to it with really high affinity and really high specificity, RF diffusion is really good at that.
*  It'll design binders for pretty much any protein you can give it and very often the proteins that
*  it designs that bind to your target protein are very high affinity and very high specificity and
*  often very thermostable. And using Ligand and PNN you can increase your binding affinity and other
*  properties even more. And then the other functionality that's really useful is the
*  motif scaffolding, which is where you pick out pieces of a protein or multiple proteins
*  and you build a new protein that holds all those different pieces in place in a particular way.
*  And so this is one thing that you could imagine doing with this would be like building or designing
*  an adjuvant or like grafting two proteins together or let's say I have one part of a protein that
*  binds to protein A and I have some other protein that binds to protein B and I want to design a
*  protein that binds to both protein A and protein B so that I can get a complex with three proteins
*  in it, right? I want to have a protein that binds to protein A and protein B. So what I can do is
*  I can take those pieces out of the protein that bind to protein A and I can take the pieces that
*  bind to protein B and I can scaffold them together into a new protein and now I've got a new protein
*  that binds to both of those proteins. And I can do things like build out protein interaction networks
*  this way. So if I want to design a particular protein interaction network, this is really
*  useful for that. That's a pretty technical and involved thing to do is a non-trivial thing to do
*  but you can do it with RFDiffusion. You can design proteins that will bind to multiple different
*  proteins in multiple different contexts and build out these networks this way. And this gives you
*  like a way to modulate protein interaction networks, right? Because you can modulate your
*  protein interaction network by blocking particular interactions by designing a binder but you can
*  also add in interactions that weren't there before using the motif scaffolding or maybe binder design
*  and motif scaffolding together. So it's very much geared towards people who are like really
*  interested in performing surgery on proteins and protein interaction networks. And it's very useful
*  in a lot of different contexts. And now with RFDiffusion All Atom also with other interactions as
*  well because with the All Atom models you can model more interactions than just the protein
*  interactions. So how does this in practice get used? Maybe the cancer example from the top is
*  a good one. In that scenario we already had an understanding of the cancer cell has this thing
*  that disables the immune cell and so then you could say, okay, let's brainstorm some ideas here,
*  right? If we can bind something to that bit of the cancer cell that would cap it blunt its ability to
*  then interfere with the immune cell, then the immune cell presumably would do its job still and
*  kill the cancer. Of course you've got highly tangled webs of interaction that you're doing this within
*  but you've got something local like that. Now kind of take me through the cycles and the practical
*  application of some of these tools for a specific problem of that sort. Yeah, so like the one that
*  we were talking about earlier with the cancer with PD-1 and PD-L1 is a really good first example
*  that I think is really good place for pretty much anybody to start because you can very easily and
*  very quickly design a binder to one of these proteins with RF diffusion. It's really good at
*  designing binders for pretty much anything. If I have this PD-1 PD-L1 interaction between these two
*  proteins, essentially what's happening is the cancer is turning off your immune system's response
*  to it and then your immune system doesn't effectively combat the cancer. But if I design a binder
*  to one of these two proteins to block that interaction and my binder outcompete that
*  interaction so it has a higher affinity than the PD-1 PD-L1 interaction has, then I can
*  successfully block that interaction and prevent the cancer from turning off the immune cell's
*  responses to it. Another way that RF diffusion can be used, so let's say you have a protein that
*  binds to a target but it doesn't bind very well. The affinity is low and the shape complement
*  complementarity isn't terribly good. I can use RF diffusion and protein MPNN or ligand MPNN to modify
*  that and increase the binding affinity. So something I can do with RF diffusion is partial diffusion.
*  So I can take my protein of interest that binds to my target and I can perform partial
*  diffusion which is where I add a little bit of noise. I don't completely noise it. I don't turn
*  it into a Gaussian distribution or anything. I just add a little bit of noise into it and then
*  have RF diffusion denoise that and what it'll do is it'll denoise it into a structure that's
*  kind of similar to the one that I started with but it's also a little bit different now because I
*  added that noise and then denoised it with RF diffusion. And if I do this and I give RF diffusion
*  the target protein that I'm interested in, I can improve the shape complementarity between those
*  two. So the new denoised protein or the new denoised version of my original protein is going
*  to have a higher shape complementarity to my target and then I can go and design sequences
*  for that backbone that are different from my starting sequence. So maybe my starting sequence,
*  maybe there were some residues that had unfavorable chemical properties at the interface.
*  Maybe I need to use different amino acids to improve some chemical properties so that the
*  binding affinity goes up. I can do that with protein and PNN or ligand and PNN. So ligand and
*  PNN is the newer all-atom version of protein and PNN. It's an improvement on protein and PNN and
*  it also generalizes to contexts where you have other kinds of molecules other than just proteins.
*  And I design a sequence with ligand and PNN and I can tell ligand and PNN to bias certain residues
*  towards certain amino acids or away from certain amino acids like at the interface, for example,
*  to get those more favorable chemical properties to increase my binding affinity further. There's
*  also versions of ligand and PNN that will allow you to specify whether a residue is a buried
*  residue, an interface residue, or something else. So using partial diffusion with RF diffusion to
*  slightly noise and then denoise the structure that you already have can help you increase things
*  like binding affinity and things like thermo stability and other properties. Then let's see,
*  what's another application of RF diffusion? Symmetric generation. You can design
*  symmetric oligomers. Let's say I want to have a protein that interacts with other copies of
*  itself and if I have enough copies of this protein, it forms a symmetric complex. For example,
*  let's say I have a protein that fits together with two other copies of itself
*  in a triangle formation, right? And it's symmetric to the cyclic group of order three,
*  right? So I've got an order three rotational symmetry that's happening. I can use RF diffusion
*  to generate proteins with symmetry like this and it has other symmetries that it can use. So there's
*  dihedral symmetries, there's symmetries, icosahedral symmetries, and tetrahedral
*  symmetries in addition to the cyclic symmetries. And I can, the cyclic and the dihedral, I can
*  choose any order, cyclic group or dihedral group for my symmetry for those. And RF diffusion will
*  design a symmetric complex of proteins where there's multiple copies of the protein in this
*  nice symmetric structure. This occurs in nature in multiple places. One example is in viral capsids
*  and they've also recently some, David Baker's lab recently published some work where they design
*  these like symmetric oligomers as like biosensors. And I think they also designed some to help with
*  like drug delivery. So they have these like, the like pocket that forms when you have a cyclically
*  symmetric complex of proteins, the pocket that forms inside of that. You can design that in such
*  a way that it captures a small molecule drug really well and delivers it to somewhere in
*  particular, right? So that's another application of RF diffusion that's really useful. What else?
*  There's the binder design, fold conditioning, which is where you can tell it like specific
*  tertiary structures to condition on. Maybe I want to design something like a tin barrel.
*  I can tell RF diffusion to generate something that has the rough 3D shape of a barrel. So I can
*  tell RF diffusion specific tertiary structures to generate and it will generate these different
*  folds for you. It's called fold conditioning. Yeah, so here's a good example of how to use
*  motif scaffolding. Let's say if I want to design an inhibitor for two different proteins that are
*  interacting with each other, I could extract the motif corresponding to the interaction and then
*  use that to design a new protein, scaffold that with the motif scaffolding. And then I can optimize
*  it using like partial diffusion and like ligand and pNN to design sequences that have like favorable
*  chemical properties. And then I can check and see using the LIS score from Alpha Fold Multimer,
*  how well my new protein interacts. If I'm getting it, it's like, okay, we have an interaction that
*  is problematic. We want to interfere with it one way or another. We can like cap the one thing or
*  cap the other thing. And so there's this kind of cycle of generate a 3D structure. That's one model,
*  generate a sequence to do that. That's another model. Refine those to look for favorable chemical
*  properties. And then you're validating this to the degree that you can validate it before you're
*  actually doing any actual lab work with something like Alpha Fold Multimer and looking for a high
*  score there. So how quick does this happen? It seems like we're talking orders of magnitude
*  speed up compared to the pre-AI way of doing this. And how accurate is it?
*  Yeah, I mean, RF diffusion, like I can generate a single backbone in a minute,
*  even like a pretty big one. It just takes a minute to generate a backbone. And if you have
*  a really good GPU, that's way faster, right? If I'm just working on my laptop or something,
*  like I can generate something in just like a minute. And then ligand and pNN is significantly
*  faster than that. So like designing a sequence for the 3D structure is actually really fast.
*  Per protein and per sequence, it's less than a couple of minutes to do that whole thing.
*  And so I can design hundreds of thousands of backbones and then design hundreds or
*  thousands of sequences for each backbone with ligand and pNN. So it's pretty fast and then
*  pretty computationally efficient. And they've made some improvements to RF diffusion to reduce how
*  many time steps you need to actually get a good structure out of it. And time and time again,
*  when they actually synthesize these and check for like thermo stability or specificity or
*  binding affinity, very often they're very high. And if I have like low thermo stability or low
*  binding affinity or low specificity, very often when I use these models to improve that,
*  they improve it dramatically. So they're pretty effective. And they're not perfect, but they're
*  pretty good. It's not a hard thing to do to design a protein with RF diffusion and then design a
*  sequence with ligand and pNN and get something that really does fold into that structure with
*  high confidence or that really does interact with my target protein with high affinity and specificity.
*  Yeah. So how does this then fit into the broader validation loop? You have this one thing, you're
*  like going back to our cancer example, right? Oh, this part of the cancer cell interacts with
*  this part of the immune cell and disables it. So we want to put essentially a physical cap on that
*  thing. So that is blocked and that can't happen and the cancer can get, okay, cool. So I'm going to
*  generate potentially thousands of shapes, thousands of sequences per shape, then potentially run
*  millions of things through an alpha fold multimer getting scores. And then what do I do at the end
*  of that? Do I take the top hundred and go actually try them in a living cell?
*  Yeah, exactly.
*  And so this seems, and you're saying they tend to work. And then I guess we also have questions of
*  side effects would be another big downstream question, right? We don't know what else this
*  thing could do when put into the full environment of the cell.
*  Well, that's where the specificity comes in, right? Generally speaking, RF diffusion is capable of
*  designing binders, for example, with really high specificity. So they bind to the target and pretty
*  much only bind to the target. Yeah. And it's a really good thing, right? Because if you design
*  a binder that just interacts with a whole bunch of other stuff, it may never make it to the target.
*  It may cause other side effects, like you're saying have off-target effects, but yeah, RF
*  diffusion is pretty capable of designing really high specificity binders. The motif scaffolding,
*  there's more nuance there because you're performing surgery on proteins and pieces of proteins.
*  And so that can get a little more nuanced and a little more complicated. But if you're just
*  designing a binder with RF diffusion, it's pretty easy to design one that has really high specificity
*  and that doesn't have a lot of off-target effects and stuff.
*  So what's the bottleneck on this process? Is it identifying targets? Especially if you can design
*  things that are that specific and they don't have much in the way of other knock-on effects.
*  I mean, it seems like we should be curing a lot of diseases pretty quick here.
*  I think, I mean, diseases are pretty complicated and sometimes it's not just one thing that you're
*  targeting. Sometimes it's multiple targets and multiple kinds of interactions. And so you have
*  to think in terms of like entire like protein interaction networks or even like interaction
*  networks that involve other molecules as well and modulating those in very specific ways.
*  And often figuring out what parts of a protein interaction network to change or to modulate
*  and how to do that, like what sort of changes you should make to this interaction network.
*  That's a pretty complicated problem. And so I think part of it is identifying specific targets
*  within an interaction network because some of the interaction networks can get really complicated
*  and figuring out which parts of them to modulate is not an easy thing to do.
*  And then computationally, there isn't much of a bottleneck. If you just have a good GPU,
*  you don't really need multiple GPUs even. Like you just have a good H100 or something. Like
*  you can get a lot done with that with RF diffusion and like an NPNN. The hardware requirements are
*  not very taxing. They're probably a little less efficient than I would like them to be because
*  most average people are not going to have access to an H100. Like a lot of people are going to be
*  using like much lower, lower tier GPUs and stuff. But like RF diffusion, for example,
*  there's a Colab notebook that you can run on like a T4. You can run it in Google Colab and
*  it takes a little while. It's not as fast, but the computational bottleneck is not a huge bottleneck
*  right now. I think it could be a little better, but the models aren't huge models. These aren't
*  billions of parameters. I think RF diffusion has a couple hundred million parameters or something
*  like that. An alpha fold, same thing. It's a couple hundred million parameters or something.
*  So they're not really big models that require really excessive hardware to do the computations.
*  And I think the slowest part of that pipeline where you design binders or motif scaffold with
*  RF diffusion or partial diffusion or what have you, and then designing a sequence with like
*  protein NPNN or ligand NPNN, and then validating with like alpha fold or alpha fold multimer,
*  the slowest part in that whole thing is actually the alpha fold multimer part or the alpha fold
*  two part where you're validating and like predicting the structure of whatever you've
*  generated and designed with the other two models. That's actually the slowest part in the whole
*  thing. If you're able to predict a lot of structures with alpha fold, then you're fine.
*  There's no real computational bottleneck there. And as far as like, why are we not curing a bunch
*  of diseases? A lot of this also has to do with how long it takes to get these things to market.
*  And the traditional system that's set up right now for drug discovery and protein therapeutic,
*  it's hard and slow to get new things through. It's a very slow system and it wasn't designed for
*  large high throughput methods. And it just takes a lot of time to get a new drug or a new
*  protein therapeutic through and approved and get it through all the testing,
*  like the different clinical testing phases. Are we like stuffing the pipeline at this point
*  with new things? I mean, it seems like the biggest reason that this used to be a hard thing,
*  of course, it's like slow and there's a lot of like safety, perhaps redundant steps in there,
*  especially if you could say, hey, we have like very high confidence that this is a highly specific
*  thing. I mean, that would really do a lot to inform what the safety profile might be.
*  But even if you, not even if, but in the past, it's like the biggest problem was like,
*  either it wouldn't work, right? Or it would have side effects that were like intolerable.
*  And if you could take both of those things, not entirely off the table, but if you could sort of
*  say, hey, we can be much more confident now, seemingly like at least in order of magnitude,
*  more confident that any given thing is going to do what you expect it to do. And then it won't do
*  other things that you don't want it to do. I can improve both of those by an order of magnitude,
*  then it's you're sort of seemingly two orders of magnitude more likely for things to work,
*  which would take you like from sort of sub 1%, a lot of shooting in the dark to
*  a lot of the clinical trials would be expected to work. Is that the kind of
*  era that we're entering into now where clinical trials should go from like, roll of the dice to
*  you'd be more like disappointed when they don't work?
*  Yeah. I mean, I think we're definitely moving into an era where all this stuff is going to speed up
*  a lot. And I think so there are like a lot of situations where you want to understand
*  more than just a static structure. Like we've been talking about like having models that give
*  you more dynamic information and stuff like that. And those are so recent that they haven't really
*  been adopted by a lot of people yet. And I think once those get used more, that'll speed things
*  up a lot and improve things a lot as well. But yeah, I think also part of it is just adoption,
*  a lot of researchers are not using this stuff yet because it's so new. It's such a new paradigm.
*  It's such a new methodology. There isn't a ton of information out there about how to use them.
*  A lot of researchers don't understand how to use these models effectively or how to use them at all.
*  Because right now you've got to go through this somewhat complicated process of setting up these
*  models. And you don't have to know a lot of coding, but you do have to code some. And you have to
*  understand how to set these things up in like a conda environment or something like that a lot
*  of times. And so if you're not coming from like a programming background or you don't have some
*  experience with programming, like a lot of these models are kind of hard to touch. They're hard to
*  use because you can't really use them unless you know a little bit of coding at least.
*  It does seem to be quite a different skill set. I actually studied it. And the kinds of things
*  that I was taught to do, there were no collab notebooks involved. It was like physical techniques
*  for separating chemicals from one another was a big part of where the time went.
*  Yeah. And that's a whole other thing too, like drug synthesis and small molecules is like a whole
*  other story that we can get into. But because there are like really interesting diffusion models out
*  for those as well that'll generate molecules with specific properties. But yeah, it's a very new and
*  a very unique skill set. Most people working on them are still developing their understanding.
*  There aren't very many experts on this stuff. There aren't a lot of people that are training
*  people to do this. I think we're all learning together. I'm definitely still learning a lot of
*  stuff from my coworkers and other researchers in the field. And it's kind of mind blowing how fast
*  this stuff is developing too. It's developing incredibly fast, which is really good in my
*  opinion. I want to see this stuff proliferated and developed and used because we're going to
*  solve problems much faster this way. There are some platforms that are popping up and
*  making these things a lot more accessible. One that I would mention is 310 AI is working on
*  a tool that they're calling Copilot. And it's essentially a chat interface that uses tools.
*  You can talk to it in natural language, like you talk to chat GPT or something. And then it
*  knows how to use function calling to use other models as tools. So you can say generate a
*  protein with such and such property, and then it'll use a particular model to do that,
*  generate some protein with that particular property. And then you can say like increase
*  binding affinity with such and such protein, and it'll modify your protein for you to increase
*  the binding affinity or something. Or you can say dock this small molecule to this protein,
*  and it'll call on diff dock and dock the small molecule to the protein for you and then return
*  that. And that's all using like a chat interface, which is making a bunch of these models a lot
*  more accessible to people. And right now it's pretty good already. It uses a pretty wide range
*  of tools for different things. Like it'll use like protein and PNN or ligand and PNN to design
*  sequences for a structure. I'm not sure if it uses RF diffusion yet, but they just keep adding more
*  tools to it. And they probably are going to start including RF diffusion and some other models as
*  tools for it as well. And once they have a good selection of tools for it to use, that'll be really
*  good. And that'll lower the barrier to entry for a lot of people. But so 310 AI, depending on how
*  good that gets and how fast it gets really good, I think it's going to make a lot of these models a
*  lot more accessible and really increase adoption of these techniques. And I think that's going to
*  have a huge impact in the near future. And I think that's going to be really big and important
*  because adoption right now is pretty limited. Just using a really simple metric by if you just look
*  at like how many views a YouTube video on RF diffusion gets, it's not that many, right? There
*  aren't that many people watching these videos. This is going to be the one that goes viral and changes at all.
*  I hope so. That would be great because adoption is going to be big. I think because the more
*  creative people you get using these things, the more you're going to see creative uses of them
*  and like novel approaches to solving problems that people weren't even thinking of before. Like when
*  have you been able to design proteins that build out complicated protein interaction networks using
*  like binder design and motif scaffolding? Like that's just so brand new within the last couple
*  of years that the adoption just hasn't caught on yet. So hopefully more people will start experimenting
*  with these models and really learn how to use them well. And we'll see a lot of really interesting
*  novel techniques popping up in the near future. Yeah, that's pretty remarkable. So it seems like
*  the problem then shifts to the case that given a target, we can pretty reliably and like even
*  relatively computationally efficiently come up with something that will hit the target,
*  not hit other things, not cause a lot of collateral damage. Now it's like target identification becomes
*  the thing that really matters the most. And this seems like it's happening in like a lot of areas
*  at once. Certainly thinking about like a military environment, like we've got really good missiles
*  that can hit very precise targets, but then the targeting obviously becomes the high stakes
*  decision. And yeah, in lots of just business operations context too, right? Like figuring out
*  the right thing to do is often the hard part. So what do you think are the prospects for that sort
*  of thing? I've been working through this and thinking we've got quite a tech stack for,
*  obviously we can like sequence lots of DNA. We can also pull out from an individual cell now,
*  what was the sort of state of the transcriptome, what genes were being expressed at any given time,
*  what proteins were being created. I don't know quite the degree to which we can do that with
*  small molecules with a really localized sample, but it seems like we've got like a lot of ability
*  to generate a lot of data and to probably then create a foundation model of some sort. This is
*  kind of where EVO I sort of sense is going, even though that's not even doing all this stuff yet,
*  but already they're training a language model on DNA sequences, purely bacteria and phage DNA from
*  what I understand. And yeah, I was a little disappointed by that, but I think part of their
*  reason for doing such a specific selection was for safety reasons. I think they're trying to be a
*  little cautious about what they train on and what the model is capable of doing for safety reasons.
*  But I was a little disappointed that they only trained on that data for sure. Hopefully there'll
*  be another version at some point that's trained on other data as well. But yeah.
*  I'm sure there's a lot more to come. So they train on all this data. Now they can generate
*  sequences in the same way that a language model can generate text, right? In autoregressive
*  byte by byte, base pair by base pair generation. And then there's these really interesting things
*  that they can do downstream of it where, for example, a gene essentiality score or test,
*  basically, if you change a sequence in a particular gene and generate from that
*  changed sequence, it seems that the model has developed a sort of higher order understanding
*  of how things fit together such that if you do make a change to something that really matters,
*  then you see sort of an unraveling of the later generation. You see a very high perplexity
*  downstream of this changed sequence. And that reflects the fact that, hey, if you've changed
*  that sequence, I can't really make any confident predictions now because we're outside of the set
*  of things that can work. And so what's the use of that? It's all kind of noise. Whereas if you
*  change something and predictions remain confident downstream, then you infer that must not have been
*  super important. That was an area that more easily could be, change could be tolerated in
*  that particular sequence because, and we can infer that from the fact that it continues to make
*  confident predictions downstream. That's pretty remarkable stuff that suggests to me that especially
*  as we scale up the data set a lot more, which, and this one was 300 billion, I mean, that's not
*  nothing, but it's not much compared to what we could easily imagine doing. Certainly not much
*  compared to the 15 trillion tokens that Mediterranean Llama 3 on, but then also like more modalities,
*  right? I mean, we're seeing this in the language models where you can have obviously language
*  integrated with image and plenty of other things. Audio now it fits into Gemini 2. It seems like you
*  imagine from just the DNA to the DNA and maybe the transcriptome or the proteome or whatever the
*  state of a cell is. You can even imagine scaling this up another degree to the systems level too,
*  but to learn to predict the next state from the current state seems like we're getting really
*  close to being able to do that. I would kind of expect that in the next couple of years at most,
*  we would start to see large scale foundation models for biology that would predict how a cell
*  will evolve through time, how a system level description would evolve through time.
*  And then you can start to do these counterfactual hypothetical perturbations and see, okay, if we
*  change this, then how will that make things evolve? If we change this, how will that make things
*  evolve? And so then I guess what we would expect to be learned by those systems is what is now the
*  black box, right? Of all these interactions that we have only mapped out, whatever, 5% of.
*  And then you could even imagine a situation where you start to do interpretability techniques on
*  digital neural networks to then figure out what the actual pattern of interactions is in
*  the actual biological systems. So is that where this is going over the next couple of years?
*  I mean, and then it seems like if we can achieve that, then you kind of have a fairly closed loop
*  of, okay, we can now identify good targets at a pretty high rate. We can identify or design
*  interventions that are pretty likely to be successful. The specificity is already high.
*  I mean, we're entering into sort of a super steep part of the S curve in terms of not just
*  like understanding biological systems, but really being able to intervene in them. And it just seems
*  like a totally different regime that we're headed for. So is that what you basically expect to see
*  over the next couple of years? I hope so. I hope that all of that comes to reality or comes into
*  existence. I think it's about to get crazy for sure. I think like we're fast approaching a
*  scenario where all of these technologies are going to kind of converge and we're going to have a lot
*  of power over editing and modifying our biology. And I think that's a very exciting thing because
*  there's a lot of problems that I really want to see solved in my lifetime. And I think we are
*  definitely moving in the right direction. And I think we are fast approaching a situation where
*  we can actually solve a lot of these problems. The main thing that you're talking about is like this
*  complicated sort of hierarchical structure that's happening. And the level that I think at
*  most of the time is at the level of like molecule interactions. But you can definitely take that up
*  another level and look at how those interactions come together in a network to create a particular
*  sort of like phenotype or to create a particular sort of state of the organism. And like some of
*  those states are diseased states that we don't want. But figuring out like how to modify these
*  interaction networks I think is somewhere that we really need to focus on a lot. And one thing
*  that's really useful and that I really want to see pushed further is this notion of LIS score with
*  alpha fold multimer and seeing also like things like alpha flow or distributional graph former
*  generalized to complexes, to like complicated complexes of molecules and not just one or two
*  proteins or something. Like I really want to see more progress happen there because once we
*  understand all of the interaction networks and we're able to modulate them in very specific ways,
*  we're going to solve a substantial amount of problems. And like modeling these interaction
*  networks is becoming possible now. I think before alpha fold multimer and before some of these other
*  like docking methods and before like Rosetta fold all atom came out, we really didn't have the tools
*  to model all of these different interactions. But we have very recently just hit a point where we do
*  have most of the tools that we need if not all of them to model all of these interactions. And
*  once we implement something like alpha flow or distributional graph form for complicated complexes
*  of molecules, that's really going to be like pretty substantial. And I'm not sure how I would
*  approach the problem of determining what specific interactions or interaction networks to modulate.
*  Like that feels like such a big problem to me. But I also know that there are a lot of biologists
*  that know specific interaction networks they want to modulate and they want to modulate them in very
*  specific ways. And there's a lot of that. And now we can do that. I think we just need to get these
*  tools into the hands of those biologists and make them really accessible because they're not super
*  accessible yet. I mean, like a lot of them are open source and they're out there and you can get
*  the model weights and a lot of them have the training code and the inference code and all
*  this stuff available. But probably your average biologist is not going to know how to use those
*  tools right now. So making them accessible and easy to use is really where a lot of the work is
*  going to be as well. Because there are a lot of people that want to do these things, but they
*  haven't quite gotten to the point where they've adopted all of these tools yet. And also figuring
*  out how to use them all in tandem with each other. Because you don't want to just use one of these
*  models. You want to use multiple and use them all together to solve a problem. And so that requires
*  you to learn multiple different models and how they work and how to use each one of them. And
*  that's not an easy thing to do for a lot of people. Yeah, this is an issue in AI even in much more
*  simple use cases of just using JTPT effectively. The technology diffusion through society is really
*  the big bottleneck I would say right now to when people say like, if JTPT is so great, why hasn't
*  it changed productivity all that much? It's like people are not using it nearly as much as they
*  could is one really big reason. So a huge reason. If I had to kind of map out the story of the next
*  couple of years as I understand it, or as I'm kind of piecing it together from everything that
*  you're teaching me about, it is right now we have a big backlog of targets. And we have a
*  pretty robust new set of tools that used together can design things that will hit those targets
*  and not create too much collateral damage such that it's not super hard. It's hard to learn to
*  use the tools. But once you have the skill set, it becomes relatively easy to take a target and
*  crunch through a bunch of iterations and come to a bunch of candidates. And those are likely enough
*  to work that we should start to see serious acceleration of the ability to make these sort
*  of find the solutions to these well-posed problems. And then sort of in parallel,
*  we should probably also expect that Evo 5 or Evo 4 will be capable of dramatically better holistic
*  modeling of the overall networks. And that will then once we sort of deplete the current
*  set of targets that have been painstakingly worked out through non-AI methods, why does it always seem
*  like it happens at the same time? It's always these sort of gradual overlapping curves. But
*  my gut says we've got a few years in front of us of picking the low-hanging fruit of, hey,
*  we've got all these targets out there and now we've got good methods to hit those targets.
*  That's going to take a while for people to learn the tools, do it, obviously validate it,
*  run clinical trials going in lots of different areas. And then as the sort of current backlog
*  gets worked through, it's probably a better way to phrase it, right around the same time,
*  I sort of expect that all of a sudden the tension will turn to, oh my God, now we have these
*  foundation models that kind of model the whole causal graph in all of its crazy complexity.
*  And now we're actually going one level out and saying, now we can apply similar computational
*  techniques to the identification of the targets. And we'll do that in sort of a similar way of
*  being like, okay, I want this, this is what's happening and I want to prevent it from happening
*  or this is what I want to happen proactively that isn't currently happening.
*  Let me just kind of brute force my way through a bunch of perturbations to the, and of course,
*  we can get better than brute force too, but even just imagining a sort of several couple
*  generations down of Evo, it seems to make a tweak, see what happens is going to be so radically
*  accessible from a computational perspective that we'll then also just have this explosion of like
*  quality targets to identify. It seems like we may be not super far from a,
*  this is not, we're not even in a world here of like an any sort of AGI, right? We're talking like,
*  these are still tool simulation and tool type things that people would be using that we're
*  not assuming anything here about AI agents doing the work. Although you did have a little bit of
*  that with the 310 kind of copilot, but is there anything that I should be like raining in my
*  expectations on? I mean, are there things about like, one tweet that I sent you was around,
*  to what degree can these things handle sort of point mutations or whatever? And there was,
*  there's maybe individual idiosyncrasy becomes a really hard problem at some point, but like,
*  how far does this paradigm that I'm sketching out extend do you think, and what limits does it hit?
*  Yeah, so I think, so just briefly on point mutations or more complicated
*  mutations where you mutate multiple things and just predicting how positive or deleterious that
*  mutation or set of mutations might be on the protein or something. That's actually,
*  that's a capability that ESM has, and that's already two or three years old at this point.
*  And EVO does it, they got state of the art performance with EVO on predicting which
*  mutations were positive and which mutations were negative and which sets of mutations were positive
*  or negative. And you can compute a few different kinds of like scores that tell you about this.
*  And you can actually build out evolutionary trajectories to show over time how things are
*  likely to evolve based on how positive or negative the impact of a mutation is on protein
*  or something or DNA sequence or whatever. And EVO, they got state of the art performance on this.
*  And that's actually, they also did this with alpha folds. I think they called it alpha missense or
*  something like that. They predicted like all the single point mutations and all the effects that
*  those have. And that's actually like not a hard thing to do. So like mapping out how a mutation
*  affects like a protein or DNA or something and like the course of evolution that's likely to occur,
*  that's actually like pretty easy to do now. I also want to draw attention to another project
*  that I'm aware of. It's not a model per se, but they are using, I think they are using GPT-4.
*  They may have trained their own in-house model. I'm not sure. But there's a company called Futurehouse
*  and they're designing like an agent, an autonomous agent that will do a lot of this research for you.
*  And it'll do things like literature search and review and come up with hypotheses of different
*  kinds of interaction networks that you might want to modulate or different targets that you might
*  want. And it'll do it pretty well. That's a pretty new thing that just started happening like last
*  year, I think, maybe late last year. And they're getting pretty good results with that. And that's
*  actually using an LLM like as the base, right, to build an agent to do this research. And then
*  I think they're also building an autonomous lab that drives itself. So once the agent comes up
*  with hypotheses or targets or what have you, the lab is autonomous as well. And that's a pretty
*  exciting direction. I think that coupled with some of these more like specific tools to like
*  perform these like fine-grained operations on like proteins and small molecules and DNA and RNA,
*  when those two kind of converge, that's going to be a really big deal. And I see that happening
*  like in the next year. But the progress that they made that they're making at Futurehouse is really
*  impressive, I think. So that would also be something that people should definitely look into.
*  And like I think your timeline is within a couple of years for sure. I don't think it's going to be
*  that long before we start seeing like substantial progress and changes. I mean, OpenAI just partnered
*  with Moderna, right? Yeah, hundreds of GPTs. I'm sure that's just the beginning. And I think that
*  also is like a paradigm that's going to match well with these other more specific tools. Because
*  when you enable an agent to use tools, you unlock a lot of possibilities, right? When you enable
*  something that can review thousands of research articles, then develop like targets or hypotheses
*  to test, and then can call on these specific tools to design molecules or proteins or nucleic acids
*  to perform these specific functions or hit these specific targets, that's going to move really fast.
*  And I think I'm excited. I'm also a little nervous, because I think there's a lot of
*  potential for misuse in the wrong hands. Like the sort of things that you can accomplish will be
*  amazing and beautiful. And we're going to see a lot of health problems just disappearing. We're
*  going to see lifespan extended. And that's going to really improve the quality of life for everyone.
*  But also we do have bad actors in the world. And that is something I worry about for sure,
*  because in the wrong hands, we could be looking at very dangerous things as well. And so having
*  some kind of oversight for these things is very important. Because, I mean, we're looking at moving
*  into an age where you could target a specific group of people based on their genetics or something.
*  That's both immensely useful and also very dangerous. And I have a lot of faith in the
*  people that are working on these things. Like the people that are building these models and
*  doing this research are really good people with a lot of really good intentions and a lot of know-how
*  and experience. And that to me is very reassuring. But there's always some random
*  jerk that has the potential to mess it up for everyone. We have to be prepared for that.
*  Yeah, no doubt. I mean, preparing for this, definitely one of the major updates that I've
*  made is that when people talk about the bio risks from AI, the conversation that I've heard most of
*  has been like, how does it compare to Google? How does GPT-4 compare to Google? Does it make it
*  easier for you to get certain information or figure out how to do certain things?
*  And in familiarizing myself to the degree that I have with all this technology, it's like,
*  that all of a sudden feels very quaint already. It's like, this is not a question of comparing
*  to Google. This is like generating entirely new stuff. And I looked back not long ago at the
*  list of mass extinctions in the history of the planet and what caused them. Of course,
*  some were caused by totally exogenous shocks like asteroid hits the earth. But the first one on the
*  list on Wikipedia is the oxygenation of the atmosphere. And it's simply that something
*  pops up and either itself, nobody knows how to eat, or it creates some waste product that
*  you know, that nobody's prepared to deal with. And what we now breathe and depend on was at one
*  point, the cause of mass extinction event. I kind of try to keep these zoomed out perspectives in
*  mind. And it does seem, I mean, tell me if you think there's any limitation to this or whatever.
*  But with this sort of brute force search through sort of biological space, right? It seems like
*  there's not really anything conceptual that I could identify preventing or talk about gain of
*  function type research on a totally different level. Those seem like the really dangerous things. And
*  I don't know how you prepare yourself for that. I think there are multiple things that we can do
*  to help prevent some of these bad things from happening. And I think we're going to need to
*  rely on the models that we build, especially the agentic models that we build to help guide us in
*  some of this, because at some point in the near future, we're going to have agents based on really
*  robust language models or something similar. And they're going to be able to review thousands of
*  research papers and do tests in a lab on things. Take in an amount of data that we can't really take
*  in, right? That no human or even group of humans can really take in and process and digest and use.
*  The scale is going to be much larger than a human can really work with. And so we're going to have
*  to rely on some of our models to help guide us. And also, going back to how does it compare to
*  Google, I think another argument that could be made for why not to worry about some of
*  these things is, okay, maybe I can get on my computer and design some new thing that was really
*  toxic or something, but I still have to go into a lab and synthesize all that stuff.
*  And a lot of that part of the process is very highly regulated and watched, right? I can't just
*  go get a bunch of random chemicals and build this stuff in my house, right? Like, it's harder to do
*  than that. And synthesizing proteins, it's a non-trivial process. So a lot of the worry,
*  I think, of, oh God, we're going to have an AI that designs a deadly virus or a bioweapon or something.
*  A lot of that is really overblown, especially at the moment. And I think a lot of people overlook
*  the fact that computationally designing a molecule is just one step in the process.
*  You also have to do all the lab work and synthesis and work on some kind of delivery mechanism.
*  And this is all stuff that's non-trivial to do. And that helps prevent bad actors from actually
*  going through with some of this stuff. Now, there may be state-sponsored bad actors with access to
*  good labs and lab equipment that will circumvent a lot of that. But when you're working at a state
*  sponsored level, that's a matter of international relations and also national security.
*  That has almost nothing to do with AI, right? The computational design of some random toxic molecule
*  is just one step in a complicated process. And people don't often think of that. And I see a lot
*  of very influential big name people in the industry who are coming from the NLP side of
*  things and the LLM side of things. And they don't really understand the biology and the process that
*  goes into actually making these things. And I think their worry is justified, but they're also
*  not understanding the nuances and where the dangers actually are. So I think it's important
*  for people to keep that in mind. I think it's very important before we start getting all anxious
*  and worried about some random person using LAMA-3 to design a superflu or something,
*  you have to remember it's very unlikely and very difficult for just a random average person
*  to go through the entire process of designing and synthesizing and delivering some kind of
*  toxic molecule. That's a long, difficult process that an individual would be very unlikely to be
*  able to accomplish, even with the help of a very intelligent LLM or a very capable agent. Now,
*  when you have larger research-oriented companies working on these things that have their own wet
*  labs, and they're building agents to run these wet labs and to computationally design the molecules
*  and form plans on how to use them, there I can see, okay, we need some kind of oversight. We need
*  some people working on how to make sure that process is safe, how to protect that information
*  and data and equipment, because there are plenty of situations where something like corporate
*  espionage is happening and people are trying to do nefarious things with some of the technology
*  that some of these companies have. But again, that has very little to do with the AI itself and has
*  more to do with how we're interacting with other countries and other research organizations.
*  So definitely we need to be developing plans for how to use and regulate and oversee a really capable
*  agent that is going to go through the entire process of computationally designing and
*  verifying and then also synthesizing and delivering. And that is technology that is
*  in existence now. We already have agents that are doing most of this process, right? And a lot of
*  people are pushing for more of that, which I agree with, because we're not going to be able to solve
*  these problems on our own. We're going to need some kind of really capable agent that can help
*  guide us through these processes because they're so complicated and so difficult to understand the
*  whole picture and all of its nuances that I don't know if humans can get there without some kind of
*  agent helping out and helping design the molecules and producing it and delivering it and et cetera.
*  My concern is just making sure that these companies and organizations that are building
*  this technology and using it have some people that are overseeing the safety side of things
*  and that are concerned with red teaming and preventing things like corporate espionage and
*  making sure that everyone that's using that technology is using it responsibly and making
*  sure that the companies are hiring not just capable people but also people with good moral
*  grounding and good intentions. That's not even the future. That's kind of now. That's already a
*  concern that we need to address now because we already have agents that are doing these things.
*  Most people don't have access to them though. Most people don't have access to a really capable agent
*  that can do this whole process or do most of this process. That's not something that even most
*  companies have access to, much less individuals because a lot of these models are closed.
*  I could see maybe some kind of state-sponsored group of researchers could use open source models
*  to build something similar and do something nefarious, but that's a very complicated process
*  of building such a thing. Do we have any read on whether offense or defense is favored here,
*  so to speak? In the sense of, for nuclear weapons, for example, if one of the major nuclear powers
*  fires all its missiles, nobody can shoot all those missiles down. It seems to me that is an offense
*  favored regime and so we're kind of stuck in this mutually assured destruction paradigm, which is,
*  yikes, we kind of need to get to a different paradigm because we're under real threat of
*  nuclear catastrophe as long as we've all got thousands of missiles pointed at each other
*  and no viable defense. I don't have an intuition for if biology works the same way or not.
*  I think this is less of a question about biology and more of a question about cyber security
*  because I think it's very similar in spirit to cyber security. There as well, most often,
*  the attacker has the advantage over the defender, but there are a couple of things that may change
*  that. One is really capable agents because if you have a really capable agent that's able to
*  defend against human attacks that are just inferior, that's going to be a really big part of
*  protecting against bad actors. I guess that's an argument for acceleration, actually, because
*  if you have the most capable agent, then probably your defense is going to be a lot better than
*  everyone else's. If your agent is capable enough, it may be effective enough to ward off pretty much
*  anything. I don't know how soon that's going to come into the picture, but I think that is a good
*  argument for keeping up the pace of development of LLMs and agents and things like that. I think
*  the advantage of the attacker over the defender may end up shifting because of agents. We may
*  end up having a situation where that's no longer the case. I'm a little confused about why is the
*  shift from biology to cyber security because I'm envisioning a world where, for example,
*  EVO is open source, LLAMA 3 is open source. If EVO 3 is open source, then we start to, at some point,
*  we enter into a regime where, yeah, it may not be easy, it may be hard for one person,
*  but at some point, it does get lower than state actor level where somebody could launch some
*  crazy attack. Then it's, okay, if you create some superbug with certain properties,
*  can we defend against it? I'm a little bit unclear as to how you're... I'm not sure if you're
*  equating that to cyber security or saying that's primary somehow.
*  Yeah, no, I think that's a good point. Yeah, because if you develop some kind of... I guess
*  a virus is probably as good an example as any, but let's say you develop a virus of some kind
*  that targets a specific population. Developing a cure for that traditionally has been a very
*  slow process. The fastest that we've ever done it was probably COVID, and that still took some time.
*  Right? And on the other hand, there is recent work that came out of... It was the University
*  of California, but I'm not sure which one. They recently published some research about
*  like universal vaccines, and they're able to design a vaccine that was applicable to a wide
*  range of mutants of a virus. And they said that the technology or the method was highly transferable
*  to other vaccines. And so there's no reason that this can't be applied to pretty much any vaccine
*  to develop universal vaccines against all variants of a virus or most variants anyway.
*  So that'll be helpful. That'll be good for defense sort of things. And then as far as the
*  applications of certain AI models to developing defenses, it's a very complex topic that I don't...
*  Some of the new things that are coming out feel like they might be the answer,
*  but it's a little too early to tell. Yeah. That's definitely a... That's a very good data point. I
*  mean, my kind of default would be just to think I have three kids and I'm no expert in how babies
*  develop in the womb, but it's definitely clear that a lot of things have to go right. Like an
*  unbelievable number of things have to go right in the proper sequence. At any point, if something
*  goes wrong, that could be the end of it. My general default model would be like a lot of
*  things have to go right and only one or two big things would have to go wrong. And so it seems
*  like there's a lot of surface area to defend and a lot of places that could be attacked.
*  But then, hey, if you can make a universal vaccine, then all of a sudden that does start to look
*  quite a bit different. And I think you're right also to say a big part of this does seem to be
*  what is the prevailing international relations regime because it seems like pretty safe to say,
*  if we get into a bio weapons arms race, we're going to be in bad shape. We really have to have
*  some more globally cooperative approach. Or the missiles have one really nice property, which is
*  they don't spontaneously escape their silos and self-replicate around the world. Whereas
*  the list of lab leaks is quite long. It just seems like there's no way that we can get into
*  an international bio weapons arms race and survive it. We just have to avoid that trap
*  in the first place. And yeah, also, what happens when you develop cures for a wide range of diseases
*  and you're able to extend human lifespan significantly longer than what it is now
*  and eliminate a lot of the diseases that we face? Once that exists, I don't know, maybe that's a
*  paradigm shift. Maybe that's like a shift in human consciousness at that point. And we start thinking
*  about things very differently because we're all used to thinking about everything in terms of
*  being finite. And I think having an approach or thinking about things in a way that isn't finite
*  anymore and thinking about things in terms of how valuable our health and our life is because of
*  the fact that enables us to be with who we love for longer. The time that we have with the people
*  we care about is, in my opinion, the most valuable thing that we have. And once you enable people to
*  have healthy lives with people they care about, more or less indefinitely, that changes a lot.
*  And I'm very excited to see, I hope that happens in my lifetime. I think it will. I think it'll
*  probably happen within the next decade even. But I hope that really changes human consciousness
*  to a point to where a lot of these problems just kind of start to go away because we stop thinking
*  of everything in terms of finite resources, finite lifespans, finite time with the people that we
*  care about. Hopefully it's enough of a shift in consciousness that we see some of these problems
*  fading because a lot of them are cultural. A lot of these problems or a lot of these threats
*  at the heart are very cultural. It's not about the technology. It's about how we use the technology
*  and how we're interacting with each other when we use it. And that requires people to think
*  differently. It's not a problem that can just always be addressed with some new technology
*  or some new defense mechanism. We really have to change our thinking. And I hope that when these
*  things start becoming widely available, people's thinking will shift dramatically. Maybe that's
*  where things are headed. I actually have a lot of hope that's where things are headed and a lot of
*  optimism because I think overall most people are good. And I think we can heal a lot of things,
*  not just health problems, but a lot of psychological things we can heal with these
*  tools because it's going to change the way that we interact with each other and the way that we
*  perceive our environment and our relationship to it. That is beautiful sentiment and maybe a good
*  place to end. Yeah, I think I agree with you. This has been really great, by the way. I had a lot of
*  fun doing this and I really appreciated this. Well, I appreciate you teaching somebody who
*  doesn't know nearly as much as I suddenly feel like I really should about this area.
*  So feelings definitely mutual. Amelie Schreiber, thank you for being part of the cognitive
*  revolution. It is both energizing and enlightening to hear why people listen and learn what they
*  value about the show. So please don't hesitate to reach out via email at tcr at turpentine.co
*  or you can DM me on the social media platform of your choice.

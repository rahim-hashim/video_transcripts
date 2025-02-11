---
Date Generated: June 26, 2024
Transcription Model: whisper medium 20231117
Length: 6841s
Video Keywords: []
Video Views: 294
Video Rating: None
Video Description: Explore the fusion of AI and computational chemistry with University of Queensland's researcher, Tim Duignan. Learn about transforming our understanding of electrolytes, the art of simulating physical processes using neural networks, and the potential of AI in scientific breakthroughs. Discover Tim's journey creating AI models for complex system predictions and join the discussion on advancing AI's role in future scientific discoveries.

Apply to join over 400 founders and execs in the Turpentine Network: https://hmplogxqz0y.typeform.com/to/JCkphVqj

RECOMMENDED PODCAST:
Byrne Hobart, the writer of The Diff, is revered in Silicon Valley. You can get an hour with him each week. See for yourself how his thinking can upgrade yours.
Spotify: https://open.spotify.com/show/6rANlV54GCARLgMOtpkzKt
Apple: https://podcasts.apple.com/us/podcast/the-riff-with-byrne-hobart-and-erik-torenberg/id1716646486

SPONSORS:
Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

CHAPTERS:
(00:00:00) About the Show
(00:02:47) Introduction
(00:04:09) Why electrolyte solutions are important
(00:06:53) What properties are we trying to predict with electrolyte solutions?
(00:09:33) Battery fires
(00:13:38) Molecular dynamics
(00:16:40) Time step
(00:18:51) Scaling
(00:23:09) Sponsors: Oracle | Brave
(00:25:17) Decoherence
(00:27:23) Neural Network Potentials
(00:31:04) How big are the models?
(00:35:46) What architecture is used?
(00:38:12) Equivariance (Part 1)
(00:42:29) Sponsors: Omneky | Squad
(00:44:15) Equivariance (Part 2)
(00:44:16) AlphaFold3
(00:46:52) Zero-shot latent space communication
(00:48:21) What is coarse graining?
(00:54:31) How to know if there is no crystallization
(00:56:53) What is the role of water in the simulation?
(01:01:25) Crystallization
(01:05:26) Matching surfaces
(01:09:32) Self-ionization of water
(01:13:22) Active learning
(01:16:41) Temperature
(01:19:20) Ice and water
(01:21:12) Scaling up the model
(01:25:21) Big tech singularity
(01:27:54) China is not far behind
(01:29:15) Safety concerns
(01:31:16) KANs
(01:34:36) The future of scientific progress
(01:39:28) The art of discovery
(01:43:02) One model to rule them all
(01:47:46) AGI, its risks and benefits
(01:50:21) Power vs. Generality
(01:53:01) Generality for Utility
(01:53:40) Outro
---

# Fluid Intelligence: Simulating Solutions with Tim Duignan
**Cognitive Revolution:** [June 26, 2024](https://www.youtube.com/watch?v=iESd3eCSnq8)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution. Today I'm thrilled to share
*  my conversation with Tim Daigman, an applied mathematician at the University of Queensland,
*  Australia, who is using cutting-edge AI techniques for computational chemistry
*  with the goal of deepening and perhaps one day revolutionizing our understanding of electrolyte
*  solutions, from the humble and familiar salt water to the latest lithium batteries.
*  Tim recently shared a short video of salt crystallizing in a water solution.
*  He called this the most exciting result of his career, and this mesmerizing visualization
*  reached nearly 2 million people on Twitter, sparking widespread fascination.
*  In this conversation, we unpack all the techniques that went into making that magic moment.
*  We explore how Tim simulates fundamental physical processes, and how by training neural networks on
*  quantum mechanical simulation data, he's created models that can accurately predict the behavior
*  of systems, of atoms and molecules, several orders of magnitude faster than conventional approaches.
*  This breakthrough unlocks the potential for much larger and longer-lived simulations
*  at various levels of scale, all with compute requirements that are remarkably modest by the
*  standards of the foundation models that we're most familiar with today.
*  Throughout our discussion, Tim offers a masterclass crash course on computational chemistry.
*  He explains concepts like coarse graining, that's a method to simplify complex systems by
*  abstracting away detail thus ultimately average out, and also equivariance, a way of representing
*  data that abstracts away from any particular coordinate system and thus helps models generalize
*  better, all with remarkable clarity. We dive into the technical details of how these neural
*  network potentials work, the surprising behaviors that they can capture, and the exciting potential
*  for integrating these techniques into larger, more general AI systems in the future.
*  This conversation is a powerful reminder of how AI is accelerating scientific discovery in ways
*  that we're only beginning to grasp, and for me, it's a compelling reason to believe that AI systems
*  could become meaningfully superhuman in all sorts of weird and unexpected ways over the next couple
*  of years. As always, if you're finding value in the show, we'd appreciate it if you could take a
*  moment and share it with a friend. You can always contact us via our website, cognitiverevolution.ai,
*  where I'm now accepting resumes via a Google form, and I always welcome DMs on any social network.
*  Now, I hope you enjoy this deep dive into the frontiers of computational chemistry
*  and its intersection with AI with Tim Deignan.
*  Tim Deignan, welcome to the Cognitive Revolution.
*  Hi, thanks for having me. I'm a big fan of Pocos.
*  That's kind to say. Thank you for getting up super early. We're 14 hours apart or 10, I guess,
*  if we count the other way. And appreciate you accommodating, and I know it's early there for
*  you. I was attracted to your work in the first place as I so often discover things on Twitter,
*  and you posted a tweet that probably is the most viral tweet you've ever posted, I imagine.
*  Yes, definitely.
*  Certainly went, probably traveled a lot farther than you expected,
*  which basically showed a short video of salt crystallizing in water solution. So basically,
*  salt water with a little salt crystal. And you said that this is the most exciting result of
*  your career, and that inspired me to dig in and try to learn more. Maybe for starters, give us
*  a little bit of the sort of context. I think people, obviously, who tune into the Cognitive
*  Revolution are paying attention to AI. They're probably not paying attention to the sorts of
*  computational chemistry work that you're doing. So they may not even have any sense for like,
*  we're still studying salt water. That may be a sort of revelation to some. So can you give us the
*  background of what exactly it is you're studying? What are the sort of fundamental questions you're
*  trying to answer? And then we can get into how you're using some cool AI techniques to
*  approach those questions. Yeah, definitely. So I've been fascinated with salt water, or the more
*  technical term as electrolyte solutions. For over a decade now, I've been studying them since my PhD.
*  And I've kind of fallen in love with them. And you talk to people, normal people, and you say,
*  I'm studying electrolyte solutions, and they kind of glaze over a bit. They go like, powerade or
*  gatorade, and they don't quite get it. They're like, why would you be studying that? Surely,
*  we know everything there is to know about them. But remarkably, we really don't. And there's still
*  a ton we need to learn about them and understand them better. And they're actually also incredibly
*  important. I would argue one of the most important substances on the earth. The ocean is a salt
*  solution, obviously. But saltiness plays a critical role in all sorts of phenomena. So climate change,
*  CO2 dissolves into the ocean to form carbonate ions. And that's critical to where our CO2 is going.
*  In all of the technologies we need to fight climate change as well, electrolyte solutions
*  are critically important. Batteries, they determine how fast a battery can charge and how long they
*  can last. They're the thing that connects the positive and the negative terminals in the lithium
*  ion battery. So they're really everywhere. And their biology is the other big one. The flow of ions
*  in and out of your cells is what creates all the electrical signals that make life possible. It's
*  what all of your brain functions on. And the body has developed all of these machines called
*  ion channels and ion pumps to move these ions around. So they're critically important just
*  throughout all of science and technology, really. So we really want to understand them better.
*  So that's why I've been working on trying to understand them for so long.
*  And the remarkable thing about it is that we really can't even predict their most basic properties
*  from what we call first principles, right? Which means, at least in our context, means from
*  fundamental physics, starting from nothing but the equations of physics. And that's the dream I've
*  had really for a decade or now is could we start from nothing but physics and particular Schrodinger
*  equation and Newton's laws and these kinds of things, and predict the properties of these
*  electrolyte solutions? Because that would be an incredible achievement if you could do it, I think.
*  And then it would be a really nice demonstration that you could take this technique and then start
*  taking it further and simulating larger and more complex systems as well. So that's kind of what
*  we've been working on for so long. And this is why I'm excited about this latest paper we put up
*  on Twitter, which you've got this remarkable response, I think. It was great to see other
*  people getting excited about it. For a long time, I thought no one cares about this. I'm just working
*  on it kind of on my own or with a small team of people. And there's a very small number of
*  researchers in the world actually working on these cell solutions, right? So it's amazing to see other
*  people get excited about it as well. So that was really great. So I think great job on motivating
*  the problem in terms of all these different domains in which it turns out to be important.
*  If you can cover climate change and batteries and life, you can even touch on all those with a single
*  question. It's clearly an important question. When you say that we can't predict the properties of
*  these solutions from first principles, what are the sort of properties that you would want to
*  predict? And I guess those are all just determined experimentally?
*  Yes, exactly. So currently we measure all these properties experimentally. And the main one would
*  be things like solubility. So like how much can you dissolve in water or solution? That's a really
*  important one, particularly for batteries that determines you. You want a battery, an electrolyte
*  that can dissolve a lot of ions in it to have high concentration ones in many cases. And then
*  there's kind of more technical chemistry things that come along with that, things called activity
*  coefficients and chemical potentials and kind of all of these important quantities. And what you do
*  with those numbers is you actually then plug them into larger scale models that you could then use
*  to model bigger processes. So you might plug those into a climate model, for instance, to predict
*  the different properties of the ocean and then saltwater actually aerosols form as well from these
*  electrolyte solutions. So there's all sorts of different cases where you would really want to
*  know these properties that you could then plug into the models. And at the moment we get all that
*  data from experiment. And the problem with that is that in many cases, say you have very high
*  temperatures, which very often occurs in many minerals processing instances, where again,
*  these electrolyte solutions crop up, but it's very high temperatures, it's very hard to get that data
*  experimentally because you need very expensive equipment that can handle those kind of temperatures.
*  Or whenever you have like a new electrolyte solution that isn't well studied, then suddenly
*  it's like, oh, we've got to go back to the lab, and we've got to do these exhaustive experiments
*  to characterize these electrolyte solutions as a function of temperature and pressure and get all
*  that data. And that can be very, very expensive. And that means that very often people just don't
*  bother. And in particular, it's very hard as an experimentalist to get funding to just go and do
*  basic measurements of electrolyte solutions. You're not going to get a Nature of Science
*  publication out of that. And so there's honestly not a lot of this happening really anymore. Most
*  of the data that we have comes from a long time ago when experimentalists were working on building
*  up these databases, and we're not really building these databases much more anymore. And so this is
*  a real problem when it comes to machine learning and AI, because databases are key here. So in
*  particular for electrolyte solutions, this is a real problem, the limited size of the databases.
*  And there's people doing amazing jobs taking the data that's out there in the literature now and
*  taking models that can allow you to extrapolate that data a little bit, but it's still inherently
*  limited to having good measurements relatively close to the systems that you're interested in.
*  So that's really an issue there. Interesting. Are there surprising findings anecdotally that
*  could just give us a little bit more intuition for the kinds of things that you may encounter
*  if a solution doesn't behave the way you expect it? I guess I'm imagining
*  battery fire is the extreme failure mode, right? Exactly. So that's a big one. So in a
*  battery, you have the positive and negative terminals, and you've got the electrolyte in
*  between. And actually on that surface, that interface between the positive, the metal terminal,
*  or the crystal terminal and the liquid electrolyte, you can actually get salt precipitating out.
*  And that plays a critical role in determining the lifetime of the battery. And if that salt layer,
*  that crystal salt layer on that surface of that electrode doesn't form properly,
*  you can get real problems. And particularly you can get things called lithium dendrites forming,
*  which then cause a battery to short circuit. And that then destroys the battery and starts
*  these battery fires. So actually, yeah, this process of crystallization can be really important
*  there, for instance, where you want your salts to crystallize out in the right form, essentially,
*  because if you get the wrong form, you can get really nasty things. And this is something that
*  we still really don't understand at all. So there's one thing, which is just predicting these kind of
*  what we call thermodynamic properties, which is what I was talking about before. But then another
*  thing is often you just want to know at the molecular scale, what exactly structures are forming?
*  What are these things? What do these salt crystals look like? How are they arranged
*  and these kind of things? Because that would give you useful information about,
*  you know, what's going to happen when we have a battery and we put it at a certain temperature
*  and pressure, and with a certain charge on it, say, what's going to happen with that layer of
*  salt on that surface of the electrode is a really important question for your batteries. And yeah,
*  things can go badly wrong if you don't understand this properly.
*  So for something like a battery, are there sort of additives? I guess I'm thinking about like
*  doping sort of strategies. You might say, okay, here's a naive, you know, lithium battery with
*  sort of the simplest possible recipe. Now, I may be making an array of these if I'm Tesla,
*  and I try to operate them under a bunch of different pressure and temperature conditions
*  and characterize like what the viable range is and figure out if that's going to work for me or not.
*  And then presumably the naive approach doesn't really work and then I have to go,
*  now I start adding in like little admixtures, doping type of things. Is that?
*  Yes, definitely.
*  So it helped me develop my intuition there as far as it goes.
*  So yeah, this is a big field. And there's a guy called Jeff Dunn, who's really the leader on this,
*  who's developed, he's doing some really nice work on this, developing the million mile battery,
*  right? Which is the idea that you want to make a battery that can go for a million miles,
*  which is very cool. And the way essentially they do that is they're using fairly standard lithium
*  ion batteries, but they're doing exactly what you're saying, doing different additives to the
*  electrolyte to try and control the formation of what's this layer on that surface of the
*  terminal, the positive terminal, the negative terminal of the battery, which is called the
*  solvent electrolyte interface. So they're trying to control that process by adding different
*  chemicals to the electrolyte before you charge up the battery. Because it's actually the first time
*  you charge up the battery, which is called the formatting step, that's when this layer forms.
*  It's really critically important for determining how long the battery will last. But the critical
*  thing is that the way we do that currently is a huge amount of experimental trial and error,
*  so just trying different things, adding them. And this is a real problem if you want a million
*  mile battery, right? Because you have to then put the additives in and then cycle it for the
*  equivalent of a million miles, which takes a long time. So there's a huge amount of experimental
*  effort to try and find these right additives to do this. So if we could instead kind of understand
*  it from first principles, get a really deep molecular scale insight and understanding of
*  exactly how these crystals are forming and what effect that's going to have on the lifetime of
*  the battery, that's the dream and that would be really useful, right? And so there is actually
*  some ways machine learning are coming in here. So people, you know, you can do things like you
*  put some additives in and then cycle the battery for a few cycles and then use machine learning
*  to try and predict what it's going to do after a million. So there are other ways you can use
*  machine learning AI here, which is quite interesting. But in the long term, I think to
*  really crack this problem and solve it once and for all, you'd really want to have this
*  full understanding of exactly what are all the different species forming at these
*  surfaces of these electrodes and how does that affect the cycling performance of these batteries?
*  Gotcha. Okay, cool. So that gives me a good outsider intuition for why you would be excited
*  to see crystallization happening in one of your AI projects. But let's take maybe one step at a time.
*  So in terms of trying to figure this stuff out from a first principles perspective,
*  my understanding is that what kind of comes between experiment and the AI models is super
*  computationally intensive simulation. So that is to say, we're looking basically very small.
*  These are like sub microscopic, right? You're talking about lithium atoms. It's a single
*  atom. It's lost its third electron. We're really down to a very small shell of a thing.
*  So this would be very much in the quantum realm and you are then forced to compute
*  numerically, I suppose. This is not the closed form stuff, right? But just heavily computationally
*  grinding out time steps in the wave equation. Exactly. Yeah. So we do a thing which is called
*  ebonitio molecular dynamics, which is a bit confusing because the acronym is AIMD,
*  but it doesn't have anything to do with AI. So if you've got first principles molecular dynamics
*  as well as another term, I think, and the basic idea is you want to solve Schrödinger's equation
*  to calculate the forces on all of the atoms in your system. So you're starting with quantum
*  mechanics with Schrödinger's equation. And the key reason you use it is to compute both the energies
*  and the forces, which are linked of every atom in your system. And if you can do that, then that's
*  really useful because you can then do what's called propagate the equations of motion or basically
*  solve Newton's equations to calculate how all of the atoms will move through time, make this kind
*  of movie of how the atoms are moving. So that's what a molecular dynamics simulation is. And I did
*  some work at a national lab in the States working on running these simulations on this huge DOE,
*  Department of Energy, supercomputers they have over there, which is very fun. But yeah, these
*  things are really, really expensive. So you're talking huge supercomputers and you'll run these
*  things for months and you're looking at really tiny systems. So you might be looking at something
*  very simple like a lithium chloride electrolyte solution and maybe a hundred water molecules or
*  so. And you can simulate it for, you know, picoseconds, which is, you know,
*  fractions of tiny, tiny fractions of a second. So this is actually far smaller than you can see
*  really using any experimental technique. But that kind of makes it on as a plus as well, right?
*  Because it gives you access to kind of a spatial scale and a time scale that we can't access any
*  other way really, because it's just moving way too fast and much too small to see using
*  light or x-rays or anything like that normally. I mean, you can indirectly get at this thing,
*  these things experimentally, but you can't directly kind of observe them. So that's the
*  advantage of it. It's actually kind of good that it can access these tiny short time scales,
*  but it does mean that it's inherently limited, right? Because a lot of phenomena happen at
*  larger time scales, larger spatial scales and longer time scales, right? And so that's really
*  what we'd like to be able to do, take these techniques, which we know work really well for
*  small systems, right? There are certain experiments you can calculate and show that you agree with
*  experiment to demonstrate that these techniques do work. The problems are just so computationally
*  expensive that you need these huge supercomputers. And so it's not the kind of thing you can scale,
*  right? You're not going to take this and simulate every possible different electrolyte solution
*  or look at any kind of bigger, complex, more complex systems really with it. And that's where
*  the AI comes in here. So these simulations are done on picoseconds. That's 10 to the minus 12
*  seconds. Yes. So technically your time step is a femtosecond, but you run it for thousands,
*  many thousands of femtoseconds to get you to picoseconds. Yeah, which is 10 to the negative 12.
*  So your time step is 10 to the minus 15 seconds. And you're running thousands of those. So you're
*  getting a slice of time. Yeah, that's the kind of time scale which intermolecular vibrations happen.
*  So you really need to capture those. So that's really, you're forced to use that kind of time
*  scale. And is this, when you're solving the wave equation, this is a, if I recall correctly,
*  the second order differential equation. And I believe you would solve that by a polynomial
*  approximation, like we're using like Taylor series type stuff.
*  Kind of, yeah. So we're solving the time independent Schrodinger equation, which makes
*  things a little easier. So we're not doing the full Schrodinger equation, which is time dependent,
*  which can be very hard to solve, but there's some approximations we can use, a particular thing
*  called the Born-Oppenheimer, some tricks we use. Basically the electrons are way faster than the
*  nuclei. So that's a very useful fact of the world that allows us to use some tricks to find easy
*  ways to solve Schrodinger's equation approximately. So we don't have to calculate how the full wave
*  function kind of evolves with time. In fact, we're just doing a thing called calculating the ground
*  state energy and the ground state wave function. So it makes the problem a little bit easier.
*  We're not trying to calculate this complicated quantum mechanical evolution of the wave function.
*  It's just one kind of wave function that we're trying to get a static kind of wave function.
*  So that makes it a little easier. And yeah, there's all sorts of beautiful mathematics people have
*  developed to kind of solve these things really fast and really efficiently. So the main way people use
*  it is Gaussian basis sets actually. So you can run in polynomials, you use Gaussians, and you
*  put those on the center of your atoms basically, and those kind of just, you write your wave function
*  as a linear combination of these functions to describe your wave function. Or you can use what's
*  called a plane wave basis as well. And we can mix and match these things, which is actually the code
*  we use called CP2K, which is really efficient and fast at doing these things. So yeah, there's a ton
*  of really beautiful mathematics going into how do you go about solving these equations really
*  fast enough to do some of these simulations. You just get to this kind of picosecond time
*  scales and beyond. And this is an all to all forces on all other atoms in the system,
*  or all other molecules in the system are calculated to 100 water molecules. That gives you,
*  yeah, so that's the way we know it's an attention like relationship. It goes with the square of the
*  number of, oh yes, the scaling is very interesting. So you have to calculate the force of every single
*  water molecule. So you calculate a total energy and you take the gradient of that energy as the
*  function of the position of every atom to get the force on every atom. So, and because the force is
*  really what we care about because that determines how they move. So you get a force of every atom.
*  The scaling is interesting. So it depends on which approximation you're using. So we don't,
*  you know, if you use the brute force method, it actually scale exponentially with system size,
*  which is a really nasty thing. So you want to avoid that, right? But with the quantum chemists,
*  this is the discipline that tries to do this. They've found all these beautiful ways of solving
*  this Schrodinger equation really quite efficiently so that it doesn't scale quite so badly with
*  system size. So you can't quite get it down to a quadratic, which would be nice, but you can get
*  it down to kind of some kind of polynomial times, depending on which approximation you're using.
*  And that allows you to push to reasonably large systems such that you can kind of get a decent
*  approximation of what a liquid is like, right? Which is where we really want to get to so much
*  important chemistry, all of biology happens in kind of this liquid phase. And the nice thing
*  about these, you know, all these approximations we have now is they can get decent accuracy,
*  but they can start to approximate the things that look a little bit like liquid will look enough
*  like liquid that we can really start to make predictions about the phases, which is really
*  exciting. Interesting. Just because I'm so curious, why is it exponential time instead of
*  quite, I mean, my naive intuition for this would be like each molecule or atom has some force
*  relationship with each other one. And that would seem to be-
*  Oh, yes. So there are, in fact, we can get linear scaling ways of computer force when we talk about
*  neural network projections, but when we were solving Schrodinger's equation, that's because
*  you actually have to treat every single electron in the system, right? So you're not even, you're
*  not treating the atoms on the base unit. They actually just are static. You just say, okay,
*  the atoms or the cores of my atoms are just fixed in position. The electrons is what you're
*  calculating. You're calculating the wave function effect. And the thing about the wave function is
*  when you add electrons, the space that you're in increases combinatorially. So as you add
*  more electrons, an electron can be coupled with every other electron in the system. So this gives
*  you this exponential growth in terms of the computational cost of the calculation. If you
*  were to try to brute force, this is using a thing called full configuration interaction. If you're
*  trying to brute force it out, every single electron can couple with every single other
*  electron in the system. And so you get this very nasty scaling behavior when you try and do that.
*  And you can't use it. So what you're saying is, yeah, you could probably use an approximation where
*  you only worry about things locally, or you don't have to try and worry about everything being
*  coupled with everything else, which is why you get this nasty scaling. Yeah, interesting. So is this
*  kind of a, when you run these simulations, is it sort of a tick tock type of thing where you first,
*  at each step you compute the forces and then you propagate one step and things move and then you
*  recompute the forces and you're going back and forth through that cycle? Yes. Yeah. So it's kind
*  of a combination of two things. We solve Schrödinger's equation first to get the forces,
*  and then you go and use what's called a molecular dynamics engine to calculate how the atoms are
*  going to move. So you update the positions of the atoms using those forces, and then you will redo
*  the force calculation in that new positions. So you get that, it was a loop going back and forth
*  between the energy calculation and updating the positions, and that allows you to make this
*  trajectory. And the reason we do that is because it turns out that the atoms are big enough that
*  they behave fairly classically. So they follow Newton's equations, which is like the limit of
*  Schrödinger's equation when things get big and high temperatures, turns out you could just use
*  Newton's equation. So we don't want to use the full quantum mechanics for how the atoms behave.
*  Although there are rare cases where you do have to do that, in particular for hydrogen atoms sometimes,
*  but mostly it's okay to treat the movement of these atoms using classical laws, whereas the
*  electrons are inherently quantum mechanical beasts, right? They're just so small, so light
*  that you have to use quantum mechanics to treat the properties. That's why we have to solve
*  Schrödinger's equation to get the forces, because that's all about what the electrons are doing.
*  But then if you want to know how the atoms are moving, there you use Newton's equations because
*  they're more classical. Fascinating. Okay. Hey, we'll continue our interview in a moment after
*  a word from our sponsors. AI might be the most important new computer technology ever. It's
*  storming every industry and literally billions of dollars are being invested. So buckle up.
*  The problem is that AI needs a lot of speed and processing power. So how do you compete without
*  costs spiraling out of control? It's time to upgrade to the next generation of the cloud,
*  Oracle Cloud Infrastructure or OCI. OCI is a single platform for your infrastructure, database,
*  application development, and AI needs. OCI has four to eight times the bandwidth of other clouds,
*  offers one consistent price instead of variable regional pricing. And of course, nobody does data
*  better than Oracle. So now you can train your AI models at twice the speed and less than half the
*  cost of other clouds. If you want to do more and spend less like Uber, 8x8 and Databricks Mosaic,
*  take a free test drive of OCI at oracle.com slash cognitive. That's oracle.com slash cognitive.
*  Oracle.com slash cognitive.
*  The Brave Search API brings affordable developer access to the Brave Search index,
*  an independent index of the web with over 20 billion web pages. So what makes the Brave Search
*  index stand out? One, it's entirely independent and built from scratch. That means no big tech
*  biases or extortionate prices. Two, it's built on real page visits from actual humans, collected
*  anonymously of course, which filters out tons of junk data. And three, the index is refreshed with
*  tens of millions of pages daily. So it always has accurate up to date information. The Brave Search
*  API can be used to assemble a data set to train your AI models and help with retrieval augmentation
*  at the time of inference, all while remaining affordable with developer first pricing.
*  Integrating the Brave Search API into your workflow translates to more ethical data
*  sourcing and more human representative data sets. Try the Brave Search API for free for
*  up to 2000 queries per month at brave.com slash API.
*  So at what point does the wave collapse happen? If I'm thinking of quantum mechanics as being these
*  sort of distributions over possible positions or position momentum combinations or whatever,
*  and then you do this sort of next step like propagation, how should I think about the
*  sort of the apparent contrast between a wave or a distribution and a discreet like this thing is
*  moving this much in this direction? Yes, that's a great question. We never really have to worry
*  about wave function collapse, which is quite nice, because that starts to get very complicated,
*  right? And that's why, and the reason essentially is because of something called decoherence,
*  which means that at room temperature, you get decoherence, which means everything essentially
*  just the way functions is always collapsed. So we really only care about the wave function
*  in its ground state, which means it's kind of a very well defined states, stationary state,
*  and it's kind of been collapsed into that state. So we're not too worried about things where you
*  get the wave function and superposition, which gets very complicated. That's when you get back
*  to needing these kind of exponential scaling calculations, which get very tricky. So that's
*  another nice approximation that we can make because we're kind of at room temperature
*  and we're dealing with relatively large systems. And there are cases where this happens, but
*  certainly for a quantum computer or something, they're trying to exploit these kind of
*  phenomena like wave function collapse and put their systems in these unusual quantum superposition
*  states, they called it. So they have to be really careful to kind of isolate their systems and
*  make sure cosmic rays aren't interfering or something, because as soon as anything
*  touches your system, suddenly that wave function could collapse because it starts
*  interacting with its environment. So that's really all of these unusual quantum mechanical
*  phenomena only really happen when things are isolated completely by themselves. As soon as
*  they start interacting with something at room temperature, then that's all going to immediately
*  kind of get washed out and things are just going to collapse down to their normal states. So that's
*  really what we're just trying to do is just find the wave function in this kind of ground state,
*  which is kind of almost the easiest problem you could have to do, which is nice in quantum mechanics,
*  just finding technically it's the lowest eigenvalue of the Hamiltonian operator.
*  And it makes things a little easier. Interesting. Okay. I'm not sure I fully
*  grabbed that. And I suspect that probably a lot of people don't feel like they have
*  full intuition for it either. I don't think I have either.
*  Yeah. Well, nevertheless, though, I think that's at a minimum, a great motivation for why it would
*  be nice if we could have an AI that could figure all this stuff out for us. So tell me how you're
*  now training AIs. And I understand, first of all, you're training the AIs based on this simulation
*  data. So we've set up to the point where there's a quantum mechanical approximation solve based on
*  where everything is and the forces that that exerts, and then there's a timestamp.
*  So how does that simulation data turn into training data? And then what exactly is the model
*  learning in terms of what are its inputs and its outputs?
*  Yes. Great. So basically, by far the most expensive part of these simulations is the
*  solving Schrodinger's equation. That's very, very expensive. And that's where your computer spends
*  almost all its time. And so that's the piece that if you could speed that up, it would be really
*  potentially transformative, really useful. And this is exactly why people have developed this
*  tool called neural network potentials. Okay. And so the idea is that this is basically,
*  it's a neural network. So it's just kind of a very, very flexible function with a huge
*  number of parameters. And then you're just going to adjust those parameters to predict what that
*  quantum chemistry calculation is doing, that solving Schrodinger's equation. And essentially,
*  so the input there is the coordinates, the positions of all of your atoms. So you've got
*  an oxygen atom here and a hydrogen here and a sodium here. And each of those has a force on it.
*  And there's a total energy as well. And that's what you're trying to predict. So you're trying
*  to go from the positions of the atoms to the forces on all of the atoms. And that is the expensive
*  quantum calculation that we're trying to replace with a neural network. And then, so you do need
*  to do at least some of these quantum mechanical calculations to generate your training data. And
*  then sort of supervised learning on that training data that you've generated from these quantum
*  chemistry calculations. And these neural network potentials then can reproduce this mapping fairly
*  well, as long as you have in your training data, something that's sufficiently similar
*  to the case you're interested in, you then don't have to go back and do the full quantum
*  chemistry calculation again, you can just use the neural network to calculate those energies and
*  forces much more quickly. So this allows you this loop between the quantum chemistry and the
*  classical, you can then massively speed that up because you're not spending so long waiting for
*  the quantum solver to work. So you're basically doing the same tic-tac kind of loop, except instead
*  of the numerical solution for the wave equation. Now you've trained a neural network to make a
*  guess. And it turns out that guess is quite good. Pretty good normally. Yeah, exactly. So we keep
*  the part where we're solving Newton's equations, because that's actually pretty quick, it turns
*  out that updating the positions of all of the atoms based on the forces on them is actually
*  doesn't take too long at all. So by far the biggest cost is this quantum part. So if you
*  replace that, then that gives you access to a whole new range of systems you can look at.
*  So normally that's the quantum, you can speed that by a factor of a thousand or more. And so
*  suddenly you can look at systems that are a thousand times bigger and a thousand times longer,
*  and that opens up such a range of systems that that alone is a really useful tool to look at a
*  huge number of important things that we haven't been able to look at previously. And this idea
*  has been around for a long time, actually. It goes back to the 90s, people came up with it.
*  There's a beautiful paper in 2007, actually, Jörg Báillé came up with this with Paranello,
*  this idea of using these new potentials and they train them. The initial ones were just using a
*  very kind of vanilla neural network. So multi-lapsed septron, just a standing kind of dense fee
*  floor neural network. Since then, we've started to develop these things a bit further and get a
*  bit more sophisticated in terms of the ways we do this thing. So these tools are really getting a
*  lot more useful now, just exciting as well. So I want to, you know, a lot of questions about the
*  nature of the networks, maybe for starters, like how big are they? Like how much data is going into
*  training? People, you know, I think are at this point most familiar with large language models.
*  We're thinking in terms of like trillions of tokens and 10 to the 24, 25, maybe 26 flops
*  and many billions of parameters, if not even into the trillions with mixture of experts. How does the
*  just size of like data sets, compute resources and models compare for these purposes?
*  Yeah, I mean, this is what I'm excited about is really they're very moderate, I think, compared to
*  these things people talk about. Yeah, well, these large language models are kind of hard to
*  fathom the size of these GPU clusters and things to me, right? So we're talking to generate my
*  training data. So for me, I'm only interested in like one electrolyte solution, but to generate
*  that training data, you need maybe a few GPUs for a day or so, you know, so nothing is significant
*  at all. So I don't have access to huge, you know, resources at all, really, just using kind of the
*  standard allocation on our supercomputer here in Australia. So, you know, I don't have access to
*  that huge, you don't really need these huge clusters or anything, I think, to generate.
*  And the training data generation is still probably the most expensive part. And yeah,
*  that's fairly you can do that in a few days. Then running the simulations is not too bad,
*  but you can do that on, you know, at least for my system, simple electrolyte solutions, you know,
*  just a few GPUs is really all you need. And you can run these simulations for really long enough
*  to converge everything very well. So the cost of these are really very reasonable.
*  Having said that, people are trying to do much more ambitious things, obviously, now with these
*  neural net potential. So there's a nice paper from the people who developed the neural net potential
*  that I use, they showed they could simulate an entire HIV capsid, right? So a huge system there,
*  you know, millions of atoms. So that kind of thing, then you do want to use one of these huge GPU
*  clusters, which they use to simulate that kind of thing. So you can really push these things to
*  huge system sizes when they start to get really expensive and start to get comparable to some of
*  these large language models and things. But in my opinion, there's a huge number of systems that
*  we don't understand fully yet. They're actually quite small. And if you just simulate like those,
*  there's a ton of interesting insights you could get. So I don't think you need these huge
*  resources to study interesting scientific problems. Although there are certainly
*  ways you could use these really huge resources if they were made available to us.
*  Cool. So what you're doing, the recent results have come from a couple days of GPU time. And
*  I guess intuitively that sounds like hundreds of millions of parameters in a model.
*  Oh, yes. So the parameter size, actually about I think tens of thousands of parameters is what we
*  use. Yeah, so not too big at all. So it's very small compared to, it's funny because it's very
*  small compared to the large language models, obviously, but that's trying to model the
*  entirety of the internet. So whereas ours, in fact, it's quite a lot simpler, I think, the
*  distributions essentially that we're trying to model, then all knowledge. So we don't need that
*  kind of number of parameters. People are trying to build these things called universal force fields,
*  which maybe gets later, but those will have much higher parameter counts and getting up closer to
*  that kind of thing that you need for a large language model. But it's actually interesting
*  because there's a classical method of doing these simulations, obviously, which we haven't talked
*  about yet. But the basic idea is you kind of guess at some physical equations about what this force
*  field should look like. And there you have a parameter fitting problem as well. But they
*  actually only use a few dozen parameters. So in some sense, we've got way more parameters than the
*  kind of classical approach to doing this, but still a lot less than these very large AI models. So
*  it's interesting, we're kind of in this in-between zone, but there's a lot of work people are trying
*  to see, can you get the parameter count down even lower? Which would be very interesting. So we'll
*  see where the best models end up. It's going to be a very interesting question. Yeah, I'm really
*  surprised that it's only in the tens of thousands of parameters. That's strikingly small. That also
*  suggests, I guess, if you're training something that small for days on GPUs, that would sound
*  like overtraining on a standard thing. But is there a... It sounds like there may be some sort
*  of grokking type phenomenon going on here, right? Yeah, interesting. So the training is actually not
*  days. The training is only done within a day for my systems, at least. It's mainly the days would
*  be generating the quantum chemical data, because that's the really expensive part. And that works
*  on GPUs too, so that's also parallelizable. Yeah, technically I did it on CPUs, but you can do it
*  on GPUs now. There's now codes that do it on GPUs even faster. So that's really where things are
*  going. I think we'll be running all these quantum chemistry calculations on GPUs now. And yeah,
*  that's the kind of thing you need a few days probably to generate your training data. But
*  the actual training is, I don't know the exact timing, but it's probably a few hours really.
*  Is there a grokking phenomenon? I don't believe so. I haven't seen any evidence of that yet,
*  but that would be very interesting if we saw something like that.
*  So how about the architectures? Are we talking like transformers here or is other familiar
*  architectures or are these exotic architectures you're using? Yeah, no. So the one I use is called
*  an Equip developed by the Kaczynski Lab out of Harvard. And that is a graph neural network,
*  an equivalent graph neural network. So it's got message passing. So I'm sure people are familiar
*  with those kinds of things. There are also some, there's one called TorchMD, I believe,
*  which is a transformer, which has quite good performance as well. So you can use a transformer
*  there. And yeah, so the traditional ones, which some people still use, are also just plain
*  multi-lap ceptron, as I said. So yeah, these are all kind of standard architectures that would be
*  familiar to people working in AI, I think. And then there's some interesting stuff around
*  like how the data is represented, right? There's this, when you, the Equivariance
*  concept is critical to this whole thing, right? Yeah. So Equivariance is this idea, and this was
*  kind of the big advance that we just had in the last couple of years, I think. So as I said,
*  this idea has been around for a long time, but the issue was always you needed so much training
*  data that I always really struggled to get it to work efficiently, effectively. Basically,
*  you need to keep going back and generating training data constantly to kind of look at
*  the things I was interested in, in particular, kind of these pairing of these ions, how strong
*  were they, stick to each other in water. And so that was always a real challenge and real frustration
*  I had. But then we saw this paper that came out in a clip, is the architecture that we use. And the
*  incredible thing in that paper, they got this table and they say, we get lower error for a water box.
*  They're trying to calculate the forces on a system of water. We get, I think it was four times lower
*  error, and they got that using a thousand times less data. So three orders of magnitude less data.
*  So that kind of blew me away. So as soon as I saw that, I kind of jumped on this because it's not
*  often in science. You'll see a breakthrough with something that goes down by three orders of
*  magnitude. That's the kind of thing that's inevitably going to have an impact, I think.
*  So that's really why I jumped on that quickly and to try to exploit these new tools, which have much
*  more training data requirements. Because then, as I said, the biggest cost is this quantum chemistry
*  calculation you have to do to generate the training data. So if you can get the amount of that data
*  that you need down, that's really exciting because then you can start to really scale these things,
*  essentially, and look at many different systems. So that's what I'm really excited about now,
*  this tool of equivalence that allows you to kind of have this training data.
*  And can you explain a little bit more like what that is? Is it a sort of like a module of certain
*  symmetries? You're sort of finding a way to represent things that is in some way more
*  general, less contingent on the specific coordinates, but somehow relative to each other?
*  Exactly. Yeah. So it's a really, really nice idea. It comes out of group theory and representation
*  theory, some beautiful mathematics that actually kind of revolutionized particle physics a few
*  decades ago. So as a physicist, it's kind of really appealing to me that these same tools now
*  are being transferred and being useful in chemistry and useful in molecular simulation,
*  which is really exciting, and AI. And it's obviously highly mathematical. I'm not an
*  equivalence expert, so I could give you kind of a high level understanding. And the basic idea is
*  that you don't want to just feed raw coordinates into these neural networks, because the raw
*  coordinates are fairly arbitrary. In fact, if you rotate the molecule, the coordinates, the positions
*  of all the atoms are going to change, but its properties really shouldn't change. Because if
*  you rotate a water molecule, it's still a water molecule. It's still going to have all the same
*  properties of a water molecule. They're just going to be rotated as well. And so what you really want
*  to build is a neural network that kind of has this kind of rotational symmetries of space embedded
*  into it, so it knows about the fact that you're on three-dimensional space, and if you rotate something,
*  it's still the same thing. And the way you do this mathematically is you, one way of doing it is you
*  build tensors into the neural network. So it's not just operating on matrices or big list numbers,
*  but it's actually operating with these mathematical entities, and the basic idea of a tensor is just
*  it has these nice rotational properties. It can kind of keep track of directions. So it has some
*  idea of which direction it's pointing in is the basic idea. And it turns out when you do this,
*  yes, it turns out the training data goes right down. And this was really appealing to me because
*  it has actually got deep parallels to the way we model intermolecular interactions,
*  which is what's important for building these simulations. There's the ways these things have
*  been modeled for decades. There's a thing called the multipole expansion, which basically describe
*  your interactions in terms of these tensors, dipoles, quadruples, oxipoles. You've heard these
*  terms, but these are actually mathematical tensors. And that's the way we've been doing it for
*  decades. And so it turns out that when you build that fact into the neural network, your training
*  data requirements go way down, obviously, because it can kind of exploit the fact that this is the
*  natural mathematical way to describe interactions of molecules. So that was a really nice kind of
*  example of how you could use fundamental physics ideas and combine it with AI to get you these
*  really advances in performance. Now, but there's a really interesting debate going on at the moment
*  about this, though, actually, because alpha fold two was the kind of one of the biggest breakthroughs,
*  obviously, in AI for science, and it used equivalence in the way its architecture worked.
*  But the latest version of alpha fold, alpha fold three, actually got rid of the equivalence,
*  and yet they still managed to get comparable performance to alpha fold two. So there's people
*  debating, is this actually critical or is it not? And the trick they used was a thing called
*  data augmentation. So they actually did feed raw coordinates into the model. And some other people
*  have showed this works for neural network potentials too. But they took the data set,
*  and then they rotated it in like a thousand different ways, and then fed that big, much
*  bigger data set with all these rotations into the neural network. And it turns out that when you do
*  that, you can at least get error metrics. So your loss and things can get as low as the
*  equilibrium models with a similar size training data. So it'll be very interesting to see
*  if these neural networks are actually as useful for practical tasks like running MD simulations,
*  which I haven't really seen yet. So that's going to be very interesting question moving forward.
*  Are there ways to get around building this equivalence into the neural network potentials?
*  Because the disadvantage of it is that it can slow your neural network down quite a lot,
*  because it's just a little bit more inherently complicated doing these kind of tensors, having
*  these tensors interact with each other rather than just normal matrices or lists of numbers.
*  So that's a really interesting thing to keep an eye on how that field advances. And as an example,
*  there's a paper from Apple recently where they said, swallowing the bitter pill. It's an example,
*  perhaps, of this bitter lesson that really there's no way to be smart about how you build your neural
*  network. And the answer is just to make it big with lots of parameters, and then get as much
*  data as you can basically, and let the neural network learn everything and don't try and
*  constrain it in interesting ways. So that's an interesting example. I'm kind of rooting for
*  equivalence to hold out because it's, you know, you think if there's anything that's worth building
*  into neural network, it would be like fundamental physical laws and like the symmetries of nature.
*  So we'll see how that turns out. It's very interesting. Hey, we'll continue our interview
*  in a moment after a word from our sponsors. Omnike uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work customized across all platforms
*  with a click of a button. I believe in Omnike so much that I invested in it,
*  and I recommend you use it too. Use Cogrev to get a 10% discount.
*  Hey, all. Eric Torenberg here. I'm hearing more and more that founders want to get profitable
*  and do more with less, especially with engineering. Listen, I love your 30 year old ex-fang senior
*  software engineer as much as the next guy, but honestly, I can't afford them anymore.
*  Founders everywhere are trying to turn to global talent, but boy, is it a hassle to do at scale,
*  from sourcing to interviewing to on the ground operations and management. That's why I teamed
*  up with Sean Lanahan, who's been building engineering teams in Vietnam at a very high level
*  for over five years to help you access global engineering without the headache. Squad, Sean's
*  a new company, takes care of sourcing, legal compliance, and local HR for global talent so
*  you don't have to. With teams across Asia and South America, we can cover you no matter which
*  time zone you operate in. Their engineers follow your process and use your tools. They work with
*  React, Next.js, or your favorite front end frameworks. And on the backend, they're experts at Node,
*  Python, Java, and anything under the sun. Full disclosure, it's going to cost more than the
*  random person you found on Upwork that's doing two hours of work per week but billing you for 40.
*  But you'll get premium quality at a fraction of the typical cost. Our engineers are vetted
*  top 1% talent and actually working hard for you every day. Increase your velocity without
*  amping up burn. Head to choose squad.com and mention Turpentine to skip the wait list.
*  So let me just make sure I understand a couple things. It seems like the big idea is from a
*  principles level, the coordinate system shouldn't matter, right? That's a very common thing in
*  physics. You can choose a convenient coordinate system, but in general, the coordinate system
*  shouldn't matter. So you can either find an elegant way to represent your data in this
*  relative to one another form, that is the equivalence form, and that abstracts away from
*  any particular choice of coordinate or any particular choice of origin point in the
*  representation of the data. But then your neural network architecture gets more complicated because
*  it has to handle this relative representation. Or you can do what Alpha Fold 3 did, and that is
*  just systematically apply a bunch of rotations and translations to the data and then feed that
*  all into a less complicated neural network but more data points sort of synthetically generated.
*  All of us are synthetically generated, but there's like the expensive waveform solution
*  generations, but then also the sort of very cheap presumably like translation and rotation
*  generations based on those, feed that into a comparatively simple neural network, more data
*  points, and it seems like we're in a world where either of those can work. And you might even
*  think it could come out in the wash or sort of in the limit they might converge on kind of
*  being the same thing. Yeah, exactly. I think that's probably where we're headed is that you can just
*  you can impose these, essentially you need to tell the neural network that it's in three-dimensional
*  space and it has these rotational properties. But you can do that in different ways. One is you can
*  put it on the data side and augment the data, or you can kind of encode it, hard code it into the
*  neural network itself and tell the neural network that actually restrict the things the neural
*  network can do so that it makes sure that it keeps track of the orientations of all these things in
*  space. Yeah, so there's kind of the two alternative ways of doing that and it'll be interesting to see
*  which one wins out. I suspect perhaps for these simulations, running these molecular dynamic
*  simulations, it may be worth having keeping that equivalence in the neural network itself just
*  because it may give you better generalizability once you get away from the data set or once you're
*  trying to do things like look at this crystallization from a lot of resources. So I'd be really
*  surprised, I guess, if these neural networks that impose it on the data side could still see this
*  kind of generalizability properties. So that's going to be something interesting to watch.
*  But yeah, that's essentially it. Yeah. Okay, cool. One ML paper that I would recommend
*  if anybody's interested in developing their intuition for this sort of equivalence concept,
*  but also just a really interesting finding about neural networks is called Relative Representations
*  Enable Zero-Shot Late-In-Space Communication. This is out of a group in Rome and also some folks from
*  Amazon. And this is a paper I kind of always go back to because they basically showed that the
*  latent spaces learned from the same data set across different training runs with different
*  initializations seem to be converging to the same thing, modulo, some sort of like rotation and
*  maybe like a scaling factor. And with that, if they can like figure out, you know, what is the sort of
*  rotation or scaling factor that's applied, then it creates potential for these model spaces to kind
*  of talk to each other or to potentially like distribute training. There could be implications
*  for that model merging, like who knows, right? There's a lot of kind of interesting, if there's
*  this like fundamental convergence, there's a lot of interesting downstream consequences of that. So
*  that paper is Relative Representations Enable Zero-Shot Late-In-Space Communication and a side.
*  Nice.
*  So, okay, going back to this crystallization phenomenon. So now we're all queued up to
*  hopefully appreciate, not on your level, but, you know, hopefully much more than we were at the
*  beginning, why this is special. So what you saw was you trained a, you collect a bunch of this data
*  in the computationally expensive way of solving the wave equation. You train a neural network
*  on it with positions in forces out. Now you're able to run this simulation propagating one femto or,
*  you know, a couple femto seconds at a time in this TikTok sort of way where it's here's the position,
*  calculate the forces, apply the forces, update the position, loop through that. But you're doing
*  this now with the network, doing the force predictions. And lo and behold, you see a salt
*  crystal forming in your simulated solution. You had said that there was no crystal in the training
*  data. How do you know that for one really stupid starting question?
*  Yeah. So, yeah, there's one other piece of the puzzle, which we should explain first, perhaps,
*  which is that that wasn't just a pure all-atom simulation where we saw the crystallization.
*  So we actually had one other step, which is we used coarse graining to get rid of the solvent
*  molecules, which maybe we can get to that. So that actual simulation was just the ions itself. And
*  we actually used a neural network potential to do that as well. So this is a really exciting, even
*  more recent use of these neural network potentials is not only can you go from predicting from the
*  positions of every atom to predicting the forces on every atom, but you can also do this trick called
*  coarse graining where you kind of ignore certain parts of the system. So we actually took a
*  simulation, an all-atom simulation, and then use this neural network potential to predict
*  the energies and the forces just on the ions. So that simulation actually didn't have any explicit
*  water in it. It was what we call an implicit water simulation. The AI had learned to kind of
*  implicitly, approximately account for what the water molecules are doing without having to exactly
*  calculate them. So this is kind of exactly analogous to what you do with the normal
*  neural network potential where you're getting rid of all of the electrons. So with a neural
*  network potential, you can just calculate the energies and forces from the positions of the
*  atoms themselves without ever kind of thinking about the electrons. And then you can do exactly
*  that same procedure again, but getting rid of the solvent molecules. So now you don't have to
*  incorporate the position of the solvent molecules into the neural network. You just predict the
*  energies and forces from the ions themselves. So this is another exciting way you can use these
*  neural network potentials to kind of push to even larger scales. So you're not having to stuck with
*  this simulations where you're treating every single water molecule in the simulation, because
*  that kind of has inherent data limitations. You've got to deal with when you want to push
*  to large systems, you've got to keep track of every single water molecule, and you end up just
*  spending a lot of computational time wasted studying how some water molecule out in the bulk
*  is buzzing around and rotating, which you don't actually care about at all. So this is the other
*  exciting thing we did in this paper. So people had done neural network potential MD of electrolytes
*  before. And if you do the all-atom way, you probably won't see crystallization, because
*  this crystallization phenomenon normally happens on very, very long time scales.
*  So that's how we're feeling confident that it isn't in the simulation, because it's very rare
*  to see these kind of things. It only happens typically if there's something really wrong with
*  your forces, if you're studying a normal salt like sodium chloride that doesn't normally precipitate
*  crystallize out of solution. But then you can also go back and explicitly check these things. So we
*  can compute a thing called the radial distribution function. It's basically just a histogram of the
*  distances. And you could look at that and it looks totally liquid-like, it has all the features of
*  the liquid at low concentration and so on. So there's no evidence in that simulation of any
*  crystals forming. And then you can just inspect the trajectories more directly as well and just
*  check and make sure that there's no signs of these crystals forming. So we did go back and check for
*  that in the all-atom and the full simulation that we trained this neural network potential on.
*  And so the exciting thing was, yeah, we saw this crystallization using this additional way that
*  you can use neural network potentials. We also, of course, ran out the solvent. And that was exciting,
*  because it means that you can do something that you can't do with these all-atom simulations,
*  really, which is that you can look at, very quickly look at things like crystallization with much less
*  compute time, basically. Because if you wanted to look at these kind of crystallization things with
*  the all-atom case, it would take a huge amount of computer time. You'd have to run it for very,
*  very long times. And you'd have to use probably a technique called enhanced sampling, where you kind
*  of force this crystallization to happen. Where here it just kind of dropped for free out of the
*  simulation. And the remarkable thing about that was, in particular, was when you do this
*  coarse-graining or getting rid of the solvent, is that the solvent is actually really, really
*  important in determining the interaction of ions. It actually makes the interactions about a hundred
*  times smaller. It's the thing called dielectric screening. The water molecules are incredibly
*  important in determining the interaction of the ions in water. So it's quite remarkable,
*  but that doesn't occur in the crystal, because there's no water there. And so, yes, somehow this
*  neural network potential now that's trained to get rid of the water molecules can, in fact,
*  kind of predict that as you go from this water to this crystal, what the structures are going to
*  look like, even though the strength of these interactions could be changing by almost a hundred
*  times as you go from these two different phases of material. So that was what made that even more
*  remarkable, is that it would have been nice if you just looked at longer time scales with the
*  neural net potential for crystallization, but we could also use this trick where you got rid of the
*  solvent molecules, and yet it still works to see these kind of phase transformations. Whereas I
*  would have thought that would never be possible. And this is actually what I was originally trying
*  to build in my PhD were these continuum solvent models, which is these models which ignore the
*  water and just treat the ions, which can be much, much faster, which is really their advantage.
*  But the problem is the water is so critically important that it's not clear at all how to do
*  that. So I spent my whole PhD, literally years, trying to build these things. And I didn't really
*  get very far trying to build them by hand and come up with mathematical equations and fit these
*  parameters and do all these things. Anyway, I built some models that were okay, but they're
*  really inherently limited in their generalizability. But here, the model, this was trained in just a few
*  hours, I think, automatically kind of realized and learned how to build one of these continuum
*  solvent models itself, and it could run simulations and it could see these emergent phenomena. So
*  that's really why it blew me away and was so surprising. This is the kind of thing that I'd
*  been trying to do for years. I had kind of given up and thought it was impossible, and yet it just
*  dropped out for free from training one of these neural networks, which was kind of all so exciting
*  about it. Okay. I want to dig in on this on a number of different fronts. That is definitely
*  really interesting, and I want to make sure I understand it all. I guess for
*  starters, in terms of how you knew that there wasn't crystallization in the data set,
*  it's a combination of you're running it for a very short period of time, a shorter
*  time scale than crystallization usually takes. And you also went back and screened the data and said,
*  can we spot any apparent crystals by just looking at are there things that appear to be bunched
*  together? And if you don't see that, then you can say, okay, there's no crystallization in this data
*  set. Yeah, exactly. So what you do see in the simulations is you see the sodium and chloride
*  ions kind of periodically pairing up, and then they'll come apart. And then occasionally you
*  might get triplet forming, but you don't really see any of these bigger clusters that look like
*  the crystal really. So yeah, that really indicates that it's not crystallizing the data.
*  It's a bit hard to determine exactly what the biggest cluster that forms is or what the most
*  similar thing in that liquid simulation is to the crystals. That's something to potentially dig into
*  further. How close is the training data? What is the closest example in that training data to a
*  true crystal? But definitely there's nothing like this crystal growth phenomenon where it starts
*  growing larger and larger and larger and kind of phase transforming the whole system.
*  Gotcha. Okay. So then in terms of the coarse graining concept, again, just for intuition's sake,
*  when we talk about solutions, I think of these measured in like molarity, right? So
*  a one molar, you can tell me how many molar your solutions are, but a one molar solution of salt
*  water would be one mole of salt in a liter of water. And so a liter of water is a kilogram
*  and a mole of salt would be whatever, like 30 grams or something. So we're one part in 30
*  something along those lines. Yeah, that's a rough order of magnitude. Yeah. So I think technically
*  we were at four moles. So the molarity of pure water, I believe is around 55 moles per liter. So
*  if you're at four moles, you have 10 water molecules for every salt ion is probably reasonable.
*  Gotcha. Okay. So now we got one ion per 10 water molecules. The idea with the
*  removing of the water portion of the all-item simulation. So you're running in the simulation,
*  you are computing all the water molecules, all the ions, but then is the intuition that
*  the main forces come from the ions because they're actually imbalanced in charge,
*  whereas the water is neutral and it has its polarity, but it's not because of the fundamental
*  neutrality versus the imbalance in charge. Is that where my intuition should come from,
*  that I might be able to abstract away from the water in the first place?
*  Yeah. So the forces from the water molecules are actually very large though. So they actually play
*  a really important role in determining the force on the ions. So the technical thing we're doing is
*  it's called integrating out or, you know, probability speak, it's marginalization.
*  So the water molecules are still implicitly accounted for. It's not like you're ignoring them,
*  although I may have said that technically, they're more kind of the average effect is still
*  accounted for in the simulation through a kind of average effect. And that's the real challenge of
*  it is that these water molecules do play a big role in determining the interactions of the ions,
*  but it's just, you can account for that effect in an average way is the basic idea. So that
*  rather than treating, so you've got these two ions interacting and rather than saying, okay,
*  I need to know how every single water molecule around them is arranged to calculate the force on
*  them. I can say on average, what would the force between these two ions be if I average over all
*  the potential configurations of the water molecules around them? And that's the really challenging
*  thing. So that's why it's so incredibly hard to build these continuum solvent models, because the
*  water molecules are actually critically important. So you're right, the water molecules are neutral
*  and the ions are charged. So you get these large charge-charge interactions, but the water molecules
*  are absolutely critical there because they actually reduce the size of that charge-charge
*  interaction by a factor of 80. So it's absolutely critical. The water is absolutely central there,
*  it's really, really hard to get rid of. And that's why it's so hard in my PhD, trying to find ways of
*  ignoring them. It turns out it's just really hard to do. But that's the beauty of these neural
*  network potentials is that they can somehow automatically average over all of the effects
*  of all of these water molecules. And you still get you an accurate prediction of what the forces
*  on the ions are going to be on average, when you average over the behavior of all the water molecules.
*  And so that's what, yeah, that's really... So does that suggest if I'm envisioning
*  what's going on in solution, the ability to average in this way, which I guess procedurally is like,
*  you're taking this all-atom simulated output and literally just removing the water from it,
*  and now you're training the network on purely the positions of the ions?
*  Yeah, that's what you do, it's pretty simple.
*  So each ion, then I guess I should understand this, being surrounded by a lot of water
*  model molecules most of the time. It's not like it's randomly interacting with one molecule at a
*  time, because then it would seem really hard to abstract away. It's like in a shell of water
*  molecules as kind of its default state. Yeah, exactly. They're surrounded by many water
*  molecules. And so you have to give the neural network a lot of examples of the positions and
*  forces on the ions alone. And you need to do that so that it can average over the water molecules.
*  So if you only gave it a few examples of ions without the water molecules, it wouldn't be able
*  to do it because it needs to know all of the different ways that these water molecules could
*  be arranged. Can we average over that? So you actually need to train the coarse grain model,
*  you actually need a lot more data or a lot longer simulations. The data is obviously smaller because
*  you only need the ions, but you need a lot longer simulations to generate the training data for
*  training these coarse grain models because they have to do this averaging over all of the water
*  molecules. So in a given position of ions, you don't have a unique set of forces because it's
*  going to depend on the waters, but you do have a unique average set of forces. And that's what
*  you're getting the neural network to calculate, this average forces on all of the ions in these
*  positions. Whereas the normal way we use the neural network potential, which we talked about before,
*  there is actually a unique force on every single atom in the system, which comes from solving
*  Schrodinger's equation. So you're kind of using the neural network in two slightly different ways.
*  One is to compute the exact energies and forces on every single atom. And then the second way you
*  can use it is to calculate the average energies and forces on these things. And technically,
*  what we're talking about here is actually free energies. So we're using the neural network
*  potential to calculate free energies rather than pure energies. There's some underlying statistical
*  mechanical theory that kind of makes all of this make sense and makes this rigorous, which is quite
*  nice. Okay, very interesting. So now, through the crystallization, how should we understand this?
*  I mean, it is a, for one thing, it's a phase change, right? You talked about orders of magnitude,
*  different amount of force being exerted by the ions on one another when they're in crystal form
*  versus when they're in solution form. I think you said it was like 80 times or something?
*  Yeah, exactly. So you've got this in water, the ions obviously come apart and they're dissolved
*  and they're floating around freely and the water in between actually reduces their interactions by
*  this factor of 80. It's called dielectric screening. Whereas in the crystal, that's not going to happen
*  at all. There, you know, you have much stronger forces kind of sticking these ions together.
*  So that's why I thought that it would never be possible to look at crystallization and liquid
*  phase with the same kind of continuum solvent model. So that's why it kind of blew me away
*  when we saw it happen. Because obviously, you could see these crystallization phenomena in the
*  all-atom case, if you kind of drive it to happen, because there, you know, you don't have this
*  problem with the water molecules kind of being very relevant in the solution and not relevant
*  to the crystal. So that's what was so surprising about the fact that it was able to do that.
*  We still don't have our head around exactly why it can do these things. Is there something we want
*  to dig into kind of further? What I suspect is that because in the solution phase, because you
*  get those kind of pairs forming and these triplets forming and the possibly larger clusters
*  forming transiently, that the neural network can look at those and kind of extrapolate and say,
*  oh, I see what's happening when these pairs are forming, that water is squeezed out and therefore
*  the forces are getting larger between the ions in those cases. And so it's kind of then learning
*  that information implicitly, and then it can take that and extrapolate to what it's going to look
*  like in the crystal. That's what's kind of interesting now. But an important caveat is
*  that it cannot do this kind of quantitatively precisely. You know, so I don't think,
*  in effect, we know that it's not going to get the quantitatively exactly things like the solubility,
*  how much salt you need to make the crystal precisely right. That's not the kind of thing
*  it'll get right because it doesn't have any training data on the crystal itself. You know,
*  there's going to be small quantitative errors there. So that's an issue, but that can still be fixed,
*  I think, fairly easily. Once you've seen the crystallization, then the obvious next step to
*  do is to take those crystal structures and then you could add that to your training data set and
*  do a thing called active learning and try and get those things quantitatively. So that's kind
*  of where we want to go from here, I think, to start trying to add data on the crystal and see
*  how precise we can get these things in terms of actually making precise predictions of experiment,
*  which would even be even nicer. But yeah, this stage is still a bit of a surprise that it could
*  do this at all. So still just trying to work out exactly what's going on, where it's getting the
*  information it needs to kind of predict what the crystal is going to look like.
*  I wonder if we should think about this as the network generalizing out of distribution or
*  if this is sort of a property of like the outer loop. Because I mean, in language models,
*  you're probably familiar with this. It's pretty well established at this point. And certainly
*  listeners heard me talk about it many times, that there are these higher order concepts that are
*  being learned purely as a means to next token prediction. But nevertheless, we can now go in
*  and identify these concepts for autoencoder techniques and representation engineering and
*  even demonstrate that you can steer a language model by injecting one of those directions or
*  activations or features is a better term than activation. You can inject that at runtime and
*  you can steer the output of the model based on that. Sounds like that's not quite what's
*  happening here. I don't think from your account that I should expect that there is a feature
*  that's been learned in the network that is like the crystallization feature or concept. But rather,
*  it would seem to be more of just like, as things sort of approach a certain position,
*  the forces are such that they walk into a grid and stay there for at least some amount of time.
*  Does that seem right? Or could we even resolve that with what we know?
*  Yeah, this is a fascinating question. I definitely don't have the answer. So
*  the way to think about it, though, I think is to think in terms of matching surfaces, essentially.
*  So when we're trying to compute the energies from the positions, you can think of that as trying to
*  match what we call the potential energy surface, which is the basic idea that as a function of
*  the position, which is just a vector, the positions of all of your atoms, that has some energy value.
*  And this is a high dimensional surface, you can imagine. It's like a single value that you
*  map to from the positions of all of your atoms. And it's exactly the same thing with these
*  coarse-grained simulations, where it's now a free energy surface that you're trying to match.
*  And so in the simplest possible case, so imagine you just had two positions. So you have a single
*  atom and it's in two dimensions. That actually you can visualize that exactly as a surface.
*  Every two points in that two dimensional plane, there's some energy, which you can imagine is
*  kind of the height of that surface. And then you can generalize this to higher dimensions.
*  And this is what the neural network potential is actually learning. It's learning that surface.
*  And it turns out that the neural network potential, you can train it on one region of the surface
*  and somehow it can extrapolate to what it would look like in other areas of that surface.
*  So then you're only training it where it's in the liquid phase and it's kind of matching the
*  surface as best it can. And it's got these kind of equivalence and these various constraints, which
*  it's trying to use to match that. And it turns out that somehow that can also do a good job,
*  at least approximately, at predicting what that surface is going to look like when it's in the
*  crystal structure. So you can imagine the crystal, there's some like a potential energy well, we call
*  it. There's some like sharp dip in that surface, which means it has a lower energy, which means
*  it's likely to be in that state. And so that's the way to think about what it's learning. It's
*  actually learning that high dimensional energy surface. And then that's what it's using to then
*  do these dynamics, because you use MD to kind of move the atoms around on the surface. And the
*  atoms like to be in lower energy states. That's what statistical mechanics tells us. And so that's
*  kind of what it's, if you want to think about the concept it's learning, although this is a very big
*  idea, what is even is the concept, but that's kind of what intuitively I would think about what it's
*  learning. And now there's interesting parallel with this to large language models, which is that
*  people often talk about large language models as fitting a surface as well. They're just fitting
*  a different kind of surface. In fact, they're fitting the probability surface of next words.
*  Right. And so that's what these GPT, these big transformers are doing. They're predicting the
*  next word. And that's just a probability, right? That's every vector that represents your sentence,
*  every word has another probability. So that's a probability surface that you're fitting.
*  And in fact, this actually has deep connections to statistical mechanics,
*  because the log of your probability density and statistical mechanics is actually an energy
*  to do with think of the Boltzmann distribution. So there are actually deep connections between
*  what's going on with these large language models and what's going on with the training, these neural
*  network potentials. Now, when it comes to this idea of these concepts or the fact that these
*  large language models seem to have this ability to kind of have some notion of concepts and
*  generalize out of exactly what they've been trained on, which is kind of this surprising
*  phenomena. I mean, I would speculate that it may be something similar going on. I mean, that in
*  sense that when you learn this kind of probability surface very accurately, that then allows you to
*  extrapolate to other regions of that probability surface and to make predictions there. And so
*  probably, you know, I mean, we don't really fully know what's going on in these things,
*  but there may be some parallels there. And you actually see some evidence for this in the way
*  these large language models work. I mean, they use a softmax layer in them, which means they're,
*  which is the softmax is the normalization layer. That is actually a Boltzmann distribution they're
*  using. That's actually an idea that comes from statistical mechanics that comes from these MD
*  simulations. And so there are, you know, they always talk about log probabilities, you know,
*  you hear that very often. Well, a log probability in statistical mechanics is a free energy. So
*  there's actually some deep mathematical connections going on here. And I don't have my head fully
*  around it, but I really think this is a direction that's worth pursuing is thinking about these
*  connections between statistical mechanics and large language models, because I think there may
*  be some kind of deeper connections going on there. Yeah. Okay. Definitely very interesting. So
*  more about the generalization potential. You had another phenomenon that you reported as well,
*  which was self-bionization of water, I guess, now back to the all-atom case there. But
*  tell us about that. Yeah. So that was another kind of thing that really kind of blew me away
*  and surprised me. And now that people have actually seen this as well, and I think no one
*  really knew quite what to make of it, but it's very interesting. So when you run these water
*  simulations, so now you're including all of the water molecules. And in this case, you were just
*  trained on pure water or maybe some ions in water. When you run these simulations for long enough,
*  you actually see this phenomenon called water self-ionization. And basically what that means
*  is the hydrogen pops off a water molecule onto its neighboring water molecule, and it forms an OH
*  and an H3O. So instead of two H2Os, you have these two separate, what they're now ions.
*  And this is a phenomenon that we know happens in real water. In fact, about one out of every,
*  I think it's 10 million atoms or 10 million water molecules will be in this kind of ionized state.
*  And it's very, very important. That's pH. That's where the pH of water comes from.
*  10 to the minus 7. Yeah. Exactly. Yeah. So we know that this happens in real water. And so
*  the remarkable thing is the neural network potential is actually kind of predicting that
*  this will happen. It's saying, oh, possibly it's running these simulations. And then every now and
*  then, occasionally, one of these hydrogens is hopping off onto its neighboring atom. And that's
*  not something that it's seen in the training data. And it somehow knows that that's kind of
*  a fairly plausible thing that might happen. And then the really impressive thing is it keeps the
*  correct shape of that hydronium ion, that H3O ion. It keeps it in this kind of pyramid type shape,
*  which was really surprising. I would have thought it would kind of, once you get outside of where
*  it's seen, I would have thought it would just kind of break and go crazy or do something very
*  unphysical, which you do see quite often, honestly. So I would have thought it would break and not be
*  able to handle that. But it actually keeps running. The simulation stays stable. And then you see the
*  thing called growthless hopping, which is then another hydrogen will hop off from that H3O to
*  its neighbor. And you get these chains of hopping hydrogens, which is actually this really important
*  mechanism which explains why acid diffuses through water so quickly. So this is actually
*  a really important physical phenomenon. The neural network potential is just kind of guessing that
*  it's going to happen, which I thought was quite impressive. Now, this is very well studied. So
*  it's not really telling us anything new. But it does imply that maybe there will be cases where
*  it could find things or suggest things that are new that we haven't thought of, which is quite
*  an interesting idea. Now, but there's a big caveat, which I need to mention, which is coming back to
*  the same point about crystallization, that it doesn't get these quantitatively precisely. So
*  it's not going to predict the rate at which this occurs exactly. In fact, it does it much too fast.
*  So it shouldn't really happen in a normal simulation. You shouldn't see this happen on the
*  kind of this picosecond time scale we normally access. Or you can get to nanoseconds or much
*  longer with these NNPs, the neural network potentials. But you still shouldn't really see it.
*  You should have to force it to happen. So the fact that it happens is not necessarily physically
*  correct. And so that's an important caveat that you can't get things quantitatively precisely
*  outside of its training data. But it's almost, it's not necessarily a bad thing. When it goes
*  outside of training data, it can still make reasonable guesses and suggest interesting
*  phenomena that might occur. And that's something that we can easily fix if we want to. And in fact,
*  people have now fixed this and trained these neural network potentials explicitly to get this
*  process right. So you add training data exactly on this hydrogen atom as it comes off the water
*  molecule, get lots and lots of quantum chemical training data on that, and then simulate the
*  whole thing very well. And you can actually precisely predict now that pH7 belly of water,
*  which is very nice. So how does that process work? I guess I'm imagining when you're generating
*  the training data via the simulation, you could take one initial condition and just run it
*  indefinitely. But I guess you could also set up a bunch of initial conditions intentionally,
*  and then run from a bunch of different starting points. I'm guessing something like that is
*  what's happening where people are saying, let's bring two water molecules into the right,
*  form the right configuration for that to happen. So we can start to have more of that in the
*  training data. Is that right? Yes, exactly. So what I normally do is just start with what's
*  called an equilibrium molecular simulation. So you just give the atoms, you tell it the
*  temperature, room temperature, and then you just run the simulation and generate your training data
*  from that. But that won't sample what we call rare events, which are things that happen very
*  infrequently, things like crystallization or this hydrogen hopping off the water molecule type
*  phenomenon. And so there are various strategies you can use to get some of those more rare events.
*  One is you can run it at higher temperature, or you could, as you say, run a ton of these things
*  in parallel and hope that that explores your phase space better with different initial starting
*  coordinates. Another thing you can do is called enhanced sampling. You kind of drive these systems
*  out of their local minima, you know, the positions they'd like to sit in, you kind of force them to
*  different arrangements and things. But then another really nice idea, which is probably the most
*  powerful one, is this idea of active learning, which people have shown now works really well
*  for these. And the idea here is you train a neural network, and you go and run much longer molecular
*  simulations with that neural network. And then you have some method of estimating the uncertainty
*  and the predictions of the neural network. And then whenever that uncertainty spikes, whenever it
*  says, oh, I'm not sure about this one, then you take that data, and then you go and add that to
*  your training data set and do new quantum chemistry calculations on it. And then you can expand your
*  data set to cover kind of these rare events that don't normally happen in the simulation when you're
*  just running these short ones to get the training data. And people are showing now that this is a
*  really powerful technique. And you start to kind of, and you can imagine this is kind of a feedback
*  loop, right? You can start to build your training data set, cover more and more space, cover more
*  interesting phenomena. And then you can start to think about simulating things, yeah, like chemical
*  reactions, which is really important. So people now are doing some really nice things on this,
*  simulating, you know, catalysis, so the reactions on surfaces using these techniques,
*  and they're getting really powerful. So that's really exciting as well.
*  Yeah, that's interesting. That honestly reminds me in some ways of just down the fairway,
*  LLM app development that I've done at times where there's just sort of bootstrapping loop in
*  a lot of cases where, especially if you're working with a pre-trained model,
*  as we normally are in a language model case, you don't need that many examples to fine tune.
*  And, you know, I often recommend like SVU S10 can be enough to do that initial fine tune.
*  And then it's all about identifying edge cases and supplementing that data set.
*  Exactly, yeah.
*  It's a more quantitative way to identify your edge cases than I typically do.
*  Yeah, because the problem with the chat, you know, the hallucinations and things is there's no
*  just function you can go call and go say, you know, what is the ground truth here? And so,
*  you know, it's very hard to tell or to add to your training data the correct things. Often you'll
*  have to go get a human to kind of label those things, I guess, is the way you do the same thing
*  for a large language model. But the nice thing here is you can kind of do it all within a
*  computational loop, right? So you can kind of automate it and get it all internally happening
*  on one supercomputer. And so you can really start to get these things scaling up in a kind
*  of automated way, which is quite nice because you've always got that kind of ground truth,
*  you can go and just automatically refer to them and calculate, which makes it a kind of really
*  nice powerful technique, I think. Yeah. So if we're seeing this level of generalization,
*  where we're seeing these self-ionization and crystallization phenomena happening with really
*  rather modest compute resources to generate these data sets, then I guess I wonder how far can this
*  go? And you're probably wondering that too, but has it gone any farther than this yet? And what
*  would be prospects for, I guess, there's a lot of different dimensions, right? I guess I don't really
*  know how you're dealing with temperature. You said a second ago that you can, you know, you put your
*  temperature into the simulation. Do you also put the temperature in as like a free parameter into
*  the network? Do these networks have or have the prospect to accept a bunch of other free parameters
*  like temperature, pressure, whatever else? Yeah. So the really nice thing about this method is that
*  the potential energy surface, you know, these energies and these forces that we're learning,
*  those don't depend on temperature. So when you solve Schrodinger's equation, it doesn't know
*  anything about temperature, right? That's just given the positions, give me the energies and
*  forces. The way that temperature comes in is actually in this classical motion solver,
*  solving Newton's equations where you calculate how the atoms are moving. That's where you add
*  a thing called a thermostat, which just basically controls the temperature, right? Just like a normal
*  thermostat. If it's getting too hot, you'll remove some energy. If it's too cold, you'll add some
*  energy. So it's actually really trivial to run these things at high temperatures. So we've run
*  all these electrolyte solutions simulations at different temperatures and they're perfectly
*  stable. So that's quite exciting because it should be definitely generalizable to different
*  temperatures as well. Microsoft just had a big paper called MatterSim where they were looking
*  at this and they showed you, you can simulate over a huge range of temperatures, which is really nice.
*  So definitely, yeah, that's the kind of directions we want to be going in, right? Because this is
*  where it gets very hard experimentally. You can, you're going to measure everything at different
*  temperatures and then when things get hot, you know, your equipment starts to run into issues.
*  So this is a really nice aspect of this computation. I think it's almost trivial to change the
*  temperature. Now you may, in some cases, you probably need to add training data at these higher
*  temperatures, say, or so there may be some cases where things break at different temperatures if
*  you don't have enough training data. But in principle, yes, changing the temperatures is a
*  very trivial thing to do. And this is the nice thing about kind of coupling it with this more
*  physical solver, you know, this kind of physical engine, the physics engine, because that means
*  that you don't really have, you know, if you were relying on the neural network to learn everything,
*  it would have to learn like, oh, how does everything change with temperature? Right?
*  So that would be a much harder kind of AI problem, I think. Whereas in this case, you can kind of
*  use the fact that you're learning something that's independent of temperature, which is
*  really nice feature. So if you have this thermostat and you can turn it up and down so freely, can you
*  turn it down to freezing point and see everything crystallize or turn it up to boiling point and see
*  everything turn to gas? Yes, yes, you can definitely do that. The issue with just cooling everything
*  down to try and crystallize it is that you get this called amorphous crystallization. So like a
*  glass, you know, if you take silicon and cool it down too quickly, it amorphously crystallizes and
*  forms like a basically just like a solid liquid, just a liquid that stops the atom stop moving
*  very much. So if you just turn the temperature down too quickly, that's often what you see there.
*  But so it's not as easy to induce crystallization as you might think. But
*  yeah, that's certainly something that we want to explore more. Can you do those kind of things?
*  Absolutely. When I freeze water in my freezer at home, I'm getting an actual crystal, right? Or
*  am I getting a sort of water glass? Yeah, you can get water glasses, but those have to be done in
*  the lab because you have to freeze it very, very quickly, I think. In the normal forms of ice are
*  a type of crystal. Yeah, they have a nice crystalline structure, kind of where you get this
*  hydrogen bonding structures forming. So yeah, you're getting a crystal when you freeze it at
*  home, but there are certain types of ice. You know, there is actually a whole phase diagram of ice
*  can form all of these crazy different phases at different temperatures and pressures and speed.
*  So if in a simulation, you know, because we're using these picosecond time scales, if you just
*  turn the temperature down too quickly, it will just, you'll probably just get an amorphous freezing.
*  But people have, people are now using these neural net potentials a lot to look at ice phases and ice
*  water equilibrium and doing all sorts of fantastic work there. So you can definitely probe the
*  crystallization of ice water. And there is actually a paper, so there is some precedent for the salt
*  crystallization we saw. There's a nice paper where they looked at simulating water and they showed
*  basically the same thing. You can see little water structures that look a little bit like the ice
*  structures. And so you can actually train a neural network on water and then use that to say interesting
*  things about ice as well. So there's probably similar parallels going on with ice crystallization,
*  water crystallization, which is ice. So what other dimensions of generalization do you see or
*  expect? Like you could imagine training on two kinds of salt solution and trying to predict what
*  happens with a third. I mean, obviously you could really run with this thing a lot if you're scaling
*  up the data sets. And it sounds like there are quite a few orders of magnitude of scale up that
*  would be like start to get expensive, but certainly not out of bounds of the sorts of models that we're
*  seeing trained today. You're talking about a couple of days of compute time here or there.
*  Certainly you probably have a thousand X room to go that you could like plausibly write a grant for.
*  Right. What would you expect to see as you go up these orders of magnitude?
*  Yeah, definitely. So that's the interesting thing. Yeah. Moving forward. And people are already doing
*  this in fact, bike dance actually, the company behind TikTok actually had a paper on electrolyte
*  simulation on exactly this, right? They're trying to do this scaling up. So they're not,
*  I'm trying to get these things really, really accurate and precise. They're trying to scale up
*  and look at many different electrolyte solutions and they'll build a big database of electrolyte
*  solutions. And they saw exactly this. They could train their model on certain electrolytes and then
*  generalize it to new ones that hadn't been seen in the training data, which is very interesting.
*  So they were simulating organic electrolytes, I think, where it turns out these things are made
*  up of carbons and hydrogens. So you can kind of extrapolate from one to another, which is quite
*  exciting. So definitely we're starting to see evidence of the ability of these things to
*  generalize to new cases where they don't have the training data on them, because there's enough
*  similar examples where you do have the training data. And so that's really the exciting direction
*  to go in. And yeah, so this is starting to become a big field. And people talk about these things as
*  the universal kind of machine learning potential. And the basic idea is you want to train one model
*  that then you can put any elements into it and any kind of arrangement of atoms and calculate the
*  forces on every single one of them. And so it's quite different to what I'm doing where I'm trying
*  to build a model just for one particular case. They're trying to build these universal ones that
*  can handle any arrangement of atoms. And the big tech companies are starting to get into this as
*  well. So the ByteDance has the electrolyte one, Microsoft has one called MatterSim just came out,
*  Google had this Nature paper recently where they trained one of these called Gnome, and they showed
*  that they could find millions of new crystal structures, which was very, very cool. Meta are
*  working on one of these as well. So yeah, all of these, this is starting to really take off now.
*  The kind of thing that I think maybe industry is a better place to do because they have these huge
*  compute resources and they're starting to scale up these models and build these really universal ones.
*  And what we're hoping, I think we're starting to see evidence of this, certainly these papers are
*  starting to show evidence of this, is that you'll see the same thing that you saw with the large
*  language models when you scaled them up, right? That yeah, exactly as you were saying earlier,
*  you don't need to add nearly as much additional training data once you've got this good, really
*  good foundation to start with. So it's learning all these kind of general features about the ways
*  atoms interact. And then if you want to get, if you want to study a new system,
*  just adding a little bit of extra data on that new system will then get you a really accurate
*  description of it much more quickly than you would need if you're starting from scratch.
*  And so that's really exciting because you can start to think about, well, this could be a
*  universal tool that we start to use as a kind of first estimate to get an estimate of what any
*  system is doing. And it's just go straight to one of these universal force fields and simulate it,
*  if they could run them quickly enough and start to get a picture of exactly what's happening at
*  the molecular scale for any system you're interested in, which is a really, really exciting
*  idea. And I think it could be a profoundly kind of transformative scientific tool once you get
*  this thing really up and running efficiently and get it in the hands of scientists who can really
*  use it to do exciting things with it. And there will always be cases where it breaks and where
*  it fails, right? Just like ChaktiVidhi hallucinates and goes wrong in different places. There'll be
*  systems where it has problems and has issues. And so you'll need to keep it in this kind of
*  interactive loop where you're always adding extra training data, going and doing extra quantum
*  chemistry calculations, and then essentially fine tuning it, right? Fine tuning for particular
*  applications is probably what we'll have to keep doing. But it's a really exciting future, I think,
*  as people start to scale these models up. And there's a nice one called MACE Zero, an open
*  source one recently, which is very cool. And the remarkable thing about that was they trained it on
*  crystal data. So solid data is kind of the inverse of what we saw. We trained on the solution and
*  saw crystallization. They trained it only on crystals and they showed that you could simulate
*  liquids with it. So that was very exciting too. So I think these things are really going to start
*  taking off in the near-term future and that's really exciting. Yeah, there's a couple big themes
*  there. One is the possibility of what I've brought, a term I brought from a friend, the big tech
*  singularity, where it seems like we've seen plenty of fiction over the years where like five companies
*  take over the world or whatever. But this is another dimension on which, man, if you really
*  just have to scale it up and there's only a handful of companies that have the ability to do that,
*  these big tech companies potentially start to come in and dominate material science.
*  Is that kind of what you would expect the future of the field to look like?
*  Yeah, I think it's certainly a possibility and I think it's a risk. And I think the governments
*  and the public sector needs to get onto this and start saying, okay, this is a serious area. We need
*  to fund independent groups who aren't in private companies to build these things as well, build
*  these tools as well so that we can have experts who are outside these companies who really
*  understand these things. I think that's a really important thing that needs to be done. Yeah,
*  I think there's no reason we can build, there's like CERN, the Large Hadron Collider. There's
*  examples of huge science projects where the public sector has put large amounts of investment and
*  built these big things. So I think there's no reason that we have to leave it to these big
*  companies. It's not the kind of thing that's suited to maybe academia. We have these small groups with
*  one professor and a number of PhD students. I think we need to move away from that model,
*  but I think there are examples of science. There's big interdisciplinary collaborations.
*  We start to think about getting all these people together. And the Mesa Zero paper was a really
*  nice example of that where they got a huge team of people together who are collaborating to build
*  one of these foundational models. So I think there's hope yet that we can build these things
*  and open source them. But yeah, I think there is really a possibility that these things stay
*  internally in these companies. And so we saw this big debate around this with AlphaFold 3,
*  where they're hanging on to keeping those models private, at least for now. And so that'll be a
*  very interesting to see how this plays out. Will they release these models to allow the scientists
*  to use them? Because a big concern I have is I've trained these big models. There's so many
*  incredible simulations you could run with these things. And yet internally in these companies,
*  there's not that many people to run these simulations. So I think it would be way more
*  valuable if they released these tools to the public or to other scientists in academia to use
*  them. But having said that, these things take a huge amount of resources to build. If you're
*  spending huge amounts of GPUs on building these data sets, that's a big investment of money.
*  And it's understandable that these companies want to recoup their investments. So it's a complicated
*  issue. And it'll be very interesting to see how it plays out. But I think definitely there's room
*  for the governments and academia and the public sector essentially to get into this area as well.
*  Yeah. Another big theme is the fact that China is not really all that far behind. I'm one who
*  wants to avoid the AI arms race with China almost at all costs, maybe not at all costs. But
*  in terms of ways the future could go badly, I feel like a throw caution to the wind AI arms
*  race with China would be a bad one. And one way I think we might trick ourselves into going down
*  that path is if we dilute ourselves into thinking that we have a big lead and we're going to win the
*  race. And so I always note these examples where Chinese big tech companies or whatever academic
*  groups in some cases as well are producing top-notch stuff. And as far as I can tell,
*  don't actually seem to be all that far behind. That could change, but I don't even need to
*  comment on that unless you have one. But it is notable that they're not far behind on this
*  dimension either. Yeah. There's definitely a lot of fantastic research in this area coming out of
*  China. And I think it has big economic implications. You could start to really do materials design,
*  understand biology. There's so much... Whenever you get big scientific breakthroughs, it has
*  a massive technological and economic implications as well. So yeah, I think it's something that we
*  should really be thinking about a lot more. And yeah, how to avoid the arms race, I'm not sure.
*  That's a very tricky question that's above my pay grade, fortunately.
*  Unfortunately, I don't think there's any designated adults either that we can
*  answer that question too. Regardless of pay grade, we might all have to take that one up.
*  Yeah, that's true.
*  To our little part on it. Is there a safety concern with these sorts of models? I mean,
*  obviously, people talk a lot about highly generalist models and are they going to do
*  what we want them to do and not. And then with biology models, you have sort of inherent dual
*  use of like... If you can cure a disease, you can probably also cause a disease. Is there something
*  similar here or is this more of a one-way bet type of technology? I have a little bit of harder time
*  imagining this sort of harmful material science use case. But maybe it's that I just have limited
*  imagination.
*  No, no. So I mean, one point is that these neural network potentials are not at all just limited
*  to material science, right? People are also using them in biology to really interesting effects.
*  So there's a paper from the David Baker group in science recently where they used any one of these
*  neural network potentials to design new drug molecules. And that seemed to work pretty well.
*  And the state of the art, in fact, for this problem of drug binding to proteins,
*  calculating how strongly a drug molecule will bind to a protein, a recent pre-pron actually showed
*  that the state of the art was using one of these neural network potentials, at least for the core
*  component of it, for that actual drug molecule. So these things definitely have implications for
*  biology as well. So just the same pathway that biology and AI is a very powerful tool could be
*  potentially a concern there. You could use these neural net potentials to design drugs and things
*  that could potentially be harmful. So yeah, that's definitely a concern. Yeah, in terms of material
*  science, yeah, I don't think so much, it's not probably not so much been issued there.
*  Other than to say that material science is really important for a lot of defense industries,
*  obviously, if you're trying to make various new materials, a key limitation of a lot of things is
*  the ability to design new materials. But I'm not too concerned about the safety things at this stage.
*  I wouldn't be too much too worried about it. But yeah, you can imagine at some point when these
*  tools get powerful enough that they start to have enough technological implications that something
*  you want to start thinking about quite seriously. Have you seen the recent paper on cans? Instead of
*  the Tegmark group? K-A-Ns, yeah. Yeah. That's a very interesting paper. But it's basically new
*  architecture, right? Where instead of learning the weights that are edges between nodes in a network,
*  they are learning functions that sit on those edges. So instead of just a single number at each edge,
*  it's a function at each edge. And then instead of having an activation function on a layer by layer
*  basis at the nodes, they're just adding the inputs from the different learned functions on the edges.
*  So this makes more intuitive sense if you look at a diagram, which they have in the paper and
*  definitely recommend that and hopefully, again, have an episode coming soon about it. They seem
*  to think that this is going to be most applicable in science because it seems to address the sort of
*  composability problem where you can now learn functions of functions and do all sorts of
*  interesting more. And it's also much more interpretable because you can actually just
*  look at the shape of the individual functions that are being learned. Do you think that has
*  promise for the sort of work you're doing or how would you connect the dots between
*  your work and that new potential tool? Yeah. That's definitely really exciting.
*  I think it certainly has potential. I really like this idea. The problem essentially is a
*  simple word like fitting a surface, right? It's a very high dimensional function. You have some
*  the positions of every single atom and you're trying to predict the energy, just a single number.
*  And so that's exactly what these KANs are trying to do, trying to find good approximations of these
*  multi-dimensional high dimensional functions. And so that, yeah, it makes sense to me as an
*  approach that could really perhaps help with the generalizability and build these things that are
*  generalizable. And I like that they showed in the paper that you could improve the generalizability
*  without spoiling what they'd already been trained on. Whereas with some of the normal multi-lapsed
*  electron type approaches, perhaps you would lose some of what it had been trained on previously
*  when you added additional data and fine-tuned these things. So yeah, there's potential advantages
*  there. I definitely think these things should be explored. I think a big issue though is obviously
*  that the computational limitations, what's going to be computationally most efficient? Because in the
*  end, we are looking to run these things as fast as possible. And so you really need to demonstrate
*  that you get some really solid advances in order to justify switching to a new architecture. But I
*  definitely hope someone is trying out building a neural net potential with these KANs. I think that
*  would be really cool and really interesting to see how they perform. I think that makes a lot of sense.
*  I think, yeah, my kind of philosophy and the thing I love about the machine learning community,
*  which is that it's very empirical. So there's a lot of trial and error and just empirically
*  testing things out, seeing what works well and seeing what doesn't. But then also using fundamental
*  theory where you need to, it is inspiration for coming up with new ideas. And so that KANs was a
*  nice example of that. But it'll be interesting to see how it plays out if they are actually
*  generalizable. I saw some people arguing that they were kind of, you could map them to a simple
*  multi-lapsed electron in a way. So whether they are genuinely give you additional new properties
*  or new behaviors will be very interesting to see. Or whether it's just a matter of whether they
*  reduce training data requirements. It's always very hard to predict in advance what's going to
*  work and what's not. So it'll be great, interesting to see. But I think this just needs to be empirically
*  tested. There's definitely a strong trend of some sort of fundamental equivalence between a lot of
*  very apparently different things. Yeah. Sometimes I get frustrated. I feel like there's some deeper
*  theory missing underlying these things. And I think it would be really great if we could get a
*  more rigorous description. And I know a lot of people on this. It's exactly why these neural
*  network potentials, neural networks in general work so well. When do they work? When are they
*  not going to work? That's really lacking. I don't know. That's a big area of research. So it'll be
*  very interesting to see what comes out of that. So just zooming out, how do you expect all this to
*  shape the pace of discovery in science over the next few years? It seems like you've touched on
*  a number of obviously super high value use cases. And I guess the general expectation,
*  it's very similar to the episode we did on the biological applications of this. And this sort
*  of overlaps with that, but it's definitely more fine grained. I guess the loop is like,
*  we're going to run a lot of experiments on the computer. We're going to identify things that
*  look good. Then we'll do actual experiments with those to try to verify that they're right. If
*  they're right, we'll have new discoveries. If they're wrong, we'll kind of feed that back
*  end and patch the models and try to get better on those failure modes. And it seems like in biology,
*  we're looking at potentially one to two orders of magnitude speed up in terms of how much overall
*  resources, human and financial maybe would need to go into discovering new things,
*  maybe even more than that. It seems like one is kind of a bare case and two is maybe like
*  the mainline case and above two orders of magnitude would be like obviously a super bowl case.
*  Is that your expectation? How do you expect the sort of trajectory of technology progress to change
*  based on these tools? Yeah, I mean, I'm really excited and really optimistic, frankly. And
*  you want to be careful because you don't want to overhype things. And other people will disagree.
*  Obviously, a lot of senior professors, in fact, are quite skeptical of a lot of these things. But
*  in my opinion, I think they're genuinely a transformably useful new tool, which will have
*  a profound impact on every discipline of fundamental science, I think. And so I'm really,
*  really excited about them. The central challenge, AI is clearly an incredibly powerful tool, but the
*  central challenge of it is the training data requirements. These are very data-hungry beasts.
*  You want to be thinking about where are the problems where you can generate large amounts
*  of data efficiently and increasingly diverse but very high quality amounts of data. And so I was
*  stuck with machine learning and AI for science for a long time because for electrolyte solutions,
*  you actually have not that much data. It's fairly limited amounts of data that you can use to train
*  these things. So I didn't really get into this until around Alpha Fold came out quite late.
*  But since then, it's become really clear that there are cases where you can, exactly as you're
*  saying, have these stages where you can iteratively generate larger and increasingly diverse data
*  sets. And one way to do this is with automated labs and or having experiments in the loop,
*  where you're constantly generating extra data. And there's an interesting article in the New
*  York Times about this Thoreau Pharmaceutical Company, where they have these huge automated
*  labs where they're generating all of this new data, which is really one way to go. And I think
*  that's really promising. And then the other way to go, I think, is to use quantum chemistry,
*  fundamental physics to generate this data on the fly as well. And I think that's a really nice
*  exciting avenue. And I honestly don't see what the limitation is. There's probably things that
*  are unforeseen that will cause these things to not be useful at some point, maybe. But at this stage,
*  I don't really see what the limits are in terms of as you scale these things up, get larger and
*  bigger models, why you won't be able to simulate a really large range of interesting systems,
*  and really get a lot of insight into many, many different systems that we've been waiting for a
*  long time to really understand. Because if you look at the way traditional experiment works,
*  drug discovery in particular, there's huge amounts of trial and error. So working with
*  experimentalists, there's a lot of just intuition and guesswork and trying different things, and
*  then getting some interesting results and then saying, well, we don't know what's actually
*  happening at the molecular scale, and then trying to work out some way to model it. And there's this
*  really just, you can just feel the progress being held back by a lack of ability to just really
*  understand what's happening, particularly at this molecular scale, which is so critical,
*  with so many important processes happening. So if you have this ability to simulate these
*  processes really fast and really accurately, I think that could be really transformatively useful.
*  And I'm incredibly excited about it, both for biology and for material science and chemical
*  engineering, and even things like climate change as well, where there's a lot of important molecular
*  scale processes go on. So I think it's a really exciting time to be involved in science.
*  You had a couple of interesting thoughts on the importance of or the opportunity of taking tools
*  from one domain and applying them to another. And I guess you can comment on that in any number of
*  ways, but I'm curious if you see like, untapped opportunity right now of tools you'd like to see
*  move from one place to another. We talked a little bit offline about the diffusion models,
*  roots in physical processes and how that's obviously now gone kind of horizontal and is
*  in use in a lot of different areas. But tell us more about the sort of borrowing tools from one
*  domain to another, as present and future. Yeah, so there's this brilliant book I was
*  reading recently called The Incomplete Guide to the Art of Discovery by Jake Oliver,
*  who is a scientist involved in discovering plate tectonics, which is this big paradigm shift in
*  geology. We realized that the Earth's not static, it's made of these tectonic plates, which were
*  all moving around. And he made this fantastic point that there's a really easy kind of hack to
*  do really exciting science, and that's to find tools from one field or discipline and take them
*  and apply them in your own. So this is what they did to discover plate tectonics, particularly
*  taking a ton of tools from physics and things and applying them to discover that these plates
*  were moving around. And I think when you start to look at science, you see this cropping up
*  everywhere, historically. So the classic example is physics itself, right? When Newton realized that
*  if you took tools from mathematics, calculus, and then apply them to physics, you get this
*  transformatively useful tool, right? You can suddenly explain gravity and huge amounts of
*  physics, which was incredibly exciting. And that's so kind of ingrained in physicists now, but we
*  don't really even think of that as being kind of interdisciplinary, but it really still is a type
*  of interdisciplinarity. And then there are many other examples of this, right? X-ray crystallography,
*  for instance, that you use to get crystal structures of proteins, you know, that came out of physics
*  and you're applying it to biology. So it's a very, very common feature of important science,
*  is taking these tools from one field and applying them to another. And yet diffusion models are
*  actually a fantastic example of this, where if you go back and look at the original papers that
*  motivated these diffusion models, they're actually explicitly citing non-equilibrium statistical
*  mechanics as inspiration for these models. And in some sense, using actually the mathematical
*  tools of it. So using thermal annealing and using a thing called Langevin dynamics, you know, which
*  is actually the equations or the algorithms that we use to do molecular simulations, invented by
*  physicists to simulate molecules moving around. And then, you know, people thought, oh, we could
*  take this and adapt this to generating new images. And then you've got these fantastic results, you
*  know, we can make these incredible images now using these algorithms. So that's another example
*  of this more recently. And then the coolest thing now, though, is that we're starting to go back in
*  the other direction and kind of complete the loop. And you had this fantastic guest on the other week
*  talking about, you know, all the ways these diffusion models and things have been used to
*  impact biology and problems that we would traditionally have been tackling with normal
*  molecular simulation. So you're starting to complete this loop where you're using the same
*  tools again now back in biology, which is very exciting and doing molecular simulation, which is
*  very, very cool. Although you want to be a bit careful because then it turns out that you may
*  end up just doing molecular simulation again without realizing it, which I think there's a
*  little bit of that going on there. You're running Langevin dynamics and you're using it, this thing
*  you call the score. But there's a great paper out of Microsoft recently where they showed that if
*  you train a diffusion model on molecular simulations, the score, which is the thing the
*  diffusion model is learning, is actually mathematically identical to the force field.
*  And so you've actually come back full circle and you're just doing molecular simulation again.
*  But now you've got a bunch of extra exciting nice tricks you can use to make it really more
*  efficient and make it more generalizable, which is exciting. So yeah, I think this is a really
*  profound example of this importance of interdisciplinary and thinking across different
*  fields and trying to take tools from one field and use them for another. And I think looking
*  forward, another example of this is this idea of taking tools and I think understandings from
*  statistical mechanics and actually applying them to understand the theory of large, you know,
*  of AI itself, of machine learning, of what's actually going on in stochastic gradient descent.
*  What are things learning? What does it mean for things to learn? And I think there's a ton of
*  tools from statistical mechanics, which could really be brought to bear on this. And we're
*  starting to see some examples of this. There's a paper just the other day showing that the
*  distribution your parameters go to when you're training a model go to a Boltzmann distribution,
*  right, which is a tool from statistical mechanics. It's also the distribution of molecules go to
*  this Boltzmann distribution. So we're starting to see really interesting parallels emerge.
*  And then another really lovely example of this was a Japanese group actually looking at the
*  mathematics of phase transformations. So we have beautiful theories which can explain phase
*  transformations, which is exactly like crystallization. And what they actually showed
*  is when you're training these neural networks, you start to see some of these same mathematical
*  features emerge in this training of these neural networks, which is a very nice idea. So then you
*  can start to think, oh, rocking, you know, this phenomena that seems so mysterious, actually,
*  it has a lot of parallels to something like a phase transformation physics, right. And when you
*  look at something like a learning curve, it actually looks a lot like an energy curve when
*  you're equilibrating a simulation starts high, it drops down to a low value, it will be jumping
*  around some plateau with some noise. And then you may get a phase transition where it suddenly
*  drops lower, right. And that's exactly what you see when you're trying to train your model,
*  you see these rocking phenomena emerge. So this is a really exciting direction, I think, as well,
*  using tools again, from different fields to try and understand things within your own field.
*  You see something like Sora. And the open AI folks behind that are less interested in the
*  video generation and more interested in the world simulation. And, you know, it's obviously like
*  macroscopic world simulation. What do you think is the outlook for one model to rule them all
*  across all these orders of magnitude versus when you see this coarse graining? Is that something
*  that sort of inherently suggests that we're going to have a hierarchy of models that handle these
*  different orders of magnitude of system? Or can that all be integrated into one thing if you just
*  dump everything into one data set, one training run, one network? Yeah, that's a fascinating
*  question, right? Yeah, that would be the dream if you just have one neural network to rule them all.
*  Yeah, I don't know that we'll get there. I mean, the way I think in the future, you know, thinking
*  long term how we'll do these molecular simulations is we'll use kind of a hierarchical coarse graining
*  approach. And perhaps you could incorporate this into one model. But where so you would have a
*  neural network that ignores the parts of the systems that aren't relevant, but then it will
*  have, you know, higher resolution pictures of the system that are relevant. So you think about
*  something like a drug binding to a protein, right? You at the local region where that that's a really
*  important process, right? You probably need an atomistic description of that. You need to know
*  where every atom is as a function of time and simulate that. But further away from that protein,
*  you could probably use a coarse grain description where you're not treating every water molecule,
*  and you're only kind of treating them in a kind of average way using this kind of coarse graining
*  technique. And so I think that's really exciting long term thinking about how you can build models
*  that kind of combine different scales, kind of multi scale modeling all within one neural network
*  that both study the kind of atomistic detail where it's important, but then where it's not important,
*  and you can kind of average it out, it can do that kind of on the fly. So that's really exciting.
*  You can start to think about potentially, yeah, building models that can do both scales at once
*  or look at multiple scales, because there's a huge range of phenomena where it's not just happening
*  at one scale, right? Where there's molecular scale processes that then determine larger
*  macroscopic things. And so you need to have this kind of multi scale approach. And that's a really
*  challenging problem that's going to take us some time to work out. But I think again, machine
*  learning and AI will be a critical tool to kind of try and help us do that efficiently.
*  Would it be like one, would the first step in your world toward that be training a single network on
*  the all atom versus, and also the coarse grain as opposed to like, separately? Have you tried that?
*  No, I haven't tried that. But it's a great idea. And then having it or allowing it to kind of
*  automatically jump between descriptions where it thinks it's best. Maybe I need it all in a
*  description here. So I'll go back to a higher resolution picture of it here would be very cool.
*  So that's something I think people should be thinking about more long term to try and do
*  something more ambitious here. Because this is the real key problem is that you want to use this
*  coarse grain picture so you can look at bigger systems. But then also these microscopic phenomena
*  are really important in many cases. So having some way that you can couple these things in
*  one neural network would be very cool. But yeah, that's a tricky technical problem. I'm not too
*  sure about how to go about. Cool. There's always more to do, at least for now until the AIs are
*  doing it. For a few years at least, there's always more to do. I mean, that's one other point I would
*  make is that I really encourage, there seems to be a real excitement and attention around making an
*  AGI or artificial super intelligence. But I just encourage people that there are so many important,
*  incredibly exciting problems you could tackle with machine learning. And I think this goal of
*  creating something that's smarter than any human is maybe something that comes along with all these
*  risks and uncertainties. And I know it's an appealing idea, but it's maybe not the kind of
*  thing that society actually wants us to do. So I encourage machine learning researchers to think,
*  is this actually a goal that we should be pursuing? Because we're throwing billions and
*  billions of dollars at it at the moment. But I think if you go and ask the average person,
*  do you want something that's smarter than a human in every single way? They'll probably say no. They'll
*  say, no, I want something that can do my dishes and do my chores, but not something that can make
*  art and music better than I can. And similarly for scientists, I don't want an AI bot that can
*  come along and do hypothesis generation and come up with new ideas and read the literature. But
*  those are the things I love doing and solving problems. That's what I like doing. So what I
*  would kind of prefer is people to build tools that I can use to do things like massively accelerate
*  simulations, for instance, take the kind of really hard problems that we're stuck on in science and
*  give us new powerful tools that we could then use to solve problems. So that's if there's one thing,
*  a message I could give to that community would be kind of just try and find tools to solve problems
*  for humans to do these things. Because building something that's smarter than any human is not
*  really something that I think any of us really want to do. And so the only geneticists could be
*  using CRISPR and genetic editing to make it humans that are smarter than anyone. But it's not something
*  that they're trying to do, because it's not something that society has decided that we want
*  to do. So I think we want to take a step back maybe and sometimes think about at a more fundamental
*  level, what are we trying to do? And why are we trying to do it? So Sam Altman talks about this
*  idea of, he wants to build an AGI that can discover the grand unified theory of physics, unifying
*  gravity and quantum mechanics and then explain it to him. But I think that's something that we should
*  save for a human, right? And we should build tools that help us do it. But I don't think we just want
*  to have an AI explain it to us, right? That feels to me like just looking in the back of the book
*  and just reading the answers, right? I mean, there's a source of meaning for so many people.
*  And I think it's maybe something that we should think about trying to preserve. And I understand
*  that an AGI would be incredibly practical useful. It allows us to help solve cancer and things.
*  But I think there's ways you could use AI to help solve these problems by developing really
*  powerful tools rather than just by developing something that tells us all the answers.
*  Yeah. Yeah. Amen to that. I'm very largely with you. I think there's an interesting distinction
*  there too between, is it the power or is it the generality that should concern us more? I tend to
*  fall more on the fear of generality side. And it's an odd feature of the current reality that like
*  the path to a lot of the best performance on even narrow tasks is like through pretty generalist
*  systems. But I do share your concern that first of all, that I'm like not sure society wants an AGI
*  or certainly a super intelligence. Obviously, I definitely do think the risks of that are not to
*  be dismissed. And it does feel to me like a kind of fundamentally ideological project. It's not
*  necessarily framed that way. But I do think that it probably should be understood that way.
*  But I think the only point of divergence I think from what I understood you saying just now is,
*  if I could have a narrow system that could do some of these frontier things,
*  but couldn't do anything else, sort of the AlphaGo of understanding physics,
*  I think I would be on board for that. Even if that meant that the human who counterfactually
*  would have made that discovery gets deprived of that Eureka moment, the joy of that Eureka moment,
*  I still think I would probably be inclined to make those trades. But the part for me where it
*  becomes very concerning is when that physics solver is also a general purpose intelligence that can do
*  anything better than a human. And then we have all these sort of control problems along the lines of
*  the research coming out of Anthropiq. They generalize in pretty nasty ways, it seems like,
*  too, where they just showed one where simple flattery or sycophancy toward the user starts
*  to generalize toward much more problematic forms of deception. And it's like, yikes.
*  I think the path through this superhuman intelligence to a good outcome is definitely fraught,
*  to say the least. If we could find a path to a narrow physics solver or material science discoverer
*  that was better than humans at only that narrow task, I think I would be on board with that. But
*  unfortunately, right now, that path is not super obvious.
*  Yeah, no, fair enough. I understand. If we could build one of these things, yeah,
*  it would probably inevitably get built. I just think, I don't know if we want to throw
*  that many resources at it. It's a question of where we direct our resources to.
*  You're building a narrow AI physics solver. If it's easier, then sure. Then building tools
*  for humans to use, then yeah, maybe that is the way to go. And yeah, the other massive,
*  obvious counter argument is obviously the only way to get something that's really useful is to build
*  this generality into it. So maybe there's no way to build things that are narrowly really good at
*  individual tasks. And the only way to really go is to build this kind of general intelligence,
*  which may be just an unfortunate fact of the way reality works. But yeah, it will be interesting
*  to see how it plays out. It's going to be a fascinating time. Yeah, no doubt about that.
*  All right. I'll say it again. Thank you for getting up early in the morning. And thank you,
*  Tim Dugman, for being part of the cognitive revolution. No problem. Thanks for having me.
*  It's a pleasure. It is both energizing and enlightening to hear why people listen and
*  learn what they value about the show. So please don't hesitate to reach out via email at tcr
*  at turpentine.co or you can DM me on the social media platform of your choice.

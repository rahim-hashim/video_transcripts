---
Date Generated: April 12, 2024
Transcription Model: whisper medium 20231117
Length: 13123s
Video Keywords: ['agi', 'ai', 'ai podcast', 'artificial intelligence', 'artificial intelligence podcast', 'black holes', 'cellular automata', 'computational irreducibility', 'computer science', 'intelligence', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'math', 'mathematics', 'mit ai', 'quantum mechanics', 'ruliology', 'stephen wolfram', 'theoretical physics', 'wolfram alpha', 'wolfram mathematica', 'wolfram physics project']
Video Views: 3050089
Video Rating: None
---

# Stephen Wolfram: Complexity and the Fabric of Reality | Lex Fridman Podcast #234
**Lex Fridman:** [October 26, 2021](https://www.youtube.com/watch?v=4-SGpEInX_c)
*  The following is a conversation with Stephen Wolfram, his third time on the podcast. He's a
*  computer scientist, mathematician, theoretical physicist, and the founder of Wolfram Research,
*  a company behind Mathematica, Wolfram Alpha, Wolfram Language, and the new Wolfram Physics Project.
*  This conversation is a wild technical roller coaster ride through topics of complexity,
*  mathematics, physics, computing, and consciousness. I think this is what this podcast is becoming,
*  a wild ride. Some episodes are about physics, some about robots, some are about war and power,
*  some are about the human condition and our search for meaning, and some are just what the comedian
*  Tim Dillon calls fun. This is the Lex Friedman Podcast. To support it, please check out the
*  sponsors in the description. And now here's my conversation with Stephen Wolfram.
*  Almost 20 years ago, you published a new kind of science where you presented a study of complexity
*  and an approach for modeling of complex systems. So let us return again to the core idea of
*  complexity. What is complexity? I don't know. I think that's not the most interesting question.
*  It's like, if you ask a biologist, what is life? That's not the question they care the most about.
*  What I was interested in is, how does something that we would usually identify as complexity
*  arise in nature? And I got interested in that question like 50 years ago, which is really
*  embarrassingly long time ago. And how does snowflakes get to have complicated forms? How
*  do galaxies get to have complicated shapes? How do living systems get produced? Things like that.
*  And the question is, what's the sort of underlying scientific basis for those kinds of things?
*  And the thing that I was at first very surprised by, because I'd been doing physics, some particle
*  physics, some fancy mathematical physics, and so on. And it's like, I know all this fancy stuff.
*  I should be able to solve this sort of basic science question. And I couldn't. This was like
*  early, maybe 1980-ish timeframe. And it's like, okay, what can one do to understand the sort of
*  basic secret that nature seems to have? Because it seems like nature, you look around in the natural
*  world, it's full of incredibly complicated forms. You look at sort of most engineered kinds of things.
*  For instance, they tend to be, you know, we've got sort of circles and lines and things like this.
*  The question is, what secret does nature have that lets it make all this complexity that we
*  in doing engineering, for example, don't naturally seem to have? And so that was the kind of the thing
*  that I got interested in. And then the question was, you know, could I understand that with things
*  like mathematical physics? Well, it didn't work very well. So then I got to thinking about, okay,
*  is there some other way to try to understand this? And then the question was, if you're going to look
*  at some system in nature, how do you make a model for that system, for what that system does?
*  So, you know, a model is some abstract representation of the system, some formal
*  representation of the system. What is the raw material that you can make that model out of?
*  And so what I realized was, well, actually, programs are really good source of raw material
*  for making models of things. And, you know, in terms of my personal history, to me, that seemed
*  really obvious. And the reason it seemed really obvious is because I just spent several years
*  building this big piece of software that was sort of a predecessor to Mathematica and Morphin
*  language, then called SMP, Symbolic Manipulation Program, which was something that had this idea
*  of starting from just these computational primitives and building up everything one had to
*  build up. And so kind of the notion of, well, let's just try and make models by starting from
*  computational primitives and seeing what we can build up. That seemed like a totally obvious thing
*  to do. In retrospect, it might not have been externally quite so obvious, but it was obvious
*  to me at the time, given the path that I happened to have been on. So that got me into this question
*  of, let's use programs to model what happens in nature. And the question then is, well, what kind
*  of programs? And we're used to programs that you write for some particular purpose, and it's a big
*  long piece of code, and it does some specific thing. But what I got interested in was, okay,
*  if you just go out into the sort of computational universe of possible programs, you say,
*  take the simplest program you can imagine, what does it do? And so I started studying these things
*  called cellular automata. Actually, I didn't know at first they were called cellular automata, but I
*  found that out subsequently. But it's just a line of cells, you know, each one is black or white.
*  And it's just some rule that says the color of the cell is determined by the color that had on
*  previous step and its two neighbors on the previous step. And I had initially thought
*  that's, you know, sufficiently simple setup is not going to do anything interesting. It's always
*  going to be simple, no complexity, simple rules, simple behavior. Okay, but then I actually ran
*  the computer experiment, which is pretty easy to do. I mean, it probably took a few hours
*  originally. And the results were not what I'd expected at all. Now, needless to say, in the
*  way that science actually works, the results that I got a lot of unexpected things, which I thought
*  were really interesting, but the really strongest results, which was already right there in the
*  printouts I made, I didn't really understand for a couple more years. So it was it was not,
*  you know, the compressed version of the story is you run the experiment and you immediately see
*  what's going on. But I wasn't smart enough to do that, so to speak. But the big the big thing is,
*  even with very simple rules of that type, sort of the minimal tiniest program, sort of the, the
*  one line program or something, it's possible to get very complicated behavior. My favorite example
*  is the thing called rule 30, which is a particular cellular automaton rule. You just started off in
*  one black cell, and it makes this really complicated pattern. And so that, for me, was sort of a
*  critical discovery that then kind of said, playing back on to, you know, how does nature make
*  complexity? I sort of realized that might be how it does it. That might be kind of the secret that
*  it's using is that in this kind of computational universe of possible programs, it's actually
*  pretty easy to get programs where even though the program is simple, the behavior when you run the
*  program is not simple at all. And that was so for me, that was the, the kind of the, the story of
*  kind of how that was sort of the, the indication that one had got an idea of what the sort of
*  secret that nature uses to make complexity and the complexity, how complexity can be made in
*  other places. Now, if you say, what is complexity? You know, it's, it's complexity is, it's not easy
*  to tell what's going on. That's the informal version of what is complexity. But there is
*  something going on, but it's not easy to know what, right? Well, no, the rules can generate
*  just randomness, right? Well, that's not obvious. In other words, that's not obvious at all. And it
*  wasn't what I expected. It's not what people's intuition had been and has been for, you know,
*  for a long time. That is one might think you have a rule, you can tell there's a rule behind it. I
*  mean, it's just like, you know, the early, you know, robots in science fiction movies, right? You
*  can tell it's a robot cause it does simple things, right? Turns out that isn't actually the right
*  story, but it's not obvious that isn't the right story. Cause people assume simple rules, simple
*  behavior. And that the sort of the key discovery about the computational universe is that isn't
*  true. And that discovery goes very deep and relates to all kinds of things that I've spent
*  years and years studying. But, you know, that, that in the end, the sort of the, the, what is
*  complexity is, well, you can't easily tell what it's going to do. You could just run the rule
*  and see what happens, but you can't just say, Oh, you know, show me the rule. Great. I now I know
*  what's going to happen. And, you know, the key phenomenon around that is this thing I call
*  computational irreducibility. This fact that in something like rule 30, you might say, well,
*  what's it going to do after a million steps? Well, you can run it for a million steps and just do
*  what it does to find out, but you can't compress that. You can't reduce that and say, I'm going to
*  be able to jump ahead and say, this is what it's going to do after a million steps, but I don't
*  have to go through anything like that computational effort. By the way, has anybody succeeded at that?
*  Do you had a challenge, a competition for predicting the middle column of rule 30?
*  And indeed, anybody, a number of people have sent things in and sort of people are picking away at
*  it, but it's hard. I mean, it's, it's, uh, I've been, I've been actually, uh, even proving that
*  the center column of rule 30 doesn't repeat. That's something I think might be doable. Okay.
*  Mathematically proving.
*  Yes. And so that's analogous to a similar kind of things like the digits of pi,
*  which are also generated in this very deterministic way. And so a question is how random
*  are the digits of pi? For example, does every foot, first of all, do the digits of pi ever repeat?
*  Well, we know they don't because it was proved in the 1800s that pi is not a rational number.
*  So that means only rational numbers have digit sequences that repeat. So we know the digits of
*  pi don't repeat. So now the question is, does, you know, zero, one, two, three, or whatever,
*  do all the digits based 10 or base two, or however you work it out, do they all occur with equal
*  frequency? Nobody knows that's far away from what can be understood mathematically at this point.
*  And, um, that's, that's kind of, uh, but I'm, I'm even looking for step one, which is prove that the,
*  the, the, the center column doesn't repeat and then prove other things about it, like equidistribution
*  of, of, uh, equal numbers of zeros and ones. And those are things which I, you know, I kind of set
*  up this little, little prize thing because I thought those were not not too out of range.
*  Those are things which are within, you know, a modest amount of time. It's conceivable that
*  those could be done. They're not, they're not far away from what current mathematics might allow.
*  They'll require a bunch of cleverness and hopefully some interesting new ideas that,
*  you know, will be useful other places. But you started in 1980 with this idea before,
*  I think you realized, you know, this idea of programs, you thought that there might be some
*  kind of a thermodynamic, like randomness and then complexity comes from a clever filter
*  that, uh, you kind of like, I don't know, spaghetti or something. You, you, you filter the randomness
*  and outcomes complexity, which is an interesting intuition. I mean, how do we know that's not
*  actually what's happening? So just because you were then able to develop, look, you don't need
*  this like incredible randomness. You can just have very simple, predictable initial conditions
*  and predictable rules. And then from that emerged complexity. Still there might be some systems where
*  it's a filtering randomness. Yes. The inputs. Well, the point is when you have quotes,
*  randomness than the input, that means there's all kinds of information in the input. Yeah.
*  And in a sense, what you get out will be maybe just something close to what you put in. Like
*  people are very in dynamical systems theory, sort of big area of mathematics that developed
*  from the early 1900s and, and really got big in the 1980s. You know, an example of what people
*  study there a lot and it's popular version is chaos theory. Um, and an example of what people
*  study a lot is the shift map, which is basically taking two X mod one to the fractional part of
*  two X, which is basically just taking digits in binary and shifting them to the left. So at every
*  step you get to see, if you say, how big is this number that I got out? Well, the most important
*  digit in that number is whatever ended up at the, at the left-hand end. But now if you start off
*  from an arbitrary random number, which is quotes randomly chosen, so all its digits are random,
*  then when you run that sort of chaos theory shift map, all that you get out is just whatever you put
*  in. You just get to see what you, what, uh, it's not obvious that you would excavate all of those
*  digits. And if you're, for example, making a theory, I don't know, fluid mechanics, for example,
*  if there was that phenomenon and fluid mechanics, then the equations of fluid mechanics can't be
*  right because what that would be saying is the equations of that, that it matters to the fluid,
*  what happens in the fluid at the level of the millionth digit of the initial conditions,
*  which is far below the point at which you're hitting kind of sizes of molecules and things
*  like that. So it's kind of almost explaining if that phenomenon is an important thing,
*  it's kind of telling you that the fluid dynamics, which describes fluids as continuous media and so
*  on, isn't, isn't really right. But so, you know, so this idea that, you know, there's a, there's,
*  it's a, it's a tricky thing because as soon as you put randomness in, you have to know, you know,
*  what, how much of what's coming out is what you put in versus how much is actually something
*  that's being generated. And what's really nice about these systems where you just have very
*  simple initial conditions and where you get random stuff out or seemingly random stuff out
*  is you don't have that issue. You don't have to argue about was there something complicated put in
*  because it's plainly obvious there wasn't. Now as a practical matter in doing experiments,
*  the big thing is if the thing you see is complex and reproducible, then it didn't come from just
*  filtering some quotes randomness from the outside world. It has to be something that is intrinsically
*  made because it wouldn't otherwise be, I mean, you know, the, the, the, it could be the case that
*  you set things up and it's always the same each time. And you say, well, it's kind of the same,
*  but it's not then it's not random each time because it's kind of the definition of it being random
*  is it was kind of picked, picked at random each time, so to speak.
*  So is it possible to for sure know that our universe does not at the fundamental level have
*  randomness? Is it possible to conclusively say there's no randomness at the bottom?
*  Well, it's an interesting question. I mean, you know, science, natural science is an inductive
*  business, right? You observe a bunch of things and you say, can we fit these together? What is our
*  hypothesis for what's going on? The thing that I think I can say fairly definitively is at this
*  point, we understand enough about fundamental physics that there is, if there was sort of an
*  extra dice being thrown, it's something that doesn't need to be there. We can get what we see
*  without that. Now, you know, could you add that in as an extra little featureoid, you know,
*  without breaking the universe? Probably. But in fact, almost certainly, yes. But is it necessary
*  for understanding the universe? No. And I think actually from a more fundamental point of view,
*  it's, it's, I think I might be able to argue. So one of the things that I've been interested in,
*  I've been pretty surprised that I've had anything sent in to say about is the question of why does
*  the universe exist? I didn't think that was a question that I would, you know, I thought that
*  was a far out there metaphysical kind of thing. Even the philosophers have stayed away from that
*  question for the most part. It's so such a kind of, you know, difficult to address question. But
*  I actually think, to my great surprise that from our physics project and so on, that it is possible
*  to actually address that question and explain why the universe exists. And I kind of have a
*  suspicion. I've not thought it through. I kind of have a suspicion that that explanation will
*  eventually show you that in no meaningful sense, can there be randomness underneath the universe?
*  That is that if there is, it's something that is necessarily irrelevant to our perception of the
*  universe. That is that it could be there, but doesn't matter. Because in a sense, we've already,
*  you know, whatever it would do, whatever extra thing it would add is not relevant to our
*  perception of what's going on. So why does the universe exist? How does the irrelevance of
*  randomness connect to the big why question of the universe? So, okay, so I mean, why does the
*  universe exist? Well, let's see. And is this the only universe we got? It's the only one.
*  About that, I'm pretty sure. So now maybe which one, which of these topics is better to enter
*  first? Why does the universe exist? And why you think it's the only one that exists? Well,
*  I think they're very closely related. Okay. Okay. So I mean, the first thing, let's see,
*  I mean, this why does the universe exist question is built on top of all these things that we've
*  been figuring out about fundamental physics. Because if you want to know why the universe
*  exists, you kind of have to know what the universe is made of. And I think the Well, let me let me
*  describe a little bit about the why does the universe exist question. So the main issue is,
*  let's say you have a model for the universe. And you say, I've got this, this program or something,
*  and you run it and you make the universe. Now you say, Well, how do you act? Why is that program
*  actually running? And people say, you've got this program that makes the universe, what computer is
*  it running on? Right? What does it mean? What actualizes something, you know, two plus two
*  equals four, but that's different from saying there's two, a pile of two rocks, another pile
*  of two rocks, and somebody moves them together and makes four, so to speak. And so what is it
*  that kind of turns it from being just this formal thing to being something that is actualized?
*  Okay, so there we have to start thinking about, well, well, what do we actually know about what's
*  going on in the universe? Well, we are observers of this universe. But confusingly enough, we're
*  part of this universe. So in a sense, we what what what if we say, what do we what do we know about
*  what's going on in the universe? Well, what we know is what sort of our consciousness records about
*  what's going on in the universe. And consciousness is part of the fabric of the universe. So we're in
*  it. Yes, we're in it. And maybe I should maybe I should start off by saying something about
*  the consciousness story, because that's some. Maybe we should begin even before that at the very base
*  layer of the Wolfram physics project. Maybe you can give a broad overview once again,
*  really quick about this hypergraph model. Yes. And also, what is it a year and a half ago,
*  since you've brought this project to the world? What is the status update? Where What are all
*  the beautiful ideas you have come across? What are the interesting things you mentioned? It's,
*  I mean, it's a it's a frigging Cambrian explosion. It's, it's crazy. I mean, there are all these
*  things which I've kind of wondered about for years. And suddenly, there's actually a way to
*  think about them. And I really did not see. I mean, the real strength of what's happened,
*  I absolutely did not see coming. And the real strength of it is, we've got this model for
*  physics, but it turns out it's a foundational kind of model. That's a different kind of
*  computation like model that I'm kind of calling the sort of multi computational model. And that
*  kind of model is applicable not only to physics, but also to lots of other kinds of things.
*  And one reason that's extremely powerful is because physics has been very successful.
*  So we know a lot based on what we figured out in physics. And if we know that the same model
*  governs physics, and governs, I don't know, economics, linguistics, immunology, whatever,
*  we know that the same kind of model governs those things, we can start using things that we've
*  successfully discovered in physics, and applying those intuitions in all these other areas. And
*  that's, that's pretty exciting. And I'm very surprising to me. And in fact, it's kind of like,
*  in the original story of sort of you go and you explain why is there complexity in the natural
*  world, then you realize, well, there's all this complexity, there's all this computational
*  irreducibility, you know, there's a lot we can't know about what's going to happen. It's kind of,
*  it's kind of very confusing thing for people who say, you know, science has nailed everything down,
*  we're going to, you know, based on science, we can know everything. Well, actually, there's
*  this computational irreducibility thing, right in the middle of that, thrown up by science,
*  so to speak. And then the question is, well, given computational irreducibility, how can we
*  actually figure out anything about what happens in the world? Why aren't we, why are we able to
*  predict anything? Why are we able to sort of operate in the world? And the answer is that we
*  sort of live in these slices of computational reusability that exists in this kind of ocean of
*  computational irreducibility. And it turns out that seems that it's a very fundamental feature
*  of the kind of model that seems to operate in physics, and perhaps in a lot of these other areas,
*  that there are these particular slices of computational reusability that are relevant to
*  us. And those are the things that both allow us to operate in the world, and not just have everything
*  be completely unpredictable. But there are also things that potentially give us what amount to
*  physics-like laws in all these other areas. So that's been sort of an exciting thing. But
*  I would say that in general, for our project, it's been going spectacularly well. Honestly,
*  it wasn't something I expected to happen in my lifetime. It's something where, and in fact,
*  one of the things about it, some of the things that we've discovered are things where I was
*  pretty sure that wasn't how things worked. And turns out I'm wrong. And in a major area in
*  mathematics, I've been realizing that something I've long believed, we can talk about it later,
*  that just really isn't right. So what's happened with the physics project? It can explain a little
*  bit about how the model works, but basically- Well, I can maybe ask you the following question.
*  So it's easy, through words, to describe how cellular automata works. You've explained this.
*  And it's the fundamental mechanism by which you, in your book, and your kind of science,
*  explored the idea of complexity and how to do science in this world of reducible islands and
*  irreducible, generally irreducibility. Okay. So how does the model of hypergraphs differ from
*  cellular automata? And how does the idea of multi-computation differ? Maybe that's a way
*  to describe it. Right. Yeah, right. This is a, my life is, like all of our lives, something of a
*  story of computational irreducibility. And it's been going for a few years now, so it's always a
*  challenge to kind of find these appropriate pockets of reducibility. But let me see what I can do.
*  So, I mean, first of all, let's talk about physics, first of all. And a key observation,
*  the starting point of our physics project is things about what is space? What is the universe
*  made of? And ever since Euclid, people just sort of say, space is just this thing where you can
*  put things at any position you want. And they're just points and they're just geometrical things
*  that you can just arbitrarily put at different coordinate positions. So the first thing in our
*  physics project is the idea that space is made of something. Just like water is made of molecules,
*  space is made of kind of atoms of space. And the only thing we can say about these atoms of space
*  is they have some identity. There's a, there is, it's this atom as opposed to this atom.
*  And you could give them, if you were a computer person, you'd give them UUIDs or something.
*  But that's all there is to say about them, so to speak. And then all we know about these atoms
*  of space is how they relate to each other. So we say these three atoms of space are associated with
*  each other in some relation. So you can think about that as, you know, what atom of space is
*  friends with what other atom of space? You can build this essentially friend network of the atoms
*  of space. And the sort of starting point of our physics project is that's what our universe is.
*  It's a giant friend network of the atoms of space. And so how can that possibly represent our
*  universe? Well, it's like in something like water, you know, there are molecules bouncing around,
*  but on a large scale that, you know, that produces fluid flow and we have fluid vortices and we have
*  all of these phenomena that are sort of the emergent phenomena from that underlying kind
*  of collection of molecules bouncing around. And by the way, it's important that that collection
*  of molecules bouncing around have this phenomenon of computational irreducibility. That's actually
*  what leads to the second law of thermodynamics among other things. And that leads to the sort
*  of randomness of the underlying behavior, which is what gives you something which on a large scale
*  seems like it's a smooth continuous type of thing. And so, okay, so first thing is space is made of
*  something. It's made of all these atoms of space connected together in this network. And then
*  everything that we experience is sort of features of that structure of space. So, you know, when we
*  have an electron or something or a photon, it's some kind of tangle in the structure of space,
*  much like kind of a vortex and a fluid would be just this thing that is, you know, it can actually,
*  the vortex can move around, it can involve different molecules in the fluid, but the vortex still
*  stays there. And if you zoom out enough, the vortex looks like an atom itself, like a basic
*  atom. So there's the levels of abstraction. If you squint and kind of blur things out, it looks like
*  at every level of abstraction, you can define what is a basic individual entity. Yes, but, you know,
*  in this model, there's a bottom level. You know, there's an elementary length, maybe 10 to the minus
*  100 meters, let's say, which is really small, you know, proton is 10 to the minus 15 meters,
*  the smallest we've ever been able to sort of see with a particle accelerator is around 10 to the
*  minus 21 meters. So, you know, if we don't know precisely what the correct scale is, but it's
*  perhaps over the order of 10 to the minus 100 meters. So it's pretty small. And but that's
*  the end. That's what things are made of. What's your intuition where the 10 to the minus 100
*  comes from? What's your intuition about this scale? Well, okay, so there's a calculation,
*  which I consider to be somewhat rickety, okay, which has to do with comparing. So,
*  so there are various fundamental constants, there's the speed of light, the speed of light,
*  once you know the elementary time, the speed of light is tells you the conversion from the
*  elementary time to the elementary length. Then there's the question of how do you convert to
*  the elementary energy? And how do you convert to between other things? And the various constants
*  we know we know the speed of light, we know the gravitational constant, we know Planck's constant
*  and quantum mechanics, those are the three important ones. And we actually know some other
*  things we know things like the size of the universe, the Hubble constant, things like that.
*  And essentially, this calculation of the elementary length comes from looking at these sort of
*  combination of those. Okay, so the most obvious thing people have sort of assumed that quantum
*  gravity happens at this thing, the Planck scale 10 to the minus 34 meters, which is the sort of
*  the combination of Planck's constant and the gravitational constant, the speed of light,
*  that gives you that kind of length. Turns out in our model, there is an additional parameter,
*  which is essentially the number of simultaneous threads of execution of the universe,
*  which is essentially the number of sort of independent quantum processes that are going on.
*  And that number, let's see if I remember that number, that number is 10 to the 170, I think.
*  And so it's a big number. But that number then connects, you know, sort of modifies what you
*  might think from all these Planck units to give you the things we're giving. And there's been sort
*  of a mystery, actually, in the more technical physics thing, that the Planck mass, the Planck
*  energy, Planck energy is actually surprisingly big. The Planck length is tiny, 10 to the minus
*  34 meters, the Planck time 10 to the minus 43 meters, I think, 30 seconds, I think. But the
*  Planck energy is like the energy of a lightning strike, okay, which is pretty weird. In our models,
*  the actual elementary energy is that divided by the number of sort of simultaneous quantum threads,
*  and it ends up being really small, too. And that sort of explains that mystery that's been around
*  for a while about how Planck units work. But whether that precise estimate is right,
*  we don't know yet. I mean, that's one of the things that's sort of been a thing we've been
*  pretty interested in, is how do you see through, you know, how do you make a gravitational microscope
*  that can kind of see through to the atoms of space? You know, how do you get in fluid flow,
*  for example, if you go to hypersonic flow or something, you know, you've got a Mark 20,
*  you know, space plane or something, it really matters that there are individual molecules
*  hitting the space plane, not a continuous fluid. The question is, what is the analogous kind of,
*  what is the analog of hypersonic flow for things about the structure of space time?
*  And it looks like a rapidly rotating black hole, right, at the sort of critical rotation rate,
*  is it looks as if that's a case where essentially the structure of space time is just about to fall
*  apart. And you may be able to kind of see the evidence of sort of discrete elements, you know,
*  you may be able to kind of see there, the sort of gravitational microscope of actually seeing
*  these discrete elements of space. And there may be some effect in, for example, gravitational waves
*  produced by rapidly rotating black hole, that in which one could actually see some phenomenon
*  where one could say, yes, they don't come out the way one would expect based on having a continuous
*  structure of space time. That is something where you can kind of see through to the discrete
*  structure. We don't know that yet. So you can maybe elaborate a little bit deeper how a microscope
*  that can see to 10 to the minus 100, how rotating black holes, and presumably the
*  detailed accurate detection of gravitational waves from such black holes can reveal the
*  discreteness of space. Okay, first thing is what is a black hole? Actually, we need to go a little
*  bit further in the story of what space time is, because I explained a little bit about what space
*  is, but I didn't talk about what time is. And that's sort of important in understanding space
*  time, so to speak. And your sense is both space and time in the story are discrete.
*  Absolutely. Absolutely. But it's a complicated story. And needless to say.
*  Well, it's simple at the bottom. It's very simple at the bottom. In the end,
*  it's simple, but deeply abstract. And something that is simple in conception, but kind of wrapping
*  one's head around what's going on is pretty hard. So first of all, we have this, so I've described
*  these kind of atoms of space and their connections. You can think about these things as a hypergraph.
*  A graph is just you connect nodes to nodes, but a hypergraph you can have sort of not just friends,
*  individual friends to friends, but you can have these triplets of friends or whatever else.
*  And so we're just saying, and that's just the relations between atoms of space are the
*  hyper edges of the hypergraph. And so we got some big collection of these atoms of space,
*  maybe 10 to the 400 or something in our universe. And that's the structure of space. That's an every
*  feature of what we experience in the world is a feature of that hypergraph, that spatial hypergraph.
*  So then the question is, well, what does that spatial hypergraph do? Well, the idea is that
*  there are rules that update that spatial hypergraph. And in a cellular automaton,
*  you've just got this line of cells and you just say at every step, at every time step,
*  you've got fixed time steps, fixed array of cells. At every step, every cell gets updated
*  according to a certain rule. And that's the way it works. Now in this hypergraph,
*  it's sort of vaguely the same kind of thing. We say every time you see a little piece of
*  hypergraph that looks like this, update it to one that looks like this. So it's just keep rewriting
*  this hypergraph. Every time you see something that looks like that anywhere in the universe,
*  it gets rewritten. Now, one thing that's tricky about that, which we'll come to is this
*  multi-computational idea, which has to do with, you're not saying in some kind of lockstep way,
*  do this one, then this one, then this one. It's just whenever you see one you can do,
*  you can go ahead and do it. And that leads one not to have a single thread of time in the universe.
*  Because if you knew which one to do, you would just say, okay, we do this one, then we do this
*  one, then we do this one. But if you say, just do whichever one you feel like, you end up with these
*  multiple threads of time, these kind of multiple histories of the universe, depending on which
*  order you happen to do the things you could do in. So it's fundamentally asynchronous and parallel.
*  Yes. Which is very uncomfortable for the human brain that seeks for things to be sequential
*  and synchronous. Right. Well, I think that this is part of the story of consciousness,
*  is I think the key aspect of consciousness that is important for sort of parsing the universe
*  is this point that we have a single thread of experience. We have a memory of what happened
*  in the past, we can predict something about the future, but there's a single thread of experience.
*  It's not obvious it should work that way. I mean, we've got 100 billion neurons in our brains,
*  and they're all firing at all guns in different ways. But yet, our experience is that there is
*  the single thread of time that goes along. And I think that one of the things I've kind of realized
*  with a lot more clarity in the last year is the fact that we conclude that the universe has the
*  laws it has as a consequence of the fact that we have consciousness the way we have consciousness.
*  And so the fact, so I mean, just to go on with kind of the basic setup,
*  so we've got this spatial hypergraph, it's got all these atoms of space, they're getting these
*  little clumps of atoms of space are getting turned into other clumps of atoms of space,
*  and that's happening everywhere in the universe all the time. And so one thing that's a little
*  bit weird is there's nothing permanent in the universe. The universe is getting rewritten
*  everywhere all the time. And if it wasn't getting rewritten, space wouldn't be knitted together.
*  That is, space would just fall apart. There wouldn't be any way in which we could say this
*  part of space is next to this part of space. One of the things that people were confused about back
*  in antiquity, the ancient Greek philosophers and so on, is how does motion work? How can it be the
*  case that you can take a thing that we can walk around and it's still us when we walked a foot
*  forward, so to speak? And in a sense with our models, that's again a question, because it's a
*  different set of atoms of space. When I move my hand, it's moving into a different set of atoms
*  of space. It's having to be recreated. The thing itself is not there. It's being continuously
*  recreated all the time. Now it's a little bit like waves in an ocean, vortices in a fluid,
*  which again, the actual molecules that exist in those are not what define the identity of the thing.
*  But it's a little bit, this idea that there can be pure motion, that it is even possible
*  for an object to just move around in the universe and not change. It's not self-evident that such a
*  thing should be possible. And that is part of our perception of the universe, is that we
*  parse those aspects of the universe where things like pure motion are possible. Now, pure motion,
*  even in general relativity, the theory of gravity, pure motion is a little bit of a complicated
*  thing. If you imagine your average teacup or something approaching a black hole, it is
*  deformed and distorted by the structure of spacetime. And to say, is it really pure motion? Is it that
*  same teacup that's the same shape? Well, it's a bit of a complicated story. And this is a more
*  extreme version of that. So anyway, the thing that's happening is we've got space, we've got
*  this notion of time. So time is this rewriting of the hypergraph. And one of the things that's
*  important about that, time is this sort of computationally irreducible process. There's
*  something, time is not something where, in kind of the mathematical view of time, tends to be,
*  time is just a coordinate. We can slide a slider, turn a knob, and we'll change the time that we've
*  got in this equation. But in this picture of time, that's not how it works at all. Time is this
*  inexorable, irreducible kind of set of computations that go on, that go from where we are now
*  to the future. And one of the things that is, again, something one sort of has to break out of,
*  is your average trained physicist like me says space and time are the same kind of thing. They're
*  related by the Poincare group and Lorentz transformations and relativity and all these
*  kinds of things. And space and time, there are all these kind of sort of folk stories you
*  can tell about why space and time are the same kind of thing. In this model, they're fundamentally
*  not the same kind of thing. Space is this kind of sort of connections between these atoms of space,
*  time is this computational process. So the thing that the first sort of surprising thing is, well,
*  it turns out you get relativity anyway. And the reason that happens, there are a few bits and
*  pieces here which one has to understand, but the fundamental point is, if you are an observer
*  embedded in the system, that a part of this whole story of things getting updated in this way and
*  that, there's sort of a limit to what you can tell about what's going on. And really in the end,
*  the only thing you can tell is what are the causal relationships between events. So an event in this
*  sort of an elementary event is a little piece of hypergraph got rewritten. And that means
*  a few hyper edges of the hypergraph were consumed by the event, and you produce some other hyper
*  edges, and that's an elementary event. And so then the question is, what we can tell is kind of
*  what the network of causal relationships between elementary events is. That's the ultimate thing,
*  the causal graph of the universe. And it turns out that, well, there's this property of causal
*  invariance that is true of a bunch of these models and I think is inevitably true for a variety of
*  reasons. That makes it be the case that it doesn't matter kind of if you are sort of saying,
*  well, I've got this hypergraph and I can rewrite this piece here and this piece here, and I do them
*  all in different orders. When you construct the causal graph for each of those orders that you
*  choose to do things in, you'll end up with the same causal graph. And so that's essentially why,
*  well, that's in the end why relativity works. It's why our perception of space and time is
*  as having this kind of connection that relativity says they should have.
*  And that's kind of how that works. I think I'm missing a little piece,
*  if we can go there again. You said the fact that the observer is embedded in this hypergraph,
*  what's missing? What is the observer not able to state about this universe of space and time?
*  If you look from the outside, you can say, oh, I see this particular place was updated and then
*  this one was updated and I'm seeing which order things were updated in. But the observer embedded
*  in the universe doesn't know which order things were updated in because until they've been updated,
*  they have no idea what else happened. So the only thing they know is the set of causal relationships.
*  Let me give an extreme example. Let's imagine that the universe is a Turing machine. Turing
*  machines have just this one update head which does something and otherwise the Turing machine
*  just does nothing. And the Turing machine works by having this head move around and do its updating
*  just where the head happens to be. The question is, could the universe be a Turing machine?
*  Could the universe just have a single updating head that's just zipping around all over the place?
*  You say that's crazy because I'm talking to you, you seem to be updating, I'm updating, etc. But
*  the thing is, there's no way to know that because if there was just this head moving around, it's
*  like, okay, it updates me, but you're completely frozen at that point. Until the head has come
*  over and updated you, you have no idea what happened to me. And so if you sort of unravel
*  that argument, you realize the only thing we actually can tell is what the network of causal
*  relationships between the things that happened were. We don't get to know from some sort of
*  outside sort of God's eye view of the thing. We don't get to know what sort of from the outside
*  what happened. We only get to know sort of what the set of relationships between the things that
*  happened actually were. Yeah, but if I somehow record like a trace of this, I guess would be
*  called multi computation. Can't I then look back? In the
*  way you record the trace, some you place throughout the universe, like throughout,
*  like a log that records my own pocket of in this hypergraph, can't I like,
*  realizing that I'm getting an outdated picture? Can't I record?
*  See, the problem is, and this is where things start getting very entangled in terms of what
*  one understands. The problem is that any such recording device is itself part of the universe.
*  So you don't get to say you never get to say let's go outside the universe and go do this.
*  And that's why I mean, lots of the features of this of this model and the way things work
*  end up being a result of that. So but what I guess from on a human level,
*  what is the cost you're paying? What are you missing from not getting an updated picture
*  all the time? Okay, I got I understand what you're saying. Yeah, right.
*  But like what, like how does consciousness emerge from that? Like, how, like, what are the
*  limitations of that observer? I understand you're getting a delayed picture.
*  Well, there's a okay, there's a bunch of limitations of the observer, I think.
*  Maybe it just explains something about quantum mechanics, because that maybe is an extreme
*  version of some of these issues, which helps to kind of motivate why one should sort of think
*  things through a little bit more carefully. So one feature of the of this, okay, so in standard
*  physics, like high school physics, you learn, you know, the equations of motion for a ball.
*  And the you know, it says, you throw the ball this angle, this velocity,
*  things will move in this way. And there's a definite answer. Right? The story, the key
*  story of quantum mechanics is there aren't definite answers to where does the ball go.
*  There's kind of this whole sort of bundle of possible paths. And all we say we know from
*  quantum mechanics is certain probabilities for where the ball will end up. Okay, so that's kind
*  of the core idea of quantum mechanics. So in our models, you quantum mechanics is not some kind of
*  plugin add on type thing, you absolutely cannot get away from quantum mechanics. Because as you
*  think about updating this hypergraph, there isn't just one sequence of things, one definite sequence
*  of things that can happen. There are all these different possible update sequences that can occur.
*  You could do this, you know, piece of the hypergraph now and then this one later, and etc,
*  etc, etc. All those different paths of history correspond to these quantum quantum paths in
*  quantum mechanics, these different possible quantum histories. And one of the things that's kind of
*  surprising about it is they they branch, you know, there can be a certain state of the universe,
*  and it could do this or it could do that. But they can also merge, there can be two states
*  of the universe, which their next state, the next state they produce is the same for both of them.
*  Yeah. And that process of branching and merging is kind of critical. And the idea that they can
*  be merging is critical and somewhat non-trivial for these hypergraphs, because there's a whole
*  graph isomorphism story and there's a whole very elaborate set of mathematics.
*  That's where the causal invariance comes in.
*  Yes, among other things. Right. Yes. But so then what happens is that what one's seeing,
*  okay, so we've got this thing, it's branching, it's merging, etc, etc, etc. Okay, so now the
*  question is, how do we perceive that? Why don't we notice that the universe is branching and merging?
*  Why is it the case that we just think a definite set of things happen? Well, the answer is we are
*  embedded in that universe, and our brains are branching and merging too. And so what quantum
*  mechanics becomes a story of is how does a branching brain perceive a branching universe?
*  And the key thing is, as soon as you say, I think definite things happen in the universe,
*  that means you are essentially conflating lots of different parts of history. You're saying,
*  actually, as far as I'm concerned, because I'm convinced that definite things happen in the
*  universe, all these parts of history must be equivalent. Now, it's not obvious that that
*  would be a consistent thing to do. It might be you say all these parts of history are equivalent,
*  but by golly, moments later, that would be a completely inconsistent point of view.
*  Everything would have gone to hell in different ways. The fact that that doesn't happen is, well,
*  that's a consequence of this causal invariance thing. And the fact that that does happen a
*  little bit is what causes little quantum effects. And if that didn't happen at all, there wouldn't
*  be anything that is like quantum mechanics. Quantum mechanics is like in this bundle of paths,
*  it's a little bit like what happens in statistical mechanics and fluid mechanics, whatever,
*  that most of the time you just see this continuous fluid. You just see the world just progressing
*  in this kind of way that's like this continuous fluid. But every so often, if you look at the
*  exact right experiment, you can start seeing, well, actually, it's made of these molecules
*  where they might go that way or they might go this way, and that's kind of quantum effects.
*  So this kind of idea of where we're sort of embedded in the universe, this branching brain
*  is perceiving this branching universe, and that ends up being sort of a story of quantum mechanics.
*  That's part of the whole picture of what's going on. But I think, I mean, to come back to sort of
*  where does conscious, what is the story of consciousness? So in the universe, we've got
*  whatever it is, 10 to the 400 atoms of space, they're all doing these complicated things.
*  It's all a big complicated irreducible computation. The question is, what do we perceive from all of
*  that? And the answer is that we are parsing the universe in a particular way. Let me again go back
*  to the gas molecules analogy. In the gas in this room, there are molecules bouncing around all kinds
*  of complicated patterns, but we don't care. All we notice is the gas laws are satisfied,
*  maybe there's some fluid dynamics. These are kind of features of that assembly of molecules that
*  we notice, and then lots of details we don't notice. When you say we, do you mean the tools
*  of physics? Or do you mean literally the human brain and its perception system?
*  Well, okay. So the human brain is where it starts, but we built a bunch of instruments to do a bit
*  better than the human brain, but they still have many of the same kinds of ideas, you know, their
*  cameras and their pressure sensors and these kinds of things. They're not, you know, at this point,
*  we don't know how to make fundamentally qualitatively different sensory devices.
*  Right. So it's always just an extension of the consciousness experience.
*  Or our sensory experience.
*  Sensory experience, but sensory experience is somehow intricately tied to consciousness.
*  Right. Well, so one question is when we are looking at all these molecules in the gas,
*  and there might be 10th to 20th molecules in some little box or something, it's like,
*  what do we notice about those molecules? So one thing that we can say is we don't notice that much.
*  We are computationally bounded observers. We can't go in and say, okay, they're 10th to 20th
*  molecules and I know that I can sort of decrypt their motions and I can figure out this and that.
*  It's like, I'm just going to say what's the average density of molecules. And so one key feature of us
*  is that we are computationally bounded. And that when you are looking at a universe,
*  which is full of computation and doing huge amounts of computation, but we are computationally
*  bounded, there's only certain things about that universe that we're going to be sensitive to.
*  We're not going to be figuring out what all the atoms of space are doing because we're just
*  computationally bounded observers and we are only sampling these small set of features.
*  So I think the two defining features of consciousness that, and I would say that
*  the preamble to this is for years, as I've talked about sort of computation and fundamental features
*  of physics and science, people ask me, so what about consciousness? And for years I've said,
*  I have nothing to say about consciousness. And I've kind of told this story, you talk about
*  intelligence, you talk about life. These are both features where you say, what's the abstract
*  definition of life? We don't really know the abstract definition. We know the one for life
*  on earth. It's got RNA, it's got cell membranes, it's got all this kind of stuff. Similarly for
*  intelligence, we know the human definition of intelligence, but what is intelligence abstractly?
*  We don't really know. And so what I've long believed is that sort of the abstract definition
*  of intelligence is just computational sophistication. That is, that as soon as you can be computationally
*  sophisticated, that's kind of the abstract version, the generalized version of intelligence.
*  So then the question is, what about consciousness? And what I sort of realized is that consciousness
*  is actually a step down from intelligence. That is, that you might think, oh, consciousness
*  is the top of the pile, but actually I don't think it is. I think that there's this notion
*  of kind of computational sophistication, which is the generalized intelligence,
*  but consciousness has two limitations, I think. One of them is computational boundedness. That is,
*  that we're only perceiving a sort of computationally bounded view of the universe. And the other is
*  this idea of a single thread of time. That is, that we, and in fact, we know neurophysiologically
*  our brains go to some trouble to give us this one thread of attention, so to speak. And it isn't
*  the case that in all the neurons in our brains, that at least in our conscious, the correspondence
*  of language in our conscious experience, we just have the single thread of attention, single thread
*  of perception. And maybe there's something unconscious that's bubbling around that's
*  almost the quantum version of what's happening in our brains, so to speak. We've got the classical
*  flow of what we are mostly thinking about, so to speak. But there's this kind of bubbling around
*  of other paths that is all those other neurons that didn't make it to be part of our conscious
*  stream of experience. So in that sense, intelligence as computational sophistication is much broader
*  than the computational constraints which consciousness operates under, and also the
*  sequential thing, the notion of time. That's kind of interesting, but then the follow-up question
*  is like, okay, starting to get a sense of what is intelligence, and how does that connect to our
*  human brain? Because you're saying intelligence is almost like a fabric, like what, we plug into it
*  or something? Our consciousness plugs into it? Yeah, I mean, intelligence, I think the core,
*  intelligence at some level is just a word, but we are asking what is the notion of intelligence
*  as we generalize it beyond the bounds of humans, beyond the bounds of even the AIs that we humans
*  have built and so on. What is intelligence? Is the weather, people say the weather has a
*  mind of its own. What does that mean? Can the weather be intelligent? Yeah, what does agency
*  have to do with intelligence here? So is intelligence just like your conception of
*  computation? Just intelligence is the capacity to perform computation in a sea of-
*  Yeah, I think so. I mean, I think that's right. And I think that this question of,
*  is it for a purpose? That quickly degenerates into a horrible philosophical mess, because
*  whenever you say, did the weather do that for a purpose? Yeah. Right? Well, yes, it did. It
*  was trying to move a bunch of hot air from the equator to the poles or something. That's its
*  purpose. But why, because I seem to be equally as dumb today as I was yesterday. So there's some
*  persistence, like consistency over time that the intelligence I plugged into. So it seems like
*  there's a hard constraint between the amount of computation I can perform and my consciousness.
*  They seem to be really closely connected somehow. Well, I think the point is that the thing that
*  gives you the ability to have conscious intelligence, you can have this- Okay, so one
*  thing is we don't know intelligences other than the ones that are very much like us.
*  Right? And the ones that are very much like us, I think, have this feature of single thread of time
*  computationally bounded. Now, but you also need computational sophistication. Having a single
*  thread of time and being computationally bounded, you could just be a clock going tick tock. That
*  would satisfy those conditions. But the fact that we have this irreducible computational ability,
*  that's an important feature. That's the bedrock on which we can construct the things we construct.
*  Now, the fact that we have this experience of the world that has the single thread of time and
*  computational boundedness, the thing that I realized is it's that that causes us to deduce
*  from this irreducible mess of what's going on in the physical world the laws of physics that we
*  think exist. So in other words, if we say, why do we believe that there is continuous space, let's
*  say? Why do we believe that gravity works the way it does? Well, in principle, we could be parsing
*  details of the universe that were- Okay, the analogy is, again, with statistical mechanics and
*  molecules in a box, we could be sensitive to every little detail of the swirling around of
*  those molecules. And we could say, what really matters is the wiggle effect. That is something
*  that we humans just never notice because it's some weird thing that happens when there are 15
*  collisions of air molecules and this happens and that happens. We just see the pure motion of a
*  ball moving about. Why do we see that? Right. And the point is that what seems to be the case
*  is that the things that if we say, given this sort of hypergraph that's updating and all the
*  details about all the sort of atoms of space and what they do, and we say, how do we slice that
*  to what we can be sensitive to? What seems to be the case is that as soon as we assume computational
*  boundedness, single thread of time, that leads us to general relativity. In other words, we can't
*  avoid that. That's the way that we will parse the universe. Given those constraints, we parse the
*  universe according to those particular, in such a way that we say the aggregate reducible
*  pocket of computational reducibility that we slice out of this kind of whole computational
*  irreducible ocean of behavior is just this one that corresponds to general relativity.
*  Yeah, but we don't perceive general relativity. Well, we do if we do fancy experiments.
*  So you're saying so perceive really does mean the full-
*  We drop something. That's a great example of general relativity in action.
*  What's the difference in that and Newtonian mechanics?
*  When I say general relativity, that's the uber theory, so to speak. I mean,
*  Newtonian gravity is just the approximation that we can make on the earth and things like that.
*  The phenomenon of gravity is one that is a consequence of, we would perceive something
*  very different from gravity. So the way to understand that is when we think about, okay,
*  so we make up reference frames with which we parse what's happening in space and time.
*  In other words, one of the things that we do is we say as time progresses,
*  everywhere in space something happens at a particular time, and then we go to the next time,
*  and we say this is what space is like at the next time, this is what space is like at the next time.
*  That's the reason we are used to doing that is because when we look around, we might see
*  10, 100 meters away. The time it takes light to travel that distance is really short compared
*  to the time it takes our brains to know what happened. So as far as our brains are concerned,
*  we are parsing the universe in this, there is a moment in time, it's all of space. There's a moment
*  in time, it's all of space. If we were the size of planets or something, we would have a different
*  perception because the speed of light would be much more important to us. We wouldn't have this
*  perception that things happen progressively in time everywhere in space. And so that's an important
*  kind of constraint. And the reason that we kind of parse the universe in the way that causes us to
*  say gravity works the way it does is because we're doing things like deciding that we can say the
*  universe exists, space has a definite structure. There is a moment in time, space has this definite
*  structure. We move to the next moment in time, space has another structure. That kind of setup
*  is what lets us kind of deduce kind of what to parse the universe in such a way that we say
*  gravity works the way it does. So that kind of reference frame is that the illusion of that
*  is that you're saying that's somehow useful for consciousness.
*  That's what consciousness does. Because in a sense, what consciousness is doing is
*  it's insisting that the universe is kind of sequentialized. And it is not allowing the
*  possibility that, oh, there are these multiple threads of time and they're all flowing differently.
*  It's like saying, no, everything is happening in this one thread of experience that we have.
*  And that illusion of that one thread of experience cannot happen at the planetary scale.
*  Are you saying typical human? Are you saying we are at a human level as special here for
*  consciousness? Well, for our kind of consciousness, if we existed at a scale close to the elementary
*  length, for example, then our perception of the universe will be absurdly different.
*  Okay. But this makes consciousness seem like a weird side effect to this particular scale.
*  And so who cares? I mean, consciousness is not that special.
*  Look, I think that a very interesting question is, which I've certainly thought a little bit about,
*  is what can you imagine? What is the sort of factoring of something? What are some other
*  possible ways you could exist, so to speak? And if you were a photon, if you were sort of
*  some kind of thing that was kind of intelligence represented in terms of photons, for example,
*  the photons we receive in the cosmic microwave background, those photons, as far as they're
*  concerned, the universe just started. They were emitted 100,000 years after the beginning of the
*  universe. They've been traveling at the speed of light. Time stayed still for them. And then they
*  just arrived and we just detected them. So for them, the universe just started. And that's a
*  different perception that has implications for a very different perception of time.
*  They don't have that single thread that seems to be really important for being able to tell a
*  heck of a good story. So we humans... Yes. We can tell a story. Right. We can tell a story.
*  And what other kind of stories can you tell? So a photon is a really boring story.
*  Yeah. I mean, so I don't know if they're a boring story, but I think it's... I've been wondering
*  about this and I've been asking friends of mine who are science fiction writers and things,
*  have you written stuff about this? And I've got one example, a great collection of books from my
*  friend, Rudy Rooker, which I have to say, they're books that are very informed by a bunch of science
*  that I've done. And the thing that I really loved about them is... In the first chapter of the book,
*  the Earth is consumed by these things he called Nants, which are nanobots type things.
*  Nice.
*  But so the Earth is gone in the first, but then it comes back. But then...
*  Spoiler alert.
*  Yeah, right. That was only a micro spoiler. It's only chapter one.
*  Okay. Good.
*  But the thing that is not a real spoiler alert because it's such a complicated concept,
*  in the end, the Earth is saved by this thing called the principle of computational equivalence,
*  which is a kind of a core scientific idea of mine. And I was just thrilled. I don't read fiction
*  books very often. And I was just thrilled. I get to the end of this and it's like, oh my gosh,
*  everything is saved by this sort of deep scientific principle.
*  Can you maybe elaborate how the principle of computational equivalence can save a planet?
*  That would be a terrible spoiler for me.
*  That would be a spoiler. Okay.
*  Yeah. But no, but let me say what the principle of computational equivalence is.
*  Mm-hmm.
*  So the question is, you have a system, you have some rule, you can think of its behavior
*  as corresponding to a computation. The question is, how sophisticated is that computation?
*  The statement of the principle of computational equivalence is, as soon as it's not obviously
*  simple, it will be as sophisticated as anything. And so that has the implication that rule 30,
*  you know, our brains, other things in physics, they're all ultimately equivalent in the
*  computations they can do. And that's what leads to this computational irreducibility idea, because
*  the reason we don't get to jump ahead and out think rule 30 is because we're just computationally
*  equivalent to rule 30. So we're kind of both just running computations that are the same sort of raw,
*  the same level of computation, so to speak. So that's kind of the idea there. And the question,
*  I mean, it's like the, you know, in the science fiction version would be, okay, somebody says,
*  we just need more servers, get us more servers. The way to get even more servers is turn the
*  whole planet into a bunch of microservers. And that's where it starts. And so the question of,
*  you know, computational equivalence, principle of computational equivalence is, well, actually,
*  you don't need to build those custom servers. Actually, you can just use natural computation
*  to compute things, so to speak, you can use nature to compute, you don't need to have done
*  all that engineering. And it's kind of feels a little disappointing that you say, we're going
*  to build all these servers, we're going to do all these things, we're going to make, you know, maybe
*  we're going to have human consciousness uploaded into, you know, some elaborate digital environment.
*  And then you look at that thing, and you say, it's got electrons moving around, just like in a rock.
*  And then you say, well, what's the difference? And principle of computational equivalence says,
*  there isn't, at some level, a fundamental, you know, you can't say mathematically, there's a
*  fundamental difference between the rock that is the future of human consciousness, and the rock
*  that's just a rock. Now, what I've sort of realized with this kind of consciousness thing is, there is
*  there is an aspect of this that seems to be more special, that isn't. And for example, something I
*  I haven't really teased apart properly, is when it comes to something like the weather and the
*  weather having a mind of its own or whatever, or your average, you know, pulsar magnetosphere,
*  acting like a sort of intelligent thing, how does that relate to, you know, how is that
*  that entity related to the kind of consciousness that we have, and sort of what would the world
*  look like, you know, to the weather, if we think about the weather as a mind,
*  what will it perceive? What will it laws, its laws of physics be? I don't really know.
*  Because it's very parallel.
*  It's very parallel, among other things. And it's not obvious. I mean, this is a really kind of
*  mind bending thing, because we've got to try and imagine where, you know, we've got to try and
*  imagine a parsing of the universe different from the one we have. And by the way, when we think
*  about extraterrestrial intelligence, and so on, I think that's kind of the key thing is, you know,
*  we've always assumed, I've always assumed, okay, the extraterrestrials, at least they have the
*  same physics, we all live in the same universe, they've got the same physics. But actually,
*  that's not really right, because the extraterrestrials could have a completely different
*  way of parsing that the universe so it's as if, you know, there could be for all we know,
*  right here in this room, you know, in the in the details of the motion of these gas molecules,
*  there could be an amazing intelligence that we were like, but we have no way of we're not parsing
*  the universe in the same way, if only we could parse the universe in the right way, you know,
*  immediately this amazing thing that's going on, and this, you know, huge culture that's developed
*  and all that kind of thing would be obvious to us, but it's not because we have our particular way
*  of parsing the universe. Would that thing also have an agency? I don't know the right word to use,
*  but something like consciousness, but a different kind of consciousness?
*  I think it's a question of just what you mean by the word, because I think that the,
*  you know, this notion of consciousness and the, okay, so some people think of consciousness as
*  sort of a key aspect of it is that we feel that the sort of a feeling of that we exist in some
*  way that we have this intrinsic feeling about ourselves. You know, I suspect that any of these
*  things would also have an intrinsic feeling about themselves. I've been sort of trying to think
*  recently about constructing an experiment about what if you were just a piece of a cellular
*  automaton, let's say, you know, what would your feeling about yourself actually be? And, you know,
*  can we put ourselves in the shoes, in the cells of the cellular automaton, so to speak? Can we get
*  ourselves close enough to that, that we could have a sense of what the world would be like if you were
*  operating in that way? And it's a little difficult because, you know, you have to not only think
*  about what are you perceiving, but also what's actually going on in your brain. And our brains
*  do what they actually do. And they don't, it's, you know, I think there might be some experiments
*  that are possible with, you know, neural nets and so on, where you can have something where you can
*  at least see in detail what's happening inside the system. And I've been sort of one of my projects
*  to think about is, is there a way of kind of getting a sense kind of from inside the system
*  about what its view of the world is and how it, you know, can we make a bridge? See, the main issue
*  is this, where, you know, it's a sort of philosophically difficult thing because it's like,
*  we do what we do. We understand ourselves, at least to some extent.
*  We humans understand ourselves.
*  That's correct. And, but yet, okay, so what are we trying to do, for example, when we are trying to
*  make a model of physics? What are we actually trying to do? Because, you know, you say, well,
*  can we work out what the universe does? Well, of course we can. We just watch the universe.
*  The universe does what it does. But what we're trying to do when we make a model of physics
*  is we're trying to get to the point where we can tell a story to ourselves that we understand
*  that is also a representation of what the universe does. So it's this kind of, you know,
*  can we make a bridge between what we humans can understand in our minds and what the universe does?
*  And in a sense, you know, a large part of my kind of life efforts have been devoted to making
*  computational language, which kind of is a bridge between what is possible in the computational
*  universe and what we humans can conceptualize and think about. In a sense, what, you know,
*  when I built Wolfram Language and our whole sort of computational language story, it's all about
*  how do you take sort of raw computation and this ocean of computational possibility, and how do we
*  represent pieces of it in a way that we humans can understand and that map onto things that we care
*  about doing? And in a sense, when you add physics, you're adding this other piece where we can, you
*  know, mediate it by computer. Can we get physics to the point where we humans can understand
*  something about what's happening in it? And when we talk about an alien intelligence, it's kind of
*  the same story. It's like, is there a way of mapping what's happening there onto something
*  that we humans can understand? And, you know, physics, in some sense, is like our exhibit one
*  of the story of alien intelligence. It's an alien intelligence in some sense. And what we're doing
*  in making a model of physics is mapping that onto something that we understand. And I think, you
*  know, a lot of these other things that I've recently been kind of studying, whether it's
*  molecular biology, other kinds of things, which we can talk about a bit, those are other cases
*  where we're in a sense, trying to again, make that bridge between what we humans understand,
*  and sort of the natural language of that sort of alien intelligence in some sense.
*  When you're talking about, just to backtrack a little bit about cellular automata, being able to,
*  what's it like to be a cellular automata in a way that's equivalent to what it's like to be a
*  conscious human being? How do you approach that? So is it looking at some subset of the cellular
*  automata, asking questions of that subset, like how the world is perceived as that subset,
*  like for that local pocket of computation, what are you able to say about the broader
*  cellular type? And that somehow then can give you a sense of how to step outside of that cellular
*  automata. Right. But the tricky part is that that little subset, what it's doing is it has a view
*  of itself. And the question is, how do you get inside it? It's like, you know, when we, with
*  humans, right? It's like, we can't get inside each other's consciousness. That doesn't really
*  make sense. It's like, there is an experience that somebody is having, but you can perceive
*  things from the outside, but sort of getting inside it, it doesn't quite make sense. And
*  for me, these sort of philosophical issues, and this one I have not untangled, so let's be...
*  For me, the thing that has been really interesting in thinking through some of these things is,
*  when it comes to questions about consciousness or whatever else, it's like, when I can run a program
*  and actually see pictures and make things concrete, I have a much better chance to understand what's
*  going on than when I'm just trying to reason about things in a very abstract way. Yeah, but there may
*  be a way to map the program to your conscious experience. So for example, when you play a video
*  game, you do a first person shooter, you walk around inside this entity. It's a very different
*  thing than watching this entity. So if you can somehow connect more and more, connect this full
*  conscious experience to the subset of the cellular automata. Yeah, it's something like that. But the
*  difference in the first person shooter thing is there's still your brain and your memory is still
*  remembering. It's hard to... Again, what one's going to get, one is not going to actually be
*  able to be the cellular automaton. One's going to be able to watch what the cellular automaton does.
*  But this is the frustrating thing that I'm trying to understand how to think about being it, so to
*  speak. Okay, so like in virtual reality, there's a concept of immersion, like with anything,
*  with video games, with books, there's a concept of immersion. It feels like over time, if the
*  virtual reality experience is well done and maybe in the future it'll be extremely well done,
*  the immersion leads you to feel like... You mentioned memories. You forget that you even
*  ever existed outside that experience. It's so immersive. I mean, you could argue sort of
*  mathematically that you can never truly become immersed, but maybe you can. I mean, why can't
*  you merge with the cellular automaton? I mean, aren't you just part of the same fabric? Why can't
*  you just like... Well, that's a good question. I mean, so let's imagine the following scenario.
*  Let's imagine... Then can you return? But then can you return back?
*  Well, yeah, right. I mean, it's like, let's imagine you've uploaded, your brain is scanned,
*  you've got every synapse mapped out. You upload everything about you, the brain simulator. You
*  upload the brain simulator and the brain simulator is basically some glorified cellular
*  automaton. And then you say, well, now we've got an answer to what does it feel like to be a cellular
*  automaton? It feels just like it felt to be ordinary you because they're both computational
*  systems and they're both operating in the same way. So in a sense, but I think there's somehow
*  more to it because in that sense, when you're just making a brain simulator, it's just... We're just
*  saying there's another version of our consciousness. The question that we're asking is,
*  if we tease away from our consciousness and get to something that is different,
*  how do we make a bridge to understanding what's going on there? And there's a way of thinking
*  about this. Okay, so this is coming on to sort of questions about the existence of the universe
*  and so on. But one of the things is there's this notion that we have of rule-iel space.
*  So we have this idea of this physical space, which is something you can move around in that's
*  associated with the actual extent of the spatial hypergraph. Then there's what we call branch-iel
*  space, the space of quantum branches. So in this thing we call the multi-way graph of all of this
*  sort of branching histories, there's this idea of a kind of space where instead of moving around in
*  physical space, you're moving from history to history, so to speak, from one possible history
*  to another possible history. And that's kind of a different kind of space that is the space in which
*  quantum mechanics plays out. Quantum mechanics, like for example, oh, something like, I think we're
*  slowly understanding things like destructive interference in quantum mechanics. That what's
*  happening is branch-iel space is associated with phase in quantum mechanics. And what's happening
*  is the two photons that are supposed to be interfering and destructively interfering
*  are winding up at different ends of branch-iel space. And so us, as these poor observers that
*  have branching brains that are trying to conflate together these different threads of history
*  and say, we've really got a consistent story that we're telling here. We're really knitting
*  together these threads of history. By the time the two photons wound up at opposite ends of branch-iel
*  space, we just can't knit them together to tell a consistent story. So for us, that's sort of the
*  analog of destructive interference. Got it. And then there's rule-iel space too, which is the space
*  of rules. Yes. Well, that's another level up. So there's the question. Actually, I do want to
*  mention one thing because it's something I've realized in recent times and I think it's really,
*  really kind of cool, which is about time dilation and relativity. And it kind of helps to understand.
*  It's something that kind of helps in understanding what's going on. So according to relativity,
*  if you have a clock, it's ticking at a certain rate, you send it in a spacecraft that's going
*  at some significant fraction of the speed of light. To you as an observer at rest, that clock
*  that's in the spacecraft will seem to be ticking much more slowly. And so in other words, it's kind
*  of like the twin who goes off to Alpha Centauri and goes very fast will age much less than the
*  twin who's on Earth that is just hanging out where they're hanging out. Okay, why does that happen?
*  Okay, so it has to do with what motion is. So in our models of physics, what is motion? Well,
*  when you move from somewhere to somewhere, you're having to sort of recreate yourself at a different
*  place in space. When you exist at a particular place and you just evolve with time, you're again,
*  you're updating yourself, you're following these rules to update what happens. Well, so the question
*  is when you have a certain amount of computation in you, so to speak, when there's a certain amount,
*  you know, you're computing, the universe is computing at a certain rate, you can either use
*  that computation to work out sitting still where you are, what's going to happen successively in
*  time, or you can use that computation to recreate yourself as you move around the universe. And so
*  time dilation ends up being, it's really cool actually that this is explainable in a way that
*  isn't just imagine the mathematics of relativity. But that time dilation is a story of the fact that
*  as you kind of are recreating yourself as you move, you are using up some of your computation.
*  And so you don't have as much computation left over to actually work out what happens
*  progressively with time. So that means that time is running more slowly for you because it is,
*  you're using up your computation, your clock can't tick as quickly because every tick of the clock
*  is using up some computation, but you already use that computation up on moving at, you know,
*  half the speed of light or something. And so that's why time dilation happens. And so you can start,
*  so it's kind of interesting that one can sort of get an intuition about something like that,
*  because it has seemed like just a mathematical fact about the mathematics of special relativity
*  and so on. Well, for me, it's a little bit confusing what the you in that picture is,
*  because you're using up computation. Okay. So we're simply saying the entity is updating itself
*  according to the way that the universe updates itself. And the question is, those updates,
*  let's imagine the you as a clock, okay? And the clock is, there's all these updates, the
*  hypergraph and a sequence of updates cause the pendulum to swing back the other way and then
*  swing back and forth. Okay. And all of those updates are contributing to the motion of the
*  pendulum going back and forth or the little oscillator moving, whatever it is. Okay. But
*  then the alternative is that sort of situation one, where the thing is at rest. Situation two,
*  where it's kind of moving, what's happening is it is having to recreate itself. At every moment,
*  the thing is going to have to do the computations to be able to sort of recreate itself at a
*  different position in space. And that's kind of the intuition behind. So it's either going to
*  spend its computation recreating itself at a different position in space, or it's going to
*  spend its computation doing the sort of doing the updating of the ticking of the clock, so to speak.
*  And so the more updating is doing the less the ticking of the clock update is doing.
*  That's right. The more it's having to update because of motion, the less it can update the
*  clock. So that's some, I mean, obviously there's a sort of mathematical version of it that relates
*  to how it actually works in relativity, but that's kind of, to me that was sort of exciting to me,
*  that it's possible to have a really mechanically explainable story there. That isn't, and similarly
*  in quantum mechanics, this notion of branching brains, perceiving branching universes, to me,
*  that's getting towards a sort of mechanically explainable version of what happens in quantum
*  mechanics, even though it's a little bit mind bending to see these things about under what
*  circumstances can you successfully knit together those different threads of history and when do
*  things sort of escape and those kinds of things. But the thing about this physical space and
*  physical space, the main sort of big theory is general relativity, the theory of gravity,
*  and that tells you how things move in physical space. In branchial space, the big theory is the
*  Feynman path integral, which it turns out tells you essentially how things move in quantum,
*  in the space of quantum phases. So it's kind of like motion in branchial space. And it's kind of
*  a fun thing to start thinking about what, oh, you know, all these things that we know in physical
*  space, like event horizons and black holes and so on, what are the analogous things in branchial
*  space? For example, the speed of light, what's the analog of the speed of light in branchial space?
*  It's the maximum speed of quantum entanglement. So the speed of light is a flash bulb goes off here,
*  what's the maximum rate at which the effect of that flash bulb is detectable moving away in space?
*  So similarly in branchial space, something happens. And the question is, how far in this branchial
*  space in the space of quantum states, how far away can that get within a certain period of time?
*  And so there's this notion of a maximum entanglement speed. And that might be observable.
*  That's the thing we've been sort of poking at is might there be a way to observe it even in some
*  atomic physics kind of situation? Because one of the things that's weird in quantum mechanics is
*  we're, you know, when we study quantum mechanics, we mostly study it in terms of small numbers of
*  particles, you know, this electron does this, this thing on an ion trap does that and so on.
*  But when we deal with large numbers of particles, kind of all bets are off. It's kind of too
*  complicated to deal with quantum mechanics. And so what ends up happening is, so this question
*  about maximum entanglement speed and things like that may actually play in one of these in the sort
*  of story of many body quantum mechanics, and even have some suspicions about things that might happen
*  even in one of the things I realized I'd never understood. And it's kind of embarrassing, but I
*  think I now understand a little better is when you have chemistry, and you have quantum mechanics,
*  it's like, well, there's two carbon atoms in this molecule, and we do a reaction,
*  and we draw a diagram, and we say this carbon atom ends up in this place. And it's like,
*  but wait a minute, in quantum mechanics, nothing ends up in a definite place. There's always just
*  some wave function for this to happen. How can it be the case that we can draw these reasonable,
*  it just ended up in this place? And you have to kind of say, well, the environment of the molecule
*  effectively made a bunch of measurements on the molecule to keep it kind of classical.
*  And that's a story that has to do with this whole thing about measurements have to do with this idea
*  of can we conclude that something definite happened? Because in quantum mechanics,
*  the intrinsic quantum mechanics, the mathematics of quantum mechanics is all about,
*  they're just these amplitudes for different things to happen. Then there's this thing of,
*  and then we make a measurement, and we conclude that something definite happened.
*  And that has to do with this thing, I think, about sort of knitting together these different
*  threads of history and saying, this is now something where we can definitively say something
*  definite happened. In the traditional theory of quantum mechanics, it's just like, you know,
*  after you've done all the sample shoot computation, then this big hammer comes down and you do a
*  measurement and it's all over. And that's been very confusing. For example, in quantum computing,
*  it's been a very confusing thing because when you say, you know, in quantum computing, the basic idea
*  is you're going to use all these separate threads of computation, so to speak, to do all the different
*  parts of, you know, try these different factors for an integer or something like this. And it looks
*  like you can do a lot because you've got all these different threads going on. But then you have to
*  say, well, at the end of it, you've got all these threads and every thread came up with a definite
*  answer. But we got to conflate those together to figure out a definite thing that we humans
*  can take away from it, a definite, so the computer actually produced this output.
*  So having this branch of space and this hypergraph model of physics, do you think it's possible to
*  then make predictions that are definite about many body quantum mechanical systems? Is that the hope?
*  I think it's likely, yes. But I don't, you know, this is every one of these things when you go
*  from the underlying theory, which is complicated enough, and it's, I mean, the theory at some level
*  is beautifully simple. But as soon as you start actually trying to, it's this whole question about
*  how do you bridge it to things that we humans can talk about, it gets really complicated.
*  And this thing about actually getting it to a definite prediction about, you know, a definite
*  thing you can say about chemistry or something like this, you know, that's just a lot of work.
*  So I'll give you an example. There's a thing called the quantum Zeno effect. So the idea is,
*  you know, quantum stuff happens, but then if you make a measurement, you're kind of freezing time
*  in quantum mechanics. And so it looks like there's a possibility that with sort of the
*  relationship between the quantum Zeno effect and the way that many body quantum mechanics works and
*  so on, maybe just conceivably, it may be possible to actually figure out a way to measure the maximum
*  entanglement speed. And the reason we can potentially do that is because the systems we deal with in
*  terms of atoms and things, they're pretty big, you know, a mole of atoms is, you know, it's a lot of
*  atoms. And, you know, but it isn't a very, you know, it's something where to get, you know,
*  when we're dealing with how can you see 10 to the minus 100, so to speak, well, by the time you've
*  got, you know, 10 to the 30th atoms, you're not, you know, you're within a little bit closer
*  striking distance of that. It's not like, oh, we've just got, you know, two atoms, and we're
*  trying to see down to 10 to the minus 100 meters or whatever. So I don't know how it will work,
*  but this is a potential direction. And if you can tell, by the way, if we could measure the
*  maximum entanglement speed, we would know the elementary length. These are all related. So
*  if we got that one number, we just need one number. If we can get that one number, we can,
*  you know, the theory has no parameters anymore. And, you know, there are other places, well,
*  there's another hope for doing that is in cosmology. In this model, one of the features is the
*  universe is not fixed dimensional. I mean, we think we live in three dimensional space,
*  but this hypergraph doesn't have any particular dimension. It can emerge as something which on
*  an approximation, it's as if, you know, you say, what's the volume of a sphere in the hypergraph
*  where a sphere is defined as how many nodes do you get to when you go a distance r away from a
*  given point? And you can say, well, if I get to about r cubed nodes, when I go a distance r
*  away in the hypergraph, then I'm living roughly in three dimensional space. But you might also get
*  to r to the point, you know, 2.92, you know, for some value of r in, you know, as r increases,
*  that might be the sort of fit to what happens. And so one of the things we suspect is that the
*  very early universe was essentially infinite dimensional, and that as the universe expanded,
*  it became lower dimensional. And so one of the things that is another little sort of point where
*  we think there might be a way to actually measure some things is dimension fluctuations in the
*  early universe. That is, is there a, is there leftover dimension fluctuation of at the time of
*  the cosmic microwave background, 100,000 years or something after the beginning of the universe?
*  Is it still the case that there are, there were pieces of the universe that didn't have dimension
*  three, that had dimension 3.01 or something? And can we tell that? Is that possible to observe
*  a fluctuations in dimensions? I don't even know what that entails.
*  Okay. So the question, which should be an elementary exercise in electrodynamics,
*  except it isn't, is understanding what happens to a photon when it propagates through 3.01
*  dimensional space. So for example, the inverse square law is a consequence of the, you know,
*  the, the surface area of a sphere is proportional to r squared. But if you're not in three
*  dimensional space, the surface area of sphere is not proportional to r squared. It's r to the,
*  whatever 2.01 or something. And so that means that I think when you can try and do optics,
*  you know, a common principle in optics is Huygens principle, which basically says that every
*  piece of a wavefront of a, of a, of, of light is a source of new spherical waves.
*  And those spherical waves, if they're different dimensional spherical waves,
*  will have other characteristics. And so there will be bizarre optical phenomena,
*  which we haven't figured out yet. So you're, you're, you're what? Looking for some weird
*  photon trajectories that designate that as 3.01 dimensional space?
*  Yeah. Yeah. That would be an example of, I mean, you know, there are, there are only a certain
*  number of things we can measure about photons. You know, we can measure their polarization,
*  we can measure their frequency, we can measure their direction, those kinds of things.
*  And, you know, how that all works out. And, you know, in the current models of physics,
*  you know, it's been hard to explain how the universe manages to be as uniform as it is.
*  And that's led to this inflation idea that to the, to the great annoyance of my then
*  collaborator, I, we had, we figured out in like 1979, we had this realization that,
*  that you could get something like this, but it seemed implausible that that's the way the
*  universe worked. So we put in a footnote and that was, so that's a, but, but in any case,
*  I've never really completely believed it, but this, that's an idea for how to sort of puff out
*  the universe faster than the speed of light, early moments of the universe, that that's the sort of
*  the inflation idea and that, that you can somehow explain how the universe manages to be as uniform
*  as it is in our model. This turns out to be much more natural because the universe just starts very
*  connected. The hypergraph is not such that the ball that you grow starting from a single point
*  has volume R cubed. It might have volume R to the 500 or R to the infinity. And so that means that
*  you, you sort of naturally get this much higher degree of connectivity and uniformity in the
*  universe. And then the question is, this is sort of the mathematical physics challenge is in the
*  standard theory of the universe, there's the Friedman Robertson Walker universe, which is the
*  kind of standard model where the universe is isotropic and homogeneous. And you can then
*  work out the equations of general relativity and you can figure out how the universe expands.
*  We would like to do the same kind of thing, including dimension change. This is just difficult
*  mathematical physics. I mean, the reason it's difficult is the sort of fundamental reason.
*  It's difficult when, when people invented calculus 300 years ago, calculus was a story of
*  understanding change and change as a function of a variable. And so people study univariate calculus
*  they study multivariate calculus. It's one variable, it's two variables, three variables,
*  but whoever studied, you know, 2.5 variable calculus turns out nobody turns out that,
*  but what we need to have to understand these fractional dimensional spaces, which don't work
*  like, well, they're, they're, they're spaces where, where the effective dimension is not an integer.
*  So you can't apply the tools of calculus and naturally and easily to fractional dimensions.
*  And so somebody has to figure out how to do that. We're trying to figure this out. I mean,
*  it's, it's very interesting. I mean, it's very connected to very frontier issues in mathematics.
*  It's very beautiful, but so is it possible, is it possible we're dealing with a scale that's so,
*  so much smaller than our human scale. Is it possible to make predictions versus explanations?
*  Do you have a hope that with this hypergraph model, you'd be able to make predictions that
*  then could be validated with a physics experiment, predictions that couldn't have been done or weren't
*  done otherwise. Yeah, yeah, yeah. I mean, you know, I think-
*  In which domain do you think that prediction- Okay, so they're going to be cosmology ones
*  to do with dimension fluctuations in the universe. That's a very bizarre effect. Nobody,
*  you know, dimension fluctuation is just something nobody ever looked for that. If anybody sees
*  dimension fluctuation, that's a huge flag that something like our model is going on.
*  And how one detects that, you know, that's a problem of kind of, you know, that's a problem
*  of traditional physics in a sense of what's the best way to actually figure that out. And for
*  example, that's one, there are all kinds of things one can imagine. I mean, there are things that
*  in black hole mergers, it's possible that there will be effects of maximum entanglement speed
*  in large black hole mergers. That's another possible thing. And all of that is detected
*  through like what? Do you have a hope for a LIGO type of situation? Like that's gravitational waves?
*  Yeah. Or alternatively, I mean, I think it's, you know, look, figuring out experiments is like
*  figuring out technology inventions. That is, you know, you've got a set of raw materials,
*  you've got an underlying model, and now you've got to be very clever to figure out, you know,
*  what is that thing I can measure that just somehow, you know, leverages into the right place?
*  And we've spent less effort on that than I would have liked. Because one of the reasons is that I
*  think that the physicists who've been working on our models, we've now, lots of physicists,
*  actually, it's very, very nice. It's kind of, it's one of these cases where I'm almost, I'm really
*  kind of pleasantly surprised that the sort of absorption of the things we've done has been
*  quite rapid and quite sort of, you know, very positive.
*  So it's a Cambrian explosion of physicists too, not just ideas.
*  Yes. I mean, you know, a lot of what's happened that's really interesting, and again, not what
*  I expected is there are a lot of areas of sort of very elaborate, sophisticated mathematical physics,
*  whether that's causal set theory, whether it's higher category theory, whether it's
*  categorical quantum mechanics, all sorts of elaborate names for these things, spin networks,
*  perhaps, you know, causal dynamical triangulations, all kinds of names of these fields.
*  And these fields have a bunch of good mathematical physicists in them who've been working for decades
*  in these particular areas. And the question is, but they've been building these mathematical
*  structures. And the mathematical structures are interesting, but they don't typically sit on
*  anything. They're just mathematical structures. And I think what's happened is our models provide
*  kind of a machine code that lives underneath those models. So a typical example, this is
*  due to Jonathan Gorod, who's one of the key people who's been working on our project.
*  This is in, okay, so I'll give you an example, just to give a sense of how these things connect.
*  This is in causal set theory. So the idea of causal set theory is there are, in space time,
*  we imagine that there's space and time, it's a three plus one dimensional, you know, setup.
*  We imagine that there are just events that happen at different times and places in space and time.
*  And the idea of causal set theory is the only thing you say about the universe is there are a
*  bunch of events that happen sort of randomly at different places in space and time. And then the
*  whole sort of theory of physics has to be to do with this graph of causal relationships between
*  these randomly thrown down events. So they've always been confused by the fact that to get even
*  Lorentz invariance, even relativistic invariance, you need a very special way to throw down those
*  events. And they've had no natural way to understand how that would happen. So what
*  Jonathan figured out is that, in fact, from our models, instead of just generating events at
*  random, our models necessarily generate events in some pattern in space time effectively, that then
*  leads to Lorentz invariance and relativistic invariance and all those kinds of things.
*  So it's a place where all the mathematics that's been done on, well, we just have a random collection
*  of events. Now what consequences does that have in terms of causal set theory and so on? That can
*  all be kind of wheeled in now that we have some different underlying foundational idea for what
*  the particular distribution of events is, as opposed to just where we throw down random events.
*  And so that's a typical sort of example of what we're seeing in all these different areas of kind
*  of how you can take really interesting things that have been done in mathematical physics
*  and connect them. And it's really kind of beautiful because the abstract models we have
*  just seem to plug into all these different very interesting, very elegant abstract ideas.
*  But we're now giving sort of a reason for that to be the way, a reason for one to care. I mean,
*  it's like saying you can think about computation abstractly. You can think about, I don't know,
*  combinators or something as abstract computational things. And you can sort of do all kinds of study
*  of them. But it's like, why do we care? Well, okay, Turing machines are a good start because
*  you can kind of see that sort of mechanically doing things. But when we actually start thinking
*  about computers computing things, we have a really good reason to care. And this is sort of what we're
*  providing, I think, is a reason to care about a lot of these areas of mathematical physics. So
*  that's been very nice. So I'm not sure we've ever got to the question of why does the universe
*  exist at all? No, let's talk about that. So it's not the simplest question in the world. So
*  it takes a few steps to get to it. And it's nevertheless even surprising that you can even
*  begin to answer this question, as you were saying. I'm very surprised. So the next thing to perhaps
*  understand is this idea of ruleial space. So we've got kind of physical space, we've got
*  branchial space, the space of possible quantum histories. And now we've got another level of
*  kind of abstraction, which is ruleial space. And here's where that comes from. So you say, okay,
*  you say we've got this model for the universe, we've got a particular rule, and we run this
*  rule and we get the universe. Okay, so that's interesting. Why that rule? Why not another rule?
*  And so that confused me for a long time. And I realized, well, actually, what if the thing could
*  be using all possible rules? What if at every step, in addition to saying apply a particular rule
*  at all places in this hypergraph, one could say, just take all possible rules and apply all possible
*  rules at all possible places in this hypergraph. Okay. And then you make this ruleial multi-way
*  graph, which both is all possible histories for a particular rule and all possible rules.
*  So the next thing you'd say is, how can you get anything reasonable out of how can anything,
*  you know, real come out of the set of all possible rules applied in all possible ways?
*  Okay, this is a subtle thing. So which I haven't fully untangled. The there is this object, which
*  is the result of running all possible rules and all possible ways. And you might say, if you're
*  running all possible rules, why can't everything possible happen? Well, the answer is because when
*  you there's sort of this entanglement that occurs. So let's say that you have a lot of different
*  possible initial conditions, a lot of different possible states, then you're applying these
*  different rules. Well, some of those rules can end up with the same state. So it isn't the case that
*  you can just get from anywhere to anywhere. There's this whole entangled structure of what can lead to
*  what and there's a definite structure that's produced. I think I'm going to call that definite
*  structure the ruley add the limit of the limits of kind of all possible rules being applied in
*  all possible ways. And you're saying that structure is finite. So that somehow connects to maybe a
*  similar kind of thing as like causal invariance. Well, it happens really, necessarily has causal
*  invariance. That's a feature of that's just a mathematical consequence of essentially using
*  all possible rules plus universal computation gives you the fact that from any diverging paths,
*  you can always the pause will always come. But does that say that the rule does that
*  necessarily infer that the ruley add is finite? In the end, it's not necessarily finite. I mean,
*  it's a it's a the just like the history of the universe may not be finite, the history of the
*  universe time may keep going forever. You can keep running the computations of the ruley add and you'll
*  keep spewing out more and more and more structure. It's like time doesn't have to end. It's it's
*  that but the issue is there are there are three limits that happen in this ruley add object.
*  One is how long you run the computation for. Another is how many different rules you're applying.
*  Another is how many different states you start from. And the mixture of those three limits. I
*  mean, this is just mathematically a horrendous object. Okay. And what's what's interesting about
*  this object is the one thing that does seem to be the case about this object is it connects with
*  ideas and higher category theory. And in particular, it connects to some of the 20th century's most
*  abstract mathematics done by this chap growth and deke growth and deke had a thing called the
*  infinity group void, which is closely related to this ruley add object. Although the details the
*  relationship, you know, I don't fully understand yet. But I think that the what's what's interesting
*  is this thing that is sort of this very limiting object. So so okay, so a way to think about this
*  that that again, will will take us into another direction, which is the equivalence between
*  physics and mathematics. The way that well, let's see, maybe this is just just to give a sense of
*  this kind of group wide and things like that you can think about in mathematics, you can think you
*  have certain axioms, they're kind of like atoms. And you well, actually, let's say, let's talk about
*  mathematics for a second. So what is mathematics? What What is what is it made of, so to speak,
*  mathematics, there's a bunch of statements like, for addition, x plus y is equal to y plus x,
*  that's a statement of mathematics. Another statement will be, you know, x squared minus one
*  is equal to x plus one x minus one, there are infinite number of these possible statements of
*  mathematics. So it's not I mean, it's not just a guess a statement, but with x plus y, it's a rule
*  that you can, it's a I mean, it's a rule. It's a it is a rule. It's also just a thing that is true
*  in mathematics. Right. The statement of truth. Okay. Right. And and what you can imagine is you
*  you imagine just laying out this giant kind of ocean of all all statements. Well, actually,
*  you first start. Okay, this is where this was segueing into a different thing. Let me let me
*  not go in this direction for us. Let's not go to meta mathematics just yet. Yeah, we'll we'll maybe
*  get to meta mathematics, but but it's it's um, so let me not let me explain the groupoid and things
*  later. Yes. Yeah, but but so let's come back to the universe. Always a good place to be in. So
*  yeah, so what does the universe have to do with the really add the really all space and how that's
*  possible? We connected to why the thing exists at all and why there's just one of them. Yes. Okay,
*  so here's the point. So the thing that had confused me for a long time was, let's say we get
*  the rule for the universe, we hold it in our hand, we say this is our universe, then the immediate
*  question is, well, why isn't another one? And, you know, that's kind of the, you know, the the sort of
*  the lesson of Copernicus is we're not very special. So how come we got universe number 312 and not
*  universe quadrillion, quadrillion, quadrillion. And I think the resolution of that is the
*  realization that there that the universe is running all possible rules. So then you say, well,
*  how on earth do we perceive the universe to be running according to a particular rule? How do we
*  perceive definite things happening in the universe? Well, it's the same story. It's the observer,
*  there is a reference frame that we are picking in this rule, real space. And that that is what
*  determines our perception of the universe with our particular sensory information,
*  and so on. We are parsing the universe in this particular way. So here's the way to think about
*  it. In physical space, we live in a particular place in the universe. And, you know, we could
*  live in Alpha Centauri, but we don't, we live here. And similarly, in ruleial space, we could live in
*  many different places in ruleial space, but we happen to live here. And what does it mean to
*  live here? It means we have certain sensory input, we have certain ways to parse the universe.
*  Those are our interpretation of the universe. What would it mean to travel in ruleial space?
*  What it basically means is that we are successively interpreting the universe in different ways. So in
*  other words, to be at a different point in ruleial space is to have a different, in a sense,
*  a different interpretation of what's going on in the universe. And we can imagine even things like
*  an analog of the speed of light as the maximum speed of translation in ruleial space, and so on.
*  So wait, what's the interpretation? So ruleial space, and we, I'm confused by the we and the
*  interpretation and the universe. I thought moving about in ruleial space changes the way the universe
*  is, is the way we would perceive it. The way that-
*  So it ultimately has to do with the perception. So it doesn't, ruleial space is not somehow changing
*  like branching into another universe or something like that.
*  No, I mean, the whole point of this is the Ruliat is sort of the encapsulated version
*  of everything that is the universe running according to all possible rules.
*  We think of our universe, the observable universe, as its thing. So we're a little
*  bit loose with the word universe then, because wouldn't the Ruliat potentially encapsulate
*  a very large number, like combinatorially large, maybe infinite set of what we
*  human physicists think of as universes?
*  That's an interesting, interesting parsing of the word universe, right? Because what we're saying is
*  just as we're at a particular place in physical space, we're at a particular place in ruleial
*  space, at that particular place in ruleial space, our experience of the universe is this.
*  Yeah.
*  Just as if we lived at the center of the galaxy, our universe, our experience of the universe will
*  be different from the way it is given where we actually live. And so what we're saying is
*  what you might say, I mean, in a sense, this Ruliat is sort of a super universe, so to speak,
*  but it's all entangled together. It's not like you can separate out. You can say,
*  let me, it's like when we take a reference, okay, it's like our experience of the universe
*  is based on where we are in the universe. We could imagine moving to somewhere else in the
*  universe, but it's still the same universe.
*  So there's not like universes existing in parallel.
*  No. Because the whole point is that if we were able to change our interpretation of what's going on,
*  we could perceive a different reference frame in this Ruliat.
*  Yeah, but that's not, that's just, yeah, that's the same Ruliat. That's the same universe.
*  You're just moving about. These are just coordinates in the universe.
*  So the way that's the reason that's interesting is imagine the extraterrestrial intelligence.
*  So the alien intelligence, we should say the alien intelligence might live on Alpha Centauri,
*  but it might also live at a different place in real space.
*  It can live right here on earth. It just has a different reference frame that
*  includes a very different perception of the universe.
*  And then because that real space is very large, I mean,
*  Do we get to communicate with them? Right. That's-
*  Yeah. But it's also, well, one thing is how different the perception of the universe could be.
*  I think it could be bizarrely, unimaginably, completely different. And I mean, one thing to
*  realize is even in kind of things I don't understand well, I know about the kind of
*  Western tradition of understanding science and all that kind of thing. And you talk to
*  people who say, well, I'm really into some Eastern tradition of this, that, and the other.
*  And it's really obvious to me how things work. I don't understand it at all. But it is not obvious,
*  I think, with this kind of realization that there's these very different ways to interpret
*  what's going on in the universe. That kind of gives me at least, it doesn't help me to
*  understand that different interpretation, but it gives me at least more respect for the possibility
*  that there will be other interpretations. Yeah. It humbles you to the possibility that,
*  like, what is it? Reincarnation or all these, like, eternal recurrence with Nietzsche,
*  like, just these ideas. Yeah. Well, you know, the thing that I've realized about a bunch of those
*  things is that, you know, I've been sort of doing my little survey of the history of philosophy,
*  just trying to understand, you know, what can I actually say now about some of these things?
*  And you realize that some of these concepts, like the immortal soul concept, which, you know,
*  I remember when I was a kid and, you know, it was kind of lots of religion bashing type stuff
*  of people saying, you know, well, we know about physics, tell us how much does a soul weigh?
*  And people are like, well, how can it be a thing if it doesn't weigh anything? Well, now we
*  understand, you know, there is this notion of what's in brains that isn't the matter of brains,
*  and it's something computational. And there is a sense, and in fact, it is correct, that it is in
*  some sense, immortal, because this pattern of computation is something abstract that is not
*  specific to the particular material of a brain. Now, we don't know how to extract it, you know,
*  in our traditional scientific approach, but it's still something where it isn't a crazy thing to
*  say there is something doesn't weigh anything. That's a kind of a silly question. How much does
*  it weigh? Well, actually, maybe it isn't such a silly question in our model of physics, because
*  the actual computational activity has a consequence for gravity and things, but that's
*  a very subtle- Right. You can start talking about mass and energy and so on. There could be a,
*  what would you call it, a solitron. Yes, yes, yes. A particle that somehow contains soleness.
*  Yeah, right. Well, that's what, by the way, that's what Leibniz said. And, you know, one thing,
*  I've never understood this, you know, Leibniz had this idea of monads and monadology, and he had
*  this idea that what exists in the universe is this big collection of monads, and that the only
*  thing that one knows about the monads is sort of how they relate to each other. It sounds awfully
*  like hypergraphs, right? But Leibniz had really lost me at the following thing. He said, each of
*  these monads has a soul, and each of them has a consciousness. And it's like, okay, I'm out of
*  here. I don't understand this at all. I don't know what's going on. But I realized recently
*  that in his day, the concept that a thing could do something, could spontaneously do something,
*  that was his only way of describing that. And so what I would now say is, well, there's this
*  abstract rule that runs. To Leibniz, that would have been, you know, in 1690 or whatever, that
*  would have been kind of, well, it has a soul, it has a consciousness. And so, you know, in a sense,
*  it's like one of these, there's no new idea under the sun, so to speak. That's, you know,
*  that's a sort of a version of the same kinds of ideas, but couched in terms that are sort of
*  bizarrely different from the ones that we would use today. Would you be able to maybe play devil's
*  advocate on your conception of consciousness that, like the two characteristics of it that
*  is constrained and there's a single thread of time? Is it possible that Leibniz was onto something
*  that the basic atom, the screwy atom of space has a consciousness? Is that, so these are just words,
*  right? But what is there, is there some sense where consciousness is much more fundamental
*  than you're making it seem? I don't know. I mean, you know, I think-
*  Can you construct a world in which it is much more fundamental?
*  I think that, okay, so the question would be, is there a way to think about kind of,
*  if we sort of parse the universe down at the level of atoms of space or something, could we say,
*  well, so that's really a question of a different point of view, a different place in real space.
*  You're asking the question, could there be a civilization that exists, could there be sort of
*  conscious entities that exist at the level of atoms of space, and what would that be like?
*  And I think that comes back to this question of, can we, you know, what's it like to be a cellular
*  automaton type thing? I mean, it's, you know, I'm not yet there. I don't know. I mean, I think that
*  this is a, and I don't even know yet quite how to think about this in the sense that I was considering,
*  you know, I never write fiction, but I haven't written it since I was like 10 years old.
*  My fiction, I made one attempt, which I sent to some science fiction writer friends of mine,
*  and they told me it was terrible. So, but- This is a long time ago?
*  No, it was recently. Recently. And they said it was terrible.
*  That'd be interesting to see you write a short story based on what sounds like it's already
*  inspiring short stories by, or stories by science fiction writers. Yeah, right. But I think the
*  interesting thing for me is, you know, in the, what does it, what is it like to be a whatever?
*  Yeah. How do you describe that? I mean, it's like, that's not a thing that you describe in
*  mathematics, that what is it like to be such and such? Well, see, to me, when you say, what is it
*  like to be something presumes that you're talking about a singular entity. So, yeah, like there's a
*  some kind of feeling of the entity, the stuff that's inside of it and the stuff that's outside
*  of it. And then that's when consciousness starts making sense. But then it seems like that could be
*  generalizable. If you take some subset of a cellular automata, you could start talking about
*  what does that subset feel. But then you can, I think you could just take arbitrary numbers of
*  subsets. Like to me, like you and I individually are consciousnesses, but you could also say the
*  two of us together is a singular consciousness. Maybe, maybe. I'm not so sure about that. I think
*  that the single thread of time thing may be pretty important. And that as soon as you start saying,
*  there are two different threads of time, there are two different experiences. And then we have to say,
*  how do they relate? How are they sort of entangled with each other? I mean, that may be a different
*  story of a thing that isn't much like, you know, what are the ants? What's it like to be an ant?
*  You know, where there's a sort of more collective view of the world, so to speak. I don't know. I
*  think that, I mean, this is, you know, I don't really have a good, I mean, you know, my best
*  thought is, you know, can we turn it into a human story? It's like the question of, you know, when
*  we try and understand physics, can we turn that into something which is sort of a human understandable
*  narrative? And now what's it like to be a such and such? You know, maybe the only medium in which we
*  can describe that is something like fiction, where it's kind of like you're telling, you know, the
*  life story in that setting. But this is beyond what I've yet understood how to do.
*  Yeah, but it does seem so, like with human consciousness, you know, we're made up of cells
*  and like, there's a bunch of systems that are networked that work together that at this,
*  at the human level, feel like a singular consciousness when you take...
*  Yes.
*  And so maybe like an ant colony is just too low level. Sorry, an ant is too low level.
*  Right.
*  Maybe you have to look at the ant colony.
*  Yeah, I agree.
*  Like there's some level at which it's a conscious being. And then if you go to the planetary scale,
*  then maybe that's going too far. So there's a nice sweet spot.
*  Yeah, right.
*  For consciousness.
*  No, I mean, I agree. I think the difficulty is that, you know, okay, so in sort of people who
*  talk about consciousness, one of the terrible things I've realized, because I've now interacted
*  with some of this community, so to speak, some interesting people who do that kind of thinking.
*  But, you know, one of the things I was saying to one of the leading people in that area,
*  I was saying, you know, that, you know, it must be kind of frustrating because it's kind of like a
*  poetry story. That is many people are writing poems, but few people are reading them.
*  Yes.
*  So there are always these different, you know, everybody has their own theory of consciousness
*  and they are very non-inter sort of inter discussable. And by the way, I mean, you know,
*  my own approach to sort of the question of consciousness, as far as I'm concerned,
*  I'm an applied consciousness operative, so to speak, because I don't really, in a sense,
*  the thing I'm trying to get out of it is how does it help me to understand what's a possible
*  theory of physics? And how does it help me to say, how do I go from this incoherent collection of
*  things happening in the universe to our definite perception and definite laws and so on, and sort
*  of an applied version of consciousness? And I think the reason it sort of segues to a different
*  kind of topic, but the reason that one of the things I'm particularly interested in is kind of
*  what's the analog of consciousness in systems very different from brains? And so why does that matter?
*  Well, you know, this whole description of this kind of, you know, we haven't talked about why
*  the universe exists. So let's get to why the universe exists. And then we can talk about,
*  perhaps a little bit about what these models of physics kind of show you about other kinds of
*  things like molecular computing and so on. Yes, that's good. Why does the universe exist? Okay,
*  so we finally sort of more or less set the stage. We've got this idea of this rulliad, of this object
*  that is made from following all possible rules, the fact that it's sort of not just this incoherent
*  mess, it's got all this entangled structure in it, and so on. Okay, so what is this rulliad?
*  Well, it is the working out of all possible formal systems. So the sort of the question of why does
*  the universe exist? Its core question, we kind of started with is, you've got two plus two equals
*  four, you've got some other abstract results, but that's not actualized. It's just an abstract thing.
*  And when we say we've got a model for the universe, okay, it's this rule, you run it,
*  and it'll make the universe. But it's like, but where's it actually running? What is it actually
*  doing? Is it actual or is it merely a formal description of something? Okay, so the thing to
*  realize with this, the thing about the rulliad is it's an inevitable, it is the entangled running
*  of all possible rules. So you don't get to say it's not like you're saying, which rulliad are
*  you picking? Because it's all possible formal rules. It's not like it's just, you know, well,
*  actually, it's only footnote. The only footnote, it's an important footnote, is it's all possible
*  computational rules, not hyper computational rules. That is, it's running all the rules that would be
*  accessible to a Turing machine, but is not running all the rules that will be accessible to a thing
*  that can solve problems in finite time that would take a Turing machine infinite time to solve.
*  So you can, even Alan Turing knew this, that you could make oracles for Turing machines, where you
*  say a Turing machine can't solve the halting problem for Turing machines. It can't know what
*  will happen in any Turing machine after an infinite time in any finite time, but you could invent a
*  box, just make a black box, you say, I'm going to sell you an oracle that will just tell you,
*  you know, press this button, it'll tell you what the Turing machine will do after an infinite time.
*  You can imagine such a box. You can't necessarily build one in the physical universe, but you can
*  imagine such a box. And so we could say, well, in addition to so in this rulliad, we're imagining
*  that there is a computational that at the end, it's, it's running rules that are computational,
*  it doesn't have a bunch of oracle black boxes in it. You say, well, why not? Well, it turns out if
*  there are oracle black boxes, the rulliad that is you can make a sort of super rulliad that contains
*  those oracle black boxes, but it has a cosmological event horizon relative to the first one, they
*  can't communicate. In other words, you can, you can end up with what you end up happening. What
*  ends up happening is it's like in the physical universe, we in this causal graph that represents
*  the causal relationships of different things, you can have an event horizon, where there's where the
*  causal graph is disconnected, where the effect here an event happening here does not affect an
*  event happening here, because there's a disconnection in the causal graph. And that's what happens in
*  the event horizon. And so the what will happen between this kind of the ordinary rulliad,
*  and the hyper rulliad is there is an event horizon. And you know, we in our rulliad will
*  just never know that there is that they're just separate things, they're not they're not connected.
*  And maybe I'm not understanding, but just because we can't observe it.
*  Why does that mean it doesn't exist?
*  It might exist, but it does. It's not clear what it it's so what, so to speak, whether it exists.
*  You know, what we're trying to understand is why does our universe exist? We're not trying to ask
*  the question, what, you know, it's, let me say another thing, let me make a meta comment, okay,
*  which is that, that I have not thought through this hyper rulliad business properly. So I'm I'm I
*  can't the hyper rulliad is referring to a rulliad in which hyper computation is possible. That's
*  correct. Okay. So like what the footnote, the footnote to the footnote is, we're not sure why
*  this is important. Yeah, that's right. So let's let's ignore that. Okay. It's already abstract
*  enough. Okay. So, so okay, so the one question is, we have to say, if we're saying, why does
*  the universe exist? One question is, why is it this universe and not another universe? Yeah. Okay.
*  So the important point about this rulliad idea is that it's in the rulliad are all possible formal
*  systems. So there's no choice being made. There's no, there's no like, oh, we pick this particular
*  universe and not that one. That's the first thing. The second thing is the, that we have to ask the
*  question. So, so you say, why does two plus two equals four exists? That's not really a, that is
*  a thing that necessarily is that way, just on the basis of the meaning of the terms two and plus
*  and equals and so on. Right? So the thing is that this, this rulliad object is in a sense,
*  a necessary object. It is just the thing that is the consequence of working out the consequence
*  of the formal definition of things. You don't, it is not a thing where you're saying, and this is
*  picked as the particular thing. This is just something which necessarily is that thing because
*  of the definition of what it means to have computation. So it's a formal system. Yes.
*  But does it exist? Ah, well, where are we in this whole thing? We are part of this rulliad.
*  And so our, so there is no sense to say does two plus two equals four exist? Well, that's, that's
*  in some sense, it necessarily exists. It's a necessary object. It's not a thing that way you
*  can ask. You know, it's, it's usually in philosophy, there's a sort of distinction made between,
*  you know, necessary truths, contingent truths, analytic propositions, synthetic propositions,
*  there are a variety of different versions of this. There are things which are necessarily true
*  just based on the definition of terms. And there are things which happen to be true in our universe.
*  But we're, we don't exist in rullial space. We, that's one of the coordinates that define our
*  existence, right? Well, okay. So, so yes, yes. But this rulliad is the set of all possible
*  rullial coordinates. So what we're saying is, it contains that. So what we're saying is,
*  we exist as, okay, so our perception of what's going on is we're at a particular place in this
*  rulliad. And we are concluding certain things about how the universe works based on that.
*  But the question is, do we understand, you know, is there something where we say,
*  so, so why does it work that way? Well, the answer is, I think it has to work that way,
*  because this, there isn't, this rulliad is a necessary object, in the sense that it is a
*  purely formal object, just like two plus two equals four. It's not an object that was made
*  of something. It's an object that is just an expression of the necessary collection of formal
*  relations that exist. And so then the issue is, can we, in our experience of that, is it,
*  you know, can we have tables and chairs, so to speak, in that, just by virtue of our experience
*  of that necessary thing? And, you know, what people have generally thought, and honestly,
*  that I don't know of a lot of discussion of this, why does the universe exist question?
*  It's been a very, you know, I've been surprised actually at how little, I mean, I think it's one
*  of these things that's really kind of far out there, but the thing that, that is, you know,
*  the surprise here is that all possible formal rules, when you run them together, and that's
*  the critical thing, when you run them together, they produce this kind of entangled structure
*  that has a definite structure. It's not just, you know, a random arbitrary thing, it's a thing with
*  definite structure. And that structure is the thing, when we are embedded in that structure,
*  when anything, you know, an entity embedded in that structure perceives something, which is,
*  then we can interpret as physics and things like this. So in other words, we don't have to ask the
*  question, the, why does it exist? It necessarily exists. I'm missing this part. Why does it
*  necessarily exist? Okay. Okay. So like, you need to have it if you want to formalize the relation
*  between entities, but why did, why do you need to have relations?
*  Okay. Okay. So, so let's say you say, well,
*  it's like, why does math have to exist?
*  Okay. That's the question. Yeah. Okay. Fair question. Let's see. I think the thing to think
*  about is the existence of mathematics is something where, given a definition of terms,
*  what follows from that definition inevitably follows. So now you can say, why define any terms?
*  But in a sense, the, well, that's okay. So the definition of terms, I mean, I think the way to
*  think about this, let me see. So like concrete terms.
*  Well, they're not very concrete. I mean, they're just things like, you know,
*  logical or. Right. But that's a thing. That's a powerful thing.
*  Well, it's a, yes. Okay. But it's a, the point is that it is not a thing of a, you know,
*  people imagine there is, I don't know, the, you know, an elephant or something, or the, you know,
*  elephants are presumably not necessary objects. They are, they happen to exist as a result of
*  kind of biological evolution and whatever else. But the, the thing is that in some sense,
*  that there is, it is a different kind of thing to say, does plus exist? The, the, it is not,
*  it's not, not like an elephant. So a plus is, seems more fundamental,
*  more basic than an elephant. Yes. But you can imagine a world without
*  a plus or anything like it. Like why do formal things that are discreet that can be used
*  to reason have to exist or. Well, okay. So why, okay. So then the question is,
*  but the whole point is computation. We can certainly imagine computation. That is,
*  we can certainly say there is a formal system that we can construct abstractly in our minds
*  that is computation. And that, that's the, and you know, we can, we can imagine it.
*  Right. Now the question is, is it is that formal system, once we exist as observers embedded in
*  that formal system, that's enough to have something which is like our universe. And so then the, then
*  what you're kind of asking is perhaps is why, I mean, the point is we definitely can imagine it.
*  There's nothing that says that we're not saying that there's, it's sort of inevitable that, that
*  is a thing that we can imagine. We don't have to ask, does it exist? We're just, it is definitely
*  something we can imagine. Now that's, then we have this thing that is a formally constructable thing
*  that we can imagine. And now we have to ask the question what, you know, given that formally
*  constructable thing, what is, what consequences does that, if we were to perceive that formally,
*  if we were embedded in that formally constructable thing, what would we perceive about the world?
*  And we would say we perceive that the world exists because we are, we are seeing all of this
*  mechanism of all these things happening. And, but that's something that is just a feature of,
*  it's something where we are- See another way of asking this that I'm trying to get at,
*  I understand why it feels like this Ruliat is necessary, but maybe it's just me being human,
*  but it feels like then you should be able to, not us, but somehow step outside of the Ruliat.
*  Like what's outside the Ruliat? Well, the Ruliat is all formal systems, so there's nothing,
*  because- But that's what a human would say.
*  I know that's what a human would say, because we're used to the idea that there's, but the whole
*  point is that by the time it's all possible formal systems, it's like, it is all things you can
*  imagine, but- No, all computations you can imagine, but like we don't-
*  Well, so the issue is can we encode? Okay, so that's a fair question. Is it possible to encode
*  all, I mean, is there something that isn't what we can represent formally?
*  Right. That is, is there something that,
*  and that's, I think, related to the hyper Ruliat footnote, so to speak, of which I'm afraid that
*  one of the things sort of interesting about this is there has been some discussion of this in
*  theology and things like that, which I don't necessarily understand all of, but the key
*  new input is this idea that all possible formal systems, it's like if you make a world,
*  people say, well, you make a world in a particular way with particular rules, but no, you don't do
*  that. You can make a world that deals with all possible rules and then merely by virtue of living
*  in a particular place in that world, so to speak, we have the perception we have of what the world
*  is like. Now, I have to say, it's sort of interesting because I wrote this piece about this and
*  this philosophy stuff is not super easy and as I'm talking to you about it and I actually haven't,
*  people have been interested in lots of different things we've been doing, but this,
*  why does the universe exist, has been, I would say, one of the ones that you would think people
*  will be most interested in, but actually, I think they're just like, oh, that's just something
*  complicated. So I haven't explained it as much as I've explained a bunch of other things and I have
*  to say, I think I may be missing a couple of pieces of that argument that would be, so it's kind of like-
*  Well, your conscious being is computationally bounded, so you're missing-
*  Indeed.
*  Having written quite a few articles yourself, you're now missing some of the pieces.
*  Yes, right.
*  That's the limitation of being human.
*  Right. One of the consequences of this why the universe exists thing and this kind of concept of
*  Ruly ads and places in there representing our perception of the universe and so on,
*  one of the weird consequences is if the universe exists, mathematics must also exist.
*  That's a weird thing because mathematics, people have been very confused, including me,
*  have been very confused about the question of kind of what is the foundation of mathematics?
*  What kind of a thing is mathematics? Is mathematics something where we just write down axioms like
*  Euclid did for geometry and we just build the structure and we could have written down
*  different axioms and we'd have a different structure or is it something that has a more
*  fundamental sort of truth to it? I have to say, this is one of these cases where I've long believed
*  that mathematics has a great deal of arbitrariness to it, that there are particular axioms that kind
*  of got written down by the Babylonians and that's what we've ended up with the mathematics that we
*  have. I have to say, actually, my wife has been telling me for 25 years, she's a mathematician,
*  she's been telling me, you're wrong about the foundations of mathematics and I'm like, no, no,
*  no, I know what I'm talking about. Finally, she's much more right than I've been.
*  So, I mean, her sense and your sense, are we just, so this is to the question of
*  meta-mathematics, are we just kind of on a trajectory through
*  rule-y space except in mathematics, through a trajectory of certain kind of...
*  I think that's partly the idea. So, I think that the notion is this. So,
*  a hundred years ago, a little bit more than a hundred years ago, people have been doing
*  mathematics for ages, but then in the late 1800s, people decided to try and formalize mathematics
*  and say, you know, it is mathematics, we're going to break it down, we're going to make it like
*  logic, we're going to make it out of sort of fundamental primitives and that was people like
*  Freger and Piano and Hilbert and so on. And they kind of got this idea of let's do kind of Euclid,
*  but even better, let's just make everything just in terms of this sort of symbolic axioms
*  and then build up mathematics from that. And that, you know, they thought at the time,
*  as soon as they get these symbolic axioms, that they made the same mistake, the kind of computational
*  irreducibility mistake. They thought as soon as we've written down the axioms, then it'll just,
*  we'll just have a machine, kind of a super-mathematica, so to speak, that can just
*  grind out all true theorems of mathematics. That got exploited by Gödel's theorem, which is
*  basically the story of computational irreducibility. It's that even though you know those underlying
*  rules, you can't deduce all the consequences in any finite way. And so, that was, but now the
*  question is, okay, so they broke mathematics down into these axioms and they say, now you build up
*  from that. So, what I'm increasingly coming to realize is that's similar to saying, let's take
*  a gas and break it down into molecules. There's gas laws that are the large scale structure and so
*  on that we humans are familiar with, and then there's the underlying molecular dynamics.
*  And I think that the axiomatic level of mathematics, which we can access with automated
*  theorem proving and proof assistance and these kinds of things, that's the molecular dynamics of
*  mathematics. And occasionally we see through to that molecular dynamics. We see undecidability,
*  we see other things like this. One of the things I've always found very mysterious is that Gödel's
*  theorem shows that there are sort of things which cannot be finitely proved in mathematics. There
*  are proofs of arbitrary length, infinite length proofs that you might need. But in practical
*  mathematics, mathematicians don't typically run into this. They just happily go along doing their
*  mathematics. And I think what's actually happening is that what they're doing is they're looking at
*  this. They are essentially observers in meta-mathematical space and they are
*  picking a reference frame in meta-mathematical space and they are computationally bounded
*  observers of meta-mathematical space, which is causing them to deduce that the laws of
*  meta-mathematics and the laws of mathematics, like the laws of fluid mechanics, are much more
*  understandable than this underlying molecular dynamics. And so what gets really bizarre is
*  thinking about kind of the analogy between meta-mathematics, this idea of you exist in this
*  kind of, in this sort of space of possible, in this kind of mathematical space where the individual
*  kind of points in the mathematical space are statements in mathematics and they're connected
*  by proofs where one statement, you know, you take a couple of different statements, you can use those
*  to prove some other statement and you've got this whole network of proofs. That's the kind of causal
*  network of mathematics, of what can prove what and so on. And you can say at any moment in the
*  history of a mathematician, of a single mathematical consciousness, you are in a single kind of slice
*  of this kind of meta-mathematical space. You know a certain set of mathematical statements.
*  You can then deduce with proofs, you can deduce other ones and so on. You're kind of gradually
*  moving through meta-mathematical space. And so it's kind of the view is that the reason that
*  mathematicians perceive mathematics to have the sort of integrity and lack of kind of undecidability
*  and so on that they do is because they, like we as observers of the physical universe, we have these
*  limitations associated with computational boundedness, single thread of time, consciousness
*  limitations basically. That the same thing is true of mathematicians perceiving sort of
*  meta-mathematical space. And so what's happening is that when you look at, if you look at one of
*  these formalized mathematics systems, something like, you know, Pythagoras' theorem, it'll be,
*  it'll take, oh I don't know, what is it, maybe 10,000 individual little steps to prove Pythagoras'
*  theorem. And one of the bizarre things that's sort of an empirical fact that I'm trying to understand
*  a little bit better, if you look at different proof, if you look at different formalized
*  mathematics systems, they actually have different axioms underneath that they can all prove Pythagoras'
*  theorem. And so in other words, it's a little bit like what happens with gases. We can have air
*  molecules, we can have water molecules, but they still have fluid dynamics. Both of them have fluid
*  dynamics. And so similarly at the level that mathematics, that mathematicians care about
*  mathematics, it's way above the molecular dynamics, so to speak. And there are all kinds of weird
*  things like, for example, one thing I was realizing recently is the quantum theory of
*  mathematics. That's a very bizarre idea. But basically when you prove what is, you know,
*  a proof is you've got one statement in mathematics, you go through other statements, you eventually
*  get to a statement you're trying to prove, for example. That's a path in metamathematical space.
*  And that's a single path. A single proof is a single path. But you can imagine there are
*  other proofs of the same result. There are a bundle of proofs. There's this whole set of
*  possible proofs. You could think of it as branching similar to the quantum mechanics model that you
*  were talking about. Exactly. And so there's some invariance that you can formalize in the same way
*  that you can for the quantum mechanical. Right. So the question is in proof space, you know,
*  as you start thinking about multiple proofs, are there analogs of, for example, destructive
*  interference of multiple proofs? So here's a bizarre idea that's just a couple of days old,
*  so not yet fully formed. But as you try and do that, when you have two different proofs,
*  it's like two photons going in different directions, you have two proofs which at an
*  intermediate stage are incompatible. And that's kind of like destructive interference.
*  Is it possible for this to instruct the engineering of automated proof systems?
*  Absolutely. I mean, as a practical matter, I mean, you know, this whole question, in fact,
*  Jonathan Gorard has a nice heuristic for automated theorem provers that's based on our physics
*  project that is looking for essentially using kind of using energy and in our models, energy
*  is kind of level of activity in this hypergraph. And so there's sort of a heuristic for automated
*  theorem proving about how do you pick which path to go down that is based on essentially physics.
*  And I mean, the thing that gets interesting about this is, is the way that one could sort of have
*  the interplay between like, for example, a black hole, what is a black hole in mathematics?
*  So the answer is, what is black hole in physics? A black hole in physics is where in the simplest
*  form of black hole time ends. That is all, you know, everything is crunched down to the space
*  time singularity, and everything just ends up at that singularity. So in our models, and that's a
*  little hard to understand in general relativity with continuous mathematics, and what does
*  singularity look like? In our models, it's something very pragmatic. It's just, you're
*  applying these rules, time is moving forward. And then there comes a moment where the rules,
*  no rules apply. So time stops, it's kind of like the universe dies, that, you know, that nothing
*  happens in the universe anymore. Well, in mathematics, that's a decidable theory. That's
*  a theory. So theories which have undecidability, which are things like arithmetic, set theory,
*  all the serious models, theories in mathematics, they all have the feature that there are proofs
*  of arbitrarily long length. In something like Boolean algebra, which is a decidable theory,
*  there are, you know, any question in Boolean algebra, you can just go crunch, crunch, crunch,
*  and in a known number of steps, you can answer it. You know, satisfiability, you know, might be hard,
*  but it's still a bounded number of steps to answer any satisfiability problem. And so that's the
*  notion of a black hole in physics where time stops. That's analogous to in mathematics,
*  where there aren't infinite length proofs. Where when in physics, you know, you can wander around
*  the universe forever if you don't run into a black hole. If you run into a black hole and time
*  stops, you're done. And it's the same thing in mathematics between decidable theories and
*  undecidable theories. That's an example. And I think we're sort of the attempt to understand.
*  So another question is kind of what is the general relativity of meta mathematics? What is the bulk
*  theory of meta mathematics? So in the literature of mathematics, there are about three million
*  theorems that people have published. And those represent, it's kind of on this, it's like,
*  like on the earth, we would be, you know, you know, we've put cities in particular places on the
*  earth, but yet there is ultimately, you know, we know the earth is roughly spherical, and there's
*  an underlying space. And we could just talk about, you know, the world of space in terms of where our
*  cities happen to be, but there's actually an underlying space. And so the question is, what's
*  that for meta mathematics? And as we kind of explore what is, for example, for mathematics,
*  which is always likes taking sort of abstract limits. So an obvious abstract limit for mathematics
*  to take is the limit of the future of mathematics. That is, what will be, you know, the ultimate
*  structure of mathematics. And one of the things that's an empirical observation about mathematics,
*  that's quite interesting is that a lot of theories in one area of mathematics, algebraic,
*  geometry or something might have, they play into another area of mathematics, that that same,
*  the same kind of fundamental construct seem to occur in very different areas of mathematics.
*  And that's structurally captured a bit with category theory and things like that. But I think
*  that there's probably an understanding of this meta mathematical space that will explain why
*  different areas of mathematics ultimately sort of map into the same thing. And I mean, you know,
*  my little challenge to myself is what's time dilation in, in meta mathematics. In other words,
*  as you as you basically as you move around in this mathematical space of possible statements,
*  you know, what's how does that moving around, it's basically what's happening is that as you
*  move around in the space of mathematical statements, it's like you're changing from algebra
*  to geometry to whatever else. And you're trying to prove the same theorem. But as you try, if you
*  keep on moving to these different places, it's slower to prove that theorem because you keep on
*  having to translate what you're doing back to where you started from. And that's kind of the
*  beginnings of the analog of time dilation in mathematics. Plus, there's probably fractional
*  dimensions in this space as well. Oh, this space is a very messy space. This space is much messier
*  than physical space. I mean, even in even in the models of physics, physical space is very tame
*  compared to branchial space and rural space. I mean, the mathematical structure, you know,
*  branchial space, probably more like Hilbert space, but it's a rather complicated Hilbert space.
*  And rural space is more like this weird infinity groupoid story of growth and deacon. And you know,
*  I can explain that a little bit because in you know, in in meta mathematical space, a path in
*  medical space is a is a path between two statements is a way to get by proofs is to way to find a
*  proof that goes from one statement to another. And so one of the things you can do you can think
*  about is you've got between statements, you've got proofs, they are paths between statements.
*  Okay, so now you can go to the next level, and you can ask, what about a mapping from one proof to
*  another. And so that's in category theory, that's kind of a higher category, notion of higher
*  categories where you're where you're mapping not just between not just between objects, but you're
*  mapping between the mappings between objects and so on. And so you can keep doing that you keep
*  saying higher order proofs, I want mappings between proofs between proofs and so on. And that limiting
*  structure, oh, by the way, one thing that's very interesting is, imagine in proof space, you've got
*  these two proofs. And the question is, what is the topology of proof space? In other words, if you
*  take these two paths, can you continuously deform them into each other? Or is there some big hole in
*  the middle that prevents you from continuously deforming them one into the other? It's kind of
*  like, you know, when you when you think about some I don't know, some puzzle, for example, you're
*  moving pieces around on some puzzle, and you can think about the space of possible states of the
*  puzzle. And you can make this graph that shows from one state of the puzzle to another state of the
*  puzzle, and so on. And sometimes you can easily get from one state to any other state. But sometimes
*  there'll be a hole in that space. And there'll be you know, you always have to go around the securitas
*  route to get from here to there, there won't be any direct way. That's kind of a question of,
*  of whether there's sort of an obstruction in the space. And so the question is, in proof space,
*  what is the what are you know, what does it mean if there's an obstruction in proof space?
*  Yeah, I don't even know what an obstruction means in proof space, because for it to be an obstruction,
*  it should be reachable some other way from some other place. Right? So this is like an unreachable
*  part of the graph. No, it's not just an unreachable part. It's a part where there are
*  paths that go one way, there are paths that go the other way. And this question of homotopy in
*  mathematics is this question, can you continuously deform, you know, from one path to another path?
*  Or do you have to go in a jump, so to speak? So it's like if you're going around a sphere,
*  for example, if you're going around this, I don't know, a cylinder or something, you can wind around
*  one way. And you can, there's no could there paths where you can, where you can easily deform one path
*  into another because it's just sort of sitting on the same side of the cylinder. But when you've got
*  something that winds all the way around a cylinder, you can't continuously deform that down to a point
*  because it's it's stuck wrapped around. My intuition about proof space is you should be able to deform
*  it. I mean, that because then otherwise, it doesn't even make sense. Because if the topology matters
*  of the way you move about the space that I don't even know what that means. Well, what it would
*  mean is that you would have one way of doing a proof of something over here in algebra,
*  and another way of doing a proof of something over here in geometry. And there would not be
*  an intermediate way to map between those proofs. How would that be possible if they start at the
*  same place and end at the same place? Well, it's the same thing as you know, we've got points on a,
*  you know, if we've got paths on a cylinder. Now I understand how it works in physical space,
*  but it just doesn't. It feels like proof space shouldn't have that. Okay, I mean, I'm not sure.
*  I don't know. We'll know very soon because we get to do some experiments. This is the great thing
*  about this stuff is that in fact, you know, in the next few days, I hope to do a bunch of
*  experiments on this. So you're playing with like proofs in this kind of space. Yes. Yes. I mean,
*  so you know, this is toy, you know, theories, and you know, we've got good so this kind of segues to
*  perhaps another thing, which is this whole idea of multi computation. So this is another kind of
*  bigger idea that so, okay, this has to do with how do you make models of things? And it's going
*  to it's some so I've sort of claimed that they've been sort of four epochs in the history of making
*  models of things. And, and this multi computation thing is the fourth is a new epoch. What are the
*  first three? The first one is, is back in antiquity, ancient Greek times, people were like,
*  what's the universe made of? Oh, it's made of, you know, everything is water, Thales, you know,
*  or everything is made of atoms. It's sort of what are things made of? Or the you know, there are
*  these crystal spheres that represent where the planets are, and so on. It's like a structural
*  idea of how the universe is constructed. There's no real notion of dynamics is just what is the
*  universe? How is the universe made? Then we get to the 1600s. And we get to the sort of revolution
*  of mathematics being introduced into physics. And then we have this kind of idea of you write
*  down some equation, the what happens in the universe is the solving of that equation,
*  time enters, but it's usually just a parameter, we just can, you know, sort of slide it back and
*  forth and say, here's, here's where it is. Okay, then we come to this kind of computational idea
*  that I kind of started really pushing in the in the 19 early 1980s. As a result, you know,
*  the things we were talking about before about complexity, that was my motivation. But the
*  biggest story was the story of kind of computational models of things. And the big difference there
*  from the mathematical models is mathematical models, there's an equation, you solve it,
*  you got kind of slide time to the place where you want it. In computational models, you give the rule,
*  and then you just say, go run the rule. And time is not something you get to slide. Time is something
*  where it just you run the rule, time goes in steps. And that's how you work out what how the
*  system behaves, you don't time is not just a parameter. Time is something that is about the
*  running of these of these rules. And so there's this computational irreducibility, you can't jump
*  ahead in time. But there's still important thing is there's still one thread of time, it's still
*  the case, you know, the cellular automaton state, then it has the next state and the next state and
*  so on. The thing that is kind of we've sort of tipped off by quantum mechanics, in a sense,
*  although it it actually feeds back even into relativity and things like that, that there's
*  these multiple threads of time. And so in this multi computation paradigm, the kind of idea is,
*  instead of there being the single thread of time, there are these kind of distributed asynchronous
*  threads of time that are happening. And the thing that's sort of different there is, if you want to
*  know what happened, if you say what happened in the system, in the case of the computational
*  paradigm, you just say, well, after 1000 steps, we got this result. Right. But in the multi
*  computational paradigm, after 1000 steps, not even clear what 1000 steps means, because you've got
*  all these different threads of time, but there is no state, there's all these different possible,
*  you know, there's all these different pods. And so the only way you can know what happened is to
*  have some kind of observer who is saying, here's how to parse the results of what was going on.
*  Right. But that observer is embedded, and they don't have a complete picture. So
*  in the case of physics, that's right. Yes. And then in the but that's, but so the idea is that
*  in this multi computation setup, that it's this idea of these multiple threads of time, and models
*  that are based on that. And this is similar to what people think about in non deterministic
*  computation. So you have a Turing machine, usually it has a definite state, it follows
*  another state follows another state. But typically, what people have done when they've thought about
*  these kinds of things, is they've said, well, there are all these possible pods, and non
*  deterministic Turing machine can follow all these possible pods. But we just want one of them, we
*  just want the one that's the winner, that factors the number or whatever else. And similarly, it's
*  the same story in logic programming, and so on. But we say we've got this goal, find us a path to
*  that goal. I just want one path, then I'm happy. Or theorem proving, same story, I just want one
*  proof and then I'm happy. What's happening in multi computation in physics, is we actually care
*  about many pods. And well, there is a case, for example, probabilistic programming is a version
*  of multi computation in which you're looking at all the pods, you're just asking for probabilities
*  of things. But in a sense, in physics, we're taking different kinds of samplings. For example,
*  in quantum mechanics, we're taking a different kind of sampling of all these multiple pods.
*  But the thing that is notable is that when you are an observer embedded in this thing, etc., etc.,
*  with various other sort of footnotes and so on, it is inevitable that the thing that you parse out
*  of the system looks like general relativity and quantum mechanics. In other words, that just by
*  the very structure of this multi computational setup, it inevitably is the case that you have
*  certain emergent laws. Now, why is this perhaps not surprising in thermodynamics and statistical
*  mechanics, there are sort of inevitable emergent laws of sort of gas dynamics that are independent
*  of the details of molecular dynamics, sort of the same kind of thing. But I think what happens is,
*  what's a sort of a funny thing that I've just been understanding very recently is when I kind
*  of introduced this whole sort of computational paradigm complexity-ish thing back in the 80s,
*  it was kind of like a big downer because it's like there's a lot of stuff you can't say about
*  what systems will do. And then what I realized is, and then you might say, now we've got
*  multi computation, it's even worse. It isn't just one thread of time that we can't explain,
*  it's all these threads of time, we can't explain anything. But the following thing happens.
*  Because there is all this irreducibility, and any detailed thing you might want to answer,
*  it's very hard to answer. But when you have an observer who has certain characteristics,
*  like computational boundedness, sequentiality of time, and so on, that observer only samples
*  certain aspects of this incredible complexity going on in this multi computational system.
*  And that observer is sensitive only to some underlying core structure of this multi
*  computational system. There is all this irreducible computation going on, all these details,
*  but to that kind of observer, what's important is only the core structure of multi computation,
*  which means that observer observes comparatively simple laws. And I think it is inevitable that
*  that observer observes laws which are mathematically structured like general relativity and quantum
*  mechanics, which by the way are the same law in our model of physics.
*  So that's an explanation why there's simple laws that explain a lot for this observer.
*  Potentially, yes. But what the place where this gets really interesting is there are all these
*  fields of science where people have kind of gotten stuck, where they say we'd really love to have a
*  physics like theory of economics. We'd really love to have a physics like law and linguistics.
*  We got to talk about molecular biology here. Okay. So where does multi computation come in
*  for biology? Economics is super interesting too, but biology.
*  Okay. Let's talk about that. So let's talk about chemistry for a second. Okay. So I mean, I have
*  to say, you know, this is such a weird business for me because, you know, there are these kind of
*  paradigmatic ideas and then the actual applications. And it's like I've always said, I know nothing
*  about chemistry. I learned all the chemistry I know, you know, the night before some exam when I was
*  14 years old. But I've actually learned a bunch more chemistry. And in Wolfram language these days,
*  we have really pretty nice symbolic representation of chemistry. And in understanding the design of
*  that, I've actually, I think learned a certain amount of chemistry. Though if you quizzed me
*  on sort of basic high school chemistry, I would probably totally fail. But, okay. So what is
*  chemistry? I mean, chemistry is sort of a story of, you know, chemical reactions are like you've got
*  this particular chemical that's represented as some graph of, you know, these are this configuration
*  of molecules with these bonds and so on. And a chemical reaction happens. You've got these sort
*  of two graphs, they interact in some way, you get another graph or multiple other graphs out. So
*  that's kind of the sort of the abstract view of what's happening in chemistry. And so when you do
*  a chemical synthesis, for example, you are given certain sort of these are possible reactions that
*  can happen. And you're asked, can you piece together this a sequence of such reactions,
*  a sequence of such sort of axiomatic reactions, usually called name reactions in chemistry,
*  can you piece together a sequence of these reactions so that you get out at the end
*  this great molecule we were trying to synthesize. And so that's a story very much like theorem
*  proving. And people have done, actually, they started in the 1960s looking at kind of the
*  theorem proving approach to that, although it didn't really, it didn't, it didn't, it was sort
*  of done too early, I think. But anyway, so that's kind of the view is that that chemistry, chemical
*  reactions are the story of, of all these different sort of paths of possible things that go on.
*  Okay, let's let's go to an even lower level. Let's say, instead of asking about which species of
*  molecules we're talking about, let's look at individual molecules. And let's say we're looking
*  at individual molecules, and they are having chemical reactions. And we're building up this
*  big graph of all these reactions that are happening. Okay, so so then we've got this big graph. And by
*  the way, that big graph is incredibly similar to this hypergraph rewriting things. In fact,
*  in the underlying theory of multi computation, there are these things we call token event graphs,
*  which are basically, you've broken your state into tokens, like in the case of a hypergraph,
*  you've broken it into hyper edges, and each event is just consuming some number of tokens
*  and producing some number of tokens. But then you have to there's a lot of work to be done on
*  update rules. In terms of what they actually offer chemistry? Yeah, what they offer are observed
*  chemistry. Yes, indeed. Yes, indeed. And we've been working on that, actually, because we have
*  this beautiful system in Wolfram language for representing chemistry symbolically. So we actually
*  have, you know, this is a this is an ongoing thing to actually figure out what they are for some
*  practical cases. Does that require human injection? Or can it be automatically discovered? These update
*  rules? Well, if we can be better chemistry, we could probably discover them automatically. But I
*  think in reality, right now, it's like there are these particular reactions. And really,
*  to understand what's going on, we're probably going to pick a particular subtype of chemistry.
*  And just because because let me explain where this is going, the place that here's here's where this
*  is going. So got this whole network of all these molecules, having all these reactions and so on.
*  And this is some whole multi computational story, because each each sort of chemical reaction event
*  is its own separate event, we're saying they all happen asynchronously, we're not describing
*  in what order they happen. You know, maybe that order is governed by some quantum mechanics thing
*  doesn't really matter. We're just saying they happen in some order. And then we ask, what is
*  the what's the you know, how do we think about the system? Well, this thing is some kind of big
*  multi computational system. The question is, what is the chemical observer? And one possible chemical
*  observer is, all you care about is did you make that particular drug molecule? You're just asking,
*  you know, the for the one path. Another thing you might care about is, I want to know the
*  concentration of each species, right? I want to know, you know, at every stage, I'm going to solve
*  the differential equations that represent the concentrations. And I want to know what those all
*  are. But there's more. Because when it's kind of like, you're going below in statistical mechanics,
*  there's kind of all these molecules bouncing around. And you might say, we're just going to
*  ignore we're just going to look at the aggregate densities of certain kinds of molecules. But you
*  can look at a lower level, you can look at this whole graph of possible interactions. And so the
*  kind of the idea would be what, you know, is the only chemical observer, one who just cares about
*  overall concentrations? Or can there be a chemical observer who cares about this network of what
*  happened? And so that the question then is, so let me give an analogy. So this is where I think
*  this is potentially very relevant to molecular molecular biology and molecular computing.
*  When we think about a computation, usually, we say it's input, it's output, we, you know,
*  or chemistry, we say there's this input, we're going to make this molecule is the output.
*  But what if what we actually encode, what if our computation, what are the thing we care about
*  is some part of this dynamic network? What if it isn't just the input and the output that we care
*  about? What if there's some dynamics of the network that we care about? Now,
*  imagine you're a chemical observer. What is a chemical observer? Well, in molecular biology,
*  there are all kinds of weird sorts of observers, there are membranes that exist that have, you
*  know, different kinds of molecules that combine to them, things like this. It's not obvious that the
*  from a human scale, we just measure the concentration of something is the relevant story.
*  We can imagine that, for example, when we look at this whole network of possible reactions,
*  we can imagine, you know, at a physical level, we can imagine, well, what was the actual momentum
*  direction of that of that molecule? What was it which we don't pay any attention to when we're
*  just talking about chemical concentrations? What was the orientation of that molecule?
*  These kinds of things. And so here's the here's the place where I'm I have a little suspicion.
*  Okay. So one of the questions in biology is what matters in biology. And that is, you know, we have
*  all these chemical reactions, we have all these all these molecular processes going on in, you know,
*  in biological systems, what matters? And, you know, one of the things is to be able to tell what
*  matters well, so a big story of the what matters question was what happened in genetics in 1953,
*  when DNA, when it was figured out how DNA worked. Because before that time, you know, genetics have
*  been all these different effects and complicated things. And then it was realized, ah, there's
*  something new, a molecule can store information, which wasn't obvious before that time, a single
*  molecule can store information. So there's a place where there can be something important
*  that's happening in molecular biology. And it's just in the sequence that storing information in
*  a molecule. So the possibility now is imagine this dynamic network, this, you know, causal graphs and
*  multi-way causal graphs, and so on, that represent all of these different reactions between molecules.
*  What if there is some aspect of that, that is storing information that's relevant for
*  molecular biology. In the dynamic aspect of that? Yes, that's right. So it's similar to how the
*  structure of a DNA molecule stores information, it could be the dynamics of the system somehow
*  stores information. And this kind of process might allow you to give predictions of what that
*  would be. Well, yes, but also imagine that you're trying to do, for example, imagine you're trying
*  to do molecular computation. Okay, you might think the way we're going to do molecular computation is
*  we're just going to run the thing, we're going to see what came out, we're going to see what molecule
*  came out. This is saying that's not the only thing you can do. There is a different kind of chemical
*  observer that you can imagine constructing, which is somehow sensitive to this dynamic network,
*  exactly how that works, how we make that measurement, I don't know, but I have a few ideas,
*  but that's what's important, so to speak. And that means, and by the way, you can do the same
*  thing even for Turing machines. You can say if you have a multi-way Turing machine, you can say,
*  how do you compute with a multi-way Turing machine? You can't say, well, we've got this input and this
*  output, because the thing has all these threads of time, it's got lots of outputs. And so then you say,
*  well, what does it even mean to be a universal multi-way Turing machine? I don't fully know the
*  answer to that. It's an interesting idea, it would freak Turing out for sure, because then
*  the dynamics of the trajectory of the computation matters. Yes, yes. I mean, but the thing is that
*  this is again a story of what's the observer, so to speak, in chemistry, what's the observer there?
*  Now, to give an example of where that might matter, a very present day example is in immunology,
*  where we have whatever it is, 10 billion different kinds of antibodies that are all these
*  different shapes and so on. We have a trillion different kinds of T cell receptors that we
*  produce. And the traditional theory of immunology is this clonal selection theory where we are
*  constantly producing, randomly producing all these different antibodies, and as soon as one of them
*  binds to an antigen, then that one gets amplified and we produce more of that antibody and so on.
*  Back in the 1960s, an immunologist called Niels Jörner, who was the guy who invented
*  monoclonal antibodies, various other things, kind of had this network theory of the immune system,
*  where it would be like, well, we produce antibodies, but then we produce antibodies
*  to the antibodies, anti-antibodies, and we produce anti-anti-antibodies, and we get this whole dynamic
*  network of interactions between different immune system cells. And that was kind of a qualitative
*  theory at that time. And I've been a little disappointed because I've been studying immunology
*  a bit recently. And I knew something about this like 35 years ago or something. And I knew,
*  you know, I'd read a bunch of the books and I'd talked to a bunch of the people and so on. And
*  it was like an emerging theoretical immunology world. And then I look at the books now and they're
*  very thick because they've got, you know, there's just a ton known about immunology and, you know,
*  all these different pathways, all these different details and so on. But the theoretical sections
*  seem to have shrunk. And so the question is, what, you know, for example, immune memory,
*  where does the immune memory reside? Is it actually some cell sitting in our bone marrow
*  that is, you know, living for the whole of our lives that's going to spring into action
*  as soon as we're shown the same antigen? Or is it something different from that? Is it something
*  more dynamic? Is it something more like some network of interactions between these different
*  kinds of immune system cells and so on? And it's known that there are plenty of interactions between
*  T cells and, you know, there's plenty of dynamics. But what the consequence of that dynamics is,
*  is not clear. And to have a qualitative theory for that doesn't seem to exist. In fact, I was
*  just been trying to study this. So I'm quite incomplete in my study of these things, but I
*  was a little bit taken aback because I've been looking at these things. And it's like, and then
*  they get to the end where they have the most advanced theory that they've got. And it turns
*  out it's a cellular automaton theory. It's like, okay, well, at least I understand that theory.
*  Yeah. But, you know, I think that the possibility is that in, this is a place where if you want to
*  explain roughly how the immune system works, it ends up being this dynamic network. And then the
*  immune consciousness, so to speak, the observer ends up being something that, you know, in the end,
*  it's kind of like, does the human get sick or whatever? But it's something which is a complicated
*  story that relates to this whole sort of dynamic network and so on. And I think that's another
*  place where this kind of notion of, where I think multi-computation has the possibility.
*  See, one of the things, okay, you can end up with something where, yes, there is a general
*  relativity in there. But it turns out, but it may turn out that the observer who sees general
*  relativity in the immune system is an observer that's irrelevant to what we care about the
*  immune system. I mean, it could be, yes, there is some effect where, you know, there's some,
*  you know, time dilation of T cells interacting with whatever, but it's like, that's an effect
*  that's just irrelevant. And the thing we actually care about is things about, you know, what happens
*  when you have a vaccine that goes into some place in shape space and, you know, how does that affect
*  other places in shape space and how does that spread? You know, what's the analog of the speed
*  of light in shape space, for example? That's an important issue. If you have one of these dynamic
*  theories, it's like, you know, you're poking to shape space by having, you know, let's say,
*  a vaccine or something that has a particular configuration in shape space. How quickly as
*  this dynamic network spreads out, how quickly do you get sort of other antibodies in different
*  places in shape space, things like that. When you say shape space, you mean the shape of the
*  molecules? And then, so this is like, could be deeply connected to the protein and multi-protein
*  folding, all of that kind of stuff. So be able to say something interesting about the dance of
*  proteins that then actually has an impact on helping develop drugs, for example, or has an
*  impact on virology, immunology of how people do it. Well, I think the big thing is, you know,
*  when we think about molecular biology, what is the qualitative way to think about it?
*  You know, in other words, is it chemical reaction networks? Is it, you know, genetics, you know,
*  DNA, big news? It's kind of, there's a digital aspect to the whole thing. You know, what is
*  the qualitative way to think about how things work in biology? You know, when we think about,
*  I don't know, some phenomenon like aging or something, which is a big complicated phenomenon,
*  which just seems to have all these different tentacles. Is it really the case that that can
*  be thought about in some, you know, without DNA, when people were describing, you know, genetic
*  phenomena, there were, you know, dominant, recessive, this, that and the other, it got very,
*  very complicated. And then people realized, oh, it's just, you know, and what is a gene and so on,
*  and so on, and so on. Then people realize it's just base pairs. And there's this digital
*  representation. And so the question is, what is the overarching representation that we can now
*  start to think about using a molecular biology? I don't know how this will work out. And this is,
*  again, one of these things where, and the place where that gets important is, you know, maybe
*  molecular biology is doing molecular computing by using some dynamic process. That is something where
*  it is very happily saying, oh, I just got a result. It's in the dynamic structure of this network. Now
*  I'm going to go and do some other thing based on that result, for example. But we're like, oh,
*  I don't know what's going on. You know, it's just, we just measured the levels of these chemicals
*  and we couldn't conclude anything, but it just, we're looking at the wrong thing. And so that's the,
*  that's kind of the potential there. And it's, I mean, these things are, I don't know, it's for me,
*  it's like, I've not really, that was not a view. I mean, I've thought about molecular computing for
*  ages and ages and ages. And I've always imagined that the big story is kind of the original promise
*  of nanotechnology of like, can we make a molecular scale constructor that will just build a molecule
*  in any shape? I don't think I'm now increasingly concluding that's not the big point. The big point
*  is something more dynamic. That will be an interesting end point for any of these things,
*  but that's perhaps not the thing, you know, because the one example we have in molecular computing
*  that's really working is us biological organisms. And, you know, maybe the thing that's important
*  there is not this, you know, what chemicals do you make, so to speak, but more this kind of
*  dynamic process. The dynamic process, and then you can have a good model like the hypograft to then
*  explore, what, like simulate, again, make predictions. And if they- I think just have a way to reason
*  about biology. I mean, it's hard, you know, but first of all, biology doesn't have theories like
*  physics. You know, physics is a much more successful sort of global theory kind of area.
*  You know, biology, what are the global theories of biology? Pretty much Darwinian evolution. That's
*  the only global theory of biology. You know, any other theory is just a, well, the kidneys work
*  this way, this thing works this way, and so on. There isn't, I suppose, another global theory is
*  digital information in DNA. That's another sort of global fact about biology. But the difficult
*  thing to do is to match something you have a model of in the hypograft to the actual- like,
*  how do you discover the theory? How do you discover the theory? Okay, you have something that looks
*  nice and makes sense, but like, you have to match it to validation and experiment. And that's tricky
*  because you're walking around in the dark. Not entirely. I mean, so, you know, for example,
*  in what we've been trying to think about is take actual chemical reactions, okay? So, you know,
*  one of my goals is can I compute the primes with molecules? Okay, that's- if I can do that,
*  then I kind of- maybe I can compute things. And, you know, there's this nice automated lab,
*  these guys, this Emerald Cloud lab people have built with Wolfram Language and so on,
*  that's an actual physical lab, and you send it a piece of Wolfram Language code, and it goes and,
*  you know, actually does physical experiments. And so, one of my goals, because I'm not a test tube
*  kind of guy, I'm more of a software kind of person, is can I make something where, you know,
*  in this automated lab, we can actually get it so that there's some gel that we made and, you know,
*  the positions of the stripes are the primes. Is the primes. I love it. Yeah. I mean, that would be-
*  that would be an example of where- and that would be with a particular, you know, framework for
*  actually doing the molecular computing, you know, with particular kinds of molecules. And there's a
*  lot of kind of ambient technological mess, so to speak, associated with, oh, is it carbon? Is it
*  this? Is it that? You know, is it important that there's a bromine atom here? Et cetera, et cetera,
*  et cetera. This is all chemistry that I don't know much about. And, you know, that's a sort of,
*  you know, unfortunately, that's down at the level, you know, I would like to be at the software level,
*  not at the level of the transistors, so to speak. But in chemistry, you know, there's a certain
*  amount we have to do, I think, at the level of transistors before we get up to being able to do
*  it, although, you know, automated labs certainly help in setting that up. I talked to a guy named
*  Charles Hoskinson. He mentioned that he's collaborating with you. He's an interesting
*  guy. He sends me papers on speaking of automated theorem proving a lot. He's exceptionally well
*  read on that area as well. So what's the nature of your collaboration with him? He's the creator
*  of Cardano. What's the nature of the collaboration between Cardano and the whole space of blockchain
*  and Wolfram, Wolfram Alpha, Wolfram blockchain, all that kind of stuff? Well, okay, we're segueing to a
*  slightly different world. But so, although not completely unconnected, right, the whole thing
*  is somehow connected. I know. I mean, the, you know, the strange thing in my life is I've sort
*  of alternated between doing basic science and doing technology about five times in my life so far.
*  And the thing that's just crazy about it is, you know, every time I do one of these alternations,
*  I think there's not going to be a way back to the other thing. And like I thought for this physics
*  project, I thought, you know, we're doing fundamental theory of physics. Maybe it'll have an application
*  in 200 years. But now I've realized, actually, this multi computation idea is applicable here.
*  Now, it's and in fact, it's also giving us this way. I'll just mention one other thing, and then
*  then we can talk about blockchain. The question of actually that relates to several different things,
*  but one of the things about about okay, so our Wolfram language, which is our attempt to kind
*  of represent everything in the world computationally. And it's the thing I kind of started building 40
*  years ago in the form of actual Wolfram language 35 years ago. It's kind of this idea of can we
*  can we express things about the world in computational terms. And, you know, we've
*  come a long way in being able to do that. Wolfram Alpha is kind of the consumer version of that
*  way you're just using natural languages input the and it turns it into our symbolic language.
*  And that's, you know, the symbolic language Wolfram language is what people use and have been
*  using for the last 33 years. Actually, Mathematica, which is its first instantiation, will be one
*  third of a century old in in October. And that it's it's kind of interesting. What do you mean,
*  one third of a century? Does that mean 33 or 30? What do we 33 and a third? So,
*  I've never heard of anyone celebrating that anniversary, but I like it. I know a third of
*  a century though. It's it's like, you know, get many many slices of a century that interesting.
*  But you know, I think that the the thing that's really striking about that is that means,
*  you know, including the whole sort of technology stack up built around that's about 40 years old.
*  And that means it's a significant fraction of the total age of the computer industry.
*  And it's I mean, I think it's cool that we can still run, you know, Mathematica version one
*  programs today and so on. And we've sort of maintained compatibility. And we've been just
*  building this big tower all those years of just more and more and more computational capabilities.
*  It's sort of interesting. We just made this this picture of kind of the different kind of threads
*  of computational content of, you know, mathematical content and, and, you know,
*  all sorts of things with, you know, data and graphs and whatever else. And what you see in
*  this picture is about the first 10 years, it's kind of like it's just a few threads. And then,
*  then about maybe 1520 years ago, it kind of explodes in this whole collection different threads
*  of all these different capabilities that are now part of Wolfram language and representing
*  different things in the world. But the thing that was super lucky in some sense is it's all
*  based on one idea. It's all based on the idea of symbolic expressions and transformation rules for
*  symbolic expressions, which was kind of what I originally put into this SMP system back in 1979,
*  that was a predecessor of the whole Wolfram language stack. So that idea was an idea that
*  I got from sort of trying to understand mathematical logic and so on. It was my attempt
*  to kind of make a general human comprehensible model of computation of just everything is a
*  symbolic expression and all you do is transform symbolic expressions. And, you know, in, in
*  retrospect, I was very lucky that I understood as little as I understood then, because had I
*  understood more, I would have been completely freaked out about all the different ways that
*  that kind of model can, can fail. Because what do you do when you have a symbolic expression,
*  you make transformations for symbolic expressions? Well, for example, one question is there may be
*  many transformations that could be made in a very multi computational kind of way. But what we're
*  doing is picking, we're using the first transformation that applies. And we keep doing that until we
*  reach a fixed point. And that's the result. And that's kind of a very, it's kind of a way of sort
*  of sliding around the edge of multi computation. Back when I was working on SMP and things, I
*  actually thought about these questions about, about how, you know, how, what determines the,
*  this kind of evaluation path. So for example, you know, you work out Fibonacci, you know, Fibonacci
*  is a recursive thing, f of n is f of n minus one plus f of n minus two, and you get this whole tree
*  of recursion, right. And there's the question of how do you evaluate that tree of recursion? Do you
*  do it sort of depth first, where you go all the way down one side, do you do it breadth first,
*  where you're kind of collecting the terms together, where you know that, you know, f of eight plus f
*  of seven, f of seven plus f of six, you can collect the f of sevens and so on. These are, you know,
*  I didn't realize it at the time, it's kind of funny, I was working on, on gauge field theories
*  back in 1979. And I was also working on the evaluation model in SMP, and they're the same
*  problem. But it took me 40 more years to realize that. And this question about how you do this sort
*  of evaluation front, that's a question of reference frames. It's a question of kind of the, the story
*  of, I mean, that's, that is basically this question of, in what order is the universe evaluated?
*  And that, and so what you realize is, there's this whole sort of world of different kinds
*  of computation that you can do sort of multi computationally. And that's a, that's an
*  interesting thing. It has a lot of implications for distributed computing and so on. It also has a
*  potential implication for blockchain, which we haven't fully worked out, which is, and this is
*  not what we're doing with Cardano, but this is a different thing. The, this is something where,
*  one of the questions is, when you have, in a sense, blockchain is a deeply sequentialized
*  story of time, because in blockchain, there's just one copy of the ledger. And you're saying,
*  this is what happened. Time has progressed in this way. And there are little things around the edge
*  as you try and reach consensus and so on. And actually we just recently, we've had this little
*  conference we organized about the theory of distributed consensus, because I realized that
*  there are a bunch of interesting things that some of our science can tell one about that,
*  but that's a different, let's not go down that path.
*  Yeah, but distributed consensus, that still has a sequential, there's like one.
*  There's still sequentiality. So distributed consensus.
*  Don't tell me you're thinking through like how to apply multi computation to blockchain.
*  Yes. And so that becomes a story of, you know, instead of transactions all having to settle in
*  one ledger, it's like a story of all these different ledgers and they all have to have
*  some ultimate consistency, which is what causal invariance would give one. But it can take a while
*  and it can take a while is kind of like quantum mechanics. So it's kind of what's happening is
*  there are these different paths of history that correspond to, you know, in one path of history,
*  you got paid this amount. In another path of history, you got paid this amount. In the end,
*  the universe will always become consistent. Now, the way it works is, okay, it's a little
*  bit more complicated than that. What happens is the way space is knitted together in our
*  theory of physics is through all these events. And the idea is that the way that economic space
*  is knitted together is there these autonomous events that essentially knit together economic space.
*  So there are all these threads of transactions that are happening. And the question is, can they
*  be made consistent? Is there something forcing them to be sort of a consistent fabric of economic
*  reality? And sort of what this has led me to is trying to realize how does economics fundamentally
*  work? And, you know, what is economics? And, you know, what are the atoms of economics, so to speak?
*  And so what I've kind of realized is that sort of the perhaps, I don't even know if this is right
*  yet, there's sort of events in economics of transactions. There are states of agents that
*  are kind of the atoms of economics. And then transactions are kind of agents,
*  transact in some way, and that's an event. And then the question is, how do you knit together
*  sort of economic space from that? What is there in economic space? Well, all these transactions,
*  there's a whole complicated collection of possible transactions. But one thing that's true about
*  economics is we tend to have the notion of a definite value for things. We could imagine
*  that, you know, you buy a cookie from somebody, and they want to get a movie ticket. And there
*  is some way that AI bots could make some path from the cookie to the movie ticket by all these
*  different intermediate transactions. But in fact, we have an approximation to that, which is we say,
*  they each have a dollar value. And we have this kind of numeraire concept of there's just a way
*  of kind of taking this whole complicated space of transactions and parsing it in something which
*  is a kind of a simplified thing that is kind of like a parsing of physical space. And so my guess
*  is that the yet again, I mean, it's crazy that all these things are so connected. This is another
*  multi computation story. Another story of where what's happening is that the economic consciousness,
*  the economic observer is not going to deal with all of those different microscopic transactions.
*  They're just going to parse the whole thing by saying, there's this value, it's a number.
*  And that's their understanding of their summary of this economic network. And there will be all
*  kinds of things like there are all kinds of arbitrage opportunities, which are kind of like
*  the quantum effects in this whole thing. And that's, you know, and places where there's
*  where there's sort of different paths that can be followed and, and so on. And there's so
*  the question is, can one make a sort of global theory of economics? And then my test case is,
*  again, what is time dilation in economics? And I know for, you know, if you imagine a very
*  agricultural economics, where people are growing lettuces and fields and things like this, and you
*  ask questions about, well, if you're transporting lettuces to different places, you know, what is
*  the value of the lettuces after you have to transport them versus if you're just sitting in
*  one place and selling them, you can kind of get a little bit of an analogy there. But I think there's
*  a there's a better and more complete analogy. And that's the question of is there a theory like
*  general relativity, that is a global theory of economics? And is it about something we care
*  about? It could be that there is a global theory, but it's about a feature of economic reality that
*  isn't important to us. Now, another part of the story is, can one use those ideas to make
*  essentially a distributed blockchain, a distributed generalization of blockchain, kind of the quantum
*  analog of money, so to speak, where where you have, for example, you can have uncertainty
*  relations where you're saying, you know, well, if I if I insist on knowing my bank account right now,
*  there'll be some uncertainty. If I'm prepared to wait a while, then it'll be much more certain.
*  And so there's, you know, is there a way of using and so we've made a bunch of prototypes of this,
*  which I'm not yet happy with. But I realized is to really understand these prototypes,
*  I actually have to have a foundational theory of economics. And so that's kind of a, you know,
*  it may be that we could deploy one of these prototypes as a practical system. But I think
*  it's really going to be much better if we actually have an understanding of how this plugs into kind
*  of economics. And that means like a fundamental theory of transactions between entities,
*  that's what you mean by economics. Yes, I think so. But I mean, you know, how how there emerge sort
*  of laws of economics, I don't even know. And I've been asking friends of mine who are who are
*  economists and things, what is economics? You know, is it an axiomatic theory? Is it a theory
*  that is a kind of a qualitative description theory? Is it you know, what kind of a theory is it? Is
*  it a theory? You know, what kind of thinking it's like, like in biology, in evolutionary biology,
*  for example, there's a certain there's a certain pattern of thinking that goes on in evolutionary
*  biology, where if you're a, you know, a good evolutionary biologist, somebody says, that
*  creature has a weird horn. And they'll say, Well, that's because this and this and this and the
*  selection of this kind and that kind. And that's the story. And it's not a mathematical story. It's
*  a story of a different type of thinking about these things. By the way, evolutionary biology
*  is yet another place where it looks like this multi computational idea can be applied. And that's
*  where maybe speciation is related to things like event horizons. And there's a whole whole other
*  kind of world of that. But because it seems like this kind of model can be applicable so many
*  aspects, like the different levels of understanding of our reality. So it can be the biology at the
*  chemistry at the physics level, right, the economics and you could potentially say the thing is,
*  it's like, okay, sure, at all these levels in my rhyme, it might make sense as a model.
*  The question is, can you make useful predictions as one of these levels?
*  That's right. And that's really a question of, you know, it's a weird situation, because the
*  situation where the model probably has definite consequences. The question is, are they consequences
*  we care about? And that's some, you know, and so, in the case of in the economic case,
*  so, you know, the one thing is this idea of using kind of physics like notions to construct a kind
*  of distributed analog of blockchain. Okay, the much more pragmatic thing is a different direction.
*  And it has to do with this computational language that we built to describe the world
*  that knows about, you know, different kinds of cookies and knows about different cities and
*  knows about how to compute all these kinds of things. One of the things that is of interest is
*  if you want to run the world, you need, you know, with contracts and laws and rules and so on,
*  there are rules at a human level. And there are kind of things like and so this gets one into the
*  idea of computational contracts. You know, right now, when we write a contract, it's a piece of
*  legalese. It's, you know, it's just written in English. And it's not something that's
*  automatically analyzable, executable, whatever else, it's just English. You know, back in
*  Gottfried Leibniz, back in, you know, 1680 or whatever, was like, I'm going to, you know,
*  figure out how to use logic to decide legal cases and so on. And he had kind of this idea of let's
*  make a computational language for the human law. Forget about modeling nature, forgot about natural
*  laws. What about human law? Can we make kind of a computational representation of that? Well,
*  I think finally, we're close to being able to do that. And one of the projects that I hope to get
*  to as soon as the there's a little bit of slowing down of some of this Cambrian explosion that's
*  happening is a project I've been meaning to really do for a long time, which is what I'm calling a
*  symbolic discourse language. It's just finishing the job of being able to represent everything,
*  like the conversation we're having in computational terms. And one of the use cases for that is
*  computational contracts. Another use case is something like the Constitution that says what
*  we want the AIs to do. So, but this is useful. So you're saying, so these are like, you're saying
*  computational contracts, but smart contracts. This is what's in the domain of cryptocurrency is known
*  as smart contracts. And so the language you've developed, this symbolic or seek to further
*  develop symbolic discourse language enables you to write a contract and write a contract that
*  richly represents some aspect of the world. But so, I mean, smart contracts tend to be right now,
*  mostly about things happening on the blockchain. Yes. Sometimes they have oracles. And in fact,
*  our Wolfram Alpha API is the main thing people use to get information about the real world,
*  so to speak, within smart contracts. So Wolfram Alpha, as it stands, is a really good oracle.
*  Whoever wants to use it. That's perhaps where the relationship with Cardano is.
*  Yeah, well, that's how we started getting involved with blockchains is we realized people were using,
*  you know, Wolfram Alpha as the oracle for smart contracts, so to speak. And so that got us
*  interested in blockchains in general. And what was ended up happening is Wolfram language is with its
*  symbolic representation of things is really very good at representing things like blockchains.
*  And so I think we now have, I mean, I don't really know all the comparisons, but we now have a really
*  nice environment within Wolfram language for dealing with the sort of, you know, for representing
*  what happens in blockchains, for analyzing what happens in blockchains. We have a whole effort
*  in blockchain analytics. And, you know, we've sort of published some samples of how that works. But
*  it's, you know, because our technology stack, Wolfram language and Mathematica, are very widely
*  used in the quant finance world. There's a sort of immediate sort of coevolution there of sort of
*  the quant finance kind of thing and blockchain analytics. And that's so it's kind of the
*  representation of blockchain in computational language. Then ultimately, it's kind of like,
*  how do you run the world with code? That is, how do you write sort of all these things, which are
*  right now regulations and laws and contracts and things in computational language and kind of the
*  ultimate vision is that sort of something happens in the world. And then there's this giant domino
*  effect of all these computational contracts that trigger based on the thing that happened. And
*  there's a whole story to that. And of course, you know, I like to always pay attention to
*  the latest things that are going on. And I really, I kind of like blockchain because it's a,
*  it's another rethinking of kind of computation. It's kind of like, you know, cloud computing was
*  a little bit of that of sort of persistent kind of computational resources and so on.
*  And, you know, this multi computation is a big rethinking of kind of what it means to compute.
*  Blockchain is another bit of rethinking of what it means to compute the idea that you lodge kind
*  of these autonomous lumps of computation out there in the blockchain world. And one of the things that
*  just sort of for fun, so to speak, as we've been doing a bit of stuff with NFTs, and we just did
*  some NFTs on Cardano and we'll be doing some more. And, you know, we did some cellular automaton
*  NFTs on Cardano, which people simply like quite a bit. And, you know, one of the things I've
*  realized about NFTs is that there's kind of this notion, and we're really working on this, you know,
*  I like recording stuff. You know, one of the things that's come out of kind of my science,
*  I suppose, is this history matters type story of, you know, it's not just the current state,
*  it's the history that matters. And I've kind of, I don't think this is realizing maybe it's not
*  coincidental that I'm sort of the human who's recorded more about themselves than anybody else.
*  And then I end up with these science results that say history matters, which was not those things.
*  I didn't think those were connected, but they're at least correlated. Yes. Yeah, right. So,
*  you know, this question about sort of recording what has happened and having sort of a permanent
*  record of things. One of the things that's kind of interesting there is, you know, you put up a
*  website and it's got a bunch of stuff on it, but, you know, you have to keep paying the hosting fees
*  or the things are going to go away. But one of the things about blockchain is kind of interesting is
*  if you put something on a blockchain and you pay, you know, your commission to get that thing,
*  you know, put on, you know, mine, put on the blockchain, then in a sense, everybody who
*  comes after you is, you know, they are motivated to keep your thing alive because that's what keeps
*  the consistency of the blockchain. So in a sense with sort of the NFT world, it's kind of like,
*  if you want to have something permanent, well, at least for the life of the blockchain, but even
*  if the blockchain goes out of circulation, so to speak, there's going to be enough value in that
*  whole collection of transactions that people are going to archive the thing. But that means that,
*  you know, pay once and you're kind of, you're lodged in the blockchain forever. And so we've
*  been kind of playing around with sort of a hobby thing of mine of thinking about sort of the NFTs
*  and how you sort of the consumer idea of kind of the, it's the, it's the anti, you know,
*  it's the opposite of the Snapchat view of the world. There's a permanence to it. That's
*  heavily incentivized and thereby you can have a permanence of history. Right. And that's,
*  that's, that's kind of the now, you know, so that's, so that's one of the things we've been
*  doing with Cardano and it's kind of fun. I think that, that, I mean, this whole question about,
*  you know, you mentioned automated theorem proving and blockchains and so on. And as I've thought
*  about this kind of physics inspired distributed blockchain, obviously there, the sort of the proof
*  that it works, that there are no double spends, there's no whatever else. That proof becomes a
*  very formal kind of almost a matter of physics, so to speak. And, you know, it's been, it's been an
*  interesting thing for the, for the practical blockchains to do kind of actual automated
*  theorem proving. And I don't think anybody's really managed it in an interesting case yet.
*  It's a thing that people, you know, aspire to, but I think it's a challenging thing.
*  Because basically the point is one of the, one of the things about proving correctness of something
*  is, well, you know, people say, I've got this program and I'm going to prove it's correct.
*  And it's like, what does that mean? You have to say what correct means. I mean, it's,
*  it's kind of like, then you have to have another language. And people were very confused back in
*  past decades of, you know, oh, we're going to prove the correctness by representing the program.
*  And another language, which we also don't know whether it's correct. And, you know, often by
*  correctness, we just mean it can't crash or it can't scribble on memory. But, but the thing is
*  that there's this complicated trade off because as soon as there's, as soon as you're really using
*  computation, you have computational irreducibility, you have undecidability. If you want to use
*  computation seriously, you have to kind of let go of the idea that you're going to be able to box it
*  in and say, we're going to have just this happen and not anything else. I mean, this is a, this is
*  an old fact. I mean, Gödel's theorem tries to say, you know, piano arithmetic, the axioms of
*  arithmetic, can you box in the integers and say these axioms give just the integers and nothing
*  but the integers? Gödel's theorem showed that wasn't the case. There's a, you know, you can have
*  all these wild, weird things that are obey the piano axioms, but aren't integers. And there's
*  this kind of infinite hierarchy of additional axioms you would have to add. And it's kind of
*  the same thing. You don't get to, you know, if you want to say, I want to know what happens,
*  you're boxing yourself in and there's a limit to what can happen, so to speak. So it's a complicated
*  trade off and it's a big trade off for AI, so to speak. It's kind of like, do you want to let
*  computation actually do what it can do? Or do you want to say, no, it's very, very boxed into the
*  point where we can understand every step. And that's kind of a thing that becomes difficult to do.
*  But that's some, I mean, in general, I would say one of the things that's kind of complicated in my
*  sort of life and the whole sort of story of computational language and all this technology
*  and science and so on. I mean, I kind of in the flow of one's life, it's sort of interesting to see
*  how these things play out because I, you know, I've kind of concluded that I'm in the business
*  of making kind of artifacts from the future, which means, you know, there are things that I've done,
*  I don't know, this physics project, I don't know whether anybody would have gotten to it for 50
*  years. You know, the fact that Mathematica is a third of a century old, and I know that a bunch
*  of the core ideas are not well absorbed. I mean, that is people finally got this idea that I thought
*  was a triviality of notebooks, that was 25 years. And, you know, some of these core ideas about
*  symbolic computation and so on, are not absorbed. I mean, people use them every day in Wolfram
*  language and, you know, do all kinds of cool things with them. But if you say, what is the
*  fundamental intellectual point here? It's not well absorbed. And it's something where you kind of
*  realize that you're sort of building things. And I kind of made this thing about, you know,
*  we're building artifacts from the future, so to speak. And I mentioned that at Tower, we have a
*  conference every, it's coming up actually in a couple of weeks, annual technology conference,
*  where we talk about all the things we're doing. And, you know, so I was talking about it last year,
*  we're making artifacts from the future. And I was kind of like, I had some version of that that was
*  kind of a dark and frustrated thing of like, you know, I'm building things which nobody's going to
*  care about until long after I'm dead, so to speak. But then I realized, you know, people were sort of
*  telling me afterwards, you know, that's exactly how, you know, we're using Wolfram language in
*  some particular setting, in some computational X field or some organization or whatever.
*  And it's like people are saying, oh, you know, what did you manage to do? You know, well, we know
*  that in principle, it will be possible to do that. But we didn't know that was possible now. And it's
*  kind of like that's the that's sort of the business we're in. And in a sense, with some of these ideas
*  in science, you know, I feel a little bit the same way that there are some of these things where,
*  you know, some things like, for example, this whole idea, well, so to relate to another sort
*  of piece of history on the future, one of, you know, I mentioned, we mentioned at the beginning
*  kind of complexity as this thing that I was interested in back 40 years ago and so on.
*  Where does complexity come from? Well, I think we kind of nailed that. The answer is in the
*  computational universe, even simple programs make it. And that's kind of the secret that nature has
*  that allows you to make it. So that's kind of the that that's that part. But the bigger picture there
*  was this idea of this kind of computational paradigm, the idea that you could go beyond
*  mathematical equations, which have been sort of the primary modeling medium for 300 years.
*  And so it was like, look, it is inexorably the case that people will use programs rather than
*  just equations. And, you know, I was saying that in the 1980s, and people were, you know,
*  I published my big book, New Kind of Science, that'll be 20 years ago, next year, so in 2002.
*  And people are saying, Oh, no, this can't possibly be true. You know, we know, for 300 years, we've
*  been doing all this stuff, right? To be fair, I now realize a little bit more analysis of what
*  people actually said. In pretty much every field other than physics, people said, Oh, these are new
*  models. That's pretty interesting. In physics, people were like, we've got our physics models.
*  We're very happy with them. Yeah, in physics, there's more resistance because of the attachment
*  and the power of the equations. The idea that programs might be the right way to approach
*  right this field was there some resistance and like you're saying, it takes time for somebody
*  who likes the idea of time dilation and all these applications. I thought you would understand this.
*  Yeah, right. But you know, and computational irreducibility. Yes, exactly. But I mean,
*  it is really interesting that just 20 years, the span of 20 years, it's gone from, you know, pitch
*  forks and horror to, yeah, we get it. And, you know, it's helped that we've, you know, in our
*  current effort in fundamental physics, we've gotten a lot further and we've managed to put a
*  lot of puzzle pieces together that make sense. But the thing that I've been thinking about recently
*  is this field of complexity. So I've kind of was a sort of a field builder. Back in the 1980s,
*  I was kind of like, okay, you know, can we, you know, I'd understood this point that there was
*  this sort of fundamental phenomenon of complexity and showed up in lots of places. And I was like,
*  this is an interesting sort of field of science. And I was recently was reminded I was at this,
*  the very first sort of get together of what became the Santa Fe Institute. And I was like, in fact,
*  there's even an audio recording of me sort of saying, people have been talking about, oh,
*  what should this, you know, outfit do? And I was saying, well, there is this thing that I've been
*  thinking about. It's this kind of idea of complexity. And it's kind of like, and that's
*  what that ended up in. And you planted the seed of complexity at Santa Fe. That's beautiful.
*  It's a beautiful vision. But I mean, so that, but what's happened then is this idea of complexity.
*  And, you know, and I started the first research center at University of Illinois for doing that
*  in the first journal, complex systems and so on. And it's kind of an interesting thing in my life,
*  at least, that it's kind of like, you plant the seed, you have this idea, it's a kind of a science
*  idea. You have this idea of sort of focusing on the phenomenon of complexity. The deeper idea was
*  this computational paradigm. But the nominal idea is this kind of idea of complexity. Okay, then you
*  roll time forward 30 years or whatever, 35 years, whatever it is. And you say, what happened? Okay,
*  well, now there are 1000 complexity institutes around the world. I think more or less, we've
*  been trying to count them. And, you know, there are 40 complexity journals, I think. And so
*  it's kind of like what actually happened in this field, right? And I look at a lot of what happened,
*  and I'm like, you know, I have to admit to some eye rolling, so to speak, because it's kind of like,
*  like, what is what's actually going on? Well, what people definitely got was this idea of
*  computational models. And then they got but they thought one of the one of the kind of cognitive
*  mistakes, I think, is they say, we've got a computational model. And it's, and we're looking
*  at a system that's complex. And our computational model gives complexity, by golly, that must mean
*  it's right. And unfortunately, because complexity is a generic phenomenon, and computational
*  irreducibility is a generic phenomenon that actually tells you nothing. And so then the
*  question is, well, what can you do? You know, there's a lot of things that have been sort of
*  done under this banner of complexity. And I think it's been very successful in providing sort of an
*  interdisciplinary way of connecting different fields together, which is powerful in itself,
*  right? I mean, that's a very useful economics. And yeah, it is right. It's a good organizing
*  principle. But but in the end, a lot of that is around this kind of computational paradigm,
*  computational modeling. That's the raw material that powers that kind of that kind of correspondence,
*  I think. But the question is sort of what is the, you know, I was just thinking recently,
*  you know, we've been, I mean, the other, we've been, we've been, for years, people have told me,
*  you should start some Wolfram Institute that does basic science. You know, all I have is a company
*  that builds software. And we, you know, we have a little piece that does basic science as kind of a
*  hobby. People are saying, you should start this Wolfram Institute thing. And I've been, you know,
*  because I've known about lots of institutes, and I've seen kind of their flow of money and,
*  and kind of, you know, what happens in different situations, and so on. So I've been kind of
*  reluctant, but, but I've, I've, I have realized that, you know, what we've done with our company
*  over the last 35 years, you know, we built a very good machine for doing R&D, and, you know,
*  innovating and creating things. And I just applied that machine to the physics project. That's how
*  we did the physics project in a fairly short amount of time, with a, you know, efficient
*  machine with, you know, various people involved and so on. And so, you know, it works for basic
*  science. And it's like, we can do more of this. And so-
*  Biology and chemistry, so it's become an institute.
*  Yes. Well, it needs to become an institute.
*  An official institute.
*  Right. Right. But the thing that, so I was thinking about, okay, so what do we do with complexity?
*  You know, what, what, there are all these people who've, you know, what, what should happen to that
*  field? And what I realized is, there's kind of this area of foundations of complexity
*  that's about these questions about simple programs, what they do, that's far away from
*  a bunch of the detailed applications that people, well, it's not far away. It's the, it's the under,
*  you know, the, the bedrock underneath those applications. And so I realized recently, this
*  is my, a recent kind of little innovation of a sort, a post that I'll do very soon, about
*  kind of, you know, the foundations of complexity. What really are they? I think there are really
*  two ideas, two conceptual ideas that I hadn't really enunciated, I think, before. One is what
*  I call meta-modeling. The other is rulliology. So what is meta-modeling? So meta-modeling is,
*  you've got this complicated model, and it's a model of, you know, hedgehogs interacting with
*  this, interacting with that. And the question is, what's really underneath that? What is it?
*  You know, is it a Turing machine? Is it a cellular automaton? You know, what is the underlying stuff
*  underneath that model? And so there's this kind of meta-science question of, given these models,
*  what is the core model? And I realized, I mean, to me, that's sort of an obvious question. But then
*  I realized, I've been doing language design for 40 years, and language design is exactly that
*  question. You know, underneath all of this detailed stuff people do, what are the underlying
*  primitives? And that's a question people haven't tended to ask about models. They say, well, we've
*  got this nice model for this and that and the other. What's really underneath it? And what,
*  you know, because once you have the thing that's underneath it, well, for example, this
*  multi-computation idea is an ultimate meta-modeling idea, because it's saying underneath all these
*  fields is one kind of paradigmatic structure. And, you know, you can imagine the same kind of thing
*  in much more sort of much sort of shallower levels in different kinds of modeling. So the
*  first activity is this kind of meta-modeling, the kind of the models about models, so to speak.
*  You know, what is the, what's drilling down into models? That's one thing. The other thing is this
*  thing that I think we're going to call rulliology, which is kind of the, okay, you've got these simple
*  rules. You've got cellular automata, you've got Turing machines, you've got substitution systems,
*  register machines, got all these different things. What do they actually do in the wild?
*  And this is an area that I've spent a lot of time, you know, working on. It's a lot of stuff in my
*  new kind of science book is about this. You know, this new book I wrote about combinators is full of
*  stuff like this. And this journal Complex Systems has lots of papers about these kinds of things.
*  But there isn't really a home for people who do rullology or whatever.
*  It's the, as you call it, the basic science of rules.
*  Yes. Yes, right. So it's like, you've got some, what is it? Is it mathematics? No,
*  it isn't really like mathematics. In fact, from my now understanding of meta-mathematics,
*  I understand that it's the molecular dynamics level. It's not the level that mathematicians
*  have traditionally cared about. It's not computer science, because computer science is about writing
*  programs that do things, you know, that were for a purpose, not programs in the wild, so to speak.
*  It's not physics. It doesn't have anything to do with, you know, it may be underneath some physics,
*  but it's not physics as such. So it just hasn't had a home. And if you look at, you know, but
*  what's great about it is it's a surviving field, so to speak. It's something where, you know, one of
*  the things I find sort of inspiring about mathematics, for example, is you look at mathematics
*  that was done, you know, in ancient Greece, ancient, you know, Babylon, Egypt, and so on.
*  It's still here today. You know, you find an icosahedron that somebody made in ancient Egypt.
*  You look at it, oh, that's a very modern thing. It's an icosahedron. You know, it's a timeless kind
*  of activity. And this idea of studying simple rules and what they do, it's a timeless activity.
*  And I can see that over the last 40 years or so, as, you know, even with cellular automata,
*  it's kind of like, you know, you can sort of catalog what are the different cellular automata
*  used for, and, you know, like the simplest rules, like one, you might even know this one, rule 184.
*  Rule 184 is a minimal model for road traffic flow. And, you know, it's also a minimal model
*  for various other things. But it's kind of fun that you can literally say, you know, rule 90 is
*  a minimal model for this and this and this. Rule 4 is a minimal model for this. And it's kind of
*  remarkable that you can just by, in this raw level of this kind of study of rules, they then branch,
*  they're the raw material that you can use to make models of different things. So it's a very pure
*  basic science. But it's one that, you know, people have explored it, but they've been kind of a
*  little bit in the wilderness. And I think, you know, one of the things that I would like to do
*  finally, is, you know, I always thought that sort of this notion of pure NKS, pure NKS being the
*  acronym for my book, New Kind of Science, was something that people should be doing. And,
*  you know, we tried to figure out what's the right institutional structure to do this stuff. You know,
*  we dealt with a bunch of universities, oh, you know, can we do this here? Well, what department
*  would it be in? Well, it isn't in a department. It's its own new kind of thing. That's why the
*  book was called The New Kind of Science. It's kind of the, because that's an increasingly good
*  description of what it is, so to speak. We're actually, we were thinking about kind of the
*  ruleological society, because we're realizing that it's kind of, you know, it's very interesting. I
*  mean, I've never really done something like this before, because there's this whole group of
*  researchers who have been doing things that are really, in some cases, very elegant, very surviving,
*  very solid, you know, here's this thing that happens in this very abstract system. But it's
*  like, what is that part of? You know, it doesn't have a home. And I think that's something, you know,
*  I kind of fault myself for not having been more, you know, when complexity was developing in the
*  80s. I didn't understand the danger of applications. That is, it's really cool that you can apply this
*  to economics, and you can apply it to evolutionary biology, and this and that and the other. But what
*  happens with applications is everything gets sucked into the applications. And the pure stuff, it's
*  like the pure mathematics, there isn't any pure mathematics, so to speak. It's all just applications
*  of mathematics. And I failed to kind of make sure that this kind of pure area was kind of
*  maintained and developed. And I think now, you know, one of the things I want to try to do, and,
*  you know, it's a funny thing, because I'm used to, look, I've been a tech CEO for more than half my
*  life now. So, you know, this is what I know how to do. And, you know, I can make stuff happen
*  and get projects to happen, even as it turns out basic science projects in that kind of setting,
*  and how that translates into kind of, you know, there are a lot of people working on, for example,
*  our physics project sort of distributed through the academic world, and that's working just great.
*  But the question is, you know, can we have a sort of accelerator mechanism that makes use of kind
*  of what we've learned in sort of R&D innovation? And, you know, but on the other hand, it's a funny
*  thing, because, you know, in a company, in the end, the thing is, you know, it's a company,
*  it makes products, it sells things, sells things to people. And, you know, when you're doing basic
*  research, one of the challenges is there isn't that same kind of sort of mechanism. And so it's,
*  you know, how do you drive the thing in a kind of, in a led kind of way, so that it really can
*  make forward progress, rather than, you know, what can often happen in, you know, in academic
*  settings, where it's like, well, there are all these flowers blooming, but it's not clear that
*  they're, you know, that it's- You have to have a central mission and a drive, just like you do
*  with a company that's delivering a big overarching product. And that's-
*  Right. But the challenge is, you know, when you have the economics of the world are such that,
*  you know, when you're delivering a product and people say, wow, that's useful, we'll buy it.
*  And then that kind of feeds back and, okay, then you can pay the people who build it to eat, you
*  know, so they can eat and so on. And with basic science, the payoff is very much less visible.
*  And, you know, with this physics project, as I say, the big surprise has been that, I mean,
*  you know, for example, well, the big surprise with the physics project is that it looks like it has
*  near term applications. And I was like, I'm guessing this is 200 years away. It's, I was kind of
*  using the analogy of, you know, Newton starting a satellite launch company, which would have been
*  kind of wrong time. And, you know, but it turns out that's not the case. But we can't guarantee
*  that. And if you say we're signing up to do basic research, basic radiology, let's say, and,
*  you know, and we can't, we don't know the horizon, you know, it's an unknown horizon. It's kind of
*  like an undecidable kind of proposition of when is this proof going to end, so to speak, when is
*  it going to be something that gets applied? Well, I hope this is, this becomes a vibrant new field
*  of radiology. I love it. Like I told you many, many times, it's one of the most amazing ideas
*  that has been brought to this world. So I hope you get a bunch of people to explore this world.
*  Thank you once again for spending your really valuable time with me today.
*  Fun stuff. Thank you.
*  Thank you for listening and hope to see you next time.

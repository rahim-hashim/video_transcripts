---
Date Generated: November 01, 2024
Transcription Model: whisper medium 20231117
Length: 4558s
Video Keywords: []
Video Views: 182352
Video Rating: None
Video Description: 
---

# Yann LeCun Deep Learning, ConvNets, and Self-Supervised Learning  Lex Fridman Podcast #36
**Lex Fridman:** [August 31, 2019](https://www.youtube.com/watch?v=SGSOCuByo24)
*  The following is a conversation with Yan LeCun. He's considered to be one of the fathers of deep
*  learning, which, if you've been hiding under a rock, is the recent revolution in AI that has
*  captivated the world with the possibility of what machines can learn from data. He's a professor
*  at New York University, a vice president and chief AI scientist at Facebook, and co-recipient of the
*  Turing Award for his work on deep learning. He's probably best known as the founding father of
*  convolutional neural networks, in particular their application to optical character recognition
*  and the famed MNIST dataset. He is also an outspoken personality, unafraid to speak his
*  mind in a distinctive French accent and explore provocative ideas both in the rigorous medium of
*  academic research and the somewhat less rigorous medium of Twitter and Facebook.
*  This is the Artificial Intelligence Podcast. If you enjoy it, subscribe on YouTube, give it five
*  stars on iTunes, support it on Patreon, or simply connect with me on Twitter at Lex Friedman,
*  spelled F-R-I-D-M-A-N. And now here's my conversation with Yan LeCun.
*  You said that 2001 Space Odyssey is one of your favorite movies.
*  Hal 9000 decides to get rid of the astronauts for people who haven't seen the movie, spoiler alert,
*  because he, it, she believes that the astronauts, they will interfere with the mission.
*  Do you see Hal as flawed in some fundamental way or even evil, or did he do the right thing?
*  Neither. There's no notion of evil in that context, other than the fact that people die. But
*  it was an example of what people call value misalignment, right? You give an objective
*  to a machine and the machine tries to achieve this objective. And if you don't put any constraints
*  on this objective, like don't kill people and don't do things like this, the machine, given the
*  power, will do stupid things just to achieve this objective or damaging things to achieve this
*  objective. It's a little bit like, I mean, we're used to this in the context of human society.
*  We put in place laws to prevent people from doing bad things because spontaneously they would do
*  those bad things, right? So we have to shape their cost function, their objective function,
*  if you want, through laws to kind of correct and education, obviously, to sort of correct for those.
*  So maybe just pushing a little further on that point, Hal, there's a mission, there's
*  a fuzziness around the ambiguity around what the actual mission is. But do you think that there
*  will be a time from a utilitarian perspective where an AI system, where it is not misalignment,
*  where it is alignment for the greater good of society, that an AI system will meet the
*  decisions that are difficult? Well, that's the trick. I mean, eventually we'll have to figure out
*  how to do this. And again, we're not starting from scratch because we've been doing this with humans
*  for millennia. So designing objective functions for people is something that we know how to do.
*  And we don't do it by programming things, although the legal code is called code. So that tells you
*  something. And it's actually the design of an objective function. That's really what legal code
*  is, right? It tells you, here's what you can do, here's what you can't do. If you do it, you pay
*  that much, that's an objective function. So there is this idea somehow that it's a new thing for
*  people to try to design objective functions that are aligned with the common good. But no, we've
*  been writing laws for millennia and that's exactly what it is. So that's where the science of law
*  making and computer science will come together. So there's nothing special about HAL or AI systems,
*  it's just the continuation of tools used to make some of these difficult ethical judgments that
*  laws make. Yeah, and we have systems like this already that make mini decisions for ourselves
*  in society that need to be designed in a way that they like rules about things that sometimes have
*  bad side effects. And we have to be flexible enough about those rules so that they can be broken when
*  it's obvious that they shouldn't be applied. So you don't see this on the camera here, but all
*  the decoration in this room is all pictures from 2001 in Space Odyssey. Wow, is that by accident?
*  It's not by accident, it's by design.
*  Wow. So if you were to build HAL 10,000, so an improvement of HAL 9000,
*  what would you improve? Well, first of all, I wouldn't ask it to hold secrets and tell lies
*  because that's really what breaks it in the end. That's the fact that it's asking itself questions
*  about the purpose of the mission and it's, you know, pieces things together that it's heard,
*  all the secrecy of the preparation of the mission and the fact that it was a discovery
*  on the lunar surface that really was kept secret. And one part of HAL's memory knows this and the
*  other part does not know it and is supposed to not tell anyone and that creates internal conflict.
*  So you think there never should be a set of things that an AI system should not be allowed,
*  like a set of facts that should not be shared with the human operators.
*  Well, I think no, I think it should be a bit like in the design of
*  autonomous AI systems, there should be the equivalent of, you know, the oath that
*  Hippocrates that doctors sign up to, right? So there's certain things, certain rules that
*  you have to abide by and we can sort of hardwire this into our machines to kind of
*  make sure they don't go. So I'm not, you know, an advocate of the three laws of robotics, you know,
*  the azimuth kind of thing, because I don't think it's practical, but you know, some level of limits.
*  But to be clear, these are not questions that are kind of really worth asking today because we just
*  don't have the technology to do this. We don't have autonomous intelligence machines. We have
*  intelligent machines, semi-intelligent machines that are very specialized, but they don't really
*  sort of satisfy an objective. They're just, you know, kind of trained to do one thing. So until we
*  have some idea for design of a full-fledged autonomous intelligent system, asking the question
*  of how we design this objective, I think is a little too abstract. It's a little too abstract.
*  There's useful elements to it in that it helps us understand our own ethical codes, humans. So even
*  just as a thought experiment, if you imagine that an AGI system is here today, how would we program
*  it is a kind of nice thought experiment of constructing how should we have a law, have a
*  system of laws for us humans. It's just a nice practical tool. And I think there's echoes of that
*  idea too in the AI systems we have today that don't have to be that intelligent, like autonomous
*  vehicles. These things start creeping in that are worth thinking about, but certainly they shouldn't
*  be framed as how. Looking back, what is the most, I'm sorry if it's a silly question, but what is the
*  most beautiful or surprising idea in deep learning or AI in general that you've ever come across?
*  Personally, when you said back and just had this kind of, that's pretty cool moment. That's nice.
*  Well, I don't know if it's an idea rather than a sort of empirical fact. The fact that
*  you can build gigantic neural nets, train them on relatively small amounts of data relatively
*  with stochastic grid and descent, and that it actually works, breaks everything you read in
*  every textbook, right? Every pre-deep learning textbook that told you, you need to have fewer
*  parameters and you have data samples. If you have a non-convex objective function, you have no
*  guarantee of convergence, all those things that you read in textbook and they tell you stay away
*  from this and they're all wrong. And these number of parameters, non-convex, and somehow, which is
*  very relative to the number of parameters, data, it's able to learn anything. Does that still
*  surprise you today? Well, it was kind of obvious to me before I knew anything that this is a good
*  idea. And then it became surprising that it worked because I started reading those textbooks.
*  Okay. So can you talk through the intuition of why it was obvious to you, if you remember?
*  Well, okay. So the intuition was, it's sort of like those people in the late 19th century who
*  proved that heavier than air flight was impossible, right? And of course you have birds, right? They
*  do fly. And so on the face of it, it's obviously wrong as an empirical question, right? And so we
*  have the same kind of thing that we know that the brain works. We don't know how, but we know it
*  works. And we know it's a large network of neurons and interaction and that learning takes
*  place by changing the connection. So kind of getting this level of inspiration without
*  copying the details, but sort of trying to derive basic principles, that kind of gives you a clue as
*  to which direction to go. There's also the idea somehow that I've been convinced of since I was
*  an undergrad that even before, that intelligence is inseparable from learning. So the idea somehow
*  that you can create an intelligent machine by basically programming. For me, it was an on
*  starter from the start. Every intelligent entity that we know about arrives at this intelligence
*  through learning. So machine learning was a completely obvious path. Also because I'm lazy,
*  so kind of. You automate basically everything and learning is the automation of intelligence.
*  Right. So do you think, so what is learning then? What falls under learning? Because
*  do you think of reasoning as learning? Well, reasoning is certainly a consequence of learning
*  as well, just like other functions of the brain. The big question about reasoning is how do you
*  make reasoning compatible with gradient-based learning? Do you think neural networks can be
*  made to reason? Yes, there is no question about that. Again, we have a good example, right?
*  The question is how? So the question is how much prior structure do you have to put in the neural
*  net so that something like human reasoning will emerge from it, from learning? Another question is
*  all of our kind of model of what reasoning is that are based on logic are discrete and are therefore
*  incompatible with gradient-based learning? And I'm a very strong believer in this idea of
*  gradient-based learning. I don't believe that other types of learning that don't use kind of
*  gradient information if you want. So you don't like discrete mathematics? You don't like anything
*  discrete? Well, it's not that I don't like it. It's just that it's incompatible with learning and I'm
*  a big fan of learning, right? So in fact, that's perhaps one reason why deep learning has been
*  kind of looked at with suspicion by a lot of computer scientists because the math is very
*  different. The math that you use for deep learning has more to do with cybernetics,
*  the kind of math you do in electrical engineering than the kind of math you do in computer science.
*  And nothing in machine learning is exact, right? Computer science is all about
*  obviously compulsive attention to details of like every index has to be right and you can prove that
*  an algorithm is correct, right? Machine learning is the science of sloppiness, really.
*  That's beautiful. So, okay, maybe let's feel around in the dark of what is a neural network
*  that reasons or a system that works with continuous functions that's able to do,
*  uh, build knowledge, however we think about reasoning, build on previous knowledge, build
*  on extra knowledge, create new knowledge, generalize outside of any training set ever built. What does
*  that look like if, uh, yeah, maybe do you have inklings of thoughts of what that might look like?
*  Well, yeah, I mean, yes and no. If I had precise ideas about this, I think, you know,
*  we'd be building it right now. But, and there are people working on this,
*  whose main research interest is actually exactly that, right? So, what you need to have is a working
*  memory. So, you need to have some device, if you want, some subsystem that can store a relatively
*  large number of factual episodic information for, you know, a reasonable amount of time. So,
*  you know, in the brain, for example, there are kind of three main types of memory. One is the
*  sort of memory of the state of your cortex. And that sort of disappears within 20 seconds. You
*  can't remember things for more than about 20 seconds or a minute if you don't have any other
*  form of memory. The second type of memory, which is longer term, is still short term, is the
*  hippocampus. So, you can, you know, you came into this building, you remember where the exit is,
*  where the elevators are. You have some map of that building that's stored in your hippocampus.
*  You might remember something about what I said, you know, a few minutes ago.
*  I forgot it all already. Of course, it's been erased. But, you know, that would be in your
*  hippocampus. And then the longer term memory is in the synapses, right? So, what you need, if you
*  want a system that's capable of reasoning, is that you want the hippocampus-like thing, right?
*  And that's what people have tried to do with memory networks and, you know,
*  neural training machines and stuff like that, right? And now with transformers, which have
*  sort of a memory in their kind of self-attention system. You can think of it this way. So,
*  that's one element you need. Another thing you need is some sort of network that can
*  access this memory, get an information back, and then kind of crunch on it, and then
*  do this iteratively multiple times. Because a chain of reasoning
*  is a process by which you update your knowledge about the state of the world, about, you know,
*  what's going to happen, et cetera. And that has to be the sort of recurrent operation, basically.
*  And you think that kind of, if we think about a transformer, so that seems to be too small to
*  contain the knowledge that's to represent the knowledge that's contained in Wikipedia, for example.
*  But a transformer doesn't have this idea of recurrence. It's got a fixed number of layers,
*  and that's the number of steps that, you know, limits basically its representation.
*  But recurrence would build on the knowledge, somehow. I mean, it would evolve the knowledge
*  and expand the amount of information, perhaps, or useful information within that knowledge.
*  But is this something that just can emerge with size? Because it seems like everything we have
*  now is too small. No, it's not clear. I mean, how you access and write into an associative
*  memory in an efficient way. I mean, sort of the original memory network maybe had something like
*  the right architecture, but if you try to scale up a memory network so that the memory contains
*  all Wikipedia, it doesn't quite work. So there's a need for new ideas there.
*  But it's not the only form of reasoning. So there's another form of reasoning, which is true,
*  which is very classical also in some types of AI, and it's based on, let's call it energy
*  minimization. So you have some sort of objective, some energy function that represents the
*  quality or the negative quality. Energy goes up when things get bad and they get low when things
*  get good. So let's say you want to figure out, you know, what gestures do I need to do
*  to grab an object or walk out the door? If you have a good model of your own body, a good model of
*  the environment, using this kind of energy minimization, you can do planning. And it's
*  in optimal control, it's called model predictive control. You have a model of what's going to
*  happen in the world as a consequence of your actions. And that allows you to buy energy
*  minimization, figure out a sequence of action that optimizes a particular objective function,
*  which measures, you know, minimize the number of times you're going to hit something and
*  the energy you're going to spend doing the gesture and et cetera. So that's a form of reasoning.
*  Planning is a form of reasoning. And perhaps, you know, if you're going to do a lot of things,
*  what led to the ability of humans to reason is the fact that, or, you know, species, you know,
*  that appear before us had to do some sort of planning to be able to hunt and survive and
*  survive the winter in particular. And so, you know, it's the same capacity that you need to have.
*  So in your intuition is, if we look at expert systems and encoding knowledge as logic systems,
*  and as graphs, in this kind of way, is not a useful way to think about knowledge?
*  Graphs are a little brittle or logic representation. So basically, you know,
*  variables that have values and then constraint between them that are represented by rules,
*  it's a little too rigid and too brittle, right? So one of the, you know, some of the early efforts
*  in that respect were to put probabilities on them. So a rule, you know, if you have this and that
*  symptom, you know, you have this disease with that probability and you should prescribe that
*  antibiotic with that probability, right? That's the mycin system from the 70s. And that's what
*  that branch of AI led to, you know, based on networks and graphical models and causal
*  inference and variational, you know, method. So there is, I mean, certainly a lot of interesting
*  work going on in this area. The main issue with this is knowledge acquisition. How do you
*  reduce a bunch of data to a graph of this type?
*  Yeah, it relies on the expert, on the human being to encode, to add knowledge.
*  And that's essentially impractical.
*  Yeah. So it's not scalable.
*  That's a big question. The second question is, do you want to represent knowledge as symbols?
*  And do you want to manipulate them with logic? And again, that's incompatible with learning.
*  So one suggestion with Jeff Hinton has been advocating for many decades is replace symbols by
*  vectors. Think of it as pattern of activities in a bunch of neurons or units or whatever you want
*  to call them and replace logic by continuous functions. Okay. And that becomes now compatible.
*  This is a very good set of ideas written in a paper about 10 years ago by Leon Bottou
*  on who is here at Facebook. The title of the paper is From Machine Learning to Machine
*  Reasoning. And his idea is that learning systems should be able to manipulate objects that are
*  in a space and then put the result back in the same space. So it's this idea of working memory,
*  basically. And it's very enlightening.
*  And in a sense, that might learn something like the simple expert systems.
*  I mean, you can learn basic logic operations there.
*  Yeah, quite possibly. Yeah. There's a big debate on sort of how much prior structure you have to
*  put in for this kind of stuff to emerge. That's the debate I have with Gary Marcus and people
*  like that. Yeah. Yeah. So and the other person, so I just talked to Judea Pearl from the mentioned
*  causal inference world. So his worry is that the current neural networks are not able to learn
*  what causes what causal inference between things.
*  So I think I think he's right and wrong about this. If he's talking about the sort of classic
*  type of neural nets, people didn't worry too much about this. But there's a lot of people now
*  working on causal inference. And there's a paper that just came out last week by Leon Butu, among
*  others, David Lopez-Paz and a bunch of other people, exactly on that problem of how do you kind of,
*  you know, get a neural net to sort of pay attention to real causal relationships,
*  which may also solve issues of bias in data and things like this. So
*  I'd like to read that paper because that ultimately the challenge is also seems to fall back on the
*  human expert to ultimately decide causality between things.
*  People are not very good at establishing causality, first of all. So first of all,
*  you talk to physicists and physicists actually don't believe in causality because look at the
*  all the basic laws of microphysics are time reversible. So there's no causality. The arrow of time
*  is not real. It's as soon as you start looking at macroscopic systems where there is unpredictable
*  randomness, where there is clearly an arrow of time, but it's a big mystery in physics actually,
*  how that emerges. Is it emergent or is it part of the fundamental fabric of reality?
*  Or is it a bias of intelligent systems that, you know, because of the second law of thermodynamics,
*  we perceive a particular hour of time, but in fact, it's not a real time.
*  In fact, it's kind of arbitrary, right? So yeah, physicists, mathematicians, they don't care about,
*  I mean, the math doesn't care about the flow of time. Well, certainly, certainly,
*  microphysics doesn't. People themselves are not very good at establishing causal relationships.
*  If you ask this, I think it was in one of Seymour Pepper's book on children learning,
*  you know, he studied with Jean Piaget, you know, he's the guy who co-authored the book
*  Perceptron with Marvin Minsky that kind of killed the first wave of neural nets. But he was actually
*  a learning person, in the sense of studying learning in humans and machines. That's why he got
*  interested in perceptron. And he wrote that if you ask a little kid about what is the cause of
*  the wind, a lot of kids will say, they will think for a while and they'll say, oh, it's the branches
*  in the trees, they move and that creates wind, right? So they get the causal relationship
*  backwards. And it's because their understanding of the world and intuitive physics is not that great,
*  right? I mean, these are like, you know, four or five year old kids, you know, it gets better and
*  then you understand that this can be right. But there are many things which we can,
*  because of our common sense understanding of things, what people call common sense,
*  and our understanding of physics, we can, there's a lot of stuff that we can figure out causality,
*  even with diseases, we can figure out what's not causing what often. There's a lot of mystery,
*  of course, but the idea is that you should be able to encode that into systems. It seems unlikely
*  to be able to figure that out themselves. Well, whenever we can do intervention, but you know,
*  all of humanity has been completely deluded for millennia, probably since its existence,
*  about a very, very wrong causal relationship, where whatever you can explain, you attribute it to,
*  you know, some deity, some divinity, right? And that's a cop out. That's the way of saying like,
*  I don't know the cause, so you know, God did it, right? So you mentioned Marvin Minsky and
*  the irony of, you know, maybe causing the first AI winter. You were there in the 90s, you were there
*  in the 80s, of course, in the 90s, why do you think people lost faith in deep learning in the 90s,
*  and found it again, a decade later, over a decade later? Yeah, it wasn't called deep learning yet,
*  it was just called neural nets. Yeah, they lost interest. I mean, I think I would put that
*  around 1995, at least the machine learning community, there was always a neural net
*  community, but it became kind of disconnected from sort of mainstream machine learning,
*  if you want. There were, it was basically electrical engineering that kept at it,
*  and computer science gave up on neural nets. I don't know, you know, I was too close to it to really
*  sort of analyze it with sort of an unbiased eye, if you want, but I would make a few guesses.
*  So the first one is, at the time, neural nets were, it was very hard to make them work,
*  in the sense that you would, you know, implement backprop in your favorite language. And that
*  favorite language was not Python, it was not MATLAB, it was not any of those things, because
*  they didn't exist, right, you know, to write it in Fortran or C or something like this, right.
*  So you would experiment with it, you would probably make some very basic mistakes, like,
*  you know, badly initialize your weights, make the network too small, because you read in the
*  textbook, you know, you don't want too many parameters, right. And of course, you know,
*  and you would train on XOR, because you didn't have any other data set to trade on. And of course,
*  you know, it works half the time. So you'd say, I give up. Also, you're training to the batch
*  gradient, which, you know, isn't sufficient. So there's a lot of, there's bad good tricks that
*  you had to know to make those things work, or you had to reinvent. And a lot of people just didn't,
*  and they just couldn't make it work. So that's one thing, the investment in software platform to
*  be able to kind of, you know, display things, figure out why things don't work, kind of get
*  a good intuition for how to get them to work, have enough flexibility, so you can create, you know,
*  network architectures like convolutional nets and stuff like that. It was hard, I mean, you had to
*  write everything from scratch. And again, you didn't have any Python or MATLAB or anything,
*  right? I read that, sorry to interrupt, but I read that you wrote in in Lisp, the first versions of
*  Lynette with the convolutional networks, which by the way, one of my favorite languages.
*  That's how I knew you were legit. Touring award, whatever this with you programmed unless that's
*  still my favorite language. But it's not that we programmed in Lisp is that we had to write all this
*  interpreter. Okay, because it's not that's right. That's one that existed. So we wrote a
*  Lisp interpreter that we hooked up to, you know, a back end library that we wrote also for sort of
*  neural net computation. And then after a few years around 1991, we invented this idea of
*  basically having modules that know how to forward propagate and back propagate gradients,
*  and then interconnecting those modules in a graph. You know, but who had made proposals on this
*  about this in the late 80s, and we're able to implement this using our list system.
*  Eventually, we wanted to use that system to make build production code for character recognition
*  at Bell Labs. So we actually wrote a compiler for that Lisp interpreter so that Patricia Mard,
*  who is now at Microsoft, kind of did the bulk of it with Leon and me. And so we could write our
*  system in Lisp and then compile to C and then we'll have a self-contained complete system that could
*  kind of do the entire thing. Neither PyTorch, nor Transunflux can do this today. Yet. Okay,
*  it's coming. I mean, there's something like that in PyTorch called Torch script. And so, you know,
*  we had to write all this interpreter, we had to write all this compiler, we had to invest a huge
*  amount of effort to do this. And not everybody, if you don't completely believe in the concept,
*  you're not going to invest the time to do this. Now, at the time also, you know,
*  today, this would turn into Torch or PyTorch or Transunflux or whatever, we'd put it in open
*  source, everybody would use it and, you know, realize it's good. Back before 1995, working at
*  AT&T, there's no way the lawyers would let you release anything in open source of this nature.
*  And so we could not distribute our code really. And on that point, and sorry to go into million
*  tangents, but on that point, I also read that there was some almost like a patent on
*  convolutional neural networks. So that, first of all, I mean, just two actually, that ran out.
*  Thankfully, in 2007.
*  In 2007. Can we just talk about that? I know you're on Facebook, but you're also at NYU.
*  And what does it mean to patent ideas like these software ideas, essentially? Or what are
*  mathematical ideas? Or what are they? Okay, so they're not mathematical ideas. So there are,
*  you know, algorithms. And there was a period where the US patent office would allow the patent of
*  software as long as it was embodied. The Europeans are very different. They don't quite accept that
*  they have a different concept. But you know, I don't, I no longer, I mean, I never actually
*  strongly believed in this, but I don't believe in this kind of patent. Facebook basically doesn't
*  believe in this kind of patent. Google files patents because they've been burned with Apple.
*  And so now they do this for defensive purpose. But usually they say, we're not going to see you if
*  you infringe. Facebook has a similar policy. They say, you know, we found a patent on certain
*  things for defensive purpose. We're not going to see you if you infringe unless you sue us.
*  So the industry does not believe in patents. They are there because of, you know, the legal
*  landscape and various things. But I don't really believe in patents for this kind of stuff.
*  So that's a great thing. So I'll tell you a worse story. So what happens was the first
*  patent about convolutional net was about kind of the early version of convolutional net that
*  didn't have separate pooling layers. It had convolutional layers which tried more than one,
*  if you want, right. And then there was a second one on convolutional nets with separate pooling
*  layers, train with backprop. And there were files filed in 89 and 1990 or something like this.
*  At the time, the life of patent was 17 years. So here's what happened over the next few years is
*  that we started developing character recognition technology around convolutional nets.
*  And in 1994, a check reading system was deployed in ATM machines. In 1995, it was for large
*  check reading machines in back offices, etc. And those systems were developed by an engineering
*  group that we were collaborating with at AT&T and they were commercialized by NCR, which at the time
*  was a subsidiary of AT&T. Now AT&T split up in 1996, early 1996. And the lawyers just looked
*  at all the patents and they distributed the patents among the various companies. They gave
*  the convolutional net patent to NCR because they were actually selling products that used it.
*  But nobody at NCR had any idea what a convolutional net was. So between 1996 and 2007,
*  so there's a whole period until 2002 where I didn't actually work on machine learning or
*  convolutional net. I resumed working on this around 2002. And between 2002 and 2007, I was working on
*  them, crossing my finger that nobody at NCR would notice, nobody noticed.
*  Yeah. And I hope that this kind of somewhat, as you said, lawyers aside, relative openness
*  of the community now will continue.
*  It accelerates the entire progress of the industry. And the problems that
*  Facebook and Google and others are facing today is not whether Facebook or Google or
*  Microsoft or IBM or whoever is ahead of the other. It's that we don't have the technology
*  to build the things we want to build. We want to build intelligent virtual assistants that have
*  common sense. We don't have monopoly on good ideas for this. We don't believe we do. Maybe
*  others believe they do, but we don't. If a startup tells you they have the secret to
*  human level intelligence and common sense, don't believe them. They don't. And it's going to take
*  the entire work of the world research community for a while to get to the point where you can
*  go off and each of those companies can start to build things on this. We're not there yet.
*  It's absolutely. And this calls to the gap between the space of ideas and the rigorous
*  testing of those ideas of practical application that you often speak to. You've written advice
*  saying, don't get fooled by people who claim to have a solution to artificial general intelligence,
*  who claim to have an AI system that works just like the human brain or who claim to have figured
*  out how the brain works. Ask them what the error rate they get on MNIST or ImageNet.
*  This is a little dated by the way.
*  I mean, five years. Who's counting? Okay. But I think your opinion is the MNIST and ImageNet,
*  yes, may be dated. There may be new benchmarks, right? But I think that philosophy
*  is when you still somewhat hold that benchmarks and the practical testing,
*  the practical application is where you really get to test the ideas.
*  Well, it may not be completely practical. For example, it could be a toy data set,
*  but it has to be some sort of task that the community as a whole has accepted as some
*  sort of standard benchmark, if you want. It doesn't need to be real. So for example,
*  many years ago here at FAIR, Jason West and Antoine Bourne and a few others proposed the
*  Babi tasks, which were kind of a toy problem to test the ability of machines to reason actually
*  to access working memory and things like this. And it was very useful, even though it wasn't
*  a real task. MNIST is kind of halfway real task. So toy problems can be very useful. It's just that
*  I was really struck by the fact that a lot of people, particularly a lot of people with money
*  to invest, would be fooled by people telling them, oh, we have the algorithm of the cortex and you
*  should give us 50 million. Yes, absolutely. So there's a lot of people who
*  try to take advantage of the hype for business reasons and so on. But let me sort of talk to this
*  idea that the new ideas, the ideas that push the field forward may not yet have a benchmark
*  or it may be very difficult to establish a benchmark. I agree. That's part of the process.
*  Establishing benchmarks is part of the process. So what are your thoughts about?
*  So we have these benchmarks on around stuff we can do with images from classification to
*  captioning to just every kind of information you can pull off from images and the surface level.
*  There's audio data sets, there's some video. What can we start, natural language, what kind of stuff,
*  what kind of benchmarks do you see that start creeping on to more something like intelligence,
*  like reasoning, like maybe you don't like the term, but AGI echoes of that kind of formulation.
*  A lot of people are working on interactive environments in which you can train and test
*  intelligence systems. So there, for example, the classical paradigm of supervised learning is that
*  you have a data set, you partition it into a training set, validation set, test set, and there's
*  a clear protocol. But what if that assumes that the samples are statistically independent? You can
*  exchange them, the order in which you see them shouldn't matter, things like that. But what if
*  the answer you give determines the next sample you see, which is the case, for example, in robotics.
*  Robot does something and then it gets exposed to a new room and depending on where it goes,
*  the room will be different. So that creates the exploration problem.
*  So that creates also a dependency between samples. If you can only move in space, the next sample
*  you're going to see is going to be probably in the same building, most likely. So all the assumptions
*  about the validity of this training set, test set, hypothesis break whenever a machine gets
*  taken action that has an influence in the world and it's what it's going to see. So people are
*  setting up artificial environments where that takes place. The robot runs around a 3D model of
*  a house and can interact with objects and things like this. You do robotics by simulation, you have
*  those opening a gym type thing or a mujoko kind of simulated robots and you have games, things like
*  that. So that's where the field is going really, this kind of thing. So that's where the field is
*  going really, this kind of environment. Now back to the question of AGI. I don't like the term AGI
*  because it implies that human intelligence is general and human intelligence is nothing like
*  general. It's very, very specialized. We think it's general. We'd like to think of ourselves as
*  having general intelligence. We don't. We're very specialized. We're only slightly more general.
*  Why does it feel general? So you're saying that the human intelligence is very, very specialized.
*  Why does it feel general? So you kind of, the term general. I think what's impressive about humans is
*  ability to learn as we were talking about learning, to learn in just so many different domains. It's
*  perhaps not arbitrarily general, but just you can learn in many domains and integrate that knowledge
*  somehow. Okay. That knowledge persists. So let me take a very specific example. Yes. It's not an
*  example. It's more like a quasi mathematical demonstration. So you have about 1 million fibers
*  coming out of one of your eyes. Okay. 2 million total, but let's talk about just one of them.
*  It's 1 million nerve fibers, your optical nerve. Let's imagine that they are binary. So they can
*  be active or inactive, right? So the input to your visual cortex is 1 million bits.
*  Now they're connected to your brain in a particular way and your brain
*  has connections that are kind of a little bit like a convolutional net, they're kind of local,
*  you know, in space and things like this. Now imagine I play a trick on you.
*  It's a pretty nasty trick, I admit. I cut your optical nerve and I put a device that makes a
*  random perturbation of a permutation of all the nerve fibers. So now what comes to your
*  to your brain is a fixed but random permutation of all the pixels.
*  There's no way in hell that your visual cortex, even if I do this to you in infancy,
*  will actually run vision to the same level of quality that you can.
*  Got it. And you're saying there's no way you've learned that.
*  No, because now two pixels that are nearby in the world will end up in very different
*  places in your visual cortex. And your neurons there have no connections with each other because
*  they only connected locally. So this whole, our entire, the hardware is built in many ways to
*  support the locality of the real world. Yeah, yes. That's specialization.
*  Yeah, but it's still pretty damn impressive. So it's not perfect generalization. It's not even
*  close. No, no, it's, it's, it's, it's not that it's not even close. It's not at all.
*  Yes, it's specialized. So how many Boolean functions, so let's imagine you want to
*  train your visual system to, you know, recognize particular patterns of those 1 million bits.
*  Okay. So that's a Boolean function, right? Either the pattern is here or not here. There's a two,
*  two way classification with 1 million binary inputs.
*  How many such Boolean functions are there? Okay. You have, you have two to the 1 million
*  combinations of inputs. For each of those, you have an output bit. And so you have two to the,
*  two to the 1 million Boolean functions of this type. Okay. Which is an unlimited number of
*  which is an unimaginably large number. How many of those functions can actually be computed by
*  your visual cortex? And the answer is a tiny, tiny, tiny, tiny, tiny, tiny sliver, like an
*  enormously tiny sliver. Yeah. Yeah. So we are ridiculously specialized. Okay. But,
*  okay, that's an argument against the word general. I think there's, there's a, I, I, there's,
*  I agree with your intuition, but I'm not sure it's, it seems the brain, the, the brain is
*  impressively capable of adjusting to things. So it's because we can't imagine
*  tasks that are outside of our comprehension, right? So we think, we think we are general
*  because we're general of all the things that we can apprehend. So yeah, but there is a huge world
*  out there of things that we have no idea. We call that heat, by the way, heat, heat. So,
*  at least physicists call that heat or they call it entropy, which is kind of, you have a
*  thing full of gas, right? Close system for gas. Right. Close or not close. It has, you know,
*  pressure, it has a temperature has, you know, and you can write equations, PV equal to nRT,
*  you know, things like that. Right. When you reduce the volume, the temperature goes up,
*  the pressure goes up, you know, things like that. Right. For perfect gas, at least. Those are the
*  things you can know about that system. And it's a tiny, tiny number of bits compared to the complete
*  information of the state of the entire system, because the state of the entire system will give
*  you the position of momentum of every molecule of the gas. And what you don't know about it is
*  the entropy and you interpret it as heat. The energy contained in that thing is what we call
*  heat. Now, it's very possible that in fact, there is some very strong structure in how those
*  molecules are moving. It's just that they are in a way that we are just not wired to perceive.
*  Yeah, we're ignorant to it. And there's in your infinite amount of things we're not wired to
*  perceive. Yeah. You're right. That's a nice way to put it. We're general to all the things we can
*  imagine, which is a very tiny subset of all things that are possible.
*  So it's like chromograph complexity or the chromograph chitin, so one of complexity.
*  Yeah. You know, every bit string or every integer is random, except for all the ones that you can
*  actually write down. Yeah. Okay. So beautifully put, but you know, so we can just call it
*  artificial intelligence. We don't need to have a general. Or human level intelligence.
*  You know, you'll start anytime you touch human, it gets interesting because
*  we attach ourselves to human and it's difficult to define what human intelligence is. Yeah.
*  Nevertheless, my definition is maybe a damn impressive intelligence. Okay. Damn impressive
*  demonstration of intelligence, whatever. And so on that topic, most successes in deep learning
*  have been in supervised learning. What is your view on unsupervised learning? Is there a hope
*  to reduce involvement of human input and still have successful systems that have practical use?
*  Yeah. I mean, there's definitely a hope. It's more than a hope actually. It's
*  this mounting evidence for it. And that's basically all I do. Like the only thing I'm
*  interested in at the moment is I call it self-supervised learning, not unsupervised,
*  because unsupervised learning is a loaded term. People who know something about machine learning,
*  tell you, so you're doing clustering or PCA, which is not the case. And the way public,
*  when you say unsupervised learning, oh my God, machines are going to learn by themselves
*  without supervision. They see this as- Where's the parents?
*  Yeah. So I call it self-supervised learning because in fact, the underlying algorithms
*  that are used are the same algorithms as the supervised learning algorithms,
*  except that what we train them to do is not predict a particular set of variables, like the
*  category of an image, and not to predict a set of variables that have been provided by human
*  labelers. But what you train the machine to do is basically reconstruct a piece of its input that
*  it's being masked out, essentially. You can think of it this way, right? So show a piece of video
*  to a machine and ask it to predict what's going to happen next. And of course, after a while,
*  you can show what happens and the machine will train itself to do better at that task.
*  You can do- All the latest, most successful models in natural language processing use
*  self-supervised learning. So the BERT style systems, for example, you show it a window
*  of a dozen words on a text corpus, you take out 15% of the words, and then you train the machine
*  to predict the words that are missing, that self-supervised learning. It's not predicting
*  the future, it's just predicting things in the middle, but you could predict the future,
*  that's what language models do. So you construct, so in an unsupervised way,
*  you construct a model of language. Do you think- Or video, or the physical world, or whatever,
*  right? How far do you think that can take us? Do you think BERT understands anything?
*  To some level, it has a shallow understanding of text, but it needs to- I mean, to have true
*  human level intelligence, I think you need to ground language in reality. So some people are
*  attempting to do this, right? Having systems that have some visual representation of what is being
*  talked about, which is one reason you need those interactive environments, actually. But this is
*  a huge technical problem that is not solved, and that explains why self-supervised learning
*  works in the context of natural language, but does not work in the context, or at least not well,
*  in the context of image recognition and video, although it's making progress quickly.
*  And the reason, that reason is the fact that it's much easier to represent uncertainty in the
*  prediction in the context of natural language than it is in the context of things like video and
*  images. So for example, if I ask you to predict what words are missing, you know, 15% of the words
*  that are taken out. The possibilities are small. I mean- Small, right? There is 100,000 words in the
*  lexicon, and what the machine spits out is a big probability vector, right? It's a bunch of numbers
*  between 0 and 1 that's onto 1. And we know how to do this with computers. So there, representing
*  uncertainty in the prediction is relatively easy, and that's, in my opinion, why those techniques
*  work for NLP. For images, if you ask, if you block a piece of an image and you ask the system,
*  reconstruct that piece of the image, there are many possible answers. They are all perfectly legit,
*  right? And how do you represent that, the set of possible answers? You can't train a system to make
*  one prediction. You can't train a neural net to say, here it is. That's the image, because there's
*  a whole set of things that are compatible with it. So how do you get the machine to represent not a
*  single output, but a whole set of outputs? And, you know, similarly with video prediction, there's a
*  lot of things that can happen in the future of video. You're looking at me right now. I'm not
*  moving my head very much, but, you know, I might turn my head to the left or to the right. If you
*  don't have a system that can predict this, and you train it with least square to kind of minimize
*  the error with a prediction and what I'm doing, what you get is a blurry image of myself in all
*  possible future positions that I might be in, which is not a good prediction. But so there might be
*  other ways to do the self-supervision, right? For visual scenes. Like what? If I, I mean, if I knew,
*  I wouldn't tell you. I mean, publish it first. I don't know. No, there might be.
*  So, I mean, these are kind of, there might be artificial ways of like self-play in games,
*  the way you can simulate part of the environment. You can- Oh, that doesn't solve the problem. It's
*  just a way of generating data. But because you have more of a control, like maybe you can control,
*  yeah, it's a way to generate data. That's right. And because you can do huge amounts of data
*  generation that doesn't, you're right. Well, it's a creeps up on the problem from the side of data
*  and you don't think that's the right way to creep up on the problem.
*  It doesn't solve this problem of handling uncertainty in the world, right? So if you,
*  if you have a machine, learn a predictive model of the world in a game that is deterministic or
*  quasi-deterministic, it's easy, right? Just, you know, give a few frames of the game to a conv net,
*  put a bunch of layers, and then have the game generates the next few frames.
*  And if the game is deterministic, it works fine. And that includes, you know, feeding
*  the system with the action that your little character is going to take.
*  The problem comes from the fact that the real world and most games are not entirely predictable.
*  And so there you get those blurry predictions and you can't do planning with blurry predictions.
*  Right. So if you have a perfect model of the world, you can in your head, run this model with a
*  hypothesis for a sequence of actions, and you're going to predict the outcome of that sequence of
*  actions. But if your model is imperfect, how can you plan?
*  Yeah, it quickly explodes. What are your thoughts on the extension of this, which topic I'm super
*  excited about, it's connected to something you were talking about in terms of robotics.
*  Active learning. So as opposed to sort of unsupervised, completely unsupervised,
*  self-supervised learning, you ask the system for human help for selecting parts you want annotated
*  next. So if you think about a robot exploring a space, or a baby exploring a space, or a system
*  exploring a data set, every once in a while asking for human input, do you see value in that kind of
*  work? I don't see transformative value. It's going to make things that we can already do
*  more efficient, or they will learn slightly more efficiently, but it's not going to make machines
*  sort of significantly more intelligent. I think, and by the way, there is no opposition, there's no
*  conflict between self-supervised learning, reinforcement learning, unsupervised learning,
*  or imitation learning, or active learning. I see self-supervised learning as a preliminary to all
*  of the above. So the example I use very often is, if you use classical reinforcement learning,
*  deep reinforcement learning, if you want, the best methods today, so-called model-free reinforcement
*  learning to learn to play Atari games, take about 80 hours of training to reach the level that any
*  human can reach in about 15 minutes. They get better than humans, but it takes them a long time.
*  AlphaStar, the, you know, Ariovinias and his team's system to play StarCraft
*  plays, you know, a single map, a single type of player, and can reach
*  better than human level with about the equivalent of 200 years of training, playing against itself.
*  It's 200 years, right? It's not something that no human can, could ever do. I mean, I'm not sure
*  what lesson to take away from that. Okay, now take those algorithms, the best RL algorithms we have
*  today to train a car to drive itself. It would probably have to drive millions of hours. It will
*  have to kill thousands of pedestrians. It will have to run into thousands of trees. It will have to
*  run off cliffs. And it had to run off cliff multiple times before it figures out that it's
*  a bad idea, first of all. And second of all, before it figures out how not to do it. And so,
*  I mean, this type of learning obviously does not reflect the kind of learning that animals and
*  humans do. There is something missing that's really, really important there. And my hypothesis,
*  which I've been advocating for like five years now, is that we have predictive models of the world
*  that include the ability to predict under uncertainty. And what allows us to
*  not run off a cliff when we learn to drive, most of us can learn to drive in about 20 or 30 hours
*  of training without ever crashing, causing any accident. And if we drive next to a cliff,
*  we know that if we turn the wheel to the right, the car is going to run off the cliff and nothing
*  good is going to come out of this. Because we have a pretty good model of intuitive physics that
*  tells us the car is going to fall. We know about gravity. Babies learn this around the age of
*  eight or nine months, that objects don't float, they fall. And we have a pretty good idea of the
*  effect of turning the wheel on the car and we know we need to stay on the road. So there's a
*  lot of things that we bring to the table, which is basically our predictive model of the world.
*  And that model allows us to not do stupid things and to basically stay within the context of
*  things we need to do. We still face unpredictable situations and that's how we learn.
*  But that allows us to learn really, really, really quickly. So that's called model-based
*  reinforcement learning. There's some imitation and supervised learning because we have a driving
*  instructor that tells us occasionally what to do. But most of the learning is learning the model,
*  learning physics that we've done since we were babies. That's where almost all the learning
*  And the physics is somewhat transferable from scene to scene. Stupid things are the same everywhere.
*  Yeah. I mean, if you have experience of the world, you don't need to be
*  from a particularly intelligent species to know that if you spill water from a container,
*  the rest is going to get wet. You might get wet. So cats know this, right?
*  So the main problem we need to solve is how do we learn models of the world?
*  And that's what I'm interested in. That's what self-supervised learning is all about.
*  If you were to try to construct a benchmark for...
*  Let's look at MNIST. I love that data set. But do you think it's useful, interesting,
*  slash possible to perform well on MNIST with just one example of each digit?
*  And how would we solve that problem?
*  The answer is probably yes. The question is what other type of learning are you allowed to do?
*  So if what you're allowed to do is train on some gigantic data set of labeled
*  digit, that's called transfer learning. And we know that works. Okay. We do this at Facebook,
*  like in production, right? We train large convolutional NIST to predict hashtags that
*  people type on Instagram, and we train on billions of images, literally billions.
*  And then we chop off the last layer and fine tune on whatever task we want. That works really well.
*  You can beat the ImageNet record with this. We actually open sourced the whole thing
*  like a few weeks ago. Yeah, that's still pretty cool. But yeah, so what would be impressive?
*  What's useful and impressive? What kind of transfer learning would be useful and impressive?
*  Is it Wikipedia? That kind of thing? No, no. I don't think transfer learning is really where
*  we should focus. We should try to have a kind of scenario for a benchmark where you have
*  unlabeled data and it's a very large number of unlabeled data. It could be video clips.
*  It could be where you do frame prediction. It could be images where you could choose to mask
*  a piece of it. It could be whatever, but they're unlabeled and you're not allowed to label them.
*  So you do some training on this and then you train on a particular supervised task,
*  ImageNet or NIST, and you measure how your test error or validation error decreases as you increase
*  the number of labeled training samples. Okay. And what you'd like to see is that your error
*  decreases much faster than if you train from scratch from random weights. So that to reach
*  the same level of performance and a completely supervised, purely supervised system would reach,
*  you would need way fewer samples. So that's the crucial question because it will answer the
*  question to people interested in medical image analysis. Okay. If I want to get a particular
*  level of error rate for this task, I know I need a million samples. Can I do
*  self-supervised pre-training to reduce this to about a hundred or something?
*  And you think the answer there is self-supervised pre-training?
*  Yeah. Some form. Some form of it.
*  Telling you active learning, but you disagree.
*  No, it's not useless. It's just not going to lead to a quantum leap. It's just going to make things
*  that we already do. So you're way smarter than me. I just disagree with you.
*  But I don't have anything to back that. It's just intuition. So I worked with a lot of large scale
*  datasets and there's something that might be magic in active learning. But okay. At least I
*  said it publicly. At least I'm being an idiot publicly. Okay. It's not being an idiot. It's,
*  you know, working with the data you have. I mean, I mean, certainly people are doing things like,
*  okay, I have 3000 hours of, you know, imitation learning for a car, but most of those are incredibly
*  boring. What I like is select, you know, 10% of them that are kind of the most informative.
*  And with just that, I would probably reach the same. So it's a weak form of,
*  uh, of active learning if you want. Yes, but there might be a, a much stronger version.
*  Yeah, that's right. That's what, and that's an awful question if it exists.
*  The question is how much stronger can you get? Elon Musk is confident. I talked to him recently.
*  He's confident that large scale data and deep learning can solve the autonomous driving problem.
*  What are your thoughts on the limits, possibilities of deep learning in this space?
*  It's obviously part of the solution. I mean, I don't think we'll ever have a self-driving system
*  or it is not in the foreseeable future that does not use deep learning. Let me put it this way.
*  Now, how much of it? So in the history of sort of engineering, particularly sort of,
*  sort of AI like systems, there's generally a first phase where everything is built by hand.
*  Then there is a second phase. And that was the case for autonomous driving, you know,
*  20, 30 years ago. There's a phase where there's a little bit of learning is used, but there's a lot
*  of engineering that's involved in kind of, you know, taking care of corner cases and, and putting
*  limits, et cetera, because the learning system is not perfect. And then as technology progresses,
*  we end up relying more and more on learning. That's the history of character recognition.
*  It's the history of speech recognition, now computer vision, natural language processing.
*  And I think the same is going to happen with autonomous driving that currently the,
*  the methods that are closest to providing some level of autonomy, some, you know,
*  decent level of autonomy where you don't expect a driver to kind of do anything
*  is where you constrain the world. So you only run within, you know, a hundred square kilometers or
*  square miles in Phoenix, but the weather is nice and the roads are wide, which is what Waymo is
*  doing. You completely over-engineer the car with tons of lidars and sophisticated sensors that are
*  too expensive for consumer cars, but they're fine if you just run a fleet. And you engineer
*  the hell out of everything else. You map the entire world. So you have complete 3D model of
*  everything. So the only thing that the perception system has to take care of is moving objects and,
*  and construction and sort of, you know, things that weren't in your map.
*  And you can engineer a good, you know, slam system and all that stuff. Right. So,
*  so that's kind of the current approach that's closest to some level of autonomy. But I think
*  eventually the long-term solution is going to rely more and more on learning and possibly using
*  a combination of self-supervised learning and model-based reinforcement or something like that.
*  But ultimately learning will be at not just at the core, but really the fundamental part of the
*  system. Yeah, it already is, but it will become more and more. What do you think it takes to build
*  a system with human level intelligence? You talked about the AI system in the movie Her
*  being way out of reach, our current reach. This might be outdated as well, but it's still way out
*  of reach. It's still way out of reach. What would it take to build Her? Do you think? So I can tell
*  you the first two obstacles that we have to clear, but I don't know how many obstacles there are
*  after this. So the image I usually use is that there is a bunch of mountains that we have to climb
*  and we can see the first one, but we don't know if there are 50 mountains behind it or not.
*  And this might be a good sort of metaphor for why AI researchers in the past have been overly
*  optimistic about the result of AI. For example, New Orleans Simon wrote the general problem solver
*  and they call it the general problem solver. And of course the first thing you realize is that all
*  the problems you want to solve are exponential and so you can't actually use it for anything useful.
*  But you know. Yeah, so yeah, all you see is the first peak. So what are the first couple of
*  peaks for Her? So the first peak, which is precisely what I'm working on, is self-supervised
*  learning. How do we get machines to learn models of the world by observation, kind of like babies
*  and like young animals? So we've been working with cognitive scientists. So this Emmanuelle Dupoux,
*  who's at fair in Paris, is half time, is also a researcher in the French University. And he
*  has this chart that shows how many months of life baby humans can learn different concepts.
*  And you can measure this in various ways. So things like distinguishing animate objects from
*  inanimate objects. You can tell the difference at age two, three months.
*  Whether an object is going to stay stable is going to fall, you know,
*  about four months you can tell. There are various things like this. And then things like gravity,
*  the fact that objects are not supposed to float in the air but are supposed to fall, you run this
*  around the age of eight or nine months. If you look at a lot of eight-month-old babies, you give
*  them a bunch of toys on their high chair. First thing they do is throw them on the ground and they
*  look at them. It's because they're learning about, actively learning about gravity.
*  Gravity, yeah.
*  Okay. So they're not trying to annoy you, but they need to do the experiment, right?
*  So how do we get machines to learn like babies? Mostly by observation with a little bit of
*  interaction and learning those models of the world, because I think that's really a crucial
*  piece of an intelligent autonomous system. So if you think about the architecture of an intelligent
*  autonomous system, it needs to have a predictive model of the world. So something that says,
*  here is a world at time t, here is a state of the world at time t plus one if I take this action.
*  And it's not a single answer. It can be a...
*  Yeah, it can be distribution.
*  Yeah.
*  Yeah. Well, but we don't know how to represent distributions in third-dimensional spaces. So
*  it's got to be something weaker than that, okay? But with some representation of uncertainty.
*  If you have that, then you can do what optimal control theory is called model predictive control,
*  which means that you can run your model with a hypothesis for a sequence of action and then see
*  the result. Now, what you need, the other thing you need is some sort of objective
*  that you want to optimize. Am I reaching the goal of grabbing this object? Am I minimizing energy?
*  Am I whatever, right? So there is some sort of objective that you have to minimize. And so in
*  your head, if you have this model, you can figure out the sequence of action that will optimize your
*  objective. That objective is something that ultimately is rooted in your basal ganglia,
*  at least in the human brain. That's what it's basal ganglia computes your level of contentment
*  or miscontentment. I don't know if that's a word. Unhappiness, okay?
*  Yeah.
*  Discontentment.
*  Discontentment, maybe.
*  And so your entire behavior is driven towards kind of minimizing that objective, which is
*  maximizing your contentment computed by your basal ganglia. And what you have is an objective
*  function, which is basically a predictor of what your basal ganglia is going to tell you.
*  So you're not going to put your hand on fire because you know it's going to burn and you're
*  going to get hurt. And you're predicting this because of your model of the world and your
*  predictor of this objective, right? So if you have those three components,
*  you have four components. You have the hardwired contentment objective
*  computer, if you want, calculator. And then you have the three components. One is the objective
*  predictor, which basically predicts your level of contentment. One is the model of the world.
*  And there's a third module I didn't mention, which is a module that will
*  figure out the best course of action to optimize an objective given your model.
*  Okay. Yeah. Cool. This policy network or something like that, right?
*  Now you need those three components to act autonomously intelligently. And you can be
*  stupid in three different ways. You can be stupid because your model of the world is wrong.
*  You can be stupid because your objective is not aligned with what you actually want to achieve.
*  Okay. In humans, that would be a psychopath. And then the third way you can be stupid is
*  that you have the right model, you have the right objective, but you're unable to figure out a
*  course of action to optimize your objective given your model. Okay. Some people who are in charge
*  of big countries actually have all three that are wrong. All right. Which countries? I don't know.
*  Okay. So if we think about this, this agent, if you think about the movie, her, you've
*  criticized the art project that is Sophia the robot. And what that project essentially does
*  is uses our natural inclination to anthropomorphize things that look like human and give them more.
*  Do you think that could be used by AI systems like in the movie, her?
*  So do you think that body is needed to create a feeling of intelligence?
*  Well, if Sophia was just an art piece, I would have no problem with it, but it's presented as
*  something else. Let me add that comment real quick. If creators of Sophia could change something
*  about their marketing or behavior in general, what would it be? What's just about everything.
*  I mean, don't you think, here's a tough question. Let me, so I agree with you. So Sophia is not,
*  the general public feels that Sophia can do way more than she actually can. That's right.
*  And the people who created Sophia are not honestly publicly communicating, trying to teach the public.
*  But here's a tough question. Don't you think the same thing is scientists in industry and research
*  are taking advantage of the same misunderstanding in the public when they create AI companies or
*  publish stuff? Some companies, yes. I mean, there is no sense of, there's no desire to delude.
*  There's no desire to kind of over claim with something that's done. You publish a paper on AI
*  that has this result on ImageNet, it's pretty clear. I mean, that's not even interesting anymore.
*  But I don't think there is that, I mean, the reviewers are generally not very forgiving of
*  unsupported claims of this type. But there are certainly quite a few startups that have
*  had a huge amount of hype around this that I find extremely damaging and I've been calling
*  it out when I've seen it. So yeah, but to go back to your original question, like
*  the necessity of embodiment, I think, I don't think embodiment is necessary. I think grounding
*  is necessary. So I don't think we're going to get machines that really understand language without
*  some level of grounding in the real world. And it's not clear to me that language is a high enough
*  bandwidth, but it's not clear to me that language is a high enough bandwidth to be able to understand
*  with medium to communicate how the real world works. I think for this-
*  Can you talk to what grounding means to you?
*  So grounding means that, so there is this classic problem of common sense reasoning,
*  you know, the Winograd schema, right? And so I tell you the trophy doesn't fit in the suitcase
*  because it's too big, or the trophy doesn't fit in the suitcase because it's too small.
*  And the it in the first case refers to the trophy in the second case to the suitcase.
*  And the reason you can figure this out is because you know what the trophy in the suitcase are,
*  one is supposed to fit in the other one, and you know the notion of size and the big object
*  doesn't fit in a small object unless it's a stardust, things like that, right? So you have
*  this knowledge of how the world works, of geometry and things like that. I don't believe you can learn
*  everything about the world by just being told in language how the world works. I think you need some
*  low-level perception of the world, you know, be it visual touch, you know, whatever, but some
*  higher bandwidth perception of the world. So by reading all the world's text,
*  you still may not have enough information. That's right. There's a lot of things that just
*  will never appear in text and that you can't really infer. So I think common sense will emerge from,
*  you know, certainly a lot of language interaction, but also with watching videos or perhaps even
*  interacting in virtual environments and possibly, you know, robot interacting in the real world. But
*  I don't actually believe necessarily that this last one is absolutely necessary,
*  but I think there's a need for some grounding. But the final product doesn't necessarily need
*  to be embodied, you're saying? No. It just needs to have an awareness, a grounding.
*  Right, but it needs to know how the world works to have, you know, to not be frustrated, frustrating
*  to talk to. And you talked about emotions being important. That's a whole other topic.
*  Well, so, you know, I talked about this, the Bizzle Ganglia as the thing that calculates
*  your level of mixed contentment. And then there is this other module that sort of tries to do a
*  prediction of whether you're going to be content or not. That's the source of some emotion. So fear,
*  for example, is an anticipation of bad things that can happen to you. Right? You have this
*  inkling that there is some chance that something really bad is going to happen to you and that
*  creates fear. When you know for sure that something bad is going to happen to you, you kind of give
*  up. Right? It's not there anymore. It's uncertainty that creates fear. So the punchline is, we're not
*  going to have autonomous intelligence without emotions. Whatever the heck emotions are. So you
*  mentioned very practical things of fear, but there's a lot of other mess around it. But there
*  are kind of the results of, you know, drives. Yeah, there's deeper biological stuff going on. And
*  I've talked to a few folks on this. There's fascinating stuff that ultimately connects to our
*  to our brain. If we create an AGI system, sorry, human level intelligence system,
*  and you get to ask her one question, what would that question be?
*  You know, I think the first one we'll create will probably not be that smart. They'd be like a four
*  year old. Okay. So you would have to ask her a question to know she's not that smart.
*  Yeah. Well, what's a good question to ask, you know, to be impressive? What is the cause of wind?
*  Wind. And if she answers, oh, it's because the leaves of the tree are moving and that creates
*  wind. She's onto something. And if she says that's a stupid question, she's really not the sun. No.
*  And then you tell her, actually, you know, here is the real thing. And she says, oh, yeah, that makes
*  sense. So questions that, that reveal the ability to do common sense reasoning about the physical
*  world. Yeah. And you know, some of the little costs on inference, cause inference. Well,
*  it was a huge honor. Congratulations on the Turing Award. Thank you so much for talking today.
*  Thank you. Appreciate it.